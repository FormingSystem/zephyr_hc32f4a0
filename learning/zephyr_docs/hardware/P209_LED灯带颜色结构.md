---
id: learning.zephyr-docs.hardware.stripapi-1
title: LED灯带颜色结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structled__rgb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第209章\_LED灯带颜色结构

原文：[structled__rgb](https://docs.zephyrproject.org/latest/doxygen/html/structled__rgb.html)。读取日期：2026-10-13，`latest`。

## 209.1\_用途

[`led_rgb`](https://docs.zephyrproject.org/latest/doxygen/html/structled__rgb.html) 表示一个 **发光二极管（Light-Emitting Diode，LED）**的红、绿、蓝（Red, Green, Blue，RGB）颜色值。定义来自官方头文件 `zephyr/drivers/led_strip.h`。

## 209.2\_颜色分量

| 字段 | 原始类型 | 含义 |
| --- | --- | --- |
| [`r`](https://docs.zephyrproject.org/latest/doxygen/html/structled__rgb.html#a2b3072dbddc32f7a93b87b9ed01e1a33) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 红色通道（Red Channel）。 |
| [`g`](https://docs.zephyrproject.org/latest/doxygen/html/structled__rgb.html#ab24a1948906fcb4c5978a84ac46b779a) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 绿色通道（Green Channel）。 |
| [`b`](https://docs.zephyrproject.org/latest/doxygen/html/structled__rgb.html#abf071f86f224daa42b3b905071e550af) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 蓝色通道（Blue Channel）。 |

如果特定灯带驱动的某个通道分辨率不足一个完整字节，驱动可能忽略该通道数据的低有效位（Lower-order Bits）。

数组更新方法见[LED灯带公共接口](P208_LED灯带公共接口.md)。


---

[上一章：LED灯带公共接口](P208_LED灯带公共接口.md) · [下一章：LED灯带后端接口](P210_LED灯带后端接口.md) · [返回大纲](大纲.md)
