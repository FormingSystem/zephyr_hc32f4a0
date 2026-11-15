---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-145
title: bt_hci_cp_mesh_set_scan_filter_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__mesh__set__scan__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第145章\_bt\_hci\_cp\_mesh\_set\_scan\_filter\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__mesh__set__scan__filter.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 145.1\_数据成员（Data Fields）

<a id="r_aa1e74c7f4dc39cf2ad0c130bf8dafa72"></a>

```c
uint8_t scan_filter
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scan_filter](#aa1e74c7f4dc39cf2ad0c130bf8dafa72)。

<a id="r_a41737323ab5723ce781f77f5752915e3"></a>

```c
uint8_t filter_dup
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter_dup](#a41737323ab5723ce781f77f5752915e3)。

<a id="r_a3f99242946f3a5a8322a8333d9c58b30"></a>

```c
uint8_t num_patterns
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_patterns](#a3f99242946f3a5a8322a8333d9c58b30)。

<a id="r_a4e72bcfac1beec704d860034abcf22c0"></a>

```c
struct bt_hci_mesh_pattern patterns [0]
```

相关声明：[bt_hci_mesh_pattern](P327_bt_hci_mesh_pattern_结构体.md)、[patterns](#a4e72bcfac1beec704d860034abcf22c0)。

## 145.2\_详细说明（Detailed Documentation）

<a id="a41737323ab5723ce781f77f5752915e3"></a>

### `filter_dup`

```c
uint8_t bt_hci_cp_mesh_set_scan_filter::filter_dup
```

<a id="a3f99242946f3a5a8322a8333d9c58b30"></a>

### `num_patterns`

```c
uint8_t bt_hci_cp_mesh_set_scan_filter::num_patterns
```

<a id="a4e72bcfac1beec704d860034abcf22c0"></a>

### `patterns`

```c
struct bt_hci_mesh_pattern bt_hci_cp_mesh_set_scan_filter::patterns[0]
```

<a id="aa1e74c7f4dc39cf2ad0c130bf8dafa72"></a>

### `scan_filter`

```c
uint8_t bt_hci_cp_mesh_set_scan_filter::scan_filter
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 145.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_mesh_pattern](P327_bt_hci_mesh_pattern_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P144_bt_hci_cp_mesh_advertise_timed_结构体.md) · [返回大纲](大纲.md) · [下一章](P146_bt_hci_cp_mesh_set_scanning_结构体.md)
