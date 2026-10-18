---
id: learning.zephyr-docs.intercore_reference.zbuscoreref-211
title: zbus核心头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zbus_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第211章\_zbus核心头文件参考

原文：[zbus_8h](https://docs.zephyrproject.org/latest/doxygen/html/zbus_8h.html)。读取日期：2026-10-13，`latest`。

本页是消息总线（Message Bus）zbus 的`zephyr/zbus/zbus.h`头文件参考（Header Reference）。

## 211.1\_依赖头文件

```c
#include <string.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/check.h>
#include <zephyr/sys/iterable_sections.h>
```

## 211.2\_数据结构

| 结构 | 用途 |
| --- | --- |
| [zbus通道运行时结构](P207_zbus通道运行时结构.md) | 表示通道可变数据（Channel Mutable Data） |
| [zbus通道结构](P206_zbus通道结构.md) | 表示通道（Channel） |
| [zbus运行时通道结构](P210_zbus运行时通道结构.md) | 表示运行时通道（Runtime Channel） |
| [zbus观察者结构](P208_zbus观察者结构.md) | 表示观察者（Observer） |
| [zbus运行时观察者节点](P209_zbus运行时观察者节点.md) | 注册运行时观察者（Runtime Observer） |

## 211.3\_宏定义

宏中的 Listener 为监听器，Subscriber 为订阅者，Message Subscriber 为消息订阅者，Async Listener 为异步监听器，ID 为标识（Identifier）。下列18项按原参考页顺序排列。


```c
#define ZBUS_CHAN_ADD_OBS(_chan, _obs, _prio)
```

添加静态观察关系。


```c
#define ZBUS_CHAN_ADD_OBS_WITH_MASK(_chan, _obs, _masked, _prio)
```

添加带屏蔽状态的静态观察关系。


```c
#define ZBUS_OBS_DECLARE(...)
```

声明外部观察者。


```c
#define ZBUS_CHAN_DECLARE(...)
```

声明外部通道。


```c
#define ZBUS_OBSERVERS(...)
```

指定观察者列表。


```c
#define ZBUS_OBSERVERS_EMPTY
```

空观察者列表。


```c
#define ZBUS_CHAN_ID_INVALID UINT32_MAX
```

无效通道标识。


```c
#define ZBUS_CHAN_DEFINE(_name, _type, _validator, _user_data, _observers, _init_val)
```

定义通道。


```c
#define ZBUS_CHAN_DEFINE_WITH_ID(_name, _id, _type, _validator, _user_data, _observers, _init_val)
```

定义具有数字标识的通道。


```c
#define ZBUS_MSG_INIT(_val, ...)
```

初始化消息。


```c
#define ZBUS_SUBSCRIBER_DEFINE(_name, _queue_size)
```

定义启用的订阅者。


```c
#define ZBUS_SUBSCRIBER_DEFINE_WITH_ENABLE(_name, _queue_size, _enable)
```

定义指定初始状态的订阅者。


```c
#define ZBUS_LISTENER_DEFINE(_name, _cb)
```

定义启用的监听器。


```c
#define ZBUS_LISTENER_DEFINE_WITH_ENABLE(_name, _cb, _enable)
```

定义指定初始状态的监听器。


```c
#define ZBUS_MSG_SUBSCRIBER_DEFINE(_name)
```

定义启用的消息订阅者。


```c
#define ZBUS_MSG_SUBSCRIBER_DEFINE_WITH_ENABLE(_name, _enable)
```

定义指定初始状态的消息订阅者。


```c
#define ZBUS_ASYNC_LISTENER_DEFINE(_name, _cb)
```

定义启用的异步监听器。


```c
#define ZBUS_ASYNC_LISTENER_DEFINE_WITH_ENABLE(_name, _cb, _enable)
```

定义指定初始状态的异步监听器。

## 211.4\_验证器与观察者类型

```c
typedef bool (*zbus_validator)(const void *msg, size_t msg_size);
```

验证器（Validator）在发布前检查消息有效性。

枚举`zbus_observer_type`表示观察者类型，包含监听器`ZBUS_OBSERVER_LISTENER_TYPE`、订阅者`ZBUS_OBSERVER_SUBSCRIBER_TYPE`、消息订阅者`ZBUS_OBSERVER_MSG_SUBSCRIBER_TYPE`和异步监听器`ZBUS_OBSERVER_ASYNC_LISTENER_TYPE`。

## 211.5\_函数接口

下列38项按原参考页顺序排列，保留完整参数类型。回调（Callback）、工作队列（Work Queue）、用户数据（User Data）、通知屏蔽（Notification Masking）和线程优先级（Thread Priority）的详细契约见[zbus核心接口](P213_zbus核心接口.md)。


```c
static inline int zbus_async_listener_set_work_queue(const struct zbus_observer *obs,
                                                     struct k_work_q *queue);
```

设置异步监听器工作队列。


```c
int zbus_chan_pub(const struct zbus_channel *chan, const void *msg, k_timeout_t timeout);
```

发布消息。


```c
int zbus_chan_read(const struct zbus_channel *chan, void *msg, k_timeout_t timeout);
```

读取消息。


```c
int zbus_chan_claim(const struct zbus_channel *chan, k_timeout_t timeout);
```

占用通道。


```c
int zbus_chan_finish(const struct zbus_channel *chan);
```

结束通道占用。


```c
int zbus_chan_notify(const struct zbus_channel *chan, k_timeout_t timeout);
```

强制发出通道通知。


```c
static inline const char *zbus_chan_name(const struct zbus_channel *chan);
```

取得通道名称。


```c
const struct zbus_channel *zbus_chan_from_id(uint32_t channel_id);
```

按数字标识查找通道。


```c
const struct zbus_channel *zbus_chan_from_name(const char *name);
```

按名称查找通道。


```c
static inline void zbus_runtime_channel_init(struct zbus_runtime_channel *chan,
                                             struct zbus_channel_data *data, const char *name,
                                             uint32_t id, zbus_validator validator, void *message,
                                             size_t message_size, void *user_data);
```

初始化运行时通道。


```c
int zbus_runtime_channel_register(struct zbus_runtime_channel *chan);
```

注册运行时通道。


```c
int zbus_runtime_channel_unregister(struct zbus_runtime_channel *chan);
```

注销运行时通道。


```c
static inline void *zbus_chan_msg(const struct zbus_channel *chan);
```

直接取得消息引用。


```c
static inline const void *zbus_chan_const_msg(const struct zbus_channel *chan);
```

直接取得只读消息引用。


```c
static inline uint16_t zbus_chan_msg_size(const struct zbus_channel *chan);
```

取得消息大小。


```c
static inline void *zbus_chan_user_data(const struct zbus_channel *chan);
```

取得用户数据。


## 211.6\_缓冲池、发布统计与运行时观察者

```c
static inline void zbus_chan_set_msg_sub_pool(const struct zbus_channel *chan,
                                              struct net_buf_pool *pool);
```

设置消息订阅者缓冲池。


```c
static inline void zbus_chan_pub_stats_update(const struct zbus_channel *chan);
```

手动更新发布统计。


```c
static inline k_ticks_t zbus_chan_pub_stats_last_time(const struct zbus_channel *chan);
```

取得最近发布时间。


```c
static inline uint32_t zbus_chan_pub_stats_count(const struct zbus_channel *chan);
```

取得发布次数。


```c
static inline uint32_t zbus_chan_pub_stats_avg_period(const struct zbus_channel *chan);
```

取得平均发布周期。


```c
static inline uint64_t zbus_chan_pub_stats_msg_age(const struct zbus_channel *chan);
```

取得消息年龄。


```c
int zbus_chan_add_obs(const struct zbus_channel *chan, const struct zbus_observer *obs,
                      k_timeout_t timeout);
```

添加运行时观察者。


```c
int zbus_chan_add_obs_with_node(const struct zbus_channel *chan, const struct zbus_observer *obs,
                                struct zbus_observer_node *node, k_timeout_t timeout);
```

使用现有节点添加观察者。


```c
int zbus_chan_rm_obs(const struct zbus_channel *chan, const struct zbus_observer *obs,
                     k_timeout_t timeout);
```

移除运行时观察者。


## 211.7\_观察者状态与通知等待

```c
int zbus_obs_set_enable(const struct zbus_observer *obs, bool enabled);
```

设置观察者启用状态。


```c
static inline int zbus_obs_is_enabled(const struct zbus_observer *obs, bool *enable);
```

取得观察者启用状态。


```c
int zbus_obs_set_chan_notification_mask(const struct zbus_observer *obs,
                                        const struct zbus_channel *chan, bool masked);
```

设置通道通知屏蔽状态。


```c
int zbus_obs_is_chan_notification_masked(const struct zbus_observer *obs,
                                         const struct zbus_channel *chan, bool *masked);
```

取得通道通知屏蔽状态。


```c
static inline const char *zbus_obs_name(const struct zbus_observer *obs);
```

取得观察者名称。


```c
int zbus_obs_attach_to_thread(const struct zbus_observer *obs);
```

将观察者附加到线程。


```c
int zbus_obs_detach_from_thread(const struct zbus_observer *obs);
```

将观察者与线程分离。


```c
int zbus_sub_wait(const struct zbus_observer *sub, const struct zbus_channel **chan,
                  k_timeout_t timeout);
```

等待通道通知。


```c
int zbus_sub_wait_msg(const struct zbus_observer *sub, const struct zbus_channel **chan, void *msg,
                      k_timeout_t timeout);
```

等待通道消息。


## 211.8\_遍历接口

```c
bool zbus_iterate_over_channels(bool (*iterator_func)(const struct zbus_channel *chan));
```

遍历通道。


```c
bool zbus_iterate_over_channels_with_user_data(
        bool (*iterator_func)(const struct zbus_channel *chan, void *user_data), void *user_data);
```

遍历通道并传递用户数据。


```c
bool zbus_iterate_over_observers(bool (*iterator_func)(const struct zbus_observer *obs));
```

遍历观察者。


```c
bool zbus_iterate_over_observers_with_user_data(
        bool (*iterator_func)(const struct zbus_observer *obs, void *user_data), void *user_data);
```

遍历观察者并传递用户数据。

完整原始头文件见[zbus核心完整头文件](P212_zbus核心完整头文件.md)。

---

[上一章：zbus运行时通道结构](P210_zbus运行时通道结构.md) · [下一章：zbus核心完整头文件](P212_zbus核心完整头文件.md) · [返回大纲](大纲.md)
