---
id: learning.zephyr-docs.qemu-arm-reference.page-4
title: QEMU_Cortex_M3仿真开发板
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/cortex_m3/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_QEMU\_Cortex\_M3仿真开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/cortex_m3/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="qemu_cortex_m3"></a>

## 4.1\_开发板概况

名称：`qemu_cortex_m3`。厂商：[QEMU，通用开源机器仿真器与虚拟化器](https://docs.zephyrproject.org/latest/boards/index.html#vendor=qemu)。维护状态：未积极维护（Not Actively Maintained）。架构（Architecture）：[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)；片上系统（SoC）：[ti_lm3s6965](https://docs.zephyrproject.org/latest/boards/index.html#soc=ti_lm3s6965)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/cortex_m3)。

<a id="overview"></a>

此开发板配置使用 QEMU 仿真 TI LM3S6965 平台。配置支持 ARM Cortex-M3 CPU，以及嵌套向量中断控制器（NVIC）、系统节拍系统时钟（System Tick System Clock）和 Stellaris 通用异步收发器（UART）。

> 原文注意：此开发板配置不声称适用于实际的 `ti_lm3s6965` 硬件系统或任何其他硬件系统。

<a id="hardware"></a>

## 4.2\_硬件与支持特性

<a id="supported-features"></a>

<a id="qemu_cortex_m3-hw-features"></a>

`qemu_cortex_m3` 支持下表列出的硬件特性（Supported Features）。

“片上（on-chip）”表示特性集成于 SoC，“板上（on-board）”表示特性位于开发板。启用／禁用两列分别保留官方页面的实例计数（Enabled/Disabled Instance Count）；数字链接指向开发板或 SoC 设备树源码（DTS）中相应状态的第一个实例。兼容字符串（Compatible String，如 `vnd,foo`）链接指向对应设备树绑定文档。RAM 指随机存取存储器，Flash 指闪存；KiB、MiB 分别为二进制千字节、兆字节。

<a id="qemu_cortex_m3-qemu_cortex_m3/ti_lm3s6965-hw-features-section"></a>

<a id="qemu_cortex_m3-qemu_cortex_m3/ti_lm3s6965-hw-features-panel"></a>

<a id="qemu_cortex_m3-qemu_cortex_m3/ti_lm3s6965-hw-features-memory"></a>

<a id="qemu_cortex_m3-qemu_cortex_m3/ti_lm3s6965-hw-features-table"></a>

### 4.2.1\_目标 `qemu_cortex_m3/ti_lm3s6965`

目标存储容量：RAM 为 64 KiB，Flash 为 256 KiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中央处理器（Central Processing Unit，CPU） | 片上（on-chip） | ARM Cortex-M3 中央处理器（CPU） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/lm3s6965.dtsi?plain=1#L12) | — | [`arm,cortex-m3`](../cpu_arm_riscv_binding_reference/P021_arm_cortex-m3.md#std-dtcompatible-arm-cortex-m3) |
| 时钟控制（Clock Control） | 片上（on-chip） | 通用固定频率时钟提供者（Generic Fixed-rate Clock Provider） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/lm3s6965.dtsi?plain=1#L24) | — | [`fixed-clock`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/fixed-clock.html#std-dtcompatible-fixed-clock) |
| 以太网（Ethernet） | 片上（on-chip） | TI Stellaris 以太网（Ethernet） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/lm3s6965.dtsi?plain=1#L67) | — | [`ti,stellaris-ethernet`](../ethernet_synopsys_st_xilinx_binding_reference/P014_ti_stellaris-ethernet.md#std-dtcompatible-ti-stellaris-ethernet) |
| 闪存控制器（Flash Controller） | 片上（on-chip） | TI Stellaris 闪存控制器（Flash Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/lm3s6965.dtsi?plain=1#L31) | — | [`ti,stellaris-flash-controller`](../flash_renesas_st_ti_binding_reference/P033_ti_stellaris-flash-controller.md#std-dtcompatible-ti-stellaris-flash-controller) |
| 通用输入输出与接针（GPIO & Headers） | 片上（on-chip） | TI Stellaris 通用输入输出（GPIO） | [7](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/lm3s6965.dtsi?plain=1#L75) | — | [`ti,stellaris-gpio`](../gpio_ti_xilinx_sdl_binding_reference/P018_ti_stellaris-gpio.md#std-dtcompatible-ti-stellaris-gpio) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | — | [`arm,v7m-nvic`](../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic) |
| 存储技术设备（Memory Technology Device，MTD） | 片上（on-chip） | 闪存节点（Flash Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/lm3s6965.dtsi?plain=1#L37) | — | [`soc-nv-flash`](../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| 串行控制器（Serial Controller） | 片上（on-chip） | TI Stellaris 通用异步收发器（UART） | [3](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/lm3s6965.dtsi?plain=1#L43) | — | [`ti,stellaris-uart`](../uart_ti_wch_virtual_binding_reference/P003_ti_stellaris-uart.md#std-dtcompatible-ti-stellaris-uart) |
| 静态随机存取存储器（Static Random-Access Memory，SRAM） | 片上（on-chip） | 通用片上 SRAM（Generic On-chip SRAM） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/lm3s6965.dtsi?plain=1#L19) | — | [`mmio-sram`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sram/mmio-sram.html#std-dtcompatible-mmio-sram) |
| 定时器（Timer） | 片上（on-chip） | ARMv7-M 系统节拍（System Tick） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | — | [`arm,armv7m-systick`](../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick) |

<a id="devices"></a>

## 4.3\_设备

<a id="system-clock"></a>

### 4.3.1\_系统时钟

此配置使用 12 MHz 的系统时钟频率（System Clock Frequency）。

<a id="serial-port"></a>

### 4.3.2\_串口

此配置通过CPU 的 UART0 使用单个串行通信通道（Serial Communication Channel）。

如果启用下文所述的串行线路互联网协议（Serial Line Internet Protocol，SLIP）网络，将另用一个串口承载它。

<a id="known-problems-or-limitations"></a>

### 4.3.3\_已知问题与限制

以下平台特性不受支持：

- 通过可选内存保护单元（MPU）实现内存保护。不过，使用就地执行（Execute In Place，XIP）内核，实际上可对只读存储器（ROM）中的代码段／只读数据段（TEXT/RODATA）提供写保护。
- 地址 `0x1FFF0000-0x1FFFFFFF` 范围内的 SRAM。
- 写入硬件闪存（Flash Memory）。

<a id="programming-and-debugging"></a>

## 4.4\_编程与调试

`qemu_cortex_m3` 支持以下运行器（Runner）及对应 west 命令：

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

可用此配置在 QEMU 仿真环境中运行基本 Zephyr 应用及内核测试。以下以[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)为例，从 Zephyr 仓库根目录执行（代码注释 `From the root of the zephyr repository` 也表示这一位置）：

```shell
# From the root of the zephyr repository
west build -b qemu_cortex_m3 samples/synchronization
west build -t run
```

这会构建包含同步示例应用的镜像（Image），使用 QEMU 启动，并显示以下控制台输出（Console Output）：

```text
***** BOOTING ZEPHYR OS v1.8.99 - BUILD: Jun 27 2017 13:09:26 *****
threadA: Hello World from arm!
threadB: Hello World from arm!
threadA: Hello World from arm!
threadB: Hello World from arm!
threadA: Hello World from arm!
threadB: Hello World from arm!
threadA: Hello World from arm!
threadB: Hello World from arm!
threadA: Hello World from arm!
threadB: Hello World from arm!
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

> 译注：输出是官方页面给出的示例，版本字符串按原样保留；本次翻译没有运行固件或重新生成这些输出。

<a id="debugging"></a>

### 4.4.1\_调试

详细概述参见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

<a id="networking"></a>

### 4.4.2\_网络

此开发板支持通过仿真串口使用 SLIP 网络（`CONFIG_NET_SLIP_TAP=y`），配置方法见[QEMU 联网](../networking/P009_QEMU联网概览.md#networking-with-qemu)。

也可以使用 QEMU 内置以太网适配器连接宿主系统；这种方式比 SLIP 更快，也是优先推荐的方式，详见[QEMU 以太网联网](../networking/P010_QEMU以太网联网.md#networking-with-eth-qemu)。

<a id="references"></a>

## 4.5\_参考资料

1. Joseph Yiu 著《ARM Cortex-M3 权威指南》，第二版（The Definitive Guide to the ARM Cortex-M3, Second Edition by Joseph Yiu (ISBN 978-0-12-382090-7)）。
2. ARM 架构技术参考手册（ARMv7-M Architecture Technical Reference Manual (ARM DDI 0403D ID021310)）。
3. ARM 架构过程调用标准（Procedure Call Standard for the ARM Architecture (ARM IHI 0042E, current through ABI release 2.09, 2012/11/30)）。
4. Cortex-M3 r2p1 版技术参考手册（Cortex-M3 Revision r2p1 Technical Reference Manual (ARM DDI 0337I ID072410)）。
5. Cortex-M3 器件通用用户指南（Cortex-M3 Devices Generic User Guide (ARM DUI 0052A ID121610)）。

---

[上一章](P003_QEMU_Cortex_M0仿真开发板.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P005_QEMU_Cortex_R5仿真开发板.md)
