---
id: learning.zephyr-docs.hardware.emulstruct-6
title: MSPI仿真设备API结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structemul__mspi__device__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第483章\_MSPI仿真设备API结构

原文：[structemul__mspi__device__api](https://docs.zephyrproject.org/latest/doxygen/html/structemul__mspi__device__api.html)。读取日期：2026-10-13，`latest`。

`struct emul_mspi_device_api` 定义**多线串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）**设备仿真器的**应用程序编程接口（Application Programming Interface，API）**。结构位于 `zephyr/drivers/mspi_emul.h`。

## 483.1\_收发请求处理函数

该结构只有一个字段，用于将 MSPI 的**收发（Transceive）**请求交给设备仿真器。

| 类型与字段 | 官方说明译文 |
| --- | --- |
| `emul_mspi_dev_api_transceive transceive` | 将 MSPI 收发请求传递给设备仿真器 |

> 译注：字段类型是收发处理函数的类型别名，完整签名由对应类型参考给出。本页没有单独规定同步、异步或缓冲区寿命条件，不应仅凭字段名称推断。

---

[上一章：eSPI仿真驱动API结构](P482_eSPI仿真驱动API结构.md) · [下一章：MSPI仿真驱动API结构](P484_MSPI仿真驱动API结构.md) · [返回大纲](大纲.md)
