---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-241
title: bt_hci_evt_le_cs_procedure_enable_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__procedure__enable__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第241章\_bt\_hci\_evt\_le\_cs\_procedure\_enable\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__procedure__enable__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 241.1\_数据成员（Data Fields）

<a id="r_a5822ff654eee794442a05033e0f10fae"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a5822ff654eee794442a05033e0f10fae)。

<a id="r_adcf8e32c2346073e0fbe273d261f6741"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#adcf8e32c2346073e0fbe273d261f6741)。

<a id="r_a17b62e13cda5f47dee2e8873686b978e"></a>

```c
uint8_t config_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config_id](#a17b62e13cda5f47dee2e8873686b978e)。

<a id="r_a7ff8f1e713d9b835f3a4e0e79cb1b3d1"></a>

```c
uint8_t state
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](#a7ff8f1e713d9b835f3a4e0e79cb1b3d1)。

<a id="r_a60a9e00cba665d73e65d0ee5b0d9efbc"></a>

```c
uint8_t tone_antenna_config_selection
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tone_antenna_config_selection](#a60a9e00cba665d73e65d0ee5b0d9efbc)。

<a id="r_afd760c9b6809e6764a652ecb3ee4c2b5"></a>

```c
uint8_t selected_tx_power
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[selected_tx_power](#afd760c9b6809e6764a652ecb3ee4c2b5)。

<a id="r_af5959274cb88a8e4fdf09e8dd756f31c"></a>

```c
uint8_t subevent_len [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_len](#af5959274cb88a8e4fdf09e8dd756f31c)。

<a id="r_aacc14948a9e6c384ec94051fb4323599"></a>

```c
uint8_t subevents_per_event
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevents_per_event](#aacc14948a9e6c384ec94051fb4323599)。

<a id="r_a8f5485967662dbd1676d8edd6345fd13"></a>

```c
uint16_t subevent_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subevent_interval](#a8f5485967662dbd1676d8edd6345fd13)。

<a id="r_a688bfcb6781b2e3480f021c66a3109fe"></a>

```c
uint16_t event_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[event_interval](#a688bfcb6781b2e3480f021c66a3109fe)。

<a id="r_ad7c21907a38747ec405c992ef14e8dd7"></a>

```c
uint16_t procedure_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[procedure_interval](#ad7c21907a38747ec405c992ef14e8dd7)。

<a id="r_ac8489dc8ff5f9bf052a7c1a67a544106"></a>

```c
uint16_t procedure_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[procedure_count](#ac8489dc8ff5f9bf052a7c1a67a544106)。

<a id="r_a7a38c8ced8720a428df42e821ec7e9e6"></a>

```c
uint16_t max_procedure_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_procedure_len](#a7a38c8ced8720a428df42e821ec7e9e6)。

## 241.2\_详细说明（Detailed Documentation）

<a id="a17b62e13cda5f47dee2e8873686b978e"></a>

### `config_id`

```c
uint8_t bt_hci_evt_le_cs_procedure_enable_complete::config_id
```

<a id="a688bfcb6781b2e3480f021c66a3109fe"></a>

### `event_interval`

```c
uint16_t bt_hci_evt_le_cs_procedure_enable_complete::event_interval
```

<a id="adcf8e32c2346073e0fbe273d261f6741"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_cs_procedure_enable_complete::handle
```

<a id="a7a38c8ced8720a428df42e821ec7e9e6"></a>

### `max_procedure_len`

```c
uint16_t bt_hci_evt_le_cs_procedure_enable_complete::max_procedure_len
```

<a id="ac8489dc8ff5f9bf052a7c1a67a544106"></a>

### `procedure_count`

```c
uint16_t bt_hci_evt_le_cs_procedure_enable_complete::procedure_count
```

<a id="ad7c21907a38747ec405c992ef14e8dd7"></a>

### `procedure_interval`

```c
uint16_t bt_hci_evt_le_cs_procedure_enable_complete::procedure_interval
```

<a id="afd760c9b6809e6764a652ecb3ee4c2b5"></a>

### `selected_tx_power`

```c
uint8_t bt_hci_evt_le_cs_procedure_enable_complete::selected_tx_power
```

<a id="a7ff8f1e713d9b835f3a4e0e79cb1b3d1"></a>

### `state`

```c
uint8_t bt_hci_evt_le_cs_procedure_enable_complete::state
```

<a id="a5822ff654eee794442a05033e0f10fae"></a>

### `status`

```c
uint8_t bt_hci_evt_le_cs_procedure_enable_complete::status
```

<a id="a8f5485967662dbd1676d8edd6345fd13"></a>

### `subevent_interval`

```c
uint16_t bt_hci_evt_le_cs_procedure_enable_complete::subevent_interval
```

<a id="af5959274cb88a8e4fdf09e8dd756f31c"></a>

### `subevent_len`

```c
uint8_t bt_hci_evt_le_cs_procedure_enable_complete::subevent_len[3]
```

<a id="aacc14948a9e6c384ec94051fb4323599"></a>

### `subevents_per_event`

```c
uint8_t bt_hci_evt_le_cs_procedure_enable_complete::subevents_per_event
```

<a id="a60a9e00cba665d73e65d0ee5b0d9efbc"></a>

### `tone_antenna_config_selection`

```c
uint8_t bt_hci_evt_le_cs_procedure_enable_complete::tone_antenna_config_selection
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 241.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P240_bt_hci_evt_le_cs_config_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P242_bt_hci_evt_le_cs_read_remote_fae_table_complete_结构体.md)
