---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-35
title: bt_hci_cp_le_cs_create_config_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__cs__create__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_bt\_hci\_cp\_le\_cs\_create\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__cs__create__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_a3742081b071b992176b725448cc6ab29"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a3742081b071b992176b725448cc6ab29)。

<a id="r_ae833b5f02f878f54dca1a25753eca1f3"></a>

```c
uint8_t config_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config_id](#ae833b5f02f878f54dca1a25753eca1f3)。

<a id="r_a9dc7a6b577c33583b7ca7548e2b555ac"></a>

```c
uint8_t create_context
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[create_context](#a9dc7a6b577c33583b7ca7548e2b555ac)。

<a id="r_a74c5fdfbc97b112c35ee318aa2b9b463"></a>

```c
uint8_t main_mode_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[main_mode_type](#a74c5fdfbc97b112c35ee318aa2b9b463)。

<a id="r_a34fa54e8bbd641bb0901b0b057134ffb"></a>

```c
uint8_t sub_mode_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sub_mode_type](#a34fa54e8bbd641bb0901b0b057134ffb)。

<a id="r_aeb26115c8b500829ef6bc238aa3a495f"></a>

```c
uint8_t min_main_mode_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_main_mode_steps](#aeb26115c8b500829ef6bc238aa3a495f)。

<a id="r_aa13e091f99114bb5217489757c1522bd"></a>

```c
uint8_t max_main_mode_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_main_mode_steps](#aa13e091f99114bb5217489757c1522bd)。

<a id="r_acd11430a6c94b0f0c34e2788a2326a40"></a>

```c
uint8_t main_mode_repetition
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[main_mode_repetition](#acd11430a6c94b0f0c34e2788a2326a40)。

<a id="r_a909e409d55ac539a119e932899a97204"></a>

```c
uint8_t mode_0_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode_0_steps](#a909e409d55ac539a119e932899a97204)。

<a id="r_a5a17d6c72daaefcb55fdfa24194cc886"></a>

```c
uint8_t role
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[role](#a5a17d6c72daaefcb55fdfa24194cc886)。

<a id="r_a709938176023c5482c91af8995001782"></a>

```c
uint8_t rtt_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_type](#a709938176023c5482c91af8995001782)。

<a id="r_ac6c9c568918c9ef9aa4f2038a4922020"></a>

```c
uint8_t cs_sync_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_sync_phy](#ac6c9c568918c9ef9aa4f2038a4922020)。

<a id="r_abab4907ec883430044bb9f9d6cf9f25d"></a>

```c
uint8_t channel_map [10]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_map](#abab4907ec883430044bb9f9d6cf9f25d)。

<a id="r_a8182f4becdef488b84f12fe7e4274193"></a>

```c
uint8_t channel_map_repetition
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_map_repetition](#a8182f4becdef488b84f12fe7e4274193)。

<a id="r_a2c8be699bfd8eaaababd6d0de0b13e18"></a>

```c
uint8_t channel_selection_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_selection_type](#a2c8be699bfd8eaaababd6d0de0b13e18)。

<a id="r_addaa3592a97bda96a4aba17e809e4018"></a>

```c
uint8_t ch3c_shape
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch3c_shape](#addaa3592a97bda96a4aba17e809e4018)。

<a id="r_a0223c41abc034d515421fad8c3123387"></a>

```c
uint8_t ch3c_jump
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch3c_jump](#a0223c41abc034d515421fad8c3123387)。

<a id="r_a6088c8413ca175c0231fc53bfb168b29"></a>

```c
uint8_t cs_enhancements_1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_enhancements_1](#a6088c8413ca175c0231fc53bfb168b29)。

信道探测增强项 1（CS Enhancements 1）。

## 35.2\_详细说明（Detailed Documentation）

<a id="a0223c41abc034d515421fad8c3123387"></a>

### `ch3c_jump`

```c
uint8_t bt_hci_cp_le_cs_create_config::ch3c_jump
```

<a id="addaa3592a97bda96a4aba17e809e4018"></a>

### `ch3c_shape`

```c
uint8_t bt_hci_cp_le_cs_create_config::ch3c_shape
```

<a id="abab4907ec883430044bb9f9d6cf9f25d"></a>

### `channel_map`

```c
uint8_t bt_hci_cp_le_cs_create_config::channel_map[10]
```

<a id="a8182f4becdef488b84f12fe7e4274193"></a>

### `channel_map_repetition`

```c
uint8_t bt_hci_cp_le_cs_create_config::channel_map_repetition
```

<a id="a2c8be699bfd8eaaababd6d0de0b13e18"></a>

### `channel_selection_type`

```c
uint8_t bt_hci_cp_le_cs_create_config::channel_selection_type
```

<a id="ae833b5f02f878f54dca1a25753eca1f3"></a>

### `config_id`

```c
uint8_t bt_hci_cp_le_cs_create_config::config_id
```

<a id="a9dc7a6b577c33583b7ca7548e2b555ac"></a>

### `create_context`

```c
uint8_t bt_hci_cp_le_cs_create_config::create_context
```

<a id="a6088c8413ca175c0231fc53bfb168b29"></a>

### `cs_enhancements_1`

```c
uint8_t bt_hci_cp_le_cs_create_config::cs_enhancements_1
```

信道探测增强项 1（CS Enhancements 1）。

<a id="ac6c9c568918c9ef9aa4f2038a4922020"></a>

### `cs_sync_phy`

```c
uint8_t bt_hci_cp_le_cs_create_config::cs_sync_phy
```

<a id="a3742081b071b992176b725448cc6ab29"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_cs_create_config::handle
```

<a id="acd11430a6c94b0f0c34e2788a2326a40"></a>

### `main_mode_repetition`

```c
uint8_t bt_hci_cp_le_cs_create_config::main_mode_repetition
```

<a id="a74c5fdfbc97b112c35ee318aa2b9b463"></a>

### `main_mode_type`

```c
uint8_t bt_hci_cp_le_cs_create_config::main_mode_type
```

<a id="aa13e091f99114bb5217489757c1522bd"></a>

### `max_main_mode_steps`

```c
uint8_t bt_hci_cp_le_cs_create_config::max_main_mode_steps
```

<a id="aeb26115c8b500829ef6bc238aa3a495f"></a>

### `min_main_mode_steps`

```c
uint8_t bt_hci_cp_le_cs_create_config::min_main_mode_steps
```

<a id="a909e409d55ac539a119e932899a97204"></a>

### `mode_0_steps`

```c
uint8_t bt_hci_cp_le_cs_create_config::mode_0_steps
```

<a id="a5a17d6c72daaefcb55fdfa24194cc886"></a>

### `role`

```c
uint8_t bt_hci_cp_le_cs_create_config::role
```

<a id="a709938176023c5482c91af8995001782"></a>

### `rtt_type`

```c
uint8_t bt_hci_cp_le_cs_create_config::rtt_type
```

<a id="a34fa54e8bbd641bb0901b0b057134ffb"></a>

### `sub_mode_type`

```c
uint8_t bt_hci_cp_le_cs_create_config::sub_mode_type
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_bt_hci_cp_le_create_conn_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_bt_hci_cp_le_cs_remove_config_结构体.md)
