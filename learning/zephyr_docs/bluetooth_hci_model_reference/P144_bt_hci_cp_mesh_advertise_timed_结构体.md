---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-144
title: bt_hci_cp_mesh_advertise_timed_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__mesh__advertise__timed.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第144章\_bt\_hci\_cp\_mesh\_advertise\_timed\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__mesh__advertise__timed.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 144.1\_数据成员（Data Fields）

<a id="r_a92f0163ec0854296ab76e49741d45196"></a>

```c
uint8_t adv_slot
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_slot](#a92f0163ec0854296ab76e49741d45196)。

<a id="r_ae395b4a53ff9e7af8885b9583562022a"></a>

```c
uint8_t own_addr_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[own_addr_type](#ae395b4a53ff9e7af8885b9583562022a)。

<a id="r_ada4348480db5f95acaad86bfa2ddbc7e"></a>

```c
bt_addr_t random_addr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[random_addr](#ada4348480db5f95acaad86bfa2ddbc7e)。

<a id="r_aa5bf4322faa354cc6de0c707502b4ed0"></a>

```c
uint8_t ch_map
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch_map](#aa5bf4322faa354cc6de0c707502b4ed0)。

<a id="r_aae34dd11723383b5559dc102c59213c2"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#aae34dd11723383b5559dc102c59213c2)。

<a id="r_adfb3acf9ea540d8405c5979115053b15"></a>

```c
uint8_t retx_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retx_count](#adfb3acf9ea540d8405c5979115053b15)。

<a id="r_a6718fd6031b2351eb033333a7302a21b"></a>

```c
uint8_t retx_interval
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retx_interval](#a6718fd6031b2351eb033333a7302a21b)。

<a id="r_a85a7e965b8004cac3a4bc0107844c69b"></a>

```c
uint32_t instant
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[instant](#a85a7e965b8004cac3a4bc0107844c69b)。

<a id="r_aee05619f0ed3b79f3bce5676c1f3aa8a"></a>

```c
uint16_t tx_delay
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_delay](#aee05619f0ed3b79f3bce5676c1f3aa8a)。

<a id="r_a1a5a5964eeff05fa232543756d234759"></a>

```c
uint16_t tx_window
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_window](#a1a5a5964eeff05fa232543756d234759)。

<a id="r_a78ecf7aa6ebf0739a585fed2a8710301"></a>

```c
uint8_t data_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_len](#a78ecf7aa6ebf0739a585fed2a8710301)。

<a id="r_ac097c1ee537d9a480ae16205eafc7105"></a>

```c
uint8_t data [31]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ac097c1ee537d9a480ae16205eafc7105)。

## 144.2\_详细说明（Detailed Documentation）

<a id="a92f0163ec0854296ab76e49741d45196"></a>

### `adv_slot`

```c
uint8_t bt_hci_cp_mesh_advertise_timed::adv_slot
```

<a id="aa5bf4322faa354cc6de0c707502b4ed0"></a>

### `ch_map`

```c
uint8_t bt_hci_cp_mesh_advertise_timed::ch_map
```

<a id="ac097c1ee537d9a480ae16205eafc7105"></a>

### `data`

```c
uint8_t bt_hci_cp_mesh_advertise_timed::data[31]
```

<a id="a78ecf7aa6ebf0739a585fed2a8710301"></a>

### `data_len`

```c
uint8_t bt_hci_cp_mesh_advertise_timed::data_len
```

<a id="a85a7e965b8004cac3a4bc0107844c69b"></a>

### `instant`

```c
uint32_t bt_hci_cp_mesh_advertise_timed::instant
```

<a id="ae395b4a53ff9e7af8885b9583562022a"></a>

### `own_addr_type`

```c
uint8_t bt_hci_cp_mesh_advertise_timed::own_addr_type
```

<a id="ada4348480db5f95acaad86bfa2ddbc7e"></a>

### `random_addr`

```c
bt_addr_t bt_hci_cp_mesh_advertise_timed::random_addr
```

<a id="adfb3acf9ea540d8405c5979115053b15"></a>

### `retx_count`

```c
uint8_t bt_hci_cp_mesh_advertise_timed::retx_count
```

<a id="a6718fd6031b2351eb033333a7302a21b"></a>

### `retx_interval`

```c
uint8_t bt_hci_cp_mesh_advertise_timed::retx_interval
```

<a id="aee05619f0ed3b79f3bce5676c1f3aa8a"></a>

### `tx_delay`

```c
uint16_t bt_hci_cp_mesh_advertise_timed::tx_delay
```

<a id="aae34dd11723383b5559dc102c59213c2"></a>

### `tx_power`

```c
int8_t bt_hci_cp_mesh_advertise_timed::tx_power
```

<a id="a1a5a5964eeff05fa232543756d234759"></a>

### `tx_window`

```c
uint16_t bt_hci_cp_mesh_advertise_timed::tx_window
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 144.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P143_bt_hci_cp_mesh_advertise_cancel_结构体.md) · [返回大纲](大纲.md) · [下一章](P145_bt_hci_cp_mesh_set_scan_filter_结构体.md)
