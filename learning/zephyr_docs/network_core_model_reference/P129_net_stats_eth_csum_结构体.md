---
id: learning.zephyr-docs.network-core-model-reference.page-129
title: net_stats_eth_csum_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__eth__csum.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第129章\_net\_stats\_eth\_csum\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__eth__csum.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网校验和（Checksum）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

以太网校验和（Checksum）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 129.1\_数据成员（Data Fields）

<a id="r_a1f1ba5c01c6232cd739d069ddb871b17"></a>

```c
net_stats_t rx_csum_offload_good
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_csum_offload_good](#a1f1ba5c01c6232cd739d069ddb871b17)。

接收校验和卸载（RX checksum offloading）成功次数。

<a id="r_ac4fc04d66193070d4f52a4c07f29ccce"></a>

```c
net_stats_t rx_csum_offload_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_csum_offload_errors](#ac4fc04d66193070d4f52a4c07f29ccce)。

接收校验和卸载（RX checksum offloading）失败次数。

## 129.2\_详细说明（Detailed Documentation）

<a id="ac4fc04d66193070d4f52a4c07f29ccce"></a>

### `rx_csum_offload_errors`

```c
net_stats_t net_stats_eth_csum::rx_csum_offload_errors
```

接收校验和卸载（RX checksum offloading）失败次数。

<a id="a1f1ba5c01c6232cd739d069ddb871b17"></a>

### `rx_csum_offload_good`

```c
net_stats_t net_stats_eth_csum::rx_csum_offload_good
```

接收校验和卸载（RX checksum offloading）成功次数。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 129.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P128_net_stats_eth_结构体.md) · [返回大纲](大纲.md) · [下一章](P130_net_stats_eth_errors_结构体.md)
