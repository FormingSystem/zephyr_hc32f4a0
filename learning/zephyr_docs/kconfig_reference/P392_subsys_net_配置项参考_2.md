---
id: learning.zephyr-docs.kconfig-reference.page-392
title: "`subsys/net`配置项参考（2/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第392章\_`subsys/net`配置项参考（2/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DNS_SERVER_IP_ADDRESSES"></a>

## 392.1 `CONFIG_DNS_SERVER_IP_ADDRESSES`

**提示（Prompt）**：设置 DNS 服务器 IP 地址

**说明（Help）**

允许在网络应用的配置文件中设置 DNS IP 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_SOCKET_DISPATCHER"></a>

## 392.2 `CONFIG_DNS_SOCKET_DISPATCHER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

DNS 套接字分发器（socket dispatcher），允许同时使用 DNS 解析器与组播 DNS（mDNS）响应器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_DNS_RESOLVER || CONFIG_MDNS_RESPONDER) && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS_SERVICE
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:529`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L529)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_MDNS_RESPONDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SERVICE)。

<a id="CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE"></a>

## 392.3 `CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：DNS 套接字分发器日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_DNS_SOCKET_DISPATCHER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_OFF
CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_ERR
CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_WRN
CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_INF
CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_DBG
CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_DNS_SOCKET_DISPATCHER`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_DEFAULT`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_DEFAULT)、[`CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_OFF`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_OFF)、[`CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_ERR`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_ERR)、[`CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_WRN`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_WRN)、[`CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_INF`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_INF)、[`CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_DBG`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_DBG)。

<a id="CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_DBG"></a>

## 392.4 `CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS 套接字分发器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_DEFAULT"></a>

## 392.5 `CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS 套接字分发器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_ERR"></a>

## 392.6 `CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS 套接字分发器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_INF"></a>

## 392.7 `CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS 套接字分发器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_OFF"></a>

## 392.8 `CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS 套接字分发器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_WRN"></a>

## 392.9 `CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS 套接字分发器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DSA_CONDUIT_PROMISC_ON"></a>

## 392.10 `CONFIG_DSA_CONDUIT_PROMISC_ON`

**提示（Prompt）**：使 DSA 上联接口以混杂模式运行（promiscuous mode）

**说明（Help）**

某些上联接口（conduits）通过入口过滤器（ingress filters），在软件看到数据包之前，就丢弃目的 MAC（DMAC）字段与接口所配置 MAC 不匹配的数据包。这类接口通常必须运行于混杂模式（promiscuous mode），才能确保 DSA 端口收到的数据包得到处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DSA && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_PROMISCUOUS_MODE
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/dsa/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/dsa/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 分布式交换架构支持（Distributed Switch Architecture）

**配置项引用（Symbol References）**：[`CONFIG_NET_DSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DSA)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_PROMISCUOUS_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PROMISCUOUS_MODE)。

<a id="CONFIG_DSA_PORT_MAX_COUNT"></a>

## 392.11 `CONFIG_DSA_PORT_MAX_COUNT`

**提示（Prompt）**：DSA 端口数量上限（port max count）

**说明（Help）**

设置 DSA 端口数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DSA && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/dsa/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/dsa/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 分布式交换架构支持（Distributed Switch Architecture）

**配置项引用（Symbol References）**：[`CONFIG_NET_DSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DSA)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DSA_TAG_SIZE"></a>

## 392.12 `CONFIG_DSA_TAG_SIZE`

**提示（Prompt）**：DSA 标签大小（字节，tag size）

**说明（Help）**

设置 DSA 标签长度，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DSA && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/dsa/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/dsa/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 分布式交换架构支持（Distributed Switch Architecture）

**配置项引用（Symbol References）**：[`CONFIG_NET_DSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DSA)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_ETHERNET_LOG_LEVEL_CHOICE"></a>

## 392.13 `CONFIG_ETHERNET_LOG_LEVEL_CHOICE`

**提示（Prompt）**：以太网驱动日志级别（Ethernet driver log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_ETHERNET_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ETHERNET_LOG_LEVEL_OFF
CONFIG_ETHERNET_LOG_LEVEL_ERR
CONFIG_ETHERNET_LOG_LEVEL_WRN
CONFIG_ETHERNET_LOG_LEVEL_INF
CONFIG_ETHERNET_LOG_LEVEL_DBG
CONFIG_ETHERNET_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_ETHERNET_LOG_LEVEL_DEFAULT`](P392_subsys_net_配置项参考_2.md#CONFIG_ETHERNET_LOG_LEVEL_DEFAULT)、[`CONFIG_ETHERNET_LOG_LEVEL_OFF`](P392_subsys_net_配置项参考_2.md#CONFIG_ETHERNET_LOG_LEVEL_OFF)、[`CONFIG_ETHERNET_LOG_LEVEL_ERR`](P392_subsys_net_配置项参考_2.md#CONFIG_ETHERNET_LOG_LEVEL_ERR)、[`CONFIG_ETHERNET_LOG_LEVEL_WRN`](P392_subsys_net_配置项参考_2.md#CONFIG_ETHERNET_LOG_LEVEL_WRN)、[`CONFIG_ETHERNET_LOG_LEVEL_INF`](P392_subsys_net_配置项参考_2.md#CONFIG_ETHERNET_LOG_LEVEL_INF)、[`CONFIG_ETHERNET_LOG_LEVEL_DBG`](P392_subsys_net_配置项参考_2.md#CONFIG_ETHERNET_LOG_LEVEL_DBG)。

<a id="CONFIG_ETHERNET_LOG_LEVEL_DBG"></a>

## 392.14 `CONFIG_ETHERNET_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHERNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网驱动日志级别（Ethernet driver log level）

**配置项引用（Symbol References）**：[`CONFIG_ETHERNET_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_ETHERNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ETHERNET_LOG_LEVEL_DEFAULT"></a>

## 392.15 `CONFIG_ETHERNET_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHERNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网驱动日志级别（Ethernet driver log level）

**配置项引用（Symbol References）**：[`CONFIG_ETHERNET_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_ETHERNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ETHERNET_LOG_LEVEL_ERR"></a>

## 392.16 `CONFIG_ETHERNET_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHERNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网驱动日志级别（Ethernet driver log level）

**配置项引用（Symbol References）**：[`CONFIG_ETHERNET_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_ETHERNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ETHERNET_LOG_LEVEL_INF"></a>

## 392.17 `CONFIG_ETHERNET_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHERNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网驱动日志级别（Ethernet driver log level）

**配置项引用（Symbol References）**：[`CONFIG_ETHERNET_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_ETHERNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ETHERNET_LOG_LEVEL_OFF"></a>

## 392.18 `CONFIG_ETHERNET_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHERNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网驱动日志级别（Ethernet driver log level）

**配置项引用（Symbol References）**：[`CONFIG_ETHERNET_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_ETHERNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ETHERNET_LOG_LEVEL_WRN"></a>

## 392.19 `CONFIG_ETHERNET_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ETHERNET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网驱动日志级别（Ethernet driver log level）

**配置项引用（Symbol References）**：[`CONFIG_ETHERNET_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_ETHERNET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FTP_CLIENT"></a>

## 392.20 `CONFIG_FTP_CLIENT`

**提示（Prompt）**：文件传输协议客户端（FTP client）【实验性 EXPERIMENTAL】

**说明（Help）**

启用符合 RFC 959 文件传输协议（File Transfer Protocol）的 FTP 客户端库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/ftp/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ftp/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_FTP_CLIENT_BUF_SIZE"></a>

## 392.21 `CONFIG_FTP_CLIENT_BUF_SIZE`

**提示（Prompt）**：FTP 客户端使用的缓冲区大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FTP_CLIENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[128, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/ftp/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ftp/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 文件传输协议客户端（FTP client）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_FTP_CLIENT`](P392_subsys_net_配置项参考_2.md#CONFIG_FTP_CLIENT)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_FTP_CLIENT_KEEPALIVE_TIME"></a>

## 392.22 `CONFIG_FTP_CLIENT_KEEPALIVE_TIME`

**提示（Prompt）**：连接后的保活时间（秒，keep-alive time）

**说明（Help）**

定义 FTP 客户端自动保活（keep-alive）时间，单位为秒。设为 `0` 禁用自动保活，可节省专用工作队列所需资源。禁用后，应用仍可通过 `ftp_keepalive()` 执行保活交互。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FTP_CLIENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
60
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/ftp/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ftp/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 文件传输协议客户端（FTP client）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_FTP_CLIENT`](P392_subsys_net_配置项参考_2.md#CONFIG_FTP_CLIENT)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_FTP_CLIENT_LISTEN_TIME"></a>

## 392.23 `CONFIG_FTP_CLIENT_LISTEN_TIME`

**提示（Prompt）**：接收 FTP 消息的轮询时间（秒）

**说明（Help）**

定义接收等待时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FTP_CLIENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/net/lib/ftp/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ftp/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 文件传输协议客户端（FTP client）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_FTP_CLIENT`](P392_subsys_net_配置项参考_2.md#CONFIG_FTP_CLIENT)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_TLS_CRED_SHELL"></a>

## 392.24 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_TLS_CRED_SHELL`

**提示（Prompt）**：TLS 凭据命令行内存池大小

**说明（Help）**

TLS 凭据命令行（credentials shell）使用的内存池大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TLS_CREDENTIALS_BACKEND_VOLATILE && CONFIG_TLS_CREDENTIALS_SHELL && CONFIG_TLS_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
6000
```

**定义位置（Location）**：[`subsys/net/lib/tls_credentials/Kconfig.shell:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tls_credentials/Kconfig.shell#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。 → TLS 凭据管理命令行（credentials management shell）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS_BACKEND_VOLATILE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS_BACKEND_VOLATILE)、[`CONFIG_TLS_CREDENTIALS_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS_SHELL)、[`CONFIG_TLS_CREDENTIALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_WIFI_CERT"></a>

## 392.25 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_WIFI_CERT`

原库同名定义共 2 条；本项为数据库第 7443 条记录，各定义分别保留。

**提示（Prompt）**：Wi-Fi 企业级安全证书内存池大小

**说明（Help）**

Wi-Fi 企业级安全证书（enterprise security certificates）使用的内存池大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES && CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
12000
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → 在运行时提供 Wi-Fi 企业级安全证书

**配置项引用（Symbol References）**：[`CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_WIFI_CERT--record-7444"></a>

## 392.26 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_WIFI_CERT`

原库同名定义共 2 条；本项为数据库第 7444 条记录，各定义分别保留。

**提示（Prompt）**：Wi-Fi 企业级安全证书内存池大小

**说明（Help）**

Wi-Fi 企业级安全证书（enterprise security certificates）使用的内存池大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_CREDENTIALS_RUNTIME_CERTIFICATES && CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_CREDENTIALS_CONNECT_STORED && CONFIG_WIFI_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
12000
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management） → 添加直接连接已存储网络的命令。 → 在运行时提供 Wi-Fi 企业级安全证书

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_RUNTIME_CERTIFICATES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CREDENTIALS_RUNTIME_CERTIFICATES)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_CREDENTIALS_CONNECT_STORED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CREDENTIALS_CONNECT_STORED)、[`CONFIG_WIFI_CREDENTIALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CREDENTIALS)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_CLIENT"></a>

## 392.27 `CONFIG_HTTP_CLIENT`

**提示（Prompt）**：HTTP客户端（Client）API。

**说明（Help）**

HTTP客户端（Client）API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_HTTP_PARSER
CONFIG_HTTP_PARSER_URL
```

**被选择（Selected by）**

```text
CONFIG_SIWX91X_FIRMWARE_UPGRADE_SHELL
CONFIG_WEBSOCKET_CLIENT
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_HTTP_PARSER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER)、[`CONFIG_HTTP_PARSER_URL`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER_URL)、[`CONFIG_SIWX91X_FIRMWARE_UPGRADE_SHELL`](P308_soc_silabs_配置项参考_1.md#CONFIG_SIWX91X_FIRMWARE_UPGRADE_SHELL)、[`CONFIG_WEBSOCKET_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CLIENT)。

<a id="CONFIG_HTTP_CLIENT_SEND_BUF_SIZE"></a>

## 392.28 `CONFIG_HTTP_CLIENT_SEND_BUF_SIZE`

**提示（Prompt）**：HTTP 客户端请求发送缓冲区大小

**说明（Help）**

HTTP 客户端构造并发送请求头（request headers）时使用的临时栈缓冲区大小。增大可减少套接字发送调用次数，但增加栈占用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_CLIENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
192
```

**取值范围（Ranges）**

```text
[64, 4096]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP客户端（Client）API。

**配置项引用（Symbol References）**：[`CONFIG_HTTP_CLIENT`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_CLIENT)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_PARSER"></a>

## 392.29 `CONFIG_HTTP_PARSER`

**提示（Prompt）**：HTTP 解析器支持（Parser support）

**说明（Help）**

启用来自 Node.js 的 `http_parser` 库。此解析器需要一些通常由 C 标准库（libc）提供的字符串处理例程。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_HTTP_PARSER_URL
```

**被选择（Selected by）**

```text
CONFIG_HTTP_CLIENT
CONFIG_HTTP_SERVER
CONFIG_WEBSOCKET_CLIENT
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_HTTP_PARSER_URL`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER_URL)、[`CONFIG_HTTP_CLIENT`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_CLIENT)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_WEBSOCKET_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CLIENT)。

<a id="CONFIG_HTTP_PARSER_MAX_HEADER_SIZE"></a>

## 392.30 `CONFIG_HTTP_PARSER_MAX_HEADER_SIZE`

**提示（Prompt）**：允许的 HTTP 头部最大大小

**说明（Help）**

配置允许的 HTTP 头部（header）最大大小。将此项设为很大的数，可实际移除头部大小限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_PARSER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
81920
```

**取值范围（Ranges）**

```text
[32, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_HTTP_PARSER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_PARSER_STRICT"></a>

## 392.31 `CONFIG_HTTP_PARSER_STRICT`

**提示（Prompt）**：HTTP 严格解析（strict parsing）

**说明（Help）**

启用严格解析选项（strict parsing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_HTTP_PARSER || CONFIG_HTTP_PARSER_URL) && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_HTTP_PARSER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER)、[`CONFIG_HTTP_PARSER_URL`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER_URL)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_PARSER_URL"></a>

## 392.32 `CONFIG_HTTP_PARSER_URL`

**提示（Prompt）**：URL 的 HTTP 解析器支持

**说明（Help）**

启用基于 Node.js 源码的 URI 解析器库，需要一些通常由 C 标准库（libc）提供的字符串处理例程。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_HTTP_PARSER
CONFIG_HTTP_CLIENT
CONFIG_HTTP_SERVER
CONFIG_WEBSOCKET_CLIENT
CONFIG_LWM2M
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_HTTP_PARSER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER)、[`CONFIG_HTTP_CLIENT`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_CLIENT)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_WEBSOCKET_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CLIENT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)。

<a id="CONFIG_HTTP_SERVER"></a>

## 392.33 `CONFIG_HTTP_SERVER`

**提示（Prompt）**：HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**说明（Help）**

支持 HTTP/1、HTTP/2 和 HTTP/3 服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_HTTP_PARSER
CONFIG_HTTP_PARSER_URL
CONFIG_EXPERIMENTAL
CONFIG_NET_SOCKETS
CONFIG_ZVFS
CONFIG_ZVFS_EVENTFD
```

**被选择（Selected by）**

```text
CONFIG_MCP_TRANSPORT_HTTP
```

**弱选择（Implies）**

```text
CONFIG_NET_IPV4_MAPPING_TO_IPV6 if CONFIG_NET_IPV4 && CONFIG_NET_IPV6
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_HTTP_PARSER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER)、[`CONFIG_HTTP_PARSER_URL`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER_URL)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_EVENTFD`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_EVENTFD)、[`CONFIG_MCP_TRANSPORT_HTTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_NET_IPV4_MAPPING_TO_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_MAPPING_TO_IPV6)、[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)。

<a id="CONFIG_HTTP_SERVER_CAPTURE_HEADERS"></a>

## 392.34 `CONFIG_HTTP_SERVER_CAPTURE_HEADERS`

**提示（Prompt）**：允许捕获 HTTP 头部供应用使用

**说明（Help）**

允许 HTTP 服务器捕获应用已注册的指定头部（headers）。对于一个请求，捕获的头部仅在首次调用动态资源回调（dynamic resource callback）时提供，后续回调均不可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_MCP_TRANSPORT_HTTP
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:213`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L213)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_MCP_TRANSPORT_HTTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCP_TRANSPORT_HTTP)。

<a id="CONFIG_HTTP_SERVER_CAPTURE_HEADER_BUFFER_SIZE"></a>

## 392.35 `CONFIG_HTTP_SERVER_CAPTURE_HEADER_BUFFER_SIZE`

**提示（Prompt）**：供应用使用的 HTTP 头部捕获缓冲区大小

**说明（Help）**

设置每个客户端用于保存 HTTP 头部、供应用稍后使用的缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER_CAPTURE_HEADERS && CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[32, 2048]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】 → 允许捕获 HTTP 头部供应用使用

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER_CAPTURE_HEADERS`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_CAPTURE_HEADERS)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_CAPTURE_HEADER_COUNT"></a>

## 392.36 `CONFIG_HTTP_SERVER_CAPTURE_HEADER_COUNT`

**提示（Prompt）**：单次请求可捕获的 HTTP 头部数量上限

**说明（Help）**

设置单个 HTTP 请求中，可捕获并供应用使用的 HTTP 头部数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER_CAPTURE_HEADERS && CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:231`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L231)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】 → 允许捕获 HTTP 头部供应用使用

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER_CAPTURE_HEADERS`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_CAPTURE_HEADERS)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_CLIENT_BUFFER_SIZE"></a>

## 392.37 `CONFIG_HTTP_SERVER_CLIENT_BUFFER_SIZE`

**提示（Prompt）**：客户端缓冲区大小（Client Buffer Size）

**说明（Help）**

设置每个客户端的缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[64, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_CLIENT_INACTIVITY_TIMEOUT"></a>

## 392.38 `CONFIG_HTTP_SERVER_CLIENT_INACTIVITY_TIMEOUT`

**提示（Prompt）**：客户端无活动超时（秒，inactivity timeout）

**说明（Help）**

客户端不发送也不接收数据的最大持续时间，超过后服务器断开连接。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5 if CONFIG_HTTP_SERVER_VERSION_3
10
```

**取值范围（Ranges）**

```text
[1, 86400]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:240`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L240)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_HTTP_SERVER_VERSION_3`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_3)。

<a id="CONFIG_HTTP_SERVER_COMPLETE_STATUS_PHRASES"></a>

## 392.39 `CONFIG_HTTP_SERVER_COMPLETE_STATUS_PHRASES`

**提示（Prompt）**：完整 HTTP 状态原因短语（status reason phrases）

**说明（Help）**

在服务器响应中包含 HTTP 状态码的原因短语（reason phrases）。禁用后不包含，可减小代码大小。HTTP 规范允许省略原因短语，缺少它们不影响协议符合性或客户端行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:329`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L329)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_COMPRESSION"></a>

## 392.40 `CONFIG_HTTP_SERVER_COMPRESSION`

**提示（Prompt）**：HTTP 文件服务器压缩支持（Compression support）

**说明（Help）**

启用后，文件服务器解析客户端的 `accept-encoding` 头部，提取其支持的压缩方式；随后按照以下顺序，依据文件扩展名识别压缩格式，提供第一个可用的压缩文件：

1. Brotli：`.br`。
2. gzip：`.gz`。
3. Zstandard（zstd）：`.zst`。
4. compress：`.lzw`。
5. deflate：`.zz`。
6. 未压缩文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:304`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L304)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_HTTP2_MAX_HEADER_FRAME_LEN"></a>

## 392.41 `CONFIG_HTTP_SERVER_HTTP2_MAX_HEADER_FRAME_LEN`

**提示（Prompt）**：HTTP/2 响应头帧最大长度（response header frame length）

**说明（Help）**

设置 HTTP/2 头帧的最大长度，仅适用于响应头，不适用于请求头。默认值足以容纳响应的标准头部；只有应用需要发送额外响应头时，才需要增大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[64, 2048]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_HUFFMAN_DECODE_BUFFER_SIZE"></a>

## 392.42 `CONFIG_HTTP_SERVER_HUFFMAN_DECODE_BUFFER_SIZE`

**提示（Prompt）**：解码霍夫曼编码字符串的缓冲区大小

**说明（Help）**

处理 HPACK 压缩头部时，解码霍夫曼编码（Huffman-encoded）字符串所用的缓冲区大小，实际上限制了支持的单个 HTTP 头部最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[64, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_MAX_CLIENTS"></a>

## 392.43 `CONFIG_HTTP_SERVER_MAX_CLIENTS`

**提示（Prompt）**：HTTP/2／HTTP/3 客户端数量上限

**说明（Help）**

设置服务器同时处理的 HTTP/2 或 HTTP/3 客户端数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_MAX_ENDPOINTS if CONFIG_HTTP_SERVER_VERSION_3
3
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_QUIC_MAX_ENDPOINTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_ENDPOINTS)、[`CONFIG_HTTP_SERVER_VERSION_3`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_3)。

<a id="CONFIG_HTTP_SERVER_MAX_CONTENT_TYPE_LENGTH"></a>

## 392.44 `CONFIG_HTTP_SERVER_MAX_CONTENT_TYPE_LENGTH`

**提示（Prompt）**：HTTP 内容类型最大长度（Content-Type Length）

**说明（Help）**

设置 HTTP `Content-Length` 字段的最大长度。译注：原文标题写 `Content-Type`，帮助正文写 `Content-Length`，此处保留差异，配置时请核对对应选项标识及源码。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[1, 128]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_MAX_HEADER_LEN"></a>

## 392.45 `CONFIG_HTTP_SERVER_MAX_HEADER_LEN`

**提示（Prompt）**：HTTP 头字段／值最大长度（Header Field/Value Length）

**说明（Help）**

设置可解析的 HTTP 头字段或值的最大长度。默认值足以满足 HTTP 服务器内部头部处理；应用需要访问更长头部时才需要增大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[32, 512]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_MAX_STREAMS"></a>

## 392.46 `CONFIG_HTTP_SERVER_MAX_STREAMS`

**提示（Prompt）**：HTTP/2 流数量上限（streams）

**说明（Help）**

设置每个客户端的 HTTP/2 流（streams）数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_MAX_URL_LENGTH"></a>

## 392.47 `CONFIG_HTTP_SERVER_MAX_URL_LENGTH`

**提示（Prompt）**：HTTP URL 最大长度

**说明（Help）**

设置服务器可处理的 HTTP URL 最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[32, 2048]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_NUM_SERVICES"></a>

## 392.48 `CONFIG_HTTP_SERVER_NUM_SERVICES`

**提示（Prompt）**：HTTP 服务器实例数量（Server Instances）

**说明（Help）**

设置服务器支持的 HTTP 服务数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_MAX_CONTEXTS if CONFIG_HTTP_SERVER_VERSION_3 && !CONFIG_HTTP_SERVER_VERSION_2 && !CONFIG_HTTP_SERVER_VERSION_1
3 if CONFIG_HTTP_SERVER_VERSION_3 && CONFIG_HTTP_SERVER_VERSION_2 && CONFIG_HTTP_SERVER_VERSION_1
2 if CONFIG_HTTP_SERVER_VERSION_3 && CONFIG_HTTP_SERVER_VERSION_2 && !CONFIG_HTTP_SERVER_VERSION_1
2 if CONFIG_HTTP_SERVER_VERSION_3 && !CONFIG_HTTP_SERVER_VERSION_2 && CONFIG_HTTP_SERVER_VERSION_1
2 if !CONFIG_HTTP_SERVER_VERSION_3 && CONFIG_HTTP_SERVER_VERSION_2 && CONFIG_HTTP_SERVER_VERSION_1
1
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_QUIC_MAX_CONTEXTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_MAX_CONTEXTS)、[`CONFIG_HTTP_SERVER_VERSION_3`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_3)、[`CONFIG_HTTP_SERVER_VERSION_2`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_2)、[`CONFIG_HTTP_SERVER_VERSION_1`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_1)。

<a id="CONFIG_HTTP_SERVER_REPORT_FAILURE_REASON"></a>

## 392.49 `CONFIG_HTTP_SERVER_REPORT_FAILURE_REASON`

**提示（Prompt）**：在 HTTP 500 内部服务器错误响应中报告失败原因

**说明（Help）**

启用后，服务器在 `HTTP 500 Internal Server Error` 响应中包含失败原因；否则，消息中不提供该信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:290`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L290)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_RESOURCE_WILDCARD"></a>

## 392.50 `CONFIG_HTTP_SERVER_RESOURCE_WILDCARD`

**提示（Prompt）**：允许资源通配符匹配（wildcard matching）

**说明（Help）**

允许用户在配置资源字符串时使用通配符（wildcards），这样单个资源处理函数（resource handler）就能处理多个 URL，而不必定义多个精确匹配资源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_POSIX_C_LIB_EXT
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:261`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L261)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_POSIX_C_LIB_EXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_C_LIB_EXT)。

<a id="CONFIG_HTTP_SERVER_RESTART_DELAY"></a>

## 392.51 `CONFIG_HTTP_SERVER_RESTART_DELAY`

**提示（Prompt）**：服务器重启时重新初始化前的延迟

**说明（Help）**

服务器因任何原因重启时，在重新初始化前等待此时间，单位为毫秒。延迟用于让现有连接完成收尾，以免初始化时发生绑定错误（binding errors）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[1, 60000]
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:270`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L270)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_STACK_SIZE"></a>

## 392.52 `CONFIG_HTTP_SERVER_STACK_SIZE`

**提示（Prompt）**：HTTP 服务器线程栈大小（thread stack size）

**说明（Help）**

处理接收／发送（RX/TX）事件的 HTTP 服务器线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4096 if CONFIG_FILE_SYSTEM
3072
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_HTTP_SERVER_STATIC_FS_RESPONSE_SIZE"></a>

## 392.53 `CONFIG_HTTP_SERVER_STATIC_FS_RESPONSE_SIZE`

**提示（Prompt）**：静态文件系统响应缓冲区大小

**说明（Help）**

从文件系统提供静态文件时，单个响应数据块（chunk）的大小。必须足够大，使头部能够装入一个块。设为 `0` 时，服务器采用响应所需的最小可用缓冲区大小。注意：此缓冲区在 HTTP 服务器线程栈上分配，因此 `CONFIG_HTTP_SERVER_STACK_SIZE` 必须足够大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM && CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:318`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L318)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_TLS_USE_ALPN"></a>

## 392.54 `CONFIG_HTTP_SERVER_TLS_USE_ALPN`

**提示（Prompt）**：HTTPS 服务器的应用层协议协商支持（ALPN）

**说明（Help）**

使用应用层协议协商（Application-Layer Protocol Negotiation，ALPN）为 TLS 连接协商 HTTP/2 或 HTTP/3。原文说明，浏览器使用此机制确定是否支持 HTTP/2 或 HTTP/3。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_HTTP_SERVER_VERSION_3
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L280)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_HTTP_SERVER_VERSION_3`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_3)。

<a id="CONFIG_HTTP_SERVER_TO_H3_UPGRADE"></a>

## 392.55 `CONFIG_HTTP_SERVER_TO_H3_UPGRADE`

**提示（Prompt）**：默认通告 HTTP/3 升级（Advertise upgrade）

**说明（Help）**

启用后，支持 HTTP/3 的服务在 HTTP/1 头部中发送：

```http
Alt-Svc: h3=":443"; ma=86400
```

客户端据此知道可以通过 HTTP/3 连接。各服务可在 `http_service_config` 中覆盖此默认设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER_VERSION_3 && CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER_VERSION_3`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_3)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_TO_H3_UPGRADE_MAX_AGE_SECS"></a>

## 392.56 `CONFIG_HTTP_SERVER_TO_H3_UPGRADE_MAX_AGE_SECS`

**提示（Prompt）**：HTTP/3 升级通告的最大有效期（秒，max age）

**说明（Help）**

默认为 1 天，即 86400 秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER_TO_H3_UPGRADE && CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
86400
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】 → 默认通告 HTTP/3 升级（Advertise upgrade）

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER_TO_H3_UPGRADE`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_TO_H3_UPGRADE)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_HTTP_SERVER_VERSION"></a>

## 392.57 `CONFIG_HTTP_SERVER_VERSION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

HTTP 服务器支持的 HTTP 版本。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
123 if CONFIG_HTTP_SERVER_VERSION_1 && CONFIG_HTTP_SERVER_VERSION_2 && CONFIG_HTTP_SERVER_VERSION_3
23 if !CONFIG_HTTP_SERVER_VERSION_1 && CONFIG_HTTP_SERVER_VERSION_2 && CONFIG_HTTP_SERVER_VERSION_3
13 if CONFIG_HTTP_SERVER_VERSION_1 && !CONFIG_HTTP_SERVER_VERSION_2 && CONFIG_HTTP_SERVER_VERSION_3
12 if CONFIG_HTTP_SERVER_VERSION_1 && CONFIG_HTTP_SERVER_VERSION_2 && !CONFIG_HTTP_SERVER_VERSION_3
3 if !CONFIG_HTTP_SERVER_VERSION_1 && !CONFIG_HTTP_SERVER_VERSION_2 && CONFIG_HTTP_SERVER_VERSION_3
2 if !CONFIG_HTTP_SERVER_VERSION_1 && CONFIG_HTTP_SERVER_VERSION_2 && !CONFIG_HTTP_SERVER_VERSION_3
1 if CONFIG_HTTP_SERVER_VERSION_1 && !CONFIG_HTTP_SERVER_VERSION_2 && !CONFIG_HTTP_SERVER_VERSION_3
0
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_HTTP_SERVER_VERSION_1`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_1)、[`CONFIG_HTTP_SERVER_VERSION_2`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_2)、[`CONFIG_HTTP_SERVER_VERSION_3`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_3)。

<a id="CONFIG_HTTP_SERVER_VERSION_1"></a>

## 392.58 `CONFIG_HTTP_SERVER_VERSION_1`

**提示（Prompt）**：HTTP/1.x 支持

**说明（Help）**

支持 HTTP/1.x 版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_TCP if CONFIG_NET_NATIVE
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE)。

<a id="CONFIG_HTTP_SERVER_VERSION_2"></a>

## 392.59 `CONFIG_HTTP_SERVER_VERSION_2`

**提示（Prompt）**：HTTP/2 支持

**说明（Help）**

支持 HTTP/2 版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_TCP if CONFIG_NET_NATIVE
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE)。

<a id="CONFIG_HTTP_SERVER_VERSION_3"></a>

## 392.60 `CONFIG_HTTP_SERVER_VERSION_3`

**提示（Prompt）**：HTTP/3 支持

**说明（Help）**

支持 HTTP/3 版本，依赖 QUIC 传输协议支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS)。

<a id="CONFIG_HTTP_SERVER_WEBSOCKET"></a>

## 392.61 `CONFIG_HTTP_SERVER_WEBSOCKET`

**提示（Prompt）**：允许升级为 WebSocket 连接

**说明（Help）**

启用后，用户可允许将 HTTP 连接升级为 WebSocket 连接，并定义在升级完成后调用的 WebSocket 处理函数（handler），以处理后续网络通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_SHA_1
CONFIG_WEBSOCKET_CLIENT
CONFIG_WEBSOCKET
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_PSA_WANT_ALG_SHA_1`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_1)、[`CONFIG_WEBSOCKET_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CLIENT)、[`CONFIG_WEBSOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET)。

<a id="CONFIG_LATMON_LOG_LEVEL_CHOICE"></a>

## 392.62 `CONFIG_LATMON_LOG_LEVEL_CHOICE`

**提示（Prompt）**：延迟监控服务（Latency monitoring Service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_LATMON && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LATMON_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LATMON_LOG_LEVEL_OFF
CONFIG_LATMON_LOG_LEVEL_ERR
CONFIG_LATMON_LOG_LEVEL_WRN
CONFIG_LATMON_LOG_LEVEL_INF
CONFIG_LATMON_LOG_LEVEL_DBG
CONFIG_LATMON_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_LATMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LATMON)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LATMON_LOG_LEVEL_DEFAULT`](P392_subsys_net_配置项参考_2.md#CONFIG_LATMON_LOG_LEVEL_DEFAULT)、[`CONFIG_LATMON_LOG_LEVEL_OFF`](P392_subsys_net_配置项参考_2.md#CONFIG_LATMON_LOG_LEVEL_OFF)、[`CONFIG_LATMON_LOG_LEVEL_ERR`](P392_subsys_net_配置项参考_2.md#CONFIG_LATMON_LOG_LEVEL_ERR)、[`CONFIG_LATMON_LOG_LEVEL_WRN`](P392_subsys_net_配置项参考_2.md#CONFIG_LATMON_LOG_LEVEL_WRN)、[`CONFIG_LATMON_LOG_LEVEL_INF`](P392_subsys_net_配置项参考_2.md#CONFIG_LATMON_LOG_LEVEL_INF)、[`CONFIG_LATMON_LOG_LEVEL_DBG`](P392_subsys_net_配置项参考_2.md#CONFIG_LATMON_LOG_LEVEL_DBG)。

<a id="CONFIG_LATMON_LOG_LEVEL_DBG"></a>

## 392.63 `CONFIG_LATMON_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LATMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】 → 延迟监控服务（Latency monitoring Service）

**配置项引用（Symbol References）**：[`CONFIG_LATMON_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_LATMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LATMON_LOG_LEVEL_DEFAULT"></a>

## 392.64 `CONFIG_LATMON_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LATMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】 → 延迟监控服务（Latency monitoring Service）

**配置项引用（Symbol References）**：[`CONFIG_LATMON_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_LATMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LATMON_LOG_LEVEL_ERR"></a>

## 392.65 `CONFIG_LATMON_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LATMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】 → 延迟监控服务（Latency monitoring Service）

**配置项引用（Symbol References）**：[`CONFIG_LATMON_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_LATMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LATMON_LOG_LEVEL_INF"></a>

## 392.66 `CONFIG_LATMON_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LATMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】 → 延迟监控服务（Latency monitoring Service）

**配置项引用（Symbol References）**：[`CONFIG_LATMON_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_LATMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LATMON_LOG_LEVEL_OFF"></a>

## 392.67 `CONFIG_LATMON_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LATMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】 → 延迟监控服务（Latency monitoring Service）

**配置项引用（Symbol References）**：[`CONFIG_LATMON_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_LATMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LATMON_LOG_LEVEL_WRN"></a>

## 392.68 `CONFIG_LATMON_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LATMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】 → 延迟监控服务（Latency monitoring Service）

**配置项引用（Symbol References）**：[`CONFIG_LATMON_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_LATMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLMNR_RESOLVER"></a>

## 392.69 `CONFIG_LLMNR_RESOLVER`

**提示（Prompt）**：链路本地组播名称解析支持（LLMNR）【已弃用 DEPRECATED】

**说明（Help）**

启用链路本地组播名称解析（Link-Local Multicast Name Resolution，LLMNR）客户端支持，详情参见 RFC 4795。LLMNR 通常由 Windows 主机使用。启用后，单标签名称查询发送到众所周知的组播地址 `224.0.0.252:5355` 或 `[ff02::1:3]:5355`，包含点号的查询仍使用配置的 DNS 服务器。

原文说明：LLMNR 正在逐步退出，Microsoft 正在弃用该协议；此选项已弃用，将在未来版本移除。应改用组播 DNS，即 `CONFIG_MDNS_RESOLVER`，或单播 DNS。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_LLMNR_RESOLVER_ADDITIONAL_BUF_CTR"></a>

## 392.70 `CONFIG_LLMNR_RESOLVER_ADDITIONAL_BUF_CTR`

**提示（Prompt）**：附加 DNS 缓冲区（Additional buffers）

**说明（Help）**

LLMNR 响应器可用的附加缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LLMNR_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:462`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L462)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → LLMNR 响应器（responder）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_LLMNR_RESPONDER`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LLMNR_RESPONDER"></a>

## 392.71 `CONFIG_LLMNR_RESPONDER`

**提示（Prompt）**：LLMNR 响应器（responder）【已弃用 DEPRECATED】

**说明（Help）**

为 Zephyr 启用链路本地组播名称解析（LLMNR）响应器，监听众所周知的地址 `ff02::1:3` 和 `224.0.0.252`。当前仅返回 IP 地址信息。必须将 `CONFIG_NET_HOSTNAME` 设为有意义的值，随后响应器才会回复 `<hostname>` 的 LLMNR 查询。查询应只含单标签名称，名称中不能有点号 `.`，见 RFC 4795 第 3 节。当前实现不支持 TCP，其他详情参见 RFC 4795。

原文说明：LLMNR 正在逐步退出，Microsoft 正在弃用该协议；此选项已弃用，将在未来版本移除。应改用 `CONFIG_MDNS_RESPONDER` 提供的 mDNS 响应器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_HOSTNAME_ENABLE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
CONFIG_NET_IPV4_IGMP if CONFIG_NET_IPV4
CONFIG_NET_IPV6_MLD if CONFIG_NET_IPV6
CONFIG_NET_SOCKETS
CONFIG_NET_SOCKETS_SERVICE
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:417`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L417)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NET_HOSTNAME_ENABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_HOSTNAME_ENABLE)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_NET_IPV4_IGMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_IGMP)、[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6_MLD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_MLD)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_NET_SOCKETS_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SERVICE)。

<a id="CONFIG_LLMNR_RESPONDER_INIT_PRIO"></a>

## 392.72 `CONFIG_LLMNR_RESPONDER_INIT_PRIO`

**提示（Prompt）**：LLMNR 响应器初始化的启动优先级

**说明（Help）**

启用 `NET_CONFIG_AUTO_INIT` 时，本值应大于其配置值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LLMNR_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
96
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:449`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L449)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → LLMNR 响应器（responder）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_LLMNR_RESPONDER`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE"></a>

## 392.73 `CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：LLMNR 响应器日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_LLMNR_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LLMNR_RESPONDER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LLMNR_RESPONDER_LOG_LEVEL_OFF
CONFIG_LLMNR_RESPONDER_LOG_LEVEL_ERR
CONFIG_LLMNR_RESPONDER_LOG_LEVEL_WRN
CONFIG_LLMNR_RESPONDER_LOG_LEVEL_INF
CONFIG_LLMNR_RESPONDER_LOG_LEVEL_DBG
CONFIG_LLMNR_RESPONDER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → LLMNR 响应器（responder）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_LLMNR_RESPONDER`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LLMNR_RESPONDER_LOG_LEVEL_DEFAULT`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER_LOG_LEVEL_DEFAULT)、[`CONFIG_LLMNR_RESPONDER_LOG_LEVEL_OFF`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER_LOG_LEVEL_OFF)、[`CONFIG_LLMNR_RESPONDER_LOG_LEVEL_ERR`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER_LOG_LEVEL_ERR)、[`CONFIG_LLMNR_RESPONDER_LOG_LEVEL_WRN`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER_LOG_LEVEL_WRN)、[`CONFIG_LLMNR_RESPONDER_LOG_LEVEL_INF`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER_LOG_LEVEL_INF)、[`CONFIG_LLMNR_RESPONDER_LOG_LEVEL_DBG`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER_LOG_LEVEL_DBG)。

<a id="CONFIG_LLMNR_RESPONDER_LOG_LEVEL_DBG"></a>

## 392.74 `CONFIG_LLMNR_RESPONDER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → LLMNR 响应器（responder）【已弃用 DEPRECATED】 → LLMNR 响应器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLMNR_RESPONDER_LOG_LEVEL_DEFAULT"></a>

## 392.75 `CONFIG_LLMNR_RESPONDER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → LLMNR 响应器（responder）【已弃用 DEPRECATED】 → LLMNR 响应器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLMNR_RESPONDER_LOG_LEVEL_ERR"></a>

## 392.76 `CONFIG_LLMNR_RESPONDER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → LLMNR 响应器（responder）【已弃用 DEPRECATED】 → LLMNR 响应器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLMNR_RESPONDER_LOG_LEVEL_INF"></a>

## 392.77 `CONFIG_LLMNR_RESPONDER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → LLMNR 响应器（responder）【已弃用 DEPRECATED】 → LLMNR 响应器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLMNR_RESPONDER_LOG_LEVEL_OFF"></a>

## 392.78 `CONFIG_LLMNR_RESPONDER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → LLMNR 响应器（responder）【已弃用 DEPRECATED】 → LLMNR 响应器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLMNR_RESPONDER_LOG_LEVEL_WRN"></a>

## 392.79 `CONFIG_LLMNR_RESPONDER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → LLMNR 响应器（responder）【已弃用 DEPRECATED】 → LLMNR 响应器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LLMNR_RESPONDER_TTL"></a>

## 392.80 `CONFIG_LLMNR_RESPONDER_TTL`

**提示（Prompt）**：返回的 DNS 名称生存时间（Time-to-Live）

**说明（Help）**

DNS 回答使用的生存时间（TTL），单位为秒。默认 30 秒，遵循 RFC 4795 第 2.8 节建议。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LLMNR_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:442`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L442)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → LLMNR 响应器（responder）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_LLMNR_RESPONDER`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M"></a>

## 392.81 `CONFIG_LWM2M`

**提示（Prompt）**：开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**说明（Help）**

添加管理 OMA 轻量级机器到机器（LwM2M）数据的逻辑。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_COAP
CONFIG_HTTP_PARSER_URL
CONFIG_NET_SOCKETS
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_HTTP_PARSER_URL`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER_URL)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)。

<a id="CONFIG_LWM2M_ACCESS_CONTROL_ENABLE"></a>

## 392.82 `CONFIG_LWM2M_ACCESS_CONTROL_ENABLE`

**提示（Prompt）**：访问控制支持（Access control，ID 2）

**说明（Help）**

启用后，注册访问控制对象（access control object）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:569`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L569)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_ACCESS_CONTROL_INSTANCE_COUNT"></a>

## 392.83 `CONFIG_LWM2M_ACCESS_CONTROL_INSTANCE_COUNT`

**提示（Prompt）**：LwM2M 访问控制对象实例数量上限

**说明（Help）**

设置客户端可用的 LwM2M 访问控制（Access Control）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:574`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L574)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 访问控制支持（Access control，ID 2）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_BINARYAPPDATA_DATA_INSTANCE_COUNT"></a>

## 392.84 `CONFIG_LWM2M_BINARYAPPDATA_DATA_INSTANCE_COUNT`

**提示（Prompt）**：二进制应用数据容器的数据资源实例数量上限

**说明（Help）**

设置客户端可用的二进制应用数据容器（BinaryAppDataContainer）数据资源实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_BINARYAPPDATA_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:710`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L710)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 二进制应用数据容器对象（BinaryAppDataContainer，ID 19）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_BINARYAPPDATA_OBJ_SUPPORT`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M_BINARYAPPDATA_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_BINARYAPPDATA_INSTANCE_COUNT"></a>

## 392.85 `CONFIG_LWM2M_BINARYAPPDATA_INSTANCE_COUNT`

**提示（Prompt）**：二进制应用数据容器对象实例数量上限

**说明（Help）**

设置客户端可用的二进制应用数据容器（BinaryAppDataContainer）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_BINARYAPPDATA_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:702`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L702)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 二进制应用数据容器对象（BinaryAppDataContainer，ID 19）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_BINARYAPPDATA_OBJ_SUPPORT`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M_BINARYAPPDATA_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_BINARYAPPDATA_OBJ_SUPPORT"></a>

## 392.86 `CONFIG_LWM2M_BINARYAPPDATA_OBJ_SUPPORT`

**提示（Prompt）**：LwM2M 二进制应用数据容器对象（BinaryAppDataContainer，ID 19）

**说明（Help）**

加入 LwM2M 二进制应用数据容器对象（BinaryAppDataContainer Object）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:696`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L696)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_CACHE_DROP_LATEST"></a>

## 392.87 `CONFIG_LWM2M_CACHE_DROP_LATEST`

**提示（Prompt）**：缓存满时丢弃新数据（Drop new data）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 资源时间序列数据缓存支持（Resource Time series data cache） → 缓存满时的策略（Cache full policy）

<a id="CONFIG_LWM2M_CACHE_DROP_OLDEST"></a>

## 392.88 `CONFIG_LWM2M_CACHE_DROP_OLDEST`

**提示（Prompt）**：缓存满时丢弃最旧数据（Drop oldest data）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 资源时间序列数据缓存支持（Resource Time series data cache） → 缓存满时的策略（Cache full policy）

<a id="CONFIG_LWM2M_CANCEL_OBSERVE_BY_PATH"></a>

## 392.89 `CONFIG_LWM2M_CANCEL_OBSERVE_BY_PATH`

**提示（Prompt）**：取消观察时以路径匹配作为回退方式（cancel-observe）

**说明（Help）**

LwM2M 规范中的部分模糊表述，使某些服务器通过指定资源路径而非原始观察请求的令牌（token）实现取消观察（cancel-observe）。未启用本项时，连接这些服务器的取消观察操作可能无法正常工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_COAP_BLOCK_SIZE"></a>

## 392.90 `CONFIG_LWM2M_COAP_BLOCK_SIZE`

**提示（Prompt）**：LwM2M CoAP 分块传输大小（block-wise transfer size）

**说明（Help）**

LwM2M 执行 CoAP 分块传输时使用的块大小，可选 `64`、`128`、`256`、`512` 和 `1024`。调整时必须确保 `LWM2M_COAP_MAX_MSG_SIZE` 足以容纳全部 CoAP 头部和完整数据块。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[64, 1024]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:298`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L298)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_COAP_BLOCK_TRANSFER"></a>

## 392.91 `CONFIG_LWM2M_COAP_BLOCK_TRANSFER`

**提示（Prompt）**：大型出站 LwM2M 消息的 CoAP 分块传输支持【实验性 EXPERIMENTAL】

**说明（Help）**

正文超过块大小的 LwM2M 消息会拆分为多个块发送。若要在出站分块传输中附加 CoAP 实体标签（ETag）选项，应启用 `CONFIG_SYS_HASH_FUNC32`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_LWM2M_COAP_ENCODE_BUFFER_SIZE"></a>

## 392.92 `CONFIG_LWM2M_COAP_ENCODE_BUFFER_SIZE`

**提示（Prompt）**：为分块传输编码完整消息的 LwM2M CoAP 缓冲区大小

**说明（Help）**

用于序列化大型 LwM2M CoAP 消息的缓冲区大小，这些消息需要分块发送。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_COAP_BLOCK_TRANSFER && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:393`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L393)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_COAP_BLOCK_TRANSFER`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M_COAP_BLOCK_TRANSFER)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_COAP_MAX_MSG_SIZE"></a>

## 392.93 `CONFIG_LWM2M_COAP_MAX_MSG_SIZE`

**提示（Prompt）**：LwM2M CoAP 消息最大大小（maximum message size）

**说明（Help）**

LwM2M 使用的 CoAP 消息大小。默认按 IPv6 网络的最大数据包大小计算：

```text
MTU(1280)-IPv6(40)-UDP(8)-DTLS(29..53)
```

即最大传输单元（MTU）减去 IPv6、UDP 和 DTLS 的相应开销。网络 MTU 更小时，应相应调整。启用 CoAP 分块传输后，此值应大于块大小与预计 CoAP 头部大小之和。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1232 if !CONFIG_LWM2M_DTLS_SUPPORT
1195 if CONFIG_LWM2M_DTLS_SUPPORT && !CONFIG_LWM2M_DTLS_CID
1187 if CONFIG_LWM2M_DTLS_SUPPORT && CONFIG_LWM2M_DTLS_CID
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:308`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L308)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M_DTLS_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_DTLS_SUPPORT)、[`CONFIG_LWM2M_DTLS_CID`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_DTLS_CID)。

<a id="CONFIG_LWM2M_COMPOSITE_PATH_LIST_SIZE"></a>

## 392.94 `CONFIG_LWM2M_COMPOSITE_PATH_LIST_SIZE`

**提示（Prompt）**：复合读取与发送操作的 URL 路径数量上限

**说明（Help）**

定义复合读取（Composite Read）及发送操作的路径列表大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
6
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:428`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L428)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_CONNMON_OBJECT_VERSION_1_0"></a>

## 392.95 `CONFIG_LWM2M_CONNMON_OBJECT_VERSION_1_0`

**提示（Prompt）**：连接监控对象版本 1.0（Connectivity monitor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:594`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L594)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 连接监控对象支持（Connectivity Monitoring，ID 4） → LwM2M 连接监控对象版本（object version）

<a id="CONFIG_LWM2M_CONNMON_OBJECT_VERSION_1_2"></a>

## 392.96 `CONFIG_LWM2M_CONNMON_OBJECT_VERSION_1_2`

**提示（Prompt）**：连接监控对象版本 1.2（Connectivity monitor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:597`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L597)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 连接监控对象支持（Connectivity Monitoring，ID 4） → LwM2M 连接监控对象版本（object version）

<a id="CONFIG_LWM2M_CONNMON_OBJECT_VERSION_1_3"></a>

## 392.97 `CONFIG_LWM2M_CONNMON_OBJECT_VERSION_1_3`

**提示（Prompt）**：连接监控对象版本 1.3（Connectivity monitor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:600`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L600)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 连接监控对象支持（Connectivity Monitoring，ID 4） → LwM2M 连接监控对象版本（object version）

<a id="CONFIG_LWM2M_CONN_MON_APN_MAX"></a>

## 392.98 `CONFIG_LWM2M_CONN_MON_APN_MAX`

**提示（Prompt）**：接入点名称资源实例数量上限（APN）

**说明（Help）**

设置接入点名称（APN）资源实例数量上限，通过连接监控（Connection Monitoring）对象的 `/4/0/7` 资源呈现。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_CONN_MON_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:613`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L613)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 连接监控对象支持（Connectivity Monitoring，ID 4）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_CONN_MON_OBJ_SUPPORT`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M_CONN_MON_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_CONN_MON_BEARER_MAX"></a>

## 392.99 `CONFIG_LWM2M_CONN_MON_BEARER_MAX`

**提示（Prompt）**：可用网络承载资源实例数量上限

**说明（Help）**

设置可用网络承载（network bearer）资源实例数量上限，通过连接监控（Connection Monitoring）对象的 `/4/0/1` 资源呈现。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_CONN_MON_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:605`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L605)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 连接监控对象支持（Connectivity Monitoring，ID 4）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_CONN_MON_OBJ_SUPPORT`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M_CONN_MON_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_CONN_MON_OBJ_SUPPORT"></a>

## 392.100 `CONFIG_LWM2M_CONN_MON_OBJ_SUPPORT`

**提示（Prompt）**：连接监控对象支持（Connectivity Monitoring，ID 4）

**说明（Help）**

加入 LwM2M 连接监控对象（Connectivity Monitoring Object）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:581`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L581)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<!-- kconfig-navigation -->

[上一章](P391_subsys_net_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P393_subsys_net_配置项参考_3.md)
