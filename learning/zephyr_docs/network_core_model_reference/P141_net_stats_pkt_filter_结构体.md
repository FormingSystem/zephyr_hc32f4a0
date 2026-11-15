---
id: learning.zephyr-docs.network-core-model-reference.page-141
title: net_stats_pkt_filter_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__pkt__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第141章\_net\_stats\_pkt\_filter\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__pkt__filter.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络数据包过滤器（Network Packet Filter）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

网络数据包过滤器（Network Packet Filter）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 141.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a9ef9becf81f95a66cd675e611ada3d16"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#a62d2d86781e6224b09f21929f27b2ef7)。

在网络接口层级（Network interface level）丢弃的网络数据包。

<a id="r_a8cf9912d574873832b85a614eb776789"></a>

```c
} rx
```

相关声明：[rx](#a8cf9912d574873832b85a614eb776789)。

网络数据包过滤器接收统计（Network packet filter RX statistics）。

```c
struct {
```

<a id="r_a1adf317df2540cb87f85045766e69217"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#a62d2d86781e6224b09f21929f27b2ef7)。

在网络接口层级（Network interface level）丢弃的网络数据包。

<a id="r_a5e88001e143c0adb129ca93b108c277d"></a>

```c
} tx
```

相关声明：[tx](#a5e88001e143c0adb129ca93b108c277d)。

网络数据包过滤器发送统计（Network packet filter TX statistics）。

## 141.2\_详细说明（Detailed Documentation）

<a id="a62d2d86781e6224b09f21929f27b2ef7"></a>

### `drop`

```c
net_stats_t net_stats_pkt_filter::drop
```

在网络接口层级（Network interface level）丢弃的网络数据包。

<a id="a8cf9912d574873832b85a614eb776789"></a>

### `[struct]`

```c
struct { ... } net_stats_pkt_filter::rx
```

网络数据包过滤器接收统计（Network packet filter RX statistics）。

<a id="a5e88001e143c0adb129ca93b108c277d"></a>

### `[struct]`

```c
struct { ... } net_stats_pkt_filter::tx
```

网络数据包过滤器发送统计（Network packet filter TX statistics）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 141.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P140_net_stats_ipv6_pmtu_结构体.md) · [返回大纲](大纲.md) · [下一章](P142_net_stats_pkts_结构体.md)
