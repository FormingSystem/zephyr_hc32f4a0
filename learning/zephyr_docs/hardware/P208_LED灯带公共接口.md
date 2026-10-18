---
id: learning.zephyr-docs.hardware.stripapi-0
title: LED灯带公共接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第208章\_LED灯带公共接口

原文：[group__led__strip__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html)。读取日期：2026-10-13，`latest`。

## 208.1\_范围与版本

本页提供 **发光二极管灯带（Light-Emitting Diode Strip，LED Strip）**的 **应用程序编程接口（Application Programming Interface，API）**。接口自 Zephyr 1.10 提供，本页版本为 0.8.0，主头文件为官方 `zephyr/drivers/led_strip.h`。

颜色数组使用颜色结构 [`led_rgb`](P209_LED灯带颜色结构.md)，其中 RGB 表示红、绿、蓝（Red, Green, Blue）。

## 208.2\_更新RGB像素数组

函数声明为：

```c
static inline int led_strip_update_rgb(const struct device *dev,
                                       struct led_rgb *pixels,
                                       size_t num_pixels);
```

函数 [`led_strip_update_rgb()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga6e63331a5be2430968ab8b60692f8d67) 使用给定 RGB 数组更新灯带。`dev` 是灯带设备；`pixels` 指向像素数据数组（Pixel Data Array）；`num_pixels` 是数组长度。

成功返回 0，失败返回负的错误码（Negative errno Code）。**原文警告：函数可能覆写 `pixels` 数组。**

## 208.3\_按通道数组更新

```c
static inline int led_strip_update_channels(const struct device *dev,
                                            uint8_t *channels,
                                            size_t num_channels);
```

函数 [`led_strip_update_channels()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga846b1d37bc6f7ed2014bea9603788b34) 使用给定的通道数组（Channel Array）更新灯带。每个字节对应一个可独立寻址的颜色通道或 LED，按灯带顺序线性更新。

`dev` 是灯带设备；`channels` 是逐通道数据数组；`num_channels` 是数组长度。

返回值：成功为 0；未实现为 `-ENOSYS`；其他失败为负的错误码。**原文警告：函数可能覆写 `channels` 数组。**

## 208.4\_查询灯带长度

```c
static inline size_t led_strip_length(const struct device *dev);
```

函数 [`led_strip_length()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga7f94eab0b357a81cccb5f0ea1575714a) 返回 `dev` 灯带设备的级联长度（Chain Length），以像素数为单位。

## 208.5\_相关接口

[灯带驱动后端](P210_LED灯带后端接口.md) · [器件扩展目录](P212_LED灯带扩展接口目录.md) · [灯带示例](P191_LED灯带示例.md)


---

[上一章：模拟LED控制器](P207_模拟LED控制器.md) · [下一章：LED灯带颜色结构](P209_LED灯带颜色结构.md) · [返回大纲](大纲.md)
