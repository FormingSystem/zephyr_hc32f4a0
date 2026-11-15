---
id: learning.zephyr-docs.object-trace-reference.page-1
title: FIFO跟踪接口
kind: reference
status: maintained
domains: [zephyr, kernel, tracing, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__tracing__apis__fifo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_FIFO跟踪接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__tracing__apis__fifo.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入FIFO、LIFO、队列、消息队列、邮箱、管道、栈、堆和内存块池的跟踪接口，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

先进先出队列（FIFO）事件的跟踪钩子（Tracing Hooks）。

<a id="details"></a>

先进先出队列（FIFO）事件的跟踪钩子（Tracing Hooks）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_gac0da5eca137a970c67b7b94a568c93e6"></a>

```c
#define sys_port_trace_k_fifo_init_enter(fifo)
```

相关声明：[sys_port_trace_k_fifo_init_enter](#gac0da5eca137a970c67b7b94a568c93e6)。

跟踪FIFO队列初始化的入口。

<a id="r_gaaf6c7c710377f449d52c5d6f5f7103c8"></a>

```c
#define sys_port_trace_k_fifo_init_exit(fifo)
```

相关声明：[sys_port_trace_k_fifo_init_exit](#gaaf6c7c710377f449d52c5d6f5f7103c8)。

跟踪FIFO队列初始化的出口。

<a id="r_ga81e706aff605468683a96b14940745e7"></a>

```c
#define sys_port_trace_k_fifo_cancel_wait_enter(fifo)
```

相关声明：[sys_port_trace_k_fifo_cancel_wait_enter](#ga81e706aff605468683a96b14940745e7)。

跟踪取消FIFO队列等待（Cancel Wait）的入口。

<a id="r_ga03ccb2bb3141c2842959ba77e4cd7337"></a>

```c
#define sys_port_trace_k_fifo_cancel_wait_exit(fifo)
```

相关声明：[sys_port_trace_k_fifo_cancel_wait_exit](#ga03ccb2bb3141c2842959ba77e4cd7337)。

跟踪取消FIFO队列等待（Cancel Wait）的出口。

<a id="r_gaac5f6b9e77dad9de4652d24502ab46d0"></a>

```c
#define sys_port_trace_k_fifo_put_enter(fifo, data)
```

相关声明：[sys_port_trace_k_fifo_put_enter](#gaac5f6b9e77dad9de4652d24502ab46d0)。

跟踪向FIFO队列放入数据（Put）的入口。

<a id="r_ga7a1d15a538f23d2b7f290435803cd73e"></a>

```c
#define sys_port_trace_k_fifo_put_exit(fifo, data)
```

相关声明：[sys_port_trace_k_fifo_put_exit](#ga7a1d15a538f23d2b7f290435803cd73e)。

跟踪向FIFO队列放入数据（Put）的出口。

<a id="r_ga9c433ad8dc99ac38b8d5b4755da05c67"></a>

```c
#define sys_port_trace_k_fifo_alloc_put_enter(fifo, data)
```

相关声明：[sys_port_trace_k_fifo_alloc_put_enter](#ga9c433ad8dc99ac38b8d5b4755da05c67)。

跟踪FIFO队列分配节点并放入数据（Alloc Put）的入口。

<a id="r_gad9871fb1487a387a4f73e94bccb99a6d"></a>

```c
#define sys_port_trace_k_fifo_alloc_put_exit(fifo, data, ret)
```

相关声明：[sys_port_trace_k_fifo_alloc_put_exit](#gad9871fb1487a387a4f73e94bccb99a6d)。

跟踪FIFO队列分配节点并放入数据（Alloc Put）的出口。

<a id="r_gace20fdce59a99b92c8ac3711c4085b28"></a>

```c
#define sys_port_trace_k_fifo_put_list_enter(fifo, head, tail)
```

相关声明：[sys_port_trace_k_fifo_put_list_enter](#gace20fdce59a99b92c8ac3711c4085b28)。

跟踪向FIFO队列放入链表（Put List）的入口。

<a id="r_ga739360e2cefa158f22ce20a1e9369aea"></a>

```c
#define sys_port_trace_k_fifo_put_list_exit(fifo, head, tail)
```

相关声明：[sys_port_trace_k_fifo_put_list_exit](#ga739360e2cefa158f22ce20a1e9369aea)。

跟踪向FIFO队列放入链表（Put List）的出口。

<a id="r_gabe92127699cc59f09b5099ae92c96ef9"></a>

```c
#define sys_port_trace_k_fifo_put_slist_enter(fifo, list)
```

相关声明：[sys_port_trace_k_fifo_put_slist_enter](#gabe92127699cc59f09b5099ae92c96ef9)。

跟踪向FIFO队列放入单向链表（Put Slist）的入口。

<a id="r_gaf80375a67c45ce490bebbfec6ddedab7"></a>

```c
#define sys_port_trace_k_fifo_put_slist_exit(fifo, list)
```

相关声明：[sys_port_trace_k_fifo_put_slist_exit](#gaf80375a67c45ce490bebbfec6ddedab7)。

跟踪向FIFO队列放入单向链表（Put Slist）的出口。

<a id="r_gaa3539eea74888c6257c5f5d456748155"></a>

```c
#define sys_port_trace_k_fifo_get_enter(fifo, timeout)
```

相关声明：[sys_port_trace_k_fifo_get_enter](#gaa3539eea74888c6257c5f5d456748155)。

跟踪从FIFO队列取出数据（Get）的入口。

<a id="r_gae6f06386f224063ee756e8ff0000dfe4"></a>

```c
#define sys_port_trace_k_fifo_get_exit(fifo, timeout, ret)
```

相关声明：[sys_port_trace_k_fifo_get_exit](#gae6f06386f224063ee756e8ff0000dfe4)。

跟踪从FIFO队列取出数据（Get）的出口。

<a id="r_gab0fea5751e0296e623606e54efe5687b"></a>

```c
#define sys_port_trace_k_fifo_peek_head_enter(fifo)
```

相关声明：[sys_port_trace_k_fifo_peek_head_enter](#gab0fea5751e0296e623606e54efe5687b)。

跟踪查看FIFO队首（Peek Head）的入口。

<a id="r_ga06b74415be416b137092cb72187c1fb6"></a>

```c
#define sys_port_trace_k_fifo_peek_head_exit(fifo, ret)
```

相关声明：[sys_port_trace_k_fifo_peek_head_exit](#ga06b74415be416b137092cb72187c1fb6)。

跟踪查看FIFO队首（Peek Head）的出口。

<a id="r_gad9f9b3193ed2c7270030036aef8d343d"></a>

```c
#define sys_port_trace_k_fifo_peek_tail_enter(fifo)
```

相关声明：[sys_port_trace_k_fifo_peek_tail_enter](#gad9f9b3193ed2c7270030036aef8d343d)。

跟踪查看FIFO队尾（Peek Tail）的入口。

<a id="r_gae33baafbaac06ada7d6b53026a973d81"></a>

```c
#define sys_port_trace_k_fifo_peek_tail_exit(fifo, ret)
```

相关声明：[sys_port_trace_k_fifo_peek_tail_exit](#gae33baafbaac06ada7d6b53026a973d81)。

跟踪查看FIFO队尾（Peek Tail）的出口。

## 1.2\_详细说明（Detailed Documentation）

<a id="ga9c433ad8dc99ac38b8d5b4755da05c67"></a>

### `sys_port_trace_k_fifo_alloc_put_enter`

```c
#define sys_port_trace_k_fifo_alloc_put_enter ( fifo, data )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪FIFO队列分配节点并放入数据（Alloc Put）的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |
| `data` | 数据项（Data Item） |

<a id="gad9871fb1487a387a4f73e94bccb99a6d"></a>

### `sys_port_trace_k_fifo_alloc_put_exit`

```c
#define sys_port_trace_k_fifo_alloc_put_exit ( fifo, data, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪FIFO队列分配节点并放入数据（Alloc Put）的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |
| `data` | 数据项（Data Item） |
| `ret` | 返回值（Return Value） |

<a id="ga81e706aff605468683a96b14940745e7"></a>

### `sys_port_trace_k_fifo_cancel_wait_enter`

```c
#define sys_port_trace_k_fifo_cancel_wait_enter ( fifo)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪取消FIFO队列等待（Cancel Wait）的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |

<a id="ga03ccb2bb3141c2842959ba77e4cd7337"></a>

### `sys_port_trace_k_fifo_cancel_wait_exit`

```c
#define sys_port_trace_k_fifo_cancel_wait_exit ( fifo)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪取消FIFO队列等待（Cancel Wait）的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |

<a id="gaa3539eea74888c6257c5f5d456748155"></a>

### `sys_port_trace_k_fifo_get_enter`

```c
#define sys_port_trace_k_fifo_get_enter ( fifo, timeout )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪从FIFO队列取出数据（Get）的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |
| `timeout` | 超时时间（Timeout Period） |

<a id="gae6f06386f224063ee756e8ff0000dfe4"></a>

### `sys_port_trace_k_fifo_get_exit`

```c
#define sys_port_trace_k_fifo_get_exit ( fifo, timeout, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪从FIFO队列取出数据（Get）的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |
| `timeout` | 超时时间（Timeout Period） |
| `ret` | 返回值（Return Value） |

<a id="gac0da5eca137a970c67b7b94a568c93e6"></a>

### `sys_port_trace_k_fifo_init_enter`

```c
#define sys_port_trace_k_fifo_init_enter ( fifo)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪FIFO队列初始化的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |

<a id="gaaf6c7c710377f449d52c5d6f5f7103c8"></a>

### `sys_port_trace_k_fifo_init_exit`

```c
#define sys_port_trace_k_fifo_init_exit ( fifo)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪FIFO队列初始化的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |

<a id="gab0fea5751e0296e623606e54efe5687b"></a>

### `sys_port_trace_k_fifo_peek_head_enter`

```c
#define sys_port_trace_k_fifo_peek_head_enter ( fifo)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪查看FIFO队首（Peek Head）的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |

<a id="ga06b74415be416b137092cb72187c1fb6"></a>

### `sys_port_trace_k_fifo_peek_head_exit`

```c
#define sys_port_trace_k_fifo_peek_head_exit ( fifo, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪查看FIFO队首（Peek Head）的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |
| `ret` | 返回值（Return Value） |

<a id="gad9f9b3193ed2c7270030036aef8d343d"></a>

### `sys_port_trace_k_fifo_peek_tail_enter`

```c
#define sys_port_trace_k_fifo_peek_tail_enter ( fifo)
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪查看FIFO队尾（Peek Tail）的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |

<a id="gae33baafbaac06ada7d6b53026a973d81"></a>

### `sys_port_trace_k_fifo_peek_tail_exit`

```c
#define sys_port_trace_k_fifo_peek_tail_exit ( fifo, ret )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪查看FIFO队尾（Peek Tail）的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |
| `ret` | 返回值（Return Value） |

<a id="gaac5f6b9e77dad9de4652d24502ab46d0"></a>

### `sys_port_trace_k_fifo_put_enter`

```c
#define sys_port_trace_k_fifo_put_enter ( fifo, data )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪向FIFO队列放入数据（Put）的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |
| `data` | 数据项（Data Item） |

<a id="ga7a1d15a538f23d2b7f290435803cd73e"></a>

### `sys_port_trace_k_fifo_put_exit`

```c
#define sys_port_trace_k_fifo_put_exit ( fifo, data )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪向FIFO队列放入数据（Put）的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |
| `data` | 数据项（Data Item） |

<a id="gace20fdce59a99b92c8ac3711c4085b28"></a>

### `sys_port_trace_k_fifo_put_list_enter`

```c
#define sys_port_trace_k_fifo_put_list_enter ( fifo, head, tail )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪向FIFO队列放入链表（Put List）的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |
| `head` | 首个链表节点（First Linked-list Node） |
| `tail` | 最后一个链表节点（Last Linked-list Node） |

<a id="ga739360e2cefa158f22ce20a1e9369aea"></a>

### `sys_port_trace_k_fifo_put_list_exit`

```c
#define sys_port_trace_k_fifo_put_list_exit ( fifo, head, tail )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪向FIFO队列放入链表（Put List）的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |
| `head` | 首个链表节点（First Linked-list Node） |
| `tail` | 最后一个链表节点（Last Linked-list Node） |

<a id="gabe92127699cc59f09b5099ae92c96ef9"></a>

### `sys_port_trace_k_fifo_put_slist_enter`

```c
#define sys_port_trace_k_fifo_put_slist_enter ( fifo, list )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪向FIFO队列放入单向链表（Put Slist）的入口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |
| `list` | 系统单向链表对象（Syslist Object） |

<a id="gaf80375a67c45ce490bebbfec6ddedab7"></a>

### `sys_port_trace_k_fifo_put_slist_exit`

```c
#define sys_port_trace_k_fifo_put_slist_exit ( fifo, list )
```

```c
#include <zephyr/tracing/tracing_hooks.h>
```

跟踪向FIFO队列放入单向链表（Put Slist）的出口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | 先进先出队列对象（FIFO Object） |
| `list` | 系统单向链表对象（Syslist Object） |

## 1.3\_源码定位与版本边界

相对源码定位：[跟踪入口](../../../include/zephyr/tracing/tracing.h)、[钩子声明](../../../include/zephyr/tracing/tracing_hooks.h)、[包装宏](../../../include/zephyr/tracing/tracing_macros.h)、[跟踪配置](../../../subsys/tracing/Kconfig)、[内核公共接口](../../../include/zephyr/kernel.h)、[队列](../../../kernel/queue.c)、[消息队列](../../../kernel/msg_q.c)、[邮箱](../../../kernel/mailbox.c)、[管道](../../../kernel/pipe.c)、[栈](../../../kernel/stack.c)、[内核堆](../../../kernel/kheap.c)、[系统内存分配](../../../kernel/mempool.c)及[内存块池](../../../kernel/mem_slab.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：这些跟踪钩子（Tracing Hooks）用于记录原API的调用位置，不替代对象操作。tracing_hooks.h通过#ifndef为后端尚未定义的钩子提供空宏；启用对象功能并不自动产生可导出的记录。总跟踪开关、对象开关和所选后端共同决定实际输出。

> 译注——源码核对：入口（Enter）、阻塞（Blocking）和出口（Exit）是源码中的标记名称，不保证所有路径都有成对记录。钩子直接在调用点执行，可能处于自旋锁保护、中断或调度敏感上下文。timeout是请求参数；ret可能是指针、布尔值、字节数或错误码，应以对应API为准。

> 译注——源码核对：先进先出（First In, First Out，FIFO）包装宏位于kernel.h，底层使用k_queue。一次FIFO操作可能同时出现FIFO和Queue两层事件，它们属于同一次调用的不同层次，不能当成两次数据操作。

> 译注——源码核对：put传递数据项指针，alloc_put在需要时分配的是队列包装节点，不是自动深拷贝数据内容。get_exit与peek出口的ret是数据指针，可能为NULL；put_list／put_slist出口没有底层返回码，不能仅凭出口事件判断所有输入均有效。

> 译注——源码核对：以上源码译注以来源记录中的官方版本摘要为依据，与官方正文分开标注。仓库源码用相对路径定位；未配置采集设备或验证实测事件顺序。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.4\_原页交叉引用（Cross References）

- [zephyr/tracing/tracing_hooks.h](../tracing_hooks_reference/P001_完整跟踪钩子头文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_LIFO跟踪接口.md)
