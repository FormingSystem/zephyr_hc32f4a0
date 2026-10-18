---
id: learning.zephyr-docs.posix-system-model-reference.page-16
title: servent_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structservent.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_servent\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structservent.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/netdb.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_a1bdae74e6bdf91235fbba6d08eb4537c"></a>

```c
char * s_name
```

相关声明：[s_name](#a1bdae74e6bdf91235fbba6d08eb4537c)。

<a id="r_a3f8d3cf12c142b8f0bfab810975783d5"></a>

```c
char ** s_aliases
```

相关声明：[s_aliases](#a3f8d3cf12c142b8f0bfab810975783d5)。

<a id="r_a6f0175c9ea10b6749032259c26677815"></a>

```c
int s_port
```

相关声明：[s_port](#a6f0175c9ea10b6749032259c26677815)。

<a id="r_a379e36da163ba55b73d770a27bb2430b"></a>

```c
char * s_proto
```

相关声明：[s_proto](#a379e36da163ba55b73d770a27bb2430b)。

## 16.2\_详细说明（Detailed Documentation）

<a id="a3f8d3cf12c142b8f0bfab810975783d5"></a>

### `s_aliases`

```c
char** servent::s_aliases
```

<a id="a1bdae74e6bdf91235fbba6d08eb4537c"></a>

### `s_name`

```c
char* servent::s_name
```

<a id="a6f0175c9ea10b6749032259c26677815"></a>

### `s_port`

```c
int servent::s_port
```

<a id="a379e36da163ba55b73d770a27bb2430b"></a>

### `s_proto`

```c
char* servent::s_proto
```

本数据类型文档由以下文件生成：

- `zephyr/posix/netdb.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/posix/netdb.h](https://docs.zephyrproject.org/latest/doxygen/html/netdb_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_pthread_once_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_sigaction_结构体.md)
