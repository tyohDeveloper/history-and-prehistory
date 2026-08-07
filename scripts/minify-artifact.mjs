#!/usr/bin/env node
/**
 * minify-artifact.mjs — final HTML-shell minimization pass.
 *
 * Runs after `vite build` and before `verify:build`. Never runs in dev.
 * Vite/esbuild already minified the inlined JS, so `minifyJS: false` keeps
 * that untouched. XHTML-conformant markup is preserved via keepClosingSlash
 * and caseSensitive; boolean attributes are then expanded to long form so
 * the artifact stays strict-XML parseable.
 */
import fs from "node:fs";
import path from "node:path";
import zlib from "node:zlib";
import { fileURLToPath } from "node:url";
import { minify } from "html-minifier-terser";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const ARTIFACT = path.join(ROOT, "dist", "public", "index.html");

if (!fs.existsSync(ARTIFACT)) {
  console.error(`MINIFY ERROR: artifact not found at ${ARTIFACT}. Run \`vite build\` first.`);
  process.exit(1);
}

const before = fs.readFileSync(ARTIFACT, "utf8");
const beforeGzip = zlib.gzipSync(before).length;

let after = await minify(before, {
  collapseWhitespace: true,
  removeComments: true,
  minifyCSS: true,
  minifyJS: false,
  keepClosingSlash: true,
  caseSensitive: true,
  useShortDoctype: false,
  decodeEntities: false,
  html5: true,
  removeAttributeQuotes: false,
  removeEmptyAttributes: false,
  collapseBooleanAttributes: false,
});

const BOOLEAN_ATTRS = [
  "allowfullscreen", "async", "autofocus", "autoplay", "checked", "controls",
  "crossorigin", "default", "defer", "disabled", "formnovalidate", "hidden",
  "ismap", "itemscope", "loop", "multiple", "muted", "nomodule", "novalidate",
  "open", "playsinline", "readonly", "required", "reversed", "selected",
];
for (const attr of BOOLEAN_ATTRS) {
  after = after.replace(
    new RegExp(`(<[a-zA-Z][^>]*?)\\s${attr}(?=[\\s/>])(?![=-])`, "g"),
    `$1 ${attr}="${attr}"`,
  );
}

fs.writeFileSync(ARTIFACT, after, "utf8");
const afterGzip = zlib.gzipSync(after).length;
console.log(
  `Minified artifact: ${(beforeGzip / 1024).toFixed(1)} kB \u2192 ${(afterGzip / 1024).toFixed(1)} kB gzip`,
);
