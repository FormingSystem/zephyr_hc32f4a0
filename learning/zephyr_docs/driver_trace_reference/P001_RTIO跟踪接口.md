---
id: learning.zephyr-docs.driver-trace-reference.page-1
title: RTIO跟踪接口
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__tracing__apis__rtio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_RTIO跟踪接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__tracing__apis__rtio.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO、GPIO、电源管理与工作项的跟踪接口，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

RTIO跟踪API（Tracing APIs）。

<a id="details"></a>

RTIO跟踪API（Tracing APIs）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_ga47d934c79b989e0188f8b507b6cc5283"></a>

```c
#define sys_port_trace_rtio_submit_enter(rtio, wait_count)
```

相关声明：[sys_port_trace_rtio_submit_enter](#ga47d934c79b989e0188f8b507b6cc5283)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪RTIO提交API的入口（Submit Enter）。

<a id="r_gaf51564de963093cb5e738232363aebe6"></a>

```c
#define sys_port_trace_rtio_submit_exit(rtio)
```

相关声明：[sys_port_trace_rtio_submit_exit](#gaf51564de963093cb5e738232363aebe6)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪RTIO提交API的出口（Submit Exit）。

<a id="r_ga3d2692eeafbb425a32927c012762a9be"></a>

```c
#define sys_port_trace_rtio_sqe_acquire_enter(rtio)
```

相关声明：[sys_port_trace_rtio_sqe_acquire_enter](#ga3d2692eeafbb425a32927c012762a9be)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪获取RTIO提交队列事件的API入口（SQE Acquire Enter）。

<a id="r_ga1606ca3ab8397414075b430d7c3d9a82"></a>

```c
#define sys_port_trace_rtio_sqe_acquire_exit(rtio, sqe)
```

相关声明：[sys_port_trace_rtio_sqe_acquire_exit](#ga1606ca3ab8397414075b430d7c3d9a82)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪获取RTIO提交队列事件的API出口（SQE Acquire Exit）。

<a id="r_ga24fc0a40280f6f06f15c70ba803a4cb6"></a>

```c
#define sys_port_trace_rtio_sqe_cancel(sqe)
```

相关声明：[sys_port_trace_rtio_sqe_cancel](#ga24fc0a40280f6f06f15c70ba803a4cb6)。

跟踪取消RTIO提交队列事件的API（SQE Cancel）。

<a id="r_gab31d0584e66a5a705adcb97c4c383b60"></a>

```c
#define sys_port_trace_rtio_cqe_submit_enter(rtio, result, flags)
```

相关声明：[sys_port_trace_rtio_cqe_submit_enter](#gab31d0584e66a5a705adcb97c4c383b60)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

跟踪提交RTIO完成队列事件的API入口（CQE Submit Enter）。

<a id="r_gac9bdbc3e33419eff6f7262108e98882d"></a>

```c
#define sys_port_trace_rtio_cqe_submit_exit(rtio)
```

相关声明：[sys_port_trace_rtio_cqe_submit_exit](#gac9bdbc3e33419eff6f7262108e98882d)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪提交RTIO完成队列事件的API出口（CQE Submit Exit）。

<a id="r_ga69b771f39b617335c1093a56f2e091c1"></a>

```c
#define sys_port_trace_rtio_cqe_acquire_enter(rtio)
```

相关声明：[sys_port_trace_rtio_cqe_acquire_enter](#ga69b771f39b617335c1093a56f2e091c1)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪获取RTIO完成队列事件的API入口（CQE Acquire Enter）。

<a id="r_ga3276c6d26ba5bbe5d0d84e2096a72162"></a>

```c
#define sys_port_trace_rtio_cqe_acquire_exit(rtio, cqe)
```

相关声明：[sys_port_trace_rtio_cqe_acquire_exit](#ga3276c6d26ba5bbe5d0d84e2096a72162)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪获取RTIO完成队列事件的API出口（CQE Acquire Exit）。

<a id="r_ga3c9cba898702f33dd67a0d4d39207c1f"></a>

```c
#define sys_port_trace_rtio_cqe_release(rtio, cqe)
```

相关声明：[sys_port_trace_rtio_cqe_release](#ga3c9cba898702f33dd67a0d4d39207c1f)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪释放RTIO完成队列事件的API（CQE Release）。

<a id="r_ga455112ec167445cd74d0766e9fd1f42d"></a>

```c
#define sys_port_trace_rtio_cqe_consume_enter(rtio)
```

相关声明：[sys_port_trace_rtio_cqe_consume_enter](#ga455112ec167445cd74d0766e9fd1f42d)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪取出RTIO完成队列事件的API入口（CQE Consume Enter）。

<a id="r_ga07ab46849195d30a7afc5a075021ad01"></a>

```c
#define sys_port_trace_rtio_cqe_consume_exit(rtio, cqe)
```

相关声明：[sys_port_trace_rtio_cqe_consume_exit](#ga07ab46849195d30a7afc5a075021ad01)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪取出RTIO完成队列事件的API出口（CQE Consume Exit）。

<a id="r_ga6332568a55719d48d99081a47eff477e"></a>

```c
#define sys_port_trace_rtio_txn_next_enter(rtio, iodev_sqe)
```

相关声明：[sys_port_trace_rtio_txn_next_enter](#ga6332568a55719d48d99081a47eff477e)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪RTIO获取下一事务条目的API入口（Transaction Next Enter）。

<a id="r_gade670a99f495bdf294af3240a453b357"></a>

```c
#define sys_port_trace_rtio_txn_next_exit(rtio, iodev_sqe)
```

相关声明：[sys_port_trace_rtio_txn_next_exit](#gade670a99f495bdf294af3240a453b357)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪RTIO获取下一事务条目的API出口（Transaction Next Exit）。

<a id="r_gabf68d73b57c2003df5afdf0e44fc4985"></a>

```c
#define sys_port_trace_rtio_chain_next_enter(rtio, iodev_sqe)
```

相关声明：[sys_port_trace_rtio_chain_next_enter](#gabf68d73b57c2003df5afdf0e44fc4985)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪RTIO获取链中下一个SQE的API入口（Chain Next Enter）。

<a id="r_ga4ef03a9bc62f6a16951750902d355aa2"></a>

```c
#define sys_port_trace_rtio_chain_next_exit(rtio, iodev_sqe)
```

相关声明：[sys_port_trace_rtio_chain_next_exit](#ga4ef03a9bc62f6a16951750902d355aa2)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

跟踪RTIO获取链中下一个SQE的API出口（Chain Next Exit）。

## 1.2\_详细说明（Detailed Documentation）

<a id="gabf68d73b57c2003df5afdf0e44fc4985"></a>

### `sys_port_trace_rtio_chain_next_enter`

```c
#define sys_port_trace_rtio_chain_next_enter ( rtio, iodev_sqe )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪RTIO获取链中下一个SQE的API入口（Chain Next Enter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |
| `iodev_sqe` | 当前提交队列条目（Submission Queue Entry）。 |

<a id="ga4ef03a9bc62f6a16951750902d355aa2"></a>

### `sys_port_trace_rtio_chain_next_exit`

```c
#define sys_port_trace_rtio_chain_next_exit ( rtio, iodev_sqe )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪RTIO获取链中下一个SQE的API出口（Chain Next Exit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |
| `iodev_sqe` | 下一个提交队列条目。 |

<a id="ga69b771f39b617335c1093a56f2e091c1"></a>

### `sys_port_trace_rtio_cqe_acquire_enter`

```c
#define sys_port_trace_rtio_cqe_acquire_enter ( rtio)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪获取RTIO完成队列事件的API入口（CQE Acquire Enter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |

<a id="ga3276c6d26ba5bbe5d0d84e2096a72162"></a>

### `sys_port_trace_rtio_cqe_acquire_exit`

```c
#define sys_port_trace_rtio_cqe_acquire_exit ( rtio, cqe )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪获取RTIO完成队列事件的API出口（CQE Acquire Exit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |
| `cqe` | 完成队列事件（Completion Queue Event，CQE）。 |

<a id="ga455112ec167445cd74d0766e9fd1f42d"></a>

### `sys_port_trace_rtio_cqe_consume_enter`

```c
#define sys_port_trace_rtio_cqe_consume_enter ( rtio)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪取出RTIO完成队列事件的API入口（CQE Consume Enter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |

<a id="ga07ab46849195d30a7afc5a075021ad01"></a>

### `sys_port_trace_rtio_cqe_consume_exit`

```c
#define sys_port_trace_rtio_cqe_consume_exit ( rtio, cqe )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪取出RTIO完成队列事件的API出口（CQE Consume Exit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |
| `cqe` | 完成队列事件（Completion Queue Event，CQE）。 |

<a id="ga3c9cba898702f33dd67a0d4d39207c1f"></a>

### `sys_port_trace_rtio_cqe_release`

```c
#define sys_port_trace_rtio_cqe_release ( rtio, cqe )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪释放RTIO完成队列事件的API（CQE Release）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |
| `cqe` | 完成队列事件（Completion Queue Event，CQE）。 |

<a id="gab31d0584e66a5a705adcb97c4c383b60"></a>

### `sys_port_trace_rtio_cqe_submit_enter`

```c
#define sys_port_trace_rtio_cqe_submit_enter ( rtio, result, flags )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪提交RTIO完成队列事件的API入口（CQE Submit Enter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |
| `result` | 整数结果码，可能为`-errno`。 |
| `flags` | 用于CQE的标志，参见`RTIO_CQE_FLAG_*`。 |

<a id="gac9bdbc3e33419eff6f7262108e98882d"></a>

### `sys_port_trace_rtio_cqe_submit_exit`

```c
#define sys_port_trace_rtio_cqe_submit_exit ( rtio)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪提交RTIO完成队列事件的API出口（CQE Submit Exit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |

<a id="ga3d2692eeafbb425a32927c012762a9be"></a>

### `sys_port_trace_rtio_sqe_acquire_enter`

```c
#define sys_port_trace_rtio_sqe_acquire_enter ( rtio)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪获取RTIO提交队列事件的API入口（SQE Acquire Enter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |

<a id="ga1606ca3ab8397414075b430d7c3d9a82"></a>

### `sys_port_trace_rtio_sqe_acquire_exit`

```c
#define sys_port_trace_rtio_sqe_acquire_exit ( rtio, sqe )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪获取RTIO提交队列事件的API出口（SQE Acquire Exit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |
| `sqe` | 提交队列事件（Submission Queue Event，SQE）。 |

<a id="ga24fc0a40280f6f06f15c70ba803a4cb6"></a>

### `sys_port_trace_rtio_sqe_cancel`

```c
#define sys_port_trace_rtio_sqe_cancel ( sqe)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪取消RTIO提交队列事件的API（SQE Cancel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sqe` | 提交队列事件（Submission Queue Event，SQE）。 |

<a id="ga47d934c79b989e0188f8b507b6cc5283"></a>

### `sys_port_trace_rtio_submit_enter`

```c
#define sys_port_trace_rtio_submit_enter ( rtio, wait_count )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪RTIO提交API的入口（Submit Enter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |
| `wait_count` | 要等待其完成的提交数量。 |

<a id="gaf51564de963093cb5e738232363aebe6"></a>

### `sys_port_trace_rtio_submit_exit`

```c
#define sys_port_trace_rtio_submit_exit ( rtio)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪RTIO提交API的出口（Submit Exit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |

<a id="ga6332568a55719d48d99081a47eff477e"></a>

### `sys_port_trace_rtio_txn_next_enter`

```c
#define sys_port_trace_rtio_txn_next_enter ( rtio, iodev_sqe )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪RTIO获取下一事务条目的API入口（Transaction Next Enter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |
| `iodev_sqe` | 当前提交队列条目（Submission Queue Entry）。 |

<a id="gade670a99f495bdf294af3240a453b357"></a>

### `sys_port_trace_rtio_txn_next_exit`

```c
#define sys_port_trace_rtio_txn_next_exit ( rtio, iodev_sqe )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪RTIO获取下一事务条目的API出口（Transaction Next Exit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rtio` | RTIO上下文（Context）。 |
| `iodev_sqe` | 下一个提交队列条目。 |

## 1.3\_源码定位与版本边界

相对源码定位：[跟踪入口](../../../include/zephyr/tracing/tracing.h)、[钩子声明](../../../include/zephyr/tracing/tracing_hooks.h)、[包装宏](../../../include/zephyr/tracing/tracing_macros.h)、[跟踪配置](../../../subsys/tracing/Kconfig)、[RTIO核心](../../../include/zephyr/rtio/rtio.h)、[SQE辅助函数](../../../include/zephyr/rtio/sqe.h)、[GPIO接口](../../../include/zephyr/drivers/gpio.h)、[GPIO回调分派](../../../include/zephyr/drivers/gpio/gpio_utils.h)、[工作队列](../../../kernel/work.c)、[轮询工作](../../../kernel/poll.c)、[设备运行时电源管理](../../../subsys/pm/device_runtime.c)及[系统电源管理](../../../subsys/pm/pm.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：本页是跟踪钩子（Tracing Hooks）的接口约定，不是替代原功能API的操作入口。tracing_hooks.h为尚未由后端定义的钩子提供空宏，并用#ifndef保留后端已有定义。仅有宏声明或开启功能模块，不等于已经生成可导出的事件数据；具体记录由所选跟踪格式与后端实现。

> 译注——源码核对：跟踪包装宏在原调用位置执行，不自动转到独立工作线程。CONFIG_TRACING关闭时，SYS_PORT_TRACING系列编译为空操作；对象类钩子还受相应类型开关控制。钩子可能位于中断、锁保护或调度敏感路径，后端实现应遵守实际调用上下文，不能把宏参数求值当作业务必需的副作用。

> 译注——源码核对：Enter、Blocking、Exit分别表示调用入口、某处阻塞标记与调用出口；它们不天然组成每条路径都一一配对的记录，也不自动表示外设完成或回调已执行。返回值按所属API解释，不能把所有ret都当成同一种errno或成功布尔值。

> 译注——源码核对：提交跟踪中的wait_count是请求等待的完成数量。submit_exit只有rtio上下文参数，没有操作结果参数；观察该出口不等于获得全部CQE，也不能推断所有I/O成功。CQE提交入口记录result和flags，SQE／CQE acquire或consume出口的指针可能为空，需按实际资源状态解读。

> 译注——源码核对：本次sqe.h中的rtio_chain_next()实际仍通过txn_next名称发出进入和退出跟踪；本页虽然声明chain_next钩子，不能据声明就认定当前该函数会调用它。译文保留两组官方接口，并把调用点差异明确列出。

> 译注——源码核对：SQE取消钩子记录取消请求，不证明硬件被中止。CQE释放与数据缓冲区释放也不同。完整生命周期见[RTIO核心接口](../rtio_core_reference/P001_RTIO公共接口.md)。

> 译注——源码核对：本次译注以来源记录中的官方源码摘要为界，本仓库同名文件通过相对链接定位；未配置跟踪硬件、运行采集或验证事件时序。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.4\_原页交叉引用（Cross References）

- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zephyr/tracing/tracing_hooks.h](../tracing_hooks_reference/P001_完整跟踪钩子头文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_GPIO跟踪接口.md)
