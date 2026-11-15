---
id: learning.zephyr-docs.network-core-model-reference.page-60
title: net_eth_mac_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__eth__mac__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_net\_eth\_mac\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__eth__mac__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MAC地址配置（Address Configuration）。

```c
#include <zephyr/net/ethernet.h>
```

<a id="details"></a>

MAC地址配置（Address Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_a0bac0f7f2af6cb03eeb90435799c7a2d"></a>

```c
enum net_eth_mac_type type
```

相关声明：[net_eth_mac_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac2433b0d82ef25373b2c0f994e248e92)、[type](#a0bac0f7f2af6cb03eeb90435799c7a2d)。

配置类型（Configuration Type）。

<a id="r_a66656331031d3324e4fd0429028311f4"></a>

```c
uint8_t addr [6U]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr](#a66656331031d3324e4fd0429028311f4)。

静态MAC地址部分（Static MAC Address Part）。

<a id="r_aa9e496b7d76e2920381365275a405412"></a>

```c
uint8_t addr_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr_len](#aa9e496b7d76e2920381365275a405412)。

静态提供部分的长度。

<a id="r_a344aa4435360014cc6080dc0ba2d7dc3"></a>

```c
struct nvmem_cell cell
```

相关声明：[nvmem_cell](../storage/P019_NVMEM数据单元结构.md)、[cell](#a344aa4435360014cc6080dc0ba2d7dc3)。

用于读取MAC地址的非易失性内存单元（NVMEM Cell）。

## 60.2\_详细说明（Detailed Documentation）

<a id="a66656331031d3324e4fd0429028311f4"></a>

### `addr`

```c
uint8_t net_eth_mac_config::addr[6U]
```

静态MAC地址部分（Static MAC Address Part）。

提供的数据少于6字节时，可将其作为随机生成MAC地址或NVMEM单元读出数据的前缀，例如用来设置组织唯一标识符（OUI）。

<a id="aa9e496b7d76e2920381365275a405412"></a>

### `addr_len`

```c
uint8_t net_eth_mac_config::addr_len
```

静态提供部分的长度。

<a id="a344aa4435360014cc6080dc0ba2d7dc3"></a>

### `cell`

```c
struct nvmem_cell net_eth_mac_config::cell
```

用于读取MAC地址的非易失性内存单元（NVMEM Cell）。

**注意（Attention）**：注意（Attention）：仅在启用Kconfig选项CONFIG_NVMEM时可用。

<a id="a0bac0f7f2af6cb03eeb90435799c7a2d"></a>

### `type`

```c
enum net_eth_mac_type net_eth_mac_config::type
```

配置类型（Configuration Type）。

本数据类型文档由以下文件生成：

- `zephyr/net/ethernet.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [net_eth_mac_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac2433b0d82ef25373b2c0f994e248e92)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [nvmem_cell](../storage/P019_NVMEM数据单元结构.md)
- [CONFIG_NVMEM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_net_eth_addr_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_net_eth_mcast_addr_结构体.md)
