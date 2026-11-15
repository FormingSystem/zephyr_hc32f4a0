---
id: learning.zephyr-docs.intercore_reference.zbuscoreref-213
title: zbus核心接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第213章\_zbus核心接口

原文：[group__zbus__apis](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html)。读取日期：2026-10-13，`latest`。

本页完整翻译 zbus 消息总线（Message Bus）的应用程序编程接口（Application Programming Interface，API），头文件为`zephyr/zbus/zbus.h`。原页注明：自 Zephyr **3.3.0** 提供，接口版本为 **1.0.0**。

## 213.1\_术语与读取约定

通道（Channel）保存消息；观察者（Observer）关注通道。监听器（Listener）通过同步回调（Synchronous Callback）收到通知，订阅者（Subscriber）通过消息队列（Message Queue）异步等待通知；消息订阅者（Message Subscriber）和异步监听器（Asynchronous Listener）使用消息副本及先进先出队列（First In, First Out，FIFO）。

运行时（Runtime）表示系统运行期间；占用（Claim）锁定通道，结束占用（Finish）释放该访问控制。屏蔽（Mask）针对通道与观察者的特定观察关系。回调（Callback）、工作队列（Work Queue）、信号量（Semaphore）和缓冲池（Buffer Pool）分别按下面接口说明使用。

`CONFIG_`选项由 Kconfig 构建配置系统（Build Configuration System）提供。`K_NO_WAIT`表示不等待，`K_FOREVER`表示无限等待。ISR 指中断服务程序（Interrupt Service Routine）；表中的`[in]`为输入、`[out]`为输出，`—`表示原表未标注方向。`NULL`为空指针，`true/false`为布尔真／假。ID 指标识（Identifier）。

下面宏展开涉及的`IF_ENABLED`是按配置决定是否展开的辅助宏，`STRUCT_SECTION_ITERABLE`用于定义可迭代段（Iterable Section）对象，`Z_WORK_INITIALIZER`初始化工作项，`ZBUS_OBSERVER_NAME_INIT`初始化观察者名称字段。`ZBUS_MIN_THREAD_PRIORITY`是最低线程优先级宏，`ZBUS_OBSERVER_LISTENER_TYPE`是监听器类型枚举项。

`CONFIG_ZBUS_ASYNC_LISTENER`是异步监听器配置宏，`CONFIG_ZBUS_PRIORITY_BOOST`是优先级提升配置宏，`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE`选择不由接口分配运行时观察者节点的配置，`CONFIG_ZBUS_ASSERT_MOCK`控制用于测试的断言替代行为，`CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION`控制运行时通道注册。它们均为 Kconfig 构建配置系统的选项。

错误码（Error Code）保持原 C 标识；每张返回值表说明该接口下的具体条件，不能仅凭通用错误名推断。`timeout`参数为超时时间，`node`为持久节点参数，`masked`为屏蔽状态参数。`UINT64_MAX`为64位无符号整数最大值，`age_ms`是文档表示毫秒消息年龄的返回值名称。

## 213.2\_相关结构与代理接口

| 参考 | 内容 |
| --- | --- |
| [zbus通道运行时结构](P207_zbus通道运行时结构.md) | 通道可变数据 |
| [zbus通道结构](P206_zbus通道结构.md) | 通道访问与使用 |
| [zbus运行时通道结构](P210_zbus运行时通道结构.md) | 运行时通道 |
| [zbus观察者结构](P208_zbus观察者结构.md) | 观察者 |
| [zbus运行时观察者节点](P209_zbus运行时观察者节点.md) | 运行时观察者节点 |

跨域代理主题见[zbus代理接口](P193_zbus代理接口.md)。完整头文件见[zbus核心完整头文件](P212_zbus核心完整头文件.md)。

## 213.3\_定义启用的异步监听器

宏`ZBUS_ASYNC_LISTENER_DEFINE`：定义异步监听器类型的观察者，并以启用状态初始化。仅在启用`CONFIG_ZBUS_ASYNC_LISTENER`时可用。


```c
#define ZBUS_ASYNC_LISTENER_DEFINE(_name, _cb)
```

原始宏展开：

```c
ZBUS_ASYNC_LISTENER_DEFINE_WITH_ENABLE(_name, _cb, true)
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_name` | [in] | 异步监听器名称 |
| `_cb` | [in] | 异步监听器回调函数 |


## 213.4\_定义指定初始状态的异步监听器

宏`ZBUS_ASYNC_LISTENER_DEFINE_WITH_ENABLE`：定义`ZBUS_OBSERVER_ASYNC_LISTENER_TYPE`类型的观察者。创建异步监听器工作项（Work Item），处理用于异步接收消息的先进先出队列（First In, First Out，FIFO），并初始化表示该监听器的`zbus_observer`结构。仅在启用`CONFIG_ZBUS_ASYNC_LISTENER`时可用。宏中的`Name field`注释表示名称字段。


```c
#define ZBUS_ASYNC_LISTENER_DEFINE_WITH_ENABLE(_name, _cb, _enable)
```

原始宏展开：

```c
static K_FIFO_DEFINE(_zbus_observer_work_fifo_##_name);                   \
static struct zbus_async_listener_work _zbus_observer_work_##_name = {    \
        .work = Z_WORK_INITIALIZER(async_listener_work_handler),          \
        .message_fifo = &_CONCAT(_zbus_observer_work_fifo_, _name),       \
        .queue = &k_sys_work_q,                                           \
        .callback = _cb,                                                  \
};                                                                        \
static struct zbus_observer_data _CONCAT(_zbus_obs_data_, _name) = {      \
        .enabled = _enable,                                               \
        IF_ENABLED(CONFIG_ZBUS_PRIORITY_BOOST, (                          \
                .priority = ZBUS_MIN_THREAD_PRIORITY,                     \
        ))                                                                \
};                                                                        \
_ZBUS_CPP_EXTERN const STRUCT_SECTION_ITERABLE(zbus_observer, _name) = {  \
        ZBUS_OBSERVER_NAME_INIT(_name) /* Name field */                   \
        .type = ZBUS_OBSERVER_ASYNC_LISTENER_TYPE,                        \
        .data = &_CONCAT(_zbus_obs_data_, _name),                         \
        .work = &_CONCAT(_zbus_observer_work_, _name).work,               \
}
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_name` | [in] | 异步监听器名称 |
| `_cb` | [in] | 异步监听器回调函数 |
| `_enable` | [in] | 异步监听器初始状态 |


## 213.5\_添加静态观察关系

宏`ZBUS_CHAN_ADD_OBS`：通过给定通道和观察者，初始化静态通道观察关系（Static Channel Observation）。展开调用带屏蔽参数的宏，并将初始屏蔽状态设为`false`。


```c
#define ZBUS_CHAN_ADD_OBS(_chan, _obs, _prio)
```

原始宏展开：

```c
ZBUS_CHAN_ADD_OBS_WITH_MASK(_chan, _obs, false, _prio)
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_chan` | — | 通道实例 |
| `_obs` | — | 观察者实例 |
| `_prio` | — | 观察者通知顺序的优先级 |


## 213.6\_添加带屏蔽状态的静态观察关系

宏`ZBUS_CHAN_ADD_OBS_WITH_MASK`：通过给定通道和观察者，初始化静态通道观察关系。观察关系的屏蔽状态由`_masked`指定。


```c
#define ZBUS_CHAN_ADD_OBS_WITH_MASK(_chan, _obs, _masked, _prio)
```

原始宏展开：

```c
const STRUCT_SECTION_ITERABLE(zbus_channel_observation,                                    \
        _CONCAT(_CONCAT(_chan, zz), _CONCAT(_prio, _obs))) = {                             \
                .chan = &_chan,                                                            \
                .obs = &_obs,                                                              \
};                                                                                         \
STRUCT_SECTION_ITERABLE(zbus_channel_observation_mask,                                     \
                        _CONCAT(_CONCAT(_CONCAT(_chan, zz), _CONCAT(_prio, _obs)),         \
                                _mask)) = {.enabled = _masked}
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_chan` | — | 通道实例 |
| `_obs` | — | 观察者实例 |
| `_masked` | — | 观察关系的状态 |
| `_prio` | — | 观察者通知顺序的优先级 |


## 213.7\_声明外部通道

宏`ZBUS_CHAN_DECLARE`：列出文件内要使用的通道；内部使用`extern`声明。仅在通道定义位于本文件之外时才需要。


```c
#define ZBUS_CHAN_DECLARE(...)
```

原始宏展开：

```c
FOR_EACH(_ZBUS_CHAN_EXTERN, (;), __VA_ARGS__)
```

## 213.8\_定义通道

宏`ZBUS_CHAN_DEFINE`：定义一个 zbus 通道。参见[zbus通道结构](P206_zbus通道结构.md)。宏中两条注释依次表示“观察者的外部声明”和“从观察者列表创建全部通道观察关系”。


```c
#define ZBUS_CHAN_DEFINE(_name, _type, _validator, _user_data, _observers, _init_val)
```

原始宏展开：

```c
static _type _ZBUS_MESSAGE_NAME(_name) = _init_val;                                        \
_ZBUS_CHAN_DEFINE(_name, ZBUS_CHAN_ID_INVALID, _type, _validator, _user_data);             \
/* Extern declaration of observers */                                                      \
ZBUS_OBS_DECLARE(_observers);                                                              \
/* Create all channel observations from observers list */                                  \
FOR_EACH_FIXED_ARG_NONEMPTY_TERM(_ZBUS_CHAN_OBSERVATION, (;), _name, _observers)
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_name` | — | 通道名称 |
| `_type` | — | 消息类型，必须是结构体（Struct）或联合体（Union） |
| `_validator` | — | 验证函数 |
| `_user_data` | — | 用户数据指针 |
| `_observers` | — | 观察者列表；列表顺序决定观察者优先级，第一个观察者的优先级最高 |
| `_init_val` | — | 消息初始化值 |


## 213.9\_定义具有数字标识的通道

宏`ZBUS_CHAN_DEFINE_WITH_ID`：定义具有唯一数字标识的 zbus 通道。参见[zbus通道结构](P206_zbus通道结构.md)。宏中两条注释依次表示“观察者的外部声明”和“从观察者列表创建全部通道观察关系”。


```c
#define ZBUS_CHAN_DEFINE_WITH_ID(_name, _id, _type, _validator, _user_data, _observers, _init_val)
```

原始宏展开：

```c
static _type _ZBUS_MESSAGE_NAME(_name) = _init_val;                                        \
_ZBUS_CHAN_DEFINE(_name, _id, _type, _validator, _user_data);                              \
/* Extern declaration of observers */                                                      \
ZBUS_OBS_DECLARE(_observers);                                                              \
/* Create all channel observations from observers list */                                  \
FOR_EACH_FIXED_ARG_NONEMPTY_TERM(_ZBUS_CHAN_OBSERVATION, (;), _name, _observers)
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_name` | — | 通道名称 |
| `_id` | — | 通道的唯一数字标识 |
| `_type` | — | 消息类型，必须是结构体（Struct）或联合体（Union） |
| `_validator` | — | 验证函数 |
| `_user_data` | — | 用户数据指针 |
| `_observers` | — | 观察者列表；列表顺序决定观察者优先级，第一个观察者的优先级最高 |
| `_init_val` | — | 消息初始化值 |


## 213.10\_无效通道标识

宏`ZBUS_CHAN_ID_INVALID`：值为`UINT32_MAX`，表示通道没有唯一标识（ID）。


```c
#define ZBUS_CHAN_ID_INVALID
```

## 213.11\_定义启用的监听器

宏`ZBUS_LISTENER_DEFINE`：定义监听器类型的观察者，建立同步通知时执行的回调，并初始化表示监听器的`zbus_observer`结构。此宏创建的监听器初始处于启用状态。


```c
#define ZBUS_LISTENER_DEFINE(_name, _cb)
```

原始宏展开：

```c
ZBUS_LISTENER_DEFINE_WITH_ENABLE(_name, _cb, true)
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_name` | [in] | 监听器名称 |
| `_cb` | [in] | 回调函数 |


## 213.12\_定义指定初始状态的监听器

宏`ZBUS_LISTENER_DEFINE_WITH_ENABLE`：定义监听器类型的观察者，建立同步通知时执行的回调，并初始化表示监听器的`zbus_observer`结构。初始启用状态由参数指定；宏中的`Name field`表示名称字段。


```c
#define ZBUS_LISTENER_DEFINE_WITH_ENABLE(_name, _cb, _enable)
```

原始宏展开：

```c
static struct zbus_observer_data _CONCAT(_zbus_obs_data_, _name) = {                       \
        .enabled = _enable,                                                                \
        IF_ENABLED(CONFIG_ZBUS_PRIORITY_BOOST, (                                           \
                .priority = ZBUS_MIN_THREAD_PRIORITY,                                      \
        ))                                                                                 \
};                                                                                         \
_ZBUS_CPP_EXTERN const STRUCT_SECTION_ITERABLE(zbus_observer, _name) = {                   \
        ZBUS_OBSERVER_NAME_INIT(_name) /* Name field */                                    \
        .type = ZBUS_OBSERVER_LISTENER_TYPE,                                               \
        .data = &_CONCAT(_zbus_obs_data_, _name),                                          \
        .callback = (_cb)                                                                  \
}
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_name` | [in] | 监听器名称 |
| `_cb` | [in] | 回调函数 |
| `_enable` | [in] | 监听器初始启用状态 |


## 213.13\_初始化消息

宏`ZBUS_MSG_INIT`：传入初始值，初始化消息结构体或联合体。**译注：** 原参数说明举例使用`ZBUS_INIT`，而本页声明和源码的实际宏名是`ZBUS_MSG_INIT`。下方保留原示例拼写，使用时应依据实际声明。


```c
#define ZBUS_MSG_INIT(_val, ...)
```

原始宏展开：

```c
{_val, ##__VA_ARGS__}
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_val` | [in] | 提供初始值的可变参数（Variadic Arguments）。原文例：`ZBUS_INIT(0)`表示`{0}`，`ZBUS_INIT(.a=10, .b=30)`表示`{.a=10, .b=30}` |


## 213.14\_定义启用的消息订阅者

宏`ZBUS_MSG_SUBSCRIBER_DEFINE`：定义消息订阅者类型的观察者，创建用于异步接收消息的 FIFO，并初始化对应`zbus_observer`。此宏创建的消息订阅者初始处于启用状态。


```c
#define ZBUS_MSG_SUBSCRIBER_DEFINE(_name)
```

原始宏展开：

```c
ZBUS_MSG_SUBSCRIBER_DEFINE_WITH_ENABLE(_name, true)
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_name` | [in] | 订阅者名称 |


## 213.15\_定义指定初始状态的消息订阅者

宏`ZBUS_MSG_SUBSCRIBER_DEFINE_WITH_ENABLE`：原说明称定义`ZBUS_OBSERVER_SUBSCRIBER_TYPE`类型的观察者；创建异步接收消息的 FIFO 并初始化对应`zbus_observer`。**译注：** 宏展开实际设置的是`ZBUS_OBSERVER_MSG_SUBSCRIBER_TYPE`，原说明的类型名称与代码不一致，代码完整保留。宏中`Name field`表示名称字段。


```c
#define ZBUS_MSG_SUBSCRIBER_DEFINE_WITH_ENABLE(_name, _enable)
```

原始宏展开：

```c
static K_FIFO_DEFINE(_zbus_observer_fifo_##_name);                    \
static struct zbus_observer_data _CONCAT(_zbus_obs_data_, _name) = {  \
        .enabled = _enable,                                           \
        IF_ENABLED(CONFIG_ZBUS_PRIORITY_BOOST, (                      \
                .priority = ZBUS_MIN_THREAD_PRIORITY,                 \
        ))                                                            \
};                                                                    \
_ZBUS_CPP_EXTERN const STRUCT_SECTION_ITERABLE(zbus_observer, _name) = {  \
        ZBUS_OBSERVER_NAME_INIT(_name) /* Name field */               \
        .type = ZBUS_OBSERVER_MSG_SUBSCRIBER_TYPE,                    \
        .data = &_CONCAT(_zbus_obs_data_, _name),                     \
        .message_fifo = &_zbus_observer_fifo_##_name,                 \
}
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_name` | [in] | 订阅者名称 |
| `_enable` | [in] | 订阅者初始状态 |


## 213.16\_声明外部观察者

宏`ZBUS_OBS_DECLARE`：列出文件内要使用的观察者；内部使用`extern`声明。仅在观察者定义位于本文件之外时才需要。


```c
#define ZBUS_OBS_DECLARE(...)
```

原始宏展开：

```c
FOR_EACH_NONEMPTY_TERM(_ZBUS_OBS_EXTERN, (;), __VA_ARGS__)
```

## 213.17\_指定观察者列表

宏`ZBUS_OBSERVERS`：表示通道具有所列观察者。观察者收到通知的顺序与此处列出的顺序相同。


```c
#define ZBUS_OBSERVERS(...)
```

原始宏展开：

```c
__VA_ARGS__
```

## 213.18\_空观察者列表

宏`ZBUS_OBSERVERS_EMPTY`：表示通道没有观察者。


```c
#define ZBUS_OBSERVERS_EMPTY
```

## 213.19\_定义启用的订阅者

宏`ZBUS_SUBSCRIBER_DEFINE`：定义订阅者类型的观察者，创建用于异步接收通知的消息队列，并初始化对应`zbus_observer`结构。此宏创建的订阅者初始处于启用状态。


```c
#define ZBUS_SUBSCRIBER_DEFINE(_name, _queue_size)
```

原始宏展开：

```c
ZBUS_SUBSCRIBER_DEFINE_WITH_ENABLE(_name, _queue_size, true)
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_name` | [in] | 订阅者名称 |
| `_queue_size` | [in] | 通知队列大小 |


## 213.20\_定义指定初始状态的订阅者

宏`ZBUS_SUBSCRIBER_DEFINE_WITH_ENABLE`：定义订阅者类型的观察者，创建用于异步接收通知的消息队列，并初始化对应`zbus_observer`结构。初始启用状态由参数指定；宏中`Name field`表示名称字段。


```c
#define ZBUS_SUBSCRIBER_DEFINE_WITH_ENABLE(_name, _queue_size, _enable)
```

原始宏展开：

```c
K_MSGQ_DEFINE_STATIC_TYPE(_zbus_observer_queue_##_name,               \
                          struct zbus_channel *, _queue_size          \
);                                                                    \
static struct zbus_observer_data _CONCAT(_zbus_obs_data_, _name) = {  \
        .enabled = _enable,                                           \
        IF_ENABLED(CONFIG_ZBUS_PRIORITY_BOOST, (                      \
                .priority = ZBUS_MIN_THREAD_PRIORITY,                 \
        ))                                                            \
};                                                                    \
_ZBUS_CPP_EXTERN const STRUCT_SECTION_ITERABLE(zbus_observer, _name) = {  \
        ZBUS_OBSERVER_NAME_INIT(_name) /* Name field */               \
        .type = ZBUS_OBSERVER_SUBSCRIBER_TYPE,                        \
        .data = &_CONCAT(_zbus_obs_data_, _name),                     \
        .queue = &_zbus_observer_queue_##_name,                       \
}
```

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `_name` | [in] | 订阅者名称 |
| `_queue_size` | [in] | 通知队列大小 |
| `_enable` | [in] | 订阅者初始启用状态 |


## 213.21\_发布前验证消息

```c
typedef bool (*zbus_validator)(const void *msg, size_t msg_size);
```

验证器（Validator）在发布前检查消息有效性。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `msg` | — | 待检查的消息 |
| `msg_size` | — | `msg`的大小，单位为字节（Byte） |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `true` | 消息有效，应当发布 |
| `false` | 消息无效，不应发布 |


## 213.22\_观察者类型

枚举`zbus_observer_type`表示观察者类型。原文简介称观察者可以是监听器或订阅者；当前枚举实际包含以下四项。

| 枚举项 | 名称 |
| --- | --- |
| `ZBUS_OBSERVER_LISTENER_TYPE` | 监听器（Listener） |
| `ZBUS_OBSERVER_SUBSCRIBER_TYPE` | 订阅者（Subscriber） |
| `ZBUS_OBSERVER_MSG_SUBSCRIBER_TYPE` | 消息订阅者（Message Subscriber） |
| `ZBUS_OBSERVER_ASYNC_LISTENER_TYPE` | 异步监听器（Asynchronous Listener） |

## 213.23\_设置异步监听器工作队列

```c
static inline int zbus_async_listener_set_work_queue(const struct zbus_observer *obs,
                                                     struct k_work_q *queue);
```

设置收到通知时用于执行异步监听器回调的工作队列。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_ASYNC_LISTENER`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `obs` | [in] | 异步监听器观察者的引用 |
| `queue` | [in] | 用于执行异步监听器的工作队列 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功设置工作队列 |
| `-ENOENT` | 观察者引用为`NULL` |
| `-EINVAL` | 观察者类型无效 |
| `-EBADF` | 工作队列引用为`NULL` |


**译注：** 上表保留原 API 页错误码；同批完整头文件中，`obs == NULL`、观察者类型无效以及`queue == NULL`三个检查分支均返回`-EINVAL`。因此文档中的`-ENOENT``-EBADF`与此可见实现不一致，见[zbus核心完整头文件](P212_zbus核心完整头文件.md)。

## 213.24\_添加运行时观察者

```c
int zbus_chan_add_obs(const struct zbus_channel *chan, const struct zbus_observer *obs,
                      k_timeout_t timeout);
```

在运行时将观察者添加到通道。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_RUNTIME_OBSERVERS`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |
| `obs` | — | 待添加的观察者引用（原文如此表述） |
| `timeout` | — | 添加观察者的等待时间，或特殊值`K_NO_WAIT``K_FOREVER`之一 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已将观察者添加到通道 |
| `-EBUSY` | 未等待便返回 |
| `-EAGAIN` | 等待超时 |
| `-EEXIST` | 观察者已存在于通道的观察者列表中 |
| `-EALREADY` | 观察者已存在于通道的运行时观察者列表中 |
| `-ENOMEM` | 没有可用于新运行时观察者节点的内存 |
| `-ENOTSUP` | 启用了`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE` |


## 213.25\_使用现有节点添加观察者

```c
int zbus_chan_add_obs_with_node(const struct zbus_channel *chan, const struct zbus_observer *obs,
                                struct zbus_observer_node *node, k_timeout_t timeout);
```

提供已分配的节点，将观察者添加到通道。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_RUNTIME_OBSERVERS`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |
| `obs` | — | 待添加的观察者引用（原文如此表述） |
| `node` | — | 持久存在的结构，用于将通道与观察者连接起来 |
| `timeout` | — | 添加观察者的等待时间，或特殊值`K_NO_WAIT``K_FOREVER`之一 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已将观察者添加到通道 |
| `-EEXIST` | 观察者已存在于通道的观察者列表中 |
| `-EALREADY` | 观察者已存在于通道的运行时观察者列表中 |
| `-EAGAIN` | 等待超时 |
| `-EINVAL` | 某个参数无效 |
| `-EBUSY` | 节点已在使用中 |
| `-ENOTSUP` | 未启用`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE` |


## 213.26\_占用通道

```c
int zbus_chan_claim(const struct zbus_channel *chan, k_timeout_t timeout);
```

占用期间，通道不能发布、读取、通知或再次占用；只有结束占用操作可用。**警告：** 调用后，在执行`zbus_chan_finish`之前，其他线程不能使用通道。在一次`zbus_chan_finish`之前只能调用一次此函数。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | [in] | 通道引用 |
| `timeout` | [in] | 占用通道的等待时间，或特殊值`K_NO_WAIT``K_FOREVER`之一 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已占用通道 |
| `-EBUSY` | 通道忙 |
| `-EAGAIN` | 等待超时 |
| `-EFAULT` | 参数不正确，或函数上下文无效（处于中断服务程序 ISR 内）。仅在启用`CONFIG_ZBUS_ASSERT_MOCK`时返回此值 |


## 213.27\_直接取得只读消息引用

```c
static inline const void *zbus_chan_const_msg(const struct zbus_channel *chan);
```

返回通道消息的常量引用。供监听器直接访问消息，借此避免监听器在通知过程中改变正在通知的通道消息。**警告：** 只能直接用于已经锁定的通道，例如监听器正在接收通知的通道，或已经成功占用的通道。返回值为通道消息的常量引用。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道的常量引用 |


## 213.28\_结束通道占用

```c
int zbus_chan_finish(const struct zbus_channel *chan);
```

成功结束占用后，其他线程可以再次使用通道。**警告：** 只能在调用`zbus_chan_claim`之后使用。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已结束通道占用 |
| `-EFAULT` | 参数不正确，或函数上下文无效（处于中断服务程序 ISR 内）。仅在启用`CONFIG_ZBUS_ASSERT_MOCK`时返回此值 |


## 213.29\_按数字标识查找通道

```c
const struct zbus_channel *zbus_chan_from_id(uint32_t channel_id);
```

按唯一数字标识检索 zbus 通道。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_CHANNEL_ID`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `channel_id` | — | 来自`ZBUS_CHAN_DEFINE_WITH_ID`的唯一通道标识 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `NULL` | 不存在标识为`channel_id`的通道 |
| `chan` | 否则返回标识为`channel_id`的通道指针 |


## 213.30\_按名称查找通道

```c
const struct zbus_channel *zbus_chan_from_name(const char *name);
```

按名称字符串检索 zbus 通道。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_CHANNEL_NAME`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `name` | — | 要检索的通道名称 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `NULL` | 不存在名称为`name`的通道 |
| `chan` | 否则返回名称为`name`的通道指针 |


## 213.31\_直接取得消息引用

```c
static inline void *zbus_chan_msg(const struct zbus_channel *chan);
```

直接返回通道消息的引用。**警告：** 只能直接用于已经锁定的通道，例如监听器正在接收通知的通道，或已经成功占用的通道。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |


## 213.32\_取得消息大小

```c
static inline uint16_t zbus_chan_msg_size(const struct zbus_channel *chan);
```

返回通道的消息大小。返回类型为`uint16_t`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |


## 213.33\_取得通道名称

```c
static inline const char *zbus_chan_name(const struct zbus_channel *chan);
```

返回通道名称的引用。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_CHANNEL_NAME`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |


## 213.34\_强制发出通道通知

```c
int zbus_chan_notify(const struct zbus_channel *chan, k_timeout_t timeout);
```

即使消息没有变化，也强制事件分发器（Event Dispatcher）通知该通道的观察者。此函数可用于占用／结束占用操作之后。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |
| `timeout` | — | 通知通道的等待时间，或特殊值`K_NO_WAIT``K_FOREVER`之一 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已发出通道通知 |
| `-EBUSY` | 获取通道信号量的操作未等待便返回 |
| `-EAGAIN` | 获取通道信号量超时 |
| `-ENOMEM` | 消息缓冲池中没有更多可用缓冲区 |
| `-EFAULT` | 参数不正确、无法向一个或多个观察者发送通知，或函数上下文无效（处于中断服务程序 ISR 内）。仅在启用`CONFIG_ZBUS_ASSERT_MOCK`时返回此值 |


## 213.35\_发布消息

```c
int zbus_chan_pub(const struct zbus_channel *chan, const void *msg, k_timeout_t timeout);
```

向通道发布消息。消息数据从`msg`指向的源存储区复制到通道。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |
| `msg` | — | 源消息引用；发布函数从这里复制消息数据到通道 |
| `timeout` | — | 发布通道的等待时间，或特殊值`K_NO_WAIT``K_FOREVER`之一 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已发布通道消息 |
| `-ENOMSG` | 验证函数判定消息无效，或某些观察者无法接收通知 |
| `-EBUSY` | 通道忙 |
| `-EAGAIN` | 等待超时 |
| `-EFAULT` | 参数不正确、无法向一个或多个观察者发送通知，或函数上下文无效（处于中断服务程序 ISR 内）。仅在启用`CONFIG_ZBUS_ASSERT_MOCK`时返回此值 |


## 213.36\_取得平均发布周期

```c
static inline uint32_t zbus_chan_pub_stats_avg_period(const struct zbus_channel *chan);
```

返回发布之间的平均间隔，单位为毫秒（Millisecond）。通道尚未发布过消息时返回0。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_CHANNEL_PUBLISH_STATS`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |


源码阅读补充：当前实现采用`k_uptime_get() / publish_count`，即以应用运行至今的时间计算平均周期；这不是仅对相邻两次发布时间戳作差。

## 213.37\_取得发布次数

```c
static inline uint32_t zbus_chan_pub_stats_count(const struct zbus_channel *chan);
```

返回通道已发布消息的次数；尚未发布时返回0。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_CHANNEL_PUBLISH_STATS`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |


## 213.38\_取得最近发布时间

```c
static inline k_ticks_t zbus_chan_pub_stats_last_time(const struct zbus_channel *chan);
```

返回最近一次发布动作的内核时间戳（Kernel Timestamp）；尚未发布时返回0。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_CHANNEL_PUBLISH_STATS`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |


## 213.39\_取得消息年龄

```c
static inline uint64_t zbus_chan_pub_stats_msg_age(const struct zbus_channel *chan);
```

取得通道消息的年龄（Message Age），即距离发布的时间。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_CHANNEL_PUBLISH_STATS`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `UINT64_MAX` | 通道从未发布过消息 |
| `age_ms` | 否则返回消息年龄，单位为毫秒 |


## 213.40\_手动更新发布统计

```c
static inline void zbus_chan_pub_stats_update(const struct zbus_channel *chan);
```

为`zbus_chan_claim → zbus_chan_finish`流程更新发布统计；该流程不能自动判断是否发布了新数据。**警告：** 只能直接用于已经锁定的通道。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_CHANNEL_PUBLISH_STATS`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |


源码阅读补充：未启用发布统计时，头文件仍提供一个不执行操作的同名内联函数；上方“可用条件”沿用 API 文档对统计功能的说明。

## 213.41\_读取消息

```c
int zbus_chan_read(const struct zbus_channel *chan, void *msg, k_timeout_t timeout);
```

从通道读取消息，复制到`msg`指向的目标存储区。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | [in] | 通道引用 |
| `msg` | [out] | 目标消息引用；读取函数把通道消息数据复制到这里 |
| `timeout` | [in] | 读取通道的等待时间，或特殊值`K_NO_WAIT``K_FOREVER`之一 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已读取通道消息 |
| `-EBUSY` | 通道忙 |
| `-EAGAIN` | 等待超时 |
| `-EFAULT` | 参数不正确，或函数上下文无效（处于中断服务程序 ISR 内）。仅在启用`CONFIG_ZBUS_ASSERT_MOCK`时返回此值 |


## 213.42\_移除运行时观察者

```c
int zbus_chan_rm_obs(const struct zbus_channel *chan, const struct zbus_observer *obs,
                     k_timeout_t timeout);
```

从通道移除观察者。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_RUNTIME_OBSERVERS`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |
| `obs` | — | 要移除的观察者引用 |
| `timeout` | — | 移除观察者的等待时间，或特殊值`K_NO_WAIT``K_FOREVER`之一 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已从通道移除观察者 |
| `-EBUSY` | 未等待便返回 |
| `-EAGAIN` | 等待超时 |
| `-ENODATA` | 通道的运行时观察者列表中未找到该观察者 |


## 213.43\_设置消息订阅者缓冲池

```c
static inline void zbus_chan_set_msg_sub_pool(const struct zbus_channel *chan,
                                              struct net_buf_pool *pool);
```

设置通道的消息订阅者所用的`net_buf`缓冲池（Buffer Pool）。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |
| `pool` | — | `net_buf`内存池（Memory Pool）的引用 |


## 213.44\_取得用户数据

```c
static inline void *zbus_chan_user_data(const struct zbus_channel *chan);
```

返回通道关联的用户数据（User Data）。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 通道引用 |


## 213.45\_遍历通道

```c
bool zbus_iterate_over_channels(bool (*iterator_func)(const struct zbus_channel *chan));
```

对每个通道调用`iterator_func`迭代函数（Iterator Function）；任意一次返回`false`，整个遍历立即停止。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `iterator_func` | [in] | 每次迭代时执行的函数 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `true` | 已对所有通道执行迭代器（原文使用 channels） |
| `false` | 无法完成迭代；某次迭代返回了`false` |


## 213.46\_遍历通道并传递用户数据

```c
bool zbus_iterate_over_channels_with_user_data(
        bool (*iterator_func)(const struct zbus_channel *chan, void *user_data), void *user_data);
```

对每个通道调用`iterator_func`迭代函数（Iterator Function）；任意一次返回`false`，整个遍历立即停止。`user_data`会传入每次迭代。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `iterator_func` | [in] | 每次迭代时执行的函数 |
| `user_data` | [in] | 可以传给该函数的用户数据 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `true` | 已对所有通道执行迭代器（原文使用 channels） |
| `false` | 无法完成迭代；某次迭代返回了`false` |


## 213.47\_遍历观察者

```c
bool zbus_iterate_over_observers(bool (*iterator_func)(const struct zbus_observer *obs));
```

对每个观察者调用`iterator_func`迭代函数（Iterator Function）；任意一次返回`false`，整个遍历立即停止。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `iterator_func` | [in] | 每次迭代时执行的函数 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `true` | 已对所有通道执行迭代器（原文使用 channels） |
| `false` | 无法完成迭代；某次迭代返回了`false` |


**译注：** 原成功返回说明使用“所有通道（all channels）”；本函数遍历的是观察者，应结合函数名称和迭代参数理解，原措辞已在表中标明。

## 213.48\_遍历观察者并传递用户数据

```c
bool zbus_iterate_over_observers_with_user_data(
        bool (*iterator_func)(const struct zbus_observer *obs, void *user_data), void *user_data);
```

对每个观察者调用`iterator_func`迭代函数（Iterator Function）；任意一次返回`false`，整个遍历立即停止。`user_data`会传入每次迭代。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `iterator_func` | [in] | 每次迭代时执行的函数 |
| `user_data` | [in] | 可以传给该函数的用户数据 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `true` | 已对所有通道执行迭代器（原文使用 channels） |
| `false` | 无法完成迭代；某次迭代返回了`false` |


**译注：** 原成功返回说明使用“所有通道（all channels）”；本函数遍历的是观察者，应结合函数名称和迭代参数理解，原措辞已在表中标明。

## 213.49\_将观察者附加到线程

```c
int zbus_obs_attach_to_thread(const struct zbus_observer *obs);
```

通过把观察者附加到线程，设置观察者线程优先级（Thread Priority）。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_PRIORITY_BOOST`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `obs` | [in] | 观察者引用 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 观察者已从线程分离（原文如此表述） |
| `-EFAULT` | 参数不正确，或函数上下文无效（处于中断服务程序 ISR 内）。仅在启用`CONFIG_ZBUS_ASSERT_MOCK`时返回此值 |


**译注：** 原返回值表把0写成“已从线程分离”，与本函数“附加到线程”的名称和用途相矛盾；上表保留原说法以避免静默改写。

## 213.50\_将观察者与线程分离

```c
int zbus_obs_detach_from_thread(const struct zbus_observer *obs);
```

通过把观察者从线程分离，清除其线程优先级。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_PRIORITY_BOOST`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `obs` | [in] | 观察者引用 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 观察者已从线程分离（原文如此表述） |
| `-EFAULT` | 参数不正确，或函数上下文无效（处于中断服务程序 ISR 内）。仅在启用`CONFIG_ZBUS_ASSERT_MOCK`时返回此值 |


## 213.51\_取得通道通知屏蔽状态

```c
int zbus_obs_is_chan_notification_masked(const struct zbus_observer *obs,
                                         const struct zbus_channel *chan, bool *masked);
```

取得特定通道到特定观察者的通知屏蔽状态。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `obs` | — | 待添加的观察者引用（原文如此表述） |
| `chan` | — | 通道引用 |
| `masked` | [out] | 屏蔽状态；为`true`时，观察者不会收到此通道的通知 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已取得屏蔽状态 |
| `-ESRCH` | 未找到对应`chan/obs`组合的观察关系 |
| `-EINVAL` | 某个参数无效 |


**译注：** 原`obs`参数说明写成“待添加”，但此处执行查询或设置屏蔽状态，并非添加观察者。

## 213.52\_取得观察者启用状态

```c
static inline int zbus_obs_is_enabled(const struct zbus_observer *obs, bool *enable);
```

读取观察者状态。原返回值说明为“观察者状态”。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `obs` | [in] | 观察者引用 |
| `enable` | [out] | 布尔输出值的引用 |


**译注：** 同批可见源码通过`*enable = obs->data->enabled`输出布尔状态，正常返回的`int`值为0；不可把函数返回值直接当作启用状态。源码使用`_ZBUS_ASSERT`检查两个指针。

## 213.53\_取得观察者名称

```c
static inline const char *zbus_obs_name(const struct zbus_observer *obs);
```

返回观察者名称的引用。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_OBSERVER_NAME`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `obs` | — | 观察者引用 |


## 213.54\_设置通道通知屏蔽状态

```c
int zbus_obs_set_chan_notification_mask(const struct zbus_observer *obs,
                                        const struct zbus_channel *chan, bool masked);
```

观察者可以用此函数屏蔽其正在观察的某个特定通道的通知。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `obs` | — | 待添加的观察者引用（原文如此表述） |
| `chan` | — | 通道引用 |
| `masked` | — | 屏蔽状态；为`true`时，观察者不会收到此通道的通知 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已设置该观察者的通道通知屏蔽状态 |
| `-ESRCH` | 未找到对应`chan/obs`组合的观察关系 |
| `-EINVAL` | 某个参数无效 |


**译注：** 原`obs`参数说明写成“待添加”，但此处执行查询或设置屏蔽状态，并非添加观察者。

## 213.55\_设置观察者启用状态

```c
int zbus_obs_set_enable(const struct zbus_observer *obs, bool enabled);
```

修改观察者状态。原说明称“禁用的通道不会收到事件分发器通知”。**译注：** 本接口的对象和`enabled`参数均是观察者，该句中的 channel 与上下文不一致；观察者禁用后停止接收通知。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `obs` | [in] | 观察者引用 |
| `enabled` | [in] | 要设置的状态；为`false`时，观察者停止接收通知 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已设置观察者的启用状态 |
| `-EFAULT` | 参数不正确，或函数上下文无效（处于中断服务程序 ISR 内）。仅在启用`CONFIG_ZBUS_ASSERT_MOCK`时返回此值 |


## 213.56\_初始化运行时通道

```c
static inline void zbus_runtime_channel_init(struct zbus_runtime_channel *chan,
                                             struct zbus_channel_data *data, const char *name,
                                             uint32_t id, zbus_validator validator, void *message,
                                             size_t message_size, void *user_data);
```

初始化 zbus 运行时通道结构。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 待初始化的通道结构 |
| `data` | — | 通道数据指针，其内容由此函数初始化 |
| `name` | — | 要为通道设置的名称 |
| `id` | — | 通道使用的唯一数字标识；不需要时使用`ZBUS_CHAN_ID_INVALID` |
| `validator` | — | 发布时使用的验证函数 |
| `message` | — | 消息存储区，**必须在通道的整个生命周期内保持有效** |
| `message_size` | — | 消息存储区大小，单位为字节 |
| `user_data` | — | 与通道关联的任意用户数据 |


源码可用条件补充：该组函数位于`CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION`条件内；`__DOXYGEN__`分支用于生成文档。

## 213.57\_注册运行时通道

```c
int zbus_runtime_channel_register(struct zbus_runtime_channel *chan);
```

向 zbus 基础设施注册运行时通道。由于内部锁定机制，**不能从通道迭代函数`zbus_iterate_over_channels`或`zbus_iterate_over_channels_with_user_data`中调用**。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 待注册的运行时通道 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-EEXIST` | 通道标识已存在于 zbus 中 |


源码可用条件补充：该组函数位于`CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION`条件内；`__DOXYGEN__`分支用于生成文档。

## 213.58\_注销运行时通道

```c
int zbus_runtime_channel_unregister(struct zbus_runtime_channel *chan);
```

从 zbus 基础设施注销运行时通道。由于内部锁定机制，**不能从通道迭代函数`zbus_iterate_over_channels`或`zbus_iterate_over_channels_with_user_data`中调用**。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `chan` | — | 待注销的运行时通道 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已成功注销通道 |
| `-ENODATA` | 通道此前未注册 |


源码可用条件补充：该组函数位于`CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION`条件内；`__DOXYGEN__`分支用于生成文档。

## 213.59\_等待通道通知

```c
int zbus_sub_wait(const struct zbus_observer *sub, const struct zbus_channel **chan,
                  k_timeout_t timeout);
```

让订阅者等待通知；收到的通知是一个通道引用。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `sub` | [in] | 订阅者引用 |
| `chan` | [out] | 发出通知的通道引用 |
| `timeout` | [in] | 等待通知到达的时间，或特殊值`K_NO_WAIT``K_FOREVER`之一 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已收到通知 |
| `-ENOMSG` | 未等待便返回 |
| `-EAGAIN` | 等待超时 |
| `-EINVAL` | 观察者不是订阅者 |
| `-EFAULT` | 参数不正确，或函数上下文无效（处于中断服务程序 ISR 内）。仅在启用`CONFIG_ZBUS_ASSERT_MOCK`时返回此值 |


## 213.60\_等待通道消息

```c
int zbus_sub_wait_msg(const struct zbus_observer *sub, const struct zbus_channel **chan, void *msg,
                      k_timeout_t timeout);
```

在通道发布时，等待新消息。

**可用条件：** 启用 Kconfig 配置宏`CONFIG_ZBUS_MSG_SUBSCRIBER`。

**参数：**

| 参数 | 方向 | 说明 |
| --- | --- | --- |
| `sub` | [in] | 订阅者引用 |
| `chan` | [out] | 发出通知的通道引用 |
| `msg` | [out] | 已发布消息副本的引用 |
| `timeout` | [in] | 等待通知到达的时间，或特殊值`K_NO_WAIT``K_FOREVER`之一 |


**返回值：**

| 返回值 | 含义 |
| --- | --- |
| `0` | 已收到消息 |
| `-EINVAL` | 观察者不是订阅者 |
| `-ENOMSG` | 无法从订阅者的先进先出队列（FIFO）取得`net_buf` |
| `-EILSEQ` | 收到无效的通道引用 |
| `-EFAULT` | 参数不正确，或函数上下文无效（处于中断服务程序 ISR 内）。仅在启用`CONFIG_ZBUS_ASSERT_MOCK`时返回此值 |

---

[上一章：zbus核心完整头文件](P212_zbus核心完整头文件.md) · [返回大纲](大纲.md) · [下一章](P214_IVSHMEM共享内存接口.md)
