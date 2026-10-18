---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-244
title: bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第244章\_bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

低功耗信道探测读取远端支持能力完成（LE CS Read Remote Supported Capabilities Complete，v2）的 HCI 事件参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

低功耗信道探测读取远端支持能力完成（LE CS Read Remote Supported Capabilities Complete，v2）的 HCI 事件参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 244.1\_数据成员（Data Fields）

<a id="r_a8695548057df5e398f65de93fd097b04"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a8695548057df5e398f65de93fd097b04)。

状态（Status）。

<a id="r_adb3ce0c00b922e72373a93cb5d0f2f1f"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#adb3ce0c00b922e72373a93cb5d0f2f1f)。

连接句柄（Connection Handle）。

<a id="r_ab21b4a5b2e3005fc3589251c7b8f77f1"></a>

```c
uint8_t num_config_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_config_supported](#ab21b4a5b2e3005fc3589251c7b8f77f1)。

支持的信道探测（Channel Sounding，CS）配置数量。

<a id="r_a9e2a36e0181a8cf5a9d61b8b31e21617"></a>

```c
uint16_t max_consecutive_procedures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_consecutive_procedures_supported](#a9e2a36e0181a8cf5a9d61b8b31e21617)。

支持的最大连续过程数量（Maximum Consecutive Procedures）。

<a id="r_ad1f03a6a550a5c5cb9b0c997c239ba6a"></a>

```c
uint8_t num_antennas_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_antennas_supported](#ad1f03a6a550a5c5cb9b0c997c239ba6a)。

支持的天线数量。

<a id="r_ac130ecc14ce78f0c179ad56a1985d60c"></a>

```c
uint8_t max_antenna_paths_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_antenna_paths_supported](#ac130ecc14ce78f0c179ad56a1985d60c)。

支持的最大天线路径数量（Antenna Paths）。

<a id="r_a2e7d55a93000730a565c93b3394186e3"></a>

```c
uint8_t roles_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[roles_supported](#a2e7d55a93000730a565c93b3394186e3)。

支持的角色（Roles）。

<a id="r_aa78b03177bbfc69de0a066f610b1cfa6"></a>

```c
uint8_t modes_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[modes_supported](#aa78b03177bbfc69de0a066f610b1cfa6)。

支持的模式（Modes）。

<a id="r_aba890de001e752b497bc91bd6356c359"></a>

```c
uint8_t rtt_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_capability](#aba890de001e752b497bc91bd6356c359)。

往返时间（Round-Trip Time，RTT）能力。

<a id="r_ae8091780f4153ead9a9414593b648f5a"></a>

```c
uint8_t rtt_aa_only_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_aa_only_n](#ae8091780f4153ead9a9414593b648f5a)。

仅使用访问地址的 RTT N 参数（RTT AA-only N）。

<a id="r_ab93bb486d50a79c34a6002885436605b"></a>

```c
uint8_t rtt_sounding_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_sounding_n](#ab93bb486d50a79c34a6002885436605b)。

RTT 探测 N 参数（RTT Sounding N）。

<a id="r_a73b7054a056ca3256098608e565033b2"></a>

```c
uint8_t rtt_random_payload_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_random_payload_n](#a73b7054a056ca3256098608e565033b2)。

RTT 随机载荷 N 参数（RTT Random Payload N）。

<a id="r_a43a8dd8b09c9e498b64798fcfe73af53"></a>

```c
uint16_t nadm_sounding_capability
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nadm_sounding_capability](#a43a8dd8b09c9e498b64798fcfe73af53)。

归一化攻击检测度量（Normalized Attack Detector Metric，NADM）的探测能力（Sounding Capability）。

<a id="r_a974007b9f1d81991f55c40cb1da1c51e"></a>

```c
uint16_t nadm_random_capability
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nadm_random_capability](#a974007b9f1d81991f55c40cb1da1c51e)。

NADM 随机能力（Random Capability）。

<a id="r_aff9e1f081101d2eabc83a7a2ce99d64f"></a>

```c
uint8_t cs_sync_phys_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_sync_phys_supported](#aff9e1f081101d2eabc83a7a2ce99d64f)。

支持的 CS 同步物理层（CS Sync PHYs）。

<a id="r_abe01a9d4d6fdb042fdfa5c045ac66519"></a>

```c
uint16_t subfeatures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subfeatures_supported](#abe01a9d4d6fdb042fdfa5c045ac66519)。

支持的子功能（Subfeatures）。

<a id="r_ab692972f1388e6641493a5cc0faf2fac"></a>

```c
uint16_t t_ip1_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip1_times_supported](#ab692972f1388e6641493a5cc0faf2fac)。

支持的 `T_IP1` 时间。

<a id="r_aa3e4e049cbb322a35171686635e2cc9c"></a>

```c
uint16_t t_ip2_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip2_times_supported](#aa3e4e049cbb322a35171686635e2cc9c)。

支持的 `T_IP2` 时间。

<a id="r_a77669a86a0c75439417d4e53629a9cfd"></a>

```c
uint16_t t_fcs_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_fcs_times_supported](#a77669a86a0c75439417d4e53629a9cfd)。

支持的 `T_FCS` 时间。

<a id="r_ad5c7c16d0b2096d4c00156800bf9181b"></a>

```c
uint16_t t_pm_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_pm_times_supported](#ad5c7c16d0b2096d4c00156800bf9181b)。

支持的 `T_PM` 时间。

<a id="r_a0c60c0b2677a8635a185277453db9613"></a>

```c
uint8_t t_sw_time_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_time_supported](#a0c60c0b2677a8635a185277453db9613)。

支持的 `T_SW` 时间。

<a id="r_a07642a2edeb882e5c9a2a7727e8a55fd"></a>

```c
uint8_t tx_snr_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_snr_capability](#a07642a2edeb882e5c9a2a7727e8a55fd)。

发送信噪比能力（TX SNR Capability）。

<a id="r_a365c4afcf1c034bb42c24ce4bedbf1c3"></a>

```c
uint16_t t_ip2_ipt_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip2_ipt_times_supported](#a365c4afcf1c034bb42c24ce4bedbf1c3)。

支持的 `T_IP2 IPT` 时间。

<a id="r_af7f35ce7c16fc7cf1d76be1450d4566c"></a>

```c
uint8_t t_sw_ipt_time_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_ipt_time_supported](#af7f35ce7c16fc7cf1d76be1450d4566c)。

支持的 `T_SW IPT` 时间。

## 244.2\_详细说明（Detailed Documentation）

<a id="adb3ce0c00b922e72373a93cb5d0f2f1f"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::conn_handle
```

连接句柄（Connection Handle）。

<a id="aff9e1f081101d2eabc83a7a2ce99d64f"></a>

### `cs_sync_phys_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::cs_sync_phys_supported
```

支持的 CS 同步物理层（CS Sync PHYs）。

<a id="ac130ecc14ce78f0c179ad56a1985d60c"></a>

### `max_antenna_paths_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::max_antenna_paths_supported
```

支持的最大天线路径数量（Antenna Paths）。

<a id="a9e2a36e0181a8cf5a9d61b8b31e21617"></a>

### `max_consecutive_procedures_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::max_consecutive_procedures_supported
```

支持的最大连续过程数量（Maximum Consecutive Procedures）。

<a id="aa78b03177bbfc69de0a066f610b1cfa6"></a>

### `modes_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::modes_supported
```

支持的模式（Modes）。

<a id="a974007b9f1d81991f55c40cb1da1c51e"></a>

### `nadm_random_capability`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::nadm_random_capability
```

NADM 随机能力（Random Capability）。

<a id="a43a8dd8b09c9e498b64798fcfe73af53"></a>

### `nadm_sounding_capability`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::nadm_sounding_capability
```

归一化攻击检测度量（Normalized Attack Detector Metric，NADM）的探测能力（Sounding Capability）。

<a id="ad1f03a6a550a5c5cb9b0c997c239ba6a"></a>

### `num_antennas_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::num_antennas_supported
```

支持的天线数量。

<a id="ab21b4a5b2e3005fc3589251c7b8f77f1"></a>

### `num_config_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::num_config_supported
```

支持的信道探测（Channel Sounding，CS）配置数量。

<a id="a2e7d55a93000730a565c93b3394186e3"></a>

### `roles_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::roles_supported
```

支持的角色（Roles）。

<a id="ae8091780f4153ead9a9414593b648f5a"></a>

### `rtt_aa_only_n`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::rtt_aa_only_n
```

仅使用访问地址的 RTT N 参数（RTT AA-only N）。

<a id="aba890de001e752b497bc91bd6356c359"></a>

### `rtt_capability`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::rtt_capability
```

往返时间（Round-Trip Time，RTT）能力。

<a id="a73b7054a056ca3256098608e565033b2"></a>

### `rtt_random_payload_n`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::rtt_random_payload_n
```

RTT 随机载荷 N 参数（RTT Random Payload N）。

<a id="ab93bb486d50a79c34a6002885436605b"></a>

### `rtt_sounding_n`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::rtt_sounding_n
```

RTT 探测 N 参数（RTT Sounding N）。

<a id="a8695548057df5e398f65de93fd097b04"></a>

### `status`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::status
```

状态（Status）。

<a id="abe01a9d4d6fdb042fdfa5c045ac66519"></a>

### `subfeatures_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::subfeatures_supported
```

支持的子功能（Subfeatures）。

<a id="a77669a86a0c75439417d4e53629a9cfd"></a>

### `t_fcs_times_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_fcs_times_supported
```

支持的 `T_FCS` 时间。

<a id="ab692972f1388e6641493a5cc0faf2fac"></a>

### `t_ip1_times_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_ip1_times_supported
```

支持的 `T_IP1` 时间。

<a id="a365c4afcf1c034bb42c24ce4bedbf1c3"></a>

### `t_ip2_ipt_times_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_ip2_ipt_times_supported
```

支持的 `T_IP2 IPT` 时间。

<a id="aa3e4e049cbb322a35171686635e2cc9c"></a>

### `t_ip2_times_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_ip2_times_supported
```

支持的 `T_IP2` 时间。

<a id="ad5c7c16d0b2096d4c00156800bf9181b"></a>

### `t_pm_times_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_pm_times_supported
```

支持的 `T_PM` 时间。

<a id="af7f35ce7c16fc7cf1d76be1450d4566c"></a>

### `t_sw_ipt_time_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_sw_ipt_time_supported
```

支持的 `T_SW IPT` 时间。

<a id="a0c60c0b2677a8635a185277453db9613"></a>

### `t_sw_time_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::t_sw_time_supported
```

支持的 `T_SW` 时间。

<a id="a07642a2edeb882e5c9a2a7727e8a55fd"></a>

### `tx_snr_capability`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2::tx_snr_capability
```

发送信噪比能力（TX SNR Capability）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 244.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P245_bt_hci_evt_le_cs_security_enable_complete_结构体.md)
