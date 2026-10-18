---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-21
title: lin_driver_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlin__driver__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_lin\_driver\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlin__driver__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用LIN驱动配置结构。

```c
#include <zephyr/drivers/lin.h>
```

<a id="details"></a>

通用 LIN 驱动配置结构体（Driver configuration structure）。此结构体用于配置 LIN 设备，应作为 `device` 结构体的 `config` 字段所指对象的第一个成员。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_af62ec3ddcc7c42281e0d6cf9758645f7"></a>

```c
const struct device * phy
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[phy](#af62ec3ddcc7c42281e0d6cf9758645f7)。

指向关联 LIN 收发器（Transceiver）设备结构体的指针，或 `NULL`。

<a id="r_a561b88e59156f48fb5694cf4f00ed2ea"></a>

```c
uint32_t min_bitrate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_bitrate](#a561b88e59156f48fb5694cf4f00ed2ea)。

LIN 控制器与收发器组合支持的最低位速率（Bitrate）。

<a id="r_ae26b0452f7aa43f8f710647a6f00ea67"></a>

```c
uint32_t max_bitrate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_bitrate](#ae26b0452f7aa43f8f710647a6f00ea67)。

LIN 控制器与收发器组合支持的最高位速率。

<a id="r_a6affbea0028b2c0876f74ff9397b41df"></a>

```c
uint32_t bitrate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bitrate](#a6affbea0028b2c0876f74ff9397b41df)。

初始 LIN 位速率。

## 21.2\_详细说明（Detailed Documentation）

<a id="a6affbea0028b2c0876f74ff9397b41df"></a>

### `bitrate`

```c
uint32_t lin_driver_config::bitrate
```

初始 LIN 位速率。

<a id="ae26b0452f7aa43f8f710647a6f00ea67"></a>

### `max_bitrate`

```c
uint32_t lin_driver_config::max_bitrate
```

LIN 控制器与收发器组合支持的最高位速率。

<a id="a561b88e59156f48fb5694cf4f00ed2ea"></a>

### `min_bitrate`

```c
uint32_t lin_driver_config::min_bitrate
```

LIN 控制器与收发器组合支持的最低位速率（Bitrate）。

<a id="af62ec3ddcc7c42281e0d6cf9758645f7"></a>

### `phy`

```c
const struct device* lin_driver_config::phy
```

指向关联 LIN 收发器（Transceiver）设备结构体的指针，或 `NULL`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/lin.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/drivers/lin.h](https://docs.zephyrproject.org/latest/doxygen/html/lin_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_lin_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_lin_driver_data_结构体.md)
