---
id: learning.zephyr-docs.network-core-model-reference.page-97
title: net_in_pktinfo_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__in__pktinfo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第97章\_net\_in\_pktinfo\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__in__pktinfo.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传入的IPv4数据包信息（Packet Information）。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

接收到的 IPv4 数据包信息（Incoming IPv4 packet information）。调用 `recvmsg()` 且设置了 `IP_PKTINFO` 套接字选项时，用作辅助数据（Ancillary data）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 97.1\_数据成员（Data Fields）

<a id="r_a00e5cde6d36f127d2f0710c541038ca0"></a>

```c
unsigned int ipi_ifindex
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[ipi_ifindex](#a00e5cde6d36f127d2f0710c541038ca0)。

网络接口索引（Network interface index）。

<a id="r_ad1fb0298ae64454f28f7e4b6738bf7fe"></a>

```c
struct net_in_addr ipi_spec_dst
```

相关声明：[net_in_addr](P096_net_in_addr_结构体.md)、[ipi_spec_dst](#ad1fb0298ae64454f28f7e4b6738bf7fe)。

本地地址（Local address）。

<a id="r_a75c8fff8b98862aef9ceba341b9276fe"></a>

```c
struct net_in_addr ipi_addr
```

相关声明：[net_in_addr](P096_net_in_addr_结构体.md)、[ipi_addr](#a75c8fff8b98862aef9ceba341b9276fe)。

报头中的目的地址（Header Destination address）。

## 97.2\_详细说明（Detailed Documentation）

<a id="a75c8fff8b98862aef9ceba341b9276fe"></a>

### `ipi_addr`

```c
struct net_in_addr net_in_pktinfo::ipi_addr
```

报头中的目的地址（Header Destination address）。

<a id="a00e5cde6d36f127d2f0710c541038ca0"></a>

### `ipi_ifindex`

```c
unsigned int net_in_pktinfo::ipi_ifindex
```

网络接口索引（Network interface index）。

<a id="ad1fb0298ae64454f28f7e4b6738bf7fe"></a>

### `ipi_spec_dst`

```c
struct net_in_addr net_in_pktinfo::ipi_spec_dst
```

本地地址（Local address）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 97.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [net_in_addr](P096_net_in_addr_结构体.md)
- [recvmsg()](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#ae074d22829eb79c596fd60d0f9f9611f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P096_net_in_addr_结构体.md) · [返回大纲](大纲.md) · [下一章](P098_net_iovec_结构体.md)
