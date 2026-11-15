---
id: learning.zephyr-docs.driver_samples.page-63
title: RISC_V_AIA中断示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/interrupt_controller/intc_riscv_aia/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="riscv-aia-uart-echo"></a>

# 第63章\_RISC\_V\_AIA中断示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/interrupt_controller/intc_riscv_aia/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 63.1 概述（Overview）

本示例用通用异步收发器（Universal Asynchronous Receiver-Transmitter，UART）中断演示RISC-V高级中断架构（Advanced Interrupt Architecture，AIA）的中断传递。

中断依次经过：

1. UART。
2. 高级平台级中断控制器（Advanced Platform-Level Interrupt Controller，APLIC）。
3. 消息信号中断（Message-Signaled Interrupt，MSI）。
4. 传入消息信号中断控制器（Incoming MSI Controller，IMSIC）。
5. 中央处理器（Central Processing Unit，CPU）。

示例配置APLIC中断源路由，通过MSI把UART中断路由到IMSIC，并在UART中断处理函数中回显输入字符。

<a id="requirements"></a>

## 63.2 要求（Requirements）

本示例面向`qemu_riscv32/qemu_virt_riscv32/aia-imsic`开发板。该板提供使用MSI传递模式的APLIC与IMSIC中断控制器。

<a id="configuration"></a>

## 63.3 配置（Configuration）

示例配置如下：

- 开发板：`qemu_riscv32/qemu_virt_riscv32/aia-imsic`。
- UART中断请求（Interrupt Request，IRQ）：APLIC中断源10。
- 目标外部中断标识（External Interrupt Identity，EIID）：32。
- 模式：边沿触发的MSI传递。

> 译注——实现跟踪：这些数值是原页面描述的板级配置。当前官方[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/interrupt_controller/intc_riscv_aia/src/main.c)从设备树选定的控制台节点读取UART地址、寄存器步移、IRQ及标志，调用`IRQ_CONNECT()`和`irq_enable()`，由AIA驱动处理控制器配置。应用并非在代码里自行硬编码全部APLIC／IMSIC寄存器；中断处理函数读取接收字符并输出带ISR次数的记录。

<a id="building-and-running"></a>

## 63.4 构建与运行（Building and Running）

在Zephyr源码根目录，为AIA IMSIC QEMU RISC-V开发板构建并运行：

```sh
west build -b qemu_riscv32/qemu_virt_riscv32/aia-imsic samples/drivers/interrupt_controller/intc_riscv_aia
west build -t run
```

在QEMU控制台输入字符即可看到回显。按`Ctrl+A`，再按`X`退出QEMU。


对应官方文档源码：[samples/drivers/interrupt_controller/intc_riscv_aia/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/interrupt_controller/intc_riscv_aia/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/interrupt_controller/intc_riscv_aia/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/interrupt_controller/intc_riscv_aia/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P062_中断控制器示例目录.md) · [返回大纲](大纲.md) · [下一章](P064_RISC_V_AIA多处理器中断示例.md)
