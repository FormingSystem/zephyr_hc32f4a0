---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-331
title: bt_hci_op_le_read_min_supported_conn_interval_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__op__le__read__min__supported__conn__interval.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第331章\_bt\_hci\_op\_le\_read\_min\_supported\_conn\_interval\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__op__le__read__min__supported__conn__interval.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 331.1\_数据成员（Data Fields）

<a id="r_aa049350b4f8fafe3bf74780924e1eeff"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#aa049350b4f8fafe3bf74780924e1eeff)。

<a id="r_a0c71077c8e7db5b1bdba1372bc7ac5ac"></a>

```c
uint8_t min_supported_conn_interval
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_supported_conn_interval](#a0c71077c8e7db5b1bdba1372bc7ac5ac)。

<a id="r_a8bd4666fa42fb9a527fca5309e3bf0d6"></a>

```c
uint8_t num_groups
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_groups](#a8bd4666fa42fb9a527fca5309e3bf0d6)。

<a id="r_a92313039960815652380c301d4a5ce8d"></a>

```c
struct bt_hci_le_read_min_supported_conn_interval_group groups []
```

相关声明：[bt_hci_le_read_min_supported_conn_interval_group](P325_bt_hci_le_read_min_supported_conn_interval_group_结构体.md)、[groups](#a92313039960815652380c301d4a5ce8d)。

## 331.2\_详细说明（Detailed Documentation）

<a id="a92313039960815652380c301d4a5ce8d"></a>

### `groups`

```c
struct bt_hci_le_read_min_supported_conn_interval_group bt_hci_op_le_read_min_supported_conn_interval::groups[]
```

<a id="a0c71077c8e7db5b1bdba1372bc7ac5ac"></a>

### `min_supported_conn_interval`

```c
uint8_t bt_hci_op_le_read_min_supported_conn_interval::min_supported_conn_interval
```

<a id="a8bd4666fa42fb9a527fca5309e3bf0d6"></a>

### `num_groups`

```c
uint8_t bt_hci_op_le_read_min_supported_conn_interval::num_groups
```

<a id="aa049350b4f8fafe3bf74780924e1eeff"></a>

### `status`

```c
uint8_t bt_hci_op_le_read_min_supported_conn_interval::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 331.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_le_read_min_supported_conn_interval_group](P325_bt_hci_le_read_min_supported_conn_interval_group_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P330_bt_hci_op_le_cs_test_结构体.md) · [返回大纲](大纲.md) · [下一章](P332_bt_hci_op_le_set_default_rate_parameters_结构体.md)
