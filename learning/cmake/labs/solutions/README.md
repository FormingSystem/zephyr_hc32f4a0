<!-- SPDX-License-Identifier: Apache-2.0 -->

# P01 限幅练习的代码对照

本目录保存正文完整展示的三个修改文件，供输入代码时对照。它们是主机起始工程的增量，不是另一个需要先完成的实验。

limit.h 对应复制品 include/limit.h，limit.c 对应 src/limit.c，main_with_limit.c 对应替换后的 src/main.c。CMake 中登记 limit.c、将预期输出改为 40 的步骤与原因仍在 P01 正文中完成。

不用把 main_with_limit.c 作为第二个 main 编入目标；它的文件名用于区分材料角色。
