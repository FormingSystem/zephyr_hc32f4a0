# SPDX-License-Identifier: Apache-2.0
set pagination off
# 在校准函数的入口设置断点，run 之后才开始运行。
break calibrate
run
# 赋值前读输入；next 执行当前源码行，再读局部结果。
print value
next
print corrected
continue
