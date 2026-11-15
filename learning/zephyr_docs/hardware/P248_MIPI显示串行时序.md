---
id: learning.zephyr-docs.hardware.mipistruct-1
title: MIPI显示串行时序
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第248章\_MIPI显示串行时序

原文：[structmipi__dsi__timings](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html)。读取日期：2026-10-13，`latest`。

## 248.1\_用途

结构 [`mipi_dsi_timings`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html) 保存 MIPI **显示串行接口（Display Serial Interface，DSI）**的显示时序（Display Timings），定义来自 `zephyr/drivers/mipi_dsi.h`。

## 248.2\_数据字段（Data Fields）

全部字段类型均为 [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)：

| 字段 | 含义 |
| --- | --- |
| [`hactive`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#a3a91e874a7da6c37bf9b06944a3d658a) | 水平有效视频（Horizontal Active Video）。 |
| [`hfp`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#ad1b00493166d0276eb66d73be4b6968d) | 水平前肩（Horizontal Front Porch）。 |
| [`hbp`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#afb4451d7767a911ea6a92a9fbba5e935) | 水平后肩（Horizontal Back Porch）。 |
| [`hsync`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#a58f985d9c43cd149959dad7f12fcff8e) | 水平同步长度（Horizontal Sync Length）。 |
| [`vactive`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#acc8077892efa4977fd667680d63f5c7c) | 垂直有效视频（Vertical Active Video）。 |
| [`vfp`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#ac44c32c7d150ddd4b327308196169578) | 垂直前肩（Vertical Front Porch）。 |
| [`vbp`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#afff80261d02253b76a872ee805a4cd46) | 垂直后肩（Vertical Back Porch）。 |
| [`vsync`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__timings.html#a535e0177862b753ef9f4af011ed483a4) | 垂直同步长度（Vertical Sync Length）。 |

该结构嵌入[DSI设备描述](P249_MIPI显示串行设备.md)。

---

[上一章：MIPI显示总线配置](P247_MIPI显示总线配置.md) · [下一章：MIPI显示串行设备](P249_MIPI显示串行设备.md) · [返回大纲](大纲.md)
