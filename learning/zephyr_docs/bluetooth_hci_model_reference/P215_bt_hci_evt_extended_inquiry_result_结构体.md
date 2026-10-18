---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-215
title: bt_hci_evt_extended_inquiry_result_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__extended__inquiry__result.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第215章\_bt\_hci\_evt\_extended\_inquiry\_result\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__extended__inquiry__result.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 215.1\_数据成员（Data Fields）

<a id="r_a76e4e82d1dedaee94bd730a4134d7d77"></a>

```c
uint8_t num_reports
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_reports](#a76e4e82d1dedaee94bd730a4134d7d77)。

<a id="r_a955a7d36736badfae1f39fa9eda61ebb"></a>

```c
bt_addr_t addr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[addr](#a955a7d36736badfae1f39fa9eda61ebb)。

<a id="r_aba4aac84e23ca9d283cb8af265dcaf0d"></a>

```c
uint8_t pscan_rep_mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pscan_rep_mode](#aba4aac84e23ca9d283cb8af265dcaf0d)。

<a id="r_ab6ec4b5efe058e225d173cbda9a16f2e"></a>

```c
uint8_t reserved
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved](#ab6ec4b5efe058e225d173cbda9a16f2e)。

<a id="r_ab4ebcf09817827d1d10ddeee13832759"></a>

```c
uint8_t cod [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cod](#ab4ebcf09817827d1d10ddeee13832759)。

<a id="r_a30c5586d954585006238e8c2b33a7601"></a>

```c
uint16_t clock_offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[clock_offset](#a30c5586d954585006238e8c2b33a7601)。

<a id="r_a21f7f48422bcfb867c9ca2e4411a2fbd"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#a21f7f48422bcfb867c9ca2e4411a2fbd)。

<a id="r_a1eba2841941f7cdbb00f548ebf0485e9"></a>

```c
uint8_t eir [240]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[eir](#a1eba2841941f7cdbb00f548ebf0485e9)。

## 215.2\_详细说明（Detailed Documentation）

<a id="a955a7d36736badfae1f39fa9eda61ebb"></a>

### `addr`

```c
bt_addr_t bt_hci_evt_extended_inquiry_result::addr
```

<a id="a30c5586d954585006238e8c2b33a7601"></a>

### `clock_offset`

```c
uint16_t bt_hci_evt_extended_inquiry_result::clock_offset
```

<a id="ab4ebcf09817827d1d10ddeee13832759"></a>

### `cod`

```c
uint8_t bt_hci_evt_extended_inquiry_result::cod[3]
```

<a id="a1eba2841941f7cdbb00f548ebf0485e9"></a>

### `eir`

```c
uint8_t bt_hci_evt_extended_inquiry_result::eir[240]
```

<a id="a76e4e82d1dedaee94bd730a4134d7d77"></a>

### `num_reports`

```c
uint8_t bt_hci_evt_extended_inquiry_result::num_reports
```

<a id="aba4aac84e23ca9d283cb8af265dcaf0d"></a>

### `pscan_rep_mode`

```c
uint8_t bt_hci_evt_extended_inquiry_result::pscan_rep_mode
```

<a id="ab6ec4b5efe058e225d173cbda9a16f2e"></a>

### `reserved`

```c
uint8_t bt_hci_evt_extended_inquiry_result::reserved
```

<a id="a21f7f48422bcfb867c9ca2e4411a2fbd"></a>

### `rssi`

```c
int8_t bt_hci_evt_extended_inquiry_result::rssi
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 215.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P214_bt_hci_evt_encrypt_key_refresh_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P216_bt_hci_evt_hardware_error_结构体.md)
