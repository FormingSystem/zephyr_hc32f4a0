---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-240
title: bt_hci_evt_le_cs_config_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__config__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第240章\_bt\_hci\_evt\_le\_cs\_config\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__config__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 240.1\_数据成员（Data Fields）

<a id="r_ae94aa8c92a8d4b33213adc8fc029a02d"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ae94aa8c92a8d4b33213adc8fc029a02d)。

<a id="r_a511021f717538d4ae25eb28ad82c5f99"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a511021f717538d4ae25eb28ad82c5f99)。

<a id="r_a544b3480034087ca01d64a41c1c4b8f9"></a>

```c
uint8_t config_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config_id](#a544b3480034087ca01d64a41c1c4b8f9)。

<a id="r_a748fcb3cbd396851a3d159887b12b3e0"></a>

```c
uint8_t action
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[action](#a748fcb3cbd396851a3d159887b12b3e0)。

<a id="r_a14f4c29a7f84463f048364389341c7b5"></a>

```c
uint8_t main_mode_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[main_mode_type](#a14f4c29a7f84463f048364389341c7b5)。

<a id="r_a55789928018a6124d87e76709b1b77d9"></a>

```c
uint8_t sub_mode_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sub_mode_type](#a55789928018a6124d87e76709b1b77d9)。

<a id="r_a21928853b505764e64fcc9190905b12c"></a>

```c
uint8_t min_main_mode_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_main_mode_steps](#a21928853b505764e64fcc9190905b12c)。

<a id="r_a9b14655fa6bb3c7ac43561a399019a76"></a>

```c
uint8_t max_main_mode_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_main_mode_steps](#a9b14655fa6bb3c7ac43561a399019a76)。

<a id="r_a7fe1af954bae025b9b8bbef70bd1c60e"></a>

```c
uint8_t main_mode_repetition
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[main_mode_repetition](#a7fe1af954bae025b9b8bbef70bd1c60e)。

<a id="r_a705a7be2d5ce02c4d78319f4f842b87e"></a>

```c
uint8_t mode_0_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode_0_steps](#a705a7be2d5ce02c4d78319f4f842b87e)。

<a id="r_a6f84ebf8a34a830ced1fc738d46fe244"></a>

```c
uint8_t role
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[role](#a6f84ebf8a34a830ced1fc738d46fe244)。

<a id="r_ae64ff5dbd9d704c3a7f4c5b98ada399c"></a>

```c
uint8_t rtt_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_type](#ae64ff5dbd9d704c3a7f4c5b98ada399c)。

<a id="r_ad0454e31d55ec25a21bc272cae999238"></a>

```c
uint8_t cs_sync_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_sync_phy](#ad0454e31d55ec25a21bc272cae999238)。

<a id="r_abcf0c43f33a85bcd860323212d57ce5b"></a>

```c
uint8_t channel_map [10]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_map](#abcf0c43f33a85bcd860323212d57ce5b)。

<a id="r_a1e5ba3ebb5dcac2105a0f859683505bc"></a>

```c
uint8_t channel_map_repetition
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_map_repetition](#a1e5ba3ebb5dcac2105a0f859683505bc)。

<a id="r_aa323b4a74f7fce33e884d0c32e4014d0"></a>

```c
uint8_t channel_selection_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_selection_type](#aa323b4a74f7fce33e884d0c32e4014d0)。

<a id="r_a73bd134e9337a9a47e41bba04623ee0b"></a>

```c
uint8_t ch3c_shape
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch3c_shape](#a73bd134e9337a9a47e41bba04623ee0b)。

<a id="r_a5f886c16acd561e143a8796fcc1ea5af"></a>

```c
uint8_t ch3c_jump
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch3c_jump](#a5f886c16acd561e143a8796fcc1ea5af)。

<a id="r_a45a1b908385be6a5289698dd08d8a610"></a>

```c
uint8_t cs_enhancements_1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_enhancements_1](#a45a1b908385be6a5289698dd08d8a610)。

信道探测增强项 1（CS Enhancements 1）。

<a id="r_afd62b1ffe5388c7f094cb086da4c86ba"></a>

```c
uint8_t t_ip1_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_ip1_time](#afd62b1ffe5388c7f094cb086da4c86ba)。

<a id="r_a8fafd0e139a9c85830468e5a056c42b7"></a>

```c
uint8_t t_ip2_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_ip2_time](#a8fafd0e139a9c85830468e5a056c42b7)。

<a id="r_a7aa0fd8a1c9c7270059725416dd0a90f"></a>

```c
uint8_t t_fcs_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_fcs_time](#a7aa0fd8a1c9c7270059725416dd0a90f)。

<a id="r_a7d64425b6aa44b01332ce6fac7813471"></a>

```c
uint8_t t_pm_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_pm_time](#a7d64425b6aa44b01332ce6fac7813471)。

## 240.2\_详细说明（Detailed Documentation）

<a id="a748fcb3cbd396851a3d159887b12b3e0"></a>

### `action`

```c
uint8_t bt_hci_evt_le_cs_config_complete::action
```

<a id="a5f886c16acd561e143a8796fcc1ea5af"></a>

### `ch3c_jump`

```c
uint8_t bt_hci_evt_le_cs_config_complete::ch3c_jump
```

<a id="a73bd134e9337a9a47e41bba04623ee0b"></a>

### `ch3c_shape`

```c
uint8_t bt_hci_evt_le_cs_config_complete::ch3c_shape
```

<a id="abcf0c43f33a85bcd860323212d57ce5b"></a>

### `channel_map`

```c
uint8_t bt_hci_evt_le_cs_config_complete::channel_map[10]
```

<a id="a1e5ba3ebb5dcac2105a0f859683505bc"></a>

### `channel_map_repetition`

```c
uint8_t bt_hci_evt_le_cs_config_complete::channel_map_repetition
```

<a id="aa323b4a74f7fce33e884d0c32e4014d0"></a>

### `channel_selection_type`

```c
uint8_t bt_hci_evt_le_cs_config_complete::channel_selection_type
```

<a id="a544b3480034087ca01d64a41c1c4b8f9"></a>

### `config_id`

```c
uint8_t bt_hci_evt_le_cs_config_complete::config_id
```

<a id="a45a1b908385be6a5289698dd08d8a610"></a>

### `cs_enhancements_1`

```c
uint8_t bt_hci_evt_le_cs_config_complete::cs_enhancements_1
```

信道探测增强项 1（CS Enhancements 1）。

<a id="ad0454e31d55ec25a21bc272cae999238"></a>

### `cs_sync_phy`

```c
uint8_t bt_hci_evt_le_cs_config_complete::cs_sync_phy
```

<a id="a511021f717538d4ae25eb28ad82c5f99"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_cs_config_complete::handle
```

<a id="a7fe1af954bae025b9b8bbef70bd1c60e"></a>

### `main_mode_repetition`

```c
uint8_t bt_hci_evt_le_cs_config_complete::main_mode_repetition
```

<a id="a14f4c29a7f84463f048364389341c7b5"></a>

### `main_mode_type`

```c
uint8_t bt_hci_evt_le_cs_config_complete::main_mode_type
```

<a id="a9b14655fa6bb3c7ac43561a399019a76"></a>

### `max_main_mode_steps`

```c
uint8_t bt_hci_evt_le_cs_config_complete::max_main_mode_steps
```

<a id="a21928853b505764e64fcc9190905b12c"></a>

### `min_main_mode_steps`

```c
uint8_t bt_hci_evt_le_cs_config_complete::min_main_mode_steps
```

<a id="a705a7be2d5ce02c4d78319f4f842b87e"></a>

### `mode_0_steps`

```c
uint8_t bt_hci_evt_le_cs_config_complete::mode_0_steps
```

<a id="a6f84ebf8a34a830ced1fc738d46fe244"></a>

### `role`

```c
uint8_t bt_hci_evt_le_cs_config_complete::role
```

<a id="ae64ff5dbd9d704c3a7f4c5b98ada399c"></a>

### `rtt_type`

```c
uint8_t bt_hci_evt_le_cs_config_complete::rtt_type
```

<a id="ae94aa8c92a8d4b33213adc8fc029a02d"></a>

### `status`

```c
uint8_t bt_hci_evt_le_cs_config_complete::status
```

<a id="a55789928018a6124d87e76709b1b77d9"></a>

### `sub_mode_type`

```c
uint8_t bt_hci_evt_le_cs_config_complete::sub_mode_type
```

<a id="a7aa0fd8a1c9c7270059725416dd0a90f"></a>

### `t_fcs_time`

```c
uint8_t bt_hci_evt_le_cs_config_complete::t_fcs_time
```

<a id="afd62b1ffe5388c7f094cb086da4c86ba"></a>

### `t_ip1_time`

```c
uint8_t bt_hci_evt_le_cs_config_complete::t_ip1_time
```

<a id="a8fafd0e139a9c85830468e5a056c42b7"></a>

### `t_ip2_time`

```c
uint8_t bt_hci_evt_le_cs_config_complete::t_ip2_time
```

<a id="a7d64425b6aa44b01332ce6fac7813471"></a>

### `t_pm_time`

```c
uint8_t bt_hci_evt_le_cs_config_complete::t_pm_time
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 240.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P239_bt_hci_evt_le_connectionless_iq_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md)
