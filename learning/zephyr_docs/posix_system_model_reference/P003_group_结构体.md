---
id: learning.zephyr-docs.posix-system-model-reference.page-3
title: group_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgroup.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_group\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgroup.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

组结构（Group Structure）。

```c
#include <zephyr/posix/grp.h>
```

<a id="details"></a>

组结构（Group Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a828b9f3708aa76cecd8fda0a20b61e98"></a>

```c
char * gr_name
```

相关声明：[gr_name](#a828b9f3708aa76cecd8fda0a20b61e98)。

组名称（group name）。

<a id="r_a00f124d1201a4de3cc885fe87a91431f"></a>

```c
gid_t gr_gid
```

相关声明：[gid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3a7834be1a79bb0c5a65d3546c2e3bd8)、[gr_gid](#a00f124d1201a4de3cc885fe87a91431f)。

指向字符指针数组的指针；数组各项指向成员名称，并以空指针终止。

<a id="r_a338a8153e1e47d345a0bb578f3c2656c"></a>

```c
char ** gr_mem
```

相关声明：[gr_mem](#a338a8153e1e47d345a0bb578f3c2656c)。

## 3.2\_详细说明（Detailed Documentation）

<a id="a00f124d1201a4de3cc885fe87a91431f"></a>

### `gr_gid`

```c
gid_t group::gr_gid
```

指向字符指针数组的指针；数组各项指向成员名称，并以空指针终止。

<a id="a338a8153e1e47d345a0bb578f3c2656c"></a>

### `gr_mem`

```c
char** group::gr_mem
```

<a id="a828b9f3708aa76cecd8fda0a20b61e98"></a>

### `gr_name`

```c
char* group::gr_name
```

组名称（group name）。

数值形式的组 ID（group ID）。

本数据类型文档由以下文件生成：

- `zephyr/posix/grp.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/posix/grp.h](https://docs.zephyrproject.org/latest/doxygen/html/grp_8h_source.html)
- [gid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3a7834be1a79bb0c5a65d3546c2e3bd8)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_fd_op_vtable_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_hostent_结构体.md)
