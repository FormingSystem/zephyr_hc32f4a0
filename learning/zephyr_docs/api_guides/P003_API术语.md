---
id: learning.zephyr-docs.api-guides.api_terms
title: API术语
kind: reference
status: maintained
domains: [zephyr, api]
source_url: https://docs.zephyrproject.org/latest/develop/api/terminology.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_API术语

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/api/terminology.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML摘要见[来源记录](../SOURCES.md)。

以下词语可作为 **API标签（API Tag）**，简写函数允许的调用上下文、调用对当前线程状态的影响和其他行为特征。上下文包括线程、**中断服务程序（Interrupt Service Routine，ISR）**及内核初始化前阶段。

| 标签 | 简要含义 |
| --- | --- |
| `reschedule` | 执行函数可能到达重新调度点。 |
| `sleep` | 函数可能使调用线程休眠。 |
| `no-wait` | 某个参数能阻止调用线程尝试休眠。 |
| `isr-ok` | 在线程或中断上下文中调用均安全，并产生文档规定的效果。 |
| `pre-kernel-ok` | 内核完全初始化前即可安全调用，并产生规定效果。 |
| `async` | 函数可能在所发起操作完成前返回，即返回与操作完成异步发生。 |
| `supervisor` | 调用线程必须具备监督者权限。 |

## 3.1\_reschedule：重新调度

该属性表示函数执行可能到达**重新调度点（Reschedule Point）**，调度机制见[调度与CPU空闲](../kernel/P005_调度与CPU空闲.md)。

线程调用此类函数时，如果操作使更高优先级线程就绪，当前线程可能暂停执行。是否实际发生切换，取决于该调度点关联的操作，以及调用线程与就绪队列首个线程的相对优先级。

在**时间片轮转（Time Slicing）**或中断触发的重新调度点下，任何线程都可能在任意函数中暂停。因此，此属性不能理解为不带标签的代码绝不会被抢占。

原文给出以下调用规则：不带 `reschedule` 的函数可在线程或中断上下文调用；带 `reschedule` 的函数可在线程上下文调用；带 `reschedule` 但不带 `sleep` 的函数也可在中断上下文调用。

## 3.2\_sleep：可能休眠

该属性表示函数可能使调用线程**休眠（Sleep）**。对于仅使用不可抢占线程的应用尤其重要：内核不会仅因到达调度点就替换正在运行的协作线程，除非该线程明确执行了使自己休眠的操作。

`sleep` 不表示每次调用必然休眠，而是操作完成前可能要求调用线程挂起、等待或调用 `k_yield()`。此行为可能由 `no-wait` 参数路径控制。

- `sleep` 隐含 `reschedule`。
- `sleep` 函数可在线程上下文调用。
- 只有以 `no-wait` 模式调用时，`sleep` 函数才可用于中断和内核初始化前上下文。

`k_yield()` 的接口说明见[官方线程API](../thread_core_reference/P001_线程公共接口.md#ga08a3484c33444ecedc2d71d78495a295)。

## 3.3\_no-wait：不等待路径

此标签用于同样带 `sleep` 的函数，表示某个参数可强制选择不会让调用线程休眠的执行路径。

典型情况是接受超时参数的函数，可以传入 [`K_NO_WAIT`](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga3d9541cfe2e8395af66d186efa77362f)：若操作能立即完成就执行，否则返回错误，不通过休眠等待。

由于中断上下文不能休眠，这条不等待路径使 [`k_sem_take()`](../synchronization_reference/P008_信号量公共接口.md#gac71e2383c1920dddc45a561cacfef090) 等函数也能从ISR调用。**不等待并不保证同步完成**。只有参数选中这条路径，带该标签的函数才可以从中断及内核初始化前上下文调用。

## 3.4\_isr-ok：允许ISR调用

该标签表示从中断或线程上下文调用时，函数均按规定工作。

按原文的属性模型，不带 `sleep` 的函数本质上满足 `isr-ok`。带 `sleep` 的函数也可能满足它，但实现必须确保从中断调用时仍兑现文档行为。例如检测调用上下文，把可能休眠的操作交给线程，或者在文档中规定非线程上下文返回特定错误，通常为 `-EWOULDBLOCK`。

带 `no-wait` 的函数只有选择不等待路径时才可从中断安全调用；带 `isr-ok` 的函数则不一定需要提供 `no-wait` 路径。

> 译注：这是本页标签体系的通用解释；使用具体接口时仍须遵守它对参数、锁、生命周期和上下文的专门约束，不能仅凭“没有看到sleep标签”推定任意函数可在ISR调用。

## 3.5\_pre-kernel-ok：内核启动前可调用

该属性表示在内核主线程启动前调用，函数也能按文档工作。它与 `isr-ok` 类似，但面向可能在 `PRE_KERNEL_1`、`PRE_KERNEL_2` 初始化级别中使用的接口，例如通过 [`DEVICE_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac12521f4d900e8947aac45c1b228366d) 或 [`SYS_INIT()`](../device_reference/P005_系统初始化接口.md#gaf507cc0613add8113c41896bd631254f) 注册的初始化流程。

函数通常通过 [`k_is_pre_kernel()`](../thread_core_reference/P001_线程公共接口.md#gae74e5de996276df767b96d4b50fa47ea) 判断当前能否完成所需行为；许多情况下也检查 [`k_is_in_isr()`](../fatal_irq_reference/P007_中断服务接口.md#ga8482b0dd2283d12677a9ebe321667d16)，从而同时支持ISR调用。

## 3.6\_async：异步

若函数可能在所发起的操作完成前返回，它就是**异步（Asynchronous）**的。通常会通过回调或事件报告操作完成。

非异步函数就是**同步（Synchronous）**函数，返回时操作总已完成。因为多数函数是同步的，通常不专门用标签标识。

异步与**上下文切换（Context Switching）**是相互独立的属性。有些API通过回调报告完成，却可能在启动操作前，为等待所需资源而挂起线程，例如 [`spi_transceive_signal()`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface.html#ga41b8a541257c0d45575fdc4593417edc)。

若函数同时有 `no-wait` 与 `async`，选择不等待路径仅保证不休眠，并不改变操作是否在返回前完成。

## 3.7\_supervisor：监督者权限

该属性只与用户模式应用有关，表示函数不能从**用户模式（User Mode）**调用，调用线程必须具备**监督者权限（Supervisor Privileges）**。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：API概览](P002_API概览.md) · [本模块主线目录](../reading/api_guides.md) · [全部主线](../reading/README.md) · [下一篇：API生命周期](P004_API生命周期.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：API概览](P002_API概览.md) · [下一章：API生命周期](P004_API生命周期.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
