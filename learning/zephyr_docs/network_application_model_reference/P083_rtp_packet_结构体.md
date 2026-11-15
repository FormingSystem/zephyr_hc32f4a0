---
id: learning.zephyr-docs.network-application-model-reference.page-83
title: rtp_packet_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtp__packet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第83章\_rtp\_packet\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtp__packet.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

头部与载荷已分离的解码后RTP数据包（Packet）。

```c
#include <zephyr/net/rtp.h>
```

<a id="details"></a>

头部与载荷已分离的解码后RTP数据包（Packet）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 83.1\_数据成员（Data Fields）

<a id="r_a5fd40a8d15441f4aa22c989ad3a086af"></a>

```c
struct rtp_header header
```

相关声明：[rtp_header](P081_rtp_header_结构体.md)、[header](#a5fd40a8d15441f4aa22c989ad3a086af)。

已解析的RTP头部（Header）。

<a id="r_a4e7aa001830c27540830fae728d468a6"></a>

```c
uint8_t * payload
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[payload](#a4e7aa001830c27540830fae728d468a6)。

指向数据包载荷（Packet Payload）的指针。

<a id="r_ab6b88aae97f87c11089cdd70f24c722f"></a>

```c
size_t payload_len
```

相关声明：[payload_len](#ab6b88aae97f87c11089cdd70f24c722f)。

载荷（Payload）的长度，单位为字节。

## 83.2\_详细说明（Detailed Documentation）

<a id="a5fd40a8d15441f4aa22c989ad3a086af"></a>

### `header`

```c
struct rtp_header rtp_packet::header
```

已解析的RTP头部（Header）。

<a id="a4e7aa001830c27540830fae728d468a6"></a>

### `payload`

```c
uint8_t* rtp_packet::payload
```

指向数据包载荷（Packet Payload）的指针。

仅在接收回调（Receive Callback）执行期间有效。

<a id="ab6b88aae97f87c11089cdd70f24c722f"></a>

### `payload_len`

```c
size_t rtp_packet::payload_len
```

载荷（Payload）的长度，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/net/rtp.h`

## 83.3\_原页交叉引用（Cross References）

- [zephyr/net/rtp.h](https://docs.zephyrproject.org/latest/doxygen/html/rtp_8h_source.html)
- [rtp_header](P081_rtp_header_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P082_rtp_header_extension_结构体.md) · [返回大纲](大纲.md) · [下一章](P084_rtp_session_结构体.md)
