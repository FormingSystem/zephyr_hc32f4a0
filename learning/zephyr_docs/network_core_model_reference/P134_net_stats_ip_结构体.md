---
id: learning.zephyr-docs.network-core-model-reference.page-134
title: net_stats_ip_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ip.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第134章\_net\_stats\_ip\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__ip.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IP层（IP Layer）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

IP层（IP Layer）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 134.1\_数据成员（Data Fields）

<a id="r_ab6a6373368dd24cb51504c5729d535d3"></a>

```c
net_stats_t recv
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[recv](#ab6a6373368dd24cb51504c5729d535d3)。

IP 层接收的数据包数量（Received packets）。

<a id="r_abbe676bbe9faa89b2b6b8c4950b1c9d5"></a>

```c
net_stats_t sent
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[sent](#abbe676bbe9faa89b2b6b8c4950b1c9d5)。

IP 层发送的数据包数量（Sent packets）。

<a id="r_a4bb82a5ebebaa3e8a11973c07eed96a0"></a>

```c
net_stats_t forwarded
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[forwarded](#a4bb82a5ebebaa3e8a11973c07eed96a0)。

IP 层转发的数据包数量（Forwarded packets）。

<a id="r_ac86399b70d7f761162e5336dd15589eb"></a>

```c
net_stats_t drop
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[drop](#ac86399b70d7f761162e5336dd15589eb)。

IP 层丢弃的数据包数量（Dropped packets）。

## 134.2\_详细说明（Detailed Documentation）

<a id="ac86399b70d7f761162e5336dd15589eb"></a>

### `drop`

```c
net_stats_t net_stats_ip::drop
```

IP 层丢弃的数据包数量（Dropped packets）。

<a id="a4bb82a5ebebaa3e8a11973c07eed96a0"></a>

### `forwarded`

```c
net_stats_t net_stats_ip::forwarded
```

IP 层转发的数据包数量（Forwarded packets）。

<a id="ab6a6373368dd24cb51504c5729d535d3"></a>

### `recv`

```c
net_stats_t net_stats_ip::recv
```

IP 层接收的数据包数量（Received packets）。

<a id="abbe676bbe9faa89b2b6b8c4950b1c9d5"></a>

### `sent`

```c
net_stats_t net_stats_ip::sent
```

IP 层发送的数据包数量（Sent packets）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 134.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P133_net_stats_icmp_结构体.md) · [返回大纲](大纲.md) · [下一章](P135_net_stats_ip_errors_结构体.md)
