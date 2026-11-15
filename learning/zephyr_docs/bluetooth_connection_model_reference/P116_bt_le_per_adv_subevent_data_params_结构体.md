---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-116
title: bt_le_per_adv_subevent_data_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__subevent__data__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第116章\_bt\_le\_per\_adv\_subevent\_data\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__subevent__data__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

为特定带响应周期广播（PAwR）子事件设置数据的参数。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

为特定带响应周期广播子事件设置数据的参数（Periodic advertising with response subevent data parameters）。此结构提供在带响应的周期广播（PAwR）场景下，为特定子事件设置数据所需的信息：子事件编号、要监听的响应时隙范围以及实际待发送数据。用于在指定子事件中发送回数据，以响应广播器的数据请求。注意（Note）：用于 `bt_le_per_adv_set_subevent_data` 函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 116.1\_数据成员（Data Fields）

<a id="r_a55f2da6041b538b3bc4bff38cd4d2953"></a>

```c
uint8_t subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent](#a55f2da6041b538b3bc4bff38cd4d2953)。

要为其设置数据的子事件（Subevent）。

<a id="r_a1354e9505239de3c42969138d719d775"></a>

```c
uint8_t response_slot_start
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_start](#a1354e9505239de3c42969138d719d775)。

要监听的首个响应时隙（First response slot）。

<a id="r_a86d858606943a82917835a0172e88663"></a>

```c
uint8_t response_slot_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_count](#a86d858606943a82917835a0172e88663)。

要监听的响应时隙数量（Number of response slots）。

<a id="r_a46103c988d8ac360b7e26310a0322b4e"></a>

```c
const struct net_buf_simple * data
```

相关声明：[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[data](#a46103c988d8ac360b7e26310a0322b4e)。

要发送的数据（Data）。

## 116.2\_详细说明（Detailed Documentation）

<a id="a46103c988d8ac360b7e26310a0322b4e"></a>

### `data`

```c
const struct net_buf_simple* bt_le_per_adv_subevent_data_params::data
```

要发送的数据（Data）。

<a id="a86d858606943a82917835a0172e88663"></a>

### `response_slot_count`

```c
uint8_t bt_le_per_adv_subevent_data_params::response_slot_count
```

要监听的响应时隙数量（Number of response slots）。

<a id="a1354e9505239de3c42969138d719d775"></a>

### `response_slot_start`

```c
uint8_t bt_le_per_adv_subevent_data_params::response_slot_start
```

要监听的首个响应时隙（First response slot）。

<a id="a55f2da6041b538b3bc4bff38cd4d2953"></a>

### `subevent`

```c
uint8_t bt_le_per_adv_subevent_data_params::subevent
```

要为其设置数据的子事件（Subevent）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 116.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_le_per_adv_set_subevent_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7de30fe5040b85bb9212e3a8fec4ac45)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P115_bt_le_per_adv_response_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P117_bt_le_per_adv_sync_结构体.md)
