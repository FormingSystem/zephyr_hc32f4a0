---
id: learning.zephyr-docs.network-application-model-reference.page-27
title: http_client_internal_data_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__client__internal__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_http\_client\_internal\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__client__internal__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

应用不应访问的HTTP客户端内部数据（Internal Data）。

```c
#include <zephyr/net/http/client.h>
```

<a id="details"></a>

应用不应访问的HTTP客户端内部数据（Internal Data）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_a1620ae6631414c3ba5e462d97deca157"></a>

```c
struct http_parser parser
```

相关声明：[http_parser](P032_http_parser_结构体.md)、[parser](#a1620ae6631414c3ba5e462d97deca157)。

HTTP解析器上下文（Parser Context）。

<a id="r_a19876ea20cdca3a016d6e260e2795e83"></a>

```c
struct http_parser_settings parser_settings
```

相关声明：[http_parser_settings](P033_http_parser_settings_结构体.md)、[parser_settings](#a19876ea20cdca3a016d6e260e2795e83)。

HTTP解析器设置（Parser Settings）。

<a id="r_aa132cb0366969c04250f64075866227c"></a>

```c
struct http_response response
```

相关声明：[http_response](P043_http_response_结构体.md)、[response](#aa132cb0366969c04250f64075866227c)。

HTTP响应专用数据（Response Specific Data），由http_client_req()在接收数据时填入。

<a id="r_a330102d665b6601949eb7331ab45d517"></a>

```c
void * user_data
```

相关声明：[user_data](#a330102d665b6601949eb7331ab45d517)。

用户数据（User Data）。

<a id="r_a8486d8e8b64474e75cadeb9fb166a4a5"></a>

```c
int sock
```

相关声明：[sock](#a8486d8e8b64474e75cadeb9fb166a4a5)。

HTTP套接字（Socket）。

<a id="r_a06509a514b81f2fe72394fe147f3d86f"></a>

```c
bool aborted
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[aborted](#a06509a514b81f2fe72394fe147f3d86f)。

响应回调中止传输（Transfer）时设置。

## 27.2\_详细说明（Detailed Documentation）

<a id="a06509a514b81f2fe72394fe147f3d86f"></a>

### `aborted`

```c
bool http_client_internal_data::aborted
```

响应回调中止传输（Transfer）时设置。

<a id="a1620ae6631414c3ba5e462d97deca157"></a>

### `parser`

```c
struct http_parser http_client_internal_data::parser
```

HTTP解析器上下文（Parser Context）。

<a id="a19876ea20cdca3a016d6e260e2795e83"></a>

### `parser_settings`

```c
struct http_parser_settings http_client_internal_data::parser_settings
```

HTTP解析器设置（Parser Settings）。

<a id="aa132cb0366969c04250f64075866227c"></a>

### `response`

```c
struct http_response http_client_internal_data::response
```

HTTP响应专用数据（Response Specific Data），由http_client_req()在接收数据时填入。

<a id="a8486d8e8b64474e75cadeb9fb166a4a5"></a>

### `sock`

```c
int http_client_internal_data::sock
```

HTTP套接字（Socket）。

<a id="a330102d665b6601949eb7331ab45d517"></a>

### `user_data`

```c
void* http_client_internal_data::user_data
```

用户数据（User Data）。

本数据类型文档由以下文件生成：

- `zephyr/net/http/client.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/net/http/client.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2client_8h_source.html)
- [http_parser](P032_http_parser_结构体.md)
- [http_parser_settings](P033_http_parser_settings_结构体.md)
- [http_response](P043_http_response_结构体.md)
- [http_client_req()](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gaa38b6efb03f88d6959273a41b6acac81)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_http_client_ctx_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_http_content_range_结构体.md)
