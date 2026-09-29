# SPDX-License-Identifier: Apache-2.0
cmake_minimum_required(VERSION 3.20) # 要求 CMake 至少为此版本。
project(source_and_module C) # source_and_module 是项目名，C 是所用语言。
# 导出每个 C 文件的真实编译参数，稍后据此检查是否参与构建。
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
# 教学用开关；默认 OFF，即不故意遗漏校准实现。
option(LESSON_OMIT_CALIBRATION "Deliberately omit a required source to observe a link error" OFF)

# 先读取库的规则，再为应用创建自己的目标。
add_subdirectory(modules/scale)
add_executable(sensor_demo src/main.c)
target_include_directories(sensor_demo PRIVATE include) # 只给此目标添加搜索路径。
if(NOT LESSON_OMIT_CALIBRATION) # NOT 取反：开关 OFF 时才登记实现。
  target_sources(sensor_demo PRIVATE src/calibrate.c)
endif()
target_link_libraries(sensor_demo PRIVATE scale)

# 测试运行已经构建的程序，用输出规则判断这一项是否通过。
enable_testing()
add_test(NAME sensor_output COMMAND sensor_demo) # NAME 后是测试名，COMMAND 后是目标。
set_tests_properties(sensor_output PROPERTIES PASS_REGULAR_EXPRESSION "value=43") # 设置输出匹配属性。
