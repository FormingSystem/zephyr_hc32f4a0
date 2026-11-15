---
id: learning.zephyr-docs.network-application-model-reference.page-40
title: http_resource_detail_static_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__resource__detail__static.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_http\_resource\_detail\_static\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__resource__detail__static.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

静态服务器资源（Static Server Resource）的表示。

```c
#include <zephyr/net/http/server.h>
```

<a id="details"></a>

静态服务器资源（Static Server Resource）的表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_a67e4e9166d571d44763f3f7cecd34725"></a>

```c
struct http_resource_detail common
```

相关声明：[http_resource_detail](P038_http_resource_detail_结构体.md)、[common](#a67e4e9166d571d44763f3f7cecd34725)。

通用资源详情（Common Resource Details）。

<a id="r_a1ac562d11ee9b73c2cdcffe81f5a43b9"></a>

```c
const void * static_data
```

相关声明：[static_data](#a1ac562d11ee9b73c2cdcffe81f5a43b9)。

静态资源（Static Resource）的内容。

<a id="r_a177c212ecfd8e0320200b4ed841f0484"></a>

```c
size_t static_data_len
```

相关声明：[static_data_len](#a177c212ecfd8e0320200b4ed841f0484)。

静态资源（Static Resource）的大小。

## 40.2\_详细说明（Detailed Documentation）

<a id="a67e4e9166d571d44763f3f7cecd34725"></a>

### `common`

```c
struct http_resource_detail http_resource_detail_static::common
```

通用资源详情（Common Resource Details）。

<a id="a1ac562d11ee9b73c2cdcffe81f5a43b9"></a>

### `static_data`

```c
const void* http_resource_detail_static::static_data
```

静态资源（Static Resource）的内容。

<a id="a177c212ecfd8e0320200b4ed841f0484"></a>

### `static_data_len`

```c
size_t http_resource_detail_static::static_data_len
```

静态资源（Static Resource）的大小。

本数据类型文档由以下文件生成：

- `zephyr/net/http/server.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html)
- [http_resource_detail](P038_http_resource_detail_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_http_resource_detail_dynamic_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_http_resource_detail_static_fs_结构体.md)
