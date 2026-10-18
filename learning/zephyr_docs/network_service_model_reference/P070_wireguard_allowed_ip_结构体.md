---
id: learning.zephyr-docs.network-service-model-reference.page-70
title: wireguard_allowed_ip_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwireguard__allowed__ip.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_wireguard\_allowed\_ip\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwireguard__allowed__ip.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WireGuard允许IP地址（Allowed IP Address）的结构。

```c
#include <zephyr/net/wireguard.h>
```

<a id="details"></a>

WireGuard允许IP地址（Allowed IP Address）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 70.1\_数据成员（Data Fields）

<a id="r_a8aa426557b26b39e0d75378bb3b6191a"></a>

```c
struct net_addr addr
```

相关声明：[addr](#a8aa426557b26b39e0d75378bb3b6191a)。

允许的 IPv4 或 IPv6 地址。

<a id="r_a8fa36acaced72872623cdd31c263f53f"></a>

```c
uint8_t mask_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mask_len](#a8fa36acaced72872623cdd31c263f53f)。

网络掩码（IPv4）或前缀（IPv6）的长度。

<a id="r_afc296b40c62a86ee8beb311fbbab3655"></a>

```c
bool is_valid: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_valid](#afc296b40c62a86ee8beb311fbbab3655)。

允许的 IP 地址是否有效。

## 70.2\_详细说明（Detailed Documentation）

<a id="a8aa426557b26b39e0d75378bb3b6191a"></a>

### `addr`

```c
struct net_addr wireguard_allowed_ip::addr
```

允许的 IPv4 或 IPv6 地址。

<a id="afc296b40c62a86ee8beb311fbbab3655"></a>

### `is_valid`

```c
bool wireguard_allowed_ip::is_valid
```

允许的 IP 地址是否有效。

<a id="a8fa36acaced72872623cdd31c263f53f"></a>

### `mask_len`

```c
uint8_t wireguard_allowed_ip::mask_len
```

网络掩码（IPv4）或前缀（IPv6）的长度。

本数据类型文档由以下文件生成：

- `zephyr/net/wireguard.h`

## 70.3\_原页交叉引用（Cross References）

- [zephyr/net/wireguard.h](https://docs.zephyrproject.org/latest/doxygen/html/wireguard_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P069_virtual_interface_context_结构体.md) · [返回大纲](大纲.md) · [下一章](P071_wireguard_peer_config_结构体.md)
