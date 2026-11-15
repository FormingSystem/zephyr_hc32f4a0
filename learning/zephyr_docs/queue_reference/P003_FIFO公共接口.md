---
id: learning.zephyr-docs.queue-reference.page-3
title: FIFO公共接口
kind: reference
status: maintained
domains: [zephyr, kernel, synchronization, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__fifo__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_FIFO公共接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__fifo__apis.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本册覆盖通用队列（Queue）、先进先出队列（First In, First Out，FIFO）和后进先出队列（Last In, First Out，LIFO）。先读[本册大纲](大纲.md)及对应指南；原始宏展开、声明和参数保留，数据项布局、分配包装及源码差异另作明确译注。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_gaeebf6ef54d4be61e19408f44a734a159"></a>

```c
#define k_fifo_init(fifo)
```

相关声明：[k_fifo_init](#gaeebf6ef54d4be61e19408f44a734a159)。

初始化先进先出队列（First In, First Out，FIFO）。

<a id="r_gab744080af449e093df8dd4982e013e16"></a>

```c
#define k_fifo_cancel_wait(fifo)
```

相关声明：[k_fifo_cancel_wait](#gab744080af449e093df8dd4982e013e16)。

取消对FIFO队列的等待。

<a id="r_ga3addb10f86f19e245c23362433d5c913"></a>

```c
#define k_fifo_put(fifo, data)
```

相关声明：[k_fifo_put](#ga3addb10f86f19e245c23362433d5c913)。

向FIFO队列加入一个元素。

<a id="r_gab1c5212040d12cbb92cede5cf54928ba"></a>

```c
#define k_fifo_alloc_put(fifo, data)
```

相关声明：[k_fifo_alloc_put](#gab1c5212040d12cbb92cede5cf54928ba)。

向FIFO队列加入一个元素。

<a id="r_ga1bf5f52290c83e54ba14358cbbb4051b"></a>

```c
#define k_fifo_put_list(fifo, head, tail)
```

相关声明：[k_fifo_put_list](#ga1bf5f52290c83e54ba14358cbbb4051b)。

以原子方式向FIFO加入一个元素链表。

<a id="r_ga4cdc286a7a6f0d43acab63a4846815e7"></a>

```c
#define k_fifo_put_slist(fifo, list)
```

相关声明：[k_fifo_put_slist](#ga4cdc286a7a6f0d43acab63a4846815e7)。

以原子方式向FIFO队列加入一个元素链表。

<a id="r_ga1e2c480e2124116af97e94e7b4435de6"></a>

```c
#define k_fifo_get(fifo, timeout)
```

相关声明：[k_fifo_get](#ga1e2c480e2124116af97e94e7b4435de6)。

从FIFO队列取得一个元素。

<a id="r_gab7cec4adc128ed1fd2d194ba6cd8c640"></a>

```c
#define k_fifo_is_empty(fifo)
```

相关声明：[k_fifo_is_empty](#gab7cec4adc128ed1fd2d194ba6cd8c640)。

查询FIFO队列是否有可用数据。

<a id="r_ga2e0c8608f095a929740fa94c94a4f389"></a>

```c
#define k_fifo_peek_head(fifo)
```

相关声明：[k_fifo_peek_head](#ga2e0c8608f095a929740fa94c94a4f389)。

查看FIFO队列头部元素（Peek）。

<a id="r_gafbe2ce9a6437b886cf149016187ba92f"></a>

```c
#define k_fifo_peek_tail(fifo)
```

相关声明：[k_fifo_peek_tail](#gafbe2ce9a6437b886cf149016187ba92f)。

查看FIFO队列尾部元素（Peek）。

<a id="r_ga230b02a526ecb0ae1598be75cb9a8274"></a>

```c
#define K_FIFO_DEFINE(name)
```

相关声明：[K_FIFO_DEFINE](#ga230b02a526ecb0ae1598be75cb9a8274)。

静态定义并初始化FIFO队列。

## 3.2\_详细说明（Detailed Documentation）

<a id="gab1c5212040d12cbb92cede5cf54928ba"></a>

### `k_fifo_alloc_put`

```c
#define k_fifo_alloc_put ( fifo, data )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({ \
void *_data = data; \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_fifo, alloc_put, fifo, _data); \
int fap_ret = k_queue_alloc_append(&(fifo)->_queue, _data); \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_fifo, alloc_put, fifo, _data, fap_ret); \
fap_ret; \
})
```

向FIFO队列加入一个元素。

此例程向fifo加入一个数据项。它会隐式分配内存，从调用线程的资源池创建额外的临时管理数据结构；该项被移除时，管理结构自动释放。数据本身不会被复制。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | FIFO的地址。 |
| `data` | 数据项的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 操作成功。 |
| `-ENOMEM` | 调用者的资源池中没有足够的RAM。 |

> 译注——源码核对：当前宏显式保存并返回k_queue_alloc_append的结果。包装分配并不复制data，已有等待者时可直接交付且无须包装；不能把返回0解释为一定已发生堆分配。

<a id="gab744080af449e093df8dd4982e013e16"></a>

### `k_fifo_cancel_wait`

```c
#define k_fifo_cancel_wait ( fifo)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({ \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_fifo, cancel_wait, fifo); \
k_queue_cancel_wait(&(fifo)->_queue); \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_fifo, cancel_wait, fifo); \
})
```

取消对FIFO队列的等待。

如果存在等待fifo的线程，此例程使第一个等待线程从k_fifo_get()返回NULL，如同等待超时。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | FIFO队列的地址。 |

> 译注——源码核对：当前宏转发到k_queue_cancel_wait，取消一个get等待者，不是同时取消全部消费者或永久关闭FIFO。它不会从缓存中清除数据。

<a id="ga230b02a526ecb0ae1598be75cb9a8274"></a>

### `K_FIFO_DEFINE`

```c
#define K_FIFO_DEFINE ( name)
```

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
STRUCT_SECTION_ITERABLE(k_fifo, name) = \
        Z_FIFO_INITIALIZER(name)
```

静态定义并初始化FIFO队列。

在定义此FIFO队列的模块之外，可通过以下声明访问它：

原始示例（Example）：

```c
extern struct k_fifo <name>;
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | FIFO队列的名称。 |

> 译注——源码核对：宏定义并初始化FIFO对象，内部封装k_queue；extern示例中的<name>应替换为实际变量名。它不负责分配或复制应用数据。

<a id="ga1e2c480e2124116af97e94e7b4435de6"></a>

### `k_fifo_get`

```c
#define k_fifo_get ( fifo, timeout )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({ \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_fifo, get, fifo, timeout); \
void *fg_ret = k_queue_get(&(fifo)->_queue, timeout); \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_fifo, get, fifo, timeout, fg_ret); \
fg_ret; \
})
```

从FIFO队列取得一个元素。

此例程按照先进先出（First In, First Out）的顺序从fifo移除一个数据项。该数据项的第一个指针大小的字段保留给内核使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | FIFO队列的地址。 |
| `timeout` | 等待取得数据项的时长，或特殊值K_NO_WAIT、K_FOREVER之一。 |

**说明（Note）**：如果从中断服务程序（Interrupt Service Routine，ISR）调用，timeout必须设置为K_NO_WAIT。

**返回（Returns）**：成功时返回数据项地址；未等待便返回或等待超时时，返回NULL。

> 译注——源码核对：通过k_queue_get从头部取得数据，保持缓存项的先进先出顺序。NULL可表示空队列不等待、超时或取消；ISR必须用K_NO_WAIT。分配型包装在出队时释放，但data对象不自动释放。

<a id="gaeebf6ef54d4be61e19408f44a734a159"></a>

### `k_fifo_init`

```c
#define k_fifo_init ( fifo)
```

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({                                                   \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_fifo, init, fifo); \
k_queue_init(&(fifo)->_queue);                       \
K_OBJ_CORE_INIT(K_OBJ_CORE(fifo), _obj_type_fifo);   \
K_OBJ_CORE_LINK(K_OBJ_CORE(fifo));                   \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_fifo, init, fifo);  \
})
```

初始化先进先出队列（First In, First Out，FIFO）。

此例程在FIFO队列第一次使用前初始化它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | FIFO队列的地址。 |

> 译注——源码核对：当前宏初始化内部_queue，并按配置处理对象核心（Object Core）信息；不是销毁或回收已有数据项的接口。

<a id="gab7cec4adc128ed1fd2d194ba6cd8c640"></a>

### `k_fifo_is_empty`

```c
#define k_fifo_is_empty ( fifo)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
k_queue_is_empty(&(fifo)->_queue)
```

查询FIFO队列是否有可用数据。

如果其他线程也在尝试读取FIFO，本函数返回时，数据可能已经被取走。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | FIFO队列的地址。 |

**返回（Returns）**：FIFO队列为空时返回非零；有可用数据时返回0。

> 译注——源码核对：返回非零表示空，0表示有数据；它不能保证后续get仍能成功。多消费者场景应以get的实际结果为准。

<a id="ga2e0c8608f095a929740fa94c94a4f389"></a>

### `k_fifo_peek_head`

```c
#define k_fifo_peek_head ( fifo)
```

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({ \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_fifo, peek_head, fifo); \
void *fph_ret = k_queue_peek_head(&(fifo)->_queue); \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_fifo, peek_head, fifo, fph_ret); \
fph_ret; \
})
```

查看FIFO队列头部元素（Peek）。

返回FIFO队列头部元素，但不将其移除。一种用途是FIFO元素本身是容器（Container）：每轮处理先查看头部容器，从中处理部分数据，只有当容器为空时，才将整个容器从FIFO队列移除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | FIFO队列的地址。 |

**返回（Returns）**：返回头部元素；FIFO队列为空时返回NULL。

> 译注——源码核对：原容器用例仍需应用同步。peek不取走元素，也不预留容器或保护后续处理时间；其他上下文可能移除它，不能把窥视指针视为长期有效的所有权。

<a id="gafbe2ce9a6437b886cf149016187ba92f"></a>

### `k_fifo_peek_tail`

```c
#define k_fifo_peek_tail ( fifo)
```

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({ \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_fifo, peek_tail, fifo); \
void *fpt_ret = k_queue_peek_tail(&(fifo)->_queue); \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_fifo, peek_tail, fifo, fpt_ret); \
fpt_ret; \
})
```

查看FIFO队列尾部元素（Peek）。

返回FIFO队列尾部元素，但不将其移除。一种用途是FIFO队列元素本身是容器，此时可能需要向队列中的最后一个容器追加更多数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | FIFO队列的地址。 |

**返回（Returns）**：返回尾部元素；FIFO队列为空时返回NULL。

> 译注——源码核对：向末尾容器补充数据属于应用对象操作，peek本身没有为修改容器内容提供持续加锁。必须同时处理对象生命周期与生产者／消费者之间的同步。

<a id="ga3addb10f86f19e245c23362433d5c913"></a>

### `k_fifo_put`

```c
#define k_fifo_put ( fifo, data )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({ \
void *_data = data; \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_fifo, put, fifo, _data); \
k_queue_append(&(fifo)->_queue, _data); \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_fifo, put, fifo, _data); \
})
```

向FIFO队列加入一个元素。

此例程向fifo加入一个数据项。FIFO数据项必须满足指针的对齐要求，且其第一个指针大小的字段保留给内核使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | FIFO的地址。 |
| `data` | 数据项的地址。 |

> 译注——源码核对：当前宏使用k_queue_append实现FIFO尾部入队，直接使用数据项的预留链接字段。传送的是对象地址，不复制数据内容；必须保证对象在消费结束前有效。

<a id="ga1bf5f52290c83e54ba14358cbbb4051b"></a>

### `k_fifo_put_list`

```c
#define k_fifo_put_list ( fifo, head, tail )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({ \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_fifo, put_list, fifo, head, tail); \
k_queue_append_list(&(fifo)->_queue, head, tail); \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_fifo, put_list, fifo, head, tail); \
})
```

以原子方式向FIFO加入一个元素链表。

此例程在一次操作中向fifo加入一个数据项链表。数据项必须构成单向链表，每个数据项的第一个指针大小的字段指向下一项；链表必须以NULL结束。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | FIFO队列的地址。 |
| `head` | 指向单向链表第一个节点的指针。 |
| `tail` | 指向单向链表最后一个节点的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 操作成功。 |
| `-EINVAL` | 传入的数据无效。 |

> 译注——源码核对：原文列出0／-EINVAL返回值；本次宏体调用k_queue_append_list后，以SYS_PORT_TRACING_OBJ_FUNC_EXIT结束，没有保存并返回底层结果。本次tracing_macros.h在启用与未启用跟踪时都将该跟踪宏展开为do…while语句，因此这个语句表达式不能作为所承诺的整数结果使用。原始展开保留，不能照返回值表直接写成功比较表达式。

<a id="ga4cdc286a7a6f0d43acab63a4846815e7"></a>

### `k_fifo_put_slist`

```c
#define k_fifo_put_slist ( fifo, list )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({ \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_fifo, put_slist, fifo, list); \
k_queue_merge_slist(&(fifo)->_queue, list); \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_fifo, put_slist, fifo, list); \
})
```

以原子方式向FIFO队列加入一个元素链表。

此例程在一次操作中向fifo加入一个数据项链表。数据项必须位于由sys_slist_t对象表示的单向链表中。完成后，sys_slist_t对象失效，必须通过sys_slist_init()重新初始化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fifo` | FIFO队列的地址。 |
| `list` | 指向sys_slist_t对象的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 操作成功。 |
| `-EINVAL` | 传入的数据无效。 |

> 译注——源码核对：原文要求调用者重新初始化list；本次底层k_queue_merge_slist成功后已执行sys_slist_init，使源对象为空。节点已转移，不能继续按旧链表访问。与put_list一样，当前宏最后是跟踪语句，没有传出底层整数返回值；原返回值表保留并说明这一差异。

## 3.3\_源码定位与版本边界

> 译注——阅读与源码边界：配合[FIFO指南](../kernel/P014_FIFO先进先出队列.md)阅读。当前FIFO宏转发到k_queue并加跟踪调用；完整展开不可简化成看起来相同的函数调用，尤其两个链表宏未传出底层返回值。原文的链表重新初始化说明与当前merge实现也已分开标注。

仓库相对定位：[kernel.h](../../../include/zephyr/kernel.h)、[kernel/queue.c](../../../kernel/queue.c)与[sys/sflist.h](../../../include/zephyr/sys/sflist.h)。本次依据为[官方内核头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/kernel.h)、[官方队列实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/queue.c)及[官方带标志链表](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/sflist.h)，摘要见[来源记录](../SOURCES.md)。

FIFO链表宏的末尾语句另核对[官方tracing_macros.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/tracing/tracing_macros.h)，对应[仓库文件](../../../include/zephyr/tracing/tracing_macros.h)。

仓库源码、滚动更新的main和latest网页不能自动视为同一版本。本批完成文档与源码核对，未构建或执行队列并发、内存分配及实板实验。

## 3.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [k_fifo](P004_内核FIFO结构.md)
- [k_queue_alloc_append](P001_通用队列公共接口.md#ga690f3a1450e946d75f31b3e499d1d06a)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [k_queue_get](P001_通用队列公共接口.md#ga0a77d8556e7d253319275de034f01619)
- [K_OBJ_CORE](../object_core_reference/P001_对象核心公共接口.md#ga2bd0c2c121afc09448926a3648c7d814)
- [k_queue_is_empty](P001_通用队列公共接口.md#gadb2bb8088868b3c5801c72b320389ca9)
- [k_queue_peek_head](P001_通用队列公共接口.md#ga8ccd5137690c127a0f7d67619b88a52b)
- [k_queue_peek_tail](P001_通用队列公共接口.md#ga27a460c42836d8b093ad9274c14bb176)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [sys_slist_init()](../slist_reference/P001_单向链表公共接口.md#ga913aea7661b4ab3b4b50a8efc0d70428)

<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__queue__apis_html_ga690f3a1450e946d75f31b3e499d1d06a"></a>
<a id="astructk__fifo_html"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="agroup__queue__apis_html_ga0a77d8556e7d253319275de034f01619"></a>
<a id="agroup__obj__core__apis_html_ga2bd0c2c121afc09448926a3648c7d814"></a>
<a id="agroup__queue__apis_html_gadb2bb8088868b3c5801c72b320389ca9"></a>
<a id="agroup__queue__apis_html_ga8ccd5137690c127a0f7d67619b88a52b"></a>
<a id="agroup__queue__apis_html_ga27a460c42836d8b093ad9274c14bb176"></a>

---

[上一章](P002_内核队列结构.md) · [返回大纲](大纲.md) · [下一章](P004_内核FIFO结构.md)
