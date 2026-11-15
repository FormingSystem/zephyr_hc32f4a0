---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-20
title: k_object_data_联合体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionk__object__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_k\_object\_data\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionk__object__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/internal/kobject_internal.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_ab285ad5a6119657341be525276837fda"></a>

```c
struct k_mutex * mutex
```

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[mutex](#ab285ad5a6119657341be525276837fda)。

<a id="r_ada581c427efa9e48b441b1a323bd57e6"></a>

```c
unsigned int thread_id
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[thread_id](#ada581c427efa9e48b441b1a323bd57e6)。

<a id="r_ac8fdffd51c0b32ea262fa98a827a5bd4"></a>

```c
const struct z_stack_data * stack_data
```

相关声明：[stack_data](#ac8fdffd51c0b32ea262fa98a827a5bd4)。

<a id="r_a2f95fd75c72a619e8c5224e64d1aacc0"></a>

```c
int unused
```

相关声明：[unused](#a2f95fd75c72a619e8c5224e64d1aacc0)。

## 20.2\_详细说明（Detailed Documentation）

<a id="ab285ad5a6119657341be525276837fda"></a>

### `mutex`

```c
struct k_mutex* k_object_data::mutex
```

<a id="ac8fdffd51c0b32ea262fa98a827a5bd4"></a>

### `stack_data`

```c
const struct z_stack_data* k_object_data::stack_data
```

<a id="ada581c427efa9e48b441b1a323bd57e6"></a>

### `thread_id`

```c
unsigned int k_object_data::thread_id
```

<a id="a2f95fd75c72a619e8c5224e64d1aacc0"></a>

### `unused`

```c
int k_object_data::unused
```

本数据类型文档由以下文件生成：

- `zephyr/sys/internal/kobject_internal.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/sys/internal/kobject_internal.h](https://docs.zephyrproject.org/latest/doxygen/html/kobject__internal_8h_source.html)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_sys_winstream_结构体.md) · [返回大纲](大纲.md)
