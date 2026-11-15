---
id: learning.zephyr-docs.network-core-model-reference.page-163
title: wifi_btwt_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__btwt__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第163章\_wifi\_btwt\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__btwt__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi广播目标唤醒时间（Broadcast TWT）的参数。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi广播目标唤醒时间（Broadcast TWT）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 163.1\_数据成员（Data Fields）

<a id="r_ae52281d9f53e106fb9ed813131d8085e"></a>

```c
uint8_t btwt_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[btwt_id](#ae52281d9f53e106fb9ed813131d8085e)。

广播目标唤醒时间标识符（Broadcast TWT ID）。

<a id="r_a2c1b3551a714fbf1b948ce4bcf805934"></a>

```c
uint16_t btwt_mantissa
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[btwt_mantissa](#a2c1b3551a714fbf1b948ce4bcf805934)。

广播目标唤醒时间尾数（Broadcast TWT mantissa）。

<a id="r_a76c97bcc132405d6a1a54bcca77054ac"></a>

```c
uint8_t btwt_exponent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[btwt_exponent](#a76c97bcc132405d6a1a54bcca77054ac)。

广播目标唤醒时间指数（Broadcast TWT exponent）。

<a id="r_a0192d3a9334fc55a135206e6b74ea5b5"></a>

```c
uint8_t btwt_nominal_wake
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[btwt_nominal_wake](#a0192d3a9334fc55a135206e6b74ea5b5)。

广播目标唤醒时间范围（Broadcast TWT range）。

## 163.2\_详细说明（Detailed Documentation）

<a id="a76c97bcc132405d6a1a54bcca77054ac"></a>

### `btwt_exponent`

```c
uint8_t wifi_btwt_params::btwt_exponent
```

广播目标唤醒时间指数（Broadcast TWT exponent）。

<a id="ae52281d9f53e106fb9ed813131d8085e"></a>

### `btwt_id`

```c
uint8_t wifi_btwt_params::btwt_id
```

广播目标唤醒时间标识符（Broadcast TWT ID）。

<a id="a2c1b3551a714fbf1b948ce4bcf805934"></a>

### `btwt_mantissa`

```c
uint16_t wifi_btwt_params::btwt_mantissa
```

广播目标唤醒时间尾数（Broadcast TWT mantissa）。

<a id="a0192d3a9334fc55a135206e6b74ea5b5"></a>

### `btwt_nominal_wake`

```c
uint8_t wifi_btwt_params::btwt_nominal_wake
```

广播目标唤醒时间范围（Broadcast TWT range）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 163.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P162_wifi_bgscan_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P164_wifi_channel_info_结构体.md)
