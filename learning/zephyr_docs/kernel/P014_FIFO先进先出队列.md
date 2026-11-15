---
id: learning.zephyr-docs.kernel.fifos
title: FIFO先进先出队列
kind: reference
status: maintained
domains: [zephyr, kernel, data-passing]
source_url: https://docs.zephyrproject.org/latest/kernel/services/data_passing/fifos.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第14章\_FIFO先进先出队列

原文：[FIFOs](https://docs.zephyrproject.org/latest/kernel/services/data_passing/fifos.html)。读取日期：2026-10-12，`latest`。

**先进先出（First In, First Out，FIFO）** 是实现先进先出（First In, First Out）队列的内核对象，允许线程和**中断服务例程（Interrupt Service Routine，ISR）**加入、取出任意大小的数据项。

## 14.1\_概念与数据项内存

FIFO 数量仅受可用内存等资源限制，每个对象通过内存地址引用。它的核心属性是一个保存“已经加入但尚未取出”数据项的队列，内部用简单链表实现。使用前必须初始化，使队列为空。

普通 FIFO 数据项必须满足指针对齐要求，因为内核会保留数据项最前面的一个指针大小字段，作为指向下一项的链接。因此，保存 N 字节应用数据，需要额外 4 或 8 字节链接空间，取决于指针宽度。

若改用 `k_fifo_alloc_put()` 入队，数据项无须满足上述对齐与预留字段要求；内核会从调用线程资源池临时分配额外链接内存。

同一个数据项在所有 FIFO 队列中最多只能有一个有效入队实例。此前入队尚未取出，就再次把它加入当前或其他 FIFO，会导致未定义行为。

## 14.2\_交付与等待规则

线程或 ISR 都能加入数据项。如果已有线程等待，数据直接交给等待者；否则放入 FIFO 链表。队列本身不规定最大项数。

线程可取出数据项。队列为空时，可以选择等待；多个线程可同时等待空队列。加入新项后，优先交给优先级最高者，同优先级时交给等待最久者。ISR 也能取数据，但队列为空时不得等待。

还可以把多个数据项预先组成单向链表，一次加入 FIFO。多个写入者提交相关数据集合时，这能确保每组内部不被其他写入项穿插，也比逐项加入更高效。原文指出，取到组内第一项者随后应能不等待地取到其余项。

> 译注：最后一句描述批量入队保证整组已经可用；若多个消费者并发取数，其他消费者仍可能先取走后续项。批量提交本身不赋予某个消费者独占消费整组的权利，应用若需要整组归属，仍须另外设计同步或消息封装。

## 14.3\_定义FIFO

使用 `struct k_fifo` 定义对象，再调用 `k_fifo_init()` 初始化空队列：

```c
struct k_fifo my_fifo;

k_fifo_init(&my_fifo);
```

也可以用宏 `K_FIFO_DEFINE` 在编译时定义并初始化，效果相同：

```c
K_FIFO_DEFINE(my_fifo);
```

## 14.4\_写入FIFO

通过 `k_fifo_put()` 加入数据项。下面沿用前例，把生产者的数据交给一个或多个消费者线程；结构体首字段保留给 FIFO 使用：

```c
struct data_item_t {
    void *fifo_reserved;   /* 1st word reserved for use by FIFO */
    ...
};

struct data_item_t tx_data;

void producer_thread(int unused1, int unused2, int unused3)
{
    while (1) {
        /* create data item to send */
        tx_data = ...

        /* send data to consumers */
        k_fifo_put(&my_fifo, &tx_data);

        ...
    }
}
```

> 译注：原例循环复用同一个 `tx_data`，中间同步步骤用省略号代替。实际程序必须确认它已出队，且消费者不再读取这块数据，才能改写并再次入队；FIFO 不会复制整个应用对象。原例线程入口使用三个 `int` 参数，正式 Zephyr 线程入口采用三个 `void *` 参数，应按目标版本接口修正。

`k_fifo_put_list()` 和 `k_fifo_put_slist()` 可一次加入一个单向链表的数据项。

> 译注——当前源码与接口说明的差异：这两个宏没有将底层函数的整数返回值传给调用者，不能直接按原API说明检查宏的0或-EINVAL结果。当前链表合并实现成功后已将源单向链表初始化为空；这与原文所说的“需要重新初始化”有所区别。详见[FIFO公共接口](../queue_reference/P003_FIFO公共接口.md)中的原始宏展开及源码依据。

`k_fifo_alloc_put()` 则免去数据项内的内核预留字段，从调用线程资源池分配额外内存，保留到该项被取出为止。

> 译注：分配的是队列链接管理空间，不是替应用复制或延长数据对象寿命。应检查分配型接口的返回值，并保证对象在消费完成前有效。

## 14.5\_读取FIFO

调用 `k_fifo_get()` 取出数据项。下面无限等待生产者提供数据，再处理返回的对象指针：

```c
void consumer_thread(int unused1, int unused2, int unused3)
{
    struct data_item_t  *rx_data;

    while (1) {
        rx_data = k_fifo_get(&my_fifo, K_FOREVER);

        /* process FIFO data item */
        ...
    }
}
```

## 14.6\_用途、配置与接口

FIFO 适合按先进先出顺序异步传递任意大小的数据项。原文相关配置选项列为“无”。完整接口见[FIFO APIs](../queue_reference/P003_FIFO公共接口.md)。

相关[哲学家就餐示例](../basic_samples/P030_哲学家就餐示例.md#dining-philosophers)用 Zephyr 内核服务解决经典同步问题。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：条件变量](P013_条件变量.md) · [本模块主线目录](../reading/kernel.md) · [全部主线](../reading/README.md) · [下一篇：LIFO后进先出队列](P015_LIFO后进先出队列.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：条件变量](P013_条件变量.md) · [下一章：LIFO后进先出队列](P015_LIFO后进先出队列.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
