---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-17
title: bt_avrcp_app_setting_attr_text_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__app__setting__attr__text.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_bt\_avrcp\_app\_setting\_attr\_text\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__app__setting__attr__text.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

音视频远程控制配置文件（Audio/Video Remote Control Profile，AVRCP）的属性文本条目（Attribute Text Entry）。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

音视频远程控制配置文件（Audio/Video Remote Control Profile，AVRCP）的属性文本条目（Attribute Text Entry）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_a38306c0921d308a9127befe8b14b2780"></a>

```c
uint8_t attr_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[attr_id](#a38306c0921d308a9127befe8b14b2780)。

属性 ID。

<a id="r_ac135cdad9f6db11162f11078a5a88f08"></a>

```c
uint16_t charset_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[charset_id](#ac135cdad9f6db11162f11078a5a88f08)。

字符集 ID（Charset ID）。

<a id="r_aa2fc3a684134034a6e34b72d8aed2d94"></a>

```c
uint8_t text_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[text_len](#aa2fc3a684134034a6e34b72d8aed2d94)。

文本长度。

<a id="r_a2e3311b3067919aa8feacf24c6a4e37d"></a>

```c
uint8_t text []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[text](#a2e3311b3067919aa8feacf24c6a4e37d)。

文本字符串。

## 17.2\_详细说明（Detailed Documentation）

<a id="a38306c0921d308a9127befe8b14b2780"></a>

### `attr_id`

```c
uint8_t bt_avrcp_app_setting_attr_text::attr_id
```

属性 ID。

<a id="ac135cdad9f6db11162f11078a5a88f08"></a>

### `charset_id`

```c
uint16_t bt_avrcp_app_setting_attr_text::charset_id
```

字符集 ID（Charset ID）。

<a id="a2e3311b3067919aa8feacf24c6a4e37d"></a>

### `text`

```c
uint8_t bt_avrcp_app_setting_attr_text::text[]
```

文本字符串。

<a id="aa2fc3a684134034a6e34b72d8aed2d94"></a>

### `text_len`

```c
uint8_t bt_avrcp_app_setting_attr_text::text_len
```

文本长度。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_bt_avrcp_add_to_now_playing_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_bt_avrcp_app_setting_attr_val_结构体.md)
