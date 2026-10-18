---
id: learning.zephyr-docs.network-application-model-reference.page-3
title: coap_client_option_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__option.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_coap\_client\_option\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__option.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP客户端请求的附加选项（Extra Options）的表示。

```c
#include <zephyr/net/coap_client.h>
```

<a id="details"></a>

CoAP客户端请求的附加选项（Extra Options）的表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a3b0c23802edd7cbb162bff6cfb745bfb"></a>

```c
uint16_t code
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[code](#a3b0c23802edd7cbb162bff6cfb745bfb)。

选项代码（Option Code）。

<a id="r_aebc27705f851af910757f0bb2a73bbe5"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#aebc27705f851af910757f0bb2a73bbe5)。

选项长度（Option Length）。

<a id="r_ac60b63a5fd1e7ba8f1f3d232828c60ae"></a>

```c
uint8_t value [(12)]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[value](#ac60b63a5fd1e7ba8f1f3d232828c60ae)。

用于该长度的缓冲区（Buffer）。

## 3.2\_详细说明（Detailed Documentation）

<a id="a3b0c23802edd7cbb162bff6cfb745bfb"></a>

### `code`

```c
uint16_t coap_client_option::code
```

选项代码（Option Code）。

<a id="aebc27705f851af910757f0bb2a73bbe5"></a>

### `len`

```c
uint8_t coap_client_option::len
```

选项长度（Option Length）。

<a id="ac60b63a5fd1e7ba8f1f3d232828c60ae"></a>

### `value`

```c
uint8_t coap_client_option::value[(12)]
```

用于该长度的缓冲区（Buffer）。

本数据类型文档由以下文件生成：

- `zephyr/net/coap_client.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/net/coap_client.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__client_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_coap_client_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_coap_client_request_结构体.md)
