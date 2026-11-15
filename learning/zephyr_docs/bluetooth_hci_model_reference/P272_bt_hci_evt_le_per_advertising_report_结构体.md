---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-272
title: bt_hci_evt_le_per_advertising_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__advertising__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第272章\_bt\_hci\_evt\_le\_per\_advertising\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__advertising__report.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 272.1\_数据成员（Data Fields）

<a id="r_af81ce5bb18ef7fa1d94d00412886b081"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#af81ce5bb18ef7fa1d94d00412886b081)。

<a id="r_a3a09aca94284a9e4af765d4da543698e"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#a3a09aca94284a9e4af765d4da543698e)。

<a id="r_af874c29b89326877b499f6be1052a626"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#af874c29b89326877b499f6be1052a626)。

<a id="r_aa683d1a4bd3a851f26b3028f566b76e4"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#aa683d1a4bd3a851f26b3028f566b76e4)。

<a id="r_abf23b23a12cbfeb7f996e71e2fe8b11c"></a>

```c
uint8_t data_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_status](#abf23b23a12cbfeb7f996e71e2fe8b11c)。

<a id="r_a0ab1d3c5d7eb1487862451cc65c66a76"></a>

```c
uint8_t length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[length](#a0ab1d3c5d7eb1487862451cc65c66a76)。

<a id="r_a1f9cdfc01e46e59e957b0c557bae620a"></a>

```c
uint8_t data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a1f9cdfc01e46e59e957b0c557bae620a)。

## 272.2\_详细说明（Detailed Documentation）

<a id="aa683d1a4bd3a851f26b3028f566b76e4"></a>

### `cte_type`

```c
uint8_t bt_hci_evt_le_per_advertising_report::cte_type
```

<a id="a1f9cdfc01e46e59e957b0c557bae620a"></a>

### `data`

```c
uint8_t bt_hci_evt_le_per_advertising_report::data[0]
```

<a id="abf23b23a12cbfeb7f996e71e2fe8b11c"></a>

### `data_status`

```c
uint8_t bt_hci_evt_le_per_advertising_report::data_status
```

<a id="af81ce5bb18ef7fa1d94d00412886b081"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_per_advertising_report::handle
```

<a id="a0ab1d3c5d7eb1487862451cc65c66a76"></a>

### `length`

```c
uint8_t bt_hci_evt_le_per_advertising_report::length
```

<a id="af874c29b89326877b499f6be1052a626"></a>

### `rssi`

```c
int8_t bt_hci_evt_le_per_advertising_report::rssi
```

<a id="a3a09aca94284a9e4af765d4da543698e"></a>

### `tx_power`

```c
int8_t bt_hci_evt_le_per_advertising_report::tx_power
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 272.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P271_bt_hci_evt_le_per_adv_sync_lost_结构体.md) · [返回大纲](大纲.md) · [下一章](P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md)
