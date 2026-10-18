---
id: learning.zephyr-docs.network-core-model-reference.page-137
title: net_stats_ipv4_pmtu_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ipv4__pmtu.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第137章\_net\_stats\_ipv4\_pmtu\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ipv4__pmtu.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv4路径MTU发现（Path MTU Discovery）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

IPv4路径MTU发现（Path MTU Discovery）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 137.1\_数据成员（Data Fields）

<a id="r_ad35f9defad7c5ce29e510b8051788977"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#ad35f9defad7c5ce29e510b8051788977)。

已丢弃的 IPv4 路径最大传输单元数据包（PMTU packets）数量。

<a id="r_a64245eb7b9b1fcfa0f0efcb53eff7ec2"></a>

```c
net_stats_t recv
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[recv](#a64245eb7b9b1fcfa0f0efcb53eff7ec2)。

已接收的 IPv4 路径最大传输单元数据包（PMTU packets）数量。

<a id="r_a44f1028694d4001cd4a43f925f0bf0da"></a>

```c
net_stats_t sent
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[sent](#a44f1028694d4001cd4a43f925f0bf0da)。

已发送的 IPv4 路径最大传输单元数据包（PMTU packets）数量。

## 137.2\_详细说明（Detailed Documentation）

<a id="ad35f9defad7c5ce29e510b8051788977"></a>

### `drop`

```c
net_stats_t net_stats_ipv4_pmtu::drop
```

已丢弃的 IPv4 路径最大传输单元数据包（PMTU packets）数量。

<a id="a64245eb7b9b1fcfa0f0efcb53eff7ec2"></a>

### `recv`

```c
net_stats_t net_stats_ipv4_pmtu::recv
```

已接收的 IPv4 路径最大传输单元数据包（PMTU packets）数量。

<a id="a44f1028694d4001cd4a43f925f0bf0da"></a>

### `sent`

```c
net_stats_t net_stats_ipv4_pmtu::sent
```

已发送的 IPv4 路径最大传输单元数据包（PMTU packets）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 137.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P136_net_stats_ipv4_igmp_结构体.md) · [返回大纲](大纲.md) · [下一章](P138_net_stats_ipv6_mld_结构体.md)
