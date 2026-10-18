---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-46
title: bt_avrcp_get_total_number_of_items_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__total__number__of__items__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_bt\_avrcp\_get\_total\_number\_of\_items\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__total__number__of__items__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取条目总数（GetTotalNumberOfItems）响应。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取条目总数（GetTotalNumberOfItems）响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_a7717d866cd7ea275015309b5c8128b2b"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a7717d866cd7ea275015309b5c8128b2b)。

状态类型 `bt_avrcp_status_t`。

<a id="r_a6f1686ad482eb271bfcdfaf27a7c5f56"></a>

```c
uint16_t uid_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uid_counter](#a6f1686ad482eb271bfcdfaf27a7c5f56)。

UID 计数器（UID Counter）。

<a id="r_ab1d378b127df00c87593187a8ec25765"></a>

```c
uint32_t num_items
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_items](#ab1d378b127df00c87593187a8ec25765)。

指定作用域内的条目总数。

## 46.2\_详细说明（Detailed Documentation）

<a id="ab1d378b127df00c87593187a8ec25765"></a>

### `num_items`

```c
uint32_t bt_avrcp_get_total_number_of_items_rsp::num_items
```

指定作用域内的条目总数。

<a id="a7717d866cd7ea275015309b5c8128b2b"></a>

### `status`

```c
uint8_t bt_avrcp_get_total_number_of_items_rsp::status
```

状态类型 `bt_avrcp_status_t`。

<a id="a6f1686ad482eb271bfcdfaf27a7c5f56"></a>

### `uid_counter`

```c
uint16_t bt_avrcp_get_total_number_of_items_rsp::uid_counter
```

UID 计数器（UID Counter）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 46.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga52368f4cc655bab75f96da80ddaaabe0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_bt_avrcp_get_total_number_of_items_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_bt_avrcp_inform_batt_status_of_ct_cmd_结构体.md)
