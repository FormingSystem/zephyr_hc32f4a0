---
id: learning.zephyr-docs.network-core-model-reference.page-147
title: net_stats_sta_mgmt_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__sta__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第147章\_net\_stats\_sta\_mgmt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__sta__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全部Wi-Fi管理（Management）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

全部Wi-Fi管理（Management）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 147.1\_数据成员（Data Fields）

<a id="r_ac6e68fded8e19b20259442436923f815"></a>

```c
net_stats_t beacons_rx
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[beacons_rx](#ac6e68fded8e19b20259442436923f815)。

已接收的信标（Beacons）数量。

<a id="r_a29ae0079b4c780e0de2656a85ec15fe9"></a>

```c
net_stats_t beacons_miss
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[beacons_miss](#a29ae0079b4c780e0de2656a85ec15fe9)。

遗漏的信标（Missed beacons）数量。

## 147.2\_详细说明（Detailed Documentation）

<a id="a29ae0079b4c780e0de2656a85ec15fe9"></a>

### `beacons_miss`

```c
net_stats_t net_stats_sta_mgmt::beacons_miss
```

遗漏的信标（Missed beacons）数量。

<a id="ac6e68fded8e19b20259442436923f815"></a>

### `beacons_rx`

```c
net_stats_t net_stats_sta_mgmt::beacons_rx
```

已接收的信标（Beacons）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 147.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P146_net_stats_rx_time_结构体.md) · [返回大纲](大纲.md) · [下一章](P148_net_stats_tc_结构体.md)
