---
id: learning.zephyr-docs.network-core-model-reference.page-95
title: net_in6_pktinfo_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__in6__pktinfo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第95章\_net\_in6\_pktinfo\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__in6__pktinfo.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传入的IPv6数据包信息（Packet Information）。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

接收到的 IPv6 数据包信息（Incoming IPv6 packet information）。调用 `recvmsg()` 且设置了 `IPV6_RECVPKTINFO` 套接字选项时，用作辅助数据（Ancillary data）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 95.1\_数据成员（Data Fields）

<a id="r_af16fc143121a3557d338f8476fb0d0dd"></a>

```c
struct net_in6_addr ipi6_addr
```

相关声明：[net_in6_addr](P094_net_in6_addr_结构体.md)、[ipi6_addr](#af16fc143121a3557d338f8476fb0d0dd)。

目的 IPv6 地址（Destination IPv6 address）。

<a id="r_a471aed9984659549af97a694685869a3"></a>

```c
unsigned int ipi6_ifindex
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[ipi6_ifindex](#a471aed9984659549af97a694685869a3)。

接收接口索引（Receive interface index）。

## 95.2\_详细说明（Detailed Documentation）

<a id="af16fc143121a3557d338f8476fb0d0dd"></a>

### `ipi6_addr`

```c
struct net_in6_addr net_in6_pktinfo::ipi6_addr
```

目的 IPv6 地址（Destination IPv6 address）。

<a id="a471aed9984659549af97a694685869a3"></a>

### `ipi6_ifindex`

```c
unsigned int net_in6_pktinfo::ipi6_ifindex
```

接收接口索引（Receive interface index）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 95.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [net_in6_addr](P094_net_in6_addr_结构体.md)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [recvmsg()](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#ae074d22829eb79c596fd60d0f9f9611f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P094_net_in6_addr_结构体.md) · [返回大纲](大纲.md) · [下一章](P096_net_in_addr_结构体.md)
