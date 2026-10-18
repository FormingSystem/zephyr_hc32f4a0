---
id: learning.zephyr-docs.network-application-model-reference.page-31
title: http_hpack_header_buf_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__hpack__header__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_http\_hpack\_header\_buf\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__hpack__header__buf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

带解码缓冲区（Decoding Buffer）的HTTP/2头部字段。

```c
#include <zephyr/net/http/hpack.h>
```

<a id="details"></a>

带解码缓冲区（Decoding Buffer）的HTTP/2头部字段。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_ac0b781b733a16dc0c9e99753a4d2b25d"></a>

```c
const char * name
```

相关声明：[name](#ac0b781b733a16dc0c9e99753a4d2b25d)。

指向解码后头部字段名称（Header Field Name）的指针。

<a id="r_a957db215f89359b64a76e98e878e8c83"></a>

```c
const char * value
```

相关声明：[value](#a957db215f89359b64a76e98e878e8c83)。

指向解码后头部字段值（Header Field Value）的指针。

<a id="r_ad6079192782eec8e4a0c1d89018c6d7b"></a>

```c
size_t name_len
```

相关声明：[name_len](#ad6079192782eec8e4a0c1d89018c6d7b)。

解码后头部字段名称（Header Field Name）的长度。

<a id="r_a48291a396efc761d85ffb5f46ddddf07"></a>

```c
size_t value_len
```

相关声明：[value_len](#a48291a396efc761d85ffb5f46ddddf07)。

解码后头部字段值（Header Field Value）的长度。

<a id="r_a6d1d09942d85f148e3979cf88f1cb87a"></a>

```c
uint8_t buf [HTTP_SERVER_HUFFMAN_DECODE_BUFFER_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf](#a6d1d09942d85f148e3979cf88f1cb87a)。

编码/解码缓冲区（Encoding / Decoding Buffer）。

<a id="r_a9d1c7d2daaf55f201c03e7438b033abf"></a>

```c
size_t datalen
```

相关声明：[datalen](#a9d1c7d2daaf55f201c03e7438b033abf)。

解码缓冲区（Decoding Buffer）中的数据长度。

## 31.2\_详细说明（Detailed Documentation）

<a id="a6d1d09942d85f148e3979cf88f1cb87a"></a>

### `buf`

```c
uint8_t http_hpack_header_buf::buf[HTTP_SERVER_HUFFMAN_DECODE_BUFFER_SIZE]
```

编码/解码缓冲区（Encoding / Decoding Buffer）。

与霍夫曼编码/解码（Huffman Encoding / Decoding）一起使用。

<a id="a9d1c7d2daaf55f201c03e7438b033abf"></a>

### `datalen`

```c
size_t http_hpack_header_buf::datalen
```

解码缓冲区（Decoding Buffer）中的数据长度。

<a id="ac0b781b733a16dc0c9e99753a4d2b25d"></a>

### `name`

```c
const char* http_hpack_header_buf::name
```

指向解码后头部字段名称（Header Field Name）的指针。

<a id="ad6079192782eec8e4a0c1d89018c6d7b"></a>

### `name_len`

```c
size_t http_hpack_header_buf::name_len
```

解码后头部字段名称（Header Field Name）的长度。

<a id="a957db215f89359b64a76e98e878e8c83"></a>

### `value`

```c
const char* http_hpack_header_buf::value
```

指向解码后头部字段值（Header Field Value）的指针。

<a id="a48291a396efc761d85ffb5f46ddddf07"></a>

### `value_len`

```c
size_t http_hpack_header_buf::value_len
```

解码后头部字段值（Header Field Value）的长度。

本数据类型文档由以下文件生成：

- `zephyr/net/http/hpack.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/net/http/hpack.h](https://docs.zephyrproject.org/latest/doxygen/html/hpack_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_http_header_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_http_parser_结构体.md)
