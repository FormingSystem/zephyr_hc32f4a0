---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-135
title: bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__write__cached__remote__supported__capabilities.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第135章\_bt\_hci\_cp\_le\_write\_cached\_remote\_supported\_capabilities\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__write__cached__remote__supported__capabilities.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 135.1\_数据成员（Data Fields）

<a id="r_a8a884bca80550eb72a433f5ea280f702"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a8a884bca80550eb72a433f5ea280f702)。

<a id="r_a7a60c326707ebd60b96d25924e3c9e40"></a>

```c
uint8_t num_config_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_config_supported](#a7a60c326707ebd60b96d25924e3c9e40)。

<a id="r_afbfe48ddad696315d6e021a85d32559d"></a>

```c
uint16_t max_consecutive_procedures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_consecutive_procedures_supported](#afbfe48ddad696315d6e021a85d32559d)。

<a id="r_a96b0c7868da711271e74b82fcfd32fc2"></a>

```c
uint8_t num_antennas_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_antennas_supported](#a96b0c7868da711271e74b82fcfd32fc2)。

<a id="r_a96a49382bef8f3163cd82899f59ed5fe"></a>

```c
uint8_t max_antenna_paths_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_antenna_paths_supported](#a96a49382bef8f3163cd82899f59ed5fe)。

<a id="r_ae88cf07e3c8e6ad64a1beb60270d8961"></a>

```c
uint8_t roles_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[roles_supported](#ae88cf07e3c8e6ad64a1beb60270d8961)。

<a id="r_a93f4973a1229273c51f6a20e741e42ed"></a>

```c
uint8_t modes_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[modes_supported](#a93f4973a1229273c51f6a20e741e42ed)。

<a id="r_a94fb0f963f706c303729d7a0088ef617"></a>

```c
uint8_t rtt_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_capability](#a94fb0f963f706c303729d7a0088ef617)。

<a id="r_ae4b9b8ba0e83978f131541959062f691"></a>

```c
uint8_t rtt_aa_only_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_aa_only_n](#ae4b9b8ba0e83978f131541959062f691)。

<a id="r_a31c877363bd315786ef834215614d346"></a>

```c
uint8_t rtt_sounding_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_sounding_n](#a31c877363bd315786ef834215614d346)。

<a id="r_a8f98235e9238a80602806fb60e1261bb"></a>

```c
uint8_t rtt_random_payload_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_random_payload_n](#a8f98235e9238a80602806fb60e1261bb)。

<a id="r_a29781bbe7e25c39b06047725f1d11426"></a>

```c
uint16_t nadm_sounding_capability
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nadm_sounding_capability](#a29781bbe7e25c39b06047725f1d11426)。

<a id="r_a25faaf2be6db05c44256b9f559841c87"></a>

```c
uint16_t nadm_random_capability
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nadm_random_capability](#a25faaf2be6db05c44256b9f559841c87)。

<a id="r_a908322e5c02500abbdd8891c5248998d"></a>

```c
uint8_t cs_sync_phys_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_sync_phys_supported](#a908322e5c02500abbdd8891c5248998d)。

<a id="r_a2b5c828a30525eee5b1ce48f3ba98896"></a>

```c
uint16_t subfeatures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subfeatures_supported](#a2b5c828a30525eee5b1ce48f3ba98896)。

<a id="r_a257b38d937c1111a66f6c28f1e221211"></a>

```c
uint16_t t_ip1_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip1_times_supported](#a257b38d937c1111a66f6c28f1e221211)。

<a id="r_a0911e19deceb7f243ac706ddb4cf0a3a"></a>

```c
uint16_t t_ip2_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip2_times_supported](#a0911e19deceb7f243ac706ddb4cf0a3a)。

<a id="r_af959f1539f5bbf74b0e63db743a132f4"></a>

```c
uint16_t t_fcs_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_fcs_times_supported](#af959f1539f5bbf74b0e63db743a132f4)。

<a id="r_a870e068fcc15dd44dca3ac24334000ee"></a>

```c
uint16_t t_pm_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_pm_times_supported](#a870e068fcc15dd44dca3ac24334000ee)。

<a id="r_ab77f7bda7302cad94805e8ea43b8bf14"></a>

```c
uint8_t t_sw_time_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_time_supported](#ab77f7bda7302cad94805e8ea43b8bf14)。

<a id="r_aa9e48c6f0d22e9a64e8591a34409988e"></a>

```c
uint8_t tx_snr_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_snr_capability](#aa9e48c6f0d22e9a64e8591a34409988e)。

## 135.2\_详细说明（Detailed Documentation）

<a id="a908322e5c02500abbdd8891c5248998d"></a>

### `cs_sync_phys_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities::cs_sync_phys_supported
```

<a id="a8a884bca80550eb72a433f5ea280f702"></a>

### `handle`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities::handle
```

<a id="a96a49382bef8f3163cd82899f59ed5fe"></a>

### `max_antenna_paths_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities::max_antenna_paths_supported
```

<a id="afbfe48ddad696315d6e021a85d32559d"></a>

### `max_consecutive_procedures_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities::max_consecutive_procedures_supported
```

<a id="a93f4973a1229273c51f6a20e741e42ed"></a>

### `modes_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities::modes_supported
```

<a id="a25faaf2be6db05c44256b9f559841c87"></a>

### `nadm_random_capability`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities::nadm_random_capability
```

<a id="a29781bbe7e25c39b06047725f1d11426"></a>

### `nadm_sounding_capability`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities::nadm_sounding_capability
```

<a id="a96b0c7868da711271e74b82fcfd32fc2"></a>

### `num_antennas_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities::num_antennas_supported
```

<a id="a7a60c326707ebd60b96d25924e3c9e40"></a>

### `num_config_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities::num_config_supported
```

<a id="ae88cf07e3c8e6ad64a1beb60270d8961"></a>

### `roles_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities::roles_supported
```

<a id="ae4b9b8ba0e83978f131541959062f691"></a>

### `rtt_aa_only_n`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities::rtt_aa_only_n
```

<a id="a94fb0f963f706c303729d7a0088ef617"></a>

### `rtt_capability`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities::rtt_capability
```

<a id="a8f98235e9238a80602806fb60e1261bb"></a>

### `rtt_random_payload_n`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities::rtt_random_payload_n
```

<a id="a31c877363bd315786ef834215614d346"></a>

### `rtt_sounding_n`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities::rtt_sounding_n
```

<a id="a2b5c828a30525eee5b1ce48f3ba98896"></a>

### `subfeatures_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities::subfeatures_supported
```

<a id="af959f1539f5bbf74b0e63db743a132f4"></a>

### `t_fcs_times_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities::t_fcs_times_supported
```

<a id="a257b38d937c1111a66f6c28f1e221211"></a>

### `t_ip1_times_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities::t_ip1_times_supported
```

<a id="a0911e19deceb7f243ac706ddb4cf0a3a"></a>

### `t_ip2_times_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities::t_ip2_times_supported
```

<a id="a870e068fcc15dd44dca3ac24334000ee"></a>

### `t_pm_times_supported`

```c
uint16_t bt_hci_cp_le_write_cached_remote_supported_capabilities::t_pm_times_supported
```

<a id="ab77f7bda7302cad94805e8ea43b8bf14"></a>

### `t_sw_time_supported`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities::t_sw_time_supported
```

<a id="aa9e48c6f0d22e9a64e8591a34409988e"></a>

### `tx_snr_capability`

```c
uint8_t bt_hci_cp_le_write_cached_remote_supported_capabilities::tx_snr_capability
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 135.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P134_bt_hci_cp_le_write_cached_remote_fae_table_结构体.md) · [返回大纲](大纲.md) · [下一章](P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md)
