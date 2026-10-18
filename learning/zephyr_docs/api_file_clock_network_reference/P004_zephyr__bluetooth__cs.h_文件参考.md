---
id: learning.zephyr-docs.api-file-clock-network-reference.page-4
title: zephyr__bluetooth__cs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_bluetooth\_\_cs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙信道探测（Bluetooth Channel Sounding）的处理。

<a id="details"></a>

```c
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/bluetooth/hci_types.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

蓝牙信道探测（Bluetooth Channel Sounding）的处理。

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

相关声明：[BT_LE_CS_CHANNEL_BIT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga95e2d24515e45096912440fe8a6bd3a0)。

获取信道探测（CS）信道映射中特定位的宏。

<a id="r_gadcd3351ef99d42e93c89d48f1c8ba668"></a>

```c
#define BT_LE_CS_CHANNEL_BIT_SET_VAL(chmap, bit, val)
```

相关声明：[BT_LE_CS_CHANNEL_BIT_SET_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gadcd3351ef99d42e93c89d48f1c8ba668)。

设置信道探测（CS）信道映射中特定位值的宏。

<a id="r_gaf278a44ad602ce7e365ac0d71bcc48b4"></a>

```c
#define BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_1 BIT(0)
```

相关声明：[BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf278a44ad602ce7e365ac0d71bcc48b4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga5ff36f6e97668a9d1b6ccd39492c68f7"></a>

```c
#define BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_2 BIT(1)
```

相关声明：[BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga5ff36f6e97668a9d1b6ccd39492c68f7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga66ea3f214385c395e5f14ca80a0655b0"></a>

```c
#define BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_3 BIT(2)
```

相关声明：[BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga66ea3f214385c395e5f14ca80a0655b0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_gaa2c1c3d5e451df7ec58b4c8d3dedcf9a"></a>

```c
#define BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_4 BIT(3)
```

相关声明：[BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaa2c1c3d5e451df7ec58b4c8d3dedcf9a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.3\_枚举（Enumerations）

<a id="r_ga9f286cdeeee0e9df06e6b3df1e9ab643"></a>

```c
enum bt_le_cs_sync_antenna_selection_opt { BT_LE_CS_ANTENNA_SELECTION_OPT_ONE = 0x01 , BT_LE_CS_ANTENNA_SELECTION_OPT_TWO = 0x02 , BT_LE_CS_ANTENNA_SELECTION_OPT_THREE = 0x03 , BT_LE_CS_ANTENNA_SELECTION_OPT_FOUR = 0x04 , BT_LE_CS_ANTENNA_SELECTION_OPT_REPETITIVE = 0xFE , BT_LE_CS_ANTENNA_SELECTION_OPT_NO_RECOMMENDATION = 0xFF }
```

相关声明：[bt_le_cs_sync_antenna_selection_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga9f286cdeeee0e9df06e6b3df1e9ab643)、[BT_LE_CS_ANTENNA_SELECTION_OPT_ONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9f286cdeeee0e9df06e6b3df1e9ab643a5de14d0cc770615bd08c4e3d197bae90)、[BT_LE_CS_ANTENNA_SELECTION_OPT_TWO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9f286cdeeee0e9df06e6b3df1e9ab643a7ce16e0eab20cf432c8e93a7f6be8ca5)、[BT_LE_CS_ANTENNA_SELECTION_OPT_THREE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9f286cdeeee0e9df06e6b3df1e9ab643a35ae07887f3d55bcbd10d531f09c841d)、[BT_LE_CS_ANTENNA_SELECTION_OPT_FOUR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9f286cdeeee0e9df06e6b3df1e9ab643aa5370917d0f46fe654ba42fbbd587ceb)、[BT_LE_CS_ANTENNA_SELECTION_OPT_REPETITIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9f286cdeeee0e9df06e6b3df1e9ab643aa23b552af8b16b1371f7a362089eaca7)、[BT_LE_CS_ANTENNA_SELECTION_OPT_NO_RECOMMENDATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9f286cdeeee0e9df06e6b3df1e9ab643a861f35bdbe322238bdad67568e5674f3)。

<a id="r_ga782a500f611320a6f3feed9897ab8e16"></a>

```c
enum bt_le_cs_test_cs_sync_antenna_selection { BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_ONE = 0x01 , BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_TWO = 0x02 , BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_THREE = 0x03 , BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_FOUR = 0x04 }
```

相关声明：[bt_le_cs_test_cs_sync_antenna_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga782a500f611320a6f3feed9897ab8e16)、[BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_ONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga782a500f611320a6f3feed9897ab8e16a054f9b7f51323480106f11929425599f)、[BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_TWO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga782a500f611320a6f3feed9897ab8e16aa1931403e835ab2e18982dd0f2a67803)、[BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_THREE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga782a500f611320a6f3feed9897ab8e16aa059024bd3d90677ee00d4accd99f39c)、[BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_FOUR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga782a500f611320a6f3feed9897ab8e16a678e1a8120f21f3707d4b9ea22bd8c47)。

信道探测测试（CS Test）的 CS_SYNC 天线标识符（Antenna Identifier）。

<a id="r_gaf34c59887e8a6da0560b6428733fe8d0"></a>

```c
enum bt_le_cs_snr_control { BT_LE_CS_SNR_CONTROL_18dB = 0x0 , BT_LE_CS_SNR_CONTROL_21dB = 0x1 , BT_LE_CS_SNR_CONTROL_24dB = 0x2 , BT_LE_CS_SNR_CONTROL_27dB = 0x3 , BT_LE_CS_SNR_CONTROL_30dB = 0x4 , BT_LE_CS_SNR_CONTROL_NOT_USED = 0xFF }
```

相关声明：[bt_le_cs_snr_control](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf34c59887e8a6da0560b6428733fe8d0)、[BT_LE_CS_SNR_CONTROL_18dB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf34c59887e8a6da0560b6428733fe8d0a78af4f3bbf5adfc8ee6f9d459bb96e7d)、[BT_LE_CS_SNR_CONTROL_21dB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf34c59887e8a6da0560b6428733fe8d0a685a458547bda6af6c88626ee08c4110)、[BT_LE_CS_SNR_CONTROL_24dB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf34c59887e8a6da0560b6428733fe8d0a02394d7394f79a6e91a8f81070fdf82e)、[BT_LE_CS_SNR_CONTROL_27dB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf34c59887e8a6da0560b6428733fe8d0a43a7b210424a2aa2830a07676d3499b8)、[BT_LE_CS_SNR_CONTROL_30dB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf34c59887e8a6da0560b6428733fe8d0a18bb25e63782e9993a3853d929d58ee1)、[BT_LE_CS_SNR_CONTROL_NOT_USED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf34c59887e8a6da0560b6428733fe8d0a1a5c531f590f14773b7ddc9b0ec8cae9)。

信道探测信噪比控制选项（CS SNR Control Options）。

<a id="r_gaf50910d51c69e216ef6eb22b5c0f2d28"></a>

```c
enum bt_le_cs_test_override_3_pm_tone_ext { BT_LE_CS_TEST_OVERRIDE_3_NO_TONE_EXT = 0x0 , BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_TONE_EXT_ONLY = 0x1 , BT_LE_CS_TEST_OVERRIDE_3_REFLECTOR_TONE_EXT_ONLY = 0x2 , BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_AND_REFLECTOR_TONE_EXT , BT_LE_CS_TEST_OVERRIDE_3_REPETITIVE_TONE_EXT = 0x4 }
```

相关声明：[bt_le_cs_test_override_3_pm_tone_ext](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf50910d51c69e216ef6eb22b5c0f2d28)、[BT_LE_CS_TEST_OVERRIDE_3_NO_TONE_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf50910d51c69e216ef6eb22b5c0f2d28aa5f4fea24a1b27736cfc36c470a3a008)、[BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_TONE_EXT_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf50910d51c69e216ef6eb22b5c0f2d28aee2c022be115a4c865d5524795f2d039)、[BT_LE_CS_TEST_OVERRIDE_3_REFLECTOR_TONE_EXT_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf50910d51c69e216ef6eb22b5c0f2d28ab504c3a24b36413ea2395bd579e5bba2)、[BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_AND_REFLECTOR_TONE_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf50910d51c69e216ef6eb22b5c0f2d28ad2b323c3c54409545458c08fc6660cf4)、[BT_LE_CS_TEST_OVERRIDE_3_REPETITIVE_TONE_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf50910d51c69e216ef6eb22b5c0f2d28a9a691cb7b4a9cff799d848fc79cf40dd)。

信道探测测试覆盖项 3（CS Test Override 3）：T_PM 音调扩展（Tone Extension）。

<a id="r_ga1ba4d7d919cb5c09469f8e8aa05bb04d"></a>

```c
enum bt_le_cs_test_override_4_tone_antenna_permutation { BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_00 = 0x0 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_01 = 0x1 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_02 = 0x2 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_03 = 0x3 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_04 = 0x4 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_05 = 0x5 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_06 = 0x6 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_07 = 0x7 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_08 = 0x8 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_09 = 0x9 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_10 = 0xA , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_11 = 0xB , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_12 = 0xC , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_13 = 0xD , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_14 = 0xE , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_15 = 0xF , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_16 = 0x10 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_17 = 0x11 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_18 = 0x12 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_19 = 0x13 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_20 = 0x14 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_21 = 0x15 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_22 = 0x16 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_23 = 0x17 , BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_LOOP }
```

相关声明：[bt_le_cs_test_override_4_tone_antenna_permutation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga1ba4d7d919cb5c09469f8e8aa05bb04d)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_00](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da72b3c5a4d07ae3c73e9bb131c725d17f)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_01](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da7aed472d8ed1b3fc84e89531134fc71c)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_02](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dab986f2c0c54de93cfdf5a5334aafffb2)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_03](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da7731f27f1af37ba740764e9875d28482)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_04](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da3fe0da05e9c2493af3ea42a0c6cd4b17)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_05](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04daa73b01369a29b4ea7de2aadb71efe699)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_06](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dae4f815603cdffeb82711b994be2209dc)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_07](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da28e1b78a9bb927c4d38047e2aed57a15)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_08](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dab1cbcd7ceb33fb13b7d70b0dc671849c)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_09](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dae7f0fedfabe1748f9918befedbc45944)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_10](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da2ac77dab1caf34f436075dab45cc4aea)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_11](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dad85a40214189a9c036c95d88fb752a0c)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_12](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da45f979b88a3d63c4f270d246c98f3b53)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_13](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da2b34111edb7b0b1412de7d4485cbc164)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_14](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da5ab31e2b89fef73d838ade33de5d770b)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_15](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da144a6190783b1fbc5ccde1b9f0ec3581)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dae87750d18c24ddcece72919e107da671)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_17](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dabe494d770af056108d4679364a93acce)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_18](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04daad5f0f4d2818f986472f8cca57b37ea9)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_19](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dac02f9fa05c0f35bb306fde66bc80ab21)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_20](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dad355ee587eff65a2a2f80274fc6c5081)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_21](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da3cc8b9dfadae103bdbb0fb79c523f553)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_22](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dadf2778f065f696ad43ceca71aa6a8a80)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_23](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dac3a263bfe1f80c38647d6aeab42b12c3)、[BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da2abd10e7d80703b3d849ad19d65af31f)。

信道探测测试覆盖项 4（CS Test Override 4）：音调天线排列（Tone Antenna Permutation）。

<a id="r_gacb3f437225ad1d6320ee424c39ebc82a"></a>

```c
enum bt_le_cs_test_override_7_ss_marker_value { BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_0011 = 0x0 , BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_1100 = 0x1 , BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_LOOP = 0x2 }
```

相关声明：[bt_le_cs_test_override_7_ss_marker_value](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gacb3f437225ad1d6320ee424c39ebc82a)、[BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_0011](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggacb3f437225ad1d6320ee424c39ebc82aa99a26684d34169d062150f61cb0ba889)、[BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_1100](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggacb3f437225ad1d6320ee424c39ebc82aa6b6bc126c5e2a97de33d6c83230ebb92)、[BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggacb3f437225ad1d6320ee424c39ebc82aa3a3078691c778d1c7a30fe9400bc5f0f)。

信道探测测试覆盖项 7（CS Test Override 7）：探测序列标记值（Sounding Sequence Marker Value）。

<a id="r_ga731bbaa98dab7c88725fc64b66da62eb"></a>

```c
enum bt_le_cs_test_override_8_cs_sync_payload_pattern { BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_PRBS9 = 0x00 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_11110000 = 0x01 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_10101010 = 0x02 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_PRBS15 = 0x03 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_11111111 = 0x04 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_00000000 = 0x05 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_00001111 = 0x06 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_01010101 = 0x07 , BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_USER = 0x80 }
```

相关声明：[bt_le_cs_test_override_8_cs_sync_payload_pattern](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga731bbaa98dab7c88725fc64b66da62eb)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_PRBS9](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62eba3c8bc2a6858dc2d0de02b3b681a854a0)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_11110000](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62eba109f2588e566b9651b67dbbf9583813c)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_10101010](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62ebaef4b4455b236d70fae6a0138050d0835)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_PRBS15](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62eba1b910950b96ad0b47b0b235a2e8e45c8)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_11111111](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62ebabc520467cdbaaf34d0c815e0d62bd097)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_00000000](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62eba1b46b8b073ca599cb89d86b261fa4dd5)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_00001111](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62eba4f4ec5a6d46734e8c5801e9e79535b70)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_01010101](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62eba6c59258c52a5889e0b11aa0fb0f99bcb)、[BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62ebaf68334f70d91d587e906533ad544fef1)。

信道探测测试覆盖项 8（CS Test Override 8）：CS_SYNC 载荷模式（Payload Pattern）。

<a id="r_ga22822b2dd21d64c8c64a66f2b5dee9b1"></a>

```c
enum bt_le_cs_create_config_context { BT_LE_CS_CREATE_CONFIG_CONTEXT_LOCAL_ONLY , BT_LE_CS_CREATE_CONFIG_CONTEXT_LOCAL_AND_REMOTE }
```

相关声明：[bt_le_cs_create_config_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga22822b2dd21d64c8c64a66f2b5dee9b1)、[BT_LE_CS_CREATE_CONFIG_CONTEXT_LOCAL_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga22822b2dd21d64c8c64a66f2b5dee9b1adb8a8af222fed7262bdb57bc4f18a706)、[BT_LE_CS_CREATE_CONFIG_CONTEXT_LOCAL_AND_REMOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga22822b2dd21d64c8c64a66f2b5dee9b1ae5107dfa011451ecaa404906fabc41e4)。

信道探测配置创建上下文（CS Config Creation Context）。

<a id="r_ga9e008daa9c0c1702aa3b4479e7a37ca4"></a>

```c
enum bt_le_cs_procedure_phy { BT_LE_CS_PROCEDURE_PHY_1M = 0x01 , BT_LE_CS_PROCEDURE_PHY_2M = 0x02 , BT_LE_CS_PROCEDURE_PHY_CODED_S8 = 0x03 , BT_LE_CS_PROCEDURE_PHY_CODED_S2 = 0x04 }
```

相关声明：[bt_le_cs_procedure_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga9e008daa9c0c1702aa3b4479e7a37ca4)、[BT_LE_CS_PROCEDURE_PHY_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9e008daa9c0c1702aa3b4479e7a37ca4aa1dcc1e15aac59898c0a6c229593a76b)、[BT_LE_CS_PROCEDURE_PHY_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9e008daa9c0c1702aa3b4479e7a37ca4a072649a66bf1260ce37bd16fc7a9185d)、[BT_LE_CS_PROCEDURE_PHY_CODED_S8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9e008daa9c0c1702aa3b4479e7a37ca4a1ceb33afa661774e1077caced63bf263)、[BT_LE_CS_PROCEDURE_PHY_CODED_S2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9e008daa9c0c1702aa3b4479e7a37ca4a5370237bdbceb37a631425f472ddc322)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_gaf99d82194bbcc471c3de2094b39a2201"></a>

```c
struct bt_le_cs_iq_sample bt_le_cs_parse_pct (const uint8_t pct[3])
```

相关声明：[bt_le_cs_iq_sample](../bluetooth_connection_model_reference/P095_bt_le_cs_iq_sample_结构体.md)、[bt_le_cs_parse_pct](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf99d82194bbcc471c3de2094b39a2201)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 HCI 格式的 PCT 中提取同相与正交分量（In-phase and Quadrature Terms）。

<a id="r_gaa979dc080cf277a2382b6ba77f8a1c09"></a>

```c
void bt_le_cs_set_valid_chmap_bits (uint8_t channel_map[10])
```

相关声明：[bt_le_cs_set_valid_chmap_bits](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaa979dc080cf277a2382b6ba77f8a1c09)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置所有有效信道映射位（Channel Map Bits）。

<a id="r_gadb3afd94cd11d035cfe34c6a63b37b19"></a>

```c
int bt_le_cs_read_remote_supported_capabilities (struct bt_conn *conn)
```

相关声明：[bt_le_cs_read_remote_supported_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gadb3afd94cd11d035cfe34c6a63b37b19)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取远端支持的能力（Remote Supported Capabilities）。

<a id="r_ga6ee9b8fa52b96dce41b1c879865fa938"></a>

```c
int bt_le_cs_set_default_settings (struct bt_conn *conn, const struct bt_le_cs_set_default_settings_param *params)
```

相关声明：[bt_le_cs_set_default_settings](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga6ee9b8fa52b96dce41b1c879865fa938)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_cs_set_default_settings_param](../bluetooth_connection_model_reference/P097_bt_le_cs_set_default_settings_param_结构体.md)。

设置信道探测（Channel Sounding，CS）的默认设置。

<a id="r_ga127034536a98743d359c749fe7c79dba"></a>

```c
int bt_le_cs_read_remote_fae_table (struct bt_conn *conn)
```

相关声明：[bt_le_cs_read_remote_fae_table](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga127034536a98743d359c749fe7c79dba)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

读取远端 FAE 表（Remote FAE Table）。

<a id="r_gaf03c4ed5c7e179ee3b374efa857188e2"></a>

```c
int bt_le_cs_test_cb_register (struct bt_le_cs_test_cb cs_test_cb)
```

相关声明：[bt_le_cs_test_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf03c4ed5c7e179ee3b374efa857188e2)、[bt_le_cs_test_cb](../bluetooth_connection_model_reference/P100_bt_le_cs_test_cb_结构体.md)。

注册信道探测测试模式（CS Test Mode）的回调。

<a id="r_gada91ff7c7a82620d77bf78781ebea356"></a>

```c
int bt_le_cs_start_test (const struct bt_le_cs_test_param *params)
```

相关声明：[bt_le_cs_start_test](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gada91ff7c7a82620d77bf78781ebea356)、[bt_le_cs_test_param](../bluetooth_connection_model_reference/P101_bt_le_cs_test_param_结构体.md)。

启动信道探测测试（CS Test）。

<a id="r_ga27bae87f9769a2d5802c57adfa201b23"></a>

```c
int bt_le_cs_create_config (struct bt_conn *conn, struct bt_le_cs_create_config_params *params, enum bt_le_cs_create_config_context context)
```

相关声明：[bt_le_cs_create_config](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga27bae87f9769a2d5802c57adfa201b23)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_cs_create_config_params](../bluetooth_connection_model_reference/P094_bt_le_cs_create_config_params_结构体.md)、[bt_le_cs_create_config_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga22822b2dd21d64c8c64a66f2b5dee9b1)。

创建信道探测配置（CS Configuration）。

<a id="r_ga2a27b80e72ff2bfe986b3cbe11f225f3"></a>

```c
int bt_le_cs_remove_config (struct bt_conn *conn, uint8_t config_id)
```

相关声明：[bt_le_cs_remove_config](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga2a27b80e72ff2bfe986b3cbe11f225f3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

移除信道探测配置（CS Configuration）。

<a id="r_ga4742baeb1eb46969233f787344cb5e11"></a>

```c
int bt_le_cs_stop_test (void)
```

相关声明：[bt_le_cs_stop_test](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga4742baeb1eb46969233f787344cb5e11)。

停止正在进行的信道探测测试（CS Test）。

<a id="r_gadcd85f3799f4219a01e84fc281ff1a31"></a>

```c
void bt_le_cs_step_data_parse (struct net_buf_simple *step_data_buf, bool(*func)(struct bt_le_cs_subevent_step *step, void *user_data), void *user_data)
```

相关声明：[bt_le_cs_step_data_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gadcd85f3799f4219a01e84fc281ff1a31)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_le_cs_subevent_step](../bluetooth_connection_model_reference/P099_bt_le_cs_subevent_step_结构体.md)。

解析信道探测子事件步骤数据（CS Subevent Step Data）。

<a id="r_ga346a46dc3321c5bab034904bf09aa4e3"></a>

```c
int bt_le_cs_security_enable (struct bt_conn *conn)
```

相关声明：[bt_le_cs_security_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga346a46dc3321c5bab034904bf09aa4e3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

启用信道探测安全（CS Security Enable）。

<a id="r_ga2b6f3c3795b5eeb424542c1858f84cbc"></a>

```c
int bt_le_cs_procedure_enable (struct bt_conn *conn, const struct bt_le_cs_procedure_enable_param *params)
```

相关声明：[bt_le_cs_procedure_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga2b6f3c3795b5eeb424542c1858f84cbc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_cs_procedure_enable_param](../bluetooth_connection_model_reference/P096_bt_le_cs_procedure_enable_param_结构体.md)。

启用信道探测过程（CS Procedure Enable）。

<a id="r_gad6e0fb9c7f92678598d9780b78710961"></a>

```c
int bt_le_cs_set_procedure_parameters (struct bt_conn *conn, const struct bt_le_cs_set_procedure_parameters_param *params)
```

相关声明：[bt_le_cs_set_procedure_parameters](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gad6e0fb9c7f92678598d9780b78710961)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_cs_set_procedure_parameters_param](../bluetooth_connection_model_reference/P098_bt_le_cs_set_procedure_parameters_param_结构体.md)。

设置信道探测过程参数（CS Procedure Parameters）。

<a id="r_gafcd6a882c0da413bfef5a56e53323389"></a>

```c
int bt_le_cs_set_channel_classification (uint8_t channel_classification[10])
```

相关声明：[bt_le_cs_set_channel_classification](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gafcd6a882c0da413bfef5a56e53323389)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置信道探测信道分类（CS Channel Classification）。

<a id="r_gaa49ff6e8340bd1753485deeec8036d1b"></a>

```c
int bt_le_cs_read_local_supported_capabilities (struct bt_conn_le_cs_capabilities *ret)
```

相关声明：[bt_le_cs_read_local_supported_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaa49ff6e8340bd1753485deeec8036d1b)、[bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)。

读取信道探测本地支持的能力（CS Local Supported Capabilities）。

<a id="r_ga62ae42071ed68bd1021d368304aa4d40"></a>

```c
int bt_le_cs_read_local_supported_capabilities_v2 (struct bt_conn_le_cs_capabilities *ret)
```

相关声明：[bt_le_cs_read_local_supported_capabilities_v2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga62ae42071ed68bd1021d368304aa4d40)、[bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)。

读取信道探测本地支持的能力，第 2 版（CS Local Supported Capabilities V2）。

<a id="r_ga9d4b5b21886f0dd89b4073acaaa787a1"></a>

```c
int bt_le_cs_write_cached_remote_supported_capabilities (struct bt_conn *conn, const struct bt_conn_le_cs_capabilities *params)
```

相关声明：[bt_le_cs_write_cached_remote_supported_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga9d4b5b21886f0dd89b4073acaaa787a1)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)。

写入缓存的信道探测远端支持能力（CS Cached Remote Supported Capabilities）。

<a id="r_ga19b1a269b7202a94c6bd5153498a09c7"></a>

```c
int bt_le_cs_write_cached_remote_supported_capabilities_v2 (struct bt_conn *conn, const struct bt_conn_le_cs_capabilities *params)
```

相关声明：[bt_le_cs_write_cached_remote_supported_capabilities_v2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga19b1a269b7202a94c6bd5153498a09c7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)。

写入缓存的信道探测远端支持能力，第 2 版（CS Cached Remote Supported Capabilities V2）。

<a id="r_ga63aa61d2bd3cf9ecb3ea9f1d02bb5b8c"></a>

```c
int bt_le_cs_write_cached_remote_fae_table (struct bt_conn *conn, int8_t remote_fae_table[72])
```

相关声明：[bt_le_cs_write_cached_remote_fae_table](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga63aa61d2bd3cf9ecb3ea9f1d02bb5b8c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

写入缓存的信道探测远端 FAE 表（CS Cached Remote FAE Table）。

<a id="r_gaa9126eca834eee8e088d01295d4cf94f"></a>

```c
int bt_le_cs_get_antenna_path (uint8_t n_ap, uint8_t antenna_path_permutation_index, uint8_t tone_index)
```

相关声明：[bt_le_cs_get_antenna_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaa9126eca834eee8e088d01295d4cf94f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在模式 2 或模式 3 的信道探测过程（CS Procedure）使用多条天线路径时，获取音调交换（Tone Exchange）所使用的天线路径（Antenna Path）。


## 4.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/bluetooth/hci_types.h](../api_source_hci_multifunction_reference/P001_hci_types.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_timing_sensor_reference/P003_cs.h_源码浏览.md)
- [bt_le_cs_set_default_settings_param](../bluetooth_connection_model_reference/P097_bt_le_cs_set_default_settings_param_结构体.md)
- [bt_le_cs_test_param](../bluetooth_connection_model_reference/P101_bt_le_cs_test_param_结构体.md)
- [bt_le_cs_create_config_params](../bluetooth_connection_model_reference/P094_bt_le_cs_create_config_params_结构体.md)
- [bt_le_cs_test_cb](../bluetooth_connection_model_reference/P100_bt_le_cs_test_cb_结构体.md)
- [bt_le_cs_subevent_step](../bluetooth_connection_model_reference/P099_bt_le_cs_subevent_step_结构体.md)
- [bt_le_cs_iq_sample](../bluetooth_connection_model_reference/P095_bt_le_cs_iq_sample_结构体.md)
- [bt_le_cs_procedure_enable_param](../bluetooth_connection_model_reference/P096_bt_le_cs_procedure_enable_param_结构体.md)
- [bt_le_cs_set_procedure_parameters_param](../bluetooth_connection_model_reference/P098_bt_le_cs_set_procedure_parameters_param_结构体.md)
- [BT_LE_CS_CHANNEL_BIT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga95e2d24515e45096912440fe8a6bd3a0)
- [BT_LE_CS_CHANNEL_BIT_SET_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gadcd3351ef99d42e93c89d48f1c8ba668)
- [BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf278a44ad602ce7e365ac0d71bcc48b4)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga5ff36f6e97668a9d1b6ccd39492c68f7)
- [BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga66ea3f214385c395e5f14ca80a0655b0)
- [BT_LE_CS_PROCEDURE_PREFERRED_PEER_ANTENNA_4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaa2c1c3d5e451df7ec58b4c8d3dedcf9a)
- [bt_le_cs_sync_antenna_selection_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga9f286cdeeee0e9df06e6b3df1e9ab643)
- [BT_LE_CS_ANTENNA_SELECTION_OPT_ONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9f286cdeeee0e9df06e6b3df1e9ab643a5de14d0cc770615bd08c4e3d197bae90)
- [BT_LE_CS_ANTENNA_SELECTION_OPT_TWO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9f286cdeeee0e9df06e6b3df1e9ab643a7ce16e0eab20cf432c8e93a7f6be8ca5)
- [BT_LE_CS_ANTENNA_SELECTION_OPT_THREE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9f286cdeeee0e9df06e6b3df1e9ab643a35ae07887f3d55bcbd10d531f09c841d)
- [BT_LE_CS_ANTENNA_SELECTION_OPT_FOUR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9f286cdeeee0e9df06e6b3df1e9ab643aa5370917d0f46fe654ba42fbbd587ceb)
- [BT_LE_CS_ANTENNA_SELECTION_OPT_REPETITIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9f286cdeeee0e9df06e6b3df1e9ab643aa23b552af8b16b1371f7a362089eaca7)
- [BT_LE_CS_ANTENNA_SELECTION_OPT_NO_RECOMMENDATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9f286cdeeee0e9df06e6b3df1e9ab643a861f35bdbe322238bdad67568e5674f3)
- [bt_le_cs_test_cs_sync_antenna_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga782a500f611320a6f3feed9897ab8e16)
- [BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_ONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga782a500f611320a6f3feed9897ab8e16a054f9b7f51323480106f11929425599f)
- [BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_TWO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga782a500f611320a6f3feed9897ab8e16aa1931403e835ab2e18982dd0f2a67803)
- [BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_THREE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga782a500f611320a6f3feed9897ab8e16aa059024bd3d90677ee00d4accd99f39c)
- [BT_LE_CS_TEST_CS_SYNC_ANTENNA_SELECTION_FOUR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga782a500f611320a6f3feed9897ab8e16a678e1a8120f21f3707d4b9ea22bd8c47)
- [bt_le_cs_snr_control](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf34c59887e8a6da0560b6428733fe8d0)
- [BT_LE_CS_SNR_CONTROL_18dB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf34c59887e8a6da0560b6428733fe8d0a78af4f3bbf5adfc8ee6f9d459bb96e7d)
- [BT_LE_CS_SNR_CONTROL_21dB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf34c59887e8a6da0560b6428733fe8d0a685a458547bda6af6c88626ee08c4110)
- [BT_LE_CS_SNR_CONTROL_24dB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf34c59887e8a6da0560b6428733fe8d0a02394d7394f79a6e91a8f81070fdf82e)
- [BT_LE_CS_SNR_CONTROL_27dB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf34c59887e8a6da0560b6428733fe8d0a43a7b210424a2aa2830a07676d3499b8)
- [BT_LE_CS_SNR_CONTROL_30dB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf34c59887e8a6da0560b6428733fe8d0a18bb25e63782e9993a3853d929d58ee1)
- [BT_LE_CS_SNR_CONTROL_NOT_USED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf34c59887e8a6da0560b6428733fe8d0a1a5c531f590f14773b7ddc9b0ec8cae9)
- [bt_le_cs_test_override_3_pm_tone_ext](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf50910d51c69e216ef6eb22b5c0f2d28)
- [BT_LE_CS_TEST_OVERRIDE_3_NO_TONE_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf50910d51c69e216ef6eb22b5c0f2d28aa5f4fea24a1b27736cfc36c470a3a008)
- [BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_TONE_EXT_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf50910d51c69e216ef6eb22b5c0f2d28aee2c022be115a4c865d5524795f2d039)
- [BT_LE_CS_TEST_OVERRIDE_3_REFLECTOR_TONE_EXT_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf50910d51c69e216ef6eb22b5c0f2d28ab504c3a24b36413ea2395bd579e5bba2)
- [BT_LE_CS_TEST_OVERRIDE_3_INITIATOR_AND_REFLECTOR_TONE_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf50910d51c69e216ef6eb22b5c0f2d28ad2b323c3c54409545458c08fc6660cf4)
- [BT_LE_CS_TEST_OVERRIDE_3_REPETITIVE_TONE_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggaf50910d51c69e216ef6eb22b5c0f2d28a9a691cb7b4a9cff799d848fc79cf40dd)
- [bt_le_cs_test_override_4_tone_antenna_permutation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga1ba4d7d919cb5c09469f8e8aa05bb04d)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_00](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da72b3c5a4d07ae3c73e9bb131c725d17f)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_01](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da7aed472d8ed1b3fc84e89531134fc71c)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_02](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dab986f2c0c54de93cfdf5a5334aafffb2)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_03](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da7731f27f1af37ba740764e9875d28482)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_04](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da3fe0da05e9c2493af3ea42a0c6cd4b17)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_05](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04daa73b01369a29b4ea7de2aadb71efe699)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_06](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dae4f815603cdffeb82711b994be2209dc)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_07](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da28e1b78a9bb927c4d38047e2aed57a15)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_08](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dab1cbcd7ceb33fb13b7d70b0dc671849c)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_09](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dae7f0fedfabe1748f9918befedbc45944)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_10](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da2ac77dab1caf34f436075dab45cc4aea)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_11](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dad85a40214189a9c036c95d88fb752a0c)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_12](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da45f979b88a3d63c4f270d246c98f3b53)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_13](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da2b34111edb7b0b1412de7d4485cbc164)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_14](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da5ab31e2b89fef73d838ade33de5d770b)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_15](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da144a6190783b1fbc5ccde1b9f0ec3581)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dae87750d18c24ddcece72919e107da671)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_17](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dabe494d770af056108d4679364a93acce)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_18](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04daad5f0f4d2818f986472f8cca57b37ea9)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_19](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dac02f9fa05c0f35bb306fde66bc80ab21)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_20](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dad355ee587eff65a2a2f80274fc6c5081)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_21](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da3cc8b9dfadae103bdbb0fb79c523f553)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_22](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dadf2778f065f696ad43ceca71aa6a8a80)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_23](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04dac3a263bfe1f80c38647d6aeab42b12c3)
- [BT_LE_CS_TEST_OVERRIDE_4_ANTENNA_PERMUTATION_INDEX_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga1ba4d7d919cb5c09469f8e8aa05bb04da2abd10e7d80703b3d849ad19d65af31f)
- [bt_le_cs_test_override_7_ss_marker_value](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gacb3f437225ad1d6320ee424c39ebc82a)
- [BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_0011](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggacb3f437225ad1d6320ee424c39ebc82aa99a26684d34169d062150f61cb0ba889)
- [BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_1100](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggacb3f437225ad1d6320ee424c39ebc82aa6b6bc126c5e2a97de33d6c83230ebb92)
- [BT_LE_CS_TEST_OVERRIDE_7_SS_MARKER_VAL_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ggacb3f437225ad1d6320ee424c39ebc82aa3a3078691c778d1c7a30fe9400bc5f0f)
- [bt_le_cs_test_override_8_cs_sync_payload_pattern](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga731bbaa98dab7c88725fc64b66da62eb)
- [BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_PRBS9](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62eba3c8bc2a6858dc2d0de02b3b681a854a0)
- [BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_11110000](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62eba109f2588e566b9651b67dbbf9583813c)
- [BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_10101010](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62ebaef4b4455b236d70fae6a0138050d0835)
- [BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_PRBS15](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62eba1b910950b96ad0b47b0b235a2e8e45c8)
- [BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_11111111](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62ebabc520467cdbaaf34d0c815e0d62bd097)
- [BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_00000000](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62eba1b46b8b073ca599cb89d86b261fa4dd5)
- [BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_00001111](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62eba4f4ec5a6d46734e8c5801e9e79535b70)
- [BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_01010101](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62eba6c59258c52a5889e0b11aa0fb0f99bcb)
- [BT_LE_CS_TEST_OVERRIDE_8_PAYLOAD_PATTERN_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga731bbaa98dab7c88725fc64b66da62ebaf68334f70d91d587e906533ad544fef1)
- [bt_le_cs_create_config_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga22822b2dd21d64c8c64a66f2b5dee9b1)
- [BT_LE_CS_CREATE_CONFIG_CONTEXT_LOCAL_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga22822b2dd21d64c8c64a66f2b5dee9b1adb8a8af222fed7262bdb57bc4f18a706)
- [BT_LE_CS_CREATE_CONFIG_CONTEXT_LOCAL_AND_REMOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga22822b2dd21d64c8c64a66f2b5dee9b1ae5107dfa011451ecaa404906fabc41e4)
- [bt_le_cs_procedure_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga9e008daa9c0c1702aa3b4479e7a37ca4)
- [BT_LE_CS_PROCEDURE_PHY_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9e008daa9c0c1702aa3b4479e7a37ca4aa1dcc1e15aac59898c0a6c229593a76b)
- [BT_LE_CS_PROCEDURE_PHY_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9e008daa9c0c1702aa3b4479e7a37ca4a072649a66bf1260ce37bd16fc7a9185d)
- [BT_LE_CS_PROCEDURE_PHY_CODED_S8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9e008daa9c0c1702aa3b4479e7a37ca4a1ceb33afa661774e1077caced63bf263)
- [BT_LE_CS_PROCEDURE_PHY_CODED_S2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gga9e008daa9c0c1702aa3b4479e7a37ca4a5370237bdbceb37a631425f472ddc322)
- [bt_le_cs_parse_pct](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf99d82194bbcc471c3de2094b39a2201)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_le_cs_set_valid_chmap_bits](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaa979dc080cf277a2382b6ba77f8a1c09)
- [bt_le_cs_read_remote_supported_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gadb3afd94cd11d035cfe34c6a63b37b19)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_le_cs_set_default_settings](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga6ee9b8fa52b96dce41b1c879865fa938)
- [bt_le_cs_read_remote_fae_table](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga127034536a98743d359c749fe7c79dba)
- [bt_le_cs_test_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaf03c4ed5c7e179ee3b374efa857188e2)
- [bt_le_cs_start_test](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gada91ff7c7a82620d77bf78781ebea356)
- [bt_le_cs_create_config](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga27bae87f9769a2d5802c57adfa201b23)
- [bt_le_cs_remove_config](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga2a27b80e72ff2bfe986b3cbe11f225f3)
- [bt_le_cs_stop_test](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga4742baeb1eb46969233f787344cb5e11)
- [bt_le_cs_step_data_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gadcd85f3799f4219a01e84fc281ff1a31)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_le_cs_security_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga346a46dc3321c5bab034904bf09aa4e3)
- [bt_le_cs_procedure_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga2b6f3c3795b5eeb424542c1858f84cbc)
- [bt_le_cs_set_procedure_parameters](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gad6e0fb9c7f92678598d9780b78710961)
- [bt_le_cs_set_channel_classification](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gafcd6a882c0da413bfef5a56e53323389)
- [bt_le_cs_read_local_supported_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaa49ff6e8340bd1753485deeec8036d1b)
- [bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)
- [bt_le_cs_read_local_supported_capabilities_v2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga62ae42071ed68bd1021d368304aa4d40)
- [bt_le_cs_write_cached_remote_supported_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga9d4b5b21886f0dd89b4073acaaa787a1)
- [bt_le_cs_write_cached_remote_supported_capabilities_v2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga19b1a269b7202a94c6bd5153498a09c7)
- [bt_le_cs_write_cached_remote_fae_table](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga63aa61d2bd3cf9ecb3ea9f1d02bb5b8c)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [bt_le_cs_get_antenna_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#gaa9126eca834eee8e088d01295d4cf94f)

<a id="header-details"></a>

---

[上一章](P003_zephyr__dt-bindings__clock__ch32v10x-clocks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__gpio__digilent-pmod.h_文件参考.md)
