---
id: learning.zephyr-docs.network-application-model-reference.page-37
title: http_resource_desc_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__resource__desc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_http\_resource\_desc\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__resource__desc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP资源描述（Resource Description）。

```c
#include <zephyr/net/http/service.h>
```

<a id="details"></a>

HTTP资源描述（Resource Description）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_a2882314e271a09d6bc9fae3f58558605"></a>

```c
const char * resource
```

相关声明：[resource](#a2882314e271a09d6bc9fae3f58558605)。

资源名称（Resource Name）。

<a id="r_afdf3332dbc4fb8c10ec8bc525cd8d498"></a>

```c
void * detail
```

相关声明：[detail](#afdf3332dbc4fb8c10ec8bc525cd8d498)。

与此资源（Resource）关联的详情。

## 37.2\_详细说明（Detailed Documentation）

<a id="afdf3332dbc4fb8c10ec8bc525cd8d498"></a>

### `detail`

```c
void* http_resource_desc::detail
```

与此资源（Resource）关联的详情。

<a id="a2882314e271a09d6bc9fae3f58558605"></a>

### `resource`

```c
const char* http_resource_desc::resource
```

资源名称（Resource Name）。

本数据类型文档由以下文件生成：

- `zephyr/net/http/service.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/net/http/service.h](https://docs.zephyrproject.org/latest/doxygen/html/service_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_http_request_ctx_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_http_resource_detail_结构体.md)
