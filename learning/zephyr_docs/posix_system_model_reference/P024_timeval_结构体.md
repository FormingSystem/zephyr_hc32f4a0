---
id: learning.zephyr-docs.posix-system-model-reference.page-24
title: timeval_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtimeval.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_timeval\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtimeval.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <sys/_timeval.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_aef6ddab1064c430758f9f913b7e4a21e"></a>

```c
time_t tv_sec
```

相关声明：[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)、[tv_sec](#aef6ddab1064c430758f9f913b7e4a21e)。

<a id="r_a810bf8fcd58e255a5c1896d19538b86a"></a>

```c
suseconds_t tv_usec
```

相关声明：[suseconds_t](../time_headers_reference/P003_timespec类型头文件参考.md#ad7acf95ceafb15a1d8d86af0c4982995)、[tv_usec](#a810bf8fcd58e255a5c1896d19538b86a)。

## 24.2\_详细说明（Detailed Documentation）

<a id="aef6ddab1064c430758f9f913b7e4a21e"></a>

### `tv_sec`

```c
time_t timeval::tv_sec
```

<a id="a810bf8fcd58e255a5c1896d19538b86a"></a>

### `tv_usec`

```c
suseconds_t timeval::tv_usec
```

本数据类型文档由以下文件生成：

- `/__w/zephyr/zephyr/lib/libc/minimal/include/sys/_timeval.h`

## 24.3\_原页交叉引用（Cross References）

- [sys/_timeval.h](https://docs.zephyrproject.org/latest/doxygen/html/__timeval_8h_source.html)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [suseconds_t](../time_headers_reference/P003_timespec类型头文件参考.md#ad7acf95ceafb15a1d8d86af0c4982995)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_strbuf_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_tm_结构体.md)
