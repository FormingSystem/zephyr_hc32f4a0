---
id: learning.zephyr-docs.kconfig-reference.page-437
title: "`subsys/zbus`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第437章\_`subsys/zbus`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/zbus` 的 35 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_ZBUS"></a>

## 437.1 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_ZBUS`

**提示（Prompt）**：Zbus 请求的堆内存池大小（Heap pool size）

**说明（Help）**

配置 Zbus 可用的堆内存池（Heap memory pool）。它用于多种 Zbus 操作，尤其是消息订阅者（Message subscriber）和运行时观察者（Runtime observer）的动态缓冲区分配。使用动态网络缓冲区（Net buffer）分配时，堆必须能容纳通过消息订阅者分发的全部数据。需要更多堆空间，或默认大小对该 SoC 太大时，可手动设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**默认值（Defaults）**

```text
2048 if CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC && !CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC
1024 if !CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC && CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC
3072 if CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC && CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC
0
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)、[`CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC)、[`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC)。

<a id="CONFIG_ZBUS"></a>

## 437.2 `CONFIG_ZBUS`

**提示（Prompt）**：ZBus 消息总线支持

**说明（Help）**

启用 Zephyr 消息总线（Message Bus）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING
```

**被选择（Selected by）**

```text
CONFIG_MPIPE
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_ZBUS_ASSERT_MOCK"></a>

## 437.3 `CONFIG_ZBUS_ASSERT_MOCK`

**提示（Prompt）**：用于测试的 ZBus 断言模拟（Assert Mock）。

**说明（Help）**

此配置允许开发者改变 `_ZBUS_ASSERT` 的行为。启用后，`_ZBUS_ASSERT` 返回 `-EFAULT`，而非触发断言，从而更便于测试无效参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_ASYNC_LISTENER"></a>

## 437.4 `CONFIG_ZBUS_ASYNC_LISTENER`

**提示（Prompt）**：异步监听器（Async Listeners）

**说明（Help）**

异步监听器通过工作队列异步执行回调，默认使用系统工作队列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**主动选择（Selects）**

```text
CONFIG_ZBUS_MSG_SUBSCRIBER
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)、[`CONFIG_ZBUS_MSG_SUBSCRIBER`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_MSG_SUBSCRIBER)。

<a id="CONFIG_ZBUS_ASYNC_LISTENER_EXEC_TIMEOUT"></a>

## 437.5 `CONFIG_ZBUS_ASYNC_LISTENER_EXEC_TIMEOUT`

**提示（Prompt）**：从先进先出队列（FIFO）获取消息的超时时间

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_ASYNC_LISTENER && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
200
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → 异步监听器（Async Listeners）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_ASYNC_LISTENER`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_ASYNC_LISTENER)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_CHANNELS_SYS_INIT_PRIORITY"></a>

## 437.6 `CONFIG_ZBUS_CHANNELS_SYS_INIT_PRIORITY`

**提示（Prompt）**：`SYS_INIT` 过程中使用的优先级。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_CHANNEL_ID"></a>

## 437.7 `CONFIG_ZBUS_CHANNEL_ID`

**提示（Prompt）**：通道标识符（Channel Identifier）字段

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_CHANNEL_NAME"></a>

## 437.8 `CONFIG_ZBUS_CHANNEL_NAME`

**提示（Prompt）**：通道名称（Channel Name）字段

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**被选择（Selected by）**

```text
CONFIG_ZBUS_PROXY_AGENT
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)、[`CONFIG_ZBUS_PROXY_AGENT`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_PROXY_AGENT)。

<a id="CONFIG_ZBUS_CHANNEL_PUBLISH_STATS"></a>

## 437.9 `CONFIG_ZBUS_CHANNEL_PUBLISH_STATS`

**提示（Prompt）**：通道发布统计信息（时间戳与计数）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_MSG_SUBSCRIBER"></a>

## 437.10 `CONFIG_ZBUS_MSG_SUBSCRIBER`

**提示（Prompt）**：消息订阅者（Message Subscriber）将按顺序接收所有消息。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**主动选择（Selects）**

```text
CONFIG_NET_BUF
```

**被选择（Selected by）**

```text
CONFIG_ZBUS_ASYNC_LISTENER
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)、[`CONFIG_NET_BUF`](P198_lib_配置项参考_2.md#CONFIG_NET_BUF)、[`CONFIG_ZBUS_ASYNC_LISTENER`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_ASYNC_LISTENER)。

<a id="CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC"></a>

## 437.11 `CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC`

**提示（Prompt）**：ZBus `msg_subscribers` 缓冲区分配

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_MSG_SUBSCRIBER && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC if CONFIG_ZBUS_PREFER_DYNAMIC_ALLOCATION
CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC
```

**可选项（Choices）**

```text
CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC
CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_MSG_SUBSCRIBER`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_MSG_SUBSCRIBER)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)、[`CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC)、[`CONFIG_ZBUS_PREFER_DYNAMIC_ALLOCATION`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_PREFER_DYNAMIC_ALLOCATION)、[`CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC)。

<a id="CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC"></a>

## 437.12 `CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC`

**提示（Prompt）**：使用堆（Heap）分配 `msg_subscriber` 缓冲区的数据

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC>
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus `msg_subscribers` 缓冲区分配

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC)。

<a id="CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC"></a>

## 437.13 `CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC`

**提示（Prompt）**：为 `msg_subscriber` 缓冲池使用固定数据大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC>
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus `msg_subscribers` 缓冲区分配

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC)。

<a id="CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION"></a>

## 437.14 `CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION`

**提示（Prompt）**：使用独立的池（Isolated Pools），而非仅使用全局池。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_MSG_SUBSCRIBER && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_MSG_SUBSCRIBER`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_MSG_SUBSCRIBER)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_SIZE"></a>

## 437.15 `CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_SIZE`

**提示（Prompt）**：可同时使用的 `net_buf` 数量。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_MSG_SUBSCRIBER && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_MSG_SUBSCRIBER`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_MSG_SUBSCRIBER)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_STATIC_DATA_SIZE"></a>

## 437.16 `CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_STATIC_DATA_SIZE`

**提示（Prompt）**：与 ZBus 配合使用的最大消息的大小。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC && CONFIG_ZBUS_MSG_SUBSCRIBER && CONFIG_ZBUS
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC)、[`CONFIG_ZBUS_MSG_SUBSCRIBER`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_MSG_SUBSCRIBER)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_OBSERVER_NAME"></a>

## 437.17 `CONFIG_ZBUS_OBSERVER_NAME`

**提示（Prompt）**：观察者名称（Observer Name）字段

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_PREFER_DYNAMIC_ALLOCATION"></a>

## 437.18 `CONFIG_ZBUS_PREFER_DYNAMIC_ALLOCATION`

**提示（Prompt）**：将 ZBus 配置为使用系统堆进行动态分配

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_PRIORITY_BOOST"></a>

## 437.19 `CONFIG_ZBUS_PRIORITY_BOOST`

**提示（Prompt）**：ZBus 优先级提升算法

**说明（Help）**

ZBus 实现最高加锁者协议（Highest Locker Protocol），依据观察者线程的优先级确定发布者的临时优先级。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_PROXY_AGENT"></a>

## 437.20 `CONFIG_ZBUS_PROXY_AGENT`

**提示（Prompt）**：ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】

**说明（Help）**

启用 ZBus 代理（Proxy Agent）支持。此功能允许 ZBus 跨多个域（Domain）工作，通过代理实现域间通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**主动选择（Selects）**

```text
CONFIG_ZBUS_CHANNEL_NAME
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)、[`CONFIG_ZBUS_CHANNEL_NAME`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_CHANNEL_NAME)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_ZBUS_PROXY_AGENT_INIT_PRIORITY"></a>

## 437.21 `CONFIG_ZBUS_PROXY_AGENT_INIT_PRIORITY`

**提示（Prompt）**：代理初始化优先级

**说明（Help）**

ZBus 代理（Proxy Agent）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_PROXY_AGENT && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
99
```

**定义位置（Location）**：[`subsys/zbus/proxy_agent/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/proxy_agent/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_PROXY_AGENT)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_PROXY_AGENT_IPC"></a>

## 437.22 `CONFIG_ZBUS_PROXY_AGENT_IPC`

**提示（Prompt）**：ZBus 代理的处理器间通信后端（IPC backend）

**说明（Help）**

启用 ZBus 代理的进程间通信（Inter-Process Communication，IPC）后端，允许各域通过 IPC 通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_PROXY_AGENT && CONFIG_ZBUS
```

**主动选择（Selects）**

```text
CONFIG_IPC_SERVICE
CONFIG_MBOX
```

**定义位置（Location）**：[`subsys/zbus/proxy_agent/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/proxy_agent/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_PROXY_AGENT)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_ZBUS_PROXY_AGENT_IPC_BIND_TIMEOUT_MS"></a>

## 437.23 `CONFIG_ZBUS_PROXY_AGENT_IPC_BIND_TIMEOUT_MS`

**提示（Prompt）**：IPC 端点绑定超时（毫秒）

**说明（Help）**

初始化期间等待远端 IPC 端点（Endpoint）完成绑定的最长时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_PROXY_AGENT_IPC && CONFIG_ZBUS_PROXY_AGENT && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`subsys/zbus/proxy_agent/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/proxy_agent/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】 → ZBus 代理的处理器间通信后端（IPC backend）

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT_IPC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_PROXY_AGENT_IPC)、[`CONFIG_ZBUS_PROXY_AGENT`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_PROXY_AGENT)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_PROXY_AGENT_MAX_CHANNEL_NAME_SIZE"></a>

## 437.24 `CONFIG_ZBUS_PROXY_AGENT_MAX_CHANNEL_NAME_SIZE`

**提示（Prompt）**：通道名称的最大长度

**说明（Help）**

ZBus 代理中通道名称的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_PROXY_AGENT && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/zbus/proxy_agent/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/proxy_agent/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_PROXY_AGENT)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_PROXY_AGENT_MAX_MESSAGE_SIZE"></a>

## 437.25 `CONFIG_ZBUS_PROXY_AGENT_MAX_MESSAGE_SIZE`

**提示（Prompt）**：消息的最大大小

**说明（Help）**

ZBus 代理中消息的最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_PROXY_AGENT && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/zbus/proxy_agent/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/proxy_agent/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_PROXY_AGENT)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_PROXY_AGENT_RX_QUEUE_DEPTH"></a>

## 437.26 `CONFIG_ZBUS_PROXY_AGENT_RX_QUEUE_DEPTH`

**提示（Prompt）**：接收队列深度（Receive Queue Depth）

**说明（Help）**

每个代理可缓冲的代理消息数量；超过此容量后，新到的消息将被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_PROXY_AGENT && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/zbus/proxy_agent/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/proxy_agent/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_PROXY_AGENT)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_PROXY_AGENT_WORK_QUEUE_PRIORITY"></a>

## 437.27 `CONFIG_ZBUS_PROXY_AGENT_WORK_QUEUE_PRIORITY`

**提示（Prompt）**：接收工作队列优先级

**说明（Help）**

ZBus 代理工作队列线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_PROXY_AGENT && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/zbus/proxy_agent/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/proxy_agent/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_PROXY_AGENT)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_PROXY_AGENT_WORK_QUEUE_STACK_SIZE"></a>

## 437.28 `CONFIG_ZBUS_PROXY_AGENT_WORK_QUEUE_STACK_SIZE`

**提示（Prompt）**：接收工作队列栈大小

**说明（Help）**

ZBus 代理工作队列线程的栈大小。此线程负责在本地发布转发来的消息。如果影子通道（Shadow Channel）使用监听器（Listener），此栈必须足够大，以容纳监听器回调的执行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_PROXY_AGENT && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/zbus/proxy_agent/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/proxy_agent/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → ZBus 代理支持（proxy agent）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_PROXY_AGENT`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_PROXY_AGENT)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<a id="CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION"></a>

## 437.29 `CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION`

**提示（Prompt）**：在运行时连接到子系统的 ZBus 通道

**说明（Help）**

除了使用 `ZBUS_CHAN_DEFINE()` 静态定义通道外，还允许在运行时创建 ZBus 通道，并通过 `zbus_runtime_channel_register()`／`zbus_runtime_channel_unregister()` 注册或注销通道。此功能适用于希望在运行时创建通道的动态加载模块，例如可链接加载扩展（Linkable Loadable Extensions，LLEXT）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**被选择（Selected by）**

```text
CONFIG_MPIPE
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_ZBUS_RUNTIME_OBSERVERS"></a>

## 437.30 `CONFIG_ZBUS_RUNTIME_OBSERVERS`

**提示（Prompt）**：运行时观察者（Runtime Observer）支持。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS
```

**被选择（Selected by）**

```text
CONFIG_MPIPE
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持

**配置项引用（Symbol References）**：[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)、[`CONFIG_MPIPE`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE)。

<a id="CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC"></a>

## 437.31 `CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC`

**提示（Prompt）**：ZBus 运行时观察者节点分配

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_RUNTIME_OBSERVERS && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC if CONFIG_ZBUS_PREFER_DYNAMIC_ALLOCATION
CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC
```

**可选项（Choices）**

```text
CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC
CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC
CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → 运行时观察者（Runtime Observer）支持。

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_RUNTIME_OBSERVERS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_RUNTIME_OBSERVERS)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)、[`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC)、[`CONFIG_ZBUS_PREFER_DYNAMIC_ALLOCATION`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_PREFER_DYNAMIC_ALLOCATION)、[`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC)、[`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE)。

<a id="CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC"></a>

## 437.32 `CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC`

**提示（Prompt）**：使用堆（Heap）分配运行时观察者节点

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC>
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → 运行时观察者（Runtime Observer）支持。 → ZBus 运行时观察者节点分配

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC)。

<a id="CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE"></a>

## 437.33 `CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE`

**提示（Prompt）**：使用用户提供的运行时观察者节点

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC>
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → 运行时观察者（Runtime Observer）支持。 → ZBus 运行时观察者节点分配

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC)。

<a id="CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC"></a>

## 437.34 `CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC`

**提示（Prompt）**：使用运行时观察者节点池（Pool）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC>
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → 运行时观察者（Runtime Observer）支持。 → ZBus 运行时观察者节点分配

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC)。

<a id="CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_POOL_SIZE"></a>

## 437.35 `CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_POOL_SIZE`

**提示（Prompt）**：运行时观察者池大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC && CONFIG_ZBUS_RUNTIME_OBSERVERS && CONFIG_ZBUS
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/zbus/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/zbus/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ZBus 消息总线支持 → 运行时观察者（Runtime Observer）支持。

**配置项引用（Symbol References）**：[`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC)、[`CONFIG_ZBUS_RUNTIME_OBSERVERS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS_RUNTIME_OBSERVERS)、[`CONFIG_ZBUS`](P437_subsys_zbus_配置项参考.md#CONFIG_ZBUS)。

<!-- kconfig-navigation -->

[上一章](P436_subsys_video_配置项参考.md) · [返回大纲](大纲.md)
