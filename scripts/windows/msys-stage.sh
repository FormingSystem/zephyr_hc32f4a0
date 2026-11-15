#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
set -euo pipefail
case "${1:-}" in
    core)
        # exec allows the supervisor to observe pacman's real exit status.
        exec pacman -Syu --noconfirm
        ;;
    packages)
        pacman -Syu --noconfirm
        exec pacman -S --needed --noconfirm \
            base-devel git openssh curl wget unzip zip rsync \
            mingw-w64-ucrt-x86_64-gcc mingw-w64-ucrt-x86_64-gdb \
            mingw-w64-ucrt-x86_64-cmake mingw-w64-ucrt-x86_64-ninja \
            mingw-w64-ucrt-x86_64-dtc mingw-w64-ucrt-x86_64-gperf \
            mingw-w64-ucrt-x86_64-7zip
        ;;
    *) echo 'Unknown bootstrap stage' >&2; exit 2 ;;
esac
