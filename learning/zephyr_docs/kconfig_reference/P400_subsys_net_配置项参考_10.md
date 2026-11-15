---
id: learning.zephyr-docs.kconfig-reference.page-400
title: "`subsys/net`配置项参考（10/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第400章\_`subsys/net`配置项参考（10/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_DEFAULT"></a>

## 400.1 `CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 路由管理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_ERR"></a>

## 400.2 `CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 路由管理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_INF"></a>

## 400.3 `CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 路由管理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_OFF"></a>

## 400.4 `CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 路由管理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_WRN"></a>

## 400.5 `CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 路由管理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_ROUTING"></a>

## 400.6 `CONFIG_NET_IPV4_ROUTING`

**提示（Prompt）**：接口之间的 IPv4 路由（Routing）［已弃用，Deprecated］

**说明（Help）**

此符号已弃用，请改用 `NET_IPV4_FORWARDING`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_ROUTE && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L280)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → 邻居缓存（Neighbor cache） → IPv4 单播路由表（Unicast route table）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ROUTE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ROUTE)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV6"></a>

## 400.7 `CONFIG_NET_IPV6`

**提示（Prompt）**：IPv6（互联网协议第 6 版）

**说明（Help）**

启用 IPv6 支持。由于提供的网络承载（Network bearer）中只有有限几种支持 IPv4，因此默认应选中此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_MCP_TRANSPORT_HTTP
CONFIG_NET_CONFIG_NEED_IPV6
CONFIG_POSIX_IPV6
```

**被弱选择（Implied by）**

```text
CONFIG_NET_L2_OPENTHREAD
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MCP_TRANSPORT_HTTP`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_NET_CONFIG_NEED_IPV6`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_NEED_IPV6)、[`CONFIG_POSIX_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_IPV6)、[`CONFIG_NET_L2_OPENTHREAD`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_OPENTHREAD)。

<a id="CONFIG_NET_IPV6_DAD"></a>

## 400.8 `CONFIG_NET_IPV6_DAD`

**提示（Prompt）**：启用重复地址检测（Duplicate Address Detection，DAD）

**说明（Help）**

根据网络需求选择此项。通常应启用重复地址检测（DAD）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_NBR_CACHE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:396`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L396)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 邻居缓存（Neighbor cache）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_NBR_CACHE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_FORWARDING"></a>

## 400.9 `CONFIG_NET_IPV6_FORWARDING`

**提示（Prompt）**：接口之间的 IPv6 转发（Forwarding）

**说明（Help）**

允许设备在不同网络接口和网络技术之间转发 IPv6 数据包。此项独立于 `NET_IPV6_ROUTE`；后者仅启用用于主机端路由选择和命令行路由命令的 IPv6 路由表（Route table）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ROUTE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_ROUTING || CONFIG_NET_IPV6_ROUTING
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:231`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L231)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 单播路由表（Unicast route table）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_ROUTING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTING)、[`CONFIG_NET_IPV6_ROUTING`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTING)、[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_FRAGMENT"></a>

## 400.10 `CONFIG_NET_IPV6_FRAGMENT`

**提示（Prompt）**：支持 IPv6 分片（Fragmentation）

**说明（Help）**

IPv6 分片（Fragmentation）默认禁用，以节省内存。通常这不会造成问题，因为实现本身支持 IPv6 所要求的最小长度的数据包，即 1280 字节。如果启用分片支持，请增加接收（RX）数据缓冲区数量，以便接收超过 1280 字节的数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:300`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L300)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_FRAGMENT_MAX_COUNT"></a>

## 400.11 `CONFIG_NET_IPV6_FRAGMENT_MAX_COUNT`

**提示（Prompt）**：可同时重组（Reassemble）的数据包数量

**说明（Help）**

允许同时等待重组（Reassembly）的已分片 IPv6 数据包数量。每个分片可能占用最多 1280 字节内存，因此需要据此规划，并增加网络缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_FRAGMENT && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:309`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L309)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 支持 IPv6 分片（Fragmentation）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_FRAGMENT`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_FRAGMENT)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_FRAGMENT_MAX_PKT"></a>

## 400.12 `CONFIG_NET_IPV6_FRAGMENT_MAX_PKT`

**提示（Prompt）**：重组一个数据包时可处理的分片（Fragment）数量

**说明（Help）**

收到的分片（Fragment）在重组前存放在各数据包独立的队列中。该值定义为重组单个数据包可同时处理的分片数量。原文依据 RFC 2460 第 5 节说明，无须接受大于 1500 字节的 IPv6 数据包，因此前两个分片应能包含全部数据：第一个为 1280 字节，第二个为 220 字节。如果预计会收到分成两个以上分片的数据包，可以增大该值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_FRAGMENT && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:320`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L320)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 支持 IPv6 分片（Fragmentation）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_FRAGMENT`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_FRAGMENT)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_FRAGMENT_TIMEOUT"></a>

## 400.13 `CONFIG_NET_IPV6_FRAGMENT_TIMEOUT`

**提示（Prompt）**：等待接收分片（Fragment）的时长

**说明（Help）**

等待 IPv6 分片（Fragment）到达多久后重组操作超时。RFC 2460 第 4.5 节规定等待 60 秒，但对内存受限的设备而言可能太长。此值以秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_FRAGMENT && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 60]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:337`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L337)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 支持 IPv6 分片（Fragmentation）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_FRAGMENT`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_FRAGMENT)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_IID_EUI_64"></a>

## 400.14 `CONFIG_NET_IPV6_IID_EUI_64`

**提示（Prompt）**：使用 EUI-64 生成接口标识符（IID）

**说明（Help）**

从修改的 EUI-64，即原文所称的 MAC 地址，生成接口标识符（IID）。这是 RFC 4291 第 2.5.1 节描述的传统方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_IID_GENERATION>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:496`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L496)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 接口标识符（Interface Identifier，IID）的生成方式

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_IID_GENERATION`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_IID_GENERATION)。

<a id="CONFIG_NET_IPV6_IID_GENERATION"></a>

## 400.15 `CONFIG_NET_IPV6_IID_GENERATION`

**提示（Prompt）**：IPv6 接口标识符（Interface Identifier，IID）的生成方式

**说明（Help）**

决定如何生成 IPv6 接口标识符（Interface Identifier，IID）。默认采用 RFC 4291 第 2.5.1 节规定的传统 EUI-64（MAC 地址）格式。用户也可以选择 RFC 7217 规定的稳定 IID（Stable IID），为各网络接口生成随机化的 IID。稳定 IID 通过为不同网络接口使用不同的 IID 来增强隐私。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IPV6_IID_EUI_64
```

**可选项（Choices）**

```text
CONFIG_NET_IPV6_IID_EUI_64
CONFIG_NET_IPV6_IID_STABLE
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:484`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L484)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6_IID_EUI_64`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_IID_EUI_64)、[`CONFIG_NET_IPV6_IID_STABLE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_IID_STABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_IID_STABLE"></a>

## 400.16 `CONFIG_NET_IPV6_IID_STABLE`

**提示（Prompt）**：生成稳定接口标识符（Stable IID）［实验性，Experimental］

**说明（Help）**

生成 RFC 7217 描述的稳定接口标识符（Stable IID）。该选项指定用于 IPv6 无状态地址自动配置（Stateless Address Autoconfiguration，SLAAC）的 IID 生成方法：通过此方法配置的 IPv6 地址在同一子网中保持稳定，但主机从一个网络移动到另一个网络时，对应 IID 会改变。此方法旨在替代基于硬件地址，例如 IEEE 局域网媒体访问控制（MAC）地址，生成 IID 的方式，从而在不牺牲用户安全和隐私的前提下保留地址稳定的好处。目前因报头压缩（Header compression）的原因，6lo 网络禁用了稳定 IID 生成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_6LO && <choice CONFIG_NET_IPV6_IID_GENERATION>
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_KEY_TYPE_HMAC
CONFIG_PSA_WANT_ALG_HMAC
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:502`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L502)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 接口标识符（Interface Identifier，IID）的生成方式

**配置项引用（Symbol References）**：[`CONFIG_NET_6LO`](P395_subsys_net_配置项参考_5.md#CONFIG_NET_6LO)、[`CONFIG_NET_IPV6_IID_GENERATION`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_IID_GENERATION)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_KEY_TYPE_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_HMAC)、[`CONFIG_PSA_WANT_ALG_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_NET_IPV6_LOG_LEVEL_CHOICE"></a>

## 400.17 `CONFIG_NET_IPV6_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IPv6 核心日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IPV6_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_IPV6_LOG_LEVEL_OFF
CONFIG_NET_IPV6_LOG_LEVEL_ERR
CONFIG_NET_IPV6_LOG_LEVEL_WRN
CONFIG_NET_IPV6_LOG_LEVEL_INF
CONFIG_NET_IPV6_LOG_LEVEL_DBG
CONFIG_NET_IPV6_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6_LOG_LEVEL_DEFAULT`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_IPV6_LOG_LEVEL_OFF`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_LOG_LEVEL_OFF)、[`CONFIG_NET_IPV6_LOG_LEVEL_ERR`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_LOG_LEVEL_ERR)、[`CONFIG_NET_IPV6_LOG_LEVEL_WRN`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_LOG_LEVEL_WRN)、[`CONFIG_NET_IPV6_LOG_LEVEL_INF`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_LOG_LEVEL_INF)、[`CONFIG_NET_IPV6_LOG_LEVEL_DBG`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_LOG_LEVEL_DBG"></a>

## 400.18 `CONFIG_NET_IPV6_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 核心日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_LOG_LEVEL_DEFAULT"></a>

## 400.19 `CONFIG_NET_IPV6_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 核心日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_LOG_LEVEL_ERR"></a>

## 400.20 `CONFIG_NET_IPV6_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 核心日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_LOG_LEVEL_INF"></a>

## 400.21 `CONFIG_NET_IPV6_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 核心日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_LOG_LEVEL_OFF"></a>

## 400.22 `CONFIG_NET_IPV6_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 核心日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_LOG_LEVEL_WRN"></a>

## 400.23 `CONFIG_NET_IPV6_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 核心日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_MAX_MCAST_ROUTES"></a>

## 400.24 `CONFIG_NET_IPV6_MAX_MCAST_ROUTES`

**提示（Prompt）**：可存储的多播路由表项（Multicast routing entry）最大数量

**说明（Help）**

决定多播路由表（Multicast routing table）能够存储多少个表项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ROUTE_MCAST && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_MAX_MCAST_ROUTES if CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED
1
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:272`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L272)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 单播路由表（Unicast route table）支持 → 多播路由与转发（Multicast Routing / Forwarding）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE_MCAST`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_MCAST)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MAX_MCAST_ROUTES`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MAX_MCAST_ROUTES)、[`CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`、`CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED`。

<a id="CONFIG_NET_IPV6_MAX_NEIGHBORS"></a>

## 400.25 `CONFIG_NET_IPV6_MAX_NEIGHBORS`

**提示（Prompt）**：支持的 IPv6 邻居（Neighbor）数量

**说明（Help）**

该值取决于网络需求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 254]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L209)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_MAX_NEXTHOPS"></a>

## 400.26 `CONFIG_NET_IPV6_MAX_NEXTHOPS`

**提示（Prompt）**：可存储的下一跳表项（Next hop entry）最大数量

**说明（Help）**

决定下一跳表（Nexthop table）能够存储多少个表项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ROUTE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_MAX_NEXTHOPS if CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED
CONFIG_NET_IPV6_MAX_ROUTES
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:257`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L257)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 单播路由表（Unicast route table）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MAX_NEXTHOPS`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MAX_NEXTHOPS)、[`CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED)、[`CONFIG_NET_IPV6_MAX_ROUTES`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_MAX_ROUTES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`、`CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED`。

<a id="CONFIG_NET_IPV6_MAX_ROUTES"></a>

## 400.27 `CONFIG_NET_IPV6_MAX_ROUTES`

**提示（Prompt）**：可存储的路由表项（Routing entry）最大数量

**说明（Help）**

决定路由表（Routing table）能够存储多少个表项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ROUTE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_MAX_ROUTES if CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED
CONFIG_NET_IPV6_MAX_NEIGHBORS
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:249`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L249)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 单播路由表（Unicast route table）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MAX_ROUTES`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MAX_ROUTES)、[`CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED)、[`CONFIG_NET_IPV6_MAX_NEIGHBORS`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_MAX_NEIGHBORS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`、`CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED`。

<a id="CONFIG_NET_IPV6_MCAST_ROUTE_MAX_IFACES"></a>

## 400.28 `CONFIG_NET_IPV6_MCAST_ROUTE_MAX_IFACES`

**提示（Prompt）**：每个多播路由表项可关联的网络接口最大数量

**说明（Help）**

决定单个多播路由表项（Multicast route entry）可以分配多少个网络接口。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ROUTE_MCAST && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_MCAST_ROUTE_MAX_IFACES if CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED
1
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:281`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L281)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 单播路由表（Unicast route table）支持 → 多播路由与转发（Multicast Routing / Forwarding）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE_MCAST`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_MCAST)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MCAST_ROUTE_MAX_IFACES`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MCAST_ROUTE_MAX_IFACES)、[`CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`、`CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED`。

<a id="CONFIG_NET_IPV6_MCAST_ROUTE_MLD_REPORTS"></a>

## 400.29 `CONFIG_NET_IPV6_MCAST_ROUTE_MLD_REPORTS`

**提示（Prompt）**：在 MLDv2 报告中报告多播路由（Multicast route）

**说明（Help）**

决定是否在 MLDv2 报告中通告多播路由表项（Multicast route entry）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ROUTE_MCAST && CONFIG_NET_IPV6_MLD && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_MCAST_ROUTE_MLD_REPORTS if CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:291`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L291)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 单播路由表（Unicast route table）支持 → 多播路由与转发（Multicast Routing / Forwarding）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE_MCAST`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_MCAST)、[`CONFIG_NET_IPV6_MLD`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_MLD)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MCAST_ROUTE_MLD_REPORTS`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MCAST_ROUTE_MLD_REPORTS)、[`CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`、`CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED`。

<a id="CONFIG_NET_IPV6_MLD"></a>

## 400.30 `CONFIG_NET_IPV6_MLD`

**提示（Prompt）**：多播侦听者发现（Multicast Listener Discovery，MLD）支持

**说明（Help）**

根据网络需求选择此项，通常应启用多播侦听者发现（MLD）。节点使用 MLDv2；检测到 MLDv1 查询器（Querier）时回退到 MLDv1。详见 RFC 3810。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_NET_IPV6_ND
CONFIG_MDNS_RESPONDER
CONFIG_LLMNR_RESPONDER
CONFIG_MQTT_SN_TRANSPORT_UDP
CONFIG_PTP_UDP_IPV6_PROTOCOL
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:348`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L348)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6_ND`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_LLMNR_RESPONDER`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER)、[`CONFIG_MQTT_SN_TRANSPORT_UDP`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_TRANSPORT_UDP)、[`CONFIG_PTP_UDP_IPV6_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_UDP_IPV6_PROTOCOL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_MLD_ROBUSTNESS"></a>

## 400.31 `CONFIG_NET_IPV6_MLD_ROBUSTNESS`

**提示（Prompt）**：MLD 健壮性变量（Robustness Variable）

**说明（Help）**

RFC 3810 第 9.1 节的健壮性变量（Robustness Variable）用于根据链路预期丢包情况进行调整，不应设为 1。加入组时主动发送的报告总次数等于该变量的值。收到 MLDv1 查询器最后一次查询后，记住该查询器的时长为：健壮性变量乘以查询间隔（Query Interval），再加上一个查询响应间隔（Query Response Interval）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_MLD && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 7]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L367)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 多播侦听者发现（Multicast Listener Discovery，MLD）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_MLD`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_MLD)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_MLD_V1_COMPAT"></a>

## 400.32 `CONFIG_NET_IPV6_MLD_V1_COMPAT`

**提示（Prompt）**：MLDv1 兼容模式（Compatibility mode）

**说明（Help）**

按照 RFC 3810 第 8.2.1 节的要求，当链路上存在 MLDv1 查询器（Querier）时，以 MLDv1 侦听者（Listener）身份运行。禁用后，忽略 MLDv1 Query 和 Report，参见 RFC 3810 第 10.1 节，从而避免伪造的 MLDv1 Query 将节点切换到 MLDv1。仅在链路上没有 MLDv1 路由器时才应禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_MLD && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:356`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L356)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 多播侦听者发现（Multicast Listener Discovery，MLD）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_MLD`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_MLD)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_MTU"></a>

## 400.33 `CONFIG_NET_IPV6_MTU`

**提示（Prompt）**：IPv6 最大传输单元（MTU）的初始值

**说明（Help）**

该值通常应为 1280；按原文说明，这是实现必须在不分片的情况下支持的最小 IPv6 数据包大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1280
```

**取值范围（Ranges）**

```text
[1280, 1500]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_NBR_CACHE"></a>

## 400.34 `CONFIG_NET_IPV6_NBR_CACHE`

**提示（Prompt）**：邻居缓存（Neighbor cache）

**说明（Help）**

根据网络需求选择此项，通常应启用邻居缓存（Neighbor cache）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:380`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L380)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE"></a>

## 400.35 `CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IPv6 邻居缓存（Neighbor cache）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_OFF
CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_ERR
CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_WRN
CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_INF
CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_DBG
CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_DEFAULT`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_OFF`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_OFF)、[`CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_ERR`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_ERR)、[`CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_WRN`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_WRN)、[`CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_INF`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_INF)、[`CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_DBG`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_DBG"></a>

## 400.36 `CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 邻居缓存（Neighbor cache）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_DEFAULT"></a>

## 400.37 `CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 邻居缓存（Neighbor cache）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_ERR"></a>

## 400.38 `CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 邻居缓存（Neighbor cache）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_INF"></a>

## 400.39 `CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 邻居缓存（Neighbor cache）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_OFF"></a>

## 400.40 `CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 邻居缓存（Neighbor cache）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_WRN"></a>

## 400.41 `CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 邻居缓存（Neighbor cache）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ND"></a>

## 400.42 `CONFIG_NET_IPV6_ND`

**提示（Prompt）**：启用邻居发现（Neighbor Discovery，ND）

**说明（Help）**

根据网络需求选择此项，通常应启用邻居发现（ND）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_NBR_CACHE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_IPV6_MLD if !CONFIG_NET_TEST
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:387`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L387)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 邻居缓存（Neighbor cache）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_NBR_CACHE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6_MLD`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_MLD)、[`CONFIG_NET_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TEST)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE"></a>

## 400.43 `CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IPv6 邻居发现（Neighbor Discovery）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IPV6_ND_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_IPV6_ND_LOG_LEVEL_OFF
CONFIG_NET_IPV6_ND_LOG_LEVEL_ERR
CONFIG_NET_IPV6_ND_LOG_LEVEL_WRN
CONFIG_NET_IPV6_ND_LOG_LEVEL_INF
CONFIG_NET_IPV6_ND_LOG_LEVEL_DBG
CONFIG_NET_IPV6_ND_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6_ND_LOG_LEVEL_DEFAULT`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_IPV6_ND_LOG_LEVEL_OFF`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_LOG_LEVEL_OFF)、[`CONFIG_NET_IPV6_ND_LOG_LEVEL_ERR`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_LOG_LEVEL_ERR)、[`CONFIG_NET_IPV6_ND_LOG_LEVEL_WRN`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_LOG_LEVEL_WRN)、[`CONFIG_NET_IPV6_ND_LOG_LEVEL_INF`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_LOG_LEVEL_INF)、[`CONFIG_NET_IPV6_ND_LOG_LEVEL_DBG`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_ND_LOG_LEVEL_DBG"></a>

## 400.44 `CONFIG_NET_IPV6_ND_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 邻居发现（Neighbor Discovery）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ND_LOG_LEVEL_DEFAULT"></a>

## 400.45 `CONFIG_NET_IPV6_ND_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 邻居发现（Neighbor Discovery）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ND_LOG_LEVEL_ERR"></a>

## 400.46 `CONFIG_NET_IPV6_ND_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 邻居发现（Neighbor Discovery）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ND_LOG_LEVEL_INF"></a>

## 400.47 `CONFIG_NET_IPV6_ND_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 邻居发现（Neighbor Discovery）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ND_LOG_LEVEL_OFF"></a>

## 400.48 `CONFIG_NET_IPV6_ND_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 邻居发现（Neighbor Discovery）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ND_LOG_LEVEL_WRN"></a>

## 400.49 `CONFIG_NET_IPV6_ND_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 邻居发现（Neighbor Discovery）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ND_RA_TX"></a>

## 400.50 `CONFIG_NET_IPV6_ND_RA_TX`

**提示（Prompt）**：发送 IPv6 路由器通告（Router Advertisement；路由器角色）

**说明（Help）**

允许接口充当 IPv6 路由器：响应收到的路由器请求（Router Solicitation），并周期性地发送主动路由器通告（Unsolicited Router Advertisement）。对于接口上标记为需要通告的每个前缀，通告中都包含一个前缀信息选项（Prefix Information Option）；例如，通过 DHCPv6 前缀委派（RFC 8415）获得的前缀。将前缀委派到下游链路、让该链路上的主机通过 SLAAC 配置地址时，需要此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ND && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:446`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L446)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_ND_RA_TX_INTERVAL"></a>

## 400.51 `CONFIG_NET_IPV6_ND_RA_TX_INTERVAL`

**提示（Prompt）**：主动路由器通告（Unsolicited Router Advertisement）的发送间隔（秒）

**说明（Help）**

路由器接口连续两次主动发送路由器通告（Router Advertisement）的间隔，单位为秒。注意：此间隔固定，并非 RFC 4861 第 6.2.1 节描述的在 `MinRtrAdvInterval` 和 `MaxRtrAdvInterval` 之间随机取值；启用路由器角色时，也不会发送初始的 `MAX_INITIAL_RTR_ADVERTISEMENTS` 次突发通告。在这些定时通告之外，还会发送响应请求的通告（Solicited advertisement）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ND_RA_TX && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
600
```

**取值范围（Ranges）**

```text
[4, 1800]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:461`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L461)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 发送 IPv6 路由器通告（Router Advertisement；路由器角色）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND_RA_TX`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_RA_TX)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_ND_RA_TX_ROUTER_LIFETIME"></a>

## 400.52 `CONFIG_NET_IPV6_ND_RA_TX_ROUTER_LIFETIME`

**提示（Prompt）**：路由器通告中的路由器生存期（Router lifetime，秒）

**说明（Help）**

在路由器通告（Router Advertisement）报头中通告的生存期，单位为秒。设为 0 表示该节点不可用作默认路由器（Default router）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ND_RA_TX && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1800
```

**取值范围（Ranges）**

```text
[0, 9000]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:473`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L473)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 发送 IPv6 路由器通告（Router Advertisement；路由器角色）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND_RA_TX`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND_RA_TX)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_NS_TIMEOUT"></a>

## 400.53 `CONFIG_NET_IPV6_NS_TIMEOUT`

**提示（Prompt）**：邻居请求（Neighbor Solicitation）报文的超时（毫秒）

**说明（Help）**

两次尝试发送邻居请求（Neighbor Solicitation）报文之间的超时，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_NBR_CACHE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:404`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L404)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 邻居缓存（Neighbor cache）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_NBR_CACHE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_PE"></a>

## 400.54 `CONFIG_NET_IPV6_PE`

**提示（Prompt）**：隐私扩展（Privacy Extension，RFC 8981）支持［实验性，Experimental］

**说明（Help）**

启用 IPv6 隐私扩展（Privacy Extension，RFC 8981）。接口标识符会随机化，由此生成的 SLAAC 地址会到期，因此应用必须准备好在旧 IPv6 地址到期时使用新地址。注意，应确保 `CONFIG_NET_IF_UNICAST_IPV6_ADDR_COUNT` 足够大，允许同时为网络接口添加两个由隐私扩展（PE）生成的 IPv6 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_KEY_TYPE_HMAC
CONFIG_PSA_WANT_ALG_HMAC
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_EXPERIMENTAL
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
CONFIG_NET_MGMT_EVENT_INFO
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:526`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L526)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_KEY_TYPE_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_HMAC)、[`CONFIG_PSA_WANT_ALG_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_NET_MGMT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NET_MGMT_EVENT_INFO`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_INFO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_PE_FILTER_PREFIX_COUNT"></a>

## 400.55 `CONFIG_NET_IPV6_PE_FILTER_PREFIX_COUNT`

**提示（Prompt）**：IPv6 前缀过滤列表（Prefix filter list）的大小

**说明（Help）**

IPv6 前缀允许或拒绝过滤列表（Allow/deny filter list）的大小。用户可在运行时设置过滤规则，并依据该列表启用或禁用隐私扩展（Privacy Extension）支持。默认不启用任何过滤规则。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_PE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:548`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L548)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 隐私扩展（Privacy Extension，RFC 8981）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE"></a>

## 400.56 `CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IPv6 隐私扩展（Privacy Extension）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IPV6_PE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_IPV6_PE_LOG_LEVEL_OFF
CONFIG_NET_IPV6_PE_LOG_LEVEL_ERR
CONFIG_NET_IPV6_PE_LOG_LEVEL_WRN
CONFIG_NET_IPV6_PE_LOG_LEVEL_INF
CONFIG_NET_IPV6_PE_LOG_LEVEL_DBG
CONFIG_NET_IPV6_PE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6_PE_LOG_LEVEL_DEFAULT`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_IPV6_PE_LOG_LEVEL_OFF`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE_LOG_LEVEL_OFF)、[`CONFIG_NET_IPV6_PE_LOG_LEVEL_ERR`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE_LOG_LEVEL_ERR)、[`CONFIG_NET_IPV6_PE_LOG_LEVEL_WRN`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE_LOG_LEVEL_WRN)、[`CONFIG_NET_IPV6_PE_LOG_LEVEL_INF`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE_LOG_LEVEL_INF)、[`CONFIG_NET_IPV6_PE_LOG_LEVEL_DBG`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_PE_LOG_LEVEL_DBG"></a>

## 400.57 `CONFIG_NET_IPV6_PE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 隐私扩展（Privacy Extension）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_PE_LOG_LEVEL_DEFAULT"></a>

## 400.58 `CONFIG_NET_IPV6_PE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 隐私扩展（Privacy Extension）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_PE_LOG_LEVEL_ERR"></a>

## 400.59 `CONFIG_NET_IPV6_PE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 隐私扩展（Privacy Extension）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_PE_LOG_LEVEL_INF"></a>

## 400.60 `CONFIG_NET_IPV6_PE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 隐私扩展（Privacy Extension）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_PE_LOG_LEVEL_OFF"></a>

## 400.61 `CONFIG_NET_IPV6_PE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 隐私扩展（Privacy Extension）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_PE_LOG_LEVEL_WRN"></a>

## 400.62 `CONFIG_NET_IPV6_PE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 隐私扩展（Privacy Extension）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_PE_PREFER_PUBLIC_ADDRESSES"></a>

## 400.63 `CONFIG_NET_IPV6_PE_PREFER_PUBLIC_ADDRESSES`

**提示（Prompt）**：优先选择处于首选状态的公开地址（Public preferred address），而非临时地址

**说明（Help）**

优先选择公开地址（Public address），而非临时地址（Temporary address）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_PE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:557`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L557)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 隐私扩展（Privacy Extension，RFC 8981）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_PE_TEMP_IDGEN_RETRIES"></a>

## 400.64 `CONFIG_NET_IPV6_PE_TEMP_IDGEN_RETRIES`

**提示（Prompt）**：重复地址检测（DAD）失败尝试次数的上限

**说明（Help）**

节点必须对生成的临时地址（Temporary address）执行重复地址检测（DAD）。原文随后表述为：连续尝试 `TEMP_IDGEN_RETRIES` 次后，如果“没有生成非唯一地址（no non-unique address was generated）”，就不再尝试为该接口生成临时地址。

译注：原文此处的双重否定与本选项“DAD 失败尝试次数上限”的标题存在语义矛盾，译文保留该表述，未擅自改写其条件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_PE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:576`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L576)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 隐私扩展（Privacy Extension，RFC 8981）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_PE_TEMP_PREFERRED_LIFETIME"></a>

## 400.65 `CONFIG_NET_IPV6_PE_TEMP_PREFERRED_LIFETIME`

**提示（Prompt）**：临时地址的最大首选生存期（Preferred lifetime，分钟）

**说明（Help）**

任何临时地址（Temporary address）保持首选状态的时长都不应超过此值，单位为分钟。默认值为 23 小时，即 `23*60` 分钟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_PE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1380
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:569`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L569)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 隐私扩展（Privacy Extension，RFC 8981）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_PE_TEMP_VALID_LIFETIME"></a>

## 400.66 `CONFIG_NET_IPV6_PE_TEMP_VALID_LIFETIME`

**提示（Prompt）**：临时地址的最大生存期（Lifetime，分钟）

**说明（Help）**

任何临时地址（Temporary address）保持有效的时长都不应超过此值，单位为分钟。默认值为 1 天，即 `24*60` 分钟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_PE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1440
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:562`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L562)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 隐私扩展（Privacy Extension，RFC 8981）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_PMTU"></a>

## 400.67 `CONFIG_NET_IPV6_PMTU`

**提示（Prompt）**：IPv6 路径 MTU 发现（Path MTU Discovery）

**说明（Help）**

启用 IPv6 路径 MTU 发现（Path MTU Discovery），参见 RFC 8201。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_QUIC
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_PMTU_DESTINATION_CACHE_ENTRIES"></a>

## 400.68 `CONFIG_NET_IPV6_PMTU_DESTINATION_CACHE_ENTRIES`

**提示（Prompt）**：IPv6 路径 MTU（PMTU）目的地址缓存表项数量

**说明（Help）**

针对各目的地址可跟踪的路径 MTU（PMTU）表项数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_PMTU && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 路径 MTU 发现（Path MTU Discovery）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PMTU`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PMTU)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_PMTU_DPLPMTUD"></a>

## 400.69 `CONFIG_NET_IPV6_PMTU_DPLPMTUD`

**提示（Prompt）**：使用数据报（Datagram）执行 IPv6 路径 MTU 发现

**说明（Help）**

启用 IPv6 数据报分组化层路径 MTU 发现（Datagram Packetization Layer Path MTU Discovery），参见 RFC 8899。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && CONFIG_NET_IPV6_PMTU && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_QUIC
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 路径 MTU 发现（Path MTU Discovery）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_IPV6_PMTU`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PMTU)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_PMTU_PTB"></a>

## 400.70 `CONFIG_NET_IPV6_PMTU_PTB`

**提示（Prompt）**：使用 ICMP 报文执行 IPv6 路径 MTU 发现（PMTU Discovery）

**说明（Help）**

通过 ICMPv6 数据包过大报文（Packet Too Big）启用 IPv6 路径 MTU 发现（Path MTU Discovery），参见 RFC 8201。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_PMTU && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 路径 MTU 发现（Path MTU Discovery）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PMTU`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PMTU)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_RA_RDNSS"></a>

## 400.71 `CONFIG_NET_IPV6_RA_RDNSS`

**提示（Prompt）**：支持路由器通告递归 DNS 服务器选项（RA RDNSS）

**说明（Help）**

支持路由器通告（Router Advertisement）中的递归 DNS 服务器选项（Recursive DNS Server，RDNSS）。详见 RFC 6106，根据网络需求选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ND && CONFIG_DNS_RESOLVER && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:437`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L437)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_ROUTE"></a>

## 400.72 `CONFIG_NET_IPV6_ROUTE`

**提示（Prompt）**：IPv6 单播路由表（Unicast route table）支持

**说明（Help）**

启用 IPv6 单播路由表（Unicast route table），以及针对本地产生流量的路由感知目的地选择。静态 IPv6 路由、网络命令行中的路由查询，以及 VPN 流量导向等主机端路由选择，都需要此选项。如果设备还必须在接口之间转发数据包，请同时启用 `NET_IPV6_FORWARDING`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_NBR_CACHE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_IPV6_NBR_CACHE
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_NBR_CACHE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE"></a>

## 400.73 `CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IPv6 路由管理日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_OFF
CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_ERR
CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_WRN
CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_INF
CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_DBG
CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_DEFAULT`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_OFF`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_OFF)、[`CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_ERR`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_ERR)、[`CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_WRN`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_WRN)、[`CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_INF`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_INF)、[`CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_DBG`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_DBG"></a>

## 400.74 `CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 路由管理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_DEFAULT"></a>

## 400.75 `CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 路由管理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_ERR"></a>

## 400.76 `CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 路由管理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_INF"></a>

## 400.77 `CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 路由管理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_OFF"></a>

## 400.78 `CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 路由管理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_WRN"></a>

## 400.79 `CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 路由管理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV6_ROUTE_MCAST"></a>

## 400.80 `CONFIG_NET_IPV6_ROUTE_MCAST`

**提示（Prompt）**：多播路由与转发（Multicast Routing / Forwarding）

**说明（Help）**

启用多播路由与转发（Multicast routing/forwarding）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ROUTE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_ROUTE_MCAST if CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 单播路由表（Unicast route table）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_ROUTE_MCAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE_MCAST)、[`CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`、`CONFIG_NET_ROUTE_SYMBOLS_DEPRECATED`。

<a id="CONFIG_NET_IPV6_ROUTING"></a>

## 400.81 `CONFIG_NET_IPV6_ROUTING`

**提示（Prompt）**：接口之间的 IPv6 路由（Routing）［已弃用，Deprecated］

**说明（Help）**

此符号已弃用，请改用 `NET_IPV6_FORWARDING`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ROUTE && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:242`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L242)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → IPv6 单播路由表（Unicast route table）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ROUTE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ROUTE)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_RS_TIMEOUT"></a>

## 400.82 `CONFIG_NET_IPV6_RS_TIMEOUT`

**提示（Prompt）**：路由器请求（Router Solicitation）报文的超时

**说明（Help）**

启动时两次尝试发送路由器请求（Router Solicitation）报文之间的超时，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ND && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 30]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:428`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L428)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV6_UNSOLICITED_NA"></a>

## 400.83 `CONFIG_NET_IPV6_UNSOLICITED_NA`

**提示（Prompt）**：发送主动邻居通告（Unsolicited Neighbor Advertisement）

**说明（Help）**

启用后，每当一个单播地址被添加或通过重复地址检测（DAD）时，节点都会按照 RFC 4861 第 7.2.6 节，为该地址向所有节点地址（All-nodes address）多播一个主动邻居通告（Unsolicited Neighbor Advertisement），并设置 Override 标志。这使仍保留本节点表项的邻居无需等待邻居不可达检测（Neighbor Unreachability Detection），就能纠正过时的链路层地址；它对应 IPv4 中的免费 ARP（Gratuitous ARP，`NET_ARP_GRATUITOUS`）。注意，已经丢弃该表项的邻居会忽略此通告，参见 RFC 4861 第 7.2.5 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_NBR_CACHE && CONFIG_NET_MGMT_EVENT && CONFIG_NET_MGMT_EVENT_INFO && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:412`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L412)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 邻居缓存（Neighbor cache）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_NBR_CACHE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_NBR_CACHE)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NET_MGMT_EVENT_INFO`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_INFO)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IP_ADDR_CHECK"></a>

## 400.84 `CONFIG_NET_IP_ADDR_CHECK`

**提示（Prompt）**：发送 IP 数据包前检查 IP 地址的有效性（Validity）

**说明（Help）**

发送 IPv4 或 IPv6 网络数据包前，检查源地址或目的地址是否正确。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:436`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L436)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_IP_DSCP_ECN"></a>

## 400.85 `CONFIG_NET_IP_DSCP_ECN`

**提示（Prompt）**：在 IP 层处理差分服务代码点（DSCP）和显式拥塞通知（ECN）

**说明（Help）**

指定是否在 IP 层处理 DSCP 和 ECN 值。它们编码在 IPv4 的服务类型（ToS）字段和 IPv6 的流量类别（TC）字段中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_WIREGUARD
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:210`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L210)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_IP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IP)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_IP`。

<a id="CONFIG_NET_L2_CANBUS_RAW"></a>

## 400.86 `CONFIG_NET_L2_CANBUS_RAW`

**提示（Prompt）**：CAN 总线原始二层（CANBUS RAW L2）

**说明（Help）**

添加 CAN 总线第二层（CANBUS L2）驱动，供套接字 CAN（SocketCAN）使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_CANBUS
CONFIG_NET_SOCKETS_CAN
```

**定义位置（Location）**：[`subsys/net/l2/canbus/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/canbus/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CANBUS`](P131_drivers_net_配置项参考.md#CONFIG_NET_CANBUS)、[`CONFIG_NET_SOCKETS_CAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_CAN)。

<a id="CONFIG_NET_L2_CUSTOM_IEEE802154"></a>

## 400.87 `CONFIG_NET_L2_CUSTOM_IEEE802154`

**提示（Prompt）**：自定义 IEEE 802.15.4 第二层（Custom IEEE802154 L2）

**说明（Help）**

启用基于 IEEE 802.15.4 的自定义第二层（L2）。Zephyr 不提供此 L2 的实现；用户可通过此符号，在 IEEE 802.15.4 无线电驱动之上实现自己的 L2。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_PHY_IEEE802154
```

**定义位置（Location）**：[`subsys/net/l2/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_PHY_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PHY_IEEE802154)。

<a id="CONFIG_NET_L2_CUSTOM_IEEE802154_MTU"></a>

## 400.88 `CONFIG_NET_L2_CUSTOM_IEEE802154_MTU`

**提示（Prompt）**：自定义 IEEE 802.15.4 第二层的最大传输单元（MTU）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_CUSTOM_IEEE802154 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
127
```

**定义位置（Location）**：[`subsys/net/l2/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 自定义 IEEE 802.15.4 第二层（Custom IEEE802154 L2）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_CUSTOM_IEEE802154`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_CUSTOM_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_DUMMY"></a>

## 400.89 `CONFIG_NET_L2_DUMMY`

**提示（Prompt）**：虚拟第二层（Dummy L2）

**说明（Help）**

添加虚拟第二层（Dummy L2）驱动。通常只有在 QEMU 中运行网络协议栈、模拟网络接口时才需要它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if !CONFIG_NET_L2_ETHERNET && CONFIG_NET_TEST
```

**被选择（Selected by）**

```text
CONFIG_NET_LOOPBACK
CONFIG_NET_CAPTURE_COOKED_MODE
CONFIG_WIREGUARD
```

**定义位置（Location）**：[`subsys/net/l2/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TEST)、[`CONFIG_NET_LOOPBACK`](P131_drivers_net_配置项参考.md#CONFIG_NET_LOOPBACK)、[`CONFIG_NET_CAPTURE_COOKED_MODE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_COOKED_MODE)、[`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)。

<a id="CONFIG_NET_L2_ETHERNET"></a>

## 400.90 `CONFIG_NET_L2_ETHERNET`

**提示（Prompt）**：以太网支持（Ethernet support）

**说明（Help）**

添加以太网第二层（Ethernet L2）支持。如果选择了 `NET_SLIP_TAP`，则 `NET_L2_ETHERNET` 允许通过串行线路互联网协议（SLIP）完整模拟以太网。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_ETH_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_WIFI_AMEBA
CONFIG_WIFI_BFLB
CONFIG_WIFI_ESP32
CONFIG_WIFI_ESP32_MESH_IP
CONFIG_WIFI_ESP_HOSTED
CONFIG_WIFI_ESP_HOSTED_MCU
CONFIG_WIFI_AIROC
CONFIG_WIFI_NXP
CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_NATIVE
CONFIG_WIFI_ST67W611M1
CONFIG_NET_SLIP_TAP
CONFIG_USB_DEVICE_NETWORK
```

**被弱选择（Implied by）**

```text
CONFIG_NET_QEMU_ETHERNET
CONFIG_NET_QEMU_USER
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_WIFI_AMEBA`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AMEBA)、[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI_ESP32_MESH_IP`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH_IP)、[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI_ESP_HOSTED_MCU`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED_MCU)、[`CONFIG_WIFI_AIROC`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_NATIVE`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X_NET_STACK_NATIVE)、[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_NET_SLIP_TAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SLIP_TAP)、[`CONFIG_USB_DEVICE_NETWORK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_NETWORK)、[`CONFIG_NET_QEMU_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QEMU_ETHERNET)、[`CONFIG_NET_QEMU_USER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QEMU_USER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USB_DEVICE_NETWORK`。

<a id="CONFIG_NET_L2_ETHERNET_ACCEPT_MISMATCH_L3_L2_ADDR"></a>

## 400.91 `CONFIG_NET_L2_ETHERNET_ACCEPT_MISMATCH_L3_L2_ADDR`

**提示（Prompt）**：接受第三层与第二层（L3/L2）地址不匹配的数据包

**说明（Help）**

启用后，即使数据包的 L3 和 L2 地址不符合 RFC 1122 第 3.3.6 节，也予以接受。此功能适用于与存在缺陷、未遵守 RFC 的设备交互。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM"></a>

## 400.92 `CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM`

**提示（Prompt）**：在发送（TX）的首个 `net_buf` 中预留额外空间

**说明（Help）**

启用后，允许以太网驱动在首个 `net_buf` 中、以太网报头之前预留额外空间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_ETHERNET_RESERVE_HEADER
```

**被选择（Selected by）**

```text
CONFIG_NRF_WIFI_ZERO_COPY_TX
CONFIG_NXP_WIFI_TX_RX_ZERO_COPY
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_ETHERNET_RESERVE_HEADER`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_ETHERNET_RESERVE_HEADER)、[`CONFIG_NRF_WIFI_ZERO_COPY_TX`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NRF_WIFI_ZERO_COPY_TX)、[`CONFIG_NXP_WIFI_TX_RX_ZERO_COPY`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_TX_RX_ZERO_COPY)。

<a id="CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE"></a>

## 400.93 `CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE`

**提示（Prompt）**：以太网第二层（Ethernet L2）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_L2_ETHERNET_LOG_LEVEL_OFF
CONFIG_NET_L2_ETHERNET_LOG_LEVEL_ERR
CONFIG_NET_L2_ETHERNET_LOG_LEVEL_WRN
CONFIG_NET_L2_ETHERNET_LOG_LEVEL_INF
CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DBG
CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DEFAULT`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_OFF`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_OFF)、[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_ERR`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_ERR)、[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_WRN`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_WRN)、[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_INF`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_INF)、[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DBG`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DBG"></a>

## 400.94 `CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网第二层（Ethernet L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DEFAULT"></a>

## 400.95 `CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网第二层（Ethernet L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_ETHERNET_LOG_LEVEL_ERR"></a>

## 400.96 `CONFIG_NET_L2_ETHERNET_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网第二层（Ethernet L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_ETHERNET_LOG_LEVEL_INF"></a>

## 400.97 `CONFIG_NET_L2_ETHERNET_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网第二层（Ethernet L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_ETHERNET_LOG_LEVEL_OFF"></a>

## 400.98 `CONFIG_NET_L2_ETHERNET_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网第二层（Ethernet L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_ETHERNET_LOG_LEVEL_WRN"></a>

## 400.99 `CONFIG_NET_L2_ETHERNET_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网第二层（Ethernet L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_ETHERNET_MCAST_FILTER_ADD_COUNT_GPTP"></a>

## 400.100 `CONFIG_NET_L2_ETHERNET_MCAST_FILTER_ADD_COUNT_GPTP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

gPTP 在每个端口上监听一个链路层多播地址（Link-layer multicast address），即最近网桥组地址 `01:80:C2:00:00:0E`。这些地址按网络接口分别跟踪，因此无论端口数量多少，每个接口一个表项就足够。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<!-- kconfig-navigation -->

[上一章](P399_subsys_net_配置项参考_9.md) · [返回大纲](大纲.md) · [下一章](P401_subsys_net_配置项参考_11.md)
