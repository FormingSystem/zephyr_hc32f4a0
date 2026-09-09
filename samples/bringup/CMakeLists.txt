# SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.28.0)

get_filename_component(hc32_project_root "${CMAKE_CURRENT_LIST_DIR}/../.." ABSOLUTE)
set(ZEPHYR_BASE "${hc32_project_root}")
set(Zephyr_DIR "${hc32_project_root}/share/zephyr-package/cmake")
set(ZEPHYR_MODULES
  "${hc32_project_root}/modules/hal/cmsis_6"
  "${hc32_project_root}/modules/hal/xhsc"
)

find_package(Zephyr REQUIRED)
project(hc32f4a0_bringup)

target_sources(app PRIVATE
  src/main.c
)
