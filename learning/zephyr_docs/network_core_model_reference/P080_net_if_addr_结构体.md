---
id: learning.zephyr-docs.network-core-model-reference.page-80
title: net_if_addr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__addr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第80章\_net\_if\_addr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__addr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络接口的单播IP地址（Unicast IP Addresses）。

```c
#include <zephyr/net/net_if.h>
```

<a id="details"></a>

网络接口的单播IP地址（Unicast IP Addresses）。保存分配给此网络接口的单播IP地址。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 80.1\_数据成员（Data Fields）

<a id="r_a06b8d2e8b5ea6d8d671800d966163763"></a>

```c
struct net_addr address
```

相关声明：[address](#a06b8d2e8b5ea6d8d671800d966163763)。

IP 地址（IP address）。

<a id="r_a9abaf23ec98b22d1741bae410a1f7f3e"></a>

```c
atomic_t atomic_ref
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[atomic_ref](#a9abaf23ec98b22d1741bae410a1f7f3e)。

引用计数器。

<a id="r_ab4fd41001cc24615803bfabb9d48e7eb"></a>

```c
enum net_addr_type addr_type
```

相关声明：[net_addr_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gafecee2d4a331dc85ad962b81a6303e41)、[addr_type](#ab4fd41001cc24615803bfabb9d48e7eb)。

IP 地址的设置方式（Address configuration method）。

<a id="r_a3106fdcf0dd2479c95efafc586217a2c"></a>

```c
enum net_addr_state addr_state
```

相关声明：[net_addr_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga32e58fc83532ef57eeb6ff952f17288d)、[addr_state](#a3106fdcf0dd2479c95efafc586217a2c)。

地址的当前状态（Address state）。

```c
union {
```

<a id="r_ac888089362a0c1a188ed6c33850e1892"></a>

```c
};
```

<a id="r_a6e799428eb0633a25e4dc3c55e3a3b8c"></a>

```c
uint8_t is_infinite: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_infinite](#a6e799428eb0633a25e4dc3c55e3a3b8c)。

IP 地址是否永久有效（Valid forever）。

<a id="r_aed4d91ba064d24ad0d53c0960cde0352"></a>

```c
uint8_t is_used: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_used](#aed4d91ba064d24ad0d53c0960cde0352)。

此 IP 地址是否正在使用（In use）。

<a id="r_a1db7cc6c7566baf9340dab6771ca5010"></a>

```c
uint8_t is_mesh_local: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_mesh_local](#a1db7cc6c7566baf9340dab6771ca5010)。

此 IP 地址的使用是否仅限于子网（Subnet／Mesh）。

<a id="r_a1dd933a37afcb7d708cd602911c38e0a"></a>

```c
uint8_t is_temporary: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_temporary](#a1dd933a37afcb7d708cd602911c38e0a)。

此 IP 地址是否为临时地址（Temporary address），例如由 IPv6 隐私扩展（Privacy extension，RFC 8981）生成的地址。

<a id="r_aa556ea52e1f923fd3e39328dc254c365"></a>

```c
uint8_t is_added: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[is_added](#aa556ea52e1f923fd3e39328dc254c365)。

是否已添加此地址（Address added）。

## 80.2\_详细说明（Detailed Documentation）

<a id="ac888089362a0c1a188ed6c33850e1892"></a>

### `[union]`

```c
union { ... } net_if_addr
```

<a id="a3106fdcf0dd2479c95efafc586217a2c"></a>

### `addr_state`

```c
enum net_addr_state net_if_addr::addr_state
```

地址的当前状态（Address state）。

<a id="ab4fd41001cc24615803bfabb9d48e7eb"></a>

### `addr_type`

```c
enum net_addr_type net_if_addr::addr_type
```

IP 地址的设置方式（Address configuration method）。

<a id="a06b8d2e8b5ea6d8d671800d966163763"></a>

### `address`

```c
struct net_addr net_if_addr::address
```

IP 地址（IP address）。

<a id="a9abaf23ec98b22d1741bae410a1f7f3e"></a>

### `atomic_ref`

```c
atomic_t net_if_addr::atomic_ref
```

引用计数器。

若有套接字（Socket）已将本地端点（Local endpoint）绑定到此地址，此字段用于防止该地址被移除。

<a id="aa556ea52e1f923fd3e39328dc254c365"></a>

### `is_added`

```c
uint8_t net_if_addr::is_added
```

是否已添加此地址（Address added）。

<a id="a6e799428eb0633a25e4dc3c55e3a3b8c"></a>

### `is_infinite`

```c
uint8_t net_if_addr::is_infinite
```

IP 地址是否永久有效（Valid forever）。

<a id="a1db7cc6c7566baf9340dab6771ca5010"></a>

### `is_mesh_local`

```c
uint8_t net_if_addr::is_mesh_local
```

此 IP 地址的使用是否仅限于子网（Subnet／Mesh）。

<a id="a1dd933a37afcb7d708cd602911c38e0a"></a>

### `is_temporary`

```c
uint8_t net_if_addr::is_temporary
```

此 IP 地址是否为临时地址（Temporary address），例如由 IPv6 隐私扩展（Privacy extension，RFC 8981）生成的地址。

<a id="aed4d91ba064d24ad0d53c0960cde0352"></a>

### `is_used`

```c
uint8_t net_if_addr::is_used
```

此 IP 地址是否正在使用（In use）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_if.h`

## 80.3\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [net_addr_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gafecee2d4a331dc85ad962b81a6303e41)
- [net_addr_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga32e58fc83532ef57eeb6ff952f17288d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [RFC 8981](https://datatracker.ietf.org/doc/html/rfc8981)
- [net_if_addr](P080_net_if_addr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P079_net_if_结构体.md) · [返回大纲](大纲.md) · [下一章](P081_net_if_addr_ipv4_结构体.md)
