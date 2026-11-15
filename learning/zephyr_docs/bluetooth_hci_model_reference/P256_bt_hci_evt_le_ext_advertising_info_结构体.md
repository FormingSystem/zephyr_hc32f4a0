---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-256
title: bt_hci_evt_le_ext_advertising_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__ext__advertising__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第256章\_bt\_hci\_evt\_le\_ext\_advertising\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__ext__advertising__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 256.1\_数据成员（Data Fields）

<a id="r_a040c27dbcb337162f7ca857b8cb84cfe"></a>

```c
uint16_t evt_type
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[evt_type](#a040c27dbcb337162f7ca857b8cb84cfe)。

<a id="r_acec6858e41ae1b44a2a2ee6d6dbc294d"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#acec6858e41ae1b44a2a2ee6d6dbc294d)。

<a id="r_a088f0e6ea0dfbad25d5f72d0741f7d6d"></a>

```c
uint8_t prim_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prim_phy](#a088f0e6ea0dfbad25d5f72d0741f7d6d)。

<a id="r_af4d863e12e6f8f19426a14af292fa6d2"></a>

```c
uint8_t sec_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sec_phy](#af4d863e12e6f8f19426a14af292fa6d2)。

<a id="r_a5b4d4adff4d97c06311a76abd9847727"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#a5b4d4adff4d97c06311a76abd9847727)。

<a id="r_a39217e77e495e8c4c6288917f8e4d2dc"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#a39217e77e495e8c4c6288917f8e4d2dc)。

<a id="r_a6213edbc3ae30f02a6bf2d8e069cd035"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#a6213edbc3ae30f02a6bf2d8e069cd035)。

<a id="r_a7da4e49c49eccbf009491bb7da01e111"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a7da4e49c49eccbf009491bb7da01e111)。

<a id="r_a37f4e4981566b43d6e7c7dfffc5b13fb"></a>

```c
bt_addr_le_t direct_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[direct_addr](#a37f4e4981566b43d6e7c7dfffc5b13fb)。

<a id="r_a20ca10813f6b3aaba2756a5fe00d3878"></a>

```c
uint8_t length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[length](#a20ca10813f6b3aaba2756a5fe00d3878)。

<a id="r_a9e5536277b0132c8374147677a787b68"></a>

```c
uint8_t data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a9e5536277b0132c8374147677a787b68)。

## 256.2\_详细说明（Detailed Documentation）

<a id="acec6858e41ae1b44a2a2ee6d6dbc294d"></a>

### `addr`

```c
bt_addr_le_t bt_hci_evt_le_ext_advertising_info::addr
```

<a id="a9e5536277b0132c8374147677a787b68"></a>

### `data`

```c
uint8_t bt_hci_evt_le_ext_advertising_info::data[0]
```

<a id="a37f4e4981566b43d6e7c7dfffc5b13fb"></a>

### `direct_addr`

```c
bt_addr_le_t bt_hci_evt_le_ext_advertising_info::direct_addr
```

<a id="a040c27dbcb337162f7ca857b8cb84cfe"></a>

### `evt_type`

```c
uint16_t bt_hci_evt_le_ext_advertising_info::evt_type
```

<a id="a7da4e49c49eccbf009491bb7da01e111"></a>

### `interval`

```c
uint16_t bt_hci_evt_le_ext_advertising_info::interval
```

<a id="a20ca10813f6b3aaba2756a5fe00d3878"></a>

### `length`

```c
uint8_t bt_hci_evt_le_ext_advertising_info::length
```

<a id="a088f0e6ea0dfbad25d5f72d0741f7d6d"></a>

### `prim_phy`

```c
uint8_t bt_hci_evt_le_ext_advertising_info::prim_phy
```

<a id="a6213edbc3ae30f02a6bf2d8e069cd035"></a>

### `rssi`

```c
int8_t bt_hci_evt_le_ext_advertising_info::rssi
```

<a id="af4d863e12e6f8f19426a14af292fa6d2"></a>

### `sec_phy`

```c
uint8_t bt_hci_evt_le_ext_advertising_info::sec_phy
```

<a id="a5b4d4adff4d97c06311a76abd9847727"></a>

### `sid`

```c
uint8_t bt_hci_evt_le_ext_advertising_info::sid
```

<a id="a39217e77e495e8c4c6288917f8e4d2dc"></a>

### `tx_power`

```c
int8_t bt_hci_evt_le_ext_advertising_info::tx_power
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 256.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md) · [返回大纲](大纲.md) · [下一章](P257_bt_hci_evt_le_ext_advertising_report_结构体.md)
