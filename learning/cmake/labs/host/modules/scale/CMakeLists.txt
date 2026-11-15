# SPDX-License-Identifier: Apache-2.0
add_library(scale STATIC src/scale.c) # STATIC 选择静态库，链接时取用其中的实现。
# 库自身和链接它的调用者都需要能找到 scale.h。
target_include_directories(scale PUBLIC include)
