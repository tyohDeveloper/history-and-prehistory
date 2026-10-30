# Standards Exceptions

Policy: `tyohDeveloper/engineering-standards` release 1.0.1.1. Rule C-27: every departure has a rule, reason, owner and review date. Review dates are checked at each architecture review; an expired entry is a finding.

| ID | Rule | Gap | Reason | Owner | Review by |
|---|---|---|---|---|---|
| E-1 | C-11, C-12 function and file limits | `tools/check_standards.py` tolerates a ratcheting debt baseline (18 findings on adoption) instead of zero | Pre-standards picker and calendar modules; the ratchet may fall and may not rise, and the baseline is lowered whenever the count drops | David Hoyt | 2027-04-30 |
| E-2 | C-3 no ambient effects in PURE | No automated identifier scan for `document`, `window`, `Date.now`, `Math.random` in `src/<domain>/**` | Checker measures §3 limits only; purity is reviewed by hand | David Hoyt | 2027-04-30 |
| E-3 | C-20 dead code | No dead-code tool runs | Add knip (or equivalent) to the build gate | David Hoyt | 2027-04-30 |
| E-4 | C-26 license inventory | No generated third-party license inventory; one runtime dependency (`temporal-polyfill`, MIT) plus 114 dataset sources cited in the dataset | Generate the inventory from the shippable dependency tree and fail CI when stale | David Hoyt | 2027-04-30 |
| E-5 | C-31 no secrets | No secret scanner in CI | Add secretlint (or equivalent) to the build gate | David Hoyt | 2027-04-30 |
| E-6 | C-19 CI parity | Runners pinned to `ubuntu-24.04` | Playwright cannot install chromium on Ubuntu 26.04; the pin stays, the image moves when Playwright supports it | David Hoyt | 2027-01-31 |

Inline `EXCEPTION [coding-standards §3.8]` / `§3.9` comments in source remain the per-file mechanism for shape names and tagged re-exports (predecessor §3.7); `tools/check_standards.py` counts untagged cases as findings.

## Closed

| ID | Rule | Closed by |
|---|---|---|
