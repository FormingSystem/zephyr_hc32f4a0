---
id: learning.zephyr-docs.api-file-reference.page-180
title: zephyr__kernel_structs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kernel__structs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第180章\_zephyr\_\_kernel\_structs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/kernel__structs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/atomic.h>
#include <zephyr/types.h>
#include <zephyr/sys/dlist.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/sys_heap.h>
#include <zephyr/arch/structs.h>
#include <zephyr/kernel/stats.h>
#include <zephyr/kernel/obj_core.h>
#include <zephyr/sys/rb.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 180.1\_宏定义（Macros）

<a id="r_ae861b4805a52e8bd99d5481d3943dc5c"></a>

```c
#define K_NUM_THREAD_PRIO (CONFIG_NUM_PREEMPT_PRIORITIES + CONFIG_NUM_COOP_PRIORITIES + 1)
```

相关声明：[K_NUM_THREAD_PRIO](#ae861b4805a52e8bd99d5481d3943dc5c)。

<a id="r_a3fcfea2426c3da024f627c8ab9e754ad"></a>

```c
#define PRIQ_BITMAP_SIZE (DIV_ROUND_UP(K_NUM_THREAD_PRIO, BITS_PER_LONG))
```

相关声明：[PRIQ_BITMAP_SIZE](#a3fcfea2426c3da024f627c8ab9e754ad)、[DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)、[K_NUM_THREAD_PRIO](#ae861b4805a52e8bd99d5481d3943dc5c)、[BITS_PER_LONG](../util_reference/P001_通用工具公共接口.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)。

<a id="r_a80c653d62783a4e7ea960794bd287b49"></a>

```c
#define CPU_ID ((CONFIG_MP_MAX_NUM_CPUS == 1) ? 0 : _current_cpu->id)
```

相关声明：[CPU_ID](#a80c653d62783a4e7ea960794bd287b49)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 180.2\_类型定义（Typedefs）

<a id="r_a44c6f88a879877ad8da28706e274064f"></a>

```c
typedef void(* k_thread_timeslice_fn_t) (struct k_thread *thread, void *data)
```

相关声明：[k_thread_timeslice_fn_t](#a44c6f88a879877ad8da28706e274064f)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

## 180.3\_详细说明（Detailed Documentation）

<a id="a80c653d62783a4e7ea960794bd287b49"></a>

### `CPU_ID`

```c
#define CPU_ID ((CONFIG_MP_MAX_NUM_CPUS == 1) ? 0 : _current_cpu->id)
```

<a id="ae861b4805a52e8bd99d5481d3943dc5c"></a>

### `K_NUM_THREAD_PRIO`

```c
#define K_NUM_THREAD_PRIO (CONFIG_NUM_PREEMPT_PRIORITIES + CONFIG_NUM_COOP_PRIORITIES + 1)
```

<a id="a3fcfea2426c3da024f627c8ab9e754ad"></a>

### `PRIQ_BITMAP_SIZE`

```c
#define PRIQ_BITMAP_SIZE (DIV_ROUND_UP(K_NUM_THREAD_PRIO, BITS_PER_LONG))
```

<a id="a44c6f88a879877ad8da28706e274064f"></a>

### `k_thread_timeslice_fn_t`

```c
typedef void(* k_thread_timeslice_fn_t) (struct k_thread *thread, void *data)
```


## 180.4\_原页交叉引用（Cross References）

- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/sys/dlist.h](../dlist_reference/P003_双向链表头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/sys_heap.h](../lowheap_reference/P012_底层堆头文件源码.md)
- [zephyr/arch/structs.h](https://docs.zephyrproject.org/latest/doxygen/html/structs_8h_source.html)
- [zephyr/kernel/stats.h](../api_source_reference/P427_stats.h_源码浏览.md)
- [zephyr/kernel/obj_core.h](../object_core_reference/P004_对象核心头文件源码.md)
- [zephyr/sys/rb.h](../rbtree_reference/P005_红黑树头文件源码.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/kernel__structs_8h_source.html)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [BITS_PER_LONG](../util_reference/P001_通用工具公共接口.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P179_zephyr__kernel_includes.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P181_zephyr__dt-bindings__input__keymap.h_文件参考.md)
