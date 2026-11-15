---
id: learning.zephyr-docs.network-core-model-reference.page-139
title: net_stats_ipv6_nd_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ipv6__nd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第139章\_net\_stats\_ipv6\_nd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ipv6__nd.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv6邻居发现（Neighbor Discovery）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

IPv6邻居发现（Neighbor Discovery）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 139.1\_数据成员（Data Fields）

<a id="r_a31074d5d44138fcabdc5f7750f9f2c47"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#a31074d5d44138fcabdc5f7750f9f2c47)。

已丢弃的 IPv6 邻居发现数据包（Neighbor discovery packets）数量。

<a id="r_a0bf6f67d9112996a3b002ea160aec769"></a>

```c
net_stats_t recv
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[recv](#a0bf6f67d9112996a3b002ea160aec769)。

已接收的 IPv6 邻居发现数据包（Neighbor discovery packets）数量。

<a id="r_a0129f7892a4439c20deb2f32b9001277"></a>

```c
net_stats_t sent
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[sent](#a0129f7892a4439c20deb2f32b9001277)。

已发送的 IPv6 邻居发现数据包（Neighbor discovery packets）数量。

## 139.2\_详细说明（Detailed Documentation）

<a id="a31074d5d44138fcabdc5f7750f9f2c47"></a>

### `drop`

```c
net_stats_t net_stats_ipv6_nd::drop
```

已丢弃的 IPv6 邻居发现数据包（Neighbor discovery packets）数量。

<a id="a0bf6f67d9112996a3b002ea160aec769"></a>

### `recv`

```c
net_stats_t net_stats_ipv6_nd::recv
```

已接收的 IPv6 邻居发现数据包（Neighbor discovery packets）数量。

<a id="a0129f7892a4439c20deb2f32b9001277"></a>

### `sent`

```c
net_stats_t net_stats_ipv6_nd::sent
```

已发送的 IPv6 邻居发现数据包（Neighbor discovery packets）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 139.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P138_net_stats_ipv6_mld_结构体.md) · [返回大纲](大纲.md) · [下一章](P140_net_stats_ipv6_pmtu_结构体.md)
