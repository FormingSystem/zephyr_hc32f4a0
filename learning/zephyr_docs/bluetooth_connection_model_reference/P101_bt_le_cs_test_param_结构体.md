---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-101
title: bt_le_cs_test_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__test__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第101章\_bt\_le\_cs\_test\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__test__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

信道探测测试（CS Test）的参数。

```c
#include <zephyr/bluetooth/cs.h>
```

<a id="details"></a>

信道探测测试（CS Test）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 101.1\_数据成员（Data Fields）

<a id="r_a242edcd4c53c136810a5846d8df52834"></a>

```c
enum bt_conn_le_cs_mode mode
```

相关声明：[bt_conn_le_cs_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f757b15d1d5006ce2fa6a7a78082156)、[mode](#a242edcd4c53c136810a5846d8df52834)。

信道探测过程（CS procedure）期间使用的主模式与子模式。

<a id="r_ac13c4390574bd9a540b632c3ee387870"></a>

```c
uint8_t main_mode_repetition
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[main_mode_repetition](#ac13c4390574bd9a540b632c3ee387870)。

从上一个信道探测子事件（CS subevent）末尾取出、在当前子事件开头重复执行的主模式步骤数量；这些重复步骤紧接当前事件最后一个模式 0 步骤之后执行。

<a id="r_a84f346fafa174ba8b2acf33ff3db72eb"></a>

```c
uint8_t mode_0_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode_0_steps](#a84f346fafa174ba8b2acf33ff3db72eb)。

测试信道探测子事件（Test CS subevent）开头的模式 0 步骤数量。

<a id="r_a797dda190cc01447054ee4dc08f2a332"></a>

```c
enum bt_conn_le_cs_role role
```

相关声明：[bt_conn_le_cs_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0e6f6d4fdbdfc3ed75fef4a95136076f)、[role](#a797dda190cc01447054ee4dc08f2a332)。

信道探测测试角色（CS Test role）。

<a id="r_ab3af198a629e0fb082a177b6b482771a"></a>

```c
enum bt_conn_le_cs_rtt_type rtt_type
```

相关声明：[bt_conn_le_cs_rtt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaffd6abf9b92cc8d8463797a73b840f51)、[rtt_type](#ab3af198a629e0fb082a177b6b482771a)。

往返时间变体（RTT variant）。

<a id="r_a41c70c829d16299eb7d25029ddad01bb"></a>

```c
enum bt_conn_le_cs_sync_phy cs_sync_phy
```

相关声明：[bt_conn_le_cs_sync_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaadbf6a4dba28aec90ea07b7da634e1bb)、[cs_sync_phy](#a41c70c829d16299eb7d25029ddad01bb)。

`CS_SYNC` 物理层（PHY）。

<a id="r_af26b66e0a28e4f3c6fce0dd5ad8a7606"></a>

```c
enum bt_le_cs_test_cs_sync_antenna_selection cs_sync_antenna_selection
```

相关声明：[bt_le_cs_test_cs_sync_antenna_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga782a500f611320a6f3feed9897ab8e16)、[cs_sync_antenna_selection](#af26b66e0a28e4f3c6fce0dd5ad8a7606)。

`CS_SYNC` 数据包所用的天线标识符（Antenna identifier）。

<a id="r_a78aeb8d6e7ac9565ea19a1ffd51ceb6a"></a>

```c
uint32_t subevent_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[subevent_len](#a78aeb8d6e7ac9565ea19a1ffd51ceb6a)。

信道探测子事件长度（CS subevent length），单位为微秒。

<a id="r_a1bff7f98cb72a9f73b0499b8fc89d262"></a>

```c
uint16_t subevent_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subevent_interval](#a1bff7f98cb72a9f73b0499b8fc89d262)。

两个连续信道探测子事件（CS subevents）起始时刻之间的间隔，为 N × 0.625 毫秒。

<a id="r_aaf09c64fcfa1a0a4257d805ad9b49d56"></a>

```c
uint8_t max_num_subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_num_subevents](#aaf09c64fcfa1a0a4257d805ad9b49d56)。

此过程中允许的最大子事件数（Maximum subevents）。

<a id="r_a5951fa7f55752905a0180e8389c3d245"></a>

```c
uint8_t transmit_power_level
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transmit_power_level](#a5951fa7f55752905a0180e8389c3d245)。

信道探测过程（CS procedure）期望的发射功率等级（TX power level），单位为 dBm。

<a id="r_a02437a42f0c3e8563d1600b02e7ca517"></a>

```c
uint8_t t_ip1_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_ip1_time](#a02437a42f0c3e8563d1600b02e7ca517)。

往返时间数据包（RTT packets）之间的间歇时间（Interlude time），单位为微秒。

<a id="r_a1ce5f3400442ebdd8cf45f9db6367e58"></a>

```c
uint8_t t_ip2_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_ip2_time](#a1ce5f3400442ebdd8cf45f9db6367e58)。

信道探测音调（CS tones）之间的间歇时间（Interlude time），单位为微秒。

<a id="r_a8a2d1540e35d194729df373c79f9eaf2"></a>

```c
uint8_t t_fcs_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_fcs_time](#a8a2d1540e35d194729df373c79f9eaf2)。

频率切换时间（Frequency change time），单位为微秒。

<a id="r_a8eb7e6fcf4431513404ac5f75da401a9"></a>

```c
uint8_t t_pm_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_pm_time](#a8eb7e6fcf4431513404ac5f75da401a9)。

信道探测音调（CS tones）的相位测量周期（Phase measurement period），单位为微秒。

<a id="r_a94c3e1dcfb7290b61784c5dcd6a67531"></a>

```c
uint8_t t_sw_time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_sw_time](#a94c3e1dcfb7290b61784c5dcd6a67531)。

信道探测音调（CS tones）的天线切换周期（Antenna switch period），单位为微秒。

<a id="r_aff02c121f9c8ae63a137dbb19bf4acd2"></a>

```c
enum bt_conn_le_cs_tone_antenna_config_selection tone_antenna_config_selection
```

相关声明：[bt_conn_le_cs_tone_antenna_config_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab7acdbdf273fc760799cf0d8cf71591c)、[tone_antenna_config_selection](#aff02c121f9c8ae63a137dbb19bf4acd2)。

信道探测步骤的音调阶段（Tone phases of CS steps）进行天线切换时使用的天线配置索引（Antenna Configuration Index）。

<a id="r_aa58cf62583c83e32362216bc060a9a8e"></a>

```c
enum bt_le_cs_snr_control initiator_snr_control
```

相关声明：[bt_le_cs_snr_control](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf34c59887e8a6da0560b6428733fe8d0)、[initiator_snr_control](#aa58cf62583c83e32362216bc060a9a8e)。

发起方信噪比控制选项（Initiator SNR control options）。

<a id="r_aaa7305e11ee3e22b10b4ceb3c743d4e9"></a>

```c
enum bt_le_cs_snr_control reflector_snr_control
```

相关声明：[bt_le_cs_snr_control](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf34c59887e8a6da0560b6428733fe8d0)、[reflector_snr_control](#aaa7305e11ee3e22b10b4ceb3c743d4e9)。

反射方信噪比控制选项（Reflector SNR control options）。

<a id="r_a3ba9bfaa63f144af3117233e7a7e3d3d"></a>

```c
uint16_t drbg_nonce
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[drbg_nonce](#a3ba9bfaa63f144af3117233e7a7e3d3d)。

决定确定性随机位生成器（DRBG）的随机数（Nonce）初始值中的第 14 和第 15 个八位组。

<a id="r_a0ac14a9e1055870ee33ef83e54c1a248"></a>

```c
uint16_t override_config
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[override_config](#a0ac14a9e1055870ee33ef83e54c1a248)。

覆盖配置（Override configuration）。

```c
struct {
```

<a id="r_aef8dd11643d3cf20a6c6c5cb8107e2e7"></a>

```c
uint8_t channel_map_repetition
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_map_repetition](#a5f0cefe32070be29bc918ff4f7a3a46d)。

在一个信道探测过程（CS procedure）内，非模式 0 步骤循环遍历信道映射（Channel map）或信道字段所指示信道的次数。

```c
union {
```

```c
struct {
```

<a id="r_ac6b12d0f3cf16ca89b0d6649e2430525"></a>

```c
uint8_t num_channels
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_channels](#acb2eed00edb4cac80ce097b241d8e1c8)。

<a id="r_a15236638eeabbc749ca4794f5aa30331"></a>

```c
uint8_t * channels
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channels](#aeb66cc7b6744cd1709d6199d2ae2dc98)。

<a id="r_a34d56ae668de96bd2f8883d44fe55467"></a>

```c
} set
```

相关声明：[set](#a7eb22e2e410701b2baa5f7d9d7123721)。

```c
struct {
```

<a id="r_a63fdff646a5009a5709a98baa1a2cba8"></a>

```c
uint8_t channel_map [10]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_map](#a6092db75cfc8143d2e308fce87c18dfe)。

<a id="r_a36096451cf64df43000f780a6ffd4574"></a>

```c
enum bt_conn_le_cs_chsel_type channel_selection_type
```

相关声明：[bt_conn_le_cs_chsel_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga34e4837a77c7afd6999095985ddad4f0)、[channel_selection_type](#ad2f4775d56677c63ef1ff71c0d3bc08a)。

<a id="r_a4a08cc240afced94a14addb9ff14be2d"></a>

```c
enum bt_conn_le_cs_ch3c_shape ch3c_shape
```

相关声明：[bt_conn_le_cs_ch3c_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf2331ec1f1222de51fc4f30566e1c52b)、[ch3c_shape](#a656de42b2afb3d9c53899d3c4d6f3a88)。

<a id="r_ae28730f6d28358a860a9142bc994bf97"></a>

```c
uint8_t ch3c_jump
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch3c_jump](#aac51c328149cce847057b913f2733198)。

<a id="r_ab29487b8a0a129313242a61ceb3f61db"></a>

```c
} not_set
```

相关声明：[not_set](#a1c241926b6d1c57c1bde197c1fb37251)。

<a id="r_ac1026dc37ed46af7df1f1dbf13477a7d"></a>

```c
}
```

<a id="r_a802545d0c7f560166250d4ad585a7d80"></a>

```c
} override_config_0
```

相关声明：[override_config_0](#a802545d0c7f560166250d4ad585a7d80)。

覆盖配置（Override config）的位 0。

```c
struct {
```

<a id="r_aa9c248262d7ca9dc736aadf8cf15cf1f"></a>

```c
uint8_t main_mode_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[main_mode_steps](#a1e92044ae3538cb71a9192ebcbd8c884)。

<a id="r_a63e8e44842b894bee57ffdcdee4f2cd0"></a>

```c
} override_config_2
```

相关声明：[override_config_2](#a63e8e44842b894bee57ffdcdee4f2cd0)。

覆盖配置（Override config）的位 2。

```c
struct {
```

<a id="r_a2c0adc9e3e27a76b3a087ce6de3aacfa"></a>

```c
enum bt_le_cs_test_override_3_pm_tone_ext t_pm_tone_ext
```

相关声明：[bt_le_cs_test_override_3_pm_tone_ext](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf50910d51c69e216ef6eb22b5c0f2d28)、[t_pm_tone_ext](#a905f49912a99c105ce4087c4d3327deb)。

<a id="r_afe036f2effcb41c9a4d888592916c329"></a>

```c
} override_config_3
```

相关声明：[override_config_3](#afe036f2effcb41c9a4d888592916c329)。

覆盖配置（Override config）的位 3。

```c
struct {
```

<a id="r_a9fc8aa5501f54deee4e74b8f8eefc98a"></a>

```c
enum bt_le_cs_test_override_4_tone_antenna_permutation tone_antenna_permutation
```

相关声明：[bt_le_cs_test_override_4_tone_antenna_permutation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga1ba4d7d919cb5c09469f8e8aa05bb04d)、[tone_antenna_permutation](#a22e2ec51e87887b74c8251fa004a4497)。

<a id="r_a40671e60cf8e1ff16e7389f6a24c9bb7"></a>

```c
} override_config_4
```

相关声明：[override_config_4](#a40671e60cf8e1ff16e7389f6a24c9bb7)。

覆盖配置（Override config）的位 4。

```c
struct {
```

<a id="r_a8d6cf570a84a24c79ceefe82d56f7587"></a>

```c
uint32_t cs_sync_aa_initiator
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cs_sync_aa_initiator](#a355cdcf57dcafdfdc98959ec6b742cc1)。

发起方发送的 `CS_SYNC` 数据包所使用的接入地址（Access Address）。

<a id="r_a383e256bfb1f73327d8844936bc8b0d9"></a>

```c
uint32_t cs_sync_aa_reflector
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cs_sync_aa_reflector](#ad8ce97db93b0fbc267552db64491483a)。

反射方发送的 `CS_SYNC` 数据包所使用的接入地址（Access Address）。

<a id="r_a9bba99348c662adad1f16194409b2ae1"></a>

```c
} override_config_5
```

相关声明：[override_config_5](#a9bba99348c662adad1f16194409b2ae1)。

覆盖配置（Override config）的位 5。

```c
struct {
```

<a id="r_acd74f31b03d62bd8170f2ebac915a4b5"></a>

```c
uint8_t ss_marker1_position
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ss_marker1_position](#a1404de78072df4910a1823eadcb78cd1)。

信道探测序列（Channel sounding sequence）中第一个标记的起始位编号。

<a id="r_a0a248695a7cbbe118fdb84a19ef3472b"></a>

```c
uint8_t ss_marker2_position
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ss_marker2_position](#a093b0425d87266c9cb31c8dc209477ff)。

信道探测序列（Channel sounding sequence）中第二个标记的起始位编号。

<a id="r_af4f16878d530ec19294673756e7b6358"></a>

```c
} override_config_6
```

相关声明：[override_config_6](#af4f16878d530ec19294673756e7b6358)。

覆盖配置（Override config）的位 6。

```c
struct {
```

<a id="r_ab2d09e9381e8141c8a952fefb29a6e7e"></a>

```c
enum bt_le_cs_test_override_7_ss_marker_value ss_marker_value
```

相关声明：[bt_le_cs_test_override_7_ss_marker_value](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gacb3f437225ad1d6320ee424c39ebc82a)、[ss_marker_value](#aad705c92184ed8f1577bac68dc810373)。

探测序列标记值（Sounding Sequence marker value）。

<a id="r_a9a2763c3062b2ee4d8a1d70393ed2aa2"></a>

```c
} override_config_7
```

相关声明：[override_config_7](#a9a2763c3062b2ee4d8a1d70393ed2aa2)。

覆盖配置（Override config）的位 7。

```c
struct {
```

<a id="r_ab69ab1f4cb4c297e91ce23bd0e32897d"></a>

```c
enum bt_le_cs_test_override_8_cs_sync_payload_pattern cs_sync_payload_pattern
```

相关声明：[bt_le_cs_test_override_8_cs_sync_payload_pattern](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga731bbaa98dab7c88725fc64b66da62eb)、[cs_sync_payload_pattern](#ace81aeaeefc788ccf6bb1b6c491ff0b2)。

`CS_SYNC` 载荷模式选择（Payload pattern selection）。

<a id="r_a51e35f3987ca611df7bcb30aebc86436"></a>

```c
uint8_t cs_sync_user_payload [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_sync_user_payload](#a79ce15e5034572a4b5015240b7db4de5)。

`CS_SYNC` 数据包的用户载荷（User payload）。

<a id="r_afb85cec959d8bd59b560828af14dbced"></a>

```c
} override_config_8
```

相关声明：[override_config_8](#afb85cec959d8bd59b560828af14dbced)。

覆盖配置（Override config）的位 8。

## 101.2\_详细说明（Detailed Documentation）

<a id="aac51c328149cce847057b913f2733198"></a>

### `ch3c_jump`

```c
uint8_t bt_le_cs_test_param::ch3c_jump
```

<a id="a656de42b2afb3d9c53899d3c4d6f3a88"></a>

### `ch3c_shape`

```c
enum bt_conn_le_cs_ch3c_shape bt_le_cs_test_param::ch3c_shape
```

<a id="a6092db75cfc8143d2e308fce87c18dfe"></a>

### `channel_map`

```c
uint8_t bt_le_cs_test_param::channel_map[10]
```

<a id="a5f0cefe32070be29bc918ff4f7a3a46d"></a>

### `channel_map_repetition`

```c
uint8_t bt_le_cs_test_param::channel_map_repetition
```

在一个信道探测过程（CS procedure）内，非模式 0 步骤循环遍历信道映射（Channel map）或信道字段所指示信道的次数。

<a id="ad2f4775d56677c63ef1ff71c0d3bc08a"></a>

### `channel_selection_type`

```c
enum bt_conn_le_cs_chsel_type bt_le_cs_test_param::channel_selection_type
```

<a id="aeb66cc7b6744cd1709d6199d2ae2dc98"></a>

### `channels`

```c
uint8_t* bt_le_cs_test_param::channels
```

<a id="a355cdcf57dcafdfdc98959ec6b742cc1"></a>

### `cs_sync_aa_initiator`

```c
uint32_t bt_le_cs_test_param::cs_sync_aa_initiator
```

发起方发送的 `CS_SYNC` 数据包所使用的接入地址（Access Address）。

<a id="ad8ce97db93b0fbc267552db64491483a"></a>

### `cs_sync_aa_reflector`

```c
uint32_t bt_le_cs_test_param::cs_sync_aa_reflector
```

反射方发送的 `CS_SYNC` 数据包所使用的接入地址（Access Address）。

<a id="af26b66e0a28e4f3c6fce0dd5ad8a7606"></a>

### `cs_sync_antenna_selection`

```c
enum bt_le_cs_test_cs_sync_antenna_selection bt_le_cs_test_param::cs_sync_antenna_selection
```

`CS_SYNC` 数据包所用的天线标识符（Antenna identifier）。

<a id="ace81aeaeefc788ccf6bb1b6c491ff0b2"></a>

### `cs_sync_payload_pattern`

```c
enum bt_le_cs_test_override_8_cs_sync_payload_pattern bt_le_cs_test_param::cs_sync_payload_pattern
```

`CS_SYNC` 载荷模式选择（Payload pattern selection）。

<a id="a41c70c829d16299eb7d25029ddad01bb"></a>

### `cs_sync_phy`

```c
enum bt_conn_le_cs_sync_phy bt_le_cs_test_param::cs_sync_phy
```

`CS_SYNC` 物理层（PHY）。

<a id="a79ce15e5034572a4b5015240b7db4de5"></a>

### `cs_sync_user_payload`

```c
uint8_t bt_le_cs_test_param::cs_sync_user_payload[16]
```

`CS_SYNC` 数据包的用户载荷（User payload）。

此参数仅在使用 `BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_USER` 时使用。

最低有效位（Least significant bit）对应信道探测载荷（CS payload）的最高有效位（Most significant bit）。序列短于 16 个八位组时，最低有效的八位组必须补零。

<a id="a3ba9bfaa63f144af3117233e7a7e3d3d"></a>

### `drbg_nonce`

```c
uint16_t bt_le_cs_test_param::drbg_nonce
```

决定确定性随机位生成器（DRBG）的随机数（Nonce）初始值中的第 14 和第 15 个八位组。

<a id="aa58cf62583c83e32362216bc060a9a8e"></a>

### `initiator_snr_control`

```c
enum bt_le_cs_snr_control bt_le_cs_test_param::initiator_snr_control
```

发起方信噪比控制选项（Initiator SNR control options）。

<a id="ac13c4390574bd9a540b632c3ee387870"></a>

### `main_mode_repetition`

```c
uint8_t bt_le_cs_test_param::main_mode_repetition
```

从上一个信道探测子事件（CS subevent）末尾取出、在当前子事件开头重复执行的主模式步骤数量；这些重复步骤紧接当前事件最后一个模式 0 步骤之后执行。

<a id="a1e92044ae3538cb71a9192ebcbd8c884"></a>

### `main_mode_steps`

```c
uint8_t bt_le_cs_test_param::main_mode_steps
```

<a id="aaf09c64fcfa1a0a4257d805ad9b49d56"></a>

### `max_num_subevents`

```c
uint8_t bt_le_cs_test_param::max_num_subevents
```

此过程中允许的最大子事件数（Maximum subevents）。

值为 `0` 表示忽略此参数。

<a id="a242edcd4c53c136810a5846d8df52834"></a>

### `mode`

```c
enum bt_conn_le_cs_mode bt_le_cs_test_param::mode
```

信道探测过程（CS procedure）期间使用的主模式与子模式。

<a id="a84f346fafa174ba8b2acf33ff3db72eb"></a>

### `mode_0_steps`

```c
uint8_t bt_le_cs_test_param::mode_0_steps
```

测试信道探测子事件（Test CS subevent）开头的模式 0 步骤数量。

<a id="a1c241926b6d1c57c1bde197c1fb37251"></a>

### `[struct]`

```c
struct { ... } bt_le_cs_test_param::not_set
```

<a id="acb2eed00edb4cac80ce097b241d8e1c8"></a>

### `num_channels`

```c
uint8_t bt_le_cs_test_param::num_channels
```

<a id="a0ac14a9e1055870ee33ef83e54c1a248"></a>

### `override_config`

```c
uint16_t bt_le_cs_test_param::override_config
```

覆盖配置（Override configuration）。

此参数用于覆盖来自确定性随机位生成器（DRBG）的信道探测参数（CS parameters）。每一位配置一组不同的参数。

除位 0 所配置的覆盖项外，所有覆盖项（Overrides）均为可选。

具体如下：

- 位 0 已设置：使用信道列表（List of channels）覆盖。
- 位 0 未设置：使用信道映射（Channel map）覆盖。
- 位 2 已设置：覆盖主模式步骤（Main mode steps）。
- 位 3 已设置：覆盖 `T_PM_Tone_Ext`。
- 位 4 已设置：覆盖音调天线排列（Tone antenna permutation）。
- 位 5 已设置：覆盖 `CS_SYNC` 接入地址（AA）。
- 位 6 已设置：覆盖探测序列标记位置（SS marker positions）。
- 位 7 已设置：覆盖探测序列标记值（SS marker value）。
- 位 8 已设置：覆盖 `CS_SYNC` 载荷模式（Payload pattern）及用户载荷（User payload）。
- 位 10 已设置：将过程替换为稳定相位测试（Stable phase test）。

<a id="a802545d0c7f560166250d4ad585a7d80"></a>

### `[struct]`

```c
struct { ... } bt_le_cs_test_param::override_config_0
```

覆盖配置（Override config）的位 0。

<a id="a63e8e44842b894bee57ffdcdee4f2cd0"></a>

### `[struct]`

```c
struct { ... } bt_le_cs_test_param::override_config_2
```

覆盖配置（Override config）的位 2。

未设置该位时，忽略这些参数（Parameters）。

<a id="afe036f2effcb41c9a4d888592916c329"></a>

### `[struct]`

```c
struct { ... } bt_le_cs_test_param::override_config_3
```

覆盖配置（Override config）的位 3。

未设置该位时，忽略这些参数（Parameters）。

<a id="a40671e60cf8e1ff16e7389f6a24c9bb7"></a>

### `[struct]`

```c
struct { ... } bt_le_cs_test_param::override_config_4
```

覆盖配置（Override config）的位 4。

未设置该位时，忽略这些参数（Parameters）。

<a id="a9bba99348c662adad1f16194409b2ae1"></a>

### `[struct]`

```c
struct { ... } bt_le_cs_test_param::override_config_5
```

覆盖配置（Override config）的位 5。

未设置该位时，忽略这些参数（Parameters）。

<a id="af4f16878d530ec19294673756e7b6358"></a>

### `[struct]`

```c
struct { ... } bt_le_cs_test_param::override_config_6
```

覆盖配置（Override config）的位 6。

未设置该位时，忽略这些参数（Parameters）。

<a id="a9a2763c3062b2ee4d8a1d70393ed2aa2"></a>

### `[struct]`

```c
struct { ... } bt_le_cs_test_param::override_config_7
```

覆盖配置（Override config）的位 7。

未设置该位时，忽略这些参数（Parameters）。

<a id="afb85cec959d8bd59b560828af14dbced"></a>

### `[struct]`

```c
struct { ... } bt_le_cs_test_param::override_config_8
```

覆盖配置（Override config）的位 8。

未设置该位时，忽略这些参数（Parameters）。

<a id="aaa7305e11ee3e22b10b4ceb3c743d4e9"></a>

### `reflector_snr_control`

```c
enum bt_le_cs_snr_control bt_le_cs_test_param::reflector_snr_control
```

反射方信噪比控制选项（Reflector SNR control options）。

<a id="a797dda190cc01447054ee4dc08f2a332"></a>

### `role`

```c
enum bt_conn_le_cs_role bt_le_cs_test_param::role
```

信道探测测试角色（CS Test role）。

<a id="ab3af198a629e0fb082a177b6b482771a"></a>

### `rtt_type`

```c
enum bt_conn_le_cs_rtt_type bt_le_cs_test_param::rtt_type
```

往返时间变体（RTT variant）。

<a id="a7eb22e2e410701b2baa5f7d9d7123721"></a>

### `[struct]`

```c
struct { ... } bt_le_cs_test_param::set
```

<a id="a1404de78072df4910a1823eadcb78cd1"></a>

### `ss_marker1_position`

```c
uint8_t bt_le_cs_test_param::ss_marker1_position
```

信道探测序列（Channel sounding sequence）中第一个标记的起始位编号。

使用 `BT_CONN_LE_CS_RTT_TYPE_32_BIT_SOUNDING` 时，必须处于 0–28 范围内。

<a id="a093b0425d87266c9cb31c8dc209477ff"></a>

### `ss_marker2_position`

```c
uint8_t bt_le_cs_test_param::ss_marker2_position
```

信道探测序列（Channel sounding sequence）中第二个标记的起始位编号。

使用 `BT_CONN_LE_CS_RTT_TYPE_96_BIT_SOUNDING` 时，必须处于 67–92 范围内。

值 `BT_HCI_OP_LE_CS_TEST_SS_MARKER_2_POSITION_NOT_PRESENT` 表示此探测序列（Sounding sequence）或标记（Marker）不存在。

<a id="aad705c92184ed8f1577bac68dc810373"></a>

### `ss_marker_value`

```c
enum bt_le_cs_test_override_7_ss_marker_value bt_le_cs_test_param::ss_marker_value
```

探测序列标记值（Sounding Sequence marker value）。

<a id="a1bff7f98cb72a9f73b0499b8fc89d262"></a>

### `subevent_interval`

```c
uint16_t bt_le_cs_test_param::subevent_interval
```

两个连续信道探测子事件（CS subevents）起始时刻之间的间隔，为 N × 0.625 毫秒。

值为 `0` 表示只有一个信道探测子事件（CS subevent）。

<a id="a78aeb8d6e7ac9565ea19a1ffd51ceb6a"></a>

### `subevent_len`

```c
uint32_t bt_le_cs_test_param::subevent_len
```

信道探测子事件长度（CS subevent length），单位为微秒。

范围（Range）：1250 微秒至 4 秒。

<a id="a8a2d1540e35d194729df373c79f9eaf2"></a>

### `t_fcs_time`

```c
uint8_t bt_le_cs_test_param::t_fcs_time
```

频率切换时间（Frequency change time），单位为微秒。

有效选项（Valid options）如下：

- 15 微秒（us）。
- 20 微秒（us）。
- 30 微秒（us）。
- 40 微秒（us）。
- 50 微秒（us）。
- 60 微秒（us）。
- 80 微秒（us）。
- 100 微秒（us）。
- 120 微秒（us）。
- 150 微秒（us）。

<a id="a02437a42f0c3e8563d1600b02e7ca517"></a>

### `t_ip1_time`

```c
uint8_t bt_le_cs_test_param::t_ip1_time
```

往返时间数据包（RTT packets）之间的间歇时间（Interlude time），单位为微秒。

有效选项（Valid options）如下：

- 10 微秒（us）。
- 20 微秒（us）。
- 30 微秒（us）。
- 40 微秒（us）。
- 50 微秒（us）。
- 60 微秒（us）。
- 80 微秒（us）。
- 145 微秒（us）。

<a id="a1ce5f3400442ebdd8cf45f9db6367e58"></a>

### `t_ip2_time`

```c
uint8_t bt_le_cs_test_param::t_ip2_time
```

信道探测音调（CS tones）之间的间歇时间（Interlude time），单位为微秒。

有效选项（Valid options）如下：

- 10 微秒（us）。
- 20 微秒（us）。
- 30 微秒（us）。
- 40 微秒（us）。
- 50 微秒（us）。
- 60 微秒（us）。
- 80 微秒（us）。
- 145 微秒（us）。

<a id="a8eb7e6fcf4431513404ac5f75da401a9"></a>

### `t_pm_time`

```c
uint8_t bt_le_cs_test_param::t_pm_time
```

信道探测音调（CS tones）的相位测量周期（Phase measurement period），单位为微秒。

有效选项（Valid options）如下：

- 10 微秒（us）。
- 20 微秒（us）。
- 40 微秒（us）。

<a id="a905f49912a99c105ce4087c4d3327deb"></a>

### `t_pm_tone_ext`

```c
enum bt_le_cs_test_override_3_pm_tone_ext bt_le_cs_test_param::t_pm_tone_ext
```

<a id="a94c3e1dcfb7290b61784c5dcd6a67531"></a>

### `t_sw_time`

```c
uint8_t bt_le_cs_test_param::t_sw_time
```

信道探测音调（CS tones）的天线切换周期（Antenna switch period），单位为微秒。

有效选项（Valid options）如下：

- 0 微秒（us）。
- 1 微秒（us）。
- 2 微秒（us）。
- 4 微秒（us）。
- 10 微秒（us）。

<a id="aff02c121f9c8ae63a137dbb19bf4acd2"></a>

### `tone_antenna_config_selection`

```c
enum bt_conn_le_cs_tone_antenna_config_selection bt_le_cs_test_param::tone_antenna_config_selection
```

信道探测步骤的音调阶段（Tone phases of CS steps）进行天线切换时使用的天线配置索引（Antenna Configuration Index）。

<a id="a22e2ec51e87887b74c8251fa004a4497"></a>

### `tone_antenna_permutation`

```c
enum bt_le_cs_test_override_4_tone_antenna_permutation bt_le_cs_test_param::tone_antenna_permutation
```

<a id="a5951fa7f55752905a0180e8389c3d245"></a>

### `transmit_power_level`

```c
uint8_t bt_le_cs_test_param::transmit_power_level
```

信道探测过程（CS procedure）期望的发射功率等级（TX power level），单位为 dBm。

取值范围为 `BT_HCI_OP_LE_CS_MIN_MAX_TX_POWER` 至 `BT_HCI_OP_LE_CS_MAX_MAX_TX_POWER`。

特殊值（Special values）如下：

- `BT_HCI_OP_LE_CS_TEST_MAXIMIZE_TX_POWER` 告知控制器，应使用尽可能高的发射功率（Transmit power）。
- `BT_HCI_OP_LE_CS_TEST_MINIMIZE_TX_POWER` 告知控制器，应使用尽可能低的发射功率（Transmit power）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/cs.h`

## 101.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/cs.h](https://docs.zephyrproject.org/latest/doxygen/html/cs_8h_source.html)
- [bt_conn_le_cs_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f757b15d1d5006ce2fa6a7a78082156)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn_le_cs_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0e6f6d4fdbdfc3ed75fef4a95136076f)
- [bt_conn_le_cs_rtt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaffd6abf9b92cc8d8463797a73b840f51)
- [bt_conn_le_cs_sync_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaadbf6a4dba28aec90ea07b7da634e1bb)
- [bt_le_cs_test_cs_sync_antenna_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga782a500f611320a6f3feed9897ab8e16)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_conn_le_cs_tone_antenna_config_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab7acdbdf273fc760799cf0d8cf71591c)
- [bt_le_cs_snr_control](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf34c59887e8a6da0560b6428733fe8d0)
- [bt_conn_le_cs_chsel_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga34e4837a77c7afd6999095985ddad4f0)
- [bt_conn_le_cs_ch3c_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf2331ec1f1222de51fc4f30566e1c52b)
- [bt_le_cs_test_override_3_pm_tone_ext](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf50910d51c69e216ef6eb22b5c0f2d28)
- [bt_le_cs_test_override_4_tone_antenna_permutation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga1ba4d7d919cb5c09469f8e8aa05bb04d)
- [bt_le_cs_test_override_7_ss_marker_value](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gacb3f437225ad1d6320ee424c39ebc82a)
- [bt_le_cs_test_override_8_cs_sync_payload_pattern](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga731bbaa98dab7c88725fc64b66da62eb)
- [BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62ebaf68334f70d91d587e906533ad544fef1)
- [BT_CONN_LE_CS_RTT_TYPE_32_BIT_SOUNDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51a6350cf2f1d91e496ec49ddd09f7044fc)
- [BT_CONN_LE_CS_RTT_TYPE_96_BIT_SOUNDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51a243bb67b834cda207b61cc7ea65bdab2)
- [BT_HCI_OP_LE_CS_TEST_SS_MARKER_2_POSITION_NOT_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a1f2bfc1afab1928321c01beddb658f01)
- [BT_HCI_OP_LE_CS_MIN_MAX_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a040315a8ac4f80a2c497919a2fd4d7bc)
- [BT_HCI_OP_LE_CS_MAX_MAX_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a29a240b2d3f209b1f5f3d96e380dde08)
- [BT_HCI_OP_LE_CS_TEST_MAXIMIZE_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a50eb827977c0c596cb357ed62a6e80bd)
- [BT_HCI_OP_LE_CS_TEST_MINIMIZE_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a500597c78a6ada65d1224960bf6a370f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P100_bt_le_cs_test_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P102_bt_le_ext_adv_结构体.md)
