---
id: learning.zephyr-docs.intercore_reference.zbuscoreref-208
title: zbus观察者结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzbus__observer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第208章\_zbus观察者结构

原文：[structzbus__observer](https://docs.zephyrproject.org/latest/doxygen/html/structzbus__observer.html)。读取日期：2026-10-13，`latest`。

结构体`zbus_observer`表示观察者（Observer），头文件为`zephyr/zbus/zbus.h`。

## 208.1\_观察者的作用

每个观察者都有一个保存相关信息的结构。观察者是对某个通道（Channel）感兴趣的一段代码。它可以同步或异步收到通知，原说明分别称其为监听器（Listener）和订阅者（Subscriber）。

观察者可以在运行时（Runtime）启用或禁用。原文描述为修改结构中的布尔`enabled`字段；应使用`zbus_obs_set_enable`函数正确修改启用状态。

监听器具有回调函数（Callback Function）。总线发送通知时执行该回调，并把发生变化的通道索引（Channel Index，原文用语）作为参数。订阅者具有消息队列（Message Queue）；总线发送通知时，把发生变化的通道索引加入队列。

## 208.2\_原说明与可见声明的差异

**译注：** 同批头文件中的监听器回调参数实际是`const struct zbus_channel *chan`，订阅者定义宏创建的队列元素也是`struct zbus_channel *`。因此原说明的“索引”应结合实际的**通道指针**类型理解，不应改成整数索引传入。

`enabled`实际保存在`obs->data->enabled`中，而不是直接作为`zbus_observer`的成员。当前枚举还包含消息订阅者（Message Subscriber）和异步监听器（Asynchronous Listener），具体用途和宏见[zbus核心接口](P213_zbus核心接口.md)。

## 208.3\_对应的可见源码声明

以下保留官方可见声明及其条件编译（Conditional Compilation）。`CONFIG_`开头的配置宏来自 Kconfig 构建配置系统（Build Configuration System）。

```c
struct zbus_observer {
#if defined(CONFIG_ZBUS_OBSERVER_NAME) || defined(__DOXYGEN__)
        const char *name;
#endif
        enum zbus_observer_type type;

        struct zbus_observer_data *data;

        union {
                struct k_msgq *queue;

                void (*callback)(const struct zbus_channel *chan);

#if defined(CONFIG_ZBUS_MSG_SUBSCRIBER) || defined(__DOXYGEN__)
                struct k_fifo *message_fifo;
#endif /* CONFIG_ZBUS_MSG_SUBSCRIBER */

#if defined(CONFIG_ZBUS_ASYNC_LISTENER) || defined(__DOXYGEN__)
                struct k_work *work;
#endif /* CONFIG_ZBUS_ASYNC_LISTENER */
        };
};
```

同页可见的可变数据结构如下，其中`priority`优先级字段仅在启用优先级提升（Priority Boost）时存在：

```c
struct zbus_observer_data {
        bool enabled;

#if defined(CONFIG_ZBUS_PRIORITY_BOOST)
        int priority;
#endif /* CONFIG_ZBUS_PRIORITY_BOOST */
};
```

完整原始头文件见[zbus核心完整头文件](P212_zbus核心完整头文件.md)；启用／禁用和状态查询函数见[zbus核心接口](P213_zbus核心接口.md)。

---

[上一章：zbus通道运行时结构](P207_zbus通道运行时结构.md) · [下一章：zbus运行时观察者节点](P209_zbus运行时观察者节点.md) · [返回大纲](大纲.md)
