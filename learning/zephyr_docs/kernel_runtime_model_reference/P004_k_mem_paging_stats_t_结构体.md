---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-4
title: k_mem_paging_stats_t_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structk__mem__paging__stats__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_k\_mem\_paging\_stats\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structk__mem__paging__stats__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分页统计信息（Paging Statistics）。

```c
#include <zephyr/kernel/mm/demand_paging.h>
```

<a id="details"></a>

分页统计信息（Paging Statistics）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a606ef3d29384e3e29c58ebc87097b7d7"></a>

```c
unsigned long cnt
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[cnt](#a3daad63e37d200f44d88c3d4e49f361a)。

缺页异常（Page Faults）的次数。

<a id="r_a3be562bded54ac8b4aa6119d9d58d345"></a>

```c
unsigned long irq_locked
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[irq_locked](#aa762731df50fc81d08beb3628f9dbd71)。

中断请求（IRQ）被锁定时发生缺页异常（Page Faults）的次数。

<a id="r_a42fbde73e0d8aa3be41d48da175111fe"></a>

```c
unsigned long irq_unlocked
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[irq_unlocked](#a2c2183c1679ae158bdd232fa1fdeb250)。

中断请求（IRQ）未被锁定时发生缺页异常（Page Faults）的次数。

<a id="r_a09cf60960e4feea737a43dc32961904c"></a>

```c
unsigned long in_isr
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[in_isr](#a210c83357c14a06fbd69b0cf2263fbb6)。

在中断服务程序（ISR）中发生缺页异常（Page Faults）的次数。

<a id="r_af6331dae30074d48396151b33ac7a0a7"></a>

```c
} pagefaults
```

相关声明：[pagefaults](#af6331dae30074d48396151b33ac7a0a7)。

```c
struct {
```

<a id="r_a7ba8aaf606d1943a95e3e2d3248a5ce4"></a>

```c
unsigned long clean
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[clean](#a7b421897b3125d1a44284ca964ef1f66)。

被选中逐出的干净页（Clean Pages）数量。

<a id="r_a0df1d27d9978e11205b3c5fab262cc6b"></a>

```c
unsigned long dirty
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[dirty](#a4f8523c0e78c8de1e2443a194e875609)。

被选中逐出的脏页（Dirty Pages）数量。

<a id="r_aa8175953fd7fa0a5057069b73b930f3b"></a>

```c
} eviction
```

相关声明：[eviction](#aa8175953fd7fa0a5057069b73b930f3b)。

## 4.2\_详细说明（Detailed Documentation）

<a id="a7b421897b3125d1a44284ca964ef1f66"></a>

### `clean`

```c
unsigned long k_mem_paging_stats_t::clean
```

被选中逐出的干净页（Clean Pages）数量。

<a id="a3daad63e37d200f44d88c3d4e49f361a"></a>

### `cnt`

```c
unsigned long k_mem_paging_stats_t::cnt
```

缺页异常（Page Faults）的次数。

<a id="a4f8523c0e78c8de1e2443a194e875609"></a>

### `dirty`

```c
unsigned long k_mem_paging_stats_t::dirty
```

被选中逐出的脏页（Dirty Pages）数量。

<a id="aa8175953fd7fa0a5057069b73b930f3b"></a>

### `[struct]`

```c
struct { ... } k_mem_paging_stats_t::eviction
```

<a id="a210c83357c14a06fbd69b0cf2263fbb6"></a>

### `in_isr`

```c
unsigned long k_mem_paging_stats_t::in_isr
```

在中断服务程序（ISR）中发生缺页异常（Page Faults）的次数。

<a id="aa762731df50fc81d08beb3628f9dbd71"></a>

### `irq_locked`

```c
unsigned long k_mem_paging_stats_t::irq_locked
```

中断请求（IRQ）被锁定时发生缺页异常（Page Faults）的次数。

<a id="a2c2183c1679ae158bdd232fa1fdeb250"></a>

### `irq_unlocked`

```c
unsigned long k_mem_paging_stats_t::irq_unlocked
```

中断请求（IRQ）未被锁定时发生缺页异常（Page Faults）的次数。

<a id="af6331dae30074d48396151b33ac7a0a7"></a>

### `[struct]`

```c
struct { ... } k_mem_paging_stats_t::pagefaults
```

本数据类型文档由以下文件生成：

- `zephyr/kernel/mm/demand_paging.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/kernel/mm/demand_paging.h](https://docs.zephyrproject.org/latest/doxygen/html/demand__paging_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_k_mem_paging_histogram_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_k_object_结构体.md)
