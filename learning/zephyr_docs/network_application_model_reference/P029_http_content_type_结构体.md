---
id: learning.zephyr-docs.network-application-model-reference.page-29
title: http_content_type_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__content__type.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_http\_content\_type\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__content__type.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/net/http/server.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_afe5cc6179e38766a3ee7a97a0e981cdd"></a>

```c
const char * extension
```

相关声明：[extension](#afe5cc6179e38766a3ee7a97a0e981cdd)。

<a id="r_a9235678c39a82386df70ad5efdcc33ab"></a>

```c
size_t extension_len
```

相关声明：[extension_len](#a9235678c39a82386df70ad5efdcc33ab)。

<a id="r_a78e378def414fd5d9ad9df45df9144fe"></a>

```c
const char * content_type
```

相关声明：[content_type](#a78e378def414fd5d9ad9df45df9144fe)。

## 29.2\_详细说明（Detailed Documentation）

<a id="a78e378def414fd5d9ad9df45df9144fe"></a>

### `content_type`

```c
const char* http_content_type::content_type
```

<a id="afe5cc6179e38766a3ee7a97a0e981cdd"></a>

### `extension`

```c
const char* http_content_type::extension
```

<a id="a9235678c39a82386df70ad5efdcc33ab"></a>

### `extension_len`

```c
size_t http_content_type::extension_len
```

本数据类型文档由以下文件生成：

- `zephyr/net/http/server.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_http_content_range_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_http_header_结构体.md)
