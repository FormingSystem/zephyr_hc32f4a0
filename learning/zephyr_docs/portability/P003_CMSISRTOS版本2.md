---
id: learning.zephyr-docs.portability.page-3
title: CMSISRTOS版本2
kind: reference
status: maintained
domains: [zephyr, portability, cmsis]
source_url: https://docs.zephyrproject.org/latest/services/portability/cmsis_rtos_v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_CMSISRTOS版本2

原文：[官方页面](https://docs.zephyrproject.org/latest/services/portability/cmsis_rtos_v2.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 3.1\_CMSIS-RTOS 第 2 版

Cortex-M 软件接口标准（Cortex-M Software Interface Standard，CMSIS）RTOS 是面向 Arm Cortex-M 处理器系列、与厂商无关的硬件抽象层，并定义通用工具接口。虽然最初仅面向 Arm Cortex-M 微控制器，也容易扩展到其他微控制器，从而成为通用接口。

更多 CMSIS RTOS v2 信息见 [CMSIS-RTOS2 官方文档](https://arm-software.github.io/CMSIS_6/latest/RTOS2/index.html)。

译注：此处保留原页对 CMSIS 的概括。本页重点是 Zephyr 的 CMSIS-RTOS2 兼容实现，其配置入口为 `CONFIG_CMSIS_RTOS_V2`。它不等于 CMSIS-Core 设备头文件，也不能仅凭标准头文件中存在声明，就认定全部接口与错误返回语义均已实现。

## 3.2\_Zephyr 实现不支持的功能（Features Not Supported）

### 3.2.1\_内核（Kernel）

原文列出以下不支持的接口：`osKernelGetState`、`osKernelSuspend`、`osKernelResume`、`osKernelInitialize` 和 `osKernelStart`。

### 3.2.2\_互斥量（Mutex）

- `osMutexPrioInherit`：默认支持优先级继承（Priority Inheritance），且不可配置，不能选择或取消此属性。
- `osMutexRecursive`：原文说明默认支持递归互斥量（Recursive Mutex）；如果未设置此属性，同一线程第二次尝试获取该互斥量时会报错。
- `osMutexRobust`：Zephyr 不支持健壮互斥量（Robust Mutex）属性。

译注——实现差异：本次核对的 `mutex.c` 对优先级继承属性和不支持的 `osMutexRobust` 使用断言检查；`osMutexAcquire()` 直接调用 Zephyr 的 `k_mutex_lock()`，未看到依据 `osMutexRecursive` 拒绝同一线程再次获取的分支。因此原页所述“未设置递归属性时第二次获取报错”不能当作该源码版本已经实现的保证。应结合实际兼容层版本验证所依赖的互斥行为。

## 3.3\_Zephyr 实现不支持的返回值（Return Values Not Supported）

下表完整保留原页逐项说明。“不支持”指该页列出的接口不会提供对应返回条件，不表示所有接口都没有这种返回码。

| 接口 | 原文列出的不支持返回值及含义 |
| --- | --- |
| `osKernelUnlock`、`osKernelLock`、`osKernelRestoreLock` | `osError`：未指定的错误（Unspecified Error）。 |
| `osSemaphoreDelete` | `osErrorResource`：参数 `semaphore_id` 指定的信号量处于无效状态。 |
| `osMutexDelete` | `osErrorResource`：参数 `mutex_id` 指定的互斥量处于无效状态。 |
| `osTimerDelete` | `osErrorResource`：参数 `timer_id` 指定的定时器处于无效状态。 |
| `osMessageQueueReset` | `osErrorResource`：参数 `msgq_id` 指定的消息队列处于无效状态。 |
| `osMessageQueueDelete` | `osErrorResource`：参数 `msgq_id` 指定的消息队列处于无效状态。 |
| `osMemoryPoolFree` | `osErrorResource`：参数 `mp_id` 指定的内存池处于无效状态。 |
| `osMemoryPoolDelete` | `osErrorResource`：参数 `mp_id` 指定的内存池处于无效状态。 |
| `osEventFlagsSet`、`osEventFlagsClear` | `osFlagsErrorUnknown`：未指定的错误；`osFlagsErrorResource`：参数 `ef_id` 指定的事件标志对象尚未准备好使用。 |
| `osEventFlagsDelete` | `osErrorParameter`：参数 `ef_id` 的值不正确。 |
| `osThreadFlagsSet` | `osFlagsErrorUnknown`：未指定的错误；`osFlagsErrorResource`：参数 `thread_id` 指定的线程未处于可接收标志的活动状态。 |
| `osThreadFlagsClear` | `osFlagsErrorResource`：正在运行的线程未处于可接收标志的活动状态。 |
| `osDelayUntil` | `osParameter`：无法处理给定时间。 |

术语：信号量为 Semaphore，定时器为 Timer，消息队列为 Message Queue，内存池为 Memory Pool，事件标志为 Event Flags，线程标志为 Thread Flags。

译注——时间接口纠错：最后一行的 `osParameter` 是原页写法；当前头文件定义的参数错误为 `osErrorParameter`。本次核对的 `kernel.c` 在 `osDelayUntil()` 中先计算目标 tick 与当前 tick 的无符号差值；差值为 0 或大于 `0x7FFFFFFF` 时会返回 `osErrorParameter`。因此不能依照原页这一行假定所有时间参数均被接受。这里保留原表并明确源码差异，没有修改兼容层实现。


译注核对来源：[subsys/portability/cmsis_rtos_v2/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/portability/cmsis_rtos_v2/Kconfig)、[subsys/portability/cmsis_rtos_v2/kernel.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/kernel.c)、[subsys/portability/cmsis_rtos_v2/mutex.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/mutex.c)、[include/zephyr/portability/cmsis_os2.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/portability/cmsis_os2.h)。

本仓库的[对应源码](../../../subsys/portability/cmsis_rtos_v2/Kconfig)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="cmsis-rtos-v2"></a>
<a id="id1"></a>
<a id="features-not-supported-in-zephyr-implementation"></a>
<a id="return-values-not-supported-in-the-zephyr-implementation"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CMSISRTOS版本1](P002_CMSISRTOS版本1.md) · [本模块主线目录](../reading/portability.md) · [全部主线](../reading/README.md) · [下一篇：POSIX文档入口](P010_POSIX文档入口.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P002_CMSISRTOS版本1.md) · [返回大纲](大纲.md) · [下一章](P004_CMSISRTOS1示例目录.md)

</details>

<!-- reading-navigation:end -->
