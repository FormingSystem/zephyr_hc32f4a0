---
id: learning.zephyr-docs.network-core-model-reference.page-8
title: ieee802154_beacon_sf_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__beacon__sf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_ieee802154\_beacon\_sf\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__beacon__sf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

信标载荷中的超帧规范（Superframe Specification）字段。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

信标载荷的超帧规范字段（Superframe Specification Field）。见第7.3.1.4节及图7-7。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_aa52c67ce1c7607dfeabbfe5706a75bb8"></a>

```c
uint16_t sf_order: 4
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sf_order](#aa52c67ce1c7607dfeabbfe5706a75bb8)。

超帧阶数子字段（Superframe Order Subfield）。

<a id="r_aa3f402e1ac43b609a366f0a7c87195bd"></a>

```c
uint16_t bc_order: 4
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bc_order](#aa3f402e1ac43b609a366f0a7c87195bd)。

信标阶数子字段（Beacon Order Subfield）。

<a id="r_a33a47bde19ad49508c981b1e7940ad93"></a>

```c
uint16_t association: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[association](#a33a47bde19ad49508c981b1e7940ad93)。

允许关联子字段（Association Permit Subfield）。

<a id="r_a7f62606165bb7d2bd96cf0923de1326e"></a>

```c
uint16_t coordinator: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[coordinator](#a7f62606165bb7d2bd96cf0923de1326e)。

PAN协调器子字段（PAN Coordinator Subfield）。

<a id="r_a4a6f895c5d3a86853647516d12073c32"></a>

```c
uint16_t reserved: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[reserved](#a4a6f895c5d3a86853647516d12073c32)。

保留字段（Reserved），应为0。

<a id="r_af57a9ae07bb6adb029be235929ed903b"></a>

```c
uint16_t ble: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ble](#af57a9ae07bb6adb029be235929ed903b)。

电池寿命扩展子字段（Battery Life Extension Subfield）。

<a id="r_ac1e5e4c10de0ef0bb22ff12a5097aed9"></a>

```c
uint16_t cap_slot: 4
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cap_slot](#ac1e5e4c10de0ef0bb22ff12a5097aed9)。

最终竞争接入时隙子字段（Final CAP Slot Subfield）。

## 8.2\_详细说明（Detailed Documentation）

<a id="a33a47bde19ad49508c981b1e7940ad93"></a>

### `association`

```c
uint16_t ieee802154_beacon_sf::association
```

允许关联子字段（Association Permit Subfield）。

<a id="aa3f402e1ac43b609a366f0a7c87195bd"></a>

### `bc_order`

```c
uint16_t ieee802154_beacon_sf::bc_order
```

信标阶数子字段（Beacon Order Subfield）。

<a id="af57a9ae07bb6adb029be235929ed903b"></a>

### `ble`

```c
uint16_t ieee802154_beacon_sf::ble
```

电池寿命扩展子字段（Battery Life Extension Subfield）。

<a id="ac1e5e4c10de0ef0bb22ff12a5097aed9"></a>

### `cap_slot`

```c
uint16_t ieee802154_beacon_sf::cap_slot
```

最终竞争接入时隙子字段（Final CAP Slot Subfield）。

<a id="a7f62606165bb7d2bd96cf0923de1326e"></a>

### `coordinator`

```c
uint16_t ieee802154_beacon_sf::coordinator
```

PAN协调器子字段（PAN Coordinator Subfield）。

<a id="a4a6f895c5d3a86853647516d12073c32"></a>

### `reserved`

```c
uint16_t ieee802154_beacon_sf::reserved
```

保留字段（Reserved），应为0。

<a id="aa52c67ce1c7607dfeabbfe5706a75bb8"></a>

### `sf_order`

```c
uint16_t ieee802154_beacon_sf::sf_order
```

超帧阶数子字段（Superframe Order Subfield）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_ieee802154_beacon_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_ieee802154_cmd_assoc_req_结构体.md)
