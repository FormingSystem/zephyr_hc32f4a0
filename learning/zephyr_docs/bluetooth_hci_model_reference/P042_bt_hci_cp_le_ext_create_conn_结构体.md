---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-42
title: bt_hci_cp_le_ext_create_conn_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__ext__create__conn.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_bt\_hci\_cp\_le\_ext\_create\_conn\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__ext__create__conn.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_a0561b446effa3f735a405c0b307466bf"></a>

```c
uint8_t filter_policy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter_policy](#a0561b446effa3f735a405c0b307466bf)。

<a id="r_a12a99044f54e3d5dae30a64392444cbf"></a>

```c
uint8_t own_addr_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[own_addr_type](#a12a99044f54e3d5dae30a64392444cbf)。

<a id="r_a79bc55d9f5b1d719de4fb404db9008f3"></a>

```c
bt_addr_le_t peer_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer_addr](#a79bc55d9f5b1d719de4fb404db9008f3)。

<a id="r_ae859ff0da5e9cdc872943fd74774ef7e"></a>

```c
uint8_t phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phys](#ae859ff0da5e9cdc872943fd74774ef7e)。

<a id="r_acdb436d6bf2864745ec579622ae0d532"></a>

```c
struct bt_hci_ext_conn_phy p [0]
```

相关声明：[bt_hci_ext_conn_phy](P308_bt_hci_ext_conn_phy_结构体.md)、[p](#acdb436d6bf2864745ec579622ae0d532)。

## 42.2\_详细说明（Detailed Documentation）

<a id="a0561b446effa3f735a405c0b307466bf"></a>

### `filter_policy`

```c
uint8_t bt_hci_cp_le_ext_create_conn::filter_policy
```

<a id="a12a99044f54e3d5dae30a64392444cbf"></a>

### `own_addr_type`

```c
uint8_t bt_hci_cp_le_ext_create_conn::own_addr_type
```

<a id="acdb436d6bf2864745ec579622ae0d532"></a>

### `p`

```c
struct bt_hci_ext_conn_phy bt_hci_cp_le_ext_create_conn::p[0]
```

<a id="a79bc55d9f5b1d719de4fb404db9008f3"></a>

### `peer_addr`

```c
bt_addr_le_t bt_hci_cp_le_ext_create_conn::peer_addr
```

<a id="ae859ff0da5e9cdc872943fd74774ef7e"></a>

### `phys`

```c
uint8_t bt_hci_cp_le_ext_create_conn::phys
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_hci_ext_conn_phy](P308_bt_hci_ext_conn_phy_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_bt_hci_cp_le_enh_tx_test_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md)
