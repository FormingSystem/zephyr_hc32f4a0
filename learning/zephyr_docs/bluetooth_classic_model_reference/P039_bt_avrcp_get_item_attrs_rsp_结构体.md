---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-39
title: bt_avrcp_get_item_attrs_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__item__attrs__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_bt\_avrcp\_get\_item\_attrs\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__item__attrs__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取条目属性（GetItemAttributes）响应。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取条目属性（GetItemAttributes）响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_a0e20dc5a812fe5901ba04d772c625903"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a0e20dc5a812fe5901ba04d772c625903)。

状态类型 `bt_avrcp_status_t`。

<a id="r_a8911f071972b08d9c190e365f63496ea"></a>

```c
uint8_t num_attrs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_attrs](#a8911f071972b08d9c190e365f63496ea)。

属性数量。

<a id="r_a3a9f9dcb6df5de3d0012cd0a33e34a96"></a>

```c
struct bt_avrcp_media_attr attrs []
```

相关声明：[bt_avrcp_media_attr](P053_bt_avrcp_media_attr_结构体.md)、[attrs](#a3a9f9dcb6df5de3d0012cd0a33e34a96)。

属性元组（Attribute Tuples），包含 ID／字符集／长度／值（id/charset/len/value）。

## 39.2\_详细说明（Detailed Documentation）

<a id="a3a9f9dcb6df5de3d0012cd0a33e34a96"></a>

### `attrs`

```c
struct bt_avrcp_media_attr bt_avrcp_get_item_attrs_rsp::attrs[]
```

属性元组（Attribute Tuples），包含 ID／字符集／长度／值（id/charset/len/value）。

<a id="a8911f071972b08d9c190e365f63496ea"></a>

### `num_attrs`

```c
uint8_t bt_avrcp_get_item_attrs_rsp::num_attrs
```

属性数量。

<a id="a0e20dc5a812fe5901ba04d772c625903"></a>

### `status`

```c
uint8_t bt_avrcp_get_item_attrs_rsp::status
```

状态类型 `bt_avrcp_status_t`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 39.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga52368f4cc655bab75f96da80ddaaabe0)
- [bt_avrcp_media_attr](P053_bt_avrcp_media_attr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_bt_avrcp_get_item_attrs_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_bt_avrcp_get_play_status_rsp_结构体.md)
