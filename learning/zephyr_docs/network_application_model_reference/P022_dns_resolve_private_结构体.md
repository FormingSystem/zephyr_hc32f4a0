---
id: learning.zephyr-docs.network-application-model-reference.page-22
title: dns_resolve_private_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__private.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_dns\_resolve\_private\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__private.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

私有资源记录（RR）的信息。

```c
#include <zephyr/net/dns_resolve.h>
```

<a id="details"></a>

私有资源记录（RR）的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_a4d5ea0631d22c224771df2609b2ff450"></a>

```c
uint16_t type
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[type](#a4d5ea0631d22c224771df2609b2ff450)。

资源记录（RR）类型值，取私有用途范围65280至65534。

<a id="r_a47a7aaae4fbb4686a1df617a35f20239"></a>

```c
size_t datalen
```

相关声明：[datalen](#a47a7aaae4fbb4686a1df617a35f20239)。

data字段的长度。

<a id="r_a02840f7d43947d1b427a8acdd4e58c44"></a>

```c
uint8_t data [128]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a02840f7d43947d1b427a8acdd4e58c44)。

来自私有资源记录（RR）的原始数据。

## 22.2\_详细说明（Detailed Documentation）

<a id="a02840f7d43947d1b427a8acdd4e58c44"></a>

### `data`

```c
uint8_t dns_resolve_private::data[128]
```

来自私有资源记录（RR）的原始数据。

<a id="a47a7aaae4fbb4686a1df617a35f20239"></a>

### `datalen`

```c
size_t dns_resolve_private::datalen
```

data字段的长度。

<a id="a4d5ea0631d22c224771df2609b2ff450"></a>

### `type`

```c
uint16_t dns_resolve_private::type
```

资源记录（RR）类型值，取私有用途范围65280至65534。

本数据类型文档由以下文件生成：

- `zephyr/net/dns_resolve.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/net/dns_resolve.h](https://docs.zephyrproject.org/latest/doxygen/html/dns__resolve_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_dns_resolve_context__dns_server_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_dns_resolve_srv_结构体.md)
