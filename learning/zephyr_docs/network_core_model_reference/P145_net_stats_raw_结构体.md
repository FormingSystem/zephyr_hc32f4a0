---
id: learning.zephyr-docs.network-core-model-reference.page-145
title: net_stats_raw_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__raw.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第145章\_net\_stats\_raw\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__raw.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

原始数据包套接字（Raw Packet Socket）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

原始数据包套接字（Raw Packet Socket）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 145.1\_数据成员（Data Fields）

<a id="r_ac83a096e59c4483528a67f7209fba257"></a>

```c
struct net_stats_bytes bytes
```

相关声明：[net_stats_bytes](P126_net_stats_bytes_结构体.md)、[bytes](#ac83a096e59c4483528a67f7209fba257)。

接收与发送的原始数据包数据量（Raw packet data）。

<a id="r_aea0d3bd2836853e9f8ed6af489ad42ef"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#aea0d3bd2836853e9f8ed6af489ad42ef)。

已丢弃的原始数据包（Raw packets）数量。

<a id="r_a0decb52f848bf006f52cd575e181ffeb"></a>

```c
net_stats_t recv
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[recv](#a0decb52f848bf006f52cd575e181ffeb)。

已接收的原始数据包（Raw packets）数量。

<a id="r_ab78de1ea1ec2ff46e6f1f248cebd5fac"></a>

```c
net_stats_t sent
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[sent](#ab78de1ea1ec2ff46e6f1f248cebd5fac)。

已发送的原始数据包（Raw packets）数量。

## 145.2\_详细说明（Detailed Documentation）

<a id="ac83a096e59c4483528a67f7209fba257"></a>

### `bytes`

```c
struct net_stats_bytes net_stats_raw::bytes
```

接收与发送的原始数据包数据量（Raw packet data）。

<a id="aea0d3bd2836853e9f8ed6af489ad42ef"></a>

### `drop`

```c
net_stats_t net_stats_raw::drop
```

已丢弃的原始数据包（Raw packets）数量。

<a id="a0decb52f848bf006f52cd575e181ffeb"></a>

### `recv`

```c
net_stats_t net_stats_raw::recv
```

已接收的原始数据包（Raw packets）数量。

<a id="ab78de1ea1ec2ff46e6f1f248cebd5fac"></a>

### `sent`

```c
net_stats_t net_stats_raw::sent
```

已发送的原始数据包（Raw packets）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 145.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_bytes](P126_net_stats_bytes_结构体.md)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P144_net_stats_ppp_结构体.md) · [返回大纲](大纲.md) · [下一章](P146_net_stats_rx_time_结构体.md)
