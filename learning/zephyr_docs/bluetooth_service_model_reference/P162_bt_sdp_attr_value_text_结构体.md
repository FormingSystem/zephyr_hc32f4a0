---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-162
title: bt_sdp_attr_value_text_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attr__value__text.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第162章\_bt\_sdp\_attr\_value\_text\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attr__value__text.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务发现协议（SDP）文本字符串类型的属性值。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

文本字符串类型的 SDP 属性值。此结构体保存从 SDP 属性中解析出的文本字符串值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 162.1\_数据成员（Data Fields）

<a id="r_a89161e7cfe2185b16b2e114b85209621"></a>

```c
uint32_t len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[len](#a89161e7cfe2185b16b2e114b85209621)。

文本字符串的长度，单位为字节。

<a id="r_a440091666ca041db641c709ed172ba2d"></a>

```c
uint8_t * text
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[text](#a440091666ca041db641c709ed172ba2d)。

指向文本字符串数据的指针。

## 162.2\_详细说明（Detailed Documentation）

<a id="a89161e7cfe2185b16b2e114b85209621"></a>

### `len`

```c
uint32_t bt_sdp_attr_value_text::len
```

文本字符串的长度，单位为字节。

<a id="a440091666ca041db641c709ed172ba2d"></a>

### `text`

```c
uint8_t* bt_sdp_attr_value_text::text
```

指向文本字符串数据的指针。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 162.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P161_bt_sdp_attr_value_pair_结构体.md) · [返回大纲](大纲.md) · [下一章](P163_bt_sdp_attr_value_uint_结构体.md)
