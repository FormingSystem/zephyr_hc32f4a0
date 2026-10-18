---
id: learning.zephyr-docs.kconfig-reference.page-391
title: "`subsys/net`配置项参考（1/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第391章\_`subsys/net`配置项参考（1/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_COAP"></a>

## 391.1 `CONFIG_COAP`

**提示（Prompt）**：受限应用协议支持（CoAP Support）

**说明（Help）**

启用受限应用协议（CoAP）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_LWM2M
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)。

<a id="CONFIG_COAP_ACK_RANDOM_PERCENT"></a>

## 391.2 `CONFIG_COAP_ACK_RANDOM_PERCENT`

**提示（Prompt）**：ACK 确认超时的随机因子，以百分比表示

**说明（Help）**

用于扩展 CoAP 确认（ACK）超时的因子，以百分比表示。值 `150` 表示因子 `1.50`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_RANDOMIZE_ACK_TIMEOUT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
150
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → 按 RFC 7252 随机化初始 ACK 超时

**配置项引用（Symbol References）**：[`CONFIG_COAP_RANDOMIZE_ACK_TIMEOUT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_RANDOMIZE_ACK_TIMEOUT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_BACKOFF_PERCENT"></a>

## 391.3 `CONFIG_COAP_BACKOFF_PERCENT`

**提示（Prompt）**：ACK 超时的重传退避因子，以百分比表示

**说明（Help）**

重传时扩展 CoAP 确认（ACK）超时的因子，以百分比表示。值 `200` 表示因子 `2.0`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
200
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT"></a>

## 391.4 `CONFIG_COAP_CLIENT`

**提示（Prompt）**：CoAP 客户端支持（client support）

**说明（Help）**

启用用于发送 CoAP 请求的客户端 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_ZVFS
CONFIG_ZVFS_EVENTFD
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_EVENTFD`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_EVENTFD)。

<a id="CONFIG_COAP_CLIENT_BLOCK_SIZE"></a>

## 391.5 `CONFIG_COAP_CLIENT_BLOCK_SIZE`

**提示（Prompt）**：CoAP 分块传输块大小（block-wise transfer block size）

**说明（Help）**

CoAP 客户端执行分块传输（block-wise transfers）时使用的块大小。可选值为 `64`、`128`、`256`、`512` 和 `1024`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_CLIENT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[64, 1024]
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 客户端支持（client support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_CLIENT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT_MAX_EXTRA_OPTIONS"></a>

## 391.6 `CONFIG_COAP_CLIENT_MAX_EXTRA_OPTIONS`

**提示（Prompt）**：应用提供的额外 CoAP 选项数量上限

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_CLIENT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 客户端支持（client support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_CLIENT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT_MAX_INSTANCES"></a>

## 391.7 `CONFIG_COAP_CLIENT_MAX_INSTANCES`

**提示（Prompt）**：CoAP 客户端数量上限

**说明（Help）**

CoAP 客户端数量上限

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_CLIENT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 客户端支持（client support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_CLIENT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT_MAX_PATH_LENGTH"></a>

## 391.8 `CONFIG_COAP_CLIENT_MAX_PATH_LENGTH`

**提示（Prompt）**：路径字符串最大长度（path string length）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_CLIENT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[1, 128]
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 客户端支持（client support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_CLIENT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT_MAX_REQUESTS"></a>

## 391.9 `CONFIG_COAP_CLIENT_MAX_REQUESTS`

**提示（Prompt）**：每个客户端的并发请求数量上限

**说明（Help）**

单个 CoAP 客户端同时处理的请求数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_CLIENT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 客户端支持（client support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_CLIENT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT_MESSAGE_HEADER_SIZE"></a>

## 391.10 `CONFIG_COAP_CLIENT_MESSAGE_HEADER_SIZE`

**提示（Prompt）**：CoAP 头部数据空间（header data）

**说明（Help）**

为处理 CoAP 头部数据额外分配的空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_CLIENT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
48
```

**取值范围（Ranges）**

```text
[24, 128]
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 客户端支持（client support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_CLIENT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT_MESSAGE_SIZE"></a>

## 391.11 `CONFIG_COAP_CLIENT_MESSAGE_SIZE`

**提示（Prompt）**：消息载荷大小（Message payload size）

**说明（Help）**

CoAP 客户端消息载荷（payload）大小，不能小于 `COAP_CLIENT_BLOCK_SIZE`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_CLIENT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_COAP_CLIENT_BLOCK_SIZE
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 客户端支持（client support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_CLIENT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_COAP_CLIENT_BLOCK_SIZE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT_BLOCK_SIZE)。

<a id="CONFIG_COAP_CLIENT_MULTICAST"></a>

## 391.12 `CONFIG_COAP_CLIENT_MULTICAST`

**提示（Prompt）**：CoAP 客户端组播支持（multicast support）

**说明（Help）**

启用 CoAP 客户端的组播请求（multicast request）支持。启用后，请求可指定 `multicast_timeout_ms`，在超时时间内接收不同服务器返回的多个响应。按 RFC 7252，组播请求始终为不确认类型（non-confirmable）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_CLIENT && CONFIG_COAP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 客户端支持（client support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_CLIENT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT_STACK_SIZE"></a>

## 391.13 `CONFIG_COAP_CLIENT_STACK_SIZE`

**提示（Prompt）**：CoAP 客户端线程栈大小（stack size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_CLIENT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 客户端支持（client support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_CLIENT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT_TCP"></a>

## 391.14 `CONFIG_COAP_CLIENT_TCP`

**提示（Prompt）**：CoAP TCP 客户端支持

**说明（Help）**

按 RFC 8323，为可靠传输（reliable transports），即 TCP／TLS，启用 CoAP 客户端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_OVER_RELIABLE_TRANSPORT && CONFIG_COAP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_OVER_RELIABLE_TRANSPORT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_OVER_RELIABLE_TRANSPORT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT_TCP_BLOCKWISE_REUSE_TOKEN"></a>

## 391.15 `CONFIG_COAP_CLIENT_TCP_BLOCKWISE_REUSE_TOKEN`

**提示（Prompt）**：请求后续块时复用请求令牌（request token）

**说明（Help）**

为兼容其他 CoAP 库而提供，例如 `go-coap` 期望在分块传输（blockwise transfers）期间复用令牌（token）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_OVER_RELIABLE_TRANSPORT && CONFIG_COAP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:230`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L230)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_OVER_RELIABLE_TRANSPORT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_OVER_RELIABLE_TRANSPORT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT_TCP_EXCHANGE_LIFETIME"></a>

## 391.16 `CONFIG_COAP_CLIENT_TCP_EXCHANGE_LIFETIME`

**提示（Prompt）**：TCP CoAP 交换生存时间（毫秒，exchange lifetime）

**说明（Help）**

TCP CoAP 从初始请求到最终响应的最长交换生存时间（exchange lifetime），用于确定何时能够安全释放请求上下文（request contexts）。原文依据 RFC 8323 说明，默认值为 247 秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_OVER_RELIABLE_TRANSPORT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
247000
```

**取值范围（Ranges）**

```text
[60000, 600000]
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_OVER_RELIABLE_TRANSPORT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_OVER_RELIABLE_TRANSPORT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT_TCP_REQUEST_TIMEOUT"></a>

## 391.17 `CONFIG_COAP_CLIENT_TCP_REQUEST_TIMEOUT`

**提示（Prompt）**：TCP CoAP 请求超时（毫秒）

**说明（Help）**

基于 TCP 的 CoAP 请求超时时间。与 UDP 不同，TCP 请求只有一次超时，不进行重传（retransmission）。原文依据 RFC 8323 建议默认 30 秒，范围为 1～300 秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_OVER_RELIABLE_TRANSPORT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
30000
```

**取值范围（Ranges）**

```text
[1000, 300000]
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L212)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_OVER_RELIABLE_TRANSPORT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_OVER_RELIABLE_TRANSPORT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_CLIENT_THREAD_PRIORITY"></a>

## 391.18 `CONFIG_COAP_CLIENT_THREAD_PRIORITY`

**提示（Prompt）**：CoAP 客户端线程优先级（thread priority）

**说明（Help）**

CoAP 客户端接收线程（receive thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_CLIENT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NUM_PREEMPT_PRIORITIES
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 客户端支持（client support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_CLIENT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NUM_PREEMPT_PRIORITIES`](P001_kernel_配置项参考_1.md#CONFIG_NUM_PREEMPT_PRIORITIES)。

<a id="CONFIG_COAP_CLIENT_TRUNCATE_MSGS"></a>

## 391.19 `CONFIG_COAP_CLIENT_TRUNCATE_MSGS`

**提示（Prompt）**：块被截断时接收通知（truncation notification）

**说明（Help）**

在传给 `zsock_recvfrom()` 的标志中加入 `ZSOCK_MSG_TRUNC`，接收网络协议栈关于块截断（block truncation）的通知；否则截断会静默发生。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_CLIENT && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 客户端支持（client support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_CLIENT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_CLIENT)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_EXTENDED_OPTIONS_LEN"></a>

## 391.20 `CONFIG_COAP_EXTENDED_OPTIONS_LEN`

**提示（Prompt）**：支持 CoAP 扩展选项（extended options）

**说明（Help）**

启用 CoAP 扩展选项长度（extended options length）的解析。扩展长度值可占 2 字节，需要更多内存。禁用可节省内存，但默认仅支持最大 12 字节的长度；需要大于 12 的长度字段时应启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_EXTENDED_OPTIONS_LEN_VALUE"></a>

## 391.21 `CONFIG_COAP_EXTENDED_OPTIONS_LEN_VALUE`

**提示（Prompt）**：CoAP 扩展选项长度值（length value）

**说明（Help）**

启用 `COAP_EXTENDED_OPTIONS_LEN` 时，指定长度字段的最大值。应根据用户需求定义。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_EXTENDED_OPTIONS_LEN && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
13
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → 支持 CoAP 扩展选项（extended options）

**配置项引用（Symbol References）**：[`CONFIG_COAP_EXTENDED_OPTIONS_LEN`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_EXTENDED_OPTIONS_LEN)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_INIT_ACK_TIMEOUT_MS"></a>

## 391.22 `CONFIG_COAP_INIT_ACK_TIMEOUT_MS`

**提示（Prompt）**：随机生成初始 ACK 超时的基准时长（毫秒）

**说明（Help）**

用于重试待处理 CoAP 数据包的基准值（base value）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2000
```

**取值范围（Ranges）**

```text
[1000, 100000]
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/sparkfun_sara_r4/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/sparkfun_sara_r4/Kconfig.defconfig)。

```text
20000
```

来源：[`boards/shields/st87mxx/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st87mxx/Kconfig.defconfig)。

```text
20000
```

来源：[`boards/shields/wnc_m14a2a/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/wnc_m14a2a/Kconfig.defconfig)。

```text
20000
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_KEEP_USER_DATA"></a>

## 391.23 `CONFIG_COAP_KEEP_USER_DATA`

**提示（Prompt）**：在 CoAP 数据包中保留用户数据（user data）

**说明（Help）**

启用保留应用专用用户数据（application-specific user data）的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_LOG_LEVEL_CHOICE"></a>

## 391.24 `CONFIG_COAP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：CoAP 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_COAP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_COAP_LOG_LEVEL_OFF
CONFIG_COAP_LOG_LEVEL_ERR
CONFIG_COAP_LOG_LEVEL_WRN
CONFIG_COAP_LOG_LEVEL_INF
CONFIG_COAP_LOG_LEVEL_DBG
CONFIG_COAP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_COAP_LOG_LEVEL_DEFAULT`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_LOG_LEVEL_DEFAULT)、[`CONFIG_COAP_LOG_LEVEL_OFF`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_LOG_LEVEL_OFF)、[`CONFIG_COAP_LOG_LEVEL_ERR`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_LOG_LEVEL_ERR)、[`CONFIG_COAP_LOG_LEVEL_WRN`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_LOG_LEVEL_WRN)、[`CONFIG_COAP_LOG_LEVEL_INF`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_LOG_LEVEL_INF)、[`CONFIG_COAP_LOG_LEVEL_DBG`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_LOG_LEVEL_DBG)。

<a id="CONFIG_COAP_LOG_LEVEL_DBG"></a>

## 391.25 `CONFIG_COAP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_COAP_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COAP_LOG_LEVEL_DEFAULT"></a>

## 391.26 `CONFIG_COAP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_COAP_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COAP_LOG_LEVEL_ERR"></a>

## 391.27 `CONFIG_COAP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_COAP_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COAP_LOG_LEVEL_INF"></a>

## 391.28 `CONFIG_COAP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_COAP_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COAP_LOG_LEVEL_OFF"></a>

## 391.29 `CONFIG_COAP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_COAP_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COAP_LOG_LEVEL_WRN"></a>

## 391.30 `CONFIG_COAP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_COAP_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_COAP_MAX_RETRANSMIT"></a>

## 391.31 `CONFIG_COAP_MAX_RETRANSMIT`

**提示（Prompt）**：CoAP 数据包最大重传次数（Max retransmission）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_OSCORE"></a>

## 391.32 `CONFIG_COAP_OSCORE`

**提示（Prompt）**：CoAP 的受限 RESTful 环境对象安全支持（OSCORE，RFC 8613）【实验性 EXPERIMENTAL】

**说明（Help）**

为 CoAP 服务器启用受限 RESTful 环境对象安全（Object Security for Constrained RESTful Environments，OSCORE）。OSCORE 使用 CBOR 对象签名与加密（COSE）为 CoAP 消息提供端到端保护（end-to-end protection）。需要 `uoscore-uedhoc` 模块和 PSA Crypto 支持。启用后，可通过支持 OSCORE 的服务保护 CoAP 消息。详情参见 RFC 8613。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UOSCORE && CONFIG_PSA_CRYPTO && CONFIG_COAP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig.oscore:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig.oscore#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_UOSCORE`](P253_modules_uoscore-uedhoc_配置项参考.md#CONFIG_UOSCORE)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_COAP_OSCORE_CONTEXT_REUSE"></a>

## 391.33 `CONFIG_COAP_OSCORE_CONTEXT_REUSE`

**提示（Prompt）**：支持跨重启复用 OSCORE 上下文（context reuse）

**说明（Help）**

允许设备重启后复用 OSCORE 安全上下文（security contexts）。复用时，必须将发送方序列号（Sender Sequence Number，SSN）持久化到非易失性存储，防止带关联数据认证加密（AEAD）的一次性数（nonce）重用；重用会造成灾难性的密码安全后果。

SSN 通过 Zephyr 设置子系统自动持久化，该功能由 `UOSCORE_NVM_SUPPORT` 选择。因此，应用需要正常工作的 settings 后端，例如存储分区及匹配的 `CONFIG_SETTINGS_NVS` 后端。不能保证每次启动都有全新上下文的应用，例如未通过 EDHOC 密钥派生获得新上下文，必须启用此项；其他部署应保持禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_OSCORE && CONFIG_COAP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_UOSCORE_NVM_SUPPORT
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig.oscore:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig.oscore#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 的受限 RESTful 环境对象安全支持（OSCORE，RFC 8613）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_COAP_OSCORE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_OSCORE)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_UOSCORE_NVM_SUPPORT`](P253_modules_uoscore-uedhoc_配置项参考.md#CONFIG_UOSCORE_NVM_SUPPORT)。

<a id="CONFIG_COAP_OSCORE_EXCHANGE_CACHE_SIZE"></a>

## 391.34 `CONFIG_COAP_OSCORE_EXCHANGE_CACHE_SIZE`

**提示（Prompt）**：每个服务的 OSCORE 交换缓存大小（exchange cache size）

**说明（Help）**

每个服务端点（service endpoint）缓存的 OSCORE 交换条目数量，用于跟踪哪些进行中的交换需要受 OSCORE 保护的响应。每个条目保存客户端地址及令牌信息，以按 RFC 8613 第 8.3 节将响应匹配到 OSCORE 请求。

同步响应也经过此缓存：处理函数运行前加入条目，发送响应后移除。观察通知（Observe notifications）完全绕过缓存，使用各观察者自己的 OSCORE 上下文。缓存大小应按预期最大并发在途请求数量设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_OSCORE && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig.oscore:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig.oscore#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 的受限 RESTful 环境对象安全支持（OSCORE，RFC 8613）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_COAP_OSCORE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_OSCORE)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_OSCORE_EXCHANGE_LIFETIME_MS"></a>

## 391.35 `CONFIG_COAP_OSCORE_EXCHANGE_LIFETIME_MS`

**提示（Prompt）**：OSCORE 交换生存时间（毫秒，exchange lifetime）

**说明（Help）**

所跟踪 OSCORE 交换条目的生存时间。实际过期只影响延迟、分离式响应（deferred/separate responses），即请求处理函数返回后才生成的响应。同步响应总能找到刚创建的有效条目，而观察通知（Observe notifications）完全绕过缓存。

超过此时间后，延迟交换条目被视为过期并移除。此后生成的分离式响应被视为无效：要求 OSCORE 的服务会将其丢弃，按失败即拒绝的方式处理（fail-closed）；同时接受未保护客户端的混合服务则无法将其匹配到交换，因而会以未保护形式发送。若资源可能延迟响应这么久，应将本值保持为不小于 CoAP `EXCHANGE_LIFETIME`。默认 247 秒，与 RFC 7252 第 4.8.2 节的 CoAP `EXCHANGE_LIFETIME` 一致。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_OSCORE && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
247000
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig.oscore:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig.oscore#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 的受限 RESTful 环境对象安全支持（OSCORE，RFC 8613）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_COAP_OSCORE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_OSCORE)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_OSCORE_MASTER_SALT_MAX_LEN"></a>

## 391.36 `CONFIG_COAP_OSCORE_MASTER_SALT_MAX_LEN`

**提示（Prompt）**：OSCORE 主盐值最大长度（Master Salt，字节）

**说明（Help）**

每个上下文用于保存 OSCORE 主盐值（Master Salt）的缓冲区大小。主盐值是可选的，见 RFC 8613 第 3.1 节，可以为空；提供时通常为 8 字节。设为 `0` 可完全禁用主盐值存储，此时只能配置空盐值上下文。若部署使用更长盐值，应增大本项。`CONFIG_COAP_OSCORE_MAX_CONTEXTS` 个上下文中的每一个都会预留此数量的字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_OSCORE && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[0, 64]
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig.oscore:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig.oscore#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 的受限 RESTful 环境对象安全支持（OSCORE，RFC 8613）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_COAP_OSCORE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_OSCORE)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_OSCORE_MASTER_SECRET_MAX_LEN"></a>

## 391.37 `CONFIG_COAP_OSCORE_MASTER_SECRET_MAX_LEN`

**提示（Prompt）**：OSCORE 主秘密最大长度（Master Secret，字节）

**说明（Help）**

每个上下文用于保存 OSCORE 主秘密（Master Secret）的缓冲区大小。它是应用选择的可变长 HKDF 输入密钥材料（input keying material），见 RFC 8613 第 3.1 节。AES-CCM-16-64-128 配置的常见长度为 16 字节。若部署使用更长秘密，应增大本项。`CONFIG_COAP_OSCORE_MAX_CONTEXTS` 个上下文中的每一个都会预留此数量的字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_OSCORE && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[16, 64]
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig.oscore:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig.oscore#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 的受限 RESTful 环境对象安全支持（OSCORE，RFC 8613）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_COAP_OSCORE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_OSCORE)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_OSCORE_MAX_CONTEXTS"></a>

## 391.38 `CONFIG_COAP_OSCORE_MAX_CONTEXTS`

**提示（Prompt）**：OSCORE 安全上下文数量上限

**说明（Help）**

可通过 `coap_oscore_context_init()` 在运行时分配的 OSCORE 安全上下文数量。每个上下文用于保护和验证某个 CoAP 客户端或服务的消息。应用同时使用多个 OSCORE 端点时，应增大本项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_OSCORE && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig.oscore:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig.oscore#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 的受限 RESTful 环境对象安全支持（OSCORE，RFC 8613）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_COAP_OSCORE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_OSCORE)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_OVER_RELIABLE_TRANSPORT"></a>

## 391.39 `CONFIG_COAP_OVER_RELIABLE_TRANSPORT`

**提示（Prompt）**：可靠传输上的 CoAP（RFC 8323）【实验性 EXPERIMENTAL】

**说明（Help）**

启用 RFC 8323 实现支持，即在 TCP、TLS 和 WebSocket 上传输受限应用协议（CoAP）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_COAP_RANDOMIZE_ACK_TIMEOUT"></a>

## 391.40 `CONFIG_COAP_RANDOMIZE_ACK_TIMEOUT`

**提示（Prompt）**：按 RFC 7252 随机化初始 ACK 超时

**说明（Help）**

启用后，按 RFC 7252 随机化初始确认（ACK）超时，在 `ACK_TIMEOUT` 与 `ACK_TIMEOUT * ACK_RANDOM_FACTOR` 之间取随机值，其中 `ACK_TIMEOUT` 由 `COAP_INIT_ACK_TIMEOUT_MS` 指定。否则，初始 ACK 超时固定为 `COAP_INIT_ACK_TIMEOUT_MS` 的值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_SERVER"></a>

## 391.41 `CONFIG_COAP_SERVER`

**提示（Prompt）**：CoAP 服务器支持（server support）

**说明（Help）**

启用供 CoAP 服务注册资源（resources）的 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS
CONFIG_NET_CONTEXT_RECV_PKTINFO if CONFIG_NET_UDP
CONFIG_ZVFS
CONFIG_ZVFS_EVENTFD
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_NET_CONTEXT_RECV_PKTINFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONTEXT_RECV_PKTINFO)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_EVENTFD`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_EVENTFD)。

<a id="CONFIG_COAP_SERVER_BLOCK_SIZE"></a>

## 391.42 `CONFIG_COAP_SERVER_BLOCK_SIZE`

**提示（Prompt）**：CoAP 服务器分块传输大小（block-wise transfer size）

**说明（Help）**

CoAP 服务器资源执行分块传输（block-wise transfers）时使用的块大小，可选 `64`、`128`、`256`、`512` 和 `1024`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_SERVER && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[64, 1024]
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_SERVER_MESSAGE_OPTIONS"></a>

## 391.43 `CONFIG_COAP_SERVER_MESSAGE_OPTIONS`

**提示（Prompt）**：CoAP 服务器消息选项（message options）

**说明（Help）**

CoAP 服务器消息可解析的最大选项数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_SERVER && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:276`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L276)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_SERVER_MESSAGE_SIZE"></a>

## 391.44 `CONFIG_COAP_SERVER_MESSAGE_SIZE`

**提示（Prompt）**：CoAP 服务器消息载荷大小（payload size）

**说明（Help）**

CoAP 服务器消息载荷大小，不能小于 `COAP_SERVER_BLOCK_SIZE`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_SERVER && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_COAP_SERVER_BLOCK_SIZE
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:270`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L270)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_COAP_SERVER_BLOCK_SIZE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER_BLOCK_SIZE)。

<a id="CONFIG_COAP_SERVER_PENDING_ALLOCATOR"></a>

## 391.45 `CONFIG_COAP_SERVER_PENDING_ALLOCATOR`

**提示（Prompt）**：待处理数据分配器（Pending data allocator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_SERVER && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_COAP_SERVER_PENDING_ALLOCATOR_STATIC
```

**可选项（Choices）**

```text
CONFIG_COAP_SERVER_PENDING_ALLOCATOR_NONE
CONFIG_COAP_SERVER_PENDING_ALLOCATOR_STATIC
CONFIG_COAP_SERVER_PENDING_ALLOCATOR_SYSTEM_HEAP
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:300`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L300)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_COAP_SERVER_PENDING_ALLOCATOR_STATIC`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER_PENDING_ALLOCATOR_STATIC)、[`CONFIG_COAP_SERVER_PENDING_ALLOCATOR_NONE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER_PENDING_ALLOCATOR_NONE)、[`CONFIG_COAP_SERVER_PENDING_ALLOCATOR_SYSTEM_HEAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER_PENDING_ALLOCATOR_SYSTEM_HEAP)。

<a id="CONFIG_COAP_SERVER_PENDING_ALLOCATOR_NONE"></a>

## 391.46 `CONFIG_COAP_SERVER_PENDING_ALLOCATOR_NONE`

**提示（Prompt）**：不保留待处理数据包（No pending packets）

**说明（Help）**

不为待处理请求分配数据空间，因此禁用需确认数据包（confirmable packets）的重传。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COAP_SERVER_PENDING_ALLOCATOR>
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:304`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L304)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support） → 待处理数据分配器（Pending data allocator）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER_PENDING_ALLOCATOR`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER_PENDING_ALLOCATOR)。

<a id="CONFIG_COAP_SERVER_PENDING_ALLOCATOR_STATIC"></a>

## 391.47 `CONFIG_COAP_SERVER_PENDING_ALLOCATOR_STATIC`

**提示（Prompt）**：静态预留内存（Static reserved memory）

**说明（Help）**

为待处理消息预留静态内存，总大小等于 `COAP_SERVER_PENDING_ALLOCATOR_STATIC_BLOCKS * COAP_SERVER_MESSAGE_SIZE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COAP_SERVER_PENDING_ALLOCATOR>
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:310`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L310)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support） → 待处理数据分配器（Pending data allocator）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER_PENDING_ALLOCATOR`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER_PENDING_ALLOCATOR)。

<a id="CONFIG_COAP_SERVER_PENDING_ALLOCATOR_STATIC_BLOCKS"></a>

## 391.48 `CONFIG_COAP_SERVER_PENDING_ALLOCATOR_STATIC_BLOCKS`

**提示（Prompt）**：待处理数据块数量（pending data blocks）

**说明（Help）**

为等待重传的消息预留的数据块数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_SERVER_PENDING_ALLOCATOR_STATIC && CONFIG_COAP_SERVER && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_COAP_SERVICE_PENDING_MESSAGES
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:324`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L324)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER_PENDING_ALLOCATOR_STATIC`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER_PENDING_ALLOCATOR_STATIC)、[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_COAP_SERVICE_PENDING_MESSAGES`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVICE_PENDING_MESSAGES)。

<a id="CONFIG_COAP_SERVER_PENDING_ALLOCATOR_SYSTEM_HEAP"></a>

## 391.49 `CONFIG_COAP_SERVER_PENDING_ALLOCATOR_SYSTEM_HEAP`

**提示（Prompt）**：系统堆分配器（System heap allocator）

**说明（Help）**

使用 `k_malloc`／`k_free` 分配和释放待处理数据（pending data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HEAP_MEM_POOL_SIZE > 0 && <choice CONFIG_COAP_SERVER_PENDING_ALLOCATOR>
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:316`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L316)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support） → 待处理数据分配器（Pending data allocator）

**配置项引用（Symbol References）**：[`CONFIG_HEAP_MEM_POOL_SIZE`](P001_kernel_配置项参考_1.md#CONFIG_HEAP_MEM_POOL_SIZE)、[`CONFIG_COAP_SERVER_PENDING_ALLOCATOR`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER_PENDING_ALLOCATOR)。

<a id="CONFIG_COAP_SERVER_SHELL"></a>

## 391.50 `CONFIG_COAP_SERVER_SHELL`

**提示（Prompt）**：CoAP 服务命令行命令（shell commands）

**说明（Help）**

启用 CoAP 服务命令行命令（shell commands）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_COAP_SERVER && CONFIG_COAP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:339`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L339)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_SERVER_STACK_SIZE"></a>

## 391.51 `CONFIG_COAP_SERVER_STACK_SIZE`

**提示（Prompt）**：CoAP 服务器线程栈大小（thread stack size）

**说明（Help）**

处理接收／发送（RX/TX）事件的 CoAP 服务器线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_SERVER && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_SERVER_TRUNCATE_MSGS"></a>

## 391.52 `CONFIG_COAP_SERVER_TRUNCATE_MSGS`

**提示（Prompt）**：处理截断的消息（truncated messages）

**说明（Help）**

在传给 `zsock_recvfrom()` 的标志中加入 `ZSOCK_MSG_TRUNC`，接收网络协议栈关于块截断（block truncation）的通知；否则截断会静默发生。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_SERVER && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:331`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L331)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_SERVER_WELL_KNOWN_CORE"></a>

## 391.53 `CONFIG_COAP_SERVER_WELL_KNOWN_CORE`

**提示（Prompt）**：CoAP 服务器支持 ./well-known/core 服务

**说明（Help）**

启用对 `./well-known/core` 服务资源的响应。译注：这里按原文保留资源路径写法 `./well-known/core`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_SERVER && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:282`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L282)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_SERVICE_OBSERVERS"></a>

## 391.54 `CONFIG_COAP_SERVICE_OBSERVERS`

**提示（Prompt）**：CoAP 服务观察者（observers）

**说明（Help）**

每个活动服务的 CoAP 观察者（observers）数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_SERVER && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:294`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L294)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_SERVICE_PENDING_MESSAGES"></a>

## 391.55 `CONFIG_COAP_SERVICE_PENDING_MESSAGES`

**提示（Prompt）**：CoAP 服务待处理消息（pending messages）

**说明（Help）**

每个活动服务中等待重传的 CoAP 消息数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_SERVER && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:288`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L288)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP 服务器支持（server support）

**配置项引用（Symbol References）**：[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_TEST_API_ENABLE"></a>

## 391.56 `CONFIG_COAP_TEST_API_ENABLE`

**提示（Prompt）**：CoAP 单元测试的测试 API（Test API）

**说明（Help）**

正常使用时不要启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_URI_WILDCARD"></a>

## 391.57 `CONFIG_COAP_URI_WILDCARD`

**提示（Prompt）**：CoAP 资源路径中的通配符（Wildcards）

**说明（Help）**

在路径中启用 MQTT 风格的通配符（wildcards）。若资源路径可能包含加号 `+` 或井号 `#`，则禁用本项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_COAP_WELL_KNOWN_BLOCK_WISE"></a>

## 391.58 `CONFIG_COAP_WELL_KNOWN_BLOCK_WISE`

**提示（Prompt）**：CoAP ./well-known/core 服务的分块支持（block wise）

**说明（Help）**

启用对 `./well-known/core` 请求响应的分块支持。未启用时，全部资源信息通过一个 IP 数据包发送，依据最大传输单元（MTU）大小可能分成多个分片。此功能适用于网状网络（mesh networks）。启用 `CONFIG_SYS_HASH_FUNC32` 时，响应包含实体标签（ETag）选项，客户端可据此验证重组的块是否属于同一表示（representation），见 RFC 7959 第 2.4 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP && CONFIG_NETWORKING
```

**弱选择（Implies）**

```text
CONFIG_SYS_HASH_FUNC32
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support）

**配置项引用（Symbol References）**：[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_SYS_HASH_FUNC32`](P198_lib_配置项参考_2.md#CONFIG_SYS_HASH_FUNC32)。

<a id="CONFIG_COAP_WELL_KNOWN_BLOCK_WISE_SIZE"></a>

## 391.59 `CONFIG_COAP_WELL_KNOWN_BLOCK_WISE_SIZE`

**提示（Prompt）**：CoAP ./well-known/core 服务的分块支持（block wise）

**说明（Help）**

CoAP 块最大大小，有效值为 `16`、`32`、`64`、`128`、`256`、`512` 和 `1024`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COAP_WELL_KNOWN_BLOCK_WISE && CONFIG_COAP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/net/lib/coap/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 受限应用协议支持（CoAP Support） → CoAP ./well-known/core 服务的分块支持（block wise）

**配置项引用（Symbol References）**：[`CONFIG_COAP_WELL_KNOWN_BLOCK_WISE`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_WELL_KNOWN_BLOCK_WISE)、[`CONFIG_COAP`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_CONNECTIVITY_WIFI_MGMT_APPLICATION"></a>

## 391.60 `CONFIG_CONNECTIVITY_WIFI_MGMT_APPLICATION`

**提示（Prompt）**：连接后端的应用专用实现（connectivity backend）

**说明（Help）**

应用提供自定义的 `CONNECTIVITY_WIFI_MGMT` 实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CONNECTIVITY_WIFI_MGMT_IMPL>
```

**定义位置（Location）**：[`subsys/net/conn_mgr/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/conn_mgr/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager） → 通用 Wi-Fi 管理连接实现（connectivity implementation） → 通用 `wifi_mgmt` 连接后端（connectivity backend）的实现。

**配置项引用（Symbol References）**：[`CONFIG_CONNECTIVITY_WIFI_MGMT_IMPL`](P391_subsys_net_配置项参考_1.md#CONFIG_CONNECTIVITY_WIFI_MGMT_IMPL)。

<a id="CONFIG_CONNECTIVITY_WIFI_MGMT_IMPL"></a>

## 391.61 `CONFIG_CONNECTIVITY_WIFI_MGMT_IMPL`

**提示（Prompt）**：通用 `wifi_mgmt` 连接后端（connectivity backend）的实现。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONNECTION_MANAGER_CONNECTIVITY_WIFI_MGMT && CONFIG_NET_CONNECTION_MANAGER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_CONNECTIVITY_WIFI_MGMT_APPLICATION
```

**可选项（Choices）**

```text
CONFIG_CONNECTIVITY_WIFI_MGMT_APPLICATION
```

**定义位置（Location）**：[`subsys/net/conn_mgr/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/conn_mgr/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager） → 通用 Wi-Fi 管理连接实现（connectivity implementation）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONNECTION_MANAGER_CONNECTIVITY_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONNECTION_MANAGER_CONNECTIVITY_WIFI_MGMT)、[`CONFIG_NET_CONNECTION_MANAGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONNECTION_MANAGER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_CONNECTIVITY_WIFI_MGMT_APPLICATION`](P391_subsys_net_配置项参考_1.md#CONFIG_CONNECTIVITY_WIFI_MGMT_APPLICATION)。

<a id="CONFIG_DNS_NUM_CONCUR_QUERIES"></a>

## 391.62 `CONFIG_DNS_NUM_CONCUR_QUERIES`

**提示（Prompt）**：每个 DNS 上下文的并发查询数量

**说明（Help）**

使用同一个域名系统（DNS）上下文可同时发起的查询数量。通常 `1` 是合适的默认值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_RECONFIGURE_CLEANUP"></a>

## 391.63 `CONFIG_DNS_RECONFIGURE_CLEANUP`

**提示（Prompt）**：重新配置时清理旧 DNS 服务器条目

**说明（Help）**

调用 `dns_resolve_reconfigure()` 设置新 DNS 服务器时，例如从 DHCP 服务器收到新配置时，先移除旧条目再设置新条目。只有一个网络接口时可启用；有多个接口时应禁用，否则后续接口配置更新会删除其他接口先前设置的条目。

原文说明：Zephyr 4.1 及更早版本默认启用此项，Zephyr 4.2 默认改为禁用。此处保留原文的版本说明。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_RESOLVER"></a>

## 391.64 `CONFIG_DNS_RESOLVER`

**提示（Prompt）**：域名系统解析器（DNS resolver）

**说明（Help）**

为 Zephyr 启用 DNS 客户端支持（client-side support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS
CONFIG_NET_SOCKETS_SERVICE
CONFIG_CRC
```

**被选择（Selected by）**

```text
CONFIG_MDNS_RESPONDER_PROBE
CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED
CONFIG_SHELL_BACKEND_MQTT
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_NET_SOCKETS_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SERVICE)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)、[`CONFIG_MDNS_RESPONDER_PROBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESPONDER_PROBE)、[`CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED)、[`CONFIG_SHELL_BACKEND_MQTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_MQTT)。

<a id="CONFIG_DNS_RESOLVER_ADDITIONAL_BUF_CTR"></a>

## 391.65 `CONFIG_DNS_RESOLVER_ADDITIONAL_BUF_CTR`

**提示（Prompt）**：附加 DNS 缓冲区（Additional buffers）

**说明（Help）**

DNS 解析器可用的附加缓冲区数量。解析器至少需要一个缓冲区；本选项补充并发 DNS 服务器连接所需的缓冲区，因此默认值随配置的 DNS 服务器数量变化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_SOCKET_DISPATCHER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_DNS_RESOLVER_MAX_SERVERS
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:540`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L540)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SOCKET_DISPATCHER`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_DNS_RESOLVER_MAX_SERVERS`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_MAX_SERVERS)。

<a id="CONFIG_DNS_RESOLVER_ADDITIONAL_QUERIES"></a>

## 391.66 `CONFIG_DNS_RESOLVER_ADDITIONAL_QUERIES`

**提示（Prompt）**：附加 DNS 查询（Additional queries）

**说明（Help）**

资源记录（RR）的回答（ANSWER）部分只包含规范名称（CNAME）时，DNS 解析器可额外发起的查询数量。为避免别名循环（alias loops），本变量的最大值受到限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_RESOLVER_AI_MAX_ENTRIES"></a>

## 391.67 `CONFIG_DNS_RESOLVER_AI_MAX_ENTRIES`

**提示（Prompt）**：每个 DNS 名称的 IP 地址数量上限

**说明（Help）**

定义 DNS 解析器对每次域名解析可处理的 IP 地址数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_RESOLVER_AUTO_INIT"></a>

## 391.68 `CONFIG_DNS_RESOLVER_AUTO_INIT`

**提示（Prompt）**：自动初始化默认 DNS 上下文（context）

**说明（Help）**

自动初始化默认 DNS 上下文，无需手动调用 `dns_resolve_init`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_RESOLVER_CACHE"></a>

## 391.69 `CONFIG_DNS_RESOLVER_CACHE`

**提示（Prompt）**：DNS 解析器缓存（resolver cache）

**说明（Help）**

启用 DNS 解析器缓存。按照生存时间（TTL）缓存查询结果，并尽可能从缓存提供结果，减少网络使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_RESOLVER_CACHE_MAX_ENTRIES"></a>

## 391.70 `CONFIG_DNS_RESOLVER_CACHE_MAX_ENTRIES`

**提示（Prompt）**：DNS 缓存支持的条目数量（cache entries）

**说明（Help）**

定义 DNS 缓存可容纳的条目数量。没有足够条目空间时，替换最旧条目。调整此值会影响 RAM 使用量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER_CACHE && CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
6
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:196`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L196)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → DNS 解析器缓存（resolver cache）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER_CACHE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_CACHE)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE"></a>

## 391.71 `CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：DNS 解析器日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_DNS_RESOLVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DNS_RESOLVER_LOG_LEVEL_OFF
CONFIG_DNS_RESOLVER_LOG_LEVEL_ERR
CONFIG_DNS_RESOLVER_LOG_LEVEL_WRN
CONFIG_DNS_RESOLVER_LOG_LEVEL_INF
CONFIG_DNS_RESOLVER_LOG_LEVEL_DBG
CONFIG_DNS_RESOLVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_DNS_RESOLVER_LOG_LEVEL_DEFAULT`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_LOG_LEVEL_DEFAULT)、[`CONFIG_DNS_RESOLVER_LOG_LEVEL_OFF`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_LOG_LEVEL_OFF)、[`CONFIG_DNS_RESOLVER_LOG_LEVEL_ERR`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_LOG_LEVEL_ERR)、[`CONFIG_DNS_RESOLVER_LOG_LEVEL_WRN`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_LOG_LEVEL_WRN)、[`CONFIG_DNS_RESOLVER_LOG_LEVEL_INF`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_LOG_LEVEL_INF)、[`CONFIG_DNS_RESOLVER_LOG_LEVEL_DBG`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_LOG_LEVEL_DBG)。

<a id="CONFIG_DNS_RESOLVER_LOG_LEVEL_DBG"></a>

## 391.72 `CONFIG_DNS_RESOLVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → DNS 解析器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_RESOLVER_LOG_LEVEL_DEFAULT"></a>

## 391.73 `CONFIG_DNS_RESOLVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → DNS 解析器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_RESOLVER_LOG_LEVEL_ERR"></a>

## 391.74 `CONFIG_DNS_RESOLVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → DNS 解析器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_RESOLVER_LOG_LEVEL_INF"></a>

## 391.75 `CONFIG_DNS_RESOLVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → DNS 解析器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_RESOLVER_LOG_LEVEL_OFF"></a>

## 391.76 `CONFIG_DNS_RESOLVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → DNS 解析器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_RESOLVER_LOG_LEVEL_WRN"></a>

## 391.77 `CONFIG_DNS_RESOLVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → DNS 解析器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE"></a>

## 391.78 `CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE`

**提示（Prompt）**：DNS 回答最大长度（Max length of a DNS answer）

**说明（Help）**

能够处理的返回 DNS 回答的最大长度。RFC 1035 建议为 512 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_RESOLVER_MAX_NAME_LEN"></a>

## 391.79 `CONFIG_DNS_RESOLVER_MAX_NAME_LEN`

**提示（Prompt）**：解析所得 DNS 名称最大长度

**说明（Help）**

用于存储 DNS 服务器返回信息的缓冲区最大长度。例如，查询 DNS 服务发现（DNS-SD）服务时，此值必须足以保存返回的字符串。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
128 if CONFIG_DNS_SD
46 if CONFIG_NET_IPV6
20
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_DNS_SD`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)。

<a id="CONFIG_DNS_RESOLVER_MAX_PRIVATE_DATA_LEN"></a>

## 391.80 `CONFIG_DNS_RESOLVER_MAX_PRIVATE_DATA_LEN`

**提示（Prompt）**：私有资源记录数据最大大小（private RR data）

**说明（Help）**

私有 DNS 资源记录（resource record）数据的最大字节数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
512 if CONFIG_DNS_RESOLVER_PRIVATE_RR_SUPPORT
128
```

**取值范围（Ranges）**

```text
[1, CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE]
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:220`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L220)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_DNS_RESOLVER_PRIVATE_RR_SUPPORT`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_PRIVATE_RR_SUPPORT)、[`CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE)。

<a id="CONFIG_DNS_RESOLVER_MAX_QUERY_LEN"></a>

## 391.81 `CONFIG_DNS_RESOLVER_MAX_QUERY_LEN`

**提示（Prompt）**：DNS 查询最大长度（query length）

**说明（Help）**

待查询 DNS 名称的最大长度，包括末尾的零字符。例如，`example.com` 的查询长度为 `12`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_RESOLVER_MAX_SERVERS"></a>

## 391.82 `CONFIG_DNS_RESOLVER_MAX_SERVERS`

**提示（Prompt）**：DNS 服务器地址数量

**说明（Help）**

可连接的 DNS 服务器数量上限。通常一台 DNS 服务器已足够，每条服务器连接占用一个网络上下文（network context）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_DNS_RESOLVER || CONFIG_MDNS_RESPONDER) && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, CONFIG_DNS_RESOLVER_MAX_SERVERS_LIMIT]
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:515`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L515)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_MDNS_RESPONDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_DNS_RESOLVER_MAX_SERVERS_LIMIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DNS_RESOLVER_MAX_SERVERS_LIMIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_DNS_RESOLVER_MAX_SERVERS_LIMIT`。

<a id="CONFIG_DNS_RESOLVER_MAX_TEXT_LEN"></a>

## 391.83 `CONFIG_DNS_RESOLVER_MAX_TEXT_LEN`

**提示（Prompt）**：记录中解析所得 DNS 文本字符串的最大长度

**说明（Help）**

用于存储 DNS 服务器返回的文本记录字符串（text record string）的缓冲区最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
255 if CONFIG_DNS_SD
64
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_DNS_SD`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD)。

<a id="CONFIG_DNS_RESOLVER_PACKET_FORWARDING"></a>

## 391.84 `CONFIG_DNS_RESOLVER_PACKET_FORWARDING`

**提示（Prompt）**：将接收的 DNS 数据包转发给应用

**说明（Help）**

允许向注册了转发回调（forwarding callback）的应用转发从 DNS 服务器收到的数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_DNS_RESOLVER_CACHE && CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER_CACHE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER_CACHE)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_RESOLVER_PRIVATE_RR_SUPPORT"></a>

## 391.85 `CONFIG_DNS_RESOLVER_PRIVATE_RR_SUPPORT`

**提示（Prompt）**：私有 DNS 资源记录支持（private resource records）

**说明（Help）**

启用私有 DNS 资源记录支持，类型范围为 `65280–65534`。私有资源记录（RR）类型可用于自定义 DNS 记录。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_RESOLVER_QUERY_ALL_AVAILABLE_SERVERS"></a>

## 391.86 `CONFIG_DNS_RESOLVER_QUERY_ALL_AVAILABLE_SERVERS`

**提示（Prompt）**：向所有已配置服务器发送 DNS 查询

**说明（Help）**

启用后，同时向所有可用 DNS 服务器发送查询，采用最先收到的成功响应。配置多个服务器时，这可提高可靠性并缩短响应时间，但增加网络流量。禁用时，每次只查询一个服务器，超时或失败后再尝试下一个。默认避免同时查询全部服务器，以尽量减少网络流量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:228`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L228)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_RESOLVER_RANDOMIZE_SOURCE_PORT"></a>

## 391.87 `CONFIG_DNS_RESOLVER_RANDOMIZE_SOURCE_PORT`

**提示（Prompt）**：每次查询使用新的源端口（source port）

**说明（Help）**

向当前没有未完成请求的服务器发送查询之前，向系统请求新的本地端口，避免连续查询始终从同一个端口发出。这是 RFC 5452 第 9.2 节提出的要求。看不到查询的攻击者必须同时猜中 16 位标识符和源端口才能伪造回答；若端口不变，观察任意一次查询即可得知其中一个条件。

代价是在空闲后的下一次查询前，需要关闭并重新打开套接字（socket），并重新注册其分发器（dispatcher）。若此开销比安全加固收益更重要，可关闭本项。组播 DNS 和链路本地组播名称解析（LLMNR）不受影响，因为这些协议固定端口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:489`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L489)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_SD"></a>

## 391.88 `CONFIG_DNS_SD`

**提示（Prompt）**：DNS服务发现（Service Discovery）。

**说明（Help）**

为 Zephyr 启用 DNS 服务发现（DNS Service Discovery，DNS-SD）。几行代码即可将其用于几乎任何网络服务，同时支持单播和组播 DNS。详情参见 RFC 6763。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING if CONFIG_NET_SOCKETS_OFFLOAD
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:470`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L470)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING)、[`CONFIG_NET_SOCKETS_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD)。

<a id="CONFIG_DNS_SD_LOG_LEVEL_CHOICE"></a>

## 391.89 `CONFIG_DNS_SD_LOG_LEVEL_CHOICE`

**提示（Prompt）**：DNS-SD 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_DNS_SD && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_DNS_SD_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DNS_SD_LOG_LEVEL_OFF
CONFIG_DNS_SD_LOG_LEVEL_ERR
CONFIG_DNS_SD_LOG_LEVEL_WRN
CONFIG_DNS_SD_LOG_LEVEL_INF
CONFIG_DNS_SD_LOG_LEVEL_DBG
CONFIG_DNS_SD_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS服务发现（Service Discovery）。

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_DNS_SD`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_DNS_SD_LOG_LEVEL_DEFAULT`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD_LOG_LEVEL_DEFAULT)、[`CONFIG_DNS_SD_LOG_LEVEL_OFF`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD_LOG_LEVEL_OFF)、[`CONFIG_DNS_SD_LOG_LEVEL_ERR`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD_LOG_LEVEL_ERR)、[`CONFIG_DNS_SD_LOG_LEVEL_WRN`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD_LOG_LEVEL_WRN)、[`CONFIG_DNS_SD_LOG_LEVEL_INF`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD_LOG_LEVEL_INF)、[`CONFIG_DNS_SD_LOG_LEVEL_DBG`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD_LOG_LEVEL_DBG)。

<a id="CONFIG_DNS_SD_LOG_LEVEL_DBG"></a>

## 391.90 `CONFIG_DNS_SD_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_SD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS服务发现（Service Discovery）。 → DNS-SD 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SD_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_SD_LOG_LEVEL_DEFAULT"></a>

## 391.91 `CONFIG_DNS_SD_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_SD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS服务发现（Service Discovery）。 → DNS-SD 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SD_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_SD_LOG_LEVEL_ERR"></a>

## 391.92 `CONFIG_DNS_SD_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_SD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS服务发现（Service Discovery）。 → DNS-SD 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SD_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_SD_LOG_LEVEL_INF"></a>

## 391.93 `CONFIG_DNS_SD_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_SD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS服务发现（Service Discovery）。 → DNS-SD 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SD_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_SD_LOG_LEVEL_OFF"></a>

## 391.94 `CONFIG_DNS_SD_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_SD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS服务发现（Service Discovery）。 → DNS-SD 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SD_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_SD_LOG_LEVEL_WRN"></a>

## 391.95 `CONFIG_DNS_SD_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DNS_SD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → DNS服务发现（Service Discovery）。 → DNS-SD 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SD_LOG_LEVEL_CHOICE`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DNS_SERVER1"></a>

## 391.96 `CONFIG_DNS_SERVER1`

**提示（Prompt）**：DNS 服务器 1

**说明（Help）**

第 1 个 DNS 服务器 IP 地址，可为 IPv4 或 IPv6，并可附加端口号。支持以下语法：

```text
192.0.2.1
192.0.2.1:5353
2001:db8::1
[2001:db8::1]:5353
```

在服务器地址后添加 `%` 和网络接口名称，可将 DNS 连接绑定到特定接口，例如：

```text
192.0.2.1%eth1
```

这会将连接套接字绑定到 `eth1`。此绑定可选，默认按正常 IP 路由选择出接口。也不必使用本 Kconfig 选项：调用 `dns_resolve_init()` 的代码可以自行决定是否用它填充服务器列表。在此设置 DNS 服务器地址后，会自动为用户创建默认 DNS 上下文（context）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_SERVER_IP_ADDRESSES && CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → 设置 DNS 服务器 IP 地址

**配置项引用（Symbol References）**：[`CONFIG_DNS_SERVER_IP_ADDRESSES`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SERVER_IP_ADDRESSES)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_SERVER2"></a>

## 391.97 `CONFIG_DNS_SERVER2`

**提示（Prompt）**：DNS 服务器 2

**说明（Help）**

参见“DNS 服务器 1（DNS server 1）”选项的帮助。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_SERVER_IP_ADDRESSES && CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → 设置 DNS 服务器 IP 地址

**配置项引用（Symbol References）**：[`CONFIG_DNS_SERVER_IP_ADDRESSES`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SERVER_IP_ADDRESSES)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_SERVER3"></a>

## 391.98 `CONFIG_DNS_SERVER3`

**提示（Prompt）**：DNS 服务器 3

**说明（Help）**

参见“DNS 服务器 1（DNS server 1）”选项的帮助。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_SERVER_IP_ADDRESSES && CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → 设置 DNS 服务器 IP 地址

**配置项引用（Symbol References）**：[`CONFIG_DNS_SERVER_IP_ADDRESSES`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SERVER_IP_ADDRESSES)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_SERVER4"></a>

## 391.99 `CONFIG_DNS_SERVER4`

**提示（Prompt）**：DNS 服务器 4

**说明（Help）**

参见“DNS 服务器 1（DNS server 1）”选项的帮助。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_SERVER_IP_ADDRESSES && CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → 设置 DNS 服务器 IP 地址

**配置项引用（Symbol References）**：[`CONFIG_DNS_SERVER_IP_ADDRESSES`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SERVER_IP_ADDRESSES)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_DNS_SERVER5"></a>

## 391.100 `CONFIG_DNS_SERVER5`

**提示（Prompt）**：DNS 服务器 5

**说明（Help）**

参见“DNS 服务器 1（DNS server 1）”选项的帮助。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_SERVER_IP_ADDRESSES && CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → 设置 DNS 服务器 IP 地址

**配置项引用（Symbol References）**：[`CONFIG_DNS_SERVER_IP_ADDRESSES`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SERVER_IP_ADDRESSES)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<!-- kconfig-navigation -->

[上一章](P390_subsys_mpipe_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P392_subsys_net_配置项参考_2.md)
