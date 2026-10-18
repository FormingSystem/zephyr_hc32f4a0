---
id: learning.zephyr-docs.api-file-interface-reference.page-34
title: zephyr__mpipe__mpipe_thread.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__thread_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_zephyr\_\_mpipe\_\_mpipe\_thread.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__thread_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

k_thread的简单封装，用于在线程终止后复用其栈（Stack）。

<a id="details"></a>

```c
#include <zephyr/kernel/thread.h>
#include <zephyr/sys/atomic.h>
```

查看此文件的源码。

k_thread的简单封装，用于在线程终止后复用其栈（Stack）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 34.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fthread"></a>

```c
struct mpipe_thread
```

相关声明：[mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)。

对k_thread的简单封装（Wrapper）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 34.2\_函数（Functions）

<a id="r_gafa93b18b47d5b9cc8fa339a84db61aab"></a>

```c
k_tid_t mpipe_thread_create (struct mpipe_thread *thread, k_thread_entry_t func, void *p1, void *p2, void *p3, int priority, k_timeout_t delay)
```

相关声明：[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)、[mpipe_thread_create](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#gafa93b18b47d5b9cc8fa339a84db61aab)、[mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)、[k_thread_entry_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a3707e886593b0a8b4995309e4230b717)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

复用线程池（thread pool）中的栈来创建一个新线程。

<a id="r_gadd34ee4835e935aa33543154abdda9c5"></a>

```c
int mpipe_thread_wait (struct mpipe_thread *thread)
```

相关声明：[mpipe_thread_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#gadd34ee4835e935aa33543154abdda9c5)、[mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)。

阻塞线程，直到允许其运行或要求其退出。

<a id="r_gacdb6da11544520d860e4e9e4cfc5d743"></a>

```c
void mpipe_thread_resume (struct mpipe_thread *thread)
```

相关声明：[mpipe_thread_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#gacdb6da11544520d860e4e9e4cfc5d743)、[mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)。

恢复已暂停的线程。

<a id="r_gac18dcc29e1b57c96defdd69eaae066eb"></a>

```c
void mpipe_thread_pause (struct mpipe_thread *thread)
```

相关声明：[mpipe_thread_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#gac18dcc29e1b57c96defdd69eaae066eb)、[mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)。

暂停正在运行的线程。

<a id="r_ga2e378caa15981102db80289c9bd844cb"></a>

```c
int mpipe_thread_join (struct mpipe_thread *thread, k_timeout_t timeout)
```

相关声明：[mpipe_thread_join](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#ga2e378caa15981102db80289c9bd844cb)、[mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

等待线程结束（join），并将其栈释放回线程栈池（thread stack pool）。


## 34.3\_原页交叉引用（Cross References）

- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [zephyr/kernel/thread.h](../thread_core_reference/P003_线程头文件源码.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [查看此文件的源码。](../api_source_runtime_reference/P044_mpipe_thread.h_源码浏览.md)
- [mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)
- [k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)
- [mpipe_thread_create](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#gafa93b18b47d5b9cc8fa339a84db61aab)
- [k_thread_entry_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a3707e886593b0a8b4995309e4230b717)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [mpipe_thread_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#gadd34ee4835e935aa33543154abdda9c5)
- [mpipe_thread_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#gacdb6da11544520d860e4e9e4cfc5d743)
- [mpipe_thread_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#gac18dcc29e1b57c96defdd69eaae066eb)
- [mpipe_thread_join](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html#ga2e378caa15981102db80289c9bd844cb)

<a id="header-details"></a>

---

[上一章](P033_zephyr__mpipe__mpipe_src.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P035_zephyr__mpipe__mpipe_transform.h_文件参考.md)
