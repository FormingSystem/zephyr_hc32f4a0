---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-54
title: bt_avrcp_media_element_item_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__media__element__item.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_bt\_avrcp\_media\_element\_item\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__media__element__item.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

媒体元素条目（Media Element Item），`item_type = 0x03`。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

媒体元素条目（Media Element Item），`item_type = 0x03`。`data` 字段包含 `struct media_element_item_name`，其中依次为字符集、`name_len` 和 `name[]`；其后紧接 `struct media_element_item_attr`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_afe49a107dd657a16336087d2d518f1a7"></a>

```c
struct bt_avrcp_item_hdr hdr
```

相关声明：[bt_avrcp_item_hdr](P049_bt_avrcp_item_hdr_结构体.md)、[hdr](#afe49a107dd657a16336087d2d518f1a7)。

<a id="r_ac0c12c790e4544eaec7d5766969ff152"></a>

```c
uint8_t uid [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uid](#ac0c12c790e4544eaec7d5766969ff152)。

64 位元素 UID。

<a id="r_a1695ec1cf7ff0b5f379d31f5137c893a"></a>

```c
uint8_t media_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[media_type](#a1695ec1cf7ff0b5f379d31f5137c893a)。

媒体类型 `bt_avrcp_media_type_t`。

<a id="r_a198a755a9f0c6ff88f139ac0911ed54d"></a>

```c
uint8_t data []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a198a755a9f0c6ff88f139ac0911ed54d)。

用于名称与属性的柔性数组（Flexible Array）。

## 54.2\_详细说明（Detailed Documentation）

<a id="a198a755a9f0c6ff88f139ac0911ed54d"></a>

### `data`

```c
uint8_t bt_avrcp_media_element_item::data[]
```

用于名称与属性的柔性数组（Flexible Array）。

<a id="afe49a107dd657a16336087d2d518f1a7"></a>

### `hdr`

```c
struct bt_avrcp_item_hdr bt_avrcp_media_element_item::hdr
```

<a id="a1695ec1cf7ff0b5f379d31f5137c893a"></a>

### `media_type`

```c
uint8_t bt_avrcp_media_element_item::media_type
```

媒体类型 `bt_avrcp_media_type_t`。

<a id="ac0c12c790e4544eaec7d5766969ff152"></a>

### `uid`

```c
uint8_t bt_avrcp_media_element_item::uid[8]
```

64 位元素 UID。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [bt_avrcp_item_hdr](P049_bt_avrcp_item_hdr_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_media_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac927c7e7c59f6f0e6243ca0887945d5a)
- [media_element_item_name](https://docs.zephyrproject.org/latest/doxygen/html/structmedia__element__item__name.html)
- [media_element_item_attr](https://docs.zephyrproject.org/latest/doxygen/html/structmedia__element__item__attr.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_bt_avrcp_media_attr_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_bt_avrcp_media_player_item_结构体.md)
