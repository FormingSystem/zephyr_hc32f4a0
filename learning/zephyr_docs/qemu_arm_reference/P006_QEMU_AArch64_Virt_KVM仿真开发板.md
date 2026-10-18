---
id: learning.zephyr-docs.qemu-arm-reference.page-6
title: QEMU_AArch64_Virt_KVM仿真开发板
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/kvm_arm64/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_QEMU\_AArch64\_Virt\_KVM仿真开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/kvm_arm64/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="qemu_kvm_arm64"></a>

## 6.1\_开发板概况

名称：`qemu_kvm_arm64`。厂商：[ARM Ltd.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=arm)。维护状态：持续维护（Maintained）。架构（Architecture）：[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)；片上系统（SoC）：[qemu_virt_arm64](https://docs.zephyrproject.org/latest/boards/index.html#soc=qemu_virt_arm64)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/kvm_arm64)。

<a id="overview"></a>

此开发板配置使用 QEMU 在 AArch64 宿主机（Host）上运行基于内核的虚拟机（Kernel-based Virtual Machine，KVM）客户机（Guest）。配置支持 AArch64 Cortex-A CPU，以及 GICv3 中断控制器、ARM 架构定时器（Architected Timer）和 PL011 UART 控制器。

<a id="hardware"></a>

## 6.2\_硬件与支持特性

<a id="supported-features"></a>

<a id="qemu_kvm_arm64-hw-features"></a>

`qemu_kvm_arm64` 支持下表列出的硬件特性（Supported Features）。

“片上（on-chip）”表示特性集成于 SoC，“板上（on-board）”表示特性位于开发板。启用／禁用两列分别保留官方页面的实例计数（Enabled/Disabled Instance Count）；数字链接指向开发板或 SoC 设备树源码（DTS）中相应状态的第一个实例。兼容字符串（Compatible String，如 `vnd,foo`）链接指向对应设备树绑定文档。RAM 指随机存取存储器，Flash 指闪存；KiB、MiB 分别为二进制千字节、兆字节。

<a id="qemu_kvm_arm64-qemu_kvm_arm64/qemu_virt_arm64-hw-features-section"></a>

<a id="qemu_kvm_arm64-qemu_kvm_arm64/qemu_virt_arm64-hw-features-panel"></a>

<a id="qemu_kvm_arm64-qemu_kvm_arm64/qemu_virt_arm64-hw-features-memory"></a>

<a id="qemu_kvm_arm64-qemu_kvm_arm64/qemu_virt_arm64-hw-features-table"></a>

### 6.2.1\_目标 `qemu_kvm_arm64/qemu_virt_arm64`

目标存储容量：RAM 为 128 MiB，Flash 为 64 MiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 时钟控制（Clock Control） | 片上（on-chip） | 通用固定频率时钟提供者（Generic Fixed-rate Clock Provider） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-arm64.dtsi?plain=1#L55) | — | [`fixed-clock`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/fixed-clock.html#std-dtcompatible-fixed-clock) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | ARM 通用中断控制器第3版（Generic Interrupt Controller v3，GICv3） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-arm64.dtsi?plain=1#L68) | — | [`arm,gic-v3`](../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | GIC v3 中断转换服务（Interrupt Translation Service，ITS） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-arm64.dtsi?plain=1#L78) | — | [`arm,gic-v3-its`](../interrupt_fabric_binding_reference/P005_arm_gic-v3-its.md#std-dtcompatible-arm-gic-v3-its) |
| 高速外设互连（Peripheral Component Interconnect Express，PCIe） | 片上（on-chip） | 采用增强配置访问机制（Enhanced Configuration Access Mechanism，ECAM）模式的 PCIe 控制器 | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-arm64.dtsi?plain=1#L104) | — | [`pci-host-ecam-generic`](../pcie_memory_virtualization_binding_reference/P008_pci-host-ecam-generic.md#std-dtcompatible-pci-host-ecam-generic) |
| 电源管理 CPU 操作（Power Management CPU Operations） | 板上（on-board） | 电源状态协调接口（Power State Coordination Interface，PSCI）0.2版 | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/kvm_arm64/qemu_kvm_arm64.dts?plain=1#L16) | — | [`arm,psci-0.2`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2) |
| 串行控制器（Serial Controller） | 片上（on-chip） | ARM PL011 通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-arm64.dtsi?plain=1#L85) | — | [`arm,pl011`](../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011) |
| 静态随机存取存储器（Static Random-Access Memory，SRAM） | 板上（on-board） | 通用片上 SRAM（Generic On-chip SRAM） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/kvm_arm64/qemu_kvm_arm64.dts?plain=1#L30) | — | [`mmio-sram`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sram/mmio-sram.html#std-dtcompatible-mmio-sram) |
| 定时器（Timer） | 片上（on-chip） | 各处理器核心的 ARM 架构定时器（Architected Timer） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/qemu/qemu-virt-arm64.dtsi?plain=1#L42) | — | [`arm,armv8-timer`](../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer) |

<a id="devices"></a>

## 6.3\_设备

<a id="system-clock"></a>

### 6.3.1\_系统时钟

此配置使用宿主机系统时钟频率。

<a id="serial-port"></a>

### 6.3.2\_串口

此配置通过CPU 的 UART0 使用单个串行通信通道（Serial Communication Channel）。

<a id="programming-and-debugging"></a>

## 6.4\_编程与调试

`qemu_kvm_arm64` 支持以下运行器（Runner）及对应 west 命令：

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

此部分参见 [Cortex-A53 开发板说明](P001_QEMU_Cortex_A53仿真开发板.md#programming-and-debugging)。

<a id="debugging"></a>

### 6.4.1\_调试

详细概述参见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

---

[上一章](P005_QEMU_Cortex_R5仿真开发板.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md)
