---
id: learning.zephyr-docs.api-source-reference.page-428
title: kernel_includes.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kernel__includes_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第428章\_kernel\_includes.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/kernel__includes_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/kernel__includes_8h.html)。

## 428.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="aarch_2cpu_8h_html"></a>
<a id="aatomic_8h_html"></a>
<a id="aclock_8h_html"></a>
<a id="adlist_8h_html"></a>
<a id="afatal_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="airq_8h_html"></a>
<a id="akernel_2thread_8h_html"></a>
<a id="akernel__structs_8h_html"></a>
<a id="akernel__version_8h_html"></a>
<a id="akobject_8h_html"></a>
<a id="alimits_8h_html"></a>
<a id="amem__domain_8h_html"></a>
<a id="aobj__core_8h_html"></a>
<a id="aprintk_8h_html"></a>
<a id="arb_8h_html"></a>
<a id="asections_8h_html"></a>
<a id="asflist_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="aspinlock_8h_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="asyscall_8h_html"></a>
<a id="athread__stack_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_KERNEL_INCLUDES_H_
#define ZEPHYR_INCLUDE_KERNEL_INCLUDES_H_

#ifndef ZEPHYR_INCLUDE_KERNEL_H_
#error  Please do not include kernel-specific headers directly, use <zephyr/kernel.h> instead
#endif

#include <stddef.h>
#include <zephyr/types.h>
#include <limits.h>
#include <zephyr/toolchain.h>
#include <zephyr/linker/sections.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/sys/dlist.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/sflist.h>
#include <zephyr/sys/util.h>
#include <zephyr/kernel/obj_core.h>
#include <zephyr/kernel_structs.h>
#include <zephyr/kernel_version.h>
#include <zephyr/syscall.h>
#include <zephyr/sys/printk.h>
#include <zephyr/arch/cpu.h>
#include <zephyr/sys/rb.h>
#include <zephyr/sys/clock.h>
#include <zephyr/spinlock.h>
#include <zephyr/fatal.h>
#include <zephyr/irq.h>
#include <zephyr/kernel/thread_stack.h>
#include <zephyr/app_memory/mem_domain.h>
#include <zephyr/sys/kobject.h>
#include <zephyr/kernel/thread.h>

#endif /* ZEPHYR_INCLUDE_KERNEL_INCLUDES_H_ */
```

## 428.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 47 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_KERNEL_INCLUDES_H_`。

## 428.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/kernel__includes_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [limits.h](https://docs.zephyrproject.org/latest/doxygen/html/limits_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/linker/sections.h](https://docs.zephyrproject.org/latest/doxygen/html/sections_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/sflist.h](../sflist_reference/P002_带标志单向链表头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/kernel/obj_core.h](../object_core_reference/P003_对象核心头文件参考.md)
- [zephyr/kernel_structs.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel__structs_8h.html)
- [zephyr/kernel_version.h](../boot_control_reference/P009_内核版本头文件参考.md)
- [zephyr/syscall.h](../syscall_boot_reference/P002_系统调用头文件参考.md)
- [zephyr/sys/printk.h](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)
- [zephyr/arch/cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/arch_2cpu_8h.html)
- [zephyr/sys/rb.h](../rbtree_reference/P004_红黑树头文件参考.md)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [zephyr/spinlock.h](../kernel/P067_自旋锁头文件参考.md)
- [zephyr/fatal.h](../fatal_irq_reference/P002_致命错误头文件参考.md)
- [zephyr/irq.h](https://docs.zephyrproject.org/latest/doxygen/html/irq_8h.html)
- [zephyr/kernel/thread_stack.h](../thread_stack_reference/P002_线程栈头文件参考.md)
- [zephyr/app_memory/mem_domain.h](../memory_domain_reference/P002_内存域头文件参考.md)
- [zephyr/sys/kobject.h](https://docs.zephyrproject.org/latest/doxygen/html/kobject_8h.html)
- [zephyr/kernel/thread.h](../thread_core_reference/P002_线程头文件参考.md)
- [cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/arch_2cpu_8h.html)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [fatal.h](../fatal_irq_reference/P002_致命错误头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [irq.h](https://docs.zephyrproject.org/latest/doxygen/html/irq_8h.html)
- [thread.h](../thread_core_reference/P002_线程头文件参考.md)
- [kernel_structs.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel__structs_8h.html)
- [kernel_version.h](../boot_control_reference/P009_内核版本头文件参考.md)
- [kobject.h](https://docs.zephyrproject.org/latest/doxygen/html/kobject_8h.html)
- [mem_domain.h](../memory_domain_reference/P002_内存域头文件参考.md)
- [obj_core.h](../object_core_reference/P003_对象核心头文件参考.md)
- [printk.h](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)
- [rb.h](../rbtree_reference/P004_红黑树头文件参考.md)
- [sections.h](https://docs.zephyrproject.org/latest/doxygen/html/sections_8h.html)
- [sflist.h](../sflist_reference/P002_带标志单向链表头文件参考.md)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [spinlock.h](../kernel/P067_自旋锁头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [syscall.h](../syscall_boot_reference/P002_系统调用头文件参考.md)
- [thread_stack.h](../thread_stack_reference/P002_线程栈头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P427_stats.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P429_key_ids.h_源码浏览.md)
