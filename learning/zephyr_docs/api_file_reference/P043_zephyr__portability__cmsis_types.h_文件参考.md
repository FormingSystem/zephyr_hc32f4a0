---
id: learning.zephyr-docs.api-file-reference.page-43
title: zephyr__portability__cmsis_types.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cmsis__types_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_zephyr\_\_portability\_\_cmsis\_types.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cmsis__types_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CMSIS-RTOSv2对象控制块（Object Control Block）结构的头文件。

<a id="details"></a>

```c
#include <stdbool.h>
#include <zephyr/kernel.h>
#include <zephyr/portability/cmsis_os2.h>
```

查看此文件的源码。

CMSIS-RTOSv2对象控制块（Object Control Block）结构的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 43.1\_数据结构（Data Structures）

<a id="r_cmsis_5Frtos_5Fthread_5Fcb"></a>

```c
struct cmsis_rtos_thread_cb
```

相关声明：[cmsis_rtos_thread_cb](../clock_cmsis_model_reference/P029_cmsis_rtos_thread_cb_结构体.md)。

CMSIS-RTOSv2 线程（Thread）的控制块。

<a id="r_cmsis_5Frtos_5Ftimer_5Fcb"></a>

```c
struct cmsis_rtos_timer_cb
```

相关声明：[cmsis_rtos_timer_cb](../clock_cmsis_model_reference/P030_cmsis_rtos_timer_cb_结构体.md)。

CMSIS-RTOSv2 定时器（Timer）的控制块。

<a id="r_cmsis_5Frtos_5Fmutex_5Fcb"></a>

```c
struct cmsis_rtos_mutex_cb
```

相关声明：[cmsis_rtos_mutex_cb](../clock_cmsis_model_reference/P027_cmsis_rtos_mutex_cb_结构体.md)。

CMSIS-RTOSv2 互斥锁（Mutex）的控制块。

<a id="r_cmsis_5Frtos_5Fsemaphore_5Fcb"></a>

```c
struct cmsis_rtos_semaphore_cb
```

相关声明：[cmsis_rtos_semaphore_cb](../clock_cmsis_model_reference/P028_cmsis_rtos_semaphore_cb_结构体.md)。

CMSIS-RTOSv2 信号量（Semaphore）的控制块。

<a id="r_cmsis_5Frtos_5Fmempool_5Fcb"></a>

```c
struct cmsis_rtos_mempool_cb
```

相关声明：[cmsis_rtos_mempool_cb](../clock_cmsis_model_reference/P025_cmsis_rtos_mempool_cb_结构体.md)。

CMSIS-RTOSv2 内存池（Memory Pool）的控制块。

<a id="r_cmsis_5Frtos_5Fmsgq_5Fcb"></a>

```c
struct cmsis_rtos_msgq_cb
```

相关声明：[cmsis_rtos_msgq_cb](../clock_cmsis_model_reference/P026_cmsis_rtos_msgq_cb_结构体.md)。

CMSIS-RTOSv2 消息队列（Message Queue）的控制块。

<a id="r_cmsis_5Frtos_5Fevent_5Fcb"></a>

```c
struct cmsis_rtos_event_cb
```

相关声明：[cmsis_rtos_event_cb](../clock_cmsis_model_reference/P024_cmsis_rtos_event_cb_结构体.md)。

CMSIS-RTOSv2 事件标志（Event Flag）的控制块（Control Block）。


## 43.2\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P106_cmsis_types.h_源码浏览.md)
- [cmsis_rtos_thread_cb](../clock_cmsis_model_reference/P029_cmsis_rtos_thread_cb_结构体.md)
- [cmsis_rtos_timer_cb](../clock_cmsis_model_reference/P030_cmsis_rtos_timer_cb_结构体.md)
- [cmsis_rtos_mutex_cb](../clock_cmsis_model_reference/P027_cmsis_rtos_mutex_cb_结构体.md)
- [cmsis_rtos_semaphore_cb](../clock_cmsis_model_reference/P028_cmsis_rtos_semaphore_cb_结构体.md)
- [cmsis_rtos_mempool_cb](../clock_cmsis_model_reference/P025_cmsis_rtos_mempool_cb_结构体.md)
- [cmsis_rtos_msgq_cb](../clock_cmsis_model_reference/P026_cmsis_rtos_msgq_cb_结构体.md)
- [cmsis_rtos_event_cb](../clock_cmsis_model_reference/P024_cmsis_rtos_event_cb_结构体.md)

<a id="header-details"></a>

---

[上一章](P042_zephyr__drivers__clock_control__clock_control_rts5912.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P044_zephyr__dt-bindings__clock__silabs__common-clock.h_文件参考.md)
