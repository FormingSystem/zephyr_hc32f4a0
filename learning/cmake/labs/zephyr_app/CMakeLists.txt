# SPDX-License-Identifier: Apache-2.0
cmake_minimum_required(VERSION 3.28.0) # 此应用要求的 CMake 最低版本。
# 从当前文件位置寻找仓库，不依赖终端的当前目录。
get_filename_component(lesson_root "${CMAKE_CURRENT_LIST_DIR}/../../../.." ABSOLUTE) # 计算绝对路径。
set(ZEPHYR_BASE "${lesson_root}") # 当前使用的 Zephyr 源码根。
set(Zephyr_DIR "${lesson_root}/share/zephyr-package/cmake") # find_package 的入口位置。
# 显式选择仓库内已纳管的基础模块。
set(ZEPHYR_MODULES
  "${lesson_root}/modules/hal/cmsis_6"
  "${lesson_root}/modules/hal/xhsc"
)
# 必须在 find_package 之前交给 Zephyr，否则错过本轮模块发现。
list(APPEND EXTRA_ZEPHYR_MODULES "${CMAKE_CURRENT_LIST_DIR}/../zephyr_module") # APPEND 追加列表项。
find_package(Zephyr REQUIRED) # REQUIRED 表示找不到就报错停止。
project(learning_module)
target_sources(app PRIVATE src/main.c)
