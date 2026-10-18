---
id: learning.zephyr-docs.hardware.emulstruct-5
title: eSPI仿真驱动API结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第482章\_eSPI仿真驱动API结构

原文：[structemul__espi__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__driver__api.html)。读取日期：2026-10-13，`latest`。

`struct emul_espi_driver_api` 定义**增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）**控制器仿真器的**应用程序编程接口（Application Programming Interface，API）**。结构位于 `zephyr/drivers/espi_emul.h`。

## 482.1\_控制器接口字段

原页列出以下三个字段及其类型，没有给出逐字段行为描述。此处完整保留声明顺序。

| 类型 | 字段 |
| --- | --- |
| `struct espi_driver_api` | [`espi_api`](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__driver__api.html#a829c405693c4ef7f558004bc8106342b) |
| [`emul_trigger_event`](P486_eSPI总线仿真接口.md) | [`trigger_event`](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__driver__api.html#a77f9c77cbd2c66e0f8871f94deb7c154) |
| [`emul_find_emul`](P486_eSPI总线仿真接口.md) | [`find_emul`](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__driver__api.html#ac7523c429bc75a99d20a87243b9d1195) |

> 译注：按名称和类型，`espi_api` 承载 eSPI 驱动接口，`trigger_event` 是事件触发接口，`find_emul` 是仿真器查找接口。具体参数和返回值须以相应类型定义为准；本页没有提供函数指针签名，也没有声明这些接口的并发行为。

---

[上一章：eSPI仿真设备API结构](P481_eSPI仿真设备API结构.md) · [下一章：MSPI仿真设备API结构](P483_MSPI仿真设备API结构.md) · [返回大纲](大纲.md)
