---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-273
title: bt_hci_evt_le_per_advertising_report_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__advertising__report__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第273章\_bt\_hci\_evt\_le\_per\_advertising\_report\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__advertising__report__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 273.1\_数据成员（Data Fields）

<a id="r_a34b15fb9b5b4f0d199ccf274dd489c6a"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a34b15fb9b5b4f0d199ccf274dd489c6a)。

<a id="r_a37a9eb7d417da9285e22cc7f83071c69"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#a37a9eb7d417da9285e22cc7f83071c69)。

<a id="r_ad598ffd0108825803a4734959a354bd8"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#ad598ffd0108825803a4734959a354bd8)。

<a id="r_a3276c2e11c946744b73426f54bf62b8c"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#a3276c2e11c946744b73426f54bf62b8c)。

<a id="r_a499d82e1e3cfc501d399f570ebbcdc42"></a>

```c
uint16_t periodic_event_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[periodic_event_counter](#a499d82e1e3cfc501d399f570ebbcdc42)。

<a id="r_af27b23fe38e9ff092d8839cd81749456"></a>

```c
uint8_t subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent](#af27b23fe38e9ff092d8839cd81749456)。

<a id="r_a73496cc962721538e27e9924fff0f3db"></a>

```c
uint8_t data_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_status](#a73496cc962721538e27e9924fff0f3db)。

<a id="r_a30f4e81346957ad4f9f0488dd93fafc3"></a>

```c
uint8_t length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[length](#a30f4e81346957ad4f9f0488dd93fafc3)。

<a id="r_a7af1cd4ec9df24e575a83a640eea36d2"></a>

```c
uint8_t data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a7af1cd4ec9df24e575a83a640eea36d2)。

## 273.2\_详细说明（Detailed Documentation）

<a id="a3276c2e11c946744b73426f54bf62b8c"></a>

### `cte_type`

```c
uint8_t bt_hci_evt_le_per_advertising_report_v2::cte_type
```

<a id="a7af1cd4ec9df24e575a83a640eea36d2"></a>

### `data`

```c
uint8_t bt_hci_evt_le_per_advertising_report_v2::data[0]
```

<a id="a73496cc962721538e27e9924fff0f3db"></a>

### `data_status`

```c
uint8_t bt_hci_evt_le_per_advertising_report_v2::data_status
```

<a id="a34b15fb9b5b4f0d199ccf274dd489c6a"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_per_advertising_report_v2::handle
```

<a id="a30f4e81346957ad4f9f0488dd93fafc3"></a>

### `length`

```c
uint8_t bt_hci_evt_le_per_advertising_report_v2::length
```

<a id="a499d82e1e3cfc501d399f570ebbcdc42"></a>

### `periodic_event_counter`

```c
uint16_t bt_hci_evt_le_per_advertising_report_v2::periodic_event_counter
```

<a id="ad598ffd0108825803a4734959a354bd8"></a>

### `rssi`

```c
int8_t bt_hci_evt_le_per_advertising_report_v2::rssi
```

<a id="af27b23fe38e9ff092d8839cd81749456"></a>

### `subevent`

```c
uint8_t bt_hci_evt_le_per_advertising_report_v2::subevent
```

<a id="a37a9eb7d417da9285e22cc7f83071c69"></a>

### `tx_power`

```c
int8_t bt_hci_evt_le_per_advertising_report_v2::tx_power
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 273.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P272_bt_hci_evt_le_per_advertising_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P274_bt_hci_evt_le_phy_update_complete_结构体.md)
