#!/usr/bin/env node
/**
 * Point package-lock.json at the public npm registry.
 *
 * Why this exists
 * ---------------
 * The lockfile is generated inside Replit, whose package firewall rewrites every
 * `resolved` URL to `http://package-firewall.replit.local/npm/...`. That host does
 * not exist anywhere else, so `npm ci` cannot install from this lockfile off
 * Replit.
 *
 * The failure mode was much worse than a clean error. `npm ci` hung on the
 * unreachable host and then died with npm's "Exit handler never called!" internal
 * crash -- **and the CI step still passed**, because that crash path does not set
 * a failing exit code. The build then failed two steps later with
 * `Cannot find type definition file for 'vitest/globals'`, which points at
 * TypeScript configuration and not at the actual cause. Every push to main had
 * been failing this way, and the error told you nothing useful.
 *
 * This runs before `npm ci` in CI, and is idempotent, so a lockfile regenerated
 * in Replit does not break the build again. Replit is unaffected: its firewall
 * re-points URLs transparently when installing there.
 */

import { readFileSync, writeFileSync } from "node:fs";

const PATH = new URL("../package-lock.json", import.meta.url);
const FIREWALL = /https?:\/\/package-firewall\.replit\.local\/npm\//g;
const PUBLIC = "https://registry.npmjs.org/";

const before = readFileSync(PATH, "utf8");
const matches = before.match(FIREWALL);

if (matches === null) {
  console.log("lockfile: already pointing at the public registry, nothing to do.");
  process.exit(0);
}

const after = before.replace(FIREWALL, PUBLIC);
writeFileSync(PATH, after);
console.log(`lockfile: repointed ${matches.length} URLs to ${PUBLIC}`);
