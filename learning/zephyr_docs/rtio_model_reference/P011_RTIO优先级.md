---
id: learning.zephyr-docs.rtio-model-reference.page-11
title: RTIO优先级
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__sqe__prio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_RTIO优先级

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__sqe__prio.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO数据结构、事件标志、操作码及优先级说明，再通过交叉引用连接核心接口。源码跟踪译注与官方原文分开标示。

RTIO预定义优先级（Predefined Priorities）。

<a id="details"></a>

RTIO预定义优先级（Predefined Priorities）。I/O设备在调度操作时可以选择使用这些优先级，优先级可能进一步用于软件或硬件总线仲裁器（Bus Arbitrators）。说明（Note）：目前它们大多尚未使用，但仍应指定。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_gabc81232a7d4b7145d9898afd6ff2ae48"></a>

```c
#define RTIO_PRIO_LOW 0U
```

相关声明：[RTIO_PRIO_LOW](#gabc81232a7d4b7145d9898afd6ff2ae48)。

低优先级（Low Priority）。

<a id="r_gab02e27e01b7dd4eb3439df557899ce92"></a>

```c
#define RTIO_PRIO_NORM 127U
```

相关声明：[RTIO_PRIO_NORM](#gab02e27e01b7dd4eb3439df557899ce92)。

普通优先级（Normal Priority）。

<a id="r_ga220baa9bf2c8ff0cb6f52f0220e72b30"></a>

```c
#define RTIO_PRIO_HIGH 255U
```

相关声明：[RTIO_PRIO_HIGH](#ga220baa9bf2c8ff0cb6f52f0220e72b30)。

高优先级（High Priority）。

## 11.2\_详细说明（Detailed Documentation）

<a id="ga220baa9bf2c8ff0cb6f52f0220e72b30"></a>

### `RTIO_PRIO_HIGH`

```c
#define RTIO_PRIO_HIGH 255U
```

```c
#include <zephyr/rtio/sqe.h>
```

高优先级（High Priority）。

<a id="gabc81232a7d4b7145d9898afd6ff2ae48"></a>

### `RTIO_PRIO_LOW`

```c
#define RTIO_PRIO_LOW 0U
```

```c
#include <zephyr/rtio/sqe.h>
```

低优先级（Low Priority）。

<a id="gab02e27e01b7dd4eb3439df557899ce92"></a>

### `RTIO_PRIO_NORM`

```c
#define RTIO_PRIO_NORM 127U
```

```c
#include <zephyr/rtio/sqe.h>
```

普通优先级（Normal Priority）。

## 11.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：本次宏值分别为LOW=0U、NORM=127U和HIGH=255U，SQE.prio类型为uint8_t。这是I/O操作优先级，不是Zephyr线程调度优先级，不能套用线程优先级的数值方向或据此声称线程会抢占。

> 译注——源码核对：原文明确说设备可以选择使用优先级。当前核心执行器从提交队列取出条目并分派，没有在这里按prio重新排序；真正的软件或硬件仲裁能力取决于IODEV驱动。指定HIGH不等于所有驱动都保证优先执行。

> 译注——源码核对：本页译注以来源记录中本次读取的官方源码摘要为界。本仓库的相对源码链接用于追踪同名文件，不保证任意本地版本与滚动更新的main完全一致。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 11.4\_原页交叉引用（Cross References）

- [zephyr/rtio/sqe.h](../rtio_headers_reference/P001_RTIO提交事件头文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P010_RTIO提交事件标志.md) · [返回大纲](大纲.md)
