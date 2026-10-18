---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-53
title: bt_avrcp_media_attr_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__media__attr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_bt\_avrcp\_media\_attr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__media__attr.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

AVRCP 媒体属性（Media Attribute）结构体。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

AVRCP 媒体属性（Media Attribute）结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_ae9389f3574be88638cce4e478c532a2b"></a>

```c
uint32_t attr_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[attr_id](#ae9389f3574be88638cce4e478c532a2b)。

媒体属性 ID，参见 `bt_avrcp_media_attr_id_t`。

<a id="r_a48e88ae5b4c448e0fad0325891ed82d1"></a>

```c
uint16_t charset_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[charset_id](#a48e88ae5b4c448e0fad0325891ed82d1)。

字符集 ID，参见 `bt_avrcp_charset_t`。

<a id="r_a07ad1a91103fcec7b69d02b7967f1815"></a>

```c
uint16_t attr_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[attr_len](#a07ad1a91103fcec7b69d02b7967f1815)。

属性值的长度。

<a id="r_af8b744485f601d694fc43ae3e6d8b28a"></a>

```c
uint8_t attr_val []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[attr_val](#af8b744485f601d694fc43ae3e6d8b28a)。

属性值数据。

## 53.2\_详细说明（Detailed Documentation）

<a id="ae9389f3574be88638cce4e478c532a2b"></a>

### `attr_id`

```c
uint32_t bt_avrcp_media_attr::attr_id
```

媒体属性 ID，参见 `bt_avrcp_media_attr_id_t`。

<a id="a07ad1a91103fcec7b69d02b7967f1815"></a>

### `attr_len`

```c
uint16_t bt_avrcp_media_attr::attr_len
```

属性值的长度。

<a id="af8b744485f601d694fc43ae3e6d8b28a"></a>

### `attr_val`

```c
uint8_t bt_avrcp_media_attr::attr_val[]
```

属性值数据。

<a id="a48e88ae5b4c448e0fad0325891ed82d1"></a>

### `charset_id`

```c
uint16_t bt_avrcp_media_attr::charset_id
```

字符集 ID，参见 `bt_avrcp_charset_t`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_avrcp_media_attr_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga0ebc5d2657688b70119e11ac20d24592)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_avrcp_charset_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga81330413af9eba049da6557b14ae082c)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_bt_avrcp_list_player_app_setting_vals_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_bt_avrcp_media_element_item_结构体.md)
