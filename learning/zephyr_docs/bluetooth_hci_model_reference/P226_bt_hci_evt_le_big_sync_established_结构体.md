---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-226
title: bt_hci_evt_le_big_sync_established_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__big__sync__established.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第226章\_bt\_hci\_evt\_le\_big\_sync\_established\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__big__sync__established.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 226.1\_数据成员（Data Fields）

<a id="r_a8feb21ef6eacf45dfc09b09e0bce04b1"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a8feb21ef6eacf45dfc09b09e0bce04b1)。

<a id="r_a31a05f8afb69e5885700cc4ad3b161b2"></a>

```c
uint8_t big_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[big_handle](#a31a05f8afb69e5885700cc4ad3b161b2)。

<a id="r_aebb25f9a63fa013ec6ef891ca498dbb4"></a>

```c
uint8_t latency [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[latency](#aebb25f9a63fa013ec6ef891ca498dbb4)。

<a id="r_a383dc92f6d16ec971455e20665cd7496"></a>

```c
uint8_t nse
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nse](#a383dc92f6d16ec971455e20665cd7496)。

<a id="r_a451466916fbe2f220c277b4b4e62241d"></a>

```c
uint8_t bn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bn](#a451466916fbe2f220c277b4b4e62241d)。

<a id="r_a6b750de25b2a1afc38995030953364ce"></a>

```c
uint8_t pto
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pto](#a6b750de25b2a1afc38995030953364ce)。

<a id="r_afd52315dafe02ee28bc26f058b12fe9e"></a>

```c
uint8_t irc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[irc](#afd52315dafe02ee28bc26f058b12fe9e)。

<a id="r_a13db0d402636a71ed029575c1e5771c5"></a>

```c
uint16_t max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_pdu](#a13db0d402636a71ed029575c1e5771c5)。

<a id="r_a610313c11c65faf82e06a121affb8b2b"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#a610313c11c65faf82e06a121affb8b2b)。

<a id="r_a2fa405310a8fed0341001b316ca7bd4f"></a>

```c
uint8_t num_bis
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_bis](#a2fa405310a8fed0341001b316ca7bd4f)。

<a id="r_a48766968cb677614f525ea36551ad6c8"></a>

```c
uint16_t handle [0]
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a48766968cb677614f525ea36551ad6c8)。

## 226.2\_详细说明（Detailed Documentation）

<a id="a31a05f8afb69e5885700cc4ad3b161b2"></a>

### `big_handle`

```c
uint8_t bt_hci_evt_le_big_sync_established::big_handle
```

<a id="a451466916fbe2f220c277b4b4e62241d"></a>

### `bn`

```c
uint8_t bt_hci_evt_le_big_sync_established::bn
```

<a id="a48766968cb677614f525ea36551ad6c8"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_big_sync_established::handle[0]
```

<a id="afd52315dafe02ee28bc26f058b12fe9e"></a>

### `irc`

```c
uint8_t bt_hci_evt_le_big_sync_established::irc
```

<a id="a610313c11c65faf82e06a121affb8b2b"></a>

### `iso_interval`

```c
uint16_t bt_hci_evt_le_big_sync_established::iso_interval
```

<a id="aebb25f9a63fa013ec6ef891ca498dbb4"></a>

### `latency`

```c
uint8_t bt_hci_evt_le_big_sync_established::latency[3]
```

<a id="a13db0d402636a71ed029575c1e5771c5"></a>

### `max_pdu`

```c
uint16_t bt_hci_evt_le_big_sync_established::max_pdu
```

<a id="a383dc92f6d16ec971455e20665cd7496"></a>

### `nse`

```c
uint8_t bt_hci_evt_le_big_sync_established::nse
```

<a id="a2fa405310a8fed0341001b316ca7bd4f"></a>

### `num_bis`

```c
uint8_t bt_hci_evt_le_big_sync_established::num_bis
```

<a id="a6b750de25b2a1afc38995030953364ce"></a>

### `pto`

```c
uint8_t bt_hci_evt_le_big_sync_established::pto
```

<a id="a8feb21ef6eacf45dfc09b09e0bce04b1"></a>

### `status`

```c
uint8_t bt_hci_evt_le_big_sync_established::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 226.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P225_bt_hci_evt_le_big_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P227_bt_hci_evt_le_big_sync_lost_结构体.md)
