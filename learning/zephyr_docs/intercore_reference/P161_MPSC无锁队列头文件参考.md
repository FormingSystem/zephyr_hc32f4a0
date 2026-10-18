---
id: learning.zephyr-docs.intercore_reference.lockfreeref-161
title: MPSC无锁队列头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpsc__lockfree_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第161章\_MPSC无锁队列头文件参考

原文：[mpsc__lockfree_8h](https://docs.zephyrproject.org/latest/doxygen/html/mpsc__lockfree_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/sys/mpsc_lockfree.h`提供基于单向链表（Singly Linked List）的侵入式（Intrusive）多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）队列。它具有无等待（Wait-free）性质，元素按先进先出（First In, First Out，FIFO）顺序排列。

实现基于 Dmitry Vyukov 提出的、广为使用的无等待 MPSC 队列，并针对实时操作系统（Real-Time Operating System，RTOS）在多种体系结构上的需求做了少量调整。原文指出，生产者和消费者均无等待，不需要比较并交换（Compare-and-Swap，CAS）循环或锁（Lock）。

入队（Push）与出队（Pop）的时间复杂度为`O(1)`，可以安全地在中断服务程序（Interrupt Service Routine，ISR）中生产或消费。

**警告：不能在多个执行上下文（Execution Context）中消费同一 MPSC 队列。** 多生产者并不意味着多消费者。

译注：上文保留原参考页对无等待与锁的表述；完整源码的`mpsc_push()`仍包含`arch_irq_lock()`和`arch_irq_unlock()`中断控制调用，不能将“不需要锁”理解为没有中断控制。阅读说明：侵入式表示节点链接嵌入被排队对象；无锁（Lock-free）与无等待是相关但不同的并发进展性质，本文保留原页各处具体用词。

## 161.1\_依赖头文件

```c
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/kernel.h>
```

## 161.2\_结构与类型

[MPSC无锁队列结构](P159_MPSC无锁队列结构.md)是队列结构，[MPSC无锁队列节点](P160_MPSC无锁队列节点.md)是队列成员。

```c
typedef atomic_ptr_t mpsc_ptr_t;
```

上方为原页展示的指针类型别名（Type Alias）；完整源码保留其他构建配置分支。

## 161.3\_宏参考

| 参数 | 含义 |
| --- | --- |
| `mpsc_ptr_get(ptr)` | 读取指针 |
| `mpsc_ptr_set(ptr, val)` | 设置指针 |
| `mpsc_ptr_set_get(ptr, val)` | 设置指针并取得旧值 |
| `MPSC_INIT(symbol)` | 队列静态初始化器（Static Initializer） |

`ALWAYS_INLINE`是工具链要求内联（Inline）的宏，以下保留原函数声明中的标记。

## 161.4\_函数参考


```c
static inline void mpsc_init(struct mpsc *q);
```

初始化队列。


```c
static ALWAYS_INLINE void mpsc_push(struct mpsc *q, struct mpsc_node *n);
```

压入节点。


```c
static inline struct mpsc_node *mpsc_pop(struct mpsc *q);
```

从链表弹出节点。

完整参数及返回值见[MPSC无锁队列接口](P158_MPSC无锁队列接口.md)；官方可见源码见[MPSC无锁队列完整头文件](P162_MPSC无锁队列完整头文件.md)。

---

[上一章：MPSC无锁队列节点](P160_MPSC无锁队列节点.md) · [下一章：MPSC无锁队列完整头文件](P162_MPSC无锁队列完整头文件.md) · [返回大纲](大纲.md)
