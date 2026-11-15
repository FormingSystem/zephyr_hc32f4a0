---
id: learning.zephyr-docs.network-application-model-reference.page-13
title: coap_packet_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__packet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_coap\_packet\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__packet.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP数据包（Packet）的表示。

```c
#include <zephyr/net/coap.h>
```

<a id="details"></a>

CoAP数据包（Packet）的表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_a8116711bcdff1fa6b0cf5c4fa9ab88d1"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a8116711bcdff1fa6b0cf5c4fa9ab88d1)。

用户分配的缓冲区（Buffer）。

<a id="r_a46c0842c785b8de5eb8564950a786c02"></a>

```c
uint16_t offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[offset](#a46c0842c785b8de5eb8564950a786c02)。

添加数据时，由CoAP库维护偏移量（Offset）。

<a id="r_a48c216a7da37e85942d271c85a79bcb6"></a>

```c
uint16_t max_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_len](#a48c216a7da37e85942d271c85a79bcb6)。

CoAP数据包的最大数据长度。

<a id="r_ab302c002da88f6d3a44c3a2215082be4"></a>

```c
uint8_t hdr_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hdr_len](#ab302c002da88f6d3a44c3a2215082be4)。

CoAP头部长度（Header Length）。

<a id="r_acc5542ba2a69db8957155b90e75fd563"></a>

```c
uint16_t opt_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[opt_len](#acc5542ba2a69db8957155b90e75fd563)。

全部选项的总长度，即增量、长度和值（Delta + Length + Value）的总和。

<a id="r_a95dd8c6fb08ac61a1571c84258579475"></a>

```c
uint16_t delta
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[delta](#a95dd8c6fb08ac61a1571c84258579475)。

用于CoAP数据包中的增量计算（Delta Calculation）。

<a id="r_ab4c2196669f38bf3057e83c44c839ff4"></a>

```c
void * user_data
```

相关声明：[user_data](#ab4c2196669f38bf3057e83c44c839ff4)。

应用专用用户数据（Application Specific User Data）。

<a id="r_ab496dabc7cc0d9b588d7b1bfdd6967dc"></a>

```c
struct coap_oscore_context * oscore_ctx
```

相关声明：[oscore_ctx](#ab496dabc7cc0d9b588d7b1bfdd6967dc)。

数据包（Packet）接收时受OSCORE保护，则非NULL。

## 13.2\_详细说明（Detailed Documentation）

<a id="a8116711bcdff1fa6b0cf5c4fa9ab88d1"></a>

### `data`

```c
uint8_t* coap_packet::data
```

用户分配的缓冲区（Buffer）。

<a id="a95dd8c6fb08ac61a1571c84258579475"></a>

### `delta`

```c
uint16_t coap_packet::delta
```

用于CoAP数据包中的增量计算（Delta Calculation）。

<a id="ab302c002da88f6d3a44c3a2215082be4"></a>

### `hdr_len`

```c
uint8_t coap_packet::hdr_len
```

CoAP头部长度（Header Length）。

<a id="a48c216a7da37e85942d271c85a79bcb6"></a>

### `max_len`

```c
uint16_t coap_packet::max_len
```

CoAP数据包的最大数据长度。

<a id="a46c0842c785b8de5eb8564950a786c02"></a>

### `offset`

```c
uint16_t coap_packet::offset
```

添加数据时，由CoAP库维护偏移量（Offset）。

<a id="acc5542ba2a69db8957155b90e75fd563"></a>

### `opt_len`

```c
uint16_t coap_packet::opt_len
```

全部选项的总长度，即增量、长度和值（Delta + Length + Value）的总和。

<a id="ab496dabc7cc0d9b588d7b1bfdd6967dc"></a>

### `oscore_ctx`

```c
struct coap_oscore_context* coap_packet::oscore_ctx
```

数据包（Packet）接收时受OSCORE保护，则非NULL。

**注意（Attention）**：注意（Attention）：仅在启用Kconfig选项CONFIG_COAP_OSCORE时可用。

<a id="ab4c2196669f38bf3057e83c44c839ff4"></a>

### `user_data`

```c
void* coap_packet::user_data
```

应用专用用户数据（Application Specific User Data）。

**注意（Attention）**：注意（Attention）：仅在启用Kconfig选项CONFIG_COAP_KEEP_USER_DATA时可用。

本数据类型文档由以下文件生成：

- `zephyr/net/coap.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [CONFIG_COAP_OSCORE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE)
- [CONFIG_COAP_KEEP_USER_DATA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_KEEP_USER_DATA)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_coap_oscore_init_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_coap_pending_结构体.md)
