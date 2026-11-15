---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-14
title: bt_conn_le_cs_capabilities_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__cs__capabilities.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_bt\_conn\_le\_cs\_capabilities\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__cs__capabilities.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

支持信道探测（Channel Sounding，CS）的 LE 连接的远端信道探测能力。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

支持信道探测（Channel Sounding，CS）的 LE 连接的远端信道探测能力。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_a77aacfd02b354e04d4cc29cc1bf4b779"></a>

```c
uint8_t num_config_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_config_supported](#a77aacfd02b354e04d4cc29cc1bf4b779)。

信道探测配置数量（Number of CS configurations）。

<a id="r_ae76fbc0f88525e83717e1d8ef5acae59"></a>

```c
uint16_t max_consecutive_procedures_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_consecutive_procedures_supported](#ae76fbc0f88525e83717e1d8ef5acae59)。

最大连续信道探测过程数量（Maximum consecutive CS procedures）。

<a id="r_a4e4c56c5066d02b2a0cd59c067f1e4b9"></a>

```c
uint8_t num_antennas_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_antennas_supported](#a4e4c56c5066d02b2a0cd59c067f1e4b9)。

天线数量（Number of antennas）。

<a id="r_ac842e123166008ad1ad663f827937a3b"></a>

```c
uint8_t max_antenna_paths_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_antenna_paths_supported](#ac842e123166008ad1ad663f827937a3b)。

最大天线路径数（Maximum antenna paths）。

<a id="r_a6530d2a3fb66d498711856b723acecb7"></a>

```c
bool initiator_supported
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[initiator_supported](#a6530d2a3fb66d498711856b723acecb7)。

发起方角色（Initiator role）。

<a id="r_a694119619d359d0b7e298edf6201ee20"></a>

```c
bool reflector_supported
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[reflector_supported](#a694119619d359d0b7e298edf6201ee20)。

反射方角色（Reflector role）。

<a id="r_aa1616417e6183cf283cf96efc9a92b8e"></a>

```c
bool mode_3_supported
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[mode_3_supported](#aa1616417e6183cf283cf96efc9a92b8e)。

模式 3（Mode-3）。

<a id="r_a46c9168328d3fbc98a2625799c733818"></a>

```c
enum bt_conn_le_cs_capability_rtt_aa_only rtt_aa_only_precision
```

相关声明：[bt_conn_le_cs_capability_rtt_aa_only](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gafe14d64a64383b097760764697b035e2)、[rtt_aa_only_precision](#a46c9168328d3fbc98a2625799c733818)。

仅接入地址的往返时间类型（RTT AA-Only）。

<a id="r_acef0d65ed55ae304fea47006bfb0076f"></a>

```c
enum bt_conn_le_cs_capability_rtt_sounding rtt_sounding_precision
```

相关声明：[bt_conn_le_cs_capability_rtt_sounding](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1892ec23ca3b1818287a9d7dafc16433)、[rtt_sounding_precision](#acef0d65ed55ae304fea47006bfb0076f)。

探测序列往返时间类型（RTT Sounding）。

<a id="r_abbefdc0268a775712c7abd664adcb6b2"></a>

```c
enum bt_conn_le_cs_capability_rtt_random_payload rtt_random_payload_precision
```

相关声明：[bt_conn_le_cs_capability_rtt_random_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5568443825fc1ce9534753d8918aa813)、[rtt_random_payload_precision](#abbefdc0268a775712c7abd664adcb6b2)。

随机载荷往返时间类型（RTT Random Payload）。

<a id="r_abe3c611316bb5f710f355846ee9ec437"></a>

```c
uint8_t rtt_aa_only_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_aa_only_n](#abe3c611316bb5f710f355846ee9ec437)。

达到仅接入地址往返时间（RTT AA Only）精度要求所需的信道探测步骤数量（CS steps）。

<a id="r_a7f35343a1572800850e791ba3ff5ffb1"></a>

```c
uint8_t rtt_sounding_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_sounding_n](#a7f35343a1572800850e791ba3ff5ffb1)。

达到探测序列往返时间（RTT Sounding）精度要求所需的信道探测步骤数量（CS steps）。

<a id="r_a345d9e43222d77024a8f4283b274b48f"></a>

```c
uint8_t rtt_random_payload_n
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rtt_random_payload_n](#a345d9e43222d77024a8f4283b274b48f)。

达到随机载荷往返时间（RTT Random Payload）精度要求所需的信道探测步骤数量（CS steps）。

<a id="r_a94fd00a7a9b22d649f75c7fdd17590a9"></a>

```c
bool phase_based_nadm_sounding_supported
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[phase_based_nadm_sounding_supported](#a94fd00a7a9b22d649f75c7fdd17590a9)。

收到包含探测序列（Sounding sequence）的 `CS_SYNC` 时，基于相位的归一化攻击检测器指标（Phase-based normalized attack detector metric）。

<a id="r_a1a0076a0c97317803976f4aca86afc0d"></a>

```c
bool phase_based_nadm_random_supported
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[phase_based_nadm_random_supported](#a1a0076a0c97317803976f4aca86afc0d)。

收到包含随机序列（Random sequence）的 `CS_SYNC` 时，基于相位的归一化攻击检测器指标（Phase-based normalized attack detector metric）。

<a id="r_a3fd09db5fae9c5e307994a78131199c6"></a>

```c
bool cs_sync_2m_phy_supported
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[cs_sync_2m_phy_supported](#a3fd09db5fae9c5e307994a78131199c6)。

`CS_SYNC` 使用低功耗 2M 物理层（LE 2M PHY）。

<a id="r_a6513d8ffe7d168441205f6dd656dcbbc"></a>

```c
bool cs_sync_2m_2bt_phy_supported
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[cs_sync_2m_2bt_phy_supported](#a6513d8ffe7d168441205f6dd656dcbbc)。

`CS_SYNC` 使用低功耗 2M 2BT 物理层（LE 2M 2BT PHY）。

<a id="r_a22604c052da2f8ccf77c81a0a5c628b7"></a>

```c
bool cs_without_fae_supported
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[cs_without_fae_supported](#a22604c052da2f8ccf77c81a0a5c628b7)。

子特性（Subfeature）：无频率驱动误差的信道探测（CS with no Frequency Actuation Error）。

<a id="r_aba0db15183d4fa4ae0e3f1333202e55e"></a>

```c
bool chsel_alg_3c_supported
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[chsel_alg_3c_supported](#aba0db15183d4fa4ae0e3f1333202e55e)。

子特性（Subfeature）：信道选择算法 3c（Channel Selection Algorithm #3c）。

<a id="r_ad57f15b4dda88e2b747f30451601c923"></a>

```c
bool pbr_from_rtt_sounding_seq_supported
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[pbr_from_rtt_sounding_seq_supported](#ad57f15b4dda88e2b747f30451601c923)。

子特性（Subfeature）：基于往返时间探测序列的相位测距（Phase-based Ranging from RTT sounding sequence）。

<a id="r_adfac38e7771604971a82ece149c1d337"></a>

```c
bool cs_ipt_reflector
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[cs_ipt_reflector](#adfac38e7771604971a82ece149c1d337)。

子特性（Subfeature）：信道探测反射方（CS reflector）中的内联相位校正项传输（Inline PCT Transfer，IPT）。译注：IPT 全称依据[蓝牙官方规范说明](https://www.bluetooth.com/specifications/specs/channel-sounding-inline-phase-correction-term-transfer-2/)。

<a id="r_a090f869cfe7e39a70cea94afbd5ac376"></a>

```c
uint16_t t_ip1_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip1_times_supported](#a090f869cfe7e39a70cea94afbd5ac376)。

信道探测步骤（CS steps）期间可选的 `T_IP1` 持续时间。

<a id="r_ae93594f360430e9c0c80cf3edcf570f6"></a>

```c
uint16_t t_ip2_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip2_times_supported](#ae93594f360430e9c0c80cf3edcf570f6)。

信道探测步骤（CS steps）期间可选的 `T_IP2` 持续时间。

<a id="r_a1ff1d7d769e3ba915f91bf672a6f8a61"></a>

```c
uint16_t t_fcs_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_fcs_times_supported](#a1ff1d7d769e3ba915f91bf672a6f8a61)。

信道探测步骤（CS steps）期间可选的 `T_FCS` 持续时间。

<a id="r_a6e92391b21d4acaebba8a171643f572f"></a>

```c
uint16_t t_pm_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_pm_times_supported](#a6e92391b21d4acaebba8a171643f572f)。

信道探测步骤（CS steps）期间可选的 `T_PM` 持续时间。

<a id="r_a5a86629a5ad4203b5efe3802cd8b6ae7"></a>

```c
uint8_t t_sw_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_time](#a5a86629a5ad4203b5efe3802cd8b6ae7)。

信道探测音调（CS tones）的天线切换周期（Antenna switch period），单位为微秒。

<a id="r_ad58deea7a825bb5f0bc2ca0034183948"></a>

```c
uint8_t tx_snr_capability
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_snr_capability](#ad58deea7a825bb5f0bc2ca0034183948)。

往返时间数据包（RTT packets）支持的信噪比等级（SNR levels）。

<a id="r_a21262b0e588a75146f2d0c325d0b5cc1"></a>

```c
uint16_t t_ip2_ipt_times_supported
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[t_ip2_ipt_times_supported](#a21262b0e588a75146f2d0c325d0b5cc1)。

信道探测步骤（CS steps）期间支持的 `T_IP2_IPT` 持续时间。

<a id="r_a97b42928bcba43a6d90e8139efce0870"></a>

```c
uint8_t t_sw_ipt_time_supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_ipt_time_supported](#a97b42928bcba43a6d90e8139efce0870)。

内联相位校正项传输（Inline PCT Transfer，IPT）期间，信道探测音调（CS tones）支持的天线切换周期，单位为微秒。

## 14.2\_详细说明（Detailed Documentation）

<a id="aba0db15183d4fa4ae0e3f1333202e55e"></a>

### `chsel_alg_3c_supported`

```c
bool bt_conn_le_cs_capabilities::chsel_alg_3c_supported
```

子特性（Subfeature）：信道选择算法 3c（Channel Selection Algorithm #3c）。

<a id="adfac38e7771604971a82ece149c1d337"></a>

### `cs_ipt_reflector`

```c
bool bt_conn_le_cs_capabilities::cs_ipt_reflector
```

子特性（Subfeature）：信道探测反射方（CS reflector）中的内联相位校正项传输（Inline PCT Transfer，IPT）。译注：IPT 全称依据[蓝牙官方规范说明](https://www.bluetooth.com/specifications/specs/channel-sounding-inline-phase-correction-term-transfer-2/)。

<a id="a6513d8ffe7d168441205f6dd656dcbbc"></a>

### `cs_sync_2m_2bt_phy_supported`

```c
bool bt_conn_le_cs_capabilities::cs_sync_2m_2bt_phy_supported
```

`CS_SYNC` 使用低功耗 2M 2BT 物理层（LE 2M 2BT PHY）。

<a id="a3fd09db5fae9c5e307994a78131199c6"></a>

### `cs_sync_2m_phy_supported`

```c
bool bt_conn_le_cs_capabilities::cs_sync_2m_phy_supported
```

`CS_SYNC` 使用低功耗 2M 物理层（LE 2M PHY）。

<a id="a22604c052da2f8ccf77c81a0a5c628b7"></a>

### `cs_without_fae_supported`

```c
bool bt_conn_le_cs_capabilities::cs_without_fae_supported
```

子特性（Subfeature）：无频率驱动误差的信道探测（CS with no Frequency Actuation Error）。

<a id="a6530d2a3fb66d498711856b723acecb7"></a>

### `initiator_supported`

```c
bool bt_conn_le_cs_capabilities::initiator_supported
```

发起方角色（Initiator role）。

<a id="ac842e123166008ad1ad663f827937a3b"></a>

### `max_antenna_paths_supported`

```c
uint8_t bt_conn_le_cs_capabilities::max_antenna_paths_supported
```

最大天线路径数（Maximum antenna paths）。

<a id="ae76fbc0f88525e83717e1d8ef5acae59"></a>

### `max_consecutive_procedures_supported`

```c
uint16_t bt_conn_le_cs_capabilities::max_consecutive_procedures_supported
```

最大连续信道探测过程数量（Maximum consecutive CS procedures）。

设为零时，表示支持在终止前执行固定次数或无限次的信道探测过程（CS procedures）。

<a id="aa1616417e6183cf283cf96efc9a92b8e"></a>

### `mode_3_supported`

```c
bool bt_conn_le_cs_capabilities::mode_3_supported
```

模式 3（Mode-3）。

<a id="a4e4c56c5066d02b2a0cd59c067f1e4b9"></a>

### `num_antennas_supported`

```c
uint8_t bt_conn_le_cs_capabilities::num_antennas_supported
```

天线数量（Number of antennas）。

<a id="a77aacfd02b354e04d4cc29cc1bf4b779"></a>

### `num_config_supported`

```c
uint8_t bt_conn_le_cs_capabilities::num_config_supported
```

信道探测配置数量（Number of CS configurations）。

<a id="ad57f15b4dda88e2b747f30451601c923"></a>

### `pbr_from_rtt_sounding_seq_supported`

```c
bool bt_conn_le_cs_capabilities::pbr_from_rtt_sounding_seq_supported
```

子特性（Subfeature）：基于往返时间探测序列的相位测距（Phase-based Ranging from RTT sounding sequence）。

<a id="a1a0076a0c97317803976f4aca86afc0d"></a>

### `phase_based_nadm_random_supported`

```c
bool bt_conn_le_cs_capabilities::phase_based_nadm_random_supported
```

收到包含随机序列（Random sequence）的 `CS_SYNC` 时，基于相位的归一化攻击检测器指标（Phase-based normalized attack detector metric）。

<a id="a94fd00a7a9b22d649f75c7fdd17590a9"></a>

### `phase_based_nadm_sounding_supported`

```c
bool bt_conn_le_cs_capabilities::phase_based_nadm_sounding_supported
```

收到包含探测序列（Sounding sequence）的 `CS_SYNC` 时，基于相位的归一化攻击检测器指标（Phase-based normalized attack detector metric）。

<a id="a694119619d359d0b7e298edf6201ee20"></a>

### `reflector_supported`

```c
bool bt_conn_le_cs_capabilities::reflector_supported
```

反射方角色（Reflector role）。

<a id="abe3c611316bb5f710f355846ee9ec437"></a>

### `rtt_aa_only_n`

```c
uint8_t bt_conn_le_cs_capabilities::rtt_aa_only_n
```

达到仅接入地址往返时间（RTT AA Only）精度要求所需的信道探测步骤数量（CS steps）。

不支持仅接入地址往返时间（RTT AA Only）时，设为 `0`。

<a id="a46c9168328d3fbc98a2625799c733818"></a>

### `rtt_aa_only_precision`

```c
enum bt_conn_le_cs_capability_rtt_aa_only bt_conn_le_cs_capabilities::rtt_aa_only_precision
```

仅接入地址的往返时间类型（RTT AA-Only）。

<a id="a345d9e43222d77024a8f4283b274b48f"></a>

### `rtt_random_payload_n`

```c
uint8_t bt_conn_le_cs_capabilities::rtt_random_payload_n
```

达到随机载荷往返时间（RTT Random Payload）精度要求所需的信道探测步骤数量（CS steps）。

不支持随机载荷往返时间（RTT Random Payload）时，设为 `0`。

<a id="abbefdc0268a775712c7abd664adcb6b2"></a>

### `rtt_random_payload_precision`

```c
enum bt_conn_le_cs_capability_rtt_random_payload bt_conn_le_cs_capabilities::rtt_random_payload_precision
```

随机载荷往返时间类型（RTT Random Payload）。

<a id="a7f35343a1572800850e791ba3ff5ffb1"></a>

### `rtt_sounding_n`

```c
uint8_t bt_conn_le_cs_capabilities::rtt_sounding_n
```

达到探测序列往返时间（RTT Sounding）精度要求所需的信道探测步骤数量（CS steps）。

不支持探测序列往返时间（RTT Sounding）时，设为 `0`。

<a id="acef0d65ed55ae304fea47006bfb0076f"></a>

### `rtt_sounding_precision`

```c
enum bt_conn_le_cs_capability_rtt_sounding bt_conn_le_cs_capabilities::rtt_sounding_precision
```

探测序列往返时间类型（RTT Sounding）。

<a id="a1ff1d7d769e3ba915f91bf672a6f8a61"></a>

### `t_fcs_times_supported`

```c
uint16_t bt_conn_le_cs_capabilities::t_fcs_times_supported
```

信道探测步骤（CS steps）期间可选的 `T_FCS` 持续时间。

- 位 0（Bit 0）：15 微秒（us）。
- 位 1（Bit 1）：20 微秒（us）。
- 位 2（Bit 2）：30 微秒（us）。
- 位 3（Bit 3）：40 微秒（us）。
- 位 4（Bit 4）：50 微秒（us）。
- 位 5（Bit 5）：60 微秒（us）。
- 位 6（Bit 6）：80 微秒（us）。
- 位 7（Bit 7）：100 微秒（us）。
- 位 8（Bit 8）：120 微秒（us）。

<a id="a090f869cfe7e39a70cea94afbd5ac376"></a>

### `t_ip1_times_supported`

```c
uint16_t bt_conn_le_cs_capabilities::t_ip1_times_supported
```

信道探测步骤（CS steps）期间可选的 `T_IP1` 持续时间。

- 位 0（Bit 0）：10 微秒（us）。
- 位 1（Bit 1）：20 微秒（us）。
- 位 2（Bit 2）：30 微秒（us）。
- 位 3（Bit 3）：40 微秒（us）。
- 位 4（Bit 4）：50 微秒（us）。
- 位 5（Bit 5）：60 微秒（us）。
- 位 6（Bit 6）：80 微秒（us）。

<a id="a21262b0e588a75146f2d0c325d0b5cc1"></a>

### `t_ip2_ipt_times_supported`

```c
uint16_t bt_conn_le_cs_capabilities::t_ip2_ipt_times_supported
```

信道探测步骤（CS steps）期间支持的 `T_IP2_IPT` 持续时间。

- 位 0（Bit 0）：10 微秒（us）。
- 位 1（Bit 1）：20 微秒（us）。
- 位 2（Bit 2）：30 微秒（us）。
- 位 3（Bit 3）：40 微秒（us）。
- 位 4（Bit 4）：50 微秒（us）。
- 位 5（Bit 5）：60 微秒（us）。
- 位 6（Bit 6）：80 微秒（us）。

<a id="ae93594f360430e9c0c80cf3edcf570f6"></a>

### `t_ip2_times_supported`

```c
uint16_t bt_conn_le_cs_capabilities::t_ip2_times_supported
```

信道探测步骤（CS steps）期间可选的 `T_IP2` 持续时间。

- 位 0（Bit 0）：10 微秒（us）。
- 位 1（Bit 1）：20 微秒（us）。
- 位 2（Bit 2）：30 微秒（us）。
- 位 3（Bit 3）：40 微秒（us）。
- 位 4（Bit 4）：50 微秒（us）。
- 位 5（Bit 5）：60 微秒（us）。
- 位 6（Bit 6）：80 微秒（us）。

<a id="a6e92391b21d4acaebba8a171643f572f"></a>

### `t_pm_times_supported`

```c
uint16_t bt_conn_le_cs_capabilities::t_pm_times_supported
```

信道探测步骤（CS steps）期间可选的 `T_PM` 持续时间。

- 位 0（Bit 0）：10 微秒（us）。
- 位 1（Bit 1）：20 微秒（us）。

<a id="a97b42928bcba43a6d90e8139efce0870"></a>

### `t_sw_ipt_time_supported`

```c
uint8_t bt_conn_le_cs_capabilities::t_sw_ipt_time_supported
```

内联相位校正项传输（Inline PCT Transfer，IPT）期间，信道探测音调（CS tones）支持的天线切换周期，单位为微秒。

`0x00`、`0x01`、`0x02`、`0x04` 或 `0x0A`：信道探测音调（CS tones）的天线切换周期，单位为微秒。

<a id="a5a86629a5ad4203b5efe3802cd8b6ae7"></a>

### `t_sw_time`

```c
uint8_t bt_conn_le_cs_capabilities::t_sw_time
```

信道探测音调（CS tones）的天线切换周期（Antenna switch period），单位为微秒。

<a id="ad58deea7a825bb5f0bc2ca0034183948"></a>

### `tx_snr_capability`

```c
uint8_t bt_conn_le_cs_capabilities::tx_snr_capability
```

往返时间数据包（RTT packets）支持的信噪比等级（SNR levels）。

- 位 0（Bit 0）：18 dB。
- 位 1（Bit 1）：21 dB。
- 位 2（Bit 2）：24 dB。
- 位 3（Bit 3）：27 dB。
- 位 4（Bit 4）：30 dB。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_conn_le_cs_capability_rtt_aa_only](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gafe14d64a64383b097760764697b035e2)
- [bt_conn_le_cs_capability_rtt_sounding](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1892ec23ca3b1818287a9d7dafc16433)
- [bt_conn_le_cs_capability_rtt_random_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5568443825fc1ce9534753d8918aa813)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_bt_conn_le_create_synced_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_bt_conn_le_cs_config_结构体.md)
