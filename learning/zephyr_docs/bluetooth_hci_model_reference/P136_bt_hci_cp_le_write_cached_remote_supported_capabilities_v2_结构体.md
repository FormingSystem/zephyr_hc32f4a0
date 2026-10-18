---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-136
title: bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__write__cached__remote__supported__capabilities__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第136章\_bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__write__cached__remote__supported__capabilities__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

低功耗信道探测写入已缓存远端支持能力（LE CS Write Cached Remote Supported Capabilities，v2）的 HCI 命令参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

低功耗信道探测写入已缓存远端支持能力（LE CS Write Cached Remote Supported Capabilities，v2）的 HCI 命令参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 136.1\_数据成员（Data Fields）

<a id="r_ac599d7323d560b8f554bbaaf70aabd8b"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#ac599d7323d560b8f554bbaaf70aabd8b)。

连接句柄（Connection Handle）。

<a id="r_a65a5b6ebdbc5793ca800ee202cb4676c"></a>

```c
uint8_t num_config_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_config_supported](#a65a5b6ebdbc5793ca800ee202cb4676c)。

支持的信道探测（Channel Sounding，CS）配置数量。

<a id="r_aead25f8f371ed85e66d05af852b90a9e"></a>

```c
uint16_t max_consecutive_procedures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_consecutive_procedures_supported](#aead25f8f371ed85e66d05af852b90a9e)。

支持的最大连续过程数量（Maximum Consecutive Procedures）。

<a id="r_a6bb274c4c2ff4dc2c6136b0bc7515be3"></a>

```c
uint8_t num_antennas_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_antennas_supported](#a6bb274c4c2ff4dc2c6136b0bc7515be3)。

支持的天线数量。

<a id="r_ad7c6799d86889b67d86ca44bac4238a6"></a>

```c
uint8_t max_antenna_paths_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_antenna_paths_supported](#ad7c6799d86889b67d86ca44bac4238a6)。

支持的最大天线路径数量（Antenna Paths）。

<a id="r_a6eff7fb52e3ef1074eb875af4c79a8aa"></a>

```c
uint8_t roles_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[roles_supported](#a6eff7fb52e3ef1074eb875af4c79a8aa)。

支持的角色（Roles）。

<a id="r_a1ff4fede6b4d942f64ec2b94b222703b"></a>

```c
uint8_t modes_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[modes_supported](#a1ff4fede6b4d942f64ec2b94b222703b)。

支持的模式（Modes）。

<a id="r_a0872c2a5399e1d82f334796dd35379ad"></a>

```c
uint8_t rtt_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_capability](#a0872c2a5399e1d82f334796dd35379ad)。

往返时间（Round-Trip Time，RTT）能力。

<a id="r_a17d3094a1b93665e755b2111074de42c"></a>

```c
uint8_t rtt_aa_only_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_aa_only_n](#a17d3094a1b93665e755b2111074de42c)。

仅使用访问地址的 RTT N 参数（RTT AA-only N）。

<a id="r_ad342355fdc6396d6680b7e215ef4b16e"></a>

```c
uint8_t rtt_sounding_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_sounding_n](#ad342355fdc6396d6680b7e215ef4b16e)。

RTT 探测 N 参数（RTT Sounding N）。

<a id="r_a214f693e10c331091e34f09c2cfc9749"></a>

```c
uint8_t rtt_random_payload_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_random_payload_n](#a214f693e10c331091e34f09c2cfc9749)。

RTT 随机载荷 N 参数（RTT Random Payload N）。

<a id="r_a225720841ea95409879d51bd9a031fb7"></a>

```c
uint16_t nadm_sounding_capability
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nadm_sounding_capability](#a225720841ea95409879d51bd9a031fb7)。

归一化攻击检测度量（Normalized Attack Detector Metric，NADM）的探测能力（Sounding Capability）。

<a id="r_a22f1010c9f4de7902480d3f84d499fb1"></a>

```c
uint16_t nadm_random_capability
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nadm_random_capability](#a22f1010c9f4de7902480d3f84d499fb1)。

NADM 随机能力（Random Capability）。

<a id="r_a2077365a697d7085d7db97fb35c391f4"></a>

```c
uint8_t cs_sync_phys_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_sync_phys_supported](#a2077365a697d7085d7db97fb35c391f4)。

支持的 CS 同步物理层（CS Sync PHYs）。

<a id="r_a2e8693852819f5e4afa8cae90f8ae92c"></a>

```c
uint16_t subfeatures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subfeatures_supported](#a2e8693852819f5e4afa8cae90f8ae92c)。

支持的子功能（Subfeatures）。

<a id="r_ac370abefdc5a7acdf1e3c72093d11018"></a>

```c
uint16_t t_ip1_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip1_times_supported](#ac370abefdc5a7acdf1e3c72093d11018)。

支持的 `T_IP1` 时间。

<a id="r_a8c63e46cf58623b3ca9cbfa7b802744e"></a>

```c
uint16_t t_ip2_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip2_times_supported](#a8c63e46cf58623b3ca9cbfa7b802744e)。

支持的 `T_IP2` 时间。

<a id="r_abf661cac9a1a2a5bf38180dbfc486bcd"></a>

```c
uint16_t t_fcs_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_fcs_times_supported](#abf661cac9a1a2a5bf38180dbfc486bcd)。

支持的 `T_FCS` 时间。

<a id="r_ac930e63945abfc0cdfdaa79164e114fa"></a>

```c
uint16_t t_pm_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_pm_times_supported](#ac930e63945abfc0cdfdaa79164e114fa)。

支持的 `T_PM` 时间。

<a id="r_afbe4805ccd9db70a596afdabb6963885"></a>

```c
uint8_t t_sw_time_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_time_supported](#afbe4805ccd9db70a596afdabb6963885)。

支持的 `T_SW` 时间。

<a id="r_ae757536a884e640451e35dd2fca90605"></a>

```c
uint8_t tx_snr_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_snr_capability](#ae757536a884e640451e35dd2fca90605)。

发送信噪比能力（TX SNR Capability）。

<a id="r_a30cee084044918cb450060a164bd4b30"></a>

```c
uint16_t t_ip2_ipt_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip2_ipt_times_supported](#a30cee084044918cb450060a164bd4b30)。

支持的 `T_IP2 IPT` 时间。

<a id="r_a8aa60cab3469fadd342a0a9b0d1b094f"></a>

```c
uint8_t t_sw_ipt_time_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_ipt_time_supported](#a8aa60cab3469fadd342a0a9b0d1b094f)。

支持的 `T_SW IPT` 时间。

## 136.2\_详细说明（Detailed Documentation）

<a id="a2077365a697d7085d7db97fb35c391f4"></a>

### `cs_sync_phys_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::cs_sync_phys_supported
```

支持的 CS 同步物理层（CS Sync PHYs）。

<a id="ac599d7323d560b8f554bbaaf70aabd8b"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::handle
```

连接句柄（Connection Handle）。

<a id="ad7c6799d86889b67d86ca44bac4238a6"></a>

### `max_antenna_paths_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::max_antenna_paths_supported
```

支持的最大天线路径数量（Antenna Paths）。

<a id="aead25f8f371ed85e66d05af852b90a9e"></a>

### `max_consecutive_procedures_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::max_consecutive_procedures_supported
```

支持的最大连续过程数量（Maximum Consecutive Procedures）。

<a id="a1ff4fede6b4d942f64ec2b94b222703b"></a>

### `modes_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::modes_supported
```

支持的模式（Modes）。

<a id="a22f1010c9f4de7902480d3f84d499fb1"></a>

### `nadm_random_capability`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::nadm_random_capability
```

NADM 随机能力（Random Capability）。

<a id="a225720841ea95409879d51bd9a031fb7"></a>

### `nadm_sounding_capability`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::nadm_sounding_capability
```

归一化攻击检测度量（Normalized Attack Detector Metric，NADM）的探测能力（Sounding Capability）。

<a id="a6bb274c4c2ff4dc2c6136b0bc7515be3"></a>

### `num_antennas_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::num_antennas_supported
```

支持的天线数量。

<a id="a65a5b6ebdbc5793ca800ee202cb4676c"></a>

### `num_config_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::num_config_supported
```

支持的信道探测（Channel Sounding，CS）配置数量。

<a id="a6eff7fb52e3ef1074eb875af4c79a8aa"></a>

### `roles_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::roles_supported
```

支持的角色（Roles）。

<a id="a17d3094a1b93665e755b2111074de42c"></a>

### `rtt_aa_only_n`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::rtt_aa_only_n
```

仅使用访问地址的 RTT N 参数（RTT AA-only N）。

<a id="a0872c2a5399e1d82f334796dd35379ad"></a>

### `rtt_capability`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::rtt_capability
```

往返时间（Round-Trip Time，RTT）能力。

<a id="a214f693e10c331091e34f09c2cfc9749"></a>

### `rtt_random_payload_n`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::rtt_random_payload_n
```

RTT 随机载荷 N 参数（RTT Random Payload N）。

<a id="ad342355fdc6396d6680b7e215ef4b16e"></a>

### `rtt_sounding_n`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::rtt_sounding_n
```

RTT 探测 N 参数（RTT Sounding N）。

<a id="a2e8693852819f5e4afa8cae90f8ae92c"></a>

### `subfeatures_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::subfeatures_supported
```

支持的子功能（Subfeatures）。

<a id="abf661cac9a1a2a5bf38180dbfc486bcd"></a>

### `t_fcs_times_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_fcs_times_supported
```

支持的 `T_FCS` 时间。

<a id="ac370abefdc5a7acdf1e3c72093d11018"></a>

### `t_ip1_times_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_ip1_times_supported
```

支持的 `T_IP1` 时间。

<a id="a30cee084044918cb450060a164bd4b30"></a>

### `t_ip2_ipt_times_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_ip2_ipt_times_supported
```

支持的 `T_IP2 IPT` 时间。

<a id="a8c63e46cf58623b3ca9cbfa7b802744e"></a>

### `t_ip2_times_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_ip2_times_supported
```

支持的 `T_IP2` 时间。

<a id="ac930e63945abfc0cdfdaa79164e114fa"></a>

### `t_pm_times_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_pm_times_supported
```

支持的 `T_PM` 时间。

<a id="a8aa60cab3469fadd342a0a9b0d1b094f"></a>

### `t_sw_ipt_time_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_sw_ipt_time_supported
```

支持的 `T_SW IPT` 时间。

<a id="afbe4805ccd9db70a596afdabb6963885"></a>

### `t_sw_time_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::t_sw_time_supported
```

支持的 `T_SW` 时间。

<a id="ae757536a884e640451e35dd2fca90605"></a>

### `tx_snr_capability`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities_v2::tx_snr_capability
```

发送信噪比能力（TX SNR Capability）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 136.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md) · [返回大纲](大纲.md) · [下一章](P137_bt_hci_cp_le_write_default_data_len_结构体.md)
