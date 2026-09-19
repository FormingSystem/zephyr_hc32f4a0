# SPDX-License-Identifier: Apache-2.0
cmake_minimum_required(VERSION 3.28.0)
get_filename_component(lesson_root "${CMAKE_CURRENT_LIST_DIR}/../../../.." ABSOLUTE)
set(ZEPHYR_BASE "${lesson_root}")
set(Zephyr_DIR "${lesson_root}/share/zephyr-package/cmake")
set(ZEPHYR_MODULES
  "${lesson_root}/modules/hal/cmsis_6"
  "${lesson_root}/modules/hal/xhsc"
)
list(APPEND EXTRA_ZEPHYR_MODULES "${CMAKE_CURRENT_LIST_DIR}/../zephyr_module")
find_package(Zephyr REQUIRED)
project(learning_module)
target_sources(app PRIVATE src/main.c)
