<!-- SPDX-License-Identifier: Apache-2.0 -->

# 主机源码与库实验

从仓库根目录按 [CMake P01](../../P01_把源文件和库加入构建.md)执行。main → scale_sample → calibrate，预期 value=43。LESSON_OMIT_CALIBRATION 故意漏实现，用于观察链接失败。

源码在此目录，所有产物在 build/learning-tools；不需要 Python 或 Zephyr SDK。GDB 命令在 [VS Code 章节](../../../vscode/P01_搭建编译与单步调试环境.md)。
