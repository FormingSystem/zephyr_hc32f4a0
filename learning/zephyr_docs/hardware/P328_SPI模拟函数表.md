---
id: learning.zephyr-docs.hardware.spiback-4
title: SPI模拟函数表
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第328章\_SPI模拟函数表

原文：[structspi__emul__api](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul__api.html)。读取日期：2026-10-13，`latest`。

## 328.1\_模拟器接口定义

[`spi_emul_api`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul__api.html) 定义串行外设接口（Serial Peripheral Interface，SPI）模拟器（Emulator）的应用程序编程接口（Application Programming Interface，API），声明来自 `zephyr/drivers/spi_emul.h`。

## 328.2\_消息操作

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`io`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul__api.html#a357c2c19a5d6eb7a14d895eb9b042085) | [`spi_emul_io_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga034da8d578cd4facdff61ce3afb19487) | 将 SPI 消息传给模拟器 |

该操作使用 SPI 配置与收发缓冲区集合，模拟器通过接收缓冲区返回读到的数据；完整回调签名见 [`spi_emul_io_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga034da8d578cd4facdff61ce3afb19487)。

---

[上一章：SPI模拟器结构](P327_SPI模拟器结构.md) · [下一章：SPI设备树宏](P329_SPI设备树宏.md) · [返回大纲](大纲.md)
