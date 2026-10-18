---
id: learning.zephyr-docs.api-file-clock-network-reference.page-12
title: zephyr__bluetooth__classic__hfp_ag.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hfp__ag_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_bluetooth\_\_classic\_\_hfp\_ag.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hfp__ag_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

免提配置文件音频网关（Handsfree Profile Audio Gateway）的处理。

<a id="details"></a>

```c
#include <zephyr/bluetooth/bluetooth.h>
```

查看此文件的源码。

免提配置文件音频网关（Handsfree Profile Audio Gateway）的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="r_gada6266f825879f39147c5d889e4192c9"></a>

```c
#define BT_HFP_AG_CODEC_CVSD 0x01
```

相关声明：[BT_HFP_AG_CODEC_CVSD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gada6266f825879f39147c5d889e4192c9)。

<a id="r_ga3591201c7310288ea2e01e2f77a0c0d3"></a>

```c
#define BT_HFP_AG_CODEC_MSBC 0x02
```

相关声明：[BT_HFP_AG_CODEC_MSBC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga3591201c7310288ea2e01e2f77a0c0d3)。

<a id="r_ga8a833c4b11dc9e8fd08a73a2af418d83"></a>

```c
#define BT_HFP_AG_CODEC_LC3_SWB 0x03
```

相关声明：[BT_HFP_AG_CODEC_LC3_SWB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga8a833c4b11dc9e8fd08a73a2af418d83)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 12.3\_类型定义（Typedefs）

<a id="r_ga8e9b485f7ea0b9e16d96f578cdc587c3"></a>

```c
typedef int(* bt_hfp_ag_query_subscriber_func_t) (struct bt_hfp_ag *ag, char *number, uint8_t type, uint8_t service)
```

相关声明：[bt_hfp_ag_query_subscriber_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga8e9b485f7ea0b9e16d96f578cdc587c3)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

查询用户号码（Subscriber Number）的回调函数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.4\_枚举（Enumerations）

<a id="r_ga37640efdcc737bfa0390df889a62f810"></a>

```c
enum bt_hfp_ag_indicator { BT_HFP_AG_SERVICE_IND = 0 , BT_HFP_AG_CALL_IND = 1 , BT_HFP_AG_CALL_SETUP_IND = 2 , BT_HFP_AG_CALL_HELD_IND = 3 , BT_HFP_AG_SIGNAL_IND = 4 , BT_HFP_AG_ROAM_IND = 5 , BT_HFP_AG_BATTERY_IND = 6 , BT_HFP_AG_IND_MAX }
```

相关声明：[bt_hfp_ag_indicator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga37640efdcc737bfa0390df889a62f810)、[BT_HFP_AG_SERVICE_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234)、[BT_HFP_AG_CALL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d)、[BT_HFP_AG_CALL_SETUP_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5)、[BT_HFP_AG_CALL_HELD_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b)、[BT_HFP_AG_SIGNAL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493)、[BT_HFP_AG_ROAM_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863)、[BT_HFP_AG_BATTERY_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609)、[BT_HFP_AG_IND_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36)。

<a id="r_ga030c97d703fb45a2055653c51cb1b403"></a>

```c
enum hfp_ag_hf_indicators { HFP_AG_ENHANCED_SAFETY_IND = 1 , HFP_AG_BATTERY_LEVEL_IND = 2 }
```

相关声明：[hfp_ag_hf_indicators](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga030c97d703fb45a2055653c51cb1b403)、[HFP_AG_ENHANCED_SAFETY_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga030c97d703fb45a2055653c51cb1b403afd31a626b024de7e6e68ade0d776b14f)、[HFP_AG_BATTERY_LEVEL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga030c97d703fb45a2055653c51cb1b403a9719aca10a790eb9f62d498bc4bec9d1)。

<a id="r_gad2220b4a470cb3d537cf09492847568e"></a>

```c
enum bt_hfp_ag_call_status { BT_HFP_AG_CALL_STATUS_ACTIVE = 0 , BT_HFP_AG_CALL_STATUS_HELD = 1 , BT_HFP_AG_CALL_STATUS_DIALING = 2 , BT_HFP_AG_CALL_STATUS_ALERTING = 3 , BT_HFP_AG_CALL_STATUS_INCOMING = 4 , BT_HFP_AG_CALL_STATUS_WAITING = 5 , BT_HFP_AG_CALL_STATUS_INCOMING_HELD = 6 }
```

相关声明：[bt_hfp_ag_call_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gad2220b4a470cb3d537cf09492847568e)、[BT_HFP_AG_CALL_STATUS_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea4c387d6e8628fc40e9969c95ff9ea658)、[BT_HFP_AG_CALL_STATUS_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568eac2acf82710d562fd2852139f7e8146e2)、[BT_HFP_AG_CALL_STATUS_DIALING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea09545d4deadcc910c42b615d21f91963)、[BT_HFP_AG_CALL_STATUS_ALERTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea423017739b17f57e0a8adb7d6b9cffae)、[BT_HFP_AG_CALL_STATUS_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea4faad88cf6cb9926f78e7da7065713f8)、[BT_HFP_AG_CALL_STATUS_WAITING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea5b1a40f632b8d9ce3b02ffacb1a07fb2)、[BT_HFP_AG_CALL_STATUS_INCOMING_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea2e155da5b54cb32a400de1d44ebc2542)。

<a id="r_ga019020ee2ed73c218f7dadf8371bf9a6"></a>

```c
enum bt_hfp_ag_call_dir { BT_HFP_AG_CALL_DIR_OUTGOING = 0 , BT_HFP_AG_CALL_DIR_INCOMING = 1 }
```

相关声明：[bt_hfp_ag_call_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga019020ee2ed73c218f7dadf8371bf9a6)、[BT_HFP_AG_CALL_DIR_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga019020ee2ed73c218f7dadf8371bf9a6a83ea29c4261577438e481e2b9f0c7d37)、[BT_HFP_AG_CALL_DIR_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga019020ee2ed73c218f7dadf8371bf9a6a08a4f52a9ca4fdcaa1c6575b1b378b55)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.5\_函数（Functions）

<a id="r_ga379ec1c540195549fc59417d8d1ce7e5"></a>

```c
int bt_hfp_ag_register (struct bt_hfp_ag_cb *cb)
```

相关声明：[bt_hfp_ag_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga379ec1c540195549fc59417d8d1ce7e5)、[bt_hfp_ag_cb](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md)。

注册免提规范音频网关（HFP AG）配置文件（Profile）。

<a id="r_ga5b602810558268396f0cb64adcb0d014"></a>

```c
int bt_hfp_ag_connect (struct bt_conn *conn, struct bt_hfp_ag **ag, uint8_t channel)
```

相关声明：[bt_hfp_ag_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga5b602810558268396f0cb64adcb0d014)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

创建免提规范音频网关会话（HFP AG Session）。

<a id="r_gadf0b4aef701cf0986ea9599ad79d451a"></a>

```c
int bt_hfp_ag_disconnect (struct bt_hfp_ag *ag)
```

相关声明：[bt_hfp_ag_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gadf0b4aef701cf0986ea9599ad79d451a)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)。

断开免提规范音频网关会话（HFP AG Session）。

<a id="r_ga443cd2928686f222d61f06c7477ea793"></a>

```c
int bt_hfp_ag_remote_incoming (struct bt_hfp_ag *ag, const char *number)
```

相关声明：[bt_hfp_ag_remote_incoming](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga443cd2928686f222d61f06c7477ea793)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)。

向免提规范单元（HFP Unit）通知来电（Incoming Call）。

<a id="r_gab288d6e6b45a24b706328da58ca43a3b"></a>

```c
int bt_hfp_ag_hold_incoming (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_hold_incoming](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gab288d6e6b45a24b706328da58ca43a3b)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

保持来电（Put Incoming Call on Hold）。

<a id="r_ga195daffc37f1a3f210ba52dae1a9c4c2"></a>

```c
int bt_hfp_ag_reject (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_reject](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga195daffc37f1a3f210ba52dae1a9c4c2)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

拒接来电（Reject Incoming Call）。

<a id="r_ga351e1b78b8c19c3971554fabb331e5c6"></a>

```c
int bt_hfp_ag_accept (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga351e1b78b8c19c3971554fabb331e5c6)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

接听来电（Accept Incoming Call）。

<a id="r_ga2f2e85a6076930ed87bc0727c75209a9"></a>

```c
int bt_hfp_ag_terminate (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga2f2e85a6076930ed87bc0727c75209a9)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

终止活动／保持的通话（Active/Held Call）。

<a id="r_ga405fcf8e03bac39bd5b0e7bf2766045f"></a>

```c
int bt_hfp_ag_retrieve (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_retrieve](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga405fcf8e03bac39bd5b0e7bf2766045f)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

恢复保持的通话（Retrieve Held Call）。

<a id="r_ga4bbcec3ed5394e965aa7404dc968b94d"></a>

```c
int bt_hfp_ag_hold (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_hold](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga4bbcec3ed5394e965aa7404dc968b94d)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

保持活动通话（Hold Active Call）。

<a id="r_ga580328104cf990c6f9e0a64642c16ebd"></a>

```c
int bt_hfp_ag_outgoing (struct bt_hfp_ag *ag, const char *number)
```

相关声明：[bt_hfp_ag_outgoing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga580328104cf990c6f9e0a64642c16ebd)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)。

拨打电话（Dial a Call）。

<a id="r_ga0a12a56baa25e2aea101a387fcccb88e"></a>

```c
int bt_hfp_ag_remote_ringing (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_remote_ringing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga0a12a56baa25e2aea101a387fcccb88e)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

向 HFP 单元通知远端开始振铃（Ringing）。

<a id="r_gacb1b361e6b0a441102f7ccd641eb3e6b"></a>

```c
int bt_hfp_ag_remote_reject (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_remote_reject](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gacb1b361e6b0a441102f7ccd641eb3e6b)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

向 HFP 单元通知远端拒接通话。

<a id="r_ga018d8ed8912f9dcef8c5fa37ac2bd889"></a>

```c
int bt_hfp_ag_remote_accept (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_remote_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga018d8ed8912f9dcef8c5fa37ac2bd889)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

向 HFP 单元通知远端接听通话。

<a id="r_ga525085c7c75e412ca43ba8b23cbc0c3d"></a>

```c
int bt_hfp_ag_remote_terminate (struct bt_hfp_ag_call *call)
```

相关声明：[bt_hfp_ag_remote_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga525085c7c75e412ca43ba8b23cbc0c3d)、[bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)。

向 HFP 单元通知远端终止活动／保持的通话。

<a id="r_ga5e249248a52d7c95c9d3f3f852bf2314"></a>

```c
int bt_hfp_ag_explicit_call_transfer (struct bt_hfp_ag *ag)
```

相关声明：[bt_hfp_ag_explicit_call_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga5e249248a52d7c95c9d3f3f852bf2314)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)。

显式呼叫转移（Explicit Call Transfer）

<a id="r_ga53778bd332c95fa4357d254f5ef125a2"></a>

```c
int bt_hfp_ag_vgm (struct bt_hfp_ag *ag, uint8_t vgm)
```

相关声明：[bt_hfp_ag_vgm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga53778bd332c95fa4357d254f5ef125a2)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置免提单元麦克风增益（HF Microphone Gain）。

<a id="r_gabdad8c764c91e133598584d741ed9d4b"></a>

```c
int bt_hfp_ag_vgs (struct bt_hfp_ag *ag, uint8_t vgs)
```

相关声明：[bt_hfp_ag_vgs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gabdad8c764c91e133598584d741ed9d4b)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置免提单元扬声器增益（HF Speaker Gain）。

<a id="r_gaaf066dce38c028254b6c1880bcebaa13"></a>

```c
int bt_hfp_ag_set_operator (struct bt_hfp_ag *ag, uint8_t mode, char *name)
```

相关声明：[bt_hfp_ag_set_operator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gaaf066dce38c028254b6c1880bcebaa13)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置当前网络运营商（Network Operator）。

<a id="r_ga542a1754a16e32a9b2651f1230aa7066"></a>

```c
int bt_hfp_ag_audio_connect (struct bt_hfp_ag *ag, uint8_t id)
```

相关声明：[bt_hfp_ag_audio_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga542a1754a16e32a9b2651f1230aa7066)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

创建音频连接（Audio Connection）。

<a id="r_ga881ea4d3cc732fb5d804df203dde7746"></a>

```c
int bt_hfp_ag_inband_ringtone (struct bt_hfp_ag *ag, bool inband)
```

相关声明：[bt_hfp_ag_inband_ringtone](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga881ea4d3cc732fb5d804df203dde7746)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置带内铃音（In-Band Ring Tone）。

<a id="r_ga28682fc5d8cfee9c0adece68bcb94c3f"></a>

```c
int bt_hfp_ag_voice_recognition (struct bt_hfp_ag *ag, bool activate)
```

相关声明：[bt_hfp_ag_voice_recognition](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga28682fc5d8cfee9c0adece68bcb94c3f)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用语音识别功能（Voice Recognition）。

<a id="r_ga3668f3997afe9ab678f9eb2e6faf324d"></a>

```c
int bt_hfp_ag_vre_state (struct bt_hfp_ag *ag, uint8_t state)
```

相关声明：[bt_hfp_ag_vre_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga3668f3997afe9ab678f9eb2e6faf324d)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置语音识别引擎状态（Voice Recognition Engine State）。

<a id="r_ga4e71364283448c7c5d3306c111aa167d"></a>

```c
int bt_hfp_ag_vre_textual_representation (struct bt_hfp_ag *ag, uint8_t state, const char *id, uint8_t type, uint8_t operation, const char *text)
```

相关声明：[bt_hfp_ag_vre_textual_representation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga4e71364283448c7c5d3306c111aa167d)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置语音识别引擎状态及文本表示（Textual Representation）。

<a id="r_ga20ef1240e0ff72d914405b259cc3164f"></a>

```c
int bt_hfp_ag_signal_strength (struct bt_hfp_ag *ag, uint8_t strength)
```

相关声明：[bt_hfp_ag_signal_strength](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga20ef1240e0ff72d914405b259cc3164f)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置信号强度（Signal Strength）。

<a id="r_ga0f8b2e463aefbf74b26ac4f27033486c"></a>

```c
int bt_hfp_ag_roaming_status (struct bt_hfp_ag *ag, uint8_t status)
```

相关声明：[bt_hfp_ag_roaming_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga0f8b2e463aefbf74b26ac4f27033486c)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置漫游状态（Roaming Status）。

<a id="r_ga4da632e9775051df6a5b5010fd3806df"></a>

```c
int bt_hfp_ag_battery_level (struct bt_hfp_ag *ag, uint8_t level)
```

相关声明：[bt_hfp_ag_battery_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga4da632e9775051df6a5b5010fd3806df)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置电池电量（Battery Level）。

<a id="r_gaf838e54046c380931f23a59919ccfa5b"></a>

```c
int bt_hfp_ag_service_availability (struct bt_hfp_ag *ag, bool available)
```

相关声明：[bt_hfp_ag_service_availability](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gaf838e54046c380931f23a59919ccfa5b)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置服务可用性（Service Availability）。

<a id="r_gaacc2df6144e1a33b13635855fe74f1f1"></a>

```c
int bt_hfp_ag_hf_indicator (struct bt_hfp_ag *ag, enum hfp_ag_hf_indicators indicator, bool enable)
```

相关声明：[bt_hfp_ag_hf_indicator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gaacc2df6144e1a33b13635855fe74f1f1)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[hfp_ag_hf_indicators](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga030c97d703fb45a2055653c51cb1b403)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

激活／停用免提单元指示器（HF Indicator）。

<a id="r_ga5614bf3f1de11959a0364f458523e06e"></a>

```c
int bt_hfp_ag_ongoing_calls (struct bt_hfp_ag *ag, struct bt_hfp_ag_ongoing_call *calls, size_t count)
```

相关声明：[bt_hfp_ag_ongoing_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga5614bf3f1de11959a0364f458523e06e)、[bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)、[bt_hfp_ag_ongoing_call](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md)。

设置正在进行的通话（Ongoing Calls）。


## 12.6\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [查看此文件的源码。](../api_source_pcie_hid_reference/P005_hfp_ag.h_源码浏览.md)
- [bt_hfp_ag_ongoing_call](../bluetooth_service_model_reference/P086_bt_hfp_ag_ongoing_call_结构体.md)
- [bt_hfp_ag_cb](../bluetooth_service_model_reference/P085_bt_hfp_ag_cb_结构体.md)
- [BT_HFP_AG_CODEC_CVSD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gada6266f825879f39147c5d889e4192c9)
- [BT_HFP_AG_CODEC_MSBC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga3591201c7310288ea2e01e2f77a0c0d3)
- [BT_HFP_AG_CODEC_LC3_SWB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga8a833c4b11dc9e8fd08a73a2af418d83)
- [bt_hfp_ag_query_subscriber_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga8e9b485f7ea0b9e16d96f578cdc587c3)
- [bt_hfp_ag](../bluetooth_service_model_reference/P083_bt_hfp_ag_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hfp_ag_indicator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga37640efdcc737bfa0390df889a62f810)
- [BT_HFP_AG_SERVICE_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234)
- [BT_HFP_AG_CALL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d)
- [BT_HFP_AG_CALL_SETUP_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5)
- [BT_HFP_AG_CALL_HELD_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b)
- [BT_HFP_AG_SIGNAL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493)
- [BT_HFP_AG_ROAM_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863)
- [BT_HFP_AG_BATTERY_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609)
- [BT_HFP_AG_IND_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36)
- [hfp_ag_hf_indicators](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga030c97d703fb45a2055653c51cb1b403)
- [HFP_AG_ENHANCED_SAFETY_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga030c97d703fb45a2055653c51cb1b403afd31a626b024de7e6e68ade0d776b14f)
- [HFP_AG_BATTERY_LEVEL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga030c97d703fb45a2055653c51cb1b403a9719aca10a790eb9f62d498bc4bec9d1)
- [bt_hfp_ag_call_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gad2220b4a470cb3d537cf09492847568e)
- [BT_HFP_AG_CALL_STATUS_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea4c387d6e8628fc40e9969c95ff9ea658)
- [BT_HFP_AG_CALL_STATUS_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568eac2acf82710d562fd2852139f7e8146e2)
- [BT_HFP_AG_CALL_STATUS_DIALING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea09545d4deadcc910c42b615d21f91963)
- [BT_HFP_AG_CALL_STATUS_ALERTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea423017739b17f57e0a8adb7d6b9cffae)
- [BT_HFP_AG_CALL_STATUS_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea4faad88cf6cb9926f78e7da7065713f8)
- [BT_HFP_AG_CALL_STATUS_WAITING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea5b1a40f632b8d9ce3b02ffacb1a07fb2)
- [BT_HFP_AG_CALL_STATUS_INCOMING_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ggad2220b4a470cb3d537cf09492847568ea2e155da5b54cb32a400de1d44ebc2542)
- [bt_hfp_ag_call_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga019020ee2ed73c218f7dadf8371bf9a6)
- [BT_HFP_AG_CALL_DIR_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga019020ee2ed73c218f7dadf8371bf9a6a83ea29c4261577438e481e2b9f0c7d37)
- [BT_HFP_AG_CALL_DIR_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gga019020ee2ed73c218f7dadf8371bf9a6a08a4f52a9ca4fdcaa1c6575b1b378b55)
- [bt_hfp_ag_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga379ec1c540195549fc59417d8d1ce7e5)
- [bt_hfp_ag_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga5b602810558268396f0cb64adcb0d014)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_hfp_ag_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gadf0b4aef701cf0986ea9599ad79d451a)
- [bt_hfp_ag_remote_incoming](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga443cd2928686f222d61f06c7477ea793)
- [bt_hfp_ag_hold_incoming](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gab288d6e6b45a24b706328da58ca43a3b)
- [bt_hfp_ag_call](../bluetooth_service_model_reference/P084_bt_hfp_ag_call_结构体.md)
- [bt_hfp_ag_reject](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga195daffc37f1a3f210ba52dae1a9c4c2)
- [bt_hfp_ag_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga351e1b78b8c19c3971554fabb331e5c6)
- [bt_hfp_ag_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga2f2e85a6076930ed87bc0727c75209a9)
- [bt_hfp_ag_retrieve](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga405fcf8e03bac39bd5b0e7bf2766045f)
- [bt_hfp_ag_hold](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga4bbcec3ed5394e965aa7404dc968b94d)
- [bt_hfp_ag_outgoing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga580328104cf990c6f9e0a64642c16ebd)
- [bt_hfp_ag_remote_ringing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga0a12a56baa25e2aea101a387fcccb88e)
- [bt_hfp_ag_remote_reject](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gacb1b361e6b0a441102f7ccd641eb3e6b)
- [bt_hfp_ag_remote_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga018d8ed8912f9dcef8c5fa37ac2bd889)
- [bt_hfp_ag_remote_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga525085c7c75e412ca43ba8b23cbc0c3d)
- [bt_hfp_ag_explicit_call_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga5e249248a52d7c95c9d3f3f852bf2314)
- [bt_hfp_ag_vgm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga53778bd332c95fa4357d254f5ef125a2)
- [bt_hfp_ag_vgs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gabdad8c764c91e133598584d741ed9d4b)
- [bt_hfp_ag_set_operator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gaaf066dce38c028254b6c1880bcebaa13)
- [bt_hfp_ag_audio_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga542a1754a16e32a9b2651f1230aa7066)
- [bt_hfp_ag_inband_ringtone](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga881ea4d3cc732fb5d804df203dde7746)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_hfp_ag_voice_recognition](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga28682fc5d8cfee9c0adece68bcb94c3f)
- [bt_hfp_ag_vre_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga3668f3997afe9ab678f9eb2e6faf324d)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_hfp_ag_vre_textual_representation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga4e71364283448c7c5d3306c111aa167d)
- [bt_hfp_ag_signal_strength](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga20ef1240e0ff72d914405b259cc3164f)
- [bt_hfp_ag_roaming_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga0f8b2e463aefbf74b26ac4f27033486c)
- [bt_hfp_ag_battery_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga4da632e9775051df6a5b5010fd3806df)
- [bt_hfp_ag_service_availability](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gaf838e54046c380931f23a59919ccfa5b)
- [bt_hfp_ag_hf_indicator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gaacc2df6144e1a33b13635855fe74f1f1)
- [bt_hfp_ag_ongoing_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga5614bf3f1de11959a0364f458523e06e)

<a id="header-details"></a>

---

[上一章](P011_zephyr__dt-bindings__clock__gd32c2x1-clocks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__dt-bindings__sensor__iis3dwb.h_文件参考.md)
