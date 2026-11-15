---
id: learning.zephyr-docs.toolchains.page-13
title: ARC_MetaWare工具链
kind: reference
status: maintained
domains: [zephyr, toolchains, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/toolchains/designware_arc_mwdt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="designware-arc-metaware-development-toolkit-mwdt"></a>
<a id="toolchain-designware-arc-mwdt"></a>

# 第13章\_ARC\_MetaWare工具链

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/toolchains/designware_arc_mwdt.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

## 13.1\_安装前提

主机需要安装 [ARC MetaWare开发工具包（MetaWare Development Toolkit，MWDT）](https://www.synopsys.com/dw/ipdir.php?ds=sw_metaware)，同时安装 [Zephyr SDK](P002_ZephyrSDK.md#toolchain-zephyr-sdk)。

> 译注——外部入口：本次复核时，原ARC MWDT链接重定向到MIPS面向Infineon AURIX TC4x的MetaWare页面。原引用保留用于追溯，但该目标专用页面不能直接代替所有ARC目标的安装包选择依据；下载前须确认工具包面向实际目标。

**注意：**Zephyr软件开发工具包（Software Development Kit，SDK）提供设备树编译器（Devicetree Compiler，DTC）、QEMU等工具。即使使用ARC MWDT构建Zephyr实时操作系统（Real-Time Operating System，RTOS），设备树预处理和 `.bin` 文件生成等阶段仍可能使用GNU预处理器（Preprocessor）及GNU `objcopy`；原文同样从Zephyr SDK取得这些ARC GNU工具。

设置ARC GNU工具链时，使用SDK完整包或最小包（Full or Minimal Bundle），不要手工拼装彼此独立的归档。原文说明SDK安装并注册工具链和主机工具，可减少Zephyr构建中的工具链问题。

> 译注——包类型：Minimal本身不代表已包含ARC目标编译器，需要按[SDK说明](P002_ZephyrSDK.md)补齐所需目标工具。安装工具、让CMake发现SDK与实际构建是不同步骤；本页没有执行安装或注册。

## 13.2\_设置环境变量

按[环境变量说明](P003_环境变量.md#env-vars)操作：

- [`ZEPHYR_TOOLCHAIN_VARIANT`](P003_环境变量.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) 设为 `arcmwdt`。
- `ARCMWDT_TOOLCHAIN_PATH` 设为工具链安装目录。MWDT安装提供 `METAWARE_ROOT`，因此Linux可使用 `$METAWARE_ROOT/../`，Windows可使用 `%METAWARE_ROOT%\..\`。

**提示：**原文说明，如果机器仅安装一个ARC MWDT版本，可省略 `ARCMWDT_TOOLCHAIN_PATH`，由工具自动检测。

> 译注——自动检测的依据：所读[官方generic.cmake](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/cmake/toolchain/arcmwdt/generic.cmake)在未给出ARCMWDT_TOOLCHAIN_PATH时，使用METAWARE_ROOT环境变量的父目录；两者都未定义会报错。因此“只装一个版本”仍以安装器提供的环境可见为前提，不表示会扫描整台机器。该文件还明确查找Zephyr SDK。

## 13.3\_检查当前环境

以下保留原文交互式Shell会话；Linux使用Shell变量，Windows使用cmd变量语法。`$` 和 `>` 是提示符，不是需要复制的命令字符；紧随echo之后的路径行是预期输出示例。读者的实际安装路径可以不同。

```text
# Linux:
$ echo $ZEPHYR_TOOLCHAIN_VARIANT
arcmwdt
$ echo $ARCMWDT_TOOLCHAIN_PATH
/home/you/ARC/MWDT_2023.03/

# Windows:
> echo %ZEPHYR_TOOLCHAIN_VARIANT%
arcmwdt
> echo %ARCMWDT_TOOLCHAIN_PATH%
C:\ARC\MWDT_2023.03\
```

应确认工具链类型输出为arcmwdt，安装目录对应实际MWDT安装。若变量为空或指向不存在目录，返回上一节检查安装器环境和变量设置，再继续应用构建。


对应官方文档源码：[doc/develop/toolchains/designware_arc_mwdt.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/toolchains/designware_arc_mwdt.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/toolchains/designware_arc_mwdt.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

<a id="index-0"></a>
<a id="index-1"></a>
<a id="index-2"></a>
<a id="index-3"></a>
<a id="index-4"></a>
<a id="index-5"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Cadence_XCC工具链](P012_Cadence_XCC工具链.md) · [本模块主线目录](../reading/toolchains.md) · [全部主线](../reading/README.md) · [下一篇：Hexagon_LLVM工具链](P014_Hexagon_LLVM工具链.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P012_Cadence_XCC工具链.md) · [返回大纲](大纲.md) · [下一章](P014_Hexagon_LLVM工具链.md)

</details>

<!-- reading-navigation:end -->
