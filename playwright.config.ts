import { defineConfig } from "@playwright/test";
import path from "node:path";
import { fileURLToPath } from "node:url";

// E2E runs against the BUILT single-file artifact over file://, not the
// dev server. This is what catches inlining bugs, CSP violations, and
// offline breakage that `vite dev` hides. See docs/ARCHITECTURE.md §5.
const ROOT = path.dirname(fileURLToPath(import.meta.url));
// baseURL points at the DIRECTORY, so tests can navigate to
// "index.html#cal=..." — a fragment alone does not resolve against a
// file:// base, and a relative path against a file baseURL ending in a
// filename does not either.
const ARTIFACT_DIR = path.resolve(ROOT, "dist/public");

export default defineConfig({
  testDir: "./tests/e2e",
  testMatch: /.*\.e2e\.ts/,
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  reporter: process.env.CI ? "list" : "html",
  use: {
    baseURL: `file://${ARTIFACT_DIR}/`,
    trace: "on-first-retry",
  },
  projects: [{ name: "chromium", use: { browserName: "chromium" } }],
});
