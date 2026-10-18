---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-115
title: bt_le_per_adv_response_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__response__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第115章\_bt\_le\_per\_adv\_response\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__response__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

发送周期广播响应（Periodic Advertising Response）的参数。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

发送周期广播响应的参数（Periodic advertising response parameters）。此结构保存响应周期广播请求时使用的参数，参见 `bt_le_per_adv_set_response_data`。响应在指定子事件和响应时隙（Response slot）发送；事件计数器与子事件计数器用于跟踪该响应对应的请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 115.1\_数据成员（Data Fields）

<a id="r_a1af01d0a027fb8659615874acbd388f9"></a>

```c
uint16_t request_event
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[request_event](#a1af01d0a027fb8659615874acbd388f9)。

所响应请求的周期事件计数器（Periodic event counter）。

<a id="r_a3fc8ab0feb06714b28d22439cce60e41"></a>

```c
uint8_t request_subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[request_subevent](#a3fc8ab0feb06714b28d22439cce60e41)。

所响应请求的子事件计数器（Subevent counter）。

<a id="r_a0cec222d5ba8cc9e20939d441646c913"></a>

```c
uint8_t response_subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_subevent](#a0cec222d5ba8cc9e20939d441646c913)。

应在其中发送响应的子事件（Subevent）。

<a id="r_aea0428083ccd5f4dccc17e494f38b7c3"></a>

```c
uint8_t response_slot
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot](#aea0428083ccd5f4dccc17e494f38b7c3)。

应在其中发送响应的响应时隙（Response slot）。

## 115.2\_详细说明（Detailed Documentation）

<a id="a1af01d0a027fb8659615874acbd388f9"></a>

### `request_event`

```c
uint16_t bt_le_per_adv_response_params::request_event
```

所响应请求的周期事件计数器（Periodic event counter）。

`bt_le_per_adv_sync_recv_info`。

**说明（Note）**：注意（Note）：响应最迟可以在收到请求后的一个周期广播间隔（Periodic interval）内发送。

<a id="a3fc8ab0feb06714b28d22439cce60e41"></a>

### `request_subevent`

```c
uint8_t bt_le_per_adv_response_params::request_subevent
```

所响应请求的子事件计数器（Subevent counter）。

`bt_le_per_adv_sync_recv_info`。

<a id="aea0428083ccd5f4dccc17e494f38b7c3"></a>

### `response_slot`

```c
uint8_t bt_le_per_adv_response_params::response_slot
```

应在其中发送响应的响应时隙（Response slot）。

<a id="a0cec222d5ba8cc9e20939d441646c913"></a>

### `response_subevent`

```c
uint8_t bt_le_per_adv_response_params::response_subevent
```

应在其中发送响应的子事件（Subevent）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 115.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_le_per_adv_set_response_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaae6b8583f7d5457f20b03dccd146425e)
- [bt_le_per_adv_sync_recv_info](P121_bt_le_per_adv_sync_recv_info_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P114_bt_le_per_adv_response_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P116_bt_le_per_adv_subevent_data_params_结构体.md)
