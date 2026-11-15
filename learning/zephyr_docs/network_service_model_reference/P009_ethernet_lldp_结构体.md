---
id: learning.zephyr-docs.network-service-model-reference.page-9
title: ethernet_lldp_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structethernet__lldp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_ethernet\_lldp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__lldp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网链路层发现协议（LLDP）的专用参数。

```c
#include <zephyr/net/ethernet.h>
```

<a id="details"></a>

以太网链路层发现协议（LLDP）的专用参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_a8cf37774b067ffbc4876e42c3b28e536"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a8cf37774b067ffbc4876e42c3b28e536)。

用于跟踪定时器。

<a id="r_aede4281b7f53be43f524d47bb2c606d1"></a>

```c
const struct net_lldpdu * lldpdu
```

相关声明：[net_lldpdu](../network_core_model_reference/P109_net_lldpdu_结构体.md)、[lldpdu](#aede4281b7f53be43f524d47bb2c606d1)。

此接口的链路层发现协议数据单元（LLDP Data Unit）的必需 TLV。

<a id="r_a732d685dd27d2be5cb6b51175b8af70f"></a>

```c
const uint8_t * optional_du
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[optional_du](#a732d685dd27d2be5cb6b51175b8af70f)。

此接口的 LLDP 数据单元的可选 TLV。

<a id="r_aabc1141bbc72a17e3884138c61bd5b0c"></a>

```c
size_t optional_len
```

相关声明：[optional_len](#aabc1141bbc72a17e3884138c61bd5b0c)。

可选数据单元 TLV 的长度。

<a id="r_a9a1123c7f9e799b6fe815c554df6f023"></a>

```c
k_timepoint_t tx_timer_timeout
```

相关声明：[k_timepoint_t](../timer_reference/P088_内核时间点类型.md)、[tx_timer_timeout](#a9a1123c7f9e799b6fe815c554df6f023)。

LLDP 发送（TX）定时器超时时间。

<a id="r_a8d2452f182c52000bec93f4c53501220"></a>

```c
net_lldp_recv_cb_t cb
```

相关声明：[net_lldp_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga1e9fb662d7cdfc3c4c68cfd0312987cf)、[cb](#a8d2452f182c52000bec93f4c53501220)。

LLDP 接收（RX）回调函数。

## 9.2\_详细说明（Detailed Documentation）

<a id="a8d2452f182c52000bec93f4c53501220"></a>

### `cb`

```c
net_lldp_recv_cb_t ethernet_lldp::cb
```

LLDP 接收（RX）回调函数。

<a id="aede4281b7f53be43f524d47bb2c606d1"></a>

### `lldpdu`

```c
const struct net_lldpdu* ethernet_lldp::lldpdu
```

此接口的链路层发现协议数据单元（LLDP Data Unit）的必需 TLV。

<a id="a8cf37774b067ffbc4876e42c3b28e536"></a>

### `node`

```c
sys_snode_t ethernet_lldp::node
```

用于跟踪定时器。

<a id="a732d685dd27d2be5cb6b51175b8af70f"></a>

### `optional_du`

```c
const uint8_t* ethernet_lldp::optional_du
```

此接口的 LLDP 数据单元的可选 TLV。

<a id="aabc1141bbc72a17e3884138c61bd5b0c"></a>

### `optional_len`

```c
size_t ethernet_lldp::optional_len
```

可选数据单元 TLV 的长度。

<a id="a9a1123c7f9e799b6fe815c554df6f023"></a>

### `tx_timer_timeout`

```c
k_timepoint_t ethernet_lldp::tx_timer_timeout
```

LLDP 发送（TX）定时器超时时间。

本数据类型文档由以下文件生成：

- `zephyr/net/ethernet.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [net_lldpdu](../network_core_model_reference/P109_net_lldpdu_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [k_timepoint_t](../timer_reference/P088_内核时间点类型.md)
- [net_lldp_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga1e9fb662d7cdfc3c4c68cfd0312987cf)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_ethernet_filter_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_ethernet_qav_param_结构体.md)
