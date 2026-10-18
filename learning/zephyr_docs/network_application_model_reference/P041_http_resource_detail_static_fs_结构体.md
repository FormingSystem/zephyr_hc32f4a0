---
id: learning.zephyr-docs.network-application-model-reference.page-41
title: http_resource_detail_static_fs_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__resource__detail__static__fs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_http\_resource\_detail\_static\_fs\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__resource__detail__static__fs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

静态文件系统服务器资源（Static Filesystem Server Resource）的表示。

```c
#include <zephyr/net/http/server.h>
```

<a id="details"></a>

静态文件系统服务器资源（Static Filesystem Server Resource）的表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_a3cb3f688d0070ad3316f33bc05a78f78"></a>

```c
struct http_resource_detail common
```

相关声明：[http_resource_detail](P038_http_resource_detail_结构体.md)、[common](#a3cb3f688d0070ad3316f33bc05a78f78)。

通用资源详情（Common Resource Details）。

<a id="r_a5b25a03b953313b392096bab2faa3be8"></a>

```c
const char * fs_path
```

相关声明：[fs_path](#a5b25a03b953313b392096bab2faa3be8)。

本地文件系统（Local Filesystem）中的路径。

## 41.2\_详细说明（Detailed Documentation）

<a id="a3cb3f688d0070ad3316f33bc05a78f78"></a>

### `common`

```c
struct http_resource_detail http_resource_detail_static_fs::common
```

通用资源详情（Common Resource Details）。

<a id="a5b25a03b953313b392096bab2faa3be8"></a>

### `fs_path`

```c
const char* http_resource_detail_static_fs::fs_path
```

本地文件系统（Local Filesystem）中的路径。

本数据类型文档由以下文件生成：

- `zephyr/net/http/server.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html)
- [http_resource_detail](P038_http_resource_detail_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_http_resource_detail_static_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_http_resource_detail_websocket_结构体.md)
