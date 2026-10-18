---
id: learning.zephyr-docs.intercore_reference.lockfreeref-162
title: MPSC无锁队列完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpsc__lockfree_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第162章\_MPSC无锁队列完整头文件

原文：[mpsc__lockfree_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/mpsc__lockfree_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留`zephyr/sys/mpsc_lockfree.h`完整官方可见源码（Source Code），仅去除网页行号及行尾空白。MPSC 指多生产者、单消费者（Multiple Producer, Single Consumer）。版权声明包括2010—2011年的 Dmitry Vyukov 和2023年的 Intel Corporation，许可证为`Apache-2.0`。

阅读说明：SMP 指对称多处理（Symmetric Multiprocessing），`CONFIG_SMP`是 Kconfig 构建配置系统（Build Configuration System）的配置宏。原子操作（Atomic Operation）用于跨核访问；指针宏和接口的解释见[MPSC无锁队列接口](P158_MPSC无锁队列接口.md)。

`MPSC_INIT`为队列静态初始化器（Static Initializer）宏，`ALWAYS_INLINE`为要求内联（Inline）的工具链宏；源码注释的`HEAD`指队列头（Head）。

## 162.1\_完整源码

```c
/*
 * Copyright (c) 2010-2011 Dmitry Vyukov
 * Copyright (c) 2023 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SYS_MPSC_LOCKFREE_H_
#define ZEPHYR_INCLUDE_SYS_MPSC_LOCKFREE_H_

#include <stdint.h>
#include <stdbool.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif



/*
 * On single core systems atomics are unnecessary
 * and cause a lot of unnecessary cache invalidation
 *
 * Using volatile to at least ensure memory is read/written
 * by the compiler generated op codes is enough.
 *
 * On SMP atomics *must* be used to ensure the pointers
 * are updated in the correct order.
 */
#if defined(CONFIG_SMP)

typedef atomic_ptr_t mpsc_ptr_t;

#define mpsc_ptr_get(ptr)          atomic_ptr_get(&(ptr))
#define mpsc_ptr_set(ptr, val)     atomic_ptr_set(&(ptr), val)
#define mpsc_ptr_set_get(ptr, val) atomic_ptr_set(&(ptr), val)

#else /* defined(CONFIG_SMP) */

typedef struct mpsc_node *mpsc_ptr_t;

#define mpsc_ptr_get(ptr)      ptr
#define mpsc_ptr_set(ptr, val) ptr = val
#define mpsc_ptr_set_get(ptr, val)                                                                 \
        ({                                                                                         \
                mpsc_ptr_t tmp = ptr;                                                              \
                ptr = val;                                                                         \
                tmp;                                                                               \
        })

#endif /* defined(CONFIG_SMP) */

struct mpsc_node {
        mpsc_ptr_t next;
};

struct mpsc {
        mpsc_ptr_t head;
        struct mpsc_node *tail;
        struct mpsc_node stub;
};

#define MPSC_INIT(symbol)                                                                          \
        {                                                                                          \
                .head = (struct mpsc_node *)&symbol.stub,                                          \
                .tail = (struct mpsc_node *)&symbol.stub,                                          \
                .stub = {                                                                          \
                        .next = NULL,                                                              \
                },                                                                                 \
        }

static inline void mpsc_init(struct mpsc *q)
{
        mpsc_ptr_set(q->head, &q->stub);
        q->tail = &q->stub;
        mpsc_ptr_set(q->stub.next, NULL);
}

static ALWAYS_INLINE void mpsc_push(struct mpsc *q, struct mpsc_node *n)
{
        struct mpsc_node *prev;
        int key;

        mpsc_ptr_set(n->next, NULL);

        key = arch_irq_lock();
        prev = (struct mpsc_node *)mpsc_ptr_set_get(q->head, n);
        mpsc_ptr_set(prev->next, n);
        arch_irq_unlock(key);
}

static inline struct mpsc_node *mpsc_pop(struct mpsc *q)
{
        struct mpsc_node *head;
        struct mpsc_node *tail = q->tail;
        struct mpsc_node *next = (struct mpsc_node *)mpsc_ptr_get(tail->next);

        /* Skip over the stub/sentinel */
        if (tail == &q->stub) {
                if (next == NULL) {
                        return NULL;
                }

                q->tail = next;
                tail = next;
                next = (struct mpsc_node *)mpsc_ptr_get(next->next);
        }

        /* If next is non-NULL then a valid node is found, return it */
        if (next != NULL) {
                q->tail = next;
                return tail;
        }

        head = (struct mpsc_node *)mpsc_ptr_get(q->head);

        /* If next is NULL, and the tail != HEAD then the queue has pending
         * updates that can't yet be accessed.
         */
        if (tail != head) {
                return NULL;
        }

        mpsc_push(q, &q->stub);

        next = (struct mpsc_node *)mpsc_ptr_get(tail->next);

        if (next != NULL) {
                q->tail = next;
                return tail;
        }

        return NULL;
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SYS_MPSC_LOCKFREE_H_ */
```

## 162.2\_可见注释译文

条件编译前的原注释说明：在单核系统上，原子操作没有必要，并会造成许多不必要的缓存失效（Cache Invalidation）；使用`volatile`至少保证编译器生成的指令码进行内存读写就足够了。在 SMP 系统上，**必须使用原子操作，才能保证指针按正确顺序更新**。

译注：上一段忠实翻译该文件的注释。所展示的非 SMP 类型别名和访问宏没有显式加入`volatile`，因此不能把注释改写成“代码已使用 volatile”；也不能把此处特定实现的说明当成任意并发程序都可用`volatile`替代原子操作的规则。

`mpsc_pop()`中的三处可见注释依次表示：

1. 跳过占位／哨兵节点（Stub/Sentinel）。
2. 如果`next`不是`NULL`，就找到了有效节点，返回它。
3. 如果`next`为`NULL`且`tail != head`，队列存在尚未完成、暂时无法访问的更新。

`__cplusplus`分支提供 C++ 的 C 语言链接约定；`#else`和`#endif`注释指明`CONFIG_SMP`分支边界。末尾注释标记头文件保护宏`ZEPHYR_INCLUDE_SYS_MPSC_LOCKFREE_H_`结束。公开接口文档注释在此网页源码中被折叠，其对应译文见接口页。

---

[上一章：MPSC无锁队列头文件参考](P161_MPSC无锁队列头文件参考.md) · [下一章：SPSC无锁队列接口](P163_SPSC无锁队列接口.md) · [返回大纲](大纲.md)
