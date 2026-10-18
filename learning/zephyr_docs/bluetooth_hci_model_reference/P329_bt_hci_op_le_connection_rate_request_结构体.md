---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-329
title: bt_hci_op_le_connection_rate_request_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__op__le__connection__rate__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第329章\_bt\_hci\_op\_le\_connection\_rate\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__op__le__connection__rate__request.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 329.1\_数据成员（Data Fields）

<a id="r_a7178c6af0cdbf1376bd3e52a175be03e"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a7178c6af0cdbf1376bd3e52a175be03e)。

<a id="r_aee4d2070f12c33c5c6f6d93435f1f4b5"></a>

```c
uint16_t conn_interval_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_interval_min](#aee4d2070f12c33c5c6f6d93435f1f4b5)。

<a id="r_ae290b39a2ba9c37595de67b877a61f3b"></a>

```c
uint16_t conn_interval_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_interval_max](#ae290b39a2ba9c37595de67b877a61f3b)。

<a id="r_ab06f3b29db55a6f56ab8cc1f2e7b95df"></a>

```c
uint16_t subrate_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_min](#ab06f3b29db55a6f56ab8cc1f2e7b95df)。

<a id="r_a5ac425326df618f446bc891ea0b329ec"></a>

```c
uint16_t subrate_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_max](#a5ac425326df618f446bc891ea0b329ec)。

<a id="r_a35033b89faecdaa053e8bcff590ad5e7"></a>

```c
uint16_t max_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_latency](#a35033b89faecdaa053e8bcff590ad5e7)。

<a id="r_aa1123f8a8eafa16785e440b8b8a7e885"></a>

```c
uint16_t continuation_number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[continuation_number](#aa1123f8a8eafa16785e440b8b8a7e885)。

<a id="r_a523cde9caf261ca3f3766b4d9648c7eb"></a>

```c
uint16_t supervision_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supervision_timeout](#a523cde9caf261ca3f3766b4d9648c7eb)。

<a id="r_a87ad44b9857515b42aff8200cfb42b37"></a>

```c
uint16_t min_ce_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_ce_len](#a87ad44b9857515b42aff8200cfb42b37)。

<a id="r_af63ff615adc36c422d6be8db20e45c85"></a>

```c
uint16_t max_ce_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_ce_len](#af63ff615adc36c422d6be8db20e45c85)。

## 329.2\_详细说明（Detailed Documentation）

<a id="ae290b39a2ba9c37595de67b877a61f3b"></a>

### `conn_interval_max`

```c
uint16_t bt_hci_op_le_connection_rate_request::conn_interval_max
```

<a id="aee4d2070f12c33c5c6f6d93435f1f4b5"></a>

### `conn_interval_min`

```c
uint16_t bt_hci_op_le_connection_rate_request::conn_interval_min
```

<a id="aa1123f8a8eafa16785e440b8b8a7e885"></a>

### `continuation_number`

```c
uint16_t bt_hci_op_le_connection_rate_request::continuation_number
```

<a id="a7178c6af0cdbf1376bd3e52a175be03e"></a>

### `handle`

```c
uint16_t bt_hci_op_le_connection_rate_request::handle
```

<a id="af63ff615adc36c422d6be8db20e45c85"></a>

### `max_ce_len`

```c
uint16_t bt_hci_op_le_connection_rate_request::max_ce_len
```

<a id="a35033b89faecdaa053e8bcff590ad5e7"></a>

### `max_latency`

```c
uint16_t bt_hci_op_le_connection_rate_request::max_latency
```

<a id="a87ad44b9857515b42aff8200cfb42b37"></a>

### `min_ce_len`

```c
uint16_t bt_hci_op_le_connection_rate_request::min_ce_len
```

<a id="a5ac425326df618f446bc891ea0b329ec"></a>

### `subrate_max`

```c
uint16_t bt_hci_op_le_connection_rate_request::subrate_max
```

<a id="ab06f3b29db55a6f56ab8cc1f2e7b95df"></a>

### `subrate_min`

```c
uint16_t bt_hci_op_le_connection_rate_request::subrate_min
```

<a id="a523cde9caf261ca3f3766b4d9648c7eb"></a>

### `supervision_timeout`

```c
uint16_t bt_hci_op_le_connection_rate_request::supervision_timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 329.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P328_bt_hci_op_inquiry_结构体.md) · [返回大纲](大纲.md) · [下一章](P330_bt_hci_op_le_cs_test_结构体.md)
