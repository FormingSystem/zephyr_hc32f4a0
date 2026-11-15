---
id: learning.zephyr-docs.kconfig-reference.page-403
title: "`subsys/net`配置项参考（13/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第403章\_`subsys/net`配置项参考（13/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_PKT_LOG_LEVEL_CHOICE"></a>

## 403.1 `CONFIG_NET_PKT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：网络数据包及缓冲区分配日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_PKT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_PKT_LOG_LEVEL_OFF
CONFIG_NET_PKT_LOG_LEVEL_ERR
CONFIG_NET_PKT_LOG_LEVEL_WRN
CONFIG_NET_PKT_LOG_LEVEL_INF
CONFIG_NET_PKT_LOG_LEVEL_DBG
CONFIG_NET_PKT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络协议栈日志与调试（Logging and debugging）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_LOG_LEVEL_DEFAULT`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_PKT_LOG_LEVEL_OFF`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_LOG_LEVEL_OFF)、[`CONFIG_NET_PKT_LOG_LEVEL_ERR`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_LOG_LEVEL_ERR)、[`CONFIG_NET_PKT_LOG_LEVEL_WRN`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_LOG_LEVEL_WRN)、[`CONFIG_NET_PKT_LOG_LEVEL_INF`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_LOG_LEVEL_INF)、[`CONFIG_NET_PKT_LOG_LEVEL_DBG`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_PKT_LOG_LEVEL_DBG"></a>

## 403.2 `CONFIG_NET_PKT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络协议栈日志与调试（Logging and debugging） → 网络数据包及缓冲区分配日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_LOG_LEVEL_DEFAULT"></a>

## 403.3 `CONFIG_NET_PKT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络协议栈日志与调试（Logging and debugging） → 网络数据包及缓冲区分配日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_LOG_LEVEL_ERR"></a>

## 403.4 `CONFIG_NET_PKT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络协议栈日志与调试（Logging and debugging） → 网络数据包及缓冲区分配日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_LOG_LEVEL_INF"></a>

## 403.5 `CONFIG_NET_PKT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络协议栈日志与调试（Logging and debugging） → 网络数据包及缓冲区分配日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_LOG_LEVEL_OFF"></a>

## 403.6 `CONFIG_NET_PKT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络协议栈日志与调试（Logging and debugging） → 网络数据包及缓冲区分配日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_LOG_LEVEL_WRN"></a>

## 403.7 `CONFIG_NET_PKT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络协议栈日志与调试（Logging and debugging） → 网络数据包及缓冲区分配日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_RXTIME_STATS"></a>

## 403.8 `CONFIG_NET_PKT_RXTIME_STATS`

**提示（Prompt）**：网络数据包接收时间统计（RX time statistics）

**说明（Help）**

启用网络数据包接收时间统计（RX time statistics），用于计算数据包从设备驱动传递到即将交给应用之前所需的平均时间。可在网络命令行（net-shell）的网络接口统计信息中查看接收计时结果。仅对 UDP 和 TCP 数据包计算此项接收统计。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_UDP || CONFIG_NET_TCP || CONFIG_NET_SOCKETS_PACKET) && CONFIG_NET_NATIVE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_PKT_TIMESTAMP
CONFIG_NET_STATISTICS
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:975`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L975)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP)、[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_SOCKETS_PACKET`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_PACKET)、[`CONFIG_NET_NATIVE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_NATIVE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_TIMESTAMP`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_TIMESTAMP)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)。

<a id="CONFIG_NET_PKT_RXTIME_STATS_DETAIL"></a>

## 403.9 `CONFIG_NET_PKT_RXTIME_STATS_DETAIL`

**提示（Prompt）**：获取接收路径（RX path）的额外详细统计信息

**说明（Help）**

在接收路径（RX path）的特定关键点记录接收统计明细。这是用途很特殊的配置，会增大 `net_pkt`，因此通常不应启用。可在网络命令行（net-shell）中通过 `net stats` 查看额外统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PKT_RXTIME_STATS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:988`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L988)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络数据包接收时间统计（RX time statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_RXTIME_STATS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_RXTIME_STATS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_PKT_RX_COUNT"></a>

## 403.10 `CONFIG_NET_PKT_RX_COUNT`

**提示（Prompt）**：可同时处于待处理状态的数据包接收操作数量

**说明（Help）**

每个接收（RX）缓冲区占用少量内存。参见 `include/net/net_pkt.h` 和 `sizeof(struct net_pkt)`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
14 if CONFIG_NET_PKT_LARGE_DEFAULTS
4
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:746`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L746)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_LARGE_DEFAULTS`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_LARGE_DEFAULTS)。

<a id="CONFIG_NET_PKT_TIMESTAMP"></a>

## 403.11 `CONFIG_NET_PKT_TIMESTAMP`

**提示（Prompt）**：网络数据包时间戳（Timestamp）支持

**说明（Help）**

启用网络数据包时间戳（Timestamp）支持，允许在网络数据包中存储时间戳信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_IEEE802154_MCXW
CONFIG_NET_L2_PTP_TIMESTAMPING
CONFIG_NET_PKT_RXTIME_STATS
CONFIG_NET_PKT_TXTIME_STATS
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:945`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L945)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_IEEE802154_MCXW`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_MCXW)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PTP_TIMESTAMPING)、[`CONFIG_NET_PKT_RXTIME_STATS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_RXTIME_STATS)、[`CONFIG_NET_PKT_TXTIME_STATS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_TXTIME_STATS)。

<a id="CONFIG_NET_PKT_TIMESTAMP_STACK_SIZE"></a>

## 403.12 `CONFIG_NET_PKT_TIMESTAMP_STACK_SIZE`

**提示（Prompt）**：时间戳线程栈大小（Timestamp thread stack size）

**说明（Help）**

设置时间戳线程栈大小，单位为字节。该线程等待带有时间戳的发送（TX）帧，并调用已注册的回调（Callback）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PKT_TIMESTAMP_THREAD && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2048 if CONFIG_64BIT
1024
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:958`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L958)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络数据包时间戳（Timestamp）支持 → 创建发送时间戳线程（TX timestamp thread）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_TIMESTAMP_THREAD`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_TIMESTAMP_THREAD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)。

<a id="CONFIG_NET_PKT_TIMESTAMP_THREAD"></a>

## 403.13 `CONFIG_NET_PKT_TIMESTAMP_THREAD`

**提示（Prompt）**：创建发送时间戳线程（TX timestamp thread）

**说明（Help）**

创建发送时间戳线程（TX timestamp thread），使带时间戳的网络数据包能够入队，并由已注册的回调（Callback）处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PKT_TIMESTAMP && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_L2_PTP_TIMESTAMPING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:951`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L951)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络数据包时间戳（Timestamp）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_TIMESTAMP`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_TIMESTAMP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PTP_TIMESTAMPING)。

<a id="CONFIG_NET_PKT_TXTIME"></a>

## 403.14 `CONFIG_NET_PKT_TXTIME`

**提示（Prompt）**：网络数据包发送时刻（TX time）支持

**说明（Help）**

启用网络数据包发送时刻（TX time）支持。应用需要设置网络数据包的精确发送时间时，必须启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_IEEE802154_MCXW
CONFIG_NET_CONTEXT_TXTIME
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:968`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L968)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_IEEE802154_MCXW`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_MCXW)、[`CONFIG_NET_CONTEXT_TXTIME`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_TXTIME)。

<a id="CONFIG_NET_PKT_TXTIME_STATS"></a>

## 403.15 `CONFIG_NET_PKT_TXTIME_STATS`

**提示（Prompt）**：网络数据包发送时间统计（TX time statistics）

**说明（Help）**

启用网络数据包发送时间统计（TX time statistics），用于计算数据包从应用传递到即将发送到网络之前所需的平均时间。可在网络命令行（net-shell）的网络接口统计信息中查看发送计时结果。原文说明，接收（RX）计时仅对 UDP、TCP 或 RAW 数据包进行；发送端无法知道协议类型，因此对所有网络协议的数据包进行发送计时。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_UDP || CONFIG_NET_TCP || CONFIG_NET_SOCKETS_PACKET) && CONFIG_NET_NATIVE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_PKT_TIMESTAMP
CONFIG_NET_STATISTICS
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:998`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L998)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP)、[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_SOCKETS_PACKET`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_PACKET)、[`CONFIG_NET_NATIVE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_NATIVE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_TIMESTAMP`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_TIMESTAMP)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)。

<a id="CONFIG_NET_PKT_TXTIME_STATS_DETAIL"></a>

## 403.16 `CONFIG_NET_PKT_TXTIME_STATS_DETAIL`

**提示（Prompt）**：获取发送路径（TX path）的额外详细统计信息

**说明（Help）**

在发送路径（TX path）的特定关键点记录统计明细。原文在此将其称为“接收统计信息（receive statistics）”。这是用途很特殊的配置，会增大 `net_pkt`，因此通常不应启用。可在网络命令行（net-shell）中通过 `net stats` 查看额外统计信息。

译注：标题和路径均指发送（TX），但原文正文使用 receive；这里标明原文差异。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PKT_TXTIME_STATS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:1013`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L1013)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络数据包发送时间统计（TX time statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_TXTIME_STATS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_TXTIME_STATS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_PKT_TX_COUNT"></a>

## 403.17 `CONFIG_NET_PKT_TX_COUNT`

**提示（Prompt）**：可同时处于待处理状态的数据包发送操作数量

**说明（Help）**

每个发送（TX）缓冲区占用少量内存。参见 `include/net/net_pkt.h` 和 `sizeof(struct net_pkt)`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
14 if CONFIG_NET_PKT_LARGE_DEFAULTS
4
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:754`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L754)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_LARGE_DEFAULTS`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_LARGE_DEFAULTS)。

<a id="CONFIG_NET_PMTU_LOG_LEVEL_CHOICE"></a>

## 403.18 `CONFIG_NET_PMTU_LOG_LEVEL_CHOICE`

**提示（Prompt）**：路径 MTU（PMTU）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_PMTU && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_PMTU_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_PMTU_LOG_LEVEL_OFF
CONFIG_NET_PMTU_LOG_LEVEL_ERR
CONFIG_NET_PMTU_LOG_LEVEL_WRN
CONFIG_NET_PMTU_LOG_LEVEL_INF
CONFIG_NET_PMTU_LOG_LEVEL_DBG
CONFIG_NET_PMTU_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_PMTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PMTU)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PMTU_LOG_LEVEL_DEFAULT`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PMTU_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_PMTU_LOG_LEVEL_OFF`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PMTU_LOG_LEVEL_OFF)、[`CONFIG_NET_PMTU_LOG_LEVEL_ERR`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PMTU_LOG_LEVEL_ERR)、[`CONFIG_NET_PMTU_LOG_LEVEL_WRN`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PMTU_LOG_LEVEL_WRN)、[`CONFIG_NET_PMTU_LOG_LEVEL_INF`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PMTU_LOG_LEVEL_INF)、[`CONFIG_NET_PMTU_LOG_LEVEL_DBG`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PMTU_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_PMTU`。

<a id="CONFIG_NET_PMTU_LOG_LEVEL_DBG"></a>

## 403.19 `CONFIG_NET_PMTU_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PMTU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 路径 MTU（PMTU）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PMTU_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PMTU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PMTU_LOG_LEVEL_DEFAULT"></a>

## 403.20 `CONFIG_NET_PMTU_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PMTU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 路径 MTU（PMTU）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PMTU_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PMTU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PMTU_LOG_LEVEL_ERR"></a>

## 403.21 `CONFIG_NET_PMTU_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PMTU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 路径 MTU（PMTU）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PMTU_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PMTU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PMTU_LOG_LEVEL_INF"></a>

## 403.22 `CONFIG_NET_PMTU_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PMTU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 路径 MTU（PMTU）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PMTU_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PMTU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PMTU_LOG_LEVEL_OFF"></a>

## 403.23 `CONFIG_NET_PMTU_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PMTU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 路径 MTU（PMTU）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PMTU_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PMTU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PMTU_LOG_LEVEL_WRN"></a>

## 403.24 `CONFIG_NET_PMTU_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PMTU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 路径 MTU（PMTU）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PMTU_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PMTU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PPP_LOG_LEVEL_CHOICE"></a>

## 403.25 `CONFIG_NET_PPP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：PPP 驱动日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_NET_PPP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_PPP_LOG_LEVEL_OFF
CONFIG_NET_PPP_LOG_LEVEL_ERR
CONFIG_NET_PPP_LOG_LEVEL_WRN
CONFIG_NET_PPP_LOG_LEVEL_INF
CONFIG_NET_PPP_LOG_LEVEL_DBG
CONFIG_NET_PPP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)、[`CONFIG_NET_PPP_LOG_LEVEL_DEFAULT`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PPP_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_PPP_LOG_LEVEL_OFF`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PPP_LOG_LEVEL_OFF)、[`CONFIG_NET_PPP_LOG_LEVEL_ERR`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PPP_LOG_LEVEL_ERR)、[`CONFIG_NET_PPP_LOG_LEVEL_WRN`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PPP_LOG_LEVEL_WRN)、[`CONFIG_NET_PPP_LOG_LEVEL_INF`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PPP_LOG_LEVEL_INF)、[`CONFIG_NET_PPP_LOG_LEVEL_DBG`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PPP_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_PPP_LOG_LEVEL_DBG"></a>

## 403.26 `CONFIG_NET_PPP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动 → PPP 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PPP_LOG_LEVEL_DEFAULT"></a>

## 403.27 `CONFIG_NET_PPP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动 → PPP 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PPP_LOG_LEVEL_ERR"></a>

## 403.28 `CONFIG_NET_PPP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动 → PPP 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PPP_LOG_LEVEL_INF"></a>

## 403.29 `CONFIG_NET_PPP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动 → PPP 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PPP_LOG_LEVEL_OFF"></a>

## 403.30 `CONFIG_NET_PPP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动 → PPP 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PPP_LOG_LEVEL_WRN"></a>

## 403.31 `CONFIG_NET_PPP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动 → PPP 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PROMISCUOUS_MODE"></a>

## 403.32 `CONFIG_NET_PROMISCUOUS_MODE`

**提示（Prompt）**：混杂模式支持。

**说明（Help）**

启用混杂模式（Promiscuous mode）支持。仅当网络设备驱动支持混杂模式时才有效，用户应用也需要读取混杂模式的数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
CONFIG_NET_L2_ETHERNET_MGMT if CONFIG_NET_L2_ETHERNET
```

**被选择（Selected by）**

```text
CONFIG_NRF70_PROMISC_DATA_RX
CONFIG_DSA_CONDUIT_PROMISC_ON
CONFIG_NET_ETHERNET_BRIDGE
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:1032`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L1032)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NET_L2_ETHERNET_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_ETHERNET_MGMT)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NRF70_PROMISC_DATA_RX`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_PROMISC_DATA_RX)、[`CONFIG_DSA_CONDUIT_PROMISC_ON`](P392_subsys_net_配置项参考_2.md#CONFIG_DSA_CONDUIT_PROMISC_ON)、[`CONFIG_NET_ETHERNET_BRIDGE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE)。

<a id="CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE"></a>

## 403.33 `CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：混杂模式（Promiscuous mode）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_PROMISCUOUS_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_PROMISC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_PROMISC_LOG_LEVEL_OFF
CONFIG_NET_PROMISC_LOG_LEVEL_ERR
CONFIG_NET_PROMISC_LOG_LEVEL_WRN
CONFIG_NET_PROMISC_LOG_LEVEL_INF
CONFIG_NET_PROMISC_LOG_LEVEL_DBG
CONFIG_NET_PROMISC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 混杂模式支持。

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_PROMISCUOUS_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISCUOUS_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PROMISC_LOG_LEVEL_DEFAULT`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISC_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_PROMISC_LOG_LEVEL_OFF`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISC_LOG_LEVEL_OFF)、[`CONFIG_NET_PROMISC_LOG_LEVEL_ERR`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISC_LOG_LEVEL_ERR)、[`CONFIG_NET_PROMISC_LOG_LEVEL_WRN`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISC_LOG_LEVEL_WRN)、[`CONFIG_NET_PROMISC_LOG_LEVEL_INF`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISC_LOG_LEVEL_INF)、[`CONFIG_NET_PROMISC_LOG_LEVEL_DBG`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISC_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_PROMISC_LOG_LEVEL_DBG"></a>

## 403.34 `CONFIG_NET_PROMISC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 混杂模式支持。 → 混杂模式（Promiscuous mode）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PROMISC_LOG_LEVEL_DEFAULT"></a>

## 403.35 `CONFIG_NET_PROMISC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 混杂模式支持。 → 混杂模式（Promiscuous mode）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PROMISC_LOG_LEVEL_ERR"></a>

## 403.36 `CONFIG_NET_PROMISC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 混杂模式支持。 → 混杂模式（Promiscuous mode）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PROMISC_LOG_LEVEL_INF"></a>

## 403.37 `CONFIG_NET_PROMISC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 混杂模式支持。 → 混杂模式（Promiscuous mode）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PROMISC_LOG_LEVEL_OFF"></a>

## 403.38 `CONFIG_NET_PROMISC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 混杂模式支持。 → 混杂模式（Promiscuous mode）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PROMISC_LOG_LEVEL_WRN"></a>

## 403.39 `CONFIG_NET_PROMISC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 混杂模式支持。 → 混杂模式（Promiscuous mode）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PROMISC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PSEUDO_IFACE"></a>

## 403.40 `CONFIG_NET_PSEUDO_IFACE`

**提示（Prompt）**：伪网络接口（Pseudo network interface），也称 any 接口

**说明（Help）**

实现一个自身不执行操作的伪网络接口（Pseudo network interface）。例如，可在其上挂接虚拟接口，作为网络数据包捕获处理程序。此选项会创建名为 `any` 的网络接口，充当数据包接收汇点（Packet sink）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_DUMMY && CONFIG_NET_L2_DUMMY && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_VIRTUAL
```

**被选择（Selected by）**

```text
CONFIG_NET_CAPTURE_COOKED_MODE
```

**定义位置（Location）**：[`subsys/net/l2/dummy/any/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/dummy/any/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Dummy L2）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_DUMMY`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_DUMMY)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_VIRTUAL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL)、[`CONFIG_NET_CAPTURE_COOKED_MODE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_COOKED_MODE)。

<a id="CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE"></a>

## 403.41 `CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：伪网络接口（Pseudo network interface）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_PSEUDO_IFACE && CONFIG_NET_L2_DUMMY && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_OFF
CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_ERR
CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_WRN
CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_INF
CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_DBG
CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Dummy L2） → 伪网络接口（Pseudo network interface），也称 any 接口

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_PSEUDO_IFACE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE)、[`CONFIG_NET_L2_DUMMY`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_DUMMY)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_DEFAULT`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_OFF`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_OFF)、[`CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_ERR`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_ERR)、[`CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_WRN`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_WRN)、[`CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_INF`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_INF)、[`CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_DBG`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_DBG"></a>

## 403.42 `CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Dummy L2） → 伪网络接口（Pseudo network interface），也称 any 接口 → 伪网络接口（Pseudo network interface）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_DEFAULT"></a>

## 403.43 `CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Dummy L2） → 伪网络接口（Pseudo network interface），也称 any 接口 → 伪网络接口（Pseudo network interface）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_ERR"></a>

## 403.44 `CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Dummy L2） → 伪网络接口（Pseudo network interface），也称 any 接口 → 伪网络接口（Pseudo network interface）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_INF"></a>

## 403.45 `CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Dummy L2） → 伪网络接口（Pseudo network interface），也称 any 接口 → 伪网络接口（Pseudo network interface）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_OFF"></a>

## 403.46 `CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Dummy L2） → 伪网络接口（Pseudo network interface），也称 any 接口 → 伪网络接口（Pseudo network interface）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_WRN"></a>

## 403.47 `CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Dummy L2） → 伪网络接口（Pseudo network interface），也称 any 接口 → 伪网络接口（Pseudo network interface）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PSEUDO_IFACE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_QBV"></a>

## 403.48 `CONFIG_NET_QBV`

**提示（Prompt）**：Qbv 支持

**说明（Help）**

启用 Qbv 支持。Qbv 即调度流量增强（Enhancements for Scheduled Traffic，EST），是时间敏感网络（Time-Sensitive Networking，TSN）的一项功能。它类似于时分复用（Time Division Multiplexing，TDM），为特定类别的流量提供时间槽（Time slot）。主机还可通过超出标准范围的能力选择数据包发送的时间或时间门（Time gate），由软件精细控制数据包传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_ETHERNET_MGMT
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_ETHERNET_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_ETHERNET_MGMT)。

<a id="CONFIG_NET_QEMU_DEVICE_EXTRA_ARGS"></a>

## 403.49 `CONFIG_NET_QEMU_DEVICE_EXTRA_ARGS`

**提示（Prompt）**：QEMU 网络设备参数（Networking device arguments）

**说明（Help）**

传递给 QEMU 网络设备的额外参数。此字符串附加到 QEMU 的 `-device` 选项；对于模拟机器内置的网卡（NIC），则附加到 `-nic` 选项。通常用于设置 Zephyr 实例的网络 MAC 地址。可以包含多个 QEMU 参数，参数间必须用逗号 `,` 分隔且不能有空格。例如：`mac=02:03:04:f0:0d:01` 或 `mac=02:03:04:f0:0d:01,addr=2.0`。所有网络设备均支持 `mac` 选项；其他选项依赖具体设备，例如 `addr=2.0` 可用于设置 PCI 插槽。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_QEMU_USER || CONFIG_NET_QEMU_ETHERNET) && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_QEMU_USER`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_QEMU_USER)、[`CONFIG_NET_QEMU_ETHERNET`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_QEMU_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_QEMU_ETHERNET"></a>

## 403.50 `CONFIG_NET_QEMU_ETHERNET`

**提示（Prompt）**：以太网（Ethernet）

**说明（Help）**

通过 QEMU 以太网驱动连接宿主系统。Zephyr 支持的这类驱动包括 Intel e1000 以太网驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_QEMU_NETWORKING>
```

**弱选择（Implies）**

```text
CONFIG_ETH_DRIVER
CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → QEMU 网络连接（Networking）

**配置项引用（Symbol References）**：[`CONFIG_NET_QEMU_NETWORKING`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_QEMU_NETWORKING)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)。

<a id="CONFIG_NET_QEMU_NETWORKING"></a>

## 403.51 `CONFIG_NET_QEMU_NETWORKING`

**提示（Prompt）**：QEMU 网络连接（Networking）

**说明（Help）**

选择如何从 QEMU 内部连接宿主系统，可通过串行连接，即串行线路互联网协议（SLIP），或 QEMU 以太网驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QEMU_TARGET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_QEMU_PPP if CONFIG_NET_L2_PPP
CONFIG_NET_QEMU_SLIP
```

**可选项（Choices）**

```text
CONFIG_NET_QEMU_SLIP
CONFIG_NET_QEMU_PPP
CONFIG_NET_QEMU_ETHERNET
CONFIG_NET_QEMU_USER
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_QEMU_PPP`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_QEMU_PPP)、[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NET_QEMU_SLIP`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_QEMU_SLIP)、[`CONFIG_NET_QEMU_ETHERNET`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_QEMU_ETHERNET)、[`CONFIG_NET_QEMU_USER`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_QEMU_USER)。

<a id="CONFIG_NET_QEMU_PPP"></a>

## 403.52 `CONFIG_NET_QEMU_PPP`

**提示（Prompt）**：点对点协议（PPP）

**说明（Help）**

通过点对点协议（PPP）连接宿主机。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_TEST || n) && <choice CONFIG_NET_QEMU_NETWORKING>
```

**弱选择（Implies）**

```text
CONFIG_NET_DRIVERS
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → QEMU 网络连接（Networking）

**配置项引用（Symbol References）**：[`CONFIG_NET_TEST`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TEST)、[`CONFIG_NET_QEMU_NETWORKING`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_QEMU_NETWORKING)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_QEMU_SLIP"></a>

## 403.53 `CONFIG_NET_QEMU_SLIP`

**提示（Prompt）**：串行线路互联网协议（SLIP）

**说明（Help）**

通过串行线路互联网协议（SLIP）连接宿主机或另一个 QEMU 实例。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**弱选择（Implies）**

```text
CONFIG_NET_DRIVERS
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → QEMU 网络连接（Networking）

**配置项引用（Symbol References）**：[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_QEMU_USER"></a>

## 403.54 `CONFIG_NET_QEMU_USER`

**提示（Prompt）**：SLIRP 用户网络

**说明（Help）**

通过 QEMU 内置的用户网络（User Networking）功能连接宿主系统。其使用 `slirp`，在 QEMU 内实现完整 TCP/IP 协议栈，再通过该协议栈实现经过网络地址转换（NAT）的虚拟网络。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_QEMU_NETWORKING>
```

**弱选择（Implies）**

```text
CONFIG_ETH_DRIVER
CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → QEMU 网络连接（Networking）

**配置项引用（Symbol References）**：[`CONFIG_NET_QEMU_NETWORKING`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_QEMU_NETWORKING)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)。

<a id="CONFIG_NET_QEMU_USER_EXTRA_ARGS"></a>

## 403.55 `CONFIG_NET_QEMU_USER_EXTRA_ARGS`

**提示（Prompt）**：QEMU 用户网络参数（User Networking arguments）

**说明（Help）**

启用用户网络（User Networking）时传给 QEMU 的额外参数，可包含宿主机与来宾机的端口转发（Port forwarding）、设备 ID、网络地址信息等。此字符串附加到 QEMU 的 `-netdev user` 选项。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_QEMU_USER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L176)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_QEMU_USER`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_QEMU_USER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_RAW_MODE"></a>

## 403.56 `CONFIG_NET_RAW_MODE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

这是用途很特殊的选项，仅构建网络协议栈中最小的部分，让网络驱动在上方没有网络核心（Core）、第二层（L2）等协议栈组件的情况下工作。基本上只构建 `net_pkt` 部分。目前仅 IEEE 802.15.4 驱动使用它，但任何类型的网络驱动都可以使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_ETH_DRIVER_RAW_MODE
CONFIG_IEEE802154_RAW_MODE
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_ETH_DRIVER_RAW_MODE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER_RAW_MODE)、[`CONFIG_IEEE802154_RAW_MODE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_RAW_MODE)。

<a id="CONFIG_NET_ROUTE"></a>

## 403.57 `CONFIG_NET_ROUTE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此符号已弃用，其值由面向用户的 IPv6 路由表选项 `NET_IPV6_ROUTE` 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_NBR_CACHE && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_IPV6_ROUTE
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_NBR_CACHE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6_ROUTE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE)。

<a id="CONFIG_NET_ROUTE_MCAST"></a>

## 403.58 `CONFIG_NET_ROUTE_MCAST`

**提示（Prompt）**：多播路由与转发（Multicast Routing / Forwarding）［已弃用，Deprecated］

**说明（Help）**

启用多播路由与转发（Multicast routing/forwarding）。此符号已弃用，请改用 `NET_IPV6_ROUTE_MCAST`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ROUTE && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_ROUTE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_ROUTE)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_NET_ROUTING"></a>

## 403.59 `CONFIG_NET_ROUTING`

**提示（Prompt）**：接口之间的 IPv6 转发（Forwarding）［已弃用，Deprecated］

**说明（Help）**

此符号已弃用，请改用 `NET_IPV6_FORWARDING`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ROUTE && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_ROUTE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_ROUTE)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_NET_RX_DEFAULT_PRIORITY"></a>

## 403.60 `CONFIG_NET_RX_DEFAULT_PRIORITY`

**提示（Prompt）**：未设置时采用的网络接收数据包默认优先级（RX packet priority）

**说明（Help）**

指定用户未设置优先级时，网络接收（RX）数据包使用的默认优先级。0 为最低，7 为最高。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:422`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L422)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_RX_STACK_SIZE"></a>

## 403.61 `CONFIG_NET_RX_STACK_SIZE`

**提示（Prompt）**：接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

设置接收线程（RX thread）的栈大小，单位为字节。接收线程等待来自网络的数据，系统中只有一个此类线程。此值是基准值，实际接收线程栈大小可能因启用的功能而更大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1792 if CONFIG_DNS_RESOLVER
1500
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stack:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stack#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 栈使用情况（Stack usage）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)。

<a id="CONFIG_NET_SHELL"></a>

## 403.62 `CONFIG_NET_SHELL`

**提示（Prompt）**：网络命令行工具（Network shell utilities）

**说明（Help）**

启用命令行模块（Shell module），向控制台提供 ping 等网络命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_SHELL
CONFIG_REQUIRES_FLOAT_PRINTF
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_SMOKE_TESTS
CONFIG_NET_ETHERNET_BRIDGE_SHELL
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_REQUIRES_FLOAT_PRINTF`](P198_lib_配置项参考_2.md#CONFIG_REQUIRES_FLOAT_PRINTF)、[`CONFIG_NXP_WIFI_SMOKE_TESTS`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SMOKE_TESTS)、[`CONFIG_NET_ETHERNET_BRIDGE_SHELL`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_SHELL)。

<a id="CONFIG_NET_SHELL_CAPTURE_SUPPORTED"></a>

## 403.63 `CONFIG_NET_SHELL_CAPTURE_SUPPORTED`

**提示（Prompt）**：数据包捕获配置（Packet capture configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_CAPTURE) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_CONNECTION_MANAGER_SUPPORTED"></a>

## 403.64 `CONFIG_NET_SHELL_CONNECTION_MANAGER_SUPPORTED`

**提示（Prompt）**：连接管理器状态（Connection manager status）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_CONNECTION_MANAGER) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_DHCPV4_SUPPORTED"></a>

## 403.65 `CONFIG_NET_SHELL_DHCPV4_SUPPORTED`

**提示（Prompt）**：启动或停止 DHCPv4

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_DHCPV4_SERVER || CONFIG_NET_DHCPV4) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_DHCPV6_SUPPORTED"></a>

## 403.66 `CONFIG_NET_SHELL_DHCPV6_SUPPORTED`

**提示（Prompt）**：启动或停止 DHCPv6

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_DHCPV6_SERVER || CONFIG_NET_DHCPV6) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_DHCPV6_SERVER`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER)、[`CONFIG_NET_DHCPV6`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_DNS_RESOLVER_QUEUE_SIZE"></a>

## 403.67 `CONFIG_NET_SHELL_DNS_RESOLVER_QUEUE_SIZE`

**提示（Prompt）**：DNS 解析器信息队列大小（Resolver info queue size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SHELL_DNS_RESOLVER_SUPPORTED && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_DNS_RESOLVER_SUPPORTED`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_DNS_RESOLVER_SUPPORTED)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_DNS_RESOLVER_SUPPORTED"></a>

## 403.68 `CONFIG_NET_SHELL_DNS_RESOLVER_SUPPORTED`

**提示（Prompt）**：域名系统解析器（DNS resolver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_DNS_RESOLVER) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_DYN_CMD_COMPLETION"></a>

## 403.69 `CONFIG_NET_SHELL_DYN_CMD_COMPLETION`

**提示（Prompt）**：网络命令行动态命令补全（Dynamic command completion）

**说明（Help）**

让多个网络命令行（net-shell）命令支持动态命令补全（Dynamic command completion）。例如，`nbr` 命令可以自动补全邻居的 IPv6 地址，无需用户手动输入。注意，保存动态命令字符串会占用更多内存。例如，默认情况下 `nbr` 命令增加 320 字节，即 8 个邻居乘以每个 IPv6 地址 40 字节。其他支持动态补全的 net-shell 命令也各需少量额外内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:236`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L236)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_ETHERNET_SUPPORTED"></a>

## 403.70 `CONFIG_NET_SHELL_ETHERNET_SUPPORTED`

**提示（Prompt）**：以太网相关配置（Ethernet configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_L2_ETHERNET) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_EVENT_MONITOR_SUPPORTED"></a>

## 403.71 `CONFIG_NET_SHELL_EVENT_MONITOR_SUPPORTED`

**提示（Prompt）**：网络管理事件监测配置（Network management event monitoring configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_MGMT_EVENT_MONITOR) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_MGMT_EVENT_MONITOR`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_MONITOR)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_FTP_SUPPORTED"></a>

## 403.72 `CONFIG_NET_SHELL_FTP_SUPPORTED`

**提示（Prompt）**：文件传输协议客户端（FTP client）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_FTP_CLIENT) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_FTP_CLIENT`](P392_subsys_net_配置项参考_2.md#CONFIG_FTP_CLIENT)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_GPTP_SUPPORTED"></a>

## 403.73 `CONFIG_NET_SHELL_GPTP_SUPPORTED`

**提示（Prompt）**：gPTP 监测（Monitoring）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_GPTP) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_HTTP_CLIENT_CERTIFICATE"></a>

## 403.74 `CONFIG_NET_SHELL_HTTP_CLIENT_CERTIFICATE`

**提示（Prompt）**：HTTP 客户端 SSL 证书（SSL Certificate）

**说明（Help）**

提供以 DER 编码的证书颁发机构（CA）证书文件名，文件位于 `<app>/certs/` 目录下。示例：`CONFIG_NET_SHELL_HTTP_CLIENT_CERTIFICATE="globalsign_r1.der"`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_TLS_CREDENTIALS && CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities） → HTTP 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS)、[`CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_HTTP_CLIENT_CERTIFICATE_TAG"></a>

## 403.75 `CONFIG_NET_SHELL_HTTP_CLIENT_CERTIFICATE_TAG`

**提示（Prompt）**：HTTP 客户端 SSL 证书标签（Certificate TAG）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TLS_CREDENTIALS && CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities） → HTTP 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS)、[`CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED"></a>

## 403.76 `CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED`

**提示（Prompt）**：HTTP 客户端（Client）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_HTTP_CLIENT) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SHELL_GETOPT if CONFIG_HTTP_CLIENT
CONFIG_GETOPT_LONG if CONFIG_HTTP_CLIENT
CONFIG_NET_CONNECTION_MANAGER if CONFIG_HTTP_CLIENT
CONFIG_DNS_RESOLVER if CONFIG_HTTP_CLIENT
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_HTTP_CLIENT`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_CLIENT)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SHELL_GETOPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_GETOPT)、[`CONFIG_GETOPT_LONG`](P197_lib_配置项参考_1.md#CONFIG_GETOPT_LONG)、[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)。

<a id="CONFIG_NET_SHELL_HTTP_CLIENT_URL_LEN"></a>

## 403.77 `CONFIG_NET_SHELL_HTTP_CLIENT_URL_LEN`

**提示（Prompt）**：HTTP 客户端 URL 长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities） → HTTP 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_HTTP_SERVER_SUPPORTED"></a>

## 403.78 `CONFIG_NET_SHELL_HTTP_SERVER_SUPPORTED`

**提示（Prompt）**：HTTP 服务器状态（Server status）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_HTTP_SERVER) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_IPV4_SUPPORTED"></a>

## 403.79 `CONFIG_NET_SHELL_IPV4_SUPPORTED`

**提示（Prompt）**：IPv4 配置（Configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || (CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4)) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_SHELL_IPV6_SUPPORTED"></a>

## 403.80 `CONFIG_NET_SHELL_IPV6_SUPPORTED`

**提示（Prompt）**：IPv6 配置（Configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || (CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6)) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_SHELL_IP_SUPPORTED"></a>

## 403.81 `CONFIG_NET_SHELL_IP_SUPPORTED`

**提示（Prompt）**：通用 IP 工具（Generic IP utilities）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_IP) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_IP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IP)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_IP`。

<a id="CONFIG_NET_SHELL_IP_TABLE_SUPPORTED"></a>

## 403.82 `CONFIG_NET_SHELL_IP_TABLE_SUPPORTED`

**提示（Prompt）**：用于 IP 转发的 IP 表（IP table）

**说明（Help）**

添加 IP 表规则（IP table rule），允许特定 IPv4 数据包通过接口和子网转发。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_IPV4_NAT) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SHELL_GETOPT if CONFIG_NET_IPV4_NAT
CONFIG_GETOPT_LONG if CONFIG_NET_IPV4_NAT
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:258`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L258)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_IPV4_NAT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_NAT)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SHELL_GETOPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_GETOPT)、[`CONFIG_GETOPT_LONG`](P197_lib_配置项参考_1.md#CONFIG_GETOPT_LONG)。

<a id="CONFIG_NET_SHELL_PKT_ALLOC_SUPPORTED"></a>

## 403.83 `CONFIG_NET_SHELL_PKT_ALLOC_SUPPORTED`

**提示（Prompt）**：数据包分配监测（Packet allocation monitoring）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_DEBUG_NET_PKT_ALLOC) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_DEBUG_NET_PKT_ALLOC`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEBUG_NET_PKT_ALLOC)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_PKT_FILTER_SUPPORTED"></a>

## 403.84 `CONFIG_NET_SHELL_PKT_FILTER_SUPPORTED`

**提示（Prompt）**：网络数据包过滤器相关配置（Network packet filter configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_PKT_FILTER) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_PKT_FILTER`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_PMTU_SUPPORTED"></a>

## 403.85 `CONFIG_NET_SHELL_PMTU_SUPPORTED`

**提示（Prompt）**：路径 MTU（PMTU）配置

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_PMTU) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_PMTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PMTU)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_PMTU`。

<a id="CONFIG_NET_SHELL_POWER_MANAGEMENT_SUPPORTED"></a>

## 403.86 `CONFIG_NET_SHELL_POWER_MANAGEMENT_SUPPORTED`

**提示（Prompt）**：网络电源管理恢复与挂起（Power management resume/suspend）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_POWER_MANAGEMENT) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_POWER_MANAGEMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_POWER_MANAGEMENT)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_POWER_MANAGEMENT`。

<a id="CONFIG_NET_SHELL_PPP_SUPPORTED"></a>

## 403.87 `CONFIG_NET_SHELL_PPP_SUPPORTED`

**提示（Prompt）**：点对点协议（PPP）配置

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_L2_PPP) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_PTP_SUPPORTED"></a>

## 403.88 `CONFIG_NET_SHELL_PTP_SUPPORTED`

**提示（Prompt）**：精确时间协议（PTP）监测

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_PTP) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_POSIX_C_LANG_SUPPORT_R if CONFIG_PTP
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_PTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_POSIX_C_LANG_SUPPORT_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_C_LANG_SUPPORT_R)。

<a id="CONFIG_NET_SHELL_QBV_SUPPORTED"></a>

## 403.89 `CONFIG_NET_SHELL_QBV_SUPPORTED`

**提示（Prompt）**：Qbv 命令行（Shell）

**说明（Help）**

启用 Qbv 命令行（Shell）。目前支持设置（Set）和启用（Enable）操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_QBV) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PTP_CLOCK_SHELL if CONFIG_NET_QBV
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L212)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_QBV`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_QBV)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PTP_CLOCK_SHELL`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK_SHELL)。

<a id="CONFIG_NET_SHELL_QUIC_SUPPORTED"></a>

## 403.90 `CONFIG_NET_SHELL_QUIC_SUPPORTED`

**提示（Prompt）**：QUIC 连接状态（Connectivity status）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_QUIC_SHELL) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:226`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L226)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_QUIC_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_SHELL)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_REQUIRE_TX_THREAD"></a>

## 403.91 `CONFIG_NET_SHELL_REQUIRE_TX_THREAD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏符号，表示网络命令行（Network shell）需要独立发送线程（TX thread），因为命令行与网络协议栈操作期间可能发生死锁（Deadlock）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SHELL_BACKEND_TELNET || CONFIG_SHELL_BACKEND_MQTT) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_ARP
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_TELNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_BACKEND_MQTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_ARP`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP)。

<a id="CONFIG_NET_SHELL_ROUTE_SUPPORTED"></a>

## 403.92 `CONFIG_NET_SHELL_ROUTE_SUPPORTED`

**提示（Prompt）**：IP 路由配置（Routing configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || ((CONFIG_NET_IPV4_ROUTE || CONFIG_NET_IPV6_ROUTE) && CONFIG_NET_NATIVE)) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_IPV4_ROUTE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ROUTE)、[`CONFIG_NET_IPV6_ROUTE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE)、[`CONFIG_NET_NATIVE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_NATIVE)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS"></a>

## 403.93 `CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`

**提示（Prompt）**：显示已禁用命令的信息（Disabled command information）

**说明（Help）**

默认提供全部网络命令行命令；命令被禁用时，执行该命令会打印禁用状态及启用方法。如果不需要此提示，只希望看到实际可用的命令，则可隐藏当前配置下不可用的命令，以节省少量闪存（Flash）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_SOCKETS_SERVICE_SUPPORTED"></a>

## 403.94 `CONFIG_NET_SHELL_SOCKETS_SERVICE_SUPPORTED`

**提示（Prompt）**：套接字服务状态（Socket service status）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_SOCKETS_SERVICE) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_SOCKETS_SERVICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SERVICE)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_SSH_SUPPORTED"></a>

## 403.95 `CONFIG_NET_SHELL_SSH_SUPPORTED`

**提示（Prompt）**：安全外壳（SSH）服务器与客户端

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_SSH_SHELL) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:231`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L231)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_SSH_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_SHELL)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_SHELL`。

<a id="CONFIG_NET_SHELL_STATISTICS_SUPPORTED"></a>

## 403.96 `CONFIG_NET_SHELL_STATISTICS_SUPPORTED`

**提示（Prompt）**：网络统计监测（Network statistics monitoring）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_STATISTICS) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_TCP_SUPPORTED"></a>

## 403.97 `CONFIG_NET_SHELL_TCP_SUPPORTED`

**提示（Prompt）**：发送与接收 TCP 数据

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || (CONFIG_NET_NATIVE_TCP && CONFIG_NET_TCP)) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_NATIVE_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_TCP)、[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_TCP`。

<a id="CONFIG_NET_SHELL_TFTP_CLIENT_SUPPORTED"></a>

## 403.98 `CONFIG_NET_SHELL_TFTP_CLIENT_SUPPORTED`

**提示（Prompt）**：简单文件传输协议客户端（TFTP client）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_TFTP_LIB) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SHELL_GETOPT if CONFIG_TFTP_LIB
CONFIG_GETOPT_LONG if CONFIG_TFTP_LIB
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_TFTP_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFTP_LIB)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SHELL_GETOPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_GETOPT)、[`CONFIG_GETOPT_LONG`](P197_lib_配置项参考_1.md#CONFIG_GETOPT_LONG)。

<a id="CONFIG_NET_SHELL_UDP_SUPPORTED"></a>

## 403.99 `CONFIG_NET_SHELL_UDP_SUPPORTED`

**提示（Prompt）**：发送与接收 UDP 数据

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || (CONFIG_NET_NATIVE_UDP && CONFIG_NET_UDP)) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_NATIVE_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_UDP)、[`CONFIG_NET_UDP`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_UDP`。

<a id="CONFIG_NET_SHELL_VIRTUAL_SUPPORTED"></a>

## 403.100 `CONFIG_NET_SHELL_VIRTUAL_SUPPORTED`

**提示（Prompt）**：虚拟网络接口管理（Virtual network interface management）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_L2_VIRTUAL) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L197)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_L2_VIRTUAL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<!-- kconfig-navigation -->

[上一章](P402_subsys_net_配置项参考_12.md) · [返回大纲](大纲.md) · [下一章](P404_subsys_net_配置项参考_14.md)
