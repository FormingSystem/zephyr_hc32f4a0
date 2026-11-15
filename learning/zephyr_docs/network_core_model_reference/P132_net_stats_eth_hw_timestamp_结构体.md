---
id: learning.zephyr-docs.network-core-model-reference.page-132
title: net_stats_eth_hw_timestamp_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__eth__hw__timestamp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第132章\_net\_stats\_eth\_hw\_timestamp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__eth__hw__timestamp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网硬件时间戳（Hardware Timestamp）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

以太网硬件时间戳（Hardware Timestamp）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 132.1\_数据成员（Data Fields）

<a id="r_acd3d5f72d7df568110d96093e0c9534d"></a>

```c
net_stats_t rx_hwtstamp_cleared
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_hwtstamp_cleared](#acd3d5f72d7df568110d96093e0c9534d)。

接收硬件时间戳被清除（RX hardware timestamp cleared）的次数。

<a id="r_a41f605499dbf88a879522fdfa4633d9e"></a>

```c
net_stats_t tx_hwtstamp_timeouts
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_hwtstamp_timeouts](#a41f605499dbf88a879522fdfa4633d9e)。

发送硬件时间戳超时（TX hardware timestamp timeout）的次数。

<a id="r_ae1f983faf4a999308c464e4af5a5284b"></a>

```c
net_stats_t tx_hwtstamp_skipped
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_hwtstamp_skipped](#ae1f983faf4a999308c464e4af5a5284b)。

发送硬件时间戳被跳过（TX hardware timestamp skipped）的次数。

## 132.2\_详细说明（Detailed Documentation）

<a id="acd3d5f72d7df568110d96093e0c9534d"></a>

### `rx_hwtstamp_cleared`

```c
net_stats_t net_stats_eth_hw_timestamp::rx_hwtstamp_cleared
```

接收硬件时间戳被清除（RX hardware timestamp cleared）的次数。

<a id="ae1f983faf4a999308c464e4af5a5284b"></a>

### `tx_hwtstamp_skipped`

```c
net_stats_t net_stats_eth_hw_timestamp::tx_hwtstamp_skipped
```

发送硬件时间戳被跳过（TX hardware timestamp skipped）的次数。

<a id="a41f605499dbf88a879522fdfa4633d9e"></a>

### `tx_hwtstamp_timeouts`

```c
net_stats_t net_stats_eth_hw_timestamp::tx_hwtstamp_timeouts
```

发送硬件时间戳超时（TX hardware timestamp timeout）的次数。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 132.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P131_net_stats_eth_flow_结构体.md) · [返回大纲](大纲.md) · [下一章](P133_net_stats_icmp_结构体.md)
