---
id: learning.zephyr-docs.kernel.lifos
title: LIFO后进先出队列
kind: reference
status: maintained
domains: [zephyr, kernel, data-passing]
source_url: https://docs.zephyrproject.org/latest/kernel/services/data_passing/lifos.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第15章\_LIFO后进先出队列

原文：[LIFOs](https://docs.zephyrproject.org/latest/kernel/services/data_passing/lifos.html)。读取日期：2026-10-12，`latest`。

**后进先出（Last In, First Out，LIFO）** 是实现后进先出（Last In, First Out）队列的内核对象，允许线程与**中断服务例程（Interrupt Service Routine，ISR）**加入或取出任意大小的数据项。

## 15.1\_概念与数据布局

LIFO 数量只受可用内存等资源限制，通过内存地址引用。核心属性是已加入、尚未取出的数据项队列，内部用简单链表实现。使用前必须初始化，将队列设为空。

普通数据项必须按指针要求对齐，且把最前面的一个指针大小字段留给内核，作为下一项链接。因此 N 字节应用数据需要额外 4 或 8 字节，取决于指针宽度。

用 `k_lifo_alloc_put()` 加入时，无须满足上述对齐或预留字段要求；额外管理内存临时从调用线程资源池分配。

同一数据项在全部 LIFO 队列中只能有一个有效入队实例。尚未从之前的队列取出，就再次加入当前或其他 LIFO，会产生未定义行为。

## 15.2\_交付与等待

线程或 ISR 可以加入数据项。有等待线程时直接交给等待者，否则加入 LIFO 链表；队列本身不设置最大项数。

线程可以取出数据项，队列为空时可等待。多个线程可同时等待，加入新项时先交给最高优先级线程，同优先级时选等待最久者。ISR 也可取数据，但空队列时不得等待。

> 译注：后进先出描述的是已经缓存的数据项顺序；等待线程的选择仍按优先级与等待时长规则进行，二者不是同一排序规则。

## 15.3\_定义LIFO

用 `struct k_lifo` 类型定义，再调用 `k_lifo_init()` 初始化：

```c
struct k_lifo my_lifo;

k_lifo_init(&my_lifo);
```

宏 `K_LIFO_DEFINE` 可在编译时定义并初始化空队列，效果相同：

```c
K_LIFO_DEFINE(my_lifo);
```

## 15.4\_写入LIFO

调用 `k_lifo_put()` 加入数据项。下例沿用前例，将数据传给消费者；数据结构第一个字段留给内核：

```c
struct data_item_t {
    void *LIFO_reserved;   /* 1st word reserved for use by LIFO */
    ...
};

struct data_item_t tx data;

void producer_thread(int unused1, int unused2, int unused3)
{
    while (1) {
        /* create data item to send */
        tx_data = ...

        /* send data to consumers */
        k_lifo_put(&my_lifo, &tx_data);

        ...
    }
}
```

> 译注：原例声明写成 `struct data_item_t tx data;`，变量名中空格是笔误，后文实际使用 `tx_data`。它还省略了对象复用协议，实际程序必须等同一对象出队且消费完成后才能改写、重入队。LIFO 不复制整个对象。正式线程入口参数为三个 `void *`，原例三个 `int` 参数也需按接口修正。

调用 `k_lifo_alloc_put()` 时，数据项不用预留内核链接字段，额外管理内存来自调用线程资源池，直到数据项被读取后释放。

> 译注：管理节点分配不代替应用数据对象的生命周期管理，分配失败返回值也必须处理。

## 15.5\_读取LIFO

`k_lifo_get()` 取出一个数据项。下例无限等待生产者数据，然后处理返回的对象：

```c
void consumer_thread(int unused1, int unused2, int unused3)
{
    struct data_item_t  *rx_data;

    while (1) {
        rx_data = k_lifo_get(&my_lifo, K_FOREVER);

        /* process LIFO data item */
        ...
    }
}
```

## 15.6\_用途、配置与接口

LIFO 适合按后进先出顺序异步传递任意大小的数据项。原文相关配置列为“无”。完整接口见[LIFO APIs](../queue_reference/P005_LIFO公共接口.md)。

相关[哲学家就餐示例](../basic_samples/P030_哲学家就餐示例.md#dining-philosophers)使用 Zephyr 内核服务实现经典同步问题。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：FIFO先进先出队列](P014_FIFO先进先出队列.md) · [本模块主线目录](../reading/kernel.md) · [全部主线](../reading/README.md) · [下一篇：消息队列](P016_消息队列.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：FIFO先进先出队列](P014_FIFO先进先出队列.md) · [下一章：消息队列](P016_消息队列.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
