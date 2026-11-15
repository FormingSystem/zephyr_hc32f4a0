---
id: learning.zephyr-docs.kconfig-reference.page-401
title: "`subsys/net`配置项参考（11/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第401章\_`subsys/net`配置项参考（11/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_L2_ETHERNET_MCAST_FILTER_ADD_COUNT_IPV4"></a>

## 401.1 `CONFIG_NET_L2_ETHERNET_MCAST_FILTER_ADD_COUNT_IPV4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

每个加入的 IPv4 多播地址（Multicast address）都需要以太网接口上的一个链路层多播地址。多个 IPv4 地址可能映射到同一链路层地址，因此此数值是上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IF_MCAST_IPV4_ADDR_COUNT
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IF_MCAST_IPV4_ADDR_COUNT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_MCAST_IPV4_ADDR_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_L2_ETHERNET_MCAST_FILTER_ADD_COUNT_IPV6"></a>

## 401.2 `CONFIG_NET_L2_ETHERNET_MCAST_FILTER_ADD_COUNT_IPV6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

每个加入的 IPv6 多播地址（Multicast address）都需要以太网接口上的一个链路层多播地址，包括所有节点组（All-nodes group），以及接口上每个地址对应的请求节点组（Solicited-node group）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IF_MCAST_IPV6_ADDR_COUNT
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IF_MCAST_IPV6_ADDR_COUNT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_MCAST_IPV6_ADDR_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_L2_ETHERNET_MCAST_FILTER_ADD_COUNT_LLDP"></a>

## 401.3 `CONFIG_NET_L2_ETHERNET_MCAST_FILTER_ADD_COUNT_LLDP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

链路层发现协议（LLDP）在已注册接收回调的接口上监听一个链路层多播地址，即最近网桥组地址 `01:80:C2:00:00:0E`。这些地址按网络接口分别跟踪，因此每个接口一个表项就足够。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_ETHERNET_MCAST_FILTER_ADD_COUNT_PACKET_SOCKET"></a>

## 401.4 `CONFIG_NET_L2_ETHERNET_MCAST_FILTER_ADD_COUNT_PACKET_SOCKET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

每个数据包套接字的多播成员关系（Packet socket multicast membership）都需要以太网接口上的一个链路层多播地址。两个套接字加入同一组时共享一个地址，因此此数值是上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP && CONFIG_NET_L2_ETHERNET && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP_COUNT
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:435`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L435)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 数据包套接字（Packet socket）支持 → 数据包套接字多播成员关系（Packet socket multicast membership）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP_COUNT)。

<a id="CONFIG_NET_L2_ETHERNET_MCAST_FILTER_COUNT"></a>

## 401.5 `CONFIG_NET_L2_ETHERNET_MCAST_FILTER_COUNT`

**提示（Prompt）**：每个网络接口的第二层多播地址（L2 multicast address）最少数量

**说明（Help）**

一个以太网接口可同时监听的链路层多播地址（Link-layer multicast address）的最少数量。以太网第二层（Ethernet L2）跟踪这些地址，使驱动只在某组迎来第一个使用者或最后一个使用者退出时，才修改接收过滤器（Receive filter）。IP 层多播组和数据包套接字的多播成员关系均存储在此处；多个 IP 多播地址可以映射到同一链路层地址。每个需要此类地址的子系统通过自己的 `NET_L2_ETHERNET_MCAST_FILTER_ADD_COUNT_` 选项声明可能使用的地址数。构建时将这些数值相加，再取总和与本选项的较大值。因此，只有应用需要的地址数超过各子系统请求的总量时，才需要设置本选项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_ETHERNET_MGMT"></a>

## 401.6 `CONFIG_NET_L2_ETHERNET_MGMT`

**提示（Prompt）**：以太网网络管理接口（Ethernet network management interface）

**说明（Help）**

启用 `net_mgmt` 以太网接口支持，可在运行时配置以太网驱动及第二层（L2）设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
```

**被选择（Selected by）**

```text
CONFIG_ETH_LAN865X
CONFIG_WIFI_BFLB
CONFIG_WIFI_ESP32
CONFIG_WIFI_NRF70
CONFIG_WIFI_NXP
CONFIG_NET_QBV
CONFIG_NET_PROMISCUOUS_MODE
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_ETH_LAN865X`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_LAN865X)、[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI_NRF70`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_NET_QBV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QBV)、[`CONFIG_NET_PROMISCUOUS_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PROMISCUOUS_MODE)。

<a id="CONFIG_NET_L2_ETHERNET_RESERVE_HEADER"></a>

## 401.7 `CONFIG_NET_L2_ETHERNET_RESERVE_HEADER`

**提示（Prompt）**：在发送（TX）的首个 `net_buf` 中预留以太网报头空间

**说明（Help）**

启用后，发送数据时在首个 `net_buf` 中预留以太网报头（Ethernet header）空间。默认仍将第二层报头放在单独的 `net_buf` 中。接收（RX）端的以太网报头始终位于首个 `net_buf` 内。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM)。

<a id="CONFIG_NET_L2_IEEE802154"></a>

## 401.8 `CONFIG_NET_L2_IEEE802154`

**提示（Prompt）**：IEEE 802.15.4 无线电（Radio）

**说明（Help）**

添加低速率无线个域网（Low-rate WPAN）IEEE 802.15.4 技术支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_PHY_IEEE802154
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_PHY_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PHY_IEEE802154)。

<a id="CONFIG_NET_L2_IEEE802154_FRAGMENT"></a>

## 401.9 `CONFIG_NET_L2_IEEE802154_FRAGMENT`

**提示（Prompt）**：IEEE 802.15.4 分片（Fragmentation）支持

**说明（Help）**

如果 IPv6 数据包大小超过 IEEE 802.15.4 的最大传输单元（MTU），则按照 RFC 4944/6282 对发送的数据包分片（Fragmentation），并重组（Reassembly）收到的数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_6LO && CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio）

**配置项引用（Symbol References）**：[`CONFIG_NET_6LO`](P395_subsys_net_配置项参考_5.md#CONFIG_NET_6LO)、[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_IEEE802154_FRAGMENT_REASS_CACHE_SIZE"></a>

## 401.10 `CONFIG_NET_L2_IEEE802154_FRAGMENT_REASS_CACHE_SIZE`

**提示（Prompt）**：IEEE 802.15.4 重组缓存（Reassembly cache）大小

**说明（Help）**

根据缓存大小，同时重组（Reassemble）多个 IEEE 802.15.4 分片。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154_FRAGMENT && CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 分片（Fragmentation）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_FRAGMENT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_FRAGMENT)、[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE"></a>

## 401.11 `CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IEEE 802.15.4 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_L2_IEEE802154_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_L2_IEEE802154_LOG_LEVEL_OFF
CONFIG_NET_L2_IEEE802154_LOG_LEVEL_ERR
CONFIG_NET_L2_IEEE802154_LOG_LEVEL_WRN
CONFIG_NET_L2_IEEE802154_LOG_LEVEL_INF
CONFIG_NET_L2_IEEE802154_LOG_LEVEL_DBG
CONFIG_NET_L2_IEEE802154_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_IEEE802154_LOG_LEVEL_DEFAULT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_L2_IEEE802154_LOG_LEVEL_OFF`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_LOG_LEVEL_OFF)、[`CONFIG_NET_L2_IEEE802154_LOG_LEVEL_ERR`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_LOG_LEVEL_ERR)、[`CONFIG_NET_L2_IEEE802154_LOG_LEVEL_WRN`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_LOG_LEVEL_WRN)、[`CONFIG_NET_L2_IEEE802154_LOG_LEVEL_INF`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_LOG_LEVEL_INF)、[`CONFIG_NET_L2_IEEE802154_LOG_LEVEL_DBG`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_L2_IEEE802154_LOG_LEVEL_DBG"></a>

## 401.12 `CONFIG_NET_L2_IEEE802154_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_IEEE802154_LOG_LEVEL_DEFAULT"></a>

## 401.13 `CONFIG_NET_L2_IEEE802154_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_IEEE802154_LOG_LEVEL_ERR"></a>

## 401.14 `CONFIG_NET_L2_IEEE802154_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_IEEE802154_LOG_LEVEL_INF"></a>

## 401.15 `CONFIG_NET_L2_IEEE802154_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_IEEE802154_LOG_LEVEL_OFF"></a>

## 401.16 `CONFIG_NET_L2_IEEE802154_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_IEEE802154_LOG_LEVEL_WRN"></a>

## 401.17 `CONFIG_NET_L2_IEEE802154_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_IEEE802154_RADIO_ALOHA"></a>

## 401.18 `CONFIG_NET_L2_IEEE802154_RADIO_ALOHA`

**提示（Prompt）**：IEEE 802.15.4 Aloha 介质访问协议（Medium access protocol；CCA 模式 4）

**说明（Help）**

使用 Aloha 机制发送数据包，即不执行空闲信道评估（Clear Channel Assessment，CCA）便发送。这是一种简单的发送方式，适用于无线电频谱负载不太高的低占空比（Low duty-cycle）场景，参见 IEEE 802.15.4-2020 第 10.2.8 节。当前实现未对信道访问进行随机化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig.radio:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig.radio#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 无线电（Radio） → 无线电信道访问协议（Radio channel access protocol）

<a id="CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA"></a>

## 401.19 `CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA`

**提示（Prompt）**：IEEE 802.15.4 非时隙 CSMA-CA 介质访问协议（Unslotted CSMA-CA medium access protocol）

**说明（Help）**

使用载波侦听多路访问与冲突避免（CSMA-CA）机制发送数据包，即先听后发（Listen-before-talk）并采用指数退避（Exponential backoff）。这是协调无线电信道访问最常见的方式，适用于大多数场景，参见 IEEE 802.15.4-2020 第 6.2.5.1 节和第 10.2.8 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig.radio:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig.radio#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 无线电（Radio） → 无线电信道访问协议（Radio channel access protocol）

<a id="CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MAX_BE"></a>

## 401.20 `CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MAX_BE`

**提示（Prompt）**：CSMA MAC 最大退避指数（Maximum Backoff Exponent）

**说明（Help）**

CSMA-CA 算法中的退避指数（Backoff Exponent，BE）最大值，对应 MAC 协议信息库（PIB）属性 `macMaxBe`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA && CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[3, 8]
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig.radio:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig.radio#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 无线电（Radio）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA)、[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MAX_BO"></a>

## 401.21 `CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MAX_BO`

**提示（Prompt）**：CSMA 最大退避次数（Maximum Backoffs）

**说明（Help）**

CSMA-CA 算法在判定信道访问失败前尝试退避（Backoff）的最大次数，对应 MAC 协议信息库（PIB）属性 `macMaxCSMABackoffs`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA && CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[0, 5]
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig.radio:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig.radio#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 无线电（Radio）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA)、[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MIN_BE"></a>

## 401.22 `CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MIN_BE`

**提示（Prompt）**：CSMA MAC 最小退避指数（Minimum Backoff Exponent）

**说明（Help）**

CSMA-CA 算法中的退避指数（Backoff Exponent，BE）最小值，对应 MAC 协议信息库（PIB）属性 `macMinBe`。该值必须小于或等于 `NET_L2_IEEE802154_RADIO_CSMA_CA_MAX_BE`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA && CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 8]
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig.radio:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig.radio#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 无线电（Radio）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA)、[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_IEEE802154_RADIO_DFLT_TX_POWER"></a>

## 401.23 `CONFIG_NET_L2_IEEE802154_RADIO_DFLT_TX_POWER`

**提示（Prompt）**：无线电默认发送功率（Transmission power）

**说明（Help）**

发送（TX）功率，单位为 dBm。有效值为 -18、-7、-4、-2、0、1、2、3、5。设置错误时会静默失败，不报告错误。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig.radio:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig.radio#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 无线电（Radio）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_IEEE802154_RADIO_TX_RETRIES"></a>

## 401.24 `CONFIG_NET_L2_IEEE802154_RADIO_TX_RETRIES`

**提示（Prompt）**：无线电重传尝试次数（Retransmission attempts）

**说明（Help）**

无线电驱动在报告无法发送数据包前应执行的重传次数，对应 MAC 协议信息库（PIB）属性 `macMaxFrameRetries`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig.radio:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig.radio#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 无线电（Radio）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_IEEE802154_REASSEMBLY_TIMEOUT"></a>

## 401.25 `CONFIG_NET_L2_IEEE802154_REASSEMBLY_TIMEOUT`

**提示（Prompt）**：IEEE 802.15.4 重组超时（Reassembly timeout，秒）

**说明（Help）**

收到对端的第一个数据包时启动重组计时器（Reassembly timer）。必须在指定时间内完成重组，否则丢弃已积累的全部分片。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154_FRAGMENT && CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 60]
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 分片（Fragmentation）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_FRAGMENT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_FRAGMENT)、[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_IEEE802154_RFD"></a>

## 401.26 `CONFIG_NET_L2_IEEE802154_RFD`

**提示（Prompt）**：支持精简功能设备（Reduced Functionality Device，RFD）级别

**说明（Help）**

此级别适用于个域网（PAN）设备，而非 PAN 协调器（Coordinator）。它支持主动扫描、被动扫描，以及与 PAN 关联和解除关联（Association/Disassociation）。当前支持尚不稳健，因此未设为默认级别。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_IEEE802154_MGMT
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → 设备功能级别（Device features level）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_MGMT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_L2_IEEE802154_MGMT`。

<a id="CONFIG_NET_L2_IEEE802154_SECURITY"></a>

## 401.27 `CONFIG_NET_L2_IEEE802154_SECURITY`

**提示（Prompt）**：IEEE 802.15.4 安全（Security）［实验性，Experimental］

**说明（Help）**

启用 IEEE 802.15.4 帧安全处理，以提供数据机密性（Confidentiality）和真实性（Authenticity）。实现尚不完整，例如仅支持隐式密钥模式（Implicit key mode）、没有针对特定密钥或设备的状态、收发安全流程仅部分实现等。因此，该功能应视为仍在开发中的实验性功能（Experimental）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_NET_L2_IEEE802154_SECURITY_CRYPTO_DEV_NAME"></a>

## 401.28 `CONFIG_NET_L2_IEEE802154_SECURITY_CRYPTO_DEV_NAME`

**提示（Prompt）**：用于加密与解密（Encryption/Decryption）的密码设备名称

**说明（Help）**

设置 IEEE 802.15.4 软件 MAC（Soft MAC）使用的密码设备（Crypto device）名称，以对接收和发送的帧执行认证（Authentication）、加密（Encryption）及解密（Decryption）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154_SECURITY && CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 安全（Security）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_SECURITY`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_SECURITY)、[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_IEEE802154_SHELL"></a>

## 401.29 `CONFIG_NET_L2_IEEE802154_SHELL`

**提示（Prompt）**：IEEE 802.15.4 命令行模块（Shell module）

**说明（Help）**

提供名为 `ieee15_4` 的命令行模块（Shell module），用于通过控制台测试 IEEE 802.15.4。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154_RFD && CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_RFD`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_RFD)、[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)。

<a id="CONFIG_NET_L2_IPIP"></a>

## 401.30 `CONFIG_NET_L2_IPIP`

**提示（Prompt）**：IP 到 IP 隧道（IP-to-IP tunneling）支持

**说明（Help）**

添加 IP 到 IP 隧道（IP-to-IP tunnel，IPIP）驱动。启用后，将创建一个网络接口，在现有网络接口之上通过隧道传送流量。应用需要在运行时将 IPIP 驱动连接到正确的网络接口，并为 IP 到 IP 接口设置 IP 地址等参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_VIRTUAL && CONFIG_NET_L2_VIRTUAL && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_CAPTURE
```

**定义位置（Location）**：[`subsys/net/l2/virtual/ipip/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/virtual/ipip/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_VIRTUAL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)。

<a id="CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE"></a>

## 401.31 `CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IP 到 IP 隧道（IP-to-IP tunnel）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_L2_IPIP && CONFIG_NET_L2_VIRTUAL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_L2_IPIP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_L2_IPIP_LOG_LEVEL_OFF
CONFIG_NET_L2_IPIP_LOG_LEVEL_ERR
CONFIG_NET_L2_IPIP_LOG_LEVEL_WRN
CONFIG_NET_L2_IPIP_LOG_LEVEL_INF
CONFIG_NET_L2_IPIP_LOG_LEVEL_DBG
CONFIG_NET_L2_IPIP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → IP 到 IP 隧道（IP-to-IP tunneling）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_L2_IPIP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP)、[`CONFIG_NET_L2_VIRTUAL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_IPIP_LOG_LEVEL_DEFAULT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_L2_IPIP_LOG_LEVEL_OFF`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_OFF)、[`CONFIG_NET_L2_IPIP_LOG_LEVEL_ERR`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_ERR)、[`CONFIG_NET_L2_IPIP_LOG_LEVEL_WRN`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_WRN)、[`CONFIG_NET_L2_IPIP_LOG_LEVEL_INF`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_INF)、[`CONFIG_NET_L2_IPIP_LOG_LEVEL_DBG`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_L2_IPIP_LOG_LEVEL_DBG"></a>

## 401.32 `CONFIG_NET_L2_IPIP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → IP 到 IP 隧道（IP-to-IP tunneling）支持 → IP 到 IP 隧道（IP-to-IP tunnel）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_IPIP_LOG_LEVEL_DEFAULT"></a>

## 401.33 `CONFIG_NET_L2_IPIP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → IP 到 IP 隧道（IP-to-IP tunneling）支持 → IP 到 IP 隧道（IP-to-IP tunnel）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_IPIP_LOG_LEVEL_ERR"></a>

## 401.34 `CONFIG_NET_L2_IPIP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → IP 到 IP 隧道（IP-to-IP tunneling）支持 → IP 到 IP 隧道（IP-to-IP tunnel）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_IPIP_LOG_LEVEL_INF"></a>

## 401.35 `CONFIG_NET_L2_IPIP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → IP 到 IP 隧道（IP-to-IP tunneling）支持 → IP 到 IP 隧道（IP-to-IP tunnel）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_IPIP_LOG_LEVEL_OFF"></a>

## 401.36 `CONFIG_NET_L2_IPIP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → IP 到 IP 隧道（IP-to-IP tunneling）支持 → IP 到 IP 隧道（IP-to-IP tunnel）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_IPIP_LOG_LEVEL_WRN"></a>

## 401.37 `CONFIG_NET_L2_IPIP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → IP 到 IP 隧道（IP-to-IP tunneling）支持 → IP 到 IP 隧道（IP-to-IP tunnel）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_IPIP_TUNNEL_COUNT"></a>

## 401.38 `CONFIG_NET_L2_IPIP_TUNNEL_COUNT`

**提示（Prompt）**：IPIP 隧道（Tunnel）的最大数量

**说明（Help）**

指定支持的 IPIP 隧道（Tunnel）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IPIP && CONFIG_NET_L2_VIRTUAL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/l2/virtual/ipip/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/virtual/ipip/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → IP 到 IP 隧道（IP-to-IP tunneling）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IPIP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP)、[`CONFIG_NET_L2_VIRTUAL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_IPIP_TXRX_DEBUG"></a>

## 401.39 `CONFIG_NET_L2_IPIP_TXRX_DEBUG`

**提示（Prompt）**：调试接收和发送的数据包（Packet）

**说明（Help）**

启用后，打印接收和发送的网络数据包。这可能产生大量输出，因此默认禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IPIP_LOG_LEVEL_DBG && CONFIG_NET_L2_IPIP && CONFIG_NET_L2_VIRTUAL && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/virtual/ipip/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/virtual/ipip/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → IP 到 IP 隧道（IP-to-IP tunneling）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IPIP_LOG_LEVEL_DBG`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP_LOG_LEVEL_DBG)、[`CONFIG_NET_L2_IPIP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IPIP)、[`CONFIG_NET_L2_VIRTUAL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_OPENTHREAD"></a>

## 401.40 `CONFIG_NET_L2_OPENTHREAD`

**提示（Prompt）**：OpenThread 第二层（L2）

**说明（Help）**

使用 Zephyr 提供的 OpenThread 第二层（L2）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_OPENTHREAD
CONFIG_NET_L2_PHY_IEEE802154
```

**弱选择（Implies）**

```text
CONFIG_NET_UDP
CONFIG_NET_IPV6
CONFIG_NET_CONFIG_NEED_IPV6
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_ieee802154/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_ieee802154/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`subsys/net/l2/openthread/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/openthread/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_NET_L2_PHY_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PHY_IEEE802154)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_CONFIG_NEED_IPV6`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_NEED_IPV6)。

<a id="CONFIG_NET_L2_PHY_IEEE802154"></a>

## 401.41 `CONFIG_NET_L2_PHY_IEEE802154`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

所有基于 IEEE 802.15.4 的第二层（L2）实现共用的配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_L2_IEEE802154
CONFIG_NET_L2_OPENTHREAD
CONFIG_NET_L2_CUSTOM_IEEE802154
```

**定义位置（Location）**：[`subsys/net/l2/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_IEEE802154`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NET_L2_OPENTHREAD`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_OPENTHREAD)、[`CONFIG_NET_L2_CUSTOM_IEEE802154`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_CUSTOM_IEEE802154)。

<a id="CONFIG_NET_L2_PPP"></a>

## 401.42 `CONFIG_NET_L2_PPP`

**提示（Prompt）**：点对点协议（Point-to-Point Protocol，PPP）支持

**说明（Help）**

添加点对点协议（PPP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)。

<a id="CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE"></a>

## 401.43 `CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：PPP 第二层（L2）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_L2_PPP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_L2_PPP_LOG_LEVEL_OFF
CONFIG_NET_L2_PPP_LOG_LEVEL_ERR
CONFIG_NET_L2_PPP_LOG_LEVEL_WRN
CONFIG_NET_L2_PPP_LOG_LEVEL_INF
CONFIG_NET_L2_PPP_LOG_LEVEL_DBG
CONFIG_NET_L2_PPP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_PPP_LOG_LEVEL_DEFAULT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_L2_PPP_LOG_LEVEL_OFF`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_LOG_LEVEL_OFF)、[`CONFIG_NET_L2_PPP_LOG_LEVEL_ERR`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_LOG_LEVEL_ERR)、[`CONFIG_NET_L2_PPP_LOG_LEVEL_WRN`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_LOG_LEVEL_WRN)、[`CONFIG_NET_L2_PPP_LOG_LEVEL_INF`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_LOG_LEVEL_INF)、[`CONFIG_NET_L2_PPP_LOG_LEVEL_DBG`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_L2_PPP_LOG_LEVEL_DBG"></a>

## 401.44 `CONFIG_NET_L2_PPP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持 → PPP 第二层（L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_PPP_LOG_LEVEL_DEFAULT"></a>

## 401.45 `CONFIG_NET_L2_PPP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持 → PPP 第二层（L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_PPP_LOG_LEVEL_ERR"></a>

## 401.46 `CONFIG_NET_L2_PPP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持 → PPP 第二层（L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_PPP_LOG_LEVEL_INF"></a>

## 401.47 `CONFIG_NET_L2_PPP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持 → PPP 第二层（L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_PPP_LOG_LEVEL_OFF"></a>

## 401.48 `CONFIG_NET_L2_PPP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持 → PPP 第二层（L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_PPP_LOG_LEVEL_WRN"></a>

## 401.49 `CONFIG_NET_L2_PPP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持 → PPP 第二层（L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_PPP_MAX_CONFIGURE_REQ_RETRANSMITS"></a>

## 401.50 `CONFIG_NET_L2_PPP_MAX_CONFIGURE_REQ_RETRANSMITS`

**提示（Prompt）**：配置请求（Configure-Req）的最大重传次数

**说明（Help）**

在判定链路无法正常工作之前，重新发送配置请求（Configure-Req）报文的次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_PPP_MAX_NACK_LOOPS"></a>

## 401.51 `CONFIG_NET_L2_PPP_MAX_NACK_LOOPS`

**提示（Prompt）**：允许的否定确认（NACK）循环的最大次数

**说明（Help）**

允许出现多少次否定确认（NACK）循环。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_PPP_MAX_TERMINATE_REQ_RETRANSMITS"></a>

## 401.52 `CONFIG_NET_L2_PPP_MAX_TERMINATE_REQ_RETRANSMITS`

**提示（Prompt）**：终止请求（Terminate-Req）的最大重传次数

**说明（Help）**

在终止链路之前，重新发送终止请求（Terminate-Req）报文的次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_PPP_MGMT"></a>

## 401.53 `CONFIG_NET_L2_PPP_MGMT`

**提示（Prompt）**：PPP 网络管理接口（Network management interface）

**说明（Help）**

启用 `net_mgmt` 的 PPP 接口支持，可在运行时配置 PPP 驱动及第二层（L2）设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
```

**被选择（Selected by）**

```text
CONFIG_MODEM_CELLULAR
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)。

<a id="CONFIG_NET_L2_PPP_OPTION_ACFC"></a>

## 401.54 `CONFIG_NET_L2_PPP_OPTION_ACFC`

**提示（Prompt）**：LCP 地址与控制字段压缩（Address-and-Control-Field-Compression，ACFC）选项支持

**说明（Help）**

启用链路控制协议（LCP）的地址与控制字段压缩（ACFC）协商，参见 RFC 1661 选项 8。此功能向对端声明本端接受省略地址字段 `0xFF` 和控制字段 `0x03` 的帧，并在 PPP 上下文中记录对端提出的相应请求。本选项只控制 LCP 协商交换；接收不受其影响，接收方会按 RFC 1662 第 3.2 节解压这些字段，并接受两种形式。发送时省略这些字段的功能尚未实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_PPP_OPTION_DNS_USE"></a>

## 401.55 `CONFIG_NET_L2_PPP_OPTION_DNS_USE`

**提示（Prompt）**：使用协商得到的 DNS 服务器（Negotiated DNS servers）

**说明（Help）**

使用 IP 控制协议（IPCP）配置过程中协商得到的 DNS 服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_PPP_OPTION_MRU"></a>

## 401.56 `CONFIG_NET_L2_PPP_OPTION_MRU`

**提示（Prompt）**：LCP 最大接收单元（MRU）选项支持

**说明（Help）**

启用链路控制协议（LCP）的最大接收单元（Maximum Receive Unit，MRU）选项支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_MODEM_CELLULAR
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)。

<a id="CONFIG_NET_L2_PPP_OPTION_PFC"></a>

## 401.57 `CONFIG_NET_L2_PPP_OPTION_PFC`

**提示（Prompt）**：LCP 协议字段压缩（Protocol-Field-Compression，PFC）选项支持

**说明（Help）**

启用链路控制协议（LCP）的协议字段压缩（PFC）协商，参见 RFC 1661 选项 7。对于小于 `0x0100` 的协议编号，协议字段可以压缩为一个八位组（Octet）；此功能向对端声明本端接受这种格式，并在 PPP 上下文中记录对端提出的相应请求。本选项只控制 LCP 协商交换；接收不受其影响，接收方始终同时接受压缩和未压缩形式。发送时压缩协议字段的功能尚未实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_PPP_OPTION_SERVE_DNS"></a>

## 401.58 `CONFIG_NET_L2_PPP_OPTION_SERVE_DNS`

**提示（Prompt）**：向对端提供 DNS 地址（DNS addresses）

**说明（Help）**

启用向 PPP 对端（Peer）提供 DNS 地址的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_PPP_OPTION_SERVE_IP"></a>

## 401.59 `CONFIG_NET_L2_PPP_OPTION_SERVE_IP`

**提示（Prompt）**：向对端提供 IP 地址（IP address）

**说明（Help）**

启用向 PPP 对端（Peer）提供 IP 地址的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_PPP_PAP"></a>

## 401.60 `CONFIG_NET_L2_PPP_PAP`

**提示（Prompt）**：密码认证协议（Password Authentication Protocol，PAP）

**说明（Help）**

启用密码认证协议（PAP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_PPP_AUTH_SUPPORT
```

**被选择（Selected by）**

```text
CONFIG_MODEM_CELLULAR
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_PPP_AUTH_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PPP_AUTH_SUPPORT)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_L2_PPP_AUTH_SUPPORT`。

<a id="CONFIG_NET_L2_PPP_THREAD_PRIO"></a>

## 401.61 `CONFIG_NET_L2_PPP_THREAD_PRIO`

**提示（Prompt）**：PPP 发送线程（TX thread）的优先级

**说明（Help）**

设置负责发送全部 PPP 数据包的发送线程（TX thread）的优先级。0 表示最高优先级；当 `CONFIG_NET_TC_THREAD_COOPERATIVE = y` 时，最低优先级为 `CONFIG_NUM_COOP_PRIORITIES-1`，否则为 `CONFIG_NUM_PREEMPT_PRIORITIES-1`。将 PPP 与 TCP 一起使用时，应确保该线程的优先级高于或等于 TCP 工作队列（Work queue）的优先级。否则，TCP 协议栈可能在将执行权交给下层网络协议栈之前耗尽全部 `net_buf`，导致很高的缓冲区耗尽风险。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_PPP_TIMEOUT"></a>

## 401.62 `CONFIG_NET_L2_PPP_TIMEOUT`

**提示（Prompt）**：配置请求（Configure-Req）的最大超时（毫秒）

**说明（Help）**

等待配置请求（Configure-Req）的时长。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3000
```

**取值范围（Ranges）**

```text
[1, 4294967295]
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_PPP_TX_STACK_SIZE"></a>

## 401.63 `CONFIG_NET_L2_PPP_TX_STACK_SIZE`

**提示（Prompt）**：发送处理程序（TX handler）的栈大小

**说明（Help）**

设置发送处理程序（TX handler）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2048 if CONFIG_COVERAGE_GCOV
1024
```

**定义位置（Location）**：[`subsys/net/l2/ppp/Kconfig:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ppp/Kconfig#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 点对点协议（Point-to-Point Protocol，PPP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)。

<a id="CONFIG_NET_L2_PTP"></a>

## 401.64 `CONFIG_NET_L2_PTP`

**提示（Prompt）**：精确时间协议第二层（PTP L2）支持［已弃用，Deprecated］

**说明（Help）**

此 Kconfig 配置已弃用，请改用 `NET_L2_PTP_TIMESTAMPING`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
CONFIG_PTP_CLOCK
CONFIG_NET_L2_PTP_TIMESTAMPING
```

**定义位置（Location）**：[`subsys/net/l2/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_PTP_CLOCK`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PTP_TIMESTAMPING)。

<a id="CONFIG_NET_L2_PTP_TIMESTAMPING"></a>

## 401.65 `CONFIG_NET_L2_PTP_TIMESTAMPING`

**提示（Prompt）**：第二层（L2）的 PTP 时间戳（Timestamping）支持

**说明（Help）**

启用第二层（L2）的精确时间协议（PTP）时间戳支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_CLOCK && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_PKT_TIMESTAMP
CONFIG_NET_PKT_TIMESTAMP_THREAD
```

**被选择（Selected by）**

```text
CONFIG_ETH_E1000_PTP_CLOCK
CONFIG_PTP_CLOCK_SAM_GMAC
CONFIG_PTP_CLOCK_STM32_HAL
CONFIG_PTP_CLOCK_XMC4XXX
CONFIG_PTP_CLOCK_DWC_MAC
CONFIG_PTP_CLOCK_NATIVE
CONFIG_PTP_CLOCK_NXP_ENET
CONFIG_PTP_CLOCK_NXP_ENET_QOS
CONFIG_PTP_CLOCK_NXP_NETC
CONFIG_NET_GPTP
CONFIG_NET_L2_PTP
CONFIG_PTP
```

**定义位置（Location）**：[`subsys/net/l2/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_PTP_CLOCK`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_TIMESTAMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_TIMESTAMP)、[`CONFIG_NET_PKT_TIMESTAMP_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_TIMESTAMP_THREAD)、[`CONFIG_ETH_E1000_PTP_CLOCK`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_E1000_PTP_CLOCK)、[`CONFIG_PTP_CLOCK_SAM_GMAC`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_SAM_GMAC)、[`CONFIG_PTP_CLOCK_STM32_HAL`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_STM32_HAL)、[`CONFIG_PTP_CLOCK_XMC4XXX`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_XMC4XXX)、[`CONFIG_PTP_CLOCK_DWC_MAC`](P090_drivers_ethernet_配置项参考_4.md#CONFIG_PTP_CLOCK_DWC_MAC)、[`CONFIG_PTP_CLOCK_NATIVE`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK_NATIVE)、[`CONFIG_PTP_CLOCK_NXP_ENET`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK_NXP_ENET)、[`CONFIG_PTP_CLOCK_NXP_ENET_QOS`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK_NXP_ENET_QOS)、[`CONFIG_PTP_CLOCK_NXP_NETC`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK_NXP_NETC)、[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_PTP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PTP)、[`CONFIG_PTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP)。

<a id="CONFIG_NET_L2_VIRTUAL"></a>

## 401.66 `CONFIG_NET_L2_VIRTUAL`

**提示（Prompt）**：虚拟第二层（Virtual L2）支持

**说明（Help）**

添加虚拟第二层（Virtual L2）驱动。如果某个 L2 依赖另一个 L2，例如在以太网之上运行虚拟专用网络（VPN），就需要此驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_PSEUDO_IFACE
CONFIG_NET_VLAN
CONFIG_NET_ETHERNET_BRIDGE
CONFIG_NET_CAPTURE
CONFIG_NET_CAPTURE_COOKED_MODE
CONFIG_WIREGUARD
```

**定义位置（Location）**：[`subsys/net/l2/virtual/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/virtual/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PSEUDO_IFACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PSEUDO_IFACE)、[`CONFIG_NET_VLAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN)、[`CONFIG_NET_ETHERNET_BRIDGE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE)、[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NET_CAPTURE_COOKED_MODE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_COOKED_MODE)、[`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)。

<a id="CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE"></a>

## 401.67 `CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：虚拟第二层（Virtual L2）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_L2_VIRTUAL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_OFF
CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_ERR
CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_WRN
CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_INF
CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_DBG
CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_L2_VIRTUAL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_DEFAULT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_OFF`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_OFF)、[`CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_ERR`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_ERR)、[`CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_WRN`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_WRN)、[`CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_INF`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_INF)、[`CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_DBG`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_DBG"></a>

## 401.68 `CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → 虚拟第二层（Virtual L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_DEFAULT"></a>

## 401.69 `CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → 虚拟第二层（Virtual L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_ERR"></a>

## 401.70 `CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → 虚拟第二层（Virtual L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_INF"></a>

## 401.71 `CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → 虚拟第二层（Virtual L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_OFF"></a>

## 401.72 `CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → 虚拟第二层（Virtual L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_WRN"></a>

## 401.73 `CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持 → 虚拟第二层（Virtual L2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_VIRTUAL_MAX_NAME_LEN"></a>

## 401.74 `CONFIG_NET_L2_VIRTUAL_MAX_NAME_LEN`

**提示（Prompt）**：虚拟第二层（Virtual L2）名称的最大长度

**说明（Help）**

指定名称最大长度，包含末尾的空字符（NULL byte）。减小此值可以节省内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_VIRTUAL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[8, 128]
```

**定义位置（Location）**：[`subsys/net/l2/virtual/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/virtual/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_VIRTUAL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_L2_VIRTUAL_MGMT"></a>

## 401.75 `CONFIG_NET_L2_VIRTUAL_MGMT`

**提示（Prompt）**：虚拟接口的网络管理接口（Network management interface）

**说明（Help）**

启用 `net_mgmt` 的虚拟接口支持，可在运行时配置第二层（L2）设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_VIRTUAL && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
```

**被选择（Selected by）**

```text
CONFIG_NET_CAPTURE
CONFIG_WIREGUARD
```

**定义位置（Location）**：[`subsys/net/l2/virtual/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/virtual/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 虚拟第二层（Virtual L2）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_VIRTUAL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)。

<a id="CONFIG_NET_L2_WIFI_MGMT"></a>

## 401.76 `CONFIG_NET_L2_WIFI_MGMT`

**提示（Prompt）**：Wi-Fi 管理支持（Management support）

**说明（Help）**

启用 Wi-Fi 管理接口（Wi-Fi Management interface）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
CONFIG_NET_MGMT_EVENT_INFO
CONFIG_NET_L2_WIFI_UTILS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_BFLB
CONFIG_WIFI_ESP32
CONFIG_WIFI_ESP_AT
CONFIG_WIFI_ESP_HOSTED
CONFIG_WIFI_ESP_HOSTED_MCU
CONFIG_WIFI_ESWIFI
CONFIG_WIFI_HWSIM
CONFIG_WIFI_AIROC
CONFIG_WIFI_NATIVE_SIM
CONFIG_WIFI_NRF70
CONFIG_WIFI_NXP
CONFIG_WIFI_SIMPLELINK
CONFIG_WIFI_SILABS_SIWX91X
CONFIG_WIFI_ST67W611M1
CONFIG_WIFI_WINC1500
CONFIG_NET_L2_WIFI_SHELL
```

**定义位置（Location）**：[`subsys/net/l2/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NET_MGMT_EVENT_INFO`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_INFO)、[`CONFIG_NET_L2_WIFI_UTILS`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_UTILS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI_ESP_AT`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_AT)、[`CONFIG_WIFI_ESP_HOSTED`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED)、[`CONFIG_WIFI_ESP_HOSTED_MCU`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESP_HOSTED_MCU)、[`CONFIG_WIFI_ESWIFI`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI)、[`CONFIG_WIFI_HWSIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_HWSIM)、[`CONFIG_WIFI_AIROC`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI_NATIVE_SIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NATIVE_SIM)、[`CONFIG_WIFI_NRF70`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI_SIMPLELINK`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SIMPLELINK)、[`CONFIG_WIFI_SILABS_SIWX91X`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_SILABS_SIWX91X)、[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI_WINC1500`](P194_drivers_wifi_配置项参考_7.md#CONFIG_WIFI_WINC1500)、[`CONFIG_NET_L2_WIFI_SHELL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_SHELL)。

<a id="CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE"></a>

## 401.77 `CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Wi-Fi 管理层（Management layer）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_OFF
CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_ERR
CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_WRN
CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_INF
CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_DBG
CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_DEFAULT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_OFF`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_OFF)、[`CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_ERR`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_ERR)、[`CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_WRN`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_WRN)、[`CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_INF`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_INF)、[`CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_DBG`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_DBG"></a>

## 401.78 `CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 管理层（Management layer）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_DEFAULT"></a>

## 401.79 `CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 管理层（Management layer）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_ERR"></a>

## 401.80 `CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 管理层（Management layer）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_INF"></a>

## 401.81 `CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 管理层（Management layer）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_OFF"></a>

## 401.82 `CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 管理层（Management layer）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_WRN"></a>

## 401.83 `CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support） → Wi-Fi 管理层（Management layer）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_L2_WIFI_SHELL"></a>

## 401.84 `CONFIG_NET_L2_WIFI_SHELL`

**提示（Prompt）**：Wi-Fi 命令行模块（Shell module）

**说明（Help）**

提供名为 `wifi` 的命令行模块（Shell module），用于通过控制台控制 Wi-Fi。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_WIFI_MGMT
CONFIG_NET_L2_WIFI_UTILS
CONFIG_SHELL_GETOPT
CONFIG_GETOPT_LONG
```

**定义位置（Location）**：[`subsys/net/l2/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NET_L2_WIFI_UTILS`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_UTILS)、[`CONFIG_SHELL_GETOPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_GETOPT)、[`CONFIG_GETOPT_LONG`](P197_lib_配置项参考_1.md#CONFIG_GETOPT_LONG)。

<a id="CONFIG_NET_L2_WIFI_UTILS"></a>

## 401.85 `CONFIG_NET_L2_WIFI_UTILS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 Wi-Fi 子系统（Subsystem）提供实用函数（Utility function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_L2_WIFI_MGMT
CONFIG_NET_L2_WIFI_SHELL
```

**定义位置（Location）**：[`subsys/net/l2/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NET_L2_WIFI_SHELL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_SHELL)。

<a id="CONFIG_NET_LATMON"></a>

## 401.86 `CONFIG_NET_LATMON`

**提示（Prompt）**：延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】

**说明（Help）**

启用 Zephyr 的延迟监测（Latency monitoring）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_NET_SOCKETS
```

**定义位置（Location）**：[`subsys/net/lib/latmon/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)。

<a id="CONFIG_NET_LATMON_MONITOR_THREAD_PRIORITY"></a>

## 401.87 `CONFIG_NET_LATMON_MONITOR_THREAD_PRIORITY`

**提示（Prompt）**：监测线程（Monitor thread）的优先级

**说明（Help）**

指定延迟监测（Latency monitoring）所用监测线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LATMON && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
-16
```

**定义位置（Location）**：[`subsys/net/lib/latmon/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_LATMON`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LATMON)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LATMON_MONITOR_THREAD_STACK_SIZE"></a>

## 401.88 `CONFIG_NET_LATMON_MONITOR_THREAD_STACK_SIZE`

**提示（Prompt）**：监测线程（Monitor thread）的栈大小

**说明（Help）**

指定延迟监测（Latency monitoring）所用监测线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LATMON && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`subsys/net/lib/latmon/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_LATMON`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LATMON)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LATMON_PORT"></a>

## 401.89 `CONFIG_NET_LATMON_PORT`

**提示（Prompt）**：Latmon 与 Latmus 的通信端口（Communication port）

**说明（Help）**

指定 Latmon 与 Latmus 通信使用的端口号（Port number）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LATMON && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2306
```

**定义位置（Location）**：[`subsys/net/lib/latmon/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_LATMON`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LATMON)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LATMON_THREAD_PRIORITY"></a>

## 401.90 `CONFIG_NET_LATMON_THREAD_PRIORITY`

**提示（Prompt）**：Latmon 线程优先级（Thread priority）

**说明（Help）**

指定延迟监测（Latency monitoring）所用 Latmon 线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LATMON && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
14
```

**定义位置（Location）**：[`subsys/net/lib/latmon/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_LATMON`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LATMON)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LATMON_THREAD_STACK_SIZE"></a>

## 401.91 `CONFIG_NET_LATMON_THREAD_STACK_SIZE`

**提示（Prompt）**：Latmon 线程栈大小（Thread stack size）

**说明（Help）**

指定延迟监测（Latency monitoring）所用 Latmon 线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LATMON && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`subsys/net/lib/latmon/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_LATMON`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LATMON)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LATMON_XFER_THREAD_PRIORITY"></a>

## 401.92 `CONFIG_NET_LATMON_XFER_THREAD_PRIORITY`

**提示（Prompt）**：网络传输线程（Network transfer thread）的优先级

**说明（Help）**

指定延迟监测（Latency monitoring）所用网络传输线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LATMON && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
14
```

**定义位置（Location）**：[`subsys/net/lib/latmon/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_LATMON`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LATMON)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LATMON_XFER_THREAD_STACK_SIZE"></a>

## 401.93 `CONFIG_NET_LATMON_XFER_THREAD_STACK_SIZE`

**提示（Prompt）**：网络传输线程（Network transfer thread）的栈大小

**说明（Help）**

指定延迟监测（Latency monitoring）所用网络传输线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LATMON && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`subsys/net/lib/latmon/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 延迟监控支持（Latency monitoring support）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_LATMON`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LATMON)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LINK_ADDR_CUSTOM_LENGTH"></a>

## 401.94 `CONFIG_NET_LINK_ADDR_CUSTOM_LENGTH`

**提示（Prompt）**：自定义链路层地址长度（Custom link-layer address length）

**说明（Help）**

当所用链路层技术没有直接支持时，此项允许定义自定义链路层地址长度（Link-layer address length）。默认不使用自定义长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:871`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L871)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP"></a>

## 401.95 `CONFIG_NET_LLDP`

**提示（Prompt）**：链路层发现协议（Link Layer Discovery Protocol，LLDP）

**说明（Help）**

启用链路层发现协议（Link Layer Discovery Protocol，LLDP）的发送功能。更多信息参见 IEEE 802.1AB 标准。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_NATIVE)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)。

<a id="CONFIG_NET_LLDP_CHASSIS_ID"></a>

## 401.96 `CONFIG_NET_LLDP_CHASSIS_ID`

**提示（Prompt）**：机箱标识符（Chassis ID）的值

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE != 4 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"CHASSIS_ID_PLACEHOLDER"
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_CHASSIS_ID_MAC0"></a>

## 401.97 `CONFIG_NET_LLDP_CHASSIS_ID_MAC0`

**提示（Prompt）**：机箱标识符（Chassis ID）MAC 地址的字节 0

**说明（Help）**

MAC 地址的字节 0。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE = 4 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0x00
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_CHASSIS_ID_MAC1"></a>

## 401.98 `CONFIG_NET_LLDP_CHASSIS_ID_MAC1`

**提示（Prompt）**：机箱标识符（Chassis ID）MAC 地址的字节 1

**说明（Help）**

MAC 地址的字节 1。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE = 4 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0x00
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_CHASSIS_ID_MAC2"></a>

## 401.99 `CONFIG_NET_LLDP_CHASSIS_ID_MAC2`

**提示（Prompt）**：机箱标识符（Chassis ID）MAC 地址的字节 2

**说明（Help）**

MAC 地址的字节 2。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE = 4 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0x5e
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_CHASSIS_ID_MAC3"></a>

## 401.100 `CONFIG_NET_LLDP_CHASSIS_ID_MAC3`

**提示（Prompt）**：机箱标识符（Chassis ID）MAC 地址的字节 3

**说明（Help）**

MAC 地址的字节 3。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE = 4 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0x00
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<!-- kconfig-navigation -->

[上一章](P400_subsys_net_配置项参考_10.md) · [返回大纲](大纲.md) · [下一章](P402_subsys_net_配置项参考_12.md)
