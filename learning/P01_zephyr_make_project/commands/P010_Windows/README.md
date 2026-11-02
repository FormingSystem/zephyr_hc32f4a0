<!-- SPDX-License-Identifier: Apache-2.0 -->

# P010_Windows 可复制操作

> 历史命令附件：保留原编号与实验记录。Markdown 已重排，当前操作从 [大纲](../../大纲.md) 和 [当前命令索引](../current/README.md) 进入。

对应 [正文](../../P011_Zephyr的CMake输入与依赖发现.md)。按正文的前提、分支和预期结果选择操作，不批量执行所有文件。`step` 文件按正文操作块排列；小节编号文件保留历史入口，同一操作可能有两个入口。Bash、PowerShell 分别在正文指定的终端执行，不能把全部文件视为同一终端脚本。

本章沿 P008 的已有构建结果核对源码选择，不发起新的下载或构建。

| 完整操作单元 | 对应正文小节 | 代码语言 |
| --- | --- | --- |
| [trace-selected-sources.txt](trace-selected-sources.txt) | 10.3.5 从 BOARD、配置、模块记录查到编译单元 | bash / 内嵌 Python |

先完成 P008 的配置并启用编译命令导出。若使用自己的构建目录，修改块中唯一的 `build = Path(...)`，不要混用不同目录的结果。
