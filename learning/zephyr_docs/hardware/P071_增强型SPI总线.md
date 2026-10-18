---
id: learning.zephyr-docs.hardware.bus-1
title: 增强型SPI总线
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/espi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="espi-api"></a>

# 第71章\_增强型SPI总线

原文：[Enhanced Serial Peripheral Interface (eSPI) Bus](https://docs.zephyrproject.org/latest/hardware/peripherals/espi.html)。读取日期：2026-10-13，`latest`。

## 71.1\_增强型SPI

**增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）**是以 **串行外设接口（Serial Peripheral Interface，SPI）**为基础的串行总线。原文描述其四线接口包括接收、发送、时钟和目标选择信号，提供单线、双线和四线 **输入／输出（Input/Output，I/O）**三种配置。

原页列出的技术改进包括：较低信号电压（1.8 V对比3.3 V）、较少引脚，以及两倍频率（66 MHz对比33 MHz）。这些是原页用于比较接口演进的参数，不表示任意控制器都以最高频率运行。

由于这些增强特性，eSPI用于替代 **低引脚数接口（Low Pin Count，LPC）**、SPI、**系统管理总线（System Management Bus，SMBus）**和 **边带信号（Sideband Signals）**。原页将LPC括注写为“lower pin count”，这里采用该接口通用全称，并保留其减少引脚数量的含义。详细信息见[eSPI接口规范](https://downloadmirror.intel.com/27055/327432%20espi_base_specification%20R1-5.pdf)。

## 71.2\_接口与示例

完整 **应用程序编程接口（Application Programming Interface，API）**见[eSPI参考](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html)。[eSPI示例](../driver_samples/P053_eSPI接口示例.md#espi)展示通过eSPI连接目标设备（原文称slave device），并交换 **虚拟线数据包（Virtual Wire Packets）**。本页没有提供接线图或运行命令。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：I3C总线](P070_I3C总线.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：本地互连网络](P072_本地互连网络.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：I3C总线](P070_I3C总线.md) · [下一章：本地互连网络](P072_本地互连网络.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
