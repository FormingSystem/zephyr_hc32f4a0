---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-264
title: bt_hci_evt_le_past_received_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__past__received__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第264章\_bt\_hci\_evt\_le\_past\_received\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__past__received__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 264.1\_数据成员（Data Fields）

<a id="r_aefe79f973eda8c7c5670c7a721d55d8a"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#aefe79f973eda8c7c5670c7a721d55d8a)。

<a id="r_adb011949f592ec7f8843d4fd47eca2e9"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#adb011949f592ec7f8843d4fd47eca2e9)。

<a id="r_acffc2fa22a16a3a12a4f7dfc3bb45866"></a>

```c
uint16_t service_data
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[service_data](#acffc2fa22a16a3a12a4f7dfc3bb45866)。

<a id="r_a00bf4bdf12fce6cbf2874b9c4ae09f9f"></a>

```c
uint16_t sync_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_handle](#a00bf4bdf12fce6cbf2874b9c4ae09f9f)。

<a id="r_a05d798c9415541ef7f5716992157b1a1"></a>

```c
uint8_t adv_sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_sid](#a05d798c9415541ef7f5716992157b1a1)。

<a id="r_aff78554e8980635290767e9877ac479b"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#aff78554e8980635290767e9877ac479b)。

<a id="r_ae7a73293519ab45aec40a9a1aeaa4e89"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#ae7a73293519ab45aec40a9a1aeaa4e89)。

<a id="r_a736af2c2ee0afd3cb00e8eb4d103991c"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a736af2c2ee0afd3cb00e8eb4d103991c)。

<a id="r_a78853d14c3bf9a9aba3c4e15b2e06abb"></a>

```c
uint8_t clock_accuracy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clock_accuracy](#a78853d14c3bf9a9aba3c4e15b2e06abb)。

<a id="r_ab8a2a55fe071218284d60f1a2896945b"></a>

```c
uint8_t num_subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subevents](#ab8a2a55fe071218284d60f1a2896945b)。

<a id="r_aefdc5ac7ef125f4dc5865c198b98c67d"></a>

```c
uint8_t subevent_interval
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_interval](#aefdc5ac7ef125f4dc5865c198b98c67d)。

<a id="r_a9f55d5f6d17d11e72f7cac363a69fe97"></a>

```c
uint8_t response_slot_delay
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_delay](#a9f55d5f6d17d11e72f7cac363a69fe97)。

<a id="r_acf711399e575295dcef73cfeeb844eab"></a>

```c
uint8_t response_slot_spacing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_spacing](#acf711399e575295dcef73cfeeb844eab)。

## 264.2\_详细说明（Detailed Documentation）

<a id="aff78554e8980635290767e9877ac479b"></a>

### `addr`

```c
bt_addr_le_t bt_hci_evt_le_past_received_v2::addr
```

<a id="a05d798c9415541ef7f5716992157b1a1"></a>

### `adv_sid`

```c
uint8_t bt_hci_evt_le_past_received_v2::adv_sid
```

<a id="a78853d14c3bf9a9aba3c4e15b2e06abb"></a>

### `clock_accuracy`

```c
uint8_t bt_hci_evt_le_past_received_v2::clock_accuracy
```

<a id="adb011949f592ec7f8843d4fd47eca2e9"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_le_past_received_v2::conn_handle
```

<a id="a736af2c2ee0afd3cb00e8eb4d103991c"></a>

### `interval`

```c
uint16_t bt_hci_evt_le_past_received_v2::interval
```

<a id="ab8a2a55fe071218284d60f1a2896945b"></a>

### `num_subevents`

```c
uint8_t bt_hci_evt_le_past_received_v2::num_subevents
```

<a id="ae7a73293519ab45aec40a9a1aeaa4e89"></a>

### `phy`

```c
uint8_t bt_hci_evt_le_past_received_v2::phy
```

<a id="a9f55d5f6d17d11e72f7cac363a69fe97"></a>

### `response_slot_delay`

```c
uint8_t bt_hci_evt_le_past_received_v2::response_slot_delay
```

<a id="acf711399e575295dcef73cfeeb844eab"></a>

### `response_slot_spacing`

```c
uint8_t bt_hci_evt_le_past_received_v2::response_slot_spacing
```

<a id="acffc2fa22a16a3a12a4f7dfc3bb45866"></a>

### `service_data`

```c
uint16_t bt_hci_evt_le_past_received_v2::service_data
```

<a id="aefe79f973eda8c7c5670c7a721d55d8a"></a>

### `status`

```c
uint8_t bt_hci_evt_le_past_received_v2::status
```

<a id="aefdc5ac7ef125f4dc5865c198b98c67d"></a>

### `subevent_interval`

```c
uint8_t bt_hci_evt_le_past_received_v2::subevent_interval
```

<a id="a00bf4bdf12fce6cbf2874b9c4ae09f9f"></a>

### `sync_handle`

```c
uint16_t bt_hci_evt_le_past_received_v2::sync_handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 264.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P263_bt_hci_evt_le_past_received_结构体.md) · [返回大纲](大纲.md) · [下一章](P265_bt_hci_evt_le_path_loss_threshold_结构体.md)
