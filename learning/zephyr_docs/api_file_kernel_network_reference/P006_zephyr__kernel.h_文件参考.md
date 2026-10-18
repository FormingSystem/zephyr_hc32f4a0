---
id: learning.zephyr-docs.api-file-kernel-network-reference.page-6
title: zephyr__kernel.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_kernel.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

公共内核API（Public Kernel APIs）。

<a id="details"></a>

```c
#include <zephyr/kernel_includes.h>
#include <errno.h>
#include <limits.h>
#include <stdbool.h>
#include <zephyr/toolchain.h>
#include <zephyr/tracing/tracing_macros.h>
#include <zephyr/sleep.h>
#include <zephyr/sys/mem_stats.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/ring_buffer.h>
#include <zephyr/heap_constants.h>
#include <zephyr/tracing/tracing.h>
#include <zephyr/syscalls/kernel.h>
```

查看此文件的源码。

公共内核API（Public Kernel APIs）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_k_5Ftimer"></a>

```c
struct k_timer
```

相关声明：[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

内核定时器（Kernel Timer）结构。

<a id="r_k_5Fqueue"></a>

```c
struct k_queue
```

相关声明：[k_queue](../queue_reference/P002_内核队列结构.md)。

内核队列结构（Kernel Queue Structure）。

<a id="r_k_5Ffutex"></a>

```c
struct k_futex
```

相关声明：[k_futex](../userspace_sync_reference/P002_Futex结构.md)。

Futex结构。

<a id="r_k_5Fevent"></a>

```c
struct k_event
```

相关声明：[k_event](../eventpoll_reference/P002_内核事件结构.md)。

事件结构（Event Structure）。

<a id="r_k_5Ffifo"></a>

```c
struct k_fifo
```

相关声明：[k_fifo](../queue_reference/P004_内核FIFO结构.md)。

内核FIFO结构（Kernel FIFO Structure）。

<a id="r_k_5Flifo"></a>

```c
struct k_lifo
```

相关声明：[k_lifo](../queue_reference/P006_内核LIFO结构.md)。

内核LIFO结构（Kernel LIFO Structure）。

<a id="r_k_5Fmutex"></a>

```c
struct k_mutex
```

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)。

内核互斥量结构（Kernel Mutex Structure）。

<a id="r_k_5Fcondvar"></a>

```c
struct k_condvar
```

相关声明：[k_condvar](../synchronization_reference/P011_内核条件变量结构.md)。

内核条件变量结构（Kernel Condition Variable Structure）。

<a id="r_k_5Fsem"></a>

```c
struct k_sem
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)。

信号量结构（Semaphore Structure）。

<a id="r_k_5Fipi_5Fwork"></a>

```c
struct k_ipi_work
```

相关声明：[k_ipi_work](../kernel_runtime_model_reference/P002_k_ipi_work_结构体.md)。

处理器间中断（IPI）的工作项结构。

<a id="r_k_5Fwork"></a>

```c
struct k_work
```

相关声明：[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

用于提交工作（Work）的结构。

<a id="r_k_5Fwork_5Fdelayable"></a>

```c
struct k_work_delayable
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)。

用于延迟后提交工作（Work）的结构。

<a id="r_k_5Fwork_5Fsync"></a>

```c
struct k_work_sync
```

相关声明：[k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)。

保存工作项或队列上待完成同步操作（Synchronous Operation）内部状态的结构。

<a id="r_k_5Fwork_5Fqueue_5Fconfig"></a>

```c
struct k_work_queue_config
```

相关声明：[k_work_queue_config](../kernel_runtime_model_reference/P011_k_work_queue_config_结构体.md)。

保存工作队列（Work Queue）可选配置项的结构。

<a id="r_k_5Fwork_5Fq"></a>

```c
struct k_work_q
```

相关声明：[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)。

内核工作队列（Kernel Workqueue）结构。

<a id="r_k_5Fmsgq"></a>

```c
struct k_msgq
```

相关声明：[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)。

消息队列（Message Queue）结构。

<a id="r_k_5Fmsgq_5Fattrs"></a>

```c
struct k_msgq_attrs
```

相关声明：[k_msgq_attrs](../msgstack_reference/P003_消息队列属性结构.md)。

消息队列属性（Message Queue Attributes）。

<a id="r_k_5Fmbox_5Fmsg"></a>

```c
struct k_mbox_msg
```

相关声明：[k_mbox_msg](../mboxpipe_reference/P003_邮箱消息描述符.md)。

邮箱消息结构（Mailbox Message Structure）。

<a id="r_k_5Fmbox"></a>

```c
struct k_mbox
```

相关声明：[k_mbox](../mboxpipe_reference/P002_内核邮箱结构.md)。

邮箱结构（Mailbox Structure）。

<a id="r_k_5Fpipe"></a>

```c
struct k_pipe
```

相关声明：[k_pipe](../mboxpipe_reference/P005_内核管道结构.md)。

内核管道结构（Kernel Pipe Structure）。

<a id="r_k_5Fheap"></a>

```c
struct k_heap
```

相关声明：[k_heap](../heap_reference/P002_内核堆结构.md)。

内核同步堆结构（Kernel Synchronized Heap Structure）。

<a id="r_k_5Fpoll_5Fsignal"></a>

```c
struct k_poll_signal
```

相关声明：[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

轮询信号对象（Poll Signal Object）。

<a id="r_k_5Fpoll_5Fevent"></a>

```c
struct k_poll_event
```

相关声明：[k_poll_event](../eventpoll_reference/P004_轮询事件结构.md)。

轮询事件（Poll Event）

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_gac627cc4c3da16be4b74f0a4ab036a603"></a>

```c
#define K_ANY NULL
```

相关声明：[K_ANY](../api_device_topic_reference/P013_内核 API（Kernel APIs）.md#gac627cc4c3da16be4b74f0a4ab036a603)。

用于匹配任意线程的通配符（wildcard）。

<a id="r_gac145d4747518572acfc8ee1579007d54"></a>

```c
#define K_PRIO_COOP(x)
```

相关声明：[K_PRIO_COOP](../thread_core_reference/P001_线程公共接口.md#gac145d4747518572acfc8ee1579007d54)。

计算协作式线程优先级（Cooperative Thread Priority）。

<a id="r_gaa0e916aae3ddd0e998cd41ac32afe30a"></a>

```c
#define K_PRIO_PREEMPT(x)
```

相关声明：[K_PRIO_PREEMPT](../thread_core_reference/P001_线程公共接口.md#gaa0e916aae3ddd0e998cd41ac32afe30a)。

计算可抢占线程优先级（Preemptible Thread Priority）。

<a id="r_ga5fd4365cb6e8742e750b5e4950fb1e47"></a>

```c
#define K_HIGHEST_THREAD_PRIO (-CONFIG_NUM_COOP_PRIORITIES)
```

相关声明：[K_HIGHEST_THREAD_PRIO](../thread_core_reference/P001_线程公共接口.md#ga5fd4365cb6e8742e750b5e4950fb1e47)。

最高、最紧急的线程优先级值。

<a id="r_gafa4bcc2fdfea5cd7c63d56f476b1b32f"></a>

```c
#define K_LOWEST_THREAD_PRIO CONFIG_NUM_PREEMPT_PRIORITIES
```

相关声明：[K_LOWEST_THREAD_PRIO](../thread_core_reference/P001_线程公共接口.md#gafa4bcc2fdfea5cd7c63d56f476b1b32f)。

最低、最不紧急的线程优先级值，由空闲线程（Idle Thread）使用。

<a id="r_ga8f3f1d910dd847f0b223a4aa00788fa2"></a>

```c
#define K_IDLE_PRIO K_LOWEST_THREAD_PRIO
```

相关声明：[K_IDLE_PRIO](../thread_core_reference/P001_线程公共接口.md#ga8f3f1d910dd847f0b223a4aa00788fa2)、[K_LOWEST_THREAD_PRIO](../thread_core_reference/P001_线程公共接口.md#gafa4bcc2fdfea5cd7c63d56f476b1b32f)。

空闲线程的优先级。

<a id="r_gab326c7eb1d248650e6017dcaee8d24b2"></a>

```c
#define K_HIGHEST_APPLICATION_THREAD_PRIO (K_HIGHEST_THREAD_PRIO)
```

相关声明：[K_HIGHEST_APPLICATION_THREAD_PRIO](../thread_core_reference/P001_线程公共接口.md#gab326c7eb1d248650e6017dcaee8d24b2)、[K_HIGHEST_THREAD_PRIO](../thread_core_reference/P001_线程公共接口.md#ga5fd4365cb6e8742e750b5e4950fb1e47)。

应用线程可使用的最高优先级。

<a id="r_gad4c2df561988fa1194c2f8c768d667cd"></a>

```c
#define K_LOWEST_APPLICATION_THREAD_PRIO (K_LOWEST_THREAD_PRIO - 1)
```

相关声明：[K_LOWEST_APPLICATION_THREAD_PRIO](../thread_core_reference/P001_线程公共接口.md#gad4c2df561988fa1194c2f8c768d667cd)、[K_LOWEST_THREAD_PRIO](../thread_core_reference/P001_线程公共接口.md#gafa4bcc2fdfea5cd7c63d56f476b1b32f)。

应用线程可使用的最低优先级。

<a id="r_gad503fbcca905a9266b0e154e3ded258c"></a>

```c
#define K_ESSENTIAL (BIT(0))
```

相关声明：[K_ESSENTIAL](../thread_core_reference/P001_线程公共接口.md#gad503fbcca905a9266b0e154e3ded258c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

不得中止的系统线程（System Thread）。

<a id="r_gab18cf1e8728e7adf53db2ae4bbcdd951"></a>

```c
#define K_FP_REGS (BIT(K_FP_IDX))
```

相关声明：[K_FP_REGS](../thread_core_reference/P001_线程公共接口.md#gab18cf1e8728e7adf53db2ae4bbcdd951)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

由上下文切换管理浮点单元（Floating Point Unit，FPU）寄存器。

<a id="r_gacb5340339892f22301e02697c6039ccc"></a>

```c
#define K_USER (BIT(2))
```

相关声明：[K_USER](../thread_core_reference/P001_线程公共接口.md#gacb5340339892f22301e02697c6039ccc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

用户模式线程（User-mode Thread）。

<a id="r_gaa1788a413a055745d1de71b4da7c2eb2"></a>

```c
#define K_INHERIT_PERMS (BIT(3))
```

相关声明：[K_INHERIT_PERMS](../thread_core_reference/P001_线程公共接口.md#gaa1788a413a055745d1de71b4da7c2eb2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

继承权限（Inherit Permissions）。

<a id="r_gacbdb579370978fe07e4a863a84bd8bee"></a>

```c
#define K_CALLBACK_STATE (BIT(4))
```

相关声明：[K_CALLBACK_STATE](../thread_core_reference/P001_线程公共接口.md#gacbdb579370978fe07e4a863a84bd8bee)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

回调项状态（Callback Item State）。

<a id="r_ga8e1aeb428a418ed23e17448b796363cb"></a>

```c
#define K_DSP_REGS (BIT(K_DSP_IDX))
```

相关声明：[K_DSP_REGS](../thread_core_reference/P001_线程公共接口.md#ga8e1aeb428a418ed23e17448b796363cb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

由上下文切换管理数字信号处理（Digital Signal Processing，DSP）寄存器。

<a id="r_ga718088c1a68f03fffa960164cab60b72"></a>

```c
#define K_AGU_REGS (BIT(K_AGU_IDX))
```

相关声明：[K_AGU_REGS](../thread_core_reference/P001_线程公共接口.md#ga718088c1a68f03fffa960164cab60b72)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

由上下文切换管理地址生成单元（Address Generation Unit，AGU）寄存器。

<a id="r_gaa5b7de51b26773aa4485a711a041d9a7"></a>

```c
#define K_SSE_REGS (BIT(15))
```

相关声明：[K_SSE_REGS](../thread_core_reference/P001_线程公共接口.md#gaa5b7de51b26773aa4485a711a041d9a7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

在 x86 上，由上下文切换管理浮点（FP）和 SSE 寄存器。

<a id="r_gafec540511e6d2e0a074a5bfb515c53b0"></a>

```c
#define k_thread_access_grant(thread, ...)
```

相关声明：[k_thread_access_grant](../thread_core_reference/P001_线程公共接口.md#gafec540511e6d2e0a074a5bfb515c53b0)。

授予线程访问一组内核对象的权限。

<a id="r_gab3ced58648ca35788a40676e8478ecd2"></a>

```c
#define K_THREAD_DEFINE(name, stack_size, entry, p1, p2, p3, prio, options, delay)
```

相关声明：[K_THREAD_DEFINE](../thread_core_reference/P001_线程公共接口.md#gab3ced58648ca35788a40676e8478ecd2)。

静态定义并初始化线程。

<a id="r_gae25853424ec969f8431862c46b3ec294"></a>

```c
#define K_KERNEL_THREAD_DEFINE(name, stack_size, entry, p1, p2, p3, prio, options, delay)
```

相关声明：[K_KERNEL_THREAD_DEFINE](../thread_core_reference/P001_线程公共接口.md#gae25853424ec969f8431862c46b3ec294)。

静态定义并初始化一个仅在内核模式（Kernel Mode）运行的线程。

<a id="r_ga3d9541cfe2e8395af66d186efa77362f"></a>

```c
#define K_NO_WAIT Z_TIMEOUT_NO_WAIT
```

相关声明：[K_NO_WAIT](../timer_reference/P086_系统时钟公共接口.md#ga3d9541cfe2e8395af66d186efa77362f)。

生成零超时延迟（Null Timeout Delay）。

<a id="r_gae2f3a80170afc5fbce0337cdf5a4ce4c"></a>

```c
#define K_NSEC(t)
```

相关声明：[K_NSEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gae2f3a80170afc5fbce0337cdf5a4ce4c)。

根据纳秒值生成超时延迟（Timeout Delay）。

<a id="r_ga91198e325210ec052a8308e642058c0b"></a>

```c
#define K_USEC(t)
```

相关声明：[K_USEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga91198e325210ec052a8308e642058c0b)。

根据微秒值生成超时延迟（Timeout Delay）。

<a id="r_gab41f59fd2b724cb1279e4f6821154b33"></a>

```c
#define K_CYC(t)
```

相关声明：[K_CYC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gab41f59fd2b724cb1279e4f6821154b33)。

根据时钟周期数（Cycles）生成超时延迟（Timeout Delay）。

<a id="r_gaeda983960bd25f1dba7a386ad720e395"></a>

```c
#define K_TICKS(t)
```

相关声明：[K_TICKS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaeda983960bd25f1dba7a386ad720e395)。

根据系统节拍数（System Ticks）生成超时延迟（Timeout Delay）。

<a id="r_ga302af954e87b10a9b731f1ad07775e9f"></a>

```c
#define K_MSEC(ms)
```

相关声明：[K_MSEC](../timer_reference/P086_系统时钟公共接口.md#ga302af954e87b10a9b731f1ad07775e9f)。

根据毫秒值生成超时延迟（Timeout Delay）。

<a id="r_gadc361472aea59267f6ea38f5e7c7ca2a"></a>

```c
#define K_SECONDS(s)
```

相关声明：[K_SECONDS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gadc361472aea59267f6ea38f5e7c7ca2a)。

根据秒值生成超时延迟（Timeout Delay）。

<a id="r_gaef02f20d4d2ebfc9aa29acae01bd3698"></a>

```c
#define K_MINUTES(m)
```

相关声明：[K_MINUTES](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaef02f20d4d2ebfc9aa29acae01bd3698)。

根据分钟值生成超时延迟（Timeout Delay）。

<a id="r_gaa9e0cd890db28965b66d4bc5d719a91f"></a>

```c
#define K_HOURS(h)
```

相关声明：[K_HOURS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaa9e0cd890db28965b66d4bc5d719a91f)。

根据小时值生成超时延迟（Timeout Delay）。

<a id="r_ga0bb4b83f0222193b21a8910311bab0ca"></a>

```c
#define K_FOREVER Z_FOREVER
```

相关声明：[K_FOREVER](../timer_reference/P086_系统时钟公共接口.md#ga0bb4b83f0222193b21a8910311bab0ca)。

生成无限超时延迟（Infinite Timeout Delay）。

<a id="r_ga23f8926e4a14fba3694b92ce763d47fb"></a>

```c
#define K_TIMEOUT_SUM(timeout1, timeout2)
```

相关声明：[K_TIMEOUT_SUM](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga23f8926e4a14fba3694b92ce763d47fb)。

将两个 `k_timeout_t` 值相加。

<a id="r_gaa267fcb0a2e18cd0da29e9f9612510a6"></a>

```c
#define K_TIMER_DEFINE(name, expiry_fn, stop_fn)
```

相关声明：[K_TIMER_DEFINE](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#gaa267fcb0a2e18cd0da29e9f9612510a6)。

静态定义并初始化定时器（Timer）。

<a id="r_gacd0bc309f0147d4669f65fafa87e0e70"></a>

```c
#define K_QUEUE_DEFINE(name)
```

相关声明：[K_QUEUE_DEFINE](../queue_reference/P001_通用队列公共接口.md#gacd0bc309f0147d4669f65fafa87e0e70)。

静态定义并初始化队列（Queue）。

<a id="r_ga093449cc6686d3235944f3faad284893"></a>

```c
#define K_EVENT_DEFINE(name)
```

相关声明：[K_EVENT_DEFINE](../eventpoll_reference/P001_事件公共接口.md#ga093449cc6686d3235944f3faad284893)。

静态定义并初始化一个事件对象。

<a id="r_gaeebf6ef54d4be61e19408f44a734a159"></a>

```c
#define k_fifo_init(fifo)
```

相关声明：[k_fifo_init](../queue_reference/P003_FIFO公共接口.md#gaeebf6ef54d4be61e19408f44a734a159)。

初始化先进先出队列（First In, First Out，FIFO）。

<a id="r_gab744080af449e093df8dd4982e013e16"></a>

```c
#define k_fifo_cancel_wait(fifo)
```

相关声明：[k_fifo_cancel_wait](../queue_reference/P003_FIFO公共接口.md#gab744080af449e093df8dd4982e013e16)。

取消对FIFO队列的等待。

<a id="r_ga3addb10f86f19e245c23362433d5c913"></a>

```c
#define k_fifo_put(fifo, data)
```

相关声明：[k_fifo_put](../queue_reference/P003_FIFO公共接口.md#ga3addb10f86f19e245c23362433d5c913)。

向FIFO队列加入一个元素。

<a id="r_gab1c5212040d12cbb92cede5cf54928ba"></a>

```c
#define k_fifo_alloc_put(fifo, data)
```

相关声明：[k_fifo_alloc_put](../queue_reference/P003_FIFO公共接口.md#gab1c5212040d12cbb92cede5cf54928ba)。

向FIFO队列加入一个元素。

<a id="r_ga1bf5f52290c83e54ba14358cbbb4051b"></a>

```c
#define k_fifo_put_list(fifo, head, tail)
```

相关声明：[k_fifo_put_list](../queue_reference/P003_FIFO公共接口.md#ga1bf5f52290c83e54ba14358cbbb4051b)。

以原子方式向FIFO加入一个元素链表。

<a id="r_ga4cdc286a7a6f0d43acab63a4846815e7"></a>

```c
#define k_fifo_put_slist(fifo, list)
```

相关声明：[k_fifo_put_slist](../queue_reference/P003_FIFO公共接口.md#ga4cdc286a7a6f0d43acab63a4846815e7)。

以原子方式向FIFO队列加入一个元素链表。

<a id="r_ga1e2c480e2124116af97e94e7b4435de6"></a>

```c
#define k_fifo_get(fifo, timeout)
```

相关声明：[k_fifo_get](../queue_reference/P003_FIFO公共接口.md#ga1e2c480e2124116af97e94e7b4435de6)。

从FIFO队列取得一个元素。

<a id="r_gab7cec4adc128ed1fd2d194ba6cd8c640"></a>

```c
#define k_fifo_is_empty(fifo)
```

相关声明：[k_fifo_is_empty](../queue_reference/P003_FIFO公共接口.md#gab7cec4adc128ed1fd2d194ba6cd8c640)。

查询FIFO队列是否有可用数据。

<a id="r_ga2e0c8608f095a929740fa94c94a4f389"></a>

```c
#define k_fifo_peek_head(fifo)
```

相关声明：[k_fifo_peek_head](../queue_reference/P003_FIFO公共接口.md#ga2e0c8608f095a929740fa94c94a4f389)。

查看FIFO队列头部元素（Peek）。

<a id="r_gafbe2ce9a6437b886cf149016187ba92f"></a>

```c
#define k_fifo_peek_tail(fifo)
```

相关声明：[k_fifo_peek_tail](../queue_reference/P003_FIFO公共接口.md#gafbe2ce9a6437b886cf149016187ba92f)。

查看FIFO队列尾部元素（Peek）。

<a id="r_ga230b02a526ecb0ae1598be75cb9a8274"></a>

```c
#define K_FIFO_DEFINE(name)
```

相关声明：[K_FIFO_DEFINE](../queue_reference/P003_FIFO公共接口.md#ga230b02a526ecb0ae1598be75cb9a8274)。

静态定义并初始化FIFO队列。

<a id="r_ga69fb19716a9014f7de79f8e524d64a3e"></a>

```c
#define k_lifo_init(lifo)
```

相关声明：[k_lifo_init](../queue_reference/P005_LIFO公共接口.md#ga69fb19716a9014f7de79f8e524d64a3e)。

初始化后进先出队列（Last In, First Out，LIFO）。

<a id="r_gad662e36b1df8b9013e2dc61f9dfe3a8b"></a>

```c
#define k_lifo_put(lifo, data)
```

相关声明：[k_lifo_put](../queue_reference/P005_LIFO公共接口.md#gad662e36b1df8b9013e2dc61f9dfe3a8b)。

向LIFO队列加入一个元素。

<a id="r_ga96d885a6a36fcfcb5eaa65898eee0965"></a>

```c
#define k_lifo_alloc_put(lifo, data)
```

相关声明：[k_lifo_alloc_put](../queue_reference/P005_LIFO公共接口.md#ga96d885a6a36fcfcb5eaa65898eee0965)。

向LIFO队列加入一个元素。

<a id="r_gad5f1775947b07a2a77f667aa9e41db5a"></a>

```c
#define k_lifo_get(lifo, timeout)
```

相关声明：[k_lifo_get](../queue_reference/P005_LIFO公共接口.md#gad5f1775947b07a2a77f667aa9e41db5a)。

从LIFO队列取得一个元素。

<a id="r_gaebd450d4181f22491623ea0aed6ee576"></a>

```c
#define K_LIFO_DEFINE(name)
```

相关声明：[K_LIFO_DEFINE](../queue_reference/P005_LIFO公共接口.md#gaebd450d4181f22491623ea0aed6ee576)。

静态定义并初始化LIFO队列。

<a id="r_ga8c9ca77e5de3c9757dcd4ecb55797835"></a>

```c
#define K_STACK_DEFINE(name, stack_num_entries)
```

相关声明：[K_STACK_DEFINE](../msgstack_reference/P004_栈公共接口.md#ga8c9ca77e5de3c9757dcd4ecb55797835)。

静态定义并初始化一个栈（Stack）。

<a id="r_gab6f3d98fabbdc0918bbc9934d61d63f3"></a>

```c
#define K_MUTEX_DEFINE(name)
```

相关声明：[K_MUTEX_DEFINE](../synchronization_reference/P006_互斥量公共接口.md#gab6f3d98fabbdc0918bbc9934d61d63f3)。

静态定义并初始化互斥量（Mutex）。

<a id="r_ga770816651e25f7e7dae992a0b2260c21"></a>

```c
#define K_CONDVAR_DEFINE(name)
```

相关声明：[K_CONDVAR_DEFINE](../synchronization_reference/P010_条件变量公共接口.md#ga770816651e25f7e7dae992a0b2260c21)。

静态定义并初始化条件变量（Condition Variable）。

<a id="r_ga689359a77a0cebe737ef644c188f7e57"></a>

```c
#define K_SEM_MAX_LIMIT UINT_MAX
```

相关声明：[K_SEM_MAX_LIMIT](../synchronization_reference/P008_信号量公共接口.md#ga689359a77a0cebe737ef644c188f7e57)。

信号量所允许的最大上限值。

<a id="r_ga018a8aa43e02e704deee7b6341502946"></a>

```c
#define K_SEM_DEFINE(name, initial_count, count_limit)
```

相关声明：[K_SEM_DEFINE](../synchronization_reference/P008_信号量公共接口.md#ga018a8aa43e02e704deee7b6341502946)。

静态定义并初始化信号量（Semaphore）。

<a id="r_ga893b281f3d2bc0088650536899e17903"></a>

```c
#define K_WORK_DELAYABLE_DEFINE(work, work_handler)
```

相关声明：[K_WORK_DELAYABLE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga893b281f3d2bc0088650536899e17903)。

初始化静态定义的可延迟工作项（Delayable Work Item）。

<a id="r_ga4f3eac1fc56d5c9c21a3afa9b964b0bf"></a>

```c
#define K_WORK_USER_DEFINE(work, work_handler)
```

相关声明：[K_WORK_USER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga4f3eac1fc56d5c9c21a3afa9b964b0bf)。

初始化静态定义的用户工作项（User Work Item）。

<a id="r_gaf8e003eefa5dd66ba883688f9d39c333"></a>

```c
#define K_WORK_DEFINE(work, work_handler)
```

相关声明：[K_WORK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaf8e003eefa5dd66ba883688f9d39c333)。

初始化静态定义的工作项（Work Item）。

<a id="r_ga95ef93002766901511d09c8cd8f8293b"></a>

```c
#define K_MSGQ_DEFINE(q_name, q_msg_size, q_max_msgs, q_align)
```

相关声明：[K_MSGQ_DEFINE](../msgstack_reference/P001_消息队列公共接口.md#ga95ef93002766901511d09c8cd8f8293b)。

静态定义并初始化一个消息队列。

<a id="r_ga15e39d40c8659be688d41e2201959c4c"></a>

```c
#define K_MSGQ_DEFINE_STATIC(q_name, q_msg_size, q_max_msgs, q_align)
```

相关声明：[K_MSGQ_DEFINE_STATIC](../msgstack_reference/P001_消息队列公共接口.md#ga15e39d40c8659be688d41e2201959c4c)。

在私有（static）作用域内静态定义并初始化一个消息队列。

<a id="r_gab17e888412dd4d299dc68816a24de78a"></a>

```c
#define K_MSGQ_DEFINE_TYPE(q_name, q_msg_type, q_max_msgs)
```

相关声明：[K_MSGQ_DEFINE_TYPE](../msgstack_reference/P001_消息队列公共接口.md#gab17e888412dd4d299dc68816a24de78a)。

为指定类型的消息静态定义并初始化一个消息队列。

<a id="r_ga0f01b9e30429458e184f202c3701c54a"></a>

```c
#define K_MSGQ_DEFINE_STATIC_TYPE(q_name, q_msg_type, q_max_msgs)
```

相关声明：[K_MSGQ_DEFINE_STATIC_TYPE](../msgstack_reference/P001_消息队列公共接口.md#ga0f01b9e30429458e184f202c3701c54a)。

在私有（static）作用域内为指定类型的消息静态定义并初始化一个消息队列。

<a id="r_gab55cba898db47113a06641c01f3e3714"></a>

```c
#define K_MBOX_DEFINE(name)
```

相关声明：[K_MBOX_DEFINE](../mboxpipe_reference/P001_邮箱公共接口.md#gab55cba898db47113a06641c01f3e3714)。

静态定义并初始化一个邮箱。

<a id="r_gac2256aa00c59e78199be9bdefd61aa52"></a>

```c
#define K_PIPE_DEFINE(name, pipe_buffer_size, pipe_align)
```

相关声明：[K_PIPE_DEFINE](../mboxpipe_reference/P004_管道公共接口.md#gac2256aa00c59e78199be9bdefd61aa52)。

静态定义并初始化一个管道。

<a id="r_ga6b6751464262505c1117dea1bea56a08"></a>

```c
#define K_MEM_SLAB_DEFINE_IN_SECT(name, in_section, slab_block_size, slab_num_blocks, slab_align)
```

相关声明：[K_MEM_SLAB_DEFINE_IN_SECT](../heap_reference/P003_固定块内存池公共接口.md#ga6b6751464262505c1117dea1bea56a08)。

在用户提供的内存段中，以公开（非static）作用域静态定义并初始化固定块内存池（Memory Slab）。

<a id="r_ga60bc92eee58fcc5f121b8e4d82eaa69e"></a>

```c
#define K_MEM_SLAB_DEFINE(name, slab_block_size, slab_num_blocks, slab_align)
```

相关声明：[K_MEM_SLAB_DEFINE](../heap_reference/P003_固定块内存池公共接口.md#ga60bc92eee58fcc5f121b8e4d82eaa69e)。

以公开（非static）作用域静态定义并初始化固定块内存池。

<a id="r_ga8af8242518910449d31f7e97bed738cc"></a>

```c
#define K_MEM_SLAB_DEFINE_TYPE(name, type, slab_num_blocks)
```

相关声明：[K_MEM_SLAB_DEFINE_TYPE](../heap_reference/P003_固定块内存池公共接口.md#ga8af8242518910449d31f7e97bed738cc)。

以公开（非static）作用域，为指定类型的块静态定义并初始化固定块内存池。

<a id="r_ga7f0750f940b9a9f94b5c52373d4161f1"></a>

```c
#define K_MEM_SLAB_DEFINE_IN_SECT_STATIC(name, in_section, slab_block_size, slab_num_blocks, slab_align)
```

相关声明：[K_MEM_SLAB_DEFINE_IN_SECT_STATIC](../heap_reference/P003_固定块内存池公共接口.md#ga7f0750f940b9a9f94b5c52373d4161f1)。

在用户提供的内存段中，以私有（static）作用域静态定义并初始化固定块内存池。

<a id="r_ga90bdbb15f410991f54ba16025c24bc3c"></a>

```c
#define K_MEM_SLAB_DEFINE_STATIC(name, slab_block_size, slab_num_blocks, slab_align)
```

相关声明：[K_MEM_SLAB_DEFINE_STATIC](../heap_reference/P003_固定块内存池公共接口.md#ga90bdbb15f410991f54ba16025c24bc3c)。

以私有（static）作用域静态定义并初始化固定块内存池。

<a id="r_ga11eac52a1ed0b0f8231c62e609515c42"></a>

```c
#define K_MEM_SLAB_DEFINE_STATIC_TYPE(name, type, slab_num_blocks)
```

相关声明：[K_MEM_SLAB_DEFINE_STATIC_TYPE](../heap_reference/P003_固定块内存池公共接口.md#ga11eac52a1ed0b0f8231c62e609515c42)。

以私有（static）作用域，为指定类型的块静态定义并初始化固定块内存池。

<a id="r_ga795d7f1e6d5b7b19a7a50198d7829a0f"></a>

```c
#define K_HEAP_DEFINE(name, bytes)
```

相关声明：[K_HEAP_DEFINE](../heap_reference/P001_内核堆公共接口.md#ga795d7f1e6d5b7b19a7a50198d7829a0f)。

定义一个静态k_heap。

<a id="r_ga968f4c6a201fdf6862d62dd5d9f8d032"></a>

```c
#define K_HEAP_DEFINE_NOCACHE(name, bytes)
```

相关声明：[K_HEAP_DEFINE_NOCACHE](../heap_reference/P001_内核堆公共接口.md#ga968f4c6a201fdf6862d62dd5d9f8d032)。

在非缓存内存（Uncached Memory）中定义一个静态k_heap。

<a id="r_ga6d6321e189afca73a276cd671ec531ae"></a>

```c
#define K_POLL_SIGNAL_INITIALIZER(obj)
```

相关声明：[K_POLL_SIGNAL_INITIALIZER](../eventpoll_reference/P003_轮询公共接口.md#ga6d6321e189afca73a276cd671ec531ae)。

静态初始化轮询信号。

<a id="r_ga8e3889f2bac281a6e65e31068e58047e"></a>

```c
#define K_POLL_EVENT_INITIALIZER(_event_type, _event_mode, _event_obj)
```

相关声明：[K_POLL_EVENT_INITIALIZER](../eventpoll_reference/P003_轮询公共接口.md#ga8e3889f2bac281a6e65e31068e58047e)。

静态初始化轮询事件。

<a id="r_gada2366896d913dc916b3c28642648b63"></a>

```c
#define K_POLL_EVENT_STATIC_INITIALIZER(_event_type, _event_mode, _event_obj, event_tag)
```

相关声明：[K_POLL_EVENT_STATIC_INITIALIZER](../eventpoll_reference/P003_轮询公共接口.md#gada2366896d913dc916b3c28642648b63)。

静态初始化轮询事件，并附带用户标签（User Tag）。

<a id="r_abde5aa8ca5e64a045b25b88f91370dcd"></a>

```c
#define k_oops()
```

相关声明：[k_oops](#abde5aa8ca5e64a045b25b88f91370dcd)。

因致命错误终止线程（Thread）。

<a id="r_aedd541f707b1463aaac15c7798340329"></a>

```c
#define k_panic()
```

相关声明：[k_panic](#aedd541f707b1463aaac15c7798340329)。

因致命错误终止系统（System）。

<a id="define-members-0"></a>

### 轮询事件类型（Poll event types）

k_poll_event.type位域使用的值。

<a id="r_gafd5d801eb9e9cf6097b2c08b4933998e"></a>

```c
#define K_POLL_TYPE_IGNORE 0
```

相关声明：[K_POLL_TYPE_IGNORE](../eventpoll_reference/P003_轮询公共接口.md#gafd5d801eb9e9cf6097b2c08b4933998e)。

k_poll()忽略此事件。

<a id="r_ga144d8eb34d85f6053e454410a10bf56a"></a>

```c
#define K_POLL_TYPE_SIGNAL Z_POLL_TYPE_BIT(_POLL_TYPE_SIGNAL)
```

相关声明：[K_POLL_TYPE_SIGNAL](../eventpoll_reference/P003_轮询公共接口.md#ga144d8eb34d85f6053e454410a10bf56a)。

轮询信号是否已触发。

<a id="r_ga0fd7605bdffd43dff7480a90a603ffde"></a>

```c
#define K_POLL_TYPE_SEM_AVAILABLE Z_POLL_TYPE_BIT(_POLL_TYPE_SEM_AVAILABLE)
```

相关声明：[K_POLL_TYPE_SEM_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga0fd7605bdffd43dff7480a90a603ffde)。

轮询信号量是否变为可用。

<a id="r_ga58d656f73f031a39b8a936133fe5504f"></a>

```c
#define K_POLL_TYPE_DATA_AVAILABLE Z_POLL_TYPE_BIT(_POLL_TYPE_DATA_AVAILABLE)
```

相关声明：[K_POLL_TYPE_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga58d656f73f031a39b8a936133fe5504f)。

轮询队列中是否有数据可用。

<a id="r_ga71734fee18c523cf70276260118afb91"></a>

```c
#define K_POLL_TYPE_FIFO_DATA_AVAILABLE K_POLL_TYPE_DATA_AVAILABLE
```

相关声明：[K_POLL_TYPE_FIFO_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga71734fee18c523cf70276260118afb91)、[K_POLL_TYPE_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga58d656f73f031a39b8a936133fe5504f)。

轮询先进先出队列（FIFO）中是否有数据可用。

<a id="r_ga7b45350902d604f16de5e49087db92a4"></a>

```c
#define K_POLL_TYPE_LIFO_DATA_AVAILABLE K_POLL_TYPE_DATA_AVAILABLE
```

相关声明：[K_POLL_TYPE_LIFO_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga7b45350902d604f16de5e49087db92a4)、[K_POLL_TYPE_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga58d656f73f031a39b8a936133fe5504f)。

轮询后进先出队列（LIFO）中是否有数据可用。

<a id="r_gaa83509b54175fb6c98324422a928d5e1"></a>

```c
#define K_POLL_TYPE_MSGQ_DATA_AVAILABLE Z_POLL_TYPE_BIT(_POLL_TYPE_MSGQ_DATA_AVAILABLE)
```

相关声明：[K_POLL_TYPE_MSGQ_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gaa83509b54175fb6c98324422a928d5e1)。

轮询消息队列中是否有数据可用。

<a id="r_ga14e113201a3b3ad768c6a5ce917d1912"></a>

```c
#define K_POLL_TYPE_PIPE_DATA_AVAILABLE Z_POLL_TYPE_BIT(_POLL_TYPE_PIPE_DATA_AVAILABLE)
```

相关声明：[K_POLL_TYPE_PIPE_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga14e113201a3b3ad768c6a5ce917d1912)。

轮询管道中是否有数据可用。

<a id="define-members-1"></a>

### 轮询事件状态（Poll event states）

k_poll_event.state位域使用的值。

<a id="r_ga522822c5e06a89b22ce4dcefd10c66aa"></a>

```c
#define K_POLL_STATE_NOT_READY 0
```

相关声明：[K_POLL_STATE_NOT_READY](../eventpoll_reference/P003_轮询公共接口.md#ga522822c5e06a89b22ce4dcefd10c66aa)。

所轮询的条件尚未发生。

<a id="r_ga478aae7fe4fb5c7b7c76ed216c22a7f1"></a>

```c
#define K_POLL_STATE_SIGNALED Z_POLL_STATE_BIT(_POLL_STATE_SIGNALED)
```

相关声明：[K_POLL_STATE_SIGNALED](../eventpoll_reference/P003_轮询公共接口.md#ga478aae7fe4fb5c7b7c76ed216c22a7f1)。

轮询信号已触发。

<a id="r_gae9e3eefd5a29a538d22f53592578bb37"></a>

```c
#define K_POLL_STATE_SEM_AVAILABLE Z_POLL_STATE_BIT(_POLL_STATE_SEM_AVAILABLE)
```

相关声明：[K_POLL_STATE_SEM_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gae9e3eefd5a29a538d22f53592578bb37)。

信号量已变为可用。

<a id="r_gac166d9919d591bace163c5211e7b41f4"></a>

```c
#define K_POLL_STATE_DATA_AVAILABLE Z_POLL_STATE_BIT(_POLL_STATE_DATA_AVAILABLE)
```

相关声明：[K_POLL_STATE_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gac166d9919d591bace163c5211e7b41f4)。

队列中已有数据可用。

<a id="r_gabd5ac3341698534f39ded718079d6168"></a>

```c
#define K_POLL_STATE_FIFO_DATA_AVAILABLE K_POLL_STATE_DATA_AVAILABLE
```

相关声明：[K_POLL_STATE_FIFO_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gabd5ac3341698534f39ded718079d6168)、[K_POLL_STATE_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gac166d9919d591bace163c5211e7b41f4)。

先进先出队列（FIFO）中已有数据可用。

<a id="r_gac66d063d5ffa24179b56ac8217a922e3"></a>

```c
#define K_POLL_STATE_LIFO_DATA_AVAILABLE K_POLL_STATE_DATA_AVAILABLE
```

相关声明：[K_POLL_STATE_LIFO_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gac66d063d5ffa24179b56ac8217a922e3)、[K_POLL_STATE_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gac166d9919d591bace163c5211e7b41f4)。

后进先出队列（LIFO）中已有数据可用。

<a id="r_gac236074cd43f59f28b803fe2c4a4f6f7"></a>

```c
#define K_POLL_STATE_MSGQ_DATA_AVAILABLE Z_POLL_STATE_BIT(_POLL_STATE_MSGQ_DATA_AVAILABLE)
```

相关声明：[K_POLL_STATE_MSGQ_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gac236074cd43f59f28b803fe2c4a4f6f7)。

消息队列中已有数据可用。

<a id="r_ga9028d6868ee964ca25931ed9170068dd"></a>

```c
#define K_POLL_STATE_PIPE_DATA_AVAILABLE Z_POLL_STATE_BIT(_POLL_STATE_PIPE_DATA_AVAILABLE)
```

相关声明：[K_POLL_STATE_PIPE_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga9028d6868ee964ca25931ed9170068dd)。

管道中已有数据可用。

<a id="r_gadaf4b4c8e13afb54114af72d133e1fdb"></a>

```c
#define K_POLL_STATE_CANCELLED Z_POLL_STATE_BIT(_POLL_STATE_CANCELLED)
```

相关声明：[K_POLL_STATE_CANCELLED](../eventpoll_reference/P003_轮询公共接口.md#gadaf4b4c8e13afb54114af72d133e1fdb)。

对被轮询对象的等待已取消，例如：

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_gaf9f23a6ff9dae76af56f25b373e74c75"></a>

```c
typedef void(* k_thread_user_cb_t) (const struct k_thread *thread, void *user_data)
```

相关声明：[k_thread_user_cb_t](../thread_core_reference/P001_线程公共接口.md#gaf9f23a6ff9dae76af56f25b373e74c75)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

线程遍历函数使用的回调类型（Callback Type）。

<a id="r_ga2915762e70454d98c73c179a45cafbde"></a>

```c
typedef void(* k_timer_expiry_t) (struct k_timer *timer)
```

相关声明：[k_timer_expiry_t](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga2915762e70454d98c73c179a45cafbde)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

定时器到期函数类型（Timer Expiry Function Type）。

<a id="r_ga106733712fc4e62b59bbe6a480bb988c"></a>

```c
typedef void(* k_timer_stop_t) (struct k_timer *timer)
```

相关声明：[k_timer_stop_t](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga106733712fc4e62b59bbe6a480bb988c)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

定时器停止函数类型（Timer Stop Function Type）。

<a id="r_abc484ff16f6bef4434de98258189e7d5"></a>

```c
typedef void(* k_ipi_func_t) (struct k_ipi_work *work)
```

相关声明：[k_ipi_func_t](#abc484ff16f6bef4434de98258189e7d5)、[k_ipi_work](../kernel_runtime_model_reference/P002_k_ipi_work_结构体.md)。

处理器间中断（IPI）工作项处理函数（Handler）的函数类型。

<a id="r_ga5add9ef0dce306a08413c4140fc0bdda"></a>

```c
typedef void(* k_work_handler_t) (struct k_work *work)
```

相关声明：[k_work_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga5add9ef0dce306a08413c4140fc0bdda)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

工作项处理函数（Work Item Handler）的函数签名。

<a id="r_gaafa4dfac323cab570da1ee31c07d11bc"></a>

```c
typedef void(* k_work_user_handler_t) (struct k_work_user *work)
```

相关声明：[k_work_user_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaafa4dfac323cab570da1ee31c07d11bc)。

用户工作队列（User Work Queue）的工作项处理函数（Handler）类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.4\_枚举（Enumerations）

<a id="r_gab0b42f9804777dfa5fed2b7cd866779c"></a>

```c
enum execution_context_types { K_ISR = 0 , K_COOP_THREAD , K_PREEMPT_THREAD }
```

相关声明：[execution_context_types](../api_device_topic_reference/P013_内核 API（Kernel APIs）.md#gab0b42f9804777dfa5fed2b7cd866779c)、[K_ISR](../api_device_topic_reference/P013_内核 API（Kernel APIs）.md#ggab0b42f9804777dfa5fed2b7cd866779ca30593044743695f8184a157283dac4d5)、[K_COOP_THREAD](../api_device_topic_reference/P013_内核 API（Kernel APIs）.md#ggab0b42f9804777dfa5fed2b7cd866779ca62c0b731a1bb3c5e4aadeba3f93df58b)、[K_PREEMPT_THREAD](../api_device_topic_reference/P013_内核 API（Kernel APIs）.md#ggab0b42f9804777dfa5fed2b7cd866779cae84f57f4ac996c751d1f4c9e49789322)。

执行上下文（execution contexts）的类型。

<a id="r_gae539da4c3f3d31b039bc49b9e76744eb"></a>

```c
enum { K_WORK_RUNNING = BIT(K_WORK_RUNNING_BIT) , K_WORK_CANCELING = BIT(K_WORK_CANCELING_BIT) , K_WORK_QUEUED = BIT(K_WORK_QUEUED_BIT) , K_WORK_DELAYED = BIT(K_WORK_DELAYED_BIT) , K_WORK_FLUSHING = BIT(K_WORK_FLUSHING_BIT) }
```

相关声明：[K_WORK_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165)、[K_WORK_CANCELING](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732)、[K_WORK_QUEUED](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85)、[K_WORK_DELAYED](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed)、[K_WORK_FLUSHING](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601)。

工作项（Work Item）与工作队列（Work Queue）的状态标志值。

<a id="r_ga36d7978872a83191dd3cc16d62165add"></a>

```c
enum k_poll_modes { K_POLL_MODE_NOTIFY_ONLY = 0 , K_POLL_NUM_MODES }
```

相关声明：[k_poll_modes](../eventpoll_reference/P003_轮询公共接口.md#ga36d7978872a83191dd3cc16d62165add)、[K_POLL_MODE_NOTIFY_ONLY](../eventpoll_reference/P003_轮询公共接口.md#gga36d7978872a83191dd3cc16d62165adda22874743e2f6b0f1fd55c5375732b681)、[K_POLL_NUM_MODES](../eventpoll_reference/P003_轮询公共接口.md#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c)。

轮询事件的操作模式。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.5\_函数（Functions）

<a id="r_ga5d7f296b39346ea99a2a0efa3295b4a0"></a>

```c
static void k_thread_runtime_stats_longest_frame_reset (__maybe_unused struct k_thread *thread)
```

相关声明：[k_thread_runtime_stats_longest_frame_reset](../thread_core_reference/P001_线程公共接口.md#ga5d7f296b39346ea99a2a0efa3295b4a0)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

重置指定线程的最长帧使用量数据（Longest Frame Usage Data）。

<a id="r_gae2596d56800769b06fc03c194a126a97"></a>

```c
void k_thread_foreach (k_thread_user_cb_t user_cb, void *user_data)
```

相关声明：[k_thread_foreach](../thread_core_reference/P001_线程公共接口.md#gae2596d56800769b06fc03c194a126a97)、[k_thread_user_cb_t](../thread_core_reference/P001_线程公共接口.md#gaf9f23a6ff9dae76af56f25b373e74c75)。

遍历系统中的所有线程。

<a id="r_ga82a83c2db36b34596dcb5afa5b28e41c"></a>

```c
void k_thread_foreach_filter_by_cpu (unsigned int cpu, k_thread_user_cb_t user_cb, void *user_data)
```

相关声明：[k_thread_foreach_filter_by_cpu](../thread_core_reference/P001_线程公共接口.md#ga82a83c2db36b34596dcb5afa5b28e41c)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[k_thread_user_cb_t](../thread_core_reference/P001_线程公共接口.md#gaf9f23a6ff9dae76af56f25b373e74c75)。

遍历在指定 CPU 上运行的所有线程。

<a id="r_ga30ef8b445a6c1b4a82651674dbb737fc"></a>

```c
void k_thread_foreach_unlocked (k_thread_user_cb_t user_cb, void *user_data)
```

相关声明：[k_thread_foreach_unlocked](../thread_core_reference/P001_线程公共接口.md#ga30ef8b445a6c1b4a82651674dbb737fc)、[k_thread_user_cb_t](../thread_core_reference/P001_线程公共接口.md#gaf9f23a6ff9dae76af56f25b373e74c75)。

不加锁地遍历系统中的所有线程。

<a id="r_gad908a1b9014aa048cf12997804ab7be2"></a>

```c
void k_thread_foreach_unlocked_filter_by_cpu (unsigned int cpu, k_thread_user_cb_t user_cb, void *user_data)
```

相关声明：[k_thread_foreach_unlocked_filter_by_cpu](../thread_core_reference/P001_线程公共接口.md#gad908a1b9014aa048cf12997804ab7be2)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[k_thread_user_cb_t](../thread_core_reference/P001_线程公共接口.md#gaf9f23a6ff9dae76af56f25b373e74c75)。

不加锁地遍历在当前 CPU 上运行的线程。

<a id="r_gafe00cc70bac8a47ba6dda21bde508614"></a>

```c
k_thread_stack_t * k_thread_stack_alloc (size_t size, int flags)
```

相关声明：[k_thread_stack_t](../api_file_host_video_reference/P001_zephyr__arch__arch_interface.h_文件参考.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)、[k_thread_stack_alloc](../thread_core_reference/P001_线程公共接口.md#gafe00cc70bac8a47ba6dda21bde508614)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

动态分配线程栈（Thread Stack）。

<a id="r_ga95560cb85f6656b981a9a50ff2cd70b7"></a>

```c
int k_thread_stack_free (k_thread_stack_t *stack)
```

相关声明：[k_thread_stack_free](../thread_core_reference/P001_线程公共接口.md#ga95560cb85f6656b981a9a50ff2cd70b7)、[k_thread_stack_t](../api_file_host_video_reference/P001_zephyr__arch__arch_interface.h_文件参考.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)。

释放动态分配的线程栈。

<a id="r_gad5b0bff3102f1656089f5875d999a367"></a>

```c
k_tid_t k_thread_create (struct k_thread *new_thread, k_thread_stack_t *stack, size_t stack_size, k_thread_entry_t entry, void *p1, void *p2, void *p3, int prio, uint32_t options, k_timeout_t delay)
```

相关声明：[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)、[k_thread_create](../thread_core_reference/P001_线程公共接口.md#gad5b0bff3102f1656089f5875d999a367)、[k_thread](../thread_core_reference/P004_线程对象结构.md)、[k_thread_stack_t](../api_file_host_video_reference/P001_zephyr__arch__arch_interface.h_文件参考.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)、[k_thread_entry_t](../api_file_host_video_reference/P001_zephyr__arch__arch_interface.h_文件参考.md#a3707e886593b0a8b4995309e4230b717)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

创建线程。

<a id="r_ga3fbe1c8a5f3ef1c25382c7d6fca35764"></a>

```c
FUNC_NORETURN void k_thread_user_mode_enter (k_thread_entry_t entry, void *p1, void *p2, void *p3)
```

相关声明：[k_thread_user_mode_enter](../thread_core_reference/P001_线程公共接口.md#ga3fbe1c8a5f3ef1c25382c7d6fca35764)、[k_thread_entry_t](../api_file_host_video_reference/P001_zephyr__arch__arch_interface.h_文件参考.md#a3707e886593b0a8b4995309e4230b717)。

将线程权限永久降低到用户模式。

<a id="r_ga3f46c06833add2a2e0ddb7242f06702c"></a>

```c
static void k_thread_heap_assign (struct k_thread *thread, struct k_heap *heap)
```

相关声明：[k_thread_heap_assign](../thread_core_reference/P001_线程公共接口.md#ga3f46c06833add2a2e0ddb7242f06702c)、[k_thread](../thread_core_reference/P004_线程对象结构.md)、[k_heap](../heap_reference/P002_内核堆结构.md)。

为线程指定资源内存池（Resource Memory Pool）。

<a id="r_ga40a733561eb1f64dcaae0e01b167d233"></a>

```c
int k_thread_join (struct k_thread *thread, k_timeout_t timeout)
```

相关声明：[k_thread_join](../thread_core_reference/P001_线程公共接口.md#ga40a733561eb1f64dcaae0e01b167d233)、[k_thread](../thread_core_reference/P004_线程对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

睡眠，直到指定线程退出。

<a id="r_ga550b642e071480323e589866abb99c22"></a>

```c
void k_busy_wait (uint32_t usec_to_wait)
```

相关声明：[k_busy_wait](../thread_core_reference/P001_线程公共接口.md#ga550b642e071480323e589866abb99c22)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使当前线程忙等待（Busy Wait）。

<a id="r_ga366b9daa0be65b0a69dbc9f146064b68"></a>

```c
bool k_can_yield (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_can_yield](../thread_core_reference/P001_线程公共接口.md#ga366b9daa0be65b0a69dbc9f146064b68)。

检查当前上下文是否允许让出执行权（Yield）。

<a id="r_ga08a3484c33444ecedc2d71d78495a295"></a>

```c
void k_yield (void)
```

相关声明：[k_yield](../thread_core_reference/P001_线程公共接口.md#ga08a3484c33444ecedc2d71d78495a295)。

让当前线程让出执行权。

<a id="r_ga9275a019c8ff3c7fe49a81f8c078157e"></a>

```c
void k_wakeup (k_tid_t thread)
```

相关声明：[k_wakeup](../thread_core_reference/P001_线程公共接口.md#ga9275a019c8ff3c7fe49a81f8c078157e)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

唤醒正在睡眠的线程。

<a id="r_gac3b994b90b5bccded0895304f6b20c5d"></a>

```c
__attribute_const__ k_tid_t k_sched_current_thread_query (void)
```

相关声明：[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)、[k_sched_current_thread_query](../thread_core_reference/P001_线程公共接口.md#gac3b994b90b5bccded0895304f6b20c5d)。

查询当前线程的线程标识符（Thread ID）。

<a id="r_gae74e5de996276df767b96d4b50fa47ea"></a>

```c
static bool k_is_pre_kernel (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_is_pre_kernel](../thread_core_reference/P001_线程公共接口.md#gae74e5de996276df767b96d4b50fa47ea)。

检查启动过程是否仍处于主任务运行之前的阶段。

<a id="r_ga7ef1ed0fb9513df8096ede1e52fc76b2"></a>

```c
static __attribute_const__ k_tid_t k_current_get (void)
```

相关声明：[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)、[k_current_get](../thread_core_reference/P001_线程公共接口.md#ga7ef1ed0fb9513df8096ede1e52fc76b2)。

取得当前线程的线程标识符。

<a id="r_ga1f44bb0307bea7a97227764ecd7bf963"></a>

```c
void k_thread_abort (k_tid_t thread)
```

相关声明：[k_thread_abort](../thread_core_reference/P001_线程公共接口.md#ga1f44bb0307bea7a97227764ecd7bf963)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

中止线程（Abort）。

<a id="r_gab0b1c85b847fe74170c04538fa9949ff"></a>

```c
k_ticks_t k_thread_timeout_expires_ticks (const struct k_thread *thread)
```

相关声明：[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)、[k_thread_timeout_expires_ticks](../thread_core_reference/P001_线程公共接口.md#gab0b1c85b847fe74170c04538fa9949ff)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

以系统时钟节拍（System Ticks）为单位取得线程将被唤醒的时刻。

<a id="r_ga4688c095c86e037a18594efdb9a5e9b9"></a>

```c
k_ticks_t k_thread_timeout_remaining_ticks (const struct k_thread *thread)
```

相关声明：[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)、[k_thread_timeout_remaining_ticks](../thread_core_reference/P001_线程公共接口.md#ga4688c095c86e037a18594efdb9a5e9b9)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

以系统时钟节拍为单位取得线程被唤醒前的剩余时间。

<a id="r_ga3a46ed8ad2c3b12416fafe11325f82b3"></a>

```c
int k_thread_priority_get (k_tid_t thread)
```

相关声明：[k_thread_priority_get](../thread_core_reference/P001_线程公共接口.md#ga3a46ed8ad2c3b12416fafe11325f82b3)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

取得线程优先级。

<a id="r_ga24e50a60c524d1eb22fe21cdf269b6a6"></a>

```c
void k_thread_priority_set (k_tid_t thread, int prio)
```

相关声明：[k_thread_priority_set](../thread_core_reference/P001_线程公共接口.md#ga24e50a60c524d1eb22fe21cdf269b6a6)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

设置线程优先级。

<a id="r_gad887f16c1dd6f3247682a83beb22d1ce"></a>

```c
void k_thread_deadline_set (k_tid_t thread, int deadline)
```

相关声明：[k_thread_deadline_set](../thread_core_reference/P001_线程公共接口.md#gad887f16c1dd6f3247682a83beb22d1ce)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

为调度器设置相对截止到期时间（Relative Deadline）。

<a id="r_ga2cb0b359b9324088abbb7003011879f8"></a>

```c
void k_thread_absolute_deadline_set (k_tid_t thread, int deadline)
```

相关声明：[k_thread_absolute_deadline_set](../thread_core_reference/P001_线程公共接口.md#ga2cb0b359b9324088abbb7003011879f8)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

为调度器设置绝对截止到期时间（Absolute Deadline）。

<a id="r_gad82575e576cd08906fbc68fe36be48bd"></a>

```c
void k_reschedule (void)
```

相关声明：[k_reschedule](../thread_core_reference/P001_线程公共接口.md#gad82575e576cd08906fbc68fe36be48bd)。

调用调度器（Scheduler）。

<a id="r_ga80b9c58df6600c7e79f16756c128f44c"></a>

```c
int k_thread_cpu_mask_clear (k_tid_t thread)
```

相关声明：[k_thread_cpu_mask_clear](../thread_core_reference/P001_线程公共接口.md#ga80b9c58df6600c7e79f16756c128f44c)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

将 CPU 使能掩码的所有位清零。

<a id="r_gaedcfeb0964ae72611791241580b2119d"></a>

```c
int k_thread_cpu_mask_enable_all (k_tid_t thread)
```

相关声明：[k_thread_cpu_mask_enable_all](../thread_core_reference/P001_线程公共接口.md#gaedcfeb0964ae72611791241580b2119d)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

将 CPU 使能掩码的所有位置一。

<a id="r_ga306587604a7496db8059bd395fd90fc0"></a>

```c
int k_thread_cpu_mask_enable (k_tid_t thread, int cpu)
```

相关声明：[k_thread_cpu_mask_enable](../thread_core_reference/P001_线程公共接口.md#ga306587604a7496db8059bd395fd90fc0)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

允许线程在指定 CPU 上运行。

<a id="r_ga89e6c07ac112da75b2ef115d1a557d44"></a>

```c
int k_thread_cpu_mask_disable (k_tid_t thread, int cpu)
```

相关声明：[k_thread_cpu_mask_disable](../thread_core_reference/P001_线程公共接口.md#ga89e6c07ac112da75b2ef115d1a557d44)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

禁止线程在指定 CPU 上运行。

<a id="r_gae9ebd9845e14ed02944ab9282a185c03"></a>

```c
int k_thread_cpu_pin (k_tid_t thread, int cpu)
```

相关声明：[k_thread_cpu_pin](../thread_core_reference/P001_线程公共接口.md#gae9ebd9845e14ed02944ab9282a185c03)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

将线程固定到一个 CPU（Pin）。

<a id="r_ga66cf8682fb65870eceb5e57d667a8d4e"></a>

```c
void k_thread_suspend (k_tid_t thread)
```

相关声明：[k_thread_suspend](../thread_core_reference/P001_线程公共接口.md#ga66cf8682fb65870eceb5e57d667a8d4e)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

挂起线程（Suspend）。

<a id="r_ga117b26f8569ec3045ead1fad1851663d"></a>

```c
void k_thread_resume (k_tid_t thread)
```

相关声明：[k_thread_resume](../thread_core_reference/P001_线程公共接口.md#ga117b26f8569ec3045ead1fad1851663d)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

恢复已挂起的线程（Resume）。

<a id="r_gac539268e0b45c600315a6567ec27f965"></a>

```c
static void k_thread_start (k_tid_t thread)
```

相关声明：[k_thread_start](../thread_core_reference/P001_线程公共接口.md#gac539268e0b45c600315a6567ec27f965)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

启动尚未激活的线程。

<a id="r_ga877c1bfeffbf8f097d1656f9e10a66e8"></a>

```c
void k_sched_time_slice_set (int32_t slice, int prio)
```

相关声明：[k_sched_time_slice_set](../thread_core_reference/P001_线程公共接口.md#ga877c1bfeffbf8f097d1656f9e10a66e8)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置时间片（Time Slice）周期及适用范围。

<a id="r_ga563928f292a4134acd4142029b60e631"></a>

```c
void k_thread_time_slice_set (struct k_thread *th, int32_t slice_ticks, k_thread_timeslice_fn_t expired, void *data)
```

相关声明：[k_thread_time_slice_set](../thread_core_reference/P001_线程公共接口.md#ga563928f292a4134acd4142029b60e631)、[k_thread](../thread_core_reference/P004_线程对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[k_thread_timeslice_fn_t](../api_file_reference/P180_zephyr__kernel_structs.h_文件参考.md#a44c6f88a879877ad8da28706e274064f)。

设置线程时间片。

<a id="r_ga8482b0dd2283d12677a9ebe321667d16"></a>

```c
bool k_is_in_isr (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_is_in_isr](../fatal_irq_reference/P007_中断服务接口.md#ga8482b0dd2283d12677a9ebe321667d16)。

判断代码是否在中断级别运行。

<a id="r_ga91e1cf0dc7fc93a3214cadb74ed86666"></a>

```c
int k_is_preempt_thread (void)
```

相关声明：[k_is_preempt_thread](../fatal_irq_reference/P007_中断服务接口.md#ga91e1cf0dc7fc93a3214cadb74ed86666)。

判断代码是否在可抢占线程（Preemptible Thread）中运行。

<a id="r_ga4f0c5d0b9f279b12a4ad97db0c116a5f"></a>

```c
void k_sched_lock (void)
```

相关声明：[k_sched_lock](../thread_core_reference/P001_线程公共接口.md#ga4f0c5d0b9f279b12a4ad97db0c116a5f)。

锁定调度器。

<a id="r_ga7b26f64523cc4c36522cc828ccf85580"></a>

```c
void k_sched_unlock (void)
```

相关声明：[k_sched_unlock](../thread_core_reference/P001_线程公共接口.md#ga7b26f64523cc4c36522cc828ccf85580)。

解锁调度器。

<a id="r_ga4834d9b81ed60c00eee77b0d4f8ab9e4"></a>

```c
void k_thread_custom_data_set (void *value)
```

相关声明：[k_thread_custom_data_set](../thread_core_reference/P001_线程公共接口.md#ga4834d9b81ed60c00eee77b0d4f8ab9e4)。

设置当前线程的自定义数据（Custom Data）。

<a id="r_ga19af063cff7b306ba28062996922740d"></a>

```c
void * k_thread_custom_data_get (void)
```

相关声明：[k_thread_custom_data_get](../thread_core_reference/P001_线程公共接口.md#ga19af063cff7b306ba28062996922740d)。

取得当前线程的自定义数据。

<a id="r_ga23107333f134b9c9a8b692374211e841"></a>

```c
int k_thread_name_set (k_tid_t thread, const char *str)
```

相关声明：[k_thread_name_set](../thread_core_reference/P001_线程公共接口.md#ga23107333f134b9c9a8b692374211e841)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

设置当前线程名称。

<a id="r_gadebf45da56dee393164569742459dc0a"></a>

```c
const char * k_thread_name_get (k_tid_t thread)
```

相关声明：[k_thread_name_get](../thread_core_reference/P001_线程公共接口.md#gadebf45da56dee393164569742459dc0a)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

取得线程名称。

<a id="r_ga07b59ade055c69929ccdc08a14361794"></a>

```c
int k_thread_name_copy (k_tid_t thread, char *buf, size_t size)
```

相关声明：[k_thread_name_copy](../thread_core_reference/P001_线程公共接口.md#ga07b59ade055c69929ccdc08a14361794)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

将线程名称复制到提供的缓冲区。

<a id="r_ga0c6af32096dc7ca391ffe2522bae4cb6"></a>

```c
const char * k_thread_state_str (k_tid_t thread_id, char *buf, size_t buf_size)
```

相关声明：[k_thread_state_str](../thread_core_reference/P001_线程公共接口.md#ga0c6af32096dc7ca391ffe2522bae4cb6)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

取得线程状态字符串（Thread State String）。

<a id="r_ga318c846a740b901e5d56876a47ad7f61"></a>

```c
void k_timer_init (struct k_timer *timer, k_timer_expiry_t expiry_fn, k_timer_stop_t stop_fn)
```

相关声明：[k_timer_init](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga318c846a740b901e5d56876a47ad7f61)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)、[k_timer_expiry_t](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga2915762e70454d98c73c179a45cafbde)、[k_timer_stop_t](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga106733712fc4e62b59bbe6a480bb988c)。

初始化定时器（Timer）。

<a id="r_ga3ba70e9f059ff52fd2057ab89ea7f2ee"></a>

```c
void k_timer_start (struct k_timer *timer, k_timeout_t duration, k_timeout_t period)
```

相关声明：[k_timer_start](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga3ba70e9f059ff52fd2057ab89ea7f2ee)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

启动定时器（Timer）。

<a id="r_ga8d3e3356a10d36570e16f7920e4c8772"></a>

```c
void k_timer_stop (struct k_timer *timer)
```

相关声明：[k_timer_stop](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga8d3e3356a10d36570e16f7920e4c8772)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

停止定时器（Timer）。

<a id="r_gad532f4834cd4cf8be27b089e6ea347ce"></a>

```c
uint32_t k_timer_status_get (struct k_timer *timer)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timer_status_get](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#gad532f4834cd4cf8be27b089e6ea347ce)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

读取定时器状态（Timer Status）。

<a id="r_ga81d6d95b7021e26ad4cab161318e04f2"></a>

```c
uint32_t k_timer_status_sync (struct k_timer *timer)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timer_status_sync](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga81d6d95b7021e26ad4cab161318e04f2)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

使线程与定时器到期事件同步（Synchronize Thread to Timer Expiration）。

<a id="r_ga022b4cf5c8d0ee21b6a3b04fd425533f"></a>

```c
k_ticks_t k_timer_expires_ticks (const struct k_timer *timer)
```

相关声明：[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)、[k_timer_expires_ticks](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga022b4cf5c8d0ee21b6a3b04fd425533f)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

获取定时器下一次到期的时间，以系统节拍（System Tick）为单位。

<a id="r_ga1176b36b960e786f68eaededf99a88b4"></a>

```c
k_ticks_t k_timer_remaining_ticks (const struct k_timer *timer)
```

相关声明：[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)、[k_timer_remaining_ticks](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga1176b36b960e786f68eaededf99a88b4)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

获取距定时器下一次到期的剩余时间，以系统节拍（System Tick）为单位。

<a id="r_ga6c6d8b0aa59bfa0f5924e95ccf756259"></a>

```c
static uint32_t k_timer_remaining_get (struct k_timer *timer)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timer_remaining_get](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga6c6d8b0aa59bfa0f5924e95ccf756259)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

获取距定时器下一次到期的剩余时间（Time Remaining）。

<a id="r_gadba1884961e790dd9c5d567de91cc7e2"></a>

```c
void k_timer_user_data_set (struct k_timer *timer, void *user_data)
```

相关声明：[k_timer_user_data_set](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#gadba1884961e790dd9c5d567de91cc7e2)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

将用户特定数据（User-specific Data）与定时器关联。

<a id="r_ga19a7d99a01a83828efd7f0d3bf2dd358"></a>

```c
void * k_timer_user_data_get (const struct k_timer *timer)
```

相关声明：[k_timer_user_data_get](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga19a7d99a01a83828efd7f0d3bf2dd358)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

获取与定时器关联的用户特定数据（User-specific Data）。

<a id="r_ga39d502ccb6f299bf4efd82565684e508"></a>

```c
int k_timer_cleanup (struct k_timer *timer)
```

相关声明：[k_timer_cleanup](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga39d502ccb6f299bf4efd82565684e508)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

在释放动态分配的定时器（Dynamically Allocated Timer）之前，清理该定时器。

<a id="r_ga8f143af2ee4ad42d9f7817ef161cbd13"></a>

```c
int64_t k_uptime_ticks (void)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[k_uptime_ticks](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga8f143af2ee4ad42d9f7817ef161cbd13)。

获取系统运行时间（Uptime），以系统节拍（System Tick）为单位。

<a id="r_gae3e992cd3257c23d5b26d765fcbb2b69"></a>

```c
static int64_t k_uptime_get (void)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[k_uptime_get](../timer_reference/P086_系统时钟公共接口.md#gae3e992cd3257c23d5b26d765fcbb2b69)。

获取系统运行时间（Uptime）。

<a id="r_ga9253cfb7b46af4d8994349323ce9872b"></a>

```c
static uint32_t k_uptime_get_32 (void)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_uptime_get_32](../timer_reference/P086_系统时钟公共接口.md#ga9253cfb7b46af4d8994349323ce9872b)。

获取系统运行时间（Uptime），32 位版本。

<a id="r_gae082928ea608a8b180b4cb3a79d21a24"></a>

```c
static uint32_t k_uptime_seconds (void)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_uptime_seconds](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gae082928ea608a8b180b4cb3a79d21a24)。

获取系统运行时间（Uptime），以秒为单位。

<a id="r_gad748b2fe83b36884dc087b4af367de80"></a>

```c
static int64_t k_uptime_delta (int64_t *reftime)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[k_uptime_delta](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gad748b2fe83b36884dc087b4af367de80)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

获取经过的时间（Elapsed Time），并更新所引用的时间值。

<a id="r_ga208687de625e0036558343b4e66143d3"></a>

```c
static uint32_t k_cycle_get_32 (void)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_cycle_get_32](../timer_reference/P086_系统时钟公共接口.md#ga208687de625e0036558343b4e66143d3)。

读取硬件时钟（Hardware Clock）。

<a id="r_gae09f509d02bf75a7b45d2800d823bb3a"></a>

```c
static uint64_t k_cycle_get_64 (void)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[k_cycle_get_64](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gae09f509d02bf75a7b45d2800d823bb3a)。

读取 64 位硬件时钟（Hardware Clock）。

<a id="r_ga0236222d42768c2bf00942f328146c21"></a>

```c
void k_queue_init (struct k_queue *queue)
```

相关声明：[k_queue_init](../queue_reference/P001_通用队列公共接口.md#ga0236222d42768c2bf00942f328146c21)、[k_queue](../queue_reference/P002_内核队列结构.md)。

初始化队列。

<a id="r_ga7c39d86cc6509f59ff9223cac3ea5071"></a>

```c
void k_queue_cancel_wait (struct k_queue *queue)
```

相关声明：[k_queue_cancel_wait](../queue_reference/P001_通用队列公共接口.md#ga7c39d86cc6509f59ff9223cac3ea5071)、[k_queue](../queue_reference/P002_内核队列结构.md)。

取消对队列的等待。

<a id="r_gaa84522a5ace6e7f8ba61033baca6972f"></a>

```c
void k_queue_append (struct k_queue *queue, void *data)
```

相关声明：[k_queue_append](../queue_reference/P001_通用队列公共接口.md#gaa84522a5ace6e7f8ba61033baca6972f)、[k_queue](../queue_reference/P002_内核队列结构.md)。

将一个元素追加到队列末尾。

<a id="r_ga690f3a1450e946d75f31b3e499d1d06a"></a>

```c
int32_t k_queue_alloc_append (struct k_queue *queue, void *data)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[k_queue_alloc_append](../queue_reference/P001_通用队列公共接口.md#ga690f3a1450e946d75f31b3e499d1d06a)、[k_queue](../queue_reference/P002_内核队列结构.md)。

向队列追加一个元素。

<a id="r_ga8ce013d8a037d4be5078797e0050e9c6"></a>

```c
void k_queue_prepend (struct k_queue *queue, void *data)
```

相关声明：[k_queue_prepend](../queue_reference/P001_通用队列公共接口.md#ga8ce013d8a037d4be5078797e0050e9c6)、[k_queue](../queue_reference/P002_内核队列结构.md)。

在队列头部加入一个元素。

<a id="r_gacf3dba40125073c11075e5a134919f88"></a>

```c
int32_t k_queue_alloc_prepend (struct k_queue *queue, void *data)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[k_queue_alloc_prepend](../queue_reference/P001_通用队列公共接口.md#gacf3dba40125073c11075e5a134919f88)、[k_queue](../queue_reference/P002_内核队列结构.md)。

在队列头部加入一个元素。

<a id="r_gad47336f27e433a52600a3b67ab89556a"></a>

```c
void k_queue_insert (struct k_queue *queue, void *prev, void *data)
```

相关声明：[k_queue_insert](../queue_reference/P001_通用队列公共接口.md#gad47336f27e433a52600a3b67ab89556a)、[k_queue](../queue_reference/P002_内核队列结构.md)。

向队列插入一个元素。

<a id="r_ga91d1a144fc2aeb3dd655accc94ca43aa"></a>

```c
int k_queue_append_list (struct k_queue *queue, void *head, void *tail)
```

相关声明：[k_queue_append_list](../queue_reference/P001_通用队列公共接口.md#ga91d1a144fc2aeb3dd655accc94ca43aa)、[k_queue](../queue_reference/P002_内核队列结构.md)。

以原子方式将一个元素链表追加到队列。

<a id="r_ga4eee0da7442d60572b05d60a9996e69d"></a>

```c
int k_queue_merge_slist (struct k_queue *queue, sys_slist_t *list)
```

相关声明：[k_queue_merge_slist](../queue_reference/P001_通用队列公共接口.md#ga4eee0da7442d60572b05d60a9996e69d)、[k_queue](../queue_reference/P002_内核队列结构.md)、[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)。

以原子方式将一个元素链表加入队列。

<a id="r_ga0a77d8556e7d253319275de034f01619"></a>

```c
void * k_queue_get (struct k_queue *queue, k_timeout_t timeout)
```

相关声明：[k_queue_get](../queue_reference/P001_通用队列公共接口.md#ga0a77d8556e7d253319275de034f01619)、[k_queue](../queue_reference/P002_内核队列结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从队列取得一个元素。

<a id="r_ga4bff929ed1d366a06e00865a5bbe2544"></a>

```c
bool k_queue_remove (struct k_queue *queue, void *data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_queue_remove](../queue_reference/P001_通用队列公共接口.md#ga4bff929ed1d366a06e00865a5bbe2544)、[k_queue](../queue_reference/P002_内核队列结构.md)。

从队列移除一个元素。

<a id="r_ga287a2d81e2e3041be1cd45164e72f127"></a>

```c
bool k_queue_unique_append (struct k_queue *queue, void *data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_queue_unique_append](../queue_reference/P001_通用队列公共接口.md#ga287a2d81e2e3041be1cd45164e72f127)、[k_queue](../queue_reference/P002_内核队列结构.md)。

仅当元素尚不存在时才将其追加到队列。

<a id="r_gadb2bb8088868b3c5801c72b320389ca9"></a>

```c
int k_queue_is_empty (struct k_queue *queue)
```

相关声明：[k_queue_is_empty](../queue_reference/P001_通用队列公共接口.md#gadb2bb8088868b3c5801c72b320389ca9)、[k_queue](../queue_reference/P002_内核队列结构.md)。

查询队列是否有可用数据。

<a id="r_ga8ccd5137690c127a0f7d67619b88a52b"></a>

```c
void * k_queue_peek_head (struct k_queue *queue)
```

相关声明：[k_queue_peek_head](../queue_reference/P001_通用队列公共接口.md#ga8ccd5137690c127a0f7d67619b88a52b)、[k_queue](../queue_reference/P002_内核队列结构.md)。

查看队列头部元素（Peek）。

<a id="r_ga27a460c42836d8b093ad9274c14bb176"></a>

```c
void * k_queue_peek_tail (struct k_queue *queue)
```

相关声明：[k_queue_peek_tail](../queue_reference/P001_通用队列公共接口.md#ga27a460c42836d8b093ad9274c14bb176)、[k_queue](../queue_reference/P002_内核队列结构.md)。

查看队列尾部元素（Peek）。

<a id="r_ga596bfa265f88567ad9e80fd38cd433d3"></a>

```c
int k_futex_wait (struct k_futex *futex, int expected, k_timeout_t timeout)
```

相关声明：[k_futex_wait](../userspace_sync_reference/P001_Futex公共接口.md#ga596bfa265f88567ad9e80fd38cd433d3)、[k_futex](../userspace_sync_reference/P002_Futex结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

让当前线程在快速用户空间互斥量（Fast Userspace Mutex，Futex）上挂起等待。

<a id="r_ga62de1aeb7c5c273aed20d0e05336d7a0"></a>

```c
int k_futex_wake (struct k_futex *futex, bool wake_all)
```

相关声明：[k_futex_wake](../userspace_sync_reference/P001_Futex公共接口.md#ga62de1aeb7c5c273aed20d0e05336d7a0)、[k_futex](../userspace_sync_reference/P002_Futex结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

唤醒在Futex上等待的一个或全部线程。

<a id="r_gacf803590b39b095056f2b1c5090c4019"></a>

```c
void k_event_init (struct k_event *event)
```

相关声明：[k_event_init](../eventpoll_reference/P001_事件公共接口.md#gacf803590b39b095056f2b1c5090c4019)、[k_event](../eventpoll_reference/P002_内核事件结构.md)。

初始化事件对象。

<a id="r_gac88d17410a71642a903890e420d23d76"></a>

```c
uint32_t k_event_post (struct k_event *event, uint32_t events)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_event_post](../eventpoll_reference/P001_事件公共接口.md#gac88d17410a71642a903890e420d23d76)、[k_event](../eventpoll_reference/P002_内核事件结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向事件对象发布一个或多个事件。

<a id="r_gac22e9d768d003246e68b4b0b64e60f49"></a>

```c
uint32_t k_event_set (struct k_event *event, uint32_t events)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_event_set](../eventpoll_reference/P001_事件公共接口.md#gac22e9d768d003246e68b4b0b64e60f49)、[k_event](../eventpoll_reference/P002_内核事件结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置事件对象中的事件。

<a id="r_ga29b3ec1022b12a8c34884da3559c5864"></a>

```c
uint32_t k_event_set_masked (struct k_event *event, uint32_t events, uint32_t events_mask)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_event_set_masked](../eventpoll_reference/P001_事件公共接口.md#ga29b3ec1022b12a8c34884da3559c5864)、[k_event](../eventpoll_reference/P002_内核事件结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置或清除事件对象中的事件。

<a id="r_gad6bfd7bfd0587bc70d3aa0b988010376"></a>

```c
uint32_t k_event_clear (struct k_event *event, uint32_t events)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_event_clear](../eventpoll_reference/P001_事件公共接口.md#gad6bfd7bfd0587bc70d3aa0b988010376)、[k_event](../eventpoll_reference/P002_内核事件结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

清除事件对象中的事件。

<a id="r_ga0f83f5f034e13bab65149fb90b87a753"></a>

```c
uint32_t k_event_wait (struct k_event *event, uint32_t events, bool reset, k_timeout_t timeout)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_event_wait](../eventpoll_reference/P001_事件公共接口.md#ga0f83f5f034e13bab65149fb90b87a753)、[k_event](../eventpoll_reference/P002_内核事件结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

等待指定事件中的任意一个。

<a id="r_gaddd60a99de5ac3d84f643c9433b744c1"></a>

```c
uint32_t k_event_wait_all (struct k_event *event, uint32_t events, bool reset, k_timeout_t timeout)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_event_wait_all](../eventpoll_reference/P001_事件公共接口.md#gaddd60a99de5ac3d84f643c9433b744c1)、[k_event](../eventpoll_reference/P002_内核事件结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

等待全部指定事件。

<a id="r_gab31c5012e1ae3740c3bde23b245a077e"></a>

```c
uint32_t k_event_wait_safe (struct k_event *event, uint32_t events, bool reset, k_timeout_t timeout)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_event_wait_safe](../eventpoll_reference/P001_事件公共接口.md#gab31c5012e1ae3740c3bde23b245a077e)、[k_event](../eventpoll_reference/P002_内核事件结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

等待指定事件中的任意一个，使用安全版本（Safe Version）。

<a id="r_ga505ddf074c4903fca7e2d355b0caddac"></a>

```c
uint32_t k_event_wait_all_safe (struct k_event *event, uint32_t events, bool reset, k_timeout_t timeout)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_event_wait_all_safe](../eventpoll_reference/P001_事件公共接口.md#ga505ddf074c4903fca7e2d355b0caddac)、[k_event](../eventpoll_reference/P002_内核事件结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

等待全部指定事件，使用安全版本（Safe Version）。

<a id="r_ga81e66be0959e8cb0414d9772056a6264"></a>

```c
static uint32_t k_event_test (struct k_event *event, uint32_t events_mask)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_event_test](../eventpoll_reference/P001_事件公共接口.md#ga81e66be0959e8cb0414d9772056a6264)、[k_event](../eventpoll_reference/P002_内核事件结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

测试事件对象当前记录的事件。

<a id="r_ga4400a39ef48289305cf66a092d5c6c7d"></a>

```c
void k_stack_init (struct k_stack *stack, stack_data_t *buffer, uint32_t num_entries)
```

相关声明：[k_stack_init](../msgstack_reference/P004_栈公共接口.md#ga4400a39ef48289305cf66a092d5c6c7d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化栈。

<a id="r_gab97d924db1aef3f6adade156a107d45c"></a>

```c
int32_t k_stack_alloc_init (struct k_stack *stack, uint32_t num_entries)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[k_stack_alloc_init](../msgstack_reference/P004_栈公共接口.md#gab97d924db1aef3f6adade156a107d45c)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化栈。

<a id="r_ga819f4e7b2cf11cf2e1b80933fdcb67ea"></a>

```c
int k_stack_cleanup (struct k_stack *stack)
```

相关声明：[k_stack_cleanup](../msgstack_reference/P004_栈公共接口.md#ga819f4e7b2cf11cf2e1b80933fdcb67ea)。

释放为栈分配的缓冲区。

<a id="r_gaa6180f4db6ec93ee84149cba054d3e53"></a>

```c
int k_stack_push (struct k_stack *stack, stack_data_t data)
```

相关声明：[k_stack_push](../msgstack_reference/P004_栈公共接口.md#gaa6180f4db6ec93ee84149cba054d3e53)。

将一个元素压入栈。

<a id="r_ga36ce6ceb9ea3d5c36d22b10430789480"></a>

```c
int k_stack_pop (struct k_stack *stack, stack_data_t *data, k_timeout_t timeout)
```

相关声明：[k_stack_pop](../msgstack_reference/P004_栈公共接口.md#ga36ce6ceb9ea3d5c36d22b10430789480)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从栈弹出一个元素。

<a id="r_ga56b64952fb8b78b00268a21c28b41480"></a>

```c
int k_mutex_init (struct k_mutex *mutex)
```

相关声明：[k_mutex_init](../synchronization_reference/P006_互斥量公共接口.md#ga56b64952fb8b78b00268a21c28b41480)、[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)。

初始化互斥量（Mutex）。

<a id="r_ga850549358645249c285669baa49c33b0"></a>

```c
int k_mutex_lock (struct k_mutex *mutex, k_timeout_t timeout)
```

相关声明：[k_mutex_lock](../synchronization_reference/P006_互斥量公共接口.md#ga850549358645249c285669baa49c33b0)、[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

锁定互斥量。

<a id="r_ga360f4c0e7258b0d7030cdb1f452b2c31"></a>

```c
int k_mutex_unlock (struct k_mutex *mutex)
```

相关声明：[k_mutex_unlock](../synchronization_reference/P006_互斥量公共接口.md#ga360f4c0e7258b0d7030cdb1f452b2c31)、[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)。

解锁互斥量。

<a id="r_gac9b497c56cc4642965afa6c0c6d7ecfc"></a>

```c
int k_condvar_init (struct k_condvar *condvar)
```

相关声明：[k_condvar_init](../synchronization_reference/P010_条件变量公共接口.md#gac9b497c56cc4642965afa6c0c6d7ecfc)、[k_condvar](../synchronization_reference/P011_内核条件变量结构.md)。

初始化条件变量。

<a id="r_ga0376a8f7dc6e4f1e1eed55940f43015b"></a>

```c
int k_condvar_signal (struct k_condvar *condvar)
```

相关声明：[k_condvar_signal](../synchronization_reference/P010_条件变量公共接口.md#ga0376a8f7dc6e4f1e1eed55940f43015b)、[k_condvar](../synchronization_reference/P011_内核条件变量结构.md)。

通知一个正在等待该条件变量的线程。

<a id="r_gad2e46a7b9e1bc934fd1f5cb38dde40d8"></a>

```c
int k_condvar_broadcast (struct k_condvar *condvar)
```

相关声明：[k_condvar_broadcast](../synchronization_reference/P010_条件变量公共接口.md#gad2e46a7b9e1bc934fd1f5cb38dde40d8)、[k_condvar](../synchronization_reference/P011_内核条件变量结构.md)。

解除所有正在等待该条件变量的线程的阻塞状态。

<a id="r_gab2e1d05db4f954755f430ca894e44dbc"></a>

```c
int k_condvar_wait (struct k_condvar *condvar, struct k_mutex *mutex, k_timeout_t timeout)
```

相关声明：[k_condvar_wait](../synchronization_reference/P010_条件变量公共接口.md#gab2e1d05db4f954755f430ca894e44dbc)、[k_condvar](../synchronization_reference/P011_内核条件变量结构.md)、[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

等待条件变量，并释放互斥量锁。

<a id="r_gadcd0e6cfba3392fb887222eafe4c1845"></a>

```c
int k_sem_init (struct k_sem *sem, unsigned int initial_count, unsigned int limit)
```

相关声明：[k_sem_init](../synchronization_reference/P008_信号量公共接口.md#gadcd0e6cfba3392fb887222eafe4c1845)、[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

初始化信号量（Semaphore）。

<a id="r_gac71e2383c1920dddc45a561cacfef090"></a>

```c
int k_sem_take (struct k_sem *sem, k_timeout_t timeout)
```

相关声明：[k_sem_take](../synchronization_reference/P008_信号量公共接口.md#gac71e2383c1920dddc45a561cacfef090)、[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

获取信号量（Take）。

<a id="r_gab9be3cf1988af2cd6afdace52d497c84"></a>

```c
void k_sem_give (struct k_sem *sem)
```

相关声明：[k_sem_give](../synchronization_reference/P008_信号量公共接口.md#gab9be3cf1988af2cd6afdace52d497c84)、[k_sem](../synchronization_reference/P009_内核信号量结构.md)。

给出信号量（Give）。

<a id="r_ga1bd12d8d8c1b9c6be9b665d0fefe5562"></a>

```c
void k_sem_reset (struct k_sem *sem)
```

相关声明：[k_sem_reset](../synchronization_reference/P008_信号量公共接口.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)、[k_sem](../synchronization_reference/P009_内核信号量结构.md)。

将信号量计数重置为零。

<a id="r_ga58843b581e170a1811fc38eecbfd01f3"></a>

```c
unsigned int k_sem_count_get (struct k_sem *sem)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[k_sem_count_get](../synchronization_reference/P008_信号量公共接口.md#ga58843b581e170a1811fc38eecbfd01f3)、[k_sem](../synchronization_reference/P009_内核信号量结构.md)。

读取信号量的计数。

<a id="r_acbc5a743865ac106d85326bebe8f575b"></a>

```c
static void k_ipi_work_init (struct k_ipi_work *work)
```

相关声明：[k_ipi_work_init](#acbc5a743865ac106d85326bebe8f575b)、[k_ipi_work](../kernel_runtime_model_reference/P002_k_ipi_work_结构体.md)。

初始化指定的处理器间中断（IPI）工作项（Work Item）。

<a id="r_a43908ad6db382aa92aea565347c14611"></a>

```c
int k_ipi_work_add (struct k_ipi_work *work, uint32_t cpu_bitmask, k_ipi_func_t func)
```

相关声明：[k_ipi_work_add](#a43908ad6db382aa92aea565347c14611)、[k_ipi_work](../kernel_runtime_model_reference/P002_k_ipi_work_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_ipi_func_t](#abc484ff16f6bef4434de98258189e7d5)。

将 IPI 工作项（Work Item）加入 IPI 工作队列（Work Queue）。

<a id="r_aa06c864435b2bd9bc24a971d722dfab0"></a>

```c
int k_ipi_work_wait (struct k_ipi_work *work, k_timeout_t timeout)
```

相关声明：[k_ipi_work_wait](#aa06c864435b2bd9bc24a971d722dfab0)、[k_ipi_work](../kernel_runtime_model_reference/P002_k_ipi_work_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

等待所有目标 CPU 处理完 IPI 工作项（Work Item）。

<a id="r_a9f4947b15a3aa9c2312dff9150da9ddd"></a>

```c
void k_ipi_work_signal (void)
```

相关声明：[k_ipi_work_signal](#a9f4947b15a3aa9c2312dff9150da9ddd)。

发出信号，表明有一个或多个 IPI 工作项（Work Item）需要处理。

<a id="r_gaf20080884a2893d39cd8e862b34a2a30"></a>

```c
void k_work_init (struct k_work *work, k_work_handler_t handler)
```

相关声明：[k_work_init](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaf20080884a2893d39cd8e862b34a2a30)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[k_work_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga5add9ef0dce306a08413c4140fc0bdda)。

初始化不可延迟的工作结构体（Work Structure）。

<a id="r_gaba8a8734768d768b433f9d8490e7df7b"></a>

```c
int k_work_busy_get (const struct k_work *work)
```

相关声明：[k_work_busy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaba8a8734768d768b433f9d8490e7df7b)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

获取工作项（Work Item）的忙状态标志（Busy State Flags）。

<a id="r_ga0d1d2e1d2ba2e89a560a1bdc5365d9e0"></a>

```c
static bool k_work_is_pending (const struct k_work *work)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

检查工作项（Work Item）当前是否处于待处理（Pending）状态。

<a id="r_ga5353e76f73db070614f50d06d292d05c"></a>

```c
int k_work_submit_to_queue (struct k_work_q *queue, struct k_work *work)
```

相关声明：[k_work_submit_to_queue](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga5353e76f73db070614f50d06d292d05c)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

将工作项（Work Item）提交到队列（Queue）。

<a id="r_gace61b59575093d7442f39ccb7be686d7"></a>

```c
int k_work_submit (struct k_work *work)
```

相关声明：[k_work_submit](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gace61b59575093d7442f39ccb7be686d7)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

将工作项（Work Item）提交到系统队列（System Queue）。

<a id="r_gabd1cda459bab538fb2d6dfd84a73b253"></a>

```c
bool k_work_flush (struct k_work *work, struct k_work_sync *sync)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_flush](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gabd1cda459bab538fb2d6dfd84a73b253)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)。

等待最后提交的实例（Last-submitted Instance）完成。

<a id="r_ga389fe2a8fb20f9bd593cf8d990727078"></a>

```c
int k_work_cancel (struct k_work *work)
```

相关声明：[k_work_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga389fe2a8fb20f9bd593cf8d990727078)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

取消工作项（Work Item）。

<a id="r_gab2b05cfe3af08f7d32c3946fa1c808f9"></a>

```c
bool k_work_cancel_sync (struct k_work *work, struct k_work_sync *sync)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_cancel_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gab2b05cfe3af08f7d32c3946fa1c808f9)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)。

取消工作项（Work Item），并等待其完成。

<a id="r_gada77d818ea9e4d07c14a960872ed5492"></a>

```c
void k_work_queue_init (struct k_work_q *queue)
```

相关声明：[k_work_queue_init](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gada77d818ea9e4d07c14a960872ed5492)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)。

初始化工作队列结构体（Work Queue Structure）。

<a id="r_gadfc56554f9bfe7b52309d79660188593"></a>

```c
void k_work_queue_start (struct k_work_q *queue, k_thread_stack_t *stack, size_t stack_size, int prio, const struct k_work_queue_config *cfg)
```

相关声明：[k_work_queue_start](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gadfc56554f9bfe7b52309d79660188593)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_thread_stack_t](../api_file_host_video_reference/P001_zephyr__arch__arch_interface.h_文件参考.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)、[k_work_queue_config](../kernel_runtime_model_reference/P011_k_work_queue_config_结构体.md)。

初始化工作队列（Work Queue）。

<a id="r_gac7fc60238574769e4eae6a2cc38da87b"></a>

```c
void k_work_queue_run (struct k_work_q *queue, const struct k_work_queue_config *cfg)
```

相关声明：[k_work_queue_run](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gac7fc60238574769e4eae6a2cc38da87b)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_work_queue_config](../kernel_runtime_model_reference/P011_k_work_queue_config_结构体.md)。

使用调用线程（Calling Thread）运行工作队列（Work Queue）。

<a id="r_ga0b8b496f7e7bd82d08590a07293e38d7"></a>

```c
static k_tid_t k_work_queue_thread_get (struct k_work_q *queue)
```

相关声明：[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)、[k_work_queue_thread_get](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga0b8b496f7e7bd82d08590a07293e38d7)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)。

访问运行工作队列（Work Queue）的线程（Thread）。

<a id="r_ga0fefe3e0225ac99b47b250849f6cd863"></a>

```c
int k_work_queue_drain (struct k_work_q *queue, bool plug)
```

相关声明：[k_work_queue_drain](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga0fefe3e0225ac99b47b250849f6cd863)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

等待工作队列（Work Queue）排空，并可选择阻止其接受新提交（Plug）。

<a id="r_gaa0463bb79af3ec470f7d3be02052139f"></a>

```c
int k_work_queue_unplug (struct k_work_q *queue)
```

相关声明：[k_work_queue_unplug](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaa0463bb79af3ec470f7d3be02052139f)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)。

解除工作队列（Work Queue）的提交阻塞，使其接受新提交。

<a id="r_ga1fd2fce94eb731ccb0838ec763e62f5c"></a>

```c
int k_work_queue_stop (struct k_work_q *queue, k_timeout_t timeout)
```

相关声明：[k_work_queue_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga1fd2fce94eb731ccb0838ec763e62f5c)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

停止工作队列（Work Queue）。

<a id="r_ga2876c5d82fb2340a093bc4d689a55465"></a>

```c
void k_work_init_delayable (struct k_work_delayable *dwork, k_work_handler_t handler)
```

相关声明：[k_work_init_delayable](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga2876c5d82fb2340a093bc4d689a55465)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_work_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga5add9ef0dce306a08413c4140fc0bdda)。

初始化可延迟工作结构体（Delayable Work Structure）。

<a id="r_gabcb822a03ce7ea9ee1ed046afe31ffca"></a>

```c
static struct k_work_delayable * k_work_delayable_from_work (struct k_work *work)
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_work_delayable_from_work](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gabcb822a03ce7ea9ee1ed046afe31ffca)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

根据工作指针（Work Pointer）获取其所属的可延迟工作结构体（Delayable Work Structure）。

<a id="r_ga1b76969667844f0981d348c9c671bc9f"></a>

```c
int k_work_delayable_busy_get (const struct k_work_delayable *dwork)
```

相关声明：[k_work_delayable_busy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga1b76969667844f0981d348c9c671bc9f)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)。

获取可延迟工作项（Delayable Work Item）的忙状态标志（Busy State Flags）。

<a id="r_ga66e598dbc73f653cbfec03c21168df2e"></a>

```c
static bool k_work_delayable_is_pending (const struct k_work_delayable *dwork)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_delayable_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga66e598dbc73f653cbfec03c21168df2e)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)。

检查延迟工作项（Delayed Work Item）当前是否处于待处理（Pending）状态。

<a id="r_ga1772c37bc62b86180d5cf48fe3037624"></a>

```c
static k_ticks_t k_work_delayable_expires_get (const struct k_work_delayable *dwork)
```

相关声明：[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)、[k_work_delayable_expires_get](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga1772c37bc62b86180d5cf48fe3037624)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)。

获取已调度的可延迟工作（Delayable Work）将被提交时的绝对节拍计数（Absolute Tick Count）。

<a id="r_gabce78598a014f3ed87730fe6a9fe61b4"></a>

```c
static k_ticks_t k_work_delayable_remaining_get (const struct k_work_delayable *dwork)
```

相关声明：[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)、[k_work_delayable_remaining_get](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gabce78598a014f3ed87730fe6a9fe61b4)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)。

获取已调度的可延迟工作（Delayable Work）距离提交还需经过的节拍数（Ticks）。

<a id="r_ga17f863c9f6ff2fb41dc0f3b7de4fdf23"></a>

```c
int k_work_schedule_for_queue (struct k_work_q *queue, struct k_work_delayable *dwork, k_timeout_t delay)
```

相关声明：[k_work_schedule_for_queue](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga17f863c9f6ff2fb41dc0f3b7de4fdf23)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

延迟一段时间后，将空闲工作项（Idle Work Item）提交到队列（Queue）。

<a id="r_ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3"></a>

```c
int k_work_schedule (struct k_work_delayable *dwork, k_timeout_t delay)
```

相关声明：[k_work_schedule](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

延迟一段时间后，将空闲工作项（Idle Work Item）提交到系统工作队列（System Work Queue）。

<a id="r_gabf5db091eac19b19a4e12c0cb381f0a8"></a>

```c
int k_work_reschedule_for_queue (struct k_work_q *queue, struct k_work_delayable *dwork, k_timeout_t delay)
```

相关声明：[k_work_reschedule_for_queue](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gabf5db091eac19b19a4e12c0cb381f0a8)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

重新调度工作项（Work Item），使其延迟一段时间后提交到队列（Queue）。

<a id="r_gaacaab408fb7c848d466ad1f069dfa648"></a>

```c
int k_work_reschedule (struct k_work_delayable *dwork, k_timeout_t delay)
```

相关声明：[k_work_reschedule](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaacaab408fb7c848d466ad1f069dfa648)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

重新调度工作项（Work Item），使其延迟一段时间后提交到系统工作队列（System Work Queue）。

<a id="r_gad47d54e513030304be2600d75b1a965f"></a>

```c
bool k_work_flush_delayable (struct k_work_delayable *dwork, struct k_work_sync *sync)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_flush_delayable](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gad47d54e513030304be2600d75b1a965f)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)。

排空可延迟工作（Flush Delayable Work）。

<a id="r_ga92355914ee178d4c3e848a1946bed3e4"></a>

```c
int k_work_cancel_delayable (struct k_work_delayable *dwork)
```

相关声明：[k_work_cancel_delayable](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga92355914ee178d4c3e848a1946bed3e4)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)。

取消可延迟工作（Cancel Delayable Work）。

<a id="r_ga7e7ec237648556fc16bfda8d35f7cd86"></a>

```c
bool k_work_cancel_delayable_sync (struct k_work_delayable *dwork, struct k_work_sync *sync)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_cancel_delayable_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga7e7ec237648556fc16bfda8d35f7cd86)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)。

取消可延迟工作（Delayable Work），并等待。

<a id="r_ga9de9c7a7f13cc6b325e5453e34afe62d"></a>

```c
static void k_work_user_init (struct k_work_user *work, k_work_user_handler_t handler)
```

相关声明：[k_work_user_init](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga9de9c7a7f13cc6b325e5453e34afe62d)、[k_work_user_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaafa4dfac323cab570da1ee31c07d11bc)。

初始化用户空间工作项（Userspace Work Item）。

<a id="r_ga58d05d4127e4cd51104a1f1a87f626cd"></a>

```c
static bool k_work_user_is_pending (struct k_work_user *work)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_user_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga58d05d4127e4cd51104a1f1a87f626cd)。

检查用户空间工作项（Userspace Work Item）是否处于待处理（Pending）状态。

<a id="r_ga50ae1f6f74c0bc0a41dbbf789fff8856"></a>

```c
static int k_work_user_submit_to_queue (struct k_work_user_q *work_q, struct k_work_user *work)
```

相关声明：[k_work_user_submit_to_queue](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga50ae1f6f74c0bc0a41dbbf789fff8856)。

将工作项（Work Item）提交到用户模式工作队列（User Mode Workqueue）。

<a id="r_ga3091bc8fab5311252e41634a97a18589"></a>

```c
void k_work_user_queue_start (struct k_work_user_q *work_q, k_thread_stack_t *stack, size_t stack_size, int prio, const char *name)
```

相关声明：[k_work_user_queue_start](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga3091bc8fab5311252e41634a97a18589)、[k_thread_stack_t](../api_file_host_video_reference/P001_zephyr__arch__arch_interface.h_文件参考.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)。

在用户模式（User Mode）下启动工作队列（Workqueue）。

<a id="r_gab487068e9564cd77b6bdbac3d5670923"></a>

```c
static k_tid_t k_work_user_queue_thread_get (struct k_work_user_q *work_q)
```

相关声明：[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)、[k_work_user_queue_thread_get](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gab487068e9564cd77b6bdbac3d5670923)。

访问运行工作队列（Work Queue）的用户模式线程（User Mode Thread）。

<a id="r_ga371dab33a40622bea19b07d852863443"></a>

```c
void k_work_poll_init (struct k_work_poll *work, k_work_handler_t handler)
```

相关声明：[k_work_poll_init](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga371dab33a40622bea19b07d852863443)、[k_work_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga5add9ef0dce306a08413c4140fc0bdda)。

初始化触发式工作项（Triggered Work Item）。

<a id="r_ga0abafd7f851e42fd3572c8438e600a53"></a>

```c
int k_work_poll_submit_to_queue (struct k_work_q *work_q, struct k_work_poll *work, struct k_poll_event *events, int num_events, k_timeout_t timeout)
```

相关声明：[k_work_poll_submit_to_queue](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga0abafd7f851e42fd3572c8438e600a53)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_poll_event](../eventpoll_reference/P004_轮询事件结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

提交触发式工作项（Triggered Work Item）。

<a id="r_gad9f222e46d72c4f98739395a0c8bb4ea"></a>

```c
int k_work_poll_submit (struct k_work_poll *work, struct k_poll_event *events, int num_events, k_timeout_t timeout)
```

相关声明：[k_work_poll_submit](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gad9f222e46d72c4f98739395a0c8bb4ea)、[k_poll_event](../eventpoll_reference/P004_轮询事件结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

将触发式工作项（Triggered Work Item）提交到系统工作队列（System Workqueue）。

<a id="r_ga2a19547d04dc1a202e80b752e3177215"></a>

```c
int k_work_poll_cancel (struct k_work_poll *work)
```

相关声明：[k_work_poll_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga2a19547d04dc1a202e80b752e3177215)。

取消触发式工作项（Triggered Work Item）。

<a id="r_ga54a5cdcaea2236c383ace433fedc0d39"></a>

```c
void k_msgq_init (struct k_msgq *msgq, char *buffer, size_t msg_size, uint32_t max_msgs)
```

相关声明：[k_msgq_init](../msgstack_reference/P001_消息队列公共接口.md#ga54a5cdcaea2236c383ace433fedc0d39)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化消息队列。

<a id="r_gabe7305b8f442ebdc147dbbc6e8cf92fc"></a>

```c
int k_msgq_alloc_init (struct k_msgq *msgq, size_t msg_size, uint32_t max_msgs)
```

相关声明：[k_msgq_alloc_init](../msgstack_reference/P001_消息队列公共接口.md#gabe7305b8f442ebdc147dbbc6e8cf92fc)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化消息队列。

<a id="r_gafda4399aa9b8f1e44bdf752e00ea787b"></a>

```c
int k_msgq_cleanup (struct k_msgq *msgq)
```

相关声明：[k_msgq_cleanup](../msgstack_reference/P001_消息队列公共接口.md#gafda4399aa9b8f1e44bdf752e00ea787b)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)。

释放为队列分配的缓冲区。

<a id="r_ga54e96aaaea5462a1f963b7fd5ca82bfe"></a>

```c
int k_msgq_put (struct k_msgq *msgq, const void *data, k_timeout_t timeout)
```

相关声明：[k_msgq_put](../msgstack_reference/P001_消息队列公共接口.md#ga54e96aaaea5462a1f963b7fd5ca82bfe)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

向消息队列末尾发送一条消息。

<a id="r_gac45d9468d2b70bc4e49183ba5a9a3844"></a>

```c
int k_msgq_put_front (struct k_msgq *msgq, const void *data)
```

相关声明：[k_msgq_put_front](../msgstack_reference/P001_消息队列公共接口.md#gac45d9468d2b70bc4e49183ba5a9a3844)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)。

向消息队列头部发送一条消息。

<a id="r_gae67f2ced2df1f9c290ae15dab9097cb7"></a>

```c
int k_msgq_get (struct k_msgq *msgq, void *data, k_timeout_t timeout)
```

相关声明：[k_msgq_get](../msgstack_reference/P001_消息队列公共接口.md#gae67f2ced2df1f9c290ae15dab9097cb7)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从消息队列接收一条消息。

<a id="r_ga14f543472f2f63cfde0bdfa87b95c915"></a>

```c
int k_msgq_peek (struct k_msgq *msgq, void *data)
```

相关声明：[k_msgq_peek](../msgstack_reference/P001_消息队列公共接口.md#ga14f543472f2f63cfde0bdfa87b95c915)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)。

窥视／读取消息队列中的一条消息。

<a id="r_ga69b004a40ab4ca497de314a99960fb8e"></a>

```c
int k_msgq_peek_at (struct k_msgq *msgq, void *data, uint32_t idx)
```

相关声明：[k_msgq_peek_at](../msgstack_reference/P001_消息队列公共接口.md#ga69b004a40ab4ca497de314a99960fb8e)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

窥视／读取消息队列中指定索引处的一条消息。

<a id="r_gaa18875887773195ae44b7fe0972ee760"></a>

```c
void k_msgq_purge (struct k_msgq *msgq)
```

相关声明：[k_msgq_purge](../msgstack_reference/P001_消息队列公共接口.md#gaa18875887773195ae44b7fe0972ee760)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)。

清空消息队列。

<a id="r_ga7d154beb4f9c6227eddbef26d406ca24"></a>

```c
uint32_t k_msgq_num_free_get (struct k_msgq *msgq)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_msgq_num_free_get](../msgstack_reference/P001_消息队列公共接口.md#ga7d154beb4f9c6227eddbef26d406ca24)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)。

获取消息队列的剩余空间数量。

<a id="r_ga8f9d3eef67cbc9c0717a84190bbf7f41"></a>

```c
void k_msgq_get_attrs (struct k_msgq *msgq, struct k_msgq_attrs *attrs)
```

相关声明：[k_msgq_get_attrs](../msgstack_reference/P001_消息队列公共接口.md#ga8f9d3eef67cbc9c0717a84190bbf7f41)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)、[k_msgq_attrs](../msgstack_reference/P003_消息队列属性结构.md)。

获取消息队列的基本属性。

<a id="r_ga458793a89f1d9f762bda3422918a9faa"></a>

```c
uint32_t k_msgq_num_used_get (struct k_msgq *msgq)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_msgq_num_used_get](../msgstack_reference/P001_消息队列公共接口.md#ga458793a89f1d9f762bda3422918a9faa)、[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)。

获取消息队列中的消息数量。

<a id="r_ga686f20c199a9e971822d8279d175d8c2"></a>

```c
void k_mbox_init (struct k_mbox *mbox)
```

相关声明：[k_mbox_init](../mboxpipe_reference/P001_邮箱公共接口.md#ga686f20c199a9e971822d8279d175d8c2)、[k_mbox](../mboxpipe_reference/P002_内核邮箱结构.md)。

初始化邮箱。

<a id="r_gaa1e5cdd992d8b9be11f82254e1886ed2"></a>

```c
int k_mbox_put (struct k_mbox *mbox, struct k_mbox_msg *tx_msg, k_timeout_t timeout)
```

相关声明：[k_mbox_put](../mboxpipe_reference/P001_邮箱公共接口.md#gaa1e5cdd992d8b9be11f82254e1886ed2)、[k_mbox](../mboxpipe_reference/P002_内核邮箱结构.md)、[k_mbox_msg](../mboxpipe_reference/P003_邮箱消息描述符.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

以同步方式发送邮箱消息。

<a id="r_gadd60f7b760371c0a141a1e4da253a0f0"></a>

```c
void k_mbox_async_put (struct k_mbox *mbox, struct k_mbox_msg *tx_msg, struct k_sem *sem)
```

相关声明：[k_mbox_async_put](../mboxpipe_reference/P001_邮箱公共接口.md#gadd60f7b760371c0a141a1e4da253a0f0)、[k_mbox](../mboxpipe_reference/P002_内核邮箱结构.md)、[k_mbox_msg](../mboxpipe_reference/P003_邮箱消息描述符.md)、[k_sem](../synchronization_reference/P009_内核信号量结构.md)。

以异步方式发送邮箱消息。

<a id="r_ga2ea91154620b139dbed1ad949b97c3ef"></a>

```c
int k_mbox_get (struct k_mbox *mbox, struct k_mbox_msg *rx_msg, void *buffer, k_timeout_t timeout)
```

相关声明：[k_mbox_get](../mboxpipe_reference/P001_邮箱公共接口.md#ga2ea91154620b139dbed1ad949b97c3ef)、[k_mbox](../mboxpipe_reference/P002_内核邮箱结构.md)、[k_mbox_msg](../mboxpipe_reference/P003_邮箱消息描述符.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

接收邮箱消息。

<a id="r_ga3d19e648e67f109609259543c9a01d6e"></a>

```c
void k_mbox_data_get (struct k_mbox_msg *rx_msg, void *buffer)
```

相关声明：[k_mbox_data_get](../mboxpipe_reference/P001_邮箱公共接口.md#ga3d19e648e67f109609259543c9a01d6e)、[k_mbox_msg](../mboxpipe_reference/P003_邮箱消息描述符.md)。

将邮箱消息数据取到缓冲区。

<a id="r_gae2c8d97af1f7e9deb93e670859525cf3"></a>

```c
void k_pipe_init (struct k_pipe *pipe, uint8_t *buffer, size_t buffer_size)
```

相关声明：[k_pipe_init](../mboxpipe_reference/P004_管道公共接口.md#gae2c8d97af1f7e9deb93e670859525cf3)、[k_pipe](../mboxpipe_reference/P005_内核管道结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化管道。

<a id="r_ga514ab3d174dcada766ecbda138944ddc"></a>

```c
int k_pipe_write (struct k_pipe *pipe, const uint8_t *data, size_t len, k_timeout_t timeout)
```

相关声明：[k_pipe_write](../mboxpipe_reference/P004_管道公共接口.md#ga514ab3d174dcada766ecbda138944ddc)、[k_pipe](../mboxpipe_reference/P005_内核管道结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

向管道写入数据。

<a id="r_gaecb07412025d9e065ee7b99121522257"></a>

```c
int k_pipe_read (struct k_pipe *pipe, uint8_t *data, size_t len, k_timeout_t timeout)
```

相关声明：[k_pipe_read](../mboxpipe_reference/P004_管道公共接口.md#gaecb07412025d9e065ee7b99121522257)、[k_pipe](../mboxpipe_reference/P005_内核管道结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从管道读取数据。本例程从pipe读取最多len字节的数据。

<a id="r_gaaedff72169127b8227c80bf8adf1f9dd"></a>

```c
void k_pipe_reset (struct k_pipe *pipe)
```

相关声明：[k_pipe_reset](../mboxpipe_reference/P004_管道公共接口.md#gaaedff72169127b8227c80bf8adf1f9dd)、[k_pipe](../mboxpipe_reference/P005_内核管道结构.md)。

重置管道。本例程重置管道，丢弃所有未读数据，并解除等待写入或读取的线程的阻塞，使这些等待线程返回-ECANCELED。

<a id="r_ga83d4b5de8902845850d01b0c3db0702a"></a>

```c
void k_pipe_close (struct k_pipe *pipe)
```

相关声明：[k_pipe_close](../mboxpipe_reference/P004_管道公共接口.md#ga83d4b5de8902845850d01b0c3db0702a)、[k_pipe](../mboxpipe_reference/P005_内核管道结构.md)。

关闭管道。

<a id="r_ga094a8f173f287e29bb287119c26889d1"></a>

```c
int k_mem_slab_init (struct k_mem_slab *slab, void *buffer, size_t block_size, uint32_t num_blocks)
```

相关声明：[k_mem_slab_init](../heap_reference/P003_固定块内存池公共接口.md#ga094a8f173f287e29bb287119c26889d1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化固定块内存池。

<a id="r_gab16a46d8394aca18de740ad044a8734a"></a>

```c
int k_mem_slab_alloc (struct k_mem_slab *slab, void **mem, k_timeout_t timeout)
```

相关声明：[k_mem_slab_alloc](../heap_reference/P003_固定块内存池公共接口.md#gab16a46d8394aca18de740ad044a8734a)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从固定块内存池分配内存。

<a id="r_ga2635ea8f9a30b8751ec966fe62adc0e1"></a>

```c
void k_mem_slab_free (struct k_mem_slab *slab, void *mem)
```

相关声明：[k_mem_slab_free](../heap_reference/P003_固定块内存池公共接口.md#ga2635ea8f9a30b8751ec966fe62adc0e1)。

释放从固定块内存池分配的内存。

<a id="r_gac76b96d7055e4ad94765c93530dd0720"></a>

```c
static uint32_t k_mem_slab_num_used_get (struct k_mem_slab *slab)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_mem_slab_num_used_get](../heap_reference/P003_固定块内存池公共接口.md#gac76b96d7055e4ad94765c93530dd0720)。

取得固定块内存池中已使用的块数量。

<a id="r_gae0e949c1c3476dd57bc0c0ed627d2346"></a>

```c
static uint32_t k_mem_slab_max_used_get (struct k_mem_slab *slab)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_mem_slab_max_used_get](../heap_reference/P003_固定块内存池公共接口.md#gae0e949c1c3476dd57bc0c0ed627d2346)。

取得固定块内存池截至目前的最大已使用块数量。

<a id="r_gae87577e2873cf746db69216a82f94aea"></a>

```c
static uint32_t k_mem_slab_num_free_get (struct k_mem_slab *slab)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_mem_slab_num_free_get](../heap_reference/P003_固定块内存池公共接口.md#gae87577e2873cf746db69216a82f94aea)。

取得固定块内存池中未使用的块数量。

<a id="r_ga32030a5cfb44f663bd31b4e1b3d5dddb"></a>

```c
int k_mem_slab_runtime_stats_get (struct k_mem_slab *slab, struct sys_memory_stats *stats)
```

相关声明：[k_mem_slab_runtime_stats_get](../heap_reference/P003_固定块内存池公共接口.md#ga32030a5cfb44f663bd31b4e1b3d5dddb)、[sys_memory_stats](../lowheap_reference/P005_内存统计结构.md)。

取得固定块内存池的内存统计信息。

<a id="r_gaa1f44e30f4aee98b38e1ab5e93af505c"></a>

```c
int k_mem_slab_runtime_stats_reset_max (struct k_mem_slab *slab)
```

相关声明：[k_mem_slab_runtime_stats_reset_max](../heap_reference/P003_固定块内存池公共接口.md#gaa1f44e30f4aee98b38e1ab5e93af505c)。

将固定块内存池的最大内存使用量复位。

<a id="r_ga9273e06dc8d6a351499f2f5abfdcb39f"></a>

```c
void k_heap_init (struct k_heap *h, void *mem, size_t bytes)
```

相关声明：[k_heap_init](../heap_reference/P001_内核堆公共接口.md#ga9273e06dc8d6a351499f2f5abfdcb39f)、[k_heap](../heap_reference/P002_内核堆结构.md)。

初始化k_heap。

<a id="r_gaf77211a72441de389857bc13e10be4e6"></a>

```c
void * k_heap_aligned_alloc (struct k_heap *h, size_t align, size_t bytes, k_timeout_t timeout)
```

相关声明：[k_heap_aligned_alloc](../heap_reference/P001_内核堆公共接口.md#gaf77211a72441de389857bc13e10be4e6)、[k_heap](../heap_reference/P002_内核堆结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从k_heap分配按指定边界对齐的内存。

<a id="r_ga22b83564e50ae6177388dfe63e32a512"></a>

```c
void * k_heap_alloc (struct k_heap *h, size_t bytes, k_timeout_t timeout)
```

相关声明：[k_heap_alloc](../heap_reference/P001_内核堆公共接口.md#ga22b83564e50ae6177388dfe63e32a512)、[k_heap](../heap_reference/P002_内核堆结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从k_heap分配内存。

<a id="r_ga53de68a83567cff1cff3eab5d8572449"></a>

```c
void * k_heap_calloc (struct k_heap *h, size_t num, size_t size, k_timeout_t timeout)
```

相关声明：[k_heap_calloc](../heap_reference/P001_内核堆公共接口.md#ga53de68a83567cff1cff3eab5d8572449)、[k_heap](../heap_reference/P002_内核堆结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从k_heap为对象数组分配并初始化内存。

<a id="r_gabea4b2beae8ab138f2796fbeaa95d262"></a>

```c
void * k_heap_realloc (struct k_heap *h, void *ptr, size_t bytes, k_timeout_t timeout)
```

相关声明：[k_heap_realloc](../heap_reference/P001_内核堆公共接口.md#gabea4b2beae8ab138f2796fbeaa95d262)、[k_heap](../heap_reference/P002_内核堆结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从k_heap重新分配内存。

<a id="r_ga6cf917a0b3d91a0101192bd4808ada9c"></a>

```c
void k_heap_free (struct k_heap *h, void *mem)
```

相关声明：[k_heap_free](../heap_reference/P001_内核堆公共接口.md#ga6cf917a0b3d91a0101192bd4808ada9c)、[k_heap](../heap_reference/P002_内核堆结构.md)。

释放由k_heap_alloc()分配的内存。

<a id="r_ga3aa215396381e1513edf50bd9563dee5"></a>

```c
int k_heap_array_get (struct k_heap **heap)
```

相关声明：[k_heap_array_get](../heap_reference/P001_内核堆公共接口.md#ga3aa215396381e1513edf50bd9563dee5)、[k_heap](../heap_reference/P002_内核堆结构.md)。

取得静态定义的堆数组。

<a id="r_gae16d486aa250f9c07fa6a57342bcd3b4"></a>

```c
void * k_aligned_alloc (size_t align, size_t size)
```

相关声明：[k_aligned_alloc](../heap_reference/P001_内核堆公共接口.md#gae16d486aa250f9c07fa6a57342bcd3b4)。

从堆分配具有指定对齐要求的内存。

<a id="r_gaa8edf1e63e5d5dd78d7adcfd787394ee"></a>

```c
void * k_malloc (size_t size)
```

相关声明：[k_malloc](../heap_reference/P001_内核堆公共接口.md#gaa8edf1e63e5d5dd78d7adcfd787394ee)。

从堆分配内存。

<a id="r_ga79b63cc93b3358cf82d74f40e73b69d5"></a>

```c
void k_free (void *ptr)
```

相关声明：[k_free](../heap_reference/P001_内核堆公共接口.md#ga79b63cc93b3358cf82d74f40e73b69d5)。

释放从堆分配的内存。

<a id="r_gad031d50ed62d08202a5dcf992c20246c"></a>

```c
void * k_calloc (size_t nmemb, size_t size)
```

相关声明：[k_calloc](../heap_reference/P001_内核堆公共接口.md#gad031d50ed62d08202a5dcf992c20246c)。

按数组方式从堆分配内存。

<a id="r_ga852a7a60dce5853b6925897b24a54e02"></a>

```c
void * k_realloc (void *ptr, size_t size)
```

相关声明：[k_realloc](../heap_reference/P001_内核堆公共接口.md#ga852a7a60dce5853b6925897b24a54e02)。

调整已有分配的大小（Reallocation）。

<a id="r_gaa06bddd93a024fc5326d93187d80eb03"></a>

```c
void k_poll_event_init (struct k_poll_event *event, uint32_t type, int mode, void *obj)
```

相关声明：[k_poll_event_init](../eventpoll_reference/P003_轮询公共接口.md#gaa06bddd93a024fc5326d93187d80eb03)、[k_poll_event](../eventpoll_reference/P004_轮询事件结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化一个struct k_poll_event实例。

<a id="r_gac550dc93662ce164fb22a5a91d6830db"></a>

```c
int k_poll (struct k_poll_event *events, int num_events, k_timeout_t timeout)
```

相关声明：[k_poll](../eventpoll_reference/P003_轮询公共接口.md#gac550dc93662ce164fb22a5a91d6830db)、[k_poll_event](../eventpoll_reference/P004_轮询事件结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

等待多个轮询事件中的一个或多个发生。

<a id="r_gaee3090c2a912b93b6a5855e3018c3551"></a>

```c
void k_poll_signal_init (struct k_poll_signal *sig)
```

相关声明：[k_poll_signal_init](../eventpoll_reference/P003_轮询公共接口.md#gaee3090c2a912b93b6a5855e3018c3551)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

初始化轮询信号对象。

<a id="r_ga02d899d1455ae1f3f55ffe8f1ebd6994"></a>

```c
void k_poll_signal_reset (struct k_poll_signal *sig)
```

相关声明：[k_poll_signal_reset](../eventpoll_reference/P003_轮询公共接口.md#ga02d899d1455ae1f3f55ffe8f1ebd6994)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

将轮询信号对象复位为未触发状态。

<a id="r_ga69dae11c7cb2c669caa411c3e7001311"></a>

```c
void k_poll_signal_check (struct k_poll_signal *sig, unsigned int *signaled, int *result)
```

相关声明：[k_poll_signal_check](../eventpoll_reference/P003_轮询公共接口.md#ga69dae11c7cb2c669caa411c3e7001311)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

读取轮询信号的触发状态及结果值。

<a id="r_gad0bf3825f828ec3ca37481bf3cbd6723"></a>

```c
int k_poll_signal_raise (struct k_poll_signal *sig, int result)
```

相关声明：[k_poll_signal_raise](../eventpoll_reference/P003_轮询公共接口.md#gad0bf3825f828ec3ca37481bf3cbd6723)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

触发轮询信号对象。

<a id="r_ga7b25e1bed511a813b32fbd0f91b09356"></a>

```c
static void k_cpu_idle (void)
```

相关声明：[k_cpu_idle](../fatal_irq_reference/P011_CPU空闲接口.md#ga7b25e1bed511a813b32fbd0f91b09356)。

使 CPU 进入空闲状态（CPU Idle）。

<a id="r_gadf88ece6447b65b7d0d2f3a70ab4fe8f"></a>

```c
static void k_cpu_atomic_idle (unsigned int key)
```

相关声明：[k_cpu_atomic_idle](../fatal_irq_reference/P011_CPU空闲接口.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

以原子方式使 CPU 进入空闲状态（Atomic Idle）。

<a id="r_ga2df4b2550ace30512cddebd36b6a54a1"></a>

```c
int k_float_disable (struct k_thread *thread)
```

相关声明：[k_float_disable](../fatal_irq_reference/P012_浮点上下文接口.md#ga2df4b2550ace30512cddebd36b6a54a1)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

禁用浮点上下文信息的保存（Floating-point Context Preservation）。

<a id="r_ga81fb955ddd41658a9aad5c083f173f77"></a>

```c
int k_float_enable (struct k_thread *thread, unsigned int options)
```

相关声明：[k_float_enable](../fatal_irq_reference/P012_浮点上下文接口.md#ga81fb955ddd41658a9aad5c083f173f77)、[k_thread](../thread_core_reference/P004_线程对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

启用浮点上下文信息的保存。

<a id="r_a82d886a1c911b39c1b47c32200cedac6"></a>

```c
int k_thread_runtime_stats_get (k_tid_t thread, k_thread_runtime_stats_t *stats)
```

相关声明：[k_thread_runtime_stats_get](#a82d886a1c911b39c1b47c32200cedac6)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)、[k_thread_runtime_stats_t](../thread_core_reference/P002_线程头文件参考.md#a887f70695cd229ea8f30ea3e1faf45cf)。

获取线程的运行时统计信息（Runtime Statistics）。

<a id="r_abd855bb83b3be393b46833e7854a193e"></a>

```c
int k_thread_runtime_stats_all_get (k_thread_runtime_stats_t *stats)
```

相关声明：[k_thread_runtime_stats_all_get](#abd855bb83b3be393b46833e7854a193e)、[k_thread_runtime_stats_t](../thread_core_reference/P002_线程头文件参考.md#a887f70695cd229ea8f30ea3e1faf45cf)。

获取所有线程的运行时统计信息（Runtime Statistics）。

<a id="r_aefdd9027a50143262a7482c17873f169"></a>

```c
int k_thread_runtime_stats_cpu_get (int cpu, k_thread_runtime_stats_t *stats)
```

相关声明：[k_thread_runtime_stats_cpu_get](#aefdd9027a50143262a7482c17873f169)、[k_thread_runtime_stats_t](../thread_core_reference/P002_线程头文件参考.md#a887f70695cd229ea8f30ea3e1faf45cf)。

获取指定 CPU 上所有线程的运行时统计信息（Runtime Statistics）。

<a id="r_a3e52beb93fca2231d5860fe1cf1181fd"></a>

```c
int k_thread_runtime_stats_enable (k_tid_t thread)
```

相关声明：[k_thread_runtime_stats_enable](#a3e52beb93fca2231d5860fe1cf1181fd)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

启用指定线程的运行时统计信息（Runtime Statistics）采集。

<a id="r_ae5ea2e05a602b7d5ee78a65ced61d63b"></a>

```c
int k_thread_runtime_stats_disable (k_tid_t thread)
```

相关声明：[k_thread_runtime_stats_disable](#ae5ea2e05a602b7d5ee78a65ced61d63b)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

禁用指定线程的运行时统计信息（Runtime Statistics）采集。

<a id="r_a8954eb04bd70207b9aeff112782a1e40"></a>

```c
bool k_thread_runtime_stats_is_enabled (k_tid_t thread)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_thread_runtime_stats_is_enabled](#a8954eb04bd70207b9aeff112782a1e40)、[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

检查线程是否已启用运行时统计信息（Runtime Statistics）采集。

<a id="r_a54f2652ba1ed613219941eaaf193180c"></a>

```c
void k_sys_runtime_stats_enable (void)
```

相关声明：[k_sys_runtime_stats_enable](#a54f2652ba1ed613219941eaaf193180c)。

启用系统运行时统计信息（System Runtime Statistics）采集。

<a id="r_a2e3c96c0b11108ee7eca3f0666c780e0"></a>

```c
void k_sys_runtime_stats_disable (void)
```

相关声明：[k_sys_runtime_stats_disable](#a2e3c96c0b11108ee7eca3f0666c780e0)。

禁用系统运行时统计信息（System Runtime Statistics）采集。

## 6.6\_详细说明（Detailed Documentation）

<a id="abde5aa8ca5e64a045b25b88f91370dcd"></a>

### `k_oops`

```c
#define k_oops ( )
```

展开值（Value）：

```c
z_except_reason(K_ERR_KERNEL_OOPS)
```

因致命错误终止线程（Thread）。

当线程遇到无法恢复的运行时状况（Unrecoverable Runtime Condition）并需要终止时，应调用此函数。其最终行为由 `_fatal_error_handler()` 的实现决定；调用该处理函数时将传入原因码 `K_ERR_KERNEL_OOPS`。

如果从中断服务程序上下文（ISR Context）调用，默认系统致命错误处理程序（Fatal Error Handler）会将其视为不可恢复的系统错误，与 `k_panic()` 一样。

<a id="aedd541f707b1463aaac15c7798340329"></a>

### `k_panic`

```c
#define k_panic ( )
```

展开值（Value）：

```c
z_except_reason(K_ERR_KERNEL_PANIC)
```

因致命错误终止系统（System）。

当 Zephyr 内核遇到无法恢复的运行时状况（Unrecoverable Runtime Condition）并需要终止时，应调用此函数。其最终行为由 `_fatal_error_handler()` 的实现决定；调用该处理函数时将传入原因码 `K_ERR_KERNEL_PANIC`。

<a id="abc484ff16f6bef4434de98258189e7d5"></a>

### `k_ipi_func_t`

```c
typedef void(* k_ipi_func_t) (struct k_ipi_work *work)
```

处理器间中断（IPI）工作项处理函数（Handler）的函数类型。

在 `k_ipi_work_add()` 指定的每个目标 CPU 上，以中断服务程序级别（ISR Level）调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 正在处理的处理器间中断（IPI）工作项（Work Item）。 |

<a id="a43908ad6db382aa92aea565347c14611"></a>

### `k_ipi_work_add()`

```c
int k_ipi_work_add ( struct k_ipi_work * work, uint32_t cpu_bitmask, k_ipi_func_t func )
```

将 IPI 工作项（Work Item）加入 IPI 工作队列（Work Queue）。

将指定的 IPI 工作项（Work Item）加入 `cpu_bitmask` 标识的各 CPU 的 IPI 工作队列（Work Queue）。此后，当这些 CPU 处理收到的处理器间中断（IPI）时，该工作项将在中断服务程序级别（ISR Level）执行。在所有指定 CPU 都处理完此工作项之前，不得复用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 指向 IPI 工作项（Work Item）的指针。 |
| `cpu_bitmask` | IPI 工作项（Work Item）将发送到的 CPU 集合。 |
| `func` | 要在目标 CPU 上执行的函数（Function）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EBUSY` | 指定的 IPI 工作项（Work Item）仍在处理时。 |

**注意（Attention）**：注意（Attention）：仅当启用以下 Kconfig 选项时可用：`CONFIG_SCHED_IPI_SUPPORTED`。

<a id="acbc5a743865ac106d85326bebe8f575b"></a>

### `k_ipi_work_init()`

```c
void k_ipi_work_init ( struct k_ipi_work * work)
```

声明属性：`inline`、`static`。

初始化指定的处理器间中断（IPI）工作项（Work Item）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 指向待初始化的 IPI 工作项（Work Item）的指针。 |

**注意（Attention）**：注意（Attention）：仅当启用以下 Kconfig 选项时可用：`CONFIG_SCHED_IPI_SUPPORTED`。

<a id="a9f4947b15a3aa9c2312dff9150da9ddd"></a>

### `k_ipi_work_signal()`

```c
void k_ipi_work_signal ( void )
```

发出信号，表明有一个或多个 IPI 工作项（Work Item）需要处理。

此例程向一组 CPU 发送处理器间中断（IPI）；该 CPU 集合由本 CPU 上次发送一组 IPI 之后的 `k_ipi_work_add()` 调用确定。

**注意（Attention）**：注意（Attention）：仅当启用以下 Kconfig 选项时可用：`CONFIG_SCHED_IPI_SUPPORTED`。

<a id="aa06c864435b2bd9bc24a971d722dfab0"></a>

### `k_ipi_work_wait()`

```c
int k_ipi_work_wait ( struct k_ipi_work * work, k_timeout_t timeout )
```

等待所有目标 CPU 处理完 IPI 工作项（Work Item）。

此例程等待所有接收方 CPU 处理完 IPI 工作项（Work Item）。如果从中断服务程序（ISR）调用，`timeout` 必须设为 `K_NO_WAIT`。为避免死锁（Deadlock），调用者调用此函数时不得锁定中断请求（IRQ）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 指向 IPI 工作项（Work Item）的指针。 |
| `timeout` | 等待 IPI 工作（Work）处理完毕的最长时间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EAGAIN` | 等待时间已到，发生超时。 |
| `0` | 所有目标 CPU 都已处理完毕时。 |

**说明（Note）**：注意（Note）：在中断服务程序（ISR）上下文或已加锁、导致调用 CPU 无法响应处理器间中断（IPI）的上下文中，通常无法安全地轮询此函数的完成状态，因为目标 CPU 也可能正在等待调用 CPU。应用程序代码必须能够处理失败，或者从线程上下文（Thread Context）进行轮询。

**注意（Attention）**：注意（Attention）：仅当启用以下 Kconfig 选项时可用：`CONFIG_SCHED_IPI_SUPPORTED`。

<a id="a2e3c96c0b11108ee7eca3f0666c780e0"></a>

### `k_sys_runtime_stats_disable()`

```c
void k_sys_runtime_stats_disable ( void )
```

禁用系统运行时统计信息（System Runtime Statistics）采集。

此例程禁用系统运行时统计信息（System Runtime Statistics）的采集。注意，它不会影响单个线程的同类统计信息采集。

<a id="a54f2652ba1ed613219941eaaf193180c"></a>

### `k_sys_runtime_stats_enable()`

```c
void k_sys_runtime_stats_enable ( void )
```

启用系统运行时统计信息（System Runtime Statistics）采集。

此例程启用系统运行时统计信息（System Runtime Statistics）的采集。注意，它不会影响单个线程的同类统计信息采集。

<a id="abd855bb83b3be393b46833e7854a193e"></a>

### `k_thread_runtime_stats_all_get()`

```c
int k_thread_runtime_stats_all_get ( k_thread_runtime_stats_t * stats)
```

获取所有线程的运行时统计信息（Runtime Statistics）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stats` | 指向用于接收统计数据的结构的指针。 |

**返回（Returns）**：传入空指针时返回 -EINVAL，否则返回 0。

<a id="aefdd9027a50143262a7482c17873f169"></a>

### `k_thread_runtime_stats_cpu_get()`

```c
int k_thread_runtime_stats_cpu_get ( int cpu, k_thread_runtime_stats_t * stats )
```

获取指定 CPU 上所有线程的运行时统计信息（Runtime Statistics）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cpu` | CPU 编号（CPU Number）。 |
| `stats` | 指向用于接收统计数据的结构的指针。 |

**返回（Returns）**：返回值（Returns）：指针为空或 CPU 无效时返回 `-EINVAL`，否则返回 `0`。

<a id="ae5ea2e05a602b7d5ee78a65ced61d63b"></a>

### `k_thread_runtime_stats_disable()`

```c
int k_thread_runtime_stats_disable ( k_tid_t thread)
```

禁用指定线程的运行时统计信息（Runtime Statistics）采集。

此例程禁用指定线程的运行时统计信息（Runtime Statistics）采集。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `thread` | 线程 ID。 |

**返回（Returns）**：返回值（Returns）：线程标识符（Thread ID）无效时返回 `-EINVAL`，否则返回 `0`。

<a id="a3e52beb93fca2231d5860fe1cf1181fd"></a>

### `k_thread_runtime_stats_enable()`

```c
int k_thread_runtime_stats_enable ( k_tid_t thread)
```

启用指定线程的运行时统计信息（Runtime Statistics）采集。

此例程启用指定线程的运行时统计信息（Runtime Statistics）采集。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `thread` | 线程 ID。 |

**返回（Returns）**：返回值（Returns）：线程标识符（Thread ID）无效时返回 `-EINVAL`，否则返回 `0`。

<a id="a82d886a1c911b39c1b47c32200cedac6"></a>

### `k_thread_runtime_stats_get()`

```c
int k_thread_runtime_stats_get ( k_tid_t thread, k_thread_runtime_stats_t * stats )
```

获取线程的运行时统计信息（Runtime Statistics）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `thread` | 线程 ID。 |
| `stats` | 指向用于接收统计数据的结构的指针。 |

**返回（Returns）**：传入空指针时返回 -EINVAL，否则返回 0。

<a id="a8954eb04bd70207b9aeff112782a1e40"></a>

### `k_thread_runtime_stats_is_enabled()`

```c
bool k_thread_runtime_stats_is_enabled ( k_tid_t thread)
```

检查线程是否已启用运行时统计信息（Runtime Statistics）采集。

此例程检查指定线程是否已启用运行时统计信息（Runtime Statistics）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `thread` | 线程 ID。 |

**返回（Returns）**：返回值（Returns）：指定线程已启用使用情况统计（Usage Statistics）时返回 `true`，否则返回 `false`。


## 6.7\_原页交叉引用（Cross References）

- [zephyr/kernel_includes.h](../api_source_reference/P428_kernel_includes.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [limits.h](../api_source_runtime_reference/P039_limits.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [zephyr/tracing/tracing_macros.h](../tracing_headers_reference/P003_跟踪包装宏头文件源码.md)
- [zephyr/sleep.h](../api_source_timing_sensor_reference/P011_sleep.h_源码浏览.md)
- [zephyr/sys/mem_stats.h](../lowheap_reference/P020_内存统计头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P004_环形缓冲区头文件源码.md)
- [zephyr/tracing/tracing.h](../tracing_headers_reference/P001_跟踪公共头文件源码.md)
- [查看此文件的源码。](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)
- [k_queue](../queue_reference/P002_内核队列结构.md)
- [k_futex](../userspace_sync_reference/P002_Futex结构.md)
- [k_event](../eventpoll_reference/P002_内核事件结构.md)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [k_lifo](../queue_reference/P006_内核LIFO结构.md)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [k_condvar](../synchronization_reference/P011_内核条件变量结构.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [k_ipi_work](../kernel_runtime_model_reference/P002_k_ipi_work_结构体.md)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)
- [k_work_queue_config](../kernel_runtime_model_reference/P011_k_work_queue_config_结构体.md)
- [k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)
- [k_msgq_attrs](../msgstack_reference/P003_消息队列属性结构.md)
- [k_mbox_msg](../mboxpipe_reference/P003_邮箱消息描述符.md)
- [k_mbox](../mboxpipe_reference/P002_内核邮箱结构.md)
- [k_pipe](../mboxpipe_reference/P005_内核管道结构.md)
- [k_heap](../heap_reference/P002_内核堆结构.md)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [k_poll_event](../eventpoll_reference/P004_轮询事件结构.md)
- [K_ANY](../api_device_topic_reference/P013_内核 API（Kernel APIs）.md#gac627cc4c3da16be4b74f0a4ab036a603)
- [K_PRIO_COOP](../thread_core_reference/P001_线程公共接口.md#gac145d4747518572acfc8ee1579007d54)
- [K_PRIO_PREEMPT](../thread_core_reference/P001_线程公共接口.md#gaa0e916aae3ddd0e998cd41ac32afe30a)
- [K_HIGHEST_THREAD_PRIO](../thread_core_reference/P001_线程公共接口.md#ga5fd4365cb6e8742e750b5e4950fb1e47)
- [K_LOWEST_THREAD_PRIO](../thread_core_reference/P001_线程公共接口.md#gafa4bcc2fdfea5cd7c63d56f476b1b32f)
- [K_IDLE_PRIO](../thread_core_reference/P001_线程公共接口.md#ga8f3f1d910dd847f0b223a4aa00788fa2)
- [K_HIGHEST_APPLICATION_THREAD_PRIO](../thread_core_reference/P001_线程公共接口.md#gab326c7eb1d248650e6017dcaee8d24b2)
- [K_LOWEST_APPLICATION_THREAD_PRIO](../thread_core_reference/P001_线程公共接口.md#gad4c2df561988fa1194c2f8c768d667cd)
- [K_ESSENTIAL](../thread_core_reference/P001_线程公共接口.md#gad503fbcca905a9266b0e154e3ded258c)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [K_FP_REGS](../thread_core_reference/P001_线程公共接口.md#gab18cf1e8728e7adf53db2ae4bbcdd951)
- [K_USER](../thread_core_reference/P001_线程公共接口.md#gacb5340339892f22301e02697c6039ccc)
- [K_INHERIT_PERMS](../thread_core_reference/P001_线程公共接口.md#gaa1788a413a055745d1de71b4da7c2eb2)
- [K_CALLBACK_STATE](../thread_core_reference/P001_线程公共接口.md#gacbdb579370978fe07e4a863a84bd8bee)
- [K_DSP_REGS](../thread_core_reference/P001_线程公共接口.md#ga8e1aeb428a418ed23e17448b796363cb)
- [K_AGU_REGS](../thread_core_reference/P001_线程公共接口.md#ga718088c1a68f03fffa960164cab60b72)
- [K_SSE_REGS](../thread_core_reference/P001_线程公共接口.md#gaa5b7de51b26773aa4485a711a041d9a7)
- [k_thread_access_grant](../thread_core_reference/P001_线程公共接口.md#gafec540511e6d2e0a074a5bfb515c53b0)
- [K_THREAD_DEFINE](../thread_core_reference/P001_线程公共接口.md#gab3ced58648ca35788a40676e8478ecd2)
- [K_KERNEL_THREAD_DEFINE](../thread_core_reference/P001_线程公共接口.md#gae25853424ec969f8431862c46b3ec294)
- [K_NO_WAIT](../timer_reference/P086_系统时钟公共接口.md#ga3d9541cfe2e8395af66d186efa77362f)
- [K_NSEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gae2f3a80170afc5fbce0337cdf5a4ce4c)
- [K_USEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga91198e325210ec052a8308e642058c0b)
- [K_CYC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gab41f59fd2b724cb1279e4f6821154b33)
- [K_TICKS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaeda983960bd25f1dba7a386ad720e395)
- [K_MSEC](../timer_reference/P086_系统时钟公共接口.md#ga302af954e87b10a9b731f1ad07775e9f)
- [K_SECONDS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gadc361472aea59267f6ea38f5e7c7ca2a)
- [K_MINUTES](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaef02f20d4d2ebfc9aa29acae01bd3698)
- [K_HOURS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaa9e0cd890db28965b66d4bc5d719a91f)
- [K_FOREVER](../timer_reference/P086_系统时钟公共接口.md#ga0bb4b83f0222193b21a8910311bab0ca)
- [K_TIMEOUT_SUM](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga23f8926e4a14fba3694b92ce763d47fb)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [K_TIMER_DEFINE](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#gaa267fcb0a2e18cd0da29e9f9612510a6)
- [K_QUEUE_DEFINE](../queue_reference/P001_通用队列公共接口.md#gacd0bc309f0147d4669f65fafa87e0e70)
- [K_EVENT_DEFINE](../eventpoll_reference/P001_事件公共接口.md#ga093449cc6686d3235944f3faad284893)
- [k_fifo_init](../queue_reference/P003_FIFO公共接口.md#gaeebf6ef54d4be61e19408f44a734a159)
- [k_fifo_cancel_wait](../queue_reference/P003_FIFO公共接口.md#gab744080af449e093df8dd4982e013e16)
- [k_fifo_put](../queue_reference/P003_FIFO公共接口.md#ga3addb10f86f19e245c23362433d5c913)
- [k_fifo_alloc_put](../queue_reference/P003_FIFO公共接口.md#gab1c5212040d12cbb92cede5cf54928ba)
- [k_fifo_put_list](../queue_reference/P003_FIFO公共接口.md#ga1bf5f52290c83e54ba14358cbbb4051b)
- [k_fifo_put_slist](../queue_reference/P003_FIFO公共接口.md#ga4cdc286a7a6f0d43acab63a4846815e7)
- [k_fifo_get](../queue_reference/P003_FIFO公共接口.md#ga1e2c480e2124116af97e94e7b4435de6)
- [k_fifo_is_empty](../queue_reference/P003_FIFO公共接口.md#gab7cec4adc128ed1fd2d194ba6cd8c640)
- [k_fifo_peek_head](../queue_reference/P003_FIFO公共接口.md#ga2e0c8608f095a929740fa94c94a4f389)
- [k_fifo_peek_tail](../queue_reference/P003_FIFO公共接口.md#gafbe2ce9a6437b886cf149016187ba92f)
- [K_FIFO_DEFINE](../queue_reference/P003_FIFO公共接口.md#ga230b02a526ecb0ae1598be75cb9a8274)
- [k_lifo_init](../queue_reference/P005_LIFO公共接口.md#ga69fb19716a9014f7de79f8e524d64a3e)
- [k_lifo_put](../queue_reference/P005_LIFO公共接口.md#gad662e36b1df8b9013e2dc61f9dfe3a8b)
- [k_lifo_alloc_put](../queue_reference/P005_LIFO公共接口.md#ga96d885a6a36fcfcb5eaa65898eee0965)
- [k_lifo_get](../queue_reference/P005_LIFO公共接口.md#gad5f1775947b07a2a77f667aa9e41db5a)
- [K_LIFO_DEFINE](../queue_reference/P005_LIFO公共接口.md#gaebd450d4181f22491623ea0aed6ee576)
- [K_STACK_DEFINE](../msgstack_reference/P004_栈公共接口.md#ga8c9ca77e5de3c9757dcd4ecb55797835)
- [K_MUTEX_DEFINE](../synchronization_reference/P006_互斥量公共接口.md#gab6f3d98fabbdc0918bbc9934d61d63f3)
- [K_CONDVAR_DEFINE](../synchronization_reference/P010_条件变量公共接口.md#ga770816651e25f7e7dae992a0b2260c21)
- [K_SEM_MAX_LIMIT](../synchronization_reference/P008_信号量公共接口.md#ga689359a77a0cebe737ef644c188f7e57)
- [K_SEM_DEFINE](../synchronization_reference/P008_信号量公共接口.md#ga018a8aa43e02e704deee7b6341502946)
- [K_WORK_DELAYABLE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga893b281f3d2bc0088650536899e17903)
- [K_WORK_USER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga4f3eac1fc56d5c9c21a3afa9b964b0bf)
- [K_WORK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaf8e003eefa5dd66ba883688f9d39c333)
- [K_MSGQ_DEFINE](../msgstack_reference/P001_消息队列公共接口.md#ga95ef93002766901511d09c8cd8f8293b)
- [K_MSGQ_DEFINE_STATIC](../msgstack_reference/P001_消息队列公共接口.md#ga15e39d40c8659be688d41e2201959c4c)
- [K_MSGQ_DEFINE_TYPE](../msgstack_reference/P001_消息队列公共接口.md#gab17e888412dd4d299dc68816a24de78a)
- [K_MSGQ_DEFINE_STATIC_TYPE](../msgstack_reference/P001_消息队列公共接口.md#ga0f01b9e30429458e184f202c3701c54a)
- [K_MBOX_DEFINE](../mboxpipe_reference/P001_邮箱公共接口.md#gab55cba898db47113a06641c01f3e3714)
- [K_PIPE_DEFINE](../mboxpipe_reference/P004_管道公共接口.md#gac2256aa00c59e78199be9bdefd61aa52)
- [K_MEM_SLAB_DEFINE_IN_SECT](../heap_reference/P003_固定块内存池公共接口.md#ga6b6751464262505c1117dea1bea56a08)
- [K_MEM_SLAB_DEFINE](../heap_reference/P003_固定块内存池公共接口.md#ga60bc92eee58fcc5f121b8e4d82eaa69e)
- [K_MEM_SLAB_DEFINE_TYPE](../heap_reference/P003_固定块内存池公共接口.md#ga8af8242518910449d31f7e97bed738cc)
- [K_MEM_SLAB_DEFINE_IN_SECT_STATIC](../heap_reference/P003_固定块内存池公共接口.md#ga7f0750f940b9a9f94b5c52373d4161f1)
- [K_MEM_SLAB_DEFINE_STATIC](../heap_reference/P003_固定块内存池公共接口.md#ga90bdbb15f410991f54ba16025c24bc3c)
- [K_MEM_SLAB_DEFINE_STATIC_TYPE](../heap_reference/P003_固定块内存池公共接口.md#ga11eac52a1ed0b0f8231c62e609515c42)
- [K_HEAP_DEFINE](../heap_reference/P001_内核堆公共接口.md#ga795d7f1e6d5b7b19a7a50198d7829a0f)
- [K_HEAP_DEFINE_NOCACHE](../heap_reference/P001_内核堆公共接口.md#ga968f4c6a201fdf6862d62dd5d9f8d032)
- [K_POLL_SIGNAL_INITIALIZER](../eventpoll_reference/P003_轮询公共接口.md#ga6d6321e189afca73a276cd671ec531ae)
- [K_POLL_EVENT_INITIALIZER](../eventpoll_reference/P003_轮询公共接口.md#ga8e3889f2bac281a6e65e31068e58047e)
- [K_POLL_EVENT_STATIC_INITIALIZER](../eventpoll_reference/P003_轮询公共接口.md#gada2366896d913dc916b3c28642648b63)
- [k_poll_event.type](../eventpoll_reference/P004_轮询事件结构.md#a8f9e251aa8722eb4716f622e85be34ae)
- [K_POLL_TYPE_IGNORE](../eventpoll_reference/P003_轮询公共接口.md#gafd5d801eb9e9cf6097b2c08b4933998e)
- [k_poll()](../eventpoll_reference/P003_轮询公共接口.md#gac550dc93662ce164fb22a5a91d6830db)
- [K_POLL_TYPE_SIGNAL](../eventpoll_reference/P003_轮询公共接口.md#ga144d8eb34d85f6053e454410a10bf56a)
- [K_POLL_TYPE_SEM_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga0fd7605bdffd43dff7480a90a603ffde)
- [K_POLL_TYPE_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga58d656f73f031a39b8a936133fe5504f)
- [K_POLL_TYPE_FIFO_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga71734fee18c523cf70276260118afb91)
- [K_POLL_TYPE_LIFO_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga7b45350902d604f16de5e49087db92a4)
- [K_POLL_TYPE_MSGQ_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gaa83509b54175fb6c98324422a928d5e1)
- [K_POLL_TYPE_PIPE_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga14e113201a3b3ad768c6a5ce917d1912)
- [k_poll_event.state](../eventpoll_reference/P004_轮询事件结构.md#aaf4f32852d799a406bfeea4e57891129)
- [K_POLL_STATE_NOT_READY](../eventpoll_reference/P003_轮询公共接口.md#ga522822c5e06a89b22ce4dcefd10c66aa)
- [K_POLL_STATE_SIGNALED](../eventpoll_reference/P003_轮询公共接口.md#ga478aae7fe4fb5c7b7c76ed216c22a7f1)
- [K_POLL_STATE_SEM_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gae9e3eefd5a29a538d22f53592578bb37)
- [K_POLL_STATE_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gac166d9919d591bace163c5211e7b41f4)
- [K_POLL_STATE_FIFO_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gabd5ac3341698534f39ded718079d6168)
- [K_POLL_STATE_LIFO_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gac66d063d5ffa24179b56ac8217a922e3)
- [K_POLL_STATE_MSGQ_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#gac236074cd43f59f28b803fe2c4a4f6f7)
- [K_POLL_STATE_PIPE_DATA_AVAILABLE](../eventpoll_reference/P003_轮询公共接口.md#ga9028d6868ee964ca25931ed9170068dd)
- [K_POLL_STATE_CANCELLED](../eventpoll_reference/P003_轮询公共接口.md#gadaf4b4c8e13afb54114af72d133e1fdb)
- [k_thread_user_cb_t](../thread_core_reference/P001_线程公共接口.md#gaf9f23a6ff9dae76af56f25b373e74c75)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_timer_expiry_t](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga2915762e70454d98c73c179a45cafbde)
- [k_timer_stop_t](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga106733712fc4e62b59bbe6a480bb988c)
- [k_work_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga5add9ef0dce306a08413c4140fc0bdda)
- [k_work_user_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaafa4dfac323cab570da1ee31c07d11bc)
- [execution_context_types](../api_device_topic_reference/P013_内核 API（Kernel APIs）.md#gab0b42f9804777dfa5fed2b7cd866779c)
- [K_ISR](../api_device_topic_reference/P013_内核 API（Kernel APIs）.md#ggab0b42f9804777dfa5fed2b7cd866779ca30593044743695f8184a157283dac4d5)
- [K_COOP_THREAD](../api_device_topic_reference/P013_内核 API（Kernel APIs）.md#ggab0b42f9804777dfa5fed2b7cd866779ca62c0b731a1bb3c5e4aadeba3f93df58b)
- [K_PREEMPT_THREAD](../api_device_topic_reference/P013_内核 API（Kernel APIs）.md#ggab0b42f9804777dfa5fed2b7cd866779cae84f57f4ac996c751d1f4c9e49789322)
- [K_WORK_RUNNING](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165)
- [K_WORK_CANCELING](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732)
- [K_WORK_QUEUED](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85)
- [K_WORK_DELAYED](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed)
- [K_WORK_FLUSHING](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601)
- [k_poll_modes](../eventpoll_reference/P003_轮询公共接口.md#ga36d7978872a83191dd3cc16d62165add)
- [K_POLL_MODE_NOTIFY_ONLY](../eventpoll_reference/P003_轮询公共接口.md#gga36d7978872a83191dd3cc16d62165adda22874743e2f6b0f1fd55c5375732b681)
- [K_POLL_NUM_MODES](../eventpoll_reference/P003_轮询公共接口.md#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c)
- [k_thread_runtime_stats_longest_frame_reset](../thread_core_reference/P001_线程公共接口.md#ga5d7f296b39346ea99a2a0efa3295b4a0)
- [k_thread_foreach](../thread_core_reference/P001_线程公共接口.md#gae2596d56800769b06fc03c194a126a97)
- [k_thread_foreach_filter_by_cpu](../thread_core_reference/P001_线程公共接口.md#ga82a83c2db36b34596dcb5afa5b28e41c)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [k_thread_foreach_unlocked](../thread_core_reference/P001_线程公共接口.md#ga30ef8b445a6c1b4a82651674dbb737fc)
- [k_thread_foreach_unlocked_filter_by_cpu](../thread_core_reference/P001_线程公共接口.md#gad908a1b9014aa048cf12997804ab7be2)
- [k_thread_stack_t](../api_file_host_video_reference/P001_zephyr__arch__arch_interface.h_文件参考.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)
- [k_thread_stack_alloc](../thread_core_reference/P001_线程公共接口.md#gafe00cc70bac8a47ba6dda21bde508614)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [k_thread_stack_free](../thread_core_reference/P001_线程公共接口.md#ga95560cb85f6656b981a9a50ff2cd70b7)
- [k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)
- [k_thread_create](../thread_core_reference/P001_线程公共接口.md#gad5b0bff3102f1656089f5875d999a367)
- [k_thread_entry_t](../api_file_host_video_reference/P001_zephyr__arch__arch_interface.h_文件参考.md#a3707e886593b0a8b4995309e4230b717)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [k_thread_user_mode_enter](../thread_core_reference/P001_线程公共接口.md#ga3fbe1c8a5f3ef1c25382c7d6fca35764)
- [k_thread_heap_assign](../thread_core_reference/P001_线程公共接口.md#ga3f46c06833add2a2e0ddb7242f06702c)
- [k_thread_join](../thread_core_reference/P001_线程公共接口.md#ga40a733561eb1f64dcaae0e01b167d233)
- [k_busy_wait](../thread_core_reference/P001_线程公共接口.md#ga550b642e071480323e589866abb99c22)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [k_can_yield](../thread_core_reference/P001_线程公共接口.md#ga366b9daa0be65b0a69dbc9f146064b68)
- [k_yield](../thread_core_reference/P001_线程公共接口.md#ga08a3484c33444ecedc2d71d78495a295)
- [k_wakeup](../thread_core_reference/P001_线程公共接口.md#ga9275a019c8ff3c7fe49a81f8c078157e)
- [k_sched_current_thread_query](../thread_core_reference/P001_线程公共接口.md#gac3b994b90b5bccded0895304f6b20c5d)
- [k_is_pre_kernel](../thread_core_reference/P001_线程公共接口.md#gae74e5de996276df767b96d4b50fa47ea)
- [k_current_get](../thread_core_reference/P001_线程公共接口.md#ga7ef1ed0fb9513df8096ede1e52fc76b2)
- [k_thread_abort](../thread_core_reference/P001_线程公共接口.md#ga1f44bb0307bea7a97227764ecd7bf963)
- [k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)
- [k_thread_timeout_expires_ticks](../thread_core_reference/P001_线程公共接口.md#gab0b1c85b847fe74170c04538fa9949ff)
- [k_thread_timeout_remaining_ticks](../thread_core_reference/P001_线程公共接口.md#ga4688c095c86e037a18594efdb9a5e9b9)
- [k_thread_priority_get](../thread_core_reference/P001_线程公共接口.md#ga3a46ed8ad2c3b12416fafe11325f82b3)
- [k_thread_priority_set](../thread_core_reference/P001_线程公共接口.md#ga24e50a60c524d1eb22fe21cdf269b6a6)
- [k_thread_deadline_set](../thread_core_reference/P001_线程公共接口.md#gad887f16c1dd6f3247682a83beb22d1ce)
- [k_thread_absolute_deadline_set](../thread_core_reference/P001_线程公共接口.md#ga2cb0b359b9324088abbb7003011879f8)
- [k_reschedule](../thread_core_reference/P001_线程公共接口.md#gad82575e576cd08906fbc68fe36be48bd)
- [k_thread_cpu_mask_clear](../thread_core_reference/P001_线程公共接口.md#ga80b9c58df6600c7e79f16756c128f44c)
- [k_thread_cpu_mask_enable_all](../thread_core_reference/P001_线程公共接口.md#gaedcfeb0964ae72611791241580b2119d)
- [k_thread_cpu_mask_enable](../thread_core_reference/P001_线程公共接口.md#ga306587604a7496db8059bd395fd90fc0)
- [k_thread_cpu_mask_disable](../thread_core_reference/P001_线程公共接口.md#ga89e6c07ac112da75b2ef115d1a557d44)
- [k_thread_cpu_pin](../thread_core_reference/P001_线程公共接口.md#gae9ebd9845e14ed02944ab9282a185c03)
- [k_thread_suspend](../thread_core_reference/P001_线程公共接口.md#ga66cf8682fb65870eceb5e57d667a8d4e)
- [k_thread_resume](../thread_core_reference/P001_线程公共接口.md#ga117b26f8569ec3045ead1fad1851663d)
- [k_thread_start](../thread_core_reference/P001_线程公共接口.md#gac539268e0b45c600315a6567ec27f965)
- [k_sched_time_slice_set](../thread_core_reference/P001_线程公共接口.md#ga877c1bfeffbf8f097d1656f9e10a66e8)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [k_thread_time_slice_set](../thread_core_reference/P001_线程公共接口.md#ga563928f292a4134acd4142029b60e631)
- [k_thread_timeslice_fn_t](../api_file_reference/P180_zephyr__kernel_structs.h_文件参考.md#a44c6f88a879877ad8da28706e274064f)
- [k_is_in_isr](../fatal_irq_reference/P007_中断服务接口.md#ga8482b0dd2283d12677a9ebe321667d16)
- [k_is_preempt_thread](../fatal_irq_reference/P007_中断服务接口.md#ga91e1cf0dc7fc93a3214cadb74ed86666)
- [k_sched_lock](../thread_core_reference/P001_线程公共接口.md#ga4f0c5d0b9f279b12a4ad97db0c116a5f)
- [k_sched_unlock](../thread_core_reference/P001_线程公共接口.md#ga7b26f64523cc4c36522cc828ccf85580)
- [k_thread_custom_data_set](../thread_core_reference/P001_线程公共接口.md#ga4834d9b81ed60c00eee77b0d4f8ab9e4)
- [k_thread_custom_data_get](../thread_core_reference/P001_线程公共接口.md#ga19af063cff7b306ba28062996922740d)
- [k_thread_name_set](../thread_core_reference/P001_线程公共接口.md#ga23107333f134b9c9a8b692374211e841)
- [k_thread_name_get](../thread_core_reference/P001_线程公共接口.md#gadebf45da56dee393164569742459dc0a)
- [k_thread_name_copy](../thread_core_reference/P001_线程公共接口.md#ga07b59ade055c69929ccdc08a14361794)
- [k_thread_state_str](../thread_core_reference/P001_线程公共接口.md#ga0c6af32096dc7ca391ffe2522bae4cb6)
- [k_timer_init](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga318c846a740b901e5d56876a47ad7f61)
- [k_timer_start](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga3ba70e9f059ff52fd2057ab89ea7f2ee)
- [k_timer_stop](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga8d3e3356a10d36570e16f7920e4c8772)
- [k_timer_status_get](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#gad532f4834cd4cf8be27b089e6ea347ce)
- [k_timer_status_sync](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga81d6d95b7021e26ad4cab161318e04f2)
- [k_timer_expires_ticks](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga022b4cf5c8d0ee21b6a3b04fd425533f)
- [k_timer_remaining_ticks](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga1176b36b960e786f68eaededf99a88b4)
- [k_timer_remaining_get](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga6c6d8b0aa59bfa0f5924e95ccf756259)
- [k_timer_user_data_set](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#gadba1884961e790dd9c5d567de91cc7e2)
- [k_timer_user_data_get](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga19a7d99a01a83828efd7f0d3bf2dd358)
- [k_timer_cleanup](../api_memory_timer_topic_reference/P010_定时器 API（Timer APIs）.md#ga39d502ccb6f299bf4efd82565684e508)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [k_uptime_ticks](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga8f143af2ee4ad42d9f7817ef161cbd13)
- [k_uptime_get](../timer_reference/P086_系统时钟公共接口.md#gae3e992cd3257c23d5b26d765fcbb2b69)
- [k_uptime_get_32](../timer_reference/P086_系统时钟公共接口.md#ga9253cfb7b46af4d8994349323ce9872b)
- [k_uptime_seconds](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gae082928ea608a8b180b4cb3a79d21a24)
- [k_uptime_delta](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gad748b2fe83b36884dc087b4af367de80)
- [k_cycle_get_32](../timer_reference/P086_系统时钟公共接口.md#ga208687de625e0036558343b4e66143d3)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [k_cycle_get_64](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gae09f509d02bf75a7b45d2800d823bb3a)
- [k_queue_init](../queue_reference/P001_通用队列公共接口.md#ga0236222d42768c2bf00942f328146c21)
- [k_queue_cancel_wait](../queue_reference/P001_通用队列公共接口.md#ga7c39d86cc6509f59ff9223cac3ea5071)
- [k_queue_append](../queue_reference/P001_通用队列公共接口.md#gaa84522a5ace6e7f8ba61033baca6972f)
- [k_queue_alloc_append](../queue_reference/P001_通用队列公共接口.md#ga690f3a1450e946d75f31b3e499d1d06a)
- [k_queue_prepend](../queue_reference/P001_通用队列公共接口.md#ga8ce013d8a037d4be5078797e0050e9c6)
- [k_queue_alloc_prepend](../queue_reference/P001_通用队列公共接口.md#gacf3dba40125073c11075e5a134919f88)
- [k_queue_insert](../queue_reference/P001_通用队列公共接口.md#gad47336f27e433a52600a3b67ab89556a)
- [k_queue_append_list](../queue_reference/P001_通用队列公共接口.md#ga91d1a144fc2aeb3dd655accc94ca43aa)
- [k_queue_merge_slist](../queue_reference/P001_通用队列公共接口.md#ga4eee0da7442d60572b05d60a9996e69d)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [k_queue_get](../queue_reference/P001_通用队列公共接口.md#ga0a77d8556e7d253319275de034f01619)
- [k_queue_remove](../queue_reference/P001_通用队列公共接口.md#ga4bff929ed1d366a06e00865a5bbe2544)
- [k_queue_unique_append](../queue_reference/P001_通用队列公共接口.md#ga287a2d81e2e3041be1cd45164e72f127)
- [k_queue_is_empty](../queue_reference/P001_通用队列公共接口.md#gadb2bb8088868b3c5801c72b320389ca9)
- [k_queue_peek_head](../queue_reference/P001_通用队列公共接口.md#ga8ccd5137690c127a0f7d67619b88a52b)
- [k_queue_peek_tail](../queue_reference/P001_通用队列公共接口.md#ga27a460c42836d8b093ad9274c14bb176)
- [k_futex_wait](../userspace_sync_reference/P001_Futex公共接口.md#ga596bfa265f88567ad9e80fd38cd433d3)
- [k_futex_wake](../userspace_sync_reference/P001_Futex公共接口.md#ga62de1aeb7c5c273aed20d0e05336d7a0)
- [k_event_init](../eventpoll_reference/P001_事件公共接口.md#gacf803590b39b095056f2b1c5090c4019)
- [k_event_post](../eventpoll_reference/P001_事件公共接口.md#gac88d17410a71642a903890e420d23d76)
- [k_event_set](../eventpoll_reference/P001_事件公共接口.md#gac22e9d768d003246e68b4b0b64e60f49)
- [k_event_set_masked](../eventpoll_reference/P001_事件公共接口.md#ga29b3ec1022b12a8c34884da3559c5864)
- [k_event_clear](../eventpoll_reference/P001_事件公共接口.md#gad6bfd7bfd0587bc70d3aa0b988010376)
- [k_event_wait](../eventpoll_reference/P001_事件公共接口.md#ga0f83f5f034e13bab65149fb90b87a753)
- [k_event_wait_all](../eventpoll_reference/P001_事件公共接口.md#gaddd60a99de5ac3d84f643c9433b744c1)
- [k_event_wait_safe](../eventpoll_reference/P001_事件公共接口.md#gab31c5012e1ae3740c3bde23b245a077e)
- [k_event_wait_all_safe](../eventpoll_reference/P001_事件公共接口.md#ga505ddf074c4903fca7e2d355b0caddac)
- [k_event_test](../eventpoll_reference/P001_事件公共接口.md#ga81e66be0959e8cb0414d9772056a6264)
- [k_stack_init](../msgstack_reference/P004_栈公共接口.md#ga4400a39ef48289305cf66a092d5c6c7d)
- [k_stack_alloc_init](../msgstack_reference/P004_栈公共接口.md#gab97d924db1aef3f6adade156a107d45c)
- [k_stack_cleanup](../msgstack_reference/P004_栈公共接口.md#ga819f4e7b2cf11cf2e1b80933fdcb67ea)
- [k_stack_push](../msgstack_reference/P004_栈公共接口.md#gaa6180f4db6ec93ee84149cba054d3e53)
- [k_stack_pop](../msgstack_reference/P004_栈公共接口.md#ga36ce6ceb9ea3d5c36d22b10430789480)
- [k_mutex_init](../synchronization_reference/P006_互斥量公共接口.md#ga56b64952fb8b78b00268a21c28b41480)
- [k_mutex_lock](../synchronization_reference/P006_互斥量公共接口.md#ga850549358645249c285669baa49c33b0)
- [k_mutex_unlock](../synchronization_reference/P006_互斥量公共接口.md#ga360f4c0e7258b0d7030cdb1f452b2c31)
- [k_condvar_init](../synchronization_reference/P010_条件变量公共接口.md#gac9b497c56cc4642965afa6c0c6d7ecfc)
- [k_condvar_signal](../synchronization_reference/P010_条件变量公共接口.md#ga0376a8f7dc6e4f1e1eed55940f43015b)
- [k_condvar_broadcast](../synchronization_reference/P010_条件变量公共接口.md#gad2e46a7b9e1bc934fd1f5cb38dde40d8)
- [k_condvar_wait](../synchronization_reference/P010_条件变量公共接口.md#gab2e1d05db4f954755f430ca894e44dbc)
- [k_sem_init](../synchronization_reference/P008_信号量公共接口.md#gadcd0e6cfba3392fb887222eafe4c1845)
- [k_sem_take](../synchronization_reference/P008_信号量公共接口.md#gac71e2383c1920dddc45a561cacfef090)
- [k_sem_give](../synchronization_reference/P008_信号量公共接口.md#gab9be3cf1988af2cd6afdace52d497c84)
- [k_sem_reset](../synchronization_reference/P008_信号量公共接口.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)
- [k_sem_count_get](../synchronization_reference/P008_信号量公共接口.md#ga58843b581e170a1811fc38eecbfd01f3)
- [k_work_init](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaf20080884a2893d39cd8e862b34a2a30)
- [k_work_busy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaba8a8734768d768b433f9d8490e7df7b)
- [k_work_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)
- [k_work_submit_to_queue](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga5353e76f73db070614f50d06d292d05c)
- [k_work_submit](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gace61b59575093d7442f39ccb7be686d7)
- [k_work_flush](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gabd1cda459bab538fb2d6dfd84a73b253)
- [k_work_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga389fe2a8fb20f9bd593cf8d990727078)
- [k_work_cancel_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gab2b05cfe3af08f7d32c3946fa1c808f9)
- [k_work_queue_init](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gada77d818ea9e4d07c14a960872ed5492)
- [k_work_queue_start](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gadfc56554f9bfe7b52309d79660188593)
- [k_work_queue_run](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gac7fc60238574769e4eae6a2cc38da87b)
- [k_work_queue_thread_get](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga0b8b496f7e7bd82d08590a07293e38d7)
- [k_work_queue_drain](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga0fefe3e0225ac99b47b250849f6cd863)
- [k_work_queue_unplug](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaa0463bb79af3ec470f7d3be02052139f)
- [k_work_queue_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga1fd2fce94eb731ccb0838ec763e62f5c)
- [k_work_init_delayable](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga2876c5d82fb2340a093bc4d689a55465)
- [k_work_delayable_from_work](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gabcb822a03ce7ea9ee1ed046afe31ffca)
- [k_work_delayable_busy_get](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga1b76969667844f0981d348c9c671bc9f)
- [k_work_delayable_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga66e598dbc73f653cbfec03c21168df2e)
- [k_work_delayable_expires_get](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga1772c37bc62b86180d5cf48fe3037624)
- [k_work_delayable_remaining_get](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gabce78598a014f3ed87730fe6a9fe61b4)
- [k_work_schedule_for_queue](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga17f863c9f6ff2fb41dc0f3b7de4fdf23)
- [k_work_schedule](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)
- [k_work_reschedule_for_queue](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gabf5db091eac19b19a4e12c0cb381f0a8)
- [k_work_reschedule](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaacaab408fb7c848d466ad1f069dfa648)
- [k_work_flush_delayable](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gad47d54e513030304be2600d75b1a965f)
- [k_work_cancel_delayable](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga92355914ee178d4c3e848a1946bed3e4)
- [k_work_cancel_delayable_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga7e7ec237648556fc16bfda8d35f7cd86)
- [k_work_user_init](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga9de9c7a7f13cc6b325e5453e34afe62d)
- [k_work_user_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga58d05d4127e4cd51104a1f1a87f626cd)
- [k_work_user_submit_to_queue](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga50ae1f6f74c0bc0a41dbbf789fff8856)
- [k_work_user_queue_start](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga3091bc8fab5311252e41634a97a18589)
- [k_work_user_queue_thread_get](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gab487068e9564cd77b6bdbac3d5670923)
- [k_work_poll_init](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga371dab33a40622bea19b07d852863443)
- [k_work_poll_submit_to_queue](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga0abafd7f851e42fd3572c8438e600a53)
- [k_work_poll_submit](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gad9f222e46d72c4f98739395a0c8bb4ea)
- [k_work_poll_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga2a19547d04dc1a202e80b752e3177215)
- [k_msgq_init](../msgstack_reference/P001_消息队列公共接口.md#ga54a5cdcaea2236c383ace433fedc0d39)
- [k_msgq_alloc_init](../msgstack_reference/P001_消息队列公共接口.md#gabe7305b8f442ebdc147dbbc6e8cf92fc)
- [k_msgq_cleanup](../msgstack_reference/P001_消息队列公共接口.md#gafda4399aa9b8f1e44bdf752e00ea787b)
- [k_msgq_put](../msgstack_reference/P001_消息队列公共接口.md#ga54e96aaaea5462a1f963b7fd5ca82bfe)
- [k_msgq_put_front](../msgstack_reference/P001_消息队列公共接口.md#gac45d9468d2b70bc4e49183ba5a9a3844)
- [k_msgq_get](../msgstack_reference/P001_消息队列公共接口.md#gae67f2ced2df1f9c290ae15dab9097cb7)
- [k_msgq_peek](../msgstack_reference/P001_消息队列公共接口.md#ga14f543472f2f63cfde0bdfa87b95c915)
- [k_msgq_peek_at](../msgstack_reference/P001_消息队列公共接口.md#ga69b004a40ab4ca497de314a99960fb8e)
- [k_msgq_purge](../msgstack_reference/P001_消息队列公共接口.md#gaa18875887773195ae44b7fe0972ee760)
- [k_msgq_num_free_get](../msgstack_reference/P001_消息队列公共接口.md#ga7d154beb4f9c6227eddbef26d406ca24)
- [k_msgq_get_attrs](../msgstack_reference/P001_消息队列公共接口.md#ga8f9d3eef67cbc9c0717a84190bbf7f41)
- [k_msgq_num_used_get](../msgstack_reference/P001_消息队列公共接口.md#ga458793a89f1d9f762bda3422918a9faa)
- [k_mbox_init](../mboxpipe_reference/P001_邮箱公共接口.md#ga686f20c199a9e971822d8279d175d8c2)
- [k_mbox_put](../mboxpipe_reference/P001_邮箱公共接口.md#gaa1e5cdd992d8b9be11f82254e1886ed2)
- [k_mbox_async_put](../mboxpipe_reference/P001_邮箱公共接口.md#gadd60f7b760371c0a141a1e4da253a0f0)
- [k_mbox_get](../mboxpipe_reference/P001_邮箱公共接口.md#ga2ea91154620b139dbed1ad949b97c3ef)
- [k_mbox_data_get](../mboxpipe_reference/P001_邮箱公共接口.md#ga3d19e648e67f109609259543c9a01d6e)
- [k_pipe_init](../mboxpipe_reference/P004_管道公共接口.md#gae2c8d97af1f7e9deb93e670859525cf3)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [k_pipe_write](../mboxpipe_reference/P004_管道公共接口.md#ga514ab3d174dcada766ecbda138944ddc)
- [k_pipe_read](../mboxpipe_reference/P004_管道公共接口.md#gaecb07412025d9e065ee7b99121522257)
- [k_pipe_reset](../mboxpipe_reference/P004_管道公共接口.md#gaaedff72169127b8227c80bf8adf1f9dd)
- [k_pipe_close](../mboxpipe_reference/P004_管道公共接口.md#ga83d4b5de8902845850d01b0c3db0702a)
- [k_mem_slab_init](../heap_reference/P003_固定块内存池公共接口.md#ga094a8f173f287e29bb287119c26889d1)
- [k_mem_slab_alloc](../heap_reference/P003_固定块内存池公共接口.md#gab16a46d8394aca18de740ad044a8734a)
- [k_mem_slab_free](../heap_reference/P003_固定块内存池公共接口.md#ga2635ea8f9a30b8751ec966fe62adc0e1)
- [k_mem_slab_num_used_get](../heap_reference/P003_固定块内存池公共接口.md#gac76b96d7055e4ad94765c93530dd0720)
- [k_mem_slab_max_used_get](../heap_reference/P003_固定块内存池公共接口.md#gae0e949c1c3476dd57bc0c0ed627d2346)
- [k_mem_slab_num_free_get](../heap_reference/P003_固定块内存池公共接口.md#gae87577e2873cf746db69216a82f94aea)
- [k_mem_slab_runtime_stats_get](../heap_reference/P003_固定块内存池公共接口.md#ga32030a5cfb44f663bd31b4e1b3d5dddb)
- [sys_memory_stats](../lowheap_reference/P005_内存统计结构.md)
- [k_mem_slab_runtime_stats_reset_max](../heap_reference/P003_固定块内存池公共接口.md#gaa1f44e30f4aee98b38e1ab5e93af505c)
- [k_heap_init](../heap_reference/P001_内核堆公共接口.md#ga9273e06dc8d6a351499f2f5abfdcb39f)
- [k_heap_aligned_alloc](../heap_reference/P001_内核堆公共接口.md#gaf77211a72441de389857bc13e10be4e6)
- [k_heap_alloc](../heap_reference/P001_内核堆公共接口.md#ga22b83564e50ae6177388dfe63e32a512)
- [k_heap_calloc](../heap_reference/P001_内核堆公共接口.md#ga53de68a83567cff1cff3eab5d8572449)
- [k_heap_realloc](../heap_reference/P001_内核堆公共接口.md#gabea4b2beae8ab138f2796fbeaa95d262)
- [k_heap_free](../heap_reference/P001_内核堆公共接口.md#ga6cf917a0b3d91a0101192bd4808ada9c)
- [k_heap_array_get](../heap_reference/P001_内核堆公共接口.md#ga3aa215396381e1513edf50bd9563dee5)
- [k_aligned_alloc](../heap_reference/P001_内核堆公共接口.md#gae16d486aa250f9c07fa6a57342bcd3b4)
- [k_malloc](../heap_reference/P001_内核堆公共接口.md#gaa8edf1e63e5d5dd78d7adcfd787394ee)
- [k_free](../heap_reference/P001_内核堆公共接口.md#ga79b63cc93b3358cf82d74f40e73b69d5)
- [k_calloc](../heap_reference/P001_内核堆公共接口.md#gad031d50ed62d08202a5dcf992c20246c)
- [k_realloc](../heap_reference/P001_内核堆公共接口.md#ga852a7a60dce5853b6925897b24a54e02)
- [k_poll_event_init](../eventpoll_reference/P003_轮询公共接口.md#gaa06bddd93a024fc5326d93187d80eb03)
- [k_poll_signal_init](../eventpoll_reference/P003_轮询公共接口.md#gaee3090c2a912b93b6a5855e3018c3551)
- [k_poll_signal_reset](../eventpoll_reference/P003_轮询公共接口.md#ga02d899d1455ae1f3f55ffe8f1ebd6994)
- [k_poll_signal_check](../eventpoll_reference/P003_轮询公共接口.md#ga69dae11c7cb2c669caa411c3e7001311)
- [k_poll_signal_raise](../eventpoll_reference/P003_轮询公共接口.md#gad0bf3825f828ec3ca37481bf3cbd6723)
- [k_cpu_idle](../fatal_irq_reference/P011_CPU空闲接口.md#ga7b25e1bed511a813b32fbd0f91b09356)
- [k_cpu_atomic_idle](../fatal_irq_reference/P011_CPU空闲接口.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f)
- [k_float_disable](../fatal_irq_reference/P012_浮点上下文接口.md#ga2df4b2550ace30512cddebd36b6a54a1)
- [k_float_enable](../fatal_irq_reference/P012_浮点上下文接口.md#ga81fb955ddd41658a9aad5c083f173f77)
- [k_thread_runtime_stats_t](../thread_core_reference/P002_线程头文件参考.md#a887f70695cd229ea8f30ea3e1faf45cf)
- [K_ERR_KERNEL_OOPS](../fatal_irq_reference/P004_致命错误原因接口.md#gga5b7e799fa19549ef9416a2d6cba29b52ad6bc280fafebf22e2c97481cc4a5b7c3)
- [K_ERR_KERNEL_PANIC](../fatal_irq_reference/P004_致命错误原因接口.md#gga5b7e799fa19549ef9416a2d6cba29b52a6ea29e224a1bc958a961420471711617)
- [CONFIG_SCHED_IPI_SUPPORTED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SCHED_IPI_SUPPORTED)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__fatal__types_html_gga5b7e799fa19549ef9416a2d6cba29b52ad6bc280fafebf22e2c97481cc4a5b7c3"></a>
<a id="agroup__fatal__types_html_gga5b7e799fa19549ef9416a2d6cba29b52a6ea29e224a1bc958a961420471711617"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_zephyr__net__ieee802154_frame.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__dt-bindings__clock__mchp_pic32cm_pl_clock.h_文件参考.md)
