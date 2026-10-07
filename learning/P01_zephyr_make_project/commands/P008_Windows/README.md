<!-- SPDX-License-Identifier: Apache-2.0 -->

# P008_Windows 可复制操作

对应 [正文](../../P008_west零基础与Zephyr构建_Windows.md)。按正文的前提、分支和预期结果选择操作，不批量执行所有文件。`step` 文件按正文操作块排列；小节编号文件保留 PPT 直接跳转入口，同一操作可能有两个入口。Bash、PowerShell 分别在正文指定的终端执行，不能把全部文件视为同一终端脚本。

| 完整操作单元 | 对应正文小节 | 代码语言 |
| --- | --- | --- |
| [step-01.txt](step-01.txt) | 8.1 先把 west 程序与 Zephyr 分开 | bash |
| [step-02.txt](step-02.txt) | 8.2 工作区怎样找到正确的清单 | bash |
| [step-03.txt](step-03.txt) | 8.2 工作区怎样找到正确的清单 | bash |
| [step-04.txt](step-04.txt) | 8.3 清单怎样决定下载什么 | bash |
| [step-05.txt](step-05.txt) | 8.3 清单怎样决定下载什么 | bash |
| [step-06.txt](step-06.txt) | 8.4 Zephyr 怎样把 build 命令交给 west | bash |
| [step-07.txt](step-07.txt) | 8.5.1 先只配置，观察 west 传给 CMake 的参数 | bash |
| [step-08.txt](step-08.txt) | 8.5.2 构建，以及与直接 CMake 共用目录 | bash |
| [step-09.txt](step-09.txt) | 8.5.2 构建，以及与直接 CMake 共用目录 | bash |
| [step-10.txt](step-10.txt) | 8.6 常用方式要分清参数交给谁 | bash |
