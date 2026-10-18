---
id: learning.zephyr-docs.qemu-other-reference.page-4
title: QEMU_Renesas_RX仿真开发板
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/rx/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_QEMU\_Renesas\_RX仿真开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/rx/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

## 4.1\_开发板概况与概述

<a id="qemu_rx"></a>

名称：`qemu_rx`。厂商：[Renesas Electronics Corporation](https://docs.zephyrproject.org/latest/boards/index.html#vendor=renesas)。状态：未积极维护（Not Actively Maintained）。架构（Architecture）：[rx](https://docs.zephyrproject.org/latest/boards/index.html#arch=rx)；片上系统（System on Chip，SoC）：[r5f562n8](https://docs.zephyrproject.org/latest/boards/index.html#soc=r5f562n8)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/rx)。

<a id="overview"></a>

此配置使用 QEMU 仿真 Renesas RXv1 平台，支持 R5F562N8 微控制器（Microcontroller Unit，MCU）及以下设备：

- 片上存储器（On-chip Memory）：ROM 512KB、RAM 96KB，单位写法沿用原文。
- 中断控制单元（Interrupt Control Unit，ICUa）。
- 两个比较匹配定时器通道（Compare Match Timer，CMT0、CMT1）。
- 一个串行通信接口通道（Serial Communication Interface，SCI0）。

<a id="hardware"></a>

## 4.2\_硬件

<a id="supported-features"></a>

<a id="qemu_rx-hw-features"></a>

官方在此提供 `qemu_rx` 的硬件特性（Supported Features）及图例。片上（on-chip）表示特性集成在 SoC 内，板上（on-board）表示位于开发板。启用／禁用数字是相应状态的实例数量，数字链接跳转到开发板或 SoC 设备树源码（DTS）中该状态的第一个实例；兼容字符串（Compatible String，如 `vnd,foo`）链接跳转到绑定文档。

RAM 为随机存取存储器，Flash 为闪存，SRAM 为静态随机存取存储器；KiB、MiB 分别为二进制千字节、兆字节。CPU 为中央处理器，UART 为通用异步收发器。

<a id="qemu_rx-qemu_rx/r5f562n8-hw-features-section"></a>

<a id="qemu_rx-qemu_rx/r5f562n8-hw-features-panel"></a>

<a id="qemu_rx-qemu_rx/r5f562n8-hw-features-memory"></a>

<a id="qemu_rx-qemu_rx/r5f562n8-hw-features-table"></a>

### 4.2.1\_目标 `qemu_rx/r5f562n8`

目标存储容量：RAM 为 96 KiB，Flash 为 512 KiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中央处理器（Central Processing Unit，CPU） | 片上（on-chip） | Renesas RXv1 中央处理器（CPU） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L24) | — | [`renesas,rxv1`](../cpu_vendor_multiarc_binding_reference/P030_renesas_rxv1.md#std-dtcompatible-renesas-rxv1) |
| 时钟控制（Clock Control） | 片上（on-chip） | Renesas RX 根时钟生成电路（Root Clock Generation Circuit） | [4](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L64) | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L95) | [`renesas,rx-cgc-root-clock`](../clock_renesas_rockchip_sifli_silabs_binding_reference/P010_renesas_rx-cgc-root-clock.md#std-dtcompatible-renesas-rx-cgc-root-clock) |
| 时钟控制（Clock Control） | 片上（on-chip） | Renesas RX 时钟生成电路的锁相环时钟（PLL Clock） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L102) | — | [`renesas,rx-cgc-pll`](../clock_renesas_rockchip_sifli_silabs_binding_reference/P008_renesas_rx-cgc-pll.md#std-dtcompatible-renesas-rx-cgc-pll) |
| 时钟控制（Clock Control） | 片上（on-chip） | Renesas RX 时钟控制节点的外设时钟模块（PCLK Block） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L111) | — | [`renesas,rx-cgc-pclk-block`](../clock_renesas_rockchip_sifli_silabs_binding_reference/P006_renesas_rx-cgc-pclk-block.md#std-dtcompatible-renesas-rx-cgc-pclk-block) |
| 时钟控制（Clock Control） | 片上（on-chip） | Renesas RX 时钟控制外设时钟（Peripheral Clock） | [4](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L120) | — | [`renesas,rx-cgc-pclk`](../clock_renesas_rockchip_sifli_silabs_binding_reference/P007_renesas_rx-cgc-pclk.md#std-dtcompatible-renesas-rx-cgc-pclk) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | Renesas ICU 中断控制器（Interrupt Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L32) | — | [`renesas,rx-icu`](../renesas_interrupt_binding_reference/P002_renesas_rx-icu.md#std-dtcompatible-renesas-rx-icu) |
| 杂项（Miscellaneous） | 片上（on-chip） | Renesas RX 串行通信接口控制器（SCI Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L173) | — | [`renesas,rx-sci`](../misc_nxp_renesas_zephyr_binding_reference/P026_renesas_rx-sci.md#std-dtcompatible-renesas-rx-sci) |
| 存储技术设备（Memory Technology Device，MTD） | 片上（on-chip） | 闪存节点（Flash Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L167) | — | [`soc-nv-flash`](../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Renesas RX 架构 | 片上（on-chip） | Renesas RX 软件中断（Software Interrupt，SWINT） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L51) | — | [`renesas,rx-swint`](../platform_rmt_openthread_binding_reference/P012_renesas_rx-swint.md#std-dtcompatible-renesas-rx-swint) |
| 串行控制器（Serial Controller） | 片上（on-chip） | Renesas RX 串行通信接口 QEMU 控制器（SCI QEMU Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L181) | — | [`renesas,rx-uart-sci-qemu`](../uart_raspberrypi_realtek_renesas_binding_reference/P012_renesas_rx-uart-sci-qemu.md#std-dtcompatible-renesas-rx-uart-sci-qemu) |
| 静态随机存取存储器（Static Random-Access Memory，SRAM） | 片上（on-chip） | 通用片上 SRAM（Generic On-chip SRAM） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L156) | — | [`mmio-sram`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sram/mmio-sram.html#std-dtcompatible-mmio-sram) |
| 定时器（Timer） | 片上（on-chip） | Renesas RX 定时器节点（Timer Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L187) | — | [`renesas,rx-timer-cmt-start-control`](../renesas_timer_binding_reference/P003_renesas_rx-timer-cmt-start-control.md#std-dtcompatible-renesas-rx-timer-cmt-start-control) |
| 定时器（Timer） | 片上（on-chip） | Renesas RX 定时器节点（Timer Node） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx-qemu.dtsi?plain=1#L196) | — | [`renesas,rx-timer-cmt`](../renesas_timer_binding_reference/P004_renesas_rx-timer-cmt.md#std-dtcompatible-renesas-rx-timer-cmt) |

<a id="devices"></a>

<a id="system-clock"></a>

### 4.2.2\_设备与系统时钟

此配置使用由 CMT 定时器产生的 6 MHz 系统时钟频率（System Clock Frequency）。

<a id="serial-port"></a>

串口（Serial Port）：此配置在SCI UART 通道0上使用单个串行通信通道。

<a id="programming-and-debugging"></a>

## 4.3\_编程与调试

`qemu_rx` 支持以下运行器（Runner）及关联 west 命令：

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

使用此配置在 QEMU 仿真环境中运行基本 Zephyr 应用及内核测试，例如[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)。从 Zephyr 仓库根目录执行；原代码注释 `From the root of the zephyr repository` 也表示这一位置。

```shell
# From the root of the zephyr repository
west build -b qemu_rx samples/synchronization
west build -t run
```

这会构建包含同步示例应用的镜像（Image），使用 QEMU 启动，并显示以下控制台输出：

```text
*** Booting Zephyr OS build v4.1.0-3157-gb30f8b6a7327 ***
thread_a: Hello World from cpu 0 on qemu_rx!
thread_b: Hello World from cpu 0 on qemu_rx!
thread_a: Hello World from cpu 0 on qemu_rx!
thread_b: Hello World from cpu 0 on qemu_rx!
thread_a: Hello World from cpu 0 on qemu_rx!
thread_b: Hello World from cpu 0 on qemu_rx!
thread_a: Hello World from cpu 0 on qemu_rx!
thread_b: Hello World from cpu 0 on qemu_rx!
thread_a: Hello World from cpu 0 on qemu_rx!
thread_b: Hello World from cpu 0 on qemu_rx!
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

<a id="references"></a>

## 4.4\_参考资料

- [QEMU 官方网站](https://www.qemu.org/)。

> 译注：命令、输出和历史版本号按官方原文保留；本次翻译未运行固件，也未安装工具链。

---

[上一章](P003_QEMU_OpenRISC_1000仿真开发板.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P005_QEMU_Hexagon仿真开发板.md)
