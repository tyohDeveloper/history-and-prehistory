#!/usr/bin/env node
/**
 * Release version-sync script.
 *
 * Two independent version tracks:
 *   --app  <vX.Y.Z.W>   bump package.json "version", tag `<id>-app`
 *   --data <vX.Y.Z.W>   bump "dataset_version" in all five src/data/*.json
 *                       (and DATASET_VERSION in tools/build_data.py), tag `<id>-data`
 *
 * The data tag id and the dataset_version written to the files are separately
 * specifiable: by default the file version is the tag id minus its leading "v",
 * but --data-version <X.Y.Z.W> overrides what is written to the files.
 *
 * Usage:
 *   npm run release -- --app v3.1.1.1
 *   npm run release -- --data v0.5.0.1 --data-version 5.0.0.2
 *   npm run release -- --app v3.1.1.1 --data v0.5.0.1
 *
 * Safety: refuses to run on a dirty working tree, validates version format,
 * and fails if a target tag already exists (locally or on origin).
 * Commits, creates annotated tags, and pushes commit + tags to origin.
 */
import { execFileSync } from "node:child_process";
import { readFileSync, writeFileSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const DATA_FILES = [
  "src/data/entities.json",
  "src/data/calendars.json",
  "src/data/reference-frames.json",
  "src/data/sources.json",
  "src/data/themes.json",
];
const BUILD_DATA_PY = "tools/build_data.py";

function fail(msg) {
  console.error(`release: ERROR: ${msg}`);
  process.exit(1);
}

function git(...args) {
  return execFileSync("git", args, { cwd: ROOT, encoding: "utf8" }).trim();
}

// ---- argument parsing -------------------------------------------------------
function parseArgs(argv) {
  const opts = { app: null, data: null, dataVersion: null, dryRun: false, noVerify: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--app") opts.app = argv[++i];
    else if (a === "--data") opts.data = argv[++i];
    else if (a === "--data-version") opts.dataVersion = argv[++i];
    else if (a === "--dry-run") opts.dryRun = true;
    else if (a === "--no-verify") opts.noVerify = true;
    else if (a === "--help" || a === "-h") {
      console.log(
        "Usage: npm run release -- [--app vX.Y.Z.W] [--data vX.Y.Z.W [--data-version X.Y.Z.W]] [--dry-run] [--no-verify]"
      );
      process.exit(0);
    } else fail(`unknown argument: ${a}`);
  }
  return opts;
}

const TAG_ID_RE = /^v\d+(\.\d+){1,3}$/; // e.g. v3.1.1.1, v0.5.0.1
const FILE_VERSION_RE = /^\d+(\.\d+){1,3}$/; // e.g. 3.1.1.1, 5.0.0.2

const opts = parseArgs(process.argv.slice(2));
if (!opts.app && !opts.data) {
  fail("nothing to do — pass --app <vX.Y.Z.W> and/or --data <vX.Y.Z.W> (see --help)");
}
if (opts.dataVersion && !opts.data) fail("--data-version requires --data");
if (opts.app && !TAG_ID_RE.test(opts.app))
  fail(`--app must look like v3.1.1.1 (got "${opts.app}")`);
if (opts.data && !TAG_ID_RE.test(opts.data))
  fail(`--data must look like v0.5.0.1 (got "${opts.data}")`);
if (opts.dataVersion && !FILE_VERSION_RE.test(opts.dataVersion))
  fail(`--data-version must look like 5.0.0.2 (got "${opts.dataVersion}")`);

const appTag = opts.app ? `${opts.app}-app` : null;
const dataTag = opts.data ? `${opts.data}-data` : null;
const appFileVersion = opts.app ? opts.app.slice(1) : null; // package.json version
const dataFileVersion = opts.data ? (opts.dataVersion ?? opts.data.slice(1)) : null;

// ---- safety checks ----------------------------------------------------------
const dirty = git("status", "--porcelain");
if (dirty) fail(`working tree is dirty — commit or stash first:\n${dirty}`);

for (const tag of [appTag, dataTag].filter(Boolean)) {
  if (git("tag", "-l", tag)) fail(`tag ${tag} already exists locally`);
  try {
    const remote = git("ls-remote", "--tags", "origin", `refs/tags/${tag}`);
    if (remote) fail(`tag ${tag} already exists on origin`);
  } catch (e) {
    console.warn(`release: warning: could not check origin for tag ${tag} (${e.message.split("\n")[0]}); continuing with local check only`);
  }
}

// ---- file edits (surgical, formatting-preserving) ---------------------------
function replaceOnce(path, pattern, replacement, label) {
  const abs = resolve(ROOT, path);
  const src = readFileSync(abs, "utf8");
  const matches = src.match(new RegExp(pattern.source, pattern.flags + "g")) ?? [];
  if (matches.length !== 1)
    fail(`expected exactly one ${label} in ${path}, found ${matches.length}`);
  writeFileSync(abs, src.replace(pattern, replacement));
  console.log(`release: ${path}: ${label} -> ${replacement.match(/"([^"]+)"/)?.[1] ?? replacement}`);
}

// Keep package-lock.json's top-level and root-package ("") versions in sync
// with package.json, surgically and with exact-match validation.
function updateLockfile(newVersion) {
  const path = "package-lock.json";
  const abs = resolve(ROOT, path);
  const src = readFileSync(abs, "utf8");
  const lock = JSON.parse(src);
  const prev = lock.version;
  if (!prev || lock.packages?.[""]?.version !== prev)
    fail(`${path}: top-level version and root-package version disagree — refresh the lockfile first`);
  const pattern = new RegExp(`^(\\s*)"version": "${prev.replaceAll(".", "\\.")}",$`, "gm");
  const matches = src.match(pattern) ?? [];
  if (matches.length !== 2)
    fail(`${path}: expected exactly 2 root "version" entries to update, found ${matches.length}`);
  writeFileSync(abs, src.replace(pattern, `$1"version": "${newVersion}",`));
  console.log(`release: ${path}: version -> ${newVersion} (2 entries)`);
  touched.push(path);
}

const touched = [];
if (opts.dryRun) {
  console.log("release: dry run — no files changed, no git operations.");
  if (appTag) console.log(`  would set package.json version=${appFileVersion}, tag ${appTag}`);
  if (dataTag)
    console.log(
      `  would set dataset_version=${dataFileVersion} in ${DATA_FILES.length} data files + ${BUILD_DATA_PY}, tag ${dataTag}`
    );
  process.exit(0);
}

if (opts.app) {
  replaceOnce(
    "package.json",
    /^  "version": "[^"]+",$/m,
    `  "version": "${appFileVersion}",`,
    "version field"
  );
  touched.push("package.json");
  updateLockfile(appFileVersion);
}

if (opts.data) {
  // Fail fast if the generator constant and the committed JSON already disagree:
  // stamping a new version on top of an inconsistent baseline would tag data
  // that was never generated from the constant it claims.
  const generatorVersion = readFileSync(resolve(ROOT, BUILD_DATA_PY), "utf8")
    .match(/^DATASET_VERSION = "([^"]+)"$/m)?.[1];
  for (const f of DATA_FILES) {
    const v = JSON.parse(readFileSync(resolve(ROOT, f), "utf8")).dataset_version;
    if (v !== generatorVersion)
      fail(
        `pre-existing dataset version mismatch: ${BUILD_DATA_PY} has DATASET_VERSION="${generatorVersion}" ` +
          `but ${f} has dataset_version="${v}". Fix the baseline (regenerate via tools/build_data.py) before releasing.`
      );
  }
  for (const f of DATA_FILES) {
    replaceOnce(
      f,
      /^  "dataset_version": "[^"]+",$/m,
      `  "dataset_version": "${dataFileVersion}",`,
      "dataset_version field"
    );
    touched.push(f);
  }
  // Keep the generator in sync so tools/check_regenerated.py does not drift.
  replaceOnce(
    BUILD_DATA_PY,
    /^DATASET_VERSION = "[^"]+"$/m,
    `DATASET_VERSION = "${dataFileVersion}"`,
    "DATASET_VERSION constant"
  );
  touched.push(BUILD_DATA_PY);
}

// ---- validation before commit -----------------------------------------------
// For data releases, prove the committed JSON is what the generator produces
// (schema validation + regeneration drift check) before anything is tagged.
if (opts.data && !opts.noVerify) {
  try {
    execFileSync("npm", ["run", "validate:data"], { cwd: ROOT, stdio: "inherit" });
  } catch {
    git("checkout", "--", ...touched);
    fail("`npm run validate:data` failed — changes reverted, nothing committed or tagged. (Use --no-verify only if you know why validation cannot run.)");
  }
}

// ---- commit, tag, push ------------------------------------------------------
const parts = [];
if (opts.app) parts.push(`app ${appFileVersion}`);
if (opts.data) parts.push(`data ${dataFileVersion} (${opts.data})`);
const commitMsg = `release: ${parts.join(", ")}`;

git("add", ...touched);
git("commit", "-m", commitMsg);
console.log(`release: committed "${commitMsg}"`);

if (appTag) {
  git("tag", "-a", appTag, "-m", `App release ${opts.app}`);
  console.log(`release: created annotated tag ${appTag}`);
}
if (dataTag) {
  git("tag", "-a", dataTag, "-m", `Data release ${opts.data} (dataset_version ${dataFileVersion})`);
  console.log(`release: created annotated tag ${dataTag}`);
}

const branch = git("rev-parse", "--abbrev-ref", "HEAD");
try {
  git("push", "origin", branch, ...[appTag, dataTag].filter(Boolean));
} catch (e) {
  fail(
    `push failed — commit and tags exist locally; push manually with:\n` +
      `  git push origin ${branch} ${[appTag, dataTag].filter(Boolean).join(" ")}\n${e.message}`
  );
}
console.log(`release: pushed ${branch} + tags to origin. Done.`);
