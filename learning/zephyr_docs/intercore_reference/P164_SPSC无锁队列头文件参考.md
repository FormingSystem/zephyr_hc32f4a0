---
id: learning.zephyr-docs.intercore_reference.lockfreeref-164
title: SPSC无锁队列头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/spsc__lockfree_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第164章\_SPSC无锁队列头文件参考

原文：[spsc__lockfree_8h](https://docs.zephyrproject.org/latest/doxygen/html/spsc__lockfree_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/sys/spsc_lockfree.h`提供无锁（Lock-free）、类型安全（Type-safe）的单生产者、单消费者（Single Producer, Single Consumer，SPSC）队列。它使用固定大小、容量为2的幂的环形缓冲区（Ring Buffer），并用原子操作（Atomic Operation）保证一致性（Coherency）。

实现基于数组，以2的幂大小进行回绕（Wrap），使用位掩码（Bit Mask）完成取模（Modulo）。原子操作使单生产者、单消费者无需锁也能安全交互。元素预期具有固定大小。底层缓冲区有明确类型，所有操作通过宏（Macro）完成，因此应用程序编程接口（Application Programming Interface，API）具有类型安全性。

队列可以声明在栈（Stack）上，也可以静态声明；只要其生命周期（Lifetime）覆盖所有使用过程，就能正常工作。原文建议优先采用静态声明。它用于两个执行上下文（Execution Context）之间共享，例如一个中断服务程序（Interrupt Service Routine，ISR）与一个线程（Thread）。

译注：原句“Static declarations should be the preferred method as stack .”在“as stack”之后缺少解释，这里保留明确的优先静态声明建议，不补写缺失原因。

在 ISR 中生产或消费是安全的，推入／取出（Push/Pull）的时间复杂度为`O(1)`。

**警告：不能由多个执行上下文共同承担生产者角色，也不能由多个执行上下文共同承担消费者角色。** 当 A、B 各自为唯一执行上下文时，下列组合是安全用法：

| 生产者 A | 消费者 B |
| --- | --- |
| ISR A | 线程 B |
| 线程 A | ISR B |
| 线程 A | 线程 B |
| ISR A | ISR B |

## 164.1\_依赖头文件

```c
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/toolchain/common.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/util_macro.h>
```

## 164.2\_全部宏接口

| 宏签名 | 作用 |
| --- | --- |
| `SPSC_INITIALIZER(sz, buf)` | 静态初始化队列 |
| `SPSC_DECLARE(name, type)` | 声明队列结构类型 |
| `SPSC_DEFINE(name, type, sz)` | 定义固定容量队列 |
| `spsc_size(spsc)` | 查询队列大小 |
| `spsc_reset(spsc)` | 初始化或重置为空队列 |
| `spsc_acquire(spsc)` | 取得一个待生产元素 |
| `spsc_produce(spsc)` | 发布一个已取得元素 |
| `spsc_produce_all(spsc)` | 发布全部已取得元素 |
| `spsc_drop_all(spsc)` | 放弃全部已取得元素 |
| `spsc_consume(spsc)` | 消费一个元素 |
| `spsc_release(spsc)` | 释放一个已消费元素 |
| `spsc_release_all(spsc)` | 释放全部已消费元素 |
| `spsc_acquirable(spsc)` | 查询可取得元素数量 |
| `spsc_consumable(spsc)` | 查询可消费元素数量 |
| `spsc_peek(spsc)` | 查看第一个可用元素 |
| `spsc_next(spsc, item)` | 查看下一个元素 |
| `spsc_prev(spsc, item)` | 查看前一个元素 |

原页共列出17个宏，完整展开、参数和返回值见[SPSC无锁队列接口](P163_SPSC无锁队列接口.md)；完整源码见[SPSC无锁队列完整头文件](P165_SPSC无锁队列完整头文件.md)。

---

[上一章：SPSC无锁队列接口](P163_SPSC无锁队列接口.md) · [下一章：SPSC无锁队列完整头文件](P165_SPSC无锁队列完整头文件.md) · [返回大纲](大纲.md)
