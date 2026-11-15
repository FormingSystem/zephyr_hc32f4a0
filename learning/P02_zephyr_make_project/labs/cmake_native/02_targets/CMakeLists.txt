# SPDX-License-Identifier: Apache-2.0
# 文件内容：本章练习 source/CMakeLists.txt，不是终端命令。
cmake_minimum_required(VERSION 3.28)
project(native_demo LANGUAGES C)

add_library(arithmetic STATIC)
target_sources(arithmetic PRIVATE src/add.c)
target_include_directories(arithmetic PUBLIC
  "${CMAKE_CURRENT_SOURCE_DIR}/include")

add_executable(my_app)
target_sources(my_app PRIVATE main.c)
target_link_libraries(my_app PRIVATE arithmetic)
