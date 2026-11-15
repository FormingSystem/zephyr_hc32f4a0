---
id: learning.zephyr-docs.hardware.stripapi-2
title: LED灯带后端接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第210章\_LED灯带后端接口

原文：[group__led__strip__interface__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html)。读取日期：2026-10-13，`latest`。

## 210.1\_用途

本组定义实现 **发光二极管灯带（Light-Emitting Diode Strip，LED Strip）**驱动所需的 **应用程序编程接口（Application Programming Interface，API）**类型、回调签名（Callback Signature）及辅助内容，声明来自官方头文件 `zephyr/drivers/led_strip.h`。

驱动操作通过[灯带驱动函数表](P211_LED灯带驱动函数表.md)提供。

## 210.2\_回调类型

红、绿、蓝（Red, Green, Blue，RGB）是本接口使用的颜色分量。以下是三个函数指针类型定义（Function Pointer Typedef）：

```c
typedef int (*led_api_update_rgb)(const struct device *dev,
                                 struct led_rgb *pixels, size_t num_pixels);
typedef int (*led_api_update_channels)(const struct device *dev,
                                      uint8_t *channels, size_t num_channels);
typedef size_t (*led_api_length)(const struct device *dev);
```

| 类型 | 用途与参数说明入口 |
| --- | --- |
| [`led_api_update_rgb`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#gaa36be40a962173021a547192d0d39151) | 更新红、绿、蓝（Red, Green, Blue，RGB）灯带；参数见 [`led_strip_update_rgb()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga6e63331a5be2430968ab8b60692f8d67)。 |
| [`led_api_update_channels`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#gab11579a7b5b7febfd48fa12560254501) | 直接更新通道数据，不按 RGB 解释；参数见 [`led_strip_update_channels()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga846b1d37bc6f7ed2014bea9603788b34)。 |
| [`led_api_length`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface__backend.html#ga3487e5d4a339898f88a225bb3678776b) | 获取灯带长度；参数见 [`led_strip_length()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga7f94eab0b357a81cccb5f0ea1575714a)。 |

完整参数语义与更新时可能覆写输入数组的行为，见[LED灯带公共接口](P208_LED灯带公共接口.md)。


---

[上一章：LED灯带颜色结构](P209_LED灯带颜色结构.md) · [下一章：LED灯带驱动函数表](P211_LED灯带驱动函数表.md) · [返回大纲](大纲.md)
