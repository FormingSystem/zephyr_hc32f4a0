---
id: learning.zephyr-docs.hardware.ledapi-2
title: LED信息结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第204章\_LED信息结构

原文：[structled__info](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html)。读取日期：2026-10-13，`latest`。

## 204.1\_用途

结构 [`led_info`](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html) 汇集 **发光二极管（Light-Emitting Diode，LED）**控制器的有用信息，定义来自官方头文件 `zephyr/drivers/led.h`。

## 204.2\_数据字段（Data Fields）

| 字段 | 原始类型 | 含义 |
| --- | --- | --- |
| [`label`](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html#a5d01795e49663654e9fe4a821797956a) | `const char *` | LED 标签（Label）。 |
| [`index`](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html#a7f87ebb0718e1dc189e6d48d5bb97c55) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | LED 在控制器上的索引（Index）。 |
| [`num_colors`](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html#ab6db05157b960669e3b01154a9621530) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 每个 LED 的颜色数量（Number of Colors）。 |
| [`color_mapping`](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html#a8daacbe0a68d7ff710938722003fceaf) | `const uint8_t *` | LED 的颜色映射（Color Mapping）。 |

获取该结构，以及按照颜色映射设置颜色的方法，见[LED公共接口](P202_LED公共接口.md)。

[上一章：LED设备树描述结构](P203_LED设备树描述结构.md) · [下一章：LED驱动后端接口](P205_LED驱动后端接口.md) · [返回大纲](大纲.md)
