---
id: learning.zephyr-docs.hardware.dacapi-4
title: DAC驱动实现接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第823章\_DAC驱动实现接口

原文：[group__dac__interface__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface__backend.html)。读取日期：2026-10-13，`latest`。

本组为数模转换器（Digital-to-Analog Converter，DAC）驱动实现提供应用程序接口（Application Programming Interface，API）类型定义、回调签名（Callback Signature）及其他辅助项，即驱动后端接口（Driver Backend API）。

公共头文件为 `zephyr/drivers/dac.h`。驱动操作保存在[驱动接口结构](P827_DAC驱动接口结构.md)中；配置参数参见[通道配置结构](P825_DAC通道配置结构.md)。

## 823.1\_通道配置函数类型

```c
#include <zephyr/drivers/dac.h>

typedef int (*dac_api_channel_setup)(const struct device *dev,
                                     const struct dac_channel_cfg *channel_cfg);
```

[`dac_api_channel_setup`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface__backend.html#ga48651a0355b893551661297cb2d5e483) 是配置DAC通道的函数指针类型（Function Pointer Type）。参数含义见[通道配置接口](P822_数模转换器接口.md)：`dev` 为驱动实例的设备结构指针，`channel_cfg` 为通道配置。返回值按 [`dac_channel_setup()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gab8be77003ba8fd7225c0808f95602a56) 的约定处理。

## 823.2\_单值写入函数类型

```c
typedef int (*dac_api_write_value)(const struct device *dev,
                                   uint8_t channel, uint32_t value);
```

[`dac_api_write_value`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface__backend.html#gacde710d856a65d8961c339fc8b7a41a3) 是设置写请求（Write Request）的函数指针类型。参数含义见[单值写入接口](P822_数模转换器接口.md)：`dev` 为设备结构指针，`channel` 为通道编号，`value` 为写入DAC输出寄存器的数据。返回值按 [`dac_write_value()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga437a6f6b2402cf2e2a2a689429663b4e) 的约定处理。

---

[上一章：数模转换器接口](P822_数模转换器接口.md) · [下一章：DAC驱动扩展入口](P824_DAC驱动扩展入口.md) · [返回大纲](大纲.md)
