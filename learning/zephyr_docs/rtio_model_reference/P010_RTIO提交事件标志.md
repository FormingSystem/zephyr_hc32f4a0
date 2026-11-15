---
id: learning.zephyr-docs.rtio-model-reference.page-10
title: RTIO提交事件标志
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__sqe__flags.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_RTIO提交事件标志

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__sqe__flags.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO数据结构、事件标志、操作码及优先级说明，再通过交叉引用连接核心接口。源码跟踪译注与官方原文分开标示。

RTIO提交队列事件标志（SQE Flags）。

<a id="details"></a>

RTIO提交队列事件标志（SQE Flags）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="r_gae9191d521d4ab602b53fefb74020d06b"></a>

```c
#define RTIO_SQE_CHAINED BIT(0)
```

相关声明：[RTIO_SQE_CHAINED](#gae9191d521d4ab602b53fefb74020d06b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

队列中的下一个请求应等待此请求。

<a id="r_ga07f09cc0c95be6cfdddb23f8acacb1ea"></a>

```c
#define RTIO_SQE_TRANSACTION BIT(1)
```

相关声明：[RTIO_SQE_TRANSACTION](#ga07f09cc0c95be6cfdddb23f8acacb1ea)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

队列中的下一个请求属于同一事务（Transaction）。

<a id="r_ga2802b46584220afffa0e959e149d5a4d"></a>

```c
#define RTIO_SQE_MEMPOOL_BUFFER BIT(2)
```

相关声明：[RTIO_SQE_MEMPOOL_BUFFER](#ga2802b46584220afffa0e959e149d5a4d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

缓冲区应由RTIO内存池分配。

<a id="r_ga7f7f9b038ab8409f271b1aebc1b95ee6"></a>

```c
#define RTIO_SQE_CANCELED BIT(3)
```

相关声明：[RTIO_SQE_CANCELED](#ga7f7f9b038ab8409f271b1aebc1b95ee6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

如果可能，不应执行该SQE。

<a id="r_ga00f8ead8f043fe40d49d0bc3325fb299"></a>

```c
#define RTIO_SQE_MULTISHOT BIT(4)
```

相关声明：[RTIO_SQE_MULTISHOT](#ga00f8ead8f043fe40d49d0bc3325fb299)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

该SQE应持续产生CQE，直到被取消。

<a id="r_ga8578ffdb8f53a51b94fa86a6f02d4a11"></a>

```c
#define RTIO_SQE_NO_RESPONSE BIT(5)
```

相关声明：[RTIO_SQE_NO_RESPONSE](#ga8578ffdb8f53a51b94fa86a6f02d4a11)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

该SQE不产生CQE。

## 10.2\_详细说明（Detailed Documentation）

<a id="ga7f7f9b038ab8409f271b1aebc1b95ee6"></a>

### `RTIO_SQE_CANCELED`

```c
#define RTIO_SQE_CANCELED BIT(3)
```

```c
#include <zephyr/rtio/sqe.h>
```

如果可能，不应执行该SQE。

如果可能，即尚未执行，应通过将SQE标记为失败并返回`-ECANCELED`结果来取消它。

<a id="gae9191d521d4ab602b53fefb74020d06b"></a>

### `RTIO_SQE_CHAINED`

```c
#define RTIO_SQE_CHAINED BIT(0)
```

```c
#include <zephyr/rtio/sqe.h>
```

队列中的下一个请求应等待此请求。

链接的SQE是独立的工作单元，描述执行顺序及失败级联（Failure Cascading）模式。链中的SQE必须在前一个SQE之后才能启动，它们会依次交给IODEV。

<a id="ga2802b46584220afffa0e959e149d5a4d"></a>

### `RTIO_SQE_MEMPOOL_BUFFER`

```c
#define RTIO_SQE_MEMPOOL_BUFFER BIT(2)
```

```c
#include <zephyr/rtio/sqe.h>
```

缓冲区应由RTIO内存池分配。

只有启用了`CONFIG_RTIO_SYS_MEM_BLOCKS`这个Kconfig选项，并通过`RTIO_DEFINE_WITH_MEMPOOL()`宏创建RTIO上下文时，才能使用此标志。如果设置了此标志，则表示与该条目关联的缓冲区由内部内存池分配；一旦不再需要，应尽快调用`rtio_release_mempool()`释放。

<a id="ga00f8ead8f043fe40d49d0bc3325fb299"></a>

### `RTIO_SQE_MULTISHOT`

```c
#define RTIO_SQE_MULTISHOT BIT(4)
```

```c
#include <zephyr/rtio/sqe.h>
```

该SQE应持续产生CQE，直到被取消。

此标志必须与`RTIO_SQE_MEMPOOL_BUFFER`同时存在，表示读操作完成后应重新放回队列，直到被取消。

<a id="ga8578ffdb8f53a51b94fa86a6f02d4a11"></a>

### `RTIO_SQE_NO_RESPONSE`

```c
#define RTIO_SQE_NO_RESPONSE BIT(5)
```

```c
#include <zephyr/rtio/sqe.h>
```

该SQE不产生CQE。

<a id="ga07f09cc0c95be6cfdddb23f8acacb1ea"></a>

### `RTIO_SQE_TRANSACTION`

```c
#define RTIO_SQE_TRANSACTION BIT(1)
```

```c
#include <zephyr/rtio/sqe.h>
```

队列中的下一个请求属于同一事务（Transaction）。

事务中的SQE是一个工作单元的连续组成部分。只有事务中的第一个SQE会提交给IODEV，其余SQE从不单独提交，而是被视为交给同一个IODEV的事务的一部分。序列中的第一个SQE保存要使用的IODEV，最后一个SQE保存用户数据（User Data），这些数据将在失败或成功时通过单个完成事件返回。

## 10.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：CHAINED与TRANSACTION分别描述下一个SQE与当前SQE的关系，不是I2C／I3C的STOP或RESTART总线标志；后者位于`iodev_flags`。应为整组SQE设置完整的连接关系并提供末项，不能设置连接标志却缺失下一个条目。

> 译注——源码核对：事务原文称最终通过单个完成事件返回最后一个SQE的userdata；本次读取的`rtio_executor_handle_oneshot()`却逐个遍历事务成员，在未取消且未设置NO_RESPONSE时为成员生成CQE，使用各成员userdata。译文保留原文，并把此差异列为版本边界，不能据原文概括固定CQE数量或仅保留最后一个userdata。

> 译注——源码核对：原文的`rtio_release_mempool()`是旧名称，本次公共接口为`rtio_release_buffer()`。MEMPOOL_BUFFER标志配合RTIO_SYS_MEM_BLOCKS和带内存池的上下文使用；准备读请求时不一定已分配数据缓冲区，实际分配可在驱动调用`rtio_sqe_rx_buf()`时发生。

> 译注——源码核对：取消标志不是立即中止硬件的保证，也不是每次必定产生-ECANCELED CQE。提交前取消的条目可能附加NO_RESPONSE；多次完成读在错误或取消后停止重提。NO_RESPONSE会抑制完成事件，因此等待数量必须考虑实际会生成的事件。

> 译注——源码核对：原文的失败级联（Failure Cascading）约定与当前执行器的CHAINED后续分派存在差异，详见[核心接口源码译注](../rtio_core_reference/P001_RTIO公共接口.md)。本次只对照源码，没有通过运行测试证明全链失败、取消时序或总线行为。

> 译注——源码核对：本页译注以来源记录中本次读取的官方源码摘要为界。本仓库的相对源码链接用于追踪同名文件，不保证任意本地版本与滚动更新的main完全一致。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 10.4\_原页交叉引用（Cross References）

- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [zephyr/rtio/sqe.h](../rtio_headers_reference/P001_RTIO提交事件头文件参考.md)
- [RTIO_DEFINE_WITH_MEMPOOL()](../rtio_core_reference/P001_RTIO公共接口.md#gae4c2a9384a9ae4ed16dff914b1184ca8)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P009_RTIO操作码.md) · [返回大纲](大纲.md) · [下一章](P011_RTIO优先级.md)
