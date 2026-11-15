---
id: learning.zephyr-docs.network-core-model-reference.page-113
title: net_packet_mreq_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__packet__mreq.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第113章\_net\_packet\_mreq\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__packet__mreq.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设置数据包套接字（Packet Socket）组播过滤时使用的结构。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

设置数据包套接字（Packet Socket）组播过滤时使用的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 113.1\_数据成员（Data Fields）

<a id="r_a87a230e77612ab9bd25b6d5d6021615c"></a>

```c
int mr_ifindex
```

相关声明：[mr_ifindex](#a87a230e77612ab9bd25b6d5d6021615c)。

网络接口索引（Network interface index）。

<a id="r_a0f775f8c4c00a0f6ffd5f14b82379133"></a>

```c
uint16_t mr_type
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mr_type](#a0f775f8c4c00a0f6ffd5f14b82379133)。

数据包类型（Packet type），即动作（Action）。

<a id="r_a5f4e8579b69cd082baa79ffa3f3ab77f"></a>

```c
uint16_t mr_alen
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mr_alen](#a5f4e8579b69cd082baa79ffa3f3ab77f)。

地址长度（Address Length）

<a id="r_a382435d63e1ffda9197ca3984629e31d"></a>

```c
uint8_t mr_address [NET_LINK_ADDR_MAX_LENGTH]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mr_address](#a382435d63e1ffda9197ca3984629e31d)、[NET_LINK_ADDR_MAX_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga5680cf2ac9302bbee824148f36193b2b)。

物理层地址（Physical layer address）。

## 113.2\_详细说明（Detailed Documentation）

<a id="a382435d63e1ffda9197ca3984629e31d"></a>

### `mr_address`

```c
uint8_t net_packet_mreq::mr_address[NET_LINK_ADDR_MAX_LENGTH]
```

物理层地址（Physical layer address）。

<a id="a5f4e8579b69cd082baa79ffa3f3ab77f"></a>

### `mr_alen`

```c
uint16_t net_packet_mreq::mr_alen
```

地址长度（Address Length）

<a id="a87a230e77612ab9bd25b6d5d6021615c"></a>

### `mr_ifindex`

```c
int net_packet_mreq::mr_ifindex
```

网络接口索引（Network interface index）。

<a id="a0f775f8c4c00a0f6ffd5f14b82379133"></a>

### `mr_type`

```c
uint16_t net_packet_mreq::mr_type
```

数据包类型（Packet type），即动作（Action）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 113.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [NET_LINK_ADDR_MAX_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__net__linkaddr.html#ga5680cf2ac9302bbee824148f36193b2b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P112_net_msghdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P114_net_pkt_结构体.md)
