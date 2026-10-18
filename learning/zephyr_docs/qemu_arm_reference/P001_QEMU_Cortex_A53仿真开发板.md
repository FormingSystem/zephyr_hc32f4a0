---
id: learning.zephyr-docs.qemu-arm-reference.page-1
title: QEMU_Cortex_A53仿真开发板
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/cortex_a53/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_QEMU\_Cortex\_A53仿真开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/cortex_a53/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="qemu_cortex_a53"></a>

## 1.1\_开发板概况

名称：`qemu_cortex_a53`。厂商：[ARM Ltd.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=arm)。维护状态：持续维护（Maintained）。架构（Architecture）：[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)；片上系统（SoC）：[qemu_cortex_a53](https://docs.zephyrproject.org/latest/boards/index.html#soc=qemu_cortex_a53)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/cortex_a53)。

<a id="overview"></a>

此开发板配置使用 QEMU 仿真（Emulation）通用 Cortex-A53 硬件平台。配置支持 ARM Cortex-A53 中央处理器（CPU）以及以下设备：

- GIC-400 中断控制器（Interrupt Controller）。
- ARM 架构定时器（Architected Timer）。
- PL011 通用异步收发器控制器（UART Controller）。

<a id="hardware"></a>

## 1.2\_硬件与支持特性

<a id="supported-features"></a>

<a id="qemu_cortex_a53-hw-features"></a>

`qemu_cortex_a53` 支持下表列出的硬件特性（Supported Features）。

“片上（on-chip）”表示特性集成于 SoC，“板上（on-board）”表示特性位于开发板。启用／禁用两列分别保留官方页面的实例计数（Enabled/Disabled Instance Count）；数字链接指向开发板或 SoC 设备树源码（DTS）中相应状态的第一个实例。兼容字符串（Compatible String，如 `vnd,foo`）链接指向对应设备树绑定文档。RAM 指随机存取存储器，Flash 指闪存；KiB、MiB 分别为二进制千字节、兆字节。

> 译注：原文概述写 GIC-400，而下方自动生成的设备树特性表写 GICv3；两处均按原文保留。

<a id="qemu_cortex_a53-qemu_cortex_a53/qemu_cortex_a53-hw-features-section"></a>

<a id="qemu_cortex_a53-qemu_cortex_a53/qemu_cortex_a53-hw-features-panel"></a>

<a id="qemu_cortex_a53-qemu_cortex_a53/qemu_cortex_a53-hw-features-memory"></a>

<a id="qemu_cortex_a53-qemu_cortex_a53/qemu_cortex_a53-hw-features-table"></a>

### 1.2.1\_目标 `qemu_cortex_a53/qemu_cortex_a53`

目标存储容量：RAM 为 128 MiB，Flash 为 64 MiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中央处理器（Central Processing Unit，CPU） | 片上（on-chip） | ARM Cortex-A53 中央处理器（CPU） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L31) | — | [`arm,cortex-a53`](../cpu_arm_riscv_binding_reference/P008_arm_cortex-a53.md#std-dtcompatible-arm-cortex-a53) |
| 时钟控制（Clock Control） | 片上（on-chip） | 通用固定频率时钟提供者（Generic Fixed-rate Clock Provider） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L61) | — | [`fixed-clock`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/fixed-clock.html#std-dtcompatible-fixed-clock) |
| 显示（Display） | 板上（on-board） | QEMU RAM 帧缓冲显示设备（Framebuffer Display Device） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L278) | — | [`qemu,ramfb`](../display_panel_renesas_sharp_binding_reference/P005_qemu_ramfb.md#std-dtcompatible-qemu-ramfb) |
| 以太网（Ethernet） | 板上（on-board） | Intel E1000 以太网控制器（Ethernet Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L304) | — | [`intel,e1000`](../ethernet_mac_mdio_binding_reference/P010_intel_e1000.md#std-dtcompatible-intel-e1000) |
| 固件（Firmware） | 板上（on-board） | QEMU 固件配置接口 fw_cfg，采用内存映射输入输出传输（MMIO Transport） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L261) | — | [`qemu,fw-cfg-mmio`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/firmware/qemu%2Cfw-cfg-mmio.html#std-dtcompatible-qemu-fw-cfg-mmio) |
| 输入（Input） | 板上（on-board） | VIRTIO 输入设备（Input Device） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L296) | — | [`virtio,input`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/virtio%2Cinput.html#std-dtcompatible-virtio-input) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | ARM 通用中断控制器第3版（Generic Interrupt Controller v3，GICv3） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L74) | — | [`arm,gic-v3`](../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | GIC v3 中断转换服务（Interrupt Translation Service，ITS） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L84) | — | [`arm,gic-v3-its`](../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its) |
| 高速外设互连（Peripheral Component Interconnect Express，PCIe） | 片上（on-chip） | 采用增强配置访问机制（Enhanced Configuration Access Mechanism，ECAM）模式的 PCIe 控制器 | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L110) | — | [`pci-host-ecam-generic`](../pcie_memory_virtualization_binding_reference/P008_pci-host-ecam-generic.md#std-dtcompatible-pci-host-ecam-generic) |
| 电源管理 CPU 操作（Power Management CPU Operations） | 板上（on-board） | 电源状态协调接口（Power State Coordination Interface，PSCI）0.2版 | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L15) | — | [`arm,psci-0.2`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2) |
| 串行控制器（Serial Controller） | 片上（on-chip） | ARM PL011 通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L91) | — | [`arm,pl011`](../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011) |
| 静态随机存取存储器（Static Random-Access Memory，SRAM） | 板上（on-board） | 通用片上 SRAM（Generic On-chip SRAM） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L31) | — | [`mmio-sram`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sram/mmio-sram.html#std-dtcompatible-mmio-sram) |
| 定时器（Timer） | 片上（on-chip） | 各处理器核心的 ARM 架构定时器（Architected Timer） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L48) | — | [`arm,armv8-timer`](../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer) |
| Virtio 虚拟输入输出（Virtual I/O） | 板上（on-board） | 基于内存映射输入输出（Memory-Mapped I/O，MMIO）的 VIRTIO | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L57) | [31](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L36) | [`virtio,mmio`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/virtio/virtio%2Cmmio.html#std-dtcompatible-virtio-mmio) |

<a id="qemu_cortex_a53-qemu_cortex_a53/qemu_cortex_a53/smp-hw-features-section"></a>

<a id="qemu_cortex_a53-qemu_cortex_a53/qemu_cortex_a53/smp-hw-features-panel"></a>

<a id="qemu_cortex_a53-qemu_cortex_a53/qemu_cortex_a53/smp-hw-features-memory"></a>

<a id="qemu_cortex_a53-qemu_cortex_a53/qemu_cortex_a53/smp-hw-features-table"></a>

### 1.2.2\_目标 `qemu_cortex_a53/qemu_cortex_a53/smp`

目标存储容量：RAM 为 128 MiB，Flash 为 64 MiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中央处理器（Central Processing Unit，CPU） | 片上（on-chip） | ARM Cortex-A53 中央处理器（CPU） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L31) | — | [`arm,cortex-a53`](../cpu_arm_riscv_binding_reference/P008_arm_cortex-a53.md#std-dtcompatible-arm-cortex-a53) |
| 时钟控制（Clock Control） | 片上（on-chip） | 通用固定频率时钟提供者（Generic Fixed-rate Clock Provider） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L61) | — | [`fixed-clock`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/fixed-clock.html#std-dtcompatible-fixed-clock) |
| 显示（Display） | 板上（on-board） | QEMU RAM 帧缓冲显示设备（Framebuffer Display Device） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L278) | — | [`qemu,ramfb`](../display_panel_renesas_sharp_binding_reference/P005_qemu_ramfb.md#std-dtcompatible-qemu-ramfb) |
| 以太网（Ethernet） | 板上（on-board） | Intel E1000 以太网控制器（Ethernet Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L304) | — | [`intel,e1000`](../ethernet_mac_mdio_binding_reference/P010_intel_e1000.md#std-dtcompatible-intel-e1000) |
| 固件（Firmware） | 板上（on-board） | QEMU 固件配置接口 fw_cfg，采用内存映射输入输出传输（MMIO Transport） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L261) | — | [`qemu,fw-cfg-mmio`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/firmware/qemu%2Cfw-cfg-mmio.html#std-dtcompatible-qemu-fw-cfg-mmio) |
| 输入（Input） | 板上（on-board） | VIRTIO 输入设备（Input Device） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L296) | — | [`virtio,input`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/virtio%2Cinput.html#std-dtcompatible-virtio-input) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | ARM 通用中断控制器第3版（Generic Interrupt Controller v3，GICv3） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L74) | — | [`arm,gic-v3`](../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | GIC v3 中断转换服务（Interrupt Translation Service，ITS） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L84) | — | [`arm,gic-v3-its`](../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its) |
| 高速外设互连（Peripheral Component Interconnect Express，PCIe） | 片上（on-chip） | 采用增强配置访问机制（Enhanced Configuration Access Mechanism，ECAM）模式的 PCIe 控制器 | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L110) | — | [`pci-host-ecam-generic`](../pcie_memory_virtualization_binding_reference/P008_pci-host-ecam-generic.md#std-dtcompatible-pci-host-ecam-generic) |
| 电源管理 CPU 操作（Power Management CPU Operations） | 板上（on-board） | 电源状态协调接口（Power State Coordination Interface，PSCI）0.2版 | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L15) | — | [`arm,psci-0.2`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2) |
| 串行控制器（Serial Controller） | 片上（on-chip） | ARM PL011 通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L91) | — | [`arm,pl011`](../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011) |
| 静态随机存取存储器（Static Random-Access Memory，SRAM） | 板上（on-board） | 通用片上 SRAM（Generic On-chip SRAM） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L31) | — | [`mmio-sram`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sram/mmio-sram.html#std-dtcompatible-mmio-sram) |
| 定时器（Timer） | 片上（on-chip） | 各处理器核心的 ARM 架构定时器（Architected Timer） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-a53.dtsi?plain=1#L48) | — | [`arm,armv8-timer`](../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer) |
| Virtio 虚拟输入输出（Virtual I/O） | 板上（on-board） | 基于内存映射输入输出（Memory-Mapped I/O，MMIO）的 VIRTIO | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L57) | [31](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_a53/qemu_cortex_a53.dts?plain=1#L36) | [`virtio,mmio`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/virtio/virtio%2Cmmio.html#std-dtcompatible-virtio-mmio) |

<a id="devices"></a>

## 1.3\_设备

<a id="system-clock"></a>

### 1.3.1\_系统时钟

此配置使用 62.5 MHz 的系统时钟频率（System Clock Frequency）。

<a id="serial-port"></a>

### 1.3.2\_串口

此配置通过CPU 的 UART0 使用单个串行通信通道（Serial Communication Channel）。

<a id="known-problems-or-limitations"></a>

### 1.3.3\_已知问题与限制

以下平台特性不受支持：

- 写入硬件闪存（Flash Memory）。

<a id="programming-and-debugging"></a>

## 1.4\_编程与调试

`qemu_cortex_a53` 支持以下运行器（Runner）及对应 west 命令：

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

可用此配置在 QEMU 仿真环境中运行基本 Zephyr 应用及内核测试。以下以[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)为例，从 Zephyr 仓库根目录执行（代码注释 `From the root of the zephyr repository` 也表示这一位置）：

```shell
# From the root of the zephyr repository
west build -b qemu_cortex_a53 samples/synchronization
west build -t run
```

这会构建包含同步示例应用的镜像（Image），使用 QEMU 启动，并显示以下控制台输出（Console Output）：

```text
***** Booting Zephyr OS build zephyr-v2.0.0-1657-g99d310da48e5 *****
threadA: Hello World from qemu_cortex_a53!
threadB: Hello World from qemu_cortex_a53!
threadA: Hello World from qemu_cortex_a53!
threadB: Hello World from qemu_cortex_a53!
threadA: Hello World from qemu_cortex_a53!
threadB: Hello World from qemu_cortex_a53!
threadA: Hello World from qemu_cortex_a53!
threadB: Hello World from qemu_cortex_a53!
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

> 译注：输出是官方页面给出的示例，版本字符串按原样保留；本次翻译没有运行固件或重新生成这些输出。

<a id="debugging"></a>

### 1.4.1\_调试

详细概述参见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

<a id="networking"></a>

### 1.4.2\_网络

此开发板支持使用 QEMU 内置以太网适配器连接宿主系统，详见[QEMU 以太网联网](../networking/P010_QEMU以太网联网.md#networking-with-eth-qemu)。

也可以通过仿真串口使用 SLIP 网络。不过，此开发板仅支持一个 UART，因此必须禁用日志（Logging）、命令行（Shell）等子系统；所以这种方式不直接受支持。

<a id="references"></a>

## 1.5\_参考资料

1. ARM Cortex-A 系列：ARMv8-A 程序员指南（(ID050815) ARM® Cortex®-A Series - Programmer’s Guide for ARMv8-A）。
2. Arm 架构参考手册：Armv8-A 架构配置（(ID070919) Arm® Architecture Reference Manual - Armv8, for Armv8-A architecture profile）。
3. 应用笔记：ARMv8-A 处理器裸机启动代码（(ARM DAI 0527A) Application Note Bare-metal Boot Code for ARMv8-A Processors）。
4. AArch64 异常与中断处理（AArch64 Exception and Interrupt Handling）。
5. ARMv8-A 基础（Fundamentals of ARMv8-A）。

---

[本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P002_QEMU_Cortex_A72仿真开发板.md)
