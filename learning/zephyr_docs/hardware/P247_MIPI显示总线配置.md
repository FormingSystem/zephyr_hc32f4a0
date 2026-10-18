---
id: learning.zephyr-docs.hardware.mipistruct-0
title: MIPI显示总线配置
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第247章\_MIPI显示总线配置

原文：[structmipi__dbi__config](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__config.html)。读取日期：2026-10-13，`latest`。

## 247.1\_用途

结构 [`mipi_dbi_config`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__config.html) 保存 MIPI **显示总线接口（Display Bus Interface，DBI）**控制器配置，用于控制器写入操作。定义来自 `zephyr/drivers/mipi_dbi.h`。

## 247.2\_数据字段（Data Fields）

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`mode`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__config.html#a2eafaaa6cda8f17f4b518c007bb3a7c3) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | MIPI DBI 模式（Mode）。 |
| [`color_coding`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__config.html#ab8182314f21f49de880b4b78ccf8a0aa) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | Type A 或 Type B（6800/8080）接口的颜色编码（Color Coding）。 |
| [`config`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__config.html#a50d0893838455e3b8faa29d6459bc9c8) | `struct spi_config` | 串行外设接口（Serial Peripheral Interface，SPI）配置。 |

模式与颜色编码常量、设备树初始化宏以及写入函数见[MIPI显示总线接口](P245_MIPI显示总线接口.md)。

---

[上一章：MIPI显示串行接口](P246_MIPI显示串行接口.md) · [下一章：MIPI显示串行时序](P248_MIPI显示串行时序.md) · [返回大纲](大纲.md)
