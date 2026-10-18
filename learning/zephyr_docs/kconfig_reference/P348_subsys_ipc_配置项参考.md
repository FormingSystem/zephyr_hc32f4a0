---
id: learning.zephyr-docs.kconfig-reference.page-348
title: "`subsys/ipc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第348章\_`subsys/ipc`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/ipc` 的 61 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_IPC_SERVICE"></a>

## 348.1 `CONFIG_IPC_SERVICE`

**提示（Prompt）**：支持多个后端的处理器间通信服务（IPC service）

**说明（Help）**

启用可由多个用户共享、支持不同后端（backends）的服务。应用开始使用处理器间通信服务（IPC Service）之前，应先注册后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_NRF_802154_SERIALIZATION
CONFIG_NRF_802154_SERIALIZATION
CONFIG_SOC_FAMILY_INTEL_ADSP
CONFIG_BT_HCI_IPC
CONFIG_ZBUS_PROXY_AGENT_IPC
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_SERIALIZATION`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_BT_HCI_IPC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_IPC)、[`CONFIG_ZBUS_PROXY_AGENT_IPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_PROXY_AGENT_IPC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICBMSG"></a>

## 348.2 `CONFIG_IPC_SERVICE_BACKEND_ICBMSG`

**提示（Prompt）**：使用动态分配缓冲区的 ICMSG 后端（backend）

**说明（Help）**

选择此后端将使用基于动态分配缓冲区的多端点实现（multi endpoint implementation），缓冲区引用通过 ICMsg 环形缓冲区（circular buffer）传递。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX && DT_HAS_ZEPHYR_IPC_ICBMSG_ENABLED && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SYS_HASH_FUNC32
CONFIG_SYS_HASH_FUNC32_DJB2
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.icbmsg:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.icbmsg#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_SYS_HASH_FUNC32`](P198_lib_配置项参考_2.md#CONFIG_SYS_HASH_FUNC32)、[`CONFIG_SYS_HASH_FUNC32_DJB2`](P198_lib_配置项参考_2.md#CONFIG_SYS_HASH_FUNC32_DJB2)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICBMSG_DEINIT"></a>

## 348.3 `CONFIG_IPC_SERVICE_BACKEND_ICBMSG_DEINIT`

**提示（Prompt）**：支持关闭和注销端点（endpoints）

**说明（Help）**

启用端点（endpoints）的关闭和注销支持。默认禁用，以减小代码大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_ICBMSG && CONFIG_IPC_SERVICE
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.icbmsg:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.icbmsg#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 使用动态分配缓冲区的 ICMSG 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICBMSG_MAX_ACTIVE_COUNT"></a>

## 348.4 `CONFIG_IPC_SERVICE_BACKEND_ICBMSG_MAX_ACTIVE_COUNT`

**提示（Prompt）**：活动缓冲区数量上限（active buffers）

**说明（Help）**

消息队列（message queues）中同时处于活动状态的缓冲区数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_ICBMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[16, 32]
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.icbmsg:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.icbmsg#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 使用动态分配缓冲区的 ICMSG 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICBMSG_NUM_EP"></a>

## 348.5 `CONFIG_IPC_SERVICE_BACKEND_ICBMSG_NUM_EP`

**提示（Prompt）**：端点数量（Endpoints count）

**说明（Help）**

ICBMsg 处理器间通信（IPC）服务后端支持的端点数量。该值适用于所有实例，因此应设为各实例所需数量中的最大值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_ICBMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 254]
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.icbmsg:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.icbmsg#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 使用动态分配缓冲区的 ICMSG 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICBMSG_SHELL"></a>

## 348.6 `CONFIG_IPC_SERVICE_BACKEND_ICBMSG_SHELL`

**提示（Prompt）**：ICBMsg 命令行命令（shell commands）

**说明（Help）**

为 ICBMsg IPC 后端启用命令行命令（shell commands）。启用后，`icbmsg stats` 命令以便于阅读的格式打印 IPC 统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_IPC_SERVICE_BACKEND_ICBMSG && CONFIG_IPC_SERVICE
```

**主动选择（Selects）**

```text
CONFIG_STATS
CONFIG_STATS_NAMES
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.icbmsg:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.icbmsg#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 使用动态分配缓冲区的 ICMSG 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_IPC_SERVICE_BACKEND_ICBMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICBMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS)、[`CONFIG_STATS_NAMES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS_NAMES)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICMSG"></a>

## 348.7 `CONFIG_IPC_SERVICE_BACKEND_ICMSG`

**提示（Prompt）**：使用单生产者单消费者（SPSC）数据包缓冲区的 ICMSG 后端

**说明（Help）**

选择此后端将使用基于环形数据包缓冲区（circular packet buffer）的单端点实现（single endpoint implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX && DT_HAS_ZEPHYR_IPC_ICMSG_ENABLED && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_IPC_SERVICE_ICMSG
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_IPC_SERVICE_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_EP_NAME_LEN"></a>

## 348.8 `CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_EP_NAME_LEN`

**提示（Prompt）**：端点名称长度（Endpoint name length）

**说明（Help）**

发起方（initiator）与跟随方（follower）之间用于发现端点的字符串最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR || CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER) && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 252]
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.icmsg_me:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.icmsg_me#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR)、[`CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER"></a>

## 348.9 `CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER`

**提示（Prompt）**：支持跟随方角色（follower role）多端点的 ICMSG 后端

**说明（Help）**

选择此后端将使用基于环形数据包缓冲区（circular packet buffer）的多端点实现，并启用端点发现的跟随方角色（follower role）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX && DT_HAS_ZEPHYR_IPC_ICMSG_ME_FOLLOWER_ENABLED && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_IPC_SERVICE_ICMSG_ME
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_IPC_SERVICE_ICMSG_ME`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG_ME)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR"></a>

## 348.10 `CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR`

**提示（Prompt）**：支持发起方角色（initiator role）多端点的 ICMSG 后端

**说明（Help）**

选择此后端将使用基于环形数据包缓冲区（circular packet buffer）的多端点实现，并启用端点发现的发起方角色（initiator role）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX && DT_HAS_ZEPHYR_IPC_ICMSG_ME_INITIATOR_ENABLED && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_IPC_SERVICE_ICMSG_ME
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_IPC_SERVICE_ICMSG_ME`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG_ME)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_NUM_EP"></a>

## 348.11 `CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_NUM_EP`

**提示（Prompt）**：端点数量（Endpoints number）

**说明（Help）**

多端点 ICMSG 库支持的端点（endpoints）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR || CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER) && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 254]
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.icmsg_me:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.icmsg_me#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR)、[`CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_SEND_BUF_SIZE"></a>

## 348.12 `CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_SEND_BUF_SIZE`

**提示（Prompt）**：发送缓冲区大小（sending buffer size）

**说明（Help）**

发送函数中用于准备待发送数据的静态缓冲区大小。若确定应用发送的数据绝不超过某一大小，可以安全调整此值，以减少应用的 RAM 占用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR || CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER) && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.icmsg_me:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.icmsg_me#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR)、[`CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICMSG_WQ_ENABLE"></a>

## 348.13 `CONFIG_IPC_SERVICE_BACKEND_ICMSG_WQ_ENABLE`

**提示（Prompt）**：使用专用工作队列（dedicated workqueue）

**说明（Help）**

为 ICMsg 后端启用专用工作队列线程（workqueue thread）。禁用后，ICMsg 后端在系统工作队列上下文中处理接收数据，可减少后端的 RAM 占用，但某些使用场景可能发生死锁（deadlock），例如在系统工作队列上下文中执行同步 IPC。

后端发出的回调在工作队列上下文中执行。禁用本项时，用户必须遵守系统工作队列的限制，例如绝不能在回调中执行阻塞操作（blocking operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_IPC_SERVICE_ICMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig.icmsg:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig.icmsg#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → icmsg 处理器间通信库（IPC library）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_IPC_SERVICE_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICMSG_WQ_PRIORITY"></a>

## 348.14 `CONFIG_IPC_SERVICE_BACKEND_ICMSG_WQ_PRIORITY`

**提示（Prompt）**：接收工作队列线程优先级（RX work queue thread priority）

**说明（Help）**

ICMSG 接收工作队列线程的优先级。为保持实现简单，ICMSG 库要求此工作队列以协作式优先级（cooperative priority）执行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_ICMSG_WQ_ENABLE && CONFIG_IPC_SERVICE_ICMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
-1
```

**取值范围（Ranges）**

```text
[-256, -1]
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig.icmsg:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig.icmsg#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → icmsg 处理器间通信库（IPC library） → 使用专用工作队列（dedicated workqueue）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICMSG_WQ_ENABLE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICMSG_WQ_ENABLE)、[`CONFIG_IPC_SERVICE_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_ICMSG_WQ_STACK_SIZE"></a>

## 348.15 `CONFIG_IPC_SERVICE_BACKEND_ICMSG_WQ_STACK_SIZE`

**提示（Prompt）**：接收工作队列栈大小（RX work queue stack size）

**说明（Help）**

接收工作队列线程使用的栈大小。创建此工作队列是为了避免在系统工作队列中向服务用户通知收到的数据。该队列由各实例共享。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_ICMSG_WQ_ENABLE && CONFIG_IPC_SERVICE_ICMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
1280
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig.icmsg:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig.icmsg#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → icmsg 处理器间通信库（IPC library） → 使用专用工作队列（dedicated workqueue）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_ICMSG_WQ_ENABLE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICMSG_WQ_ENABLE)、[`CONFIG_IPC_SERVICE_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_INTEL_ADSP_HOST_IPC"></a>

## 348.16 `CONFIG_IPC_SERVICE_BACKEND_INTEL_ADSP_HOST_IPC`

**提示（Prompt）**：Intel 音频 DSP 主机 IPC 后端（Audio DSP Host IPC backend）

**说明（Help）**

用于 Intel 音频 DSP 主机 IPC 的处理器间通信服务后端（IPC Service Backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
DT_HAS_INTEL_ADSP_HOST_IPC_ENABLED
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.intel_adsp:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.intel_adsp#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_RPMSG"></a>

## 348.17 `CONFIG_IPC_SERVICE_BACKEND_RPMSG`

**提示（Prompt）**：使用静态虚拟环（VRINGs）的 OpenAMP RPMSG 后端

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX && DT_HAS_ZEPHYR_IPC_OPENAMP_STATIC_VRINGS_ENABLED && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_IPC_SERVICE_RPMSG
CONFIG_IPC_SERVICE_STATIC_VRINGS
CONFIG_OPENAMP
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_IPC_SERVICE_RPMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_RPMSG)、[`CONFIG_IPC_SERVICE_STATIC_VRINGS`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_STATIC_VRINGS)、[`CONFIG_OPENAMP`](P208_modules_Kconfig.open-amp_配置项参考.md#CONFIG_OPENAMP)。

<a id="CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE"></a>

## 348.18 `CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE`

**提示（Prompt）**：RPMSG-Lite 后端（backend）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX && DT_HAS_NXP_IPC_RPMSG_LITE_ENABLED && CONFIG_ZEPHYR_HAL_NXP_MODULE && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RPMSGLITE
CONFIG_RPMSGLITE_NS
CONFIG_EVENTS
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_ZEPHYR_HAL_NXP_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_NXP_MODULE)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)、[`CONFIG_RPMSGLITE_NS`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE_NS)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_NXP_MODULE`。

<a id="CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_LINK_UP_TIMEOUT_MS"></a>

## 348.19 `CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_LINK_UP_TIMEOUT_MS`

**提示（Prompt）**：远程角色的链路建立超时（Link-up timeout，毫秒）

**说明（Help）**

实例角色为远程端（remote）时，传给 `rpmsg_lite_wait_for_link_up()` 的超时时间。若主机核心一直未启动，可防止 `ipc_service_open_instance()` 永久阻塞。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.rpmsg-lite:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.rpmsg-lite#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_DIRECT"></a>

## 348.20 `CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_DIRECT`

**提示（Prompt）**：直接通知（Direct notification，较低延迟）

**说明（Help）**

仅保存最新通知，不排队。这可将延迟和 RAM 占用降至最低，但如果工作处理函数运行前发生多次邮箱（MBOX）中断，就可能丢失通知。

优点：

- 尽可能低的延迟。
- 极少的 RAM 占用，4 字节，对比队列方案的 44 字节。
- 更简单的代码执行路径。

缺点：

- 高负载下通知丢失更多。
- 仅保留最新通知。
- 多个信号可能合并为一个。

建议用于流量较低至中等、对延迟敏感且可接受偶尔丢失通知的场景。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_MODE>
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.rpmsg-lite:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.rpmsg-lite#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 邮箱（MBOX）通知处理模式

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_MODE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_MODE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_MODE"></a>

## 348.21 `CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_MODE`

**提示（Prompt）**：邮箱（MBOX）通知处理模式

**说明（Help）**

选择邮箱（MBOX）通知的处理方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_DIRECT
```

**可选项（Choices）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_QUEUE
CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_DIRECT
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.rpmsg-lite:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.rpmsg-lite#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_DIRECT`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_DIRECT)、[`CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_QUEUE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_QUEUE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_QUEUE"></a>

## 348.22 `CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_QUEUE`

**提示（Prompt）**：基于队列的通知（Queue-based notification，更可靠）

**说明（Help）**

使用消息队列（message queue）缓冲到达的邮箱（MBOX）通知，最多排队保存 4 个待处理信号，可显著降低高消息速率下丢失通知的风险。

优点：

- 大幅减少通知丢失，但不能完全消除。
- 更好地处理突发流量（burst traffic）。
- 负载下行为更可预测。

缺点：

- 延迟略高，约增加 5%～15%。
- 每个 IPC 实例额外占用 40 字节 RAM。
- 额外的 `k_msgq` 开销。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_MODE>
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.rpmsg-lite:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.rpmsg-lite#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 邮箱（MBOX）通知处理模式

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_MODE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NOTIFY_MODE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NUM_ENDPOINTS_PER_INSTANCE"></a>

## 348.23 `CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_NUM_ENDPOINTS_PER_INSTANCE`

**提示（Prompt）**：每个实例注册端点数量上限

**说明（Help）**

RPMSG-Lite 后端的单个实例最多可注册的端点（endpoints）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.rpmsg-lite:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.rpmsg-lite#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_WQ_STACK_SIZE"></a>

## 348.24 `CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE_WQ_STACK_SIZE`

**提示（Prompt）**：接收工作队列栈大小（RX work queue stack size）

**说明（Help）**

接收工作队列线程所用的栈大小。多实例／多核心 RPMSG-Lite 后端模块创建此队列，以免从系统工作队列向服务用户通知收到的数据。所有实例使用相同的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.rpmsg-lite:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.rpmsg-lite#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_RPMSG_NUM_ENDPOINTS_PER_INSTANCE"></a>

## 348.25 `CONFIG_IPC_SERVICE_BACKEND_RPMSG_NUM_ENDPOINTS_PER_INSTANCE`

**提示（Prompt）**：每个实例注册端点数量上限

**说明（Help）**

RPMSG 后端的单个实例最多可注册的端点（endpoints）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.rpmsg:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.rpmsg#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_RPMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_RPMSG_SHMEM_INIT_PRIORITY"></a>

## 348.26 `CONFIG_IPC_SERVICE_BACKEND_RPMSG_SHMEM_INIT_PRIORITY`

**提示（Prompt）**：共享内存重置的初始化优先级（init priority）

**说明（Help）**

RPMsg 静态虚拟环（static vrings）后端执行共享内存重置时的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG_SHMEM_RESET && CONFIG_IPC_SERVICE_BACKEND_RPMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.rpmsg:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.rpmsg#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 重置共享内存状态（Reset shared memory state）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_RPMSG_SHMEM_RESET`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG_SHMEM_RESET)、[`CONFIG_IPC_SERVICE_BACKEND_RPMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_RPMSG_SHMEM_RESET"></a>

## 348.27 `CONFIG_IPC_SERVICE_BACKEND_RPMSG_SHMEM_RESET`

**提示（Prompt）**：重置共享内存状态（Reset shared memory state）

**说明（Help）**

某些平台在复位（reset）后保留内存内容，但后端需要已清零的内存，才能在初始化时正确建立实例和端点，这会造成问题。将本参数设为 `y` 后，会在内核初始化时重置共享内存的状态区域（status region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG && CONFIG_IPC_SERVICE
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.rpmsg:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.rpmsg#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_RPMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_BACKEND_RPMSG_WQ_STACK_SIZE"></a>

## 348.28 `CONFIG_IPC_SERVICE_BACKEND_RPMSG_WQ_STACK_SIZE`

**提示（Prompt）**：接收工作队列栈大小（RX work queue stack size）

**说明（Help）**

接收工作队列线程使用的栈大小。多实例／多核心 RPMsg 后端模块创建此队列，以免从系统工作队列向服务用户通知收到的数据。所有实例使用相同的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig.rpmsg:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig.rpmsg#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_RPMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_ICMSG"></a>

## 348.29 `CONFIG_IPC_SERVICE_ICMSG`

**提示（Prompt）**：icmsg 处理器间通信库（IPC library）

**说明（Help）**

Icmsg 库（library）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE
```

**主动选择（Selects）**

```text
CONFIG_PBUF
```

**被选择（Selected by）**

```text
CONFIG_IPC_SERVICE_BACKEND_ICMSG
CONFIG_IPC_SERVICE_ICMSG_ME
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_PBUF`](P348_subsys_ipc_配置项参考.md#CONFIG_PBUF)、[`CONFIG_IPC_SERVICE_BACKEND_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICMSG)、[`CONFIG_IPC_SERVICE_ICMSG_ME`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG_ME)。

<a id="CONFIG_IPC_SERVICE_ICMSG_ME"></a>

## 348.30 `CONFIG_IPC_SERVICE_ICMSG_ME`

**提示（Prompt）**：具备多端点功能（multi-endpoint functionality）的 icmsg IPC 库

**说明（Help）**

icmsg 库的多端点功能（Multi-endpoint functionality）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE
```

**主动选择（Selects）**

```text
CONFIG_IPC_SERVICE_ICMSG
CONFIG_EVENTS
```

**被选择（Selected by）**

```text
CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR
CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_IPC_SERVICE_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_INITIATOR)、[`CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_FOLLOWER)。

<a id="CONFIG_IPC_SERVICE_ICMSG_SHMEM_ACCESS_SYNC"></a>

## 348.31 `CONFIG_IPC_SERVICE_ICMSG_SHMEM_ACCESS_SYNC`

**提示（Prompt）**：同步共享内存访问（Synchronize access）

**说明（Help）**

在库级别提供共享内存同步访问。默认启用，以便从多个上下文（contexts）使用发送 API；使用互斥锁（mutex）保护内存访问。若应用保证只从单一上下文发送数据，则可安全禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_IPC_SERVICE_ICMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig.icmsg:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig.icmsg#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → icmsg 处理器间通信库（IPC library）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_IPC_SERVICE_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_ICMSG_SHMEM_ACCESS_TO_MS"></a>

## 348.32 `CONFIG_IPC_SERVICE_ICMSG_SHMEM_ACCESS_TO_MS`

**提示（Prompt）**：互斥锁加锁超时（Mutex lock timeout，毫秒）

**说明（Help）**

使用基于 icmsg 库的后端发送数据时，为获得访问权而等待的最长时间，单位为毫秒。此值应相对较小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_ICMSG_SHMEM_ACCESS_SYNC && CONFIG_IPC_SERVICE_ICMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig.icmsg:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig.icmsg#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → icmsg 处理器间通信库（IPC library） → 同步共享内存访问（Synchronize access）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_ICMSG_SHMEM_ACCESS_SYNC`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG_SHMEM_ACCESS_SYNC)、[`CONFIG_IPC_SERVICE_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_ICMSG_UNBOUND_DETECT_ALLOWED"></a>

## 348.33 `CONFIG_IPC_SERVICE_ICMSG_UNBOUND_DETECT_ALLOWED`

**提示（Prompt）**：允许实例将 unbound 设为 detect

**说明（Help）**

控制是否允许任意 ICMsg 实例将 `unbound` 属性设为 `detect`。原文指出，如果希望减小代码大小，且所有 ICMsg 实例都使用解绑检测功能（unbound detection functionality），可以将此选项设为 `n`。

译注：原文同时写了“允许 detect”以及“全部使用检测时可以禁用”，两者表述存在疑点；这里保留两项原意，具体裁剪条件应核对对应源码，不能仅据此句推断运行行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_ICMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig.icmsg:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig.icmsg#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → icmsg 处理器间通信库（IPC library）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_ICMSG_UNBOUND_DISABLED_ALLOWED"></a>

## 348.34 `CONFIG_IPC_SERVICE_ICMSG_UNBOUND_DISABLED_ALLOWED`

**提示（Prompt）**：允许实例将 unbound 设为 disabled

**说明（Help）**

控制是否允许任意 ICMsg 实例将 `unbound` 属性设为 `disabled`。若希望减小代码大小，且所有 ICMsg 实例都使用解绑功能（unbound functionality），可以将此选项设为 `n`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_ICMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig.icmsg:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig.icmsg#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → icmsg 处理器间通信库（IPC library）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_ICMSG_UNBOUND_ENABLED_ALLOWED"></a>

## 348.35 `CONFIG_IPC_SERVICE_ICMSG_UNBOUND_ENABLED_ALLOWED`

**提示（Prompt）**：允许实例将 unbound 设为 enabled

**说明（Help）**

控制是否允许任意 ICMsg 实例将 `unbound` 属性设为 `enabled`。若希望减小代码大小，且没有任何 ICMsg 实例使用解绑功能（unbound functionality），可以将此选项设为 `n`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_ICMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig.icmsg:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig.icmsg#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → icmsg 处理器间通信库（IPC library）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_REG_BACKEND_PRIORITY"></a>

## 348.36 `CONFIG_IPC_SERVICE_REG_BACKEND_PRIORITY`

**提示（Prompt）**：注册 IPC 后端的模块初始化优先级（initialization priority）

**说明（Help）**

后端（backend）必须在端点（endpoint）注册之前完成注册。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
46
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/backends/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/backends/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_IPC_SERVICE_RPMSG"></a>

## 348.37 `CONFIG_IPC_SERVICE_RPMSG`

**提示（Prompt）**：RPMsg 支持库（support library）

**说明（Help）**

RPMsg 库（library）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE
```

**被选择（Selected by）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_IPC_SERVICE_BACKEND_RPMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG)。

<a id="CONFIG_IPC_SERVICE_STATIC_VRINGS"></a>

## 348.38 `CONFIG_IPC_SERVICE_STATIC_VRINGS`

**提示（Prompt）**：静态虚拟环（Static VRINGs）支持库

**说明（Help）**

静态虚拟环库（Static VRINGs library）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE
```

**被选择（Selected by）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_IPC_SERVICE_BACKEND_RPMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_BACKEND_RPMSG)。

<a id="CONFIG_IPC_SERVICE_STATIC_VRINGS_MEM_ALIGNMENT"></a>

## 348.39 `CONFIG_IPC_SERVICE_STATIC_VRINGS_MEM_ALIGNMENT`

**提示（Prompt）**：虚拟环对齐（VRINGs alignment）

**说明（Help）**

静态虚拟环（Static VRINGs）的对齐要求。若启用缓存（cache），应考虑缓存行对齐（cache line alignment）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_STATIC_VRINGS && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → 静态虚拟环（Static VRINGs）支持库

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_STATIC_VRINGS`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_STATIC_VRINGS)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_OPENAMP_COPY_RSC_TABLE"></a>

## 348.40 `CONFIG_OPENAMP_COPY_RSC_TABLE`

**提示（Prompt）**：复制资源表段（resource table section）

**说明（Help）**

`.resource_table` 段必须放置在本核心和远程核心均已知的特定位置。若远程端未负责安排此位置，本固件可以将资源表复制到指定位置。可通过设备树中的 `zephyr,ipc_rsc_table` 节点声明该内存区域。若远程端加载本固件并控制 `.resource_table` 段的位置，例如 remoteproc，则不需要此操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP_RSC_TABLE
```

**定义位置（Location）**：[`subsys/ipc/open-amp/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/open-amp/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 协处理器资源表（coprocessor resource table）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP_RSC_TABLE`](P348_subsys_ipc_配置项参考.md#CONFIG_OPENAMP_RSC_TABLE)。

<a id="CONFIG_OPENAMP_RSC_TABLE"></a>

## 348.41 `CONFIG_OPENAMP_RSC_TABLE`

**提示（Prompt）**：协处理器资源表（coprocessor resource table）

**说明（Help）**

在生成的二进制文件中加入资源表（resource table）。该表兼容 Linux 远程处理器框架（remoteproc framework）和 OpenAMP 库。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_STM32MP1X
```

**弱选择（Implies）**

```text
CONFIG_OPENAMP
```

**定义位置（Location）**：[`subsys/ipc/open-amp/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/open-amp/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32MP1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP1X)、[`CONFIG_OPENAMP`](P208_modules_Kconfig.open-amp_配置项参考.md#CONFIG_OPENAMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32MP1X`。

<a id="CONFIG_OPENAMP_RSC_TABLE_IPM_RX_ID"></a>

## 348.42 `CONFIG_OPENAMP_RSC_TABLE_IPM_RX_ID`

**提示（Prompt）**：处理器间邮箱接收通道标识（IPM RX channel ID）

**说明（Help）**

指定虚拟环（VRING）用于处理器间通信的 IPM 接收（RX）通道 ID。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP_RSC_TABLE
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/ipc/open-amp/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/open-amp/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 协处理器资源表（coprocessor resource table）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP_RSC_TABLE`](P348_subsys_ipc_配置项参考.md#CONFIG_OPENAMP_RSC_TABLE)。

<a id="CONFIG_OPENAMP_RSC_TABLE_IPM_TX_ID"></a>

## 348.43 `CONFIG_OPENAMP_RSC_TABLE_IPM_TX_ID`

**提示（Prompt）**：处理器间邮箱发送通道标识（IPM TX channel ID）

**说明（Help）**

指定虚拟环（VRING）用于处理器间通信的 IPM 发送（TX）通道 ID。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP_RSC_TABLE
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/ipc/open-amp/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/open-amp/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 协处理器资源表（coprocessor resource table）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP_RSC_TABLE`](P348_subsys_ipc_配置项参考.md#CONFIG_OPENAMP_RSC_TABLE)。

<a id="CONFIG_OPENAMP_RSC_TABLE_NUM_RPMSG_BUFF"></a>

## 348.44 `CONFIG_OPENAMP_RSC_TABLE_NUM_RPMSG_BUFF`

**提示（Prompt）**：资源表中的 RPMsg 缓冲区数量

**说明（Help）**

指定虚拟环（Vring）用于处理器间通信的缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP_RSC_TABLE
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/ipc/open-amp/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/open-amp/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 协处理器资源表（coprocessor resource table）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP_RSC_TABLE`](P348_subsys_ipc_配置项参考.md#CONFIG_OPENAMP_RSC_TABLE)。

<a id="CONFIG_OPENAMP_VENDOR_ADDR_TRANSLATION"></a>

## 348.45 `CONFIG_OPENAMP_VENDOR_ADDR_TRANSLATION`

**提示（Prompt）**：OpenAMP 地址转换支持（Address translation）

**说明（Help）**

启用从远程驱动到设备的地址转换（address translation）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP_RSC_TABLE
```

**定义位置（Location）**：[`subsys/ipc/open-amp/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/open-amp/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 协处理器资源表（coprocessor resource table）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP_RSC_TABLE`](P348_subsys_ipc_配置项参考.md#CONFIG_OPENAMP_RSC_TABLE)。

<a id="CONFIG_OPENAMP_VENDOR_ADDR_TRANSLATION_FILE"></a>

## 348.46 `CONFIG_OPENAMP_VENDOR_ADDR_TRANSLATION_FILE`

**提示（Prompt）**：包含厂商专用地址转换表的头文件

**说明（Help）**

包含厂商专用地址转换表（vendor-specific address translation table）的头文件名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP_VENDOR_ADDR_TRANSLATION && CONFIG_OPENAMP_RSC_TABLE
```

**默认值（Defaults）**

```text
"addr_translation.h"
```

**定义位置（Location）**：[`subsys/ipc/open-amp/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/open-amp/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 协处理器资源表（coprocessor resource table） → OpenAMP 地址转换支持（Address translation）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP_VENDOR_ADDR_TRANSLATION`](P348_subsys_ipc_配置项参考.md#CONFIG_OPENAMP_VENDOR_ADDR_TRANSLATION)、[`CONFIG_OPENAMP_RSC_TABLE`](P348_subsys_ipc_配置项参考.md#CONFIG_OPENAMP_RSC_TABLE)。

<a id="CONFIG_OPENAMP_VENDOR_RSC_TABLE"></a>

## 348.47 `CONFIG_OPENAMP_VENDOR_RSC_TABLE`

**提示（Prompt）**：厂商专用资源表（Vendor specific resource table）

**说明（Help）**

启用厂商专用资源表（vendor-specific resource table），包含远程处理器支持的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP_RSC_TABLE
```

**定义位置（Location）**：[`subsys/ipc/open-amp/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/open-amp/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 协处理器资源表（coprocessor resource table）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP_RSC_TABLE`](P348_subsys_ipc_配置项参考.md#CONFIG_OPENAMP_RSC_TABLE)。

<a id="CONFIG_OPENAMP_VENDOR_RSC_TABLE_FILE"></a>

## 348.48 `CONFIG_OPENAMP_VENDOR_RSC_TABLE_FILE`

**提示（Prompt）**：包含厂商专用资源表的源文件

**说明（Help）**

包含厂商专用资源表（vendor-specific resource table）的源文件名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP_VENDOR_RSC_TABLE && CONFIG_OPENAMP_RSC_TABLE
```

**默认值（Defaults）**

```text
"resource_table.c"
```

**定义位置（Location）**：[`subsys/ipc/open-amp/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/open-amp/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 协处理器资源表（coprocessor resource table） → 厂商专用资源表（Vendor specific resource table）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP_VENDOR_RSC_TABLE`](P348_subsys_ipc_配置项参考.md#CONFIG_OPENAMP_VENDOR_RSC_TABLE)、[`CONFIG_OPENAMP_RSC_TABLE`](P348_subsys_ipc_配置项参考.md#CONFIG_OPENAMP_RSC_TABLE)。

<a id="CONFIG_OPENAMP_VRING_ALIGNMENT"></a>

## 348.49 `CONFIG_OPENAMP_VRING_ALIGNMENT`

**提示（Prompt）**：IPM 虚拟环对齐（VRing Alignment）

**说明（Help）**

资源表中虚拟环（vring）的可用部分（avail）与已用部分（used）之间使用的对齐值。应为正的 2 的幂；平台的缓存行或共享内存约束有要求时，应增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP_RSC_TABLE
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/ipc/open-amp/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/open-amp/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 协处理器资源表（coprocessor resource table）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP_RSC_TABLE`](P348_subsys_ipc_配置项参考.md#CONFIG_OPENAMP_RSC_TABLE)。

<a id="CONFIG_PBUF"></a>

## 348.50 `CONFIG_PBUF`

**提示（Prompt）**：打包缓冲区支持库（原文：Packed buffer support library）

**说明（Help）**

数据包缓冲区（packet buffer）在读写方共享的内存区域上实现轻量级单向数据包缓冲，具有读／写语义。可按需集成缓存（cache）和内存屏障（memory barrier）管理，以确保正确访问数据。译注：标题用 “Packed”，正文用 “packet”，这里保留该差别并按正文说明功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE_ICMSG && CONFIG_IPC_SERVICE
```

**被选择（Selected by）**

```text
CONFIG_IPC_SERVICE_ICMSG
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig.icmsg:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig.icmsg#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → icmsg 处理器间通信库（IPC library）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_PBUF_RX_READ_BUF_SIZE"></a>

## 348.51 `CONFIG_PBUF_RX_READ_BUF_SIZE`

**提示（Prompt）**：PBUF 读取缓冲区大小（字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PBUF && CONFIG_IPC_SERVICE_ICMSG && CONFIG_IPC_SERVICE
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/ipc/ipc_service/lib/Kconfig.icmsg:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/ipc_service/lib/Kconfig.icmsg#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 支持多个后端的处理器间通信服务（IPC service） → icmsg 处理器间通信库（IPC library） → 打包缓冲区支持库（原文：Packed buffer support library）

**配置项引用（Symbol References）**：[`CONFIG_PBUF`](P348_subsys_ipc_配置项参考.md#CONFIG_PBUF)、[`CONFIG_IPC_SERVICE_ICMSG`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE_ICMSG)、[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)。

<a id="CONFIG_RPMSG_SERVICE"></a>

## 348.52 `CONFIG_RPMSG_SERVICE`

**提示（Prompt）**：供多个用户使用的 RPMsg 服务（service）

**说明（Help）**

启用可由多个用户共享的服务，为指定通道（channel）建立 RPMsg 端点（endpoints）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_IPM
CONFIG_OPENAMP
```

**定义位置（Location）**：[`subsys/ipc/rpmsg_service/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/rpmsg_service/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication）

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_OPENAMP`](P208_modules_Kconfig.open-amp_配置项参考.md#CONFIG_OPENAMP)。

<a id="CONFIG_RPMSG_SERVICE_DUAL_IPM_SUPPORT"></a>

## 348.53 `CONFIG_RPMSG_SERVICE_DUAL_IPM_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

发送（TX）与接收（RX）通信使用独立的处理器间邮箱（IPM）时，必须选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
n && n
```

**定义位置（Location）**：[`subsys/ipc/rpmsg_service/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/rpmsg_service/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication）

<a id="CONFIG_RPMSG_SERVICE_EP_REG_PRIORITY"></a>

## 348.54 `CONFIG_RPMSG_SERVICE_EP_REG_PRIORITY`

**提示（Prompt）**：注册 RPMsg 端点的模块初始化优先级

**说明（Help）**

必须在 RPMsg 服务初始化之前注册端点（endpoints）。不确定时，不要修改此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSG_SERVICE
```

**默认值（Defaults）**

```text
47
```

**定义位置（Location）**：[`subsys/ipc/rpmsg_service/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/rpmsg_service/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_RPMSG_SERVICE)。

<a id="CONFIG_RPMSG_SERVICE_INIT_PRIORITY"></a>

## 348.55 `CONFIG_RPMSG_SERVICE_INIT_PRIORITY`

**提示（Prompt）**：RPMsg 服务初始化优先级（initialization priority）

**说明（Help）**

RPMsg 服务初始化与端点注册的顺序非常重要，用于避免端点握手（handshake）过程中的竞态条件（race conditions）。不确定时，不要修改此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSG_SERVICE
```

**默认值（Defaults）**

```text
48
```

**定义位置（Location）**：[`subsys/ipc/rpmsg_service/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/rpmsg_service/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_RPMSG_SERVICE)。

<a id="CONFIG_RPMSG_SERVICE_MODE"></a>

## 348.56 `CONFIG_RPMSG_SERVICE_MODE`

**提示（Prompt）**：RPMsg 服务模式（Service mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSG_SERVICE
```

**可选项（Choices）**

```text
CONFIG_RPMSG_SERVICE_MODE_MASTER
CONFIG_RPMSG_SERVICE_MODE_REMOTE
```

**定义位置（Location）**：[`subsys/ipc/rpmsg_service/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/rpmsg_service/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_RPMSG_SERVICE)、[`CONFIG_RPMSG_SERVICE_MODE_MASTER`](P348_subsys_ipc_配置项参考.md#CONFIG_RPMSG_SERVICE_MODE_MASTER)、[`CONFIG_RPMSG_SERVICE_MODE_REMOTE`](P348_subsys_ipc_配置项参考.md#CONFIG_RPMSG_SERVICE_MODE_REMOTE)。

<a id="CONFIG_RPMSG_SERVICE_MODE_MASTER"></a>

## 348.57 `CONFIG_RPMSG_SERVICE_MODE_MASTER`

**提示（Prompt）**：RPMsg 主端（master）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RPMSG_SERVICE_MODE>
```

**主动选择（Selects）**

```text
CONFIG_OPENAMP_MASTER
```

**定义位置（Location）**：[`subsys/ipc/rpmsg_service/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/rpmsg_service/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service） → RPMsg 服务模式（Service mode）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE_MODE`](P348_subsys_ipc_配置项参考.md#CONFIG_RPMSG_SERVICE_MODE)、[`CONFIG_OPENAMP_MASTER`](P208_modules_Kconfig.open-amp_配置项参考.md#CONFIG_OPENAMP_MASTER)。

<a id="CONFIG_RPMSG_SERVICE_MODE_REMOTE"></a>

## 348.58 `CONFIG_RPMSG_SERVICE_MODE_REMOTE`

**提示（Prompt）**：RPMsg 远程端（remote）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RPMSG_SERVICE_MODE>
```

**主动选择（Selects）**

```text
CONFIG_OPENAMP_SLAVE
```

**定义位置（Location）**：[`subsys/ipc/rpmsg_service/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/rpmsg_service/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service） → RPMsg 服务模式（Service mode）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE_MODE`](P348_subsys_ipc_配置项参考.md#CONFIG_RPMSG_SERVICE_MODE)、[`CONFIG_OPENAMP_SLAVE`](P208_modules_Kconfig.open-amp_配置项参考.md#CONFIG_OPENAMP_SLAVE)。

<a id="CONFIG_RPMSG_SERVICE_NUM_ENDPOINTS"></a>

## 348.59 `CONFIG_RPMSG_SERVICE_NUM_ENDPOINTS`

**提示（Prompt）**：已注册端点数量上限（registered endpoints）

**说明（Help）**

指定 RPMsg 服务可注册的端点（endpoints）数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSG_SERVICE
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/ipc/rpmsg_service/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/rpmsg_service/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_RPMSG_SERVICE)。

<a id="CONFIG_RPMSG_SERVICE_SINGLE_IPM_SUPPORT"></a>

## 348.60 `CONFIG_RPMSG_SERVICE_SINGLE_IPM_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

发送（TX）与接收（RX）通信共用一个处理器间邮箱（IPM）时，必须选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/ipc/rpmsg_service/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/rpmsg_service/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication）

<a id="CONFIG_RPMSG_SERVICE_WORK_QUEUE_STACK_SIZE"></a>

## 348.61 `CONFIG_RPMSG_SERVICE_WORK_QUEUE_STACK_SIZE`

**提示（Prompt）**：接收工作队列栈大小（RX work queue stack size）

**说明（Help）**

接收工作队列线程使用的栈大小。RPMsg 服务后端模块创建此工作队列，以免从系统工作队列向服务用户通知收到的数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSG_SERVICE
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/ipc/rpmsg_service/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/ipc/rpmsg_service/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 处理器间通信（Inter Processor Communication） → 供多个用户使用的 RPMsg 服务（service）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_RPMSG_SERVICE)。

<!-- kconfig-navigation -->

[上一章](P347_subsys_instrumentation_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P349_subsys_jwt_配置项参考.md)
