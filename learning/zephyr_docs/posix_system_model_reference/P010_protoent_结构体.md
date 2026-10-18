---
id: learning.zephyr-docs.posix-system-model-reference.page-10
title: protoent_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structprotoent.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_protoent\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structprotoent.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/netdb.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_ac70bd11c764a52b2ed1a7c54760b5385"></a>

```c
char * p_name
```

相关声明：[p_name](#ac70bd11c764a52b2ed1a7c54760b5385)。

<a id="r_aa0adbe8a3e56d93695d9e1d171e1f2f4"></a>

```c
char ** p_aliases
```

相关声明：[p_aliases](#aa0adbe8a3e56d93695d9e1d171e1f2f4)。

<a id="r_a3ee5b885146ea094cc17e0e210cfc606"></a>

```c
int p_proto
```

相关声明：[p_proto](#a3ee5b885146ea094cc17e0e210cfc606)。

## 10.2\_详细说明（Detailed Documentation）

<a id="aa0adbe8a3e56d93695d9e1d171e1f2f4"></a>

### `p_aliases`

```c
char** protoent::p_aliases
```

<a id="ac70bd11c764a52b2ed1a7c54760b5385"></a>

### `p_name`

```c
char* protoent::p_name
```

<a id="a3ee5b885146ea094cc17e0e210cfc606"></a>

### `p_proto`

```c
int protoent::p_proto
```

本数据类型文档由以下文件生成：

- `zephyr/posix/netdb.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/posix/netdb.h](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_passwd_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_pthread_attr_t_结构体.md)
