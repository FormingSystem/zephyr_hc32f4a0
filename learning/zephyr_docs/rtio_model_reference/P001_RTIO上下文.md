---
id: learning.zephyr-docs.rtio-model-reference.page-1
title: RTIO上下文
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_RTIO上下文

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtio.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO数据结构、事件标志、操作码及优先级说明，再通过交叉引用连接核心接口。源码跟踪译注与官方原文分开标示。

一个RTIO上下文（Context），其内容可以视为一对队列。

```c
#include <zephyr/rtio/rtio.h>
```

<a id="details"></a>

一个RTIO上下文（Context），其内容可以视为一对队列：一个用于提交的队列，保存可用和已入队待处理的提交；另一个用于完成事件的队列，保存可用和已准备好被取出的完成事件。RTIO执行器（Executor）以及实现`rtio_iodev`接口的对象，都是提交的消费者（Consumers）和完成事件的生产者（Producers）。调用`rtio_submit()`之前不会启动工作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_a358de1033ab4396d1f1baee2699c993f"></a>

```c
atomic_t cq_count
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[cq_count](#a358de1033ab4396d1f1baee2699c993f)。

完成事件总数。

<a id="r_ac45facdcc6d64cd70113b9b05b2fb086"></a>

```c
atomic_t xcqcnt
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[xcqcnt](#ac45facdcc6d64cd70113b9b05b2fb086)。

因没有可用CQE而丢弃的完成事件数量。

<a id="r_a955f012bac623e7c037b5f1dba8e7fda"></a>

```c
struct rtio_sqe_pool * sqe_pool
```

相关声明：[sqe_pool](#a955f012bac623e7c037b5f1dba8e7fda)。

带空闲链表（Free List）的提交队列对象池。

<a id="r_a1bce3c3bb0150275ece65975adf3ee4f"></a>

```c
struct rtio_cqe_pool * cqe_pool
```

相关声明：[cqe_pool](#a1bce3c3bb0150275ece65975adf3ee4f)。

带空闲链表（Free List）的完成队列对象池。

<a id="r_a34fbabfdbef3144f4520bf678684cdfb"></a>

```c
struct mpsc sq
```

相关声明：[mpsc](../intercore_reference/P159_MPSC无锁队列结构.md)、[sq](#a34fbabfdbef3144f4520bf678684cdfb)。

提交队列（Submission Queue）。

<a id="r_ad6f44a354a170cb04a584beee7728fa9"></a>

```c
struct mpsc cq
```

相关声明：[mpsc](../intercore_reference/P159_MPSC无锁队列结构.md)、[cq](#ad6f44a354a170cb04a584beee7728fa9)。

完成队列（Completion Queue）。

## 1.2\_详细说明（Detailed Documentation）

<a id="ad6f44a354a170cb04a584beee7728fa9"></a>

### `cq`

```c
struct mpsc rtio::cq
```

完成队列（Completion Queue）。

<a id="a358de1033ab4396d1f1baee2699c993f"></a>

### `cq_count`

```c
atomic_t rtio::cq_count
```

完成事件总数。

<a id="a1bce3c3bb0150275ece65975adf3ee4f"></a>

### `cqe_pool`

```c
struct rtio_cqe_pool* rtio::cqe_pool
```

带空闲链表（Free List）的完成队列对象池。

<a id="a34fbabfdbef3144f4520bf678684cdfb"></a>

### `sq`

```c
struct mpsc rtio::sq
```

提交队列（Submission Queue）。

<a id="a955f012bac623e7c037b5f1dba8e7fda"></a>

### `sqe_pool`

```c
struct rtio_sqe_pool* rtio::sqe_pool
```

带空闲链表（Free List）的提交队列对象池。

<a id="ac45facdcc6d64cd70113b9b05b2fb086"></a>

### `xcqcnt`

```c
atomic_t rtio::xcqcnt
```

因没有可用CQE而丢弃的完成事件数量。

## 1.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：上下文（Context）把SQE对象池、CQE对象池和两条活动队列连接起来。`rtio_sqe_acquire()`从池取得条目并放入待提交队列；`rtio_submit()`把队列交给执行器。本页的`sq`、`cq`与`sqe_pool`、`cqe_pool`分别代表排队状态与存储资源，不能把它们当成同一个对象。相关完整操作见[核心接口](../rtio_core_reference/P001_RTIO公共接口.md)。

> 译注——源码核对：`cq_count`统计完成计数，`xcqcnt`记录因CQE对象不足而丢弃的完成事件。读取的`rtio_cqe_submit()`即使无法取得CQE，也会增加完成计数；所以完成计数增加不代表完成队列里必定存在同样数量的可读结果。消费和释放CQE不会把这个累计计数当作队列长度维护。

> 译注——源码核对：本页显示的是官方Doxygen公开成员。原始头文件还含按配置编译的提交／消费信号量、内存块池和完成回调字段；不能用网页显示的成员数推算任何配置下的结构体大小或二进制接口（ABI）。

> 译注——源码核对：本页译注以来源记录中本次读取的官方源码摘要为界。本仓库的相对源码链接用于追踪同名文件，不保证任意本地版本与滚动更新的main完全一致。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.4\_原页交叉引用（Cross References）

- [zephyr/rtio/rtio.h](../rtio_core_reference/P003_RTIO核心头文件源码.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [mpsc](../intercore_reference/P159_MPSC无锁队列结构.md)
- [rtio_iodev](P003_RTIO输入输出设备.md)
- [rtio_submit()](../rtio_core_reference/P001_RTIO公共接口.md#gafee27c64a4a4989c4eb774addde8eb2e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_RTIO完成事件.md)
