---
id: learning.zephyr-docs.network-core-model-reference.page-142
title: net_stats_pkts_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__pkts.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第142章\_net\_stats\_pkts\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__pkts.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

发送与接收的网络数据包数量（Network Packets Sent and Received）。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

发送与接收的网络数据包数量（Network Packets Sent and Received）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 142.1\_数据成员（Data Fields）

<a id="r_aee1e302d0f8dac79b693a06d8fa3b3c5"></a>

```c
net_stats_t tx
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx](#aee1e302d0f8dac79b693a06d8fa3b3c5)。

已发送的数据包数量（Packets sent）。

<a id="r_ac9784b5a245e6c57e39318aaf314f0cf"></a>

```c
net_stats_t rx
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx](#ac9784b5a245e6c57e39318aaf314f0cf)。

已接收的数据包数量（Packets received）。

## 142.2\_详细说明（Detailed Documentation）

<a id="ac9784b5a245e6c57e39318aaf314f0cf"></a>

### `rx`

```c
net_stats_t net_stats_pkts::rx
```

已接收的数据包数量（Packets received）。

<a id="aee1e302d0f8dac79b693a06d8fa3b3c5"></a>

### `tx`

```c
net_stats_t net_stats_pkts::tx
```

已发送的数据包数量（Packets sent）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 142.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P141_net_stats_pkt_filter_结构体.md) · [返回大纲](大纲.md) · [下一章](P143_net_stats_pm_结构体.md)
