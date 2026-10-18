---
id: learning.zephyr-docs.intercore_reference.lockfreeref-165
title: SPSC无锁队列完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/spsc__lockfree_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第165章\_SPSC无锁队列完整头文件

原文：[spsc__lockfree_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/spsc__lockfree_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留`zephyr/sys/spsc_lockfree.h`完整官方可见源码（Source Code），仅去除网页行号及行尾空白。SPSC 为单生产者、单消费者（Single Producer, Single Consumer）。版权为2023年的 Intel Corporation，许可证为`Apache-2.0`，原声明完整保留。

本文件通过原子操作（Atomic Operation）协调队列索引，使用位掩码（Bit Mask）实现回绕（Wrap）。生产者先取得（Acquire）再发布（Produce），消费者先消费（Consume）再释放（Release）；公共宏说明见[SPSC无锁队列接口](P163_SPSC无锁队列接口.md)。

`SPSC_INITIALIZER`为静态初始化器（Static Initializer），`SPSC_DECLARE`声明结构类型，`SPSC_DEFINE`定义队列。`ATOMIC_INIT`初始化原子值；`BUILD_ASSERT`是构建断言（Build Assertion）宏，`IS_POWER_OF_TWO`检查2的幂。后文的 ISR 指中断服务程序（Interrupt Service Routine）。

## 165.1\_完整源码

```c
/*
 * Copyright (c) 2023 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SYS_SPSC_LOCKFREE_H_
#define ZEPHYR_INCLUDE_SYS_SPSC_LOCKFREE_H_

#include <stdint.h>
#include <stdbool.h>
#include <zephyr/toolchain/common.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/util_macro.h>



struct spsc {
        /* private value only the producer thread should mutate */
        unsigned long acquire;

        /* private value only the consumer thread should mutate */
        unsigned long consume;

        /* producer mutable, consumer readable */
        atomic_t in;

        /* consumer mutable, producer readable */
        atomic_t out;

        /* mask used to automatically wrap values */
        const unsigned long mask;
};

#define SPSC_INITIALIZER(sz, buf)                                                                  \
        {                                                                                          \
                ._spsc =                                                                           \
                        {                                                                          \
                                .acquire = 0,                                                      \
                                .consume = 0,                                                      \
                                .in = ATOMIC_INIT(0),                                              \
                                .out = ATOMIC_INIT(0),                                             \
                                .mask = sz - 1,                                                    \
                        },                                                                         \
                .buffer = buf,                                                                     \
        }

#define SPSC_DECLARE(name, type)                                                                   \
        struct spsc_##name {                                                                       \
                struct spsc _spsc;                                                                 \
                type * const buffer;                                                               \
        }

#define SPSC_DEFINE(name, type, sz)                                                                \
        BUILD_ASSERT(IS_POWER_OF_TWO(sz));                                                         \
        static type __spsc_buf_##name[sz];                                                         \
        SPSC_DECLARE(name, type) name = SPSC_INITIALIZER(sz, __spsc_buf_##name);

#define spsc_size(spsc) ((spsc)->_spsc.mask + 1)

#define z_spsc_mask(spsc, i) ((i) & (spsc)->_spsc.mask)

#define z_spsc_in(spsc) (unsigned long)atomic_get(&(spsc)->_spsc.in)

#define z_spsc_out(spsc) (unsigned long)atomic_get(&(spsc)->_spsc.out)

#define spsc_reset(spsc)                                                                           \
        ({                                                                                         \
                (spsc)->_spsc.consume = 0;                                                         \
                (spsc)->_spsc.acquire = 0;                                                         \
                atomic_set(&(spsc)->_spsc.in, 0);                                                  \
                atomic_set(&(spsc)->_spsc.out, 0);                                                 \
        })

#define spsc_acquire(spsc)                                                                         \
        ({                                                                                         \
                unsigned long idx = z_spsc_in(spsc) + (spsc)->_spsc.acquire;                       \
                bool spsc_acq = (idx - z_spsc_out(spsc)) < spsc_size(spsc);                        \
                if (spsc_acq) {                                                                    \
                        (spsc)->_spsc.acquire += 1;                                                \
                }                                                                                  \
                spsc_acq ? &((spsc)->buffer[z_spsc_mask(spsc, idx)]) : NULL;                       \
        })

#define spsc_produce(spsc)                                                                         \
        ({                                                                                         \
                if ((spsc)->_spsc.acquire > 0) {                                                   \
                        (spsc)->_spsc.acquire -= 1;                                                \
                        atomic_add(&(spsc)->_spsc.in, 1);                                          \
                }                                                                                  \
        })

#define spsc_produce_all(spsc)                                                                     \
        ({                                                                                         \
                if ((spsc)->_spsc.acquire > 0) {                                                   \
                        unsigned long acquired = (spsc)->_spsc.acquire;                            \
                        (spsc)->_spsc.acquire = 0;                                                 \
                        atomic_add(&(spsc)->_spsc.in, acquired);                                   \
                }                                                                                  \
        })

#define spsc_drop_all(spsc)                                                                        \
        do {                                                                                       \
                (spsc)->_spsc.acquire = 0;                                                         \
        } while (false)

#define spsc_consume(spsc)                                                                         \
        ({                                                                                         \
                unsigned long idx = z_spsc_out(spsc) + (spsc)->_spsc.consume;                      \
                bool has_consumable = (idx != z_spsc_in(spsc));                                    \
                if (has_consumable) {                                                              \
                        (spsc)->_spsc.consume += 1;                                                \
                }                                                                                  \
                has_consumable ? &((spsc)->buffer[z_spsc_mask(spsc, idx)]) : NULL;                 \
        })

#define spsc_release(spsc)                                                                         \
        ({                                                                                         \
                if ((spsc)->_spsc.consume > 0) {                                                   \
                        (spsc)->_spsc.consume -= 1;                                                \
                        atomic_add(&(spsc)->_spsc.out, 1);                                         \
                }                                                                                  \
        })

#define spsc_release_all(spsc)                                                                     \
        ({                                                                                         \
                if ((spsc)->_spsc.consume > 0) {                                                   \
                        unsigned long consumed = (spsc)->_spsc.consume;                            \
                        (spsc)->_spsc.consume = 0;                                                 \
                        atomic_add(&(spsc)->_spsc.out, consumed);                                  \
                }                                                                                  \
        })

#define spsc_acquirable(spsc)                                                                      \
        ({ (((spsc)->_spsc.in + (spsc)->_spsc.acquire) - (spsc)->_spsc.out) - spsc_size(spsc); })

#define spsc_consumable(spsc) ({ (spsc)->_spsc.in - (spsc)->_spsc.out - (spsc)->_spsc.consume; })

#define spsc_peek(spsc)                                                                            \
        ({                                                                                         \
                unsigned long idx = z_spsc_out(spsc) + (spsc)->_spsc.consume;                      \
                bool has_consumable = (idx != z_spsc_in(spsc));                                    \
                has_consumable ? &((spsc)->buffer[z_spsc_mask(spsc, idx)]) : NULL;                 \
        })

#define spsc_next(spsc, item)                                                                      \
        ({                                                                                         \
                unsigned long idx = ((item) - (spsc)->buffer);                                     \
                bool has_next =                                                                    \
                        z_spsc_mask(spsc, (idx + 1)) != (z_spsc_mask(spsc, z_spsc_in(spsc)));      \
                has_next ? &((spsc)->buffer[z_spsc_mask((spsc), idx + 1)]) : NULL;                 \
        })

#define spsc_prev(spsc, item)                                                                      \
        ({                                                                                         \
                unsigned long idx = ((item) - &(spsc)->buffer[0]) / sizeof((spsc)->buffer[0]);     \
                bool has_prev = idx != z_spsc_mask(spsc, z_spsc_out(spsc));                        \
                has_prev ? &((spsc)->buffer[z_spsc_mask(spsc, idx - 1)]) : NULL;                   \
        })


#endif /* ZEPHYR_INCLUDE_SYS_SPSC_LOCKFREE_H_ */
```

## 165.2\_结构可见注释译文

原始`struct spsc`有五个成员：

| 成员声明 | 原注释含义 |
| --- | --- |
| `unsigned long acquire` | 私有值（Private Value），只能由生产者线程（Producer Thread）修改 |
| `unsigned long consume` | 私有值，只能由消费者线程（Consumer Thread）修改 |
| `atomic_t in` | 生产者可修改，消费者可读取 |
| `atomic_t out` | 消费者可修改，生产者可读取 |
| `const unsigned long mask` | 用于让数值自动回绕的掩码（Mask） |

这些注释中的“线程”用词按源码保留；头文件参考另列出 ISR 与线程的安全使用组合，见[SPSC无锁队列头文件参考](P164_SPSC无锁队列头文件参考.md)。

## 165.3\_阅读说明

`ATOMIC_INIT`初始化原子值，`atomic_get()``atomic_set()``atomic_add()`分别读取、设置、相加。`BUILD_ASSERT`是构建断言（Build Assertion）宏，`IS_POWER_OF_TWO`检查大小为2的幂。内部宏`z_spsc_mask`按掩码回绕，`z_spsc_in`和`z_spsc_out`取得原子索引。

所有17个公共宏和3个内部辅助宏均按原文件保留。`spsc_acquirable`与`spsc_prev`中的原表达式没有改写，相关数值与指针运算疑点见接口页译注。文件末尾注释标记头文件保护宏`ZEPHYR_INCLUDE_SYS_SPSC_LOCKFREE_H_`结束。网页未显示的文档注释不补造到源码中。

---

[上一章：SPSC无锁队列头文件参考](P164_SPSC无锁队列头文件参考.md) · [下一章：MPSC数据包缓冲区接口](P166_MPSC数据包缓冲区接口.md) · [返回大纲](大纲.md)
