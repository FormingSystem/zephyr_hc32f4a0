---
id: learning.zephyr-docs.tracing-core-reference.page-2
title: 跟踪API总览
kind: reference
status: maintained
domains: [zephyr, kernel, tracing, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__tracing__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_跟踪API总览

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__tracing__apis.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入跟踪总览、格式接口、包装宏、数据结构和公共头文件参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

跟踪后端（Tracing Backends）使用的钩子位置（Hook Points）。

<a id="details"></a>

跟踪后端（Tracing Backends）使用的钩子位置（Hook Points）。这些宏在内核及子系统代码中调用，用于标记入口（Entry）、阻塞（Blocking）、出口（Exit）及各类生命周期事件（Lifecycle Events）。

<a id="header-groups"></a>
<a id="groups"></a>

## 2.1\_主题（Topics）

<a id="r_subsys_5Ftracing_5Fapis_5Fbackend_5Fext"></a>

相关声明：[后端专用扩展（Backend-specific Extensions）](../network_thread_trace_reference/P005_后端扩展跟踪接口.md)。

仅由特定后端（Backends）提供的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fcondvar"></a>

相关声明：[条件变量（Condition Variable）](../sync_trace_reference/P003_条件变量跟踪接口.md)。

条件变量（Condition Variable）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fwork_5Fdelayable"></a>

相关声明：[可延时工作项（Delayable Work Item）](../driver_trace_reference/P006_可延时工作项跟踪接口.md)。

可延时工作项（Delayable Work Item）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fevent"></a>

相关声明：[事件对象（Event）](../sync_trace_reference/P004_事件对象跟踪接口.md)。

事件对象（Event）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Ffifo"></a>

相关声明：[先进先出队列（FIFO）](../object_trace_reference/P001_FIFO跟踪接口.md)。

先进先出队列（FIFO）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fgpio"></a>

相关声明：[通用输入输出（GPIO）](../driver_trace_reference/P002_GPIO跟踪接口.md)。

通用输入输出（GPIO）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fheap"></a>

相关声明：[堆（Heap）](../object_trace_reference/P008_堆跟踪接口.md)。

堆（Heap）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Flifo"></a>

相关声明：[后进先出队列（LIFO）](../object_trace_reference/P002_LIFO跟踪接口.md)。

后进先出队列（LIFO）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fmbox"></a>

相关声明：[邮箱（Mailbox）](../object_trace_reference/P005_邮箱跟踪接口.md)。

邮箱（Mailbox）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fmslab"></a>

相关声明：[内存块池（Memory Slab）](../object_trace_reference/P009_内存块池跟踪接口.md)。

内存块池（Memory Slab）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fmsgq"></a>

相关声明：[消息队列（Message Queue）](../object_trace_reference/P004_消息队列跟踪接口.md)。

消息队列（Message Queue）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fmutex"></a>

相关声明：[互斥锁（Mutex）](../sync_trace_reference/P002_互斥锁跟踪接口.md)。

互斥锁（Mutex）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fnet"></a>

相关声明：[网络（Network）](../network_thread_trace_reference/P002_网络跟踪接口.md)。

网络（Network）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fsocket"></a>

相关声明：[网络套接字（Network Socket）](../network_thread_trace_reference/P003_套接字跟踪接口.md)。

网络套接字（Network Socket）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fpm_5Fdevice_5Fruntime"></a>

相关声明：[设备运行时电源管理（Runtime PM）](../driver_trace_reference/P003_设备运行时电源管理跟踪.md)。

设备运行时电源管理（Device Runtime Power Management）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fpipe"></a>

相关声明：[管道（Pipe）](../object_trace_reference/P006_管道跟踪接口.md)。

管道（Pipe）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fpoll"></a>

相关声明：[轮询（Polling）](../sync_trace_reference/P006_轮询跟踪接口.md)。

轮询（Polling）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fqueue"></a>

相关声明：[队列（Queue）](../object_trace_reference/P003_队列跟踪接口.md)。

队列（Queue）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Frtio"></a>

相关声明：[实时输入输出跟踪API（RTIO Tracing APIs）](../driver_trace_reference/P001_RTIO跟踪接口.md)。

实时输入输出（RTIO）跟踪API（Tracing APIs）。

<a id="r_subsys_5Ftracing_5Fapis_5Fsem"></a>

相关声明：[信号量（Semaphore）](../sync_trace_reference/P001_信号量跟踪接口.md)。

信号量（Semaphore）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fstack"></a>

相关声明：[栈（Stack）](../object_trace_reference/P007_栈跟踪接口.md)。

栈（Stack）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fsyscall"></a>

相关声明：[系统调用跟踪（Syscall Tracing）](../sync_trace_reference/P007_系统调用跟踪接口.md)。

系统调用（System Calls）的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fpm_5Fsystem"></a>

相关声明：[系统电源管理（System PM）](../driver_trace_reference/P004_系统电源管理跟踪.md)。

系统电源管理（System Power Management）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fthread"></a>

相关声明：[线程（Thread）](../network_thread_trace_reference/P001_线程跟踪接口.md)。

线程（Thread）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Ftimer"></a>

相关声明：[定时器（Timer）](../sync_trace_reference/P005_定时器跟踪接口.md)。

定时器（Timer）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fwork_5Fpoll"></a>

相关声明：[触发式工作项（Triggered Work Item）](../driver_trace_reference/P007_轮询工作项跟踪接口.md)。

触发式工作项（Triggered Work Item）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fnamed"></a>

相关声明：[用户定义事件（User-defined Event）](../network_thread_trace_reference/P004_命名事件跟踪接口.md)。

用户定义的命名事件（Named Events）的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fwork"></a>

相关声明：[工作项（Work Item）](../driver_trace_reference/P005_工作项跟踪接口.md)。

工作项（Work Item）事件的跟踪钩子（Tracing Hooks）。

<a id="r_subsys_5Ftracing_5Fapis_5Fwork_5Fq"></a>

相关声明：[工作队列（Work Queue）](../driver_trace_reference/P008_工作队列跟踪接口.md)。

工作队列（Work Queue）事件的跟踪钩子（Tracing Hooks）。

<a id="header-files"></a>
<a id="files"></a>

## 2.2\_文件（Files）

<a id="r_tracing_2Eh"></a>

```c
file tracing.h
```

相关声明：[tracing.h](P007_跟踪公共头文件参考.md)。

跟踪子系统API的主头文件。

<a id="r_tracing_5Fdefault_5Fhooks_2Eh"></a>

```c
file tracing_default_hooks.h
```

相关声明：[tracing_default_hooks.h](../tracing_headers_reference/P004_默认底层钩子头文件参考.md)。

底层sys_trace_*钩子层的默认实现（Default Implementations）。

<a id="r_tracing_5Fhooks_2Eh"></a>

```c
file tracing_hooks.h
```

相关声明：[tracing_hooks.h](../tracing_hooks_reference/P001_完整跟踪钩子头文件参考.md)。

统一的跟踪钩子清单（Canonical Tracing Hook List）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.3\_宏定义（Macros）

<a id="r_ga9b5a02fc57b86d38f857597c7a2553f6"></a>

```c
#define sys_trace_sys_init_enter(entry, level)
```

相关声明：[sys_trace_sys_init_enter](#ga9b5a02fc57b86d38f857597c7a2553f6)。

进入初始化函数（Init Function）时调用。

<a id="r_gacd56f9b376b4639cbe21e12055ca74c7"></a>

```c
#define sys_trace_sys_init_exit(entry, level, result)
```

相关声明：[sys_trace_sys_init_exit](#gacd56f9b376b4639cbe21e12055ca74c7)。

退出初始化函数（Init Function）时调用。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_ga37f43a02961a847af3b7de6c474a8da4"></a>

```c
void sys_trace_isr_enter (void)
```

相关声明：[sys_trace_isr_enter](#ga37f43a02961a847af3b7de6c474a8da4)。

进入中断服务程序（ISR）时调用。

<a id="r_ga7113e2760b1a7ffb1bfa108ad9bfb4be"></a>

```c
void sys_trace_isr_exit (void)
```

相关声明：[sys_trace_isr_exit](#ga7113e2760b1a7ffb1bfa108ad9bfb4be)。

退出中断服务程序（ISR）时调用。

<a id="r_ga303fe60fd4de8ddcc02c6920656e326d"></a>

```c
void sys_trace_isr_exit_to_scheduler (void)
```

相关声明：[sys_trace_isr_exit_to_scheduler](#ga303fe60fd4de8ddcc02c6920656e326d)。

退出中断服务程序（ISR）并切换到调度器（Scheduler）时调用。

<a id="r_gac9b542f78ed796b4b572de19d295c824"></a>

```c
void sys_trace_idle (void)
```

相关声明：[sys_trace_idle](#gac9b542f78ed796b4b572de19d295c824)。

CPU进入空闲状态（Idle State）时调用。

<a id="r_gac7b7973acf38a440e88242aca52e424c"></a>

```c
void sys_trace_idle_exit (void)
```

相关声明：[sys_trace_idle_exit](#gac7b7973acf38a440e88242aca52e424c)。

CPU退出空闲状态（Idle State）时调用。

## 2.5\_详细说明（Detailed Documentation）

<a id="ga9b5a02fc57b86d38f857597c7a2553f6"></a>

### `sys_trace_sys_init_enter`

```c
#define sys_trace_sys_init_enter ( entry, level )
```

```c
#include <zephyr/tracing/tracing.h>
```

进入初始化函数（Init Function）时调用。

<a id="gacd56f9b376b4639cbe21e12055ca74c7"></a>

### `sys_trace_sys_init_exit`

```c
#define sys_trace_sys_init_exit ( entry, level, result )
```

```c
#include <zephyr/tracing/tracing.h>
```

退出初始化函数（Init Function）时调用。

<a id="gac9b542f78ed796b4b572de19d295c824"></a>

### `sys_trace_idle()`

```c
void sys_trace_idle ( void )
```

```c
#include <zephyr/tracing/tracing.h>
```

CPU进入空闲状态（Idle State）时调用。

<a id="gac7b7973acf38a440e88242aca52e424c"></a>

### `sys_trace_idle_exit()`

```c
void sys_trace_idle_exit ( void )
```

```c
#include <zephyr/tracing/tracing.h>
```

CPU退出空闲状态（Idle State）时调用。

<a id="ga37f43a02961a847af3b7de6c474a8da4"></a>

### `sys_trace_isr_enter()`

```c
void sys_trace_isr_enter ( void )
```

```c
#include <zephyr/tracing/tracing.h>
```

进入中断服务程序（ISR）时调用。

<a id="ga7113e2760b1a7ffb1bfa108ad9bfb4be"></a>

### `sys_trace_isr_exit()`

```c
void sys_trace_isr_exit ( void )
```

```c
#include <zephyr/tracing/tracing.h>
```

退出中断服务程序（ISR）时调用。

<a id="ga303fe60fd4de8ddcc02c6920656e326d"></a>

### `sys_trace_isr_exit_to_scheduler()`

```c
void sys_trace_isr_exit_to_scheduler ( void )
```

```c
#include <zephyr/tracing/tracing.h>
```

退出中断服务程序（ISR）并切换到调度器（Scheduler）时调用。

## 2.6\_源码定位与版本边界

相对源码定位：[跟踪入口](../../../include/zephyr/tracing/tracing.h)、[钩子声明](../../../include/zephyr/tracing/tracing_hooks.h)、[包装宏](../../../include/zephyr/tracing/tracing_macros.h)、[格式接口](../../../include/zephyr/tracing/tracing_format.h)、[默认底层钩子](../../../include/zephyr/tracing/tracing_default_hooks.h)、[跟踪配置](../../../subsys/tracing/Kconfig)、[构建选择](../../../subsys/tracing/CMakeLists.txt)、[公共格式处理](../../../subsys/tracing/tracing_format_common.c)、[同步格式处理](../../../subsys/tracing/tracing_format_sync.c)、[异步格式处理](../../../subsys/tracing/tracing_format_async.c)、[跟踪核心](../../../subsys/tracing/tracing_core.c)、[跟踪缓冲区](../../../subsys/tracing/tracing_buffer.c)、[默认弱钩子](../../../subsys/tracing/tracing_none.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：官方接口正文、原始宏展开与源码译注分别保留。来源记录固定本次官方页面及源码的摘要；仓库文件通过相对链接定位，读者使用的源码版本可能不同。

> 译注——源码核对：跟踪包含sys_port_trace_*宏钩子和较低层的sys_trace_*入口。tracing_hooks.h补齐宏钩子，tracing_default_hooks.h为未覆盖低层入口的树外格式提供声明及默认宏；二者职责不同，不能只补一层就假定全部记录已实现。

> 译注——源码核对：初始化钩子参数entry、level、result保留原签名；本页未提供更详细的参数表，译文不把自行解释冒充官方参数说明。ISR与idle函数也可能由后端覆盖；默认弱实现并非一律无行为，启用CONFIG_CPU_LOAD_BACKEND_IDLE_HOOK时会参与CPU负载的空闲区间统计。

> 译注——源码核对：本次验证限于官方文档与源码对照，未配置采集后端、运行事件采集或测量时序。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.7\_原页交叉引用（Cross References）

- [后端专用扩展（Backend-specific Extensions）](../network_thread_trace_reference/P005_后端扩展跟踪接口.md)
- [条件变量（Condition Variable）](../sync_trace_reference/P003_条件变量跟踪接口.md)
- [可延时工作项（Delayable Work Item）](../driver_trace_reference/P006_可延时工作项跟踪接口.md)
- [事件对象（Event）](../sync_trace_reference/P004_事件对象跟踪接口.md)
- [先进先出队列（FIFO）](../object_trace_reference/P001_FIFO跟踪接口.md)
- [通用输入输出（GPIO）](../driver_trace_reference/P002_GPIO跟踪接口.md)
- [堆（Heap）](../object_trace_reference/P008_堆跟踪接口.md)
- [后进先出队列（LIFO）](../object_trace_reference/P002_LIFO跟踪接口.md)
- [邮箱（Mailbox）](../object_trace_reference/P005_邮箱跟踪接口.md)
- [内存块池（Memory Slab）](../object_trace_reference/P009_内存块池跟踪接口.md)
- [消息队列（Message Queue）](../object_trace_reference/P004_消息队列跟踪接口.md)
- [互斥锁（Mutex）](../sync_trace_reference/P002_互斥锁跟踪接口.md)
- [网络（Network）](../network_thread_trace_reference/P002_网络跟踪接口.md)
- [网络套接字（Network Socket）](../network_thread_trace_reference/P003_套接字跟踪接口.md)
- [设备运行时电源管理（Runtime PM）](../driver_trace_reference/P003_设备运行时电源管理跟踪.md)
- [管道（Pipe）](../object_trace_reference/P006_管道跟踪接口.md)
- [轮询（Polling）](../sync_trace_reference/P006_轮询跟踪接口.md)
- [队列（Queue）](../object_trace_reference/P003_队列跟踪接口.md)
- [实时输入输出跟踪API（RTIO Tracing APIs）](../driver_trace_reference/P001_RTIO跟踪接口.md)
- [信号量（Semaphore）](../sync_trace_reference/P001_信号量跟踪接口.md)
- [栈（Stack）](../object_trace_reference/P007_栈跟踪接口.md)
- [系统调用跟踪（Syscall Tracing）](../sync_trace_reference/P007_系统调用跟踪接口.md)
- [系统电源管理（System PM）](../driver_trace_reference/P004_系统电源管理跟踪.md)
- [线程（Thread）](../network_thread_trace_reference/P001_线程跟踪接口.md)
- [定时器（Timer）](../sync_trace_reference/P005_定时器跟踪接口.md)
- [触发式工作项（Triggered Work Item）](../driver_trace_reference/P007_轮询工作项跟踪接口.md)
- [用户定义事件（User-defined Event）](../network_thread_trace_reference/P004_命名事件跟踪接口.md)
- [工作项（Work Item）](../driver_trace_reference/P005_工作项跟踪接口.md)
- [工作队列（Work Queue）](../driver_trace_reference/P008_工作队列跟踪接口.md)
- [tracing.h](P007_跟踪公共头文件参考.md)
- [tracing_default_hooks.h](../tracing_headers_reference/P004_默认底层钩子头文件参考.md)
- [tracing_hooks.h](../tracing_hooks_reference/P001_完整跟踪钩子头文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_跟踪子系统总览.md) · [返回大纲](大纲.md) · [下一章](P003_跟踪格式接口.md)
