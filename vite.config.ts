import { defineConfig } from "vite";
import { viteSingleFile } from "vite-plugin-singlefile";
import { readFileSync } from "node:fs";

const pkg = JSON.parse(readFileSync(new URL("./package.json", import.meta.url), "utf8")) as {
  version: string;
};

// Production builds emit exactly one self-contained index.html.
// Nothing is fetched at runtime: the dataset is inlined at build time
// via `import ... from "./data/*.json"`. See docs/ARCHITECTURE.md §2.
export default defineConfig({
  plugins: [...(process.env.NODE_ENV === "production" ? [viteSingleFile()] : [])],
  define: { __APP_VERSION__: JSON.stringify(pkg.version) },
  build: {
    outDir: "dist/public",
    emptyOutDir: true,
    // Vite's modulePreload polyfill injects a fetch() call. A single-file
    // artifact has nothing to preload, and the CSP forbids fetch outright.
    modulePreload: false,
    assetsInlineLimit: 100_000_000,
    cssCodeSplit: false,
    target: "es2022",
  },
  server: { host: "0.0.0.0", port: 5000, allowedHosts: true },
  preview: { host: "0.0.0.0", port: 5000, allowedHosts: true },
});
