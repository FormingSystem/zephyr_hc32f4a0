#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
set -euo pipefail
# The login profile prepends UCRT64. Put the selected Windows Python first again.
export PATH="$(cygpath -p -u "$HC32_WINDOWS_PATH")"
unset HC32_WINDOWS_PATH
printf '\nHC32 / Zephyr UCRT64: %s\n' "$PWD"
exec bash --noprofile --norc -i
