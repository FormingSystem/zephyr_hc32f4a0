# SPDX-License-Identifier: Apache-2.0
if(CONFIG_APP_GREETING)
  zephyr_library()
  zephyr_library_sources(src/greeting.c)
  zephyr_include_directories(include)
endif()
