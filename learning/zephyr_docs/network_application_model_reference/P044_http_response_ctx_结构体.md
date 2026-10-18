---
id: learning.zephyr-docs.network-application-model-reference.page-44
title: http_response_ctx_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__response__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_http\_response\_ctx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__response__ctx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP响应上下文（Response Context）。

```c
#include <zephyr/net/http/server.h>
```

<a id="details"></a>

HTTP响应上下文（Response Context）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="r_ada151e7a981885622a79a5ae1f12b2e9"></a>

```c
enum http_status status
```

相关声明：[http_status](https://docs.zephyrproject.org/latest/doxygen/html/group__http__status__codes.html#gabc3b93f68c8bdd857ad32913628dfa8d)、[status](#ada151e7a981885622a79a5ae1f12b2e9)。

要包含在响应中的HTTP状态码（Status Code）。

<a id="r_a63acf00d5ff891ab51107458c545399d"></a>

```c
const struct http_header * headers
```

相关声明：[http_header](P030_http_header_结构体.md)、[headers](#a63acf00d5ff891ab51107458c545399d)。

HTTP头部（Headers）的数组。

<a id="r_a7a7b446baf1a1ab343437ee527ddde95"></a>

```c
size_t header_count
```

相关声明：[header_count](#a7a7b446baf1a1ab343437ee527ddde95)。

headers数组的长度。

<a id="r_aa027d1577dd19db43a17cdd0959b8e39"></a>

```c
const uint8_t * body
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[body](#aa027d1577dd19db43a17cdd0959b8e39)。

指向正文数据（Body Data）的指针。

<a id="r_a88b128e354c85f574409abd55633d2e2"></a>

```c
size_t body_len
```

相关声明：[body_len](#a88b128e354c85f574409abd55633d2e2)。

正文数据（Body Data）的长度。

<a id="r_a53162ff65b66567b31ec323558bc1fe2"></a>

```c
bool final_chunk
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[final_chunk](#a53162ff65b66567b31ec323558bc1fe2)。

应用没有更多数据需要发送时，将此标志（Flag）设为true。

## 44.2\_详细说明（Detailed Documentation）

<a id="aa027d1577dd19db43a17cdd0959b8e39"></a>

### `body`

```c
const uint8_t* http_response_ctx::body
```

指向正文数据（Body Data）的指针。

<a id="a88b128e354c85f574409abd55633d2e2"></a>

### `body_len`

```c
size_t http_response_ctx::body_len
```

正文数据（Body Data）的长度。

<a id="a53162ff65b66567b31ec323558bc1fe2"></a>

### `final_chunk`

```c
bool http_response_ctx::final_chunk
```

应用没有更多数据需要发送时，将此标志（Flag）设为true。

<a id="a7a7b446baf1a1ab343437ee527ddde95"></a>

### `header_count`

```c
size_t http_response_ctx::header_count
```

headers数组的长度。

<a id="a63acf00d5ff891ab51107458c545399d"></a>

### `headers`

```c
const struct http_header* http_response_ctx::headers
```

HTTP头部（Headers）的数组。

<a id="ada151e7a981885622a79a5ae1f12b2e9"></a>

### `status`

```c
enum http_status http_response_ctx::status
```

要包含在响应中的HTTP状态码（Status Code）。

本数据类型文档由以下文件生成：

- `zephyr/net/http/server.h`

## 44.3\_原页交叉引用（Cross References）

- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html)
- [http_status](https://docs.zephyrproject.org/latest/doxygen/html/group__http__status__codes.html#gabc3b93f68c8bdd857ad32913628dfa8d)
- [http_header](P030_http_header_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_http_response_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_http_service_config_结构体.md)
