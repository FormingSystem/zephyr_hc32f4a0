---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-364
title: bt_hci_rp_le_read_local_supported_capabilities_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__local__supported__capabilities.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第364章\_bt\_hci\_rp\_le\_read\_local\_supported\_capabilities\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__local__supported__capabilities.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 364.1\_数据成员（Data Fields）

<a id="r_aaf578336893980f2ec1b2343b81860e5"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#aaf578336893980f2ec1b2343b81860e5)。

<a id="r_a5f59d0b65cc4e7e44e487fa5535b76a9"></a>

```c
uint8_t num_config_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_config_supported](#a5f59d0b65cc4e7e44e487fa5535b76a9)。

<a id="r_ad667ba51ffdbaf7754dea6f519615cb7"></a>

```c
uint16_t max_consecutive_procedures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_consecutive_procedures_supported](#ad667ba51ffdbaf7754dea6f519615cb7)。

<a id="r_ae0767bb41b7b57e955ddbede2f83c166"></a>

```c
uint8_t num_antennas_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_antennas_supported](#ae0767bb41b7b57e955ddbede2f83c166)。

<a id="r_a7975eb0ce27f0326d1d909bffef57840"></a>

```c
uint8_t max_antenna_paths_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_antenna_paths_supported](#a7975eb0ce27f0326d1d909bffef57840)。

<a id="r_a0958a5426e0057e2b8ccb80c222d0248"></a>

```c
uint8_t roles_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[roles_supported](#a0958a5426e0057e2b8ccb80c222d0248)。

<a id="r_aaf09d10c19980729ef04654114919211"></a>

```c
uint8_t modes_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[modes_supported](#aaf09d10c19980729ef04654114919211)。

<a id="r_a24ffa02b6a8bfbff8b7d32f5ee46bea5"></a>

```c
uint8_t rtt_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_capability](#a24ffa02b6a8bfbff8b7d32f5ee46bea5)。

<a id="r_a3a16c62ea321620608d706a80d90575e"></a>

```c
uint8_t rtt_aa_only_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_aa_only_n](#a3a16c62ea321620608d706a80d90575e)。

<a id="r_ababf476100298c2ba7d79bdadd7a9d1b"></a>

```c
uint8_t rtt_sounding_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_sounding_n](#ababf476100298c2ba7d79bdadd7a9d1b)。

<a id="r_ad90ce3e635b8bccd29eefe73303f6e42"></a>

```c
uint8_t rtt_random_payload_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_random_payload_n](#ad90ce3e635b8bccd29eefe73303f6e42)。

<a id="r_a3eb4830443e7912bf8ca97f603b91545"></a>

```c
uint16_t nadm_sounding_capability
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nadm_sounding_capability](#a3eb4830443e7912bf8ca97f603b91545)。

<a id="r_a0e0bd5b1c624c7143b0229b5d3eeec6e"></a>

```c
uint16_t nadm_random_capability
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nadm_random_capability](#a0e0bd5b1c624c7143b0229b5d3eeec6e)。

<a id="r_af3d1e7588f2429bb400fac81733748c3"></a>

```c
uint8_t cs_sync_phys_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_sync_phys_supported](#af3d1e7588f2429bb400fac81733748c3)。

<a id="r_a8e7cc92cc4099774e8d0b385fc5f3d79"></a>

```c
uint16_t subfeatures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subfeatures_supported](#a8e7cc92cc4099774e8d0b385fc5f3d79)。

<a id="r_a115ffe697da3e09ece4091493fa8f2da"></a>

```c
uint16_t t_ip1_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip1_times_supported](#a115ffe697da3e09ece4091493fa8f2da)。

<a id="r_a88a4277c5dea41b8171c33c85ed760bf"></a>

```c
uint16_t t_ip2_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip2_times_supported](#a88a4277c5dea41b8171c33c85ed760bf)。

<a id="r_a81bd809a734b6cdde2d55e0b23e41237"></a>

```c
uint16_t t_fcs_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_fcs_times_supported](#a81bd809a734b6cdde2d55e0b23e41237)。

<a id="r_ab026e5abfdead47eca1c5d8d316bc62c"></a>

```c
uint16_t t_pm_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_pm_times_supported](#ab026e5abfdead47eca1c5d8d316bc62c)。

<a id="r_ad07b464737c59b33de4c89948d4c5686"></a>

```c
uint8_t t_sw_time_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_time_supported](#ad07b464737c59b33de4c89948d4c5686)。

<a id="r_a1806f2f5ec2738b026453bbdb8b38ce9"></a>

```c
uint8_t tx_snr_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_snr_capability](#a1806f2f5ec2738b026453bbdb8b38ce9)。

## 364.2\_详细说明（Detailed Documentation）

<a id="af3d1e7588f2429bb400fac81733748c3"></a>

### `cs_sync_phys_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::cs_sync_phys_supported
```

<a id="a7975eb0ce27f0326d1d909bffef57840"></a>

### `max_antenna_paths_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::max_antenna_paths_supported
```

<a id="ad667ba51ffdbaf7754dea6f519615cb7"></a>

### `max_consecutive_procedures_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities::max_consecutive_procedures_supported
```

<a id="aaf09d10c19980729ef04654114919211"></a>

### `modes_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::modes_supported
```

<a id="a0e0bd5b1c624c7143b0229b5d3eeec6e"></a>

### `nadm_random_capability`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities::nadm_random_capability
```

<a id="a3eb4830443e7912bf8ca97f603b91545"></a>

### `nadm_sounding_capability`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities::nadm_sounding_capability
```

<a id="ae0767bb41b7b57e955ddbede2f83c166"></a>

### `num_antennas_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::num_antennas_supported
```

<a id="a5f59d0b65cc4e7e44e487fa5535b76a9"></a>

### `num_config_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::num_config_supported
```

<a id="a0958a5426e0057e2b8ccb80c222d0248"></a>

### `roles_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::roles_supported
```

<a id="a3a16c62ea321620608d706a80d90575e"></a>

### `rtt_aa_only_n`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::rtt_aa_only_n
```

<a id="a24ffa02b6a8bfbff8b7d32f5ee46bea5"></a>

### `rtt_capability`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::rtt_capability
```

<a id="ad90ce3e635b8bccd29eefe73303f6e42"></a>

### `rtt_random_payload_n`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::rtt_random_payload_n
```

<a id="ababf476100298c2ba7d79bdadd7a9d1b"></a>

### `rtt_sounding_n`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::rtt_sounding_n
```

<a id="aaf578336893980f2ec1b2343b81860e5"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::status
```

<a id="a8e7cc92cc4099774e8d0b385fc5f3d79"></a>

### `subfeatures_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities::subfeatures_supported
```

<a id="a81bd809a734b6cdde2d55e0b23e41237"></a>

### `t_fcs_times_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities::t_fcs_times_supported
```

<a id="a115ffe697da3e09ece4091493fa8f2da"></a>

### `t_ip1_times_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities::t_ip1_times_supported
```

<a id="a88a4277c5dea41b8171c33c85ed760bf"></a>

### `t_ip2_times_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities::t_ip2_times_supported
```

<a id="ab026e5abfdead47eca1c5d8d316bc62c"></a>

### `t_pm_times_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities::t_pm_times_supported
```

<a id="ad07b464737c59b33de4c89948d4c5686"></a>

### `t_sw_time_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::t_sw_time_supported
```

<a id="a1806f2f5ec2738b026453bbdb8b38ce9"></a>

### `tx_snr_capability`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities::tx_snr_capability
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 364.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P363_bt_hci_rp_le_read_local_rpa_结构体.md) · [返回大纲](大纲.md) · [下一章](P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md)
