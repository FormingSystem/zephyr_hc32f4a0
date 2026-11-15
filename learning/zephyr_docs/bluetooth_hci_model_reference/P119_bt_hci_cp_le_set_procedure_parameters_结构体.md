---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-119
title: bt_hci_cp_le_set_procedure_parameters_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__procedure__parameters.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第119章\_bt\_hci\_cp\_le\_set\_procedure\_parameters\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__procedure__parameters.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 119.1\_数据成员（Data Fields）

<a id="r_ab8a15269255fb7d960ae712a844b9f35"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ab8a15269255fb7d960ae712a844b9f35)。

<a id="r_a7d2f5d9242df436906b005e66c7bb75d"></a>

```c
uint8_t config_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config_id](#a7d2f5d9242df436906b005e66c7bb75d)。

<a id="r_a5de9205fdf1b6e342f53a12aa82c10c5"></a>

```c
uint16_t max_procedure_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_procedure_len](#a5de9205fdf1b6e342f53a12aa82c10c5)。

<a id="r_a22ecbaff0fd48a0716a15d265adc590e"></a>

```c
uint16_t min_procedure_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_procedure_interval](#a22ecbaff0fd48a0716a15d265adc590e)。

<a id="r_ad46165bc5f6d875940ee53a8b98cb5b4"></a>

```c
uint16_t max_procedure_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_procedure_interval](#ad46165bc5f6d875940ee53a8b98cb5b4)。

<a id="r_ac6bb66fa24aec17a964f27365ca65ec9"></a>

```c
uint16_t max_procedure_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_procedure_count](#ac6bb66fa24aec17a964f27365ca65ec9)。

<a id="r_a51fb8c789cefce09d5da2b86d5c862ce"></a>

```c
uint8_t min_subevent_len [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_subevent_len](#a51fb8c789cefce09d5da2b86d5c862ce)。

<a id="r_aa9ec99aff85de173ccb2d3f144c85319"></a>

```c
uint8_t max_subevent_len [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_subevent_len](#aa9ec99aff85de173ccb2d3f144c85319)。

<a id="r_aa783e0e63c38ceee503c0b73ac873ca7"></a>

```c
uint8_t tone_antenna_config_selection
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tone_antenna_config_selection](#aa783e0e63c38ceee503c0b73ac873ca7)。

<a id="r_afcd4e8b390fd996ee134043ec2930fe8"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#afcd4e8b390fd996ee134043ec2930fe8)。

<a id="r_ade09ca9d42b0db682cf677d9ac4326d2"></a>

```c
uint8_t tx_power_delta
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_power_delta](#ade09ca9d42b0db682cf677d9ac4326d2)。

<a id="r_a7a61ff539f68a02ea7aa466f182dc5ab"></a>

```c
uint8_t preferred_peer_antenna
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[preferred_peer_antenna](#a7a61ff539f68a02ea7aa466f182dc5ab)。

<a id="r_a8524fd01e35094d2b78488c0a2876832"></a>

```c
uint8_t snr_control_initiator
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[snr_control_initiator](#a8524fd01e35094d2b78488c0a2876832)。

<a id="r_aa5a6a677b6e0d57658041e891535d74b"></a>

```c
uint8_t snr_control_reflector
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[snr_control_reflector](#aa5a6a677b6e0d57658041e891535d74b)。

## 119.2\_详细说明（Detailed Documentation）

<a id="a7d2f5d9242df436906b005e66c7bb75d"></a>

### `config_id`

```c
uint8_t bt_hci_cp_le_set_procedure_parameters::config_id
```

<a id="ab8a15269255fb7d960ae712a844b9f35"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_set_procedure_parameters::handle
```

<a id="ac6bb66fa24aec17a964f27365ca65ec9"></a>

### `max_procedure_count`

```c
uint16_t bt_hci_cp_le_set_procedure_parameters::max_procedure_count
```

<a id="ad46165bc5f6d875940ee53a8b98cb5b4"></a>

### `max_procedure_interval`

```c
uint16_t bt_hci_cp_le_set_procedure_parameters::max_procedure_interval
```

<a id="a5de9205fdf1b6e342f53a12aa82c10c5"></a>

### `max_procedure_len`

```c
uint16_t bt_hci_cp_le_set_procedure_parameters::max_procedure_len
```

<a id="aa9ec99aff85de173ccb2d3f144c85319"></a>

### `max_subevent_len`

```c
uint8_t bt_hci_cp_le_set_procedure_parameters::max_subevent_len[3]
```

<a id="a22ecbaff0fd48a0716a15d265adc590e"></a>

### `min_procedure_interval`

```c
uint16_t bt_hci_cp_le_set_procedure_parameters::min_procedure_interval
```

<a id="a51fb8c789cefce09d5da2b86d5c862ce"></a>

### `min_subevent_len`

```c
uint8_t bt_hci_cp_le_set_procedure_parameters::min_subevent_len[3]
```

<a id="afcd4e8b390fd996ee134043ec2930fe8"></a>

### `phy`

```c
uint8_t bt_hci_cp_le_set_procedure_parameters::phy
```

<a id="a7a61ff539f68a02ea7aa466f182dc5ab"></a>

### `preferred_peer_antenna`

```c
uint8_t bt_hci_cp_le_set_procedure_parameters::preferred_peer_antenna
```

<a id="a8524fd01e35094d2b78488c0a2876832"></a>

### `snr_control_initiator`

```c
uint8_t bt_hci_cp_le_set_procedure_parameters::snr_control_initiator
```

<a id="aa5a6a677b6e0d57658041e891535d74b"></a>

### `snr_control_reflector`

```c
uint8_t bt_hci_cp_le_set_procedure_parameters::snr_control_reflector
```

<a id="aa783e0e63c38ceee503c0b73ac873ca7"></a>

### `tone_antenna_config_selection`

```c
uint8_t bt_hci_cp_le_set_procedure_parameters::tone_antenna_config_selection
```

<a id="ade09ca9d42b0db682cf677d9ac4326d2"></a>

### `tx_power_delta`

```c
uint8_t bt_hci_cp_le_set_procedure_parameters::tx_power_delta
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 119.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P118_bt_hci_cp_le_set_privacy_mode_结构体.md) · [返回大纲](大纲.md) · [下一章](P120_bt_hci_cp_le_set_random_address_结构体.md)
