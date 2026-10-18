---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-303
title: bt_hci_evt_vs_le_connection_iq_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__vs__le__connection__iq__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第303章\_bt\_hci\_evt\_vs\_le\_connection\_iq\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__vs__le__connection__iq__report.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 303.1\_数据成员（Data Fields）

<a id="r_a941d0e025334a0c041cc7a59b69f0af3"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#a941d0e025334a0c041cc7a59b69f0af3)。

<a id="r_a959c7e2b910aec90f8b186550cb7f4d8"></a>

```c
uint8_t rx_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_phy](#a959c7e2b910aec90f8b186550cb7f4d8)。

<a id="r_af634fa464d4ca435ea935ae58db86cfa"></a>

```c
uint8_t data_chan_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_chan_idx](#af634fa464d4ca435ea935ae58db86cfa)。

<a id="r_a87d4a6ebd1cc172816f3fe786c22f058"></a>

```c
int16_t rssi
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rssi](#a87d4a6ebd1cc172816f3fe786c22f058)。

<a id="r_a55a290121f661f155684d37fa0df77d2"></a>

```c
uint8_t rssi_ant_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rssi_ant_id](#a55a290121f661f155684d37fa0df77d2)。

<a id="r_ad714bb1f2292764eba9c506bcc72bccd"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#ad714bb1f2292764eba9c506bcc72bccd)。

<a id="r_a71227b896453143a6a4ad11b7e985a16"></a>

```c
uint8_t slot_durations
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[slot_durations](#a71227b896453143a6a4ad11b7e985a16)。

<a id="r_aa2a9c3589bf8e152627a79c17102ec7c"></a>

```c
uint8_t packet_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_status](#aa2a9c3589bf8e152627a79c17102ec7c)。

<a id="r_aaa29121a6b7fc8f9a76e6b83f6b80f4d"></a>

```c
uint16_t conn_evt_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_evt_counter](#aaa29121a6b7fc8f9a76e6b83f6b80f4d)。

<a id="r_ab96606229994abe966f03c65d57e5568"></a>

```c
uint8_t sample_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sample_count](#ab96606229994abe966f03c65d57e5568)。

<a id="r_abb2b6e915f8de6ad2013a79d0b4ee288"></a>

```c
struct bt_hci_le_iq_sample16 sample [0]
```

相关声明：[bt_hci_le_iq_sample16](P324_bt_hci_le_iq_sample16_结构体.md)、[sample](#abb2b6e915f8de6ad2013a79d0b4ee288)。

## 303.2\_详细说明（Detailed Documentation）

<a id="aaa29121a6b7fc8f9a76e6b83f6b80f4d"></a>

### `conn_evt_counter`

```c
uint16_t bt_hci_evt_vs_le_connection_iq_report::conn_evt_counter
```

<a id="a941d0e025334a0c041cc7a59b69f0af3"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_vs_le_connection_iq_report::conn_handle
```

<a id="ad714bb1f2292764eba9c506bcc72bccd"></a>

### `cte_type`

```c
uint8_t bt_hci_evt_vs_le_connection_iq_report::cte_type
```

<a id="af634fa464d4ca435ea935ae58db86cfa"></a>

### `data_chan_idx`

```c
uint8_t bt_hci_evt_vs_le_connection_iq_report::data_chan_idx
```

<a id="aa2a9c3589bf8e152627a79c17102ec7c"></a>

### `packet_status`

```c
uint8_t bt_hci_evt_vs_le_connection_iq_report::packet_status
```

<a id="a87d4a6ebd1cc172816f3fe786c22f058"></a>

### `rssi`

```c
int16_t bt_hci_evt_vs_le_connection_iq_report::rssi
```

<a id="a55a290121f661f155684d37fa0df77d2"></a>

### `rssi_ant_id`

```c
uint8_t bt_hci_evt_vs_le_connection_iq_report::rssi_ant_id
```

<a id="a959c7e2b910aec90f8b186550cb7f4d8"></a>

### `rx_phy`

```c
uint8_t bt_hci_evt_vs_le_connection_iq_report::rx_phy
```

<a id="abb2b6e915f8de6ad2013a79d0b4ee288"></a>

### `sample`

```c
struct bt_hci_le_iq_sample16 bt_hci_evt_vs_le_connection_iq_report::sample[0]
```

<a id="ab96606229994abe966f03c65d57e5568"></a>

### `sample_count`

```c
uint8_t bt_hci_evt_vs_le_connection_iq_report::sample_count
```

<a id="a71227b896453143a6a4ad11b7e985a16"></a>

### `slot_durations`

```c
uint8_t bt_hci_evt_vs_le_connection_iq_report::slot_durations
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 303.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_hci_le_iq_sample16](P324_bt_hci_le_iq_sample16_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P302_bt_hci_evt_vs_fatal_error_trace_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md)
