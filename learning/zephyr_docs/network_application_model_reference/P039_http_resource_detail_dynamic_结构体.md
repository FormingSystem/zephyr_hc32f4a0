---
id: learning.zephyr-docs.network-application-model-reference.page-39
title: http_resource_detail_dynamic_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__resource__detail__dynamic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_http\_resource\_detail\_dynamic\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__resource__detail__dynamic.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

动态服务器资源（Dynamic Server Resource）的表示。

```c
#include <zephyr/net/http/server.h>
```

<a id="details"></a>

动态服务器资源（Dynamic Server Resource）的表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_aed22a9df2725eab8fc1032903cecacab"></a>

```c
struct http_resource_detail common
```

相关声明：[http_resource_detail](P038_http_resource_detail_结构体.md)、[common](#aed22a9df2725eab8fc1032903cecacab)。

通用资源详情（Common Resource Details）。

<a id="r_a9f131e0302bbdff94ae6d5147413bec7"></a>

```c
http_resource_dynamic_cb_t cb
```

相关声明：[http_resource_dynamic_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gae15ea0da7140b38609492bf23ec35b4c)、[cb](#a9f131e0302bbdff94ae6d5147413bec7)。

服务器与应用交互所用的资源回调（Resource Callback）。

<a id="r_aa06123f6333e561d515a3d1468ec0856"></a>

```c
struct http_client_ctx * holder
```

相关声明：[http_client_ctx](P026_http_client_ctx_结构体.md)、[holder](#aa06123f6333e561d515a3d1468ec0856)。

指向当前处理资源的客户端的指针，用于防止多个客户端并发访问（Concurrent Access）该资源。

<a id="r_a8b6170c4d98efa27616d1e3132c61cd4"></a>

```c
void * user_data
```

相关声明：[user_data](#a8b6170c4d98efa27616d1e3132c61cd4)。

指向应用注册的用户数据（User Data）的指针。

## 39.2\_详细说明（Detailed Documentation）

<a id="a9f131e0302bbdff94ae6d5147413bec7"></a>

### `cb`

```c
http_resource_dynamic_cb_t http_resource_detail_dynamic::cb
```

服务器与应用交互所用的资源回调（Resource Callback）。

<a id="aed22a9df2725eab8fc1032903cecacab"></a>

### `common`

```c
struct http_resource_detail http_resource_detail_dynamic::common
```

通用资源详情（Common Resource Details）。

<a id="aa06123f6333e561d515a3d1468ec0856"></a>

### `holder`

```c
struct http_client_ctx* http_resource_detail_dynamic::holder
```

指向当前处理资源的客户端的指针，用于防止多个客户端并发访问（Concurrent Access）该资源。

<a id="a8b6170c4d98efa27616d1e3132c61cd4"></a>

### `user_data`

```c
void* http_resource_detail_dynamic::user_data
```

指向应用注册的用户数据（User Data）的指针。

本数据类型文档由以下文件生成：

- `zephyr/net/http/server.h`

## 39.3\_原页交叉引用（Cross References）

- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html)
- [http_resource_detail](P038_http_resource_detail_结构体.md)
- [http_resource_dynamic_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html#gae15ea0da7140b38609492bf23ec35b4c)
- [http_client_ctx](P026_http_client_ctx_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_http_resource_detail_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_http_resource_detail_static_结构体.md)
