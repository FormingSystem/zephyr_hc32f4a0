---
id: learning.zephyr-docs.hardware.spistruct-3
title: SPI缓冲区结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第322章\_SPI缓冲区结构

原文：[structspi__buf](https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf.html)。读取日期：2026-10-13，`latest`。

## 322.1\_真实缓冲区与空操作指示

[`spi_buf`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf.html) 是串行外设接口（Serial Peripheral Interface，SPI）缓冲区结构，声明来自 `zephyr/drivers/spi.h`。它既能描述实际数据缓冲区（Buffer），也能表示空操作（No Operation，NOP）。

此处空操作仍会占用总线上的传输长度：用于发送（Transmit，TX）时，在指定长度内只发送零；用于接收（Receive，RX）时，忽略或跳过总线收到的对应长度数据。它不表示直接省略这段总线传输。

## 322.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="aeaf52d3ff5af10545b2d6904ed452cba"></a>[`buf`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf.html#aeaf52d3ff5af10545b2d6904ed452cba) | `void *` | 指向有效数据缓冲区；为 `NULL` 时表示 NOP |
| <a id="a9755deadff0dd01a886f22e41099b8ba"></a>[`len`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf.html#a9755deadff0dd01a886f22e41099b8ba) | `size_t` | 缓冲区的字节长度，或 NOP 的长度 |

---

[上一章：SPI设备树描述结构](P321_SPI设备树描述结构.md) · [下一章：SPI缓冲区集合结构](P323_SPI缓冲区集合结构.md) · [返回大纲](大纲.md)
