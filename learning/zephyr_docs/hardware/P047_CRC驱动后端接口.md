---
id: learning.zephyr-docs.hardware.backend-1
title: CRC驱动后端接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第47章\_CRC驱动后端接口

原文：[group__crc__interface__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html)。读取日期：2026-10-13，`latest`。

## 47.1\_后端接口的作用

本组提供实现 **循环冗余校验（Cyclic Redundancy Check，CRC）**驱动需要的 **应用程序编程接口（Application Programming Interface，API）**类型定义、回调签名和辅助内容。声明来自官方头文件 `zephyr/drivers/crc.h`。

**回调函数（Callback Function）**在这里表示驱动提供的具体操作；上层公共接口借助这些操作访问实现。原页列出的 `struct crc_driver_api` 是CRC驱动操作结构，字段见其[结构参考](P052_CRC驱动操作结构.md)。

## 47.2\_开始、更新和结束回调

三种函数指针类型与计算阶段对应，声明如下：

```c
typedef int (*crc_api_begin)(const struct device *dev,
                             struct crc_ctx *ctx);
typedef int (*crc_api_update)(const struct device *dev,
                              struct crc_ctx *ctx,
                              const void *buffer, size_t bufsize);
typedef int (*crc_api_finish)(const struct device *dev,
                              struct crc_ctx *ctx);
```

| 回调类型 | 作用 | 原文参数说明入口 |
| --- | --- | --- |
| [`crc_api_begin`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#ga8babc96e0e656e3974c5e3df32f59107) | 为CRC计算配置CRC单元。 | [`crc_begin()`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gae6f2adfd858b18765b2e58d8135c28fa)。 |
| [`crc_api_update`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#ga7d6a2a6b119a8fb51d91e6f5f6269af7) | 向正在进行的CRC计算送入数据。 | [`crc_update()`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gaf5e71e99b5838e4b21f30e4b2fb4a684)。 |
| [`crc_api_finish`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#gadaec1299bbc8b5a03e4b724b32064abc) | 完成CRC计算。 | [`crc_finish()`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gab144200cba95d6cc08c85cf9c5c1dd91)。 |

三个回调都接收设备指针 `dev` 与CRC上下文指针 `ctx`；更新回调额外接收输入缓冲区 `buffer` 及其字节数 `bufsize`。公共函数的参数和返回约束已译在[CRC驱动接口参考](P038_CRC驱动接口参考.md)，上下文字段见[CRC上下文结构](P046_CRC上下文结构.md)。原页没有额外规定另一套后端错误码。

[上一章：CRC上下文结构](P046_CRC上下文结构.md) · [下一章：熵源驱动后端接口](P048_熵源驱动后端接口.md) · [返回大纲](大纲.md)
