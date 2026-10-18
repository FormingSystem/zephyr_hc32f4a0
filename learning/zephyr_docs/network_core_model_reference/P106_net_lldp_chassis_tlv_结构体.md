---
id: learning.zephyr-docs.network-core-model-reference.page-106
title: net_lldp_chassis_tlv_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__lldp__chassis__tlv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第106章\_net\_lldp\_chassis\_tlv\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__lldp__chassis__tlv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

机箱ID类型-长度-值（Chassis ID TLV），见IEEE 802.1AB第8.5.2节。

```c
#include <zephyr/net/lldp.h>
```

<a id="details"></a>

机箱ID类型-长度-值（Chassis ID TLV），见IEEE 802.1AB第8.5.2节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 106.1\_数据成员（Data Fields）

<a id="r_af81d3102ad0ec1f7ef76bb1533dcc7cd"></a>

```c
uint16_t type_length
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[type_length](#af81d3102ad0ec1f7ef76bb1533dcc7cd)。

类型（Type）占 7 位，长度（Length）占 9 位。

<a id="r_ad9d415f6a1e9018953728de1b529fd98"></a>

```c
uint8_t subtype
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subtype](#ad9d415f6a1e9018953728de1b529fd98)。

标识符子类型（ID subtype）。

<a id="r_a37b7e81a670595d1c6c77a45bf9cfc73"></a>

```c
uint8_t value [NET_LLDP_CHASSIS_ID_VALUE_LEN]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[value](#a37b7e81a670595d1c6c77a45bf9cfc73)。

机箱标识符值（Chassis ID value）。

## 106.2\_详细说明（Detailed Documentation）

<a id="ad9d415f6a1e9018953728de1b529fd98"></a>

### `subtype`

```c
uint8_t net_lldp_chassis_tlv::subtype
```

标识符子类型（ID subtype）。

<a id="af81d3102ad0ec1f7ef76bb1533dcc7cd"></a>

### `type_length`

```c
uint16_t net_lldp_chassis_tlv::type_length
```

类型（Type）占 7 位，长度（Length）占 9 位。

<a id="a37b7e81a670595d1c6c77a45bf9cfc73"></a>

### `value`

```c
uint8_t net_lldp_chassis_tlv::value[NET_LLDP_CHASSIS_ID_VALUE_LEN]
```

机箱标识符值（Chassis ID value）。

本数据类型文档由以下文件生成：

- `zephyr/net/lldp.h`

## 106.3\_原页交叉引用（Cross References）

- [zephyr/net/lldp.h](https://docs.zephyrproject.org/latest/doxygen/html/lldp_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P105_net_linkaddr_结构体.md) · [返回大纲](大纲.md) · [下一章](P107_net_lldp_port_tlv_结构体.md)
