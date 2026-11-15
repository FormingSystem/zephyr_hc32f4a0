---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-6
title: k_object_assignment_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structk__object__assignment.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_k\_object\_assignment\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structk__object__assignment.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/internal/kobject_internal.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_aca82e8f65cfdcfb7497a4b9f3df4eb8d"></a>

```c
struct k_thread * thread
```

相关声明：[k_thread](../thread_core_reference/P004_线程对象结构.md)、[thread](#aca82e8f65cfdcfb7497a4b9f3df4eb8d)。

<a id="r_ad034fa126915ad604f1edc3b0a177d5a"></a>

```c
void *const * objects
```

相关声明：[objects](#ad034fa126915ad604f1edc3b0a177d5a)。

## 6.2\_详细说明（Detailed Documentation）

<a id="ad034fa126915ad604f1edc3b0a177d5a"></a>

### `objects`

```c
void* const* k_object_assignment::objects
```

<a id="aca82e8f65cfdcfb7497a4b9f3df4eb8d"></a>

### `thread`

```c
struct k_thread* k_object_assignment::thread
```

本数据类型文档由以下文件生成：

- `zephyr/sys/internal/kobject_internal.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/sys/internal/kobject_internal.h](https://docs.zephyrproject.org/latest/doxygen/html/kobject__internal_8h_source.html)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_k_object_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_k_timer_结构体.md)
