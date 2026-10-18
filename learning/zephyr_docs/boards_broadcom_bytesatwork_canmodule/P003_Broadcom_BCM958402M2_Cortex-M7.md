---
id: learning.zephyr-docs.boards-broadcom-bytesatwork-canmodule.page-3
title: Broadcom BCM958402M2 Cortex-M7
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/brcm/bcm958402m2/doc/m7.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="broadcom-bcm958402m2-cortex-m7"></a>

<a id="bcm958402m2-m7"></a>

# 第3章\_博通BCM958402M2（Cortex-M7）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/brcm/bcm958402m2/doc/m7.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

博通`bcm958402m2/bcm58402/m7`开发板采用Viper BCM58402_M7 SoC，提供PCIe卸载引擎（Offload Engine）功能。

<a id="hardware"></a>

## 硬件（Hardware）

`bcm958402m2/bcm58402/m7`是一张PCIe卡，具有以下物理接口：


- PCIe Gen4接口
- RS232通用异步收发器（UART），可选装
- JTAG接口，可选装

<a id="supported-features"></a>

### 支持的功能（Supported Features）

博通`bcm958402m2/bcm58402/m7`开发板配置支持以下硬件功能：

<table>
<tr>
<th>接口（Interface）</th>
<th>控制器（Controller）</th>
<th>驱动／组件（Driver/Component）</th>
</tr>
<tr>
<td>嵌套向量中断控制器（NVIC）</td>
<td>片上（On-Chip）</td>
<td>嵌套向量中断控制器（Nested Vectored Interrupt Controller）</td>
</tr>
<tr>
<td>通用异步收发器（UART）</td>
<td>片上（On-Chip）</td>
<td>兼容UART NS16550</td>
</tr>
</table>

尚未为该开发板启用其他硬件功能。

默认配置位于[boards/brcm/bcm958402m2/bcm958402m2_bcm58402_m7_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/brcm/bcm958402m2/bcm958402m2_bcm58402_m7_defconfig)。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

<a id="flashing"></a>

### 烧录（Flashing）

Zephyr目前不支持板载闪存。开发板通过PCIe接口启动。

<a id="debugging"></a>

### 调试（Debugging）

`bcm958402m2/bcm58402/m7`开发板预留了焊接JTAG连接器的焊盘。也可以通过观察UART控制台输出，测试运行在M7内核上的Zephyr应用。

## 译注

博通板卡的PCIe启动、未启用的硬件功能及可选焊接JTAG接口均依官方页面保留；不能把SoC具有的硬件能力等同于Zephyr已支持的功能。

---

[上一章](P002_Broadcom_BCM958402M2_Cortex-A72.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_Broadcom_Corporation.md)
