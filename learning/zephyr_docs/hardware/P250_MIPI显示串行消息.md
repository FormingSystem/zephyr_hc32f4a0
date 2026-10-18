---
id: learning.zephyr-docs.hardware.mipistruct-3
title: MIPI显示串行消息
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第250章\_MIPI显示串行消息

原文：[structmipi__dsi__msg](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html)。读取日期：2026-10-13，`latest`。

## 250.1\_用途

结构 [`mipi_dsi_msg`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html) 表示 MIPI **显示串行接口（Display Serial Interface，DSI）**的读写消息（Read/Write Message），定义来自 `zephyr/drivers/mipi_dsi.h`。

## 250.2\_数据字段（Data Fields）

DCS 是显示命令集（Display Command Set）；发送与接收分别称为传输（Transmission）与接收（Reception）。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`type`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a92dc0767c36f31cb23207a0581d3355f) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 载荷数据类型（Payload Data Type）。 |
| [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#ac93016853da47dc07094e7fe44e4625f) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 控制消息传输的标志。 |
| [`cmd`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a45ee5101f773a600e116d41a247cdcf4) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 命令，仅用于 DCS。 |
| [`tx_len`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a4cb0756c8cffa6acc10fee77ba6d4b17) | `size_t` | 发送缓冲区长度。 |
| [`tx_buf`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a73e62f4c7e45f0553fd0deeec06356a2) | `const void *` | 发送缓冲区。 |
| [`rx_len`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#ab17fda1dbb330bc8e66597ef816f413f) | `size_t` | 接收缓冲区长度。 |
| [`rx_buf`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#aa21b5be5cdfac9411601c83f72e58405) | `void *` | 接收缓冲区。 |
| [`user_data`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__msg.html#a9bc57ad1617fec4bd42560c6133fd774) | `void *` | 用户数据（User Data）。 |

该结构用于[MIPI显示串行接口](P246_MIPI显示串行接口.md)的消息传输函数。

---

[上一章：MIPI显示串行设备](P249_MIPI显示串行设备.md) · [下一章：MIPI显示总线后端](P251_MIPI显示总线后端.md) · [返回大纲](大纲.md)
