---
id: learning.zephyr-docs.device-power-control-model-reference.page-27
title: media_element_item_attr_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmedia__element__item__attr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_media\_element\_item\_attr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmedia__element__item__attr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

媒体元素项属性（Media Element Item Attributes）的结构。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

媒体元素项属性（Media Element Item Attributes）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_aee96c7d393f086f89e995a96eb95cce9"></a>

```c
uint8_t num_attrs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_attrs](#aee96c7d393f086f89e995a96eb95cce9)。

属性数量。

<a id="r_a00c0f6e1b42a8b6448574105acb0481d"></a>

```c
struct bt_avrcp_media_attr attrs []
```

相关声明：[bt_avrcp_media_attr](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md)、[attrs](#a00c0f6e1b42a8b6448574105acb0481d)。

属性元组（Attribute Tuples），包含 ID／字符集／长度／值（id/charset/len/value）。

## 27.2\_详细说明（Detailed Documentation）

<a id="a00c0f6e1b42a8b6448574105acb0481d"></a>

### `attrs`

```c
struct bt_avrcp_media_attr media_element_item_attr::attrs[]
```

属性元组（Attribute Tuples），包含 ID／字符集／长度／值（id/charset/len/value）。

<a id="aee96c7d393f086f89e995a96eb95cce9"></a>

### `num_attrs`

```c
uint8_t media_element_item_attr::num_attrs
```

属性数量。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_media_attr](../bluetooth_classic_model_reference/P053_bt_avrcp_media_attr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_mb_image_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_media_element_item_name_结构体.md)
