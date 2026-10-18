---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-110
title: bt_hci_cp_le_set_pawr_subevent_data_element_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__pawr__subevent__data__element.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第110章\_bt\_hci\_cp\_le\_set\_pawr\_subevent\_data\_element\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__pawr__subevent__data__element.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 110.1\_数据成员（Data Fields）

<a id="r_abf33f93f0f1ddf3532c6cae13483ec1e"></a>

```c
uint8_t subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent](#abf33f93f0f1ddf3532c6cae13483ec1e)。

<a id="r_a90178bcd86c1bad0a768f391ce11613f"></a>

```c
uint8_t response_slot_start
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_start](#a90178bcd86c1bad0a768f391ce11613f)。

<a id="r_ad8da1cc672eedf8be8cfc7d0d7ec1b41"></a>

```c
uint8_t response_slot_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_count](#ad8da1cc672eedf8be8cfc7d0d7ec1b41)。

<a id="r_ace5860dfa0f628eaed2b68b171d875da"></a>

```c
uint8_t subevent_data_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_data_length](#ace5860dfa0f628eaed2b68b171d875da)。

<a id="r_a91c975189e409b733ac9a4af5763b12a"></a>

```c
uint8_t subevent_data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_data](#a91c975189e409b733ac9a4af5763b12a)。

## 110.2\_详细说明（Detailed Documentation）

<a id="ad8da1cc672eedf8be8cfc7d0d7ec1b41"></a>

### `response_slot_count`

```c
uint8_t bt_hci_cp_le_set_pawr_subevent_data_element::response_slot_count
```

<a id="a90178bcd86c1bad0a768f391ce11613f"></a>

### `response_slot_start`

```c
uint8_t bt_hci_cp_le_set_pawr_subevent_data_element::response_slot_start
```

<a id="abf33f93f0f1ddf3532c6cae13483ec1e"></a>

### `subevent`

```c
uint8_t bt_hci_cp_le_set_pawr_subevent_data_element::subevent
```

<a id="a91c975189e409b733ac9a4af5763b12a"></a>

### `subevent_data`

```c
uint8_t bt_hci_cp_le_set_pawr_subevent_data_element::subevent_data[0]
```

<a id="ace5860dfa0f628eaed2b68b171d875da"></a>

### `subevent_data_length`

```c
uint8_t bt_hci_cp_le_set_pawr_subevent_data_element::subevent_data_length
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 110.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P109_bt_hci_cp_le_set_pawr_subevent_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md)
