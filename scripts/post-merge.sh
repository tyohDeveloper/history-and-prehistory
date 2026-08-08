#!/bin/bash
set -e

# Post-merge setup: install dependencies after any task merge.
# Idempotent and non-interactive.

npm install
