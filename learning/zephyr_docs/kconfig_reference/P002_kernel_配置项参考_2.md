---
id: learning.zephyr-docs.kconfig-reference.page-2
title: "内核（Kernel）配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第2章\_内核（Kernel）配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `kernel` 的 81 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_OBJ_CORE_TIMER"></a>

## 2.1 `CONFIG_OBJ_CORE_TIMER`

**提示（Prompt）**：将定时器（Timer）集成到对象核心框架。

**说明（Help）**

启用后，将定时器（Timer）集成到对象核心框架（Object Core Framework）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig.obj_core:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.obj_core#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对象核心框架（Object Core Framework）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_POLL"></a>

## 2.2 `CONFIG_POLL`

**提示（Prompt）**：异步 I/O 框架（Async I/O Framework）。

**说明（Help）**

异步通知框架（Asynchronous Notification Framework）。启用 `k_poll()` 和 `k_poll_signal_raise()` API。前者可同时等待多个事件，事件既可直接触发，也可由某些内核对象（信号量和 FIFO）变为可用来触发。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_USE_REALTEK_BEE_OS_INTERFACE
CONFIG_USE_REALTEK_BEE_OS_INTERFACE
CONFIG_SILABS_SIWX91X_NWP
CONFIG_ADC_ASYNC
CONFIG_CAN_SHELL
CONFIG_LORA
CONFIG_MSPI_ASYNC
CONFIG_SPI_ASYNC
CONFIG_ZVFS_POLL
CONFIG_BT_MESH
CONFIG_BT_CTLR_RX_POLL
CONFIG_ISOTP
CONFIG_NETWORKING
CONFIG_CMSIS_RTOS_V1
CONFIG_CMSIS_RTOS_V2
CONFIG_USB_DFU_CLASS
```

**定义位置（Location）**：[`kernel/Kconfig:628`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L628)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 其他内核对象选项（Other Kernel Object Options）。

**配置项引用（Symbol References）**：[`CONFIG_USE_REALTEK_BEE_OS_INTERFACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_REALTEK_BEE_OS_INTERFACE)、[`CONFIG_SILABS_SIWX91X_NWP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SIWX91X_NWP)、[`CONFIG_ADC_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_ASYNC)、[`CONFIG_CAN_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_SHELL)、[`CONFIG_LORA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA)、[`CONFIG_MSPI_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_ASYNC)、[`CONFIG_SPI_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_ASYNC)、[`CONFIG_ZVFS_POLL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_POLL)、[`CONFIG_BT_MESH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH)、[`CONFIG_BT_CTLR_RX_POLL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_RX_POLL)、[`CONFIG_ISOTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISOTP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_CMSIS_RTOS_V1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CMSIS_RTOS_V1)、[`CONFIG_CMSIS_RTOS_V2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CMSIS_RTOS_V2)、[`CONFIG_USB_DFU_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DFU_CLASS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_CTLR_RX_POLL`。

<a id="CONFIG_PRIORITY_CEILING"></a>

## 2.3 `CONFIG_PRIORITY_CEILING`

**提示（Prompt）**：优先级继承上限（Priority Inheritance Ceiling）。

**说明（Help）**

定义线程通过 `k_mutex` 优先级继承（Priority Inheritance）所能获得的最小优先级数值，也就是逻辑上的最高优先级。将它设为等于或低于空闲线程的优先级，会禁用 `k_mutex` 优先级继承算法。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
-128
```

**取值范围（Ranges）**

```text
[-128, 127]
```

**定义位置（Location）**：[`kernel/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

<a id="CONFIG_REQUIRES_STACK_CANARIES"></a>

## 2.4 `CONFIG_REQUIRES_STACK_CANARIES`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，表示需要软件栈保护（Software Stack Protection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_STACK_CANARIES
CONFIG_STACK_CANARIES_STRONG
CONFIG_STACK_CANARIES_ALL
CONFIG_STACK_CANARIES_EXPLICIT
```

**定义位置（Location）**：[`kernel/Kconfig:925`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L925)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 安全选项（Security Options）。

**配置项引用（Symbol References）**：[`CONFIG_STACK_CANARIES`](P002_kernel_配置项参考_2.md#CONFIG_STACK_CANARIES)、[`CONFIG_STACK_CANARIES_STRONG`](P002_kernel_配置项参考_2.md#CONFIG_STACK_CANARIES_STRONG)、[`CONFIG_STACK_CANARIES_ALL`](P002_kernel_配置项参考_2.md#CONFIG_STACK_CANARIES_ALL)、[`CONFIG_STACK_CANARIES_EXPLICIT`](P002_kernel_配置项参考_2.md#CONFIG_STACK_CANARIES_EXPLICIT)。

<a id="CONFIG_SCHED_ALGORITHM"></a>

## 2.5 `CONFIG_SCHED_ALGORITHM`

**提示（Prompt）**：调度器优先级队列算法（Scheduler Priority Queue Algorithm）。

**说明（Help）**

内核可选择多种就绪队列（Ready Queue）实现，在代码大小、运行时常数项开销，以及线程数量增加时的性能扩展性之间作出不同权衡。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
CONFIG_SCHED_SIMPLE
```

**可选项（Choices）**

```text
CONFIG_SCHED_SIMPLE
CONFIG_SCHED_SCALABLE
CONFIG_SCHED_MULTIQ
```

**定义位置（Location）**：[`kernel/Kconfig:271`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L271)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_SCHED_SIMPLE`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_SIMPLE)、[`CONFIG_SCHED_SCALABLE`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_SCALABLE)、[`CONFIG_SCHED_MULTIQ`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_MULTIQ)。

<a id="CONFIG_SCHED_CPU_MASK"></a>

## 2.6 `CONFIG_SCHED_CPU_MASK`

**提示（Prompt）**：CPU 掩码亲和性／绑定 API（CPU Mask Affinity/Pinning API）。

**说明（Help）**

设为 `true` 时，应用可使用 `k_thread_cpu_mask_*()` API，在对称多处理（SMP）模式下控制 CPU 亲和性掩码，将线程绑定到指定 CPU，或者禁止线程在给定 CPU 上运行。三个调度器后端都支持此 API，但考虑掩码的“最佳线程”搜索具有不同性能：

- `SCHED_SIMPLE`（默认）：运行队列为按优先级排序的链表。为当前 CPU 查找最佳可运行线程时，线性扫描到首个 `cpu_mask` 包含当前 CPU 的线程，复杂度相对于可运行线程数为 O(N)。由于链表按优先级排序，找到首个符合条件的线程即停止，因此实际开销与优先级更高、且被绑定到当前 CPU 之外的线程数量成正比。
- `SCHED_SCALABLE`：运行队列为按优先级排序的红黑树（Red/Black Tree）。考虑掩码的搜索按中序遍历，返回首个 `cpu_mask` 匹配的线程。最坏复杂度为 O(N)，但找到匹配线程即提前结束；通常只访问少量节点。若同时启用 `WAITQ_SCALABLE`，红黑树所需约 2 kB 附加代码由两者共享。
- `SCHED_MULTIQ`：运行队列是按优先级组织的双向链表数组，并配有非空优先级位图。搜索利用位图从最高到最低遍历非空优先级，复杂度为 O(P)，P 是实际使用的不同优先级数量；在每个级别内，扫描线程链表，寻找首个 `cpu_mask` 包含当前 CPU 的线程。受亲和性约束的线程较少时，搜索很快；极端情况下，许多相同高优先级线程都被绑定到其他 CPU，内部链表扫描则退化为 O(N)。注意，`SCHED_MULTIQ` 与 `SCHED_DEADLINE` 不兼容。

三种实现中的 `cpu_mask` 检查都会增加未启用本选项时不存在的开销，因此只有确实需要 CPU 亲和性时才应启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP
```

**被选择（Selected by）**

```text
CONFIG_ARC_VPX_COOPERATIVE_SHARING
```

**定义位置（Location）**：[`kernel/smp/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/smp/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对称多处理选项（SMP Options）。

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_ARC_VPX_COOPERATIVE_SHARING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_VPX_COOPERATIVE_SHARING)。

<a id="CONFIG_SCHED_CPU_MASK_PIN_ONLY"></a>

## 2.7 `CONFIG_SCHED_CPU_MASK_PIN_ONLY`

**提示（Prompt）**：仅允许绑定单个 CPU 的 CPU 掩码变体（Single-CPU Pinning Variant）。

**说明（Help）**

设为 `true` 时，启用 `SCHED_CPU_MASK` 的变体，每个线程只能指定一个 CPU。实际上，所有线程都有唯一“分配的”CPU，不再进行对称调度。通常这没有帮助，但某些应用精心设计了线程架构，希望自行决定如何将工作分配到 CPU。此时可以进行适度优化，例如为每个 CPU 使用独立运行队列以缩短链表。选择后，CPU 掩码成为线程的不可变属性，只能在线程启动之前修改。大多数应用不需要它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SCHED_CPU_MASK && CONFIG_SMP
```

**定义位置（Location）**：[`kernel/smp/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/smp/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对称多处理选项（SMP Options）。 → CPU 掩码亲和性／绑定 API（CPU Mask Affinity/Pinning API）。

**配置项引用（Symbol References）**：[`CONFIG_SCHED_CPU_MASK`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_CPU_MASK)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)。

<a id="CONFIG_SCHED_DEADLINE"></a>

## 2.8 `CONFIG_SCHED_DEADLINE`

**提示（Prompt）**：最早截止时间优先调度（Earliest-deadline-first Scheduling）。

**说明（Help）**

启用简单的最早截止时间优先（Earliest Deadline First）调度模式，线程可按 `k_cycle_get_32()` 的单位设置截止时间差值。注意，只有在同一优先级内部，才按最早到期的截止时间决定下一个线程，而不是简单选择最早加入的线程。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_MPIPE_WORKQUEUE
```

**定义位置（Location）**：[`kernel/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_WORKQUEUE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_WORKQUEUE)。

<a id="CONFIG_SCHED_IPI_CASCADE"></a>

## 2.9 `CONFIG_SCHED_IPI_CASCADE`

**提示（Prompt）**：使用级联处理器间中断纠正局部调度（Cascading IPIs）。

**说明（Help）**

局部线程指其 CPU 掩码将执行范围限制为全部 CPU 的一个子集。如果一个线程被局部线程抢占，且被抢占线程的优先级高于另一 CPU 上正在执行的线程，就可能触发额外的处理器间中断（IPI）。这些级联 IPI 可确保系统最终运行一组有效的高优先级线程，但会付出性能代价。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SCHED_CPU_MASK && !CONFIG_SCHED_CPU_MASK_PIN_ONLY && CONFIG_SMP
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`kernel/smp/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/smp/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对称多处理选项（SMP Options）。

**配置项引用（Symbol References）**：[`CONFIG_SCHED_CPU_MASK`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_CPU_MASK)、[`CONFIG_SCHED_CPU_MASK_PIN_ONLY`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_CPU_MASK_PIN_ONLY)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)。

<a id="CONFIG_SCHED_IPI_SUPPORTED"></a>

## 2.10 `CONFIG_SCHED_IPI_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果架构支持调用 `arch_sched_broadcast_ipi()` 广播中断，使系统其他 CPU 调用 `z_sched_ipi()`，则本选项为 `true`。这使 `k_thread_abort()` 能以合理延迟完成；否则可能必须等待另一个线程遇到中断，而该时刻可能非常遥远。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_ESP32
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
CONFIG_SOC_CAVSV25
CONFIG_SOC_PIC64GX1000
CONFIG_SOC_POLARFIRE
CONFIG_SOC_CV32A6
CONFIG_SOC_CV64A6
CONFIG_ARC_CONNECT
CONFIG_AARCH32_ARMV8_A
CONFIG_AARCH32_ARMV8_R
CONFIG_CPU_CORTEX_A
CONFIG_ARMV8_R
CONFIG_X86_64
CONFIG_RISCV
```

**定义位置（Location）**：[`kernel/smp/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/smp/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对称多处理选项（SMP Options）。

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)、[`CONFIG_SOC_CAVSV25`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CAVSV25)、[`CONFIG_SOC_PIC64GX1000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC64GX1000)、[`CONFIG_SOC_POLARFIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_POLARFIRE)、[`CONFIG_SOC_CV32A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV32A6)、[`CONFIG_SOC_CV64A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV64A6)、[`CONFIG_ARC_CONNECT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_CONNECT)、[`CONFIG_AARCH32_ARMV8_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AARCH32_ARMV8_A)、[`CONFIG_AARCH32_ARMV8_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AARCH32_ARMV8_R)、[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_ARMV8_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV8_R)、[`CONFIG_X86_64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_64)、[`CONFIG_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_PIC64GX1000`。

<a id="CONFIG_SCHED_MULTIQ"></a>

## 2.11 `CONFIG_SCHED_MULTIQ`

**提示（Prompt）**：传统多队列就绪队列（Traditional Multi-queue Ready Queue）。

**说明（Help）**

选择后，调度器就绪队列使用经典教材式的链表数组，每个优先级一个链表，对应 Zephyr 1.12 之前的调度算法。相比“简单”调度器，代码大小仅有极少增加，几乎所有情况下都以常数因子很小的 O(1) 时间运行。但保存链表头需要较多 RAM，并且功能受限，不兼容需要更细粒度线程排序的截止时间调度等功能。可运行线程较少的典型应用通常应选择简单调度器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SCHED_DEADLINE && <choice CONFIG_SCHED_ALGORITHM>
```

**定义位置（Location）**：[`kernel/Kconfig:305`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L305)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 调度器优先级队列算法（Scheduler Priority Queue Algorithm）。

**配置项引用（Symbol References）**：[`CONFIG_SCHED_DEADLINE`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_DEADLINE)、[`CONFIG_SCHED_ALGORITHM`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_ALGORITHM)。

<a id="CONFIG_SCHED_SCALABLE"></a>

## 2.12 `CONFIG_SCHED_SCALABLE`

**提示（Prompt）**：红黑树就绪队列（Red/Black Tree Ready Queue）。

**说明（Help）**

选择后，调度器就绪队列使用红黑树（Red/Black Tree）实现。插入与移除操作的常数项开销较大，多数未在其他地方使用红黑树的平台还需要额外约 2 kB 代码。但它可以平稳高效地扩展到数千线程。适用于某一时刻可能有许多线程被标记为可运行的平台，粗略地说超过约 20 个。大多数应用不需要它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SCHED_ALGORITHM>
```

**定义位置（Location）**：[`kernel/Kconfig:292`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L292)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 调度器优先级队列算法（Scheduler Priority Queue Algorithm）。

**配置项引用（Symbol References）**：[`CONFIG_SCHED_ALGORITHM`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_ALGORITHM)。

<a id="CONFIG_SCHED_SIMPLE"></a>

## 2.13 `CONFIG_SCHED_SIMPLE`

**提示（Prompt）**：简单链表就绪队列（Simple Linked-list Ready Queue）。

**说明（Help）**

选择后，调度器就绪队列使用简单无序链表实现，只有单个线程时可获得非常快的常数时间性能，代码量也很小。适用于代码空间受限，且任何时刻队列中可运行线程都只有少量、例如约 3 个的系统。对多数未在其他地方使用红黑树的平台，可节省约 2 kB 代码。译注：本项原文称“unordered list”，而 CPU 掩码选项说明称 `SCHED_SIMPLE` 使用排序链表；两处分别保留原文表述。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SCHED_ALGORITHM>
```

**定义位置（Location）**：[`kernel/Kconfig:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L280)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 调度器优先级队列算法（Scheduler Priority Queue Algorithm）。

**配置项引用（Symbol References）**：[`CONFIG_SCHED_ALGORITHM`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_ALGORITHM)。

<a id="CONFIG_SCHED_THREAD_USAGE"></a>

## 2.14 `CONFIG_SCHED_THREAD_USAGE`

**提示（Prompt）**：收集线程运行时间用量（Thread Runtime Usage）。

**说明（Help）**

在上下文切换时收集线程运行时间信息（Thread Runtime Info）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_RUNTIME_STATS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_INSTRUMENT_THREAD_SWITCHING if !CONFIG_USE_SWITCH
```

**被选择（Selected by）**

```text
CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS
CONFIG_POSIX_MULTI_PROCESS
```

**定义位置（Location）**：[`kernel/Kconfig:460`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L460)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。 → 线程运行时间统计（Thread Runtime Statistics）。

**配置项引用（Symbol References）**：[`CONFIG_THREAD_RUNTIME_STATS`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_RUNTIME_STATS)、[`CONFIG_INSTRUMENT_THREAD_SWITCHING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENT_THREAD_SWITCHING)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)、[`CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS)、[`CONFIG_POSIX_MULTI_PROCESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MULTI_PROCESS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_INSTRUMENT_THREAD_SWITCHING`。

<a id="CONFIG_SCHED_THREAD_USAGE_ALL"></a>

## 2.15 `CONFIG_SCHED_THREAD_USAGE_ALL`

**提示（Prompt）**：收集系统总运行时间用量（Total System Runtime Usage）。

**说明（Help）**

累计所有非空闲线程使用的周期数（Cycle Usage）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SCHED_THREAD_USAGE && CONFIG_THREAD_RUNTIME_STATS
```

**默认值（Defaults）**

```text
y if CONFIG_SCHED_THREAD_USAGE
```

**被选择（Selected by）**

```text
CONFIG_OBJ_CORE_STATS_SYSTEM
CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS
```

**定义位置（Location）**：[`kernel/Kconfig:478`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L478)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。 → 线程运行时间统计（Thread Runtime Statistics）。 → 收集线程运行时间用量（Thread Runtime Usage）。

**配置项引用（Symbol References）**：[`CONFIG_SCHED_THREAD_USAGE`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_THREAD_USAGE)、[`CONFIG_THREAD_RUNTIME_STATS`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_RUNTIME_STATS)、[`CONFIG_OBJ_CORE_STATS_SYSTEM`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE_STATS_SYSTEM)、[`CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS)。

<a id="CONFIG_SCHED_THREAD_USAGE_ANALYSIS"></a>

## 2.16 `CONFIG_SCHED_THREAD_USAGE_ANALYSIS`

**提示（Prompt）**：分析已收集的线程运行时间用量统计。

**说明（Help）**

为分析目的收集与线程调度相关的附加计时信息，包括线程被调度运行的总时间、单次最长运行时间等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SCHED_THREAD_USAGE && CONFIG_THREAD_RUNTIME_STATS
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_INSTRUMENT_THREAD_SWITCHING if !CONFIG_USE_SWITCH
```

**定义位置（Location）**：[`kernel/Kconfig:467`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L467)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。 → 线程运行时间统计（Thread Runtime Statistics）。 → 收集线程运行时间用量（Thread Runtime Usage）。

**配置项引用（Symbol References）**：[`CONFIG_SCHED_THREAD_USAGE`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_THREAD_USAGE)、[`CONFIG_THREAD_RUNTIME_STATS`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_RUNTIME_STATS)、[`CONFIG_INSTRUMENT_THREAD_SWITCHING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENT_THREAD_SWITCHING)、[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_INSTRUMENT_THREAD_SWITCHING`。

<a id="CONFIG_SCHED_THREAD_USAGE_AUTO_ENABLE"></a>

## 2.17 `CONFIG_SCHED_THREAD_USAGE_AUTO_ENABLE`

**提示（Prompt）**：自动启用运行时间用量统计（Runtime Usage Statistics）。

**说明（Help）**

设置后，自动启用线程和 CPU 用量统计信息的收集。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SCHED_THREAD_USAGE && CONFIG_THREAD_RUNTIME_STATS
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS
```

**定义位置（Location）**：[`kernel/Kconfig:485`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L485)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。 → 线程运行时间统计（Thread Runtime Statistics）。 → 收集线程运行时间用量（Thread Runtime Usage）。

**配置项引用（Symbol References）**：[`CONFIG_SCHED_THREAD_USAGE`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_THREAD_USAGE)、[`CONFIG_THREAD_RUNTIME_STATS`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_RUNTIME_STATS)、[`CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS)。

<a id="CONFIG_SEM_LOCK_STRIPES"></a>

## 2.18 `CONFIG_SEM_LOCK_STRIPES`

**提示（Prompt）**：信号量自旋锁条带数量（Semaphore Spinlock Stripes）。

**说明（Help）**

用于同步信号量操作的自旋锁（Spinlock）数量，必须是 2 的幂。默认使用一个系统范围的锁，以保持现有信号量行为和内存占用。非 SMP 系统始终只使用一个锁。增加条带（Stripe）可减少 SMP 系统上的串行化和哈希冲突，代价是更多静态内存。各条带并不独立按缓存行对齐；自旋锁为 4 字节、缓存行为 64 字节时，16 个条带可位于同一缓存行。将数量增加到 16 以上，还能减少缓存行竞争。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`kernel/Kconfig:353`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L353)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

<a id="CONFIG_SKIP_BSS_CLEAR"></a>

## 2.19 `CONFIG_SKIP_BSS_CLEAR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

本选项禁用 Zephyr 初始化期间由软件对 `.bss` 节清零。对于已由外部机制清零 `.bss` 的平台，可使用此启动优化。注意，启用后，所有可能场景下（例如软件复位）的 `.bss` 清零责任都交给外部软件或硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ARCH_POSIX
```

**定义位置（Location）**：[`kernel/Kconfig:404`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L404)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_POSIX)。

<a id="CONFIG_SMP"></a>

## 2.20 `CONFIG_SMP`

**提示（Prompt）**：对称多处理支持（Symmetric Multiprocessing，SMP）。

**说明（Help）**

设为 `true` 时，内核带有对称多处理（SMP）支持，允许多个 CPU 同时调度 Zephyr 任务。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SWITCH
```

**定义位置（Location）**：[`kernel/smp/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/smp/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对称多处理选项（SMP Options）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SWITCH`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH)。

<a id="CONFIG_SOC_EARLY_INIT_HOOK"></a>

## 2.21 `CONFIG_SOC_EARLY_INIT_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

运行早期片上系统初始化钩子（Early SoC Initialization Hook）。在内核和设备初始化之前执行自定义钩子 `soc_early_init_hook()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
CONFIG_SOC_NEORV32_READ_FREQUENCY_AT_RUNTIME
CONFIG_SOC_SERIES_KB106X
CONFIG_SOC_SERIES_PSOC4000T
CONFIG_SOC_SERIES_PSOC4100SMAX
CONFIG_SOC_SERIES_PSOC4100TP
CONFIG_SOC_R8A78000_R52
CONFIG_SOC_CH32H417_BOOT_V5F
CONFIG_SOC_FT9001
CONFIG_SOC_ARC_IOT
CONFIG_SOC_SERIES_LPC51U68
CONFIG_SOC_SR100
CONFIG_SOC_SERIES_MEC15XX
CONFIG_SOC_SERIES_MEC172X
CONFIG_SOC_EOS_S3
CONFIG_SOC_BCM58402_M7
CONFIG_SOC_BCM58402_A72
CONFIG_SOC_KB1200
CONFIG_SOC_FAMILY_RENESAS_RA
CONFIG_SOC_SERIES_RA0E1
CONFIG_SOC_FAMILY_MCXC
CONFIG_SOC_SERIES_MCXE31X
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_SERIES_AM62LX_A53
CONFIG_SOC_SERIES_AM62X_A53
CONFIG_SOC_SERIES_AM62X_M4
CONFIG_SOC_SERIES_AM64X_M4
CONFIG_SOC_SERIES_AM64X_R5
CONFIG_SOC_SERIES_J721E_R5
CONFIG_SOC_SERIES_J722S_R5
CONFIG_SOC_FAMILY_SILABS_S0
CONFIG_SOC_FAMILY_SILABS_S1
CONFIG_SOC_FAMILY_SILABS_S2
CONFIG_SOC_FAMILY_SILABS_S3
CONFIG_SOC_SERIES_SIM3U
CONFIG_SOC_SERIES_SIWG917
CONFIG_SOC_SERIES_IMXRT10XX
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT266X
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MIMXRT685S_HIFI4
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_MIMXRT798S_HIFI4
CONFIG_SOC_SERIES_M55M1X
CONFIG_SOC_SERIES_K2X
CONFIG_SOC_SERIES_K32LX
CONFIG_SOC_SERIES_K6X
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_SERIES_KE1XF
CONFIG_SOC_SERIES_KE1XZ
CONFIG_SOC_SERIES_KL2X
CONFIG_SOC_SERIES_KV5X
CONFIG_SOC_SERIES_KWX
CONFIG_SOC_SERIES_SF32LB52X
CONFIG_SOC_EMSK
CONFIG_SOC_EMSK_EM7D
CONFIG_SOC_EMSK_EM9D
CONFIG_SOC_EMSK_EM11D
CONFIG_SOC_SERIES_NRF52
CONFIG_SOC_SERIES_NRF53
CONFIG_SOC_SERIES_NRF54H
CONFIG_SOC_SERIES_NRF91
CONFIG_SOC_SERIES_NRF92
CONFIG_SOC_OPENTITAN
CONFIG_SOC_SERIES_TM4C123X
CONFIG_SOC_FAMILY_REALTEK_AMEBA
CONFIG_SOC_FAMILY_PSOC6
CONFIG_SOC_FAMILY_PSOC6_LEGACY
CONFIG_SOC_SERIES_IMX6SX
CONFIG_SOC_SERIES_IMX7D
CONFIG_SOC_MIMX8MM6_M4
CONFIG_SOC_MIMX8ML8_M7
CONFIG_SOC_MIMX9352_M33
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_MIMX94398_M7_0
CONFIG_SOC_MIMX94398_M7_1
CONFIG_SOC_MIMX9596_M7
CONFIG_SOC_MIMX9529_M7
CONFIG_SOC_SERIES_PSE84
CONFIG_SOC_CYT4DNJBZS_M7_0
CONFIG_SOC_CYT4DNJBZS_M7_1
CONFIG_SOC_SERIES_CYW20829
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_SERIES_GD32A50X
CONFIG_SOC_SERIES_GD32C2X1
CONFIG_SOC_SERIES_GD32E10X
CONFIG_SOC_SERIES_GD32E50X
CONFIG_SOC_SERIES_GD32F3X0
CONFIG_SOC_SERIES_GD32F403
CONFIG_SOC_SERIES_GD32F4XX
CONFIG_SOC_SERIES_GD32L23X
CONFIG_SOC_SERIES_GD32VF103
CONFIG_SOC_SERIES_CC13X2_CC26X2
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
CONFIG_SOC_SERIES_CC32XX
CONFIG_SOC_SERIES_MSP432P4XX
CONFIG_SOC_XILINX_ZYNQMP_RPU
CONFIG_SOC_SERIES_AE350
CONFIG_SOC_SERIES_TLSR951X
CONFIG_SOC_SERIES_APOLLO2X
CONFIG_SOC_SERIES_APOLLO3X
CONFIG_SOC_SERIES_APOLLO4X
CONFIG_SOC_SERIES_APOLLO5X
CONFIG_SOC_VERSAL_RPU
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_SERIES_RZA3M
CONFIG_SOC_SERIES_RZA3UL
CONFIG_SOC_SERIES_RZG2L
CONFIG_SOC_SERIES_RZG2UL
CONFIG_SOC_SERIES_RZG3E
CONFIG_SOC_SERIES_RZG3S
CONFIG_SOC_SERIES_RZN2H
CONFIG_SOC_SERIES_RZN2L
CONFIG_SOC_SERIES_RZT2H
CONFIG_SOC_SERIES_RZT2L
CONFIG_SOC_SERIES_RZT2M
CONFIG_SOC_R9A09G057H44GBG_CM33
CONFIG_SOC_R9A09G057H44GBG_CR8
CONFIG_SOC_SERIES_RZV2L
CONFIG_SOC_SERIES_RZV2N
CONFIG_SOC_SERIES_RX130
CONFIG_SOC_SERIES_RX140
CONFIG_SOC_SERIES_RX14T
CONFIG_SOC_SERIES_RX261
CONFIG_SOC_SERIES_RX26T
CONFIG_SOC_SERIES_RX74M
CONFIG_SOC_SERIES_RX74N
CONFIG_SOC_FAMILY_INTEL_ISH
CONFIG_SOC_OPENISA_RV32M1
CONFIG_SOC_SERIES_SAMX7X
CONFIG_SOC_SERIES_SMARTFUSION2
CONFIG_SOC_AMD_VERSALNET_RPU
CONFIG_SOC_SERIES_SY1XX
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_SOC_FAMILY_MAX32
CONFIG_SOC_RTS5817
CONFIG_SOC_SERIES_MSPM0G
CONFIG_SOC_SERIES_MSPM0L
CONFIG_SOC_AMD_VERSAL2_RPU
CONFIG_SOC_EGIS_ET171
CONFIG_SOC_SERIES_RTS5912
CONFIG_SOC_SERIES_STM32C0X
CONFIG_SOC_SERIES_STM32C5X
CONFIG_SOC_SERIES_STM32F0X
CONFIG_SOC_SERIES_STM32F1X
CONFIG_SOC_SERIES_STM32F2X
CONFIG_SOC_SERIES_STM32F3X
CONFIG_SOC_SERIES_STM32F4X
CONFIG_SOC_SERIES_STM32F7X
CONFIG_SOC_SERIES_STM32G0X
CONFIG_SOC_SERIES_STM32G4X
CONFIG_SOC_SERIES_STM32H5X
CONFIG_SOC_SERIES_STM32H7RSX
CONFIG_SOC_SERIES_STM32H7X
CONFIG_SOC_SERIES_STM32L0X
CONFIG_SOC_SERIES_STM32L1X
CONFIG_SOC_SERIES_STM32L4X
CONFIG_SOC_SERIES_STM32L5X
CONFIG_SOC_SERIES_STM32MP13X
CONFIG_SOC_SERIES_STM32MP1X
CONFIG_SOC_STM32MP2X_M33
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_SERIES_STM32U0X
CONFIG_SOC_SERIES_STM32U3X
CONFIG_SOC_SERIES_STM32U5X
CONFIG_SOC_SERIES_STM32WB0X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_SERIES_STM32WBX
CONFIG_SOC_SERIES_STM32WL3X
CONFIG_SOC_SERIES_STM32WLX
CONFIG_SOC_SERIES_BEETLE
CONFIG_SOC_SERIES_NPCK3
CONFIG_SOC_SERIES_NPCX4
CONFIG_SOC_SERIES_NPCX7
CONFIG_SOC_SERIES_NPCX9
CONFIG_SOC_SERIES_RW6XX
CONFIG_SOC_SERIES_CYCLONEV
CONFIG_SOC_SERIES_S32K1
CONFIG_SOC_SERIES_S32K3
CONFIG_SOC_SERIES_S32K5
CONFIG_SOC_SERIES_S32ZE
CONFIG_SOC_SERIES_FE300
CONFIG_SOC_SERIES_FU500
CONFIG_SOC_SERIES_FU700
```

**定义位置（Location）**：[`kernel/Kconfig.init:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.init#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 平台钩子（Platform Hooks）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_SOC_NEORV32_READ_FREQUENCY_AT_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NEORV32_READ_FREQUENCY_AT_RUNTIME)、[`CONFIG_SOC_SERIES_KB106X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KB106X)、[`CONFIG_SOC_SERIES_PSOC4000T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4000T)、[`CONFIG_SOC_SERIES_PSOC4100SMAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100SMAX)、[`CONFIG_SOC_SERIES_PSOC4100TP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100TP)、[`CONFIG_SOC_R8A78000_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_R52)、[`CONFIG_SOC_CH32H417_BOOT_V5F`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CH32H417_BOOT_V5F)、[`CONFIG_SOC_FT9001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FT9001)、[`CONFIG_SOC_ARC_IOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_IOT)、[`CONFIG_SOC_SERIES_LPC51U68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC51U68)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_SOC_SERIES_MEC15XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC15XX)、[`CONFIG_SOC_SERIES_MEC172X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC172X)、[`CONFIG_SOC_EOS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EOS_S3)、[`CONFIG_SOC_BCM58402_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM58402_M7)、[`CONFIG_SOC_BCM58402_A72`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM58402_A72)、[`CONFIG_SOC_KB1200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_KB1200)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_SERIES_RA0E1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA0E1)、[`CONFIG_SOC_FAMILY_MCXC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXC)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_SERIES_AM62LX_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62LX_A53)、[`CONFIG_SOC_SERIES_AM62X_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_A53)、[`CONFIG_SOC_SERIES_AM62X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_M4)、[`CONFIG_SOC_SERIES_AM64X_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_M4)、[`CONFIG_SOC_SERIES_AM64X_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_R5)、[`CONFIG_SOC_SERIES_J721E_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J721E_R5)、[`CONFIG_SOC_SERIES_J722S_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J722S_R5)、[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_SOC_SERIES_SIM3U`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SIM3U)、[`CONFIG_SOC_SERIES_SIWG917`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SIWG917)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT266X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT685S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_HIFI4)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT798S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_HIFI4)、[`CONFIG_SOC_SERIES_M55M1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M55M1X)、[`CONFIG_SOC_SERIES_K2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K2X)、[`CONFIG_SOC_SERIES_K32LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K32LX)、[`CONFIG_SOC_SERIES_K6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K6X)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_SERIES_KE1XZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XZ)、[`CONFIG_SOC_SERIES_KL2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KL2X)、[`CONFIG_SOC_SERIES_KV5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KV5X)、[`CONFIG_SOC_SERIES_KWX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KWX)、[`CONFIG_SOC_SERIES_SF32LB52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SF32LB52X)、[`CONFIG_SOC_EMSK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSK)、[`CONFIG_SOC_EMSK_EM7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSK_EM7D)、[`CONFIG_SOC_EMSK_EM9D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSK_EM9D)、[`CONFIG_SOC_EMSK_EM11D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EMSK_EM11D)、[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_SERIES_NRF53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_SERIES_NRF54H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54H)、[`CONFIG_SOC_SERIES_NRF91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_SERIES_NRF92`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF92)、[`CONFIG_SOC_OPENTITAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENTITAN)、[`CONFIG_SOC_SERIES_TM4C123X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TM4C123X)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_SOC_FAMILY_PSOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_SERIES_IMX6SX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX6SX)、[`CONFIG_SOC_SERIES_IMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX7D)、[`CONFIG_SOC_MIMX8MM6_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6_M4)、[`CONFIG_SOC_MIMX8ML8_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_M7)、[`CONFIG_SOC_MIMX9352_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_M33)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_MIMX94398_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_SOC_MIMX9596_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_M7)、[`CONFIG_SOC_MIMX9529_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_M7)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_SOC_CYT4DNJBZS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_0)、[`CONFIG_SOC_CYT4DNJBZS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_1)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_SERIES_GD32A50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32A50X)、[`CONFIG_SOC_SERIES_GD32C2X1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32C2X1)、[`CONFIG_SOC_SERIES_GD32E10X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E10X)、[`CONFIG_SOC_SERIES_GD32E50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32E50X)、[`CONFIG_SOC_SERIES_GD32F3X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F3X0)、[`CONFIG_SOC_SERIES_GD32F403`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F403)、[`CONFIG_SOC_SERIES_GD32F4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32F4XX)、[`CONFIG_SOC_SERIES_GD32L23X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32L23X)、[`CONFIG_SOC_SERIES_GD32VF103`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32VF103)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_SERIES_CC32XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC32XX)、[`CONFIG_SOC_SERIES_MSP432P4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSP432P4XX)、[`CONFIG_SOC_XILINX_ZYNQMP_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_RPU)、[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)、[`CONFIG_SOC_SERIES_TLSR951X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TLSR951X)、[`CONFIG_SOC_SERIES_APOLLO2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO2X)、[`CONFIG_SOC_SERIES_APOLLO3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_SOC_SERIES_APOLLO4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO4X)、[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_SOC_VERSAL_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_RPU)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_RZA3M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3M)、[`CONFIG_SOC_SERIES_RZA3UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3UL)、[`CONFIG_SOC_SERIES_RZG2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2L)、[`CONFIG_SOC_SERIES_RZG2UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2UL)、[`CONFIG_SOC_SERIES_RZG3E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3E)、[`CONFIG_SOC_SERIES_RZG3S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3S)、[`CONFIG_SOC_SERIES_RZN2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2H)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_SOC_SERIES_RZT2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2H)、[`CONFIG_SOC_SERIES_RZT2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2L)、[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_R9A09G057H44GBG_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CM33)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)、[`CONFIG_SOC_SERIES_RZV2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2L)、[`CONFIG_SOC_SERIES_RZV2N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2N)、[`CONFIG_SOC_SERIES_RX130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX130)、[`CONFIG_SOC_SERIES_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX140)、[`CONFIG_SOC_SERIES_RX14T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX14T)、[`CONFIG_SOC_SERIES_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX261)、[`CONFIG_SOC_SERIES_RX26T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX26T)、[`CONFIG_SOC_SERIES_RX74M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74M)、[`CONFIG_SOC_SERIES_RX74N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX74N)、[`CONFIG_SOC_FAMILY_INTEL_ISH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ISH)、[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_SERIES_SMARTFUSION2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SMARTFUSION2)、[`CONFIG_SOC_AMD_VERSALNET_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_RPU)、[`CONFIG_SOC_SERIES_SY1XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SY1XX)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_SOC_RTS5817`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5817)、[`CONFIG_SOC_SERIES_MSPM0G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0G)、[`CONFIG_SOC_SERIES_MSPM0L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0L)、[`CONFIG_SOC_AMD_VERSAL2_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_RPU)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)、[`CONFIG_SOC_SERIES_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SOC_SERIES_STM32C0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C0X)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32F0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F0X)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F2X)、[`CONFIG_SOC_SERIES_STM32F3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F3X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32G0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G0X)、[`CONFIG_SOC_SERIES_STM32G4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G4X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32L0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L0X)、[`CONFIG_SOC_SERIES_STM32L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L1X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)、[`CONFIG_SOC_SERIES_STM32MP1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP1X)、[`CONFIG_SOC_STM32MP2X_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32MP2X_M33)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_SERIES_STM32U0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U0X)、[`CONFIG_SOC_SERIES_STM32U3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U3X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_SERIES_STM32WBX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBX)、[`CONFIG_SOC_SERIES_STM32WL3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WL3X)、[`CONFIG_SOC_SERIES_STM32WLX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WLX)、[`CONFIG_SOC_SERIES_BEETLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BEETLE)、[`CONFIG_SOC_SERIES_NPCK3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCK3)、[`CONFIG_SOC_SERIES_NPCX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX4)、[`CONFIG_SOC_SERIES_NPCX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX7)、[`CONFIG_SOC_SERIES_NPCX9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCX9)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_SOC_SERIES_CYCLONEV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYCLONEV)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_SERIES_S32K5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K5)、[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)、[`CONFIG_SOC_SERIES_FE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FE300)、[`CONFIG_SOC_SERIES_FU500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU500)、[`CONFIG_SOC_SERIES_FU700`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FU700)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC51U68`、`CONFIG_SOC_SR100`、`CONFIG_SOC_FAMILY_RENESAS_RA`、`CONFIG_SOC_FAMILY_MCXC`、`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_FAMILY_SILABS_S2`、`CONFIG_SOC_FAMILY_SILABS_S3`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT266X`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT685S_HIFI4`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_SERIES_K2X`、`CONFIG_SOC_SERIES_K32LX`、`CONFIG_SOC_SERIES_K6X`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_SERIES_KE1XZ`、`CONFIG_SOC_SERIES_KL2X`、`CONFIG_SOC_SERIES_KV5X`、`CONFIG_SOC_SERIES_KWX`、`CONFIG_SOC_SERIES_SF32LB52X`、`CONFIG_SOC_OPENTITAN`、`CONFIG_SOC_SERIES_TM4C123X`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_SOC_FAMILY_PSOC6`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_SERIES_IMX6SX`、`CONFIG_SOC_SERIES_PSE84`、`CONFIG_SOC_CYT4DNJBZS_M7_0`、`CONFIG_SOC_CYT4DNJBZS_M7_1`、`CONFIG_SOC_SERIES_CYW20829`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_FAMILY_INTEL_ISH`、`CONFIG_SOC_SERIES_SY1XX`、`CONFIG_SOC_FAMILY_MAX32`、`CONFIG_SOC_RTS5817`、`CONFIG_SOC_SERIES_STM32C0X`、`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32F0X`、`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F2X`、`CONFIG_SOC_SERIES_STM32F3X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32G0X`、`CONFIG_SOC_SERIES_STM32G4X`、`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32L0X`、`CONFIG_SOC_SERIES_STM32L1X`、`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_SERIES_STM32MP13X`、`CONFIG_SOC_SERIES_STM32MP1X`、`CONFIG_SOC_STM32MP2X_M33`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_SERIES_STM32U0X`、`CONFIG_SOC_SERIES_STM32U3X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32WB0X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_SERIES_STM32WBX`、`CONFIG_SOC_SERIES_STM32WL3X`、`CONFIG_SOC_SERIES_STM32WLX`、`CONFIG_SOC_SERIES_RW6XX`、`CONFIG_SOC_SERIES_S32K1`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_SERIES_S32K5`、`CONFIG_SOC_SERIES_S32ZE`、`CONFIG_SOC_SERIES_FE300`、`CONFIG_SOC_SERIES_FU500`、`CONFIG_SOC_SERIES_FU700`。

<a id="CONFIG_SOC_EARLY_RESET_HOOK"></a>

## 2.22 `CONFIG_SOC_EARLY_RESET_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在复位／启动代码 `__start` 的早期运行 SoC 专用钩子。自定义 `soc_early_reset_hook()` 在架构专用启动代码开头执行，位于硬件配置完成（按 `CONFIG_INIT_ARCH_HW_AT_BOOT` 要求）之后、架构自身恢复逻辑之前。不强制要求从此钩子返回；可用它实现某些场景下的特殊恢复执行逻辑，例如使用引导加载程序（Bootloader）时。

调用此钩子时，应视为栈指针寄存器尚未初始化，尤其不得使用该栈指针值压入任何数据。钩子可以按需使用实现专用区域作为栈；这种情况下，将控制权交回调用者之前，无需恢复原来的栈指针值。架构还可能对钩子施加其他约束。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC
CONFIG_SOC_MCXA_EARLY_SRAM_ECC_INIT
CONFIG_SOC_SERIES_MCXE31X
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN236
CONFIG_SOC_MIMX94398_M33
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_FAMILY_MAX32_HALT_AFTER_BOOTLOADER_SUPPORT
CONFIG_SOC_SERIES_S32K3
CONFIG_SOC_S32K566_M7
```

**定义位置（Location）**：[`kernel/Kconfig.init:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.init#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 平台钩子（Platform Hooks）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC)、[`CONFIG_SOC_MCXA_EARLY_SRAM_ECC_INIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXA_EARLY_SRAM_ECC_INIT)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_MIMX94398_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_FAMILY_MAX32_HALT_AFTER_BOOTLOADER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_HALT_AFTER_BOOTLOADER_SUPPORT)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_S32K566_M7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K566_M7)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CK_SG_GC`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`、`CONFIG_SOC_MCXA_EARLY_SRAM_ECC_INIT`、`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN236`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_S32K566_M7`。

<a id="CONFIG_SOC_LATE_INIT_HOOK"></a>

## 2.23 `CONFIG_SOC_LATE_INIT_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

运行后期片上系统初始化钩子（Late SoC Initialization Hook）。在内核和设备初始化之后执行自定义钩子 `soc_late_init_hook()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_RENESAS_RA
CONFIG_ESP32_ULP_COPROC_ENABLED
CONFIG_SOC_SERIES_MCXE31X
CONFIG_SECOND_CORE_MCUX
CONFIG_SOC_NRF54H20_CPURAD_ENABLE
CONFIG_SOC_SERIES_PSE84_M33
CONFIG_SOC_CYT4DNJBZS_M0P
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_SERIES_RTL87X2G
```

**定义位置（Location）**：[`kernel/Kconfig.init:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.init#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 平台钩子（Platform Hooks）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_ESP32_ULP_COPROC_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP32_ULP_COPROC_ENABLED)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SECOND_CORE_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECOND_CORE_MCUX)、[`CONFIG_SOC_NRF54H20_CPURAD_ENABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_ENABLE)、[`CONFIG_SOC_SERIES_PSE84_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84_M33)、[`CONFIG_SOC_CYT4DNJBZS_M0P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M0P)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RA`、`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_SERIES_PSE84_M33`、`CONFIG_SOC_CYT4DNJBZS_M0P`。

<a id="CONFIG_SOC_PER_CORE_INIT_HOOK"></a>

## 2.24 `CONFIG_SOC_PER_CORE_INIT_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为每个处理器核运行片上系统初始化钩子（Per-core SoC Initialization Hook）。主核在 `arch_kernel_init()` 末尾执行自定义 `soc_per_core_init_hook()`，次核则在 `arch_secondary_cpu_init()` 末尾执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AE350
```

**定义位置（Location）**：[`kernel/Kconfig.init:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.init#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 平台钩子（Platform Hooks）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AE350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)。

<a id="CONFIG_SOC_PREP_HOOK"></a>

## 2.25 `CONFIG_SOC_PREP_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

运行早期片上系统准备钩子（Early SoC Preparation Hook）。在 C 环境准备代码 `prep_c` 开头执行自定义 `soc_prep_hook()`。SoC 必须实现 `soc_prep_hook()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
CONFIG_SOC_SERIES_MEC165XB
CONFIG_SOC_SERIES_MEC174X
CONFIG_SOC_SERIES_MEC175X
CONFIG_SOC_FAMILY_SILABS_S2
CONFIG_SOC_FAMILY_SILABS_S3
CONFIG_SOC_MIMX8MM6_A53
CONFIG_SOC_MIMX8ML8_A53
CONFIG_SOC_MIMX8MN6_A53
CONFIG_SOC_CYT4DNJBZS_M0P
CONFIG_SOC_CYT4DNJBZS_M7_0
CONFIG_SOC_CYT4DNJBZS_M7_1
CONFIG_SOC_SERIES_XMC7200
CONFIG_SOC_SERIES_IT51XXX
CONFIG_SOC_SERIES_IT8XXX2
```

**定义位置（Location）**：[`kernel/Kconfig.init:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.init#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 平台钩子（Platform Hooks）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_SOC_SERIES_MEC165XB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC165XB)、[`CONFIG_SOC_SERIES_MEC174X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC174X)、[`CONFIG_SOC_SERIES_MEC175X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MEC175X)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_SOC_MIMX8MM6_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6_A53)、[`CONFIG_SOC_MIMX8ML8_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_A53)、[`CONFIG_SOC_MIMX8MN6_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MN6_A53)、[`CONFIG_SOC_CYT4DNJBZS_M0P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M0P)、[`CONFIG_SOC_CYT4DNJBZS_M7_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_0)、[`CONFIG_SOC_CYT4DNJBZS_M7_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CYT4DNJBZS_M7_1)、[`CONFIG_SOC_SERIES_XMC7200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XMC7200)、[`CONFIG_SOC_SERIES_IT51XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IT51XXX)、[`CONFIG_SOC_SERIES_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IT8XXX2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`、`CONFIG_SOC_FAMILY_SILABS_S3`、`CONFIG_SOC_CYT4DNJBZS_M0P`、`CONFIG_SOC_CYT4DNJBZS_M7_0`、`CONFIG_SOC_CYT4DNJBZS_M7_1`、`CONFIG_SOC_SERIES_XMC7200`。

<a id="CONFIG_SOC_RESET_HOOK"></a>

## 2.26 `CONFIG_SOC_RESET_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在复位／启动代码 `__start` 中运行 SoC 专用钩子。自定义 `soc_reset_hook()` 在架构专用启动代码的前部执行，位于硬件配置完成（按 `CONFIG_INIT_ARCH_HW_AT_BOOT` 要求）、栈指针加载，以及架构自身恢复逻辑执行完毕（启用 `CONFIG_PM_S2RAM` 时）之后。由于此钩子在恢复逻辑之后运行，系统从挂起到 RAM（Suspend-to-RAM）电源状态恢复时，不会调用它。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_R8A77951_R7
CONFIG_SOC_SERIES_LPC51U68
CONFIG_SOC_SERIES_LPC54XXX
CONFIG_SOC_LPC54114_M4
CONFIG_SOC_SERIES_LPC55XXX
CONFIG_SOC_CORTEX_R8_VIRTUAL
CONFIG_SOC_SERIES_SAMC20
CONFIG_SOC_SERIES_SAMC21
CONFIG_SOC_SERIES_SAMD20
CONFIG_SOC_SERIES_SAMD21
CONFIG_SOC_SERIES_SAMD51
CONFIG_SOC_SERIES_SAME51
CONFIG_SOC_SERIES_SAME53
CONFIG_SOC_SERIES_SAME54
CONFIG_SOC_SERIES_SAML21
CONFIG_SOC_SERIES_SAMR21
CONFIG_SOC_SERIES_SAMR34
CONFIG_SOC_SERIES_SAMR35
CONFIG_SOC_SERIES_RP2350
CONFIG_SOC_FAMILY_RENESAS_RA
CONFIG_SOC_FAMILY_MCXA
CONFIG_SOC_FAMILY_MCXC
CONFIG_SOC_SERIES_MCXE24X
CONFIG_SOC_MCXL255_CPU0
CONFIG_SOC_MCXL254_CPU0
CONFIG_SOC_MCXL253_CPU0
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN236
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_SERIES_IMXRT10XX
CONFIG_SOC_SERIES_IMXRT118X
CONFIG_SOC_SERIES_IMXRT11XX
CONFIG_SOC_SERIES_IMXRT266X
CONFIG_SOC_MIMXRT595S_CM33
CONFIG_SOC_MIMXRT685S_CM33
CONFIG_SOC_MIMXRT798S_CM33_CPU0
CONFIG_SOC_MIMXRT758S_CM33_CPU0
CONFIG_SOC_MIMXRT735S_CM33_CPU0
CONFIG_SOC_FAMILY_NUMAKER
CONFIG_SOC_SERIES_K2X
CONFIG_SOC_SERIES_K32LX
CONFIG_SOC_SERIES_K6X
CONFIG_SOC_SERIES_K8X
CONFIG_SOC_SERIES_KE1XF
CONFIG_SOC_SERIES_KE1XZ
CONFIG_SOC_SERIES_KL2X
CONFIG_SOC_SERIES_KV5X
CONFIG_SOC_SERIES_KWX
CONFIG_SOC_FAMILY_ASPEED
CONFIG_SOC_FAMILY_NORDIC_NRF
CONFIG_SOC_SERIES_NRF71
CONFIG_SOC_MIMX9352_M33
CONFIG_SOC_SERIES_GD32A50X
CONFIG_SOC_SERIES_GD32C2X1
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
CONFIG_SOC_SERIES_CC23X0
CONFIG_SOC_XILINX_ZYNQMP_RPU
CONFIG_SOC_VERSAL_RPU
CONFIG_SOC_FAMILY_ENSEMBLE_RTSS
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_SERIES_RZN2H
CONFIG_SOC_SERIES_RZN2L
CONFIG_SOC_SERIES_RZT2H
CONFIG_SOC_SERIES_RZT2L
CONFIG_SOC_SERIES_RZT2M
CONFIG_SOC_R9A09G057H44GBG_CR8
CONFIG_SOC_SERIES_B1
CONFIG_SOC_SERIES_SAM3X
CONFIG_SOC_SERIES_SAM4E
CONFIG_SOC_SERIES_SAM4L
CONFIG_SOC_SERIES_SAM4S
CONFIG_SOC_SERIES_SAMX7X
CONFIG_SOC_FAMILY_INFINEON_XMC
CONFIG_SOC_FAMILY_NUMICRO
CONFIG_SOC_SERIES_STM32H7X
CONFIG_SOC_SERIES_STM32N6X
CONFIG_SOC_FVP_AEMV8R_AARCH32
CONFIG_SOC_SERIES_RW6XX
CONFIG_SOC_S32K566_R52
CONFIG_SOC_SERIES_S32ZE
```

**定义位置（Location）**：[`kernel/Kconfig.init:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig.init#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 平台钩子（Platform Hooks）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_R8A77951_R7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A77951_R7)、[`CONFIG_SOC_SERIES_LPC51U68`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC51U68)、[`CONFIG_SOC_SERIES_LPC54XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC54XXX)、[`CONFIG_SOC_LPC54114_M4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LPC54114_M4)、[`CONFIG_SOC_SERIES_LPC55XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC55XXX)、[`CONFIG_SOC_CORTEX_R8_VIRTUAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORTEX_R8_VIRTUAL)、[`CONFIG_SOC_SERIES_SAMC20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC20)、[`CONFIG_SOC_SERIES_SAMC21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMC21)、[`CONFIG_SOC_SERIES_SAMD20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD20)、[`CONFIG_SOC_SERIES_SAMD21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD21)、[`CONFIG_SOC_SERIES_SAMD51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMD51)、[`CONFIG_SOC_SERIES_SAME51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME51)、[`CONFIG_SOC_SERIES_SAME53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME53)、[`CONFIG_SOC_SERIES_SAME54`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAME54)、[`CONFIG_SOC_SERIES_SAML21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAML21)、[`CONFIG_SOC_SERIES_SAMR21`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR21)、[`CONFIG_SOC_SERIES_SAMR34`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR34)、[`CONFIG_SOC_SERIES_SAMR35`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMR35)、[`CONFIG_SOC_SERIES_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2350)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_FAMILY_MCXA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXA)、[`CONFIG_SOC_FAMILY_MCXC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXC)、[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_MCXL255_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL255_CPU0)、[`CONFIG_SOC_MCXL254_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL254_CPU0)、[`CONFIG_SOC_MCXL253_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXL253_CPU0)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT266X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT266X)、[`CONFIG_SOC_MIMXRT595S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S_CM33)、[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT758S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S_CM33_CPU0)、[`CONFIG_SOC_MIMXRT735S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S_CM33_CPU0)、[`CONFIG_SOC_FAMILY_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NUMAKER)、[`CONFIG_SOC_SERIES_K2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K2X)、[`CONFIG_SOC_SERIES_K32LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K32LX)、[`CONFIG_SOC_SERIES_K6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K6X)、[`CONFIG_SOC_SERIES_K8X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_K8X)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_SERIES_KE1XZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XZ)、[`CONFIG_SOC_SERIES_KL2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KL2X)、[`CONFIG_SOC_SERIES_KV5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KV5X)、[`CONFIG_SOC_SERIES_KWX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KWX)、[`CONFIG_SOC_FAMILY_ASPEED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ASPEED)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_SERIES_NRF71`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_MIMX9352_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_M33)、[`CONFIG_SOC_SERIES_GD32A50X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32A50X)、[`CONFIG_SOC_SERIES_GD32C2X1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_GD32C2X1)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH)、[`CONFIG_SOC_SERIES_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SOC_XILINX_ZYNQMP_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_RPU)、[`CONFIG_SOC_VERSAL_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_RPU)、[`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_RTSS)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_SERIES_RZN2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2H)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_SOC_SERIES_RZT2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2H)、[`CONFIG_SOC_SERIES_RZT2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2L)、[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)、[`CONFIG_SOC_SERIES_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_B1)、[`CONFIG_SOC_SERIES_SAM3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM3X)、[`CONFIG_SOC_SERIES_SAM4E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4E)、[`CONFIG_SOC_SERIES_SAM4L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4L)、[`CONFIG_SOC_SERIES_SAM4S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4S)、[`CONFIG_SOC_SERIES_SAMX7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAMX7X)、[`CONFIG_SOC_FAMILY_INFINEON_XMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_XMC)、[`CONFIG_SOC_FAMILY_NUMICRO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NUMICRO)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_FVP_AEMV8R_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH32)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_SOC_S32K566_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K566_R52)、[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC51U68`、`CONFIG_SOC_SERIES_LPC54XXX`、`CONFIG_SOC_LPC54114_M4`、`CONFIG_SOC_SERIES_LPC55XXX`、`CONFIG_SOC_SERIES_RP2350`、`CONFIG_SOC_FAMILY_RENESAS_RA`、`CONFIG_SOC_FAMILY_MCXA`、`CONFIG_SOC_FAMILY_MCXC`、`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_MCXL255_CPU0`、`CONFIG_SOC_MCXL254_CPU0`、`CONFIG_SOC_MCXL253_CPU0`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN236`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT266X`、`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`、`CONFIG_SOC_MIMXRT758S_CM33_CPU0`、`CONFIG_SOC_MIMXRT735S_CM33_CPU0`、`CONFIG_SOC_FAMILY_NUMAKER`、`CONFIG_SOC_SERIES_K2X`、`CONFIG_SOC_SERIES_K32LX`、`CONFIG_SOC_SERIES_K6X`、`CONFIG_SOC_SERIES_K8X`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_SERIES_KE1XZ`、`CONFIG_SOC_SERIES_KL2X`、`CONFIG_SOC_SERIES_KV5X`、`CONFIG_SOC_SERIES_KWX`、`CONFIG_SOC_FAMILY_ASPEED`、`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`、`CONFIG_SOC_FAMILY_ENSEMBLE_RTSS`、`CONFIG_SOC_SERIES_B1`、`CONFIG_SOC_FAMILY_INFINEON_XMC`、`CONFIG_SOC_FAMILY_NUMICRO`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_FVP_AEMV8R_AARCH32`、`CONFIG_SOC_SERIES_RW6XX`、`CONFIG_SOC_S32K566_R52`、`CONFIG_SOC_SERIES_S32ZE`。

<a id="CONFIG_STACK_CANARIES"></a>

## 2.27 `CONFIG_STACK_CANARIES`

**提示（Prompt）**：默认保护（Default Protection）。

**说明（Help）**

本选项为包含易受攻击对象的函数启用编译器栈金丝雀（Stack Canary）。通常指调用 `alloca` 或包含大于 8 字节缓冲区的函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ENTROPY_GENERATOR || CONFIG_TEST_RANDOM_GENERATOR) && <choice>
```

**主动选择（Selects）**

```text
CONFIG_NEED_LIBC_MEM_PARTITION if !CONFIG_STACK_CANARIES_TLS
CONFIG_REQUIRES_STACK_CANARIES
```

**定义位置（Location）**：[`kernel/Kconfig:945`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L945)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 安全选项（Security Options）。 → 栈金丝雀保护选项（Stack Canary Protection Options）。

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_TEST_RANDOM_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_NEED_LIBC_MEM_PARTITION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEED_LIBC_MEM_PARTITION)、[`CONFIG_STACK_CANARIES_TLS`](P002_kernel_配置项参考_2.md#CONFIG_STACK_CANARIES_TLS)、[`CONFIG_REQUIRES_STACK_CANARIES`](P002_kernel_配置项参考_2.md#CONFIG_REQUIRES_STACK_CANARIES)。

<a id="CONFIG_STACK_CANARIES_ALL"></a>

## 2.28 `CONFIG_STACK_CANARIES_ALL`

**提示（Prompt）**：可用的最高保护级别（Maximum Protection）。

**说明（Help）**

本选项为所有函数启用编译器栈金丝雀（Stack Canary）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ENTROPY_GENERATOR || CONFIG_TEST_RANDOM_GENERATOR) && <choice>
```

**主动选择（Selects）**

```text
CONFIG_NEED_LIBC_MEM_PARTITION if !CONFIG_STACK_CANARIES_TLS
CONFIG_REQUIRES_STACK_CANARIES
```

**定义位置（Location）**：[`kernel/Kconfig:965`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L965)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 安全选项（Security Options）。 → 栈金丝雀保护选项（Stack Canary Protection Options）。

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_TEST_RANDOM_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_NEED_LIBC_MEM_PARTITION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEED_LIBC_MEM_PARTITION)、[`CONFIG_STACK_CANARIES_TLS`](P002_kernel_配置项参考_2.md#CONFIG_STACK_CANARIES_TLS)、[`CONFIG_REQUIRES_STACK_CANARIES`](P002_kernel_配置项参考_2.md#CONFIG_REQUIRES_STACK_CANARIES)。

<a id="CONFIG_STACK_CANARIES_EXPLICIT"></a>

## 2.29 `CONFIG_STACK_CANARIES_EXPLICIT`

**提示（Prompt）**：显式保护（Explicit Protection）。

**说明（Help）**

本选项仅为具有 `stack_protect` 属性的函数启用编译器栈金丝雀（Stack Canary）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ENTROPY_GENERATOR || CONFIG_TEST_RANDOM_GENERATOR) && "zephyr" = "zephyr" && <choice>
```

**主动选择（Selects）**

```text
CONFIG_NEED_LIBC_MEM_PARTITION if !CONFIG_STACK_CANARIES_TLS
CONFIG_REQUIRES_STACK_CANARIES
```

**定义位置（Location）**：[`kernel/Kconfig:973`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L973)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 安全选项（Security Options）。 → 栈金丝雀保护选项（Stack Canary Protection Options）。

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_TEST_RANDOM_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_NEED_LIBC_MEM_PARTITION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEED_LIBC_MEM_PARTITION)、[`CONFIG_STACK_CANARIES_TLS`](P002_kernel_配置项参考_2.md#CONFIG_STACK_CANARIES_TLS)、[`CONFIG_REQUIRES_STACK_CANARIES`](P002_kernel_配置项参考_2.md#CONFIG_REQUIRES_STACK_CANARIES)。

<a id="CONFIG_STACK_CANARIES_STRONG"></a>

## 2.30 `CONFIG_STACK_CANARIES_STRONG`

**提示（Prompt）**：强保护（Strong Protection）。

**说明（Help）**

本选项为调用 `alloca`、定义局部数组，或引用局部栈帧地址的函数启用编译器栈金丝雀（Stack Canary）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ENTROPY_GENERATOR || CONFIG_TEST_RANDOM_GENERATOR) && <choice>
```

**主动选择（Selects）**

```text
CONFIG_NEED_LIBC_MEM_PARTITION if !CONFIG_STACK_CANARIES_TLS
CONFIG_REQUIRES_STACK_CANARIES
```

**定义位置（Location）**：[`kernel/Kconfig:955`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L955)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 安全选项（Security Options）。 → 栈金丝雀保护选项（Stack Canary Protection Options）。

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_TEST_RANDOM_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_NEED_LIBC_MEM_PARTITION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEED_LIBC_MEM_PARTITION)、[`CONFIG_STACK_CANARIES_TLS`](P002_kernel_配置项参考_2.md#CONFIG_STACK_CANARIES_TLS)、[`CONFIG_REQUIRES_STACK_CANARIES`](P002_kernel_配置项参考_2.md#CONFIG_REQUIRES_STACK_CANARIES)。

<a id="CONFIG_STACK_CANARIES_TLS"></a>

## 2.31 `CONFIG_STACK_CANARIES_TLS`

**提示（Prompt）**：使用线程局部存储的栈金丝雀（TLS Stack Canaries）。

**说明（Help）**

本选项将编译器栈金丝雀（Stack Canary）放在线程局部存储（TLS）中，使每个线程拥有自己的金丝雀值，更难预测其位置和值。启用后，每个线程都需要生成新的随机值，因此线程创建时会增加性能开销。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_LOCAL_STORAGE && CONFIG_ARCH_HAS_STACK_CANARIES_TLS && !(CONFIG_RISCV && "" = "llvm") && CONFIG_REQUIRES_STACK_CANARIES
```

**定义位置（Location）**：[`kernel/Kconfig:987`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L987)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 安全选项（Security Options）。

**配置项引用（Symbol References）**：[`CONFIG_THREAD_LOCAL_STORAGE`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_LOCAL_STORAGE)、[`CONFIG_ARCH_HAS_STACK_CANARIES_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACK_CANARIES_TLS)、[`CONFIG_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV)、[`CONFIG_REQUIRES_STACK_CANARIES`](P002_kernel_配置项参考_2.md#CONFIG_REQUIRES_STACK_CANARIES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_STACK_CANARIES_TLS`。

<a id="CONFIG_STACK_POINTER_RANDOM"></a>

## 2.32 `CONFIG_STACK_POINTER_RANDOM`

**提示（Prompt）**：初始栈指针随机化边界（Initial Stack Pointer Randomization Bounds）。

**说明（Help）**

本选项在线程创建时，为初始栈指针增加随机偏移，实现有限形式的地址空间布局随机化（Address Space Layout Randomization，ASLR）。这样可使特定栈帧的位置不再确定，从而阻碍某些安全攻击。该功能会从栈区域总大小中划出一部分空间，最多浪费所指定字节数。若内存允许，合理的最小值约为 100 字节。目前仅在栈指针向低地址增长的系统中实现。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_STACK_GROWS_UP && CONFIG_MULTITHREADING && (CONFIG_TEST_RANDOM_GENERATOR || CONFIG_ENTROPY_HAS_DRIVER)
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`kernel/Kconfig:1010`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1010)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 安全选项（Security Options）。

**配置项引用（Symbol References）**：[`CONFIG_STACK_GROWS_UP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STACK_GROWS_UP)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_TEST_RANDOM_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_ENTROPY_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_STATIC_INIT_GNU"></a>

## 2.33 `CONFIG_STATIC_INIT_GNU`

**提示（Prompt）**：支持 GNU 兼容初始化器和构造函数（Initializers and Constructors）。

**说明（Help）**

为静态对象提供 GNU 兼容初始化。C++ 构造函数，以及 GNU 兼容工具链定义的初始化函数，都需要此支持。它使 Zephyr 二进制大小增加约 24 字节。若确定应用不需要任何初始化器，可以禁用。如果需要构造函数但已禁用本选项，链接器会报错。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TOOLCHAIN_SUPPORTS_STATIC_INIT_GNU && !CONFIG_CMAKE_LINKER_GENERATOR
```

**默认值（Defaults）**

```text
y if CONFIG_CPP || CONFIG_NATIVE_LIBRARY || CONFIG_COVERAGE
```

**被选择（Selected by）**

```text
CONFIG_ARCMWDT_LIBC
```

**定义位置（Location）**：[`kernel/Kconfig:1139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1139)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_TOOLCHAIN_SUPPORTS_STATIC_INIT_GNU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TOOLCHAIN_SUPPORTS_STATIC_INIT_GNU)、[`CONFIG_CMAKE_LINKER_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CMAKE_LINKER_GENERATOR)、[`CONFIG_CPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPP)、[`CONFIG_NATIVE_LIBRARY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NATIVE_LIBRARY)、[`CONFIG_COVERAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE)、[`CONFIG_ARCMWDT_LIBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCMWDT_LIBC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TOOLCHAIN_SUPPORTS_STATIC_INIT_GNU`。

<a id="CONFIG_SWAP_NONATOMIC"></a>

## 2.34 `CONFIG_SWAP_NONATOMIC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在某些架构上，`z_swap()` 原语相对于 `irq_lock` 的释放无法保持原子性，即从进入 `z_swap` 到上下文切换完成之间可能收到中断。出现这种情况时，需要启用内核中的若干变通处理。目前只有 ARM 会出现：PendSV 异常优先级低于 Zephyr 处理的中断优先级。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_CORTEX_M
```

**定义位置（Location）**：[`kernel/Kconfig:710`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L710)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M)。

<a id="CONFIG_SYSTEM_WORKQUEUE_NO_YIELD"></a>

## 2.35 `CONFIG_SYSTEM_WORKQUEUE_NO_YIELD`

**提示（Prompt）**：选择系统工作队列是否主动让出 CPU（Yield）。

**说明（Help）**

默认情况下，系统工作队列（System Work Queue）会在各工作项之间主动让出 CPU，防止其他线程饥饿。选择本选项会取消该让出操作；如果工作队列线程是协作式线程，且预期一系列工作项应连续完成、期间不让出 CPU，这可能有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`kernel/Kconfig:545`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L545)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 系统工作队列选项（System Work Queue Options）。

<a id="CONFIG_SYSTEM_WORKQUEUE_PRIORITY"></a>

## 2.36 `CONFIG_SYSTEM_WORKQUEUE_PRIORITY`

**提示（Prompt）**：系统工作队列优先级（System Workqueue Priority）。

**说明（Help）**

默认情况下，系统工作队列使用最低的协作式优先级。这意味着任何工作处理函数一旦开始，在完成之前都不会被其他线程抢占。译注：这里保留原选项说明；元中断（Meta-IRQ）配置另有针对协作式线程的特殊抢占约定，参见对应配置项。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
-2 if CONFIG_COOP_ENABLED && !CONFIG_PREEMPT_ENABLED
0 if !CONFIG_COOP_ENABLED
-1
```

**定义位置（Location）**：[`kernel/Kconfig:535`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L535)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 系统工作队列选项（System Work Queue Options）。

**配置项引用（Symbol References）**：[`CONFIG_COOP_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COOP_ENABLED)、[`CONFIG_PREEMPT_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PREEMPT_ENABLED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_COOP_ENABLED`、`CONFIG_PREEMPT_ENABLED`。

<a id="CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE"></a>

## 2.37 `CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE`

**提示（Prompt）**：系统工作队列栈大小（System Workqueue Stack Size）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
4096 if CONFIG_COVERAGE_GCOV || CONFIG_WIFI_NRF70
2560 if CONFIG_WIFI_NM_WPA_SUPPLICANT
1024
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_arduino_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_arduino_wifi_bt/Kconfig.defconfig)。

```text
2048
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
2048
```

**定义位置（Location）**：[`kernel/Kconfig:529`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L529)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 系统工作队列选项（System Work Queue Options）。

**配置项引用（Symbol References）**：[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)、[`CONFIG_WIFI_NRF70`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_SYSTEM_WORKQUEUE_WORK_TIMEOUT_MS"></a>

## 2.38 `CONFIG_SYSTEM_WORKQUEUE_WORK_TIMEOUT_MS`

**提示（Prompt）**：选择系统工作队列的工作项超时时间，单位为毫秒。

**说明（Help）**

设为 0 可禁用系统工作队列的工作项超时。未启用 `WORKQUEUE_WORK_TIMEOUT` 时，本选项无效。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
5000 if CONFIG_ASSERT
0
```

**定义位置（Location）**：[`kernel/Kconfig:554`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L554)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 系统工作队列选项（System Work Queue Options）。

**配置项引用（Symbol References）**：[`CONFIG_ASSERT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT)。

<a id="CONFIG_SYS_CLOCK_EXISTS"></a>

## 2.39 `CONFIG_SYS_CLOCK_EXISTS`

**提示（Prompt）**：系统时钟存在并已启用（System Clock Enabled）。

**说明（Help）**

本选项表示内核具有定时器支持。禁用后，某些设备配置可以省去大量代码；但与超时相关的 API 将无法工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_SUN8I_H3
CONFIG_SOC_SUN50I_H618
CONFIG_SOC_RV1106
CONFIG_SOC_SERIES_RTS5912
CONFIG_SOC_SERIES_STM32MP13X
```

**定义位置（Location）**：[`kernel/Kconfig:767`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L767)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_SUN8I_H3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SUN8I_H3)、[`CONFIG_SOC_SUN50I_H618`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SUN50I_H618)、[`CONFIG_SOC_RV1106`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RV1106)、[`CONFIG_SOC_SERIES_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SUN8I_H3`、`CONFIG_SOC_SUN50I_H618`、`CONFIG_SOC_RV1106`、`CONFIG_SOC_SERIES_STM32MP13X`。

<a id="CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC"></a>

## 2.40 `CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC`

**提示（Prompt）**：系统时钟硬件定时器频率（Hardware Timer Frequency）。

**说明（Help）**

本选项指定系统时钟使用的硬件定时器频率，单位为 Hz。由 SoC 或开发板的 Kconfig 文件设置，用户通常应避免通过菜单配置修改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
0 if CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME
0 if n
```

**定义位置（Location）**：[`kernel/Kconfig:756`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L756)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME)。

<a id="CONFIG_SYS_CLOCK_MAX_TIMEOUT_DAYS"></a>

## 2.41 `CONFIG_SYS_CLOCK_MAX_TIMEOUT_DAYS`

**提示（Prompt）**：时间转换使用的最大超时，单位为天。

**说明（Help）**

该值供时间转换静态内联函数使用，在编译时决定算法。一种算法更快、代码更少，但若源频率与目标频率的乘法结果超出 64 位，可能溢出；另一种算法可避免这种情况。当以源频率表示的最大超时乘以目标频率仍可容纳于 64 位时，选择较快算法。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
365
```

**定义位置（Location）**：[`kernel/Kconfig:900`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L900)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

<a id="CONFIG_SYS_CLOCK_TICKS_PER_SEC"></a>

## 2.42 `CONFIG_SYS_CLOCK_TICKS_PER_SEC`

**提示（Prompt）**：系统节拍频率（System Tick Frequency），单位为节拍／秒。

**说明（Help）**

本选项指定系统时钟的标称频率，单位为 Hz。为进行异步计时，内核定义“节拍”（Tick），将其作为内部记录运行时长（Uptime）和超时的计数单位。实际可行时，中断应在节拍边界送达；内核不跟踪分数节拍。本选项用于配置节拍速率，每个节拍的周期数也应使 1 毫秒能够用整数个节拍精确表示。

多数支持任意中断超时的平台，默认值预计在 10 kHz 左右；软件仿真平台和传统驱动使用更传统的 100 Hz。注意，在支持并启用无节拍（Tickless）模式时，本配置指定最小可用定时粒度，不一定等于实际送达内核的中断次数或频率。设为 0 将完全禁用内核定时器支持。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
100 if CONFIG_QEMU_TARGET || CONFIG_SOC_POSIX
10000 if CONFIG_TICKLESS_KERNEL
100
```

**定义位置（Location）**：[`kernel/Kconfig:728`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L728)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_QEMU_TARGET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QEMU_TARGET)、[`CONFIG_SOC_POSIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_POSIX)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)。

<a id="CONFIG_THREAD_ABORT_HOOK"></a>

## 2.43 `CONFIG_THREAD_ABORT_HOOK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

供可移植性层（Portability Layer）修改本地管理的状态掩码。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CMSIS_RTOS_V1
```

**定义位置（Location）**：[`kernel/Kconfig:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CMSIS_RTOS_V1)。

<a id="CONFIG_THREAD_ABORT_NEED_CLEANUP"></a>

## 2.44 `CONFIG_THREAD_ABORT_NEED_CLEANUP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用在调用 `k_thread_abort(_current)` 时清理当前线程所需的支持，因为清理过程不能在当前线程栈上运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_THREAD_STACK_MEM_MAPPED
```

**定义位置（Location）**：[`kernel/Kconfig:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_THREAD_STACK_MEM_MAPPED`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_MEM_MAPPED)。

<a id="CONFIG_THREAD_CUSTOM_DATA"></a>

## 2.45 `CONFIG_THREAD_CUSTOM_DATA`

**提示（Prompt）**：线程自定义数据（Thread Custom Data）。

**说明（Help）**

允许每个线程保存 32 位自定义数据，并通过 `k_thread_custom_data_xxx()` API 访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_WIFI_ESP32
CONFIG_WIFI_AIROC
```

**定义位置（Location）**：[`kernel/Kconfig:201`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L201)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI_AIROC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_AIROC)。

<a id="CONFIG_THREAD_LOCAL_STORAGE"></a>

## 2.46 `CONFIG_THREAD_LOCAL_STORAGE`

**提示（Prompt）**：线程局部存储（Thread Local Storage，TLS）。

**说明（Help）**

启用内核的线程局部存储（Thread Local Storage，TLS）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE && CONFIG_TOOLCHAIN_SUPPORTS_THREAD_LOCAL_STORAGE
```

**主动选择（Selects）**

```text
CONFIG_NEED_LIBC_MEM_PARTITION if CONFIG_CPU_CORTEX_M && CONFIG_USERSPACE
```

**被选择（Selected by）**

```text
CONFIG_RISCV_PMP
CONFIG_PICOLIBC_USE_TOOLCHAIN
```

**被弱选择（Implied by）**

```text
CONFIG_PICOLIBC
```

**定义位置（Location）**：[`kernel/Kconfig:1120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1120)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE)、[`CONFIG_TOOLCHAIN_SUPPORTS_THREAD_LOCAL_STORAGE`](P002_kernel_配置项参考_2.md#CONFIG_TOOLCHAIN_SUPPORTS_THREAD_LOCAL_STORAGE)、[`CONFIG_NEED_LIBC_MEM_PARTITION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEED_LIBC_MEM_PARTITION)、[`CONFIG_CPU_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M)、[`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE)、[`CONFIG_RISCV_PMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_PMP)、[`CONFIG_PICOLIBC_USE_TOOLCHAIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOLIBC_USE_TOOLCHAIN)、[`CONFIG_PICOLIBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOLIBC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE`。

<a id="CONFIG_THREAD_MAX_NAME_LEN"></a>

## 2.47 `CONFIG_THREAD_MAX_NAME_LEN`

**提示（Prompt）**：线程名称最大长度（Maximum Thread Name Length）。

**说明（Help）**

线程名称保存在 `k_thread` 结构中。本项指定名称最大长度，包含末尾的空字符字节（NUL）。减小此值可节省内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_NAME
```

**默认值（Defaults）**

```text
32
64 if CONFIG_ZTEST
```

**取值范围（Ranges）**

```text
[8, 128]
```

**定义位置（Location）**：[`kernel/Kconfig:426`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L426)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。 → 线程名称（Thread Name）。

**配置项引用（Symbol References）**：[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)、[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)。

<a id="CONFIG_THREAD_MONITOR"></a>

## 2.48 `CONFIG_THREAD_MONITOR`

**提示（Prompt）**：线程监视（Thread Monitoring）。

**说明（Help）**

要求内核维护所有线程的列表，不包括尚未启动或已终止的线程。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SILABS_SIWX91X_NWP
CONFIG_DYNAMIC_THREAD
CONFIG_THREAD_ANALYZER
CONFIG_DEBUG_THREAD_INFO
CONFIG_ZTRESS
CONFIG_PERCEPIO_TRACERECORDER
CONFIG_SEGGER_SYSTEMVIEW
```

**被弱选择（Implied by）**

```text
CONFIG_KERNEL_SHELL
CONFIG_TRACING
```

**定义位置（Location）**：[`kernel/Kconfig:414`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L414)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。

**配置项引用（Symbol References）**：[`CONFIG_SILABS_SIWX91X_NWP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SIWX91X_NWP)、[`CONFIG_DYNAMIC_THREAD`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD)、[`CONFIG_THREAD_ANALYZER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_THREAD_ANALYZER)、[`CONFIG_DEBUG_THREAD_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_THREAD_INFO)、[`CONFIG_ZTRESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTRESS)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_SEGGER_SYSTEMVIEW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_SYSTEMVIEW)、[`CONFIG_KERNEL_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_KERNEL_SHELL)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)。

<a id="CONFIG_THREAD_NAME"></a>

## 2.49 `CONFIG_THREAD_NAME`

**提示（Prompt）**：线程名称（Thread Name）。

**说明（Help）**

允许为线程设置名称。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SILABS_SIWX91X_NWP
CONFIG_DEBUG_THREAD_INFO
CONFIG_INSTRUMENTATION_MODE_CALLGRAPH
CONFIG_TEST
CONFIG_PERCEPIO_TRACERECORDER
```

**被弱选择（Implied by）**

```text
CONFIG_MPIPE
CONFIG_KERNEL_SHELL
CONFIG_TRACING
```

**定义位置（Location）**：[`kernel/Kconfig:421`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L421)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。

**配置项引用（Symbol References）**：[`CONFIG_SILABS_SIWX91X_NWP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SIWX91X_NWP)、[`CONFIG_DEBUG_THREAD_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_THREAD_INFO)、[`CONFIG_INSTRUMENTATION_MODE_CALLGRAPH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_MODE_CALLGRAPH)、[`CONFIG_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_MPIPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE)、[`CONFIG_KERNEL_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_KERNEL_SHELL)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)。

<a id="CONFIG_THREAD_RUNTIME_STACK_SAFETY"></a>

## 2.50 `CONFIG_THREAD_RUNTIME_STACK_SAFETY`

**提示（Prompt）**：线程运行时栈安全支持（Runtime Stack Safety）。

**说明（Help）**

启用线程运行时栈安全检查例程。这些例程检测线程未使用的栈空间；若发现其低于配置阈值，则调用用户定义的处理函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_THREAD_ANALYZER_STACK_SAFETY
```

**定义位置（Location）**：[`kernel/Kconfig:495`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L495)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER_STACK_SAFETY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_THREAD_ANALYZER_STACK_SAFETY)。

<a id="CONFIG_THREAD_RUNTIME_STACK_SAFETY_DEFAULT_UNUSED_THRESHOLD_PCT"></a>

## 2.51 `CONFIG_THREAD_RUNTIME_STACK_SAFETY_DEFAULT_UNUSED_THRESHOLD_PCT`

**提示（Prompt）**：运行时栈安全检查的未使用栈百分比阈值。

**说明（Help）**

将线程默认运行时栈安全阈值定义为栈大小的百分比。若检查例程发现线程未使用栈的百分比低于此阈值，则调用用户定义的处理函数。设为 0 时，默认对所有线程禁用该检查。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_RUNTIME_STACK_SAFETY
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 99]
```

**定义位置（Location）**：[`kernel/Kconfig:504`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L504)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。 → 线程运行时栈安全支持（Runtime Stack Safety）。

**配置项引用（Symbol References）**：[`CONFIG_THREAD_RUNTIME_STACK_SAFETY`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_RUNTIME_STACK_SAFETY)。

<a id="CONFIG_THREAD_RUNTIME_STATS"></a>

## 2.52 `CONFIG_THREAD_RUNTIME_STATS`

**提示（Prompt）**：线程运行时间统计（Thread Runtime Statistics）。

**说明（Help）**

收集线程运行时间统计（Thread Runtime Statistics），例如线程总执行周期数、系统总执行周期数。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_OBJ_CORE_STATS_THREAD
CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS
CONFIG_POSIX_MULTI_PROCESS
CONFIG_ZTRESS
```

**定义位置（Location）**：[`kernel/Kconfig:440`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L440)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE_STATS_THREAD`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE_STATS_THREAD)、[`CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS)、[`CONFIG_POSIX_MULTI_PROCESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MULTI_PROCESS)、[`CONFIG_ZTRESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTRESS)。

<a id="CONFIG_THREAD_RUNTIME_STATS_USE_TIMING_FUNCTIONS"></a>

## 2.53 `CONFIG_THREAD_RUNTIME_STATS_USE_TIMING_FUNCTIONS`

**提示（Prompt）**：使用计时函数收集统计信息（Timing Functions）。

**说明（Help）**

使用计时函数（Timing Functions）收集线程运行时间统计。注意，计时函数可能使用与操作系统计时默认定时器不同的定时器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_RUNTIME_STATS
```

**主动选择（Selects）**

```text
CONFIG_TIMING_FUNCTIONS_NEED_AT_BOOT
```

**定义位置（Location）**：[`kernel/Kconfig:451`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L451)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 内核调试与度量（Kernel Debugging and Metrics）。 → 线程运行时间统计（Thread Runtime Statistics）。

**配置项引用（Symbol References）**：[`CONFIG_THREAD_RUNTIME_STATS`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_RUNTIME_STATS)、[`CONFIG_TIMING_FUNCTIONS_NEED_AT_BOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TIMING_FUNCTIONS_NEED_AT_BOOT)。

<a id="CONFIG_THREAD_STACK_INFO"></a>

## 2.54 `CONFIG_THREAD_STACK_INFO`

**提示（Prompt）**：线程栈信息（Thread Stack Info）。

**说明（Help）**

允许每个线程将线程栈信息保存到 `k_thread` 数据结构中。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR
CONFIG_SILABS_SIWX91X_NWP
CONFIG_SOC_SERIES_CC23X0
CONFIG_SOC_SERIES_RTL8752H
CONFIG_SOC_SERIES_RTL87X2G
CONFIG_ARC_STACK_PROTECTION
CONFIG_ARC_MPU
CONFIG_BUILTIN_STACK_GUARD
CONFIG_ARM_AARCH32_MMU
CONFIG_ARM64_STACK_PROTECTION
CONFIG_RISCV_PMP
CONFIG_CUSTOM_STACK_GUARD
CONFIG_X86_STACK_PROTECTION
CONFIG_X86_USERSPACE
CONFIG_ARCH_HAS_STACKWALK
CONFIG_ARCH_HAS_STACKWALK
CONFIG_X86_STACK_PROTECTION
CONFIG_X86_USERSPACE
CONFIG_XTENSA
CONFIG_ARM_MPU
CONFIG_USERSPACE
CONFIG_THREAD_STACK_MEM_MAPPED
CONFIG_OBJ_CORE
CONFIG_KERNEL_COHERENCE
CONFIG_WIFI_ESP32
CONFIG_THREAD_ANALYZER
CONFIG_STACK_SENTINEL
CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN
CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS
```

**被弱选择（Implied by）**

```text
CONFIG_ARCH_HAS_STACKWALK
CONFIG_ARCH_HAS_STACKWALK
CONFIG_KERNEL_SHELL
CONFIG_TRACING
```

**定义位置（Location）**：[`kernel/Kconfig:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR)、[`CONFIG_SILABS_SIWX91X_NWP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SIWX91X_NWP)、[`CONFIG_SOC_SERIES_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SOC_SERIES_RTL8752H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL8752H)、[`CONFIG_SOC_SERIES_RTL87X2G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTL87X2G)、[`CONFIG_ARC_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_STACK_PROTECTION)、[`CONFIG_ARC_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_MPU)、[`CONFIG_BUILTIN_STACK_GUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILTIN_STACK_GUARD)、[`CONFIG_ARM_AARCH32_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_AARCH32_MMU)、[`CONFIG_ARM64_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM64_STACK_PROTECTION)、[`CONFIG_RISCV_PMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_PMP)、[`CONFIG_CUSTOM_STACK_GUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CUSTOM_STACK_GUARD)、[`CONFIG_X86_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_STACK_PROTECTION)、[`CONFIG_X86_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_USERSPACE)、[`CONFIG_ARCH_HAS_STACKWALK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_STACKWALK)、[`CONFIG_XTENSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA)、[`CONFIG_ARM_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU)、[`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE)、[`CONFIG_THREAD_STACK_MEM_MAPPED`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_MEM_MAPPED)、[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)、[`CONFIG_KERNEL_COHERENCE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_COHERENCE)、[`CONFIG_WIFI_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESP32)、[`CONFIG_THREAD_ANALYZER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_THREAD_ANALYZER)、[`CONFIG_STACK_SENTINEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STACK_SENTINEL)、[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN)、[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_THREADS)、[`CONFIG_KERNEL_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_KERNEL_SHELL)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)。

<a id="CONFIG_THREAD_STACK_MEM_MAPPED"></a>

## 2.55 `CONFIG_THREAD_STACK_MEM_MAPPED`

**提示（Prompt）**：在运行时对栈进行内存映射（Memory-mapped Stack）。

**说明（Help）**

改变线程栈的处理方式：对线程栈进行内存映射，并在两端设置保护页（Guard Page），以捕获不应发生的访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MMU && CONFIG_ARCH_SUPPORTS_MEM_MAPPED_STACKS
```

**主动选择（Selects）**

```text
CONFIG_THREAD_STACK_INFO
CONFIG_THREAD_ABORT_NEED_CLEANUP
```

**被弱选择（Implied by）**

```text
CONFIG_X86_STACK_PROTECTION
CONFIG_X86_STACK_PROTECTION
```

**定义位置（Location）**：[`kernel/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_ARCH_SUPPORTS_MEM_MAPPED_STACKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_MEM_MAPPED_STACKS)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_THREAD_ABORT_NEED_CLEANUP`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_ABORT_NEED_CLEANUP)、[`CONFIG_X86_STACK_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_STACK_PROTECTION)。

<a id="CONFIG_TICKET_SPINLOCKS"></a>

## 2.56 `CONFIG_TICKET_SPINLOCKS`

**提示（Prompt）**：用于公平获取锁的票据自旋锁（Ticket Spinlock）［实验性］。

**说明（Help）**

基础自旋锁（Spinlock）基于单个原子变量实现，无法保证多个 CPU 之间获取锁的公平性；甚至可能由同一个 CPU 每次都赢得竞争，导致活锁（Live-lock）。票据自旋锁（Ticket Spinlock）按先进先出（FIFO）顺序分配锁，解决这种不公平问题，代价是略微增加内存占用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`kernel/smp/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/smp/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对称多处理选项（SMP Options）。

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_EXPERIMENTAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_TICKLESS_KERNEL"></a>

## 2.57 `CONFIG_TICKLESS_KERNEL`

**提示（Prompt）**：无节拍内核（Tickless Kernel）。

**说明（Help）**

启用完全由事件驱动的内核（Event-driven Kernel），始终停止生成周期性系统时钟中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TICKLESS_CAPABLE
```

**默认值（Defaults）**

```text
y if CONFIG_TICKLESS_CAPABLE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_RP2350
CONFIG_SOC_SERIES_CC23X0
```

**定义位置（Location）**：[`kernel/Kconfig:1105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1105)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_TICKLESS_CAPABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_SOC_SERIES_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2350)、[`CONFIG_SOC_SERIES_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC23X0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RP2350`。

<a id="CONFIG_TIMEOUT_64BIT"></a>

## 2.58 `CONFIG_TIMEOUT_64BIT`

**提示（Prompt）**：以 64 位精度保存内核超时（64-bit Kernel Timeouts）。

**说明（Help）**

设为 `true` 时，传给内核 API 的 `k_ticks_t` 值使用 64 位，可使用更大数值及更高精度的节拍速率，而不必担心 32 位字溢出。本功能还决定是否提供需要额外精度的绝对超时值（Absolute Timeout）。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_GNSS_EMUL
CONFIG_MPSC_PBUF
```

**定义位置（Location）**：[`kernel/Kconfig:777`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L777)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_GNSS_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GNSS_EMUL)、[`CONFIG_MPSC_PBUF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPSC_PBUF)。

<a id="CONFIG_TIMEOUT_BACKEND"></a>

## 2.59 `CONFIG_TIMEOUT_BACKEND`

**提示（Prompt）**：超时队列后端（Timeout Queue Backend）。

**说明（Help）**

选择内核超时子系统用于跟踪待处理超时的数据结构。所有后端共享同一前端 `kernel/timeout.c`，区别仅在队列表示方式及其性能权衡。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
CONFIG_TIMEOUT_BACKEND_DLIST
```

**可选项（Choices）**

```text
CONFIG_TIMEOUT_BACKEND_DLIST
CONFIG_TIMEOUT_BACKEND_MINHEAP
CONFIG_TIMEOUT_BACKEND_WHEEL
CONFIG_TIMEOUT_BACKEND_BUCKET
CONFIG_TIMEOUT_BACKEND_SKIPLIST
```

**定义位置（Location）**：[`kernel/Kconfig:788`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L788)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TIMEOUT_BACKEND_DLIST`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND_DLIST)、[`CONFIG_TIMEOUT_BACKEND_MINHEAP`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND_MINHEAP)、[`CONFIG_TIMEOUT_BACKEND_WHEEL`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND_WHEEL)、[`CONFIG_TIMEOUT_BACKEND_BUCKET`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND_BUCKET)、[`CONFIG_TIMEOUT_BACKEND_SKIPLIST`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND_SKIPLIST)。

<a id="CONFIG_TIMEOUT_BACKEND_BUCKET"></a>

## 2.60 `CONFIG_TIMEOUT_BACKEND_BUCKET`

**提示（Prompt）**：单层分桶差值链表（Single-level Bucketed Delta List）［实验性］。

**说明（Help）**

时间轮（Timer Wheel）的简化近似形式：为接下来 `CONFIG_TIMEOUT_BUCKET_LISTS` 个节拍中的每个节拍提供桶链表，插入／移除复杂度为 O(1)；更远的超时放入排序溢出链表，插入复杂度为 O(n)。迁移根据实际下一事件按需进行，因此不会为无节拍空闲（Tickless Idle）强加最小处理间隔。需要 64 位超时。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TIMEOUT_64BIT && <choice CONFIG_TIMEOUT_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`kernel/Kconfig:828`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L828)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 超时队列后端（Timeout Queue Backend）。

**配置项引用（Symbol References）**：[`CONFIG_TIMEOUT_64BIT`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_64BIT)、[`CONFIG_TIMEOUT_BACKEND`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND)、[`CONFIG_EXPERIMENTAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_TIMEOUT_BACKEND_DLIST"></a>

## 2.61 `CONFIG_TIMEOUT_BACKEND_DLIST`

**提示（Prompt）**：排序差值链表（Sorted Delta List）。

**说明（Help）**

Zephyr 原有后端：按到期时间排序的双向链表，每个节点保存相对于前驱节点的时间差。插入复杂度为 O(n)，移除头节点为 O(1)。没有容量上限，也不增加静态 RAM，是多数系统合适的默认选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMEOUT_BACKEND>
```

**定义位置（Location）**：[`kernel/Kconfig:798`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L798)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 超时队列后端（Timeout Queue Backend）。

**配置项引用（Symbol References）**：[`CONFIG_TIMEOUT_BACKEND`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND)。

<a id="CONFIG_TIMEOUT_BACKEND_MINHEAP"></a>

## 2.62 `CONFIG_TIMEOUT_BACKEND_MINHEAP`

**提示（Prompt）**：二叉最小堆（Binary Min-heap）［实验性］。

**说明（Help）**

以绝对到期节拍为键的二叉最小堆（Binary Min-heap），插入与任意节点移除复杂度均为 O(log n)。需要 64 位超时及固定容量堆（`CONFIG_TIMEOUT_HEAP_MAX_ENTRIES`）；溢出属于致命错误。当待处理超时很多，且差值链表插入开销占主导时，可考虑此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TIMEOUT_64BIT && <choice CONFIG_TIMEOUT_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`kernel/Kconfig:806`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L806)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 超时队列后端（Timeout Queue Backend）。

**配置项引用（Symbol References）**：[`CONFIG_TIMEOUT_64BIT`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_64BIT)、[`CONFIG_TIMEOUT_BACKEND`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND)、[`CONFIG_EXPERIMENTAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_TIMEOUT_BACKEND_SKIPLIST"></a>

## 2.63 `CONFIG_TIMEOUT_BACKEND_SKIPLIST`

**提示（Prompt）**：跳表（Skip List）［实验性］。

**说明（Help）**

以绝对到期节拍为键的 Pugh 跳表（Skip List）。插入与任意节点移除的期望复杂度为 O(log n)，获取最早超时为 O(1)，且无容量上限。同一节拍内按先进先出（FIFO）顺序触发。虽然期望高度为 2，每个待处理超时仍按最坏情况携带 `CONFIG_TIMEOUT_SKIPLIST_MAX_LEVEL` 个前向指针。默认 8 层时，64 位目标上的 `struct _timeout` 为 88 字节；相比之下，差值链表为 32 字节，最小堆为 24 字节。每个 `k_thread`、`k_timer` 和可延迟工作项都承担此开销。需要 64 位超时。待处理超时很多且不希望使用有界堆时，可考虑此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TIMEOUT_64BIT && <choice CONFIG_TIMEOUT_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`kernel/Kconfig:839`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L839)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 超时队列后端（Timeout Queue Backend）。

**配置项引用（Symbol References）**：[`CONFIG_TIMEOUT_64BIT`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_64BIT)、[`CONFIG_TIMEOUT_BACKEND`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND)、[`CONFIG_EXPERIMENTAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_TIMEOUT_BACKEND_WHEEL"></a>

## 2.64 `CONFIG_TIMEOUT_BACKEND_WHEEL`

**提示（Prompt）**：分层时间轮（Hierarchical Timer Wheel）［实验性］。

**说明（Help）**

分层时间轮（Hierarchical Timer Wheel）：接下来约 1024 个节拍内到期的超时，插入与移除复杂度为 O(1)；更远的超时放入排序溢出链表。筛选工作在 32 节拍边界上摊销。适合存在许多短期待处理超时的情况。静态状态占用约 1 KB，因此不适合 RAM 很小的目标，且不保证同一节拍内的触发顺序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMEOUT_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`kernel/Kconfig:817`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L817)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 超时队列后端（Timeout Queue Backend）。

**配置项引用（Symbol References）**：[`CONFIG_TIMEOUT_BACKEND`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND)、[`CONFIG_EXPERIMENTAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_TIMEOUT_BUCKET_LISTS"></a>

## 2.65 `CONFIG_TIMEOUT_BUCKET_LISTS`

**提示（Prompt）**：分桶后端每节拍桶的数量（Per-tick Buckets）。

**说明（Help）**

单节拍桶链表数量，必须是 8 至 64 之间的 2 的幂。在这些节拍内到期的超时可按 O(1) 插入，更长的超时进入排序溢出链表。增大该值可扩大 O(1) 时间窗口，代价是更多静态 RAM，每个桶需要一个链表头。少于 8 个桶时，普通差值链表后端可能更合适。桶数不超过 32 时，占用位图使用 `uint32_t`，超过时使用 `uint64_t`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TIMEOUT_BACKEND_BUCKET
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[8, 64]
```

**定义位置（Location）**：[`kernel/Kconfig:857`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L857)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_TIMEOUT_BACKEND_BUCKET`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND_BUCKET)。

<a id="CONFIG_TIMEOUT_HEAP_MAX_ENTRIES"></a>

## 2.66 `CONFIG_TIMEOUT_HEAP_MAX_ENTRIES`

**提示（Prompt）**：堆中同时待处理超时的最大数量。

**说明（Help）**

超时最小堆数组的静态容量。应设为应用所需同时待处理超时的峰值数量，可先统计活动线程（每个可能有一个待处理超时）、活动 `k_timer` 实例、可延迟工作项，以及网络／套接字超时。溢出会在运行时触发 `k_panic()`。若出现意外的内核致命错误，应增大此值并重新构建。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TIMEOUT_BACKEND_MINHEAP
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`kernel/Kconfig:883`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L883)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_TIMEOUT_BACKEND_MINHEAP`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND_MINHEAP)。

<a id="CONFIG_TIMEOUT_SKIPLIST_MAX_LEVEL"></a>

## 2.67 `CONFIG_TIMEOUT_SKIPLIST_MAX_LEVEL`

**提示（Prompt）**：跳表最大高度（Maximum Skip-list Height）。

**说明（Help）**

每个超时节点中前向指针层级的最大数量。高度服从参数为 1/2 的几何分布，因此只要该值至少等于待处理超时峰值数量的 log2，期望搜索复杂度就是 O(log n)。每增加一层，每个 `struct _timeout` 都增加一个指针，包括 `k_timer`、`k_thread`、可延迟工作项等使用的结构。8 层可从容处理数百个并发超时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TIMEOUT_BACKEND_SKIPLIST
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[4, 16]
```

**定义位置（Location）**：[`kernel/Kconfig:870`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L870)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_TIMEOUT_BACKEND_SKIPLIST`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND_SKIPLIST)。

<a id="CONFIG_TIMER_OBSERVER"></a>

## 2.68 `CONFIG_TIMER_OBSERVER`

**提示（Prompt）**：支持 `k_timer` 生命周期扩展点（Lifecycle Extension Points）。

**说明（Help）**

增加可迭代段（Iterable Section）支持，以观察 `k_timer` 事件，允许不修改内核就扩展定时器行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`kernel/Kconfig:618`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L618)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 定时器 API 选项（Timer API Options）。

<a id="CONFIG_TIMESLICE_PER_THREAD"></a>

## 2.69 `CONFIG_TIMESLICE_PER_THREAD`

**提示（Prompt）**：支持逐线程时间片值（Per-thread Timeslice Values）。

**说明（Help）**

启用按线程设置时间片（Timeslice）的 API，并在线程用完时间片时调用应用回调。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TIMESLICING
```

**定义位置（Location）**：[`kernel/Kconfig:610`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L610)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 定时器 API 选项（Timer API Options）。 → 线程时间片轮转（Thread Time Slicing）。

**配置项引用（Symbol References）**：[`CONFIG_TIMESLICING`](P002_kernel_配置项参考_2.md#CONFIG_TIMESLICING)。

<a id="CONFIG_TIMESLICE_PRIORITY"></a>

## 2.70 `CONFIG_TIMESLICE_PRIORITY`

**提示（Prompt）**：时间片轮转的线程优先级上限（Time Slicing Priority Ceiling）。

**说明（Help）**

指定时间片轮转开始生效的线程优先级；优先级高于此上限的线程不参与时间片轮转。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TIMESLICING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, CONFIG_NUM_PREEMPT_PRIORITIES]
```

**定义位置（Location）**：[`kernel/Kconfig:600`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L600)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 定时器 API 选项（Timer API Options）。 → 线程时间片轮转（Thread Time Slicing）。

**配置项引用（Symbol References）**：[`CONFIG_TIMESLICING`](P002_kernel_配置项参考_2.md#CONFIG_TIMESLICING)、[`CONFIG_NUM_PREEMPT_PRIORITIES`](P001_kernel_配置项参考_1.md#CONFIG_NUM_PREEMPT_PRIORITIES)。

<a id="CONFIG_TIMESLICE_SIZE"></a>

## 2.71 `CONFIG_TIMESLICE_SIZE`

**提示（Prompt）**：时间片大小（Time Slice Size），单位为毫秒。

**说明（Help）**

指定线程在给同优先级其他线程运行机会之前，最多可以执行的时间。时间片大小为零表示“不限制”，即无限大的时间片。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TIMESLICING
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[0, 2147483647]
```

**定义位置（Location）**：[`kernel/Kconfig:589`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L589)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 定时器 API 选项（Timer API Options）。 → 线程时间片轮转（Thread Time Slicing）。

**配置项引用（Symbol References）**：[`CONFIG_TIMESLICING`](P002_kernel_配置项参考_2.md#CONFIG_TIMESLICING)。

<a id="CONFIG_TIMESLICING"></a>

## 2.72 `CONFIG_TIMESLICING`

**提示（Prompt）**：线程时间片轮转（Thread Time Slicing）。

**说明（Help）**

启用相同优先级的可抢占线程之间的时间片轮转（Time Slicing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS && CONFIG_NUM_PREEMPT_PRIORITIES != 0
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`kernel/Kconfig:581`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L581)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 定时器 API 选项（Timer API Options）。

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_NUM_PREEMPT_PRIORITIES`](P001_kernel_配置项参考_1.md#CONFIG_NUM_PREEMPT_PRIORITIES)。

<a id="CONFIG_TOOLCHAIN_SUPPORTS_THREAD_LOCAL_STORAGE"></a>

## 2.73 `CONFIG_TOOLCHAIN_SUPPORTS_THREAD_LOCAL_STORAGE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，表示工具链支持生成使用线程局部存储（TLS）的代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if "zephyr" = "zephyr" || "" = y
```

**定义位置（Location）**：[`kernel/Kconfig:1113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1113)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

<a id="CONFIG_TRACE_SCHED_IPI"></a>

## 2.74 `CONFIG_TRACE_SCHED_IPI`

**提示（Prompt）**：测试处理器间中断（Test IPI）。

**说明（Help）**

设为 `true` 时，在 `z_sched_ipi()` 中加入钩子，用于测试调度处理器间中断（Scheduling IPI）是否已被调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SCHED_IPI_SUPPORTED && CONFIG_MP_MAX_NUM_CPUS > 1 && CONFIG_SMP
```

**定义位置（Location）**：[`kernel/smp/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/smp/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 对称多处理选项（SMP Options）。

**配置项引用（Symbol References）**：[`CONFIG_SCHED_IPI_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_IPI_SUPPORTED)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)。

<a id="CONFIG_USERSPACE_THREAD_MAY_RAISE_PRIORITY"></a>

## 2.75 `CONFIG_USERSPACE_THREAD_MAY_RAISE_PRIORITY`

**提示（Prompt）**：线程可提高自身优先级（Raise Own Priority）。

**说明（Help）**

线程可在用户空间模式（Userspace Mode）下提高自身优先级。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TEST && CONFIG_USERSPACE
```

**定义位置（Location）**：[`kernel/userspace/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/userspace/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST)、[`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE)。

<a id="CONFIG_USE_SWITCH"></a>

## 2.76 `CONFIG_USE_SWITCH`

**提示（Prompt）**：使用新式 `_arch_switch` 替代 `arch_swap`。

**说明（Help）**

与原有 `arch_swap` 机制相比，`_arch_switch()` API 是更底层的上下文切换原语（Context-switching Primitive）。支持 SMP 的调度器需要它；架构不提供 `arch_swap` 时也需要它。在架构同时提供两者的单处理器场景中，`_arch_switch` 的开销稍大，可能更慢。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SWITCH_SUPPORTED
```

**被选择（Selected by）**

```text
CONFIG_SOC_PIC64GX1000
CONFIG_SOC_POLARFIRE
CONFIG_SOC_CV32A6
CONFIG_SOC_CV64A6
CONFIG_ISA_ARCV2
CONFIG_ISA_ARCV3
CONFIG_CPU_AARCH32_ARM9
CONFIG_X86_64
CONFIG_ARM64
CONFIG_OPENRISC
CONFIG_SPARC
CONFIG_RISCV
CONFIG_XTENSA
CONFIG_TRICORE
CONFIG_HEXAGON
CONFIG_RX
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_CORSTONE300
CONFIG_SOC_CORSTONE320
```

**定义位置（Location）**：[`kernel/Kconfig:1085`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1085)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SWITCH_SUPPORTED`](P002_kernel_配置项参考_2.md#CONFIG_USE_SWITCH_SUPPORTED)、[`CONFIG_SOC_PIC64GX1000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC64GX1000)、[`CONFIG_SOC_POLARFIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_POLARFIRE)、[`CONFIG_SOC_CV32A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV32A6)、[`CONFIG_SOC_CV64A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV64A6)、[`CONFIG_ISA_ARCV2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISA_ARCV2)、[`CONFIG_ISA_ARCV3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISA_ARCV3)、[`CONFIG_CPU_AARCH32_ARM9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_ARM9)、[`CONFIG_X86_64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_64)、[`CONFIG_ARM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM64)、[`CONFIG_OPENRISC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENRISC)、[`CONFIG_SPARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPARC)、[`CONFIG_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV)、[`CONFIG_XTENSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA)、[`CONFIG_TRICORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRICORE)、[`CONFIG_HEXAGON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HEXAGON)、[`CONFIG_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RX)、[`CONFIG_SOC_CORSTONE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE300)、[`CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE320)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_PIC64GX1000`、`CONFIG_SOC_CORSTONE300`、`CONFIG_SOC_CORSTONE320`。

<a id="CONFIG_USE_SWITCH_SUPPORTED"></a>

## 2.77 `CONFIG_USE_SWITCH_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示当前启用的平台是否支持 `_arch_switch()` API。实现此 API 的平台应选择本选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_PIC64GX1000
CONFIG_SOC_POLARFIRE
CONFIG_SOC_CV32A6
CONFIG_SOC_CV64A6
CONFIG_ISA_ARCV2
CONFIG_ISA_ARCV3
CONFIG_CPU_AARCH32_ARM9
CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_ARMV7_M_ARMV8_M_MAINLINE
CONFIG_X86_64
CONFIG_ARM64
CONFIG_OPENRISC
CONFIG_SPARC
CONFIG_RISCV
CONFIG_XTENSA
CONFIG_TRICORE
CONFIG_HEXAGON
CONFIG_RX
```

**定义位置（Location）**：[`kernel/Kconfig:1096`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L1096)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_PIC64GX1000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_PIC64GX1000)、[`CONFIG_SOC_POLARFIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_POLARFIRE)、[`CONFIG_SOC_CV32A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV32A6)、[`CONFIG_SOC_CV64A6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV64A6)、[`CONFIG_ISA_ARCV2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISA_ARCV2)、[`CONFIG_ISA_ARCV3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISA_ARCV3)、[`CONFIG_CPU_AARCH32_ARM9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_ARM9)、[`CONFIG_CPU_AARCH32_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_CPU_AARCH32_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_X86_64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_64)、[`CONFIG_ARM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM64)、[`CONFIG_OPENRISC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENRISC)、[`CONFIG_SPARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPARC)、[`CONFIG_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV)、[`CONFIG_XTENSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA)、[`CONFIG_TRICORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRICORE)、[`CONFIG_HEXAGON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HEXAGON)、[`CONFIG_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_PIC64GX1000`。

<a id="CONFIG_WAITQ_ALGORITHM"></a>

## 2.78 `CONFIG_WAITQ_ALGORITHM`

**提示（Prompt）**：等待队列优先级算法（Wait Queue Priority Algorithm）。

**说明（Help）**

进程间通信（IPC）原语使用 `wait_q` 抽象挂起线程，等待日后唤醒。它与调度器共享相同的后端数据结构选择，并可使用相同选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
CONFIG_WAITQ_SIMPLE
```

**可选项（Choices）**

```text
CONFIG_WAITQ_SCALABLE
CONFIG_WAITQ_SIMPLE
```

**定义位置（Location）**：[`kernel/Kconfig:323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L323)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

**配置项引用（Symbol References）**：[`CONFIG_WAITQ_SIMPLE`](P002_kernel_配置项参考_2.md#CONFIG_WAITQ_SIMPLE)、[`CONFIG_WAITQ_SCALABLE`](P002_kernel_配置项参考_2.md#CONFIG_WAITQ_SCALABLE)。

<a id="CONFIG_WAITQ_SCALABLE"></a>

## 2.79 `CONFIG_WAITQ_SCALABLE`

**提示（Prompt）**：使用可扩展的 `wait_q` 实现（Scalable Wait Queue）。

**说明（Help）**

选择后，`wait_q` 使用平衡树（Balanced Tree）实现。若预期许多线程等待同一个原语，可选择此项。如果应用其他位置未使用红黑树（Red/Black Tree），相较 `WAITQ_SIMPLE`，代码大小约增加 2 kB，此开销可与 `SCHED_SCALABLE` 共享；小队列的挂起／解除挂起（Pend/Unpend）操作会稍慢，不过通常不属于性能关键路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WAITQ_ALGORITHM>
```

**定义位置（Location）**：[`kernel/Kconfig:332`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L332)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 等待队列优先级算法（Wait Queue Priority Algorithm）。

**配置项引用（Symbol References）**：[`CONFIG_WAITQ_ALGORITHM`](P002_kernel_配置项参考_2.md#CONFIG_WAITQ_ALGORITHM)。

<a id="CONFIG_WAITQ_SIMPLE"></a>

## 2.80 `CONFIG_WAITQ_SIMPLE`

**提示（Prompt）**：简单链表等待队列（Simple Linked-list `wait_q`）。

**说明（Help）**

选择后，`wait_q` 使用双向链表（Doubly Linked List）实现。若预期只有少数线程阻塞在任一 IPC 原语上，可选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WAITQ_ALGORITHM>
```

**定义位置（Location）**：[`kernel/Kconfig:344`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L344)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。 → 等待队列优先级算法（Wait Queue Priority Algorithm）。

**配置项引用（Symbol References）**：[`CONFIG_WAITQ_ALGORITHM`](P002_kernel_配置项参考_2.md#CONFIG_WAITQ_ALGORITHM)。

<a id="CONFIG_WORKQUEUE_WORK_TIMEOUT"></a>

## 2.81 `CONFIG_WORKQUEUE_WORK_TIMEOUT`

**提示（Prompt）**：支持工作队列工作项超时监视（Workqueue Work Timeout Monitoring）。

**说明（Help）**

启用后，工作队列监视每个工作项的持续时间。如果工作项处理函数执行超过指定时长，则中止工作队列线程，并记录错误。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`kernel/Kconfig:520`](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/Kconfig#L520)。

**菜单路径（Menu Path）**：顶层（Top） → 通用内核选项（General Kernel Options）。

<!-- kconfig-navigation -->

[上一章](P001_kernel_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P003_Kconfig.zephyr_配置项参考_1.md)
