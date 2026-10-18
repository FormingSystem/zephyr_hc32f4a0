---
id: learning.zephyr-docs.qemu-catalog-reference.page-3
title: QEMU_X86
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/x86/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_QEMU\_X86

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/x86/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="qemu_x86"></a>

## 3.1\_开发板概况与概述

名称：`qemu_x86`。厂商：[Intel Corporation](https://docs.zephyrproject.org/latest/boards/index.html#vendor=intel)。状态：未积极维护（Not Actively Maintained）。架构（Architecture）：[x86](https://docs.zephyrproject.org/latest/boards/index.html#arch=x86)；片上系统（SoC）：[atom](https://docs.zephyrproject.org/latest/boards/index.html#soc=atom)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/x86)。

<a id="overview"></a>

X86 QEMU 开发板配置用于仿真 X86 架构，支持32位 Atom 级 x86 CPU，以及以下设备：

- 高精度事件定时器（HPET）。
- 高级可编程中断控制器（APIC）。
- NS16550 UART。
- 仿真 PCI 总线上的 E1000 以太网、CAN 和 VirtIO 输入设备。
- 仿真的闪存（Flash）及电可擦可编程只读存储器（EEPROM）。
- QEMU ramfb 帧缓冲显示设备。

`qemu_x86/atom/*` 各变体在同一虚拟机器上使用特定的内存管理配置：无内存管理单元（MMU）、32位页表、禁用内核页表隔离（KPTI）、就地执行（XIP），或重定位后的虚拟地址空间。`qemu_x86_tiny` 使用同一设备树，但 RAM 仅有384 KiB，用于测试按需分页（Demand Paging）。

<a id="hardware"></a>

## 3.2\_硬件

<a id="supported-features"></a>

<a id="qemu_x86-hw-features"></a>

`qemu_x86` 的硬件特性（Supported Features）及图例如下。片上（on-chip）表示集成在 SoC 内，板上（on-board）表示位于开发板。启用／禁用数字保留相应实例数量，链接指向开发板或 SoC 设备树源码（DTS）中该状态的第一个实例；兼容字符串（Compatible String，如 `vnd,foo`）链接指向绑定文档。

CPU 为中央处理器，UART 为通用异步收发器；RAM 为随机存取存储器，Flash 为闪存；KiB、MiB 为二进制千字节和兆字节。

<a id="qemu_x86-qemu_x86/atom-hw-features-section"></a>

<a id="qemu_x86-qemu_x86/atom-hw-features-panel"></a>

<a id="qemu_x86-qemu_x86/atom-hw-features-memory"></a>

<a id="qemu_x86-qemu_x86/atom-hw-features-table"></a>

### 3.2.1\_目标 `qemu_x86/atom`

目标存储容量：RAM 为 32 MiB，Flash 为 4 MiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中央处理器（Central Processing Unit，CPU） | 片上（on-chip） | 通用 x86 QEMU 中央处理器（CPU） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/atom.dtsi?plain=1#L15) | — | [`intel,x86`](../cpu_vendor_multiarc_binding_reference/P015_intel_x86.md#std-dtcompatible-intel-x86) |
| 控制器局域网（Controller Area Network，CAN） | 板上（on-board） | Kvaser PCIcan 设备 | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/x86/../common/qemu_x86.dtsi?plain=1#L71) | — | [`kvaser,pcican`](../can_adi_atmel_nxp_binding_reference/P011_kvaser_pcican.md#std-dtcompatible-kvaser-pcican) |
| 显示（Display） | 板上（on-board） | QEMU RAM 帧缓冲显示设备（Framebuffer Display Device） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/x86/../common/qemu_x86.dtsi?plain=1#L167) | — | [`qemu,ramfb`](../display_panel_renesas_sharp_binding_reference/P005_qemu_ramfb.md#std-dtcompatible-qemu-ramfb) |
| 以太网（Ethernet） | 板上（on-board） | Intel E1000 以太网控制器（Ethernet Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/x86/../common/qemu_x86.dtsi?plain=1#L84) | — | [`intel,e1000`](../ethernet_mac_mdio_binding_reference/P010_intel_e1000.md#std-dtcompatible-intel-e1000) |
| 固件（Firmware） | 板上（on-board） | QEMU 固件配置接口 fw_cfg，采用输入输出端口传输（I/O Port Transport） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/x86/../common/qemu_x86.dtsi?plain=1#L150) | — | [`qemu,fw-cfg-ioport`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/firmware/qemu%2Cfw-cfg-ioport.html#std-dtcompatible-qemu-fw-cfg-ioport) |
| 输入（Input） | 板上（on-board） | VIRTIO 输入设备（Input Device） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/x86/../common/qemu_x86.dtsi?plain=1#L107) | — | [`virtio,input`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/virtio%2Cinput.html#std-dtcompatible-virtio-input) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | Intel I/O 高级可编程中断控制器（Advanced Programmable Interrupt Controller，APIC） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/atom.dtsi?plain=1#L22) | — | [`intel,ioapic`](../multiarch_interrupt_binding_reference/P001_intel_ioapic.md#std-dtcompatible-intel-ioapic) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | 本地高级可编程中断控制器（Local APIC） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/atom.dtsi?plain=1#L30) | — | [`intel,loapic`](../multiarch_interrupt_binding_reference/P002_intel_loapic.md#std-dtcompatible-intel-loapic) |
| 多功能设备（Multi-Function Device，MFD） | 片上（on-chip） | Motorola MC146818 多功能设备（MFD） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/atom.dtsi?plain=1#L80) | — | [`motorola,mc146818-mfd`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/motorola%2Cmc146818-mfd.html#std-dtcompatible-motorola-mc146818-mfd) |
| 存储技术设备（Memory Technology Device，MTD） | 板上（on-board） | 闪存节点（Flash Node） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/x86/../common/qemu_x86.dtsi?plain=1#L35) | — | [`soc-nv-flash`](../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| 高速外设互连（Peripheral Component Interconnect Express，PCIe） | 板上（on-board） | 通用 PCIe 主控制器（Host Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/x86/../common/qemu_x86.dtsi?plain=1#L64) | — | [`pcie-controller`](../pcie_memory_virtualization_binding_reference/P009_pcie-controller.md#std-dtcompatible-pcie-controller) |
| 实时时钟／计数器（RTC） | 片上（on-chip） | 兼容 Motorola MC146818 的实时时钟（原文 Real Timer Clock） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/atom.dtsi?plain=1#L84) | — | [`motorola,mc146818`](../microchip_microcrystal_nxp_rtc_binding_reference/P009_motorola_mc146818.md#std-dtcompatible-motorola-mc146818) |
| 串行控制器（Serial Controller） | 片上（on-chip） | ns16550 通用异步收发器（UART） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/atom.dtsi?plain=1#L49) | — | [`ns16550`](../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550) |
| 定时器（Timer） | 片上（on-chip） | 高精度事件定时器（High-Precision Event Timer，HPET） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/x86/intel/atom.dtsi?plain=1#L71) | — | [`intel,hpet`](../system_timer_binding_reference/P007_intel_hpet.md#std-dtcompatible-intel-hpet) |
| Virtio 虚拟输入输出（Virtual I/O） | 板上（on-board） | 基于外设互连总线（PCI）的 VIRTIO | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/x86/../common/qemu_x86.dtsi?plain=1#L96) | — | [`virtio,pci`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/virtio/virtio%2Cpci.html#std-dtcompatible-virtio-pci) |

<a id="devices"></a>

<a id="hpet-system-clock-support"></a>

### 3.2.2\_设备与系统时钟

此配置使用25 MHz的HPET时钟频率。

<a id="serial-port"></a>

此配置使用单个串行通信通道，NS16550 串口驱动以轮询模式（Polling Mode）工作。若需改变此行为，可启用 `UART_INTERRUPT_DRIVEN` Kconfig 选项，让系统采用中断驱动（Interrupt-driven）方式。如果启用下文的串行线路互联网协议（SLIP）网络，将另用一个串口承载它。

<a id="known-problems-or-limitations"></a>

以下平台特性不受支持：

- 隔离内存区域（Isolated Memory Regions）。
- 直接存储器访问（DMA）模式串口。
- 串行外设接口（SPI）闪存。
- 通用输入输出（GPIO）。
- 集成电路间总线（I2C）。
- 以太网（Ethernet）。
- 监管者模式执行保护（Supervisor Mode Execution Protection，SMEP）。

> 译注：原页概述和特性表列出以太网设备，后文也介绍以太网联网，但限制列表仍包含以太网；此处保留原文各处信息，不自行消除该差异。

<a id="programming-and-debugging"></a>

## 3.3\_编程与调试

原页列出 `qemu_x86` 支持的运行器（Runner）及关联 west 命令：

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

应用可按仿真开发板的通常方式构建和运行，详见[构建应用](../application/P001_应用开发.md#build-an-application)和[运行应用](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)。

<a id="flashing"></a>

虽然该开发板是仿真的，不能实际“烧写”（Flash），但可用此配置运行基本 Zephyr 应用及内核测试。

以[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)为例，下面的命令从 Zephyr 仓库根目录执行，原代码注释也表示这一位置。

```shell
# From the root of the zephyr repository
west build -b qemu_x86 samples/synchronization
west build -t run
```

这会构建包含同步示例的镜像（Image），使用 QEMU 启动，并显示以下控制台输出：

```text
***** BOOTING ZEPHYR OS v1.8.99 - BUILD: Jun 27 2017 13:09:26 *****
threadA: Hello World from x86!
threadB: Hello World from x86!
threadA: Hello World from x86!
threadB: Hello World from x86!
threadA: Hello World from x86!
threadB: Hello World from x86!
threadA: Hello World from x86!
threadB: Hello World from x86!
threadA: Hello World from x86!
threadB: Hello World from x86!
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

<a id="debugging"></a>

详细概述参见[应用调试](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

<a id="networking"></a>

网络（Networking）：此开发板支持通过仿真串口使用 SLIP 网络（`CONFIG_NET_SLIP_TAP=y`），配置详见[QEMU 联网](../networking/P009_QEMU联网概览.md#networking-with-qemu)。

也可使用 QEMU 内置以太网适配器连接宿主系统；这比 SLIP 更快，也是优先推荐的方式，详见[QEMU 以太网联网](../networking/P010_QEMU以太网联网.md#networking-with-eth-qemu)。

> 译注：命令、日志和版本号按官方示例保留，本次翻译未构建或运行固件。

---

[上一章](P002_QEMU_ARCv2与ARCv3.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P004_QEMU_X86_64位.md)
