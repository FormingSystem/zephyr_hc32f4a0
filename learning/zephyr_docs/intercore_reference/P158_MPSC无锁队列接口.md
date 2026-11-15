---
id: learning.zephyr-docs.intercore_reference.lockfreeref-158
title: MPSC无锁队列接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpsc__lockfree.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第158章\_MPSC无锁队列接口

原文：[group__mpsc__lockfree](https://docs.zephyrproject.org/latest/doxygen/html/group__mpsc__lockfree.html)。读取日期：2026-10-13，`latest`。

本页介绍多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）无锁队列（Lock-free Queue）的应用程序编程接口（Application Programming Interface，API），头文件为`zephyr/sys/mpsc_lockfree.h`。

原文件摘要将其描述为使用单向链表（Singly Linked List）的无等待（Wait-free）侵入式（Intrusive）队列。完整并发限制见[MPSC无锁队列头文件参考](P161_MPSC无锁队列头文件参考.md)，数据结构见[MPSC无锁队列结构](P159_MPSC无锁队列结构.md)和[MPSC无锁队列节点](P160_MPSC无锁队列节点.md)。

## 158.1\_静态初始化

`MPSC_INIT(symbol)`为 MPSC 队列提供静态初始化器（Static Initializer）。

```c
{                                                                                          \
        .head = (struct mpsc_node *)&symbol.stub,                                          \
        .tail = (struct mpsc_node *)&symbol.stub,                                          \
        .stub = {                                                                          \
                .next = NULL,                                                              \
        },                                                                                 \
}
```

| 参数 | 含义 |
| --- | --- |
| `symbol` | 队列名称 |

译注：原页在摘要后只有未写完的“Since the queue is”（由于该队列……），没有后续内容；这里不猜测缺失原因或补写条件。

## 158.2\_读取指针

`mpsc_ptr_get(ptr)`在本参考页所展示的配置下展开为：

```c
atomic_ptr_get(&(ptr))
```

## 158.3\_设置指针

`mpsc_ptr_set(ptr, val)`在本参考页所展示的配置下展开为：

```c
atomic_ptr_set(&(ptr), val)
```

## 158.4\_交换指针

`mpsc_ptr_set_get(ptr, val)`在本参考页所展示的配置下展开为：

```c
atomic_ptr_set(&(ptr), val)
```

上述三项宏原页没有额外的参数表。阅读说明：`ptr`是被访问的指针变量，`val`是要写入的值。`atomic_ptr_get()`执行原子读取（Atomic Read）；`atomic_ptr_set()`执行原子取旧值并设置新值（Atomic Get-and-set）。

## 158.5\_指针类型

```c
typedef atomic_ptr_t mpsc_ptr_t;
```

原参考页展示原子指针类型（Atomic Pointer Type）`atomic_ptr_t`的别名`mpsc_ptr_t`。完整源码在启用对称多处理（Symmetric Multiprocessing，SMP）的`CONFIG_SMP`构建配置时使用此定义；其他情况下使用`struct mpsc_node *`，三个指针宏也采用相应的直接访问实现。Kconfig 是 Zephyr 的构建配置系统（Build Configuration System），`CONFIG_`前缀为其配置宏形式。

## 158.6\_初始化或重置队列

```c
static inline void mpsc_init(struct mpsc *q);
```

初始化队列。

| 参数 | 含义 |
| --- | --- |
| `q` | 要初始化或重置的队列 |

<a id="ga823ec37b84ac43e46167aac954bce9d7"></a>

## 158.7\_弹出节点

```c
static inline struct mpsc_node *mpsc_pop(struct mpsc *q);
```

从链表中弹出一个节点（Node）。原页没有单独列出参数表；从签名可知`q`为被操作的队列指针。

| 返回值 | 含义 |
| --- | --- |
| `NULL` | 没有可用节点 |
| `node` | 存在可用节点时返回该节点 |

阅读说明：源码注释还区分了“队列存在待完成更新、暂时无法访问”的情况；这里的`NULL`不能扩大解释为所有生产者都已停止且队列永久为空。

<a id="ga403add133841ef88e10d74141e782b37"></a>

## 158.8\_压入节点

```c
static ALWAYS_INLINE void mpsc_push(struct mpsc *q, struct mpsc_node *n);
```

向队列压入一个节点。`ALWAYS_INLINE`是要求内联（Inline）的工具链宏，其原标记保留。

| 参数 | 含义 |
| --- | --- |
| `q` | 要向其中压入节点的队列 |
| `n` | 要压入队列的节点 |

---

[上一章：SPSC数据包缓冲区标志](P157_SPSC数据包缓冲区标志.md) · [下一章：MPSC无锁队列结构](P159_MPSC无锁队列结构.md) · [返回大纲](大纲.md)
