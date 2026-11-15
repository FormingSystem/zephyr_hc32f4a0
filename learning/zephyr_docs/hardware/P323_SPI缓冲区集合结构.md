---
id: learning.zephyr-docs.hardware.spistruct-4
title: SPI缓冲区集合结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf__set.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第323章\_SPI缓冲区集合结构

原文：[structspi__buf__set](https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf__set.html)。读取日期：2026-10-13，`latest`。

## 323.1\_分散聚集传输

[`spi_buf_set`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf__set.html) 是串行外设接口（Serial Peripheral Interface，SPI）的分散聚集（Scatter-Gather）缓冲区数组结构，声明来自 `zephyr/drivers/spi.h`。它灵活地描述一次完整 SPI 总线传输。

集合由描述缓冲区的数组组成，因此一次传输定义中的各个片段可以在不同传输之间复用，不必每次重新定义或分配内存。这是在驱动层利用用户提供的缓冲区实现分散聚集管理：一次传输由多个缓冲区片段共同组成。

> 译注：原文概述使用“指向缓冲区的指针数组”这一措辞；字段类型实际为指向 [`spi_buf`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf.html) 数组的指针，而每个 [`spi_buf`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf.html) 再保存数据缓冲区指针。两层结构应按下面的类型理解。

## 323.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a2b88917ca29487b2d0b5b63d2083db67"></a>[`buffers`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf__set.html#a2b88917ca29487b2d0b5b63d2083db67) | `const struct spi_buf *` | 指向 [`spi_buf`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf.html) 数组，也可以为 `NULL` |
| <a id="abc7c37cffebb7873aaba2e524c9a23dc"></a>[`count`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__buf__set.html#abc7c37cffebb7873aaba2e524c9a23dc) | `size_t` | `buffers` 所指数组中的缓冲区数量 |

---

[上一章：SPI缓冲区结构](P322_SPI缓冲区结构.md) · [下一章：SPI驱动后端接口](P324_SPI驱动后端接口.md) · [返回大纲](大纲.md)
