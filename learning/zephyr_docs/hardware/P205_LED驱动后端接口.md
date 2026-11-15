---
id: learning.zephyr-docs.hardware.ledbackend-0
title: LED驱动后端接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第205章\_LED驱动后端接口

原文：[group__led__interface__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html)。读取日期：2026-10-13，`latest`。

## 205.1\_用途

本组定义实现 **发光二极管（Light-Emitting Diode，LED）**驱动所需的 **应用程序编程接口（Application Programming Interface，API）**类型、回调签名（Callback Signature）和辅助内容。声明来自官方头文件 `zephyr/drivers/led.h`。

驱动通过函数表 [`led_driver_api`](P206_LED驱动函数表.md)提供操作；应用使用[LED公共接口](P202_LED公共接口.md)。

## 205.2\_七种回调类型

以下为完整的函数指针类型定义（Function Pointer Typedef）：

```c
typedef int (*led_api_blink)(const struct device *dev, uint32_t led,
                            uint32_t delay_on, uint32_t delay_off);
typedef int (*led_api_get_info)(const struct device *dev, uint32_t led,
                               const struct led_info **info);
typedef int (*led_api_set_brightness)(const struct device *dev,
                                     uint32_t led, uint8_t value);
typedef int (*led_api_set_color)(const struct device *dev, uint32_t led,
                                uint8_t num_colors, const uint8_t *color);
typedef int (*led_api_on)(const struct device *dev, uint32_t led);
typedef int (*led_api_off)(const struct device *dev, uint32_t led);
typedef int (*led_api_write_channels)(const struct device *dev,
                                     uint32_t start_channel,
                                     uint32_t num_channels, const uint8_t *buf);
```

| 类型 | 原页说明与参数依据 |
| --- | --- |
| [`led_api_blink`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gad3c655794f58045459cbd910592d2cdd) | 闪烁回调；参数见 [`led_blink()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga4f31fecd215e5597999be4d16b0d2dd5)。 |
| [`led_api_get_info`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga3828b1e544a2f64378d5c3bfbbaa0c77) | 可选的信息获取回调；参数见 [`led_get_info()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga9925483b97073354f7be6b40aa2dad1a)。 |
| [`led_api_set_brightness`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gae24caa14f6aa41c2a509d2eaf468463f) | 亮度设置回调；参数见 [`led_set_brightness()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaca479fd77518331f4fc84f788e345882)。 |
| [`led_api_set_color`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga977317f3208d5336463edf9979def4ae) | 可选的颜色设置回调；参数见 [`led_set_color()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)。 |
| [`led_api_on`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gad13f55702668133575658d2ccc295339) | 点亮回调；参数见 [`led_on()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gad4daafd7fcab22d1d68745b7264d0f73)。 |
| [`led_api_off`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga5ae67fe64f97b0e716f9eb2f3a34f1fd) | 关闭回调；参数见 [`led_off()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga22c9dbe76f06fec327aebe06448d1542)。 |
| [`led_api_write_channels`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga66dac12510c3a2281378d532ba6db2ae) | 连续通道写入回调；参数见 [`led_write_channels()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga24d4007f81483d0fe8b9988288adf59a)。 |

原页将具体参数说明统一指向对应公共函数。驱动必须提供哪些操作，以及开关和亮度操作如何互相补充，见[LED驱动函数表](P206_LED驱动函数表.md)。

[上一章：LED信息结构](P204_LED信息结构.md) · [下一章：LED驱动函数表](P206_LED驱动函数表.md) · [返回大纲](大纲.md)
