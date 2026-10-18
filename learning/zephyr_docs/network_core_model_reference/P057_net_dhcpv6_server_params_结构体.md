---
id: learning.zephyr-docs.network-core-model-reference.page-57
title: net_dhcpv6_server_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__dhcpv6__server__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_net\_dhcpv6\_server\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__dhcpv6__server__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DHCPv6服务器（Server）的配置参数。

```c
#include <zephyr/net/dhcpv6_server.h>
```

<a id="details"></a>

DHCPv6服务器（Server）的配置参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_a426d99918b620fdc614d5812bc130256"></a>

```c
struct net_in6_addr prefix
```

相关声明：[net_in6_addr](P094_net_in6_addr_结构体.md)、[prefix](#a426d99918b620fdc614d5812bc130256)。

用于前缀委派（IA_PD）的前缀池基址（Prefix Pool Base）。

<a id="r_a83e5a07233e7558c487fe6804d21fd09"></a>

```c
struct net_in6_addr addr
```

相关声明：[net_in6_addr](P094_net_in6_addr_结构体.md)、[addr](#a83e5a07233e7558c487fe6804d21fd09)。

用于非临时地址分配（IA_NA）的地址池基址（Address Pool Base）。

<a id="r_aeeaf66c9475df8dc0e948938228f08d7"></a>

```c
uint32_t valid_lifetime
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[valid_lifetime](#aeeaf66c9475df8dc0e948938228f08d7)。

向客户端通告的有效生存期（Valid Lifetime），单位为秒。

<a id="r_a18cb34a5b577bebac7217fa13be13a5f"></a>

```c
uint32_t preferred_lifetime
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[preferred_lifetime](#a18cb34a5b577bebac7217fa13be13a5f)。

向客户端通告的优先生存期（Preferred Lifetime），单位为秒。

<a id="r_a3cedeee330d5b1765757b4c45d9caf6c"></a>

```c
uint8_t prefix_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prefix_len](#a3cedeee330d5b1765757b4c45d9caf6c)。

委派给客户端的前缀长度（Prefix Length），单位为位，例如：

<a id="r_ae22caa5aeceefbfec8abac15334b1d67"></a>

```c
bool offer_addr: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[offer_addr](#ae22caa5aeceefbfec8abac15334b1d67)。

分发非临时地址（IA_NA）。

<a id="r_a809af0885a7bbd7860d699eebe7b9e08"></a>

```c
bool offer_prefix: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[offer_prefix](#a809af0885a7bbd7860d699eebe7b9e08)。

分发委派前缀（IA_PD）。

## 57.2\_详细说明（Detailed Documentation）

<a id="a83e5a07233e7558c487fe6804d21fd09"></a>

### `addr`

```c
struct net_in6_addr net_dhcpv6_server_params::addr
```

用于非临时地址分配（IA_NA）的地址池基址（Address Pool Base）。

租用地址（Leased Addresses）由此基址派生。

<a id="ae22caa5aeceefbfec8abac15334b1d67"></a>

### `offer_addr`

```c
bool net_dhcpv6_server_params::offer_addr
```

分发非临时地址（IA_NA）。

<a id="a809af0885a7bbd7860d699eebe7b9e08"></a>

### `offer_prefix`

```c
bool net_dhcpv6_server_params::offer_prefix
```

分发委派前缀（IA_PD）。

<a id="a18cb34a5b577bebac7217fa13be13a5f"></a>

### `preferred_lifetime`

```c
uint32_t net_dhcpv6_server_params::preferred_lifetime
```

向客户端通告的优先生存期（Preferred Lifetime），单位为秒。

0表示选择默认值。

<a id="a426d99918b620fdc614d5812bc130256"></a>

### `prefix`

```c
struct net_in6_addr net_dhcpv6_server_params::prefix
```

用于前缀委派（IA_PD）的前缀池基址（Prefix Pool Base）。

分发给请求路由器（Requesting Routers）的前缀，通过改变子网位从此基址派生。

<a id="a3cedeee330d5b1765757b4c45d9caf6c"></a>

### `prefix_len`

```c
uint8_t net_dhcpv6_server_params::prefix_len
```

委派给客户端的前缀长度（Prefix Length），单位为位，例如：

> 译注：原页此处的列表项为空，未提供示例内容。

<a id="aeeaf66c9475df8dc0e948938228f08d7"></a>

### `valid_lifetime`

```c
uint32_t net_dhcpv6_server_params::valid_lifetime
```

向客户端通告的有效生存期（Valid Lifetime），单位为秒。

0表示选择默认值。

本数据类型文档由以下文件生成：

- `zephyr/net/dhcpv6_server.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/net/dhcpv6_server.h](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6__server_8h_source.html)
- [net_in6_addr](P094_net_in6_addr_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_net_dhcpv6_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_net_dplpmtud_path_结构体.md)
