---
id: learning.zephyr-docs.hardware.mipistruct-2
title: MIPI显示串行设备
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第249章\_MIPI显示串行设备

原文：[structmipi__dsi__device](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html)。读取日期：2026-10-13，`latest`。

## 249.1\_用途

结构 [`mipi_dsi_device`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html) 描述 MIPI **显示串行接口（Display Serial Interface，DSI）**设备，定义来自 `zephyr/drivers/mipi_dsi.h`。

## 249.2\_数据字段（Data Fields）

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`data_lanes`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html#ae2e6fddb1651a71c1b969ecec295e1c0) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 数据通道（Data Lane）数量。 |
| [`timings`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html#af9ec42cd1fcb16cf63060b0097180f3f) | `struct mipi_dsi_timings` | 显示时序（Display Timings），完整字段见[时序结构](P248_MIPI显示串行时序.md)。 |
| [`pixfmt`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html#a729dd69843ee3eaf6bd5cbd2e725fdea) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 像素格式（Pixel Format）。 |
| [`mode_flags`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__device.html#af22eab1f95d8865fe7a67e49d6e36f8c) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 模式标志（Mode Flags）。 |

像素格式、模式标志以及连接/分离操作见[MIPI显示串行接口](P246_MIPI显示串行接口.md)。

---

[上一章：MIPI显示串行时序](P248_MIPI显示串行时序.md) · [下一章：MIPI显示串行消息](P250_MIPI显示串行消息.md) · [返回大纲](大纲.md)
