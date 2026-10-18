---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-238
title: bt_hci_evt_le_connection_iq_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__connection__iq__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第238章\_bt\_hci\_evt\_le\_connection\_iq\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__connection__iq__report.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 238.1\_数据成员（Data Fields）

<a id="r_a446f4eab3db19452a84023a676333d1d"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#a446f4eab3db19452a84023a676333d1d)。

<a id="r_aa052e03491647acc9f7a6dc7d91cedcc"></a>

```c
uint8_t rx_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_phy](#aa052e03491647acc9f7a6dc7d91cedcc)。

<a id="r_ac01a14c591c8bd8e6313aff021ca8d61"></a>

```c
uint8_t data_chan_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_chan_idx](#ac01a14c591c8bd8e6313aff021ca8d61)。

<a id="r_a49e63523f7219174540666c7e5ab3550"></a>

```c
int16_t rssi
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rssi](#a49e63523f7219174540666c7e5ab3550)。

<a id="r_a135498a4abae604967f94840e2f88d2c"></a>

```c
uint8_t rssi_ant_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rssi_ant_id](#a135498a4abae604967f94840e2f88d2c)。

<a id="r_a0188ce28a6c0a2002ae2c64a7bd95e52"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#a0188ce28a6c0a2002ae2c64a7bd95e52)。

<a id="r_a74670ca77bb2be81db2cee613dd9c82b"></a>

```c
uint8_t slot_durations
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[slot_durations](#a74670ca77bb2be81db2cee613dd9c82b)。

<a id="r_af66e8f09a4442b658b80a6eb4dd3064b"></a>

```c
uint8_t packet_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_status](#af66e8f09a4442b658b80a6eb4dd3064b)。

<a id="r_a1f388ba96bd52f9ce0f68bacb2945ed8"></a>

```c
uint16_t conn_evt_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_evt_counter](#a1f388ba96bd52f9ce0f68bacb2945ed8)。

<a id="r_a801dd9373935ba06175ac52237fea759"></a>

```c
uint8_t sample_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sample_count](#a801dd9373935ba06175ac52237fea759)。

<a id="r_a5acc2683312523a1137db7897a7373a6"></a>

```c
struct bt_hci_le_iq_sample sample [0]
```

相关声明：[bt_hci_le_iq_sample](P323_bt_hci_le_iq_sample_结构体.md)、[sample](#a5acc2683312523a1137db7897a7373a6)。

## 238.2\_详细说明（Detailed Documentation）

<a id="a1f388ba96bd52f9ce0f68bacb2945ed8"></a>

### `conn_evt_counter`

```c
uint16_t bt_hci_evt_le_connection_iq_report::conn_evt_counter
```

<a id="a446f4eab3db19452a84023a676333d1d"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_le_connection_iq_report::conn_handle
```

<a id="a0188ce28a6c0a2002ae2c64a7bd95e52"></a>

### `cte_type`

```c
uint8_t bt_hci_evt_le_connection_iq_report::cte_type
```

<a id="ac01a14c591c8bd8e6313aff021ca8d61"></a>

### `data_chan_idx`

```c
uint8_t bt_hci_evt_le_connection_iq_report::data_chan_idx
```

<a id="af66e8f09a4442b658b80a6eb4dd3064b"></a>

### `packet_status`

```c
uint8_t bt_hci_evt_le_connection_iq_report::packet_status
```

<a id="a49e63523f7219174540666c7e5ab3550"></a>

### `rssi`

```c
int16_t bt_hci_evt_le_connection_iq_report::rssi
```

<a id="a135498a4abae604967f94840e2f88d2c"></a>

### `rssi_ant_id`

```c
uint8_t bt_hci_evt_le_connection_iq_report::rssi_ant_id
```

<a id="aa052e03491647acc9f7a6dc7d91cedcc"></a>

### `rx_phy`

```c
uint8_t bt_hci_evt_le_connection_iq_report::rx_phy
```

<a id="a5acc2683312523a1137db7897a7373a6"></a>

### `sample`

```c
struct bt_hci_le_iq_sample bt_hci_evt_le_connection_iq_report::sample[0]
```

<a id="a801dd9373935ba06175ac52237fea759"></a>

### `sample_count`

```c
uint8_t bt_hci_evt_le_connection_iq_report::sample_count
```

<a id="a74670ca77bb2be81db2cee613dd9c82b"></a>

### `slot_durations`

```c
uint8_t bt_hci_evt_le_connection_iq_report::slot_durations
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 238.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_hci_le_iq_sample](P323_bt_hci_le_iq_sample_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P237_bt_hci_evt_le_conn_update_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P239_bt_hci_evt_le_connectionless_iq_report_结构体.md)
