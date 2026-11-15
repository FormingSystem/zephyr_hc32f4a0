---
id: learning.zephyr-docs.api-file-network-device-reference.page-11
title: zephyr__net__ethernet_vlan.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ethernet__vlan_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_net\_\_ethernet\_vlan.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__vlan_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

虚拟局域网（VLAN）的专用定义。

<a id="details"></a>

```c
#include <zephyr/types.h>
```

查看此文件的源码。

虚拟局域网（Virtual LAN，VLAN）专用定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_ga665458f4b8f9c83ea0c1609207d3dd70"></a>

```c
#define NET_VLAN_TAG_UNSPEC 0x0fff
```

相关声明：[NET_VLAN_TAG_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#ga665458f4b8f9c83ea0c1609207d3dd70)。

未指定 VLAN 标签值（Unspecified VLAN Tag Value）。

<a id="r_gad1db5bb85a9744c8a8af8d2e1ebcfe69"></a>

```c
#define NET_VLAN_TAG_PRIORITY 0x0000
```

相关声明：[NET_VLAN_TAG_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#gad1db5bb85a9744c8a8af8d2e1ebcfe69)。

用于转发到原生接口的 VLAN 标识（VLAN ID），即优先级标记（Priority Tagging）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.2\_函数（Functions）

<a id="r_gad12123bb6c9920f21a6faed0e9bf70a6"></a>

```c
static uint16_t net_eth_vlan_get_vid (uint16_t tci)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_eth_vlan_get_vid](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#gad12123bb6c9920f21a6faed0e9bf70a6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从标签控制信息（TCI）中获取 VLAN 标识符（VID）。

<a id="r_ga090648b166db1dc5ee9db71bfba1f97b"></a>

```c
static uint8_t net_eth_vlan_get_dei (uint16_t tci)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_eth_vlan_get_dei](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#ga090648b166db1dc5ee9db71bfba1f97b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从标签控制信息（TCI）中获取可丢弃指示位（DEI）。

<a id="r_gafc746a075a23e4ad2c1c76328a8d773a"></a>

```c
static uint8_t net_eth_vlan_get_pcp (uint16_t tci)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_eth_vlan_get_pcp](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#gafc746a075a23e4ad2c1c76328a8d773a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从标签控制信息（TCI）中获取优先级代码点（PCP）。

<a id="r_ga06b2977281f627ebb9529512aecc20dd"></a>

```c
static uint16_t net_eth_vlan_set_vid (uint16_t tci, uint16_t vid)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_eth_vlan_set_vid](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#ga06b2977281f627ebb9529512aecc20dd)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在标签控制信息（TCI）中设置 VLAN 标识符（VID）。

<a id="r_ga6fcea099258c6be9c7cbfbd92fd4e8ab"></a>

```c
static uint16_t net_eth_vlan_set_dei (uint16_t tci, bool dei)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_eth_vlan_set_dei](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#ga6fcea099258c6be9c7cbfbd92fd4e8ab)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

在标签控制信息（TCI）中设置可丢弃指示位（DEI）。

<a id="r_gadee54f9a2af345dd3981f39d73e1bc10"></a>

```c
static uint16_t net_eth_vlan_set_pcp (uint16_t tci, uint8_t pcp)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_eth_vlan_set_pcp](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#gadee54f9a2af345dd3981f39d73e1bc10)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在标签控制信息（TCI）中设置优先级代码点（PCP）。


## 11.3\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P247_ethernet_vlan.h_源码浏览.md)
- [NET_VLAN_TAG_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#ga665458f4b8f9c83ea0c1609207d3dd70)
- [NET_VLAN_TAG_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#gad1db5bb85a9744c8a8af8d2e1ebcfe69)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_eth_vlan_get_vid](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#gad12123bb6c9920f21a6faed0e9bf70a6)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_eth_vlan_get_dei](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#ga090648b166db1dc5ee9db71bfba1f97b)
- [net_eth_vlan_get_pcp](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#gafc746a075a23e4ad2c1c76328a8d773a)
- [net_eth_vlan_set_vid](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#ga06b2977281f627ebb9529512aecc20dd)
- [net_eth_vlan_set_dei](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#ga6fcea099258c6be9c7cbfbd92fd4e8ab)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_eth_vlan_set_pcp](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html#gadee54f9a2af345dd3981f39d73e1bc10)

<a id="header-details"></a>

---

[上一章](P010_zephyr__dt-bindings__sensor__tmp11x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__bluetooth__audio__gmap.h_文件参考.md)
