---
id: learning.zephyr-docs.adc_reference.adcheaderremaining-77
title: InfineonSARMUX常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-sar_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第77章\_InfineonSARMUX常量参考

原文：[infineon-sar_8h](https://docs.zephyrproject.org/latest/doxygen/html/infineon-sar_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/infineon-sar.h` 为Infineon逐次逼近寄存器（Successive Approximation Register，SAR）模数转换器（Analog-to-Digital Converter，ADC）定义SARMUX输入选择值。SARMUX是此处SAR输入多路复用器（Multiplexer）的名称。

## 77.1\_输入选择常量

原文件的八个宏及其说明如下。数值是硬件输入选择地址，保留十六进制表示。

| 宏 | 值 | 原文含义 |
| --- | --- | --- |
| `CY_SAR_ADDR_SARMUX_0` | `0x0` | SARMUX专用（Dedicated）端口2引脚0。 |
| `CY_SAR_ADDR_SARMUX_1` | `0x1` | SARMUX端口2引脚1。 |
| `CY_SAR_ADDR_SARMUX_2` | `0x2` | SARMUX端口2引脚2。 |
| `CY_SAR_ADDR_SARMUX_3` | `0x3` | SARMUX端口2引脚3。 |
| `CY_SAR_ADDR_SARMUX_4` | `0x4` | SARMUX端口2引脚4。 |
| `CY_SAR_ADDR_SARMUX_5` | `0x5` | SARMUX端口2引脚5。 |
| `CY_SAR_ADDR_SARMUX_6` | `0x6` | SARMUX端口2引脚6。 |
| `CY_SAR_ADDR_SARMUX_7` | `0x7` | SARMUX端口2引脚7。 |

## 77.2\_设备树用途

源码注释说明：这些SARMUX硬件地址（Hardware Address）用于 `zephyr,input-positive` 与 `zephyr,input-negative`，即正输入（Positive Input）与负输入（Negative Input）选择。SARMUX专用端口**通常为端口2（Typically Port 2）**；保留“通常”这一限定，不能据此认定所有器件的专用端口均固定为端口2。

完整定义与原注释见[源码页](P078_InfineonSARMUX常量源码.md)。

---

[上一章：Infineon自主模拟SAR驱动头文件源码](P076_Infineon自主模拟SAR驱动头文件源码.md) · [下一章：InfineonSARMUX常量源码](P078_InfineonSARMUX常量源码.md) · [返回大纲](大纲.md)
