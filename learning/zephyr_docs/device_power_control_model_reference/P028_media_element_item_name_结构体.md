---
id: learning.zephyr-docs.device-power-control-model-reference.page-28
title: media_element_item_name_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmedia__element__item__name.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_media\_element\_item\_name\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmedia__element__item__name.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

媒体元素项名称（Media Element Item Name）的结构。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

媒体元素项名称（Media Element Item Name）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_a9ab8705023810277a63566d5b05bc777"></a>

```c
uint16_t charset_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[charset_id](#a9ab8705023810277a63566d5b05bc777)。

名称使用的字符集 ID，参见 `bt_avrcp_charset_t`。

<a id="r_a51866bcc43ed3ed31feb87ac60f97171"></a>

```c
uint16_t name_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[name_len](#a51866bcc43ed3ed31feb87ac60f97171)。

名称长度，单位为字节。

<a id="r_a66b939713a0b4f7aadfbbf65e5b8cef3"></a>

```c
uint8_t name []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[name](#a66b939713a0b4f7aadfbbf65e5b8cef3)。

名称字符串数据。

## 28.2\_详细说明（Detailed Documentation）

<a id="a9ab8705023810277a63566d5b05bc777"></a>

### `charset_id`

```c
uint16_t media_element_item_name::charset_id
```

名称使用的字符集 ID，参见 `bt_avrcp_charset_t`。

<a id="a66b939713a0b4f7aadfbbf65e5b8cef3"></a>

### `name`

```c
uint8_t media_element_item_name::name[]
```

名称字符串数据。

<a id="a51866bcc43ed3ed31feb87ac60f97171"></a>

### `name_len`

```c
uint16_t media_element_item_name::name_len
```

名称长度，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_avrcp_charset_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga81330413af9eba049da6557b14ae082c)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_media_element_item_attr_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_media_proxy_ctrl_cbs_结构体.md)
