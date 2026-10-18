---
id: learning.zephyr-docs.adc_reference.adcdirectory-66
title: ADC设备树头文件目录
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dir_1661dc856f6689c520a6419e0ea32218.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第66章\_ADC设备树头文件目录

原文：[dir_1661dc856f6689c520a6419e0ea32218](https://docs.zephyrproject.org/latest/doxygen/html/dir_1661dc856f6689c520a6419e0ea32218.html)。读取日期：2026-10-13，`latest`。

本页对应官方 `zephyr/dt-bindings/adc` 目录参考，列出其23个头文件。模数转换器（Analog-to-Digital Converter，ADC）的应用程序接口（Application Programming Interface，API）与设备树（Devicetree）常量在前文分别说明；这里保留官方目录的全部文件入口和附带简述。

## 66.1\_文件列表

本目录列出的头文件参考与源码均已翻译，使用本地相对链接。没有简述的条目按原目录范围保留，不凭文件名扩写为完整接口说明。

| 头文件 | 参考与源码入口 | 官方简述中文译文 |
| --- | --- | --- |
| `ad4130-adc.h` | [参考](P003_AD4130设备树常量参考.md) · [源码](P004_AD4130设备树常量源码.md) | 原目录未附加简述。 |
| `ad4170-adc.h` | [参考](P005_AD4170设备树常量参考.md) · [源码](P006_AD4170设备树常量源码.md) | 原目录未附加简述。 |
| `ad7124-adc.h` | [参考](P007_AD7124设备树常量参考.md) · [源码](P008_AD7124设备树常量源码.md) | 原目录未附加简述。 |
| `adc.h` | [参考](P001_ADC通用设备树常量参考.md) · [源码](P002_ADC通用设备树常量源码.md) | 原目录未附加简述。 |
| `ads1x4s0x_adc.h` | [参考](P049_ADS1x4S0x设备树常量参考.md) · [源码](P050_ADS1x4S0x设备树常量源码.md) | 原目录未附加简述。 |
| `b91-adc.h` | [参考](P013_B91ADC设备树常量参考.md) · [源码](P014_B91ADC设备树常量源码.md) | 原目录未附加简述。 |
| `gd32f3x0.h` | [参考](P011_GD32F3x0ADC设备树常量参考.md) · [源码](P012_GD32F3x0ADC设备树常量源码.md) | 原目录未附加简述。 |
| `infineon-autanalog-sar.h` | [参考](P033_Infineon自主模拟SAR常量参考.md) · [源码](P034_Infineon自主模拟SAR常量源码.md) | Infineon自主模拟（Autonomous Analog，AutAnalog）逐次逼近寄存器（Successive Approximation Register，SAR）ADC的设备树绑定常量。 |
| `infineon-sar.h` | [参考](P077_InfineonSARMUX常量参考.md) · [源码](P078_InfineonSARMUX常量源码.md) | Infineon SAR ADC的SARMUX（SAR输入多路复用器）。 |
| `mchp_pic32cm_jh_adc.h` | [参考](P035_PIC32CMJHADC常量参考.md) · [源码](P036_PIC32CMJHADC常量源码.md) | Copyright (c) 2026 Microchip Technology Inc. |
| `mchp_pic32cx_sg_adc.h` | [参考](P037_PIC32CXSGADC常量参考.md) · [源码](P038_PIC32CXSGADC常量源码.md) | Copyright (c) 2026 Microchip Technology Inc. |
| `mchp_sam_d5x_e5x_adc.h` | [参考](P039_SAMD5xE5xADC常量参考.md) · [源码](P040_SAMD5xE5xADC常量源码.md) | Copyright (c) 2025-2026 Microchip Technology Inc. |
| `mcp356xr-adc.h` | [参考](P009_MCP356xR设备树常量参考.md) · [源码](P010_MCP356xR设备树常量源码.md) | 原目录未附加简述。 |
| `mcux-adc16.h` | [参考](P023_MCUXADC16设备树常量参考.md) · [源码](P024_MCUXADC16设备树常量源码.md) | 原目录未附加简述。 |
| `mcux-lpadc.h` | [参考](P025_MCUXLPADC设备树常量参考.md) · [源码](P026_MCUXLPADC设备树常量源码.md) | 原目录未附加简述。 |
| `nrf-adc.h` | [参考](P015_NordicADC设备树常量参考.md) · [源码](P016_NordicADC设备树常量源码.md) | 原目录未附加简述。 |
| `nrf-saadc.h` | [参考](P017_NordicSAADC设备树常量参考.md) · [源码](P018_NordicSAADC设备树常量源码.md) | 原目录未附加简述。 |
| `nxp,gau-adc.h` | [参考](P019_NXPGAUADC设备树常量参考.md) · [源码](P020_NXPGAUADC设备树常量源码.md) | 原目录未附加简述。 |
| `renesas-adc-b.h` | [参考](P041_RenesasADCB常量参考.md) · [源码](P042_RenesasADCB常量源码.md) | Renesas RA ADC_B的物理模拟输入通道选择器（Physical Analog Input Channel Selectors）。 |
| `silabs-adc.h` | [参考](P027_SilabsADC设备树常量参考.md) · [源码](P028_SilabsADC设备树常量源码.md) | 原目录未附加简述。 |
| `silabs-siwx91x-adc.h` | [参考](P029_SilabsSiWx91xADC设备树常量参考.md) · [源码](P030_SilabsSiWx91xADC设备树常量源码.md) | 原目录未附加简述。 |
| `smartbond-adc.h` | [参考](P021_SmartBondADC设备树常量参考.md) · [源码](P022_SmartBondADC设备树常量源码.md) | 原目录未附加简述。 |
| `wisblock-adc.h` | [参考](P031_WisBlockADC设备树常量参考.md) · [源码](P032_WisBlockADC设备树常量源码.md) | WisBlock ADC通道常量。 |

## 66.2\_阅读范围

设备树常量头文件与驱动扩展头文件用途不同，即使名称相近也不互换。Microchip条目的原目录摘要本身为版权声明，这里保持其法律文本原样。

本页及所列头文件的参考、源码页均已翻译。整站其余待译页面继续记录在[全站进度](../PROGRESS.md)中。

---

[上一章：ADC驱动头文件目录](P065_ADC驱动头文件目录.md) · [下一章：电流检测放大器扩展头文件参考](P067_电流检测放大器扩展头文件参考.md) · [返回大纲](大纲.md)
