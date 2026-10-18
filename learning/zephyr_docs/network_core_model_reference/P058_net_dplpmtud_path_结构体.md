---
id: learning.zephyr-docs.network-core-model-reference.page-58
title: net_dplpmtud_path_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__dplpmtud__path.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_net\_dplpmtud\_path\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__dplpmtud__path.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

归传输层所有的数据报分组层路径MTU发现（DPLPMTUD）路径句柄。

```c
#include <zephyr/net/dplpmtud.h>
```

<a id="details"></a>

归传输层所有的数据报分组层路径MTU发现（DPLPMTUD）路径句柄。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_a54087b52e2fdb7a79c600fe746e8233c"></a>

```c
struct net_sockaddr_storage dst
```

相关声明：[dst](#a54087b52e2fdb7a79c600fe746e8233c)。

此路径的远端目的地（Remote Destination）。

<a id="r_a96f94f2f1ef88dfbe010fb1df74e101e"></a>

```c
uint16_t max_plpmtu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_plpmtu](#a96f94f2f1ef88dfbe010fb1df74e101e)。

传输本地的最大分组层路径MTU（PLPMTU）；不设上限时为UINT16_MAX。

<a id="r_a899fb7ac2822e8921a8b1232c5315dd0"></a>

```c
bool in_use
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[in_use](#a899fb7ac2822e8921a8b1232c5315dd0)。

路径句柄（Path Handle）已初始化。

## 58.2\_详细说明（Detailed Documentation）

<a id="a54087b52e2fdb7a79c600fe746e8233c"></a>

### `dst`

```c
struct net_sockaddr_storage net_dplpmtud_path::dst
```

此路径的远端目的地（Remote Destination）。

<a id="a899fb7ac2822e8921a8b1232c5315dd0"></a>

### `in_use`

```c
bool net_dplpmtud_path::in_use
```

路径句柄（Path Handle）已初始化。

<a id="a96f94f2f1ef88dfbe010fb1df74e101e"></a>

### `max_plpmtu`

```c
uint16_t net_dplpmtud_path::max_plpmtu
```

传输本地的最大分组层路径MTU（PLPMTU）；不设上限时为UINT16_MAX。

本数据类型文档由以下文件生成：

- `zephyr/net/dplpmtud.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/net/dplpmtud.h](https://docs.zephyrproject.org/latest/doxygen/html/dplpmtud_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_net_dhcpv6_server_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_net_eth_addr_结构体.md)
