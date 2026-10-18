---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-304
title: bt_hci_evt_vs_le_connectionless_iq_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__vs__le__connectionless__iq__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第304章\_bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__vs__le__connectionless__iq__report.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 304.1\_数据成员（Data Fields）

<a id="r_a9c199121ac475d635fc51289e8eba979"></a>

```c
uint16_t sync_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_handle](#a9c199121ac475d635fc51289e8eba979)。

<a id="r_ad15beccc7c2207565678ebef72346158"></a>

```c
uint8_t chan_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[chan_idx](#ad15beccc7c2207565678ebef72346158)。

<a id="r_a9b7eb8a5cf363c3aec96b49853056dc7"></a>

```c
int16_t rssi
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rssi](#a9b7eb8a5cf363c3aec96b49853056dc7)。

<a id="r_a5fcd776dce904763c5cc6fab9a1373f4"></a>

```c
uint8_t rssi_ant_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rssi_ant_id](#a5fcd776dce904763c5cc6fab9a1373f4)。

<a id="r_a808a2a134104c69073af253a3c4dd1bd"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#a808a2a134104c69073af253a3c4dd1bd)。

<a id="r_ac0b077d7b5e2b7c5ce61b3060913cad5"></a>

```c
uint8_t slot_durations
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[slot_durations](#ac0b077d7b5e2b7c5ce61b3060913cad5)。

<a id="r_af5b27c1504ce4ff8afe23c28a9ac423f"></a>

```c
uint8_t packet_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_status](#af5b27c1504ce4ff8afe23c28a9ac423f)。

<a id="r_ab6911af90d85c565615c437715d9c7eb"></a>

```c
uint16_t per_evt_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[per_evt_counter](#ab6911af90d85c565615c437715d9c7eb)。

<a id="r_a2698510deb6bd8943bf57104f96673db"></a>

```c
uint8_t sample_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sample_count](#a2698510deb6bd8943bf57104f96673db)。

<a id="r_a17c9d19883c9d8e34f300fbff614b475"></a>

```c
struct bt_hci_le_iq_sample16 sample [0]
```

相关声明：[bt_hci_le_iq_sample16](P324_bt_hci_le_iq_sample16_结构体.md)、[sample](#a17c9d19883c9d8e34f300fbff614b475)。

## 304.2\_详细说明（Detailed Documentation）

<a id="ad15beccc7c2207565678ebef72346158"></a>

### `chan_idx`

```c
uint8_t bt_hci_evt_vs_le_connectionless_iq_report::chan_idx
```

<a id="a808a2a134104c69073af253a3c4dd1bd"></a>

### `cte_type`

```c
uint8_t bt_hci_evt_vs_le_connectionless_iq_report::cte_type
```

<a id="af5b27c1504ce4ff8afe23c28a9ac423f"></a>

### `packet_status`

```c
uint8_t bt_hci_evt_vs_le_connectionless_iq_report::packet_status
```

<a id="ab6911af90d85c565615c437715d9c7eb"></a>

### `per_evt_counter`

```c
uint16_t bt_hci_evt_vs_le_connectionless_iq_report::per_evt_counter
```

<a id="a9b7eb8a5cf363c3aec96b49853056dc7"></a>

### `rssi`

```c
int16_t bt_hci_evt_vs_le_connectionless_iq_report::rssi
```

<a id="a5fcd776dce904763c5cc6fab9a1373f4"></a>

### `rssi_ant_id`

```c
uint8_t bt_hci_evt_vs_le_connectionless_iq_report::rssi_ant_id
```

<a id="a17c9d19883c9d8e34f300fbff614b475"></a>

### `sample`

```c
struct bt_hci_le_iq_sample16 bt_hci_evt_vs_le_connectionless_iq_report::sample[0]
```

<a id="a2698510deb6bd8943bf57104f96673db"></a>

### `sample_count`

```c
uint8_t bt_hci_evt_vs_le_connectionless_iq_report::sample_count
```

<a id="ac0b077d7b5e2b7c5ce61b3060913cad5"></a>

### `slot_durations`

```c
uint8_t bt_hci_evt_vs_le_connectionless_iq_report::slot_durations
```

<a id="a9c199121ac475d635fc51289e8eba979"></a>

### `sync_handle`

```c
uint16_t bt_hci_evt_vs_le_connectionless_iq_report::sync_handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 304.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_hci_le_iq_sample16](P324_bt_hci_le_iq_sample16_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P305_bt_hci_evt_vs_scan_req_rx_结构体.md)
