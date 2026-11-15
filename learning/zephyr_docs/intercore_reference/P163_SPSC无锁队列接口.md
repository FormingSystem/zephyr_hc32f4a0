---
id: learning.zephyr-docs.intercore_reference.lockfreeref-163
title: SPSC无锁队列接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__spsc__lockfree.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第163章\_SPSC无锁队列接口

原文：[group__spsc__lockfree](https://docs.zephyrproject.org/latest/doxygen/html/group__spsc__lockfree.html)。读取日期：2026-10-13，`latest`。

本页介绍单生产者、单消费者（Single Producer, Single Consumer，SPSC）无锁队列（Lock-free Queue）的应用程序编程接口（Application Programming Interface，API）。它通过环形缓冲区（Ring Buffer）和原子操作（Atomic Operation）提供类型安全（Type-safe）的固定大小队列，容量为2的幂。头文件为`zephyr/sys/spsc_lockfree.h`。

生产者先取得（Acquire）元素，再发布（Produce）；消费者消费（Consume）元素后再释放（Release）。这几个动作名称保留英文，以便与宏名对应。运行约束与四种安全的执行上下文组合见[SPSC无锁队列头文件参考](P164_SPSC无锁队列头文件参考.md)。

下文保留原页宏展开顺序。原子初始化宏`ATOMIC_INIT`、原子读取／设置／加法函数`atomic_get()``atomic_set()``atomic_add()`以及构建断言（Build Assertion）宏`BUILD_ASSERT`保持原名；`IS_POWER_OF_TWO`检查2的幂。`z_spsc_in``z_spsc_out`读取队列索引，`z_spsc_mask`进行掩码回绕。它们的完整定义见[SPSC无锁队列完整头文件](P165_SPSC无锁队列完整头文件.md)。

以下重置限制中的 ISR 指中断服务程序（Interrupt Service Routine）。静态初始化器（Static Initializer）`SPSC_INITIALIZER`会在定义队列的宏展开中被调用，其自身定义在后面单独保留。

## 163.1\_查询可取得元素数量

`spsc_acquirable(spsc)`：返回队列中可取得（Acquirable）的元素数量。

```c
({ (((spsc)->_spsc.in + (spsc)->_spsc.acquire) - (spsc)->_spsc.out) - spsc_size(spsc); })
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要查询元素数量的 SPSC 队列 |

译注：原页称其为可取得数量，但所展示表达式按“已使用部分减队列大小”的顺序计算；这里保留原式，未改写为常见的“容量减已用量”。实际采用此宏前，应结合所用版本核对其数值语义。

## 163.2\_取得一个待生产元素

`spsc_acquire(spsc)`：从队列取得（Acquire）一个元素供生产者使用。

```c
({                                                                                         \
        unsigned long idx = z_spsc_in(spsc) + (spsc)->_spsc.acquire;                       \
        bool spsc_acq = (idx - z_spsc_out(spsc)) < spsc_size(spsc);                        \
        if (spsc_acq) {                                                                    \
                (spsc)->_spsc.acquire += 1;                                                \
        }                                                                                  \
        spsc_acq ? &((spsc)->buffer[z_spsc_mask(spsc, idx)]) : NULL;                       \
})
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要从中取得待生产元素的 SPSC 队列 |

返回所取得元素的指针；队列已满时返回`NULL`。

## 163.3\_查询可消费元素数量

`spsc_consumable(spsc)`：返回队列中可消费（Consumable）的元素数量。

```c
({ (spsc)->_spsc.in - (spsc)->_spsc.out - (spsc)->_spsc.consume; })
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要查询元素数量的 SPSC 队列 |

## 163.4\_消费一个元素

`spsc_consume(spsc)`：从队列消费（Consume）一个元素。

```c
({                                                                                         \
        unsigned long idx = z_spsc_out(spsc) + (spsc)->_spsc.consume;                      \
        bool has_consumable = (idx != z_spsc_in(spsc));                                    \
        if (has_consumable) {                                                              \
                (spsc)->_spsc.consume += 1;                                                \
        }                                                                                  \
        has_consumable ? &((spsc)->buffer[z_spsc_mask(spsc, idx)]) : NULL;                 \
})
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要从中消费元素的 SPSC 队列 |

返回元素指针；没有剩余可消费元素时返回`NULL`。

## 163.5\_声明队列结构类型

`SPSC_DECLARE(name, type)`：原文表述为：为 SPSC 声明匿名结构类型（Anonymous Structure Type）。

```c
struct spsc_##name {                                                                       \
        struct spsc _spsc;                                                                 \
        type * const buffer;                                                               \
}
```

| 参数 | 含义 |
| --- | --- |
| `name` | 要提供的 SPSC 符号名称 |
| `type` | SPSC 队列存储的数据类型 |

译注：原文称“匿名”，但展开代码实际带有通过`spsc_##name`拼接的结构标签（Structure Tag）；保留原说明并指出这一差异。

## 163.6\_定义固定容量队列

`SPSC_DEFINE(name, type, sz)`：定义固定大小的 SPSC 队列。

```c
BUILD_ASSERT(IS_POWER_OF_TWO(sz));                                                         \
static type __spsc_buf_##name[sz];                                                         \
SPSC_DECLARE(name, type) name = SPSC_INITIALIZER(sz, __spsc_buf_##name);
```

| 参数 | 含义 |
| --- | --- |
| `name` | 要提供的 SPSC 符号名称 |
| `type` | SPSC 队列存储的数据类型 |
| `sz` | 队列大小，必须是2的幂，例如2、4、8 |

## 163.7\_放弃全部已取得元素

`spsc_drop_all(spsc)`：放弃（Drop）先前取得的全部元素，使这些元素可再次被取得。

```c
do {                                                                                       \
        (spsc)->_spsc.acquire = 0;                                                         \
} while (false)
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要放弃全部已取得元素的 SPSC 队列；没有相应元素时不执行操作 |

## 163.8\_静态初始化队列

`SPSC_INITIALIZER(sz, buf)`：静态初始化 SPSC 队列。

```c
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
```

| 参数 | 含义 |
| --- | --- |
| `sz` | 队列大小，必须是2的幂，例如2、4、8 |
| `buf` | 缓冲区指针 |

## 163.9\_查看下一个元素

`spsc_next(spsc, item)`：从给定元素开始，查看（Peek）队列中的下一个元素。

```c
({                                                                                         \
        unsigned long idx = ((item) - (spsc)->buffer);                                     \
        bool has_next =                                                                    \
                z_spsc_mask(spsc, (idx + 1)) != (z_spsc_mask(spsc, z_spsc_in(spsc)));      \
        has_next ? &((spsc)->buffer[z_spsc_mask((spsc), idx + 1)]) : NULL;                 \
})
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要查看的 SPSC 队列 |
| `item` | 指向队列中某个元素的指针 |

返回元素指针；没有剩余元素时返回`NULL`。

## 163.10\_查看第一个可用元素

`spsc_peek(spsc)`：查看队列中的第一个可用元素。

```c
({                                                                                         \
        unsigned long idx = z_spsc_out(spsc) + (spsc)->_spsc.consume;                      \
        bool has_consumable = (idx != z_spsc_in(spsc));                                    \
        has_consumable ? &((spsc)->buffer[z_spsc_mask(spsc, idx)]) : NULL;                 \
})
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要查看的 SPSC 队列 |

返回元素指针；没有剩余可消费元素时返回`NULL`。

## 163.11\_查看前一个元素

`spsc_prev(spsc, item)`：取得队列中给定元素之前的元素。

```c
({                                                                                         \
        unsigned long idx = ((item) - &(spsc)->buffer[0]) / sizeof((spsc)->buffer[0]);     \
        bool has_prev = idx != z_spsc_mask(spsc, z_spsc_out(spsc));                        \
        has_prev ? &((spsc)->buffer[z_spsc_mask(spsc, idx - 1)]) : NULL;                   \
})
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要查看的 SPSC 队列 |
| `item` | 指向队列中某个元素的指针 |

返回元素指针；没有剩余元素时返回`NULL`。

译注：原展开式在带类型指针相减后又除以`sizeof((spsc)->buffer[0])`。C 指针相减本身以元素为单位，这一原始表达式值得在所用版本中核对；本译文未修改该代码。

## 163.12\_发布一个已取得元素

`spsc_produce(spsc)`：向队列生产／发布（Produce）一个先前取得的元素，使一个元素立即对消费者可用。

```c
({                                                                                         \
        if ((spsc)->_spsc.acquire > 0) {                                                   \
                (spsc)->_spsc.acquire -= 1;                                                \
                atomic_add(&(spsc)->_spsc.in, 1);                                          \
        }                                                                                  \
})
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要发布先前取得元素的 SPSC 队列；没有相应元素时不执行操作 |

## 163.13\_发布全部已取得元素

`spsc_produce_all(spsc)`：向队列发布先前取得的全部元素，使它们立即对消费者可用。

```c
({                                                                                         \
        if ((spsc)->_spsc.acquire > 0) {                                                   \
                unsigned long acquired = (spsc)->_spsc.acquire;                            \
                (spsc)->_spsc.acquire = 0;                                                 \
                atomic_add(&(spsc)->_spsc.in, acquired);                                   \
        }                                                                                  \
})
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要发布先前取得的全部元素的 SPSC 队列；没有相应元素时不执行操作 |

## 163.14\_释放一个已消费元素

`spsc_release(spsc)`：释放（Release）一个已消费元素。

```c
({                                                                                         \
        if ((spsc)->_spsc.consume > 0) {                                                   \
                (spsc)->_spsc.consume -= 1;                                                \
                atomic_add(&(spsc)->_spsc.out, 1);                                         \
        }                                                                                  \
})
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要释放已消费元素的 SPSC 队列；没有相应元素时不执行操作 |

## 163.15\_释放全部已消费元素

`spsc_release_all(spsc)`：释放全部已消费元素。

```c
({                                                                                         \
        if ((spsc)->_spsc.consume > 0) {                                                   \
                unsigned long consumed = (spsc)->_spsc.consume;                            \
                (spsc)->_spsc.consume = 0;                                                 \
                atomic_add(&(spsc)->_spsc.out, consumed);                                  \
        }                                                                                  \
})
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要释放已消费元素的 SPSC 队列；没有相应元素时不执行操作 |

## 163.16\_初始化或重置为空队列

`spsc_reset(spsc)`：初始化／重置（Reset）队列，使其为空。**多个调用上下文（ISR／线程）正在以生产者／消费者方式使用队列时，执行重置并不安全。**

```c
({                                                                                         \
        (spsc)->_spsc.consume = 0;                                                         \
        (spsc)->_spsc.acquire = 0;                                                         \
        atomic_set(&(spsc)->_spsc.in, 0);                                                  \
        atomic_set(&(spsc)->_spsc.out, 0);                                                 \
})
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | 要初始化或重置的 SPSC 队列 |

## 163.17\_查询队列大小

`spsc_size(spsc)`：取得 SPSC 队列大小。

```c
((spsc)->_spsc.mask + 1)
```

| 参数 | 含义 |
| --- | --- |
| `spsc` | SPSC 队列引用 |

---

[上一章：MPSC无锁队列完整头文件](P162_MPSC无锁队列完整头文件.md) · [下一章：SPSC无锁队列头文件参考](P164_SPSC无锁队列头文件参考.md) · [返回大纲](大纲.md)
