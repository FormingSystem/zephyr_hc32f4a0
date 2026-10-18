---
id: learning.zephyr-docs.adc_reference.adcdirectory-65
title: ADC驱动头文件目录
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dir_62d9a819ff274ddc8f9299d578f6ebce.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第65章\_ADC驱动头文件目录

原文：[dir_62d9a819ff274ddc8f9299d578f6ebce](https://docs.zephyrproject.org/latest/doxygen/html/dir_62d9a819ff274ddc8f9299d578f6ebce.html)。读取日期：2026-10-13，`latest`。

本页对应官方 `zephyr/drivers/adc` 目录参考，列出其12个头文件。模数转换器（Analog-to-Digital Converter，ADC）的应用程序接口（Application Programming Interface，API）与设备树（Devicetree）常量在前文分别说明；这里保留官方目录的全部文件入口和附带简述。

## 65.1\_文件列表

本目录列出的头文件参考与源码均已翻译，使用本地相对链接。没有简述的条目按原目录范围保留，不凭文件名扩写为完整接口说明。

| 头文件 | 参考与源码入口 | 官方简述中文译文 |
| --- | --- | --- |
| `adc_emul.h` | [参考](P061_ADC仿真器头文件参考.md) · [源码](P062_ADC仿真器头文件源码.md) | 仿真ADC的后端API。 |
| `adc_npcx_threshold.h` | [参考](P055_NPCXADC阈值参数头文件参考.md) · [源码](P056_NPCXADC阈值参数头文件源码.md) | 原目录未附加简述。 |
| `adc_npcx_v2t.h` | [参考](P057_NPCXADC温度参数头文件参考.md) · [源码](P058_NPCXADC温度参数头文件源码.md) | 原目录未附加简述。 |
| `ads126x.h` | [参考](P043_ADS126x扩展头文件参考.md) · [源码](P044_ADS126x扩展头文件源码.md) | Texas Instruments（德州仪器）ADS126X ADC驱动API。 |
| `ads131m02.h` | [参考](P045_ADS131M02扩展头文件参考.md) · [源码](P046_ADS131M02扩展头文件源码.md) | ADS131M02 ADC扩展API头文件。 |
| `ads1x4s0x.h` | [参考](P047_ADS1x4S0x扩展头文件参考.md) · [源码](P048_ADS1x4S0x扩展头文件源码.md) | ADS1x4s0x ADC扩展API头文件。 |
| `current_sense_amplifier.h` | [参考](P067_电流检测放大器扩展头文件参考.md) · [源码](P068_电流检测放大器扩展头文件源码.md) | 电流检测放大器（Current Sense Amplifier）的扩展ADC API头文件。 |
| `current_sense_shunt.h` | [参考](P069_电流检测分流器扩展头文件参考.md) · [源码](P070_电流检测分流器扩展头文件源码.md) | 电流检测分流器（Current Sense Shunt）的扩展ADC API头文件。 |
| `infineon_autanalog_sar.h` | [参考](P075_Infineon自主模拟SAR驱动头文件参考.md) · [源码](P076_Infineon自主模拟SAR驱动头文件源码.md) | Infineon自主模拟（Autonomous Analog，AutAnalog）逐次逼近寄存器（Successive Approximation Register，SAR）ADC驱动的公共扩展API。 |
| `lmp90xxx.h` | [参考](P073_LMP90xxx扩展头文件参考.md) · [源码](P074_LMP90xxx扩展头文件源码.md) | LMP90xxx ADC扩展API头文件。 |
| `mcp356xr.h` | [参考](P051_MCP356xR扩展头文件参考.md) · [源码](P052_MCP356xR扩展头文件源码.md) | 原目录未附加简述。 |
| `voltage_divider.h` | [参考](P071_分压器扩展头文件参考.md) · [源码](P072_分压器扩展头文件源码.md) | 分压器（Voltage Divider）的扩展API头文件。 |

## 65.2\_阅读范围

公共ADC主头文件位于上一级的 `zephyr/drivers/adc.h`，见[公共头文件参考](P063_ADC公共头文件参考.md)。本目录中的器件或测量电路扩展不替代该公共接口。

本页及所列头文件的参考、源码页均已翻译。整站其余待译页面继续记录在[全站进度](../PROGRESS.md)中。

---

[上一章：ADC公共头文件源码](P064_ADC公共头文件源码.md) · [下一章：ADC设备树头文件目录](P066_ADC设备树头文件目录.md) · [返回大纲](大纲.md)
