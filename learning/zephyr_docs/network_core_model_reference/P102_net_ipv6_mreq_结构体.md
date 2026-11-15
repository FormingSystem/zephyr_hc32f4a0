---
id: learning.zephyr-docs.network-core-model-reference.page-102
title: net_ipv6_mreq_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__ipv6__mreq.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第102章\_net\_ipv6\_mreq\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__ipv6__mreq.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

加入或离开IPv6组播组（Multicast Group）时使用的结构。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

加入或离开IPv6组播组（Multicast Group）时使用的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 102.1\_数据成员（Data Fields）

<a id="r_a17fd782a854df2a8c793aaec9892420d"></a>

```c
struct net_in6_addr ipv6mr_multiaddr
```

相关声明：[net_in6_addr](P094_net_in6_addr_结构体.md)、[ipv6mr_multiaddr](#a17fd782a854df2a8c793aaec9892420d)。

组的 IPv6 多播地址（IPv6 multicast address）。

<a id="r_a3903141b4b67e2dfc977b3fad38d24a8"></a>

```c
int ipv6mr_ifindex
```

相关声明：[ipv6mr_ifindex](#a3903141b4b67e2dfc977b3fad38d24a8)。

本地 IPv6 地址所属的网络接口索引（Network interface index）。

## 102.2\_详细说明（Detailed Documentation）

<a id="a3903141b4b67e2dfc977b3fad38d24a8"></a>

### `ipv6mr_ifindex`

```c
int net_ipv6_mreq::ipv6mr_ifindex
```

本地 IPv6 地址所属的网络接口索引（Network interface index）。

<a id="a17fd782a854df2a8c793aaec9892420d"></a>

### `ipv6mr_multiaddr`

```c
struct net_in6_addr net_ipv6_mreq::ipv6mr_multiaddr
```

组的 IPv6 多播地址（IPv6 multicast address）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 102.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [net_in6_addr](P094_net_in6_addr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P101_net_iptable_rule_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P103_net_l2_结构体.md)
