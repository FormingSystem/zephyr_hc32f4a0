---
id: learning.zephyr-docs.object-trace-reference.page-2
title: LIFO跟踪接口
kind: reference
status: maintained
domains: [zephyr, kernel, tracing, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__tracing__apis__lifo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_LIFO跟踪接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__tracing__apis__lifo.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入FIFO、LIFO、队列、消息队列、邮箱、管道、栈、堆和内存块池的跟踪接口，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

后进先出队列（LIFO）事件的跟踪钩子（Tracing Hooks）。

<a id="details"></a>

后进先出队列（LIFO）事件的跟踪钩子（Tracing Hooks）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_gaad81b60363467b56d887baee8c8b5bf2"></a>

```c
#define sys_port_trace_k_lifo_init_enter(lifo)
```

相关声明：[sys_port_trace_k_lifo_init_enter](#gaad81b60363467b56d887baee8c8b5bf2)。

跟踪LIFO队列初始化的入口。

<a id="r_ga4f08168ded97456265abb3a903585ecf"></a>

```c
#define sys_port_trace_k_lifo_init_exit(lifo)
```

相关声明：[sys_port_trace_k_lifo_init_exit](#ga4f08168ded97456265abb3a903585ecf)。

跟踪LIFO队列初始化的出口。

<a id="r_gafd9c45a171a2fb146defa356ff0bc0f5"></a>

```c
#define sys_port_trace_k_lifo_put_enter(lifo, data)
```

相关声明：[sys_port_trace_k_lifo_put_enter](#gafd9c45a171a2fb146defa356ff0bc0f5)。

跟踪向LIFO队列放入数据（Put）的入口。

<a id="r_ga0e5372c37bdd3a47adf11ab9d3a5e22d"></a>

```c
#define sys_port_trace_k_lifo_put_exit(lifo, data)
```

相关声明：[sys_port_trace_k_lifo_put_exit](#ga0e5372c37bdd3a47adf11ab9d3a5e22d)。

跟踪向LIFO队列放入数据（Put）的出口。

<a id="r_ga0d9717f4b43e344518cc451a2fe9d224"></a>

```c
#define sys_port_trace_k_lifo_alloc_put_enter(lifo, data)
```

相关声明：[sys_port_trace_k_lifo_alloc_put_enter](#ga0d9717f4b43e344518cc451a2fe9d224)。

跟踪LIFO队列分配节点并放入数据（Alloc Put）的入口。

<a id="r_ga19bb748367aba8f576e72cdc30834ab1"></a>

```c
#define sys_port_trace_k_lifo_alloc_put_exit(lifo, data, ret)
```

相关声明：[sys_port_trace_k_lifo_alloc_put_exit](#ga19bb748367aba8f576e72cdc30834ab1)。

跟踪LIFO队列分配节点并放入数据（Alloc Put）的出口。

<a id="r_ga61556928453492dc6ed4efc999668f01"></a>

```c
#define sys_port_trace_k_lifo_get_enter(lifo, timeout)
```

相关声明：[sys_port_trace_k_lifo_get_enter](#ga61556928453492dc6ed4efc999668f01)。

跟踪从LIFO队列取出数据（Get）的入口。

<a id="r_ga2f7e8e680cac03844ca5dbab0438a754"></a>

```c
#define sys_port_trace_k_lifo_get_exit(lifo, timeout, ret)
```

相关声明：[sys_port_trace_k_lifo_get_exit](#ga2f7e8e680cac03844ca5dbab0438a754)。

跟踪从LIFO队列取出数据（Get）的出口。

## 2.2\_详细说明（Detailed Documentation）

<a id="ga0d9717f4b43e344518cc451a2fe9d224"></a>

### `sys_port_trace_k_lifo_alloc_put_enter`

```c
#define sys_port_trace_k_lifo_alloc_put_enter ( lifo, data )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪LIFO队列分配节点并放入数据（Alloc Put）的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lifo` | 后进先出队列对象（LIFO Object） |
| `data` | 数据项（Data Item） |

<a id="ga19bb748367aba8f576e72cdc30834ab1"></a>

### `sys_port_trace_k_lifo_alloc_put_exit`

```c
#define sys_port_trace_k_lifo_alloc_put_exit ( lifo, data, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪LIFO队列分配节点并放入数据（Alloc Put）的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lifo` | 后进先出队列对象（LIFO Object） |
| `data` | 数据项（Data Item） |
| `ret` | 返回值（Return Value） |

<a id="ga61556928453492dc6ed4efc999668f01"></a>

### `sys_port_trace_k_lifo_get_enter`

```c
#define sys_port_trace_k_lifo_get_enter ( lifo, timeout )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪从LIFO队列取出数据（Get）的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lifo` | 后进先出队列对象（LIFO Object） |
| `timeout` | 超时时间（Timeout Period） |

<a id="ga2f7e8e680cac03844ca5dbab0438a754"></a>

### `sys_port_trace_k_lifo_get_exit`

```c
#define sys_port_trace_k_lifo_get_exit ( lifo, timeout, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪从LIFO队列取出数据（Get）的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lifo` | 后进先出队列对象（LIFO Object） |
| `timeout` | 超时时间（Timeout Period） |
| `ret` | 返回值（Return Value） |

<a id="gaad81b60363467b56d887baee8c8b5bf2"></a>

### `sys_port_trace_k_lifo_init_enter`

```c
#define sys_port_trace_k_lifo_init_enter ( lifo)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪LIFO队列初始化的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lifo` | 后进先出队列对象（LIFO Object） |

<a id="ga4f08168ded97456265abb3a903585ecf"></a>

### `sys_port_trace_k_lifo_init_exit`

```c
#define sys_port_trace_k_lifo_init_exit ( lifo)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪LIFO队列初始化的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lifo` | 后进先出队列对象（LIFO Object） |

<a id="gafd9c45a171a2fb146defa356ff0bc0f5"></a>

### `sys_port_trace_k_lifo_put_enter`

```c
#define sys_port_trace_k_lifo_put_enter ( lifo, data )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪向LIFO队列放入数据（Put）的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lifo` | 后进先出队列对象（LIFO Object） |
| `data` | 数据项（Data Item） |

<a id="ga0e5372c37bdd3a47adf11ab9d3a5e22d"></a>

### `sys_port_trace_k_lifo_put_exit`

```c
#define sys_port_trace_k_lifo_put_exit ( lifo, data )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪向LIFO队列放入数据（Put）的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lifo` | 后进先出队列对象（LIFO Object） |
| `data` | 数据项（Data Item） |

## 2.3\_源码定位与版本边界

相对源码定位：[跟踪入口](../../../include/zephyr/tracing/tracing.h)、[钩子声明](../../../include/zephyr/tracing/tracing_hooks.h)、[包装宏](../../../include/zephyr/tracing/tracing_macros.h)、[跟踪配置](../../../subsys/tracing/Kconfig)、[内核公共接口](../../../include/zephyr/kernel.h)、[队列](../../../kernel/queue.c)、[消息队列](../../../kernel/msg_q.c)、[邮箱](../../../kernel/mailbox.c)、[管道](../../../kernel/pipe.c)、[栈](../../../kernel/stack.c)、[内核堆](../../../kernel/kheap.c)、[系统内存分配](../../../kernel/mempool.c)及[内存块池](../../../kernel/mem_slab.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：这些跟踪钩子（Tracing Hooks）用于记录原API的调用位置，不替代对象操作。tracing_hooks.h通过#ifndef为后端尚未定义的钩子提供空宏；启用对象功能并不自动产生可导出的记录。总跟踪开关、对象开关和所选后端共同决定实际输出。

> 译注——源码核对：入口（Enter）、阻塞（Blocking）和出口（Exit）是源码中的标记名称，不保证所有路径都有成对记录。钩子直接在调用点执行，可能处于自旋锁保护、中断或调度敏感上下文。timeout是请求参数；ret可能是指针、布尔值、字节数或错误码，应以对应API为准。

> 译注——源码核对：后进先出（Last In, First Out，LIFO）使用k_queue_prepend插入队首，get使用k_queue_get。外层LIFO和内层Queue事件可以嵌套出现；原始宏名与对象地址需要一起分析。

> 译注——源码核对：alloc_put的ret是节点分配／插入操作结果，而get的ret是取出的数据指针。带alloc不表示为应用数据另外分配并复制内容；没有单独LIFO blocking钩子也不表示get不会等待，实际等待发生在底层队列中。

> 译注——源码核对：以上源码译注以来源记录中的官方版本摘要为依据，与官方正文分开标注。仓库源码用相对路径定位；未配置采集设备或验证实测事件顺序。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.4\_原页交叉引用（Cross References）

- [zephyr/tracing/tracing_hooks.h](../tracing_hooks_reference/P001_完整跟踪钩子头文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P001_FIFO跟踪接口.md) · [返回大纲](大纲.md) · [下一章](P003_队列跟踪接口.md)
