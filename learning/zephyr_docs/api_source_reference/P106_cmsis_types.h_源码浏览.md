---
id: learning.zephyr-docs.api-source-reference.page-106
title: cmsis_types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cmsis__types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第106章\_cmsis\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cmsis__types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cmsis__types_8h.html)。

## 106.1\_原始可见代码（Source Code）

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
<a id="foldopen00026"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="foldopen00061"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00090"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="agroup__doubly-linked-list__apis_html_ga57fdb936802a617d16c00ab08cd2ad98"></a>
<a id="akernel_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructcmsis__rtos__event__cb_html"></a>
<a id="astructcmsis__rtos__mempool__cb_html"></a>
<a id="astructcmsis__rtos__msgq__cb_html"></a>
<a id="astructcmsis__rtos__mutex__cb_html"></a>
<a id="astructcmsis__rtos__semaphore__cb_html"></a>
<a id="astructcmsis__rtos__thread__cb_html"></a>
<a id="astructcmsis__rtos__timer__cb_html"></a>
<a id="astructk__event_html"></a>
<a id="astructk__msgq_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructk__poll__event_html"></a>
<a id="astructk__poll__signal_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__thread_html"></a>
<a id="astructk__timer_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_PORTABILITY_CMSIS_TYPES_H_
#define ZEPHYR_INCLUDE_PORTABILITY_CMSIS_TYPES_H_

#include <stdbool.h>
#include <zephyr/kernel.h>
#include <zephyr/portability/cmsis_os2.h>

struct cmsis_rtos_thread_cb {
        sys_dnode_t node;
        struct k_thread z_thread;
        struct k_poll_signal poll_signal;
        struct k_poll_event poll_event;
        uint32_t signal_results;
        uint32_t attr_bits;
};

struct cmsis_rtos_timer_cb {
        struct k_timer z_timer;
        osTimerType_t type;
        uint32_t status;
        bool is_cb_dynamic_allocation;
        const char *name;
        void (*callback_function)(void *argument);
        void *arg;
};

struct cmsis_rtos_mutex_cb {
        struct k_mutex z_mutex;
        bool is_cb_dynamic_allocation;
        const char *name;
        uint32_t state;
};

struct cmsis_rtos_semaphore_cb {
        struct k_sem z_semaphore;
        bool is_cb_dynamic_allocation;
        const char *name;
};

struct cmsis_rtos_mempool_cb {
        struct k_mem_slab z_mslab;
        void *pool;
        char is_dynamic_allocation;
        bool is_cb_dynamic_allocation;
        const char *name;
};

struct cmsis_rtos_msgq_cb {
        struct k_msgq z_msgq;
        void *pool;
        char is_dynamic_allocation;
        bool is_cb_dynamic_allocation;
        const char *name;
};

struct cmsis_rtos_event_cb {
        struct k_event z_event;
        bool is_cb_dynamic_allocation;
        const char *name;
};

#endif /* ZEPHYR_INCLUDE_PORTABILITY_CMSIS_TYPES_H_ */
```

## 106.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 130 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PORTABILITY_CMSIS_TYPES_H_`。

## 106.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cmsis__types_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [cmsis_rtos_thread_cb](../clock_cmsis_model_reference/P029_cmsis_rtos_thread_cb_结构体.md)
- [sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [k_poll_event](../eventpoll_reference/P004_轮询事件结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [cmsis_rtos_timer_cb](../clock_cmsis_model_reference/P030_cmsis_rtos_timer_cb_结构体.md)
- [k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)
- [cmsis_rtos_mutex_cb](../clock_cmsis_model_reference/P027_cmsis_rtos_mutex_cb_结构体.md)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [cmsis_rtos_semaphore_cb](../clock_cmsis_model_reference/P028_cmsis_rtos_semaphore_cb_结构体.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [cmsis_rtos_mempool_cb](../clock_cmsis_model_reference/P025_cmsis_rtos_mempool_cb_结构体.md)
- [cmsis_rtos_msgq_cb](../clock_cmsis_model_reference/P026_cmsis_rtos_msgq_cb_结构体.md)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)
- [cmsis_rtos_event_cb](../clock_cmsis_model_reference/P024_cmsis_rtos_event_cb_结构体.md)
- [k_event](../eventpoll_reference/P002_内核事件结构.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P105_clock_control_silabs_siwx91x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P107_coap_link_format.h_源码浏览.md)
