---
id: learning.zephyr-docs.network-core-model-reference.page-138
title: net_stats_ipv6_mld_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ipv6__mld.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第138章\_net\_stats\_ipv6\_mld\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ipv6__mld.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv6组播监听守护进程（Multicast Listener Daemon）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

IPv6组播监听守护进程（Multicast Listener Daemon）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 138.1\_数据成员（Data Fields）

<a id="r_a4879ff9e31f8b60973d3b169598e921d"></a>

```c
net_stats_t recv
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[recv](#a4879ff9e31f8b60973d3b169598e921d)。

已接收的 IPv6 多播监听器发现查询（MLD queries）数量。

<a id="r_ab397b74b14ce7047bf2fc63ca72ce1e5"></a>

```c
net_stats_t sent
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[sent](#ab397b74b14ce7047bf2fc63ca72ce1e5)。

已发送的 IPv6 多播监听器发现报告（MLD reports）数量。

<a id="r_ad85dc87f57296a1e7d64e959b0370ee8"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#ad85dc87f57296a1e7d64e959b0370ee8)。

已丢弃的 IPv6 多播监听器发现数据包（MLD packets）数量。

## 138.2\_详细说明（Detailed Documentation）

<a id="ad85dc87f57296a1e7d64e959b0370ee8"></a>

### `drop`

```c
net_stats_t net_stats_ipv6_mld::drop
```

已丢弃的 IPv6 多播监听器发现数据包（MLD packets）数量。

<a id="a4879ff9e31f8b60973d3b169598e921d"></a>

### `recv`

```c
net_stats_t net_stats_ipv6_mld::recv
```

已接收的 IPv6 多播监听器发现查询（MLD queries）数量。

<a id="ab397b74b14ce7047bf2fc63ca72ce1e5"></a>

### `sent`

```c
net_stats_t net_stats_ipv6_mld::sent
```

已发送的 IPv6 多播监听器发现报告（MLD reports）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 138.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P137_net_stats_ipv4_pmtu_结构体.md) · [返回大纲](大纲.md) · [下一章](P139_net_stats_ipv6_nd_结构体.md)
