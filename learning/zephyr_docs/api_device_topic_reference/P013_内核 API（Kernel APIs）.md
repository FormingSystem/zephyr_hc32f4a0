---
id: learning.zephyr-docs.api-device-topic-reference.page-13
title: 内核 API（Kernel APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_内核 API（Kernel APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__apis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内核 API（Kernel APIs）

<a id="details"></a>

内核 API（Kernel APIs）。自 Zephyr 1.0 起提供；API 版本为 1.0.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 13.1\_主题（Topics）

<a id="r_poll_5Fapis"></a>

相关声明：[异步轮询 API（Async polling APIs）](../eventpoll_reference/P003_轮询公共接口.md)。

一种能够同时等待多个条件中任意一个得到满足的API。

<a id="r_atomic_5Fapis"></a>

相关声明：[原子操作服务 API（Atomic Services APIs）](../atomic_reference/P001_原子操作公共接口.md)。

<a id="r_barrier_5Fapis"></a>

相关声明：[屏障服务 API（Barrier Services APIs）](../synchronization_reference/P001_内存屏障公共接口.md)。

<a id="r_cpu_5Fidle_5Fapis"></a>

相关声明：[CPU 空闲 API（CPU Idling APIs）](../fatal_irq_reference/P011_CPU空闲接口.md)。

<a id="r_condvar_5Fapis"></a>

相关声明：[条件变量 API（Condition Variables APIs）](../synchronization_reference/P010_条件变量公共接口.md)。

<a id="r_event_5Fapis"></a>

相关声明：[事件 API（Event APIs）](../eventpoll_reference/P001_事件公共接口.md)。

<a id="r_fifo_5Fapis"></a>

相关声明：[先进先出队列 API（FIFO APIs）](../queue_reference/P003_FIFO公共接口.md)。

<a id="r_futex_5Fapis"></a>

相关声明：[快速用户空间互斥锁 API（FUTEX APIs）](../userspace_sync_reference/P001_Futex公共接口.md)。

<a id="r_fatal_5Fapis"></a>

相关声明：[致命错误 API（Fatal error APIs）](../fatal_irq_reference/P001_致命错误处理接口.md)。

<a id="r_float_5Fapis"></a>

相关声明：[浮点 API（Floating Point APIs）](../fatal_irq_reference/P012_浮点上下文接口.md)。

<a id="r_heap_5Fapis"></a>

相关声明：[堆 API（Heap APIs）](../heap_reference/P001_内核堆公共接口.md)。

从堆（Heap）分配内存。

<a id="r_isr_5Fapis"></a>

相关声明：[中断服务程序 API（Interrupt Service Routine APIs）](../fatal_irq_reference/P007_中断服务接口.md)。

<a id="r_kernel_5Fmemory_5Fmanagement"></a>

相关声明：[内核内存管理（Kernel Memory Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html)。

内核内存管理（Kernel Memory Management）

<a id="r_lifo_5Fapis"></a>

相关声明：[后进先出队列 API（LIFO APIs）](../queue_reference/P005_LIFO公共接口.md)。

<a id="r_mailbox_5Fapis"></a>

相关声明：[邮箱 API（Mailbox APIs）](../mboxpipe_reference/P001_邮箱公共接口.md)。

<a id="r_mem_5Fslab_5Fapis"></a>

相关声明：[内存块池 API（Memory Slab APIs）](../heap_reference/P003_固定块内存池公共接口.md)。

<a id="r_mem_5Fdomain_5Fapis"></a>

相关声明：[内存域 API（Memory domain APIs）](../memory_domain_reference/P001_内存域接口.md)。

<a id="r_msgq_5Fapis"></a>

相关声明：[消息队列 API（Message Queue APIs）](../msgstack_reference/P001_消息队列公共接口.md)。

<a id="r_mutex_5Fapis"></a>

相关声明：[互斥锁 API（Mutex APIs）](../synchronization_reference/P006_互斥量公共接口.md)。

<a id="r_obj_5Fcore_5Fapis"></a>

相关声明：[对象核心 API（Object Core APIs）](../object_core_reference/P001_对象核心公共接口.md)。

<a id="r_obj_5Fcore_5Fstats_5Fapis"></a>

相关声明：[对象核心统计API（Object Core Statistics APIs）](../object_core_reference/P002_对象核心统计接口.md)。

<a id="r_pipe_5Fapis"></a>

相关声明：[管道 API（Pipe APIs）](../mboxpipe_reference/P004_管道公共接口.md)。

<a id="r_queue_5Fapis"></a>

相关声明：[队列 API（Queue APIs）](../queue_reference/P001_通用队列公共接口.md)。

<a id="r_semaphore_5Fapis"></a>

相关声明：[信号量 API（Semaphore APIs）](../synchronization_reference/P008_信号量公共接口.md)。

<a id="r_spinlock_5Fapis"></a>

相关声明：[自旋锁 API（Spinlock APIs）](../kernel/P065_自旋锁公共接口.md)。

自旋锁 API（Spinlock APIs）

<a id="r_stack_5Fapis"></a>

相关声明：[栈 API（Stack APIs）](../msgstack_reference/P004_栈公共接口.md)。

<a id="r_clock_5Fapis"></a>

相关声明：[系统时钟 API（System Clock APIs）](../timer_reference/P086_系统时钟公共接口.md)。

系统时钟 API（System Clock APIs）

<a id="r_thread_5Fapis"></a>

相关声明：[线程 API（Thread APIs）](../thread_core_reference/P001_线程公共接口.md)。

<a id="r_thread_5Fstack_5Fapi"></a>

相关声明：[线程栈 API（Thread Stack APIs）。](../thread_stack_reference/P001_线程栈接口.md)。

线程栈 API（Thread Stack APIs）。

<a id="r_timer_5Fapis"></a>

相关声明：[定时器 API（Timer APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__timer__apis.html)。

<a id="r_usermode_5Fapis"></a>

相关声明：[用户模式 API（User Mode APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html)。

<a id="r_version_5Fapis"></a>

相关声明：[版本 API（Version APIs）](../boot_control_reference/P013_内核版本接口.md)。

内核版本 API（Kernel Version APIs）。

<a id="r_workqueue_5Fapis"></a>

相关声明：[工作队列 API（Work Queue APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.2\_宏定义（Macros）

<a id="r_gac627cc4c3da16be4b74f0a4ab036a603"></a>

```c
#define K_ANY NULL
```

相关声明：[K_ANY](#gac627cc4c3da16be4b74f0a4ab036a603)。

用于匹配任意线程的通配符（wildcard）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.3\_枚举（Enumerations）

<a id="r_gab0b42f9804777dfa5fed2b7cd866779c"></a>

```c
enum execution_context_types { K_ISR = 0 , K_COOP_THREAD , K_PREEMPT_THREAD }
```

相关声明：[execution_context_types](#gab0b42f9804777dfa5fed2b7cd866779c)、[K_ISR](#ggab0b42f9804777dfa5fed2b7cd866779ca30593044743695f8184a157283dac4d5)、[K_COOP_THREAD](#ggab0b42f9804777dfa5fed2b7cd866779ca62c0b731a1bb3c5e4aadeba3f93df58b)、[K_PREEMPT_THREAD](#ggab0b42f9804777dfa5fed2b7cd866779cae84f57f4ac996c751d1f4c9e49789322)。

执行上下文（execution contexts）的类型。

## 13.4\_详细说明（Detailed Documentation）

<a id="gac627cc4c3da16be4b74f0a4ab036a603"></a>

### `K_ANY`

```c
#define K_ANY NULL
```

```c
#include <zephyr/kernel.h>
```

用于匹配任意线程的通配符（wildcard）。

可用于任何需要线程标识符且允许任意线程的位置，例如邮箱消息（mailbox message）的源线程或目标线程。

<a id="gab0b42f9804777dfa5fed2b7cd866779c"></a>

### `execution_context_types`

```c
enum execution_context_types
```

```c
#include <zephyr/kernel.h>
```

执行上下文（execution contexts）的类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `K_ISR` | 正在中断服务程序（ISR）中执行。 |
| `K_COOP_THREAD` | 正在协作式线程（cooperative thread）中执行。 |
| `K_PREEMPT_THREAD` | 正在可抢占线程（preemptible thread）中执行。 |


## 13.5\_原页交叉引用（Cross References）

- [异步轮询 API（Async polling APIs）](../eventpoll_reference/P003_轮询公共接口.md)
- [原子操作服务 API（Atomic Services APIs）](../atomic_reference/P001_原子操作公共接口.md)
- [屏障服务 API（Barrier Services APIs）](../synchronization_reference/P001_内存屏障公共接口.md)
- [CPU 空闲 API（CPU Idling APIs）](../fatal_irq_reference/P011_CPU空闲接口.md)
- [条件变量 API（Condition Variables APIs）](../synchronization_reference/P010_条件变量公共接口.md)
- [事件 API（Event APIs）](../eventpoll_reference/P001_事件公共接口.md)
- [先进先出队列 API（FIFO APIs）](../queue_reference/P003_FIFO公共接口.md)
- [快速用户空间互斥锁 API（FUTEX APIs）](../userspace_sync_reference/P001_Futex公共接口.md)
- [致命错误 API（Fatal error APIs）](../fatal_irq_reference/P001_致命错误处理接口.md)
- [浮点 API（Floating Point APIs）](../fatal_irq_reference/P012_浮点上下文接口.md)
- [堆 API（Heap APIs）](../heap_reference/P001_内核堆公共接口.md)
- [中断服务程序 API（Interrupt Service Routine APIs）](../fatal_irq_reference/P007_中断服务接口.md)
- [内核内存管理（Kernel Memory Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html)
- [后进先出队列 API（LIFO APIs）](../queue_reference/P005_LIFO公共接口.md)
- [邮箱 API（Mailbox APIs）](../mboxpipe_reference/P001_邮箱公共接口.md)
- [内存块池 API（Memory Slab APIs）](../heap_reference/P003_固定块内存池公共接口.md)
- [内存域 API（Memory domain APIs）](../memory_domain_reference/P001_内存域接口.md)
- [消息队列 API（Message Queue APIs）](../msgstack_reference/P001_消息队列公共接口.md)
- [互斥锁 API（Mutex APIs）](../synchronization_reference/P006_互斥量公共接口.md)
- [对象核心 API（Object Core APIs）](../object_core_reference/P001_对象核心公共接口.md)
- [对象核心统计API（Object Core Statistics APIs）](../object_core_reference/P002_对象核心统计接口.md)
- [管道 API（Pipe APIs）](../mboxpipe_reference/P004_管道公共接口.md)
- [队列 API（Queue APIs）](../queue_reference/P001_通用队列公共接口.md)
- [信号量 API（Semaphore APIs）](../synchronization_reference/P008_信号量公共接口.md)
- [自旋锁 API（Spinlock APIs）](../kernel/P065_自旋锁公共接口.md)
- [栈 API（Stack APIs）](../msgstack_reference/P004_栈公共接口.md)
- [系统时钟 API（System Clock APIs）](../timer_reference/P086_系统时钟公共接口.md)
- [线程 API（Thread APIs）](../thread_core_reference/P001_线程公共接口.md)
- [线程栈 API（Thread Stack APIs）。](../thread_stack_reference/P001_线程栈接口.md)
- [定时器 API（Timer APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__timer__apis.html)
- [用户模式 API（User Mode APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html)
- [版本 API（Version APIs）](../boot_control_reference/P013_内核版本接口.md)
- [工作队列 API（Work Queue APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggab0b42f9804777dfa5fed2b7cd866779ca30593044743695f8184a157283dac4d5"></a>
<a id="ggab0b42f9804777dfa5fed2b7cd866779ca62c0b731a1bb3c5e4aadeba3f93df58b"></a>
<a id="ggab0b42f9804777dfa5fed2b7cd866779cae84f57f4ac996c751d1f4c9e49789322"></a>

---

[上一章](P012_键位映射实用工具（Keymap utilities）.md) · [返回大纲](大纲.md) · [下一章](P014_文件系统管理回调（File System Management Callbacks）.md)
