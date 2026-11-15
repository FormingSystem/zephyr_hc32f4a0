# SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.28.0)

get_filename_component(hc32_project_root "${CMAKE_CURRENT_LIST_DIR}/../.." ABSOLUTE)
# Keep the selected source visible to the same provenance audit for west and
# project.py builds; do not inherit another checkout from a user cache.
set(ZEPHYR_BASE "${hc32_project_root}" CACHE PATH "Project Zephyr source" FORCE)
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
