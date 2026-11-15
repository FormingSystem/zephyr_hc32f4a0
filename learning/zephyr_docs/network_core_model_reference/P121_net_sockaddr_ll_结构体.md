---
id: learning.zephyr-docs.network-core-model-reference.page-121
title: net_sockaddr_ll_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr__ll.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第121章\_net\_sockaddr\_ll\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr__ll.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数据包套接字（Packet Socket）的套接字地址结构。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

数据包套接字（Packet Socket）的套接字地址结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 121.1\_数据成员（Data Fields）

<a id="r_a8c7064a9685e009f179a2582af50c198"></a>

```c
net_sa_family_t sll_family
```

相关声明：[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)、[sll_family](#a8c7064a9685e009f179a2582af50c198)。

始终为 `NET_AF_PACKET`。

<a id="r_acee20fa52f5544b0675064ff7c8c08ed"></a>

```c
uint16_t sll_protocol
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sll_protocol](#acee20fa52f5544b0675064ff7c8c08ed)。

物理层协议（Physical-layer protocol）。

<a id="r_a7dc05521a96c49b14dfbb178ab6ca14a"></a>

```c
int sll_ifindex
```

相关声明：[sll_ifindex](#a7dc05521a96c49b14dfbb178ab6ca14a)。

接口编号（Interface number）。

<a id="r_a917c8c2df6482ae6427ced625bc00555"></a>

```c
uint16_t sll_hatype
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sll_hatype](#a917c8c2df6482ae6427ced625bc00555)。

地址解析协议硬件类型（ARP hardware type）。

<a id="r_a40552f91379790433041e2620d7800d7"></a>

```c
uint8_t sll_pkttype
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sll_pkttype](#a40552f91379790433041e2620d7800d7)。

数据包类型（Packet type）。

<a id="r_ac575672a144a28f49b3e63ee157ec8c9"></a>

```c
uint8_t sll_halen
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sll_halen](#ac575672a144a28f49b3e63ee157ec8c9)。

地址长度（Address Length）。

<a id="r_aff9f7cf10eaceab03a9ce582c2d76fea"></a>

```c
uint8_t sll_addr [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sll_addr](#aff9f7cf10eaceab03a9ce582c2d76fea)。

物理层地址（Physical-layer address），采用大端字节序（Big endian）。

## 121.2\_详细说明（Detailed Documentation）

<a id="aff9f7cf10eaceab03a9ce582c2d76fea"></a>

### `sll_addr`

```c
uint8_t net_sockaddr_ll::sll_addr[8]
```

物理层地址（Physical-layer address），采用大端字节序（Big endian）。

<a id="a8c7064a9685e009f179a2582af50c198"></a>

### `sll_family`

```c
net_sa_family_t net_sockaddr_ll::sll_family
```

始终为 `NET_AF_PACKET`。

<a id="ac575672a144a28f49b3e63ee157ec8c9"></a>

### `sll_halen`

```c
uint8_t net_sockaddr_ll::sll_halen
```

地址长度（Address Length）。

<a id="a917c8c2df6482ae6427ced625bc00555"></a>

### `sll_hatype`

```c
uint16_t net_sockaddr_ll::sll_hatype
```

地址解析协议硬件类型（ARP hardware type）。

<a id="a7dc05521a96c49b14dfbb178ab6ca14a"></a>

### `sll_ifindex`

```c
int net_sockaddr_ll::sll_ifindex
```

接口编号（Interface number）。

<a id="a40552f91379790433041e2620d7800d7"></a>

### `sll_pkttype`

```c
uint8_t net_sockaddr_ll::sll_pkttype
```

数据包类型（Packet type）。

<a id="acee20fa52f5544b0675064ff7c8c08ed"></a>

### `sll_protocol`

```c
uint16_t net_sockaddr_ll::sll_protocol
```

物理层协议（Physical-layer protocol）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 121.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P120_net_sockaddr_in6_结构体.md) · [返回大纲](大纲.md) · [下一章](P122_net_sockaddr_nm_结构体.md)
