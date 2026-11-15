---
id: learning.zephyr-docs.intercore_reference.zbuscoreref-207
title: zbus通道运行时结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzbus__channel__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第207章\_zbus通道运行时结构

原文：[structzbus__channel__data](https://docs.zephyrproject.org/latest/doxygen/html/structzbus__channel__data.html)。读取日期：2026-10-13，`latest`。

结构体`zbus_channel_data`表示通道的可变数据（Channel Mutable Data）。每个通道都关联一个这样的结构。

头文件为`zephyr/zbus/zbus.h`。

条件字段由 Kconfig 构建配置系统（Build Configuration System）的配置宏控制：`CONFIG_ZBUS_PRIORITY_BOOST`为优先级提升，`CONFIG_ZBUS_RUNTIME_OBSERVERS`为运行时观察者，`CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION`为消息订阅者缓冲池隔离，`CONFIG_ZBUS_CHANNEL_PUBLISH_STATS`为通道发布统计。

## 207.1\_对应的可见源码声明

原结构参考页没有逐字段说明。以下声明从同一头文件的官方可见源码摘录，保留全部条件编译（Conditional Compilation）：

```c
struct zbus_channel_data {

        int16_t observers_start_idx;

        int16_t observers_end_idx;

        struct k_sem sem;

#if defined(CONFIG_ZBUS_PRIORITY_BOOST)
        int highest_observer_priority;
#endif /* CONFIG_ZBUS_PRIORITY_BOOST */

#if defined(CONFIG_ZBUS_RUNTIME_OBSERVERS) || defined(__DOXYGEN__)
        sys_slist_t observers;
#endif /* CONFIG_ZBUS_RUNTIME_OBSERVERS */

#if defined(CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION) || defined(__DOXYGEN__)
        struct net_buf_pool *msg_subscriber_pool;
#endif /* ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION */

#if defined(CONFIG_ZBUS_CHANNEL_PUBLISH_STATS) || defined(__DOXYGEN__)
        k_ticks_t publish_timestamp;
        uint32_t publish_count;
#endif /* CONFIG_ZBUS_CHANNEL_PUBLISH_STATS */

};
```

## 207.2\_源码字段阅读说明

以下根据可见源码提供成员定位，不补充原页未说明的内部算法契约。

| 成员 | 阅读定位 |
| --- | --- |
| `observers_start_idx``observers_end_idx` | 观察者（Observer）起止索引 |
| `sem` | 通道访问使用的信号量（Semaphore） |
| `highest_observer_priority` | 优先级提升（Priority Boost）配置下的最高观察者优先级 |
| `observers` | 运行时观察者（Runtime Observer）单向链表（Singly Linked List） |
| `msg_subscriber_pool` | 缓冲池隔离（Buffer Pool Isolation）配置下的消息订阅者缓冲池指针 |
| `publish_timestamp``publish_count` | 发布统计（Publish Statistics）配置下的时间戳和计数 |

`CONFIG_`开头的条件均来自 Kconfig 构建配置系统（Build Configuration System），分别对应优先级提升、运行时观察者、消息订阅者缓冲池隔离和通道发布统计；`__DOXYGEN__`用于文档生成。

通道主结构见[zbus通道结构](P206_zbus通道结构.md)，访问和统计接口见[zbus核心接口](P213_zbus核心接口.md)，完整源码见[zbus核心完整头文件](P212_zbus核心完整头文件.md)。

---

[上一章：zbus通道结构](P206_zbus通道结构.md) · [下一章：zbus观察者结构](P208_zbus观察者结构.md) · [返回大纲](大纲.md)
