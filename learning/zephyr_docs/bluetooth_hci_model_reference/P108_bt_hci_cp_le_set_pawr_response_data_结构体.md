---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-108
title: bt_hci_cp_le_set_pawr_response_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__pawr__response__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第108章\_bt\_hci\_cp\_le\_set\_pawr\_response\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__pawr__response__data.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 108.1\_数据成员（Data Fields）

<a id="r_a034afaaacf4b2168b9cd54cfde583b5c"></a>

```c
uint16_t sync_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_handle](#a034afaaacf4b2168b9cd54cfde583b5c)。

<a id="r_aaf5c337af93f13e243451b46a94ffb77"></a>

```c
uint16_t request_event
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[request_event](#aaf5c337af93f13e243451b46a94ffb77)。

<a id="r_a675a223891b28f06e78df6223439dc28"></a>

```c
uint8_t request_subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[request_subevent](#a675a223891b28f06e78df6223439dc28)。

<a id="r_aaf2e0eb3b491b5ccd15ba5259fd900c7"></a>

```c
uint8_t response_subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_subevent](#aaf2e0eb3b491b5ccd15ba5259fd900c7)。

<a id="r_a4356344510833196533bb9582f6fe18a"></a>

```c
uint8_t response_slot
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot](#a4356344510833196533bb9582f6fe18a)。

<a id="r_a8c546fa3c6d969d44c54926330e5cf85"></a>

```c
uint8_t response_data_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_data_length](#a8c546fa3c6d969d44c54926330e5cf85)。

<a id="r_a39cbc74ab95881b6dde8fa377d2951e5"></a>

```c
uint8_t response_data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_data](#a39cbc74ab95881b6dde8fa377d2951e5)。

## 108.2\_详细说明（Detailed Documentation）

<a id="aaf5c337af93f13e243451b46a94ffb77"></a>

### `request_event`

```c
uint16_t bt_hci_cp_le_set_pawr_response_data::request_event
```

<a id="a675a223891b28f06e78df6223439dc28"></a>

### `request_subevent`

```c
uint8_t bt_hci_cp_le_set_pawr_response_data::request_subevent
```

<a id="a39cbc74ab95881b6dde8fa377d2951e5"></a>

### `response_data`

```c
uint8_t bt_hci_cp_le_set_pawr_response_data::response_data[0]
```

<a id="a8c546fa3c6d969d44c54926330e5cf85"></a>

### `response_data_length`

```c
uint8_t bt_hci_cp_le_set_pawr_response_data::response_data_length
```

<a id="a4356344510833196533bb9582f6fe18a"></a>

### `response_slot`

```c
uint8_t bt_hci_cp_le_set_pawr_response_data::response_slot
```

<a id="aaf2e0eb3b491b5ccd15ba5259fd900c7"></a>

### `response_subevent`

```c
uint8_t bt_hci_cp_le_set_pawr_response_data::response_subevent
```

<a id="a034afaaacf4b2168b9cd54cfde583b5c"></a>

### `sync_handle`

```c
uint16_t bt_hci_cp_le_set_pawr_response_data::sync_handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 108.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md) · [返回大纲](大纲.md) · [下一章](P109_bt_hci_cp_le_set_pawr_subevent_data_结构体.md)
