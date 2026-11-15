---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-142
title: bt_hci_cp_mesh_advertise_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__mesh__advertise.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第142章\_bt\_hci\_cp\_mesh\_advertise\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__mesh__advertise.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 142.1\_数据成员（Data Fields）

<a id="r_a7ec17216955ac784cd213b11038c3521"></a>

```c
uint8_t adv_slot
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_slot](#a7ec17216955ac784cd213b11038c3521)。

<a id="r_a6b6248069fa1e7eaf6825c52e38c3e78"></a>

```c
uint8_t own_addr_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[own_addr_type](#a6b6248069fa1e7eaf6825c52e38c3e78)。

<a id="r_a0b22a8e1109db932f86bb7312dfeca9e"></a>

```c
bt_addr_t random_addr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[random_addr](#a0b22a8e1109db932f86bb7312dfeca9e)。

<a id="r_a9ed6d2b96d9aa417ccd996e650bb00fa"></a>

```c
uint8_t ch_map
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch_map](#a9ed6d2b96d9aa417ccd996e650bb00fa)。

<a id="r_af1482ed0255e35d7a2016017dab8713a"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#af1482ed0255e35d7a2016017dab8713a)。

<a id="r_a6ac4b4dad0ce54e69afd2b8e1f6cdf4f"></a>

```c
uint8_t min_tx_delay
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_tx_delay](#a6ac4b4dad0ce54e69afd2b8e1f6cdf4f)。

<a id="r_a3cf773db54448d5f7b3da652a798c712"></a>

```c
uint8_t max_tx_delay
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_tx_delay](#a3cf773db54448d5f7b3da652a798c712)。

<a id="r_a5ea37039c817d58d13feb98d5658cbf1"></a>

```c
uint8_t retx_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retx_count](#a5ea37039c817d58d13feb98d5658cbf1)。

<a id="r_a46242ef61b79723e5136373fa534a292"></a>

```c
uint8_t retx_interval
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retx_interval](#a46242ef61b79723e5136373fa534a292)。

<a id="r_a278c21295c73947d7b0971a6ac043d62"></a>

```c
uint8_t scan_delay
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scan_delay](#a278c21295c73947d7b0971a6ac043d62)。

<a id="r_ab1b873984143301808f23824074e4df8"></a>

```c
uint16_t scan_duration
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[scan_duration](#ab1b873984143301808f23824074e4df8)。

<a id="r_a0b190fcabae8555e65a251b37ab5b232"></a>

```c
uint8_t scan_filter
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scan_filter](#a0b190fcabae8555e65a251b37ab5b232)。

<a id="r_a67aef4d217cb6b5762b4f823c8f234df"></a>

```c
uint8_t data_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_len](#a67aef4d217cb6b5762b4f823c8f234df)。

<a id="r_ad2af78fa8d14f1334b52f659f3497b4e"></a>

```c
uint8_t data [31]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ad2af78fa8d14f1334b52f659f3497b4e)。

## 142.2\_详细说明（Detailed Documentation）

<a id="a7ec17216955ac784cd213b11038c3521"></a>

### `adv_slot`

```c
uint8_t bt_hci_cp_mesh_advertise::adv_slot
```

<a id="a9ed6d2b96d9aa417ccd996e650bb00fa"></a>

### `ch_map`

```c
uint8_t bt_hci_cp_mesh_advertise::ch_map
```

<a id="ad2af78fa8d14f1334b52f659f3497b4e"></a>

### `data`

```c
uint8_t bt_hci_cp_mesh_advertise::data[31]
```

<a id="a67aef4d217cb6b5762b4f823c8f234df"></a>

### `data_len`

```c
uint8_t bt_hci_cp_mesh_advertise::data_len
```

<a id="a3cf773db54448d5f7b3da652a798c712"></a>

### `max_tx_delay`

```c
uint8_t bt_hci_cp_mesh_advertise::max_tx_delay
```

<a id="a6ac4b4dad0ce54e69afd2b8e1f6cdf4f"></a>

### `min_tx_delay`

```c
uint8_t bt_hci_cp_mesh_advertise::min_tx_delay
```

<a id="a6b6248069fa1e7eaf6825c52e38c3e78"></a>

### `own_addr_type`

```c
uint8_t bt_hci_cp_mesh_advertise::own_addr_type
```

<a id="a0b22a8e1109db932f86bb7312dfeca9e"></a>

### `random_addr`

```c
bt_addr_t bt_hci_cp_mesh_advertise::random_addr
```

<a id="a5ea37039c817d58d13feb98d5658cbf1"></a>

### `retx_count`

```c
uint8_t bt_hci_cp_mesh_advertise::retx_count
```

<a id="a46242ef61b79723e5136373fa534a292"></a>

### `retx_interval`

```c
uint8_t bt_hci_cp_mesh_advertise::retx_interval
```

<a id="a278c21295c73947d7b0971a6ac043d62"></a>

### `scan_delay`

```c
uint8_t bt_hci_cp_mesh_advertise::scan_delay
```

<a id="ab1b873984143301808f23824074e4df8"></a>

### `scan_duration`

```c
uint16_t bt_hci_cp_mesh_advertise::scan_duration
```

<a id="a0b190fcabae8555e65a251b37ab5b232"></a>

### `scan_filter`

```c
uint8_t bt_hci_cp_mesh_advertise::scan_filter
```

<a id="af1482ed0255e35d7a2016017dab8713a"></a>

### `tx_power`

```c
int8_t bt_hci_cp_mesh_advertise::tx_power
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 142.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P141_bt_hci_cp_mesh_结构体.md) · [返回大纲](大纲.md) · [下一章](P143_bt_hci_cp_mesh_advertise_cancel_结构体.md)
