---
id: learning.zephyr-docs.network-application-model-reference.page-30
title: http_header_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_http\_header\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP头部（Header）的表示。

```c
#include <zephyr/net/http/server.h>
```

<a id="details"></a>

HTTP头部（Header）的表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_afc8e4fa57f957f1fd34ce570c98537f5"></a>

```c
const char * name
```

相关声明：[name](#afc8e4fa57f957f1fd34ce570c98537f5)。

指向以NULL结尾的头部名称（Header Name）字符串的指针。

<a id="r_acac6fa1c3ca33cd67119209dc981e5f9"></a>

```c
const char * value
```

相关声明：[value](#acac6fa1c3ca33cd67119209dc981e5f9)。

指向以NULL结尾的头部值（Header Value）字符串的指针。

## 30.2\_详细说明（Detailed Documentation）

<a id="afc8e4fa57f957f1fd34ce570c98537f5"></a>

### `name`

```c
const char* http_header::name
```

指向以NULL结尾的头部名称（Header Name）字符串的指针。

<a id="acac6fa1c3ca33cd67119209dc981e5f9"></a>

### `value`

```c
const char* http_header::value
```

指向以NULL结尾的头部值（Header Value）字符串的指针。

本数据类型文档由以下文件生成：

- `zephyr/net/http/server.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_http_content_type_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_http_hpack_header_buf_结构体.md)
