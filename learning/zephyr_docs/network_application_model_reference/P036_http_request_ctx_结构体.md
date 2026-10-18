---
id: learning.zephyr-docs.network-application-model-reference.page-36
title: http_request_ctx_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__request__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_http\_request\_ctx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__request__ctx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP请求上下文（Request Context）。

```c
#include <zephyr/net/http/server.h>
```

<a id="details"></a>

HTTP请求上下文（Request Context）。说明（Note）：捕获的请求头部headers、header_count和headers_status仅在请求的第一次动态资源回调中填充。同一请求后续回调的headers为NULL、header_count为0、headers_status为HTTP_HEADER_STATUS_NONE。第一次回调可能携带请求正文数据，也可能不携带，因此不要以是否存在数据作为处理头部的条件。所需头部值应在第一次回调期间复制出来。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_aae773946b597bb7ca70d071daadf3c1d"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#aae773946b597bb7ca70d071daadf3c1d)。

HTTP请求数据（Request Data）。

<a id="r_a4de5c3114220bef60bcd587f4796603e"></a>

```c
size_t data_len
```

相关声明：[data_len](#a4de5c3114220bef60bcd587f4796603e)。

HTTP请求数据（Request Data）的长度。

<a id="r_a9500727563dd6f33663c0a26299a16a6"></a>

```c
struct http_header * headers
```

相关声明：[http_header](P030_http_header_结构体.md)、[headers](#a9500727563dd6f33663c0a26299a16a6)。

HTTP请求头部（Request Headers）的数组。

<a id="r_a404ff7f9946f162dc0ef6c0a872bf88b"></a>

```c
size_t header_count
```

相关声明：[header_count](#a404ff7f9946f162dc0ef6c0a872bf88b)。

HTTP请求头部（Request Headers）数组的长度。

<a id="r_a312cc4db494a0415a2c0342183b3a3c6"></a>

```c
enum http_header_status headers_status
```

相关声明：[http_header_status](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga6c15e872ece1b9a740b6dca3974101b3)、[headers_status](#a312cc4db494a0415a2c0342183b3a3c6)。

HTTP请求头部（Request Headers）的状态。

## 36.2\_详细说明（Detailed Documentation）

<a id="aae773946b597bb7ca70d071daadf3c1d"></a>

### `data`

```c
uint8_t* http_request_ctx::data
```

HTTP请求数据（Request Data）。

<a id="a4de5c3114220bef60bcd587f4796603e"></a>

### `data_len`

```c
size_t http_request_ctx::data_len
```

HTTP请求数据（Request Data）的长度。

<a id="a404ff7f9946f162dc0ef6c0a872bf88b"></a>

### `header_count`

```c
size_t http_request_ctx::header_count
```

HTTP请求头部（Request Headers）数组的长度。

<a id="a9500727563dd6f33663c0a26299a16a6"></a>

### `headers`

```c
struct http_header* http_request_ctx::headers
```

HTTP请求头部（Request Headers）的数组。

<a id="a312cc4db494a0415a2c0342183b3a3c6"></a>

### `headers_status`

```c
enum http_header_status http_request_ctx::headers_status
```

HTTP请求头部（Request Headers）的状态。

本数据类型文档由以下文件生成：

- `zephyr/net/http/server.h`

## 36.3\_原页交叉引用（Cross References）

- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [http_header](P030_http_header_结构体.md)
- [http_header_status](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga6c15e872ece1b9a740b6dca3974101b3)
- [HTTP_HEADER_STATUS_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_http_request_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_http_resource_desc_结构体.md)
