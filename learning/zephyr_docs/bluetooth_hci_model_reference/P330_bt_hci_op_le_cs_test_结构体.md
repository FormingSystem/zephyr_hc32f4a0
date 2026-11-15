---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-330
title: bt_hci_op_le_cs_test_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__op__le__cs__test.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第330章\_bt\_hci\_op\_le\_cs\_test\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__op__le__cs__test.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 330.1\_数据成员（Data Fields）

<a id="r_af4cdfd8c8cab500277c06a82ac088577"></a>

```c
uint8_t main_mode_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[main_mode_type](#af4cdfd8c8cab500277c06a82ac088577)。

<a id="r_a090c5d03cf829011196d644cd9f7c7db"></a>

```c
uint8_t sub_mode_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sub_mode_type](#a090c5d03cf829011196d644cd9f7c7db)。

<a id="r_a60cc9a7c46f8cd0933dc2f5a68cca627"></a>

```c
uint8_t main_mode_repetition
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[main_mode_repetition](#a60cc9a7c46f8cd0933dc2f5a68cca627)。

<a id="r_aaf480890608b5cfc9151dac844e9a337"></a>

```c
uint8_t mode_0_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode_0_steps](#aaf480890608b5cfc9151dac844e9a337)。

<a id="r_afa0310f818002d7c1ac048f0db8c7f1c"></a>

```c
uint8_t role
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[role](#afa0310f818002d7c1ac048f0db8c7f1c)。

<a id="r_ae0234031d94e93653dd45e6e657c199f"></a>

```c
uint8_t rtt_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_type](#ae0234031d94e93653dd45e6e657c199f)。

<a id="r_af42701651bca5fe0353ae1de9c453f47"></a>

```c
uint8_t cs_sync_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_sync_phy](#af42701651bca5fe0353ae1de9c453f47)。

<a id="r_aef335dd7738634cb8f81c18e0350141e"></a>

```c
uint8_t cs_sync_antenna_selection
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_sync_antenna_selection](#aef335dd7738634cb8f81c18e0350141e)。

<a id="r_a8ad67a5a0138f32cc5295074011a3808"></a>

```c
uint8_t subevent_len [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent_len](#a8ad67a5a0138f32cc5295074011a3808)。

<a id="r_ad52cd2862d2544448a5e175c58541f89"></a>

```c
uint16_t subevent_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subevent_interval](#ad52cd2862d2544448a5e175c58541f89)。

<a id="r_a1c105f7a4d48754322fee6992db8c175"></a>

```c
uint8_t max_num_subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_num_subevents](#a1c105f7a4d48754322fee6992db8c175)。

<a id="r_adf2f24dc6988f1f0e0457a6cf3141521"></a>

```c
uint8_t transmit_power_level
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transmit_power_level](#adf2f24dc6988f1f0e0457a6cf3141521)。

<a id="r_a0675dfbb050838d98f21cfa28af8615b"></a>

```c
uint8_t t_ip1_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_ip1_time](#a0675dfbb050838d98f21cfa28af8615b)。

<a id="r_a7538e91b5ced2702965a21f8e754ebcc"></a>

```c
uint8_t t_ip2_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_ip2_time](#a7538e91b5ced2702965a21f8e754ebcc)。

<a id="r_aa3d510663e5dcc44b5acd9d1c41746d5"></a>

```c
uint8_t t_fcs_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_fcs_time](#aa3d510663e5dcc44b5acd9d1c41746d5)。

<a id="r_a981da50e0594b8bc05f811e5170b10f5"></a>

```c
uint8_t t_pm_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_pm_time](#a981da50e0594b8bc05f811e5170b10f5)。

<a id="r_a09c40ecd0d4e325e0c0504a9d8cd977b"></a>

```c
uint8_t t_sw_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_time](#a09c40ecd0d4e325e0c0504a9d8cd977b)。

<a id="r_acaa428a37e68ff56c311397e53f46526"></a>

```c
uint8_t tone_antenna_config_selection
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tone_antenna_config_selection](#acaa428a37e68ff56c311397e53f46526)。

<a id="r_a06ac1b5aa8951fe4769a1360af44df82"></a>

```c
uint8_t cs_enhancements_1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_enhancements_1](#a06ac1b5aa8951fe4769a1360af44df82)。

信道探测增强项 1（CS Enhancements 1）。

<a id="r_a551c06e651180867dd1d23b3fdf4c031"></a>

```c
uint8_t snr_control_initiator
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[snr_control_initiator](#a551c06e651180867dd1d23b3fdf4c031)。

<a id="r_a3c949d9a7eb4f56427f6e9f8be7cb77b"></a>

```c
uint8_t snr_control_reflector
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[snr_control_reflector](#a3c949d9a7eb4f56427f6e9f8be7cb77b)。

<a id="r_aee8c125df0f7136a0ecdb9f04903aaef"></a>

```c
uint16_t drbg_nonce
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[drbg_nonce](#aee8c125df0f7136a0ecdb9f04903aaef)。

<a id="r_a8c23c2e6e8c38bf33fcd6d1e343f5982"></a>

```c
uint8_t channel_map_repetition
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_map_repetition](#a8c23c2e6e8c38bf33fcd6d1e343f5982)。

<a id="r_acc2d0768b69e5f5b593e5aff71b17f20"></a>

```c
uint16_t override_config
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[override_config](#acc2d0768b69e5f5b593e5aff71b17f20)。

<a id="r_a373372a93d94e70d674c1c7b4c126734"></a>

```c
uint8_t override_parameters_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[override_parameters_length](#a373372a93d94e70d674c1c7b4c126734)。

<a id="r_a15a68fe7c98b2e242afd6eb67dd9b40a"></a>

```c
uint8_t override_parameters_data []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[override_parameters_data](#a15a68fe7c98b2e242afd6eb67dd9b40a)。

## 330.2\_详细说明（Detailed Documentation）

<a id="a8c23c2e6e8c38bf33fcd6d1e343f5982"></a>

### `channel_map_repetition`

```c
uint8_t bt_hci_op_le_cs_test::channel_map_repetition
```

<a id="a06ac1b5aa8951fe4769a1360af44df82"></a>

### `cs_enhancements_1`

```c
uint8_t bt_hci_op_le_cs_test::cs_enhancements_1
```

信道探测增强项 1（CS Enhancements 1）。

<a id="aef335dd7738634cb8f81c18e0350141e"></a>

### `cs_sync_antenna_selection`

```c
uint8_t bt_hci_op_le_cs_test::cs_sync_antenna_selection
```

<a id="af42701651bca5fe0353ae1de9c453f47"></a>

### `cs_sync_phy`

```c
uint8_t bt_hci_op_le_cs_test::cs_sync_phy
```

<a id="aee8c125df0f7136a0ecdb9f04903aaef"></a>

### `drbg_nonce`

```c
uint16_t bt_hci_op_le_cs_test::drbg_nonce
```

<a id="a60cc9a7c46f8cd0933dc2f5a68cca627"></a>

### `main_mode_repetition`

```c
uint8_t bt_hci_op_le_cs_test::main_mode_repetition
```

<a id="af4cdfd8c8cab500277c06a82ac088577"></a>

### `main_mode_type`

```c
uint8_t bt_hci_op_le_cs_test::main_mode_type
```

<a id="a1c105f7a4d48754322fee6992db8c175"></a>

### `max_num_subevents`

```c
uint8_t bt_hci_op_le_cs_test::max_num_subevents
```

<a id="aaf480890608b5cfc9151dac844e9a337"></a>

### `mode_0_steps`

```c
uint8_t bt_hci_op_le_cs_test::mode_0_steps
```

<a id="acc2d0768b69e5f5b593e5aff71b17f20"></a>

### `override_config`

```c
uint16_t bt_hci_op_le_cs_test::override_config
```

<a id="a15a68fe7c98b2e242afd6eb67dd9b40a"></a>

### `override_parameters_data`

```c
uint8_t bt_hci_op_le_cs_test::override_parameters_data[]
```

<a id="a373372a93d94e70d674c1c7b4c126734"></a>

### `override_parameters_length`

```c
uint8_t bt_hci_op_le_cs_test::override_parameters_length
```

<a id="afa0310f818002d7c1ac048f0db8c7f1c"></a>

### `role`

```c
uint8_t bt_hci_op_le_cs_test::role
```

<a id="ae0234031d94e93653dd45e6e657c199f"></a>

### `rtt_type`

```c
uint8_t bt_hci_op_le_cs_test::rtt_type
```

<a id="a551c06e651180867dd1d23b3fdf4c031"></a>

### `snr_control_initiator`

```c
uint8_t bt_hci_op_le_cs_test::snr_control_initiator
```

<a id="a3c949d9a7eb4f56427f6e9f8be7cb77b"></a>

### `snr_control_reflector`

```c
uint8_t bt_hci_op_le_cs_test::snr_control_reflector
```

<a id="a090c5d03cf829011196d644cd9f7c7db"></a>

### `sub_mode_type`

```c
uint8_t bt_hci_op_le_cs_test::sub_mode_type
```

<a id="ad52cd2862d2544448a5e175c58541f89"></a>

### `subevent_interval`

```c
uint16_t bt_hci_op_le_cs_test::subevent_interval
```

<a id="a8ad67a5a0138f32cc5295074011a3808"></a>

### `subevent_len`

```c
uint8_t bt_hci_op_le_cs_test::subevent_len[3]
```

<a id="aa3d510663e5dcc44b5acd9d1c41746d5"></a>

### `t_fcs_time`

```c
uint8_t bt_hci_op_le_cs_test::t_fcs_time
```

<a id="a0675dfbb050838d98f21cfa28af8615b"></a>

### `t_ip1_time`

```c
uint8_t bt_hci_op_le_cs_test::t_ip1_time
```

<a id="a7538e91b5ced2702965a21f8e754ebcc"></a>

### `t_ip2_time`

```c
uint8_t bt_hci_op_le_cs_test::t_ip2_time
```

<a id="a981da50e0594b8bc05f811e5170b10f5"></a>

### `t_pm_time`

```c
uint8_t bt_hci_op_le_cs_test::t_pm_time
```

<a id="a09c40ecd0d4e325e0c0504a9d8cd977b"></a>

### `t_sw_time`

```c
uint8_t bt_hci_op_le_cs_test::t_sw_time
```

<a id="acaa428a37e68ff56c311397e53f46526"></a>

### `tone_antenna_config_selection`

```c
uint8_t bt_hci_op_le_cs_test::tone_antenna_config_selection
```

<a id="adf2f24dc6988f1f0e0457a6cf3141521"></a>

### `transmit_power_level`

```c
uint8_t bt_hci_op_le_cs_test::transmit_power_level
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 330.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P329_bt_hci_op_le_connection_rate_request_结构体.md) · [返回大纲](大纲.md) · [下一章](P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md)
