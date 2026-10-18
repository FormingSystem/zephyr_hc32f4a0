---
id: learning.zephyr-docs.qemu-other-reference.page-6
title: QEMU_Infineon_AURIX_TC39x与TC4Dx仿真开发板
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/tricore/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_QEMU\_Infineon\_AURIX\_TC39x与TC4Dx仿真开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/tricore/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

## 6.1\_开发板概况与概述

<a id="qemu_tc3x"></a>

名称：`qemu_tc3x`。厂商：[Infineon Technologies](https://docs.zephyrproject.org/latest/boards/index.html#vendor=infineon)。状态：持续维护（Maintained）。架构（Architecture）：[tricore](https://docs.zephyrproject.org/latest/boards/index.html#arch=tricore)；片上系统（System on Chip，SoC）：[qemu_tc3x](https://docs.zephyrproject.org/latest/boards/index.html#soc=qemu_tc3x)。

<a id="qemu_tc4x"></a>

名称：`qemu_tc4x`。厂商：[Infineon Technologies](https://docs.zephyrproject.org/latest/boards/index.html#vendor=infineon)。状态：持续维护（Maintained）。架构（Architecture）：[tricore](https://docs.zephyrproject.org/latest/boards/index.html#arch=tricore)；片上系统（System on Chip，SoC）：[qemu_tc4x](https://docs.zephyrproject.org/latest/boards/index.html#soc=qemu_tc4x)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/tricore)。

<a id="overview"></a>

在 QEMU 下仿真 Infineon AURIX TriCore 架构，支持两款开发板：

- `qemu_tc3x`：TC39x SoC，采用 TriCore TC1.6.2P 指令集架构（Instruction Set Architecture，ISA）。
- `qemu_tc4x`：TC4Dx SoC，采用 TriCore TC1.8P ISA。

两者均提供 STM 系统定时器（System Timer）、轮询模式（Polling-mode）的 ASCLIN UART 控制台，以及中断路由器（Interrupt Router）。

<a id="hardware"></a>

## 6.2\_硬件

<a id="supported-features"></a>

<a id="qemu_tc3x-hw-features"></a>

官方在此提供 `qemu_tc3x` 的硬件特性（Supported Features）及图例。片上（on-chip）表示特性集成在 SoC 内，板上（on-board）表示位于开发板。启用／禁用数字是相应状态的实例数量，数字链接跳转到开发板或 SoC 设备树源码（DTS）中该状态的第一个实例；兼容字符串（Compatible String，如 `vnd,foo`）链接跳转到绑定文档。

RAM 为随机存取存储器，Flash 为闪存，SRAM 为静态随机存取存储器；KiB、MiB 分别为二进制千字节、兆字节。CPU 为中央处理器，UART 为通用异步收发器。

原页没有列出具体构建目标及硬件特性表行，译文保留这一状态。

<a id="known-problems-or-limitations"></a>

已知问题与限制（Known Problems or Limitations）：不仿真对称多处理（SMP）、非对称多处理（AMP）或内存保护单元（MPU）。

<a id="programming-and-debugging"></a>

## 6.3\_编程与调试

<a id="qemu-setup"></a>

### 6.3.1\_QEMU配置

TriCore QEMU 不属于 Zephyr 软件开发工具包（SDK）。可使用[预编译二进制发行版](https://github.com/linumiz/qemu-tricore/releases)，也可从源码构建：

```shell
git clone https://github.com/linumiz/qemu-tricore.git
cd qemu-tricore
./configure --target-list=tricore-softmmu
make -j$(nproc) && make install
```

确保 `qemu-system-tricore` 位于 `$PATH` 命令搜索路径中。

原页在此列出 `qemu_tc3x` 的运行器（Runner）及 west 命令，但表格只有列标题、表体为空：

| 运行器 | `west flash` | `west debug` |
| --- | --- | --- |

<a id="running"></a>

### 6.3.2\_运行

构建并运行 [Hello World 示例](../getting_started/P005_HelloWorld示例.md#hello_world)；TC4Dx 目标使用 `qemu_tc4x`。从 Zephyr 仓库根目录执行（原代码注释也表示这一位置）：

```shell
# From the root of the zephyr repository
west build -b qemu_tc3x samples/hello_world
west build -t run
```

控制台显示：

```text
*** Booting Zephyr OS build ... ***
Hello World! qemu_tc3x/qemu_tc3x
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

<a id="debugging"></a>

### 6.3.3\_调试

详细概述参见[应用调试](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

> 译注：命令、输出和历史版本号按官方原文保留；本次翻译未运行固件，也未安装工具链。

---

[上一章](P005_QEMU_Hexagon仿真开发板.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md)
