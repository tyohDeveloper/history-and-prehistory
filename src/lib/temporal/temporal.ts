// EXCEPTION [coding-standards §3.9] single-symbol runtime-dependency
// source-selection shim per §1.7. Owner: tyohDeveloper. Approved 2026-08-08.
// Expiry: contingent on external support, not a date - removable once native
// Temporal is stable across the browser matrix for a full major-version cycle,
// at which point this file goes away rather than being renewed.
//
// (The standards text tags this carve-out "§3.8"; the rule being excepted is
// §3.9, so that looks like a transcription slip in the derived copy. Flagged
// for the wiki rather than silently corrected here.)
//
// Source-selection shim for the Temporal API.
//
// Every consumer imports from this module rather than from
// `temporal-polyfill` or `globalThis.Temporal` directly. That indirection is
// the point: swapping the polyfill for native Temporal later is a one-line
// change here instead of an edit to every calling file. Ported from the
// OmniUnit implementation so both apps make the same choice the same way.
//
// Import path is `temporal-polyfill/full`, not the default entry. The default
// ships only `gregory` and `iso8601`; `/full` adds the exotic calendars
// (Hebrew, Islamic variants, Coptic, Ethiopic, Persian, Chinese, Dangi,
// Japanese, ROC, Buddhist, Indian) that a history app is entirely about.
//
// Remove when native Temporal is stable across the browser matrix for a full
// major-version cycle. Migration = point the import at globalThis.Temporal.

import { Temporal } from "temporal-polyfill/full";

export { Temporal };
