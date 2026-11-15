---
id: learning.zephyr-docs.driver_samples.page-64
title: RISC_V_AIA多处理器中断示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/interrupt_controller/intc_riscv_aia_smp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="riscv-aia-smp-uart-echo"></a>

# 第64章\_RISC\_V\_AIA多处理器中断示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/interrupt_controller/intc_riscv_aia_smp/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 64.1 概述（Overview）

本示例演示在对称多处理（Symmetric Multiprocessing，SMP）配置中，使用多个硬件线程（Hardware Thread，Hart）进行RISC-V高级中断架构（Advanced Interrupt Architecture，AIA）的中断传递。

示例展示：

- 多Hart启动，以及各Hart的IMSIC初始化。
- APLIC将消息信号中断（Message-Signaled Interrupt，MSI）路由到特定Hart。
- 通过`GENMSI`向指定Hart注入软件MSI。
- 在Hart之间动态调整中断路由。

IMSIC的外部中断标识（External Interrupt Identity，EIID）使能状态属于各Hart自身。示例将一个初始化线程固定在Hart 1上运行，使两套IMSIC中断文件都启用UART EIID，然后APLIC路由测试才能把任意一个Hart作为目标。

> 译注——术语：APLIC指高级平台级中断控制器（Advanced Platform-Level Interrupt Controller），IMSIC指传入消息信号中断控制器（Incoming MSI Controller）。这里的“中断文件”（Interrupt File）是硬件中断状态与控制寄存器的集合，不是仓库中的磁盘文件。

<a id="requirements"></a>

## 64.2 要求（Requirements）

本示例面向`qemu_riscv32/qemu_virt_riscv32/aia-imsic/smp`开发板。它提供两个Hart，以及工作于MSI传递模式的APLIC和IMSIC中断控制器。

<a id="configuration"></a>

## 64.3 配置（Configuration）

示例配置如下：

- 开发板：`qemu_riscv32/qemu_virt_riscv32/aia-imsic/smp`。
- CPU：2个Hart。
- IMSIC：每个Hart各有一个中断文件，地址分别为`0x24000000`和`0x24001000`。
- APLIC：动态地将中断路由到任意一个Hart。

> 译注——初始化顺序：当前官方[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/interrupt_controller/intc_riscv_aia_smp/src/main.c)先在Hart 0连接并使能IRQ，再创建尚未启动的线程，将其CPU掩码限定为Hart 1并启动。Hart 1调用`riscv_imsic_enable_eiid()`后通过信号量通知主线程；主线程等待就绪再启用UART接收中断，并分别向各Hart注入MSI。接收处理函数读取字符后设置下次中断的目标Hart；UART一次中断可能读出多个已有字符，不能把注释中的“字符交替”理解为所有突发输入都严格一字符一Hart。

<a id="building-and-running"></a>

## 64.4 构建与运行（Building and Running）

在Zephyr源码根目录，为AIA IMSIC SMP QEMU RISC-V开发板构建并运行：

```sh
west build -b qemu_riscv32/qemu_virt_riscv32/aia-imsic/smp samples/drivers/interrupt_controller/intc_riscv_aia_smp
west build -t run
```


对应官方文档源码：[samples/drivers/interrupt_controller/intc_riscv_aia_smp/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/interrupt_controller/intc_riscv_aia_smp/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/interrupt_controller/intc_riscv_aia_smp/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/interrupt_controller/intc_riscv_aia_smp/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P063_RISC_V_AIA中断示例.md) · [返回大纲](大纲.md) · [下一章](P065_时间感知GPIO示例.md)
