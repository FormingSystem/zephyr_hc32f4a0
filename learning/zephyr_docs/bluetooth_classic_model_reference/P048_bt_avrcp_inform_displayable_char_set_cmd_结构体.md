---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-48
title: bt_avrcp_inform_displayable_char_set_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__inform__displayable__char__set__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_bt\_avrcp\_inform\_displayable\_char\_set\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__inform__displayable__char__set__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

通知可显示字符集（InformDisplayableCharacterSet）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

通知可显示字符集（InformDisplayableCharacterSet）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_a157b2006ac2032335cc75cf14a6b4849"></a>

```c
uint8_t num_charsets
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_charsets](#a157b2006ac2032335cc75cf14a6b4849)。

支持的字符集数量。

<a id="r_a1c283439e475592935395c90b372233f"></a>

```c
uint16_t charset_ids []
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[charset_ids](#a1c283439e475592935395c90b372233f)。

字符集 ID 数组。

## 48.2\_详细说明（Detailed Documentation）

<a id="a1c283439e475592935395c90b372233f"></a>

### `charset_ids`

```c
uint16_t bt_avrcp_inform_displayable_char_set_cmd::charset_ids[]
```

字符集 ID 数组。

<a id="a157b2006ac2032335cc75cf14a6b4849"></a>

### `num_charsets`

```c
uint8_t bt_avrcp_inform_displayable_char_set_cmd::num_charsets
```

支持的字符集数量。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 48.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_bt_avrcp_inform_batt_status_of_ct_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_bt_avrcp_item_hdr_结构体.md)
