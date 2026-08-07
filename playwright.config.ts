import { defineConfig } from "@playwright/test";
import path from "node:path";
import { fileURLToPath } from "node:url";

// E2E runs against the BUILT single-file artifact over file://, not the
// dev server. This is what catches inlining bugs, CSP violations, and
// offline breakage that `vite dev` hides. See docs/ARCHITECTURE.md §5.
const ROOT = path.dirname(fileURLToPath(import.meta.url));
const ARTIFACT = path.resolve(ROOT, "dist/public/index.html");

export default defineConfig({
  testDir: "./tests/e2e",
  testMatch: /.*\.e2e\.ts/,
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  reporter: process.env.CI ? "list" : "html",
  use: {
    baseURL: `file://${ARTIFACT}`,
    trace: "on-first-retry",
  },
  projects: [{ name: "chromium", use: { browserName: "chromium" } }],
});
