---
id: learning.zephyr-docs.api-file-flash-test-reference.page-4
title: zephyr__bluetooth__classic__hfp_hf.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hfp__hf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_bluetooth\_\_classic\_\_hfp\_hf.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hfp__hf_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

免提配置文件（Handsfree Profile）的处理。

<a id="details"></a>

```c
#include <zephyr/bluetooth/bluetooth.h>
```

查看此文件的源码。

免提配置文件（Handsfree Profile）的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga0e46a981a70dcdecbae119ebb6d61aa0"></a>

```c
#define BT_HFP_HF_CODEC_CVSD 0x01
```

相关声明：[BT_HFP_HF_CODEC_CVSD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga0e46a981a70dcdecbae119ebb6d61aa0)。

<a id="r_gaea9fb177ae8ba32650dc93f1b2953333"></a>

```c
#define BT_HFP_HF_CODEC_MSBC 0x02
```

相关声明：[BT_HFP_HF_CODEC_MSBC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gaea9fb177ae8ba32650dc93f1b2953333)。

<a id="r_gac8ab2e9ff6c8b9a06ac460f751dec1ad"></a>

```c
#define BT_HFP_HF_CODEC_LC3_SWB 0x03
```

相关声明：[BT_HFP_HF_CODEC_LC3_SWB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gac8ab2e9ff6c8b9a06ac460f751dec1ad)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.3\_枚举（Enumerations）

<a id="r_ga810c80de5baf92feb23650374b60bcee"></a>

```c
enum bt_hfp_hf_call_status { BT_HFP_HF_CALL_STATUS_ACTIVE = 0 , BT_HFP_HF_CALL_STATUS_HELD = 1 , BT_HFP_HF_CALL_STATUS_DIALING = 2 , BT_HFP_HF_CALL_STATUS_ALERTING = 3 , BT_HFP_HF_CALL_STATUS_INCOMING = 4 , BT_HFP_HF_CALL_STATUS_WAITING = 5 , BT_HFP_HF_CALL_STATUS_INCOMING_HELD = 6 }
```

相关声明：[bt_hfp_hf_call_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga810c80de5baf92feb23650374b60bcee)、[BT_HFP_HF_CALL_STATUS_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea1ea1ba685375baaabab22ad1c01ca6af)、[BT_HFP_HF_CALL_STATUS_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceeab4db9c2eb21b5eb79517c0a761bc7dfa)、[BT_HFP_HF_CALL_STATUS_DIALING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea9ff342787f8a6f7b9a5c0db1afa1bfb9)、[BT_HFP_HF_CALL_STATUS_ALERTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea7377bf80fd685178d0d8b39189b2122a)、[BT_HFP_HF_CALL_STATUS_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea8f8fc15f39de43b1ed202e16cd198104)、[BT_HFP_HF_CALL_STATUS_WAITING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea974da5247c5d332b11c42e93c9cbd831)、[BT_HFP_HF_CALL_STATUS_INCOMING_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceeabfa959b76eab9fc14ae941e3c1cd45ff)。

通话状态（Call Status）。

<a id="r_ga6c2ba70d70c8f9d6d569662086985c85"></a>

```c
enum bt_hfp_hf_call_dir { BT_HFP_HF_CALL_DIR_OUTGOING = 0 , BT_HFP_HF_CALL_DIR_INCOMING = 1 }
```

相关声明：[bt_hfp_hf_call_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga6c2ba70d70c8f9d6d569662086985c85)、[BT_HFP_HF_CALL_DIR_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga6c2ba70d70c8f9d6d569662086985c85aa631c2cc079db31712ac2ec7ac3dee3f)、[BT_HFP_HF_CALL_DIR_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga6c2ba70d70c8f9d6d569662086985c85adf30d13bccb711d32a3c75e5c1d47d97)。

通话方向（Call Direction）。

<a id="r_ga38619377f146492993ee9a92a487af50"></a>

```c
enum bt_hfp_hf_call_mode { BT_HFP_HF_CALL_MODE_VOICE = 0 , BT_HFP_HF_CALL_MODE_DATA = 1 , BT_HFP_HF_CALL_MODE_FAX = 2 }
```

相关声明：[bt_hfp_hf_call_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga38619377f146492993ee9a92a487af50)、[BT_HFP_HF_CALL_MODE_VOICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga38619377f146492993ee9a92a487af50ac2233c577a6d8b8871b8e31969616f66)、[BT_HFP_HF_CALL_MODE_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga38619377f146492993ee9a92a487af50a5a35798fc921e975775c496ac49193c9)、[BT_HFP_HF_CALL_MODE_FAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga38619377f146492993ee9a92a487af50a646f51233cf8906d377bf0d6860f3bb0)。

呼叫模式（Call Mode）。

<a id="r_ga862b201be555821e932f6df5599eaa57"></a>

```c
enum hfp_hf_ag_indicators { HF_SERVICE_IND = 0 , HF_CALL_IND , HF_CALL_SETUP_IND , HF_CALL_HELD_IND , HF_SIGNAL_IND , HF_ROAM_IND , HF_BATTERY_IND }
```

相关声明：[hfp_hf_ag_indicators](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga862b201be555821e932f6df5599eaa57)、[HF_SERVICE_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57adb3fae0b3684e8d035e195a91d24deb8)、[HF_CALL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57ad8620b141e11f48b46b9cd5ef1842fe6)、[HF_CALL_SETUP_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57a24ceb35eba4e18dbde198b77a7db98de)、[HF_CALL_HELD_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57ad0cfee8ab087438502689d12cafa39cf)、[HF_SIGNAL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57ac5055465440ffe897930cbfdabb7c3d0)、[HF_ROAM_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57a3f9c27a235db99073918a904d6902eae)、[HF_BATTERY_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57a1444cacc3f0307e7b53a0375807668c5)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_ga2e4a7c05a3ba9a32eab50b9904f7f161"></a>

```c
int bt_hfp_hf_register (struct bt_hfp_hf_cb *cb)
```

相关声明：[bt_hfp_hf_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga2e4a7c05a3ba9a32eab50b9904f7f161)、[bt_hfp_hf_cb](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md)。

注册免提配置文件的免提端（HFP HF）。

<a id="r_ga302e9ed397b056edef518470c6ea1d62"></a>

```c
int bt_hfp_hf_connect (struct bt_conn *conn, struct bt_hfp_hf **hf, uint8_t channel)
```

相关声明：[bt_hfp_hf_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga302e9ed397b056edef518470c6ea1d62)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发起服务级连接建立过程（Service Level Connection Establishment Procedure）。

<a id="r_gaf5e7ef119731c0dc35bec61fb7c34774"></a>

```c
int bt_hfp_hf_disconnect (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gaf5e7ef119731c0dc35bec61fb7c34774)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

释放服务级连接（Service Level Connection）。

<a id="r_ga64ac1971dc7b1dacf6685bdc0c71e34c"></a>

```c
int bt_hfp_hf_cli (struct bt_hfp_hf *hf, bool enable)
```

相关声明：[bt_hfp_hf_cli](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga64ac1971dc7b1dacf6685bdc0c71e34c)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

免提端（HF）启用／禁用主叫线路标识通知（Calling Line Identification Notification，CLI）。

<a id="r_ga0602cee7a90ca4afe90b65d748024472"></a>

```c
int bt_hfp_hf_vgm (struct bt_hfp_hf *hf, uint8_t gain)
```

相关声明：[bt_hfp_hf_vgm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga0602cee7a90ca4afe90b65d748024472)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提端（HF）报告麦克风增益（Gain of Microphone，VGM）。

<a id="r_ga0c1c35b3117f78f43a6300d4ff7dd18b"></a>

```c
int bt_hfp_hf_vgs (struct bt_hfp_hf *hf, uint8_t gain)
```

相关声明：[bt_hfp_hf_vgs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga0c1c35b3117f78f43a6300d4ff7dd18b)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提端（HF）报告扬声器增益（Gain of Speaker，VGS）。

<a id="r_gaaa9fbdceec140f274fc88c063a4cd4b8"></a>

```c
int bt_hfp_hf_get_operator (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_get_operator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gaaa9fbdceec140f274fc88c063a4cd4b8)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）请求当前选定的运营商（Selected Operator）。

<a id="r_ga5bad80355fd7903abcee84437d399829"></a>

```c
int bt_hfp_hf_accept (struct bt_hfp_hf_call *call)
```

相关声明：[bt_hfp_hf_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga5bad80355fd7903abcee84437d399829)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）接听来电（Incoming Call）。

<a id="r_gac4e3d88b80b69840d52050dcd72c9ab3"></a>

```c
int bt_hfp_hf_reject (struct bt_hfp_hf_call *call)
```

相关声明：[bt_hfp_hf_reject](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gac4e3d88b80b69840d52050dcd72c9ab3)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）拒接来电（Incoming Call）。

<a id="r_gabbce5fbf0dec27e1c5a4da144fbfc9c1"></a>

```c
int bt_hfp_hf_terminate (struct bt_hfp_hf_call *call)
```

相关声明：[bt_hfp_hf_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gabbce5fbf0dec27e1c5a4da144fbfc9c1)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）终止来电（Incoming Call）。

<a id="r_ga540bf6ec23c632b3f736e6302ef32ebd"></a>

```c
int bt_hfp_hf_hold_incoming (struct bt_hfp_hf_call *call)
```

相关声明：[bt_hfp_hf_hold_incoming](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga540bf6ec23c632b3f736e6302ef32ebd)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）将来电置于保持状态（On Hold）。

<a id="r_ga70e086f6a02cb116317a8e80f76abf6d"></a>

```c
int bt_hfp_hf_query_respond_hold_status (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_query_respond_hold_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga70e086f6a02cb116317a8e80f76abf6d)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）查询音频网关（AG）的应答与保持状态（Respond and Hold Status）。

<a id="r_gac57d7188e3f8b6e1e28d2a55c2567dbf"></a>

```c
int bt_hfp_hf_number_call (struct bt_hfp_hf *hf, const char *number)
```

相关声明：[bt_hfp_hf_number_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gac57d7188e3f8b6e1e28d2a55c2567dbf)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）按电话号码拨号（Phone Number Call）。

<a id="r_gabacb666eb0f43db8614413a4ae0ce60a"></a>

```c
int bt_hfp_hf_memory_dial (struct bt_hfp_hf *hf, const char *location)
```

相关声明：[bt_hfp_hf_memory_dial](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gabacb666eb0f43db8614413a4ae0ce60a)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）使用存储号码拨号（Memory Dialing）。

<a id="r_ga9611012a35df66fac324b99b16e5d958"></a>

```c
int bt_hfp_hf_redial (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_redial](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga9611012a35df66fac324b99b16e5d958)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）重拨最后一个号码（Redial Last Number）。

<a id="r_gad29bf40953faf638cc08acf919eb8f4f"></a>

```c
int bt_hfp_hf_audio_connect (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_audio_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gad29bf40953faf638cc08acf919eb8f4f)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）建立音频连接（Audio Connection）。

<a id="r_ga34649dbecca2513c0b5bcd0e109b2551"></a>

```c
int bt_hfp_hf_select_codec (struct bt_hfp_hf *hf, uint8_t codec_id)
```

相关声明：[bt_hfp_hf_select_codec](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga34649dbecca2513c0b5bcd0e109b2551)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提端（HF）设置选定的编解码器标识符（Codec ID）。

<a id="r_ga91fc2204f50df07567f87a2b7a18e69f"></a>

```c
int bt_hfp_hf_set_codecs (struct bt_hfp_hf *hf, uint8_t codec_ids)
```

相关声明：[bt_hfp_hf_set_codecs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga91fc2204f50df07567f87a2b7a18e69f)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提端（HF）设置支持的编解码器标识符（Codec IDs）。

<a id="r_ga7f37a9c009b4e55b7060d635c5b0c67b"></a>

```c
int bt_hfp_hf_turn_off_ecnr (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_turn_off_ecnr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga7f37a9c009b4e55b7060d635c5b0c67b)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）关闭音频网关（AG）的回声消除（EC）和降噪（NR）。

<a id="r_ga3afb0d82551708975dbeb9c903c3d1fb"></a>

```c
int bt_hfp_hf_call_waiting_notify (struct bt_hfp_hf *hf, bool enable)
```

相关声明：[bt_hfp_hf_call_waiting_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga3afb0d82551708975dbeb9c903c3d1fb)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

免提端（HF）启用／禁用呼叫等待通知（Call Waiting Notification）。

<a id="r_ga06e7e93578601693fa377a240e0d18a7"></a>

```c
int bt_hfp_hf_release_all_held (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_release_all_held](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga06e7e93578601693fa377a240e0d18a7)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）释放所有保持中的呼叫（Held Calls）。

<a id="r_ga7389e5723e01b661b5e9c9d2114918b8"></a>

```c
int bt_hfp_hf_set_udub (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_set_udub](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga7389e5723e01b661b5e9c9d2114918b8)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）为等待中的呼叫设置用户决定的用户忙（User Determined User Busy，UDUB）。

<a id="r_ga36be4ff5fd805c4413ba90b1f62b9143"></a>

```c
int bt_hfp_hf_release_active_accept_other (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_release_active_accept_other](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga36be4ff5fd805c4413ba90b1f62b9143)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）释放所有活动呼叫（Active Calls）并接听另一呼叫。

<a id="r_ga40de46a6651eb85aa6d04ad66f528803"></a>

```c
int bt_hfp_hf_hold_active_accept_other (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_hold_active_accept_other](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga40de46a6651eb85aa6d04ad66f528803)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）保持所有活动呼叫（Active Calls）并接听另一呼叫。

<a id="r_ga04d9fe3524c9522e98830507886bdfc6"></a>

```c
int bt_hfp_hf_join_conversation (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_join_conversation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga04d9fe3524c9522e98830507886bdfc6)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）将一个保持中的呼叫（Held Call）加入通话。

<a id="r_ga2b48a0938e65899417b2f3ab1fa4c548"></a>

```c
int bt_hfp_hf_explicit_call_transfer (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_explicit_call_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga2b48a0938e65899417b2f3ab1fa4c548)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）执行显式呼叫转移（Explicit Call Transfer）。

<a id="r_ga1ad888c3b967d3f9b2e5ccee303b9ad7"></a>

```c
int bt_hfp_hf_release_specified_call (struct bt_hfp_hf_call *call)
```

相关声明：[bt_hfp_hf_release_specified_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga1ad888c3b967d3f9b2e5ccee303b9ad7)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）释放指定索引（Index）的呼叫。

<a id="r_gac3c038818cda3645eaadc5374d18c3ee"></a>

```c
int bt_hfp_hf_private_consultation_mode (struct bt_hfp_hf_call *call)
```

相关声明：[bt_hfp_hf_private_consultation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gac3c038818cda3645eaadc5374d18c3ee)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）请求与指定呼叫进行私密磋商模式（Private Consultation Mode）。

<a id="r_gaeed952ce163ef2466ece04af24b76a28"></a>

```c
int bt_hfp_hf_voice_recognition (struct bt_hfp_hf *hf, bool activate)
```

相关声明：[bt_hfp_hf_voice_recognition](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gaeed952ce163ef2466ece04af24b76a28)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

免提端（HF）启用／禁用语音识别功能（Voice Recognition Function）。

<a id="r_ga3f6b43bf53fa04a6e71e883dc38f988b"></a>

```c
int bt_hfp_hf_ready_to_accept_audio (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_ready_to_accept_audio](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga3f6b43bf53fa04a6e71e883dc38f988b)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）指示自身已准备好接收音频（Ready to Accept Audio）。

<a id="r_ga92d89b0b37186688e86091a7a8015245"></a>

```c
int bt_hfp_hf_request_phone_number (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_request_phone_number](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga92d89b0b37186688e86091a7a8015245)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）为语音标签（Voice Tag）关联一个电话号码。

<a id="r_ga6a3a6bc61a3a74f5a4a48d7e39bd74a0"></a>

```c
int bt_hfp_hf_transmit_dtmf_code (struct bt_hfp_hf_call *call, char code)
```

相关声明：[bt_hfp_hf_transmit_dtmf_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga6a3a6bc61a3a74f5a4a48d7e39bd74a0)、[bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)。

免提端（HF）发送指定的双音多频代码（DTMF Code）。

<a id="r_gad5dab4dcb66d52a80e0689a86de5fec3"></a>

```c
int bt_hfp_hf_query_subscriber (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_query_subscriber](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gad5dab4dcb66d52a80e0689a86de5fec3)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）查询用户号码信息（Subscriber Number Information）。

<a id="r_gab743d3e14fa13b71ddaf26d46cf41fb3"></a>

```c
int bt_hfp_hf_indicator_status (struct bt_hfp_hf *hf, uint8_t status)
```

相关声明：[bt_hfp_hf_indicator_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gab743d3e14fa13b71ddaf26d46cf41fb3)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提端（HF）设置音频网关指示器（AG Indicator）的激活／停用状态。

<a id="r_gab6710ce433812c3bf785b787008c36be"></a>

```c
int bt_hfp_hf_enhanced_safety (struct bt_hfp_hf *hf, bool enable)
```

相关声明：[bt_hfp_hf_enhanced_safety](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gab6710ce433812c3bf785b787008c36be)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

免提端（HF）启用／禁用增强安全功能（Enhanced Safety）。

<a id="r_ga2f0e6012503a9b59b03a0fb508d12f88"></a>

```c
int bt_hfp_hf_battery (struct bt_hfp_hf *hf, uint8_t level)
```

相关声明：[bt_hfp_hf_battery](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga2f0e6012503a9b59b03a0fb508d12f88)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提端（HF）的剩余电池电量（Remaining Battery Level）。

<a id="r_ga91637662881dd655f8fc8ed6e6f8b973"></a>

```c
int bt_hfp_hf_query_list_of_current_calls (struct bt_hfp_hf *hf)
```

相关声明：[bt_hfp_hf_query_list_of_current_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga91637662881dd655f8fc8ed6e6f8b973)、[bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)。

免提端（HF）查询当前呼叫列表（List of Current Calls）。


## 4.5\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [查看此文件的源码。](../api_source_transport_clock_reference/P017_hfp_hf.h_源码浏览.md)
- [bt_hfp_hf_current_call](../bluetooth_service_model_reference/P090_bt_hfp_hf_current_call_结构体.md)
- [bt_hfp_hf_cb](../bluetooth_service_model_reference/P089_bt_hfp_hf_cb_结构体.md)
- [BT_HFP_HF_CODEC_CVSD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga0e46a981a70dcdecbae119ebb6d61aa0)
- [BT_HFP_HF_CODEC_MSBC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gaea9fb177ae8ba32650dc93f1b2953333)
- [BT_HFP_HF_CODEC_LC3_SWB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gac8ab2e9ff6c8b9a06ac460f751dec1ad)
- [bt_hfp_hf_call_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga810c80de5baf92feb23650374b60bcee)
- [BT_HFP_HF_CALL_STATUS_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea1ea1ba685375baaabab22ad1c01ca6af)
- [BT_HFP_HF_CALL_STATUS_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceeab4db9c2eb21b5eb79517c0a761bc7dfa)
- [BT_HFP_HF_CALL_STATUS_DIALING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea9ff342787f8a6f7b9a5c0db1afa1bfb9)
- [BT_HFP_HF_CALL_STATUS_ALERTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea7377bf80fd685178d0d8b39189b2122a)
- [BT_HFP_HF_CALL_STATUS_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea8f8fc15f39de43b1ed202e16cd198104)
- [BT_HFP_HF_CALL_STATUS_WAITING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceea974da5247c5d332b11c42e93c9cbd831)
- [BT_HFP_HF_CALL_STATUS_INCOMING_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga810c80de5baf92feb23650374b60bceeabfa959b76eab9fc14ae941e3c1cd45ff)
- [bt_hfp_hf_call_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga6c2ba70d70c8f9d6d569662086985c85)
- [BT_HFP_HF_CALL_DIR_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga6c2ba70d70c8f9d6d569662086985c85aa631c2cc079db31712ac2ec7ac3dee3f)
- [BT_HFP_HF_CALL_DIR_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga6c2ba70d70c8f9d6d569662086985c85adf30d13bccb711d32a3c75e5c1d47d97)
- [bt_hfp_hf_call_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga38619377f146492993ee9a92a487af50)
- [BT_HFP_HF_CALL_MODE_VOICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga38619377f146492993ee9a92a487af50ac2233c577a6d8b8871b8e31969616f66)
- [BT_HFP_HF_CALL_MODE_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga38619377f146492993ee9a92a487af50a5a35798fc921e975775c496ac49193c9)
- [BT_HFP_HF_CALL_MODE_FAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga38619377f146492993ee9a92a487af50a646f51233cf8906d377bf0d6860f3bb0)
- [hfp_hf_ag_indicators](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga862b201be555821e932f6df5599eaa57)
- [HF_SERVICE_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57adb3fae0b3684e8d035e195a91d24deb8)
- [HF_CALL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57ad8620b141e11f48b46b9cd5ef1842fe6)
- [HF_CALL_SETUP_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57a24ceb35eba4e18dbde198b77a7db98de)
- [HF_CALL_HELD_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57ad0cfee8ab087438502689d12cafa39cf)
- [HF_SIGNAL_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57ac5055465440ffe897930cbfdabb7c3d0)
- [HF_ROAM_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57a3f9c27a235db99073918a904d6902eae)
- [HF_BATTERY_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gga862b201be555821e932f6df5599eaa57a1444cacc3f0307e7b53a0375807668c5)
- [bt_hfp_hf_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga2e4a7c05a3ba9a32eab50b9904f7f161)
- [bt_hfp_hf_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga302e9ed397b056edef518470c6ea1d62)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_hfp_hf](../bluetooth_service_model_reference/P087_bt_hfp_hf_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hfp_hf_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gaf5e7ef119731c0dc35bec61fb7c34774)
- [bt_hfp_hf_cli](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga64ac1971dc7b1dacf6685bdc0c71e34c)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_hfp_hf_vgm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga0602cee7a90ca4afe90b65d748024472)
- [bt_hfp_hf_vgs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga0c1c35b3117f78f43a6300d4ff7dd18b)
- [bt_hfp_hf_get_operator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gaaa9fbdceec140f274fc88c063a4cd4b8)
- [bt_hfp_hf_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga5bad80355fd7903abcee84437d399829)
- [bt_hfp_hf_call](../bluetooth_service_model_reference/P088_bt_hfp_hf_call_结构体.md)
- [bt_hfp_hf_reject](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gac4e3d88b80b69840d52050dcd72c9ab3)
- [bt_hfp_hf_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gabbce5fbf0dec27e1c5a4da144fbfc9c1)
- [bt_hfp_hf_hold_incoming](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga540bf6ec23c632b3f736e6302ef32ebd)
- [bt_hfp_hf_query_respond_hold_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga70e086f6a02cb116317a8e80f76abf6d)
- [bt_hfp_hf_number_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gac57d7188e3f8b6e1e28d2a55c2567dbf)
- [bt_hfp_hf_memory_dial](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gabacb666eb0f43db8614413a4ae0ce60a)
- [bt_hfp_hf_redial](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga9611012a35df66fac324b99b16e5d958)
- [bt_hfp_hf_audio_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gad29bf40953faf638cc08acf919eb8f4f)
- [bt_hfp_hf_select_codec](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga34649dbecca2513c0b5bcd0e109b2551)
- [bt_hfp_hf_set_codecs](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga91fc2204f50df07567f87a2b7a18e69f)
- [bt_hfp_hf_turn_off_ecnr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga7f37a9c009b4e55b7060d635c5b0c67b)
- [bt_hfp_hf_call_waiting_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga3afb0d82551708975dbeb9c903c3d1fb)
- [bt_hfp_hf_release_all_held](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga06e7e93578601693fa377a240e0d18a7)
- [bt_hfp_hf_set_udub](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga7389e5723e01b661b5e9c9d2114918b8)
- [bt_hfp_hf_release_active_accept_other](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga36be4ff5fd805c4413ba90b1f62b9143)
- [bt_hfp_hf_hold_active_accept_other](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga40de46a6651eb85aa6d04ad66f528803)
- [bt_hfp_hf_join_conversation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga04d9fe3524c9522e98830507886bdfc6)
- [bt_hfp_hf_explicit_call_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga2b48a0938e65899417b2f3ab1fa4c548)
- [bt_hfp_hf_release_specified_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga1ad888c3b967d3f9b2e5ccee303b9ad7)
- [bt_hfp_hf_private_consultation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gac3c038818cda3645eaadc5374d18c3ee)
- [bt_hfp_hf_voice_recognition](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gaeed952ce163ef2466ece04af24b76a28)
- [bt_hfp_hf_ready_to_accept_audio](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga3f6b43bf53fa04a6e71e883dc38f988b)
- [bt_hfp_hf_request_phone_number](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga92d89b0b37186688e86091a7a8015245)
- [bt_hfp_hf_transmit_dtmf_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga6a3a6bc61a3a74f5a4a48d7e39bd74a0)
- [bt_hfp_hf_query_subscriber](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gad5dab4dcb66d52a80e0689a86de5fec3)
- [bt_hfp_hf_indicator_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gab743d3e14fa13b71ddaf26d46cf41fb3)
- [bt_hfp_hf_enhanced_safety](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gab6710ce433812c3bf785b787008c36be)
- [bt_hfp_hf_battery](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga2f0e6012503a9b59b03a0fb508d12f88)
- [bt_hfp_hf_query_list_of_current_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga91637662881dd655f8fc8ed6e6f8b973)

<a id="header-details"></a>

---

[上一章](P003_zephyr__storage__flash_map.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__net__ieee802154_radio_openthread.h_文件参考.md)
