---
id: learning.zephyr-docs.network-core-model-reference.page-131
title: net_stats_eth_flow_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__eth__flow.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第131章\_net\_stats\_eth\_flow\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__eth__flow.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网流量控制（Flow Control）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

以太网流量控制（Flow Control）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 131.1\_数据成员（Data Fields）

<a id="r_a08e5da4ff78fe3893b9c9a628cefe4f2"></a>

```c
net_stats_t rx_flow_control_xon
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_flow_control_xon](#a08e5da4ff78fe3893b9c9a628cefe4f2)。

接收 XON 流量控制（RX XON flow control）次数。

<a id="r_a8f9b93537b3c11be70f276aaa72cb637"></a>

```c
net_stats_t rx_flow_control_xoff
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_flow_control_xoff](#a8f9b93537b3c11be70f276aaa72cb637)。

接收 XOFF 流量控制（RX XOFF flow control）次数。

<a id="r_a31412e8bf9d38ba630ea856e958a48d7"></a>

```c
net_stats_t tx_flow_control_xon
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_flow_control_xon](#a31412e8bf9d38ba630ea856e958a48d7)。

发送 XON 流量控制（TX XON flow control）次数。

<a id="r_a969d81f9db20312d2d2aa7f70f93bdd5"></a>

```c
net_stats_t tx_flow_control_xoff
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_flow_control_xoff](#a969d81f9db20312d2d2aa7f70f93bdd5)。

发送 XOFF 流量控制（TX XOFF flow control）次数。

## 131.2\_详细说明（Detailed Documentation）

<a id="a8f9b93537b3c11be70f276aaa72cb637"></a>

### `rx_flow_control_xoff`

```c
net_stats_t net_stats_eth_flow::rx_flow_control_xoff
```

接收 XOFF 流量控制（RX XOFF flow control）次数。

<a id="a08e5da4ff78fe3893b9c9a628cefe4f2"></a>

### `rx_flow_control_xon`

```c
net_stats_t net_stats_eth_flow::rx_flow_control_xon
```

接收 XON 流量控制（RX XON flow control）次数。

<a id="a969d81f9db20312d2d2aa7f70f93bdd5"></a>

### `tx_flow_control_xoff`

```c
net_stats_t net_stats_eth_flow::tx_flow_control_xoff
```

发送 XOFF 流量控制（TX XOFF flow control）次数。

<a id="a31412e8bf9d38ba630ea856e958a48d7"></a>

### `tx_flow_control_xon`

```c
net_stats_t net_stats_eth_flow::tx_flow_control_xon
```

发送 XON 流量控制（TX XON flow control）次数。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 131.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P130_net_stats_eth_errors_结构体.md) · [返回大纲](大纲.md) · [下一章](P132_net_stats_eth_hw_timestamp_结构体.md)
