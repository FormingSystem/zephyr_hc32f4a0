---
id: learning.zephyr-docs.qemu-catalog-reference.page-2
title: QEMU_ARCv2与ARCv3
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/arc/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_QEMU\_ARCv2与ARCv3

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/arc/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="qemu_arc"></a>

## 2.1\_开发板概况与概述

名称：`qemu_arc`。厂商：[QEMU，通用开源机器仿真器与虚拟化器](https://docs.zephyrproject.org/latest/boards/index.html#vendor=qemu)。状态：持续维护（Maintained）。架构（Architecture）：[arc](https://docs.zephyrproject.org/latest/boards/index.html#arch=arc)；片上系统（SoC）：[qemu_arc_hs5x](https://docs.zephyrproject.org/latest/boards/index.html#soc=qemu_arc_hs5x)、[qemu_arc_hs6x](https://docs.zephyrproject.org/latest/boards/index.html#soc=qemu_arc_hs6x)、[qemu_arc_hs](https://docs.zephyrproject.org/latest/boards/index.html#soc=qemu_arc_hs)、[qemu_arc_em](https://docs.zephyrproject.org/latest/boards/index.html#soc=qemu_arc_em)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/arc)。

<a id="overview"></a>

此配置使用 QEMU 仿真一组通用 ARCv2 与 ARCv3 硬件平台。目前支持 ARC 指令集架构（ISA）核心的以下特性：

- CPU：ARCv2 EM、ARCv2 HS3x、ARCv3 HS5x、ARCv3 HS6x。
- 仅支持小端（Little-Endian）配置。
- 完整的32个寄存器集合（Register Set）。
- ARC 核心自由运行定时器／计数器（Free-running Timers/Counters）Timer0、Timer1。
- 支持多个优先级（Priority Levels）的 ARC 核心中断控制器。
- DesignWare（DW）通用异步收发器（UART）。
- 五个内存映射输入输出（MMIO）Virtio 设备插槽。

<a id="hardware"></a>

## 2.2\_硬件

<a id="supported-features"></a>

<a id="qemu_arc-hw-features"></a>

`qemu_arc` 的硬件特性（Supported Features）及图例如下。片上（on-chip）表示集成在 SoC 内，板上（on-board）表示位于开发板。启用／禁用数字保留相应实例数量，链接指向开发板或 SoC 设备树源码（DTS）中该状态的第一个实例；兼容字符串（Compatible String，如 `vnd,foo`）链接指向绑定文档。

CPU 为中央处理器，UART 为通用异步收发器；RAM 为随机存取存储器，Flash 为闪存；KiB、MiB 为二进制千字节和兆字节。

<a id="qemu_arc-qemu_arc/qemu_arc_em-hw-features-section"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_em-hw-features-panel"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_em-hw-features-memory"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_em-hw-features-table"></a>

### 2.2.1\_目标 `qemu_arc/qemu_arc_em`

目标存储容量：RAM 为 4 MiB，Flash 为 4 MiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中央处理器（Central Processing Unit，CPU） | 板上（on-board） | Synopsys ARC EM 中央处理器（CPU） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc_qemu_arc_em.dts?plain=1#L19) | — | [`snps,arcem`](../cpu_vendor_multiarc_binding_reference/P042_snps_arcem.md#std-dtcompatible-snps-arcem) |
| 中断控制器（Interrupt Controller） | 板上（on-board） | ARCV2 中断控制器（Interrupt Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L21) | — | [`snps,arcv2-intc`](../multiarch_interrupt_binding_reference/P004_snps_arcv2-intc.md#std-dtcompatible-snps-arcv2-intc) |
| 存储技术设备（Memory Technology Device，MTD） | 板上（on-board） | 闪存节点（Flash Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L40) | — | [`soc-nv-flash`](../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| 串行控制器（Serial Controller） | 板上（on-board） | ns16550 通用异步收发器（UART） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L50) | — | [`ns16550`](../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550) |
| 定时器（Timer） | 板上（on-board） | 带中断能力的 Synopsys ARC 本地定时器（Local Timer with Interrupt Capabilities） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L27) | — | [`snps,arc-timer`](../system_timer_binding_reference/P006_snps_arc-timer.md#std-dtcompatible-snps-arc-timer) |

<a id="qemu_arc-qemu_arc/qemu_arc_hs-hw-features-section"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_hs-hw-features-panel"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_hs-hw-features-memory"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_hs-hw-features-table"></a>

### 2.2.2\_目标 `qemu_arc/qemu_arc_hs`

目标存储容量：RAM 为 4 MiB，Flash 为 4 MiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中断控制器（Interrupt Controller） | 板上（on-board） | ARCV2 中断控制器（Interrupt Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L21) | — | [`snps,arcv2-intc`](../multiarch_interrupt_binding_reference/P004_snps_arcv2-intc.md#std-dtcompatible-snps-arcv2-intc) |
| 存储技术设备（Memory Technology Device，MTD） | 板上（on-board） | 闪存节点（Flash Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L40) | — | [`soc-nv-flash`](../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| 串行控制器（Serial Controller） | 板上（on-board） | ns16550 通用异步收发器（UART） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L50) | — | [`ns16550`](../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550) |
| 定时器（Timer） | 板上（on-board） | 带中断能力的 Synopsys ARC 本地定时器（Local Timer with Interrupt Capabilities） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L27) | — | [`snps,arc-timer`](../system_timer_binding_reference/P006_snps_arc-timer.md#std-dtcompatible-snps-arc-timer) |

<a id="qemu_arc-qemu_arc/qemu_arc_hs/xip-hw-features-section"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_hs/xip-hw-features-panel"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_hs/xip-hw-features-memory"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_hs/xip-hw-features-table"></a>

### 2.2.3\_目标 `qemu_arc/qemu_arc_hs/xip`

目标存储容量：RAM 为 4 MiB，Flash 为 4 MiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中断控制器（Interrupt Controller） | 板上（on-board） | ARCV2 中断控制器（Interrupt Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L21) | — | [`snps,arcv2-intc`](../multiarch_interrupt_binding_reference/P004_snps_arcv2-intc.md#std-dtcompatible-snps-arcv2-intc) |
| 存储技术设备（Memory Technology Device，MTD） | 板上（on-board） | 闪存节点（Flash Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L40) | — | [`soc-nv-flash`](../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| 串行控制器（Serial Controller） | 板上（on-board） | ns16550 通用异步收发器（UART） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L50) | — | [`ns16550`](../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550) |
| 定时器（Timer） | 板上（on-board） | 带中断能力的 Synopsys ARC 本地定时器（Local Timer with Interrupt Capabilities） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L27) | — | [`snps,arc-timer`](../system_timer_binding_reference/P006_snps_arc-timer.md#std-dtcompatible-snps-arc-timer) |

<a id="qemu_arc-qemu_arc/qemu_arc_hs5x-hw-features-section"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_hs5x-hw-features-panel"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_hs5x-hw-features-memory"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_hs5x-hw-features-table"></a>

### 2.2.4\_目标 `qemu_arc/qemu_arc_hs5x`

目标存储容量：RAM 为 4 MiB，Flash 为 4 MiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中断控制器（Interrupt Controller） | 板上（on-board） | ARCV2 中断控制器（Interrupt Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L21) | — | [`snps,arcv2-intc`](../multiarch_interrupt_binding_reference/P004_snps_arcv2-intc.md#std-dtcompatible-snps-arcv2-intc) |
| 存储技术设备（Memory Technology Device，MTD） | 板上（on-board） | 闪存节点（Flash Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L40) | — | [`soc-nv-flash`](../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| 串行控制器（Serial Controller） | 板上（on-board） | ns16550 通用异步收发器（UART） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L50) | — | [`ns16550`](../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550) |
| 定时器（Timer） | 板上（on-board） | 带中断能力的 Synopsys ARC 本地定时器（Local Timer with Interrupt Capabilities） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L27) | — | [`snps,arc-timer`](../system_timer_binding_reference/P006_snps_arc-timer.md#std-dtcompatible-snps-arc-timer) |

<a id="qemu_arc-qemu_arc/qemu_arc_hs6x-hw-features-section"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_hs6x-hw-features-panel"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_hs6x-hw-features-memory"></a>

<a id="qemu_arc-qemu_arc/qemu_arc_hs6x-hw-features-table"></a>

### 2.2.5\_目标 `qemu_arc/qemu_arc_hs6x`

目标存储容量：RAM 为 4 MiB，Flash 为 4 MiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中断控制器（Interrupt Controller） | 板上（on-board） | ARCV2 中断控制器（Interrupt Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L21) | — | [`snps,arcv2-intc`](../multiarch_interrupt_binding_reference/P004_snps_arcv2-intc.md#std-dtcompatible-snps-arcv2-intc) |
| 存储技术设备（Memory Technology Device，MTD） | 板上（on-board） | 闪存节点（Flash Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L40) | — | [`soc-nv-flash`](../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| 串行控制器（Serial Controller） | 板上（on-board） | ns16550 通用异步收发器（UART） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L50) | — | [`ns16550`](../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550) |
| 定时器（Timer） | 板上（on-board） | 带中断能力的 Synopsys ARC 本地定时器（Local Timer with Interrupt Capabilities） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/arc/qemu_arc.dtsi?plain=1#L27) | — | [`snps,arc-timer`](../system_timer_binding_reference/P006_snps_arc-timer.md#std-dtcompatible-snps-arc-timer) |

<a id="devices"></a>

<a id="system-clock"></a>

### 2.2.6\_设备与系统时钟

此配置使用1 MHz的系统时钟频率。

<a id="serial-port"></a>

通过 DesignWare UART 使用单个串行通信通道。

<a id="known-problems-or-limitations"></a>

以下平台特性不受支持：

- 内存保护单元（MPU）。
- MMIO Virtio 以太网（Ethernet）。

<a id="programming-and-debugging"></a>

## 2.3\_编程与调试

原页列出 `qemu_arc` 支持的运行器（Runner）及关联 west 命令：

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

以[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)为例，下面的命令从 Zephyr 仓库根目录执行，原代码注释也表示这一位置。

可按目标 CPU 选择 `qemu_arc/qemu_em`、`qemu_arc/qemu_hs`、`qemu_arc/qemu_hs5x` 或 `qemu_arc/qemu_hs6x`。

> 译注：上述名称及下方命令来自原文操作说明，与硬件表中的 `qemu_arc/qemu_arc_em` 等目标拼写不一致；两处均原样保留，使用时应以实际源码支持的目标为准。

```shell
# From the root of the zephyr repository
west build -b qemu_arc/qemu_em samples/synchronization
west build -t run
```

这会构建包含同步示例的镜像（Image），使用 QEMU 启动，并显示以下控制台输出：

```text
*** Booting Zephyr OS build zephyr-v2.2.0-2486-g7dbfcf4bab57  ***
threadA: Hello World from qemu_arc!
threadB: Hello World from qemu_arc!
threadA: Hello World from qemu_arc!
threadB: Hello World from qemu_arc!
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

<a id="debugging"></a>

详细概述参见[应用调试](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

<a id="references"></a>

参考资料：[ARC HS 程序员参考手册（Programmer’s Reference Manual for ARC HS）](https://www.synopsys.com/dw/doc.php/iip/dwc_arc_hs4xd/latest/doc/ARC_V2_PublicProgrammers_Reference.pdf)。

> 译注：命令、日志和版本号按官方示例保留，本次翻译未构建或运行固件。

---

[上一章](P001_QEMU_目录.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P003_QEMU_X86.md)
