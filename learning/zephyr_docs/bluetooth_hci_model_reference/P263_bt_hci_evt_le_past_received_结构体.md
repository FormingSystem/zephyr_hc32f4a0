---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-263
title: bt_hci_evt_le_past_received_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__past__received.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第263章\_bt\_hci\_evt\_le\_past\_received\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__past__received.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 263.1\_数据成员（Data Fields）

<a id="r_a1b2c229c99d06f44057b88458f168e7c"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a1b2c229c99d06f44057b88458f168e7c)。

<a id="r_a1bdbaddb4003cea40738ee540ecb8789"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#a1bdbaddb4003cea40738ee540ecb8789)。

<a id="r_adaa1e432db60a2529ad6266f16604e15"></a>

```c
uint16_t service_data
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[service_data](#adaa1e432db60a2529ad6266f16604e15)。

<a id="r_a2cea2f3b9d51ace91ddf63639e821328"></a>

```c
uint16_t sync_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_handle](#a2cea2f3b9d51ace91ddf63639e821328)。

<a id="r_a110c7cdd2ff1178d1ca686abaae92b05"></a>

```c
uint8_t adv_sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_sid](#a110c7cdd2ff1178d1ca686abaae92b05)。

<a id="r_a3e368e95a6831f823d2efa0c0bc1ef51"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a3e368e95a6831f823d2efa0c0bc1ef51)。

<a id="r_aedb668e6f3232b1db9035ea89ccf1b71"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#aedb668e6f3232b1db9035ea89ccf1b71)。

<a id="r_a41ea6099d3cca1caf37ff518a4e95492"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a41ea6099d3cca1caf37ff518a4e95492)。

<a id="r_a00d570636a55c1d84723ad3bc5705d80"></a>

```c
uint8_t clock_accuracy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clock_accuracy](#a00d570636a55c1d84723ad3bc5705d80)。

## 263.2\_详细说明（Detailed Documentation）

<a id="a3e368e95a6831f823d2efa0c0bc1ef51"></a>

### `addr`

```c
bt_addr_le_t bt_hci_evt_le_past_received::addr
```

<a id="a110c7cdd2ff1178d1ca686abaae92b05"></a>

### `adv_sid`

```c
uint8_t bt_hci_evt_le_past_received::adv_sid
```

<a id="a00d570636a55c1d84723ad3bc5705d80"></a>

### `clock_accuracy`

```c
uint8_t bt_hci_evt_le_past_received::clock_accuracy
```

<a id="a1bdbaddb4003cea40738ee540ecb8789"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_le_past_received::conn_handle
```

<a id="a41ea6099d3cca1caf37ff518a4e95492"></a>

### `interval`

```c
uint16_t bt_hci_evt_le_past_received::interval
```

<a id="aedb668e6f3232b1db9035ea89ccf1b71"></a>

### `phy`

```c
uint8_t bt_hci_evt_le_past_received::phy
```

<a id="adaa1e432db60a2529ad6266f16604e15"></a>

### `service_data`

```c
uint16_t bt_hci_evt_le_past_received::service_data
```

<a id="a1b2c229c99d06f44057b88458f168e7c"></a>

### `status`

```c
uint8_t bt_hci_evt_le_past_received::status
```

<a id="a2cea2f3b9d51ace91ddf63639e821328"></a>

### `sync_handle`

```c
uint16_t bt_hci_evt_le_past_received::sync_handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 263.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P262_bt_hci_evt_le_p256_public_key_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P264_bt_hci_evt_le_past_received_v2_结构体.md)
