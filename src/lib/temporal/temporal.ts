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
