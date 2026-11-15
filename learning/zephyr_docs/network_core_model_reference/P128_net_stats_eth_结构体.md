---
id: learning.zephyr-docs.network-core-model-reference.page-128
title: net_stats_eth_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__eth.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第128章\_net\_stats\_eth\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__eth.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全部以太网（Ethernet）专用统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

全部以太网（Ethernet）专用统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 128.1\_数据成员（Data Fields）

<a id="r_a8c5cf1ead8ba214425a16fed1c2ad0fb"></a>

```c
struct net_stats_bytes bytes
```

相关声明：[net_stats_bytes](P126_net_stats_bytes_结构体.md)、[bytes](#a8c5cf1ead8ba214425a16fed1c2ad0fb)。

接收与发送的总字节数（Total bytes）。

<a id="r_a97bd6026b16890743f344751a21107f1"></a>

```c
struct net_stats_pkts pkts
```

相关声明：[net_stats_pkts](P142_net_stats_pkts_结构体.md)、[pkts](#a97bd6026b16890743f344751a21107f1)。

接收与发送的数据包总数（Total packets）。

<a id="r_a054beb909134b0e0f22f5df599549128"></a>

```c
struct net_stats_pkts broadcast
```

相关声明：[net_stats_pkts](P142_net_stats_pkts_结构体.md)、[broadcast](#a054beb909134b0e0f22f5df599549128)。

接收与发送的广播数据包总数（Broadcast packets）。

<a id="r_a4f6a2903330518a132e7e547820e0bf2"></a>

```c
struct net_stats_pkts multicast
```

相关声明：[net_stats_pkts](P142_net_stats_pkts_结构体.md)、[multicast](#a4f6a2903330518a132e7e547820e0bf2)。

接收与发送的多播数据包总数（Multicast packets）。

<a id="r_a9c869740f416fbe0b54d7fefacb1fe29"></a>

```c
struct net_stats_pkts errors
```

相关声明：[net_stats_pkts](P142_net_stats_pkts_结构体.md)、[errors](#a9c869740f416fbe0b54d7fefacb1fe29)。

接收与发送（RX/TX）的错误总数。

<a id="r_a922feddb17fc020371f1bcc52c709415"></a>

```c
struct net_stats_eth_errors error_details
```

相关声明：[net_stats_eth_errors](P130_net_stats_eth_errors_结构体.md)、[error_details](#a922feddb17fc020371f1bcc52c709415)。

接收与发送（RX/TX）的错误总数。

<a id="r_a643010ac6360c8c0c08016725ba12222"></a>

```c
struct net_stats_eth_flow flow_control
```

相关声明：[net_stats_eth_flow](P131_net_stats_eth_flow_结构体.md)、[flow_control](#a643010ac6360c8c0c08016725ba12222)。

接收与发送（RX/TX）的流量控制错误（Flow control errors）总数。

<a id="r_a2169ae06bace1a93663bccf88c8d7a29"></a>

```c
struct net_stats_eth_csum csum
```

相关声明：[net_stats_eth_csum](P129_net_stats_eth_csum_结构体.md)、[csum](#a2169ae06bace1a93663bccf88c8d7a29)。

接收与发送（RX/TX）的校验和错误（Checksum errors）总数。

<a id="r_a44667efff73c17c089ed22d5b0da5ad3"></a>

```c
struct net_stats_eth_hw_timestamp hw_timestamp
```

相关声明：[net_stats_eth_hw_timestamp](P132_net_stats_eth_hw_timestamp_结构体.md)、[hw_timestamp](#a44667efff73c17c089ed22d5b0da5ad3)。

接收与发送（RX/TX）的硬件时间戳错误（Hardware timestamp errors）总数。

<a id="r_a822d4205791f59999c842610522f6fc5"></a>

```c
net_stats_t collisions
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[collisions](#a822d4205791f59999c842610522f6fc5)。

碰撞（Collisions）总数。

<a id="r_a257c349cf3d32d38796e3899e702454a"></a>

```c
net_stats_t tx_dropped
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_dropped](#a257c349cf3d32d38796e3899e702454a)。

已丢弃的发送数据包（TX packets）总数。

<a id="r_ab351258ae82abd09759d37774559d8bc"></a>

```c
net_stats_t tx_timeout_count
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_timeout_count](#ab351258ae82abd09759d37774559d8bc)。

发送超时错误（TX timeout errors）总数。

<a id="r_a6699012226e25e8bad39076fed6dbfb5"></a>

```c
net_stats_t tx_restart_queue
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_restart_queue](#a6699012226e25e8bad39076fed6dbfb5)。

发送队列重启（TX queue restarts）总数。

<a id="r_afaacee7cc1d0a35ae2344175421c40dd"></a>

```c
net_stats_t unknown_protocol
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[unknown_protocol](#afaacee7cc1d0a35ae2344175421c40dd)。

接收到的未知协议数据包（RX unknown protocol packets）总数。

## 128.2\_详细说明（Detailed Documentation）

<a id="a054beb909134b0e0f22f5df599549128"></a>

### `broadcast`

```c
struct net_stats_pkts net_stats_eth::broadcast
```

接收与发送的广播数据包总数（Broadcast packets）。

<a id="a8c5cf1ead8ba214425a16fed1c2ad0fb"></a>

### `bytes`

```c
struct net_stats_bytes net_stats_eth::bytes
```

接收与发送的总字节数（Total bytes）。

<a id="a822d4205791f59999c842610522f6fc5"></a>

### `collisions`

```c
net_stats_t net_stats_eth::collisions
```

碰撞（Collisions）总数。

<a id="a2169ae06bace1a93663bccf88c8d7a29"></a>

### `csum`

```c
struct net_stats_eth_csum net_stats_eth::csum
```

接收与发送（RX/TX）的校验和错误（Checksum errors）总数。

<a id="a922feddb17fc020371f1bcc52c709415"></a>

### `error_details`

```c
struct net_stats_eth_errors net_stats_eth::error_details
```

接收与发送（RX/TX）的错误总数。

<a id="a9c869740f416fbe0b54d7fefacb1fe29"></a>

### `errors`

```c
struct net_stats_pkts net_stats_eth::errors
```

接收与发送（RX/TX）的错误总数。

<a id="a643010ac6360c8c0c08016725ba12222"></a>

### `flow_control`

```c
struct net_stats_eth_flow net_stats_eth::flow_control
```

接收与发送（RX/TX）的流量控制错误（Flow control errors）总数。

<a id="a44667efff73c17c089ed22d5b0da5ad3"></a>

### `hw_timestamp`

```c
struct net_stats_eth_hw_timestamp net_stats_eth::hw_timestamp
```

接收与发送（RX/TX）的硬件时间戳错误（Hardware timestamp errors）总数。

<a id="a4f6a2903330518a132e7e547820e0bf2"></a>

### `multicast`

```c
struct net_stats_pkts net_stats_eth::multicast
```

接收与发送的多播数据包总数（Multicast packets）。

<a id="a97bd6026b16890743f344751a21107f1"></a>

### `pkts`

```c
struct net_stats_pkts net_stats_eth::pkts
```

接收与发送的数据包总数（Total packets）。

<a id="a257c349cf3d32d38796e3899e702454a"></a>

### `tx_dropped`

```c
net_stats_t net_stats_eth::tx_dropped
```

已丢弃的发送数据包（TX packets）总数。

<a id="a6699012226e25e8bad39076fed6dbfb5"></a>

### `tx_restart_queue`

```c
net_stats_t net_stats_eth::tx_restart_queue
```

发送队列重启（TX queue restarts）总数。

<a id="ab351258ae82abd09759d37774559d8bc"></a>

### `tx_timeout_count`

```c
net_stats_t net_stats_eth::tx_timeout_count
```

发送超时错误（TX timeout errors）总数。

<a id="afaacee7cc1d0a35ae2344175421c40dd"></a>

### `unknown_protocol`

```c
net_stats_t net_stats_eth::unknown_protocol
```

接收到的未知协议数据包（RX unknown protocol packets）总数。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 128.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_bytes](P126_net_stats_bytes_结构体.md)
- [net_stats_pkts](P142_net_stats_pkts_结构体.md)
- [net_stats_eth_errors](P130_net_stats_eth_errors_结构体.md)
- [net_stats_eth_flow](P131_net_stats_eth_flow_结构体.md)
- [net_stats_eth_csum](P129_net_stats_eth_csum_结构体.md)
- [net_stats_eth_hw_timestamp](P132_net_stats_eth_hw_timestamp_结构体.md)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P127_net_stats_dns_结构体.md) · [返回大纲](大纲.md) · [下一章](P129_net_stats_eth_csum_结构体.md)
