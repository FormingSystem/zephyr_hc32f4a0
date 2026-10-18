---
id: learning.zephyr-docs.network-application-model-reference.page-10
title: coap_option_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__option.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_coap\_option\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__option.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP选项（Option）的表示。

```c
#include <zephyr/net/coap.h>
```

<a id="details"></a>

CoAP选项（Option）的表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_abca15b0a8f9bdcb3f493ab3801d4b58f"></a>

```c
uint16_t delta
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[delta](#abca15b0a8f9bdcb3f493ab3801d4b58f)。

选项增量（Option Delta）。

<a id="r_a01c8abdf27c3f8c5a816af33c0c093d4"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#a01c8abdf27c3f8c5a816af33c0c093d4)。

选项长度（Option Length）。

<a id="r_aff07b5d3673169b6316b91dc27780891"></a>

```c
uint8_t value [12]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[value](#aff07b5d3673169b6316b91dc27780891)。

选项值（Option Value）

## 10.2\_详细说明（Detailed Documentation）

<a id="abca15b0a8f9bdcb3f493ab3801d4b58f"></a>

### `delta`

```c
uint16_t coap_option::delta
```

选项增量（Option Delta）。

<a id="a01c8abdf27c3f8c5a816af33c0c093d4"></a>

### `len`

```c
uint8_t coap_option::len
```

选项长度（Option Length）。

<a id="aff07b5d3673169b6316b91dc27780891"></a>

### `value`

```c
uint8_t coap_option::value[12]
```

选项值（Option Value）

本数据类型文档由以下文件生成：

- `zephyr/net/coap.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_coap_observer_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_coap_oscore_exchange_结构体.md)
