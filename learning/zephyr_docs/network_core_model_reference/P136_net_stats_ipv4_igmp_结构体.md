---
id: learning.zephyr-docs.network-core-model-reference.page-136
title: net_stats_ipv4_igmp_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ipv4__igmp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第136章\_net\_stats\_ipv4\_igmp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ipv4__igmp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv4 IGMP守护进程（Daemon）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

IPv4 IGMP守护进程（Daemon）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 136.1\_数据成员（Data Fields）

<a id="r_a469113de7af0ba42dbd1b0365d00602c"></a>

```c
net_stats_t recv
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[recv](#a469113de7af0ba42dbd1b0365d00602c)。

已接收的 IPv4 互联网组管理协议查询（IGMP queries）数量。

<a id="r_a955e20a6ee5e19e08000b3114b9d71a6"></a>

```c
net_stats_t sent
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[sent](#a955e20a6ee5e19e08000b3114b9d71a6)。

已发送的 IPv4 互联网组管理协议报告（IGMP reports）数量。

<a id="r_a1c37702ff837b8c5cc9df5f690e7678c"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#a1c37702ff837b8c5cc9df5f690e7678c)。

已丢弃的 IPv4 互联网组管理协议数据包（IGMP packets）数量。

## 136.2\_详细说明（Detailed Documentation）

<a id="a1c37702ff837b8c5cc9df5f690e7678c"></a>

### `drop`

```c
net_stats_t net_stats_ipv4_igmp::drop
```

已丢弃的 IPv4 互联网组管理协议数据包（IGMP packets）数量。

<a id="a469113de7af0ba42dbd1b0365d00602c"></a>

### `recv`

```c
net_stats_t net_stats_ipv4_igmp::recv
```

已接收的 IPv4 互联网组管理协议查询（IGMP queries）数量。

<a id="a955e20a6ee5e19e08000b3114b9d71a6"></a>

### `sent`

```c
net_stats_t net_stats_ipv4_igmp::sent
```

已发送的 IPv4 互联网组管理协议报告（IGMP reports）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 136.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P135_net_stats_ip_errors_结构体.md) · [返回大纲](大纲.md) · [下一章](P137_net_stats_ipv4_pmtu_结构体.md)
