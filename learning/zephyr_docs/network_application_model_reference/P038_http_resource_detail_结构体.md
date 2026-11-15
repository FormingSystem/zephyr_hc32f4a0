---
id: learning.zephyr-docs.network-application-model-reference.page-38
title: http_resource_detail_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__resource__detail.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_http\_resource\_detail\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__resource__detail.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

所有资源类型通用的服务器资源（Server Resource）表示。

```c
#include <zephyr/net/http/server.h>
```

<a id="details"></a>

所有资源类型通用的服务器资源（Server Resource）表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_ae391e85a5713bceef9228b93e876c817"></a>

```c
uint32_t bitmask_of_supported_http_methods
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bitmask_of_supported_http_methods](#ae391e85a5713bceef9228b93e876c817)。

所支持HTTP方法（http_method）的位掩码（Bitmask）。

<a id="r_af90b58f593a0c5c8506efc7a54a9cf68"></a>

```c
enum http_resource_type type
```

相关声明：[http_resource_type](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga23d0077fb99827b25491111bd74d00af)、[type](#af90b58f593a0c5c8506efc7a54a9cf68)。

资源类型（Resource Type）。

<a id="r_ac3aa9d4f3781a974739810af5a9e8860"></a>

```c
int path_len
```

相关声明：[path_len](#ac3aa9d4f3781a974739810af5a9e8860)。

URL路径（Path）的长度。

<a id="r_ae5b2415ad3e42c164c4e20fd5bb67bd4"></a>

```c
const char * content_encoding
```

相关声明：[content_encoding](#ae5b2415ad3e42c164c4e20fd5bb67bd4)。

资源的内容编码（Content Encoding）。

<a id="r_acea8d8ff42d8b6ba7d451d3c4de40084"></a>

```c
const char * content_type
```

相关声明：[content_type](#acea8d8ff42d8b6ba7d451d3c4de40084)。

资源的内容类型（Content Type）。

## 38.2\_详细说明（Detailed Documentation）

<a id="ae391e85a5713bceef9228b93e876c817"></a>

### `bitmask_of_supported_http_methods`

```c
uint32_t http_resource_detail::bitmask_of_supported_http_methods
```

所支持HTTP方法（http_method）的位掩码（Bitmask）。

<a id="ae5b2415ad3e42c164c4e20fd5bb67bd4"></a>

### `content_encoding`

```c
const char* http_resource_detail::content_encoding
```

资源的内容编码（Content Encoding）。

<a id="acea8d8ff42d8b6ba7d451d3c4de40084"></a>

### `content_type`

```c
const char* http_resource_detail::content_type
```

资源的内容类型（Content Type）。

<a id="ac3aa9d4f3781a974739810af5a9e8860"></a>

### `path_len`

```c
int http_resource_detail::path_len
```

URL路径（Path）的长度。

<a id="af90b58f593a0c5c8506efc7a54a9cf68"></a>

### `type`

```c
enum http_resource_type http_resource_detail::type
```

资源类型（Resource Type）。

本数据类型文档由以下文件生成：

- `zephyr/net/http/server.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [http_method](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#gaacd5f203e33ac338ca5cb8f02a3ff3b8)
- [http_resource_type](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#ga23d0077fb99827b25491111bd74d00af)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_http_resource_desc_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_http_resource_detail_dynamic_结构体.md)
