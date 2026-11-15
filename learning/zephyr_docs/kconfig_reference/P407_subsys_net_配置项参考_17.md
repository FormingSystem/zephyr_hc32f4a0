---
id: learning.zephyr-docs.kconfig-reference.page-407
title: "`subsys/net`配置项参考（17/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第407章\_`subsys/net`配置项参考（17/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PTP_NETWORK_MODE_HYBRID_NO_FALLBACK"></a>

## 407.1 `CONFIG_PTP_NETWORK_MODE_HYBRID_NO_FALLBACK`

**提示（Prompt）**：禁用多播回退（Multicast fallback）

**说明（Help）**

始终保持混合模式（Hybrid），即使当前时间发送端（timeTransmitter）不响应，也继续发送单播 Delay_Req。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_NETWORK_MODE_HYBRID && CONFIG_PTP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP_NETWORK_MODE_HYBRID`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_NETWORK_MODE_HYBRID)、[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_NETWORK_MODE_MULTICAST"></a>

## 407.2 `CONFIG_PTP_NETWORK_MODE_MULTICAST`

**提示（Prompt）**：多播（Multicast）

**说明（Help）**

标准 PTP 模式，全部 PTP 报文发往默认多播地址（Multicast address）。每个节点都会收到其他所有节点的 Delay_Req 和 Delay_Resp；在只有少量时间接收端（timeReceiver）的小型网络中，这通常不成问题。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_NETWORK_MODE>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → 网络传输模式（Network transmission mode）

**配置项引用（Symbol References）**：[`CONFIG_PTP_NETWORK_MODE`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_NETWORK_MODE)。

<a id="CONFIG_PTP_NUM_PORTS"></a>

## 407.3 `CONFIG_PTP_NUM_PORTS`

**提示（Prompt）**：PTP 端口（Port）数量

**说明（Help）**

配置 PTP 协议栈使用的端口数量。这里的端口（Port）与网络接口（Network interface）是同一概念。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1 if CONFIG_PTP_ORDINARY_CLOCK
2 if CONFIG_PTP_BOUNDARY_CLOCK || CONFIG_PTP_TRANSPARENT_P2P_CLOCK || CONFIG_PTP_TRANSPARENT_E2E_CLOCK
```

**取值范围（Ranges）**

```text
[1, 32] if CONFIG_PTP_ORDINARY_CLOCK
[2, 32] if CONFIG_PTP_BOUNDARY_CLOCK || CONFIG_PTP_TRANSPARENT_P2P_CLOCK || CONFIG_PTP_TRANSPARENT_E2E_CLOCK
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PTP_ORDINARY_CLOCK`](P407_subsys_net_配置项参考_17.md#CONFIG_PTP_ORDINARY_CLOCK)、[`CONFIG_PTP_BOUNDARY_CLOCK`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_BOUNDARY_CLOCK)、[`CONFIG_PTP_TRANSPARENT_P2P_CLOCK`](P407_subsys_net_配置项参考_17.md#CONFIG_PTP_TRANSPARENT_P2P_CLOCK)、[`CONFIG_PTP_TRANSPARENT_E2E_CLOCK`](P407_subsys_net_配置项参考_17.md#CONFIG_PTP_TRANSPARENT_E2E_CLOCK)。

<a id="CONFIG_PTP_ORDINARY_CLOCK"></a>

## 407.4 `CONFIG_PTP_ORDINARY_CLOCK`

**提示（Prompt）**：普通时钟（Ordinary Clock）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟类型（Clock Type）

<a id="CONFIG_PTP_PEER_DELAY_MAX_NS"></a>

## 407.5 `CONFIG_PTP_PEER_DELAY_MAX_NS`

**提示（Prompt）**：可接受的最大对等延迟（Peer delay，纳秒）

**说明（Help）**

可被视为有效 Pdelay 测量的最大对等传播延迟（Peer propagation delay）。超过此值的样本被视为无效时间戳数据，不用于更新 `meanLinkDelay`。应根据预期网络拓扑和 PTP 配置文件（Profile）调整这一合理性检查阈值；它不是时钟精度要求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10000000
```

**取值范围（Ranges）**

```text
[1, 1000000000]
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:359`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L359)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_PRIORITY1"></a>

## 407.6 `CONFIG_PTP_PRIORITY1`

**提示（Prompt）**：用于最佳时间发送端时钟算法（Best TimeTransmitter Clock Algorithm，BTCA）的值

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:299`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L299)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_PRIORITY2"></a>

## 407.7 `CONFIG_PTP_PRIORITY2`

**提示（Prompt）**：用于最佳时间发送端时钟算法（Best TimeTransmitter Clock Algorithm，BTCA）的值

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:304`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L304)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_SERVICE_THREAD_PRIO"></a>

## 407.8 `CONFIG_PTP_SERVICE_THREAD_PRIO`

**提示（Prompt）**：PTP 服务线程（Service thread）的优先级

**说明（Help）**

设置 PTP 线程的优先级。此处理程序轮询套接字（Socket）并检查计时器，根据收到的 PTP 报文或超时执行标准定义的操作。应谨慎选择优先级值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NUM_PREEMPT_PRIORITIES
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NUM_PREEMPT_PRIORITIES`](P001_kernel_配置项参考_1.md#CONFIG_NUM_PREEMPT_PRIORITIES)。

<a id="CONFIG_PTP_STACK_SIZE"></a>

## 407.9 `CONFIG_PTP_STACK_SIZE`

**提示（Prompt）**：PTP 线程栈大小（Thread stack size）

**说明（Help）**

设置 PTP 线程栈大小，单位为字节。该线程处理 PTP 状态机（State machine），系统中只有一个 PTP 线程。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_SYNC_LOG_INTERVAL"></a>

## 407.10 `CONFIG_PTP_SYNC_LOG_INTERVAL`

**提示（Prompt）**：连续 Sync 报文之间的间隔

**说明（Help）**

指定以多播（Multicast）方式发送时，连续 Sync 报文之间的平均时间间隔。配置值按以下公式转换为纳秒：`nanoseconds = (10^9) * 2^(value)`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[-1, 1]
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:342`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L342)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_TIME_RECEIVER_ONLY"></a>

## 407.11 `CONFIG_PTP_TIME_RECEIVER_ONLY`

**提示（Prompt）**：将时钟配置为时间接收端（timeReceiver）PTP 实例

**说明（Help）**

普通时钟（Ordinary Clock）可以设计为时间接收端（timeReceiver）PTP 实例。在此模式下，该实例永远不能进入 `TIME_TRANSMITTER` 状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_ORDINARY_CLOCK && CONFIG_PTP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:309`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L309)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP_ORDINARY_CLOCK`](P407_subsys_net_配置项参考_17.md#CONFIG_PTP_ORDINARY_CLOCK)、[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_TRANSPARENT_E2E_CLOCK"></a>

## 407.12 `CONFIG_PTP_TRANSPARENT_E2E_CLOCK`

**提示（Prompt）**：端到端透明时钟（Transparent End-to-End Clock）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟类型（Clock Type）

<a id="CONFIG_PTP_TRANSPARENT_P2P_CLOCK"></a>

## 407.13 `CONFIG_PTP_TRANSPARENT_P2P_CLOCK`

**提示（Prompt）**：对等透明时钟（Transparent Peer-to-Peer Clock）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟类型（Clock Type）

<a id="CONFIG_PTP_UDP_IPV4_PROTOCOL"></a>

## 407.14 `CONFIG_PTP_UDP_IPV4_PROTOCOL`

**提示（Prompt）**：IPv4 上的 UDP

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && <choice CONFIG_PTP_NETWORKING_PROTOCOL>
```

**主动选择（Selects）**

```text
CONFIG_NET_IPV4_IGMP
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 协议栈使用的网络协议（Networking Protocol）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_PTP_NETWORKING_PROTOCOL`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_NETWORKING_PROTOCOL)、[`CONFIG_NET_IPV4_IGMP`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_IGMP)。

<a id="CONFIG_PTP_UDP_IPV6_PROTOCOL"></a>

## 407.15 `CONFIG_PTP_UDP_IPV6_PROTOCOL`

**提示（Prompt）**：IPv6 上的 UDP

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && <choice CONFIG_PTP_NETWORKING_PROTOCOL>
```

**主动选择（Selects）**

```text
CONFIG_NET_IPV6_MLD
CONFIG_NET_CONTEXT_RECV_PKTINFO
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L197)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 协议栈使用的网络协议（Networking Protocol）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_PTP_NETWORKING_PROTOCOL`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_NETWORKING_PROTOCOL)、[`CONFIG_NET_IPV6_MLD`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_MLD)、[`CONFIG_NET_CONTEXT_RECV_PKTINFO`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_RECV_PKTINFO)。

<a id="CONFIG_QUIC"></a>

## 407.16 `CONFIG_QUIC`

**提示（Prompt）**：QUIC 支持［实验性，Experimental］

**说明（Help）**

启用 RFC 9000 指定的 QUIC 实现，包括 Retry 和基于 NEW_TOKEN 的地址验证令牌（Address-validation token）。QUIC 要求连接 ID、地址验证令牌及 TLS 随机数使用密码学安全随机数生成器（Cryptographically Secure Pseudorandom Number Generator，CSPRNG）。此项选择 `CSPRNG_NEEDED` 以引入相应支持，但仅在平台存在熵源（Entropy source）时才能满足。如果因此构建失败，参见 `QUIC_ALLOW_NON_CSPRNG`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS
CONFIG_NET_SOCKETS_SERVICE
CONFIG_TLS_CREDENTIALS
CONFIG_EXPERIMENTAL
CONFIG_SMF
CONFIG_NET_IPV6_PMTU if CONFIG_NET_NATIVE_IPV6
CONFIG_NET_IPV4_PMTU if CONFIG_NET_NATIVE_IPV4
CONFIG_NET_IPV6_PMTU_DPLPMTUD if CONFIG_NET_NATIVE_IPV6
CONFIG_NET_IPV4_PMTU_DPLPMTUD if CONFIG_NET_NATIVE_IPV4
CONFIG_NET_PMTU_DPLPMTUD if CONFIG_NET_NATIVE_IPV6 || CONFIG_NET_NATIVE_IPV4
CONFIG_NET_STATISTICS_USER_API if CONFIG_NET_STATISTICS_QUIC
CONFIG_CSPRNG_NEEDED
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NET_SOCKETS_SERVICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SERVICE)、[`CONFIG_TLS_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_SMF`](P198_lib_配置项参考_2.md#CONFIG_SMF)、[`CONFIG_NET_IPV6_PMTU`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PMTU)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV4_PMTU`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_PMTU)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV6_PMTU_DPLPMTUD`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PMTU_DPLPMTUD)、[`CONFIG_NET_IPV4_PMTU_DPLPMTUD`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_PMTU_DPLPMTUD)、[`CONFIG_NET_PMTU_DPLPMTUD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PMTU_DPLPMTUD)、[`CONFIG_NET_STATISTICS_USER_API`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_USER_API)、[`CONFIG_NET_STATISTICS_QUIC`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_QUIC)、[`CONFIG_CSPRNG_NEEDED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CSPRNG_NEEDED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`、`CONFIG_NET_NATIVE_IPV4`、`CONFIG_NET_PMTU_DPLPMTUD`。

<a id="CONFIG_QUIC_0RTT"></a>

## 407.17 `CONFIG_QUIC_0RTT`

**提示（Prompt）**：QUIC 零往返时间（0-RTT）支持

**说明（Help）**

启用基于票据（Ticket）的 QUIC 零往返时间（0-RTT）支持，包括早期数据（Early data）的提供与接受、重放处理，以及记住的早期数据策略。网络攻击者可以重放 0-RTT 早期数据，参见 RFC 9001 第 9.2 节，因此此功能默认禁用。只有将早期数据限制为幂等操作（Idempotent operation）的应用才应启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:242`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L242)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_ALLOW_NON_CSPRNG"></a>

## 407.18 `CONFIG_QUIC_ALLOW_NON_CSPRNG`

**提示（Prompt）**：允许 QUIC 在没有密码学安全随机数生成器（CSPRNG）的情况下运行

**说明（Help）**

允许在无法满足 `CSPRNG_ENABLED` 的平台上构建 QUIC，使 `sys_csrand_get()` 回退到普通、非密码学安全的生成器。此时，连接 ID、地址验证令牌（Address-validation token）、TLS 随机数及会话票据（Session ticket），对能够观察足够输出的人而言会变得可预测，破坏 RFC 9000 要求的不可预测性。仅应在没有熵源（Entropy source）的平台上为测试启用。测试二进制默认允许这样做，使协议测试套件能在无熵源的平台构建；这些测试本就使用测试随机数生成器。应用与示例不会自动获得此例外，必须提供熵源或明确选择启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TEST_RANDOM_GENERATOR && CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_ZTEST
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_TEST_RANDOM_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)。

<a id="CONFIG_QUIC_CONNECT_TIMEOUT"></a>

## 407.19 `CONFIG_QUIC_CONNECT_TIMEOUT`

**提示（Prompt）**：连接（CONNECT）的超时时间（毫秒）

**说明（Help）**

指定连接过程中，在未收到对端另一个数据包的情况下，经过多少毫秒后判定连接超时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3000
```

**取值范围（Ranges）**

```text
[0, 60000]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:468`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L468)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_CRYPTO_OOO_SLOTS"></a>

## 407.20 `CONFIG_QUIC_CRYPTO_OOO_SLOTS`

**提示（Prompt）**：乱序 CRYPTO 报文段（Out-of-order segment）的槽位数

**说明（Help）**

每个槽位保存一个乱序 CRYPTO 帧片段的元数据（Metadata）。Chrome 可能将 ClientHello 拆分为十个以上的小片段。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[4, 16]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:420`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L420)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_CRYPTO_RX_BUFFER_SIZE"></a>

## 407.21 `CONFIG_QUIC_CRYPTO_RX_BUFFER_SIZE`

**提示（Prompt）**：CRYPTO 流重组缓冲区（Stream reassembly buffer）大小

**说明（Help）**

TLS 握手期间，CRYPTO 帧共用的重组缓冲区（Reassembly buffer）大小。Chrome 等浏览器可能将 ClientHello 拆分为多个乱序到达的 CRYPTO 帧；此缓冲区保存片段，直到能够按顺序重组。由于 QUIC 每次处理一个加密级别（Encryption level），顺序为 Initial、Handshake、Application，所以各级别共用同一个缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4096
```

**取值范围（Ranges）**

```text
[1024, 8192]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:408`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L408)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_ENDPOINT_PENDING_DATA_LEN"></a>

## 407.22 `CONFIG_QUIC_ENDPOINT_PENDING_DATA_LEN`

**提示（Prompt）**：每个端点（Endpoint）的接收缓冲区大小

**说明（Help）**

每个端点（Endpoint）都有一个缓冲区，存放已收到但尚未处理的数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:353`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L353)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_ENDPOINT_USE_IPV4_MAPPING_TO_IPV6"></a>

## 407.23 `CONFIG_QUIC_ENDPOINT_USE_IPV4_MAPPING_TO_IPV6`

**提示（Prompt）**：为监听端点的 UDP 套接字设置 IPv4 到 IPv6 的映射（Mapping）

**说明（Help）**

尽可能共享 IPv4 和 IPv6 套接字（Socket）。同时启用 IPv4 和 IPv6 时，它们可共用同一个底层 UDP 套接字，因此仅需一个监听端点（Listening endpoint），可节省大量内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_MAPPING_TO_IPV6 && CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:314`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L314)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_MAPPING_TO_IPV6`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_MAPPING_TO_IPV6)、[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_INITIAL_MAX_DATA"></a>

## 407.24 `CONFIG_QUIC_INITIAL_MAX_DATA`

**提示（Prompt）**：连接的初始最大数据量（Initial connection max data）

**说明（Help）**

此整数参数给出连接上允许发送数据总量上限的初始值，等效于握手完成后立即针对该连接发送 MAX_DATA 帧，参见 RFC 9000 第 19.9 节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
16384
```

**取值范围（Ranges）**

```text
[1, 18446744073709551615]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_INITIAL_MAX_STREAMS_BIDI"></a>

## 407.25 `CONFIG_QUIC_INITIAL_MAX_STREAMS_BIDI`

**提示（Prompt）**：双向流（Bidirectional stream）的初始最大数量

**说明（Help）**

此整数参数给出接收到该传输参数的端点（Endpoint）最初允许发起的双向流（Bidirectional stream）最大数量。参数缺省或为 0 时，对端必须等到收到 MAX_STREAMS 帧后才能打开双向流。设置该参数，等效于发送相同数值、对应类型的 MAX_STREAMS 帧，参见第 19.11 节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_MAX_STREAMS_BIDI
```

**取值范围（Ranges）**

```text
[1, CONFIG_QUIC_MAX_STREAMS_BIDI]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC_MAX_STREAMS_BIDI`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_MAX_STREAMS_BIDI)。

<a id="CONFIG_QUIC_INITIAL_MAX_STREAMS_UNI"></a>

## 407.26 `CONFIG_QUIC_INITIAL_MAX_STREAMS_UNI`

**提示（Prompt）**：单向流（Unidirectional stream）的初始最大数量

**说明（Help）**

此整数参数给出接收到该传输参数的端点（Endpoint）最初允许发起的单向流（Unidirectional stream）最大数量。参数缺省或为 0 时，对端必须等到收到 MAX_STREAMS 帧后才能打开单向流。设置该参数，等效于发送相同数值、对应类型的 MAX_STREAMS 帧，参见第 19.11 节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_MAX_STREAMS_UNI
```

**取值范围（Ranges）**

```text
[0, CONFIG_QUIC_MAX_STREAMS_UNI]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:171`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L171)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC_MAX_STREAMS_UNI`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_MAX_STREAMS_UNI)。

<a id="CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_BIDI_LOCAL"></a>

## 407.27 `CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_BIDI_LOCAL`

**提示（Prompt）**：本地发起双向流的初始最大数据量（Initial local bidirectional stream max data）

**说明（Help）**

此整数参数指定本地发起的双向流（Bidirectional stream）的初始流量控制限制（Flow control limit），适用于发送该传输参数的端点新建的双向流。在客户端传输参数中，适用于标识符最低两位为 `0x00` 的流；在服务器传输参数中，适用于最低两位为 `0x01` 的流。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_STREAM_RX_BUFFER_SIZE
```

**取值范围（Ranges）**

```text
[1, 18446744073709551615]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC_STREAM_RX_BUFFER_SIZE`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_STREAM_RX_BUFFER_SIZE)。

<a id="CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_BIDI_REMOTE"></a>

## 407.28 `CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_BIDI_REMOTE`

**提示（Prompt）**：远端发起双向流的初始最大数据量（Initial remote bidirectional stream max data）

**说明（Help）**

此整数参数指定对端发起的双向流（Bidirectional stream）的初始流量控制限制（Flow control limit），适用于接收该传输参数的端点新建的双向流。在客户端传输参数中，适用于标识符最低两位为 `0x01` 的流；在服务器传输参数中，适用于最低两位为 `0x00` 的流。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_STREAM_RX_BUFFER_SIZE
```

**取值范围（Ranges）**

```text
[1, 18446744073709551615]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC_STREAM_RX_BUFFER_SIZE`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_STREAM_RX_BUFFER_SIZE)。

<a id="CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_UNI"></a>

## 407.29 `CONFIG_QUIC_INITIAL_MAX_STREAM_DATA_UNI`

**提示（Prompt）**：单向流的初始最大数据量（Initial unidirectional stream max data）

**说明（Help）**

此整数参数指定单向流（Unidirectional stream）的初始流量控制限制（Flow control limit），适用于接收该传输参数的端点新建的单向流。在客户端传输参数中，适用于标识符最低两位为 `0x03` 的流；在服务器传输参数中，适用于最低两位为 `0x02` 的流。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_STREAM_RX_BUFFER_SIZE
```

**取值范围（Ranges）**

```text
[1, 18446744073709551615]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC_STREAM_RX_BUFFER_SIZE`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_STREAM_RX_BUFFER_SIZE)。

<a id="CONFIG_QUIC_LOG_LEVEL_CHOICE"></a>

## 407.30 `CONFIG_QUIC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：QUIC 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_QUIC_LOG_LEVEL_OFF
CONFIG_QUIC_LOG_LEVEL_ERR
CONFIG_QUIC_LOG_LEVEL_WRN
CONFIG_QUIC_LOG_LEVEL_INF
CONFIG_QUIC_LOG_LEVEL_DBG
CONFIG_QUIC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC_LOG_LEVEL_DEFAULT`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_DEFAULT)、[`CONFIG_QUIC_LOG_LEVEL_OFF`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_OFF)、[`CONFIG_QUIC_LOG_LEVEL_ERR`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_ERR)、[`CONFIG_QUIC_LOG_LEVEL_WRN`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_WRN)、[`CONFIG_QUIC_LOG_LEVEL_INF`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_INF)、[`CONFIG_QUIC_LOG_LEVEL_DBG`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_DBG)。

<a id="CONFIG_QUIC_LOG_LEVEL_DBG"></a>

## 407.31 `CONFIG_QUIC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_QUIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］ → QUIC 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_QUIC_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_QUIC_LOG_LEVEL_DEFAULT"></a>

## 407.32 `CONFIG_QUIC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_QUIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］ → QUIC 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_QUIC_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_QUIC_LOG_LEVEL_ERR"></a>

## 407.33 `CONFIG_QUIC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_QUIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］ → QUIC 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_QUIC_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_QUIC_LOG_LEVEL_INF"></a>

## 407.34 `CONFIG_QUIC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_QUIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］ → QUIC 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_QUIC_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_QUIC_LOG_LEVEL_OFF"></a>

## 407.35 `CONFIG_QUIC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_QUIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］ → QUIC 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_QUIC_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_QUIC_LOG_LEVEL_WRN"></a>

## 407.36 `CONFIG_QUIC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_QUIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］ → QUIC 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_QUIC_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_QUIC_MAX_CONTEXTS"></a>

## 407.37 `CONFIG_QUIC_MAX_CONTEXTS`

**提示（Prompt）**：可分配的 QUIC 连接（Connection）最大数量

**说明（Help）**

可同时存在的 QUIC 连接上下文（Connection context）数量。对服务器而言，应等于 `QUIC_MAX_ENDPOINTS`：监听套接字占用一个上下文，每个并发客户端连接再占用一个。如果小于 `QUIC_MAX_ENDPOINTS`，客户端连接数超过 `QUIC_MAX_CONTEXTS - 1` 后，新接受的连接将报错 `Cannot allocate context`，即无法分配上下文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_MAX_ENDPOINTS
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC_MAX_ENDPOINTS`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_MAX_ENDPOINTS)。

<a id="CONFIG_QUIC_MAX_ENDPOINTS"></a>

## 407.38 `CONFIG_QUIC_MAX_ENDPOINTS`

**提示（Prompt）**：可连接的 QUIC 端点（Endpoint）最大数量

**说明（Help）**

系统可创建的 QUIC 端点（Endpoint）数量。通常每个远程服务器对应一个端点；如果远程服务器有多个 UDP 端口，则每个端口分别对应一个端点。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3 if CONFIG_NET_IPV6 && CONFIG_NET_IPV4 && !CONFIG_QUIC_ENDPOINT_USE_IPV4_MAPPING_TO_IPV6
2
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_QUIC_ENDPOINT_USE_IPV4_MAPPING_TO_IPV6`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_ENDPOINT_USE_IPV4_MAPPING_TO_IPV6)。

<a id="CONFIG_QUIC_MAX_IDLE_TIMEOUT"></a>

## 407.39 `CONFIG_QUIC_MAX_IDLE_TIMEOUT`

**提示（Prompt）**：最大空闲超时（Idle timeout，毫秒）

**说明（Help）**

如果任一端点通过传输参数指定最大空闲超时，参见 RFC 9000 第 18.2 节，则连接空闲超过双方通告的 `max_idle_timeout` 的较小值后，会静默关闭连接并丢弃其状态。双方均省略该参数或将其设为 0 时，禁用空闲超时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
30000
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_MAX_PEER_CIDS"></a>

## 407.40 `CONFIG_QUIC_MAX_PEER_CIDS`

**提示（Prompt）**：可跟踪的对端连接 ID（Peer CID）最大数量

**说明（Help）**

需要跟踪的对端连接 ID（CID）数量。对端可提出新的连接 ID，本端需要记录这些 ID，并在需要时切换使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L323)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_MAX_PTO_TIMEOUT_MS"></a>

## 407.41 `CONFIG_QUIC_MAX_PTO_TIMEOUT_MS`

**提示（Prompt）**：QUIC 探测超时（Probe Timeout，PTO）的最大值（毫秒）

**说明（Help）**

QUIC 探测超时（Probe Timeout，PTO）时长的上限，单位为毫秒。连续发生探测超时时，PTO 计时器按指数增长：

```text
PTO_n = PTO_base * 2^pto_count
```

无论指数退避（Exponential backoff）计算结果如何，本选项将 PTO 时长限制在指定毫秒数以内，避免高延迟或高丢包网络上出现过长重传延迟，并使 PTO 不超过配置的连接空闲超时。原文建议：

- 应小于或等于 QUIC 空闲超时。
- 嵌入式系统通常使用 5～10 秒即可。

该值过小，可能使高往返时间（RTT）链路上的连接过早终止。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10000
```

**取值范围（Ranges）**

```text
[1000, 600000]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:476`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L476)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_MAX_REPLIES_PER_PAYLOAD"></a>

## 407.42 `CONFIG_QUIC_MAX_REPLIES_PER_PAYLOAD`

**提示（Prompt）**：针对单个有效载荷中各帧发送的回复数据包最大数量

**说明（Help）**

DATA_BLOCKED、STREAM_DATA_BLOCKED、STREAMS_BLOCKED、PATH_CHALLENGE 和 NEW_CONNECTION_ID 等帧，会各自通过一个独立数据包回复。单个数据报可包含数百个此类帧，若不设上限，一个小数据报就可能触发数百次加密发送，低成本耗尽受限设备的资源。针对单个收到的有效载荷（Payload），超过此数量的回复会被丢弃。对端若仍需要答复，会重发这些帧，因此代价只是延迟。为保证正确性而必须回复的帧，例如 CONNECTION_CLOSE 及确认该数据包的 ACK，不计入此限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L260)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_MAX_STREAMS_BIDI"></a>

## 407.43 `CONFIG_QUIC_MAX_STREAMS_BIDI`

**提示（Prompt）**：可分配的 QUIC 双向流（Bidirectional stream）最大数量

**说明（Help）**

系统中可创建的 QUIC 双向流（Bidirectional stream）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3 if CONFIG_NET_IPV4 && !CONFIG_NET_IPV6
3 if !CONFIG_NET_IPV4 && CONFIG_NET_IPV6
5 if CONFIG_NET_IPV4 && CONFIG_NET_IPV6
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)。

<a id="CONFIG_QUIC_MAX_STREAMS_UNI"></a>

## 407.44 `CONFIG_QUIC_MAX_STREAMS_UNI`

**提示（Prompt）**：可分配的 QUIC 单向流（Unidirectional stream）最大数量

**说明（Help）**

系统中可创建的 QUIC 单向流（Unidirectional stream）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3 if CONFIG_HTTP_SERVER_VERSION_3
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_HTTP_SERVER_VERSION_3`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_3)。

<a id="CONFIG_QUIC_NEW_TOKEN_LIFETIME_SEC"></a>

## 407.45 `CONFIG_QUIC_NEW_TOKEN_LIFETIME_SEC`

**提示（Prompt）**：NEW_TOKEN 生存期（Lifetime，秒）

**说明（Help）**

服务器生成的 NEW_TOKEN 值的最长有效时长（Maximum age）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
600
```

**取值范围（Ranges）**

```text
[1, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L307)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_PKT_ALLOC_TIMEOUT"></a>

## 407.46 `CONFIG_QUIC_PKT_ALLOC_TIMEOUT`

**提示（Prompt）**：分配数据包时的超时（Allocation timeout，毫秒）

**说明（Help）**

指定分配数据包时等待的时长。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:347`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L347)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_PKT_COUNT"></a>

## 407.47 `CONFIG_QUIC_PKT_COUNT`

**提示（Prompt）**：可同时待处理的数据包接收操作数量

**说明（Help）**

QUIC 数据包用于向 QUIC 处理线程传递数据。此值指定可同时活动的套接字操作数量。一个合适的默认值是端点（Endpoint）数量，使每个端点可以同时接收一个数据包。若需更快处理，可设为端点数量的整数倍。每个 `pkt` 占用的数据空间略大于 `CONFIG_QUIC_ENDPOINT_PENDING_DATA_LEN`。每个收到的 UDP 数据包先放入 `pkt` 结构，然后解析其中的 QUIC 数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_MAX_ENDPOINTS
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:332`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L332)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC_MAX_ENDPOINTS`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_MAX_ENDPOINTS)。

<a id="CONFIG_QUIC_RETRY_TOKEN_LIFETIME_SEC"></a>

## 407.48 `CONFIG_QUIC_RETRY_TOKEN_LIFETIME_SEC`

**提示（Prompt）**：Retry 令牌生存期（Token lifetime，秒）

**说明（Help）**

服务器生成的 Retry 令牌（Token）的最长有效时长（Maximum age）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:300`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L300)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_SENT_PKT_HISTORY_SIZE"></a>

## 407.49 `CONFIG_QUIC_SENT_PKT_HISTORY_SIZE`

**提示（Prompt）**：为 RTT 测量与丢包检测而跟踪的已发送数据包数量

**说明（Help）**

用于往返时间（RTT）测量和丢包检测（Loss detection）的近期已发送数据包记录数量。每个表项约占 24 字节内存。较大的值有利于在高延迟或高丢包链路上进行丢包检测。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[16, 256]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:458`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L458)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_SERVER_ANTI_AMPLIFICATION_LIMIT"></a>

## 407.50 `CONFIG_QUIC_SERVER_ANTI_AMPLIFICATION_LIMIT`

**提示（Prompt）**：强制执行服务器反放大限制（Anti-amplification limit）

**说明（Help）**

强制执行 RFC 9000 第 8.1 节的限制：客户端地址验证完成前，服务器向该地址发送的字节数不得超过从该地址收到字节数的三倍。当前实现会延后超出该额度的 CRYPTO 发送，直到有更多接收数据增加额度，或对端地址完成验证，而不是立即关闭连接。仅当互操作或功能测试明确需要绕过限制时，才应禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_SERVER_RETRY"></a>

## 407.51 `CONFIG_QUIC_SERVER_RETRY`

**提示（Prompt）**：服务器新握手必须执行 Retry

**说明（Help）**

对未携带有效地址验证令牌（Address-validation token）的新 Initial 数据包发送 Retry。这样可进行无状态地址验证（Stateless address validation），避免为伪造的 Initial 数据包分配连接状态。仅当互操作测试明确要求直接接受无令牌的 Initial 数据包时，才应禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:232`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L232)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_SERVICE_STACK_SIZE"></a>

## 407.52 `CONFIG_QUIC_SERVICE_STACK_SIZE`

**提示（Prompt）**：处理 QUIC 服务的线程栈大小（Thread stack size）

**说明（Help）**

设置处理 QUIC 连接的线程所用内部栈大小（Stack size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:514`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L514)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_SERVICE_THREAD_PRIO"></a>

## 407.53 `CONFIG_QUIC_SERVICE_THREAD_PRIO`

**提示（Prompt）**：QUIC 服务分派线程（Dispatcher thread）的优先级

**说明（Help）**

设置 QUIC 服务分派线程（Dispatcher thread）的优先级。数值大于或等于 0 表示抢占式线程（Preemptive thread）优先级；原文给出的最低抢占式优先级数值为 `NUM_PREEMPT_PRIORITIES`，最高为 0。最低协作式线程（Cooperative thread）优先级为 -1，最高为 `-NUM_COOP_PRIORITIES`。

译注：保留原文的 `NUM_PREEMPT_PRIORITIES`，未改成其他配置帮助中出现的 `NUM_PREEMPT_PRIORITIES-1`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NUM_PREEMPT_PRIORITIES
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:502`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L502)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NUM_PREEMPT_PRIORITIES`](P001_kernel_配置项参考_1.md#CONFIG_NUM_PREEMPT_PRIORITIES)。

<a id="CONFIG_QUIC_SHELL"></a>

## 407.54 `CONFIG_QUIC_SHELL`

**提示（Prompt）**：创建用于查看 QUIC 连接信息的命令行（Shell）

**说明（Help）**

启用 QUIC 命令行（Shell）支持，让用户监测 QUIC 连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_SHELL
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)。

<a id="CONFIG_QUIC_SOCKOPT_TLS"></a>

## 407.55 `CONFIG_QUIC_SOCKOPT_TLS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 TLS 套接字选项（Socket option）支持，以自动建立到远程主机的 TLS 连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS if CONFIG_NET_NATIVE
```

**弱选择（Implies）**

```text
CONFIG_TLS_CREDENTIALS
CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
CONFIG_MBEDTLS_PEM_PARSE_C
CONFIG_MBEDTLS_X509_CRL_PARSE_C
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_KEY_TYPE_DERIVE
CONFIG_PSA_WANT_ALG_CBC_NO_PADDING
CONFIG_PSA_WANT_ALG_ECB_NO_PADDING
CONFIG_PSA_WANT_ALG_HKDF_EXTRACT
CONFIG_PSA_WANT_ALG_HKDF_EXPAND
CONFIG_PSA_WANT_ALG_GCM
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ALG_SHA_384
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_DERIVE
CONFIG_PSA_WANT_ECC_SECP_R1_256
CONFIG_PSA_WANT_ECC_SECP_R1_384
CONFIG_PSA_WANT_ECC_MONTGOMERY_255
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L367)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_NET_NATIVE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_NATIVE)、[`CONFIG_TLS_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS)、[`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)、[`CONFIG_MBEDTLS_PEM_PARSE_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PEM_PARSE_C)、[`CONFIG_MBEDTLS_X509_CRL_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRL_PARSE_C)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_KEY_TYPE_DERIVE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_DERIVE)、[`CONFIG_PSA_WANT_ALG_CBC_NO_PADDING`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CBC_NO_PADDING)、[`CONFIG_PSA_WANT_ALG_ECB_NO_PADDING`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECB_NO_PADDING)、[`CONFIG_PSA_WANT_ALG_HKDF_EXTRACT`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HKDF_EXTRACT)、[`CONFIG_PSA_WANT_ALG_HKDF_EXPAND`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HKDF_EXPAND)、[`CONFIG_PSA_WANT_ALG_GCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_GCM)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_SHA_384`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_384)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_DERIVE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_DERIVE)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)、[`CONFIG_PSA_WANT_ECC_SECP_R1_384`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_384)、[`CONFIG_PSA_WANT_ECC_MONTGOMERY_255`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_MONTGOMERY_255)。

<a id="CONFIG_QUIC_STATS_HISTORY"></a>

## 407.56 `CONFIG_QUIC_STATS_HISTORY`

**提示（Prompt）**：保留已关闭 QUIC 连接的统计历史（Statistics history）

**说明（Help）**

保留数量受限的已关闭、非监听 QUIC 上下文（Context）的历史，使其销毁后仍能显示最终统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_STATISTICS_QUIC && CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_STATISTICS_QUIC`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_QUIC)、[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_STATS_HISTORY_SIZE"></a>

## 407.57 `CONFIG_QUIC_STATS_HISTORY_SIZE`

**提示（Prompt）**：已关闭 QUIC 连接的统计历史容量（History size）

**说明（Help）**

统计历史中保留的已关闭、非监听 QUIC 上下文（Context）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC_STATS_HISTORY && CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］ → 保留已关闭 QUIC 连接的统计历史（Statistics history）

**配置项引用（Symbol References）**：[`CONFIG_QUIC_STATS_HISTORY`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_STATS_HISTORY)、[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_STREAM_OOO_SEG_SIZE"></a>

## 407.58 `CONFIG_QUIC_STREAM_OOO_SEG_SIZE`

**提示（Prompt）**：缓冲的乱序流报文段（Out-of-order stream segment）的最大大小（字节）

**说明（Help）**

用于保存收到的乱序数据（Out-of-order data）的报文段大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1280
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:452`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L452)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_STREAM_OOO_SLOTS"></a>

## 407.59 `CONFIG_QUIC_STREAM_OOO_SLOTS`

**提示（Prompt）**：每个流的乱序报文段槽位数（Out-of-order segment slots）

**说明（Help）**

每个槽位保存一个乱序 STREAM 帧的有效载荷（Payload），最多为 `QUIC_STREAM_OOO_SEG_SIZE` 字节。较大的值可以处理更严重的乱序，但会增加 RAM 占用，每个流为 `slots * seg_size` 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:444`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L444)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_STREAM_RX_BUFFER_SIZE"></a>

## 407.60 `CONFIG_QUIC_STREAM_RX_BUFFER_SIZE`

**提示（Prompt）**：流接收缓冲区大小（Stream receive buffer size）

**说明（Help）**

每个 QUIC 流的接收缓冲区大小。默认等于 `QUIC_STREAM_TX_BUFFER_SIZE`，适用于回显（Echo）等收发对称的工作负载。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_STREAM_TX_BUFFER_SIZE
```

**取值范围（Ranges）**

```text
[1500, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:436`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L436)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC_STREAM_TX_BUFFER_SIZE`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_STREAM_TX_BUFFER_SIZE)。

<a id="CONFIG_QUIC_STREAM_RX_WINDOW_UPDATE_THRESHOLD"></a>

## 407.61 `CONFIG_QUIC_STREAM_RX_WINDOW_UPDATE_THRESHOLD`

**提示（Prompt）**：触发窗口更新（Window update）的已接收数据百分比

**说明（Help）**

指定接收数据量达到何种阈值后向对端发送窗口更新（Window update）。例如，`QUIC_INITIAL_MAX_STREAM_DATA_BIDI_LOCAL` 为 16 kb 时，将此值设为 25，表示收到 4 kb 数据后向对端发送 MAX_STREAM_DATA 窗口更新消息。

译注：这里保留原文的 `kb` 单位写法；示例表达的是容量的 25%。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
25
```

**取值范围（Ranges）**

```text
[1, 99]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_STREAM_TX_BUFFER_SIZE"></a>

## 407.62 `CONFIG_QUIC_STREAM_TX_BUFFER_SIZE`

**提示（Prompt）**：流已发送但未确认缓冲区大小（Unacked sent buffer size）

**说明（Help）**

每个 QUIC 流的发送缓冲区大小，用于在数据被对端确认（ACK）之前保留这些数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8192
```

**取值范围（Ranges）**

```text
[1500, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:428`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L428)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_TLS_CERT_VERIFY_CALLBACK"></a>

## 407.63 `CONFIG_QUIC_TLS_CERT_VERIFY_CALLBACK`

**提示（Prompt）**：TLS 证书校验回调（Certificate verification callback）支持

**说明（Help）**

控制是否提供 `TLS_CERT_VERIFY_CALLBACK` TLS 套接字选项。该选项允许注册证书校验回调（Certificate verification callback），由 TLS 后端在 TLS 握手（Handshake）期间调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC_SOCKOPT_TLS && CONFIG_QUIC && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:559`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L559)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC_SOCKOPT_TLS`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_TLS_DEBUG_KEYLOG"></a>

## 407.64 `CONFIG_QUIC_TLS_DEBUG_KEYLOG`

**提示（Prompt）**：为调试记录 TLS 秘密值（TLS secrets）

**说明（Help）**

以 NSS 密钥日志格式（NSS Key Log format）记录 TLS 会话秘密值（Session secrets），使 Wireshark 能够解密 QUIC 流量。警告：这会暴露敏感密码材料，只能为调试启用。

在 Wireshark 中进入编辑（Edit）→ 首选项（Preferences）→ 协议（Protocols）→ TLS，将 `(Pre)-Master-Secret log filename` 设置为 TLS 秘密值日志文件的路径。对于 QUIC，还应检查 Protocols → QUIC 的设置。

可按以下原始命令在 `native_sim` 中运行 Zephyr，并将 TLS 秘密值保存到独立文件：

```bash
  build/zephyr/zephyr.exe -attach_uart | \
  tee >(grep --line-buffered "^QUIC_KEYLOG: " | \
        sed -u 's/^QUIC_KEYLOG: //' > tls-secrets.log)
```

也可按以下原始命令启动 Wireshark：

```bash
  wireshark -o tls.keylog_file:tls-secrets.txt capture.pcap
```

译注：两个原始示例分别使用 `tls-secrets.log` 和 `tls-secrets.txt`，此处均予保留；实际配合使用时，应将 Wireshark 指向前一个命令生成的文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:579`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L579)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_TLS_MAX_APP_PROTOCOLS"></a>

## 407.65 `CONFIG_QUIC_TLS_MAX_APP_PROTOCOLS`

**提示（Prompt）**：支持的应用层协议（Application-layer protocol）最大数量

**说明（Help）**

设置可通过套接字选项显式指定的、QUIC 之上支持的应用层协议（Application-layer protocol）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:552`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L552)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_TLS_MAX_CERT_CHAIN_DEPTH"></a>

## 407.66 `CONFIG_QUIC_TLS_MAX_CERT_CHAIN_DEPTH`

**提示（Prompt）**：证书链（Certificate chain）的最大深度

**说明（Help）**

一个证书链（Certificate chain）中证书的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:567`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L567)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_TLS_MAX_CERT_SIZE"></a>

## 407.67 `CONFIG_QUIC_TLS_MAX_CERT_SIZE`

**提示（Prompt）**：证书（Certificate）的最大大小

**说明（Help）**

单个 DER 编码证书（DER-encoded certificate）的最大大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:573`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L573)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_TLS_MAX_CIPHERSUITES"></a>

## 407.68 `CONFIG_QUIC_TLS_MAX_CIPHERSUITES`

**提示（Prompt）**：每个套接字的 TLS/DTLS 密码套件（Cipher suite）最大数量

**说明（Help）**

设置通过套接字选项显式指定时，某个套接字可使用的 TLS 密码套件（Cipher suite）的最大数量。默认情况下，套接字可使用系统中全部可用的密码套件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC_SOCKOPT_TLS && CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:542`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L542)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC_SOCKOPT_TLS`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_TLS_MAX_CREDENTIALS"></a>

## 407.69 `CONFIG_QUIC_TLS_MAX_CREDENTIALS`

**提示（Prompt）**：每个套接字的 TLS 凭据（Credential）最大数量

**说明（Help）**

设置某个套接字可使用的 TLS/DTLS 凭据（Credential）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC_SOCKOPT_TLS && CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:534`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L534)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC_SOCKOPT_TLS`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_TLS_TRANSCRIPT_BUF_LEN"></a>

## 407.70 `CONFIG_QUIC_TLS_TRANSCRIPT_BUF_LEN`

**提示（Prompt）**：TLS 握手记录缓冲区长度（Handshake transcript buffer length，字节）

**说明（Help）**

每个连接使用的缓冲区，累积 TLS 1.3 握手记录（Handshake transcript），包括 ClientHello、ServerHello、Certificate 和 CertificateVerify，用于计算 Finished 消息认证码（MAC）及执行 HKDF 密钥派生（Key derivation）。4096 字节足以容纳使用 RSA-2048 或 EC P-256 证书的典型 TLS 1.3 握手；对于较长证书链或 RSA-4096，应增大到 6144～8192 字节。原始总内存公式为 `Total RAM = QUIC_TLS_TRANSCRIPT_BUF_LEN x QUIC_MAX_CONTEXTS`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC_SOCKOPT_TLS && CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4096
```

**取值范围（Ranges）**

```text
[512, 8192]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:521`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L521)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC_SOCKOPT_TLS`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_TOKEN_CACHE_SIZE"></a>

## 407.71 `CONFIG_QUIC_TOKEN_CACHE_SIZE`

**提示（Prompt）**：NEW_TOKEN 缓存表项（Cache entry）数量

**说明（Help）**

针对不同对端保留的 NEW_TOKEN 值的数量，用于后续客户端连接尝试。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_QUIC_MAX_CONTEXTS
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:292`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L292)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC_MAX_CONTEXTS`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_MAX_CONTEXTS)。

<a id="CONFIG_QUIC_TOKEN_MAX_LEN"></a>

## 407.72 `CONFIG_QUIC_TOKEN_MAX_LEN`

**提示（Prompt）**：QUIC 地址验证令牌（Address-validation token）的最大长度

**说明（Help）**

协议栈为处理 Retry 和 NEW_TOKEN 而在本地保存的令牌最大长度。收到更长的令牌时，会忽略或拒绝它。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[32, CONFIG_QUIC_ENDPOINT_PENDING_DATA_LEN]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:252`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L252)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC_ENDPOINT_PENDING_DATA_LEN`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_ENDPOINT_PENDING_DATA_LEN)。

<a id="CONFIG_QUIC_TOKEN_REPLAY_CACHE_SIZE"></a>

## 407.73 `CONFIG_QUIC_TOKEN_REPLAY_CACHE_SIZE`

**提示（Prompt）**：用于防重放跟踪的地址验证令牌（Address-validation token）数量

**说明（Help）**

记住多少个已接受的地址验证令牌（Address-validation token），以防再次使用。令牌以明文在 Initial 数据包报头中传输，因此观察者可复制令牌，并从伪造地址重放，获取绕过反放大限制（Anti-amplification limit）的端点。当令牌过旧、无法通过有效期检查时，移除相应表项，因此容量只需覆盖可能同时在途的令牌。全部槽位占满时，淘汰最旧表项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 128]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:277`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L277)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_TXRX_DEBUG"></a>

## 407.74 `CONFIG_QUIC_TXRX_DEBUG`

**提示（Prompt）**：调试接收和发送的数据包（Packet）

**说明（Help）**

启用后，打印接收和发送的网络数据包。这可能产生大量输出，因此默认禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC_LOG_LEVEL_DBG && CONFIG_QUIC && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:610`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L610)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC_LOG_LEVEL_DBG`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_LOG_LEVEL_DBG)、[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_QUIC_TX_BUFFER_SIZE"></a>

## 407.75 `CONFIG_QUIC_TX_BUFFER_SIZE`

**提示（Prompt）**：每个端点的数据包发送缓冲区大小（Transmit buffer size）

**说明（Help）**

用于构造待发送 QUIC 数据包的缓冲区大小，至少应等于最大传输单元（MTU）。以太网上通过 IPv4/IPv6 传输 UDP 时，典型值为 1500 字节。最小值 1280 用于满足 IPv6 的最小 MTU 要求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1500
```

**取值范围（Ranges）**

```text
[1280, 1500]
```

**定义位置（Location）**：[`subsys/net/lib/quic/Kconfig:397`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/quic/Kconfig#L397)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → QUIC 支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_RTP"></a>

## 407.76 `CONFIG_RTP`

**提示（Prompt）**：实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］

**说明（Help）**

基于 RFC 3550 的实时传输协议（Real-time Transport Protocol，RTP）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/rtp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/rtp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_RTP_LOCAL_PORT_BASE"></a>

## 407.77 `CONFIG_RTP_LOCAL_PORT_BASE`

**提示（Prompt）**：RTP 本地端口基值（Local Port Base）

**说明（Help）**

用户未指定本地端口时，RTP 本地端口从该基准端口开始分配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTP_TRANSPORT_NET_PKT && CONFIG_RTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
51000
```

**取值范围（Ranges）**

```text
[1024, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/rtp/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/rtp/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］ → RTP 网络数据包传输（Net Pkt transport）

**配置项引用（Symbol References）**：[`CONFIG_RTP_TRANSPORT_NET_PKT`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_TRANSPORT_NET_PKT)、[`CONFIG_RTP`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_RTP_LOG_LEVEL_CHOICE"></a>

## 407.78 `CONFIG_RTP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：RTP 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_RTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_RTP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_RTP_LOG_LEVEL_OFF
CONFIG_RTP_LOG_LEVEL_ERR
CONFIG_RTP_LOG_LEVEL_WRN
CONFIG_RTP_LOG_LEVEL_INF
CONFIG_RTP_LOG_LEVEL_DBG
CONFIG_RTP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_RTP`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_RTP_LOG_LEVEL_DEFAULT`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_LOG_LEVEL_DEFAULT)、[`CONFIG_RTP_LOG_LEVEL_OFF`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_LOG_LEVEL_OFF)、[`CONFIG_RTP_LOG_LEVEL_ERR`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_LOG_LEVEL_ERR)、[`CONFIG_RTP_LOG_LEVEL_WRN`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_LOG_LEVEL_WRN)、[`CONFIG_RTP_LOG_LEVEL_INF`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_LOG_LEVEL_INF)、[`CONFIG_RTP_LOG_LEVEL_DBG`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_LOG_LEVEL_DBG)。

<a id="CONFIG_RTP_LOG_LEVEL_DBG"></a>

## 407.79 `CONFIG_RTP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］ → RTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_RTP_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTP_LOG_LEVEL_DEFAULT"></a>

## 407.80 `CONFIG_RTP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］ → RTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_RTP_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTP_LOG_LEVEL_ERR"></a>

## 407.81 `CONFIG_RTP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］ → RTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_RTP_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTP_LOG_LEVEL_INF"></a>

## 407.82 `CONFIG_RTP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］ → RTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_RTP_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTP_LOG_LEVEL_OFF"></a>

## 407.83 `CONFIG_RTP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］ → RTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_RTP_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTP_LOG_LEVEL_WRN"></a>

## 407.84 `CONFIG_RTP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_RTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］ → RTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_RTP_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_RTP_MAX_CSRC_COUNT"></a>

## 407.85 `CONFIG_RTP_MAX_CSRC_COUNT`

**提示（Prompt）**：RTP 贡献源标识符（CSRC）的最大数量

**说明（Help）**

设置 RTP 报头中贡献源标识符（Contributing Source，CSRC）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`subsys/net/lib/rtp/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/rtp/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_RTP`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_RTP_MCAST_TTL"></a>

## 407.86 `CONFIG_RTP_MCAST_TTL`

**提示（Prompt）**：RTP 多播生存时间（Multicast TTL）

**说明（Help）**

设置多播 RTP 数据包的生存时间（Time to Live，TTL）。对于 IPv6 会话，此值用作多播跳数限制（Multicast hop limit）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
127
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/lib/rtp/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/rtp/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_RTP`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_RTP_TRANSPORT_NET_PKT"></a>

## 407.87 `CONFIG_RTP_TRANSPORT_NET_PKT`

**提示（Prompt）**：RTP 网络数据包传输（Net Pkt transport）

**说明（Help）**

选择 RTP 的网络数据包（Net pkt）传输实现。此实现速度最快，额外开销最小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/rtp/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/rtp/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_RTP`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_RTP_TRANSPORT_SOCKET"></a>

## 407.88 `CONFIG_RTP_TRANSPORT_SOCKET`

**提示（Prompt）**：RTP 套接字传输（Socket transport）

**说明（Help）**

选择 RTP 的套接字传输（Socket transport）实现，这是默认选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS
CONFIG_NET_SOCKETS_SERVICE
```

**定义位置（Location）**：[`subsys/net/lib/rtp/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/rtp/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_RTP`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NET_SOCKETS_SERVICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SERVICE)。

<a id="CONFIG_RTP_TRANSPORT_SOCKET_BUF_SIZE"></a>

## 407.89 `CONFIG_RTP_TRANSPORT_SOCKET_BUF_SIZE`

**提示（Prompt）**：RTP 套接字传输缓冲区大小（Socket buffer size）

**说明（Help）**

发送和接收套接字缓冲区（Socket buffer）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTP_TRANSPORT_SOCKET && CONFIG_RTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`subsys/net/lib/rtp/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/rtp/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］ → RTP 套接字传输（Socket transport）

**配置项引用（Symbol References）**：[`CONFIG_RTP_TRANSPORT_SOCKET`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_TRANSPORT_SOCKET)、[`CONFIG_RTP`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_RTP_TRANSPORT_SOCKET_INIT_PRIO"></a>

## 407.90 `CONFIG_RTP_TRANSPORT_SOCKET_INIT_PRIO`

**提示（Prompt）**：RTP 套接字传输初始化优先级（Initialization priority）

**说明（Help）**

RTP 套接字协议栈的初始化优先级（Initialization priority）。初始化时，全部套接字文件描述符（File descriptor）设为 -1。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTP_TRANSPORT_SOCKET && CONFIG_RTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`subsys/net/lib/rtp/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/rtp/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］ → RTP 套接字传输（Socket transport）

**配置项引用（Symbol References）**：[`CONFIG_RTP_TRANSPORT_SOCKET`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_TRANSPORT_SOCKET)、[`CONFIG_RTP`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_RTP_TRANSPORT_SOCKET_MAX_SESSIONS"></a>

## 407.91 `CONFIG_RTP_TRANSPORT_SOCKET_MAX_SESSIONS`

**提示（Prompt）**：RTP 套接字传输的最大会话数（Maximum sessions）

**说明（Help）**

套接字传输（Socket transport）支持的并发会话数量。每个活动会话占用一个接收套接字文件描述符（RX socket fd）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RTP_TRANSPORT_SOCKET && CONFIG_RTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/rtp/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/rtp/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 实时传输协议（Real-time Transport Protocol，RTP）［实验性，Experimental］ → RTP 套接字传输（Socket transport）

**配置项引用（Symbol References）**：[`CONFIG_RTP_TRANSPORT_SOCKET`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP_TRANSPORT_SOCKET)、[`CONFIG_RTP`](P407_subsys_net_配置项参考_17.md#CONFIG_RTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_SLIP_LOG_LEVEL_CHOICE"></a>

## 407.92 `CONFIG_SLIP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：串行线路互联网协议（SLIP）驱动日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SLIP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_SLIP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SLIP_LOG_LEVEL_OFF
CONFIG_SLIP_LOG_LEVEL_ERR
CONFIG_SLIP_LOG_LEVEL_WRN
CONFIG_SLIP_LOG_LEVEL_INF
CONFIG_SLIP_LOG_LEVEL_DBG
CONFIG_SLIP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 串行线路互联网协议（SLIP）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SLIP`](P131_drivers_net_配置项参考.md#CONFIG_SLIP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)、[`CONFIG_SLIP_LOG_LEVEL_DEFAULT`](P407_subsys_net_配置项参考_17.md#CONFIG_SLIP_LOG_LEVEL_DEFAULT)、[`CONFIG_SLIP_LOG_LEVEL_OFF`](P407_subsys_net_配置项参考_17.md#CONFIG_SLIP_LOG_LEVEL_OFF)、[`CONFIG_SLIP_LOG_LEVEL_ERR`](P407_subsys_net_配置项参考_17.md#CONFIG_SLIP_LOG_LEVEL_ERR)、[`CONFIG_SLIP_LOG_LEVEL_WRN`](P407_subsys_net_配置项参考_17.md#CONFIG_SLIP_LOG_LEVEL_WRN)、[`CONFIG_SLIP_LOG_LEVEL_INF`](P407_subsys_net_配置项参考_17.md#CONFIG_SLIP_LOG_LEVEL_INF)、[`CONFIG_SLIP_LOG_LEVEL_DBG`](P407_subsys_net_配置项参考_17.md#CONFIG_SLIP_LOG_LEVEL_DBG)。

<a id="CONFIG_SLIP_LOG_LEVEL_DBG"></a>

## 407.93 `CONFIG_SLIP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SLIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 串行线路互联网协议（SLIP）驱动 → 串行线路互联网协议（SLIP）驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SLIP_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_SLIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SLIP_LOG_LEVEL_DEFAULT"></a>

## 407.94 `CONFIG_SLIP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SLIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 串行线路互联网协议（SLIP）驱动 → 串行线路互联网协议（SLIP）驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SLIP_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_SLIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SLIP_LOG_LEVEL_ERR"></a>

## 407.95 `CONFIG_SLIP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SLIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 串行线路互联网协议（SLIP）驱动 → 串行线路互联网协议（SLIP）驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SLIP_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_SLIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SLIP_LOG_LEVEL_INF"></a>

## 407.96 `CONFIG_SLIP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SLIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 串行线路互联网协议（SLIP）驱动 → 串行线路互联网协议（SLIP）驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SLIP_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_SLIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SLIP_LOG_LEVEL_OFF"></a>

## 407.97 `CONFIG_SLIP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SLIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 串行线路互联网协议（SLIP）驱动 → 串行线路互联网协议（SLIP）驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SLIP_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_SLIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SLIP_LOG_LEVEL_WRN"></a>

## 407.98 `CONFIG_SLIP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SLIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 串行线路互联网协议（SLIP）驱动 → 串行线路互联网协议（SLIP）驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SLIP_LOG_LEVEL_CHOICE`](P407_subsys_net_配置项参考_17.md#CONFIG_SLIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SNTP"></a>

## 407.99 `CONFIG_SNTP`

**提示（Prompt）**：简单网络时间协议客户端（SNTP client）

**说明（Help）**

启用简单网络时间协议（SNTP）客户端支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_SNTP_LIB
```

**定义位置（Location）**：[`subsys/net/lib/sntp/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sntp/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 简单网络时间协议（Simple Network Time Protocol，SNTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SNTP_LIB`](P407_subsys_net_配置项参考_17.md#CONFIG_SNTP_LIB)。

<a id="CONFIG_SNTP_LIB"></a>

## 407.100 `CONFIG_SNTP_LIB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

简单网络时间协议（SNTP）支持库

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_SNTP
CONFIG_SNTP_SERVER
```

**定义位置（Location）**：[`subsys/net/lib/sntp/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sntp/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 简单网络时间协议（Simple Network Time Protocol，SNTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SNTP`](P407_subsys_net_配置项参考_17.md#CONFIG_SNTP)、[`CONFIG_SNTP_SERVER`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_SERVER)。

<!-- kconfig-navigation -->

[上一章](P406_subsys_net_配置项参考_16.md) · [返回大纲](大纲.md) · [下一章](P408_subsys_net_配置项参考_18.md)
