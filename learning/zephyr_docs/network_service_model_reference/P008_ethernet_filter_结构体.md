---
id: learning.zephyr-docs.network-service-model-reference.page-8
title: ethernet_filter_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structethernet__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_ethernet\_filter\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__filter.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网过滤器（Ethernet Filter）的描述。

```c
#include <zephyr/net/ethernet.h>
```

<a id="details"></a>

以太网过滤器（Ethernet filter）描述。以太网二层（L2）会跟踪上层加入的组播地址，因此只有第一个使用者加入某个组时，才通知驱动设置该地址；只有最后一个使用者离开时，才通知驱动取消该地址。驱动无需自行统计某个地址被注册了多少次。驱动也可以把请求视为组播地址集合发生变化的提示，通过 `net_eth_mcast_addr_foreach()` 遍历所有地址，从头重新配置接收过滤器。对于根据地址哈希进行过滤的设备，推荐此方式，因为仅凭单个地址无法判断是否还有其他地址需要同一个哈希桶。传给 `NET_REQUEST_ETHERNET_SET_MAC_FILTER` 的组播目的地址也使用相同的计数管理，因此同样具有上述保证。源地址和单播目的地址不被跟踪，而是原样传给驱动。每个接口可跟踪的组播地址数量有限；容量耗尽后，加入组会以 `-ENOMEM` 失败；取消一个从未设置过的组播地址会以 `-ENOENT` 失败。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_aec00b1ecd6af658a5164d375bccdaa10"></a>

```c
enum ethernet_filter_type type
```

相关声明：[type](#aec00b1ecd6af658a5164d375bccdaa10)。

过滤器类型。

<a id="r_aaacda9b89d6b21934654e0f2b19624e0"></a>

```c
struct net_eth_addr mac_address
```

相关声明：[net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)、[mac_address](#aaacda9b89d6b21934654e0f2b19624e0)。

要过滤的 MAC 地址。

<a id="r_ad83053c859c65e0c0432fe3f59671335"></a>

```c
bool set
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[set](#ad83053c859c65e0c0432fe3f59671335)。

设置（`true`）或取消（`false`）过滤器。

## 8.2\_详细说明（Detailed Documentation）

<a id="aaacda9b89d6b21934654e0f2b19624e0"></a>

### `mac_address`

```c
struct net_eth_addr ethernet_filter::mac_address
```

要过滤的 MAC 地址。

<a id="ad83053c859c65e0c0432fe3f59671335"></a>

### `set`

```c
bool ethernet_filter::set
```

设置（`true`）或取消（`false`）过滤器。

<a id="aec00b1ecd6af658a5164d375bccdaa10"></a>

### `type`

```c
enum ethernet_filter_type ethernet_filter::type
```

过滤器类型。

本数据类型文档由以下文件生成：

- `zephyr/net/ethernet.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [net_eth_addr](../network_core_model_reference/P059_net_eth_addr_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [net_eth_mcast_addr_foreach()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga80adc03695a8fbb9dbc9dd3adec78c04)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_ethernet_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_ethernet_lldp_结构体.md)
