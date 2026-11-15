---
id: learning.zephyr-docs.api-file-system-device-reference.page-25
title: zephyr__pmci__mctp__mctp_memory.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__memory_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_pmci\_\_mctp\_\_mctp\_memory.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mctp__memory_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCTP内存管理函数（Memory Management Functions）。

查看此文件的源码。

<a id="details"></a>

MCTP内存管理函数（Memory Management Functions）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.1\_函数（Functions）

<a id="r_a4babf10b32d5508c6db9c2de93095cfc"></a>

```c
void * mctp_heap_alloc (size_t bytes)
```

相关声明：[mctp_heap_alloc](#a4babf10b32d5508c6db9c2de93095cfc)。

从管理组件传输协议（MCTP）堆分配内存。

<a id="r_afbdb73eaf7bad77a94533b3b102bc4a5"></a>

```c
void mctp_heap_free (void *ptr)
```

相关声明：[mctp_heap_free](#afbdb73eaf7bad77a94533b3b102bc4a5)。

释放从 MCTP 堆分配的内存。

## 25.2\_详细说明（Detailed Documentation）

<a id="a4babf10b32d5508c6db9c2de93095cfc"></a>

### `mctp_heap_alloc()`

```c
void * mctp_heap_alloc ( size_t bytes)
```

从管理组件传输协议（MCTP）堆分配内存。

此函数从 MCTP 堆分配内存。返回的内存适合传给会接管内存所有权（ownership）的 libmctp 函数。不再需要时，应使用 `mctp_heap_free()` 释放所分配内存。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bytes` | 要分配的字节数。 |

**返回（Returns）**：返回值：指向所分配内存的指针；分配失败时返回 `NULL`。

<a id="afbdb73eaf7bad77a94533b3b102bc4a5"></a>

### `mctp_heap_free()`

```c
void mctp_heap_free ( void * ptr)
```

释放从 MCTP 堆分配的内存。

此函数释放先前通过 `mctp_heap_alloc()` 从 MCTP 堆分配的内存。传入指针必须由 `mctp_heap_alloc()` 返回，并且尚未被释放。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ptr` | 指向待释放内存的指针。 |


## 25.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P510_mctp_memory.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P024_zephyr__dt-bindings__sensor__lps22hh.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__xen__memory.h_文件参考.md)
