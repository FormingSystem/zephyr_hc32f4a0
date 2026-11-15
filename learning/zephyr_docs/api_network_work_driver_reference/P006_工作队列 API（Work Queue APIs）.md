---
id: learning.zephyr-docs.api-network-work-driver-reference.page-6
title: 工作队列 API（Work Queue APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_工作队列 API（Work Queue APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ga893b281f3d2bc0088650536899e17903"></a>

```c
#define K_WORK_DELAYABLE_DEFINE(work, work_handler)
```

相关声明：[K_WORK_DELAYABLE_DEFINE](#ga893b281f3d2bc0088650536899e17903)。

初始化静态定义的可延迟工作项（Delayable Work Item）。

<a id="r_ga4f3eac1fc56d5c9c21a3afa9b964b0bf"></a>

```c
#define K_WORK_USER_DEFINE(work, work_handler)
```

相关声明：[K_WORK_USER_DEFINE](#ga4f3eac1fc56d5c9c21a3afa9b964b0bf)。

初始化静态定义的用户工作项（User Work Item）。

<a id="r_gaf8e003eefa5dd66ba883688f9d39c333"></a>

```c
#define K_WORK_DEFINE(work, work_handler)
```

相关声明：[K_WORK_DEFINE](#gaf8e003eefa5dd66ba883688f9d39c333)。

初始化静态定义的工作项（Work Item）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_ga5add9ef0dce306a08413c4140fc0bdda"></a>

```c
typedef void(* k_work_handler_t) (struct k_work *work)
```

相关声明：[k_work_handler_t](#ga5add9ef0dce306a08413c4140fc0bdda)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

工作项处理函数（Work Item Handler）的函数签名。

<a id="r_gaafa4dfac323cab570da1ee31c07d11bc"></a>

```c
typedef void(* k_work_user_handler_t) (struct k_work_user *work)
```

相关声明：[k_work_user_handler_t](#gaafa4dfac323cab570da1ee31c07d11bc)。

用户工作队列（User Work Queue）的工作项处理函数（Handler）类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.4\_枚举（Enumerations）

<a id="r_gae539da4c3f3d31b039bc49b9e76744eb"></a>

```c
enum { K_WORK_RUNNING = BIT(K_WORK_RUNNING_BIT) , K_WORK_CANCELING = BIT(K_WORK_CANCELING_BIT) , K_WORK_QUEUED = BIT(K_WORK_QUEUED_BIT) , K_WORK_DELAYED = BIT(K_WORK_DELAYED_BIT) , K_WORK_FLUSHING = BIT(K_WORK_FLUSHING_BIT) }
```

相关声明：[K_WORK_RUNNING](#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165)、[K_WORK_CANCELING](#ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732)、[K_WORK_QUEUED](#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85)、[K_WORK_DELAYED](#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed)、[K_WORK_FLUSHING](#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601)。

工作项（Work Item）与工作队列（Work Queue）的状态标志值。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.5\_函数（Functions）

<a id="r_gaf20080884a2893d39cd8e862b34a2a30"></a>

```c
void k_work_init (struct k_work *work, k_work_handler_t handler)
```

相关声明：[k_work_init](#gaf20080884a2893d39cd8e862b34a2a30)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[k_work_handler_t](#ga5add9ef0dce306a08413c4140fc0bdda)。

初始化不可延迟的工作结构体（Work Structure）。

<a id="r_gaba8a8734768d768b433f9d8490e7df7b"></a>

```c
int k_work_busy_get (const struct k_work *work)
```

相关声明：[k_work_busy_get](#gaba8a8734768d768b433f9d8490e7df7b)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

获取工作项（Work Item）的忙状态标志（Busy State Flags）。

<a id="r_ga0d1d2e1d2ba2e89a560a1bdc5365d9e0"></a>

```c
static bool k_work_is_pending (const struct k_work *work)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_is_pending](#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

检查工作项（Work Item）当前是否处于待处理（Pending）状态。

<a id="r_ga5353e76f73db070614f50d06d292d05c"></a>

```c
int k_work_submit_to_queue (struct k_work_q *queue, struct k_work *work)
```

相关声明：[k_work_submit_to_queue](#ga5353e76f73db070614f50d06d292d05c)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

将工作项（Work Item）提交到队列（Queue）。

<a id="r_gace61b59575093d7442f39ccb7be686d7"></a>

```c
int k_work_submit (struct k_work *work)
```

相关声明：[k_work_submit](#gace61b59575093d7442f39ccb7be686d7)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

将工作项（Work Item）提交到系统队列（System Queue）。

<a id="r_gabd1cda459bab538fb2d6dfd84a73b253"></a>

```c
bool k_work_flush (struct k_work *work, struct k_work_sync *sync)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_flush](#gabd1cda459bab538fb2d6dfd84a73b253)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)。

等待最后提交的实例（Last-submitted Instance）完成。

<a id="r_ga389fe2a8fb20f9bd593cf8d990727078"></a>

```c
int k_work_cancel (struct k_work *work)
```

相关声明：[k_work_cancel](#ga389fe2a8fb20f9bd593cf8d990727078)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

取消工作项（Work Item）。

<a id="r_gab2b05cfe3af08f7d32c3946fa1c808f9"></a>

```c
bool k_work_cancel_sync (struct k_work *work, struct k_work_sync *sync)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_cancel_sync](#gab2b05cfe3af08f7d32c3946fa1c808f9)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)。

取消工作项（Work Item），并等待其完成。

<a id="r_gada77d818ea9e4d07c14a960872ed5492"></a>

```c
void k_work_queue_init (struct k_work_q *queue)
```

相关声明：[k_work_queue_init](#gada77d818ea9e4d07c14a960872ed5492)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)。

初始化工作队列结构体（Work Queue Structure）。

<a id="r_gadfc56554f9bfe7b52309d79660188593"></a>

```c
void k_work_queue_start (struct k_work_q *queue, k_thread_stack_t *stack, size_t stack_size, int prio, const struct k_work_queue_config *cfg)
```

相关声明：[k_work_queue_start](#gadfc56554f9bfe7b52309d79660188593)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_thread_stack_t](../api_file_host_video_reference/P001_zephyr__arch__arch_interface.h_文件参考.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)、[k_work_queue_config](../kernel_runtime_model_reference/P011_k_work_queue_config_结构体.md)。

初始化工作队列（Work Queue）。

<a id="r_gac7fc60238574769e4eae6a2cc38da87b"></a>

```c
void k_work_queue_run (struct k_work_q *queue, const struct k_work_queue_config *cfg)
```

相关声明：[k_work_queue_run](#gac7fc60238574769e4eae6a2cc38da87b)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_work_queue_config](../kernel_runtime_model_reference/P011_k_work_queue_config_结构体.md)。

使用调用线程（Calling Thread）运行工作队列（Work Queue）。

<a id="r_ga0b8b496f7e7bd82d08590a07293e38d7"></a>

```c
static k_tid_t k_work_queue_thread_get (struct k_work_q *queue)
```

相关声明：[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)、[k_work_queue_thread_get](#ga0b8b496f7e7bd82d08590a07293e38d7)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)。

访问运行工作队列（Work Queue）的线程（Thread）。

<a id="r_ga0fefe3e0225ac99b47b250849f6cd863"></a>

```c
int k_work_queue_drain (struct k_work_q *queue, bool plug)
```

相关声明：[k_work_queue_drain](#ga0fefe3e0225ac99b47b250849f6cd863)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

等待工作队列（Work Queue）排空，并可选择阻止其接受新提交（Plug）。

<a id="r_gaa0463bb79af3ec470f7d3be02052139f"></a>

```c
int k_work_queue_unplug (struct k_work_q *queue)
```

相关声明：[k_work_queue_unplug](#gaa0463bb79af3ec470f7d3be02052139f)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)。

解除工作队列（Work Queue）的提交阻塞，使其接受新提交。

<a id="r_ga1fd2fce94eb731ccb0838ec763e62f5c"></a>

```c
int k_work_queue_stop (struct k_work_q *queue, k_timeout_t timeout)
```

相关声明：[k_work_queue_stop](#ga1fd2fce94eb731ccb0838ec763e62f5c)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

停止工作队列（Work Queue）。

<a id="r_ga2876c5d82fb2340a093bc4d689a55465"></a>

```c
void k_work_init_delayable (struct k_work_delayable *dwork, k_work_handler_t handler)
```

相关声明：[k_work_init_delayable](#ga2876c5d82fb2340a093bc4d689a55465)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_work_handler_t](#ga5add9ef0dce306a08413c4140fc0bdda)。

初始化可延迟工作结构体（Delayable Work Structure）。

<a id="r_gabcb822a03ce7ea9ee1ed046afe31ffca"></a>

```c
static struct k_work_delayable * k_work_delayable_from_work (struct k_work *work)
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_work_delayable_from_work](#gabcb822a03ce7ea9ee1ed046afe31ffca)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

根据工作指针（Work Pointer）获取其所属的可延迟工作结构体（Delayable Work Structure）。

<a id="r_ga1b76969667844f0981d348c9c671bc9f"></a>

```c
int k_work_delayable_busy_get (const struct k_work_delayable *dwork)
```

相关声明：[k_work_delayable_busy_get](#ga1b76969667844f0981d348c9c671bc9f)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)。

获取可延迟工作项（Delayable Work Item）的忙状态标志（Busy State Flags）。

<a id="r_ga66e598dbc73f653cbfec03c21168df2e"></a>

```c
static bool k_work_delayable_is_pending (const struct k_work_delayable *dwork)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_delayable_is_pending](#ga66e598dbc73f653cbfec03c21168df2e)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)。

检查延迟工作项（Delayed Work Item）当前是否处于待处理（Pending）状态。

<a id="r_ga1772c37bc62b86180d5cf48fe3037624"></a>

```c
static k_ticks_t k_work_delayable_expires_get (const struct k_work_delayable *dwork)
```

相关声明：[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)、[k_work_delayable_expires_get](#ga1772c37bc62b86180d5cf48fe3037624)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)。

获取已调度的可延迟工作（Delayable Work）将被提交时的绝对节拍计数（Absolute Tick Count）。

<a id="r_gabce78598a014f3ed87730fe6a9fe61b4"></a>

```c
static k_ticks_t k_work_delayable_remaining_get (const struct k_work_delayable *dwork)
```

相关声明：[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)、[k_work_delayable_remaining_get](#gabce78598a014f3ed87730fe6a9fe61b4)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)。

获取已调度的可延迟工作（Delayable Work）距离提交还需经过的节拍数（Ticks）。

<a id="r_ga17f863c9f6ff2fb41dc0f3b7de4fdf23"></a>

```c
int k_work_schedule_for_queue (struct k_work_q *queue, struct k_work_delayable *dwork, k_timeout_t delay)
```

相关声明：[k_work_schedule_for_queue](#ga17f863c9f6ff2fb41dc0f3b7de4fdf23)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

延迟一段时间后，将空闲工作项（Idle Work Item）提交到队列（Queue）。

<a id="r_ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3"></a>

```c
int k_work_schedule (struct k_work_delayable *dwork, k_timeout_t delay)
```

相关声明：[k_work_schedule](#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

延迟一段时间后，将空闲工作项（Idle Work Item）提交到系统工作队列（System Work Queue）。

<a id="r_gabf5db091eac19b19a4e12c0cb381f0a8"></a>

```c
int k_work_reschedule_for_queue (struct k_work_q *queue, struct k_work_delayable *dwork, k_timeout_t delay)
```

相关声明：[k_work_reschedule_for_queue](#gabf5db091eac19b19a4e12c0cb381f0a8)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

重新调度工作项（Work Item），使其延迟一段时间后提交到队列（Queue）。

<a id="r_gaacaab408fb7c848d466ad1f069dfa648"></a>

```c
int k_work_reschedule (struct k_work_delayable *dwork, k_timeout_t delay)
```

相关声明：[k_work_reschedule](#gaacaab408fb7c848d466ad1f069dfa648)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

重新调度工作项（Work Item），使其延迟一段时间后提交到系统工作队列（System Work Queue）。

<a id="r_gad47d54e513030304be2600d75b1a965f"></a>

```c
bool k_work_flush_delayable (struct k_work_delayable *dwork, struct k_work_sync *sync)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_flush_delayable](#gad47d54e513030304be2600d75b1a965f)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)。

排空可延迟工作（Flush Delayable Work）。

<a id="r_ga92355914ee178d4c3e848a1946bed3e4"></a>

```c
int k_work_cancel_delayable (struct k_work_delayable *dwork)
```

相关声明：[k_work_cancel_delayable](#ga92355914ee178d4c3e848a1946bed3e4)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)。

取消可延迟工作（Cancel Delayable Work）。

<a id="r_ga7e7ec237648556fc16bfda8d35f7cd86"></a>

```c
bool k_work_cancel_delayable_sync (struct k_work_delayable *dwork, struct k_work_sync *sync)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_cancel_delayable_sync](#ga7e7ec237648556fc16bfda8d35f7cd86)、[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)。

取消可延迟工作（Delayable Work），并等待。

<a id="r_ga9de9c7a7f13cc6b325e5453e34afe62d"></a>

```c
static void k_work_user_init (struct k_work_user *work, k_work_user_handler_t handler)
```

相关声明：[k_work_user_init](#ga9de9c7a7f13cc6b325e5453e34afe62d)、[k_work_user_handler_t](#gaafa4dfac323cab570da1ee31c07d11bc)。

初始化用户空间工作项（Userspace Work Item）。

<a id="r_ga58d05d4127e4cd51104a1f1a87f626cd"></a>

```c
static bool k_work_user_is_pending (struct k_work_user *work)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_work_user_is_pending](#ga58d05d4127e4cd51104a1f1a87f626cd)。

检查用户空间工作项（Userspace Work Item）是否处于待处理（Pending）状态。

<a id="r_ga50ae1f6f74c0bc0a41dbbf789fff8856"></a>

```c
static int k_work_user_submit_to_queue (struct k_work_user_q *work_q, struct k_work_user *work)
```

相关声明：[k_work_user_submit_to_queue](#ga50ae1f6f74c0bc0a41dbbf789fff8856)。

将工作项（Work Item）提交到用户模式工作队列（User Mode Workqueue）。

<a id="r_ga3091bc8fab5311252e41634a97a18589"></a>

```c
void k_work_user_queue_start (struct k_work_user_q *work_q, k_thread_stack_t *stack, size_t stack_size, int prio, const char *name)
```

相关声明：[k_work_user_queue_start](#ga3091bc8fab5311252e41634a97a18589)、[k_thread_stack_t](../api_file_host_video_reference/P001_zephyr__arch__arch_interface.h_文件参考.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)。

在用户模式（User Mode）下启动工作队列（Workqueue）。

<a id="r_gab487068e9564cd77b6bdbac3d5670923"></a>

```c
static k_tid_t k_work_user_queue_thread_get (struct k_work_user_q *work_q)
```

相关声明：[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)、[k_work_user_queue_thread_get](#gab487068e9564cd77b6bdbac3d5670923)。

访问运行工作队列（Work Queue）的用户模式线程（User Mode Thread）。

<a id="r_ga371dab33a40622bea19b07d852863443"></a>

```c
void k_work_poll_init (struct k_work_poll *work, k_work_handler_t handler)
```

相关声明：[k_work_poll_init](#ga371dab33a40622bea19b07d852863443)、[k_work_handler_t](#ga5add9ef0dce306a08413c4140fc0bdda)。

初始化触发式工作项（Triggered Work Item）。

<a id="r_ga0abafd7f851e42fd3572c8438e600a53"></a>

```c
int k_work_poll_submit_to_queue (struct k_work_q *work_q, struct k_work_poll *work, struct k_poll_event *events, int num_events, k_timeout_t timeout)
```

相关声明：[k_work_poll_submit_to_queue](#ga0abafd7f851e42fd3572c8438e600a53)、[k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)、[k_poll_event](../eventpoll_reference/P004_轮询事件结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

提交触发式工作项（Triggered Work Item）。

<a id="r_gad9f222e46d72c4f98739395a0c8bb4ea"></a>

```c
int k_work_poll_submit (struct k_work_poll *work, struct k_poll_event *events, int num_events, k_timeout_t timeout)
```

相关声明：[k_work_poll_submit](#gad9f222e46d72c4f98739395a0c8bb4ea)、[k_poll_event](../eventpoll_reference/P004_轮询事件结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

将触发式工作项（Triggered Work Item）提交到系统工作队列（System Workqueue）。

<a id="r_ga2a19547d04dc1a202e80b752e3177215"></a>

```c
int k_work_poll_cancel (struct k_work_poll *work)
```

相关声明：[k_work_poll_cancel](#ga2a19547d04dc1a202e80b752e3177215)。

取消触发式工作项（Triggered Work Item）。

## 6.6\_详细说明（Detailed Documentation）

<a id="gaf8e003eefa5dd66ba883688f9d39c333"></a>

### `K_WORK_DEFINE`

```c
#define K_WORK_DEFINE ( work, work_handler )
```

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
struct k_work work = Z_WORK_INITIALIZER(work_handler)
```

初始化静态定义的工作项（Work Item）。

此宏可在首次使用前初始化静态定义的工作队列工作项（Workqueue Work Item）。例如：

原始示例（Example）：

```c
static K_WORK_DEFINE(<work>, <work_handler>);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 工作项对象（Work Item Object）的符号名称。 |
| `work_handler` | 每次处理工作项（Work Item）时调用的函数。 |

<a id="ga893b281f3d2bc0088650536899e17903"></a>

### `K_WORK_DELAYABLE_DEFINE`

```c
#define K_WORK_DELAYABLE_DEFINE ( work, work_handler )
```

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
struct k_work_delayable work \
  = Z_WORK_DELAYABLE_INITIALIZER(work_handler)
```

初始化静态定义的可延迟工作项（Delayable Work Item）。

此宏可在首次使用前初始化静态定义的可延迟工作项（Delayable Work Item）。例如：

原始示例（Example）：

```c
static K_WORK_DELAYABLE_DEFINE(<dwork>, <work_handler>);
```

注意：如果运行时依赖条件允许使用 `k_work_init_delayable()` 初始化，则采用该函数可以省去此宏生成在 ROM 中、并在系统启动时复制的已初始化对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 可延迟工作项对象（Delayable Work Item Object）的符号名称。 |
| `work_handler` | 每次处理工作项（Work Item）时调用的函数。 |

<a id="ga4f3eac1fc56d5c9c21a3afa9b964b0bf"></a>

### `K_WORK_USER_DEFINE`

```c
#define K_WORK_USER_DEFINE ( work, work_handler )
```

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
struct k_work_user work = Z_WORK_USER_INITIALIZER(work_handler)
```

初始化静态定义的用户工作项（User Work Item）。

此宏可在首次使用前初始化静态定义的用户工作项（User Work Item）。例如：

原始示例（Example）：

```c
static K_WORK_USER_DEFINE(<work>, <work_handler>);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 工作项对象（Work Item Object）的符号名称。 |
| `work_handler` | 每次处理工作项（Work Item）时调用的函数。 |

<a id="ga5add9ef0dce306a08413c4140fc0bdda"></a>

### `k_work_handler_t`

```c
typedef void(* k_work_handler_t) (struct k_work *work)
```

```c
#include <zephyr/kernel.h>
```

工作项处理函数（Work Item Handler）的函数签名。

此函数将由驱动工作队列（Work Queue）执行的线程调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 提供该处理函数（Handler）的工作项。 |

<a id="gaafa4dfac323cab570da1ee31c07d11bc"></a>

### `k_work_user_handler_t`

```c
typedef void(* k_work_user_handler_t) (struct k_work_user *work)
```

```c
#include <zephyr/kernel.h>
```

用户工作队列（User Work Queue）的工作项处理函数（Handler）类型。

工作项由用户工作队列（User Workqueue）处理时，其处理函数（Handler Function）由该工作队列的线程执行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 工作项（Work Item）的地址。 |

<a id="gae539da4c3f3d31b039bc49b9e76744eb"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/kernel.h>
```

工作项（Work Item）与工作队列（Work Queue）的状态标志值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `K_WORK_RUNNING` | 表示工作项正由工作队列线程执行（Running）的标志。通过 `k_work_busy_get()` 访问，可以与其他标志同时存在。 |
| `K_WORK_CANCELING` | 表示工作项正在取消（Canceling）的标志。通过 `k_work_busy_get()` 访问，可以与其他标志同时存在。 |
| `K_WORK_QUEUED` | 表示工作项已提交到队列，但尚未开始执行（Queued）的标志。通过 `k_work_busy_get()` 访问，可以与其他标志同时存在。 |
| `K_WORK_DELAYED` | 表示可延迟工作项已计划提交到队列（Delayed）的标志。通过 `k_work_busy_get()` 访问，可以与其他标志同时存在。 |
| `K_WORK_FLUSHING` | 表示同步工作项正在等待完成（Flushing）的标志。通过 `k_work_busy_get()` 访问，可以与其他标志同时存在。 |

<a id="gaba8a8734768d768b433f9d8490e7df7b"></a>

### `k_work_busy_get()`

```c
int k_work_busy_get ( const struct k_work * work)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

获取工作项（Work Item）的忙状态标志（Busy State Flags）。

返回值为 0 表示工作项当前看起来处于空闲状态（Idle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 指向工作项（Work Item）的指针。 |

**说明（Note）**：注意：这是状态的即时快照（Live Snapshot），结果被检查前状态就可能变化。必要时使用锁（Locks）。

**返回（Returns）**：返回值：由 `K_WORK_DELAYED`、`K_WORK_QUEUED`、`K_WORK_RUNNING`、`K_WORK_CANCELING` 和 `K_WORK_FLUSHING` 标志组成的掩码。

<a id="ga389fe2a8fb20f9bd593cf8d990727078"></a>

### `k_work_cancel()`

```c
int k_work_cancel ( struct k_work * work)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

取消工作项（Work Item）。

此函数尝试从工作队列移除待处理的非可延迟工作项（Non-delayable Work Item），以阻止其被处理。如果工作项正在处理，它仍会继续执行，但直到取消完成前，都拒绝再次提交（Resubmission）。

如果返回 0，则取消（Cancellation）已完成；否则，仍有对象，通常为工作队列线程，正在引用此工作项。

另请参见 `k_work_cancel_sync()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 指向工作项（Work Item）的指针。 |

**返回（Returns）**：返回值：`k_work_busy_get()` 状态，表示本次调用执行的所有取消步骤完成后，该工作项的状态。

<a id="ga92355914ee178d4c3e848a1946bed3e4"></a>

### `k_work_cancel_delayable()`

```c
int k_work_cancel_delayable ( struct k_work_delayable * dwork)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

取消可延迟工作（Cancel Delayable Work）。

类似 `k_work_cancel()`，但用于可延迟工作（Delayable Work）。如果工作项已计划调度或已提交，则取消它。此函数不等待取消完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dwork` | 指向可延迟工作项（Delayable Work Item）的指针。 |

**说明（Note）**：注意：函数返回时，工作项可能仍在执行。使用 `k_work_flush_delayable()` 或 `k_work_cancel_delayable_sync()` 可确保它不再执行。取消可延迟工作不会阻止重新调度（Rescheduling），但在取消完成前会阻止提交（Submitting）。

**返回（Returns）**：返回值：`k_work_delayable_busy_get()` 状态，表示本次调用执行的所有取消步骤完成后，该工作项的状态。

<a id="ga7e7ec237648556fc16bfda8d35f7cd86"></a>

### `k_work_cancel_delayable_sync()`

```c
bool k_work_cancel_delayable_sync ( struct k_work_delayable * dwork, struct k_work_sync * sync )
```

```c
#include <zephyr/kernel.h>
```

取消可延迟工作（Delayable Work），并等待。

类似 `k_work_cancel_delayable()`，但会等待工作项进入空闲状态（Idle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dwork` | 指向可延迟工作项（Delayable Work Item）的指针。 |
| `sync` | 指向不透明对象（Opaque Item）的指针，该对象保存与待完成取消操作相关的状态。对象必须一直存在到本次调用返回，并能被调用线程和工作队列线程访问。本操作完成前，不得将该对象用于任何其他等待完成（Flush）或取消（Cancel）操作。在启用 `CONFIG_KERNEL_COHERENCE` 的体系结构上，必须在一致性内存（Coherent Memory）中分配该对象。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 工作项原本不是空闲状态（Idle）：本次调用需要等待正在执行的处理函数取消完成，或取消了已计划调度或已提交的操作。 |
| `false` | 其他情况。 |

**说明（Note）**：注意：取消可延迟工作不会阻止重新调度（Rescheduling），但在取消完成前会阻止提交。需要注意调用线程与工作队列线程的相对优先级。如果此函数进入睡眠，必须等工作队列线程完成使本线程能够恢复的任务后才会返回。如果从正在执行 `dwork` 的工作队列中，对该 `dwork` 调用此函数，则行为未定义。

<a id="gab2b05cfe3af08f7d32c3946fa1c808f9"></a>

### `k_work_cancel_sync()`

```c
bool k_work_cancel_sync ( struct k_work * work, struct k_work_sync * sync )
```

```c
#include <zephyr/kernel.h>
```

取消工作项（Work Item），并等待其完成。

与 `k_work_cancel()` 相同，但直到取消完成后才返回。线程可在 `k_work_cancel()` 之后调用此函数，以与之前的取消操作同步（Synchronize）。

返回时，工作结构处于空闲状态（Idle），除非取消完成后有其他执行者再次提交了它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 指向工作项（Work Item）的指针。 |
| `sync` | 指向不透明对象（Opaque Item）的指针，该对象保存与待完成取消操作相关的状态。对象必须一直存在到本次调用返回，并能被调用线程和工作队列线程访问。本操作完成前，不得将该对象用于任何其他等待完成（Flush）或取消（Cancel）操作。在启用 `CONFIG_KERNEL_COHERENCE` 的体系结构上，必须在一致性内存（Coherent Memory）中分配该对象。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 工作项原本处于待处理状态（Pending）：本次调用需要等待正在执行的处理函数取消完成，或取消了已计划调度或已提交的操作。 |
| `false` | 其他情况。 |

**说明（Note）**：注意调用线程与工作队列线程的相对优先级。如果此函数进入睡眠，必须等工作队列线程完成使本线程能够恢复的任务后才会返回。如果从正在执行 `work` 的工作队列中，对该 `work` 调用此函数，则行为未定义。

<a id="ga1b76969667844f0981d348c9c671bc9f"></a>

### `k_work_delayable_busy_get()`

```c
int k_work_delayable_busy_get ( const struct k_work_delayable * dwork)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

获取可延迟工作项（Delayable Work Item）的忙状态标志（Busy State Flags）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dwork` | 指向可延迟工作项（Delayable Work Item）的指针。 |

**说明（Note）**：注意：这是状态的即时快照（Live Snapshot），结果被查看前状态就可能变化。必要时使用锁（Locks）。

**返回（Returns）**：返回值：由 `K_WORK_DELAYED`、`K_WORK_QUEUED`、`K_WORK_RUNNING`、`K_WORK_CANCELING` 和 `K_WORK_FLUSHING` 标志组成的掩码。值为 0 表示工作项当前看起来处于空闲状态（Idle）。

<a id="ga1772c37bc62b86180d5cf48fe3037624"></a>

### `k_work_delayable_expires_get()`

```c
k_ticks_t k_work_delayable_expires_get ( const struct k_work_delayable * dwork)
```

声明属性：`inline`、`static`、`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

获取已调度的可延迟工作（Delayable Work）将被提交时的绝对节拍计数（Absolute Tick Count）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dwork` | 指向可延迟工作项（Delayable Work Item）的指针。 |

**说明（Note）**：注意：这是状态的即时快照（Live Snapshot），结果被查看前状态就可能变化。必要时使用锁（Locks）。

**返回（Returns）**：返回值：用于调度此工作项的定时器到期时的系统节拍计数（Tick Count）；如果工作项未被计划调度，则返回当前节拍计数。

<a id="gabcb822a03ce7ea9ee1ed046afe31ffca"></a>

### `k_work_delayable_from_work()`

```c
struct k_work_delayable * k_work_delayable_from_work ( struct k_work * work)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/kernel.h>
```

根据工作指针（Work Pointer）获取其所属的可延迟工作结构体（Delayable Work Structure）。

当一个 `k_work_handler_t` 函数被传给 `k_work_schedule_for_queue()`，且处理函数需要访问其所属 `k_work_delayable` 所在容器的数据时，需要使用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 传给工作处理函数（Work Handler）的地址。 |

**返回（Returns）**：返回值：所属 `k_work_delayable` 结构的地址。

<a id="ga66e598dbc73f653cbfec03c21168df2e"></a>

### `k_work_delayable_is_pending()`

```c
bool k_work_delayable_is_pending ( const struct k_work_delayable * dwork)
```

声明属性：`inline`、`static`、`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

检查延迟工作项（Delayed Work Item）当前是否处于待处理（Pending）状态。

用于判断可延迟工作项是否处于非空闲状态（Non-idle State）的封装函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dwork` | 指向可延迟工作项（Delayable Work Item）的指针。 |

**说明（Note）**：注意：这是状态的即时快照（Live Snapshot），结果被查看前状态就可能变化。必要时使用锁（Locks）。

**返回（Returns）**：返回值：当且仅当 `k_work_delayable_busy_get()` 返回非零值时为 `true`。

<a id="gabce78598a014f3ed87730fe6a9fe61b4"></a>

### `k_work_delayable_remaining_get()`

```c
k_ticks_t k_work_delayable_remaining_get ( const struct k_work_delayable * dwork)
```

声明属性：`inline`、`static`、`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

获取已调度的可延迟工作（Delayable Work）距离提交还需经过的节拍数（Ticks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dwork` | 指向可延迟工作项（Delayable Work Item）的指针。 |

**说明（Note）**：注意：这是状态的即时快照（Live Snapshot），结果被查看前状态就可能变化。必要时使用锁（Locks）。

**返回（Returns）**：返回值：距离用于调度此工作项的定时器到期还剩多少系统节拍（Ticks）；工作项未被计划调度时为 0。

<a id="gabd1cda459bab538fb2d6dfd84a73b253"></a>

### `k_work_flush()`

```c
bool k_work_flush ( struct k_work * work, struct k_work_sync * sync )
```

```c
#include <zephyr/kernel.h>
```

等待最后提交的实例（Last-submitted Instance）完成。

等待期间可能发生再次提交（Resubmission），包括从处理函数内部发起的链式提交（Chained Submission）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 指向工作项（Work Item）的指针。 |
| `sync` | 指向不透明对象（Opaque Item）的指针，该对象保存与待完成取消操作相关的状态。对象必须一直存在到本次调用返回，并能被调用线程和工作队列线程访问。本操作完成前，不得将该对象用于任何其他等待完成（Flush）或取消（Cancel）操作。在启用 `CONFIG_KERNEL_COHERENCE` 的体系结构上，必须在一致性内存（Coherent Memory）中分配该对象。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 本次调用必须等待操作完成。 |
| `false` | 工作项已经空闲（Idle）。 |

**说明（Note）**：注意调用线程与工作队列线程的相对优先级。如果此函数进入睡眠，必须等工作队列线程完成使本线程能够恢复的任务后才会返回。如果从正在执行 `work` 的工作队列中，对该 `work` 调用此函数，则行为未定义。

<a id="gad47d54e513030304be2600d75b1a965f"></a>

### `k_work_flush_delayable()`

```c
bool k_work_flush_delayable ( struct k_work_delayable * dwork, struct k_work_sync * sync )
```

```c
#include <zephyr/kernel.h>
```

排空可延迟工作（Flush Delayable Work）。

如果工作项已计划调度，则立即提交它。随后调用者阻塞，直到工作项完成，与 `k_work_flush()` 相同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dwork` | 指向可延迟工作项（Delayable Work Item）的指针。 |
| `sync` | 指向不透明对象（Opaque Item）的指针，该对象保存与待完成取消操作相关的状态。对象必须一直存在到本次调用返回，并能被调用线程和工作队列线程访问。本操作完成前，不得将该对象用于任何其他等待完成（Flush）或取消（Cancel）操作。在启用 `CONFIG_KERNEL_COHERENCE` 的体系结构上，必须在一致性内存（Coherent Memory）中分配该对象。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 本次调用必须等待操作完成。 |
| `false` | 工作项已经空闲（Idle）。 |

**说明（Note）**：注意调用线程与工作队列线程的相对优先级。如果此函数进入睡眠，必须等工作队列线程完成使本线程能够恢复的任务后才会返回。如果从正在执行 `dwork` 的工作队列中，对该 `dwork` 调用此函数，则行为未定义。

<a id="gaf20080884a2893d39cd8e862b34a2a30"></a>

### `k_work_init()`

```c
void k_work_init ( struct k_work * work, k_work_handler_t handler )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

初始化不可延迟的工作结构体（Work Structure）。

首次提交工作结构（Work Structure）前必须调用此函数。同一工作结构无需再次初始化。可以再次调用以更改关联的处理函数（Handler），但必须在工作项空闲（Idle）时进行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 要初始化的工作结构（Work Structure）。 |
| `handler` | 工作项要调用的处理函数（Handler）。 |

<a id="ga2876c5d82fb2340a093bc4d689a55465"></a>

### `k_work_init_delayable()`

```c
void k_work_init_delayable ( struct k_work_delayable * dwork, k_work_handler_t handler )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

初始化可延迟工作结构体（Delayable Work Structure）。

首次调度可延迟工作结构（Delayable Work Structure）前必须调用此函数。同一结构无需再次初始化。可以再次调用以更改关联的处理函数（Handler），但必须在工作项空闲（Idle）时进行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dwork` | 要初始化的可延迟工作结构（Delayable Work Structure）。 |
| `handler` | 工作项要调用的处理函数（Handler）。 |

<a id="ga0d1d2e1d2ba2e89a560a1bdc5365d9e0"></a>

### `k_work_is_pending()`

```c
bool k_work_is_pending ( const struct k_work * work)
```

声明属性：`inline`、`static`、`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

检查工作项（Work Item）当前是否处于待处理（Pending）状态。

用于判断工作项是否处于非空闲状态（Non-idle State）的封装函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 指向工作项（Work Item）的指针。 |

**说明（Note）**：注意：这是状态的即时快照（Live Snapshot），结果被检查前状态就可能变化。必要时使用锁（Locks）。

**返回（Returns）**：返回值：当且仅当 `k_work_busy_get()` 返回非零值时为 `true`。

<a id="ga2a19547d04dc1a202e80b752e3177215"></a>

### `k_work_poll_cancel()`

```c
int k_work_poll_cancel ( struct k_work_poll * work)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

取消触发式工作项（Triggered Work Item）。

此例程取消触发式工作项（Triggered Work Item）`work` 的提交。只有在尚无事件触发工作提交时，才可以取消触发式工作项。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 延迟工作项（Delayed Work Item）的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 工作项已取消（Canceled）。 |
| `-EINVAL` | 工作项正在处理，或已经完成。 |

<a id="ga371dab33a40622bea19b07d852863443"></a>

### `k_work_poll_init()`

```c
void k_work_poll_init ( struct k_work_poll * work, k_work_handler_t handler )
```

```c
#include <zephyr/kernel.h>
```

初始化触发式工作项（Triggered Work Item）。

此例程在首次使用前初始化工作队列的触发式工作项（Triggered Work Item）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 触发式工作项（Triggered Work Item）的地址。 |
| `handler` | 每次处理工作项（Work Item）时调用的函数。 |

<a id="gad9f222e46d72c4f98739395a0c8bb4ea"></a>

### `k_work_poll_submit()`

```c
int k_work_poll_submit ( struct k_work_poll * work, struct k_poll_event * events, int num_events, k_timeout_t timeout )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

将触发式工作项（Triggered Work Item）提交到系统工作队列（System Workqueue）。

此例程安排工作项 `work` 在给定事件之一被置为有信号状态时，由系统工作队列（System Workqueue）处理。它为工作项启动内部轮询器（Internal Poller），然后返回。只有受监视的事件之一实际发生时，工作项才真正提交到工作队列，并进入待处理状态（Pending）。

再次提交一个已经提交但仍在等待事件的触发式工作项，会取消原有提交，并使用新的事件列表重新调度（Reschedule）。注意：此行为本身会与原有触发式工作项及工作队列产生竞态条件（Race Conditions），因此必须谨慎地在外部同步这些重复提交。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 延迟工作项（Delayed Work Item）的地址。 |
| `events` | 用于触发工作项的事件数组（Event Array）。 |
| `num_events` | 数组中的事件数量。 |
| `timeout` | 超时时间（Timeout），到期后即使尚未被事件触发，也会调度工作项执行。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 工作项已开始监视事件（Events）。 |
| `-EINVAL` | 工作项正在处理，或已经完成。 |
| `-EADDRINUSE` | 工作项正在另一个工作队列（Workqueue）中待处理。 |

**警告（Warning）**：警告：工作队列完成处理该工作项之前，不得修改提供的事件数组（Event Array）或触发式工作项（Triggered Work Item）。

<a id="ga0abafd7f851e42fd3572c8438e600a53"></a>

### `k_work_poll_submit_to_queue()`

```c
int k_work_poll_submit_to_queue ( struct k_work_q * work_q, struct k_work_poll * work, struct k_poll_event * events, int num_events, k_timeout_t timeout )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

提交触发式工作项（Triggered Work Item）。

此例程安排工作项 `work` 在给定事件之一被置为有信号状态时，由工作队列 `work_q` 处理。它为工作项启动内部轮询器（Internal Poller），然后返回。只有受监视的事件之一实际发生时，工作项才真正提交到工作队列，并进入待处理状态（Pending）。

再次提交一个已经提交但仍在等待事件的触发式工作项，会取消原有提交，并使用新的事件列表重新调度（Reschedule）。注意：此行为本身会与原有触发式工作项及工作队列产生竞态条件（Race Conditions），因此必须谨慎地在外部同步这些重复提交。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work_q` | 工作队列（Workqueue）的地址。 |
| `work` | 延迟工作项（Delayed Work Item）的地址。 |
| `events` | 用于触发工作项的事件数组（Event Array）。 |
| `num_events` | 数组中的事件数量。 |
| `timeout` | 超时时间（Timeout），到期后即使尚未被事件触发，也会调度工作项执行。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 工作项已开始监视事件（Events）。 |
| `-EINVAL` | 工作项正在处理，或已经完成。 |
| `-EADDRINUSE` | 工作项正在另一个工作队列（Workqueue）中待处理。 |

**警告（Warning）**：警告：提供的事件数组和触发式工作项必须放在持续有效的内存（Persistent Memory）中，至少有效至工作处理函数执行或工作取消；提交后不得修改。

<a id="ga0fefe3e0225ac99b47b250849f6cd863"></a>

### `k_work_queue_drain()`

```c
int k_work_queue_drain ( struct k_work_q * queue, bool plug )
```

```c
#include <zephyr/kernel.h>
```

等待工作队列（Work Queue）排空，并可选择阻止其接受新提交（Plug）。

阻止向工作队列提交新的工作项，但来自队列自身线程的提交除外；同时阻塞调用者，直到队列中没有更多可用工作项。

如果 `plug` 为 `true`，排空（Drain）完成后仍会阻止提交，直到调用 `k_work_queue_unplug()`。

注意：处于延迟状态的工作项尚未与其工作队列关联。如果目标是确保工作队列保持为空，必须在外部取消这些工作项。可使用封堵（Plug）功能，防止延迟工作项在排空（Drain）完成后提交。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `queue` | 指向队列结构（Queue Structure）的指针。 |
| `plug` | 为 `true` 时，工作队列在所有工作项排空（Drained）后仍会阻止新的提交。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `1` | 本次调用必须等待排空（Drain）完成。 |
| `0` | 本次调用无需等待。 |
| `negative` | 等待被中断或失败。 |

<a id="gada77d818ea9e4d07c14a960872ed5492"></a>

### `k_work_queue_init()`

```c
void k_work_queue_init ( struct k_work_q * queue)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

初始化工作队列结构体（Work Queue Structure）。

首次启动工作队列结构（Work Queue Structure）前必须调用此函数。同一工作队列结构无需再次初始化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `queue` | 要初始化的队列结构（Queue Structure）。 |

<a id="gac7fc60238574769e4eae6a2cc38da87b"></a>

### `k_work_queue_run()`

```c
void k_work_queue_run ( struct k_work_q * queue, const struct k_work_queue_config * cfg )
```

```c
#include <zephyr/kernel.h>
```

使用调用线程（Calling Thread）运行工作队列（Work Queue）。

工作队列将持续运行，直到被 `k_work_queue_stop` 停止。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `queue` | 要运行的队列（Queue）。 |
| `cfg` | 可选的附加配置参数（Configuration Parameters）。不需要时传入 `NULL`，以使用 `k_work_queue_config` 文档说明的默认值。 |

<a id="gadfc56554f9bfe7b52309d79660188593"></a>

### `k_work_queue_start()`

```c
void k_work_queue_start ( struct k_work_q * queue, k_thread_stack_t * stack, size_t stack_size, int prio, const struct k_work_queue_config * cfg )
```

```c
#include <zephyr/kernel.h>
```

初始化工作队列（Work Queue）。

配置并启动工作队列线程（Work Queue Thread）。不应对同一个队列再次调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `queue` | 指向队列结构（Queue Structure）的指针。使用前必须在已清零的内存／BSS 中初始化，或通过 `k_work_queue_init` 初始化。 |
| `stack` | 指向工作线程栈区域（Work Thread Stack Area）的指针。 |
| `stack_size` | 工作线程栈区域（Work Thread Stack Area）的大小，单位为字节。 |
| `prio` | 初始线程优先级（Initial Thread Priority）。 |
| `cfg` | 可选的附加配置参数（Configuration Parameters）。不需要时传入 `NULL`，以使用 `k_work_queue_config` 文档说明的默认值。 |

<a id="ga1fd2fce94eb731ccb0838ec763e62f5c"></a>

### `k_work_queue_stop()`

```c
int k_work_queue_stop ( struct k_work_q * queue, k_timeout_t timeout )
```

```c
#include <zephyr/kernel.h>
```

停止工作队列（Work Queue）。

停止工作队列线程（Work Queue Thread），确保不再处理后续工作。此调用会阻塞；成功时保证工作队列线程已正常终止，之后不会再处理工作项。

必须先排空并封堵队列（Drain and Plug），例如调用启用 `plug` 选项的 `k_work_queue_drain()`；否则返回 `-EBUSY`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `queue` | 指向队列结构（Queue Structure）的指针。 |
| `timeout` | 等待工作队列停止的最长时间（Maximum Wait Time）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 工作队列已停止（Stopped）。 |
| `-EALREADY` | 工作队列未启动，或已经停止。 |
| `-EBUSY` | 工作队列尚未封堵（Plugged）。 |
| `-ETIMEDOUT` | 工作队列未在规定超时时间内停止。 |
| `-ENOTSUP` | 工作队列属于必要线程（Essential）队列。 |

<a id="ga0b8b496f7e7bd82d08590a07293e38d7"></a>

### `k_work_queue_thread_get()`

```c
k_tid_t k_work_queue_thread_get ( struct k_work_q * queue)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/kernel.h>
```

访问运行工作队列（Work Queue）的线程（Thread）。

需要此函数，以授予工作队列线程访问其将处理的工作项所需对象的权限。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `queue` | 指向队列结构（Queue Structure）的指针。 |

**返回（Returns）**：返回值：与工作队列关联的线程（Thread）。

<a id="gaa0463bb79af3ec470f7d3be02052139f"></a>

### `k_work_queue_unplug()`

```c
int k_work_queue_unplug ( struct k_work_q * queue)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

解除工作队列（Work Queue）的提交阻塞，使其接受新提交。

解除以启用 `plug` 选项调用 `k_work_queue_drain()` 时设置的新提交阻止状态。如果在排空（Drain）完成前调用此函数，则排空完成后立即允许提交新工作项。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `queue` | 指向队列结构（Queue Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功解除封堵（Unplugged）。 |
| `-EALREADY` | 工作队列原本未封堵（Plugged）。 |

<a id="gaacaab408fb7c848d466ad1f069dfa648"></a>

### `k_work_reschedule()`

```c
int k_work_reschedule ( struct k_work_delayable * dwork, k_timeout_t delay )
```

```c
#include <zephyr/kernel.h>
```

重新调度工作项（Work Item），使其延迟一段时间后提交到系统工作队列（System Work Queue）。

这是对 `k_work_reschedule_for_queue()` 的简单封装，具有该函数的全部 API 特性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dwork` | 指向可延迟工作项（Delayable Work Item）的指针。 |
| `delay` | 提交工作项前等待的时间（Delay）。 |

**返回（Returns）**：返回值：与 `k_work_reschedule_for_queue()` 相同。

<a id="gabf5db091eac19b19a4e12c0cb381f0a8"></a>

### `k_work_reschedule_for_queue()`

```c
int k_work_reschedule_for_queue ( struct k_work_q * queue, struct k_work_delayable * dwork, k_timeout_t delay )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

重新调度工作项（Work Item），使其延迟一段时间后提交到队列（Queue）。

与 `k_work_schedule_for_queue()` 不同，此函数可以更改已计划调度工作项的截止时间（Deadline），也可以调度处于任何状态的工作项，例如空闲、已提交或正在执行。此函数不影响已经提交到队列的工作项，即不会“撤回提交（Unsubmit）”。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `queue` | 延迟结束后应将工作项提交到的队列（Queue）。 |
| `dwork` | 指向可延迟工作项（Delayable Work Item）的指针。 |
| `delay` | 提交工作项前等待的时间。若为 `K_NO_WAIT`，则相当于先取消任何先前计划的提交，再调用 `k_work_submit_to_queue()`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | `delay` 为 `K_NO_WAIT`，且工作项已经在队列中。 |
| `1` | `delay` 为 `K_NO_WAIT`，工作项之前未提交但现在已加入 `queue`；或者 `delay` 不为 `K_NO_WAIT`，且工作项已计划调度。 |
| `2` | `delay` 为 `K_NO_WAIT`，工作项正在执行，并已再次排入当前执行它的队列。 |
| `-EBUSY` | `delay` 为 `K_NO_WAIT`，且 `k_work_submit_to_queue()` 以此错误码失败。 |
| `-EINVAL` | `delay` 为 `K_NO_WAIT`，且 `k_work_submit_to_queue()` 以此错误码失败。 |
| `-ENODEV` | `delay` 为 `K_NO_WAIT`，且 `k_work_submit_to_queue()` 以此错误码失败。 |

**说明（Note）**：注意：如果 `delay` 为 `K_NO_WAIT`，即无延迟（No Delay），则返回值与 `k_work_submit_to_queue()` 相同。

<a id="ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3"></a>

### `k_work_schedule()`

```c
int k_work_schedule ( struct k_work_delayable * dwork, k_timeout_t delay )
```

```c
#include <zephyr/kernel.h>
```

延迟一段时间后，将空闲工作项（Idle Work Item）提交到系统工作队列（System Work Queue）。

这是对 `k_work_schedule_for_queue()` 的简单封装，具有该函数的全部 API 特性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dwork` | 指向可延迟工作项（Delayable Work Item）的指针。 |
| `delay` | 提交工作项前等待的时间。若为 `K_NO_WAIT`，则相当于调用 `k_work_submit_to_queue()`。 |

**返回（Returns）**：返回值：与 `k_work_schedule_for_queue()` 相同。

<a id="ga17f863c9f6ff2fb41dc0f3b7de4fdf23"></a>

### `k_work_schedule_for_queue()`

```c
int k_work_schedule_for_queue ( struct k_work_q * queue, struct k_work_delayable * dwork, k_timeout_t delay )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

延迟一段时间后，将空闲工作项（Idle Work Item）提交到队列（Queue）。

与 `k_work_reschedule_for_queue()` 不同，如果工作项已经计划调度或已经提交，此函数不执行任何操作（No-op），即使 `delay` 为 `K_NO_WAIT` 也是如此。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `queue` | 延迟结束后应将工作项提交到的队列（Queue）。 |
| `dwork` | 指向可延迟工作项（Delayable Work Item）的指针。 |
| `delay` | 提交工作项前等待的时间。如果为 `K_NO_WAIT` 且工作项不处于待处理状态（Pending），则相当于调用 `k_work_submit_to_queue()`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 工作项已经计划调度或已经提交。 |
| `1` | 工作项已计划调度（Scheduled）。 |
| `2` | `delay` 为 `K_NO_WAIT`，工作项正在执行，并已再次排入当前执行它的队列。 |
| `-EBUSY` | `delay` 为 `K_NO_WAIT`，且 `k_work_submit_to_queue()` 以此错误码失败。 |
| `-EINVAL` | `delay` 为 `K_NO_WAIT`，且 `k_work_submit_to_queue()` 以此错误码失败。 |
| `-ENODEV` | `delay` 为 `K_NO_WAIT`，且 `k_work_submit_to_queue()` 以此错误码失败。 |

<a id="gace61b59575093d7442f39ccb7be686d7"></a>

### `k_work_submit()`

```c
int k_work_submit ( struct k_work * work)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

将工作项（Work Item）提交到系统队列（System Queue）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 指向工作项（Work Item）的指针。 |

**返回（Returns）**：返回值：与 `k_work_submit_to_queue()` 相同。

<a id="ga5353e76f73db070614f50d06d292d05c"></a>

### `k_work_submit_to_queue()`

```c
int k_work_submit_to_queue ( struct k_work_q * queue, struct k_work * work )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

将工作项（Work Item）提交到队列（Queue）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `queue` | 指向工作项应运行于其中的工作队列（Work Queue）的指针。若为 `NULL`，则使用最近一次提交时的队列。 |
| `work` | 指向工作项（Work Item）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 工作项已经提交到某个队列。 |
| `1` | 工作项之前未提交，现在已排入 `queue`。 |
| `2` | 工作项正在执行，并已再次排入当前执行它的队列。 |
| `-EBUSY` | 提交被拒绝，原因是工作项正在取消（Canceling）、队列正在排空（Draining），或队列已封堵（Plugged）。 |
| `-EINVAL` | `queue` 为 `NULL`，且工作项从未执行过。 |
| `-ENODEV` | `queue` 尚未启动。 |

<a id="ga9de9c7a7f13cc6b325e5453e34afe62d"></a>

### `k_work_user_init()`

```c
void k_work_user_init ( struct k_work_user * work, k_work_user_handler_t handler )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/kernel.h>
```

初始化用户空间工作项（Userspace Work Item）。

此例程在首次使用前初始化用户工作队列工作项（User Workqueue Work Item）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 工作项（Work Item）的地址。 |
| `handler` | 每次处理工作项（Work Item）时调用的函数。 |

<a id="ga58d05d4127e4cd51104a1f1a87f626cd"></a>

### `k_work_user_is_pending()`

```c
bool k_work_user_is_pending ( struct k_work_user * work)
```

声明属性：`inline`、`static`、`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

检查用户空间工作项（Userspace Work Item）是否处于待处理（Pending）状态。

此例程指示用户工作项 `work` 是否在工作队列中处于待处理状态（Pending）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work` | 工作项（Work Item）的地址。 |

**说明（Note）**：注意：检查工作项是否待处理，不能保证使用该信息时它仍然待处理。调用者负责确保安全地使用此信息。

**返回（Returns）**：返回值：工作项处于待处理状态（Pending）时为 `true`，否则为 `false`。

<a id="ga3091bc8fab5311252e41634a97a18589"></a>

### `k_work_user_queue_start()`

```c
void k_work_user_queue_start ( struct k_work_user_q * work_q, k_thread_stack_t * stack, size_t stack_size, int prio, const char * name )
```

```c
#include <zephyr/kernel.h>
```

在用户模式（User Mode）下启动工作队列（Workqueue）。

工作方式与 `k_work_queue_start()` 相同，但可从用户模式（User Mode）调用，且创建的工作线程也在用户模式运行。调用者必须获得 `work_q` 参数中的线程对象和队列对象的访问权限；优先级限制与 `k_thread_create()` 相同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work_q` | 工作队列（Workqueue）的地址。 |
| `stack` | 指向由 `K_THREAD_STACK_DEFINE()` 定义的工作队列线程栈空间（Stack Space）的指针。 |
| `stack_size` | 工作队列线程栈（Stack）的大小，单位为字节；应为传给 `K_THREAD_STACK_DEFINE()` 的同一常量，或 `K_THREAD_STACK_SIZEOF()` 的值。 |
| `prio` | 工作队列线程的优先级（Priority）。 |
| `name` | 可选的线程名称（Thread Name）。非空时，将其复制到线程的名称缓冲区。 |

<a id="gab487068e9564cd77b6bdbac3d5670923"></a>

### `k_work_user_queue_thread_get()`

```c
k_tid_t k_work_user_queue_thread_get ( struct k_work_user_q * work_q)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/kernel.h>
```

访问运行工作队列（Work Queue）的用户模式线程（User Mode Thread）。

需要此函数，以授予用户模式工作队列线程访问其将处理的工作项所需对象的权限。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work_q` | 指向用户模式队列结构（User Mode Queue Structure）的指针。 |

**返回（Returns）**：返回值：与工作队列关联的用户模式线程（User Mode Thread）。

<a id="ga50ae1f6f74c0bc0a41dbbf789fff8856"></a>

### `k_work_user_submit_to_queue()`

```c
int k_work_user_submit_to_queue ( struct k_work_user_q * work_q, struct k_work_user * work )
```

声明属性：`inline`、`static`、`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

将工作项（Work Item）提交到用户模式工作队列（User Mode Workqueue）。

将工作项提交到在用户模式（User Mode）运行的工作队列。此操作从调用者的资源池（Resource Pool）分配临时内存，工作线程取走该 `k_work` 项后释放。工作队列线程必须能够访问所提交 `k_work` 项的内存。调用者必须获得 `work_q` 参数中的队列对象的访问权限。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `work_q` | 工作队列（Workqueue）的地址。 |
| `work` | 工作项（Work Item）的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EBUSY` | 工作项已经位于某个工作队列中。 |
| `-ENOMEM` | 线程资源池（Thread Resource Pool）内存分配失败。 |
| `0` | 成功。 |


## 6.7\_原页交叉引用（Cross References）

- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)
- [k_work_queue_config](../kernel_runtime_model_reference/P011_k_work_queue_config_结构体.md)
- [k_work_q](../kernel_runtime_model_reference/P010_k_work_q_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [k_thread_stack_t](../api_file_host_video_reference/P001_zephyr__arch__arch_interface.h_文件参考.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)
- [k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)
- [k_poll_event](../eventpoll_reference/P004_轮询事件结构.md)
- [zephyr/kernel.h](../api_file_kernel_network_reference/P006_zephyr__kernel.h_文件参考.md)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [k_thread_create()](../thread_core_reference/P001_线程公共接口.md#gad5b0bff3102f1656089f5875d999a367)
- [K_THREAD_STACK_DEFINE()](../thread_stack_reference/P001_线程栈接口.md#gac5368ce24fdeab3863b5c8dee2ebd955)
- [K_THREAD_STACK_SIZEOF()](../thread_stack_reference/P001_线程栈接口.md#ga775f8e6b4144cfdd24f3261b6db64150)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructk__work_html"></a>
<a id="agroup__workqueue__apis_html_gaf8e003eefa5dd66ba883688f9d39c333"></a>
<a id="astructk__work__delayable_html"></a>
<a id="agroup__workqueue__apis_html_ga893b281f3d2bc0088650536899e17903"></a>
<a id="agroup__workqueue__apis_html_ga4f3eac1fc56d5c9c21a3afa9b964b0bf"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165"></a>
<a id="ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732"></a>
<a id="ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85"></a>
<a id="ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed"></a>
<a id="ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_应用网络上下文（Application network context）.md) · [返回大纲](大纲.md)
