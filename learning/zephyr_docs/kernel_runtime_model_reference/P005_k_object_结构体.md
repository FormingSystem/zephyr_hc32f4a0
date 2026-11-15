---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-5
title: k_object_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structk__object.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_k\_object\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structk__object.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

gperf生成的表；通过k_object_find()检索这些对象。

```c
#include <zephyr/sys/internal/kobject_internal.h>
```

<a id="details"></a>

gperf生成的表；通过k_object_find()检索这些对象。说明（Note）：这是内部API。除非正在Zephyr源码树中扩展功能，否则不要使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_ad676d4edce580d351104fe09f174c323"></a>

```c
void * name
```

相关声明：[name](#ad676d4edce580d351104fe09f174c323)。

<a id="r_a9e32404b2259979e52b65983ad77ec58"></a>

```c
uint8_t perms [CONFIG_MAX_THREAD_BYTES]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[perms](#a9e32404b2259979e52b65983ad77ec58)。

<a id="r_a9c8686d9552cb48c24aef939c8a80057"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a9c8686d9552cb48c24aef939c8a80057)。

<a id="r_a351cbe565fef17ea75966085be3142c9"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#a351cbe565fef17ea75966085be3142c9)。

<a id="r_aea0ad6871d88e2756ba0cbd482fa3aa7"></a>

```c
union k_object_data data
```

相关声明：[k_object_data](P020_k_object_data_联合体.md)、[data](#aea0ad6871d88e2756ba0cbd482fa3aa7)。

## 5.2\_详细说明（Detailed Documentation）

<a id="aea0ad6871d88e2756ba0cbd482fa3aa7"></a>

### `data`

```c
union k_object_data k_object::data
```

<a id="a351cbe565fef17ea75966085be3142c9"></a>

### `flags`

```c
uint8_t k_object::flags
```

<a id="ad676d4edce580d351104fe09f174c323"></a>

### `name`

```c
void* k_object::name
```

<a id="a9e32404b2259979e52b65983ad77ec58"></a>

### `perms`

```c
uint8_t k_object::perms[CONFIG_MAX_THREAD_BYTES]
```

<a id="a9c8686d9552cb48c24aef939c8a80057"></a>

### `type`

```c
uint8_t k_object::type
```

本数据类型文档由以下文件生成：

- `zephyr/sys/internal/kobject_internal.h`

## 5.3\_原页交叉引用（Cross References）

- [k_object_find()](../syscall_boot_reference/P001_系统调用接口.md#ga0d5a4ed3856e0e57c7953f2082ee6fca)
- [zephyr/sys/internal/kobject_internal.h](https://docs.zephyrproject.org/latest/doxygen/html/kobject__internal_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [k_object_data](P020_k_object_data_联合体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_k_mem_paging_stats_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_k_object_assignment_结构体.md)
