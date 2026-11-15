---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-270
title: bt_hci_evt_le_per_adv_sync_established_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__adv__sync__established__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第270章\_bt\_hci\_evt\_le\_per\_adv\_sync\_established\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__per__adv__sync__established__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 270.1\_数据成员（Data Fields）

<a id="r_a96b975f5a2fcf193b0b58c230486ec36"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a96b975f5a2fcf193b0b58c230486ec36)。

<a id="r_ab7d3793e782d7b2bb311b8a5ac3a871b"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ab7d3793e782d7b2bb311b8a5ac3a871b)。

<a id="r_a0ce9a9170d93ff69f25ff35eb163511f"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#a0ce9a9170d93ff69f25ff35eb163511f)。

<a id="r_abd67ec989479eb793e7bf99a4cf371b8"></a>

```c
bt_addr_le_t adv_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[adv_addr](#abd67ec989479eb793e7bf99a4cf371b8)。

<a id="r_a36b5c8454ee3635d2298592c83166f14"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a36b5c8454ee3635d2298592c83166f14)。

<a id="r_a958630cb9e275ab6f8ed0c548958e5ee"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a958630cb9e275ab6f8ed0c548958e5ee)。

<a id="r_a13ab0e87d6673a34e51f3112a5fd5a0c"></a>

```c
uint8_t clock_accuracy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clock_accuracy](#a13ab0e87d6673a34e51f3112a5fd5a0c)。

<a id="r_af4fb92baa4f98c08c990ba505faf9226"></a>

```c
uint8_t num_subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subevents](#af4fb92baa4f98c08c990ba505faf9226)。

<a id="r_ad21df6269d8242d94ba9cbc1e0d4d344"></a>

```c
uint8_t subevent_interval
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_interval](#ad21df6269d8242d94ba9cbc1e0d4d344)。

<a id="r_ac4c2bc8789513692ce0f2cc81aa59476"></a>

```c
uint8_t response_slot_delay
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_delay](#ac4c2bc8789513692ce0f2cc81aa59476)。

<a id="r_aacb6946dbfeb2ffbc251910853559329"></a>

```c
uint8_t response_slot_spacing
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot_spacing](#aacb6946dbfeb2ffbc251910853559329)。

## 270.2\_详细说明（Detailed Documentation）

<a id="abd67ec989479eb793e7bf99a4cf371b8"></a>

### `adv_addr`

```c
bt_addr_le_t bt_hci_evt_le_per_adv_sync_established_v2::adv_addr
```

<a id="a13ab0e87d6673a34e51f3112a5fd5a0c"></a>

### `clock_accuracy`

```c
uint8_t bt_hci_evt_le_per_adv_sync_established_v2::clock_accuracy
```

<a id="ab7d3793e782d7b2bb311b8a5ac3a871b"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_per_adv_sync_established_v2::handle
```

<a id="a958630cb9e275ab6f8ed0c548958e5ee"></a>

### `interval`

```c
uint16_t bt_hci_evt_le_per_adv_sync_established_v2::interval
```

<a id="af4fb92baa4f98c08c990ba505faf9226"></a>

### `num_subevents`

```c
uint8_t bt_hci_evt_le_per_adv_sync_established_v2::num_subevents
```

<a id="a36b5c8454ee3635d2298592c83166f14"></a>

### `phy`

```c
uint8_t bt_hci_evt_le_per_adv_sync_established_v2::phy
```

<a id="ac4c2bc8789513692ce0f2cc81aa59476"></a>

### `response_slot_delay`

```c
uint8_t bt_hci_evt_le_per_adv_sync_established_v2::response_slot_delay
```

<a id="aacb6946dbfeb2ffbc251910853559329"></a>

### `response_slot_spacing`

```c
uint8_t bt_hci_evt_le_per_adv_sync_established_v2::response_slot_spacing
```

<a id="a0ce9a9170d93ff69f25ff35eb163511f"></a>

### `sid`

```c
uint8_t bt_hci_evt_le_per_adv_sync_established_v2::sid
```

<a id="a96b975f5a2fcf193b0b58c230486ec36"></a>

### `status`

```c
uint8_t bt_hci_evt_le_per_adv_sync_established_v2::status
```

<a id="ad21df6269d8242d94ba9cbc1e0d4d344"></a>

### `subevent_interval`

```c
uint8_t bt_hci_evt_le_per_adv_sync_established_v2::subevent_interval
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 270.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P269_bt_hci_evt_le_per_adv_sync_established_结构体.md) · [返回大纲](大纲.md) · [下一章](P271_bt_hci_evt_le_per_adv_sync_lost_结构体.md)
