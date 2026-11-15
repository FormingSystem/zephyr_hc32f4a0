---
id: learning.zephyr-docs.hardware.adcext-2
title: NPCX_ADC阈值参数
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__npcx__threshold__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第466章\_NPCX_ADC阈值参数

原文：[structadc__npcx__threshold__param](https://docs.zephyrproject.org/latest/doxygen/html/structadc__npcx__threshold__param.html)。读取日期：2026-10-13，`latest`。

## 466.1\_结构与头文件

`struct adc_npcx_threshold_param` 为 NPCX 系列**模数转换器（Analog-to-Digital Converter，ADC）**的阈值控制参数（Threshold Control Parameter）结构。

```c
#include <zephyr/drivers/adc/adc_npcx_threshold.h>
```

## 466.2\_字段

| 字段 | 类型 | 官方说明 |
| --- | --- | --- |
| [`type`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__npcx__threshold__param.html#a737a6f60a6bcf9fe952f957b0b67c777) | `enum adc_npcx_threshold_param_type` | 阈值控制参数 |
| [`val`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__npcx__threshold__param.html#a250120d513253a21c9581b74093ca2c7) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 参数值（Parameter Value） |

具体参数类型由 [`adc_npcx_threshold_param_type`](https://docs.zephyrproject.org/latest/doxygen/html/adc__npcx__threshold_8h.html#a7da5b595bef1edfb12ad8223fb7fc461) 枚举定义；原结构页没有进一步的数值范围或单位说明。

---

[上一章：ADC设备专用扩展](P465_ADC设备专用扩展.md) · [下一章：ADS131M02扩展接口](P467_ADS131M02扩展接口.md) · [返回大纲](大纲.md)
