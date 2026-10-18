---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-239
title: bt_hci_evt_le_connectionless_iq_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__connectionless__iq__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第239章\_bt\_hci\_evt\_le\_connectionless\_iq\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__connectionless__iq__report.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 239.1\_数据成员（Data Fields）

<a id="r_a36f853d29b8dae1dd393546bbdec5ae2"></a>

```c
uint16_t sync_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_handle](#a36f853d29b8dae1dd393546bbdec5ae2)。

<a id="r_af50e710884a17191d22f652eaf5788fd"></a>

```c
uint8_t chan_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[chan_idx](#af50e710884a17191d22f652eaf5788fd)。

<a id="r_a09112f3711aca00b56045c46958c0992"></a>

```c
int16_t rssi
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rssi](#a09112f3711aca00b56045c46958c0992)。

<a id="r_af8c2055666a97f3c8d95747c59515c31"></a>

```c
uint8_t rssi_ant_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rssi_ant_id](#af8c2055666a97f3c8d95747c59515c31)。

<a id="r_a6b11b00199b002129c569cfec6e83174"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#a6b11b00199b002129c569cfec6e83174)。

<a id="r_a9d9f0cfe343d81c44e8342b81e2a0608"></a>

```c
uint8_t slot_durations
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[slot_durations](#a9d9f0cfe343d81c44e8342b81e2a0608)。

<a id="r_ab6fb0f6e32e32a3364ae79d867d9e640"></a>

```c
uint8_t packet_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[packet_status](#ab6fb0f6e32e32a3364ae79d867d9e640)。

<a id="r_abfeb0aaa411464bbd7bca927219144fb"></a>

```c
uint16_t per_evt_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[per_evt_counter](#abfeb0aaa411464bbd7bca927219144fb)。

<a id="r_a39109ea3f657d0566a73c7ca81bdd2b1"></a>

```c
uint8_t sample_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sample_count](#a39109ea3f657d0566a73c7ca81bdd2b1)。

<a id="r_a1a81f2c8653d85dc29582eed67b4a2a8"></a>

```c
struct bt_hci_le_iq_sample sample [0]
```

相关声明：[bt_hci_le_iq_sample](P323_bt_hci_le_iq_sample_结构体.md)、[sample](#a1a81f2c8653d85dc29582eed67b4a2a8)。

## 239.2\_详细说明（Detailed Documentation）

<a id="af50e710884a17191d22f652eaf5788fd"></a>

### `chan_idx`

```c
uint8_t bt_hci_evt_le_connectionless_iq_report::chan_idx
```

<a id="a6b11b00199b002129c569cfec6e83174"></a>

### `cte_type`

```c
uint8_t bt_hci_evt_le_connectionless_iq_report::cte_type
```

<a id="ab6fb0f6e32e32a3364ae79d867d9e640"></a>

### `packet_status`

```c
uint8_t bt_hci_evt_le_connectionless_iq_report::packet_status
```

<a id="abfeb0aaa411464bbd7bca927219144fb"></a>

### `per_evt_counter`

```c
uint16_t bt_hci_evt_le_connectionless_iq_report::per_evt_counter
```

<a id="a09112f3711aca00b56045c46958c0992"></a>

### `rssi`

```c
int16_t bt_hci_evt_le_connectionless_iq_report::rssi
```

<a id="af8c2055666a97f3c8d95747c59515c31"></a>

### `rssi_ant_id`

```c
uint8_t bt_hci_evt_le_connectionless_iq_report::rssi_ant_id
```

<a id="a1a81f2c8653d85dc29582eed67b4a2a8"></a>

### `sample`

```c
struct bt_hci_le_iq_sample bt_hci_evt_le_connectionless_iq_report::sample[0]
```

<a id="a39109ea3f657d0566a73c7ca81bdd2b1"></a>

### `sample_count`

```c
uint8_t bt_hci_evt_le_connectionless_iq_report::sample_count
```

<a id="a9d9f0cfe343d81c44e8342b81e2a0608"></a>

### `slot_durations`

```c
uint8_t bt_hci_evt_le_connectionless_iq_report::slot_durations
```

<a id="a36f853d29b8dae1dd393546bbdec5ae2"></a>

### `sync_handle`

```c
uint16_t bt_hci_evt_le_connectionless_iq_report::sync_handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 239.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_hci_le_iq_sample](P323_bt_hci_le_iq_sample_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P238_bt_hci_evt_le_connection_iq_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P240_bt_hci_evt_le_cs_config_complete_结构体.md)
