---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-6
title: 免提配置文件——音频网关（Hands Free Profile - Audio Gateway，HFP-AG）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_免提配置文件——音频网关（Hands Free Profile - Audio Gateway，HFP-AG）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

免提配置文件——音频网关（Hands Free Profile - Audio Gateway，HFP-AG）

<a id="details"></a>

免提配置文件——音频网关（Hands Free Profile - Audio Gateway，HFP-AG）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_bt_5Fhfp_5Fag_5Fongoing_5Fcall"></a>

```c
struct bt_hfp_ag_ongoing_call
```

相关声明：[bt_hfp_ag_ongoing_call](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md)。

正在进行的呼叫（Ongoing Call）。

<a id="r_bt_5Fhfp_5Fag_5Fcb"></a>

```c
struct bt_hfp_ag_cb
```

相关声明：[bt_hfp_ag_cb](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md)。

免提配置文件音频网关（HFP AG）的应用回调。

<a id="r_bt_5Fhfp_5Fag"></a>

```c
struct bt_hfp_ag
```

相关声明：[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)。

免提配置文件音频网关（HFP AG）结构。

<a id="r_bt_5Fhfp_5Fag_5Fcall"></a>

```c
struct bt_hfp_ag_call
```

相关声明：[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

免提配置文件音频网关（HFP AG）的呼叫结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_gada6266f825879f39147c5d889e4192c9"></a>

```c
#define BT_HFP_AG_CODEC_CVSD 0x01
```

相关声明：[BT_HFP_AG_CODEC_CVSD](#gada6266f825879f39147c5d889e4192c9)。

<a id="r_ga3591201c7310288ea2e01e2f77a0c0d3"></a>

```c
#define BT_HFP_AG_CODEC_MSBC 0x02
```

相关声明：[BT_HFP_AG_CODEC_MSBC](#ga3591201c7310288ea2e01e2f77a0c0d3)。

<a id="r_ga8a833c4b11dc9e8fd08a73a2af418d83"></a>

```c
#define BT_HFP_AG_CODEC_LC3_SWB 0x03
```

相关声明：[BT_HFP_AG_CODEC_LC3_SWB](#ga8a833c4b11dc9e8fd08a73a2af418d83)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_ga8e9b485f7ea0b9e16d96f578cdc587c3"></a>

```c
typedef int(* bt_hfp_ag_query_subscriber_func_t) (struct bt_hfp_ag *ag, char *number, uint8_t type, uint8_t service)
```

相关声明：[bt_hfp_ag_query_subscriber_func_t](#ga8e9b485f7ea0b9e16d96f578cdc587c3)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

查询用户号码（Subscriber Number）的回调函数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.4\_枚举（Enumerations）

<a id="r_ga37640efdcc737bfa0390df889a62f810"></a>

```c
enum bt_hfp_ag_indicator { BT_HFP_AG_SERVICE_IND = 0 , BT_HFP_AG_CALL_IND = 1 , BT_HFP_AG_CALL_SETUP_IND = 2 , BT_HFP_AG_CALL_HELD_IND = 3 , BT_HFP_AG_SIGNAL_IND = 4 , BT_HFP_AG_ROAM_IND = 5 , BT_HFP_AG_BATTERY_IND = 6 , BT_HFP_AG_IND_MAX }
```

相关声明：[bt_hfp_ag_indicator](#ga37640efdcc737bfa0390df889a62f810)、[BT_HFP_AG_SERVICE_IND](#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234)、[BT_HFP_AG_CALL_IND](#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d)、[BT_HFP_AG_CALL_SETUP_IND](#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5)、[BT_HFP_AG_CALL_HELD_IND](#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b)、[BT_HFP_AG_SIGNAL_IND](#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493)、[BT_HFP_AG_ROAM_IND](#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863)、[BT_HFP_AG_BATTERY_IND](#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609)、[BT_HFP_AG_IND_MAX](#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36)。

<a id="r_ga030c97d703fb45a2055653c51cb1b403"></a>

```c
enum hfp_ag_hf_indicators { HFP_AG_ENHANCED_SAFETY_IND = 1 , HFP_AG_BATTERY_LEVEL_IND = 2 }
```

相关声明：[hfp_ag_hf_indicators](#ga030c97d703fb45a2055653c51cb1b403)、[HFP_AG_ENHANCED_SAFETY_IND](#gga030c97d703fb45a2055653c51cb1b403afd31a626b024de7e6e68ade0d776b14f)、[HFP_AG_BATTERY_LEVEL_IND](#gga030c97d703fb45a2055653c51cb1b403a9719aca10a790eb9f62d498bc4bec9d1)。

<a id="r_gad2220b4a470cb3d537cf09492847568e"></a>

```c
enum bt_hfp_ag_call_status { BT_HFP_AG_CALL_STATUS_ACTIVE = 0 , BT_HFP_AG_CALL_STATUS_HELD = 1 , BT_HFP_AG_CALL_STATUS_DIALING = 2 , BT_HFP_AG_CALL_STATUS_ALERTING = 3 , BT_HFP_AG_CALL_STATUS_INCOMING = 4 , BT_HFP_AG_CALL_STATUS_WAITING = 5 , BT_HFP_AG_CALL_STATUS_INCOMING_HELD = 6 }
```

相关声明：[bt_hfp_ag_call_status](#gad2220b4a470cb3d537cf09492847568e)、[BT_HFP_AG_CALL_STATUS_ACTIVE](#ggad2220b4a470cb3d537cf09492847568ea4c387d6e8628fc40e9969c95ff9ea658)、[BT_HFP_AG_CALL_STATUS_HELD](#ggad2220b4a470cb3d537cf09492847568eac2acf82710d562fd2852139f7e8146e2)、[BT_HFP_AG_CALL_STATUS_DIALING](#ggad2220b4a470cb3d537cf09492847568ea09545d4deadcc910c42b615d21f91963)、[BT_HFP_AG_CALL_STATUS_ALERTING](#ggad2220b4a470cb3d537cf09492847568ea423017739b17f57e0a8adb7d6b9cffae)、[BT_HFP_AG_CALL_STATUS_INCOMING](#ggad2220b4a470cb3d537cf09492847568ea4faad88cf6cb9926f78e7da7065713f8)、[BT_HFP_AG_CALL_STATUS_WAITING](#ggad2220b4a470cb3d537cf09492847568ea5b1a40f632b8d9ce3b02ffacb1a07fb2)、[BT_HFP_AG_CALL_STATUS_INCOMING_HELD](#ggad2220b4a470cb3d537cf09492847568ea2e155da5b54cb32a400de1d44ebc2542)。

<a id="r_ga019020ee2ed73c218f7dadf8371bf9a6"></a>

```c
enum bt_hfp_ag_call_dir { BT_HFP_AG_CALL_DIR_OUTGOING = 0 , BT_HFP_AG_CALL_DIR_INCOMING = 1 }
```

相关声明：[bt_hfp_ag_call_dir](#ga019020ee2ed73c218f7dadf8371bf9a6)、[BT_HFP_AG_CALL_DIR_OUTGOING](#gga019020ee2ed73c218f7dadf8371bf9a6a83ea29c4261577438e481e2b9f0c7d37)、[BT_HFP_AG_CALL_DIR_INCOMING](#gga019020ee2ed73c218f7dadf8371bf9a6a08a4f52a9ca4fdcaa1c6575b1b378b55)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.5\_函数（Functions）

<a id="r_ga379ec1c540195549fc59417d8d1ce7e5"></a>

```c
int bt_hfp_ag_register (struct bt_hfp_ag_cb *cb)
```

相关声明：[bt_hfp_ag_register](#ga379ec1c540195549fc59417d8d1ce7e5)、[bt_hfp_ag_cb](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md)。

注册免提规范音频网关（HFP AG）配置文件（Profile）。

<a id="r_ga5b602810558268396f0cb64adcb0d014"></a>

```c
int bt_hfp_ag_connect (struct bt_conn *conn, struct bt_hfp_ag **ag, uint8_t channel)
```

相关声明：[bt_hfp_ag_connect](#ga5b602810558268396f0cb64adcb0d014)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

创建免提规范音频网关会话（HFP AG Session）。

<a id="r_gadf0b4aef701cf0986ea9599ad79d451a"></a>

```c
int bt_hfp_ag_disconnect (struct bt_hfp_ag *ag)
```

相关声明：[bt_hfp_ag_disconnect](#gadf0b4aef701cf0986ea9599ad79d451a)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)。

断开免提规范音频网关会话（HFP AG Session）。

<a id="r_ga443cd2928686f222d61f06c7477ea793"></a>

```c
int bt_hfp_ag_remote_incoming (struct bt_hfp_ag *ag, const char *number)
```

相关声明：[bt_hfp_ag_remote_incoming](#ga443cd2928686f222d61f06c7477ea793)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)。

向免提规范单元（HFP Unit）通知来电（Incoming Call）。

<a id="r_gab288d6e6b45a24b706328da58ca43a3b"></a>

```c
int bt_hfp_ag_hold_incoming (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_hold_incoming](#gab288d6e6b45a24b706328da58ca43a3b)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

保持来电（Put Incoming Call on Hold）。

<a id="r_ga195daffc37f1a3f210ba52dae1a9c4c2"></a>

```c
int bt_hfp_ag_reject (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_reject](#ga195daffc37f1a3f210ba52dae1a9c4c2)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

拒接来电（Reject Incoming Call）。

<a id="r_ga351e1b78b8c19c3971554fabb331e5c6"></a>

```c
int bt_hfp_ag_accept (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_accept](#ga351e1b78b8c19c3971554fabb331e5c6)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

接听来电（Accept Incoming Call）。

<a id="r_ga2f2e85a6076930ed87bc0727c75209a9"></a>

```c
int bt_hfp_ag_terminate (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_terminate](#ga2f2e85a6076930ed87bc0727c75209a9)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

终止活动／保持的通话（Active/Held Call）。

<a id="r_ga405fcf8e03bac39bd5b0e7bf2766045f"></a>

```c
int bt_hfp_ag_retrieve (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_retrieve](#ga405fcf8e03bac39bd5b0e7bf2766045f)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

恢复保持的通话（Retrieve Held Call）。

<a id="r_ga4bbcec3ed5394e965aa7404dc968b94d"></a>

```c
int bt_hfp_ag_hold (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_hold](#ga4bbcec3ed5394e965aa7404dc968b94d)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

保持活动通话（Hold Active Call）。

<a id="r_ga580328104cf990c6f9e0a64642c16ebd"></a>

```c
int bt_hfp_ag_outgoing (struct bt_hfp_ag *ag, const char *number)
```

相关声明：[bt_hfp_ag_outgoing](#ga580328104cf990c6f9e0a64642c16ebd)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)。

拨打电话（Dial a Call）。

<a id="r_ga0a12a56baa25e2aea101a387fcccb88e"></a>

```c
int bt_hfp_ag_remote_ringing (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_remote_ringing](#ga0a12a56baa25e2aea101a387fcccb88e)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

向 HFP 单元通知远端开始振铃（Ringing）。

<a id="r_gacb1b361e6b0a441102f7ccd641eb3e6b"></a>

```c
int bt_hfp_ag_remote_reject (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_remote_reject](#gacb1b361e6b0a441102f7ccd641eb3e6b)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

向 HFP 单元通知远端拒接通话。

<a id="r_ga018d8ed8912f9dcef8c5fa37ac2bd889"></a>

```c
int bt_hfp_ag_remote_accept (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_remote_accept](#ga018d8ed8912f9dcef8c5fa37ac2bd889)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

向 HFP 单元通知远端接听通话。

<a id="r_ga525085c7c75e412ca43ba8b23cbc0c3d"></a>

```c
int bt_hfp_ag_remote_terminate (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_remote_terminate](#ga525085c7c75e412ca43ba8b23cbc0c3d)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

向 HFP 单元通知远端终止活动／保持的通话。

<a id="r_ga5e249248a52d7c95c9d3f3f852bf2314"></a>

```c
int bt_hfp_ag_explicit_call_transfer (struct bt_hfp_ag *ag)
```

相关声明：[bt_hfp_ag_explicit_call_transfer](#ga5e249248a52d7c95c9d3f3f852bf2314)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)。

显式呼叫转移（Explicit Call Transfer）

<a id="r_ga53778bd332c95fa4357d254f5ef125a2"></a>

```c
int bt_hfp_ag_vgm (struct bt_hfp_ag *ag, uint8_t vgm)
```

相关声明：[bt_hfp_ag_vgm](#ga53778bd332c95fa4357d254f5ef125a2)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置免提单元麦克风增益（HF Microphone Gain）。

<a id="r_gabdad8c764c91e133598584d741ed9d4b"></a>

```c
int bt_hfp_ag_vgs (struct bt_hfp_ag *ag, uint8_t vgs)
```

相关声明：[bt_hfp_ag_vgs](#gabdad8c764c91e133598584d741ed9d4b)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置免提单元扬声器增益（HF Speaker Gain）。

<a id="r_gaaf066dce38c028254b6c1880bcebaa13"></a>

```c
int bt_hfp_ag_set_operator (struct bt_hfp_ag *ag, uint8_t mode, char *name)
```

相关声明：[bt_hfp_ag_set_operator](#gaaf066dce38c028254b6c1880bcebaa13)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置当前网络运营商（Network Operator）。

<a id="r_ga542a1754a16e32a9b2651f1230aa7066"></a>

```c
int bt_hfp_ag_audio_connect (struct bt_hfp_ag *ag, uint8_t id)
```

相关声明：[bt_hfp_ag_audio_connect](#ga542a1754a16e32a9b2651f1230aa7066)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

创建音频连接（Audio Connection）。

<a id="r_ga881ea4d3cc732fb5d804df203dde7746"></a>

```c
int bt_hfp_ag_inband_ringtone (struct bt_hfp_ag *ag, bool inband)
```

相关声明：[bt_hfp_ag_inband_ringtone](#ga881ea4d3cc732fb5d804df203dde7746)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置带内铃音（In-Band Ring Tone）。

<a id="r_ga28682fc5d8cfee9c0adece68bcb94c3f"></a>

```c
int bt_hfp_ag_voice_recognition (struct bt_hfp_ag *ag, bool activate)
```

相关声明：[bt_hfp_ag_voice_recognition](#ga28682fc5d8cfee9c0adece68bcb94c3f)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用语音识别功能（Voice Recognition）。

<a id="r_ga3668f3997afe9ab678f9eb2e6faf324d"></a>

```c
int bt_hfp_ag_vre_state (struct bt_hfp_ag *ag, uint8_t state)
```

相关声明：[bt_hfp_ag_vre_state](#ga3668f3997afe9ab678f9eb2e6faf324d)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置语音识别引擎状态（Voice Recognition Engine State）。

<a id="r_ga4e71364283448c7c5d3306c111aa167d"></a>

```c
int bt_hfp_ag_vre_textual_representation (struct bt_hfp_ag *ag, uint8_t state, const char *id, uint8_t type, uint8_t operation, const char *text)
```

相关声明：[bt_hfp_ag_vre_textual_representation](#ga4e71364283448c7c5d3306c111aa167d)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置语音识别引擎状态及文本表示（Textual Representation）。

<a id="r_ga20ef1240e0ff72d914405b259cc3164f"></a>

```c
int bt_hfp_ag_signal_strength (struct bt_hfp_ag *ag, uint8_t strength)
```

相关声明：[bt_hfp_ag_signal_strength](#ga20ef1240e0ff72d914405b259cc3164f)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置信号强度（Signal Strength）。

<a id="r_ga0f8b2e463aefbf74b26ac4f27033486c"></a>

```c
int bt_hfp_ag_roaming_status (struct bt_hfp_ag *ag, uint8_t status)
```

相关声明：[bt_hfp_ag_roaming_status](#ga0f8b2e463aefbf74b26ac4f27033486c)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置漫游状态（Roaming Status）。

<a id="r_ga4da632e9775051df6a5b5010fd3806df"></a>

```c
int bt_hfp_ag_battery_level (struct bt_hfp_ag *ag, uint8_t level)
```

相关声明：[bt_hfp_ag_battery_level](#ga4da632e9775051df6a5b5010fd3806df)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置电池电量（Battery Level）。

<a id="r_gaf838e54046c380931f23a59919ccfa5b"></a>

```c
int bt_hfp_ag_service_availability (struct bt_hfp_ag *ag, bool available)
```

相关声明：[bt_hfp_ag_service_availability](#gaf838e54046c380931f23a59919ccfa5b)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置服务可用性（Service Availability）。

<a id="r_gaacc2df6144e1a33b13635855fe74f1f1"></a>

```c
int bt_hfp_ag_hf_indicator (struct bt_hfp_ag *ag, enum hfp_ag_hf_indicators indicator, bool enable)
```

相关声明：[bt_hfp_ag_hf_indicator](#gaacc2df6144e1a33b13635855fe74f1f1)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[hfp_ag_hf_indicators](#ga030c97d703fb45a2055653c51cb1b403)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

激活／停用免提单元指示器（HF Indicator）。

<a id="r_ga5614bf3f1de11959a0364f458523e06e"></a>

```c
int bt_hfp_ag_ongoing_calls (struct bt_hfp_ag *ag, struct bt_hfp_ag_ongoing_call *calls, size_t count)
```

相关声明：[bt_hfp_ag_ongoing_calls](#ga5614bf3f1de11959a0364f458523e06e)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[bt_hfp_ag_ongoing_call](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md)。

设置正在进行的通话（Ongoing Calls）。

## 6.6\_详细说明（Detailed Documentation）

<a id="gada6266f825879f39147c5d889e4192c9"></a>

### `BT_HFP_AG_CODEC_CVSD`

```c
#define BT_HFP_AG_CODEC_CVSD 0x01
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

<a id="ga8a833c4b11dc9e8fd08a73a2af418d83"></a>

### `BT_HFP_AG_CODEC_LC3_SWB`

```c
#define BT_HFP_AG_CODEC_LC3_SWB 0x03
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

<a id="ga3591201c7310288ea2e01e2f77a0c0d3"></a>

### `BT_HFP_AG_CODEC_MSBC`

```c
#define BT_HFP_AG_CODEC_MSBC 0x02
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

<a id="ga8e9b485f7ea0b9e16d96f578cdc587c3"></a>

### `bt_hfp_ag_query_subscriber_func_t`

```c
typedef int(* bt_hfp_ag_query_subscriber_func_t) (struct bt_hfp_ag *ag, char *number, uint8_t type, uint8_t service)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

查询用户号码（Subscriber Number）的回调函数。

音频网关（AG）要发送用户号码信息（Subscriber Number Information）时，所有信息通过回调传递，并由此函数发送。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `number` | 用户号码（Subscriber Number）。 |
| `type` | 用户号码类型（Type of Subscriber Number）指定所提供电话号码的格式，可取以下值：128～143：号码可以是国内或国际格式，可能包含前缀及／或转义数字，无需改变号码呈现方式。144～159：号码为包含国家代码前缀的国际号码；若号码中没有加号（+），AG 应按需添加。160～175：国内号码，不包含前缀或转义数字。 |
| `service` | 用户号码服务（Service of Subscriber Number）指出此号码对应的服务，必须为 4（语音 Voice）或 5（传真 Fax）。 |

**返回（Returns）**：返回值（Returns）：应继续处理下一个用户号码信息时返回 0，返回负值则停止。

<a id="ga019020ee2ed73c218f7dadf8371bf9a6"></a>

### `bt_hfp_ag_call_dir`

```c
enum bt_hfp_ag_call_dir
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_HFP_AG_CALL_DIR_OUTGOING` |  |
| `BT_HFP_AG_CALL_DIR_INCOMING` |  |

<a id="gad2220b4a470cb3d537cf09492847568e"></a>

### `bt_hfp_ag_call_status`

```c
enum bt_hfp_ag_call_status
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_HFP_AG_CALL_STATUS_ACTIVE` |  |
| `BT_HFP_AG_CALL_STATUS_HELD` |  |
| `BT_HFP_AG_CALL_STATUS_DIALING` |  |
| `BT_HFP_AG_CALL_STATUS_ALERTING` |  |
| `BT_HFP_AG_CALL_STATUS_INCOMING` |  |
| `BT_HFP_AG_CALL_STATUS_WAITING` |  |
| `BT_HFP_AG_CALL_STATUS_INCOMING_HELD` |  |

<a id="ga37640efdcc737bfa0390df889a62f810"></a>

### `bt_hfp_ag_indicator`

```c
enum bt_hfp_ag_indicator
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_HFP_AG_SERVICE_IND` |  |
| `BT_HFP_AG_CALL_IND` |  |
| `BT_HFP_AG_CALL_SETUP_IND` |  |
| `BT_HFP_AG_CALL_HELD_IND` |  |
| `BT_HFP_AG_SIGNAL_IND` |  |
| `BT_HFP_AG_ROAM_IND` |  |
| `BT_HFP_AG_BATTERY_IND` |  |
| `BT_HFP_AG_IND_MAX` |  |

<a id="ga030c97d703fb45a2055653c51cb1b403"></a>

### `hfp_ag_hf_indicators`

```c
enum hfp_ag_hf_indicators
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HFP_AG_ENHANCED_SAFETY_IND` |  |
| `HFP_AG_BATTERY_LEVEL_IND` |  |

<a id="ga351e1b78b8c19c3971554fabb331e5c6"></a>

### `bt_hfp_ag_accept()`

```c
int bt_hfp_ag_accept ( struct bt_hfp_ag_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

接听来电（Accept Incoming Call）。

接听来电（Accept Incoming Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga542a1754a16e32a9b2651f1230aa7066"></a>

### `bt_hfp_ag_audio_connect()`

```c
int bt_hfp_ag_audio_connect ( struct bt_hfp_ag * ag, uint8_t id )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

创建音频连接（Audio Connection）。

由 HFP 音频网关（AG）创建音频连接，包含编解码器连接（Codec Connection）和音频连接（Audio Connection）两个设置过程。双方均支持编解码器协商时，先建立编解码器连接；传入的编解码器 ID 与上次连接不同，则触发编解码器连接过程。该连接建立后，再开始音频连接。传入 ID 可为 BT_HFP_AG_CODEC_XXX 之一。双方均支持协商时，ID 可从 codec 回调通知的 ID 位图中选择；否则必须为 BT_HFP_AG_CODEC_CVSD。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `id` | 编解码器 ID（Codec ID）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga4da632e9775051df6a5b5010fd3806df"></a>

### `bt_hfp_ag_battery_level()`

```c
int bt_hfp_ag_battery_level ( struct bt_hfp_ag * ag, uint8_t level )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

设置电池电量（Battery Level）。

设置电池电量（Battery Level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `level` | 电池电量（Battery Level）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga5b602810558268396f0cb64adcb0d014"></a>

### `bt_hfp_ag_connect()`

```c
int bt_hfp_ag_connect ( struct bt_conn * conn, struct bt_hfp_ag ** ag, uint8_t channel )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

创建免提规范音频网关会话（HFP AG Session）。

创建免提规范音频网关会话（HFP AG Session）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | ACL 连接对象（Connection Object）。 |
| `ag` | 已创建的 HFP AG 对象。 |
| `channel` | 要连接的对端 RFCOMM 通道（Channel）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gadf0b4aef701cf0986ea9599ad79d451a"></a>

### `bt_hfp_ag_disconnect()`

```c
int bt_hfp_ag_disconnect ( struct bt_hfp_ag * ag)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

断开免提规范音频网关会话（HFP AG Session）。

断开免提规范音频网关会话（HFP AG Session）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga5e249248a52d7c95c9d3f3f852bf2314"></a>

### `bt_hfp_ag_explicit_call_transfer()`

```c
int bt_hfp_ag_explicit_call_transfer ( struct bt_hfp_ag * ag)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

显式呼叫转移（Explicit Call Transfer）

连接两路通话，并使用户从两路通话中退出，即显式呼叫转移（Explicit Call Transfer）。未启用 CONFIG_BT_HFP_AG_3WAY_CALL 时，调用返回 -ENOTSUP。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaacc2df6144e1a33b13635855fe74f1f1"></a>

### `bt_hfp_ag_hf_indicator()`

```c
int bt_hfp_ag_hf_indicator ( struct bt_hfp_ag * ag, enum hfp_ag_hf_indicators indicator, bool enable )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

激活／停用免提单元指示器（HF Indicator）。

允许免提单元（HF）发出 +BIND 主动结果码（Unsolicited Result Code），激活或停用 AG 支持的 HF 指示器（HF Indicators）。可激活／停用的指示器定义在 enum hfp_ag_hf_indicators 中。BT_HFP_AG_HF_INDICATOR_ENH_SAFETY 支持增强安全（Enhanced Safety），仅启用对应配置后，指示器才可为 HFP_AG_ENHANCED_SAFETY_IND。BT_HFP_AG_HF_INDICATOR_BATTERY 支持剩余电池电量，仅启用对应配置后，指示器才可为 HFP_AG_BATTERY_LEVEL_IND。未启用 CONFIG_BT_HFP_HF_HF_INDICATORS 时，调用返回 -ENOTSUP。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `indicator` | AG 所支持的 HF 指示器（HF Indicator）。 |
| `enable` | 启用／禁用指定 HF 指示器（HF Indicator）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga4bbcec3ed5394e965aa7404dc968b94d"></a>

### `bt_hfp_ag_hold()`

```c
int bt_hfp_ag_hold ( struct bt_hfp_ag_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

保持活动通话（Hold Active Call）。

保持活动通话（Hold Active Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gab288d6e6b45a24b706328da58ca43a3b"></a>

### `bt_hfp_ag_hold_incoming()`

```c
int bt_hfp_ag_hold_incoming ( struct bt_hfp_ag_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

保持来电（Put Incoming Call on Hold）。

保持来电（Put Incoming Call on Hold）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga881ea4d3cc732fb5d804df203dde7746"></a>

### `bt_hfp_ag_inband_ringtone()`

```c
int bt_hfp_ag_inband_ringtone ( struct bt_hfp_ag * ag, bool inband )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

设置带内铃音（In-Band Ring Tone）。

设置带内铃音（In-Band Ring Tone）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `inband` | 带内（In-band）或非带内。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga5614bf3f1de11959a0364f458523e06e"></a>

### `bt_hfp_ag_ongoing_calls()`

```c
int bt_hfp_ag_ongoing_calls ( struct bt_hfp_ag * ag, struct bt_hfp_ag_ongoing_call * calls, size_t count )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

设置正在进行的通话（Ongoing Calls）。

收到 AT+CIND? 命令时，用于设置正在进行的通话（Ongoing Calls）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `calls` | 正在进行的通话（Ongoing Calls）。 |
| `count` | 正在进行的通话数量。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga580328104cf990c6f9e0a64642c16ebd"></a>

### `bt_hfp_ag_outgoing()`

```c
int bt_hfp_ag_outgoing ( struct bt_hfp_ag * ag, const char * number )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

拨打电话（Dial a Call）。

拨打电话（Dial a Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `number` | 拨号号码（Dialing number）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga379ec1c540195549fc59417d8d1ce7e5"></a>

### `bt_hfp_ag_register()`

```c
int bt_hfp_ag_register ( struct bt_hfp_ag_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

注册免提规范音频网关（HFP AG）配置文件（Profile）。

注册免提规范（Handsfree Profile）AG 回调，以监测状态并获取显示所需的 HFP 详细信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga195daffc37f1a3f210ba52dae1a9c4c2"></a>

### `bt_hfp_ag_reject()`

```c
int bt_hfp_ag_reject ( struct bt_hfp_ag_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

拒接来电（Reject Incoming Call）。

拒接来电（Reject Incoming Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga018d8ed8912f9dcef8c5fa37ac2bd889"></a>

### `bt_hfp_ag_remote_accept()`

```c
int bt_hfp_ag_remote_accept ( struct bt_hfp_ag_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

向 HFP 单元通知远端接听通话。

向 HFP 单元通知远端接听通话。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga443cd2928686f222d61f06c7477ea793"></a>

### `bt_hfp_ag_remote_incoming()`

```c
int bt_hfp_ag_remote_incoming ( struct bt_hfp_ag * ag, const char * number )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

向免提规范单元（HFP Unit）通知来电（Incoming Call）。

向免提规范单元（HFP Unit）通知来电（Incoming Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `number` | 拨号号码（Dialing number）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gacb1b361e6b0a441102f7ccd641eb3e6b"></a>

### `bt_hfp_ag_remote_reject()`

```c
int bt_hfp_ag_remote_reject ( struct bt_hfp_ag_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

向 HFP 单元通知远端拒接通话。

向 HFP 单元通知远端拒接通话。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga0a12a56baa25e2aea101a387fcccb88e"></a>

### `bt_hfp_ag_remote_ringing()`

```c
int bt_hfp_ag_remote_ringing ( struct bt_hfp_ag_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

向 HFP 单元通知远端开始振铃（Ringing）。

向 HFP 单元通知远端开始振铃（Ringing）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga525085c7c75e412ca43ba8b23cbc0c3d"></a>

### `bt_hfp_ag_remote_terminate()`

```c
int bt_hfp_ag_remote_terminate ( struct bt_hfp_ag_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

向 HFP 单元通知远端终止活动／保持的通话。

向 HFP 单元通知远端终止活动／保持的通话。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga405fcf8e03bac39bd5b0e7bf2766045f"></a>

### `bt_hfp_ag_retrieve()`

```c
int bt_hfp_ag_retrieve ( struct bt_hfp_ag_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

恢复保持的通话（Retrieve Held Call）。

恢复保持的通话（Retrieve Held Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga0f8b2e463aefbf74b26ac4f27033486c"></a>

### `bt_hfp_ag_roaming_status()`

```c
int bt_hfp_ag_roaming_status ( struct bt_hfp_ag * ag, uint8_t status )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

设置漫游状态（Roaming Status）。

设置漫游状态（Roaming Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `status` | 漫游状态（Roaming Status）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaf838e54046c380931f23a59919ccfa5b"></a>

### `bt_hfp_ag_service_availability()`

```c
int bt_hfp_ag_service_availability ( struct bt_hfp_ag * ag, bool available )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

设置服务可用性（Service Availability）。

设置服务可用性（Service Availability）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `available` | 服务可用性（Service Availability） |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaaf066dce38c028254b6c1880bcebaa13"></a>

### `bt_hfp_ag_set_operator()`

```c
int bt_hfp_ag_set_operator ( struct bt_hfp_ag * ag, uint8_t mode, char * name )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

设置当前网络运营商（Network Operator）。

设置当前网络运营商（Network Operator）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `mode` | 当前模式（Current Mode），不提供运营商名称的信息。 |
| `name` | 以字母数字格式表示网络运营商名称（Network Operator Name）的字符串，不得超过 16 个字符。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga20ef1240e0ff72d914405b259cc3164f"></a>

### `bt_hfp_ag_signal_strength()`

```c
int bt_hfp_ag_signal_strength ( struct bt_hfp_ag * ag, uint8_t strength )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

设置信号强度（Signal Strength）。

设置信号强度（Signal Strength）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `strength` | 信号强度（Signal Strength）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga2f2e85a6076930ed87bc0727c75209a9"></a>

### `bt_hfp_ag_terminate()`

```c
int bt_hfp_ag_terminate ( struct bt_hfp_ag_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

终止活动／保持的通话（Active/Held Call）。

终止活动／保持的通话（Active/Held Call）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga53778bd332c95fa4357d254f5ef125a2"></a>

### `bt_hfp_ag_vgm()`

```c
int bt_hfp_ag_vgm ( struct bt_hfp_ag * ag, uint8_t vgm )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

设置免提单元麦克风增益（HF Microphone Gain）。

设置免提单元麦克风增益（HF Microphone Gain）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `vgm` | 麦克风增益值（Microphone Gain Value）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gabdad8c764c91e133598584d741ed9d4b"></a>

### `bt_hfp_ag_vgs()`

```c
int bt_hfp_ag_vgs ( struct bt_hfp_ag * ag, uint8_t vgs )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

设置免提单元扬声器增益（HF Speaker Gain）。

设置免提单元扬声器增益（HF Speaker Gain）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `vgs` | 扬声器增益值（Speaker Gain Value）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga28682fc5d8cfee9c0adece68bcb94c3f"></a>

### `bt_hfp_ag_voice_recognition()`

```c
int bt_hfp_ag_voice_recognition ( struct bt_hfp_ag * ag, bool activate )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

启用／禁用语音识别功能（Voice Recognition）。

启用／禁用语音识别功能（Voice Recognition）。未启用 CONFIG_BT_HFP_AG_VOICE_RECG 时，调用返回 -ENOTSUP。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `activate` | 激活／停用语音识别功能（Voice Recognition）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga3668f3997afe9ab678f9eb2e6faf324d"></a>

### `bt_hfp_ag_vre_state()`

```c
int bt_hfp_ag_vre_state ( struct bt_hfp_ag * ag, uint8_t state )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

设置语音识别引擎状态（Voice Recognition Engine State）。

设置语音识别引擎状态（Voice Recognition Engine State），发送主动结果码 +BVRA: 1,`<vrecstate>`。`<vrecstate>` 是反映 AG 当前语音识别引擎状态的位掩码：位 0 为 1 表示 AG 已准备接受音频输入；位 1 为 1 表示 AG 正向 HF 发送音频；位 2 为 1 表示 AG 正处理音频输入。未启用 CONFIG_BT_HFP_AG_ENH_VOICE_RECG 时，调用返回 -ENOTSUP。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `state` | `<vrecstate>` 的值。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga4e71364283448c7c5d3306c111aa167d"></a>

### `bt_hfp_ag_vre_textual_representation()`

```c
int bt_hfp_ag_vre_textual_representation ( struct bt_hfp_ag * ag, uint8_t state, const char * id, uint8_t type, uint8_t operation, const char * text )
```

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

设置语音识别引擎状态及文本表示（Textual Representation）。

设置带有文本表示（Textual Representation）的语音识别引擎状态，发送主动结果码 +BVRA: 1,`<vrecstate>`, `<textualRepresentation>`。`<vrecstate>` 与 bt_hfp_ag_vre_state 的 state 参数相同。`<textualRepresentation>` 格式为 `<textID>`,`<textType>`,`<textOperation>`, `<string>`。

`<textID>`：当前文本的唯一 ID，以最多 4 个字符的十六进制字符串表示，少于 4 个字符也有效。`<textType>`：文本类型 ID，0 为 AG 从 HF 提供的音频输入中识别出的文本；1 为 AG 音频输出对应文本；2 为包含问题的 AG 音频输出文本；3 为包含错误说明的 AG 音频输出文本。`<textOperation>`：文本操作 ID，1 为 NewText（新文本），表示新文本开始，`<textID>` 改变时必须使用；2 为 Replace（替换），替换具有相同 `<textID>` 和 `<textType>` 的既有文本；3 为 Append（追加），将新文本追加到既有文本，保持相同 `<textID>` 和 `<textType>`。`<string>` 必须是 UTF-8 文本字符串，并始终用双引号括起。未启用 CONFIG_BT_HFP_AG_VOICE_RECG_TEXT 时，调用返回 -ENOTSUP。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `state` | `<vrecstate>` 的值。 |
| `id` | `<textID>` 的值。 |
| `type` | `<textType>` 的值。 |
| `operation` | `<textOperation>` 的值。 |
| `text` | `<string>` 的值。 |

**返回（Returns）**：成功返回 0，出错时返回负值。


## 6.7\_原页交叉引用（Cross References）

- [bt_hfp_ag_ongoing_call](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md)
- [bt_hfp_ag_cb](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md)
- [bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)
- [bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [zephyr/bluetooth/classic/hfp_ag.h](../api_file_clock_network_reference/P012_zephyr__bluetooth__classic__hfp_ag.h_文件参考.md)
- [CONFIG_BT_HFP_AG_3WAY_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_3WAY_CALL)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [CONFIG_BT_HFP_HF_HF_INDICATORS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_HF_INDICATORS)
- [CONFIG_BT_HFP_AG_VOICE_RECG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_VOICE_RECG)
- [CONFIG_BT_HFP_AG_ENH_VOICE_RECG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_ENH_VOICE_RECG)
- [CONFIG_BT_HFP_AG_VOICE_RECG_TEXT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_VOICE_RECG_TEXT)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga019020ee2ed73c218f7dadf8371bf9a6a83ea29c4261577438e481e2b9f0c7d37"></a>
<a id="gga019020ee2ed73c218f7dadf8371bf9a6a08a4f52a9ca4fdcaa1c6575b1b378b55"></a>
<a id="ggad2220b4a470cb3d537cf09492847568ea4c387d6e8628fc40e9969c95ff9ea658"></a>
<a id="ggad2220b4a470cb3d537cf09492847568eac2acf82710d562fd2852139f7e8146e2"></a>
<a id="ggad2220b4a470cb3d537cf09492847568ea09545d4deadcc910c42b615d21f91963"></a>
<a id="ggad2220b4a470cb3d537cf09492847568ea423017739b17f57e0a8adb7d6b9cffae"></a>
<a id="ggad2220b4a470cb3d537cf09492847568ea4faad88cf6cb9926f78e7da7065713f8"></a>
<a id="ggad2220b4a470cb3d537cf09492847568ea5b1a40f632b8d9ce3b02ffacb1a07fb2"></a>
<a id="ggad2220b4a470cb3d537cf09492847568ea2e155da5b54cb32a400de1d44ebc2542"></a>
<a id="gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234"></a>
<a id="gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d"></a>
<a id="gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5"></a>
<a id="gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b"></a>
<a id="gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493"></a>
<a id="gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863"></a>
<a id="gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609"></a>
<a id="gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36"></a>
<a id="gga030c97d703fb45a2055653c51cb1b403afd31a626b024de7e6e68ade0d776b14f"></a>
<a id="gga030c97d703fb45a2055653c51cb1b403a9719aca10a790eb9f62d498bc4bec9d1"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_蓝牙主机控制器接口（Bluetooth HCI）.md) · [返回大纲](大纲.md) · [下一章](P007_消息（Message）。.md)
