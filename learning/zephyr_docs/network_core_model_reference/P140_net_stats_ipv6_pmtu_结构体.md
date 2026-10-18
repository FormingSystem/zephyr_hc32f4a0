---
id: learning.zephyr-docs.network-core-model-reference.page-140
title: net_stats_ipv6_pmtu_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ipv6__pmtu.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第140章\_net\_stats\_ipv6\_pmtu\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ipv6__pmtu.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv6路径MTU发现（Path MTU Discovery）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

IPv6路径MTU发现（Path MTU Discovery）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 140.1\_数据成员（Data Fields）

<a id="r_a68b19ebb61e84eb876178a31c7a4e327"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#a68b19ebb61e84eb876178a31c7a4e327)。

已丢弃的 IPv6 路径最大传输单元数据包（PMTU packets）数量。

<a id="r_a66346cd9140e30727d77648f65345762"></a>

```c
net_stats_t recv
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[recv](#a66346cd9140e30727d77648f65345762)。

已接收的 IPv6 路径最大传输单元数据包（PMTU packets）数量。

<a id="r_a698f5794b73896f7a66def2d3209fafd"></a>

```c
net_stats_t sent
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[sent](#a698f5794b73896f7a66def2d3209fafd)。

已发送的 IPv6 路径最大传输单元数据包（PMTU packets）数量。

## 140.2\_详细说明（Detailed Documentation）

<a id="a68b19ebb61e84eb876178a31c7a4e327"></a>

### `drop`

```c
net_stats_t net_stats_ipv6_pmtu::drop
```

已丢弃的 IPv6 路径最大传输单元数据包（PMTU packets）数量。

<a id="a66346cd9140e30727d77648f65345762"></a>

### `recv`

```c
net_stats_t net_stats_ipv6_pmtu::recv
```

已接收的 IPv6 路径最大传输单元数据包（PMTU packets）数量。

<a id="a698f5794b73896f7a66def2d3209fafd"></a>

### `sent`

```c
net_stats_t net_stats_ipv6_pmtu::sent
```

已发送的 IPv6 路径最大传输单元数据包（PMTU packets）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 140.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P139_net_stats_ipv6_nd_结构体.md) · [返回大纲](大纲.md) · [下一章](P141_net_stats_pkt_filter_结构体.md)
