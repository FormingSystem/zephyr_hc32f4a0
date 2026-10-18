---
id: learning.zephyr-docs.network-core-model-reference.page-9
title: ieee802154_cmd_assoc_req_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__cmd__assoc__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_ieee802154\_cmd\_assoc\_req\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__cmd__assoc__req.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

关联请求（Association Request）命令的载荷，即能力信息字段。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

关联请求（Association Request）命令的载荷，即能力信息字段（Capability Information Field）。见第7.5.2节及图7-22。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a2e5d1e9bec67edc09c168b2dffcc0a1f"></a>

```c
uint8_t alloc_addr: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[alloc_addr](#a22321a62b2049202c6eb84a25316bb9c)。

分配地址（Allocate Address）。

<a id="r_a9233f15f0fb2b2e005455016037ec137"></a>

```c
uint8_t sec_capability: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sec_capability](#a99a5743d96b9ebc5153edcfb326eb38a)。

安全能力（Security Capability）。

<a id="r_a2412cd9b17f201d923771ab06ce3f21b"></a>

```c
uint8_t reserved_2: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved_2](#a43e69b46fe01aa8278e78abd341ff01e)。

保留字段（Reserved），应为0。

<a id="r_a10f6734a013783343abb78cec19964d1"></a>

```c
uint8_t association_type: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[association_type](#adc81f209a8f17a90b50fb57f2990d5b8)。

关联类型（Association Type）。

<a id="r_a25e77918b53b3fa5e1b2b7f3959f3a31"></a>

```c
uint8_t rx_on: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_on](#aea1e48101ca4ee67972e66b566e56259)。

空闲时保持接收器开启（Receiver On When Idle）。

<a id="r_acc5fddf11a3c1531ac22652d3dcc66cd"></a>

```c
uint8_t power_src: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[power_src](#a306becbe9dc40df9f897c222e0d9f222)。

电源来源（Power Source）。

<a id="r_a49982164a6bfbe0213ccadfe82aa0f02"></a>

```c
uint8_t dev_type: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dev_type](#a75f60ccf3390f5371e8af6c9c2234bf5)。

设备类型（Device Type）：全功能设备（FFD）或精简功能设备（RFD）。

<a id="r_a38fe7c0dbe150f618ab2d698ca36088f"></a>

```c
uint8_t reserved_1: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved_1](#a19039e164a4804a8f8d901206b0bd19c)。

保留字段（Reserved），应为0。

<a id="r_a035bc9f5639f91ca39ac0142279d7ccd"></a>

```c
} ci
```

相关声明：[ci](#a035bc9f5639f91ca39ac0142279d7ccd)。

能力信息位域（Capability Information Bit Field）。

## 9.2\_详细说明（Detailed Documentation）

<a id="a22321a62b2049202c6eb84a25316bb9c"></a>

### `alloc_addr`

```c
uint8_t ieee802154_cmd_assoc_req::alloc_addr
```

分配地址（Allocate Address）。

<a id="adc81f209a8f17a90b50fb57f2990d5b8"></a>

### `association_type`

```c
uint8_t ieee802154_cmd_assoc_req::association_type
```

关联类型（Association Type）。

<a id="a035bc9f5639f91ca39ac0142279d7ccd"></a>

### `[struct]`

```c
struct { ... } ieee802154_cmd_assoc_req::ci
```

能力信息位域（Capability Information Bit Field）。

<a id="a75f60ccf3390f5371e8af6c9c2234bf5"></a>

### `dev_type`

```c
uint8_t ieee802154_cmd_assoc_req::dev_type
```

设备类型（Device Type）：全功能设备（FFD）或精简功能设备（RFD）。

<a id="a306becbe9dc40df9f897c222e0d9f222"></a>

### `power_src`

```c
uint8_t ieee802154_cmd_assoc_req::power_src
```

电源来源（Power Source）。

<a id="a19039e164a4804a8f8d901206b0bd19c"></a>

### `reserved_1`

```c
uint8_t ieee802154_cmd_assoc_req::reserved_1
```

保留字段（Reserved），应为0。

<a id="a43e69b46fe01aa8278e78abd341ff01e"></a>

### `reserved_2`

```c
uint8_t ieee802154_cmd_assoc_req::reserved_2
```

保留字段（Reserved），应为0。

<a id="aea1e48101ca4ee67972e66b566e56259"></a>

### `rx_on`

```c
uint8_t ieee802154_cmd_assoc_req::rx_on
```

空闲时保持接收器开启（Receiver On When Idle）。

<a id="a99a5743d96b9ebc5153edcfb326eb38a"></a>

### `sec_capability`

```c
uint8_t ieee802154_cmd_assoc_req::sec_capability
```

安全能力（Security Capability）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_ieee802154_beacon_sf_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_ieee802154_cmd_assoc_res_结构体.md)
