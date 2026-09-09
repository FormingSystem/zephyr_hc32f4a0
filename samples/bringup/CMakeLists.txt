# SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.28.0)

get_filename_component(hc32f4a0_module_root "${CMAKE_CURRENT_LIST_DIR}/../.." ABSOLUTE)
list(APPEND EXTRA_ZEPHYR_MODULES "${hc32f4a0_module_root}")
list(REMOVE_DUPLICATES EXTRA_ZEPHYR_MODULES)

find_package(Zephyr REQUIRED HINTS "$ENV{ZEPHYR_BASE}")
project(hc32f4a0_bringup)

target_sources(app PRIVATE
  src/main.c
)
