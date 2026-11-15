# SPDX-License-Identifier: Apache-2.0
if(CONFIG_LEARNING_SCALE)
  # 建立模块库，并把实现和头文件路径接入 Zephyr 构建。
  zephyr_library()
  zephyr_library_sources(src/scale.c)
  zephyr_include_directories(include)
endif()
