---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-43
title: bt_hci_cp_le_ext_create_conn_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__ext__create__conn__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_bt\_hci\_cp\_le\_ext\_create\_conn\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__ext__create__conn__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_addf1f80c4d3625e0c6d6e716f6e2e207"></a>

```c
uint8_t adv_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_handle](#addf1f80c4d3625e0c6d6e716f6e2e207)。

<a id="r_a536da199958b3b54469f5b4b029e1bac"></a>

```c
uint8_t subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent](#a536da199958b3b54469f5b4b029e1bac)。

<a id="r_a66632dbac1605cff69e8da566e800347"></a>

```c
uint8_t filter_policy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter_policy](#a66632dbac1605cff69e8da566e800347)。

<a id="r_a05fd0089a0fd43f98042835231407a60"></a>

```c
uint8_t own_addr_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[own_addr_type](#a05fd0089a0fd43f98042835231407a60)。

<a id="r_a25466a04d224bdf495266b0064c424dd"></a>

```c
bt_addr_le_t peer_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer_addr](#a25466a04d224bdf495266b0064c424dd)。

<a id="r_ae2d3e3079a2848907224bb7ff0efc64b"></a>

```c
uint8_t phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phys](#ae2d3e3079a2848907224bb7ff0efc64b)。

<a id="r_a8d606c5aa480f54c8da9f42a35ad513e"></a>

```c
struct bt_hci_ext_conn_phy p [0]
```

相关声明：[bt_hci_ext_conn_phy](P308_bt_hci_ext_conn_phy_结构体.md)、[p](#a8d606c5aa480f54c8da9f42a35ad513e)。

## 43.2\_详细说明（Detailed Documentation）

<a id="addf1f80c4d3625e0c6d6e716f6e2e207"></a>

### `adv_handle`

```c
uint8_t bt_hci_cp_le_ext_create_conn_v2::adv_handle
```

<a id="a66632dbac1605cff69e8da566e800347"></a>

### `filter_policy`

```c
uint8_t bt_hci_cp_le_ext_create_conn_v2::filter_policy
```

<a id="a05fd0089a0fd43f98042835231407a60"></a>

### `own_addr_type`

```c
uint8_t bt_hci_cp_le_ext_create_conn_v2::own_addr_type
```

<a id="a8d606c5aa480f54c8da9f42a35ad513e"></a>

### `p`

```c
struct bt_hci_ext_conn_phy bt_hci_cp_le_ext_create_conn_v2::p[0]
```

<a id="a25466a04d224bdf495266b0064c424dd"></a>

### `peer_addr`

```c
bt_addr_le_t bt_hci_cp_le_ext_create_conn_v2::peer_addr
```

<a id="ae2d3e3079a2848907224bb7ff0efc64b"></a>

### `phys`

```c
uint8_t bt_hci_cp_le_ext_create_conn_v2::phys
```

<a id="a536da199958b3b54469f5b4b029e1bac"></a>

### `subevent`

```c
uint8_t bt_hci_cp_le_ext_create_conn_v2::subevent
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_hci_ext_conn_phy](P308_bt_hci_ext_conn_phy_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_bt_hci_cp_le_ext_create_conn_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_bt_hci_cp_le_frame_space_update_结构体.md)
