---
id: learning.zephyr-docs.queue-reference.page-5
title: LIFO公共接口
kind: reference
status: maintained
domains: [zephyr, kernel, synchronization, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lifo__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_LIFO公共接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lifo__apis.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本册覆盖通用队列（Queue）、先进先出队列（First In, First Out，FIFO）和后进先出队列（Last In, First Out，LIFO）。先读[本册大纲](大纲.md)及对应指南；原始宏展开、声明和参数保留，数据项布局、分配包装及源码差异另作明确译注。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_ga69fb19716a9014f7de79f8e524d64a3e"></a>

```c
#define k_lifo_init(lifo)
```

相关声明：[k_lifo_init](#ga69fb19716a9014f7de79f8e524d64a3e)。

初始化后进先出队列（Last In, First Out，LIFO）。

<a id="r_gad662e36b1df8b9013e2dc61f9dfe3a8b"></a>

```c
#define k_lifo_put(lifo, data)
```

相关声明：[k_lifo_put](#gad662e36b1df8b9013e2dc61f9dfe3a8b)。

向LIFO队列加入一个元素。

<a id="r_ga96d885a6a36fcfcb5eaa65898eee0965"></a>

```c
#define k_lifo_alloc_put(lifo, data)
```

相关声明：[k_lifo_alloc_put](#ga96d885a6a36fcfcb5eaa65898eee0965)。

向LIFO队列加入一个元素。

<a id="r_gad5f1775947b07a2a77f667aa9e41db5a"></a>

```c
#define k_lifo_get(lifo, timeout)
```

相关声明：[k_lifo_get](#gad5f1775947b07a2a77f667aa9e41db5a)。

从LIFO队列取得一个元素。

<a id="r_gaebd450d4181f22491623ea0aed6ee576"></a>

```c
#define K_LIFO_DEFINE(name)
```

相关声明：[K_LIFO_DEFINE](#gaebd450d4181f22491623ea0aed6ee576)。

静态定义并初始化LIFO队列。

## 5.2\_详细说明（Detailed Documentation）

<a id="ga96d885a6a36fcfcb5eaa65898eee0965"></a>

### `k_lifo_alloc_put`

```c
#define k_lifo_alloc_put ( lifo, data )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({ \
void *_data = data; \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_lifo, alloc_put, lifo, _data); \
int lap_ret = k_queue_alloc_prepend(&(lifo)->_queue, _data); \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_lifo, alloc_put, lifo, _data, lap_ret); \
lap_ret; \
})
```

向LIFO队列加入一个元素。

此例程向lifo加入一个数据项。它会隐式分配内存，从调用线程的资源池创建额外的临时管理数据结构；该项被移除时，管理结构自动释放。数据本身不会被复制。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lifo` | LIFO的地址。 |
| `data` | 数据项的地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 操作成功。 |
| `-ENOMEM` | 调用者的资源池中没有足够的RAM。 |

> 译注——源码核对：通过k_queue_alloc_prepend保存data指针，返回底层分配结果。已有等待者时不必分配包装；无等待者时需要临时包装，之后get或remove释放包装而非data本体。

<a id="gaebd450d4181f22491623ea0aed6ee576"></a>

### `K_LIFO_DEFINE`

```c
#define K_LIFO_DEFINE ( name)
```

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
STRUCT_SECTION_ITERABLE(k_lifo, name) = \
        Z_LIFO_INITIALIZER(name)
```

静态定义并初始化LIFO队列。

在定义此LIFO队列的模块之外，可通过以下声明访问它：

原始示例（Example）：

```c
extern struct k_lifo <name>;
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | fifo的名称。 |

> 译注——源码核对：参数说明中的“fifo”是原文笔误，此宏定义的是LIFO。内部仍封装k_queue；extern示例中的<name>应替换为实际变量标识符。

<a id="gad5f1775947b07a2a77f667aa9e41db5a"></a>

### `k_lifo_get`

```c
#define k_lifo_get ( lifo, timeout )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({ \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_lifo, get, lifo, timeout); \
void *lg_ret = k_queue_get(&(lifo)->_queue, timeout); \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_lifo, get, lifo, timeout, lg_ret); \
lg_ret; \
})
```

从LIFO队列取得一个元素。

此例程按照后进先出（Last In, First Out）的顺序从LIFO移除一个数据项。该数据项的第一个指针大小的字段保留给内核使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lifo` | LIFO队列的地址。 |
| `timeout` | 等待取得数据项的时长，或特殊值K_NO_WAIT、K_FOREVER之一。 |

**说明（Note）**：如果从中断服务程序（Interrupt Service Routine，ISR）调用，timeout必须设置为K_NO_WAIT。

**返回（Returns）**：成功时返回数据项地址；未等待便返回或等待超时时，返回NULL。

> 译注——源码核对：当前宏调用k_queue_get从头部取得数据；分配型数据返回原指针并释放包装。ISR不能等待，调用时须指定K_NO_WAIT；数据项生命周期仍由应用管理。

<a id="ga69fb19716a9014f7de79f8e524d64a3e"></a>

### `k_lifo_init`

```c
#define k_lifo_init ( lifo)
```

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({                                                   \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_lifo, init, lifo); \
k_queue_init(&(lifo)->_queue);                       \
K_OBJ_CORE_INIT(K_OBJ_CORE(lifo), _obj_type_lifo);   \
K_OBJ_CORE_LINK(K_OBJ_CORE(lifo));                   \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_lifo, init, lifo);  \
})
```

初始化后进先出队列（Last In, First Out，LIFO）。

此例程在LIFO队列对象第一次使用前初始化它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lifo` | LIFO队列的地址。 |

> 译注——源码核对：当前宏初始化内部_queue，并按配置处理对象核心信息，不回收已经入队的应用对象。

<a id="gad662e36b1df8b9013e2dc61f9dfe3a8b"></a>

### `k_lifo_put`

```c
#define k_lifo_put ( lifo, data )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
({ \
void *_data = data; \
SYS_PORT_TRACING_OBJ_FUNC_ENTER(k_lifo, put, lifo, _data); \
k_queue_prepend(&(lifo)->_queue, _data); \
SYS_PORT_TRACING_OBJ_FUNC_EXIT(k_lifo, put, lifo, _data); \
})
```

向LIFO队列加入一个元素。

此例程向lifo加入一个数据项。LIFO队列数据项必须满足指针的对齐要求，且其第一个指针大小的字段保留给内核使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lifo` | LIFO队列的地址。 |
| `data` | 数据项的地址。 |

> 译注——源码核对：通过k_queue_prepend把数据放到头部，get也从头部取出，构成后进先出顺序。已有等待者时仍直接交付；LIFO顺序描述缓存数据，不表示等待线程按后到先服务。

## 5.3\_源码定位与版本边界

> 译注——阅读与源码边界：配合[LIFO指南](../kernel/P015_LIFO后进先出队列.md)阅读。LIFO通过在内部队列头部插入并从头部获取实现，已有消费者等待时数据可直接交付。缓存顺序、等待者调度和应用对象生命周期是不同问题。

仓库相对定位：[kernel.h](../../../include/zephyr/kernel.h)、[kernel/queue.c](../../../kernel/queue.c)与[sys/sflist.h](../../../include/zephyr/sys/sflist.h)。本次依据为[官方内核头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/kernel.h)、[官方队列实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/kernel/queue.c)及[官方带标志链表](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/sflist.h)，摘要见[来源记录](../SOURCES.md)。

仓库源码、滚动更新的main和latest网页不能自动视为同一版本。本批完成文档与源码核对，未构建或执行队列并发、内存分配及实板实验。

## 5.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [k_lifo](P006_内核LIFO结构.md)
- [k_queue_alloc_prepend](P001_通用队列公共接口.md#gacf3dba40125073c11075e5a134919f88)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [k_queue_get](P001_通用队列公共接口.md#ga0a77d8556e7d253319275de034f01619)
- [K_OBJ_CORE](../object_core_reference/P001_对象核心公共接口.md#ga2bd0c2c121afc09448926a3648c7d814)

<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__queue__apis_html_gacf3dba40125073c11075e5a134919f88"></a>
<a id="astructk__lifo_html"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="agroup__queue__apis_html_ga0a77d8556e7d253319275de034f01619"></a>
<a id="agroup__obj__core__apis_html_ga2bd0c2c121afc09448926a3648c7d814"></a>

---

[上一章](P004_内核FIFO结构.md) · [返回大纲](大纲.md) · [下一章](P006_内核LIFO结构.md)
