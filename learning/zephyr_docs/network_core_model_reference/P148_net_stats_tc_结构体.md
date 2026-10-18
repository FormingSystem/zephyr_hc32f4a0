---
id: learning.zephyr-docs.network-core-model-reference.page-148
title: net_stats_tc_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__tc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第148章\_net\_stats\_tc\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__tc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

流量类别（Traffic Class）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

流量类别（Traffic Class）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 148.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_abeeb2fc618196b21633e0c71803def7c"></a>

```c
uint64_t bytes
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[bytes](#a74b471b77fb1c72933daa656319cc2af)。

此流量类别（Traffic class）已发送的字节数。

<a id="r_a19cf5a6ec41cc60ac91e9332b5ea6a71"></a>

```c
struct net_stats_tx_time tx_time
```

相关声明：[net_stats_tx_time](P150_net_stats_tx_time_结构体.md)、[tx_time](#a30288ef3bb0796cd18c3cf0aedbe875a)。

用于计算平均发送时间统计值（Average TX time statistics）的辅助项。

<a id="r_a8d510f404e9712fbb291636e5d53a358"></a>

```c
net_stats_t pkts
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[pkts](#a6614b5f5186635415a7d787260c39248)。

此流量类别（Traffic class）已发送的数据包数量。

<a id="r_afe5703bba3ecdc6730a10c7f27c49aa2"></a>

```c
net_stats_t dropped
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[dropped](#a1794f71f7fe7b3d20d406be4b28eb032)。

此流量类别（Traffic class）已丢弃的数据包数量。

<a id="r_a6558ffb33ca92af2a98cfb35368a3912"></a>

```c
uint8_t priority
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[priority](#a8a5c2e59990407ddbfc7973a1c183bf6)。

此流量类别（Traffic class）的优先级（Priority）。

<a id="r_a8d6a3ebcc49ce8c34a5faae986f648e2"></a>

```c
} sent [NET_TC_TX_STATS_COUNT]
```

相关声明：[sent](#a8d6a3ebcc49ce8c34a5faae986f648e2)。

各流量类别（Traffic class）的发送统计（TX statistics）。

```c
struct {
```

<a id="r_a8c36ae4ed2322a65298a2c3a93681f57"></a>

```c
uint64_t bytes
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[bytes](#a74b471b77fb1c72933daa656319cc2af)。

此流量类别（Traffic class）已接收的字节数。

<a id="r_a15539cc9bb688cc4a54931d55f34c228"></a>

```c
struct net_stats_rx_time rx_time
```

相关声明：[net_stats_rx_time](P146_net_stats_rx_time_结构体.md)、[rx_time](#a8ea00824bb0fb18e4d8912343e01c3b7)。

用于计算平均接收时间统计值（Average RX time statistics）的辅助项。

<a id="r_a493225eb9946bee29b7ef74f6369e203"></a>

```c
net_stats_t pkts
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[pkts](#a6614b5f5186635415a7d787260c39248)。

此流量类别（Traffic class）已接收的数据包数量。

<a id="r_ac435aad991ee7853eb1b1409cc45a206"></a>

```c
net_stats_t dropped
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[dropped](#a1794f71f7fe7b3d20d406be4b28eb032)。

此流量类别（Traffic class）已丢弃的数据包数量。

<a id="r_a9f5967814a1d5eb343efaf83bd60a62f"></a>

```c
uint8_t priority
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[priority](#a8a5c2e59990407ddbfc7973a1c183bf6)。

此流量类别（Traffic class）的优先级（Priority）。

<a id="r_a2c8826e27ff59154f14a1755ffd4c594"></a>

```c
} recv [NET_TC_RX_STATS_COUNT]
```

相关声明：[recv](#a2c8826e27ff59154f14a1755ffd4c594)。

各流量类别（Traffic class）的接收统计（RX statistics）。

## 148.2\_详细说明（Detailed Documentation）

<a id="a74b471b77fb1c72933daa656319cc2af"></a>

### `bytes`

```c
uint64_t net_stats_tc::bytes
```

此流量类别（Traffic class）已发送的字节数。

此流量类别（Traffic class）已接收的字节数。

<a id="a1794f71f7fe7b3d20d406be4b28eb032"></a>

### `dropped`

```c
net_stats_t net_stats_tc::dropped
```

此流量类别（Traffic class）已丢弃的数据包数量。

<a id="a6614b5f5186635415a7d787260c39248"></a>

### `pkts`

```c
net_stats_t net_stats_tc::pkts
```

此流量类别（Traffic class）已发送的数据包数量。

此流量类别（Traffic class）已接收的数据包数量。

<a id="a8a5c2e59990407ddbfc7973a1c183bf6"></a>

### `priority`

```c
uint8_t net_stats_tc::priority
```

此流量类别（Traffic class）的优先级（Priority）。

<a id="a2c8826e27ff59154f14a1755ffd4c594"></a>

### `[struct]`

```c
struct { ... } net_stats_tc::recv[NET_TC_RX_STATS_COUNT]
```

各流量类别（Traffic class）的接收统计（RX statistics）。

<a id="a8ea00824bb0fb18e4d8912343e01c3b7"></a>

### `rx_time`

```c
struct net_stats_rx_time net_stats_tc::rx_time
```

用于计算平均接收时间统计值（Average RX time statistics）的辅助项。

<a id="a8d6a3ebcc49ce8c34a5faae986f648e2"></a>

### `[struct]`

```c
struct { ... } net_stats_tc::sent[NET_TC_TX_STATS_COUNT]
```

各流量类别（Traffic class）的发送统计（TX statistics）。

<a id="a30288ef3bb0796cd18c3cf0aedbe875a"></a>

### `tx_time`

```c
struct net_stats_tx_time net_stats_tc::tx_time
```

用于计算平均发送时间统计值（Average TX time statistics）的辅助项。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 148.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [net_stats_tx_time](P150_net_stats_tx_time_结构体.md)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_stats_rx_time](P146_net_stats_rx_time_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P147_net_stats_sta_mgmt_结构体.md) · [返回大纲](大纲.md) · [下一章](P149_net_stats_tcp_结构体.md)
