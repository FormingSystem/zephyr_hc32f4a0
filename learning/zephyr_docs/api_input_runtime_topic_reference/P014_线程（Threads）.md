---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-14
title: 线程（Threads）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_线程（Threads）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__thread.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

一种 `k_thread`，其栈来自池，且栈的生命周期长于该线程。

<a id="details"></a>

栈来自存储池、且栈的生命周期长于线程的 `k_thread`。流水线（Pipeline）在启动和停止时创建、销毁线程；没有堆（Heap）的系统不能简单地释放并重新分配线程栈。本包装器从固定池获取栈，池大小由 `CONFIG_MPIPE_THREADS_NUM` 指定；线程终止后将栈归还池，供下一线程复用。线程创建时处于休眠状态，并显式启动，使流水线能够在任何处理运行前构建完整处理图（Graph）。`mpipe_thread_wait` 是循环的协作点（Cooperation Point）：暂停时阻塞，并报告是否收到等待退出（Join）请求，让源端循环能够主动退出，而非在执行中被强行终止。

<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_mpipe_5Fthread_2Eh"></a>

```c
file mpipe_thread.h
```

相关声明：[mpipe_thread.h](../api_file_interface_reference/P034_zephyr__mpipe__mpipe_thread.h_文件参考.md)。

k_thread的简单封装，用于在线程终止后复用其栈（Stack）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fthread"></a>

```c
struct mpipe_thread
```

相关声明：[mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)。

对k_thread的简单封装（Wrapper）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.3\_函数（Functions）

<a id="r_gafa93b18b47d5b9cc8fa339a84db61aab"></a>

```c
k_tid_t mpipe_thread_create (struct mpipe_thread *thread, k_thread_entry_t func, void *p1, void *p2, void *p3, int priority, k_timeout_t delay)
```

相关声明：[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)、[mpipe_thread_create](#gafa93b18b47d5b9cc8fa339a84db61aab)、[mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)、[k_thread_entry_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a3707e886593b0a8b4995309e4230b717)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

复用线程池（thread pool）中的栈来创建一个新线程。

<a id="r_gadd34ee4835e935aa33543154abdda9c5"></a>

```c
int mpipe_thread_wait (struct mpipe_thread *thread)
```

相关声明：[mpipe_thread_wait](#gadd34ee4835e935aa33543154abdda9c5)、[mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)。

阻塞线程，直到允许其运行或要求其退出。

<a id="r_gacdb6da11544520d860e4e9e4cfc5d743"></a>

```c
void mpipe_thread_resume (struct mpipe_thread *thread)
```

相关声明：[mpipe_thread_resume](#gacdb6da11544520d860e4e9e4cfc5d743)、[mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)。

恢复已暂停的线程。

<a id="r_gac18dcc29e1b57c96defdd69eaae066eb"></a>

```c
void mpipe_thread_pause (struct mpipe_thread *thread)
```

相关声明：[mpipe_thread_pause](#gac18dcc29e1b57c96defdd69eaae066eb)、[mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)。

暂停正在运行的线程。

<a id="r_ga2e378caa15981102db80289c9bd844cb"></a>

```c
int mpipe_thread_join (struct mpipe_thread *thread, k_timeout_t timeout)
```

相关声明：[mpipe_thread_join](#ga2e378caa15981102db80289c9bd844cb)、[mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

等待线程结束（join），并将其栈释放回线程栈池（thread stack pool）。

## 14.4\_详细说明（Detailed Documentation）

<a id="gafa93b18b47d5b9cc8fa339a84db61aab"></a>

### `mpipe_thread_create()`

```c
k_tid_t mpipe_thread_create ( struct mpipe_thread * thread, k_thread_entry_t func, void * p1, void * p2, void * p3, int priority, k_timeout_t delay )
```

```c
#include <zephyr/mpipe/mpipe_thread.h>
```

复用线程池（thread pool）中的栈来创建一个新线程。

线程经过 `delay` 后启动。流水线传入 `K_FOREVER`，并在 `PAUSED → PLAYING` 时用 `mpipe_thread_resume()` 启动：从未被调度的线程无论优先级如何，都不会抢占 `READY → PAUSED` 转换的其余步骤；流水线暂停期间不占用 CPU 时间，且第一条指令执行时便能看到完整处理图（Graph）。仅靠 `mpipe_thread_wait()` 把关会让线程先运行一次，然后才停驻。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `thread` | 指向尚未初始化的线程结构体（Struct Threads）的指针。 |
| `func` | 线程入口函数（Entry Function）。 |
| `p1` | 传递给线程入口函数的第一个参数（First Parameter）。 |
| `p2` | 传递给线程入口函数的第二个参数（Second Parameter）。 |
| `p3` | 传递给线程入口函数的第三个参数（Third Parameter）。 |
| `priority` | 线程优先级。 |
| `delay` | 线程启动前的延迟（Delay）；`K_FOREVER` 表示恢复时启动。 |

**返回（Returns）**：**返回值（Returns）：**线程 ID；池中没有空闲栈（Free Stack）时返回 `NULL`。

<a id="ga2e378caa15981102db80289c9bd844cb"></a>

### `mpipe_thread_join()`

```c
int mpipe_thread_join ( struct mpipe_thread * thread, k_timeout_t timeout )
```

```c
#include <zephyr/mpipe/mpipe_thread.h>
```

等待线程结束（join），并将其栈释放回线程栈池（thread stack pool）。

通知线程退出，等待其终止，并将栈归还池（Pool）。若线程从未唤醒，会将其唤醒，使其看到终止请求并退出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `thread` | 指向要等待退出（Join）的线程结构体（Struct Threads）的指针。 |
| `timeout` | 等待线程退出（Join）的最长时间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功，栈已归还池（Pool）。 |

**返回（Returns）**：**返回值（Returns）：**`k_thread_join()` 返回的任意负 `errno`，例如超时返回 `-EAGAIN`；此时栈仍处于占用状态（Claimed）。

<a id="gac18dcc29e1b57c96defdd69eaae066eb"></a>

### `mpipe_thread_pause()`

```c
void mpipe_thread_pause ( struct mpipe_thread * thread)
```

```c
#include <zephyr/mpipe/mpipe_thread.h>
```

暂停正在运行的线程。

线程将在下一次调用 `mpipe_thread_wait()` 时阻塞。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `thread` | 指向要暂停（Pause）的线程结构体（Struct Threads）的指针。 |

<a id="gacdb6da11544520d860e4e9e4cfc5d743"></a>

### `mpipe_thread_resume()`

```c
void mpipe_thread_resume ( struct mpipe_thread * thread)
```

```c
#include <zephyr/mpipe/mpipe_thread.h>
```

恢复已暂停的线程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `thread` | 指向要恢复（Resume）的线程结构体（Struct Threads）的指针。 |

<a id="gadd34ee4835e935aa33543154abdda9c5"></a>

### `mpipe_thread_wait()`

```c
int mpipe_thread_wait ( struct mpipe_thread * thread)
```

```c
#include <zephyr/mpipe/mpipe_thread.h>
```

阻塞线程，直到允许其运行或要求其退出。

线程入口函数应在处理循环开始处调用本函数。线程暂停时阻塞，处于运行状态时立即返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `thread` | 指向线程结构体（Struct Threads）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 线程应继续执行，处于运行状态（Running）。 |
| `-ECANCELED` | 线程必须退出，已收到等待退出请求（Join Requested）。 |


## 14.5\_原页交叉引用（Cross References）

- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [mpipe_thread.h](../api_file_interface_reference/P034_zephyr__mpipe__mpipe_thread.h_文件参考.md)
- [mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)
- [k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)
- [k_thread_entry_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a3707e886593b0a8b4995309e4230b717)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [CONFIG_MPIPE_THREADS_NUM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_THREADS_NUM)
- [线程（Threads）](P014_线程（Threads）.md)
- [k_thread_join()](../thread_core_reference/P001_线程公共接口.md#ga40a733561eb1f64dcaae0e01b167d233)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_映像管理客户端（Image Management Client）.md) · [返回大纲](大纲.md) · [下一章](P015_网络链路地址库（Network Link Address Library）.md)
