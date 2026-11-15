---
id: learning.zephyr-docs.api-source-runtime-reference.page-44
title: mpipe_thread.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__thread_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_mpipe\_thread.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__thread_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__thread_8h.html)。

## 44.1\_原始可见代码（Source Code）

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
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="aarch__interface_8h_html_a3707e886593b0a8b4995309e4230b717"></a>
<a id="aatomic_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__mpipe__thread_html_ga2e378caa15981102db80289c9bd844cb"></a>
<a id="agroup__mpipe__thread_html_gac18dcc29e1b57c96defdd69eaae066eb"></a>
<a id="agroup__mpipe__thread_html_gacdb6da11544520d860e4e9e4cfc5d743"></a>
<a id="agroup__mpipe__thread_html_gadd34ee4835e935aa33543154abdda9c5"></a>
<a id="agroup__mpipe__thread_html_gafa93b18b47d5b9cc8fa339a84db61aab"></a>
<a id="akernel_2thread_8h_html"></a>
<a id="akernel_2thread_8h_html_a6379f5a1f19ffbc262a6877c4f6e3647"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__thread_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructmpipe__thread_html"></a>
<a id="astructmpipe__thread_html_a4f75d45bd330b68366bbdeb0a32f8295"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_THREAD_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_THREAD_H_


#include <zephyr/kernel/thread.h>
#include <zephyr/sys/atomic.h>

/* Thread state: paused and resumable, running, or terminated */
enum mpipe_thread_state {
        MPIPE_THREAD_PAUSED = 0,
        MPIPE_THREAD_RUNNING,
        MPIPE_THREAD_TERMINATED,
};

struct mpipe_thread {
        struct k_thread thread;
        /* Gates run / pause transitions */
        struct k_sem sem;
        uint8_t stack_id;
        /* enum mpipe_thread_state */
        atomic_t state;
        int priority;
};

k_tid_t mpipe_thread_create(struct mpipe_thread *thread, k_thread_entry_t func, void *p1, void *p2,
                            void *p3, int priority, k_timeout_t delay);

int mpipe_thread_wait(struct mpipe_thread *thread);

void mpipe_thread_resume(struct mpipe_thread *thread);

void mpipe_thread_pause(struct mpipe_thread *thread);

int mpipe_thread_join(struct mpipe_thread *thread, k_timeout_t timeout);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_THREAD_H_ */
```

## 44.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 40 行

线程状态（Thread state）：已暂停且可恢复、正在运行或已终止。

### 注释 3：原第 57 行

控制运行/暂停状态转换（Run / pause transitions）。

### 注释 4：原第 60 行

枚举类型：`enum mpipe_thread_state`。

### 注释 5：原第 138 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_THREAD_H_`。

## 44.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__thread_8h.html)
- [zephyr/kernel/thread.h](../thread_core_reference/P002_线程头文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [priority](../audio_video_model_reference/P033_mpipe_thread_结构体.md#a4f75d45bd330b68366bbdeb0a32f8295)
- [k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)
- [mpipe_thread_create](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#gafa93b18b47d5b9cc8fa339a84db61aab)
- [k_thread_entry_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a3707e886593b0a8b4995309e4230b717)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [mpipe_thread_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#gadd34ee4835e935aa33543154abdda9c5)
- [mpipe_thread_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#gacdb6da11544520d860e4e9e4cfc5d743)
- [mpipe_thread_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#gac18dcc29e1b57c96defdd69eaae066eb)
- [mpipe_thread_join](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#ga2e378caa15981102db80289c9bd844cb)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [thread.h](../thread_core_reference/P002_线程头文件参考.md)
- [mpipe_thread::priority](../audio_video_model_reference/P033_mpipe_thread_结构体.md#a4f75d45bd330b68366bbdeb0a32f8295)

---

[上一章](P043_mipi_dsi_mcux_2l.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P045_ppp.h_源码浏览.md)
