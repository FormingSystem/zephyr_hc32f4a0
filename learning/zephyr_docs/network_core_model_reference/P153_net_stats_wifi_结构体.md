---
id: learning.zephyr-docs.network-core-model-reference.page-153
title: net_stats_wifi_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__wifi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第153章\_net\_stats\_wifi\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__wifi.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全部Wi-Fi专用统计信息（Statistics）。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

全部Wi-Fi专用统计信息（Statistics）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 153.1\_数据成员（Data Fields）

<a id="r_a8bee22961545674e6ab100b58a04bf91"></a>

```c
struct net_stats_sta_mgmt sta_mgmt
```

相关声明：[net_stats_sta_mgmt](P147_net_stats_sta_mgmt_结构体.md)、[sta_mgmt](#a8bee22961545674e6ab100b58a04bf91)。

信标错误（Beacon errors）总数。

<a id="r_aa055b1e8bd8f1e50815c1028b562be07"></a>

```c
struct net_stats_bytes bytes
```

相关声明：[net_stats_bytes](P126_net_stats_bytes_结构体.md)、[bytes](#aa055b1e8bd8f1e50815c1028b562be07)。

接收与发送的总字节数（Total bytes）。

<a id="r_adbcdb2dd8733f2917c00a0b2d365393b"></a>

```c
struct net_stats_pkts pkts
```

相关声明：[net_stats_pkts](P142_net_stats_pkts_结构体.md)、[pkts](#adbcdb2dd8733f2917c00a0b2d365393b)。

接收与发送的数据包总数（Total packets）。

<a id="r_a03dc04638c4b670bd7f3520d45fc1eda"></a>

```c
struct net_stats_pkts broadcast
```

相关声明：[net_stats_pkts](P142_net_stats_pkts_结构体.md)、[broadcast](#a03dc04638c4b670bd7f3520d45fc1eda)。

接收与发送的广播数据包总数（Broadcast packets）。

<a id="r_a7e7f68215101885fd51c70e981da26e7"></a>

```c
struct net_stats_pkts multicast
```

相关声明：[net_stats_pkts](P142_net_stats_pkts_结构体.md)、[multicast](#a7e7f68215101885fd51c70e981da26e7)。

接收与发送的多播数据包总数（Multicast packets）。

<a id="r_ae0149e64a94a9f96eb6680f94793c8c4"></a>

```c
struct net_stats_pkts errors
```

相关声明：[net_stats_pkts](P142_net_stats_pkts_结构体.md)、[errors](#ae0149e64a94a9f96eb6680f94793c8c4)。

接收与发送（RX/TX）的错误总数。

<a id="r_ae80dcd73a3c5ce3ec3282d1ae827b338"></a>

```c
struct net_stats_pkts unicast
```

相关声明：[net_stats_pkts](P142_net_stats_pkts_结构体.md)、[unicast](#ae80dcd73a3c5ce3ec3282d1ae827b338)。

接收与发送的单播数据包总数（Unicast packets）。

<a id="r_ac498c9e517f2cb2eb01d251e84159e7e"></a>

```c
net_stats_t overrun_count
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[overrun_count](#ac498c9e517f2cb2eb01d251e84159e7e)。

接收与发送过程中丢弃的数据包总数（Dropped packets）。

## 153.2\_详细说明（Detailed Documentation）

<a id="a03dc04638c4b670bd7f3520d45fc1eda"></a>

### `broadcast`

```c
struct net_stats_pkts net_stats_wifi::broadcast
```

接收与发送的广播数据包总数（Broadcast packets）。

<a id="aa055b1e8bd8f1e50815c1028b562be07"></a>

### `bytes`

```c
struct net_stats_bytes net_stats_wifi::bytes
```

接收与发送的总字节数（Total bytes）。

<a id="ae0149e64a94a9f96eb6680f94793c8c4"></a>

### `errors`

```c
struct net_stats_pkts net_stats_wifi::errors
```

接收与发送（RX/TX）的错误总数。

<a id="a7e7f68215101885fd51c70e981da26e7"></a>

### `multicast`

```c
struct net_stats_pkts net_stats_wifi::multicast
```

接收与发送的多播数据包总数（Multicast packets）。

<a id="ac498c9e517f2cb2eb01d251e84159e7e"></a>

### `overrun_count`

```c
net_stats_t net_stats_wifi::overrun_count
```

接收与发送过程中丢弃的数据包总数（Dropped packets）。

<a id="adbcdb2dd8733f2917c00a0b2d365393b"></a>

### `pkts`

```c
struct net_stats_pkts net_stats_wifi::pkts
```

接收与发送的数据包总数（Total packets）。

<a id="a8bee22961545674e6ab100b58a04bf91"></a>

### `sta_mgmt`

```c
struct net_stats_sta_mgmt net_stats_wifi::sta_mgmt
```

信标错误（Beacon errors）总数。

<a id="ae80dcd73a3c5ce3ec3282d1ae827b338"></a>

### `unicast`

```c
struct net_stats_pkts net_stats_wifi::unicast
```

接收与发送的单播数据包总数（Unicast packets）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 153.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_sta_mgmt](P147_net_stats_sta_mgmt_结构体.md)
- [net_stats_bytes](P126_net_stats_bytes_结构体.md)
- [net_stats_pkts](P142_net_stats_pkts_结构体.md)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P152_net_stats_vpn_结构体.md) · [返回大纲](大纲.md) · [下一章](P154_net_traffic_class_结构体.md)
