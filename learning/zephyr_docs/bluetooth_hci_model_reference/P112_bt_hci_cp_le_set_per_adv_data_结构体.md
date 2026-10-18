---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-112
title: bt_hci_cp_le_set_per_adv_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__per__adv__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第112章\_bt\_hci\_cp\_le\_set\_per\_adv\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__per__adv__data.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 112.1\_数据成员（Data Fields）

<a id="r_a93cbb46ce6664880487e009a0b47af02"></a>

```c
uint8_t handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[handle](#a93cbb46ce6664880487e009a0b47af02)。

<a id="r_aac34596f0970c976c4ef71250d326c2c"></a>

```c
uint8_t op
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[op](#aac34596f0970c976c4ef71250d326c2c)。

<a id="r_ae6ee631a153cb6fed88695e599f63e91"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#ae6ee631a153cb6fed88695e599f63e91)。

<a id="r_adaf581f8db6aafb4dc5df669df7ad26d"></a>

```c
uint8_t data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#adaf581f8db6aafb4dc5df669df7ad26d)。

## 112.2\_详细说明（Detailed Documentation）

<a id="adaf581f8db6aafb4dc5df669df7ad26d"></a>

### `data`

```c
uint8_t bt_hci_cp_le_set_per_adv_data::data[0]
```

<a id="a93cbb46ce6664880487e009a0b47af02"></a>

### `handle`

```c
uint8_t bt_hci_cp_le_set_per_adv_data::handle
```

<a id="ae6ee631a153cb6fed88695e599f63e91"></a>

### `len`

```c
uint8_t bt_hci_cp_le_set_per_adv_data::len
```

<a id="aac34596f0970c976c4ef71250d326c2c"></a>

### `op`

```c
uint8_t bt_hci_cp_le_set_per_adv_data::op
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 112.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md) · [返回大纲](大纲.md) · [下一章](P113_bt_hci_cp_le_set_per_adv_enable_结构体.md)
