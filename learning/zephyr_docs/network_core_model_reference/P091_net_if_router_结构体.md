---
id: learning.zephyr-docs.network-core-model-reference.page-91
title: net_if_router_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__router.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第91章\_net\_if\_router\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__router.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统中路由器（Routers）的信息。

```c
#include <zephyr/net/net_if.h>
```

<a id="details"></a>

系统中的路由器信息（Router information）。保存路由器信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 91.1\_数据成员（Data Fields）

<a id="r_aabbac0cd0a59ca0eafdcfc0eaf5d909a"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#aabbac0cd0a59ca0eafdcfc0eaf5d909a)。

单向链表中的生存期定时器节点（Slist lifetime timer node）。

<a id="r_a86a2ca1b95e348acbde8ce90986b83db"></a>

```c
struct net_addr address
```

相关声明：[address](#a86a2ca1b95e348acbde8ce90986b83db)。

IP 地址（IP address）。

<a id="r_a03789aa0a40f7686b76616de0ca0401a"></a>

```c
struct net_if * iface
```

相关声明：[net_if](P079_net_if_结构体.md)、[iface](#a03789aa0a40f7686b76616de0ca0401a)。

路由器连接的网络接口（Network interface）。

<a id="r_adf4f4c722917b3c30f8c73bc2519957f"></a>

```c
uint32_t life_start
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[life_start](#adf4f4c722917b3c30f8c73bc2519957f)。

路由器生存期定时器起始时刻（Router life timer start）。

<a id="r_a4b0d2ad8f225ab61022c10dfce3db199"></a>

```c
uint16_t lifetime
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[lifetime](#a4b0d2ad8f225ab61022c10dfce3db199)。

路由器生存期（Router lifetime）。

<a id="r_a7196e6d2bc2c958d98dfe29143a62048"></a>

```c
uint8_t is_used: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_used](#a7196e6d2bc2c958d98dfe29143a62048)。

此路由器是否正在使用（In use）。

<a id="r_a34745207edcad2745d6ce311e2bf1894"></a>

```c
uint8_t is_default: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_default](#a34745207edcad2745d6ce311e2bf1894)。

是否为默认路由器（Default router）。

<a id="r_a4cb47f30241ae3d410f56f1487254ed0"></a>

```c
uint8_t is_infinite: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_infinite](#a4cb47f30241ae3d410f56f1487254ed0)。

路由器是否永久有效（Valid forever）。

## 91.2\_详细说明（Detailed Documentation）

<a id="a86a2ca1b95e348acbde8ce90986b83db"></a>

### `address`

```c
struct net_addr net_if_router::address
```

IP 地址（IP address）。

<a id="a03789aa0a40f7686b76616de0ca0401a"></a>

### `iface`

```c
struct net_if* net_if_router::iface
```

路由器连接的网络接口（Network interface）。

<a id="a34745207edcad2745d6ce311e2bf1894"></a>

### `is_default`

```c
uint8_t net_if_router::is_default
```

是否为默认路由器（Default router）。

<a id="a4cb47f30241ae3d410f56f1487254ed0"></a>

### `is_infinite`

```c
uint8_t net_if_router::is_infinite
```

路由器是否永久有效（Valid forever）。

<a id="a7196e6d2bc2c958d98dfe29143a62048"></a>

### `is_used`

```c
uint8_t net_if_router::is_used
```

此路由器是否正在使用（In use）。

<a id="adf4f4c722917b3c30f8c73bc2519957f"></a>

### `life_start`

```c
uint32_t net_if_router::life_start
```

路由器生存期定时器起始时刻（Router life timer start）。

<a id="a4b0d2ad8f225ab61022c10dfce3db199"></a>

### `lifetime`

```c
uint16_t net_if_router::lifetime
```

路由器生存期（Router lifetime）。

<a id="aabbac0cd0a59ca0eafdcfc0eaf5d909a"></a>

### `node`

```c
sys_snode_t net_if_router::node
```

单向链表中的生存期定时器节点（Slist lifetime timer node）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_if.h`

## 91.3\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [net_if](P079_net_if_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P090_net_if_mcast_monitor_结构体.md) · [返回大纲](大纲.md) · [下一章](P092_net_if_timestamp_cb_结构体.md)
