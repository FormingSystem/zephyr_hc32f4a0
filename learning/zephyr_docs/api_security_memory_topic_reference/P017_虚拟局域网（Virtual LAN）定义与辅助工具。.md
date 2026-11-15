---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-17
title: 虚拟局域网（Virtual LAN）定义与辅助工具。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_虚拟局域网（Virtual LAN）定义与辅助工具。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

VLAN 定义与辅助工具。

<a id="details"></a>

虚拟局域网（VLAN）定义与辅助函数（Helpers）。**引入版本（Since）：**1.12。**版本（Version）：**0.8.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.1\_宏定义（Macros）

<a id="r_ga665458f4b8f9c83ea0c1609207d3dd70"></a>

```c
#define NET_VLAN_TAG_UNSPEC 0x0fff
```

相关声明：[NET_VLAN_TAG_UNSPEC](#ga665458f4b8f9c83ea0c1609207d3dd70)。

未指定 VLAN 标签值（Unspecified VLAN Tag Value）。

<a id="r_gad1db5bb85a9744c8a8af8d2e1ebcfe69"></a>

```c
#define NET_VLAN_TAG_PRIORITY 0x0000
```

相关声明：[NET_VLAN_TAG_PRIORITY](#gad1db5bb85a9744c8a8af8d2e1ebcfe69)。

用于转发到原生接口的 VLAN 标识（VLAN ID），即优先级标记（Priority Tagging）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.2\_函数（Functions）

<a id="r_gad12123bb6c9920f21a6faed0e9bf70a6"></a>

```c
static uint16_t net_eth_vlan_get_vid (uint16_t tci)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_eth_vlan_get_vid](#gad12123bb6c9920f21a6faed0e9bf70a6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从标签控制信息（TCI）中获取 VLAN 标识符（VID）。

<a id="r_ga090648b166db1dc5ee9db71bfba1f97b"></a>

```c
static uint8_t net_eth_vlan_get_dei (uint16_t tci)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_eth_vlan_get_dei](#ga090648b166db1dc5ee9db71bfba1f97b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从标签控制信息（TCI）中获取可丢弃指示位（DEI）。

<a id="r_gafc746a075a23e4ad2c1c76328a8d773a"></a>

```c
static uint8_t net_eth_vlan_get_pcp (uint16_t tci)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_eth_vlan_get_pcp](#gafc746a075a23e4ad2c1c76328a8d773a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从标签控制信息（TCI）中获取优先级代码点（PCP）。

<a id="r_ga06b2977281f627ebb9529512aecc20dd"></a>

```c
static uint16_t net_eth_vlan_set_vid (uint16_t tci, uint16_t vid)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_eth_vlan_set_vid](#ga06b2977281f627ebb9529512aecc20dd)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在标签控制信息（TCI）中设置 VLAN 标识符（VID）。

<a id="r_ga6fcea099258c6be9c7cbfbd92fd4e8ab"></a>

```c
static uint16_t net_eth_vlan_set_dei (uint16_t tci, bool dei)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_eth_vlan_set_dei](#ga6fcea099258c6be9c7cbfbd92fd4e8ab)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

在标签控制信息（TCI）中设置可丢弃指示位（DEI）。

<a id="r_gadee54f9a2af345dd3981f39d73e1bc10"></a>

```c
static uint16_t net_eth_vlan_set_pcp (uint16_t tci, uint8_t pcp)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_eth_vlan_set_pcp](#gadee54f9a2af345dd3981f39d73e1bc10)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在标签控制信息（TCI）中设置优先级代码点（PCP）。

## 17.3\_详细说明（Detailed Documentation）

<a id="gad1db5bb85a9744c8a8af8d2e1ebcfe69"></a>

### `NET_VLAN_TAG_PRIORITY`

```c
#define NET_VLAN_TAG_PRIORITY 0x0000
```

```c
#include <zephyr/net/ethernet_vlan.h>
```

用于转发到原生接口的 VLAN 标识（VLAN ID），即优先级标记（Priority Tagging）。

<a id="ga665458f4b8f9c83ea0c1609207d3dd70"></a>

### `NET_VLAN_TAG_UNSPEC`

```c
#define NET_VLAN_TAG_UNSPEC 0x0fff
```

```c
#include <zephyr/net/ethernet_vlan.h>
```

未指定 VLAN 标签值（Unspecified VLAN Tag Value）。

<a id="ga090648b166db1dc5ee9db71bfba1f97b"></a>

### `net_eth_vlan_get_dei()`

```c
uint8_t net_eth_vlan_get_dei ( uint16_t tci)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet_vlan.h>
```

从标签控制信息（TCI）中获取可丢弃指示位（DEI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tci` | VLAN 标签控制信息（Tag Control Information，TCI）。 |

**返回（Returns）**：**返回值（Returns）：**可丢弃指示位（Drop Eligible Indicator，DEI）。

<a id="gafc746a075a23e4ad2c1c76328a8d773a"></a>

### `net_eth_vlan_get_pcp()`

```c
uint8_t net_eth_vlan_get_pcp ( uint16_t tci)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet_vlan.h>
```

从标签控制信息（TCI）中获取优先级代码点（PCP）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tci` | VLAN 标签控制信息（Tag Control Information，TCI）。 |

**返回（Returns）**：**返回值（Returns）：**优先级代码点（Priority Code Point，PCP）。

<a id="gad12123bb6c9920f21a6faed0e9bf70a6"></a>

### `net_eth_vlan_get_vid()`

```c
uint16_t net_eth_vlan_get_vid ( uint16_t tci)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet_vlan.h>
```

从标签控制信息（TCI）中获取 VLAN 标识符（VID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tci` | VLAN 标签控制信息（Tag Control Information，TCI）。 |

**返回（Returns）**：**返回值（Returns）：**VLAN 标识符（VID）。

<a id="ga6fcea099258c6be9c7cbfbd92fd4e8ab"></a>

### `net_eth_vlan_set_dei()`

```c
uint16_t net_eth_vlan_set_dei ( uint16_t tci, bool dei )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet_vlan.h>
```

在标签控制信息（TCI）中设置可丢弃指示位（DEI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tci` | VLAN 标签控制信息（Tag Control Information，TCI）。 |
| `dei` | 可丢弃指示位（Drop Eligible Indicator，DEI）。 |

**返回（Returns）**：**返回值（Returns）：**新的标签控制信息（TCI）值。

<a id="gadee54f9a2af345dd3981f39d73e1bc10"></a>

### `net_eth_vlan_set_pcp()`

```c
uint16_t net_eth_vlan_set_pcp ( uint16_t tci, uint8_t pcp )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet_vlan.h>
```

在标签控制信息（TCI）中设置优先级代码点（PCP）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tci` | VLAN 标签控制信息（Tag Control Information，TCI）。 |
| `pcp` | 优先级代码点（Priority Code Point，PCP）。 |

**返回（Returns）**：**返回值（Returns）：**新的标签控制信息（TCI）值。

<a id="ga06b2977281f627ebb9529512aecc20dd"></a>

### `net_eth_vlan_set_vid()`

```c
uint16_t net_eth_vlan_set_vid ( uint16_t tci, uint16_t vid )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ethernet_vlan.h>
```

在标签控制信息（TCI）中设置 VLAN 标识符（VID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tci` | VLAN 标签控制信息（Tag Control Information，TCI）。 |
| `vid` | VLAN 标识符（VID）。 |

**返回（Returns）**：**返回值（Returns）：**新的标签控制信息（TCI）值。


## 17.4\_原页交叉引用（Cross References）

- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/net/ethernet_vlan.h](../api_file_network_device_reference/P011_zephyr__net__ethernet_vlan.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_VL53L0X API主题.md) · [返回大纲](大纲.md) · [下一章](P018_Wi-Fi 网络管理器 API（Network Manager API）.md)
