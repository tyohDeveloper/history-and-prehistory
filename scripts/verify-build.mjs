#!/usr/bin/env node
/**
 * verify-build.mjs — gate the single-file production artifact.
 *
 * Checks, in order:
 *   1. Artifact exists, is non-empty, is a single self-contained file
 *   2. Inlined <script> present (singlefile plugin ran)
 *   3. No license/block comments left in inlined JS
 *   4. No external URL references that would cause a network load
 *   5. No fetch/XHR/sendBeacon/WebSocket/ServiceWorker/WebRTC in the bundle
 *   6. CSP meta tag present with connect-src 'none'
 *   7. No persistent-storage API use (localStorage/IndexedDB/cookie)
 *   8. HTML shell parses as strict XML (script/style bodies masked)
 *   9. No literal "]]>" inside inlined script/style bodies
 *  10. Test-ID manifest coverage
 *  11. Size within absolute ceiling and within gzip baseline + headroom
 *
 * Checks 5-7 are the machine-enforceable half of the standalone-HTML5
 * privacy posture. They are why a reviewer can trust the artifact by
 * inspection rather than by reading every line.
 */
import fs from "node:fs";
import path from "node:path";
import zlib from "node:zlib";
import { fileURLToPath } from "node:url";
import sax from "sax";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const OUTPUT_DIR = path.join(ROOT, "dist", "public");
const OUTPUT_FILE = path.join(OUTPUT_DIR, "index.html");
const BASELINE_FILE = path.join(ROOT, "scripts", "build-baseline.json");
const MANIFEST_FILE = path.join(ROOT, "scripts", "testid-manifest.json");

// Raised from 3 MB when the Languages branch took the corpus to 7,793 entities. The number that
// governs delivery is the gzip size, checked separately against a recorded baseline, and that is
// 667 kB; this ceiling is about parse time and memory once the file is open. 5 MB of mostly-text
// HTML parses in well under a second on any browser this app targets, and the file still opens
// from disk with no network at all, which is the property that matters.
const MAX_SIZE_BYTES = 5 * 1024 * 1024;
const GZIP_HEADROOM_RATIO = 1.05;

let failed = false;
const error = (m) => {
  console.error(`BUILD ERROR: ${m}`);
  failed = true;
};

if (!fs.existsSync(OUTPUT_FILE)) {
  error(`Output file not found: ${OUTPUT_FILE}`);
  process.exit(1);
}

const content = fs.readFileSync(OUTPUT_FILE, "utf8");
const sizeBytes = Buffer.byteLength(content, "utf8");
const gzipSize = zlib.gzipSync(content).length;

console.log(`Build output: ${OUTPUT_FILE}`);
console.log(`  Raw size:  ${(sizeBytes / 1024).toFixed(1)} kB`);
console.log(`  Gzip size: ${(gzipSize / 1024).toFixed(1)} kB`);

if (sizeBytes === 0) error("Output file is empty.");
if (sizeBytes > MAX_SIZE_BYTES) {
  error(`Artifact is ${(sizeBytes / 1024).toFixed(1)} kB, over the ${MAX_SIZE_BYTES / 1024} kB ceiling.`);
}

const siblings = fs
  .readdirSync(OUTPUT_DIR, { withFileTypes: true })
  .filter((e) => e.isFile() && e.name !== "index.html")
  .map((e) => e.name);
if (siblings.length > 0) {
  error(`dist/public contains sibling files, artifact is not single-file: ${siblings.join(", ")}`);
}

const scripts = content.match(/<script[^>]*>([\s\S]*?)<\/script>/g) ?? [];
if (scripts.length === 0) {
  error("No inlined <script> found — vite-plugin-singlefile may not have run.");
}
const scriptBody = scripts.join("");

const licenseComments = scriptBody.match(/\/\*![\s\S]*?\*\//g) ?? [];
if (licenseComments.length > 0) {
  error(`${licenseComments.length} license/block comment(s) left in inlined JS — not fully minified.`);
}

// (4) External resource references.
const externalPatterns = [
  /\bsrc\s*=\s*["'](?:https?:)?\/\/[^"']+["']/gi,
  /<link[^>]+rel\s*=\s*["'](?:stylesheet|preload|prefetch|modulepreload)["'][^>]+href\s*=\s*["'](?:https?:)?\/\/[^"']+["']/gi,
  /url\(\s*["']?(?:https?:)?\/\/[^"')]+["']?\s*\)/gi,
  /@import\s+(?:url\()?["'](?:https?:)?\/\/[^"']+["']/gi,
];
const externalHits = externalPatterns.flatMap((rx) => content.match(rx) ?? []);
if (externalHits.length > 0) {
  error(`${externalHits.length} external-URL resource reference(s):\n  - ${externalHits.slice(0, 3).join("\n  - ")}`);
}

// (5) Network APIs. Matched against the inlined script bodies only.
const FORBIDDEN_APIS = [
  [/\bfetch\s*\(/, "fetch()"],
  [/\bXMLHttpRequest\b/, "XMLHttpRequest"],
  [/\bsendBeacon\b/, "navigator.sendBeacon"],
  [/\bnew\s+WebSocket\b/, "WebSocket"],
  [/\bserviceWorker\b/, "ServiceWorker"],
  [/\bRTCPeerConnection\b/, "WebRTC"],
  [/\bEventSource\b/, "EventSource"],
];
for (const [rx, label] of FORBIDDEN_APIS) {
  if (rx.test(scriptBody)) error(`Forbidden network API in bundle: ${label}. See docs/ARCHITECTURE.md §2.`);
}

// (6) CSP present and closing the network off.
const cspMatch = content.match(/<meta[^>]+http-equiv\s*=\s*["']Content-Security-Policy["'][^>]*>/i);
if (!cspMatch) error("No Content-Security-Policy <meta> tag in the artifact.");
else if (!/connect-src\s+'none'/i.test(cspMatch[0])) {
  error("CSP present but does not set connect-src 'none'.");
}

// (7) Persistent storage.
const FORBIDDEN_STORAGE = [
  [/\blocalStorage\b/, "localStorage"],
  [/\bsessionStorage\b/, "sessionStorage"],
  [/\bindexedDB\b/, "IndexedDB"],
  [/\bdocument\.cookie\b/, "document.cookie"],
];
for (const [rx, label] of FORBIDDEN_STORAGE) {
  if (rx.test(scriptBody)) error(`Forbidden persistent-storage API in bundle: ${label}.`);
}

// (8) Strict XML parse of the shell.
const shell = content
  .replace(/(<script\b[^>]*>)([\s\S]*?)(<\/script>)/gi, (_m, o, _b, c) => `${o}${c}`)
  .replace(/(<style\b[^>]*>)([\s\S]*?)(<\/style>)/gi, (_m, o, _b, c) => `${o}${c}`);
let xmlErr = null;
try {
  const parser = sax.parser(true, { xmlns: false });
  parser.onerror = (e) => {
    xmlErr = e;
  };
  parser.write(`<?xml version="1.0" encoding="UTF-8"?>\n${shell}`).close();
} catch (e) {
  xmlErr = e;
}
if (xmlErr) error(`Artifact shell fails strict XML parse: ${xmlErr.message ?? xmlErr}`);

// (9) CDATA safety.
const bodies = [
  ...[...content.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/gi)].map((m) => m[1]),
  ...[...content.matchAll(/<style\b[^>]*>([\s\S]*?)<\/style>/gi)].map((m) => m[1]),
];
const cdataClosures = bodies.reduce((n, b) => n + (b.match(/\]\]>/g)?.length ?? 0), 0);
if (cdataClosures > 0) {
  error(`${cdataClosures} literal ']]>' in inlined script/style — unsafe if CDATA-wrapped.`);
}

// (10) Test-ID coverage.
const hasTestId = (id) =>
  content.includes(`data-testid="${id}"`) ||
  content.includes(`data-testid='${id}'`) ||
  content.includes(`"data-testid":"${id}"`) ||
  content.includes(`"${id}"`);
if (fs.existsSync(MANIFEST_FILE)) {
  const required = JSON.parse(fs.readFileSync(MANIFEST_FILE, "utf8")).required ?? [];
  const missing = required.filter((id) => !hasTestId(id));
  if (missing.length > 0) {
    error(`Test-ID manifest coverage failed, ${missing.length} missing:\n  - ${missing.join("\n  - ")}`);
  } else {
    console.log(`  Test IDs: all ${required.length} required ids present.`);
  }
} else {
  console.warn("  Warning: scripts/testid-manifest.json missing — skipping coverage check.");
}

// (11) Gzip regression against the recorded baseline.
if (fs.existsSync(BASELINE_FILE)) {
  const baseline = JSON.parse(fs.readFileSync(BASELINE_FILE, "utf8"));
  const ceiling = Math.ceil(baseline.gzipBytes * GZIP_HEADROOM_RATIO);
  console.log(
    `  Baseline:  ${(baseline.gzipBytes / 1024).toFixed(1)} kB gzip (recorded ${baseline.recordedAt})`,
  );
  if (gzipSize > ceiling) {
    error(
      `Gzip ${(gzipSize / 1024).toFixed(1)} kB exceeds baseline ceiling ${(ceiling / 1024).toFixed(1)} kB — bundle regressed.`,
    );
  }
} else {
  console.warn("  Warning: no scripts/build-baseline.json — skipping size regression check.");
}

if (failed) {
  console.error("\nBuild verification failed.");
  process.exit(1);
}
console.log("Build verification passed: single-file, offline-safe, XML-well-formed, within budget.");
