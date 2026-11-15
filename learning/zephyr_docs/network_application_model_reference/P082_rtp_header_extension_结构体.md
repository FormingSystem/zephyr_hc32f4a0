---
id: learning.zephyr-docs.network-application-model-reference.page-82
title: rtp_header_extension_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtp__header__extension.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_rtp\_header\_extension\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtp__header__extension.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RFC 3550第5.3.1节定义的实时传输协议（RTP）头部扩展。

```c
#include <zephyr/net/rtp.h>
```

<a id="details"></a>

RFC 3550第5.3.1节定义的实时传输协议（RTP）头部扩展。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 82.1\_数据成员（Data Fields）

<a id="r_acdf6aa685045acea96c92ad412eaecb2"></a>

```c
uint16_t definition
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[definition](#acdf6aa685045acea96c92ad412eaecb2)。

由配置文件定义的扩展头标识符（Extension Header Identifier）。

<a id="r_acad1e7923764e9e67b3789898256ae3c"></a>

```c
uint16_t length
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[length](#acad1e7923764e9e67b3789898256ae3c)。

扩展数据（Extension Data）的长度，以32位字为单位。

<a id="r_aaad7a4d30851522e4f3f224df2f31135"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#aaad7a4d30851522e4f3f224df2f31135)。

指向扩展数据（Extension Data）的指针。

## 82.2\_详细说明（Detailed Documentation）

<a id="aaad7a4d30851522e4f3f224df2f31135"></a>

### `data`

```c
uint8_t* rtp_header_extension::data
```

指向扩展数据（Extension Data）的指针。

<a id="acdf6aa685045acea96c92ad412eaecb2"></a>

### `definition`

```c
uint16_t rtp_header_extension::definition
```

由配置文件定义的扩展头标识符（Extension Header Identifier）。

<a id="acad1e7923764e9e67b3789898256ae3c"></a>

### `length`

```c
uint16_t rtp_header_extension::length
```

扩展数据（Extension Data）的长度，以32位字为单位。

本数据类型文档由以下文件生成：

- `zephyr/net/rtp.h`

## 82.3\_原页交叉引用（Cross References）

- [RFC 3550, section-5.3.1](https://datatracker.ietf.org/doc/html/rfc3550#section-5.3.1)
- [zephyr/net/rtp.h](https://docs.zephyrproject.org/latest/doxygen/html/rtp_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P081_rtp_header_结构体.md) · [返回大纲](大纲.md) · [下一章](P083_rtp_packet_结构体.md)
