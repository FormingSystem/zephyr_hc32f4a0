# SPDX-License-Identifier: Apache-2.0
if(CONFIG_LEARNING_SCALE)
  zephyr_library()
  zephyr_library_sources(src/scale.c)
  zephyr_include_directories(include)
endif()
