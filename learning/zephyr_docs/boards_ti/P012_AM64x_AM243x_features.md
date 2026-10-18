---
id: learning.zephyr-docs.boards-ti.page-12
title: AM64x AM243x features
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ti/common/doc/k3/am64x-am243x-features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="am64x-am243x-features"></a>

# 第12章\_AM64x／AM243x功能（Features）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ti/common/doc/k3/am64x-am243x-features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

AM64x／AM243x系列SoC最多支持两个通常运行于1 GHz的Cortex-A53核，仅AM64x提供；最多四个通常运行于800 MHz的Cortex-R5F核；以及一个通常运行于400 MHz的Cortex-M4F核。由于两系列的区别在于是否存在Cortex-A核，Zephyr代码将它们统称为AM64x。AM243x用户不适用涉及Cortex-A核的内容，但共享文档中有时仍会包含这些说明。

Arm核及外设划分到主域（MAIN Domain）及微控制器域（MCU Domain），其中只有Cortex-M4F核位于MCU域。默认情况下两个域可以交互，也可配置为相互隔离。

下面列出部分功能。目前Zephyr尚未支持所有外设：


- 最多两个Arm Cortex-A53核
- 最多两个双核Cortex-R5F集群（Cluster）
- 一个Cortex-M4F核
- 2 MiB内部SRAM
- 通用输入输出（GPIO）
- 模数转换器（ADC）
- 通用异步收发器（UART）
- 串行外设接口（SPI）
- 集成电路间总线（I2C）
- 多个定时器（Timer）
- 多个看门狗（Watchdog）
- CAN-FD
- 以太网（Ethernet）
- 通用串行总线（USB）
- 高速外围组件互连（PCIe）
- 外部(LP)DDR4 RAM接口
- DMSC，集中式电源及资源管理
- 密码运算加速（Crypto Acceleration）
- 安全启动（Secure Boot）

## 译注

本页为共用硬件功能概览，硬件具备某外设不等于Zephyr已支持；MAIN与MCU域默认互通，可配置隔离。

---

[上一章](P011_The_AM64x_AM243x_bootflow.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_MCU_SDK.md)
