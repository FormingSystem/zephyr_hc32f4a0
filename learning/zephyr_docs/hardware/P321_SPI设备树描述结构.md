---
id: learning.zephyr-docs.hardware.spistruct-2
title: SPI设备树描述结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structspi__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第321章\_SPI设备树描述结构

原文：[structspi__dt__spec](https://docs.zephyrproject.org/latest/doxygen/html/structspi__dt__spec.html)。读取日期：2026-10-13，`latest`。

## 321.1\_完整硬件描述

[`spi_dt_spec`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__dt__spec.html) 保存串行外设接口（Serial Peripheral Interface，SPI）的完整设备树（Devicetree，DT）信息。它将所连接的总线与此外设的专用通信配置放在同一个结构中，声明来自 `zephyr/drivers/spi.h`。

## 321.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a37519633ae787ffaa1026e6867d7007a"></a>[`bus`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__dt__spec.html#a37519633ae787ffaa1026e6867d7007a) | `const struct device *` | SPI 总线设备 |
| <a id="a88372c17ede2e9dfb0c09c49abebf87e"></a>[`config`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__dt__spec.html#a88372c17ede2e9dfb0c09c49abebf87e) | `struct spi_config` | 此外设专用的配置 |

---

[上一章：SPI控制器配置结构](P320_SPI控制器配置结构.md) · [下一章：SPI缓冲区结构](P322_SPI缓冲区结构.md) · [返回大纲](大纲.md)
