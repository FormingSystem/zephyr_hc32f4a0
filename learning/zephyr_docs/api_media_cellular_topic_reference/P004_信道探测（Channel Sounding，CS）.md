---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-4
title: 信道探测（Channel Sounding，CS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_信道探测（Channel Sounding，CS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

低功耗蓝牙信道探测（LE Channel Sounding，CS）

<a id="details"></a>

低功耗蓝牙信道探测（LE Channel Sounding，CS）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_bt_5Fle_5Fcs_5Fset_5Fdefault_5Fsettings_5Fparam"></a>

```c
struct bt_le_cs_set_default_settings_param
```

相关声明：[bt_le_cs_set_default_settings_param](../bluetooth_connection_model_reference/P097_bt_le_cs_set_default_settings_param_结构体.md)。

本地控制器（Controller）中的默认信道探测（CS）设置。

<a id="r_bt_5Fle_5Fcs_5Ftest_5Fparam"></a>

```c
struct bt_le_cs_test_param
```

相关声明：[bt_le_cs_test_param](../bluetooth_connection_model_reference/P101_bt_le_cs_test_param_结构体.md)。

信道探测测试（CS Test）的参数。

<a id="r_bt_5Fle_5Fcs_5Fcreate_5Fconfig_5Fparams"></a>

```c
struct bt_le_cs_create_config_params
```

相关声明：[bt_le_cs_create_config_params](../bluetooth_connection_model_reference/P094_bt_le_cs_create_config_params_结构体.md)。

信道探测（CS）的创建配置参数。

<a id="r_bt_5Fle_5Fcs_5Ftest_5Fcb"></a>

```c
struct bt_le_cs_test_cb
```

相关声明：[bt_le_cs_test_cb](../bluetooth_connection_model_reference/P100_bt_le_cs_test_cb_结构体.md)。

信道探测测试（CS Test）的回调。

<a id="r_bt_5Fle_5Fcs_5Fsubevent_5Fstep"></a>

```c
struct bt_le_cs_subevent_step
```

相关声明：[bt_le_cs_subevent_step](../bluetooth_connection_model_reference/P099_bt_le_cs_subevent_step_结构体.md)。

子事件结果步骤（Subevent Result Step）。

<a id="r_bt_5Fle_5Fcs_5Fiq_5Fsample"></a>

```c
struct bt_le_cs_iq_sample
```

相关声明：[bt_le_cs_iq_sample](../bluetooth_connection_model_reference/P095_bt_le_cs_iq_sample_结构体.md)。

从步骤数据中提取并完成符号扩展的同相/正交（IQ）值。

<a id="r_bt_5Fle_5Fcs_5Fprocedure_5Fenable_5Fparam"></a>

```c
struct bt_le_cs_procedure_enable_param
```

相关声明：[bt_le_cs_procedure_enable_param](../bluetooth_connection_model_reference/P096_bt_le_cs_procedure_enable_param_结构体.md)。

<a id="r_bt_5Fle_5Fcs_5Fset_5Fprocedure_5Fparameters_5Fparam"></a>

```c
struct bt_le_cs_set_procedure_parameters_param
```

相关声明：[bt_le_cs_set_procedure_parameters_param](../bluetooth_connection_model_reference/P098_bt_le_cs_set_procedure_parameters_param_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga95e2d24515e45096912440fe8a6bd3a0"></a>

```c
#define BT_LE_CS_CHANNEL_BIT_GET(chmap, bit)
```

相关声明：[BT_LE_CS_CHANNEL_BIT_GET](#ga95e2d24515e45096912440fe8a6bd3a0)。

获取信道探测（CS）信道映射中特定位的宏。

<a id="r_gadcd3351ef99d42e93c89d48f1c8ba668"></a>

```c
#define BT_LE_CS_CHANNEL_BIT_SET_VAL(chmap, bit, val)
```

相关声明：[BT_LE_CS_CHANNEL_BIT_SET_VAL](#gadcd3351ef99d42e93c89d48f1c8ba668)。

设置信道探测（CS）信道映射中特定位值的宏。

<a id="r_gaf278a44ad602ce7e365ac0d71bcc48b4"></a>

```c
#define BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_1 BIT(0)
```

相关声明：[BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_1](#gaf278a44ad602ce7e365ac0d71bcc48b4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga5ff36f6e97668a9d1b6ccd39492c68f7"></a>

```c
#define BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_2 BIT(1)
```

相关声明：[BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_2](#ga5ff36f6e97668a9d1b6ccd39492c68f7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga66ea3f214385c395e5f14ca80a0655b0"></a>

```c
#define BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_3 BIT(2)
```

相关声明：[BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_3](#ga66ea3f214385c395e5f14ca80a0655b0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_gaa2c1c3d5e451df7ec58b4c8d3dedcf9a"></a>

```c
#define BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_4 BIT(3)
```

相关声明：[BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_4](#gaa2c1c3d5e451df7ec58b4c8d3dedcf9a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.3\_枚举（Enumerations）

<a id="r_ga9f286cdeeee0e9df06e6b3df1e9ab643"></a>

```c
enum bt_le_cs_sync_antenna_selection_opt { BT_LE_CS_ANTENNA_SELECTION_OPT_ONE = 0x01 , BT_LE_CS_ANTENNA_SELECTION_OPT_TWO = 0x02 , BT_LE_CS_ANTENNA_SELECTION_OPT_THREE = 0x03 , BT_LE_CS_ANTENNA_SELECTION_OPT_FOUR = 0x04 , BT_LE_CS_ANTENNA_SELECTION_OPT_REPETITIVE = 0xFE , BT_LE_CS_ANTENNA_SELECTION_OPT_NO_RECOMMENDATION = 0xFF }
```

相关声明：[bt_le_cs_sync_antenna_selection_opt](#ga9f286cdeeee0e9df06e6b3df1e9ab643)、[BT_LE_CS_ANTENNA_SELECTION_OPT_ONE](#gga9f286cdeeee0e9df06e6b3df1e9ab643a5de14d0cc770615bd08c4e3d197bae90)、[BT_LE_CS_ANTENNA_SELECTION_OPT_TWO](#gga9f286cdeeee0e9df06e6b3df1e9ab643a7ce16e0eab20cf432c8e93a7f6be8ca5)、[BT_LE_CS_ANTENNA_SELECTION_OPT_THREE](#gga9f286cdeeee0e9df06e6b3df1e9ab643a35ae07887f3d55bcbd10d531f09c841d)、[BT_LE_CS_ANTENNA_SELECTION_OPT_FOUR](#gga9f286cdeeee0e9df06e6b3df1e9ab643aa5370917d0f46fe654ba42fbbd587ceb)、[BT_LE_CS_ANTENNA_SELECTION_OPT_REPETITIVE](#gga9f286cdeeee0e9df06e6b3df1e9ab643aa23b552af8b16b1371f7a362089eaca7)、[BT_LE_CS_ANTENNA_SELECTION_OPT_NO_RECOMMENDATION](#gga9f286cdeeee0e9df06e6b3df1e9ab643a861f35bdbe322238bdad67568e5674f3)。

<a id="r_ga782a500f611320a6f3feed9897ab8e16"></a>

```c
enum bt_le_cs_test_cs_sync_antenna_selection { BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_ONE = 0x01 , BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_TWO = 0x02 , BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_THREE = 0x03 , BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_FOUR = 0x04 }
```

相关声明：[bt_le_cs_test_cs_sync_antenna_selection](#ga782a500f611320a6f3feed9897ab8e16)、[BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_ONE](#gga782a500f611320a6f3feed9897ab8e16a054f9b7f51323480106f11929425599f)、[BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_TWO](#gga782a500f611320a6f3feed9897ab8e16aa1931403e835ab2e18982dd0f2a67803)、[BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_THREE](#gga782a500f611320a6f3feed9897ab8e16aa059024bd3d90677ee00d4accd99f39c)、[BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_FOUR](#gga782a500f611320a6f3feed9897ab8e16a678e1a8120f21f3707d4b9ea22bd8c47)。

信道探测测试（CS Test）的 CS_SYNC 天线标识符（Antenna Identifier）。

<a id="r_gaf34c59887e8a6da0560b6428733fe8d0"></a>

```c
enum bt_le_cs_snr_control { BT_LE_CS_SNR_CONTROL_18dB = 0x0 , BT_LE_CS_SNR_CONTROL_21dB = 0x1 , BT_LE_CS_SNR_CONTROL_24dB = 0x2 , BT_LE_CS_SNR_CONTROL_27dB = 0x3 , BT_LE_CS_SNR_CONTROL_30dB = 0x4 , BT_LE_CS_SNR_CONTROL_NOT_USED = 0xFF }
```

相关声明：[bt_le_cs_snr_control](#gaf34c59887e8a6da0560b6428733fe8d0)、[BT_LE_CS_SNR_CONTROL_18dB](#ggaf34c59887e8a6da0560b6428733fe8d0a78af4f3bbf5adfc8ee6f9d459bb96e7d)、[BT_LE_CS_SNR_CONTROL_21dB](#ggaf34c59887e8a6da0560b6428733fe8d0a685a458547bda6af6c88626ee08c4110)、[BT_LE_CS_SNR_CONTROL_24dB](#ggaf34c59887e8a6da0560b6428733fe8d0a02394d7394f79a6e91a8f81070fdf82e)、[BT_LE_CS_SNR_CONTROL_27dB](#ggaf34c59887e8a6da0560b6428733fe8d0a43a7b210424a2aa2830a07676d3499b8)、[BT_LE_CS_SNR_CONTROL_30dB](#ggaf34c59887e8a6da0560b6428733fe8d0a18bb25e63782e9993a3853d929d58ee1)、[BT_LE_CS_SNR_CONTROL_NOT_USED](#ggaf34c59887e8a6da0560b6428733fe8d0a1a5c531f590f14773b7ddc9b0ec8cae9)。

信道探测信噪比控制选项（CS SNR Control Options）。

<a id="r_gaf50910d51c69e216ef6eb22b5c0f2d28"></a>

```c
enum bt_le_cs_test_override_3_pm_tone_ext { BT_LE_CS_TEST_OVERRIDE_3_NO_TONE_EXT = 0x0 , BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_TONE_EXT_ONLY = 0x1 , BT_LE_CS_TEST_OVERRIDE_3_REFLECTOR_TONE_EXT_ONLY = 0x2 , BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_AND_REFLECTOR_TONE_EXT , BT_LE_CS_TEST_OVERRIDE_3_REPETITIVE_TONE_EXT = 0x4 }
```

相关声明：[bt_le_cs_test_override_3_pm_tone_ext](#gaf50910d51c69e216ef6eb22b5c0f2d28)、[BT_LE_CS_TEST_OVERRIDE_3_NO_TONE_EXT](#ggaf50910d51c69e216ef6eb22b5c0f2d28aa5f4fea24a1b27736cfc36c470a3a008)、[BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_TONE_EXT_ONLY](#ggaf50910d51c69e216ef6eb22b5c0f2d28aee2c022be115a4c865d5524795f2d039)、[BT_LE_CS_TEST_OVERRIDE_3_REFLECTOR_TONE_EXT_ONLY](#ggaf50910d51c69e216ef6eb22b5c0f2d28ab504c3a24b36413ea2395bd579e5bba2)、[BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_AND_REFLECTOR_TONE_EXT](#ggaf50910d51c69e216ef6eb22b5c0f2d28ad2b323c3c54409545458c08fc6660cf4)、[BT_LE_CS_TEST_OVERRIDE_3_REPETITIVE_TONE_EXT](#ggaf50910d51c69e216ef6eb22b5c0f2d28a9a691cb7b4a9cff799d848fc79cf40dd)。

信道探测测试覆盖项 3（CS Test Override 3）：T_PM 音调扩展（Tone Extension）。

<a id="r_ga1ba4d7d919cb5c09469f8e8aa05bb04d"></a>

```c
enum bt_le_cs_test_override_4_tone_antenna_permutation { BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_00 = 0x0 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_01 = 0x1 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_02 = 0x2 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_03 = 0x3 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_04 = 0x4 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_05 = 0x5 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_06 = 0x6 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_07 = 0x7 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_08 = 0x8 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_09 = 0x9 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_10 = 0xA , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_11 = 0xB , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_12 = 0xC , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_13 = 0xD , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_14 = 0xE , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_15 = 0xF , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_16 = 0x10 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_17 = 0x11 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_18 = 0x12 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_19 = 0x13 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_20 = 0x14 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_21 = 0x15 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_22 = 0x16 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_23 = 0x17 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_LOOP }
```

相关声明：[bt_le_cs_test_override_4_tone_antenna_permutation](#ga1ba4d7d919cb5c09469f8e8aa05bb04d)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_00](#gga1ba4d7d919cb5c09469f8e8aa05bb04da72b3c5a4d07ae3c73e9bb131c725d17f)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_01](#gga1ba4d7d919cb5c09469f8e8aa05bb04da7aed472d8ed1b3fc84e89531134fc71c)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_02](#gga1ba4d7d919cb5c09469f8e8aa05bb04dab986f2c0c54de93cfdf5a5334aafffb2)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_03](#gga1ba4d7d919cb5c09469f8e8aa05bb04da7731f27f1af37ba740764e9875d28482)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_04](#gga1ba4d7d919cb5c09469f8e8aa05bb04da3fe0da05e9c2493af3ea42a0c6cd4b17)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_05](#gga1ba4d7d919cb5c09469f8e8aa05bb04daa73b01369a29b4ea7de2aadb71efe699)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_06](#gga1ba4d7d919cb5c09469f8e8aa05bb04dae4f815603cdffeb82711b994be2209dc)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_07](#gga1ba4d7d919cb5c09469f8e8aa05bb04da28e1b78a9bb927c4d38047e2aed57a15)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_08](#gga1ba4d7d919cb5c09469f8e8aa05bb04dab1cbcd7ceb33fb13b7d70b0dc671849c)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_09](#gga1ba4d7d919cb5c09469f8e8aa05bb04dae7f0fedfabe1748f9918befedbc45944)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_10](#gga1ba4d7d919cb5c09469f8e8aa05bb04da2ac77dab1caf34f436075dab45cc4aea)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_11](#gga1ba4d7d919cb5c09469f8e8aa05bb04dad85a40214189a9c036c95d88fb752a0c)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_12](#gga1ba4d7d919cb5c09469f8e8aa05bb04da45f979b88a3d63c4f270d246c98f3b53)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_13](#gga1ba4d7d919cb5c09469f8e8aa05bb04da2b34111edb7b0b1412de7d4485cbc164)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_14](#gga1ba4d7d919cb5c09469f8e8aa05bb04da5ab31e2b89fef73d838ade33de5d770b)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_15](#gga1ba4d7d919cb5c09469f8e8aa05bb04da144a6190783b1fbc5ccde1b9f0ec3581)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_16](#gga1ba4d7d919cb5c09469f8e8aa05bb04dae87750d18c24ddcece72919e107da671)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_17](#gga1ba4d7d919cb5c09469f8e8aa05bb04dabe494d770af056108d4679364a93acce)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_18](#gga1ba4d7d919cb5c09469f8e8aa05bb04daad5f0f4d2818f986472f8cca57b37ea9)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_19](#gga1ba4d7d919cb5c09469f8e8aa05bb04dac02f9fa05c0f35bb306fde66bc80ab21)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_20](#gga1ba4d7d919cb5c09469f8e8aa05bb04dad355ee587eff65a2a2f80274fc6c5081)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_21](#gga1ba4d7d919cb5c09469f8e8aa05bb04da3cc8b9dfadae103bdbb0fb79c523f553)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_22](#gga1ba4d7d919cb5c09469f8e8aa05bb04dadf2778f065f696ad43ceca71aa6a8a80)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_23](#gga1ba4d7d919cb5c09469f8e8aa05bb04dac3a263bfe1f80c38647d6aeab42b12c3)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_LOOP](#gga1ba4d7d919cb5c09469f8e8aa05bb04da2abd10e7d80703b3d849ad19d65af31f)。

信道探测测试覆盖项 4（CS Test Override 4）：音调天线排列（Tone Antenna Permutation）。

<a id="r_gacb3f437225ad1d6320ee424c39ebc82a"></a>

```c
enum bt_le_cs_test_override_7_ss_marker_value { BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_0011 = 0x0 , BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_1100 = 0x1 , BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_LOOP = 0x2 }
```

相关声明：[bt_le_cs_test_override_7_ss_marker_value](#gacb3f437225ad1d6320ee424c39ebc82a)、[BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_0011](#ggacb3f437225ad1d6320ee424c39ebc82aa99a26684d34169d062150f61cb0ba889)、[BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_1100](#ggacb3f437225ad1d6320ee424c39ebc82aa6b6bc126c5e2a97de33d6c83230ebb92)、[BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_LOOP](#ggacb3f437225ad1d6320ee424c39ebc82aa3a3078691c778d1c7a30fe9400bc5f0f)。

信道探测测试覆盖项 7（CS Test Override 7）：探测序列标记值（Sounding Sequence Marker Value）。

<a id="r_ga731bbaa98dab7c88725fc64b66da62eb"></a>

```c
enum bt_le_cs_test_override_8_cs_sync_payload_pattern { BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_PRBS9 = 0x00 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_11110000 = 0x01 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_10101010 = 0x02 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_PRBS15 = 0x03 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_11111111 = 0x04 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_00000000 = 0x05 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_00001111 = 0x06 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_01010101 = 0x07 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_USER = 0x80 }
```

相关声明：[bt_le_cs_test_override_8_cs_sync_payload_pattern](#ga731bbaa98dab7c88725fc64b66da62eb)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_PRBS9](#gga731bbaa98dab7c88725fc64b66da62eba3c8bc2a6858dc2d0de02b3b681a854a0)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_11110000](#gga731bbaa98dab7c88725fc64b66da62eba109f2588e566b9651b67dbbf9583813c)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_10101010](#gga731bbaa98dab7c88725fc64b66da62ebaef4b4455b236d70fae6a0138050d0835)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_PRBS15](#gga731bbaa98dab7c88725fc64b66da62eba1b910950b96ad0b47b0b235a2e8e45c8)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_11111111](#gga731bbaa98dab7c88725fc64b66da62ebabc520467cdbaaf34d0c815e0d62bd097)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_00000000](#gga731bbaa98dab7c88725fc64b66da62eba1b46b8b073ca599cb89d86b261fa4dd5)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_00001111](#gga731bbaa98dab7c88725fc64b66da62eba4f4ec5a6d46734e8c5801e9e79535b70)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_01010101](#gga731bbaa98dab7c88725fc64b66da62eba6c59258c52a5889e0b11aa0fb0f99bcb)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_USER](#gga731bbaa98dab7c88725fc64b66da62ebaf68334f70d91d587e906533ad544fef1)。

信道探测测试覆盖项 8（CS Test Override 8）：CS_SYNC 载荷模式（Payload Pattern）。

<a id="r_ga22822b2dd21d64c8c64a66f2b5dee9b1"></a>

```c
enum bt_le_cs_create_config_context { BT_LE_CS_CREATE_CONFIG_CONTEXT_LOCAL_ONLY , BT_LE_CS_CREATE_CONFIG_CONTEXT_LOCAL_AND_REMOTE }
```

相关声明：[bt_le_cs_create_config_context](#ga22822b2dd21d64c8c64a66f2b5dee9b1)、[BT_LE_CS_CREATE_CONFIG_CONTEXT_LOCAL_ONLY](#gga22822b2dd21d64c8c64a66f2b5dee9b1adb8a8af222fed7262bdb57bc4f18a706)、[BT_LE_CS_CREATE_CONFIG_CONTEXT_LOCAL_AND_REMOTE](#gga22822b2dd21d64c8c64a66f2b5dee9b1ae5107dfa011451ecaa404906fabc41e4)。

信道探测配置创建上下文（CS Config Creation Context）。

<a id="r_ga9e008daa9c0c1702aa3b4479e7a37ca4"></a>

```c
enum bt_le_cs_procedure_phy { BT_LE_CS_PROCEDURE_PHY_1M = 0x01 , BT_LE_CS_PROCEDURE_PHY_2M = 0x02 , BT_LE_CS_PROCEDURE_PHY_CODED_S8 = 0x03 , BT_LE_CS_PROCEDURE_PHY_CODED_S2 = 0x04 }
```

相关声明：[bt_le_cs_procedure_phy](#ga9e008daa9c0c1702aa3b4479e7a37ca4)、[BT_LE_CS_PROCEDURE_PHY_1M](#gga9e008daa9c0c1702aa3b4479e7a37ca4aa1dcc1e15aac59898c0a6c229593a76b)、[BT_LE_CS_PROCEDURE_PHY_2M](#gga9e008daa9c0c1702aa3b4479e7a37ca4a072649a66bf1260ce37bd16fc7a9185d)、[BT_LE_CS_PROCEDURE_PHY_CODED_S8](#gga9e008daa9c0c1702aa3b4479e7a37ca4a1ceb33afa661774e1077caced63bf263)、[BT_LE_CS_PROCEDURE_PHY_CODED_S2](#gga9e008daa9c0c1702aa3b4479e7a37ca4a5370237bdbceb37a631425f472ddc322)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_gaf99d82194bbcc471c3de2094b39a2201"></a>

```c
struct bt_le_cs_iq_sample bt_le_cs_parse_pct (const uint8_t pct[3])
```

相关声明：[bt_le_cs_iq_sample](../bluetooth_connection_model_reference/P095_bt_le_cs_iq_sample_结构体.md)、[bt_le_cs_parse_pct](#gaf99d82194bbcc471c3de2094b39a2201)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 HCI 格式的 PCT 中提取同相与正交分量（In-phase and Quadrature Terms）。

<a id="r_gaa979dc080cf277a2382b6ba77f8a1c09"></a>

```c
void bt_le_cs_set_valid_chmap_bits (uint8_t channel_map[10])
```

相关声明：[bt_le_cs_set_valid_chmap_bits](#gaa979dc080cf277a2382b6ba77f8a1c09)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置所有有效信道映射位（Channel Map Bits）。

<a id="r_gadb3afd94cd11d035cfe34c6a63b37b19"></a>

```c
int bt_le_cs_read_remote_supported_capabilities (struct bt_conn *conn)
```

相关声明：[bt_le_cs_read_remote_supported_capabilities](#gadb3afd94cd11d035cfe34c6a63b37b19)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取远端支持的能力（Remote Supported Capabilities）。

<a id="r_ga6ee9b8fa52b96dce41b1c879865fa938"></a>

```c
int bt_le_cs_set_default_settings (struct bt_conn *conn, const struct bt_le_cs_set_default_settings_param *params)
```

相关声明：[bt_le_cs_set_default_settings](#ga6ee9b8fa52b96dce41b1c879865fa938)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_cs_set_default_settings_param](../bluetooth_connection_model_reference/P097_bt_le_cs_set_default_settings_param_结构体.md)。

设置信道探测（Channel Sounding，CS）的默认设置。

<a id="r_ga127034536a98743d359c749fe7c79dba"></a>

```c
int bt_le_cs_read_remote_fae_table (struct bt_conn *conn)
```

相关声明：[bt_le_cs_read_remote_fae_table](#ga127034536a98743d359c749fe7c79dba)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取远端 FAE 表（Remote FAE Table）。

<a id="r_gaf03c4ed5c7e179ee3b374efa857188e2"></a>

```c
int bt_le_cs_test_cb_register (struct bt_le_cs_test_cb cs_test_cb)
```

相关声明：[bt_le_cs_test_cb_register](#gaf03c4ed5c7e179ee3b374efa857188e2)、[bt_le_cs_test_cb](../bluetooth_connection_model_reference/P100_bt_le_cs_test_cb_结构体.md)。

注册信道探测测试模式（CS Test Mode）的回调。

<a id="r_gada91ff7c7a82620d77bf78781ebea356"></a>

```c
int bt_le_cs_start_test (const struct bt_le_cs_test_param *params)
```

相关声明：[bt_le_cs_start_test](#gada91ff7c7a82620d77bf78781ebea356)、[bt_le_cs_test_param](../bluetooth_connection_model_reference/P101_bt_le_cs_test_param_结构体.md)。

启动信道探测测试（CS Test）。

<a id="r_ga27bae87f9769a2d5802c57adfa201b23"></a>

```c
int bt_le_cs_create_config (struct bt_conn *conn, struct bt_le_cs_create_config_params *params, enum bt_le_cs_create_config_context context)
```

相关声明：[bt_le_cs_create_config](#ga27bae87f9769a2d5802c57adfa201b23)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_cs_create_config_params](../bluetooth_connection_model_reference/P094_bt_le_cs_create_config_params_结构体.md)、[bt_le_cs_create_config_context](#ga22822b2dd21d64c8c64a66f2b5dee9b1)。

创建信道探测配置（CS Configuration）。

<a id="r_ga2a27b80e72ff2bfe986b3cbe11f225f3"></a>

```c
int bt_le_cs_remove_config (struct bt_conn *conn, uint8_t config_id)
```

相关声明：[bt_le_cs_remove_config](#ga2a27b80e72ff2bfe986b3cbe11f225f3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

移除信道探测配置（CS Configuration）。

<a id="r_ga4742baeb1eb46969233f787344cb5e11"></a>

```c
int bt_le_cs_stop_test (void)
```

相关声明：[bt_le_cs_stop_test](#ga4742baeb1eb46969233f787344cb5e11)。

停止正在进行的信道探测测试（CS Test）。

<a id="r_gadcd85f3799f4219a01e84fc281ff1a31"></a>

```c
void bt_le_cs_step_data_parse (struct net_buf_simple *step_data_buf, bool(*func)(struct bt_le_cs_subevent_step *step, void *user_data), void *user_data)
```

相关声明：[bt_le_cs_step_data_parse](#gadcd85f3799f4219a01e84fc281ff1a31)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_le_cs_subevent_step](../bluetooth_connection_model_reference/P099_bt_le_cs_subevent_step_结构体.md)。

解析信道探测子事件步骤数据（CS Subevent Step Data）。

<a id="r_ga346a46dc3321c5bab034904bf09aa4e3"></a>

```c
int bt_le_cs_security_enable (struct bt_conn *conn)
```

相关声明：[bt_le_cs_security_enable](#ga346a46dc3321c5bab034904bf09aa4e3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

启用信道探测安全（CS Security Enable）。

<a id="r_ga2b6f3c3795b5eeb424542c1858f84cbc"></a>

```c
int bt_le_cs_procedure_enable (struct bt_conn *conn, const struct bt_le_cs_procedure_enable_param *params)
```

相关声明：[bt_le_cs_procedure_enable](#ga2b6f3c3795b5eeb424542c1858f84cbc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_cs_procedure_enable_param](../bluetooth_connection_model_reference/P096_bt_le_cs_procedure_enable_param_结构体.md)。

启用信道探测过程（CS Procedure Enable）。

<a id="r_gad6e0fb9c7f92678598d9780b78710961"></a>

```c
int bt_le_cs_set_procedure_parameters (struct bt_conn *conn, const struct bt_le_cs_set_procedure_parameters_param *params)
```

相关声明：[bt_le_cs_set_procedure_parameters](#gad6e0fb9c7f92678598d9780b78710961)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_cs_set_procedure_parameters_param](../bluetooth_connection_model_reference/P098_bt_le_cs_set_procedure_parameters_param_结构体.md)。

设置信道探测过程参数（CS Procedure Parameters）。

<a id="r_gafcd6a882c0da413bfef5a56e53323389"></a>

```c
int bt_le_cs_set_channel_classification (uint8_t channel_classification[10])
```

相关声明：[bt_le_cs_set_channel_classification](#gafcd6a882c0da413bfef5a56e53323389)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置信道探测信道分类（CS Channel Classification）。

<a id="r_gaa49ff6e8340bd1753485deeec8036d1b"></a>

```c
int bt_le_cs_read_local_supported_capabilities (struct bt_conn_le_cs_capabilities *ret)
```

相关声明：[bt_le_cs_read_local_supported_capabilities](#gaa49ff6e8340bd1753485deeec8036d1b)、[bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)。

读取信道探测本地支持的能力（CS Local Supported Capabilities）。

<a id="r_ga62ae42071ed68bd1021d368304aa4d40"></a>

```c
int bt_le_cs_read_local_supported_capabilities_v2 (struct bt_conn_le_cs_capabilities *ret)
```

相关声明：[bt_le_cs_read_local_supported_capabilities_v2](#ga62ae42071ed68bd1021d368304aa4d40)、[bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)。

读取信道探测本地支持的能力，第 2 版（CS Local Supported Capabilities V2）。

<a id="r_ga9d4b5b21886f0dd89b4073acaaa787a1"></a>

```c
int bt_le_cs_write_cached_remote_supported_capabilities (struct bt_conn *conn, const struct bt_conn_le_cs_capabilities *params)
```

相关声明：[bt_le_cs_write_cached_remote_supported_capabilities](#ga9d4b5b21886f0dd89b4073acaaa787a1)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)。

写入缓存的信道探测远端支持能力（CS Cached Remote Supported Capabilities）。

<a id="r_ga19b1a269b7202a94c6bd5153498a09c7"></a>

```c
int bt_le_cs_write_cached_remote_supported_capabilities_v2 (struct bt_conn *conn, const struct bt_conn_le_cs_capabilities *params)
```

相关声明：[bt_le_cs_write_cached_remote_supported_capabilities_v2](#ga19b1a269b7202a94c6bd5153498a09c7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)。

写入缓存的信道探测远端支持能力，第 2 版（CS Cached Remote Supported Capabilities V2）。

<a id="r_ga63aa61d2bd3cf9ecb3ea9f1d02bb5b8c"></a>

```c
int bt_le_cs_write_cached_remote_fae_table (struct bt_conn *conn, int8_t remote_fae_table[72])
```

相关声明：[bt_le_cs_write_cached_remote_fae_table](#ga63aa61d2bd3cf9ecb3ea9f1d02bb5b8c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

写入缓存的信道探测远端 FAE 表（CS Cached Remote FAE Table）。

<a id="r_gaa9126eca834eee8e088d01295d4cf94f"></a>

```c
int bt_le_cs_get_antenna_path (uint8_t n_ap, uint8_t antenna_path_permutation_index, uint8_t tone_index)
```

相关声明：[bt_le_cs_get_antenna_path](#gaa9126eca834eee8e088d01295d4cf94f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在模式 2 或模式 3 的信道探测过程（CS Procedure）使用多条天线路径时，获取音调交换（Tone Exchange）所使用的天线路径（Antenna Path）。

## 4.5\_详细说明（Detailed Documentation）

<a id="ga95e2d24515e45096912440fe8a6bd3a0"></a>

### `BT_LE_CS_CHANNEL_BIT_GET`

```c
#define BT_LE_CS_CHANNEL_BIT_GET ( chmap, bit )
```

```c
#include <zephyr/bluetooth/cs.h>
```

展开值（Value）：

```c
(((chmap)[(bit) / 8] >> ((bit) % 8)) & 1)
```

获取信道探测（CS）信道映射中特定位的宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] chmap` | 信道映射数组（Channel Map Array）。 |
| `[in] bit` | 要访问的位号（Bit Number）。 |

**返回（Returns）**：返回：位值（Bit Value），为 1 或 0。

<a id="gadcd3351ef99d42e93c89d48f1c8ba668"></a>

### `BT_LE_CS_CHANNEL_BIT_SET_VAL`

```c
#define BT_LE_CS_CHANNEL_BIT_SET_VAL ( chmap, bit, val )
```

```c
#include <zephyr/bluetooth/cs.h>
```

展开值（Value）：

```c
((chmap)[(bit) / 8] = ((chmap)[(bit) / 8] & ~BIT((bit) % 8)) | ((val) << ((bit) % 8)))
```

设置信道探测（CS）信道映射中特定位值的宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] chmap` | 信道映射数组（Channel Map Array）。 |
| `[in] bit` | 要访问的位号（Bit Number）。 |
| `[in] val` | 要设置的位值（Bit Value），为 1 或 0。 |

<a id="gaf278a44ad602ce7e365ac0d71bcc48b4"></a>

### `BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_1`

```c
#define BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_1 BIT(0)
```

```c
#include <zephyr/bluetooth/cs.h>
```

<a id="ga5ff36f6e97668a9d1b6ccd39492c68f7"></a>

### `BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_2`

```c
#define BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_2 BIT(1)
```

```c
#include <zephyr/bluetooth/cs.h>
```

<a id="ga66ea3f214385c395e5f14ca80a0655b0"></a>

### `BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_3`

```c
#define BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_3 BIT(2)
```

```c
#include <zephyr/bluetooth/cs.h>
```

<a id="gaa2c1c3d5e451df7ec58b4c8d3dedcf9a"></a>

### `BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_4`

```c
#define BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_4 BIT(3)
```

```c
#include <zephyr/bluetooth/cs.h>
```

<a id="ga22822b2dd21d64c8c64a66f2b5dee9b1"></a>

### `bt_le_cs_create_config_context`

```c
enum bt_le_cs_create_config_context
```

```c
#include <zephyr/bluetooth/cs.h>
```

信道探测配置创建上下文（CS Config Creation Context）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_CS_CREATE_CONFIG_CONTEXT_LOCAL_ONLY` | 仅向本地控制器写入信道探测配置（CS Configuration）。 |
| `BT_LE_CS_CREATE_CONFIG_CONTEXT_LOCAL_AND_REMOTE` | 通过信道探测配置过程（Channel Sounding Configuration Procedure），向本地与远端控制器都写入 CS 配置。 |

<a id="ga9e008daa9c0c1702aa3b4479e7a37ca4"></a>

### `bt_le_cs_procedure_phy`

```c
enum bt_le_cs_procedure_phy
```

```c
#include <zephyr/bluetooth/cs.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_CS_PROCEDURE_PHY_1M` |  |
| `BT_LE_CS_PROCEDURE_PHY_2M` |  |
| `BT_LE_CS_PROCEDURE_PHY_CODED_S8` |  |
| `BT_LE_CS_PROCEDURE_PHY_CODED_S2` |  |

<a id="gaf34c59887e8a6da0560b6428733fe8d0"></a>

### `bt_le_cs_snr_control`

```c
enum bt_le_cs_snr_control
```

```c
#include <zephyr/bluetooth/cs.h>
```

信道探测信噪比控制选项（CS SNR Control Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_CS_SNR_CONTROL_18dB` |  |
| `BT_LE_CS_SNR_CONTROL_21dB` |  |
| `BT_LE_CS_SNR_CONTROL_24dB` |  |
| `BT_LE_CS_SNR_CONTROL_27dB` |  |
| `BT_LE_CS_SNR_CONTROL_30dB` |  |
| `BT_LE_CS_SNR_CONTROL_NOT_USED` |  |

<a id="ga9f286cdeeee0e9df06e6b3df1e9ab643"></a>

### `bt_le_cs_sync_antenna_selection_opt`

```c
enum bt_le_cs_sync_antenna_selection_opt
```

```c
#include <zephyr/bluetooth/cs.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_CS_ANTENNA_SELECTION_OPT_ONE` | CS_SYNC 数据包使用天线标识符（Antenna Identifier）1。 |
| `BT_LE_CS_ANTENNA_SELECTION_OPT_TWO` | CS_SYNC 数据包使用天线标识符（Antenna Identifier）2。 |
| `BT_LE_CS_ANTENNA_SELECTION_OPT_THREE` | CS_SYNC 数据包使用天线标识符（Antenna Identifier）3。 |
| `BT_LE_CS_ANTENNA_SELECTION_OPT_FOUR` | CS_SYNC 数据包使用天线标识符（Antenna Identifier）4。 |
| `BT_LE_CS_ANTENNA_SELECTION_OPT_REPETITIVE` | CS_SYNC 数据包按 1 到 4 的顺序循环使用天线（Antennas）。 |
| `BT_LE_CS_ANTENNA_SELECTION_OPT_NO_RECOMMENDATION` | 不对本地控制器的天线选择（Antenna Selection）提供建议。 |

<a id="ga782a500f611320a6f3feed9897ab8e16"></a>

### `bt_le_cs_test_cs_sync_antenna_selection`

```c
enum bt_le_cs_test_cs_sync_antenna_selection
```

```c
#include <zephyr/bluetooth/cs.h>
```

信道探测测试（CS Test）的 CS_SYNC 天线标识符（Antenna Identifier）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_ONE` |  |
| `BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_TWO` |  |
| `BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_THREE` |  |
| `BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_FOUR` |  |

<a id="gaf50910d51c69e216ef6eb22b5c0f2d28"></a>

### `bt_le_cs_test_override_3_pm_tone_ext`

```c
enum bt_le_cs_test_override_3_pm_tone_ext
```

```c
#include <zephyr/bluetooth/cs.h>
```

信道探测测试覆盖项 3（CS Test Override 3）：T_PM 音调扩展（Tone Extension）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_CS_TEST_OVERRIDE_3_NO_TONE_EXT` | 发起方（Initiator）和反射方（Reflector）均发送不带音调扩展（Tone Extension）的音调。 |
| `BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_TONE_EXT_ONLY` | 发起方（Initiator）发送带扩展的音调，反射方（Reflector）发送不带扩展的音调。 |
| `BT_LE_CS_TEST_OVERRIDE_3_REFLECTOR_TONE_EXT_ONLY` | 发起方（Initiator）发送不带扩展的音调，反射方（Reflector）发送带扩展的音调。 |
| `BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_AND_REFLECTOR_TONE_EXT` | 发起方（Initiator）和反射方（Reflector）均发送带音调扩展（Tone Extension）的音调。 |
| `BT_LE_CS_TEST_OVERRIDE_3_REPETITIVE_TONE_EXT` | 仅适用于模式 2（Mode-2）和模式 3（Mode-3）。循环遍历以下值：BT_LE_CS_TEST_OVERRIDE_3_NO_TONE_EXT、BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_TONE_EXT_ONLY、BT_LE_CS_TEST_OVERRIDE_3_REFLECTOR_TONE_EXT_ONLY、BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_AND_REFLECTOR_TONE_EXT。 |

<a id="ga1ba4d7d919cb5c09469f8e8aa05bb04d"></a>

### `bt_le_cs_test_override_4_tone_antenna_permutation`

```c
enum bt_le_cs_test_override_4_tone_antenna_permutation
```

```c
#include <zephyr/bluetooth/cs.h>
```

信道探测测试覆盖项 4（CS Test Override 4）：音调天线排列（Tone Antenna Permutation）。

这些值表示天线路径排列（Antenna Path Permutation）表中的索引。

适用哪个表以及哪些索引有效，取决于天线路径的最大数量（N_AP）。

N_AP = 2 时，排列表（Permutation Table）为：

天线路径排列索引（Antenna Path Permutation Index）与排列后的天线路径位置（Antenna Path Positions After Permutation）：

| 索引 | 路径位置 |
| --- | --- |
| 0 | A1 A2 |
| 1 | A2 A1 |

N_AP = 3 时，排列表（Permutation Table）为：

天线路径排列索引（Antenna Path Permutation Index）与排列后的天线路径位置（Antenna Path Positions After Permutation）：

| 索引 | 路径位置 |
| --- | --- |
| 0 | A1 A2 A3 |
| 1 | A2 A1 A3 |
| 2 | A1 A3 A2 |
| 3 | A3 A1 A2 |
| 4 | A3 A2 A1 |
| 5 | A2 A3 A1 |

N_AP = 4 时，排列表（Permutation Table）为：

天线路径排列索引（Antenna Path Permutation Index）与排列后的天线路径位置（Antenna Path Positions After Permutation）：

| 索引 | 路径位置 |
| --- | --- |
| 0 | A1 A2 A3 A4 |
| 1 | A2 A1 A3 A4 |
| 2 | A1 A3 A2 A4 |
| 3 | A3 A1 A2 A4 |
| 4 | A3 A2 A1 A4 |
| 5 | A2 A3 A1 A4 |
| 6 | A1 A2 A4 A3 |
| 7 | A2 A1 A4 A3 |
| 8 | A1 A4 A2 A3 |
| 9 | A4 A1 A2 A3 |
| 10 | A4 A2 A1 A3 |
| 11 | A2 A4 A1 A3 |
| 12 | A1 A4 A3 A2 |
| 13 | A4 A1 A3 A2 |
| 14 | A1 A3 A4 A2 |
| 15 | A3 A1 A4 A2 |
| 16 | A3 A4 A1 A2 |
| 17 | A4 A3 A1 A2 |
| 18 | A4 A2 A3 A1 |
| 19 | A2 A4 A3 A1 |
| 20 | A4 A3 A2 A1 |
| 21 | A3 A4 A2 A1 |
| 22 | A3 A2 A4 A1 |
| 23 | A2 A3 A4 A1 |

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_00` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_01` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_02` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_03` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_04` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_05` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_06` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_07` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_08` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_09` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_10` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_11` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_12` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_13` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_14` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_15` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_16` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_17` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_18` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_19` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_20` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_21` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_22` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_23` |  |
| `BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_LOOP` | 从最低索引开始，循环遍历全部有效的天线排列索引（Antenna Permutation Indices）。 |

<a id="gacb3f437225ad1d6320ee424c39ebc82a"></a>

### `bt_le_cs_test_override_7_ss_marker_value`

```c
enum bt_le_cs_test_override_7_ss_marker_value
```

```c
#include <zephyr/bluetooth/cs.h>
```

信道探测测试覆盖项 7（CS Test Override 7）：探测序列标记值（Sounding Sequence Marker Value）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_0011` |  |
| `BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_1100` |  |
| `BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_LOOP` | 按发送顺序循环使用模式 '0011' 和 '1100'（Patterns）。 |

<a id="ga731bbaa98dab7c88725fc64b66da62eb"></a>

### `bt_le_cs_test_override_8_cs_sync_payload_pattern`

```c
enum bt_le_cs_test_override_8_cs_sync_payload_pattern
```

```c
#include <zephyr/bluetooth/cs.h>
```

信道探测测试覆盖项 8（CS Test Override 8）：CS_SYNC 载荷模式（Payload Pattern）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_PRBS9` | 伪随机二进制序列 PRBS9 有效载荷序列（Payload Sequence）。 |
| `BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_11110000` | 重复 '11110000' 的有效载荷序列（Payload Sequence）。 |
| `BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_10101010` | 重复 '10101010' 的有效载荷序列（Payload Sequence）。 |
| `BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_PRBS15` | 伪随机二进制序列 PRBS15 有效载荷序列（Payload Sequence）。 |
| `BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_11111111` | 重复 '11111111' 的有效载荷序列（Payload Sequence）。 |
| `BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_00000000` | 重复 '00000000' 的有效载荷序列（Payload Sequence）。 |
| `BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_00001111` | 重复 '00001111' 的有效载荷序列（Payload Sequence）。 |
| `BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_01010101` | 重复 '01010101' 的有效载荷序列（Payload Sequence）。 |
| `BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_USER` | 使用者提供的自定义有效载荷（Custom Payload）。 |

<a id="ga27bae87f9769a2d5802c57adfa201b23"></a>

### `bt_le_cs_create_config()`

```c
int bt_le_cs_create_config ( struct bt_conn * conn, struct bt_le_cs_create_config_params * params, enum bt_le_cs_create_config_context context )
```

```c
#include <zephyr/bluetooth/cs.h>
```

创建信道探测配置（CS Configuration）。

此命令用于创建新的信道探测配置（CS Configuration），或更新具有指定配置 ID 的现有配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | CS 创建配置参数（CS Create Config Parameters）。 |
| `context` | 控制配置是只写入本地控制器，还是同时写入本地与远端控制器（Controller）。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gaa9126eca834eee8e088d01295d4cf94f"></a>

### `bt_le_cs_get_antenna_path()`

```c
int bt_le_cs_get_antenna_path ( uint8_t n_ap, uint8_t antenna_path_permutation_index, uint8_t tone_index )
```

```c
#include <zephyr/bluetooth/cs.h>
```

在模式 2 或模式 3 的信道探测过程（CS Procedure）使用多条天线路径时，获取音调交换（Tone Exchange）所使用的天线路径（Antenna Path）。

此函数实现《蓝牙核心规范》（Bluetooth Core Specification）6.0 第 6 卷 H 部分 4.7.5 节定义的天线路径排列（Antenna Path Permutation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `n_ap` | 天线路径数量（Number of Antenna Paths），范围为 [1, 4]。 |
| `antenna_path_permutation_index` | 天线路径排列索引（Antenna Path Permutation Index）。 |
| `tone_index` | CS 步骤（CS Step）中的音调索引，范围为 [0, n_ap]。tone_index = n_ap 对应扩展时隙（Extension Slot）。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：用于交换 CS 音调的天线路径（Antenna Path），范围为 [0, 3]；参数无效时返回 -EINVAL。

<a id="gaf99d82194bbcc471c3de2094b39a2201"></a>

### `bt_le_cs_parse_pct()`

```c
struct bt_le_cs_iq_sample bt_le_cs_parse_pct ( const uint8_t pct[3])
```

```c
#include <zephyr/bluetooth/cs.h>
```

从 HCI 格式的 PCT 中提取同相与正交分量（In-phase and Quadrature Terms）。

用于处理 CS 步骤数据中 24 位相位校正项（Phase Correction Terms）的便捷函数。将 12 位有符号实部与虚部分量转换为主机字节序（Host Endianness），并进行符号扩展（Sign Extension）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pct` | 24 位小端序相位校正项（Little-endian Phase Correction Term）。 |

**返回（Returns）**：返回：struct bt_le_cs_iq_sample，其中实部与虚部以 int16_t 表示。

<a id="ga2b6f3c3795b5eeb424542c1858f84cbc"></a>

### `bt_le_cs_procedure_enable()`

```c
int bt_le_cs_procedure_enable ( struct bt_conn * conn, const struct bt_le_cs_procedure_enable_param * params )
```

```c
#include <zephyr/bluetooth/cs.h>
```

启用信道探测过程（CS Procedure Enable）。

此命令启用或禁用本地控制器对信道探测过程（CS Procedures）的调度，远端设备由 conn 参数标识。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | CS 过程使能命令（CS Procedure Enable）的参数。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gaa49ff6e8340bd1753485deeec8036d1b"></a>

### `bt_le_cs_read_local_supported_capabilities()`

```c
int bt_le_cs_read_local_supported_capabilities ( struct bt_conn_le_cs_capabilities * ret)
```

```c
#include <zephyr/bluetooth/cs.h>
```

读取信道探测本地支持的能力（CS Local Supported Capabilities）。

此命令读取本地控制器支持的信道探测能力（CS Capabilities）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ret` | CS 过程使能命令（CS Procedure Enable）的返回值。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga62ae42071ed68bd1021d368304aa4d40"></a>

### `bt_le_cs_read_local_supported_capabilities_v2()`

```c
int bt_le_cs_read_local_supported_capabilities_v2 ( struct bt_conn_le_cs_capabilities * ret)
```

```c
#include <zephyr/bluetooth/cs.h>
```

读取信道探测本地支持的能力，第 2 版（CS Local Supported Capabilities V2）。

此命令读取本地控制器支持的信道探测能力（CS Capabilities）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ret` | CS 过程使能命令（CS Procedure Enable）的返回值。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga127034536a98743d359c749fe7c79dba"></a>

### `bt_le_cs_read_remote_fae_table()`

```c
int bt_le_cs_read_remote_fae_table ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/cs.h>
```

读取远端 FAE 表（Remote FAE Table）。

此命令读取远端控制器逐信道的模式 0 频率执行误差表（Frequency Actuation Error Table）。

如果远端控制器在反射方角色（Reflector Role）下的模式 0 发送支持零频率执行误差（FAE），参见 bt_conn_le_cs_capabilities::cs_without_fae_supported，则无需调用此函数；调用后会产生带错误码的远端 FAE 表读取完成事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gadb3afd94cd11d035cfe34c6a63b37b19"></a>

### `bt_le_cs_read_remote_supported_capabilities()`

```c
int bt_le_cs_read_remote_supported_capabilities ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/cs.h>
```

读取远端支持的能力（Remote Supported Capabilities）。

此命令查询远端控制器支持的信道探测能力（CS Capabilities）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga2a27b80e72ff2bfe986b3cbe11f225f3"></a>

### `bt_le_cs_remove_config()`

```c
int bt_le_cs_remove_config ( struct bt_conn * conn, uint8_t config_id )
```

```c
#include <zephyr/bluetooth/cs.h>
```

移除信道探测配置（CS Configuration）。

此命令从本地控制器移除由 config_id 标识的信道探测配置（CS Configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `config_id` | CS 配置 ID（Config ID）。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga346a46dc3321c5bab034904bf09aa4e3"></a>

### `bt_le_cs_security_enable()`

```c
int bt_le_cs_security_enable ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/cs.h>
```

启用信道探测安全（CS Security Enable）。

此命令针对 conn 参数标识的 ACL 连接，在本地控制器中启动或重新启动信道探测安全启动过程（Channel Sounding Security Start Procedure）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gafcd6a882c0da413bfef5a56e53323389"></a>

### `bt_le_cs_set_channel_classification()`

```c
int bt_le_cs_set_channel_classification ( uint8_t channel_classification[10])
```

```c
#include <zephyr/bluetooth/cs.h>
```

设置信道探测信道分类（CS Channel Classification）。

此命令根据本地信息更新信道分类（Channel Classification）。

第 n 位（n 范围为 0 到 78）保存 CS 信道索引 n 的值：1 表示信道启用（Enabled），0 表示信道禁用（Disabled）。

信道 n = 0、1、23、24、25、77 和 78 保留供未来使用，须设为 0。必须至少启用 15 个信道。

最高有效位（Most Significant Bit），即第 79 位，保留供未来使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel_classification` | 位域（Bit Fields）。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga6ee9b8fa52b96dce41b1c879865fa938"></a>

### `bt_le_cs_set_default_settings()`

```c
int bt_le_cs_set_default_settings ( struct bt_conn * conn, const struct bt_le_cs_set_default_settings_param * params )
```

```c
#include <zephyr/bluetooth/cs.h>
```

设置信道探测（Channel Sounding，CS）的默认设置。

此命令为该连接设置默认信道探测设置（Channel Sounding Settings）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 信道探测默认设置参数（Channel Sounding Default Settings Parameters）。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gad6e0fb9c7f92678598d9780b78710961"></a>

### `bt_le_cs_set_procedure_parameters()`

```c
int bt_le_cs_set_procedure_parameters ( struct bt_conn * conn, const struct bt_le_cs_set_procedure_parameters_param * params )
```

```c
#include <zephyr/bluetooth/cs.h>
```

设置信道探测过程参数（CS Procedure Parameters）。

此命令设置本地控制器调度一个或多个 CS 过程（CS Procedures）的参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | CS 设置过程参数命令（CS Set Procedure Parameters）的参数。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gaa979dc080cf277a2382b6ba77f8a1c09"></a>

### `bt_le_cs_set_valid_chmap_bits()`

```c
void bt_le_cs_set_valid_chmap_bits ( uint8_t channel_map[10])
```

```c
#include <zephyr/bluetooth/cs.h>
```

设置所有有效信道映射位（Channel Map Bits）。

此命令启用给定 CS 信道映射（Channel Map）中的全部有效信道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel_map` | 信道映射（Channel Map）。 |

<a id="gada91ff7c7a82620d77bf78781ebea356"></a>

### `bt_le_cs_start_test()`

```c
int bt_le_cs_start_test ( const struct bt_le_cs_test_param * params)
```

```c
#include <zephyr/bluetooth/cs.h>
```

启动信道探测测试（CS Test）。

此命令启动 CS 测试，将被测实现（Implementation Under Test，IUT）置于发起方（Initiator）或反射方（Reflector）角色。

列表中的第一个模式 0 信道用作测试起始信道。每次测试开始时，处于反射方角色（Reflector Role）的 IUT 须在第一个模式 0 信道上监听，直到收到发起方的第一次发送。类似地，IUT 处于发起方角色（Initiator Role）时，测试器先在第一个模式 0 信道上监听，IUT 须在第一个 CS 步骤的前半段通过该信道发送。此后，此命令的参数描述 CS 测试所需的收发行为。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `params` | 信道探测测试（CS Test）的参数。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING_TEST。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gadcd85f3799f4219a01e84fc281ff1a31"></a>

### `bt_le_cs_step_data_parse()`

```c
void bt_le_cs_step_data_parse ( struct net_buf_simple * step_data_buf, bool(* func )(struct bt_le_cs_subevent_step *step, void *user_data), void * user_data )
```

```c
#include <zephyr/bluetooth/cs.h>
```

解析信道探测子事件步骤数据（CS Subevent Step Data）。

用于解析信道探测子事件结果（Channel Sounding Subevent Results）中 HCI 格式步骤数据（Step Data）的辅助函数。

典型用途是过滤不满足特定数据包质量（Packet Quality）或 NADM 要求的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `step_data_buf` | 指向包含步骤数据（Step Data）的缓冲区的指针。 |
| `func` | 每找到一项步骤数据（Step Data）就调用的回调函数。回调返回 true 表示继续解析，返回 false 表示停止。 |
| `user_data` | 要传递给回调（Callback）的用户数据（User Data）。 |

**警告（Warning）**：警告：此函数在解析时会消耗数据（Consume the Data）。

<a id="ga4742baeb1eb46969233f787344cb5e11"></a>

### `bt_le_cs_stop_test()`

```c
int bt_le_cs_stop_test ( void )
```

```c
#include <zephyr/bluetooth/cs.h>
```

停止正在进行的信道探测测试（CS Test）。

此命令停止任何正在进行的 CS 测试（CS Test）。

控制器应在完成此次终止前，报告完全部子事件结果（Subevent Results）。

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING_TEST。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gaf03c4ed5c7e179ee3b374efa857188e2"></a>

### `bt_le_cs_test_cb_register()`

```c
int bt_le_cs_test_cb_register ( struct bt_le_cs_test_cb cs_test_cb)
```

```c
#include <zephyr/bluetooth/cs.h>
```

注册信道探测测试模式（CS Test Mode）的回调。

可通过提供 NULL 函数指针注销现有回调（Callbacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cs_test_cb` | CS 测试（CS Test）使用的一组回调。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING_TEST。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga63aa61d2bd3cf9ecb3ea9f1d02bb5b8c"></a>

### `bt_le_cs_write_cached_remote_fae_table()`

```c
int bt_le_cs_write_cached_remote_fae_table ( struct bt_conn * conn, int8_t remote_fae_table[72] )
```

```c
#include <zephyr/bluetooth/cs.h>
```

写入缓存的信道探测远端 FAE 表（CS Cached Remote FAE Table）。

此命令将远端设备逐信道模式 0 频率执行误差表（Frequency Actuation Error Table）的缓存副本写入本地控制器。

如果远端控制器在反射方角色（Reflector Role）下的模式 0 发送支持零频率执行误差（FAE），参见 bt_conn_le_cs_capabilities::cs_without_fae_supported，则无需调用此函数；调用后会返回错误码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `remote_fae_table` | 本地控制器逐信道的模式 0 FAE 表（Per-channel Mode-0 FAE Table）。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga9d4b5b21886f0dd89b4073acaaa787a1"></a>

### `bt_le_cs_write_cached_remote_supported_capabilities()`

```c
int bt_le_cs_write_cached_remote_supported_capabilities ( struct bt_conn * conn, const struct bt_conn_le_cs_capabilities * params )
```

```c
#include <zephyr/bluetooth/cs.h>
```

写入缓存的信道探测远端支持能力（CS Cached Remote Supported Capabilities）。

此命令为指定连接写入远端控制器支持的 CS 能力（CS Capabilities）的缓存副本。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | CS 写入缓存的远端支持能力命令（CS Write Cached Remote Supported Capabilities）的参数。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga19b1a269b7202a94c6bd5153498a09c7"></a>

### `bt_le_cs_write_cached_remote_supported_capabilities_v2()`

```c
int bt_le_cs_write_cached_remote_supported_capabilities_v2 ( struct bt_conn * conn, const struct bt_conn_le_cs_capabilities * params )
```

```c
#include <zephyr/bluetooth/cs.h>
```

写入缓存的信道探测远端支持能力，第 2 版（CS Cached Remote Supported Capabilities V2）。

此命令为指定连接写入远端控制器支持的 CS 能力（CS Capabilities）的缓存副本。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | CS 写入缓存的远端支持能力命令（CS Write Cached Remote Supported Capabilities）的参数。 |

**说明（Note）**：注意：使用此 API 必须设置 CONFIG_BT_CHANNEL_SOUNDING。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。


## 4.6\_原页交叉引用（Cross References）

- [bt_le_cs_set_default_settings_param](../bluetooth_connection_model_reference/P097_bt_le_cs_set_default_settings_param_结构体.md)
- [bt_le_cs_test_param](../bluetooth_connection_model_reference/P101_bt_le_cs_test_param_结构体.md)
- [bt_le_cs_create_config_params](../bluetooth_connection_model_reference/P094_bt_le_cs_create_config_params_结构体.md)
- [bt_le_cs_test_cb](../bluetooth_connection_model_reference/P100_bt_le_cs_test_cb_结构体.md)
- [bt_le_cs_subevent_step](../bluetooth_connection_model_reference/P099_bt_le_cs_subevent_step_结构体.md)
- [bt_le_cs_iq_sample](../bluetooth_connection_model_reference/P095_bt_le_cs_iq_sample_结构体.md)
- [bt_le_cs_procedure_enable_param](../bluetooth_connection_model_reference/P096_bt_le_cs_procedure_enable_param_结构体.md)
- [bt_le_cs_set_procedure_parameters_param](../bluetooth_connection_model_reference/P098_bt_le_cs_set_procedure_parameters_param_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [zephyr/bluetooth/cs.h](../api_file_clock_network_reference/P004_zephyr__bluetooth__cs.h_文件参考.md)
- [CONFIG_BT_CHANNEL_SOUNDING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CHANNEL_SOUNDING)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_conn_le_cs_capabilities::cs_without_fae_supported](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md#a22604c052da2f8ccf77c81a0a5c628b7)
- [CONFIG_BT_CHANNEL_SOUNDING_TEST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CHANNEL_SOUNDING_TEST)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga22822b2dd21d64c8c64a66f2b5dee9b1adb8a8af222fed7262bdb57bc4f18a706"></a>
<a id="gga22822b2dd21d64c8c64a66f2b5dee9b1ae5107dfa011451ecaa404906fabc41e4"></a>
<a id="gga9e008daa9c0c1702aa3b4479e7a37ca4aa1dcc1e15aac59898c0a6c229593a76b"></a>
<a id="gga9e008daa9c0c1702aa3b4479e7a37ca4a072649a66bf1260ce37bd16fc7a9185d"></a>
<a id="gga9e008daa9c0c1702aa3b4479e7a37ca4a1ceb33afa661774e1077caced63bf263"></a>
<a id="gga9e008daa9c0c1702aa3b4479e7a37ca4a5370237bdbceb37a631425f472ddc322"></a>
<a id="ggaf34c59887e8a6da0560b6428733fe8d0a78af4f3bbf5adfc8ee6f9d459bb96e7d"></a>
<a id="ggaf34c59887e8a6da0560b6428733fe8d0a685a458547bda6af6c88626ee08c4110"></a>
<a id="ggaf34c59887e8a6da0560b6428733fe8d0a02394d7394f79a6e91a8f81070fdf82e"></a>
<a id="ggaf34c59887e8a6da0560b6428733fe8d0a43a7b210424a2aa2830a07676d3499b8"></a>
<a id="ggaf34c59887e8a6da0560b6428733fe8d0a18bb25e63782e9993a3853d929d58ee1"></a>
<a id="ggaf34c59887e8a6da0560b6428733fe8d0a1a5c531f590f14773b7ddc9b0ec8cae9"></a>
<a id="gga9f286cdeeee0e9df06e6b3df1e9ab643a5de14d0cc770615bd08c4e3d197bae90"></a>
<a id="gga9f286cdeeee0e9df06e6b3df1e9ab643a7ce16e0eab20cf432c8e93a7f6be8ca5"></a>
<a id="gga9f286cdeeee0e9df06e6b3df1e9ab643a35ae07887f3d55bcbd10d531f09c841d"></a>
<a id="gga9f286cdeeee0e9df06e6b3df1e9ab643aa5370917d0f46fe654ba42fbbd587ceb"></a>
<a id="gga9f286cdeeee0e9df06e6b3df1e9ab643aa23b552af8b16b1371f7a362089eaca7"></a>
<a id="gga9f286cdeeee0e9df06e6b3df1e9ab643a861f35bdbe322238bdad67568e5674f3"></a>
<a id="gga782a500f611320a6f3feed9897ab8e16a054f9b7f51323480106f11929425599f"></a>
<a id="gga782a500f611320a6f3feed9897ab8e16aa1931403e835ab2e18982dd0f2a67803"></a>
<a id="gga782a500f611320a6f3feed9897ab8e16aa059024bd3d90677ee00d4accd99f39c"></a>
<a id="gga782a500f611320a6f3feed9897ab8e16a678e1a8120f21f3707d4b9ea22bd8c47"></a>
<a id="ggaf50910d51c69e216ef6eb22b5c0f2d28aa5f4fea24a1b27736cfc36c470a3a008"></a>
<a id="ggaf50910d51c69e216ef6eb22b5c0f2d28aee2c022be115a4c865d5524795f2d039"></a>
<a id="ggaf50910d51c69e216ef6eb22b5c0f2d28ab504c3a24b36413ea2395bd579e5bba2"></a>
<a id="ggaf50910d51c69e216ef6eb22b5c0f2d28ad2b323c3c54409545458c08fc6660cf4"></a>
<a id="ggaf50910d51c69e216ef6eb22b5c0f2d28a9a691cb7b4a9cff799d848fc79cf40dd"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04da72b3c5a4d07ae3c73e9bb131c725d17f"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04da7aed472d8ed1b3fc84e89531134fc71c"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04dab986f2c0c54de93cfdf5a5334aafffb2"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04da7731f27f1af37ba740764e9875d28482"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04da3fe0da05e9c2493af3ea42a0c6cd4b17"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04daa73b01369a29b4ea7de2aadb71efe699"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04dae4f815603cdffeb82711b994be2209dc"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04da28e1b78a9bb927c4d38047e2aed57a15"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04dab1cbcd7ceb33fb13b7d70b0dc671849c"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04dae7f0fedfabe1748f9918befedbc45944"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04da2ac77dab1caf34f436075dab45cc4aea"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04dad85a40214189a9c036c95d88fb752a0c"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04da45f979b88a3d63c4f270d246c98f3b53"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04da2b34111edb7b0b1412de7d4485cbc164"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04da5ab31e2b89fef73d838ade33de5d770b"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04da144a6190783b1fbc5ccde1b9f0ec3581"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04dae87750d18c24ddcece72919e107da671"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04dabe494d770af056108d4679364a93acce"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04daad5f0f4d2818f986472f8cca57b37ea9"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04dac02f9fa05c0f35bb306fde66bc80ab21"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04dad355ee587eff65a2a2f80274fc6c5081"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04da3cc8b9dfadae103bdbb0fb79c523f553"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04dadf2778f065f696ad43ceca71aa6a8a80"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04dac3a263bfe1f80c38647d6aeab42b12c3"></a>
<a id="gga1ba4d7d919cb5c09469f8e8aa05bb04da2abd10e7d80703b3d849ad19d65af31f"></a>
<a id="ggacb3f437225ad1d6320ee424c39ebc82aa99a26684d34169d062150f61cb0ba889"></a>
<a id="ggacb3f437225ad1d6320ee424c39ebc82aa6b6bc126c5e2a97de33d6c83230ebb92"></a>
<a id="ggacb3f437225ad1d6320ee424c39ebc82aa3a3078691c778d1c7a30fe9400bc5f0f"></a>
<a id="gga731bbaa98dab7c88725fc64b66da62eba3c8bc2a6858dc2d0de02b3b681a854a0"></a>
<a id="gga731bbaa98dab7c88725fc64b66da62eba109f2588e566b9651b67dbbf9583813c"></a>
<a id="gga731bbaa98dab7c88725fc64b66da62ebaef4b4455b236d70fae6a0138050d0835"></a>
<a id="gga731bbaa98dab7c88725fc64b66da62eba1b910950b96ad0b47b0b235a2e8e45c8"></a>
<a id="gga731bbaa98dab7c88725fc64b66da62ebabc520467cdbaaf34d0c815e0d62bd097"></a>
<a id="gga731bbaa98dab7c88725fc64b66da62eba1b46b8b073ca599cb89d86b261fa4dd5"></a>
<a id="gga731bbaa98dab7c88725fc64b66da62eba4f4ec5a6d46734e8c5801e9e79535b70"></a>
<a id="gga731bbaa98dab7c88725fc64b66da62eba6c59258c52a5889e0b11aa0fb0f99bcb"></a>
<a id="gga731bbaa98dab7c88725fc64b66da62ebaf68334f70d91d587e906533ad544fef1"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_通用属性配置文件（Generic Attribute Profile，GATT）.md) · [返回大纲](大纲.md) · [下一章](P005_媒体控制客户端（Media Control Client，MCC）.md)
