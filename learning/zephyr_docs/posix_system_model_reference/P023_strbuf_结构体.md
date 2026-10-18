---
id: learning.zephyr-docs.posix-system-model-reference.page-23
title: strbuf_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structstrbuf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_strbuf\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structstrbuf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/stropts.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_a7937239c2a6c2a6b4d76f71b96743589"></a>

```c
int maxlen
```

相关声明：[maxlen](#a7937239c2a6c2a6b4d76f71b96743589)。

<a id="r_a2ce53f2d390a31cdabe5299c73e489b0"></a>

```c
int len
```

相关声明：[len](#a2ce53f2d390a31cdabe5299c73e489b0)。

<a id="r_a421c67aa5a9400a826e8e274f1ffb900"></a>

```c
char * buf
```

相关声明：[buf](#a421c67aa5a9400a826e8e274f1ffb900)。

## 23.2\_详细说明（Detailed Documentation）

<a id="a421c67aa5a9400a826e8e274f1ffb900"></a>

### `buf`

```c
char* strbuf::buf
```

<a id="a2ce53f2d390a31cdabe5299c73e489b0"></a>

### `len`

```c
int strbuf::len
```

<a id="a7937239c2a6c2a6b4d76f71b96743589"></a>

### `maxlen`

```c
int strbuf::maxlen
```

本数据类型文档由以下文件生成：

- `zephyr/posix/stropts.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/posix/stropts.h](https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_stat_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_timeval_结构体.md)
