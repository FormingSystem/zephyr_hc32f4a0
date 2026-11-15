---
id: learning.zephyr-docs.network-core-model-reference.page-108
title: net_lldp_time_to_live_tlv_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__lldp__time__to__live__tlv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第108章\_net\_lldp\_time\_to\_live\_tlv\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__lldp__time__to__live__tlv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

生存时间类型-长度-值（Time To Live TLV），见IEEE 802.1AB第8.5.4节。

```c
#include <zephyr/net/lldp.h>
```

<a id="details"></a>

生存时间类型-长度-值（Time To Live TLV），见IEEE 802.1AB第8.5.4节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 108.1\_数据成员（Data Fields）

<a id="r_a78b88d66184a0d25c413baf2fec495ab"></a>

```c
uint16_t type_length
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[type_length](#a78b88d66184a0d25c413baf2fec495ab)。

类型（Type）占 7 位，长度（Length）占 9 位。

<a id="r_ab967792a938a5d67f744e53be8d5f0fd"></a>

```c
uint16_t ttl
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ttl](#ab967792a938a5d67f744e53be8d5f0fd)。

生存时间值（Time To Live，TTL）。

## 108.2\_详细说明（Detailed Documentation）

<a id="ab967792a938a5d67f744e53be8d5f0fd"></a>

### `ttl`

```c
uint16_t net_lldp_time_to_live_tlv::ttl
```

生存时间值（Time To Live，TTL）。

<a id="a78b88d66184a0d25c413baf2fec495ab"></a>

### `type_length`

```c
uint16_t net_lldp_time_to_live_tlv::type_length
```

类型（Type）占 7 位，长度（Length）占 9 位。

本数据类型文档由以下文件生成：

- `zephyr/net/lldp.h`

## 108.3\_原页交叉引用（Cross References）

- [zephyr/net/lldp.h](https://docs.zephyrproject.org/latest/doxygen/html/lldp_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P107_net_lldp_port_tlv_结构体.md) · [返回大纲](大纲.md) · [下一章](P109_net_lldpdu_结构体.md)
