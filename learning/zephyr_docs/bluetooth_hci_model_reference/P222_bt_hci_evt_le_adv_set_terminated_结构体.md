---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-222
title: bt_hci_evt_le_adv_set_terminated_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__adv__set__terminated.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第222章\_bt\_hci\_evt\_le\_adv\_set\_terminated\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__adv__set__terminated.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 222.1\_数据成员（Data Fields）

<a id="r_a583409e2dc912af2bd5e83124fce3a72"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a583409e2dc912af2bd5e83124fce3a72)。

<a id="r_af35564406269144cfa2532cd510aa0bd"></a>

```c
uint8_t adv_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_handle](#af35564406269144cfa2532cd510aa0bd)。

<a id="r_af2503ee8e1c9add6927fa65b69c48551"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#af2503ee8e1c9add6927fa65b69c48551)。

<a id="r_a192f13d6223e437261a225e6b28d04db"></a>

```c
uint8_t num_completed_ext_adv_evts
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_completed_ext_adv_evts](#a192f13d6223e437261a225e6b28d04db)。

## 222.2\_详细说明（Detailed Documentation）

<a id="af35564406269144cfa2532cd510aa0bd"></a>

### `adv_handle`

```c
uint8_t bt_hci_evt_le_adv_set_terminated::adv_handle
```

<a id="af2503ee8e1c9add6927fa65b69c48551"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_le_adv_set_terminated::conn_handle
```

<a id="a192f13d6223e437261a225e6b28d04db"></a>

### `num_completed_ext_adv_evts`

```c
uint8_t bt_hci_evt_le_adv_set_terminated::num_completed_ext_adv_evts
```

<a id="a583409e2dc912af2bd5e83124fce3a72"></a>

### `status`

```c
uint8_t bt_hci_evt_le_adv_set_terminated::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 222.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P221_bt_hci_evt_io_capa_resp_结构体.md) · [返回大纲](大纲.md) · [下一章](P223_bt_hci_evt_le_advertising_info_结构体.md)
