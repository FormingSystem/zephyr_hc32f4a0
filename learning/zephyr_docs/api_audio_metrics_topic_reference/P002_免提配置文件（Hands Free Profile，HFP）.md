---
id: learning.zephyr-docs.api-audio-metrics-topic-reference.page-2
title: 免提配置文件（Hands Free Profile，HFP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_免提配置文件（Hands Free Profile，HFP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

免提配置文件（Hands Free Profile，HFP）

<a id="details"></a>

免提配置文件（Hands Free Profile，HFP）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fhfp_5Fhf_5Fcurrent_5Fcall"></a>

```c
struct bt_hfp_hf_current_call
```

相关声明：[bt_hfp_hf_current_call](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md)。

当前呼叫（Current Call）的信息。

<a id="r_bt_5Fhfp_5Fhf_5Fcb"></a>

```c
struct bt_hfp_hf_cb
```

相关声明：[bt_hfp_hf_cb](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md)。

免提配置文件（HFP）的应用回调。

<a id="r_bt_5Fhfp_5Fhf"></a>

```c
struct bt_hfp_hf
```

相关声明：[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提配置文件免提单元（HFP HF）结构。

<a id="r_bt_5Fhfp_5Fhf_5Fcall"></a>

```c
struct bt_hfp_hf_call
```

相关声明：[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提配置文件免提单元（HFP HF）的呼叫结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga0e46a981a70dcdecbae119ebb6d61aa0"></a>

```c
#define BT_HFP_HF_CODEC_CVSD 0x01
```

相关声明：[BT_HFP_HF_CODEC_CVSD](#ga0e46a981a70dcdecbae119ebb6d61aa0)。

<a id="r_gaea9fb177ae8ba32650dc93f1b2953333"></a>

```c
#define BT_HFP_HF_CODEC_MSBC 0x02
```

相关声明：[BT_HFP_HF_CODEC_MSBC](#gaea9fb177ae8ba32650dc93f1b2953333)。

<a id="r_gac8ab2e9ff6c8b9a06ac460f751dec1ad"></a>

```c
#define BT_HFP_HF_CODEC_LC3_SWB 0x03
```

相关声明：[BT_HFP_HF_CODEC_LC3_SWB](#gac8ab2e9ff6c8b9a06ac460f751dec1ad)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.3\_枚举（Enumerations）

<a id="r_ga810c80de5baf92feb23650374b60bcee"></a>

```c
enum bt_hfp_hf_call_status { BT_HFP_HF_CALL_STATUS_ACTIVE = 0 , BT_HFP_HF_CALL_STATUS_HELD = 1 , BT_HFP_HF_CALL_STATUS_DIALING = 2 , BT_HFP_HF_CALL_STATUS_ALERTING = 3 , BT_HFP_HF_CALL_STATUS_INCOMING = 4 , BT_HFP_HF_CALL_STATUS_WAITING = 5 , BT_HFP_HF_CALL_STATUS_INCOMING_HELD = 6 }
```

相关声明：[bt_hfp_hf_call_status](#ga810c80de5baf92feb23650374b60bcee)、[BT_HFP_HF_CALL_STATUS_ACTIVE](#gga810c80de5baf92feb23650374b60bceea1ea1ba685375baaabab22ad1c01ca6af)、[BT_HFP_HF_CALL_STATUS_HELD](#gga810c80de5baf92feb23650374b60bceeab4db9c2eb21b5eb79517c0a761bc7dfa)、[BT_HFP_HF_CALL_STATUS_DIALING](#gga810c80de5baf92feb23650374b60bceea9ff342787f8a6f7b9a5c0db1afa1bfb9)、[BT_HFP_HF_CALL_STATUS_ALERTING](#gga810c80de5baf92feb23650374b60bceea7377bf80fd685178d0d8b39189b2122a)、[BT_HFP_HF_CALL_STATUS_INCOMING](#gga810c80de5baf92feb23650374b60bceea8f8fc15f39de43b1ed202e16cd198104)、[BT_HFP_HF_CALL_STATUS_WAITING](#gga810c80de5baf92feb23650374b60bceea974da5247c5d332b11c42e93c9cbd831)、[BT_HFP_HF_CALL_STATUS_INCOMING_HELD](#gga810c80de5baf92feb23650374b60bceeabfa959b76eab9fc14ae941e3c1cd45ff)。

通话状态（Call Status）。

<a id="r_ga6c2ba70d70c8f9d6d569662086985c85"></a>

```c
enum bt_hfp_hf_call_dir { BT_HFP_HF_CALL_DIR_OUTGOING = 0 , BT_HFP_HF_CALL_DIR_INCOMING = 1 }
```

相关声明：[bt_hfp_hf_call_dir](#ga6c2ba70d70c8f9d6d569662086985c85)、[BT_HFP_HF_CALL_DIR_OUTGOING](#gga6c2ba70d70c8f9d6d569662086985c85aa631c2cc079db31712ac2ec7ac3dee3f)、[BT_HFP_HF_CALL_DIR_INCOMING](#gga6c2ba70d70c8f9d6d569662086985c85adf30d13bccb711d32a3c75e5c1d47d97)。

通话方向（Call Direction）。

<a id="r_ga38619377f146492993ee9a92a487af50"></a>

```c
enum bt_hfp_hf_call_mode { BT_HFP_HF_CALL_MODE_VOICE = 0 , BT_HFP_HF_CALL_MODE_DATA = 1 , BT_HFP_HF_CALL_MODE_FAX = 2 }
```

相关声明：[bt_hfp_hf_call_mode](#ga38619377f146492993ee9a92a487af50)、[BT_HFP_HF_CALL_MODE_VOICE](#gga38619377f146492993ee9a92a487af50ac2233c577a6d8b8871b8e31969616f66)、[BT_HFP_HF_CALL_MODE_DATA](#gga38619377f146492993ee9a92a487af50a5a35798fc921e975775c496ac49193c9)、[BT_HFP_HF_CALL_MODE_FAX](#gga38619377f146492993ee9a92a487af50a646f51233cf8906d377bf0d6860f3bb0)。

呼叫模式（Call Mode）。

<a id="r_ga862b201be555821e932f6df5599eaa57"></a>

```c
enum hfp_hf_ag_indicators { HF_SERVICE_IND = 0 , HF_CALL_IND , HF_CALL_SETUP_IND , HF_CALL_HELD_IND , HF_SIGNAL_IND , HF_ROAM_IND , HF_BATTERY_IND }
```

相关声明：[hfp_hf_ag_indicators](#ga862b201be555821e932f6df5599eaa57)、[HF_SERVICE_IND](#gga862b201be555821e932f6df5599eaa57adb3fae0b3684e8d035e195a91d24deb8)、[HF_CALL_IND](#gga862b201be555821e932f6df5599eaa57ad8620b141e11f48b46b9cd5ef1842fe6)、[HF_CALL_SETUP_IND](#gga862b201be555821e932f6df5599eaa57a24ceb35eba4e18dbde198b77a7db98de)、[HF_CALL_HELD_IND](#gga862b201be555821e932f6df5599eaa57ad0cfee8ab087438502689d12cafa39cf)、[HF_SIGNAL_IND](#gga862b201be555821e932f6df5599eaa57ac5055465440ffe897930cbfdabb7c3d0)、[HF_ROAM_IND](#gga862b201be555821e932f6df5599eaa57a3f9c27a235db99073918a904d6902eae)、[HF_BATTERY_IND](#gga862b201be555821e932f6df5599eaa57a1444cacc3f0307e7b53a0375807668c5)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_ga2e4a7c05a3ba9a32eab50b9904f7f161"></a>

```c
int bt_hfp_hf_register (struct bt_hfp_hf_cb *cb)
```

相关声明：[bt_hfp_hf_register](#ga2e4a7c05a3ba9a32eab50b9904f7f161)、[bt_hfp_hf_cb](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md)。

注册免提配置文件的免提端（HFP HF）。

<a id="r_ga302e9ed397b056edef518470c6ea1d62"></a>

```c
int bt_hfp_hf_connect (struct bt_conn *conn, struct bt_hfp_hf **hf, uint8_t channel)
```

相关声明：[bt_hfp_hf_connect](#ga302e9ed397b056edef518470c6ea1d62)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发起服务级连接建立过程（Service Level Connection Establishment Procedure）。

<a id="r_gaf5e7ef119731c0dc35bec61fb7c34774"></a>

```c
int bt_hfp_hf_disconnect (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_disconnect](#gaf5e7ef119731c0dc35bec61fb7c34774)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

释放服务级连接（Service Level Connection）。

<a id="r_ga64ac1971dc7b1dacf6685bdc0c71e34c"></a>

```c
int bt_hfp_hf_cli (struct bt_hfp_hf *hf, bool enable)
```

相关声明：[bt_hfp_hf_cli](#ga64ac1971dc7b1dacf6685bdc0c71e34c)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

免提端（HF）启用／禁用主叫线路标识通知（Calling Line Identification Notification，CLI）。

<a id="r_ga0602cee7a90ca4afe90b65d748024472"></a>

```c
int bt_hfp_hf_vgm (struct bt_hfp_hf *hf, uint8_t gain)
```

相关声明：[bt_hfp_hf_vgm](#ga0602cee7a90ca4afe90b65d748024472)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提端（HF）报告麦克风增益（Gain of Microphone，VGM）。

<a id="r_ga0c1c35b3117f78f43a6300d4ff7dd18b"></a>

```c
int bt_hfp_hf_vgs (struct bt_hfp_hf *hf, uint8_t gain)
```

相关声明：[bt_hfp_hf_vgs](#ga0c1c35b3117f78f43a6300d4ff7dd18b)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提端（HF）报告扬声器增益（Gain of Speaker，VGS）。

<a id="r_gaaa9fbdceec140f274fc88c063a4cd4b8"></a>

```c
int bt_hfp_hf_get_operator (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_get_operator](#gaaa9fbdceec140f274fc88c063a4cd4b8)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）请求当前选定的运营商（Selected Operator）。

<a id="r_ga5bad80355fd7903abcee84437d399829"></a>

```c
int bt_hfp_hf_accept (struct bt_hfp_hf_call *call)
```

相关声明：[bt_hfp_hf_accept](#ga5bad80355fd7903abcee84437d399829)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）接听来电（Incoming Call）。

<a id="r_gac4e3d88b80b69840d52050dcd72c9ab3"></a>

```c
int bt_hfp_hf_reject (struct bt_hfp_hf_call *call)
```

相关声明：[bt_hfp_hf_reject](#gac4e3d88b80b69840d52050dcd72c9ab3)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）拒接来电（Incoming Call）。

<a id="r_gabbce5fbf0dec27e1c5a4da144fbfc9c1"></a>

```c
int bt_hfp_hf_terminate (struct bt_hfp_hf_call *call)
```

相关声明：[bt_hfp_hf_terminate](#gabbce5fbf0dec27e1c5a4da144fbfc9c1)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）终止来电（Incoming Call）。

<a id="r_ga540bf6ec23c632b3f736e6302ef32ebd"></a>

```c
int bt_hfp_hf_hold_incoming (struct bt_hfp_hf_call *call)
```

相关声明：[bt_hfp_hf_hold_incoming](#ga540bf6ec23c632b3f736e6302ef32ebd)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）将来电置于保持状态（On Hold）。

<a id="r_ga70e086f6a02cb116317a8e80f76abf6d"></a>

```c
int bt_hfp_hf_query_respond_hold_status (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_query_respond_hold_status](#ga70e086f6a02cb116317a8e80f76abf6d)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）查询音频网关（AG）的应答与保持状态（Respond and Hold Status）。

<a id="r_gac57d7188e3f8b6e1e28d2a55c2567dbf"></a>

```c
int bt_hfp_hf_number_call (struct bt_hfp_hf *hf, const char *number)
```

相关声明：[bt_hfp_hf_number_call](#gac57d7188e3f8b6e1e28d2a55c2567dbf)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）按电话号码拨号（Phone Number Call）。

<a id="r_gabacb666eb0f43db8614413a4ae0ce60a"></a>

```c
int bt_hfp_hf_memory_dial (struct bt_hfp_hf *hf, const char *location)
```

相关声明：[bt_hfp_hf_memory_dial](#gabacb666eb0f43db8614413a4ae0ce60a)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）使用存储号码拨号（Memory Dialing）。

<a id="r_ga9611012a35df66fac324b99b16e5d958"></a>

```c
int bt_hfp_hf_redial (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_redial](#ga9611012a35df66fac324b99b16e5d958)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）重拨最后一个号码（Redial Last Number）。

<a id="r_gad29bf40953faf638cc08acf919eb8f4f"></a>

```c
int bt_hfp_hf_audio_connect (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_audio_connect](#gad29bf40953faf638cc08acf919eb8f4f)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）建立音频连接（Audio Connection）。

<a id="r_ga34649dbecca2513c0b5bcd0e109b2551"></a>

```c
int bt_hfp_hf_select_codec (struct bt_hfp_hf *hf, uint8_t codec_id)
```

相关声明：[bt_hfp_hf_select_codec](#ga34649dbecca2513c0b5bcd0e109b2551)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提端（HF）设置选定的编解码器标识符（Codec ID）。

<a id="r_ga91fc2204f50df07567f87a2b7a18e69f"></a>

```c
int bt_hfp_hf_set_codecs (struct bt_hfp_hf *hf, uint8_t codec_ids)
```

相关声明：[bt_hfp_hf_set_codecs](#ga91fc2204f50df07567f87a2b7a18e69f)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提端（HF）设置支持的编解码器标识符（Codec IDs）。

<a id="r_ga7f37a9c009b4e55b7060d635c5b0c67b"></a>

```c
int bt_hfp_hf_turn_off_ecnr (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_turn_off_ecnr](#ga7f37a9c009b4e55b7060d635c5b0c67b)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）关闭音频网关（AG）的回声消除（EC）和降噪（NR）。

<a id="r_ga3afb0d82551708975dbeb9c903c3d1fb"></a>

```c
int bt_hfp_hf_call_waiting_notify (struct bt_hfp_hf *hf, bool enable)
```

相关声明：[bt_hfp_hf_call_waiting_notify](#ga3afb0d82551708975dbeb9c903c3d1fb)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

免提端（HF）启用／禁用呼叫等待通知（Call Waiting Notification）。

<a id="r_ga06e7e93578601693fa377a240e0d18a7"></a>

```c
int bt_hfp_hf_release_all_held (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_release_all_held](#ga06e7e93578601693fa377a240e0d18a7)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）释放所有保持中的呼叫（Held Calls）。

<a id="r_ga7389e5723e01b661b5e9c9d2114918b8"></a>

```c
int bt_hfp_hf_set_udub (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_set_udub](#ga7389e5723e01b661b5e9c9d2114918b8)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）为等待中的呼叫设置用户决定的用户忙（User Determined User Busy，UDUB）。

<a id="r_ga36be4ff5fd805c4413ba90b1f62b9143"></a>

```c
int bt_hfp_hf_release_active_accept_other (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_release_active_accept_other](#ga36be4ff5fd805c4413ba90b1f62b9143)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）释放所有活动呼叫（Active Calls）并接听另一呼叫。

<a id="r_ga40de46a6651eb85aa6d04ad66f528803"></a>

```c
int bt_hfp_hf_hold_active_accept_other (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_hold_active_accept_other](#ga40de46a6651eb85aa6d04ad66f528803)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）保持所有活动呼叫（Active Calls）并接听另一呼叫。

<a id="r_ga04d9fe3524c9522e98830507886bdfc6"></a>

```c
int bt_hfp_hf_join_conversation (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_join_conversation](#ga04d9fe3524c9522e98830507886bdfc6)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）将一个保持中的呼叫（Held Call）加入通话。

<a id="r_ga2b48a0938e65899417b2f3ab1fa4c548"></a>

```c
int bt_hfp_hf_explicit_call_transfer (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_explicit_call_transfer](#ga2b48a0938e65899417b2f3ab1fa4c548)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）执行显式呼叫转移（Explicit Call Transfer）。

<a id="r_ga1ad888c3b967d3f9b2e5ccee303b9ad7"></a>

```c
int bt_hfp_hf_release_specified_call (struct bt_hfp_hf_call *call)
```

相关声明：[bt_hfp_hf_release_specified_call](#ga1ad888c3b967d3f9b2e5ccee303b9ad7)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）释放指定索引（Index）的呼叫。

<a id="r_gac3c038818cda3645eaadc5374d18c3ee"></a>

```c
int bt_hfp_hf_private_consultation_mode (struct bt_hfp_hf_call *call)
```

相关声明：[bt_hfp_hf_private_consultation_mode](#gac3c038818cda3645eaadc5374d18c3ee)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）请求与指定呼叫进行私密磋商模式（Private Consultation Mode）。

<a id="r_gaeed952ce163ef2466ece04af24b76a28"></a>

```c
int bt_hfp_hf_voice_recognition (struct bt_hfp_hf *hf, bool activate)
```

相关声明：[bt_hfp_hf_voice_recognition](#gaeed952ce163ef2466ece04af24b76a28)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

免提端（HF）启用／禁用语音识别功能（Voice Recognition Function）。

<a id="r_ga3f6b43bf53fa04a6e71e883dc38f988b"></a>

```c
int bt_hfp_hf_ready_to_accept_audio (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_ready_to_accept_audio](#ga3f6b43bf53fa04a6e71e883dc38f988b)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）指示自身已准备好接收音频（Ready to Accept Audio）。

<a id="r_ga92d89b0b37186688e86091a7a8015245"></a>

```c
int bt_hfp_hf_request_phone_number (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_request_phone_number](#ga92d89b0b37186688e86091a7a8015245)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）为语音标签（Voice Tag）关联一个电话号码。

<a id="r_ga6a3a6bc61a3a74f5a4a48d7e39bd74a0"></a>

```c
int bt_hfp_hf_transmit_dtmf_code (struct bt_hfp_hf_call *call, char code)
```

相关声明：[bt_hfp_hf_transmit_dtmf_code](#ga6a3a6bc61a3a74f5a4a48d7e39bd74a0)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）发送指定的双音多频代码（DTMF Code）。

<a id="r_gad5dab4dcb66d52a80e0689a86de5fec3"></a>

```c
int bt_hfp_hf_query_subscriber (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_query_subscriber](#gad5dab4dcb66d52a80e0689a86de5fec3)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）查询用户号码信息（Subscriber Number Information）。

<a id="r_gab743d3e14fa13b71ddaf26d46cf41fb3"></a>

```c
int bt_hfp_hf_indicator_status (struct bt_hfp_hf *hf, uint8_t status)
```

相关声明：[bt_hfp_hf_indicator_status](#gab743d3e14fa13b71ddaf26d46cf41fb3)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提端（HF）设置音频网关指示器（AG Indicator）的激活／停用状态。

<a id="r_gab6710ce433812c3bf785b787008c36be"></a>

```c
int bt_hfp_hf_enhanced_safety (struct bt_hfp_hf *hf, bool enable)
```

相关声明：[bt_hfp_hf_enhanced_safety](#gab6710ce433812c3bf785b787008c36be)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

免提端（HF）启用／禁用增强安全功能（Enhanced Safety）。

<a id="r_ga2f0e6012503a9b59b03a0fb508d12f88"></a>

```c
int bt_hfp_hf_battery (struct bt_hfp_hf *hf, uint8_t level)
```

相关声明：[bt_hfp_hf_battery](#ga2f0e6012503a9b59b03a0fb508d12f88)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提端（HF）的剩余电池电量（Remaining Battery Level）。

<a id="r_ga91637662881dd655f8fc8ed6e6f8b973"></a>

```c
int bt_hfp_hf_query_list_of_current_calls (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_query_list_of_current_calls](#ga91637662881dd655f8fc8ed6e6f8b973)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）查询当前呼叫列表（List of Current Calls）。

## 2.5\_详细说明（Detailed Documentation）

<a id="ga0e46a981a70dcdecbae119ebb6d61aa0"></a>

### `BT_HFP_HF_CODEC_CVSD`

```c
#define BT_HFP_HF_CODEC_CVSD 0x01
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

<a id="gac8ab2e9ff6c8b9a06ac460f751dec1ad"></a>

### `BT_HFP_HF_CODEC_LC3_SWB`

```c
#define BT_HFP_HF_CODEC_LC3_SWB 0x03
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

<a id="gaea9fb177ae8ba32650dc93f1b2953333"></a>

### `BT_HFP_HF_CODEC_MSBC`

```c
#define BT_HFP_HF_CODEC_MSBC 0x02
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

<a id="ga6c2ba70d70c8f9d6d569662086985c85"></a>

### `bt_hfp_hf_call_dir`

```c
enum bt_hfp_hf_call_dir
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

通话方向（Call Direction）。

定义呼叫由免提单元（Hands-Free Unit，HF）发起（呼出，Outgoing），还是由远端发起（呼入，Incoming）的枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_HFP_HF_CALL_DIR_OUTGOING` | 由 HF 发起的呼出（Outgoing Call）。 |
| `BT_HFP_HF_CALL_DIR_INCOMING` | 来自远端的呼入（Incoming Call）。 |

<a id="ga38619377f146492993ee9a92a487af50"></a>

### `bt_hfp_hf_call_mode`

```c
enum bt_hfp_hf_call_mode
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

呼叫模式（Call Mode）。

定义正在建立的呼叫类型（Call Type）的枚举：语音、数据或传真传输。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_HFP_HF_CALL_MODE_VOICE` | 语音呼叫（Voice Call）。 |
| `BT_HFP_HF_CALL_MODE_DATA` | 数据呼叫（Data Call）。 |
| `BT_HFP_HF_CALL_MODE_FAX` | 传真传输（Fax Transmission）。 |

<a id="ga810c80de5baf92feb23650374b60bcee"></a>

### `bt_hfp_hf_call_status`

```c
enum bt_hfp_hf_call_status
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

通话状态（Call Status）。

定义 HF 与音频网关（Audio Gateway，AG）进行免提配置文件（Hands-Free Profile，HFP）通信时，呼叫可能处于的各种状态。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_HFP_HF_CALL_STATUS_ACTIVE` | 呼叫已激活且正在进行（Active and Ongoing）。 |
| `BT_HFP_HF_CALL_STATUS_HELD` | 通话处于保持状态（On Hold）。 |
| `BT_HFP_HF_CALL_STATUS_DIALING` | 去电正在拨号（Dialing）。 |
| `BT_HFP_HF_CALL_STATUS_ALERTING` | 呼出的呼叫正在提醒远端（Alerting，即远端振铃）。 |
| `BT_HFP_HF_CALL_STATUS_INCOMING` | 有呼入到达（Incoming Call）。 |
| `BT_HFP_HF_CALL_STATUS_WAITING` | 呼入正在等待（Call Waiting 场景）。 |
| `BT_HFP_HF_CALL_STATUS_INCOMING_HELD` | 呼叫被应答并保持功能（Response and Hold）保持。 |

<a id="ga862b201be555821e932f6df5599eaa57"></a>

### `hfp_hf_ag_indicators`

```c
enum hfp_hf_ag_indicators
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HF_SERVICE_IND` |  |
| `HF_CALL_IND` |  |
| `HF_CALL_SETUP_IND` |  |
| `HF_CALL_HELD_IND` |  |
| `HF_SIGNAL_IND` |  |
| `HF_ROAM_IND` |  |
| `HF_BATTERY_IND` |  |

<a id="ga5bad80355fd7903abcee84437d399829"></a>

### `bt_hfp_hf_accept()`

```c
int bt_hfp_hf_accept ( struct bt_hfp_hf_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）接听来电（Incoming Call）。

发送 `ATA` 命令接听呼入；或发送 `AT+BTRH=1` 命令，接听被保持的呼入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

**说明（Note）**：注（Note）：有多个呼叫正在进行时不能使用。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gad29bf40953faf638cc08acf919eb8f4f"></a>

### `bt_hfp_hf_audio_connect()`

```c
int bt_hfp_hf_audio_connect ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）建立音频连接（Audio Connection）。

若双方均支持编解码器协商（Codec Negotiation），则发送 `AT+BCC` 建立音频连接；否则直接初始化同步面向连接（SCO）的音频连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga2f0e6012503a9b59b03a0fb508d12f88"></a>

### `bt_hfp_hf_battery()`

```c
int bt_hfp_hf_battery ( struct bt_hfp_hf * hf, uint8_t level )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）的剩余电池电量（Remaining Battery Level）。

允许 HF 传送 HF 指示器（HF Indicator）的剩余电量值。未启用 `CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `level` | 剩余电池电量（Remaining Battery Level）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga3afb0d82551708975dbeb9c903c3d1fb"></a>

### `bt_hfp_hf_call_waiting_notify()`

```c
int bt_hfp_hf_call_waiting_notify ( struct bt_hfp_hf * hf, bool enable )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）启用／禁用呼叫等待通知（Call Waiting Notification）。

发送 `AT+CCWA=1` 启用呼叫等待通知（Call Waiting Notification），发送 `AT+CCWA=0` 禁用它。未启用 `CONFIG_BT_HFP_HF_3WAY_CALL` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `enable` | 启用／禁用（Enable/Disable）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga64ac1971dc7b1dacf6685bdc0c71e34c"></a>

### `bt_hfp_hf_cli()`

```c
int bt_hfp_hf_cli ( struct bt_hfp_hf * hf, bool enable )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）启用／禁用主叫线路标识通知（Calling Line Identification Notification，CLI）。

启用或禁用主叫线路标识通知（Calling Line Identification，CLI）。调用此函数时，将向 AG 发送 `AT+CLIP` 命令，以启用或禁用 CLI 非请求结果码（Unsolicited Result Code）`+CLIP`。未启用 `CONFIG_BT_HFP_HF_CLI` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `enable` | 启用／禁用主叫线路标识（CLI）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga302e9ed397b056edef518470c6ea1d62"></a>

### `bt_hfp_hf_connect()`

```c
int bt_hfp_hf_connect ( struct bt_conn * conn, struct bt_hfp_hf ** hf, uint8_t channel )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

发起服务级连接建立过程（Service Level Connection Establishment Procedure）。

在参数 `conn` 指定的 ACL 连接上，使用 `bt_br_discovery_start` 发现的特定 RFCOMM 通道，启动服务级连接（Service Level Connection）的建立流程。

参数 `hf` 是输出参数。若服务级连接建立流程成功启动且没有错误，则分配 HFP HF 对象；若 `hf` 不是 `NULL` 指针，将通过该参数返回对象。

服务级连接（Service Level Connection）建立后，触发已注册的 `connected` 回调，通知应用建立流程已完成；此时 HFP HF 对象才有效。这意味着，即使此函数调用没有错误，也必须等到已注册的 `connected` 回调触发后，才能调用 HFP HF 提供的所有接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | ACL 连接对象（Connection Object）。 |
| `hf` | 创建的 HFP HF 对象。 |
| `channel` | 要连接的对等端 RFCOMM 通道。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaf5e7ef119731c0dc35bec61fb7c34774"></a>

### `bt_hfp_hf_disconnect()`

```c
int bt_hfp_hf_disconnect ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

释放服务级连接（Service Level Connection）。

释放与对等设备的服务级连接（Service Level Connection）。

只能在已注册的 `connected` 回调触发后调用此函数。

若此函数调用没有错误，HFP HF 对象此时即失效，不应再调用 HFP HF 提供的任何接口。

服务级连接（Service Level Connection）释放后，触发已注册的 `disconnected` 回调，通知应用释放流程已完成。HFP HF 对象将在该回调返回后释放。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gab6710ce433812c3bf785b787008c36be"></a>

### `bt_hfp_hf_enhanced_safety()`

```c
int bt_hfp_hf_enhanced_safety ( struct bt_hfp_hf * hf, bool enable )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）启用／禁用增强安全功能（Enhanced Safety）。

允许 HF 传送 HF 指示器（HF Indicator）的增强安全值（Enhanced Safety Value）。未启用 `CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `enable` | 增强安全（Enhanced Safety）已启用／禁用。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga2b48a0938e65899417b2f3ab1fa4c548"></a>

### `bt_hfp_hf_explicit_call_transfer()`

```c
int bt_hfp_hf_explicit_call_transfer ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）执行显式呼叫转移（Explicit Call Transfer）。

发送 `AT+CHLD=4`，将两个呼叫接通并使本用户退出这两个呼叫，即显式呼叫转移（Explicit Call Transfer）。未启用 `CONFIG_BT_HFP_HF_3WAY_CALL` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaaa9fbdceec140f274fc88c063a4cd4b8"></a>

### `bt_hfp_hf_get_operator()`

```c
int bt_hfp_hf_get_operator ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）请求当前选定的运营商（Selected Operator）。

发送 `AT+COPS?` 读取命令，查询当前选定的运营商（Operator）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga40de46a6651eb85aa6d04ad66f528803"></a>

### `bt_hfp_hf_hold_active_accept_other()`

```c
int bt_hfp_hf_hold_active_accept_other ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）保持所有活动呼叫（Active Calls）并接听另一呼叫。

发送 `AT+CHLD=2`，保持所有活动呼叫（如有），并接听另一个被保持或等待中的呼叫。未启用 `CONFIG_BT_HFP_HF_3WAY_CALL` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga540bf6ec23c632b3f736e6302ef32ebd"></a>

### `bt_hfp_hf_hold_incoming()`

```c
int bt_hfp_hf_hold_incoming ( struct bt_hfp_hf_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）将来电置于保持状态（On Hold）。

发送 `AT+BTRH=0`，将呼入置于保持（Hold）状态。呼入被保持后，将触发 `on_hold` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

**说明（Note）**：注（Note）：有多个呼叫正在进行时不能使用。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gab743d3e14fa13b71ddaf26d46cf41fb3"></a>

### `bt_hfp_hf_indicator_status()`

```c
int bt_hfp_hf_indicator_status ( struct bt_hfp_hf * hf, uint8_t status )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）设置音频网关指示器（AG Indicator）的激活／停用状态。

允许 HF 发送 `AT+BIA` 命令，以更改 AG 中指示器的激活／停用状态。可激活或停用的所有指示器索引定义在 `enum hfp_hf_ag_indicators` 中。参数 `status` 的每一位表示对应索引的指示器状态。例如，`status` 为 `0b111110` 表示要求停用 AG 的 `service` 指示器，并激活其他指示器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `status` | AG 指示器激活／停用状态的位图（Bitmap）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga04d9fe3524c9522e98830507886bdfc6"></a>

### `bt_hfp_hf_join_conversation()`

```c
int bt_hfp_hf_join_conversation ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）将一个保持中的呼叫（Held Call）加入通话。

发送 `AT+CHLD=3`，将被保持的呼叫加入通话。未启用 `CONFIG_BT_HFP_HF_3WAY_CALL` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gabacb666eb0f43db8614413a4ae0ce60a"></a>

### `bt_hfp_hf_memory_dial()`

```c
int bt_hfp_hf_memory_dial ( struct bt_hfp_hf * hf, const char * location )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）使用存储号码拨号（Memory Dialing）。

使用 AG 的存储拨号功能（Memory Dialing）发起语音呼出。发送 `ATD>nnn...;` 命令开始存储拨号。命令结果通过 `dialing` 回调通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `location` | 存储位置（Memory Location）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gac57d7188e3f8b6e1e28d2a55c2567dbf"></a>

### `bt_hfp_hf_number_call()`

```c
int bt_hfp_hf_number_call ( struct bt_hfp_hf * hf, const char * number )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）按电话号码拨号（Phone Number Call）。

向 AG 提供目标电话号码，以发起语音呼出。发送 `ATDdd...dd;` 命令开始拨打电话号码。命令结果通过 `dialing` 回调通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `number` | 电话号码（Phone Number）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gac3c038818cda3645eaadc5374d18c3ee"></a>

### `bt_hfp_hf_private_consultation_mode()`

```c
int bt_hfp_hf_private_consultation_mode ( struct bt_hfp_hf_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）请求与指定呼叫进行私密磋商模式（Private Consultation Mode）。

发送 `AT+CHLD=2<idx>`，请求与指定呼叫进入私密通话模式（Private Consultation Mode）：保持除 `<idx>` 指定呼叫以外的所有呼叫。`<idx>` 是指定呼叫的索引。未启用 `CONFIG_BT_HFP_HF_ECC` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga91637662881dd655f8fc8ed6e6f8b973"></a>

### `bt_hfp_hf_query_list_of_current_calls()`

```c
int bt_hfp_hf_query_list_of_current_calls ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）查询当前呼叫列表（List of Current Calls）。

允许 HF 发送 `AT+CLCC` 命令，查询当前呼叫列表（List of Current Calls）。未启用 `CONFIG_BT_HFP_HF_ECS` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga70e086f6a02cb116317a8e80f76abf6d"></a>

### `bt_hfp_hf_query_respond_hold_status()`

```c
int bt_hfp_hf_query_respond_hold_status ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）查询音频网关（AG）的应答与保持状态（Respond and Hold Status）。

发送 `AT+BTRH?` 命令，查询 AG 的应答并保持状态（Respond and Hold Status）。该状态通过 `on_hold` 回调通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gad5dab4dcb66d52a80e0689a86de5fec3"></a>

### `bt_hfp_hf_query_subscriber()`

```c
int bt_hfp_hf_query_subscriber ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）查询用户号码信息（Subscriber Number Information）。

允许 HF 发送 `AT+CNUM`，查询 AG 的用户号码（Subscriber Number）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga3f6b43bf53fa04a6e71e883dc38f988b"></a>

### `bt_hfp_hf_ready_to_accept_audio()`

```c
int bt_hfp_hf_ready_to_accept_audio ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）指示自身已准备好接收音频（Ready to Accept Audio）。

此值表示初次建立音频连接（Audio Connection）时，HF 已准备好接收音频。HF 仅应在 eSCO 链路建立后发送此值。未启用 `CONFIG_BT_HFP_HF_ENH_VOICE_RECG` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga9611012a35df66fac324b99b16e5d958"></a>

### `bt_hfp_hf_redial()`

```c
int bt_hfp_hf_redial ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）重拨最后一个号码（Redial Last Number）。

重拨 AG 最后拨出的号码，以发起语音呼出。发送 `AT+BLDN` 命令重拨最后一个号码。命令结果通过 `dialing` 回调通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga2e4a7c05a3ba9a32eab50b9904f7f161"></a>

### `bt_hfp_hf_register()`

```c
int bt_hfp_hf_register ( struct bt_hfp_hf_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

注册免提配置文件的免提端（HFP HF）。

注册免提配置文件（Hands-Free Profile）回调，以监视状态并获取显示所需的 HFP 详细信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gac4e3d88b80b69840d52050dcd72c9ab3"></a>

### `bt_hfp_hf_reject()`

```c
int bt_hfp_hf_reject ( struct bt_hfp_hf_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）拒接来电（Incoming Call）。

发送 `AT+CHUP` 命令拒接呼入；或发送 `AT+BTRH=2` 命令，拒接被保持的呼入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

**说明（Note）**：注（Note）：有多个呼叫正在进行时不能使用。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga36be4ff5fd805c4413ba90b1f62b9143"></a>

### `bt_hfp_hf_release_active_accept_other()`

```c
int bt_hfp_hf_release_active_accept_other ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）释放所有活动呼叫（Active Calls）并接听另一呼叫。

发送 `AT+CHLD=1`，释放所有活动呼叫（如有），并接听另一个被保持或等待中的呼叫。未启用 `CONFIG_BT_HFP_HF_3WAY_CALL` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga06e7e93578601693fa377a240e0d18a7"></a>

### `bt_hfp_hf_release_all_held()`

```c
int bt_hfp_hf_release_all_held ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）释放所有保持中的呼叫（Held Calls）。

发送 `AT+CHLD=0`，释放所有被保持的呼叫。未启用 `CONFIG_BT_HFP_HF_3WAY_CALL` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga1ad888c3b967d3f9b2e5ccee303b9ad7"></a>

### `bt_hfp_hf_release_specified_call()`

```c
int bt_hfp_hf_release_specified_call ( struct bt_hfp_hf_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）释放指定索引（Index）的呼叫。

发送 `AT+CHLD=1<idx>`，释放指定索引的呼叫。`<idx>` 是指定呼叫的索引。未启用 `CONFIG_BT_HFP_HF_ECC` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga92d89b0b37186688e86091a7a8015245"></a>

### `bt_hfp_hf_request_phone_number()`

```c
int bt_hfp_hf_request_phone_number ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）为语音标签（Voice Tag）关联一个电话号码。

发送 AT 命令 `AT+BINP=1`，向 AG 请求电话号码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga34649dbecca2513c0b5bcd0e109b2551"></a>

### `bt_hfp_hf_select_codec()`

```c
int bt_hfp_hf_select_codec ( struct bt_hfp_hf * hf, uint8_t codec_id )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）设置选定的编解码器标识符（Codec ID）。

发送 `AT+BCS` 设置选定的编解码器 ID（Codec ID）。此函数用于响应 `codec_negotiate` 回调通知的编解码器协商请求。若支持回调提供的 ID，参数 `codec_id` 应与之相同；否则应调用 `bt_hfp_hf_set_codecs`，通知 AG 当前 HFP HF 支持的编解码器 ID。未启用 `CONFIG_BT_HFP_HF_CODEC_NEG` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `codec_id` | 选定的编解码器 ID（Codec ID）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga91fc2204f50df07567f87a2b7a18e69f"></a>

### `bt_hfp_hf_set_codecs()`

```c
int bt_hfp_hf_set_codecs ( struct bt_hfp_hf * hf, uint8_t codec_ids )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）设置支持的编解码器标识符（Codec IDs）。

发送 `AT+BAC` 设置支持的编解码器 ID（Codec IDs）。此函数用于通知 AG 当前 HF 支持的编解码器 ID。未启用 `CONFIG_BT_HFP_HF_CODEC_NEG` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `codec_ids` | 支持的编解码器 ID（Codec IDs）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga7389e5723e01b661b5e9c9d2114918b8"></a>

### `bt_hfp_hf_set_udub()`

```c
int bt_hfp_hf_set_udub ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）为等待中的呼叫设置用户决定的用户忙（User Determined User Busy，UDUB）。

发送 `AT+CHLD=0`，为等待中的呼叫设置用户判定忙（User Determined User Busy，UDUB）。未启用 `CONFIG_BT_HFP_HF_3WAY_CALL` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gabbce5fbf0dec27e1c5a4da144fbfc9c1"></a>

### `bt_hfp_hf_terminate()`

```c
int bt_hfp_hf_terminate ( struct bt_hfp_hf_call * call)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）终止来电（Incoming Call）。

发送 `AT+CHUP` 命令终止呼入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

**说明（Note）**：注（Note）：有多个呼叫正在进行时不能使用。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga6a3a6bc61a3a74f5a4a48d7e39bd74a0"></a>

### `bt_hfp_hf_transmit_dtmf_code()`

```c
int bt_hfp_hf_transmit_dtmf_code ( struct bt_hfp_hf_call * call, char code )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）发送指定的双音多频代码（DTMF Code）。

通话期间，HF 发送 `AT+VTS` 命令，指示 AG 向其网络连接发送指定的双音多频（DTMF）码。码值集合为 `0-9,#,*,A-D`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |
| `code` | 指定的双音多频代码（DTMF code）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga7f37a9c009b4e55b7060d635c5b0c67b"></a>

### `bt_hfp_hf_turn_off_ecnr()`

```c
int bt_hfp_hf_turn_off_ecnr ( struct bt_hfp_hf * hf)
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）关闭音频网关（AG）的回声消除（EC）和降噪（NR）。

发送 `AT+NREC=0` 关闭 AG 的回声消除（EC）和降噪（NR）。命令结果通过 `ecnr_turn_off` 回调通知。未启用 `CONFIG_BT_HFP_HF_ECNR` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga0602cee7a90ca4afe90b65d748024472"></a>

### `bt_hfp_hf_vgm()`

```c
int bt_hfp_hf_vgm ( struct bt_hfp_hf * hf, uint8_t gain )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）报告麦克风增益（Gain of Microphone，VGM）。

报告麦克风增益（Gain of Microphone，VGM）。向 AG 发送 AT 命令 `AT+VGM=<gain>`，报告 HF 当前的麦克风增益级别设置。`<gain>` 是十进制数值常量，对应 HF 控制的特定音量级别，具体映射取决于实现。此命令不更改 AG 的麦克风增益，仅表示 HF 当前的麦克风增益值。未启用 `CONFIG_BT_HFP_HF_VOLUME` 时，调用此函数将返回错误 `-ENOTSUP`。为实现音量级别同步（Volume Level Synchronization），HF 应用可在 HF 连接回调中调用此函数设置 VGM 增益值；回调返回后，VGM 增益将发送给 HFP AG。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `gain` | 麦克风增益（Gain of Microphone）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga0c1c35b3117f78f43a6300d4ff7dd18b"></a>

### `bt_hfp_hf_vgs()`

```c
int bt_hfp_hf_vgs ( struct bt_hfp_hf * hf, uint8_t gain )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）报告扬声器增益（Gain of Speaker，VGS）。

报告扬声器增益（Gain of Speaker，VGS）。向 AG 发送 AT 命令 `AT+VGS=<gain>`，报告 HF 当前的扬声器增益级别设置。`<gain>` 是十进制数值常量，对应 HF 控制的特定音量级别，具体映射取决于实现。此命令不更改 AG 的扬声器增益，仅表示 HF 当前的扬声器增益值。未启用 `CONFIG_BT_HFP_HF_VOLUME` 时，调用此函数将返回错误 `-ENOTSUP`。为实现音量级别同步（Volume Level Synchronization），HF 应用可在 HF 连接回调中调用此函数设置 VGS 增益值；回调返回后，VGS 增益将发送给 HFP AG。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `gain` | 扬声器增益（Gain of Speaker）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaeed952ce163ef2466ece04af24b76a28"></a>

### `bt_hfp_hf_voice_recognition()`

```c
int bt_hfp_hf_voice_recognition ( struct bt_hfp_hf * hf, bool activate )
```

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

免提端（HF）启用／禁用语音识别功能（Voice Recognition Function）。

启用／禁用 AG 的语音识别功能（Voice Recognition）。未启用 `CONFIG_BT_HFP_HF_VOICE_RECG` 时，调用此函数将返回错误 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `activate` | 激活／停用语音识别功能（Voice Recognition）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。


## 2.6\_原页交叉引用（Cross References）

- [bt_hfp_hf_current_call](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md)
- [bt_hfp_hf_cb](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md)
- [bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)
- [bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/bluetooth/classic/hfp_hf.h](../api_file_flash_test_reference/P004_zephyr__bluetooth__classic__hfp_hf.h_文件参考.md)
- [CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [CONFIG_BT_HFP_HF_3WAY_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_3WAY_CALL)
- [CONFIG_BT_HFP_HF_CLI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_CLI)
- [bt_br_discovery_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9760190192dde5c498ec96628468be8d)
- [CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY)
- [CONFIG_BT_HFP_HF_ECC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_ECC)
- [CONFIG_BT_HFP_HF_ECS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_ECS)
- [CONFIG_BT_HFP_HF_ENH_VOICE_RECG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_ENH_VOICE_RECG)
- [CONFIG_BT_HFP_HF_CODEC_NEG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_CODEC_NEG)
- [CONFIG_BT_HFP_HF_ECNR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_ECNR)
- [CONFIG_BT_HFP_HF_VOLUME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_VOLUME)
- [CONFIG_BT_HFP_HF_VOICE_RECG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_VOICE_RECG)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga6c2ba70d70c8f9d6d569662086985c85aa631c2cc079db31712ac2ec7ac3dee3f"></a>
<a id="gga6c2ba70d70c8f9d6d569662086985c85adf30d13bccb711d32a3c75e5c1d47d97"></a>
<a id="gga38619377f146492993ee9a92a487af50ac2233c577a6d8b8871b8e31969616f66"></a>
<a id="gga38619377f146492993ee9a92a487af50a5a35798fc921e975775c496ac49193c9"></a>
<a id="gga38619377f146492993ee9a92a487af50a646f51233cf8906d377bf0d6860f3bb0"></a>
<a id="gga810c80de5baf92feb23650374b60bceea1ea1ba685375baaabab22ad1c01ca6af"></a>
<a id="gga810c80de5baf92feb23650374b60bceeab4db9c2eb21b5eb79517c0a761bc7dfa"></a>
<a id="gga810c80de5baf92feb23650374b60bceea9ff342787f8a6f7b9a5c0db1afa1bfb9"></a>
<a id="gga810c80de5baf92feb23650374b60bceea7377bf80fd685178d0d8b39189b2122a"></a>
<a id="gga810c80de5baf92feb23650374b60bceea8f8fc15f39de43b1ed202e16cd198104"></a>
<a id="gga810c80de5baf92feb23650374b60bceea974da5247c5d332b11c42e93c9cbd831"></a>
<a id="gga810c80de5baf92feb23650374b60bceeabfa959b76eab9fc14ae941e3c1cd45ff"></a>
<a id="gga862b201be555821e932f6df5599eaa57adb3fae0b3684e8d035e195a91d24deb8"></a>
<a id="gga862b201be555821e932f6df5599eaa57ad8620b141e11f48b46b9cd5ef1842fe6"></a>
<a id="gga862b201be555821e932f6df5599eaa57a24ceb35eba4e18dbde198b77a7db98de"></a>
<a id="gga862b201be555821e932f6df5599eaa57ad0cfee8ab087438502689d12cafa39cf"></a>
<a id="gga862b201be555821e932f6df5599eaa57ac5055465440ffe897930cbfdabb7c3d0"></a>
<a id="gga862b201be555821e932f6df5599eaa57a3f9c27a235db99073918a904d6902eae"></a>
<a id="gga862b201be555821e932f6df5599eaa57a1444cacc3f0307e7b53a0375807668c5"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_基本音频配置文件（Basic Audio Profile，BAP）的 LC3 预设.md) · [返回大纲](大纲.md) · [下一章](P003_配网（Provisioning）.md)
