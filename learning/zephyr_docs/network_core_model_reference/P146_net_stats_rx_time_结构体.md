---
id: learning.zephyr-docs.network-core-model-reference.page-146
title: net_stats_rx_time_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__rx__time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第146章\_net\_stats\_rx\_time\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__rx__time.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于计算平均接收时间（RX Time）的网络数据包接收时间。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

用于计算平均接收时间（RX Time）的网络数据包接收时间。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 146.1\_数据成员（Data Fields）

<a id="r_a4b84c2ae2fda8fcd75fdf1bf0b2aae8d"></a>

```c
uint64_t sum
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[sum](#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d)。

网络数据包接收耗时之和（Sum of receive times）。

<a id="r_a68247051b064de081fa2e84118192958"></a>

```c
net_stats_t count
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[count](#a68247051b064de081fa2e84118192958)。

已接收的网络数据包数量（Network packets received）。

## 146.2\_详细说明（Detailed Documentation）

<a id="a68247051b064de081fa2e84118192958"></a>

### `count`

```c
net_stats_t net_stats_rx_time::count
```

已接收的网络数据包数量（Network packets received）。

<a id="a4b84c2ae2fda8fcd75fdf1bf0b2aae8d"></a>

### `sum`

```c
uint64_t net_stats_rx_time::sum
```

网络数据包接收耗时之和（Sum of receive times）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 146.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P145_net_stats_raw_结构体.md) · [返回大纲](大纲.md) · [下一章](P147_net_stats_sta_mgmt_结构体.md)
