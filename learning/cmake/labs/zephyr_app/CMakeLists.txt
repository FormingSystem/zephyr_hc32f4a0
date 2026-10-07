# SPDX-License-Identifier: Apache-2.0
cmake_minimum_required(VERSION 3.28.0)
# 由准备章 0.4 节当前终端提供 Zephyr 原生的源码与模块输入。
# 此单模块实验只接受一个 CMSIS 路径；ZEPHYR_MODULES 通用接口可以是列表。
set(ZEPHYR_BASE "$ENV{ZEPHYR_BASE}")
set(ZEPHYR_MODULES "$ENV{ZEPHYR_MODULES}")
if(NOT EXISTS "${ZEPHYR_BASE}/VERSION" OR NOT EXISTS "${ZEPHYR_MODULES}/zephyr/module.yml")
  message(FATAL_ERROR "Follow P00: set ZEPHYR_BASE and ZEPHYR_MODULES")
endif()
# 当前实验模块与应用相邻；它不是另一个 Zephyr 源码根。
list(APPEND EXTRA_ZEPHYR_MODULES "${CMAKE_CURRENT_LIST_DIR}/../zephyr_module")
find_package(Zephyr REQUIRED CONFIG
  PATHS "${ZEPHYR_BASE}/share/zephyr-package/cmake" NO_DEFAULT_PATH)
project(learning_module)
target_sources(app PRIVATE src/main.c)
