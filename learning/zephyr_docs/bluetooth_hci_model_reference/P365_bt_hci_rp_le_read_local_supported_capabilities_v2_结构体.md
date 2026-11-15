---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-365
title: bt_hci_rp_le_read_local_supported_capabilities_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__local__supported__capabilities__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第365章\_bt\_hci\_rp\_le\_read\_local\_supported\_capabilities\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__local__supported__capabilities__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

低功耗读取本地支持能力（LE Read Local Supported Capabilities，v2）命令的 HCI 响应参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

低功耗读取本地支持能力（LE Read Local Supported Capabilities，v2）命令的 HCI 响应参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 365.1\_数据成员（Data Fields）

<a id="r_a4fbd5c95fd7f2f9131cd16ff04e64adf"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a4fbd5c95fd7f2f9131cd16ff04e64adf)。

状态（Status）。

<a id="r_a7d3faf86b443db272303d3b4ad45df2d"></a>

```c
uint8_t num_config_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_config_supported](#a7d3faf86b443db272303d3b4ad45df2d)。

支持的信道探测（Channel Sounding，CS）配置数量。

<a id="r_a998504553ee046759214d0d220d8a3d3"></a>

```c
uint16_t max_consecutive_procedures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_consecutive_procedures_supported](#a998504553ee046759214d0d220d8a3d3)。

支持的最大连续过程数量（Maximum Consecutive Procedures）。

<a id="r_af21e203e96302114a411d9995cd63fa6"></a>

```c
uint8_t num_antennas_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_antennas_supported](#af21e203e96302114a411d9995cd63fa6)。

支持的天线数量。

<a id="r_a3307caaaf76bfc5cb1c88937ce788efd"></a>

```c
uint8_t max_antenna_paths_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_antenna_paths_supported](#a3307caaaf76bfc5cb1c88937ce788efd)。

支持的最大天线路径数量（Antenna Paths）。

<a id="r_a7e061a636d3d0432ca9eb65e69a44710"></a>

```c
uint8_t roles_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[roles_supported](#a7e061a636d3d0432ca9eb65e69a44710)。

支持的角色（Roles）。

<a id="r_a7131d361abdc12c29a886e338075ae8a"></a>

```c
uint8_t modes_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[modes_supported](#a7131d361abdc12c29a886e338075ae8a)。

支持的模式（Modes）。

<a id="r_afc6a9b21d8926b589cf25941e75ecb31"></a>

```c
uint8_t rtt_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_capability](#afc6a9b21d8926b589cf25941e75ecb31)。

往返时间（Round-Trip Time，RTT）能力。

<a id="r_a29667f70ea84458e304fe731d443e25a"></a>

```c
uint8_t rtt_aa_only_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_aa_only_n](#a29667f70ea84458e304fe731d443e25a)。

仅使用访问地址的 RTT N 参数（RTT AA-only N）。

<a id="r_a145d8fe34f80df9367105d1cfa7b59c1"></a>

```c
uint8_t rtt_sounding_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_sounding_n](#a145d8fe34f80df9367105d1cfa7b59c1)。

RTT 探测 N 参数（RTT Sounding N）。

<a id="r_a7cc90e1e81657d0b755df281ba6806fc"></a>

```c
uint8_t rtt_random_payload_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_random_payload_n](#a7cc90e1e81657d0b755df281ba6806fc)。

RTT 随机载荷 N 参数（RTT Random Payload N）。

<a id="r_a36f4762d9053476e84088fe8807024a3"></a>

```c
uint16_t nadm_sounding_capability
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nadm_sounding_capability](#a36f4762d9053476e84088fe8807024a3)。

归一化攻击检测度量（Normalized Attack Detector Metric，NADM）的探测能力（Sounding Capability）。

<a id="r_ae3f61c13562d8dec1812fc3c91c23539"></a>

```c
uint16_t nadm_random_capability
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nadm_random_capability](#ae3f61c13562d8dec1812fc3c91c23539)。

NADM 随机能力（Random Capability）。

<a id="r_acb720ede01b7041c9d5b6d6ade065048"></a>

```c
uint8_t cs_sync_phys_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_sync_phys_supported](#acb720ede01b7041c9d5b6d6ade065048)。

支持的 CS 同步物理层（CS Sync PHYs）。

<a id="r_a28b801d5310e4fd7e8285ba6361191df"></a>

```c
uint16_t subfeatures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subfeatures_supported](#a28b801d5310e4fd7e8285ba6361191df)。

支持的子功能（Subfeatures）。

<a id="r_a8704313f30e256e87460961f03e0719a"></a>

```c
uint16_t t_ip1_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip1_times_supported](#a8704313f30e256e87460961f03e0719a)。

支持的 `T_IP1` 时间。

<a id="r_a1f97298da17187ea1ed96ec923f54523"></a>

```c
uint16_t t_ip2_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip2_times_supported](#a1f97298da17187ea1ed96ec923f54523)。

支持的 `T_IP2` 时间。

<a id="r_a1d2e82062c0c41dce9e7428e4982223a"></a>

```c
uint16_t t_fcs_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_fcs_times_supported](#a1d2e82062c0c41dce9e7428e4982223a)。

支持的 `T_FCS` 时间。

<a id="r_a6a88f321faeea9e61bd38c696468d90f"></a>

```c
uint16_t t_pm_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_pm_times_supported](#a6a88f321faeea9e61bd38c696468d90f)。

支持的 `T_PM` 时间。

<a id="r_a61458332899b95c752b6343eda90013e"></a>

```c
uint8_t t_sw_time_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_time_supported](#a61458332899b95c752b6343eda90013e)。

支持的 `T_SW` 时间。

<a id="r_a2fc5417dbbd91b4099fb4a27f01c18fd"></a>

```c
uint8_t tx_snr_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_snr_capability](#a2fc5417dbbd91b4099fb4a27f01c18fd)。

发送信噪比能力（TX SNR Capability）。

<a id="r_ac000a669ee53e1ca4ad99fd350fe72e6"></a>

```c
uint16_t t_ip2_ipt_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip2_ipt_times_supported](#ac000a669ee53e1ca4ad99fd350fe72e6)。

支持的 `T_IP2 IPT` 时间。

<a id="r_a2c51d311adcacada33b9dec7b4395865"></a>

```c
uint8_t t_sw_ipt_time_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_ipt_time_supported](#a2c51d311adcacada33b9dec7b4395865)。

支持的 `T_SW IPT` 时间。

## 365.2\_详细说明（Detailed Documentation）

<a id="acb720ede01b7041c9d5b6d6ade065048"></a>

### `cs_sync_phys_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::cs_sync_phys_supported
```

支持的 CS 同步物理层（CS Sync PHYs）。

<a id="a3307caaaf76bfc5cb1c88937ce788efd"></a>

### `max_antenna_paths_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::max_antenna_paths_supported
```

支持的最大天线路径数量（Antenna Paths）。

<a id="a998504553ee046759214d0d220d8a3d3"></a>

### `max_consecutive_procedures_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities_v2::max_consecutive_procedures_supported
```

支持的最大连续过程数量（Maximum Consecutive Procedures）。

<a id="a7131d361abdc12c29a886e338075ae8a"></a>

### `modes_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::modes_supported
```

支持的模式（Modes）。

<a id="ae3f61c13562d8dec1812fc3c91c23539"></a>

### `nadm_random_capability`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities_v2::nadm_random_capability
```

NADM 随机能力（Random Capability）。

<a id="a36f4762d9053476e84088fe8807024a3"></a>

### `nadm_sounding_capability`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities_v2::nadm_sounding_capability
```

归一化攻击检测度量（Normalized Attack Detector Metric，NADM）的探测能力（Sounding Capability）。

<a id="af21e203e96302114a411d9995cd63fa6"></a>

### `num_antennas_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::num_antennas_supported
```

支持的天线数量。

<a id="a7d3faf86b443db272303d3b4ad45df2d"></a>

### `num_config_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::num_config_supported
```

支持的信道探测（Channel Sounding，CS）配置数量。

<a id="a7e061a636d3d0432ca9eb65e69a44710"></a>

### `roles_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::roles_supported
```

支持的角色（Roles）。

<a id="a29667f70ea84458e304fe731d443e25a"></a>

### `rtt_aa_only_n`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::rtt_aa_only_n
```

仅使用访问地址的 RTT N 参数（RTT AA-only N）。

<a id="afc6a9b21d8926b589cf25941e75ecb31"></a>

### `rtt_capability`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::rtt_capability
```

往返时间（Round-Trip Time，RTT）能力。

<a id="a7cc90e1e81657d0b755df281ba6806fc"></a>

### `rtt_random_payload_n`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::rtt_random_payload_n
```

RTT 随机载荷 N 参数（RTT Random Payload N）。

<a id="a145d8fe34f80df9367105d1cfa7b59c1"></a>

### `rtt_sounding_n`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::rtt_sounding_n
```

RTT 探测 N 参数（RTT Sounding N）。

<a id="a4fbd5c95fd7f2f9131cd16ff04e64adf"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::status
```

状态（Status）。

<a id="a28b801d5310e4fd7e8285ba6361191df"></a>

### `subfeatures_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities_v2::subfeatures_supported
```

支持的子功能（Subfeatures）。

<a id="a1d2e82062c0c41dce9e7428e4982223a"></a>

### `t_fcs_times_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities_v2::t_fcs_times_supported
```

支持的 `T_FCS` 时间。

<a id="a8704313f30e256e87460961f03e0719a"></a>

### `t_ip1_times_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities_v2::t_ip1_times_supported
```

支持的 `T_IP1` 时间。

<a id="ac000a669ee53e1ca4ad99fd350fe72e6"></a>

### `t_ip2_ipt_times_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities_v2::t_ip2_ipt_times_supported
```

支持的 `T_IP2 IPT` 时间。

<a id="a1f97298da17187ea1ed96ec923f54523"></a>

### `t_ip2_times_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities_v2::t_ip2_times_supported
```

支持的 `T_IP2` 时间。

<a id="a6a88f321faeea9e61bd38c696468d90f"></a>

### `t_pm_times_supported`

```c
uint16_t bt_hci_rp_le_read_local_supported_capabilities_v2::t_pm_times_supported
```

支持的 `T_PM` 时间。

<a id="a2c51d311adcacada33b9dec7b4395865"></a>

### `t_sw_ipt_time_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::t_sw_ipt_time_supported
```

支持的 `T_SW IPT` 时间。

<a id="a61458332899b95c752b6343eda90013e"></a>

### `t_sw_time_supported`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::t_sw_time_supported
```

支持的 `T_SW` 时间。

<a id="a2fc5417dbbd91b4099fb4a27f01c18fd"></a>

### `tx_snr_capability`

```c
uint8_t bt_hci_rp_le_read_local_supported_capabilities_v2::tx_snr_capability
```

发送信噪比能力（TX SNR Capability）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 365.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md) · [返回大纲](大纲.md) · [下一章](P366_bt_hci_rp_le_read_max_adv_data_len_结构体.md)
