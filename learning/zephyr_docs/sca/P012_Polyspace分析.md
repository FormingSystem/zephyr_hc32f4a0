---
id: learning.zephyr-docs.sca.sca-polyspace
title: Polyspace分析
kind: reference
status: maintained
domains: [zephyr, sca]
source_url: https://docs.zephyrproject.org/latest/develop/sca/polyspace.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第12章\_Polyspace分析

原文：[Polyspace support](https://docs.zephyrproject.org/latest/develop/sca/polyspace.html)。读取日期：2026-10-12，`latest`。

[Polyspace®](https://mathworks.com/products/polyspace.html) 是 MathWorks 的商业静态代码分析工具，原文说明它具有用于最高安全等级场景的相关认证。它可检查 MISRA C、CERT C 等编码指南，发现**通用弱点枚举（Common Weakness Enumeration，CWE）**类别的问题、软件缺陷，并计算代码复杂度指标。

它还可选用**形式化证明（Formal Proof）**，验证不存在数组越界、溢出、竞争条件等运行时错误，帮助实现内存安全。

> 译注：MISRA 与 CERT 在这里是编码规范名称。工具的认证与能力不等同于项目已经取得认证；形式化结果也需在所用模型、配置及工具报告所声明的范围内解释。

## 12.1\_安装、命令路径与许可

必须安装 Polyspace，并在操作系统或容器的 `PATH` 命令搜索路径中加入 `<polyspace_root>/polyspace/bin`，其中 `<polyspace_root>` 是实际安装根。

安装步骤见 [Polyspace Bug Finder安装说明](https://mathworks.com/help/bugfinder/install-polyspace.html)。如果需要证明不存在缺陷，还需按 [Polyspace Code Prover安装说明](https://mathworks.com/help/codeprover/install-polyspace.html)准备相应工具。

安装目录中必须有可用的许可证文件，试用申请见 [MathWorks试用入口](https://www.mathworks.com/campaigns/products/trials.html)。

## 12.2\_通过构建触发分析

在 `west build` 中追加 `-DZEPHYR_SCA_VARIANT=polyspace`：

```sh
west build -b qemu_x86 samples/hello_world -- -DZEPHYR_SCA_VARIANT=polyspace
```

> 译注：从准备好工具链、依赖和 Polyspace 的 Zephyr 源码根，用 Bash 执行。原例为 `qemu_x86` 的 Hello World；命令触发构建分析，不代表运行固件。若工具、许可或编译阶段失败，先处理对应错误，再检查结果是否完整。本次未执行分析。

## 12.3\_审查结果

构建末尾在控制台输出发现问题的摘要，并显示详细结果目录。

可以在 [Polyspace用户界面](https://mathworks.com/help/bugfinder/review-results-1.html)打开该目录，或按[服务器与网页工作流](https://mathworks.com/help/bugfinder/gs/run-bug-finder-on-server.html)上传后审查。

如果需要在**持续集成（Continuous Integration，CI）**流程中编程读取结果，结果目录内也包含以 **逗号分隔值（Comma-Separated Values，CSV）**格式描述各问题的文件。

## 12.4\_配置分析范围与模式

默认会检查全部 C/C++ 源码中的典型编程缺陷。下列 CMake 选项可改变行为：

| 选项 | 作用 | 示例参数 |
| --- | --- | --- |
| `POLYSPACE_ONLY_APP` | 仅分析用户应用代码，忽略 Zephyr 源码。 | `-DPOLYSPACE_ONLY_APP=1` |
| `POLYSPACE_OPTIONS` | 附加命令行选项，例如选择编码规则；选项及其值用分号分隔。 | `-DPOLYSPACE_OPTIONS="-misra3;mandatory-required;-checkers;all"` |
| `POLYSPACE_OPTIONS_FILE` | 用文本文件逐行提供选项；必须传入文件的完整路径。 | `-DPOLYSPACE_OPTIONS_FILE="$PWD/myoptions.txt"` |
| `POLYSPACE_MODE` | 在缺陷查找与证明模式之间切换，默认缺陷查找。 | `-DPOLYSPACE_MODE=prove` |
| `POLYSPACE_PROG_NAME` | 覆盖被分析应用名，默认由板和应用名组成。 | `-DPOLYSPACE_PROG_NAME=myapp` |
| `POLYSPACE_PROG_VERSION` | 覆盖应用版本，默认来自 `git describe`。 | `-DPOLYSPACE_PROG_VERSION=v1.0b-28f023` |

全部附加分析选项见 [Polyspace选项参考](https://mathworks.com/help/bugfinder/referencelist.html?type=analysisopt&s_tid=CRUX_topnav)，两种分析模式的区别见 [Bug Finder与Code Prover](https://mathworks.com/help/bugfinder/gs/use-bug-finder-and-code-prover.html)。

> 译注：文件参数把原文固定主机路径改为 Bash 的 `$PWD/myoptions.txt`，表示当前源码根内自行创建的选项文件；Bash 在调用时展开为本机完整路径，满足工具输入要求，同时不在译文中绑定盘符。上表是附加参数，不是独立终端命令。上传结果属于官方说明的后续工作流，本次没有上传工程数据。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：IAR_C_STAT分析](P011_IAR_C_STAT分析.md) · [本模块主线目录](../reading/sca.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：IAR_C_STAT分析](P011_IAR_C_STAT分析.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
