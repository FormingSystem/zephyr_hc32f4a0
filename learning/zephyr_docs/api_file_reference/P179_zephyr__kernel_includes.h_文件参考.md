---
id: learning.zephyr-docs.api-file-reference.page-179
title: zephyr__kernel_includes.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kernel__includes_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第179章\_zephyr\_\_kernel\_includes.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/kernel__includes_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

kernel.h包含的头文件（Header Files）。

<a id="details"></a>

```c
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
```

查看此文件的源码。

kernel.h包含的头文件（Header Files）。


## 179.1\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [limits.h](../api_source_runtime_reference/P039_limits.h_源码浏览.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [zephyr/linker/sections.h](https://docs.zephyrproject.org/latest/doxygen/html/sections_8h_source.html)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/sys/dlist.h](../dlist_reference/P003_双向链表头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/sflist.h](../sflist_reference/P003_带标志单向链表头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/kernel/obj_core.h](../object_core_reference/P004_对象核心头文件源码.md)
- [zephyr/kernel_structs.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel__structs_8h_source.html)
- [zephyr/kernel_version.h](../boot_control_reference/P010_内核版本头文件源码.md)
- [zephyr/syscall.h](../syscall_boot_reference/P003_系统调用头文件源码.md)
- [zephyr/sys/printk.h](../api_source_runtime_reference/P051_printk.h_源码浏览.md)
- [zephyr/arch/cpu.h](../api_source_supplement_reference/P009_cpu.h_源码浏览.md)
- [zephyr/sys/rb.h](../rbtree_reference/P005_红黑树头文件源码.md)
- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [zephyr/spinlock.h](../kernel/P068_自旋锁头文件源码.md)
- [zephyr/fatal.h](../fatal_irq_reference/P003_致命错误头文件源码.md)
- [zephyr/irq.h](https://docs.zephyrproject.org/latest/doxygen/html/irq_8h_source.html)
- [zephyr/kernel/thread_stack.h](../thread_stack_reference/P003_线程栈头文件源码.md)
- [zephyr/app_memory/mem_domain.h](../memory_domain_reference/P003_内存域头文件源码.md)
- [zephyr/sys/kobject.h](../api_source_runtime_reference/P036_kobject.h_源码浏览.md)
- [zephyr/kernel/thread.h](../thread_core_reference/P003_线程头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P428_kernel_includes.h_源码浏览.md)

<a id="header-details"></a>

---

[上一章](P178_zephyr__kernel__stats.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P180_zephyr__kernel_structs.h_文件参考.md)
