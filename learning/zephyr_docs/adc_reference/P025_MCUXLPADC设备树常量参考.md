---
id: learning.zephyr-docs.adc_reference.adcheaderplatform-25
title: MCUXLPADC设备树常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcux-lpadc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第25章\_MCUXLPADC设备树常量参考

原文：[mcux-lpadc_8h](https://docs.zephyrproject.org/latest/doxygen/html/mcux-lpadc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/mcux-lpadc.h` 定义MCUX低功耗模数转换器（Low-Power Analog-to-Digital Converter，LPADC）的输入选择常量。原页列出通道0至31各自A、B两侧的64个宏（Macro）；中文说明按名称补充，数值及括号保持原样。

## 25.1\_通道与侧选择

| 宏 | 原始值 | 中文说明 |
| --- | --- | --- |
| `MCUX_LPADC_CH0A` | `(0x0)` | 通道（Channel）0，A侧 |
| `MCUX_LPADC_CH0B` | `(0x20)` | 通道（Channel）0，B侧 |
| `MCUX_LPADC_CH1A` | `(0x1)` | 通道（Channel）1，A侧 |
| `MCUX_LPADC_CH1B` | `(0x21)` | 通道（Channel）1，B侧 |
| `MCUX_LPADC_CH2A` | `(0x2)` | 通道（Channel）2，A侧 |
| `MCUX_LPADC_CH2B` | `(0x22)` | 通道（Channel）2，B侧 |
| `MCUX_LPADC_CH3A` | `(0x3)` | 通道（Channel）3，A侧 |
| `MCUX_LPADC_CH3B` | `(0x23)` | 通道（Channel）3，B侧 |
| `MCUX_LPADC_CH4A` | `(0x4)` | 通道（Channel）4，A侧 |
| `MCUX_LPADC_CH4B` | `(0x24)` | 通道（Channel）4，B侧 |
| `MCUX_LPADC_CH5A` | `(0x5)` | 通道（Channel）5，A侧 |
| `MCUX_LPADC_CH5B` | `(0x25)` | 通道（Channel）5，B侧 |
| `MCUX_LPADC_CH6A` | `(0x6)` | 通道（Channel）6，A侧 |
| `MCUX_LPADC_CH6B` | `(0x26)` | 通道（Channel）6，B侧 |
| `MCUX_LPADC_CH7A` | `(0x7)` | 通道（Channel）7，A侧 |
| `MCUX_LPADC_CH7B` | `(0x27)` | 通道（Channel）7，B侧 |
| `MCUX_LPADC_CH8A` | `(0x8)` | 通道（Channel）8，A侧 |
| `MCUX_LPADC_CH8B` | `(0x28)` | 通道（Channel）8，B侧 |
| `MCUX_LPADC_CH9A` | `(0x9)` | 通道（Channel）9，A侧 |
| `MCUX_LPADC_CH9B` | `(0x29)` | 通道（Channel）9，B侧 |
| `MCUX_LPADC_CH10A` | `(0x0A)` | 通道（Channel）10，A侧 |
| `MCUX_LPADC_CH10B` | `(0x2A)` | 通道（Channel）10，B侧 |
| `MCUX_LPADC_CH11A` | `(0x0B)` | 通道（Channel）11，A侧 |
| `MCUX_LPADC_CH11B` | `(0x2B)` | 通道（Channel）11，B侧 |
| `MCUX_LPADC_CH12A` | `(0x0C)` | 通道（Channel）12，A侧 |
| `MCUX_LPADC_CH12B` | `(0x2C)` | 通道（Channel）12，B侧 |
| `MCUX_LPADC_CH13A` | `(0x0D)` | 通道（Channel）13，A侧 |
| `MCUX_LPADC_CH13B` | `(0x2D)` | 通道（Channel）13，B侧 |
| `MCUX_LPADC_CH14A` | `(0x0E)` | 通道（Channel）14，A侧 |
| `MCUX_LPADC_CH14B` | `(0x2E)` | 通道（Channel）14，B侧 |
| `MCUX_LPADC_CH15A` | `(0x0F)` | 通道（Channel）15，A侧 |
| `MCUX_LPADC_CH15B` | `(0x2F)` | 通道（Channel）15，B侧 |
| `MCUX_LPADC_CH16A` | `(0x10)` | 通道（Channel）16，A侧 |
| `MCUX_LPADC_CH16B` | `(0x30)` | 通道（Channel）16，B侧 |
| `MCUX_LPADC_CH17A` | `(0x11)` | 通道（Channel）17，A侧 |
| `MCUX_LPADC_CH17B` | `(0x31)` | 通道（Channel）17，B侧 |
| `MCUX_LPADC_CH18A` | `(0x12)` | 通道（Channel）18，A侧 |
| `MCUX_LPADC_CH18B` | `(0x32)` | 通道（Channel）18，B侧 |
| `MCUX_LPADC_CH19A` | `(0x13)` | 通道（Channel）19，A侧 |
| `MCUX_LPADC_CH19B` | `(0x33)` | 通道（Channel）19，B侧 |
| `MCUX_LPADC_CH20A` | `(0x14)` | 通道（Channel）20，A侧 |
| `MCUX_LPADC_CH20B` | `(0x34)` | 通道（Channel）20，B侧 |
| `MCUX_LPADC_CH21A` | `(0x15)` | 通道（Channel）21，A侧 |
| `MCUX_LPADC_CH21B` | `(0x35)` | 通道（Channel）21，B侧 |
| `MCUX_LPADC_CH22A` | `(0x16)` | 通道（Channel）22，A侧 |
| `MCUX_LPADC_CH22B` | `(0x36)` | 通道（Channel）22，B侧 |
| `MCUX_LPADC_CH23A` | `(0x17)` | 通道（Channel）23，A侧 |
| `MCUX_LPADC_CH23B` | `(0x37)` | 通道（Channel）23，B侧 |
| `MCUX_LPADC_CH24A` | `(0x18)` | 通道（Channel）24，A侧 |
| `MCUX_LPADC_CH24B` | `(0x38)` | 通道（Channel）24，B侧 |
| `MCUX_LPADC_CH25A` | `(0x19)` | 通道（Channel）25，A侧 |
| `MCUX_LPADC_CH25B` | `(0x39)` | 通道（Channel）25，B侧 |
| `MCUX_LPADC_CH26A` | `(0x1A)` | 通道（Channel）26，A侧 |
| `MCUX_LPADC_CH26B` | `(0x3A)` | 通道（Channel）26，B侧 |
| `MCUX_LPADC_CH27A` | `(0x1B)` | 通道（Channel）27，A侧 |
| `MCUX_LPADC_CH27B` | `(0x3B)` | 通道（Channel）27，B侧 |
| `MCUX_LPADC_CH28A` | `(0x1C)` | 通道（Channel）28，A侧 |
| `MCUX_LPADC_CH28B` | `(0x3C)` | 通道（Channel）28，B侧 |
| `MCUX_LPADC_CH29A` | `(0x1D)` | 通道（Channel）29，A侧 |
| `MCUX_LPADC_CH29B` | `(0x3D)` | 通道（Channel）29，B侧 |
| `MCUX_LPADC_CH30A` | `(0x1E)` | 通道（Channel）30，A侧 |
| `MCUX_LPADC_CH30B` | `(0x3E)` | 通道（Channel）30，B侧 |
| `MCUX_LPADC_CH31A` | `(0x1F)` | 通道（Channel）31，A侧 |
| `MCUX_LPADC_CH31B` | `(0x3F)` | 通道（Channel）31，B侧 |

## 25.2\_选择编码的解释

译注：A侧使用 `0x00` 至 `0x1F` 对应的编码，B侧使用 `0x20` 至 `0x3F`；表中原文件把部分值写成 `0x0` 等较短形式，已保留。相同通道的A、B侧是不同选择项。本文件没有说明每个芯片或封装实际引出的通道，不能据此推定全部64项在任意目标上均可用。原始定义见[源码页](P026_MCUXLPADC设备树常量源码.md)。

---

[上一章：MCUXADC16设备树常量源码](P024_MCUXADC16设备树常量源码.md) · [下一章：MCUXLPADC设备树常量源码](P026_MCUXLPADC设备树常量源码.md) · [返回大纲](大纲.md)
