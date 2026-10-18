---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-252
title: bt_hci_evt_le_direct_adv_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__direct__adv__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第252章\_bt\_hci\_evt\_le\_direct\_adv\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__direct__adv__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 252.1\_数据成员（Data Fields）

<a id="r_aed957c96860c5f92f9485ab743ce832b"></a>

```c
uint8_t evt_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[evt_type](#aed957c96860c5f92f9485ab743ce832b)。

<a id="r_a66bbb3e53d84e8c39b216edf91ad131d"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a66bbb3e53d84e8c39b216edf91ad131d)。

<a id="r_ad4ca2d5395bc4c5b95527ac1491c940e"></a>

```c
bt_addr_le_t dir_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[dir_addr](#ad4ca2d5395bc4c5b95527ac1491c940e)。

<a id="r_a013e5d53ed53e4cd0b923a55c68e20bc"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#a013e5d53ed53e4cd0b923a55c68e20bc)。

## 252.2\_详细说明（Detailed Documentation）

<a id="a66bbb3e53d84e8c39b216edf91ad131d"></a>

### `addr`

```c
bt_addr_le_t bt_hci_evt_le_direct_adv_info::addr
```

<a id="ad4ca2d5395bc4c5b95527ac1491c940e"></a>

### `dir_addr`

```c
bt_addr_le_t bt_hci_evt_le_direct_adv_info::dir_addr
```

<a id="aed957c96860c5f92f9485ab743ce832b"></a>

### `evt_type`

```c
uint8_t bt_hci_evt_le_direct_adv_info::evt_type
```

<a id="a013e5d53ed53e4cd0b923a55c68e20bc"></a>

### `rssi`

```c
int8_t bt_hci_evt_le_direct_adv_info::rssi
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 252.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P251_bt_hci_evt_le_data_len_change_结构体.md) · [返回大纲](大纲.md) · [下一章](P253_bt_hci_evt_le_direct_adv_report_结构体.md)
