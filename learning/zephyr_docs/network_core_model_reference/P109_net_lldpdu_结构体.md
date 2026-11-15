---
id: learning.zephyr-docs.network-core-model-reference.page-109
title: net_lldpdu_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__lldpdu.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第109章\_net\_lldpdu\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__lldpdu.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

按IEEE 802.1AB第8.2节“LLDPDU格式”的规定，链路层发现协议数据单元（LLDPDU）应按以下顺序包含类型-长度-值（TLV）项。

```c
#include <zephyr/net/lldp.h>
```

<a id="details"></a>

按IEEE 802.1AB第8.2节“LLDPDU格式”的规定，链路层发现协议数据单元（LLDPDU）应按以下顺序包含类型-长度-值（TLV）项。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 109.1\_数据成员（Data Fields）

<a id="r_a1a1c80fe7462ddbfd84289735013834c"></a>

```c
struct net_lldp_chassis_tlv chassis_id
```

相关声明：[net_lldp_chassis_tlv](P106_net_lldp_chassis_tlv_结构体.md)、[chassis_id](#a1a1c80fe7462ddbfd84289735013834c)。

必需的机箱类型长度值项（Mandatory Chassis TLV）。

<a id="r_aa55adafc5528576017c37a28413bdaf9"></a>

```c
struct net_lldp_port_tlv port_id
```

相关声明：[net_lldp_port_tlv](P107_net_lldp_port_tlv_结构体.md)、[port_id](#aa55adafc5528576017c37a28413bdaf9)。

必需的端口类型长度值项（Mandatory Port TLV）。

<a id="r_afbe0618b6d849b8ee7b225844ac399df"></a>

```c
struct net_lldp_time_to_live_tlv ttl
```

相关声明：[net_lldp_time_to_live_tlv](P108_net_lldp_time_to_live_tlv_结构体.md)、[ttl](#afbe0618b6d849b8ee7b225844ac399df)。

必需的生存时间类型长度值项（Mandatory TTL TLV）。

## 109.2\_详细说明（Detailed Documentation）

<a id="a1a1c80fe7462ddbfd84289735013834c"></a>

### `chassis_id`

```c
struct net_lldp_chassis_tlv net_lldpdu::chassis_id
```

必需的机箱类型长度值项（Mandatory Chassis TLV）。

<a id="aa55adafc5528576017c37a28413bdaf9"></a>

### `port_id`

```c
struct net_lldp_port_tlv net_lldpdu::port_id
```

必需的端口类型长度值项（Mandatory Port TLV）。

<a id="afbe0618b6d849b8ee7b225844ac399df"></a>

### `ttl`

```c
struct net_lldp_time_to_live_tlv net_lldpdu::ttl
```

必需的生存时间类型长度值项（Mandatory TTL TLV）。

本数据类型文档由以下文件生成：

- `zephyr/net/lldp.h`

## 109.3\_原页交叉引用（Cross References）

- [zephyr/net/lldp.h](https://docs.zephyrproject.org/latest/doxygen/html/lldp_8h_source.html)
- [net_lldp_chassis_tlv](P106_net_lldp_chassis_tlv_结构体.md)
- [net_lldp_port_tlv](P107_net_lldp_port_tlv_结构体.md)
- [net_lldp_time_to_live_tlv](P108_net_lldp_time_to_live_tlv_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P108_net_lldp_time_to_live_tlv_结构体.md) · [返回大纲](大纲.md) · [下一章](P110_net_mgmt_event_callback_结构体.md)
