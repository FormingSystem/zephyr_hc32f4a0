---
id: learning.zephyr-docs.network-core-model-reference.page-86
title: net_if_ipv6_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__ipv6.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第86章\_net\_if\_ipv6\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__ipv6.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv6配置（Configuration）。

```c
#include <zephyr/net/net_if.h>
```

<a id="details"></a>

IPv6配置（Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 86.1\_数据成员（Data Fields）

<a id="r_adb6431d336cc3f46972e13d2255452c8"></a>

```c
struct net_if_addr unicast [NET_IF_MAX_IPV6_ADDR]
```

相关声明：[net_if_addr](P080_net_if_addr_结构体.md)、[unicast](#adb6431d336cc3f46972e13d2255452c8)。

单播 IP 地址（Unicast IP addresses）。

<a id="r_a727d2773e0dee3be687dda5b2dd55682"></a>

```c
struct net_if_mcast_addr mcast [NET_IF_MAX_IPV6_MADDR]
```

相关声明：[net_if_mcast_addr](P089_net_if_mcast_addr_结构体.md)、[mcast](#a727d2773e0dee3be687dda5b2dd55682)。

多播 IP 地址（Multicast IP addresses）。

<a id="r_a2dccdc984f08527302d8d910a2658f72"></a>

```c
struct net_if_ipv6_prefix prefix [NET_IF_MAX_IPV6_PREFIX]
```

相关声明：[net_if_ipv6_prefix](P087_net_if_ipv6_prefix_结构体.md)、[prefix](#a2dccdc984f08527302d8d910a2658f72)。

前缀（Prefixes）。

<a id="r_a500a78fe23ee2ebc63f3d3b53b5b92ea"></a>

```c
uint32_t base_reachable_time
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[base_reachable_time](#a500a78fe23ee2ebc63f3d3b53b5b92ea)。

默认可达时间（Default reachable time；RFC 4861，第 52 页）。

<a id="r_af57b7dca189167f8cc757c4ed6b08f2f"></a>

```c
uint32_t reachable_time
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reachable_time](#af57b7dca189167f8cc757c4ed6b08f2f)。

可达时间（Reachable time；RFC 4861，第 20 页）。

<a id="r_ac5ee47ff9d3e429ecbb8623e5d713246"></a>

```c
uint32_t retrans_timer
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[retrans_timer](#ac5ee47ff9d3e429ecbb8623e5d713246)。

重传定时器（Retransmit timer；RFC 4861，第 52 页）。

<a id="r_a71775a082984274fbc7c009ead18e751"></a>

```c
uint8_t hop_limit
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hop_limit](#a71775a082984274fbc7c009ead18e751)。

IPv6跳数限制（Hop Limit）。

<a id="r_ae94906c28578f2e1ea2506b0e2972d4c"></a>

```c
uint8_t mcast_hop_limit
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mcast_hop_limit](#ae94906c28578f2e1ea2506b0e2972d4c)。

IPv6组播跳数限制（Multicast Hop Limit）。

## 86.2\_详细说明（Detailed Documentation）

<a id="a500a78fe23ee2ebc63f3d3b53b5b92ea"></a>

### `base_reachable_time`

```c
uint32_t net_if_ipv6::base_reachable_time
```

默认可达时间（Default reachable time；RFC 4861，第 52 页）。

<a id="a71775a082984274fbc7c009ead18e751"></a>

### `hop_limit`

```c
uint8_t net_if_ipv6::hop_limit
```

IPv6跳数限制（Hop Limit）。

<a id="a727d2773e0dee3be687dda5b2dd55682"></a>

### `mcast`

```c
struct net_if_mcast_addr net_if_ipv6::mcast[NET_IF_MAX_IPV6_MADDR]
```

多播 IP 地址（Multicast IP addresses）。

<a id="ae94906c28578f2e1ea2506b0e2972d4c"></a>

### `mcast_hop_limit`

```c
uint8_t net_if_ipv6::mcast_hop_limit
```

IPv6组播跳数限制（Multicast Hop Limit）。

<a id="a2dccdc984f08527302d8d910a2658f72"></a>

### `prefix`

```c
struct net_if_ipv6_prefix net_if_ipv6::prefix[NET_IF_MAX_IPV6_PREFIX]
```

前缀（Prefixes）。

<a id="af57b7dca189167f8cc757c4ed6b08f2f"></a>

### `reachable_time`

```c
uint32_t net_if_ipv6::reachable_time
```

可达时间（Reachable time；RFC 4861，第 20 页）。

<a id="ac5ee47ff9d3e429ecbb8623e5d713246"></a>

### `retrans_timer`

```c
uint32_t net_if_ipv6::retrans_timer
```

重传定时器（Retransmit timer；RFC 4861，第 52 页）。

<a id="adb6431d336cc3f46972e13d2255452c8"></a>

### `unicast`

```c
struct net_if_addr net_if_ipv6::unicast[NET_IF_MAX_IPV6_ADDR]
```

单播 IP 地址（Unicast IP addresses）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_if.h`

## 86.3\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [net_if_addr](P080_net_if_addr_结构体.md)
- [net_if_mcast_addr](P089_net_if_mcast_addr_结构体.md)
- [net_if_ipv6_prefix](P087_net_if_ipv6_prefix_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [RFC 4861, page-52](https://datatracker.ietf.org/doc/html/rfc4861#page-52)
- [RFC 4861, page-20](https://datatracker.ietf.org/doc/html/rfc4861#page-20)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P085_net_if_ipv4_结构体.md) · [返回大纲](大纲.md) · [下一章](P087_net_if_ipv6_prefix_结构体.md)
