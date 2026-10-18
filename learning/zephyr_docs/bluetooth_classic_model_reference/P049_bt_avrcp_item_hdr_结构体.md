---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-49
title: bt_avrcp_item_hdr_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__item__hdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_bt\_avrcp\_item\_hdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__item__hdr.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取文件夹条目（GetFolderItems）响应使用的通用条目头（Common Item Header）。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取文件夹条目（GetFolderItems）响应使用的通用条目头（Common Item Header）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

<a id="r_ac9327e576791370bcb7b2f7140f99ee4"></a>

```c
uint8_t item_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[item_type](#ac9327e576791370bcb7b2f7140f99ee4)。

条目类型 `bt_avrcp_item_type_t`。

<a id="r_aee91353e20e227cdf095153b101bc69a"></a>

```c
uint16_t item_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[item_len](#aee91353e20e227cdf095153b101bc69a)。

此条目剩余字段的长度。

## 49.2\_详细说明（Detailed Documentation）

<a id="aee91353e20e227cdf095153b101bc69a"></a>

### `item_len`

```c
uint16_t bt_avrcp_item_hdr::item_len
```

此条目剩余字段的长度。

<a id="ac9327e576791370bcb7b2f7140f99ee4"></a>

### `item_type`

```c
uint8_t bt_avrcp_item_hdr::item_type
```

条目类型 `bt_avrcp_item_type_t`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_item_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#gac02fed37e267996d4de50b06292d0668)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_bt_avrcp_inform_displayable_char_set_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_bt_avrcp_list_player_app_setting_attrs_rsp_结构体.md)
