---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-243
title: bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第243章\_bt\_hci\_evt\_le\_cs\_read\_remote\_supported\_capabilities\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__cs__read__remote__supported__capabilities__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 243.1\_数据成员（Data Fields）

<a id="r_a40980265955d4d58a9b5407ff845fde4"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a40980265955d4d58a9b5407ff845fde4)。

<a id="r_a4f8fe99c2392c06125ba94e61aed0e6c"></a>

```c
uint16_t conn_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_handle](#a4f8fe99c2392c06125ba94e61aed0e6c)。

<a id="r_ab09a466b2a9a0be5f5021f1da0d7393a"></a>

```c
uint8_t num_config_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_config_supported](#ab09a466b2a9a0be5f5021f1da0d7393a)。

<a id="r_ac73a8bf5425c80739e84cb30ce94f3e7"></a>

```c
uint16_t max_consecutive_procedures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_consecutive_procedures_supported](#ac73a8bf5425c80739e84cb30ce94f3e7)。

<a id="r_adcf35e055d04775c444fa28655b95337"></a>

```c
uint8_t num_antennas_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_antennas_supported](#adcf35e055d04775c444fa28655b95337)。

<a id="r_a50ad0408019dce16685215c6a1b6d0ef"></a>

```c
uint8_t max_antenna_paths_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_antenna_paths_supported](#a50ad0408019dce16685215c6a1b6d0ef)。

<a id="r_a99f9f7b08de6b41e88cea10ba0ca6010"></a>

```c
uint8_t roles_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[roles_supported](#a99f9f7b08de6b41e88cea10ba0ca6010)。

<a id="r_ab7a35b1093ece7ae9cc5def4a3e473b2"></a>

```c
uint8_t modes_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[modes_supported](#ab7a35b1093ece7ae9cc5def4a3e473b2)。

<a id="r_ace95740224b31c127f5e13550cb5a23a"></a>

```c
uint8_t rtt_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_capability](#ace95740224b31c127f5e13550cb5a23a)。

<a id="r_a843968ec69106d076596e110407d8a1a"></a>

```c
uint8_t rtt_aa_only_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_aa_only_n](#a843968ec69106d076596e110407d8a1a)。

<a id="r_a7f796e2eda8d3c7eae556932e37cd93d"></a>

```c
uint8_t rtt_sounding_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_sounding_n](#a7f796e2eda8d3c7eae556932e37cd93d)。

<a id="r_a3f275ad58ca745347172ad0b89faf2c4"></a>

```c
uint8_t rtt_random_payload_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_random_payload_n](#a3f275ad58ca745347172ad0b89faf2c4)。

<a id="r_adebb5328c7baeaa786bc185fec432e40"></a>

```c
uint16_t nadm_sounding_capability
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nadm_sounding_capability](#adebb5328c7baeaa786bc185fec432e40)。

<a id="r_a7af3067f319be094af31512d4ee5101e"></a>

```c
uint16_t nadm_random_capability
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nadm_random_capability](#a7af3067f319be094af31512d4ee5101e)。

<a id="r_a1f303dc3aa8a23fccde27a2d2f64d732"></a>

```c
uint8_t cs_sync_phys_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_sync_phys_supported](#a1f303dc3aa8a23fccde27a2d2f64d732)。

<a id="r_ac83543c17606e401d919fce841a12c6c"></a>

```c
uint16_t subfeatures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subfeatures_supported](#ac83543c17606e401d919fce841a12c6c)。

<a id="r_ad330adf1ae5b9b84756d36801a4cf289"></a>

```c
uint16_t t_ip1_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip1_times_supported](#ad330adf1ae5b9b84756d36801a4cf289)。

<a id="r_a0a1d9dcdf184e49349e86980da2e4bed"></a>

```c
uint16_t t_ip2_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip2_times_supported](#a0a1d9dcdf184e49349e86980da2e4bed)。

<a id="r_a44869fd19ae813830e38f6e4b88dbb1d"></a>

```c
uint16_t t_fcs_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_fcs_times_supported](#a44869fd19ae813830e38f6e4b88dbb1d)。

<a id="r_afef9f37784d75f54521793f07b5baece"></a>

```c
uint16_t t_pm_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_pm_times_supported](#afef9f37784d75f54521793f07b5baece)。

<a id="r_a21a322fc8efd0c410dda78e2652d506d"></a>

```c
uint8_t t_sw_time_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_time_supported](#a21a322fc8efd0c410dda78e2652d506d)。

<a id="r_ae3d06bce4df7a2ca07c5d6dd01124743"></a>

```c
uint8_t tx_snr_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_snr_capability](#ae3d06bce4df7a2ca07c5d6dd01124743)。

## 243.2\_详细说明（Detailed Documentation）

<a id="a4f8fe99c2392c06125ba94e61aed0e6c"></a>

### `conn_handle`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::conn_handle
```

<a id="a1f303dc3aa8a23fccde27a2d2f64d732"></a>

### `cs_sync_phys_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::cs_sync_phys_supported
```

<a id="a50ad0408019dce16685215c6a1b6d0ef"></a>

### `max_antenna_paths_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::max_antenna_paths_supported
```

<a id="ac73a8bf5425c80739e84cb30ce94f3e7"></a>

### `max_consecutive_procedures_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::max_consecutive_procedures_supported
```

<a id="ab7a35b1093ece7ae9cc5def4a3e473b2"></a>

### `modes_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::modes_supported
```

<a id="a7af3067f319be094af31512d4ee5101e"></a>

### `nadm_random_capability`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::nadm_random_capability
```

<a id="adebb5328c7baeaa786bc185fec432e40"></a>

### `nadm_sounding_capability`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::nadm_sounding_capability
```

<a id="adcf35e055d04775c444fa28655b95337"></a>

### `num_antennas_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::num_antennas_supported
```

<a id="ab09a466b2a9a0be5f5021f1da0d7393a"></a>

### `num_config_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::num_config_supported
```

<a id="a99f9f7b08de6b41e88cea10ba0ca6010"></a>

### `roles_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::roles_supported
```

<a id="a843968ec69106d076596e110407d8a1a"></a>

### `rtt_aa_only_n`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::rtt_aa_only_n
```

<a id="ace95740224b31c127f5e13550cb5a23a"></a>

### `rtt_capability`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::rtt_capability
```

<a id="a3f275ad58ca745347172ad0b89faf2c4"></a>

### `rtt_random_payload_n`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::rtt_random_payload_n
```

<a id="a7f796e2eda8d3c7eae556932e37cd93d"></a>

### `rtt_sounding_n`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::rtt_sounding_n
```

<a id="a40980265955d4d58a9b5407ff845fde4"></a>

### `status`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::status
```

<a id="ac83543c17606e401d919fce841a12c6c"></a>

### `subfeatures_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::subfeatures_supported
```

<a id="a44869fd19ae813830e38f6e4b88dbb1d"></a>

### `t_fcs_times_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::t_fcs_times_supported
```

<a id="ad330adf1ae5b9b84756d36801a4cf289"></a>

### `t_ip1_times_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::t_ip1_times_supported
```

<a id="a0a1d9dcdf184e49349e86980da2e4bed"></a>

### `t_ip2_times_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::t_ip2_times_supported
```

<a id="afef9f37784d75f54521793f07b5baece"></a>

### `t_pm_times_supported`

```c
uint16_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::t_pm_times_supported
```

<a id="a21a322fc8efd0c410dda78e2652d506d"></a>

### `t_sw_time_supported`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::t_sw_time_supported
```

<a id="ae3d06bce4df7a2ca07c5d6dd01124743"></a>

### `tx_snr_capability`

```c
uint8_t bt_hci_evt_le_cs_read_remote_supported_capabilities_complete::tx_snr_capability
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 243.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P242_bt_hci_evt_le_cs_read_remote_fae_table_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md)
