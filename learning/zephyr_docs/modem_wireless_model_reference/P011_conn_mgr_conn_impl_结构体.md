---
id: learning.zephyr-docs.modem-wireless-model-reference.page-11
title: conn_mgr_conn_impl_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structconn__mgr__conn__impl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_conn\_mgr\_conn\_impl\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structconn__mgr__conn__impl.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接实现（Connectivity Implementation）结构。

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

<a id="details"></a>

连接实现（Connectivity Implementation）结构体，使用提供的 API 声明一个 `conn_mgr` 连接层实现。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_a1229707a1b919659647412cb1eecd61b"></a>

```c
struct conn_mgr_conn_api * api
```

相关声明：[conn_mgr_conn_api](P009_conn_mgr_conn_api_结构体.md)、[api](#a1229707a1b919659647412cb1eecd61b)。

此实现使用的连接 API。

## 11.2\_详细说明（Detailed Documentation）

<a id="a1229707a1b919659647412cb1eecd61b"></a>

### `api`

```c
struct conn_mgr_conn_api* conn_mgr_conn_impl::api
```

此实现使用的连接 API。

本数据类型文档由以下文件生成：

- `zephyr/net/conn_mgr_connectivity_impl.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/net/conn_mgr_connectivity_impl.h](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity__impl_8h_source.html)
- [conn_mgr_conn_api](P009_conn_mgr_conn_api_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_conn_mgr_conn_binding_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_esp_wifi_mesh_addr_结构体.md)
