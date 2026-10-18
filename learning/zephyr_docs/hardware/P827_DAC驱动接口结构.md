---
id: learning.zephyr-docs.hardware.dacapi-8
title: DAC驱动接口结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdac__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第827章\_DAC驱动接口结构

原文：[structdac__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structdac__driver__api.html)。读取日期：2026-10-13，`latest`。

`struct dac_driver_api` 是每个数模转换器（Digital-to-Analog Converter，DAC）驱动需要定义的应用程序接口（Application Programming Interface，API）结构，包含驱动操作的函数指针（Function Pointer），以及其他驱动专用的常量数据。结构定义来自 `zephyr/drivers/dac.h`：

```c
#include <zephyr/drivers/dac.h>
```

## 827.1\_必需的驱动操作

原文标记REQ表示必需（Required），驱动**必须设置**；OPT表示可选（Optional）。本页列出的两个成员均为REQ。

| 字段 | 类型 | 要求 | 操作 |
| --- | --- | --- | --- |
| [`channel_setup`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__driver__api.html#ae3f53e7374013f2d3e95fd4452b18514) | [`dac_api_channel_setup`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface__backend.html#ga48651a0355b893551661297cb2d5e483) | REQ | 配置一个DAC通道 |
| [`write_value`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__driver__api.html#aac048f094c4882fb5f70e554013d00f1) | [`dac_api_write_value`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface__backend.html#gacde710d856a65d8961c339fc8b7a41a3) | REQ | 向一个DAC通道写入单个值 |

函数指针类型定义见[驱动实现接口](P823_DAC驱动实现接口.md)，应用调用方式见[DAC接口](P822_数模转换器接口.md)。

## 827.2\_相关设备定义宏

原页列出的相关项为 [`DEVICE_DT_INST_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)、[`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1) 和 [`DEVICE_API()`](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)，用于设备实例／设备接口定义。字段文档由 `zephyr/drivers/dac.h` 生成。

---

[上一章：DAC设备树规格结构](P826_DAC设备树规格结构.md) · [下一章：DAC161S997扩展接口](P828_DAC161S997扩展接口.md) · [返回大纲](大纲.md)
