---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-19
title: bt_avrcp_app_setting_val_text_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__app__setting__val__text.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_bt\_avrcp\_app\_setting\_val\_text\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__app__setting__val__text.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

音视频远程控制配置文件（Audio/Video Remote Control Profile，AVRCP）的属性文本条目（Attribute Text Entry）。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

音视频远程控制配置文件（Audio/Video Remote Control Profile，AVRCP）的属性文本条目（Attribute Text Entry）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_a64c7b1c1fdedea5d8979e2f7b2311446"></a>

```c
uint8_t value_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[value_id](#a64c7b1c1fdedea5d8979e2f7b2311446)。

值 ID。

<a id="r_a1445e315c485a9486339d183db1c76ad"></a>

```c
uint16_t charset_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[charset_id](#a1445e315c485a9486339d183db1c76ad)。

字符集 ID（Charset ID）。

<a id="r_af4d28d332712cd8a07b3dc9e6ee2f0d6"></a>

```c
uint8_t text_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[text_len](#af4d28d332712cd8a07b3dc9e6ee2f0d6)。

文本长度。

<a id="r_a880d2c79a341c575f05f380fadaade7c"></a>

```c
uint8_t text []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[text](#a880d2c79a341c575f05f380fadaade7c)。

文本字符串。

## 19.2\_详细说明（Detailed Documentation）

<a id="a1445e315c485a9486339d183db1c76ad"></a>

### `charset_id`

```c
uint16_t bt_avrcp_app_setting_val_text::charset_id
```

字符集 ID（Charset ID）。

<a id="a880d2c79a341c575f05f380fadaade7c"></a>

### `text`

```c
uint8_t bt_avrcp_app_setting_val_text::text[]
```

文本字符串。

<a id="af4d28d332712cd8a07b3dc9e6ee2f0d6"></a>

### `text_len`

```c
uint8_t bt_avrcp_app_setting_val_text::text_len
```

文本长度。

<a id="a64c7b1c1fdedea5d8979e2f7b2311446"></a>

### `value_id`

```c
uint8_t bt_avrcp_app_setting_val_text::value_id
```

值 ID。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_bt_avrcp_app_setting_attr_val_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_bt_avrcp_change_path_cmd_结构体.md)
