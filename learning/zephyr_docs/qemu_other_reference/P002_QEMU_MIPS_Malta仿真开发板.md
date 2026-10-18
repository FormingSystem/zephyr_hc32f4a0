---
id: learning.zephyr-docs.qemu-other-reference.page-2
title: QEMU_MIPS_Malta仿真开发板
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/malta/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_QEMU\_MIPS\_Malta仿真开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/malta/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

## 2.1\_开发板概况与概述

<a id="qemu_malta"></a>

名称：`qemu_malta`。厂商：[QEMU，通用开源机器仿真器与虚拟化器](https://docs.zephyrproject.org/latest/boards/index.html#vendor=qemu)。状态：未积极维护（Not Actively Maintained）。架构（Architecture）：[mips](https://docs.zephyrproject.org/latest/boards/index.html#arch=mips)；片上系统（System on Chip，SoC）：[qemu_malta](https://docs.zephyrproject.org/latest/boards/index.html#soc=qemu_malta)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/malta)。

<a id="overview"></a>

此配置使用 QEMU 仿真 MIPS Malta 平台，支持 MIPS 4Kc/24Kc CPU 核心以及 CP0 中断控制器（Interrupt Controller）、CP0 核心定时器（Core Timer）和 NS16550 通用异步收发器（UART）。

> 原文注意：此开发板配置不声称适用于实际 MIPS Malta 硬件系统或任何其他硬件系统。

<a id="hardware"></a>

## 2.2\_硬件

<a id="supported-features"></a>

<a id="qemu_malta-hw-features"></a>

官方在此提供 `qemu_malta` 的硬件特性（Supported Features）及图例。片上（on-chip）表示特性集成在 SoC 内，板上（on-board）表示位于开发板。启用／禁用数字是相应状态的实例数量，数字链接跳转到开发板或 SoC 设备树源码（DTS）中该状态的第一个实例；兼容字符串（Compatible String，如 `vnd,foo`）链接跳转到绑定文档。

RAM 为随机存取存储器，Flash 为闪存，SRAM 为静态随机存取存储器；KiB、MiB 分别为二进制千字节、兆字节。CPU 为中央处理器，UART 为通用异步收发器。

<a id="qemu_malta-qemu_malta/qemu_malta-hw-features-section"></a>

<a id="qemu_malta-qemu_malta/qemu_malta-hw-features-panel"></a>

<a id="qemu_malta-qemu_malta/qemu_malta-hw-features-memory"></a>

<a id="qemu_malta-qemu_malta/qemu_malta-hw-features-table"></a>

### 2.2.1\_目标 `qemu_malta/qemu_malta`

目标存储容量：RAM 为 1 MiB，Flash 为 不适用（N/A）。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中断控制器（Interrupt Controller） | 板上（on-board） | MIPS CPU 中断控制器（Interrupt Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/malta/qemu_malta.dts?plain=1#L30) | — | [`mti,cpu-intc`](../soc_interrupt_binding_reference/P011_mti_cpu-intc.md#std-dtcompatible-mti-cpu-intc) |
| 串行控制器（Serial Controller） | 板上（on-board） | ns16550 通用异步收发器（UART） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/malta/qemu_malta.dts?plain=1#L44) | — | [`ns16550`](../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550) |
| 静态随机存取存储器（Static Random-Access Memory，SRAM） | 板上（on-board） | 通用片上 SRAM（Generic On-chip SRAM） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/malta/qemu_malta.dts?plain=1#L38) | — | [`mmio-sram`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sram/mmio-sram.html#std-dtcompatible-mmio-sram) |

<a id="qemu_malta-qemu_malta/qemu_malta/be-hw-features-section"></a>

<a id="qemu_malta-qemu_malta/qemu_malta/be-hw-features-panel"></a>

<a id="qemu_malta-qemu_malta/qemu_malta/be-hw-features-memory"></a>

<a id="qemu_malta-qemu_malta/qemu_malta/be-hw-features-table"></a>

### 2.2.2\_目标 `qemu_malta/qemu_malta/be`

目标存储容量：RAM 为 1 MiB，Flash 为 不适用（N/A）。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中断控制器（Interrupt Controller） | 板上（on-board） | MIPS CPU 中断控制器（Interrupt Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/malta/qemu_malta.dts?plain=1#L30) | — | [`mti,cpu-intc`](../soc_interrupt_binding_reference/P011_mti_cpu-intc.md#std-dtcompatible-mti-cpu-intc) |
| 串行控制器（Serial Controller） | 板上（on-board） | ns16550 通用异步收发器（UART） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/malta/qemu_malta.dts?plain=1#L44) | — | [`ns16550`](../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550) |
| 静态随机存取存储器（Static Random-Access Memory，SRAM） | 板上（on-board） | 通用片上 SRAM（Generic On-chip SRAM） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/malta/qemu_malta.dts?plain=1#L38) | — | [`mmio-sram`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sram/mmio-sram.html#std-dtcompatible-mmio-sram) |

<a id="devices"></a>

<a id="system-clock"></a>

### 2.2.3\_设备与系统时钟

QEMU CP0 定时器使用 200 MHz 时钟频率，详情见 QEMU 源码树中的 `target/mips/cp0_timer.c`。

<a id="serial-port"></a>

串口（Serial Port）：此配置在现场可编程门阵列（FPGA）的 UART2上使用单个串行通信通道。

<a id="programming-and-debugging"></a>

## 2.3\_编程与调试

`qemu_malta` 支持以下运行器（Runner）及关联 west 命令：

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

使用此配置在 QEMU 仿真环境中运行基本 Zephyr 应用及内核测试，例如[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)。从 Zephyr 仓库根目录执行；原代码注释 `From the root of the zephyr repository` 也表示这一位置。

```shell
# From the root of the zephyr repository
west build -b qemu_malta samples/synchronization
west build -t run
```

这会构建包含同步示例应用的镜像（Image），使用 QEMU 启动，并显示以下控制台输出：

```text
*** Booting Zephyr OS build v2.7.99-1627-g9bea7790d620  ***
thread_a: Hello World from cpu 0 on qemu_malta!
thread_b: Hello World from cpu 0 on qemu_malta!
thread_a: Hello World from cpu 0 on qemu_malta!
thread_b: Hello World from cpu 0 on qemu_malta!
thread_a: Hello World from cpu 0 on qemu_malta!
thread_b: Hello World from cpu 0 on qemu_malta!
thread_a: Hello World from cpu 0 on qemu_malta!
thread_b: Hello World from cpu 0 on qemu_malta!
thread_a: Hello World from cpu 0 on qemu_malta!
thread_b: Hello World from cpu 0 on qemu_malta!
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

<a id="big-endian"></a>

### 2.3.1\_大端模式

使用以下配置，以大端模式（Big-Endian）运行基础同步示例：

```shell
# From the root of the zephyr repository
west build -b qemu_malta/qemu_malta/be samples/synchronization
west build -t run
```

<a id="references"></a>

## 2.4\_参考资料

- [QEMU 官方网站](https://www.qemu.org/)。
- [MIPS Malta 资料](https://www.linux-mips.org/wiki/MIPS_Malta)。

> 译注：命令、输出和历史版本号按官方原文保留；本次翻译未运行固件，也未安装工具链。

---

[上一章](P001_QEMU_LEON3仿真开发板.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P003_QEMU_OpenRISC_1000仿真开发板.md)
