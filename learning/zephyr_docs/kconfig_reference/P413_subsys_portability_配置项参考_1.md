---
id: learning.zephyr-docs.kconfig-reference.page-413
title: "`subsys/portability`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第413章\_`subsys/portability`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `subsys/portability` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CMSIS_MUTEX_MAX_COUNT"></a>

## 413.1 `CONFIG_CMSIS_MUTEX_MAX_COUNT`

**提示（Prompt）**：CMSIS 应用中互斥锁（Mutex）的最大数量

**说明（Help）**

指定符合 CMSIS 的应用中互斥锁（Mutex）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V1
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v1/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v1/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v1 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V1`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V1)。

<a id="CONFIG_CMSIS_RTOS_V1"></a>

## 413.2 `CONFIG_CMSIS_RTOS_V1`

**提示（Prompt）**：CMSIS 实时操作系统（RTOS）v1 API

**说明（Help）**

启用 CMSIS RTOS v1 API 支持。这是一个操作系统集成层（OS-integration layer），使使用 CMSIS RTOS API 的应用能够在 Zephyr 上构建。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_CUSTOM_DATA && CONFIG_THREAD_STACK_INFO
```

**主动选择（Selects）**

```text
CONFIG_THREAD_ABORT_HOOK
CONFIG_POLL
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v1/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v1/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_CUSTOM_DATA`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_CUSTOM_DATA)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_THREAD_ABORT_HOOK`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_ABORT_HOOK)、[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)。

<a id="CONFIG_CMSIS_RTOS_V2"></a>

## 413.3 `CONFIG_CMSIS_RTOS_V2`

**提示（Prompt）**：CMSIS 实时操作系统（RTOS）v2 API

**说明（Help）**

启用 CMSIS RTOS v2 API 支持。这是一个操作系统集成层（OS-integration layer），使使用 CMSIS RTOS v2 API 的应用能够在 Zephyr 上构建。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_NAME && CONFIG_THREAD_STACK_INFO && CONFIG_THREAD_MONITOR && CONFIG_INIT_STACKS && CONFIG_NUM_PREEMPT_PRIORITIES >= 56
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
CONFIG_POLL
```

**被选择（Selected by）**

```text
CONFIG_SILABS_SIWX91X_NWP
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_INIT_STACKS`](P001_kernel_配置项参考_1.md#CONFIG_INIT_STACKS)、[`CONFIG_NUM_PREEMPT_PRIORITIES`](P001_kernel_配置项参考_1.md#CONFIG_NUM_PREEMPT_PRIORITIES)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)、[`CONFIG_SILABS_SIWX91X_NWP`](P308_soc_silabs_配置项参考_1.md#CONFIG_SILABS_SIWX91X_NWP)。

<a id="CONFIG_CMSIS_SEMAPHORE_MAX_COUNT"></a>

## 413.4 `CONFIG_CMSIS_SEMAPHORE_MAX_COUNT`

**提示（Prompt）**：CMSIS 应用中信号量（Semaphore）的最大数量

**说明（Help）**

指定符合 CMSIS 的应用中信号量（Semaphore）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V1
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v1/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v1/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v1 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V1`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V1)。

<a id="CONFIG_CMSIS_THREAD_MAX_STACK_SIZE"></a>

## 413.5 `CONFIG_CMSIS_THREAD_MAX_STACK_SIZE`

**提示（Prompt）**：CMSIS RTOS 应用可为线程分配的最大栈大小（Stack size）

**说明（Help）**

指定 CMSIS RTOS 应用可为线程分配的最大栈大小（Stack size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V1
```

**默认值（Defaults）**

```text
4096 if CONFIG_COVERAGE_GCOV
512
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v1/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v1/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v1 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V1`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V1)、[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)。

<a id="CONFIG_CMSIS_TIMER_MAX_COUNT"></a>

## 413.6 `CONFIG_CMSIS_TIMER_MAX_COUNT`

**提示（Prompt）**：CMSIS 应用中定时器（Timer）的最大数量

**说明（Help）**

指定符合 CMSIS 的应用中定时器（Timer）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V1
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v1/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v1/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v1 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V1`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V1)。

<a id="CONFIG_CMSIS_V2_EVT_FLAGS_MAX_COUNT"></a>

## 413.7 `CONFIG_CMSIS_V2_EVT_FLAGS_MAX_COUNT`

**提示（Prompt）**：CMSIS RTOS v2 应用可动态分配的事件标志（Event flag）最大数量

**说明（Help）**

指定符合 CMSIS RTOS v2 的应用中，可通过动态分配控制块（Control block）创建的事件标志（Event flag）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V2
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v2 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V2`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V2)。

<a id="CONFIG_CMSIS_V2_MEM_SLAB_MAX_COUNT"></a>

## 413.8 `CONFIG_CMSIS_V2_MEM_SLAB_MAX_COUNT`

**提示（Prompt）**：CMSIS RTOS v2 应用可动态分配的内存池（Memory pool）最大数量

**说明（Help）**

指定符合 CMSIS RTOS v2 的应用中，可通过动态分配控制块（Control block）创建的内存块池（Memory slab）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V2
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v2 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V2`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V2)。

<a id="CONFIG_CMSIS_V2_MEM_SLAB_MAX_DYNAMIC_SIZE"></a>

## 413.9 `CONFIG_CMSIS_V2_MEM_SLAB_MAX_DYNAMIC_SIZE`

**提示（Prompt）**：CMSIS RTOS v2 应用动态内存块池（Memory slab/pool）的最大大小

**说明（Help）**

指定符合 CMSIS RTOS v2 的应用中，动态内存块池（Memory slab/pool）的最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V2
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v2 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V2`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V2)。

<a id="CONFIG_CMSIS_V2_MSGQ_MAX_COUNT"></a>

## 413.10 `CONFIG_CMSIS_V2_MSGQ_MAX_COUNT`

**提示（Prompt）**：CMSIS RTOS v2 应用可动态分配的消息队列（Message queue）最大数量

**说明（Help）**

指定符合 CMSIS RTOS v2 的应用中，可通过动态分配控制块（Control block）创建的消息队列（Message queue）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V2
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v2 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V2`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V2)。

<a id="CONFIG_CMSIS_V2_MSGQ_MAX_DYNAMIC_SIZE"></a>

## 413.11 `CONFIG_CMSIS_V2_MSGQ_MAX_DYNAMIC_SIZE`

**提示（Prompt）**：CMSIS RTOS v2 应用动态消息队列（Message queue）的最大大小

**说明（Help）**

指定符合 CMSIS RTOS v2 的应用中，动态消息队列（Message queue）的最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V2
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v2 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V2`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V2)。

<a id="CONFIG_CMSIS_V2_MUTEX_MAX_COUNT"></a>

## 413.12 `CONFIG_CMSIS_V2_MUTEX_MAX_COUNT`

**提示（Prompt）**：CMSIS RTOS v2 应用可动态分配的互斥锁（Mutex）最大数量

**说明（Help）**

指定符合 CMSIS RTOS v2 的应用中，可通过动态分配控制块（Control block）创建的互斥锁（Mutex）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V2
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v2 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V2`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V2)。

<a id="CONFIG_CMSIS_V2_SEMAPHORE_MAX_COUNT"></a>

## 413.13 `CONFIG_CMSIS_V2_SEMAPHORE_MAX_COUNT`

**提示（Prompt）**：CMSIS RTOS v2 应用可动态分配的信号量（Semaphore）最大数量

**说明（Help）**

指定符合 CMSIS RTOS v2 的应用中，可通过动态分配控制块（Control block）创建的信号量（Semaphore）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V2
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v2 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V2`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V2)。

<a id="CONFIG_CMSIS_V2_THREAD_DYNAMIC_MAX_COUNT"></a>

## 413.14 `CONFIG_CMSIS_V2_THREAD_DYNAMIC_MAX_COUNT`

**提示（Prompt）**：CMSIS RTOS v2 应用使用动态栈（Dynamic stack）的最大线程数

**说明（Help）**

CMSIS RTOS v2 应用中，可使用动态分配栈（Dynamically allocated stack）创建的线程最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V2
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v2 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V2`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V2)。

<a id="CONFIG_CMSIS_V2_THREAD_DYNAMIC_STACK_SIZE"></a>

## 413.15 `CONFIG_CMSIS_V2_THREAD_DYNAMIC_STACK_SIZE`

**提示（Prompt）**：CMSIS RTOS v2 应用为线程分配的动态栈大小（Dynamic stack size）

**说明（Help）**

指定 CMSIS RTOS v2 应用为线程分配的动态栈大小（Dynamic stack size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V2
```

**默认值（Defaults）**

```text
4096 if CONFIG_COVERAGE_GCOV
512
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v2 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V2`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V2)、[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)。

<a id="CONFIG_CMSIS_V2_THREAD_MAX_COUNT"></a>

## 413.16 `CONFIG_CMSIS_V2_THREAD_MAX_COUNT`

**提示（Prompt）**：CMSIS RTOS v2 应用使用动态控制块（Dynamic control block）的最大线程数

**说明（Help）**

CMSIS RTOS v2 应用中，可使用动态分配控制块（Dynamically allocated control block）创建的线程最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V2
```

**默认值（Defaults）**

```text
15
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v2 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V2`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V2)。

<a id="CONFIG_CMSIS_V2_THREAD_MAX_STACK_SIZE"></a>

## 413.17 `CONFIG_CMSIS_V2_THREAD_MAX_STACK_SIZE`

**提示（Prompt）**：CMSIS RTOS v2 应用可为线程分配的最大栈大小（Stack size）

**说明（Help）**

指定 CMSIS RTOS v2 应用可为线程分配的最大栈大小（Stack size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V2
```

**默认值（Defaults）**

```text
4096 if CONFIG_COVERAGE_GCOV
512
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v2 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V2`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V2)、[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)。

<a id="CONFIG_CMSIS_V2_TIMER_MAX_COUNT"></a>

## 413.18 `CONFIG_CMSIS_V2_TIMER_MAX_COUNT`

**提示（Prompt）**：CMSIS RTOS v2 应用可动态分配的定时器（Timer）最大数量

**说明（Help）**

指定符合 CMSIS RTOS v2 的应用中，可通过动态分配控制块（Control block）创建的定时器（Timer）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSIS_RTOS_V2
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/portability/cmsis_rtos_v2/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v2/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → CMSIS 实时操作系统（RTOS）v2 API

**配置项引用（Symbol References）**：[`CONFIG_CMSIS_RTOS_V2`](P413_subsys_portability_配置项参考_1.md#CONFIG_CMSIS_RTOS_V2)。

<a id="CONFIG_EVENTFD"></a>

## 413.19 `CONFIG_EVENTFD`

**提示（Prompt）**：事件文件描述符（eventfd）支持

**说明（Help）**

启用事件文件描述符（Event file descriptor，eventfd）支持。eventfd 可配合 POSIX 的 `read`、`write` 和 `poll` 等调用，实现事件等待与通知（Wait/notify）机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ZVFS
CONFIG_ZVFS_EVENTFD
```

**被弱选择（Implied by）**

```text
CONFIG_POSIX_API
```

**定义位置（Location）**：[`subsys/portability/posix/eventfd/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/eventfd/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability）

**配置项引用（Symbol References）**：[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_EVENTFD`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_EVENTFD)、[`CONFIG_POSIX_API`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_API)。

<a id="CONFIG_MAX_PTHREAD_BARRIER_COUNT"></a>

## 413.20 `CONFIG_MAX_PTHREAD_BARRIER_COUNT`

**提示（Prompt）**：POSIX 屏障（Barrier）的最大数量

**说明（Help）**

POSIX 应用中可同时处于活动状态的 `pthread_barrier_t` 的最大数量。注意，这是非标准选项（Non-standard option）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_BARRIERS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.barrier:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.barrier#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 屏障（barriers）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_BARRIERS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BARRIERS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_MAX_PTHREAD_COND_COUNT"></a>

## 413.21 `CONFIG_MAX_PTHREAD_COND_COUNT`

**提示（Prompt）**：POSIX 条件变量（Condition variable）的最大数量

**说明（Help）**

POSIX 应用中可同时处于活动状态的条件变量（Condition variable）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_MAX_PTHREAD_MUTEX_COUNT"></a>

## 413.22 `CONFIG_MAX_PTHREAD_MUTEX_COUNT`

**提示（Prompt）**：POSIX 互斥锁（Mutex）的最大数量

**说明（Help）**

POSIX 应用中可同时处于活动状态的互斥锁（Mutex）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_MAX_PTHREAD_RWLOCK_COUNT"></a>

## 413.23 `CONFIG_MAX_PTHREAD_RWLOCK_COUNT`

**提示（Prompt）**：POSIX 读写锁（Reader-writer lock）的最大数量

**说明（Help）**

POSIX 应用中可同时处于活动状态的读写锁（Reader-writer lock）的最大数量。注意，这是非标准选项（Non-standard option）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_RW_LOCKS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.rwlock:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.rwlock#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 读写锁（reader-writer locks）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_RW_LOCKS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_RW_LOCKS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_MAX_PTHREAD_SPINLOCK_COUNT"></a>

## 413.24 `CONFIG_MAX_PTHREAD_SPINLOCK_COUNT`

**提示（Prompt）**：POSIX 自旋锁（Spin lock）的最大数量

**说明（Help）**

POSIX 应用中可同时处于活动状态的自旋锁（Spin lock）的最大数量。注意，这是非标准选项（Non-standard option）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SPIN_LOCKS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.spinlock:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.spinlock#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 自旋锁（spin locks）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SPIN_LOCKS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SPIN_LOCKS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_MQUEUE_NAMELEN_MAX"></a>

## 413.25 `CONFIG_MQUEUE_NAMELEN_MAX`

**提示（Prompt）**：POSIX 消息队列名称（Message queue name）的最大大小

**说明（Help）**

指定消息队列名称（Message queue name）的大小，以字符数表示。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_MESSAGE_PASSING && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[2, 255]
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.mqueue:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.mqueue#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 消息队列（Message queue）支持

**配置项引用（Symbol References）**：[`CONFIG_POSIX_MESSAGE_PASSING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MESSAGE_PASSING)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_MSG_SIZE_MAX"></a>

## 413.26 `CONFIG_MSG_SIZE_MAX`

**提示（Prompt）**：POSIX 消息（Message）的最大大小

**说明（Help）**

指定消息（Message）的最大大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_MESSAGE_PASSING && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.mqueue:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.mqueue#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 消息队列（Message queue）支持

**配置项引用（Symbol References）**：[`CONFIG_POSIX_MESSAGE_PASSING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MESSAGE_PASSING)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_AEP_CHOICE"></a>

## 413.27 `CONFIG_POSIX_AEP_CHOICE`

**提示（Prompt）**：POSIX 子配置文件（Subprofile）

**说明（Help）**

帮助用户为应用选择合适的 POSIX 配置文件（Profile）。这些选项基于 IEEE 1003.13-2003，目前已不再活动并处于保留状态，再扩展到 IEEE 1003.3-2017 中较新的子配置文件选项组（Subprofiling Option Groups）。更多信息参见 [IEEE 1003.13](https://standards.ieee.org/ieee/1003.13/3322/) 和 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

译注（引用状态）：本次直接请求 IEEE 原始链接返回 HTTP 403，网页工具两次打开均超时。官方搜索索引可确认标准名称和 Inactive-Reserved 状态，但未取得实时页面正文。保留原始链接，本条翻译仍依据保存的 Zephyr 官方配置数据库。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
CONFIG_POSIX_AEP_CHOICE_ZEPHYR
```

**可选项（Choices）**

```text
CONFIG_POSIX_AEP_CHOICE_NONE
CONFIG_POSIX_AEP_CHOICE_ZEPHYR
CONFIG_POSIX_AEP_CHOICE_BASE
CONFIG_POSIX_AEP_CHOICE_PSE51
CONFIG_POSIX_AEP_CHOICE_PSE52
CONFIG_POSIX_AEP_CHOICE_PSE53
CONFIG_POSIX_AEP_CHOICE_NETAPP
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_AEP_CHOICE_ZEPHYR`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_ZEPHYR)、[`CONFIG_POSIX_AEP_CHOICE_NONE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_NONE)、[`CONFIG_POSIX_AEP_CHOICE_BASE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_BASE)、[`CONFIG_POSIX_AEP_CHOICE_PSE51`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE51)、[`CONFIG_POSIX_AEP_CHOICE_PSE52`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE52)、[`CONFIG_POSIX_AEP_CHOICE_PSE53`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE53)、[`CONFIG_POSIX_AEP_CHOICE_NETAPP`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_NETAPP)。

<a id="CONFIG_POSIX_AEP_CHOICE_BASE"></a>

## 413.28 `CONFIG_POSIX_AEP_CHOICE_BASE`

**提示（Prompt）**：最小 POSIX 系统配置文件（Minimal POSIX System Profile）

**说明（Help）**

仅启用所有 POSIX 系统必需的基本定义（Base definitions）。详见 [POSIX 基本定义要求](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap02.html#tag_02_01_03_01)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_AEP_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 子配置文件（Subprofile）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_AEP_CHOICE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<a id="CONFIG_POSIX_AEP_CHOICE_NETAPP"></a>

## 413.29 `CONFIG_POSIX_AEP_CHOICE_NETAPP`

**提示（Prompt）**：网络设备配置文件（Network Appliance Profile）

**说明（Help）**

这是 Zephyr 自定义的配置文件（Profile），不对应标准 POSIX 子配置文件。它包含 PSE52 的全部功能和 PSE53 的网络接口，但不包含 PSE53 的多进程、管道（Pipe）、进程生成（Spawn）或零星服务器（Sporadic server）接口。适用于无需进程管理的联网应用。只有启用 `CONFIG_NETWORKING` 时，才启用其中的网络接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_AEP_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
CONFIG_POSIX_BASE_DEFINITIONS
CONFIG_POSIX_AEP_REALTIME_MINIMAL
CONFIG_POSIX_AEP_REALTIME_CONTROLLER
CONFIG_POSIX_NETWORKING if CONFIG_NETWORKING
CONFIG_POSIX_RAW_SOCKETS if CONFIG_NETWORKING
CONFIG_POSIX_CPUTIME
CONFIG_POSIX_PRIORITY_SCHEDULING
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 子配置文件（Subprofile）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_AEP_CHOICE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)、[`CONFIG_POSIX_AEP_REALTIME_CONTROLLER`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_CONTROLLER)、[`CONFIG_POSIX_NETWORKING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_NETWORKING)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_POSIX_RAW_SOCKETS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_RAW_SOCKETS)、[`CONFIG_POSIX_CPUTIME`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_CPUTIME)、[`CONFIG_POSIX_PRIORITY_SCHEDULING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_PRIORITY_SCHEDULING)。

<a id="CONFIG_POSIX_AEP_CHOICE_NONE"></a>

## 413.30 `CONFIG_POSIX_AEP_CHOICE_NONE`

**提示（Prompt）**：不使用 POSIX 子配置文件（No POSIX subprofile）

**说明（Help）**

不选择任何 POSIX 子配置文件（Subprofile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_AEP_CHOICE>
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 子配置文件（Subprofile）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_AEP_CHOICE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE)。

<a id="CONFIG_POSIX_AEP_CHOICE_PSE51"></a>

## 413.31 `CONFIG_POSIX_AEP_CHOICE_PSE51`

**提示（Prompt）**：最小实时系统配置文件（Minimal Realtime System Profile，PSE51）

**说明（Help）**

PSE51 包含 POSIX 基本定义，即系统接口（System Interfaces），以及支持设备 I/O、信号（Signal）、必需配置工具和线程（Threading）的多个选项及选项组。详见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_AEP_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
CONFIG_POSIX_BASE_DEFINITIONS
CONFIG_POSIX_AEP_REALTIME_MINIMAL
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 子配置文件（Subprofile）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_AEP_CHOICE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)。

<a id="CONFIG_POSIX_AEP_CHOICE_PSE52"></a>

## 413.32 `CONFIG_POSIX_AEP_CHOICE_PSE52`

**提示（Prompt）**：实时控制器系统配置文件（Realtime Controller System Profile，PSE52）

**说明（Help）**

PSE52 包含 POSIX 基本定义，即系统接口（System Interfaces），以及 PSE51 的全部功能，并增加文件描述符管理（File descriptor management）、文件系统、消息队列（Message queue）和跟踪（Tracing）接口。详见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_AEP_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
CONFIG_POSIX_BASE_DEFINITIONS
CONFIG_POSIX_AEP_REALTIME_MINIMAL
CONFIG_POSIX_AEP_REALTIME_CONTROLLER
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 子配置文件（Subprofile）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_AEP_CHOICE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)、[`CONFIG_POSIX_AEP_REALTIME_CONTROLLER`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_CONTROLLER)。

<a id="CONFIG_POSIX_AEP_CHOICE_PSE53"></a>

## 413.33 `CONFIG_POSIX_AEP_CHOICE_PSE53`

**提示（Prompt）**：专用实时系统配置文件（Dedicated Realtime System Profile，PSE53）

**说明（Help）**

PSE53 包含 POSIX 基本定义，即系统接口（System Interfaces），以及 PSE52 的全部功能，并增加 POSIX 多进程（Multi-processing）、网络、管道（Pipe）和优先级 I/O（Prioritized I/O）接口。详见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_AEP_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
CONFIG_POSIX_BASE_DEFINITIONS
CONFIG_POSIX_AEP_REALTIME_MINIMAL
CONFIG_POSIX_AEP_REALTIME_CONTROLLER
CONFIG_POSIX_AEP_REALTIME_DEDICATED
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 子配置文件（Subprofile）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_AEP_CHOICE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)、[`CONFIG_POSIX_AEP_REALTIME_CONTROLLER`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_CONTROLLER)、[`CONFIG_POSIX_AEP_REALTIME_DEDICATED`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_DEDICATED)。

<a id="CONFIG_POSIX_AEP_CHOICE_ZEPHYR"></a>

## 413.34 `CONFIG_POSIX_AEP_CHOICE_ZEPHYR`

**提示（Prompt）**：最小 Zephyr 系统配置文件（Minimal Zephyr System Profile）

**说明（Help）**

Zephyr 要求整个构建环境中可用某些 POSIX 函数，例如 `gmtime_r()`、`strnlen()`、`strtok_r()` 等。这些函数分属 `POSIX_C_LIB_EXT` 和 `POSIX_C_LANG_SUPPORT_R` 两个独立选项组（Option Group），可不依赖 POSIX API 的其余实现而分别启用。如果 Zephyr 内核或应用未引用它们，启用这些组不会带来资源开销。此子配置文件为 Zephyr 自定义，不同于预定义的标准 POSIX 子配置文件，因此无需包含符合 POSIX 的系统或子配置文件原本必需的基本定义和系统接口。本配置文件自身不满足 POSIX 实现符合性（Implementation conformance）要求。更多信息参见 [Zephyr 编码规范](https://docs.zephyrproject.org/latest/contribute/coding_guidelines/index.html) 和 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_AEP_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_POSIX_C_LIB_EXT
CONFIG_POSIX_C_LANG_SUPPORT_R
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 子配置文件（Subprofile）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_AEP_CHOICE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE)、[`CONFIG_POSIX_C_LIB_EXT`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_C_LIB_EXT)、[`CONFIG_POSIX_C_LANG_SUPPORT_R`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_C_LANG_SUPPORT_R)。

<a id="CONFIG_POSIX_AEP_REALTIME_CONTROLLER"></a>

## 413.35 `CONFIG_POSIX_AEP_REALTIME_CONTROLLER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项不可由用户直接配置，可通过选择 `CONFIG_POSIX_AEP_CHOICE_PSE52=y` 间接配置。详见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_POSIX_FD_MGMT
CONFIG_POSIX_FILE_SYSTEM
CONFIG_POSIX_MESSAGE_PASSING
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_CHOICE_PSE52
CONFIG_POSIX_AEP_CHOICE_PSE53
CONFIG_POSIX_AEP_CHOICE_NETAPP
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L186)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_FD_MGMT`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_FD_MGMT)、[`CONFIG_POSIX_FILE_SYSTEM`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_FILE_SYSTEM)、[`CONFIG_POSIX_MESSAGE_PASSING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MESSAGE_PASSING)、[`CONFIG_POSIX_AEP_CHOICE_PSE52`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE52)、[`CONFIG_POSIX_AEP_CHOICE_PSE53`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE53)、[`CONFIG_POSIX_AEP_CHOICE_NETAPP`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_NETAPP)。

<a id="CONFIG_POSIX_AEP_REALTIME_DEDICATED"></a>

## 413.36 `CONFIG_POSIX_AEP_REALTIME_DEDICATED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项不可由用户直接配置，可通过选择 `CONFIG_POSIX_AEP_CHOICE_PSE53=y` 间接配置。详见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_POSIX_MULTI_PROCESS
CONFIG_POSIX_NETWORKING
CONFIG_POSIX_CPUTIME
CONFIG_POSIX_PRIORITY_SCHEDULING
CONFIG_POSIX_RAW_SOCKETS
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_CHOICE_PSE53
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_MULTI_PROCESS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MULTI_PROCESS)、[`CONFIG_POSIX_NETWORKING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_NETWORKING)、[`CONFIG_POSIX_CPUTIME`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_CPUTIME)、[`CONFIG_POSIX_PRIORITY_SCHEDULING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_PRIORITY_SCHEDULING)、[`CONFIG_POSIX_RAW_SOCKETS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_RAW_SOCKETS)、[`CONFIG_POSIX_AEP_CHOICE_PSE53`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE53)。

<a id="CONFIG_POSIX_AEP_REALTIME_MINIMAL"></a>

## 413.37 `CONFIG_POSIX_AEP_REALTIME_MINIMAL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项不可由用户直接配置，可通过选择 `CONFIG_POSIX_AEP_CHOICE_PSE51=y` 间接配置。详见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_POSIX_DEVICE_IO
CONFIG_POSIX_SIGNALS
CONFIG_POSIX_SINGLE_PROCESS
CONFIG_XSI_THREADS_EXT
CONFIG_POSIX_FSYNC
CONFIG_POSIX_MEMLOCK
CONFIG_POSIX_MEMLOCK_RANGE
CONFIG_POSIX_MONOTONIC_CLOCK
CONFIG_POSIX_SHARED_MEMORY_OBJECTS
CONFIG_POSIX_SYNCHRONIZED_IO
CONFIG_POSIX_THREAD_ATTR_STACKADDR
CONFIG_POSIX_THREAD_ATTR_STACKSIZE
CONFIG_POSIX_THREAD_CPUTIME
CONFIG_POSIX_THREAD_PRIO_INHERIT
CONFIG_POSIX_THREAD_PRIO_PROTECT
CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING
```

**被选择（Selected by）**

```text
CONFIG_POSIX_API
CONFIG_POSIX_AEP_CHOICE_PSE51
CONFIG_POSIX_AEP_CHOICE_PSE52
CONFIG_POSIX_AEP_CHOICE_PSE53
CONFIG_POSIX_AEP_CHOICE_NETAPP
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_DEVICE_IO`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_DEVICE_IO)、[`CONFIG_POSIX_SIGNALS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SIGNALS)、[`CONFIG_POSIX_SINGLE_PROCESS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SINGLE_PROCESS)、[`CONFIG_XSI_THREADS_EXT`](P414_subsys_portability_配置项参考_2.md#CONFIG_XSI_THREADS_EXT)、[`CONFIG_POSIX_FSYNC`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_FSYNC)、[`CONFIG_POSIX_MEMLOCK`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MEMLOCK)、[`CONFIG_POSIX_MEMLOCK_RANGE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MEMLOCK_RANGE)、[`CONFIG_POSIX_MONOTONIC_CLOCK`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MONOTONIC_CLOCK)、[`CONFIG_POSIX_SHARED_MEMORY_OBJECTS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SHARED_MEMORY_OBJECTS)、[`CONFIG_POSIX_SYNCHRONIZED_IO`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYNCHRONIZED_IO)、[`CONFIG_POSIX_THREAD_ATTR_STACKADDR`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_THREAD_ATTR_STACKADDR)、[`CONFIG_POSIX_THREAD_ATTR_STACKSIZE`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_THREAD_ATTR_STACKSIZE)、[`CONFIG_POSIX_THREAD_CPUTIME`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_THREAD_CPUTIME)、[`CONFIG_POSIX_THREAD_PRIO_INHERIT`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_THREAD_PRIO_INHERIT)、[`CONFIG_POSIX_THREAD_PRIO_PROTECT`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_THREAD_PRIO_PROTECT)、[`CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING)、[`CONFIG_POSIX_API`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_API)、[`CONFIG_POSIX_AEP_CHOICE_PSE51`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE51)、[`CONFIG_POSIX_AEP_CHOICE_PSE52`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE52)、[`CONFIG_POSIX_AEP_CHOICE_PSE53`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE53)、[`CONFIG_POSIX_AEP_CHOICE_NETAPP`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_NETAPP)。

<a id="CONFIG_POSIX_API"></a>

## 413.38 `CONFIG_POSIX_API`

**提示（Prompt）**：POSIX 应用程序编程接口（APIs）

**说明（Help）**

启用必需的 POSIX 系统接口（System Interfaces，即基本定义）、PSE51 的全部功能，以及 PSE52 的部分功能。注意，未来可能弃用此选项，改为使用子配置文件（Subprofiling）选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
CONFIG_POSIX_BASE_DEFINITIONS
CONFIG_POSIX_AEP_REALTIME_MINIMAL
CONFIG_POSIX_NETWORKING if CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_NXP_WIFI_SIGMA_AGENT
```

**弱选择（Implies）**

```text
CONFIG_EVENTFD
CONFIG_POSIX_FD_MGMT
CONFIG_POSIX_MULTI_PROCESS
CONFIG_XSI_SINGLE_PROCESS
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)、[`CONFIG_POSIX_NETWORKING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_NETWORKING)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_NXP_WIFI_SIGMA_AGENT`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SIGMA_AGENT)、[`CONFIG_EVENTFD`](P413_subsys_portability_配置项参考_1.md#CONFIG_EVENTFD)、[`CONFIG_POSIX_FD_MGMT`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_FD_MGMT)、[`CONFIG_POSIX_MULTI_PROCESS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MULTI_PROCESS)、[`CONFIG_XSI_SINGLE_PROCESS`](P414_subsys_portability_配置项参考_2.md#CONFIG_XSI_SINGLE_PROCESS)。

<a id="CONFIG_POSIX_ASYNCHRONOUS_IO"></a>

## 413.39 `CONFIG_POSIX_ASYNCHRONOUS_IO`

**提示（Prompt）**：POSIX 异步 I/O（Asynchronous I/O）

**说明（Help）**

启用异步 I/O（Asynchronous I/O）。此选项仅为符合性（Conformance）而提供，`<aio.h>` 中列出的全部函数都返回 -1，并将 `errno` 设为 `ENOSYS`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.aio:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.aio#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<a id="CONFIG_POSIX_BARRIERS"></a>

## 413.40 `CONFIG_POSIX_BARRIERS`

**提示（Prompt）**：POSIX 屏障（barriers）

**说明（Help）**

选择 `y` 以启用 POSIX 屏障（Barrier）。更多信息参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.barrier:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.barrier#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<a id="CONFIG_POSIX_BASE_DEFINITIONS"></a>

## 413.41 `CONFIG_POSIX_BASE_DEFINITIONS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项不可由用户直接配置，可通过选择 `CONFIG_POSIX_AEP_CHOICE_BASE=y` 间接配置。详见 [POSIX 基本定义要求](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap02.html#tag_02_01_03_01)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_POSIX_ASYNCHRONOUS_IO
CONFIG_POSIX_BARRIERS
CONFIG_POSIX_CLOCK_SELECTION
CONFIG_POSIX_MAPPED_FILES
CONFIG_POSIX_MEMORY_PROTECTION
CONFIG_POSIX_RW_LOCKS
CONFIG_POSIX_REALTIME_SIGNALS
CONFIG_POSIX_SEMAPHORES
CONFIG_POSIX_SPIN_LOCKS
CONFIG_POSIX_THREAD_SAFE_FUNCTIONS
CONFIG_POSIX_THREADS
CONFIG_POSIX_TIMEOUTS
CONFIG_POSIX_TIMERS
```

**被选择（Selected by）**

```text
CONFIG_POSIX_API
CONFIG_POSIX_AEP_CHOICE_BASE
CONFIG_POSIX_AEP_CHOICE_PSE51
CONFIG_POSIX_AEP_CHOICE_PSE52
CONFIG_POSIX_AEP_CHOICE_PSE53
CONFIG_POSIX_AEP_CHOICE_NETAPP
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig.profile:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig.profile#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_ASYNCHRONOUS_IO`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_ASYNCHRONOUS_IO)、[`CONFIG_POSIX_BARRIERS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BARRIERS)、[`CONFIG_POSIX_CLOCK_SELECTION`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_CLOCK_SELECTION)、[`CONFIG_POSIX_MAPPED_FILES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MAPPED_FILES)、[`CONFIG_POSIX_MEMORY_PROTECTION`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MEMORY_PROTECTION)、[`CONFIG_POSIX_RW_LOCKS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_RW_LOCKS)、[`CONFIG_POSIX_REALTIME_SIGNALS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_REALTIME_SIGNALS)、[`CONFIG_POSIX_SEMAPHORES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SEMAPHORES)、[`CONFIG_POSIX_SPIN_LOCKS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SPIN_LOCKS)、[`CONFIG_POSIX_THREAD_SAFE_FUNCTIONS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_THREAD_SAFE_FUNCTIONS)、[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_TIMEOUTS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_TIMEOUTS)、[`CONFIG_POSIX_TIMERS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_TIMERS)、[`CONFIG_POSIX_API`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_API)、[`CONFIG_POSIX_AEP_CHOICE_BASE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_BASE)、[`CONFIG_POSIX_AEP_CHOICE_PSE51`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE51)、[`CONFIG_POSIX_AEP_CHOICE_PSE52`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE52)、[`CONFIG_POSIX_AEP_CHOICE_PSE53`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE53)、[`CONFIG_POSIX_AEP_CHOICE_NETAPP`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_NETAPP)。

<a id="CONFIG_POSIX_CLOCK_SELECTION"></a>

## 413.42 `CONFIG_POSIX_CLOCK_SELECTION`

**提示（Prompt）**：POSIX 时钟选择（Clock selection）

**说明（Help）**

启用 POSIX 时钟选择（Clock selection）。更多信息参见 [POSIX 可移植性说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html) 和 [时钟选择相关章节](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html#tag_24_03_04)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_TIMERS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.timer:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.timer#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_TIMERS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_TIMERS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<a id="CONFIG_POSIX_CPUTIME"></a>

## 413.43 `CONFIG_POSIX_CPUTIME`

**提示（Prompt）**：POSIX 每进程 CPU 时间时钟（Per-process CPU-time clock）

**说明（Help）**

启用 `CLOCK_PROCESS_CPUTIME_ID`。更多信息参见 [POSIX 可移植性说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html)、[CPU 时间定义](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_118) 和 [CPU 时间时钟相关接口说明](https://pubs.opengroup.org/onlinepubs/9699919799/functions/V2_chap02.html#tag_15_08_05_04)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_TIMERS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_CHOICE_NETAPP
CONFIG_POSIX_AEP_REALTIME_DEDICATED
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.timer:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.timer#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_TIMERS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_TIMERS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_CHOICE_NETAPP`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_NETAPP)、[`CONFIG_POSIX_AEP_REALTIME_DEDICATED`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_DEDICATED)。

<a id="CONFIG_POSIX_C_LANG_SUPPORT_R"></a>

## 413.44 `CONFIG_POSIX_C_LANG_SUPPORT_R`

**提示（Prompt）**：线程安全的通用 ISO C 库（Thread-Safe General ISO C Library）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `POSIX_C_LANG_SUPPORT_R` 选项组（Option Group）的实现，包括 `asctime_r()`、`ctime_r()`、`gmtime_r()`、`localtime_r()`、`rand_r()`、`strerror_r()` 和 `strtok_r()`。详见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_COMMON_LIBC_ASCTIME_R if !CONFIG_TC_PROVIDES_POSIX_C_LANG_SUPPORT_R
CONFIG_COMMON_LIBC_CTIME_R if !CONFIG_TC_PROVIDES_POSIX_C_LANG_SUPPORT_R
CONFIG_COMMON_LIBC_GMTIME_R if !CONFIG_TC_PROVIDES_POSIX_C_LANG_SUPPORT_R
CONFIG_COMMON_LIBC_LOCALTIME_R_UTC if !CONFIG_TC_PROVIDES_POSIX_C_LANG_SUPPORT_R
```

**被选择（Selected by）**

```text
CONFIG_MINIMAL_LIBC_TIME
CONFIG_OCPP
CONFIG_NET_SHELL_PTP_SUPPORTED
CONFIG_POSIX_AEP_CHOICE_ZEPHYR
CONFIG_POSIX_THREAD_SAFE_FUNCTIONS
```

**定义位置（Location）**：[`subsys/portability/posix/c_lang_support_r/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/c_lang_support_r/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX C 库扩展（C Library Extensions）

**配置项引用（Symbol References）**：[`CONFIG_COMMON_LIBC_ASCTIME_R`](P197_lib_配置项参考_1.md#CONFIG_COMMON_LIBC_ASCTIME_R)、[`CONFIG_TC_PROVIDES_POSIX_C_LANG_SUPPORT_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TC_PROVIDES_POSIX_C_LANG_SUPPORT_R)、[`CONFIG_COMMON_LIBC_CTIME_R`](P197_lib_配置项参考_1.md#CONFIG_COMMON_LIBC_CTIME_R)、[`CONFIG_COMMON_LIBC_GMTIME_R`](P197_lib_配置项参考_1.md#CONFIG_COMMON_LIBC_GMTIME_R)、[`CONFIG_COMMON_LIBC_LOCALTIME_R_UTC`](P197_lib_配置项参考_1.md#CONFIG_COMMON_LIBC_LOCALTIME_R_UTC)、[`CONFIG_MINIMAL_LIBC_TIME`](P197_lib_配置项参考_1.md#CONFIG_MINIMAL_LIBC_TIME)、[`CONFIG_OCPP`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP)、[`CONFIG_NET_SHELL_PTP_SUPPORTED`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_PTP_SUPPORTED)、[`CONFIG_POSIX_AEP_CHOICE_ZEPHYR`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_ZEPHYR)、[`CONFIG_POSIX_THREAD_SAFE_FUNCTIONS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_THREAD_SAFE_FUNCTIONS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TC_PROVIDES_POSIX_C_LANG_SUPPORT_R`。

<a id="CONFIG_POSIX_C_LIB_EXT"></a>

## 413.45 `CONFIG_POSIX_C_LIB_EXT`

**提示（Prompt）**：POSIX 通用 C 库扩展（General C library extension）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `POSIX_C_LIB_EXT` 选项组（Option Group）的实现，包括 `fnmatch()`、`getopt()`、`getsubopt()`、`optarg`、`opterr`、`optind`、`optopt`、`stpcpy()`、`stpncpy()`、`strcasecmp()`、`strdup()`、`strfmon()`、`strncasecmp()`、`strndup()` 和 `strnlen()`。详见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_GETOPT
```

**被选择（Selected by）**

```text
CONFIG_HTTP_SERVER_RESOURCE_WILDCARD
CONFIG_SSH_SHELL
CONFIG_WIREGUARD_SHELL
CONFIG_POSIX_AEP_CHOICE_ZEPHYR
CONFIG_SHELL_WILDCARD
CONFIG_ZYCLICTEST_SHELL
```

**定义位置（Location）**：[`subsys/portability/posix/c_lib_ext/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/c_lib_ext/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX C 库扩展（C Library Extensions）

**配置项引用（Symbol References）**：[`CONFIG_GETOPT`](P197_lib_配置项参考_1.md#CONFIG_GETOPT)、[`CONFIG_HTTP_SERVER_RESOURCE_WILDCARD`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_RESOURCE_WILDCARD)、[`CONFIG_SSH_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_SHELL)、[`CONFIG_WIREGUARD_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_SHELL)、[`CONFIG_POSIX_AEP_CHOICE_ZEPHYR`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_ZEPHYR)、[`CONFIG_SHELL_WILDCARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_WILDCARD)、[`CONFIG_ZYCLICTEST_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZYCLICTEST_SHELL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_SHELL`、`CONFIG_WIREGUARD_SHELL`。

<a id="CONFIG_POSIX_DELAYTIMER_MAX"></a>

## 413.46 `CONFIG_POSIX_DELAYTIMER_MAX`

**提示（Prompt）**：POSIX 应用中 `timer_getoverrun()` 返回的最大计数

**说明（Help）**

控制符合 POSIX 的应用中，`timer_getoverrun()` 所反映的定时器超限（Timer overrun）最大次数。更多信息参见 [POSIX limits.h](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/limits.h.html)。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_TIMERS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.timer:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.timer#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_TIMERS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_TIMERS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_DEVICE_IO"></a>

## 413.47 `CONFIG_POSIX_DEVICE_IO`

**提示（Prompt）**：POSIX 设备 I/O（Device I/O）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `POSIX_DEVICE_IO` 选项组（Option Group）的实现，例如 `FD_CLR()`、`FD_ISSET()`、`FD_SET()`、`FD_ZERO()`、`close()`、`fdopen()`、`fileno()`、`open()`、`poll()`、`pread()`、`pselect()`、`pwrite()`、`read()`、`select()` 和 `write()`。详见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_REQUIRES_FULL_LIBC
CONFIG_ZVFS
CONFIG_ZVFS_DEFAULT_FILE_VMETHODS
CONFIG_ZVFS_POLL
CONFIG_ZVFS_SELECT
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.device_io:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.device_io#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 设备 I/O（Device I/O）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_REQUIRES_FULL_LIBC`](P198_lib_配置项参考_2.md#CONFIG_REQUIRES_FULL_LIBC)、[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_DEFAULT_FILE_VMETHODS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_DEFAULT_FILE_VMETHODS)、[`CONFIG_ZVFS_POLL`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_POLL)、[`CONFIG_ZVFS_SELECT`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_SELECT)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)。

<a id="CONFIG_POSIX_DEVICE_IO_ALIAS_CLOSE"></a>

## 413.48 `CONFIG_POSIX_DEVICE_IO_ALIAS_CLOSE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过 Kconfig 选择后，Zephyr 为 `close()` 提供别名（Alias）`_close()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_DEVICE_IO && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被弱选择（Implied by）**

```text
CONFIG_NEWLIB_LIBC
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.device_io:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.device_io#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 设备 I/O（Device I/O） → POSIX 设备 I/O（Device I/O）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_DEVICE_IO`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_DEVICE_IO)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NEWLIB_LIBC`](P198_lib_配置项参考_2.md#CONFIG_NEWLIB_LIBC)。

<a id="CONFIG_POSIX_DEVICE_IO_ALIAS_OPEN"></a>

## 413.49 `CONFIG_POSIX_DEVICE_IO_ALIAS_OPEN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过 Kconfig 选择后，Zephyr 为 `open()` 提供别名（Alias）`_open()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_DEVICE_IO && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被弱选择（Implied by）**

```text
CONFIG_NEWLIB_LIBC
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.device_io:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.device_io#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 设备 I/O（Device I/O） → POSIX 设备 I/O（Device I/O）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_DEVICE_IO`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_DEVICE_IO)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NEWLIB_LIBC`](P198_lib_配置项参考_2.md#CONFIG_NEWLIB_LIBC)。

<a id="CONFIG_POSIX_DEVICE_IO_ALIAS_READ"></a>

## 413.50 `CONFIG_POSIX_DEVICE_IO_ALIAS_READ`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过 Kconfig 选择后，Zephyr 为 `read()` 提供别名（Alias）`_read()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_DEVICE_IO && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被弱选择（Implied by）**

```text
CONFIG_NEWLIB_LIBC
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.device_io:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.device_io#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 设备 I/O（Device I/O） → POSIX 设备 I/O（Device I/O）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_DEVICE_IO`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_DEVICE_IO)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NEWLIB_LIBC`](P198_lib_配置项参考_2.md#CONFIG_NEWLIB_LIBC)。

<a id="CONFIG_POSIX_DEVICE_IO_ALIAS_WRITE"></a>

## 413.51 `CONFIG_POSIX_DEVICE_IO_ALIAS_WRITE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过 Kconfig 选择后，Zephyr 为 `write()` 提供别名（Alias）`_write()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_DEVICE_IO && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被弱选择（Implied by）**

```text
CONFIG_NEWLIB_LIBC
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.device_io:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.device_io#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 设备 I/O（Device I/O） → POSIX 设备 I/O（Device I/O）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_DEVICE_IO`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_DEVICE_IO)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NEWLIB_LIBC`](P198_lib_配置项参考_2.md#CONFIG_NEWLIB_LIBC)。

<a id="CONFIG_POSIX_ENV_SHELL"></a>

## 413.52 `CONFIG_POSIX_ENV_SHELL`

**提示（Prompt）**：命令行（Shell）支持

**说明（Help）**

此命令行（Shell）提供访问系统环境变量（Environment variable）的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_POSIX_SINGLE_PROCESS
CONFIG_POSIX_SHELL
```

**定义位置（Location）**：[`subsys/portability/posix/shell/Kconfig.env:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/shell/Kconfig.env#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 命令行工具（Shell Utilities）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_SINGLE_PROCESS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SINGLE_PROCESS)、[`CONFIG_POSIX_SHELL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SHELL)。

<a id="CONFIG_POSIX_FD_MGMT"></a>

## 413.53 `CONFIG_POSIX_FD_MGMT`

**提示（Prompt）**：POSIX 文件描述符管理（File descriptor management）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `POSIX_FD_MGMT` 选项组（Option Group）的实现，包括 `dup()`、`dup2()`、`fcntl()`、`fseeko()`、`ftello()`、`ftruncate()` 和 `lseek()`。详见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_CONTROLLER
```

**被弱选择（Implied by）**

```text
CONFIG_POSIX_API
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.fd_mgmt:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.fd_mgmt#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_CONTROLLER`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_CONTROLLER)、[`CONFIG_POSIX_API`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_API)。

<a id="CONFIG_POSIX_FD_MGMT_ALIAS_FCNTL"></a>

## 413.54 `CONFIG_POSIX_FD_MGMT_ALIAS_FCNTL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过 Kconfig 选择后，Zephyr 为 `fcntl()` 提供别名（Alias）`_fcntl()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_FD_MGMT && CONFIG_POSIX_SYSTEM_INTERFACES
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.fd_mgmt:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.fd_mgmt#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 文件描述符管理（File descriptor management）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_FD_MGMT`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_FD_MGMT)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_FD_MGMT_ALIAS_FTRUNCATE"></a>

## 413.55 `CONFIG_POSIX_FD_MGMT_ALIAS_FTRUNCATE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过 Kconfig 选择后，Zephyr 为 `ftruncate()` 提供别名（Alias）`_ftruncate()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_FD_MGMT && CONFIG_POSIX_SYSTEM_INTERFACES
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.fd_mgmt:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.fd_mgmt#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 文件描述符管理（File descriptor management）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_FD_MGMT`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_FD_MGMT)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_FD_MGMT_ALIAS_LSEEK"></a>

## 413.56 `CONFIG_POSIX_FD_MGMT_ALIAS_LSEEK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过 Kconfig 选择后，Zephyr 为 `lseek()` 提供别名（Alias）`_lseek()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_FD_MGMT && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被弱选择（Implied by）**

```text
CONFIG_NEWLIB_LIBC
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.fd_mgmt:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.fd_mgmt#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 文件描述符管理（File descriptor management）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_FD_MGMT`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_FD_MGMT)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NEWLIB_LIBC`](P198_lib_配置项参考_2.md#CONFIG_NEWLIB_LIBC)。

<a id="CONFIG_POSIX_FILE_SYSTEM"></a>

## 413.57 `CONFIG_POSIX_FILE_SYSTEM`

**提示（Prompt）**：POSIX 文件系统 API（File system API）支持

**说明（Help）**

启用 POSIX 风格的文件系统相关 API（File system API）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
y if CONFIG_POSIX_API
```

**主动选择（Selects）**

```text
CONFIG_FILE_SYSTEM
CONFIG_ZVFS
CONFIG_ZVFS_FDTABLE
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_CONTROLLER
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.fs:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.fs#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_API`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_API)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)、[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_FDTABLE`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_FDTABLE)、[`CONFIG_POSIX_AEP_REALTIME_CONTROLLER`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_CONTROLLER)。

<a id="CONFIG_POSIX_FILE_SYSTEM_ALIAS_FSTAT"></a>

## 413.58 `CONFIG_POSIX_FILE_SYSTEM_ALIAS_FSTAT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过 Kconfig 选择后，Zephyr 为 `fstat()` 提供别名（Alias）`_fstat()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_FILE_SYSTEM && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被弱选择（Implied by）**

```text
CONFIG_NEWLIB_LIBC
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.fs:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.fs#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 文件系统 API（File system API）支持

**配置项引用（Symbol References）**：[`CONFIG_POSIX_FILE_SYSTEM`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_FILE_SYSTEM)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NEWLIB_LIBC`](P198_lib_配置项参考_2.md#CONFIG_NEWLIB_LIBC)。

<a id="CONFIG_POSIX_FILE_SYSTEM_ALIAS_FSYNC"></a>

## 413.59 `CONFIG_POSIX_FILE_SYSTEM_ALIAS_FSYNC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

选择 `y` 后，Zephyr 为 `fsync()` 提供别名（Alias）`_fsync()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_FSYNC && CONFIG_POSIX_SYSTEM_INTERFACES
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.sync_io:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.sync_io#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 同步 I/O（Synchronized I/O）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_FSYNC`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_FSYNC)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_FILE_SYSTEM_R"></a>

## 413.60 `CONFIG_POSIX_FILE_SYSTEM_R`

**提示（Prompt）**：线程安全文件系统（Thread-Safe File System）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `POSIX_FILE_SYSTEM_R` 选项组（Option Group）的实现，其中包含 `readdir_r()`。详见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_FILE_SYSTEM
```

**被选择（Selected by）**

```text
CONFIG_POSIX_THREAD_SAFE_FUNCTIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.file_system_r:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.file_system_r#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)、[`CONFIG_POSIX_THREAD_SAFE_FUNCTIONS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_THREAD_SAFE_FUNCTIONS)。

<a id="CONFIG_POSIX_FSYNC"></a>

## 413.61 `CONFIG_POSIX_FSYNC`

**提示（Prompt）**：`fsync()` 支持

**说明（Help）**

选择 `y` 后，Zephyr 提供 `fsync()` 的实现。更多信息参见 [POSIX fsync() 说明](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fsync.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
CONFIG_POSIX_SYNCHRONIZED_IO
CONFIG_XSI_REALTIME
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.sync_io:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.sync_io#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 同步 I/O（Synchronized I/O）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)、[`CONFIG_POSIX_SYNCHRONIZED_IO`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYNCHRONIZED_IO)、[`CONFIG_XSI_REALTIME`](P414_subsys_portability_配置项参考_2.md#CONFIG_XSI_REALTIME)。

<a id="CONFIG_POSIX_HOST_NAME_MAX"></a>

## 413.62 `CONFIG_POSIX_HOST_NAME_MAX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

POSIX 定义的主机名（Host name）最大长度。更多细节参见 [POSIX limits.h](https://pubs.opengroup.org/onlinepubs/009695399/basedefs/limits.h.html)。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_NETWORKING && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_NET_HOSTNAME_MAX_LEN
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 网络 API（Networking API）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_NETWORKING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_NETWORKING)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NET_HOSTNAME_MAX_LEN`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_MAX_LEN)。

<a id="CONFIG_POSIX_IPV6"></a>

## 413.63 `CONFIG_POSIX_IPV6`

**提示（Prompt）**：POSIX IPv6 支持

**说明（Help）**

启用 POSIX IPv6 API 支持。更多信息参见 [POSIX 可移植性相关说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html#tag_24_03_04)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_NETWORKING && CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_NET_IPV6
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.net:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.net#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 网络 API（Networking API）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_NETWORKING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_NETWORKING)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)。

<a id="CONFIG_POSIX_MAPPED_FILES"></a>

## 413.64 `CONFIG_POSIX_MAPPED_FILES`

**提示（Prompt）**：POSIX 内存映射文件（Memory-mapped files）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `mmap()`、`msync()` 和 `munmap()` 支持。注意，此功能依赖硬件内存管理单元（MMU）；底层平台不支持 MMU 时，受影响的 POSIX API 函数可能返回 -1，并将 `errno` 设为 `ENOTSUP`。更多信息参见 [POSIX 系统接口通则](https://pubs.opengroup.org/onlinepubs/9699919799.orig/functions/V2_chap02.html) 和 [可移植性相关说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html#tag_24_03_04)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_BASE_DEFINITIONS
CONFIG_POSIX_SHARED_MEMORY_OBJECTS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.mem:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.mem#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 内存（Memory）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)、[`CONFIG_POSIX_SHARED_MEMORY_OBJECTS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SHARED_MEMORY_OBJECTS)。

<a id="CONFIG_POSIX_MEMLOCK"></a>

## 413.65 `CONFIG_POSIX_MEMLOCK`

**提示（Prompt）**：POSIX 内存锁定（Memory locking）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `mlockall()` 和 `munlockall()` 支持。注意，此功能依赖硬件内存管理单元（MMU）及按需分页（DEMAND_PAGING）；底层平台不支持其中任意一项时，受影响的 POSIX API 函数将返回 -1，并将 `errno` 设为 `ENOTSUP`。更多信息参见 [POSIX 系统接口通则](https://pubs.opengroup.org/onlinepubs/9699919799.orig/functions/V2_chap02.html) 和 [可移植性相关说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html#tag_24_03_04)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_MAPPED_FILES && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
CONFIG_XSI_REALTIME
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.mem:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.mem#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 内存（Memory） → POSIX 内存映射文件（Memory-mapped files）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_MAPPED_FILES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MAPPED_FILES)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)、[`CONFIG_XSI_REALTIME`](P414_subsys_portability_配置项参考_2.md#CONFIG_XSI_REALTIME)。

<a id="CONFIG_POSIX_MEMLOCK_RANGE"></a>

## 413.66 `CONFIG_POSIX_MEMLOCK_RANGE`

**提示（Prompt）**：POSIX 范围内存锁定（Range memory locking）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `mlock()` 和 `munlock()` 支持。注意，此功能依赖硬件内存管理单元（MMU）；底层平台不支持 MMU 时，受影响的 POSIX API 函数将返回 -1，并将 `errno` 设为 `ENOTSUP`。更多信息参见 [POSIX 系统接口通则](https://pubs.opengroup.org/onlinepubs/9699919799.orig/functions/V2_chap02.html) 和 [可移植性相关说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html#tag_24_03_04)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_MAPPED_FILES && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
CONFIG_XSI_REALTIME
```

**弱选择（Implies）**

```text
CONFIG_DEMAND_PAGING
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.mem:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.mem#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 内存（Memory） → POSIX 内存映射文件（Memory-mapped files）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_MAPPED_FILES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MAPPED_FILES)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)、[`CONFIG_XSI_REALTIME`](P414_subsys_portability_配置项参考_2.md#CONFIG_XSI_REALTIME)、[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)。

<a id="CONFIG_POSIX_MEMORY_PROTECTION"></a>

## 413.67 `CONFIG_POSIX_MEMORY_PROTECTION`

**提示（Prompt）**：POSIX 内存保护（Memory protection）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `mprotect()` 支持。更多信息参见 [POSIX 系统接口通则](https://pubs.opengroup.org/onlinepubs/9699919799.orig/functions/V2_chap02.html) 和 [可移植性相关说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html#tag_24_03_04)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.mem:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.mem#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 内存（Memory）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<a id="CONFIG_POSIX_MESSAGE_PASSING"></a>

## 413.68 `CONFIG_POSIX_MESSAGE_PASSING`

**提示（Prompt）**：POSIX 消息队列（Message queue）支持

**说明（Help）**

启用 POSIX 消息队列（Message queue）相关 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_CONTROLLER
CONFIG_XSI_REALTIME
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.mqueue:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.mqueue#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_CONTROLLER`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_CONTROLLER)、[`CONFIG_XSI_REALTIME`](P414_subsys_portability_配置项参考_2.md#CONFIG_XSI_REALTIME)。

<a id="CONFIG_POSIX_MONOTONIC_CLOCK"></a>

## 413.69 `CONFIG_POSIX_MONOTONIC_CLOCK`

**提示（Prompt）**：POSIX 单调时钟（Monotonic clock）支持

**说明（Help）**

启用 `CLOCK_MONOTONIC`。更多信息参见 [POSIX 可移植性说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html) 和 [单调时钟相关接口说明](https://pubs.opengroup.org/onlinepubs/9699919799/functions/V2_chap02.html#tag_15_08_05_03)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_TIMERS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.timer:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.timer#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_TIMERS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_TIMERS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)。

<a id="CONFIG_POSIX_MQ_OPEN_MAX"></a>

## 413.70 `CONFIG_POSIX_MQ_OPEN_MAX`

**提示（Prompt）**：POSIX 消息队列（Message queue）中的最大消息数

**说明（Help）**

指定符合 POSIX 的应用中，单个消息队列（Message queue）包含的最大消息数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_MESSAGE_PASSING && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.mqueue:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.mqueue#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 消息队列（Message queue）支持

**配置项引用（Symbol References）**：[`CONFIG_POSIX_MESSAGE_PASSING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MESSAGE_PASSING)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_MQ_PRIO_MAX"></a>

## 413.71 `CONFIG_POSIX_MQ_PRIO_MAX`

**提示（Prompt）**：POSIX 消息优先级（Message priority）的最大数量

**说明（Help）**

实现支持的消息优先级（Message priority）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_MESSAGE_PASSING && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.mqueue:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.mqueue#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 消息队列（Message queue）支持

**配置项引用（Symbol References）**：[`CONFIG_POSIX_MESSAGE_PASSING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MESSAGE_PASSING)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_MULTI_PROCESS"></a>

## 413.72 `CONFIG_POSIX_MULTI_PROCESS`

**提示（Prompt）**：POSIX 多进程（Multi-process）支持

**说明（Help）**

提供多进程（Multi-processing）支持。注意，目前 Zephyr 不支持多个进程，因此该选项组的大部分功能未实现，行为视为未定义（Undefined behaviour）。更多信息参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_SCHED_THREAD_USAGE
CONFIG_THREAD_RUNTIME_STATS
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_DEDICATED
```

**被弱选择（Implied by）**

```text
CONFIG_POSIX_API
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.procN:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.procN#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_SCHED_THREAD_USAGE`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_THREAD_USAGE)、[`CONFIG_THREAD_RUNTIME_STATS`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_RUNTIME_STATS)、[`CONFIG_POSIX_AEP_REALTIME_DEDICATED`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_DEDICATED)、[`CONFIG_POSIX_API`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_API)。

<a id="CONFIG_POSIX_MULTI_PROCESS_ALIAS_GETPID"></a>

## 413.73 `CONFIG_POSIX_MULTI_PROCESS_ALIAS_GETPID`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

选择 `y` 后，Zephyr 为 `getpid()` 提供别名（Alias）`_getpid()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_MULTI_PROCESS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
y
```

**被弱选择（Implied by）**

```text
CONFIG_NEWLIB_LIBC
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.procN:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.procN#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 多进程（Multi-process）支持

**配置项引用（Symbol References）**：[`CONFIG_POSIX_MULTI_PROCESS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MULTI_PROCESS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NEWLIB_LIBC`](P198_lib_配置项参考_2.md#CONFIG_NEWLIB_LIBC)。

<a id="CONFIG_POSIX_NETWORKING"></a>

## 413.74 `CONFIG_POSIX_NETWORKING`

**提示（Prompt）**：POSIX 网络 API（Networking API）

**说明（Help）**

启用 POSIX 网络 API（Networking API）支持，包括 BSD 套接字（BSD Sockets）。更多细节参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING && CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_NET_HOSTNAME_ENABLE
CONFIG_NET_INTERFACE_NAME
CONFIG_NET_SOCKETPAIR
CONFIG_NET_SOCKETS
```

**被选择（Selected by）**

```text
CONFIG_POSIX_API
CONFIG_POSIX_AEP_CHOICE_NETAPP
CONFIG_POSIX_AEP_REALTIME_DEDICATED
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.net:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.net#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NET_HOSTNAME_ENABLE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_ENABLE)、[`CONFIG_NET_INTERFACE_NAME`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_INTERFACE_NAME)、[`CONFIG_NET_SOCKETPAIR`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETPAIR)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_POSIX_API`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_API)、[`CONFIG_POSIX_AEP_CHOICE_NETAPP`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_NETAPP)、[`CONFIG_POSIX_AEP_REALTIME_DEDICATED`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_DEDICATED)。

<a id="CONFIG_POSIX_OPEN_MAX"></a>

## 413.75 `CONFIG_POSIX_OPEN_MAX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

进程可同时打开的文件最大数量。用户无法直接配置此项，但可通过 `CONFIG_ZVFS_OPEN_ADD_SIZE_POSIX` 调整。更多信息参见 [POSIX limits.h](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/limits.h.html)。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_ZVFS_OPEN_ADD_SIZE_POSIX
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.device_io:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.device_io#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 设备 I/O（Device I/O）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_ZVFS_OPEN_ADD_SIZE_POSIX`](P414_subsys_portability_配置项参考_2.md#CONFIG_ZVFS_OPEN_ADD_SIZE_POSIX)。

<a id="CONFIG_POSIX_PAGE_SIZE"></a>

## 413.76 `CONFIG_POSIX_PAGE_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项不可由用户配置（Not user-configurable）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_MMU_PAGE_SIZE if CONFIG_MMU
0x40
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.mem:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.mem#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 内存（Memory）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_MMU_PAGE_SIZE`](P001_kernel_配置项参考_1.md#CONFIG_MMU_PAGE_SIZE)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)。

<a id="CONFIG_POSIX_PRIORITY_SCHEDULING"></a>

## 413.77 `CONFIG_POSIX_PRIORITY_SCHEDULING`

**提示（Prompt）**：POSIX 基于优先级的进程调度（Priority-based process scheduling）

**说明（Help）**

启用 POSIX 调度 API（`_POSIX_PRIORITY_SCHEDULING`）。由于 Zephyr 尚不支持进程，除 `sched_get_priority_min()` 和 `sched_get_priority_max()` 外，大部分相关行为未定义。更多信息参见 [POSIX 可移植性相关说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html#tag_24_03_04) 和 [sched_get_priority_max() 说明](https://pubs.opengroup.org/onlinepubs/9699919799/functions/sched_get_priority_max.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_CHOICE_NETAPP
CONFIG_POSIX_AEP_REALTIME_DEDICATED
CONFIG_XSI_REALTIME
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.sched:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.sched#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 调度器选项（Scheduler options）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_CHOICE_NETAPP`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_NETAPP)、[`CONFIG_POSIX_AEP_REALTIME_DEDICATED`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_DEDICATED)、[`CONFIG_XSI_REALTIME`](P414_subsys_portability_配置项参考_2.md#CONFIG_XSI_REALTIME)。

<a id="CONFIG_POSIX_PTHREAD_ATTR_GUARDSIZE_BITS"></a>

## 413.78 `CONFIG_POSIX_PTHREAD_ATTR_GUARDSIZE_BITS`

**提示（Prompt）**：`pthread_attr_t` 的 `guardsize` 有效位数（Significant bits）

**说明（Help）**

此值参与确定支持的 `pthread_attr_t` 的 `guardsize` 最大值。有效保护区大小（Guard size）范围为 `[0, N-1]`，其中 `N = 1 << M`，M 为本配置值。实际保护区大小可能向上取整。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
9
```

**取值范围（Ranges）**

```text
[1, 31]
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_PTHREAD_ATTR_GUARDSIZE_DEFAULT"></a>

## 413.79 `CONFIG_POSIX_PTHREAD_ATTR_GUARDSIZE_DEFAULT`

**提示（Prompt）**：栈保护区（Stack guard area）的默认大小

**说明（Help）**

默认在 POSIX 线程（pthread）栈可能溢出的一端预留的空间。Zephyr 已支持基于软件的栈金丝雀（Canary）保护和基于硬件 MMU/MPU 的栈保护，因此默认设为 0。但符合标准的应用需要将其设为 `PAGESIZE`。未来此选项可能支持通过软件或硬件动态管理保护区（Guard area）；目前它仅增大线程栈的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_PTHREAD_ATTR_STACKSIZE_BITS"></a>

## 413.80 `CONFIG_POSIX_PTHREAD_ATTR_STACKSIZE_BITS`

**提示（Prompt）**：`pthread_attr_t` 的 `stacksize` 有效位数（Significant bits）

**说明（Help）**

此值参与确定支持的 `pthread_attr_t` 的 `stacksize` 最大值。有效栈大小（Stack size）范围为 `[1, N]`，其中 `N = 1 << M`，M 为本配置值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
23
```

**取值范围（Ranges）**

```text
[8, 31]
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_RAW_SOCKETS"></a>

## 413.81 `CONFIG_POSIX_RAW_SOCKETS`

**提示（Prompt）**：POSIX 原始套接字（RAW socket）支持

**说明（Help）**

启用原始套接字（Raw socket）支持。更多信息参见 [POSIX 原始套接字相关说明](https://pubs.opengroup.org/onlinepubs/9699919799.2008edition/xrat/V4_xsh_chap02.html#tag_22_02_10_18)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_NETWORKING && CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS_PACKET
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_CHOICE_NETAPP
CONFIG_POSIX_AEP_REALTIME_DEDICATED
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.net:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.net#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 网络 API（Networking API）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_NETWORKING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_NETWORKING)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NET_SOCKETS_PACKET`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_PACKET)、[`CONFIG_POSIX_AEP_CHOICE_NETAPP`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_NETAPP)、[`CONFIG_POSIX_AEP_REALTIME_DEDICATED`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_DEDICATED)。

<a id="CONFIG_POSIX_REALTIME_SIGNALS"></a>

## 413.82 `CONFIG_POSIX_REALTIME_SIGNALS`

**提示（Prompt）**：POSIX 实时信号（Realtime signals）

**说明（Help）**

启用 POSIX 实时信号（Realtime signals）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.signal:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.signal#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 信号（Signals）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<a id="CONFIG_POSIX_RTSIG_MAX"></a>

## 413.83 `CONFIG_POSIX_RTSIG_MAX`

**提示（Prompt）**：实时信号（Realtime signal）的最大数量

**说明（Help）**

定义实时信号（Realtime signal）的最大数量 `RTSIG_MAX`。原文给出的信号范围为 `[SIGRTMIN .. (SIGRTMIN+RTSIG_MAX)]`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_REALTIME_SIGNALS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.signal:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.signal#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 信号（Signals） → POSIX 实时信号（Realtime signals）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_REALTIME_SIGNALS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_REALTIME_SIGNALS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_RW_LOCKS"></a>

## 413.84 `CONFIG_POSIX_RW_LOCKS`

**提示（Prompt）**：POSIX 读写锁（reader-writer locks）

**说明（Help）**

选择 `y` 以启用 POSIX 读写锁（Reader-writer lock）。更多信息参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.rwlock:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.rwlock#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<a id="CONFIG_POSIX_SEMAPHORES"></a>

## 413.85 `CONFIG_POSIX_SEMAPHORES`

**提示（Prompt）**：POSIX 信号量（Semaphore）支持

**说明（Help）**

启用 POSIX 信号量（Semaphore）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_SIMPLELINK_HOST_DRIVER
CONFIG_WIFI_SIMPLELINK
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.semaphore:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.semaphore#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_SIMPLELINK_HOST_DRIVER`](P211_modules_Kconfig.simplelink_配置项参考.md#CONFIG_SIMPLELINK_HOST_DRIVER)、[`CONFIG_WIFI_SIMPLELINK`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SIMPLELINK)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<a id="CONFIG_POSIX_SEM_NAMELEN_MAX"></a>

## 413.86 `CONFIG_POSIX_SEM_NAMELEN_MAX`

**提示（Prompt）**：信号量名称（Semaphore name）的最大长度

**说明（Help）**

命名信号量（Named semaphore）的名称最大长度，最大值 255 对应 `{NAME_MAX}`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SEMAPHORES && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[2, 255]
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.semaphore:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.semaphore#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 信号量（Semaphore）支持

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SEMAPHORES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SEMAPHORES)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_SEM_NSEMS_MAX"></a>

## 413.87 `CONFIG_POSIX_SEM_NSEMS_MAX`

**提示（Prompt）**：最大信号量数量（semaphores）

**说明（Help）**

POSIX 应用中信号量（Semaphore）的最大数量。注意，目前在 Zephyr 中，此值仅限制命名信号量（Named semaphore）的数量，即通过 `sem_open()` 创建的信号量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SEMAPHORES && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.semaphore:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.semaphore#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 信号量（Semaphore）支持

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SEMAPHORES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SEMAPHORES)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_SEM_VALUE_MAX"></a>

## 413.88 `CONFIG_POSIX_SEM_VALUE_MAX`

**提示（Prompt）**：信号量（Semaphore）的最大值

**说明（Help）**

符合 POSIX 的应用中信号量计数（Semaphore count）的最大值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SEMAPHORES && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
32767
```

**取值范围（Ranges）**

```text
[1, 32767]
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.semaphore:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.semaphore#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 信号量（Semaphore）支持

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SEMAPHORES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SEMAPHORES)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_SHARED_MEMORY_OBJECTS"></a>

## 413.89 `CONFIG_POSIX_SHARED_MEMORY_OBJECTS`

**提示（Prompt）**：POSIX 共享内存对象（Shared memory objects）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `shm_open()` 和 `shm_unlink()` 的实现。更多信息参见 [POSIX 系统接口通则](https://pubs.opengroup.org/onlinepubs/9699919799.orig/functions/V2_chap02.html) 和 [可移植性相关说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html#tag_24_03_04)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_SYS_HASH_FUNC32
CONFIG_SYS_HASH_FUNC32_DJB2
CONFIG_ZVFS
CONFIG_ZVFS_FDTABLE
CONFIG_POSIX_MAPPED_FILES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
CONFIG_XSI_REALTIME
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.mem:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.mem#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 内存（Memory）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_SYS_HASH_FUNC32`](P198_lib_配置项参考_2.md#CONFIG_SYS_HASH_FUNC32)、[`CONFIG_SYS_HASH_FUNC32_DJB2`](P198_lib_配置项参考_2.md#CONFIG_SYS_HASH_FUNC32_DJB2)、[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_FDTABLE`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_FDTABLE)、[`CONFIG_POSIX_MAPPED_FILES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MAPPED_FILES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)、[`CONFIG_XSI_REALTIME`](P414_subsys_portability_配置项参考_2.md#CONFIG_XSI_REALTIME)。

<a id="CONFIG_POSIX_SHELL"></a>

## 413.90 `CONFIG_POSIX_SHELL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

编译上级命令行命令（Parent shell command）`posix`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_ENV_SHELL
CONFIG_POSIX_UNAME_SHELL
```

**定义位置（Location）**：[`subsys/portability/posix/shell/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/shell/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 命令行工具（Shell Utilities）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_ENV_SHELL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_ENV_SHELL)、[`CONFIG_POSIX_UNAME_SHELL`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_UNAME_SHELL)。

<a id="CONFIG_POSIX_SIGNALS"></a>

## 413.91 `CONFIG_POSIX_SIGNALS`

**提示（Prompt）**：POSIX 信号（Signals）

**说明（Help）**

启用 POSIX 信号（Signal）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_POSIX_AEP_REALTIME_MINIMAL
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.signal:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.signal#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 信号（Signals）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)。

<a id="CONFIG_POSIX_SIGNAL_STRING_DESC"></a>

## 413.92 `CONFIG_POSIX_SIGNAL_STRING_DESC`

**提示（Prompt）**：为 `strsignal` API 使用完整描述（Full description）

**说明（Help）**

为 `strsignal` API 使用完整描述（Full description），将占用 256 字节 ROM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SIGNALS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.signal:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.signal#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 信号（Signals） → POSIX 信号（Signals）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SIGNALS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SIGNALS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_SINGLE_PROCESS"></a>

## 413.93 `CONFIG_POSIX_SINGLE_PROCESS`

**提示（Prompt）**：POSIX 单进程（Single process）支持

**说明（Help）**

选择 `y` 以使用 `confstr()`、`environ`、`errno`、`getenv()`、`setenv()`、`sysconf()`、`uname()` 或 `unsetenv()`。更多信息参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
CONFIG_POSIX_ENV_SHELL
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.proc1:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.proc1#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)、[`CONFIG_POSIX_ENV_SHELL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_ENV_SHELL)。

<a id="CONFIG_POSIX_SPIN_LOCKS"></a>

## 413.94 `CONFIG_POSIX_SPIN_LOCKS`

**提示（Prompt）**：POSIX 自旋锁（spin locks）

**说明（Help）**

选择 `y` 以启用 POSIX 自旋锁（Spin lock）。更多信息参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_NONZERO_SPINLOCK_SIZE
```

**被选择（Selected by）**

```text
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.spinlock:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.spinlock#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NONZERO_SPINLOCK_SIZE`](P001_kernel_配置项参考_1.md#CONFIG_NONZERO_SPINLOCK_SIZE)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<a id="CONFIG_POSIX_SYNCHRONIZED_IO"></a>

## 413.95 `CONFIG_POSIX_SYNCHRONIZED_IO`

**提示（Prompt）**：POSIX 同步 I/O（Synchronized I/O）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `fdatasync()`、`fsync()` 和 `msync()` 的实现。更多信息参见 [msync() 说明](https://pubs.opengroup.org/onlinepubs/9699919799/functions/msync.html) 和 [fdatasync() 说明](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fdatasync.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_POSIX_FSYNC
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
CONFIG_XSI_REALTIME
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.sync_io:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.sync_io#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 同步 I/O（Synchronized I/O）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_FSYNC`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_FSYNC)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)、[`CONFIG_XSI_REALTIME`](P414_subsys_portability_配置项参考_2.md#CONFIG_XSI_REALTIME)。

<a id="CONFIG_POSIX_SYSCONF_IMPL_CHOICE"></a>

## 413.96 `CONFIG_POSIX_SYSCONF_IMPL_CHOICE`

**提示（Prompt）**：`sysconf()` 的实现方式（Implementation method）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SINGLE_PROCESS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_POSIX_SYSCONF_IMPL_FULL if CONFIG_CPP
CONFIG_POSIX_SYSCONF_IMPL_MACRO
```

**可选项（Choices）**

```text
CONFIG_POSIX_SYSCONF_IMPL_MACRO
CONFIG_POSIX_SYSCONF_IMPL_FULL
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.proc1:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.proc1#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 单进程（Single process）支持

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SINGLE_PROCESS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SINGLE_PROCESS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_SYSCONF_IMPL_FULL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSCONF_IMPL_FULL)、[`CONFIG_CPP`](P197_lib_配置项参考_1.md#CONFIG_CPP)、[`CONFIG_POSIX_SYSCONF_IMPL_MACRO`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSCONF_IMPL_MACRO)。

<a id="CONFIG_POSIX_SYSCONF_IMPL_FULL"></a>

## 413.97 `CONFIG_POSIX_SYSCONF_IMPL_FULL`

**提示（Prompt）**：完整（Full）

**说明（Help）**

将 `sysconf()` 实现为一个大型整数到整数映射数组（Integer-integer array）。优点是可查询全部 `sysconf()` 选项，并且能够取得 `sysconf()` 符号的地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_SYSCONF_IMPL_CHOICE>
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.proc1:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.proc1#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 单进程（Single process）支持 → `sysconf()` 的实现方式（Implementation method）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSCONF_IMPL_CHOICE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSCONF_IMPL_CHOICE)。

<a id="CONFIG_POSIX_SYSCONF_IMPL_MACRO"></a>

## 413.98 `CONFIG_POSIX_SYSCONF_IMPL_MACRO`

**提示（Prompt）**：宏（Macro）

**说明（Help）**

通过宏（Macro）将 `sysconf()` 实现为编译期常量（Compile-time constant）。此方式开销最小，缺点是 `sysconf()` 不再是可取地址的函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_POSIX_SYSCONF_IMPL_CHOICE>
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.proc1:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.proc1#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 单进程（Single process）支持 → `sysconf()` 的实现方式（Implementation method）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSCONF_IMPL_CHOICE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSCONF_IMPL_CHOICE)。

<a id="CONFIG_POSIX_SYSTEM_INTERFACES"></a>

## 413.99 `CONFIG_POSIX_SYSTEM_INTERFACES`

**提示（Prompt）**：POSIX 系统接口（System Interfaces）。

**说明（Help）**

选择 `y` 以在 Zephyr 中支持 POSIX 系统接口（System Interfaces）。此菜单的选项按 POSIX 子配置文件选项组（Subprofiling Option Group）组织。更多信息参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_NATIVE_LIBC_INCOMPATIBLE
```

**被选择（Selected by）**

```text
CONFIG_SIMPLELINK_HOST_DRIVER
CONFIG_POSIX_API
CONFIG_POSIX_AEP_CHOICE_BASE
CONFIG_POSIX_AEP_CHOICE_PSE51
CONFIG_POSIX_AEP_CHOICE_PSE52
CONFIG_POSIX_AEP_CHOICE_PSE53
CONFIG_POSIX_AEP_CHOICE_NETAPP
```

**定义位置（Location）**：[`subsys/portability/posix/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_NATIVE_LIBC_INCOMPATIBLE`](P197_lib_配置项参考_1.md#CONFIG_NATIVE_LIBC_INCOMPATIBLE)、[`CONFIG_SIMPLELINK_HOST_DRIVER`](P211_modules_Kconfig.simplelink_配置项参考.md#CONFIG_SIMPLELINK_HOST_DRIVER)、[`CONFIG_POSIX_API`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_API)、[`CONFIG_POSIX_AEP_CHOICE_BASE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_BASE)、[`CONFIG_POSIX_AEP_CHOICE_PSE51`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE51)、[`CONFIG_POSIX_AEP_CHOICE_PSE52`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE52)、[`CONFIG_POSIX_AEP_CHOICE_PSE53`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_PSE53)、[`CONFIG_POSIX_AEP_CHOICE_NETAPP`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_CHOICE_NETAPP)。

<a id="CONFIG_POSIX_THREADS"></a>

## 413.100 `CONFIG_POSIX_THREADS`

**提示（Prompt）**：POSIX 线程支持（thread support）

**说明（Help）**

选择 `y` 以启用 POSIX 线程（Thread）、互斥锁（Mutex）、条件变量（Condition variable）和线程专用存储（Thread-specific storage）。将提供以下函数：

`pthread_atfork()`、`pthread_attr_destroy()`、`pthread_attr_getdetachstate()`、`pthread_attr_getschedparam()`、`pthread_attr_init()`、`pthread_attr_setdetachstate()`、`pthread_attr_setschedparam()`、`pthread_cancel()`、`pthread_cleanup_pop()`、`pthread_cleanup_push()`、`pthread_cond_broadcast()`、`pthread_cond_destroy()`、`pthread_cond_init()`、`pthread_cond_signal()`、`pthread_cond_timedwait()`、`pthread_cond_wait()`、`pthread_condattr_destroy()`、`pthread_condattr_init()`、`pthread_create()`、`pthread_detach()`、`pthread_equal()`、`pthread_exit()`、`pthread_getspecific()`、`pthread_join()`、`pthread_key_create()`、`pthread_key_delete()`、`pthread_kill()`、`pthread_mutex_destroy()`、`pthread_mutex_init()`、`pthread_mutex_lock()`、`pthread_mutex_timedlock()`、`pthread_mutex_trylock()`、`pthread_mutex_unlock()`、`pthread_mutexattr_destroy()`、`pthread_mutexattr_init()`、`pthread_once()`、`pthread_self()`、`pthread_setcancelstate()`、`pthread_setcanceltype()`、`pthread_setspecific()`、`pthread_sigmask()`、`pthread_testcancel()` 和 `sched_yield()`。

更多信息参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_SIMPLELINK_HOST_DRIVER
CONFIG_NXP_WIFI_SIGMA_AGENT
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_SIMPLELINK_HOST_DRIVER`](P211_modules_Kconfig.simplelink_配置项参考.md#CONFIG_SIMPLELINK_HOST_DRIVER)、[`CONFIG_NXP_WIFI_SIGMA_AGENT`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SIGMA_AGENT)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<!-- kconfig-navigation -->

[上一章](P412_subsys_pmci_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P414_subsys_portability_配置项参考_2.md)
