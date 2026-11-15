---
id: learning.zephyr-docs.network-core-model-reference.page-18
title: ieee802154_frame_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__frame__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_ieee802154\_frame\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__frame__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

构造MAC帧的参数，包括地址和个人区域网（PAN）标识。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

构造MAC帧所用的参数，包括地址和PAN标识。以CPU字节序保存目的地址及本地寻址信息，供协议栈使用；注明之处的扩展地址按线上格式采用大端序（Big Endian）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

```c
struct {
```

```c
union {
```

<a id="r_a4837bfd479ec189a2508566af2ef2d09"></a>

```c
uint8_t ext_addr [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ext_addr](#a410afc9ab9d85c0bb04de122ceabc38e)。

扩展目的地址（Extended Destination Address），空口采用大端序。

<a id="r_a799c8ad4ce60e71e836513ced9123b0b"></a>

```c
uint16_t short_addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[short_addr](#af914ce32e424fb747d421862a5a125b6)。

短目的地址（Short Destination Address），采用CPU字节序。

<a id="r_a109ae84b4698343310b9ecf3f9ada2f1"></a>

```c
}
```

构造帧所用的目的地址（Destination Address）。

<a id="r_a552c41005cfc081423162cd83e5cdb39"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#ad45f0ac29e589c03905e7ecdcc0e38a6)。

当前使用的目的地址字段（Destination Address Field）的长度。

<a id="r_a3e04b53554185356765974f403f92c04"></a>

```c
uint16_t pan_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pan_id](#aaef4ec5c7a17547b416121d5e9ffb12c)。

目的个人区域网标识（Destination PAN Identifier），采用CPU字节序。

<a id="r_a9e1e16dfa5f5b093273c967910a89ee4"></a>

```c
} dst
```

相关声明：[dst](#a9e1e16dfa5f5b093273c967910a89ee4)。

目的寻址信息（Destination Addressing）。

## 18.2\_详细说明（Detailed Documentation）

<a id="a9e1e16dfa5f5b093273c967910a89ee4"></a>

### `[struct]`

```c
struct { ... } ieee802154_frame_params::dst
```

目的寻址信息（Destination Addressing）。

<a id="a410afc9ab9d85c0bb04de122ceabc38e"></a>

### `ext_addr`

```c
uint8_t ieee802154_frame_params::ext_addr[8]
```

扩展目的地址（Extended Destination Address），空口采用大端序。

<a id="ad45f0ac29e589c03905e7ecdcc0e38a6"></a>

### `len`

```c
uint16_t ieee802154_frame_params::len
```

当前使用的目的地址字段（Destination Address Field）的长度。

<a id="aaef4ec5c7a17547b416121d5e9ffb12c"></a>

### `pan_id`

```c
uint16_t ieee802154_frame_params::pan_id
```

目的个人区域网标识（Destination PAN Identifier），采用CPU字节序。

源个人区域网标识（Source PAN Identifier），采用CPU字节序。

<a id="af914ce32e424fb747d421862a5a125b6"></a>

### `short_addr`

```c
uint16_t ieee802154_frame_params::short_addr
```

短目的地址（Short Destination Address），采用CPU字节序。

本地短地址（Local Short Address），采用CPU字节序。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_ieee802154_filter_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_ieee802154_gts_结构体.md)
