---
id: learning.zephyr-docs.toolchains.page-14
title: Hexagon_LLVM工具链
kind: reference
status: maintained
domains: [zephyr, toolchains, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/toolchains/hexagon_llvm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="qualcomm-hexagon-llvm-toolchain"></a>
<a id="toolchain-hexagon"></a>

# 第14章\_Hexagon\_LLVM工具链

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/toolchains/hexagon_llvm.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

## 14.1\_下载与解压

从 [toolchain_for_hexagon发布页](https://github.com/quic/toolchain_for_hexagon/releases)下载预构建Hexagon LLVM交叉工具链（Cross-toolchain）并解压，例如放在 `/opt/hexagon-toolchain`。安装根目录是包含 `bin/clang` 的目录。

使用由LLVM 23或更新版本构建的发行包。原文指出旧版本会错误编译 `~BIT(n)`，修复见 [LLVM修复#205489](https://github.com/llvm/llvm-project/pull/205489)。

> 译注——版本与位置：这里的LLVM版本是官方本页要求，不能仅凭包名含Hexagon就认为满足条件。上述目录是官方示例工具位置，读者按实际解压目录设置；不要把bin目录本身当作安装根。

## 14.2\_选择Hexagon工具链

设置 [`ZEPHYR_TOOLCHAIN_VARIANT`](P003_环境变量.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) 为 `hexagon`，[`HEXAGON_TOOLCHAIN_PATH`](#envvar-HEXAGON_TOOLCHAIN_PATH) 为上述安装根：

```bash
export ZEPHYR_TOOLCHAIN_VARIANT=hexagon
export HEXAGON_TOOLCHAIN_PATH=/opt/hexagon-toolchain
```

[`HEXAGON_TOOLCHAIN_PATH`](#envvar-HEXAGON_TOOLCHAIN_PATH)：Hexagon LLVM交叉工具链的安装目录（Install Directory）。

> 译注——终端与结果：这段是主机Bash环境设置，当前Shell及其子进程随后才能读取。先确认安装根下存在bin/clang；构建若报告HEXAGON_TOOLCHAIN_PATH未设置或找不到编译器，应先回查此目录与当前环境。

## 14.3\_与主机LLVM的关系

该工具链属于普通LLVM安装，因此本变体本质上是[主机工具链](P006_主机工具链.md#host-toolchains)的 `llvm` 变体驱动另一个编译器。

它单独使用一个路径变量，是因为Hexagon clang只注册Hexagon目标，不能构建 [原生模拟器native_sim](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)等需要主机编译的目标。一个环境若同时覆盖两类目标，必须分别指定两套LLVM安装；Zephyr持续集成（Continuous Integration，CI）在一次Twister运行跨越两类平台时就这样处理。

使用 `ZEPHYR_TOOLCHAIN_VARIANT=host/llvm` 和 `LLVM_TOOLCHAIN_PATH` 构建Hexagon目标仍然受支持，并与上述方式等效，前提是该路径确实指向Hexagon版LLVM。

> 译注——源码依据：[官方hexagon/generic.cmake](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/cmake/toolchain/hexagon/generic.cmake)把HEXAGON_TOOLCHAIN_PATH交给LLVM_TOOLCHAIN_PATH，再加载host/llvm接入代码。路径变量的区别用于选择编译器安装，并不意味着Hexagon编译器也能生成主机程序。


对应官方文档源码：[doc/develop/toolchains/hexagon_llvm.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/toolchains/hexagon_llvm.rst)。

> 译注——源码版本：本仓库参照版本尚无该文档，请按上方官方来源跟踪相应版本；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

<a id="index-0"></a>
<a id="index-1"></a>
<a id="envvar-HEXAGON_TOOLCHAIN_PATH"></a>
<a id="index-2"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：ARC_MetaWare工具链](P013_ARC_MetaWare工具链.md) · [本模块主线目录](../reading/toolchains.md) · [全部主线](../reading/README.md) · [下一篇：Intel_oneAPI工具包](P015_Intel_oneAPI工具包.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P013_ARC_MetaWare工具链.md) · [返回大纲](大纲.md) · [下一章](P015_Intel_oneAPI工具包.md)

</details>

<!-- reading-navigation:end -->
