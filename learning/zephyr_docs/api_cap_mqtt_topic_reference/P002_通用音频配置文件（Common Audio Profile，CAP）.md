---
id: learning.zephyr-docs.api-cap-mqtt-topic-reference.page-2
title: 通用音频配置文件（Common Audio Profile，CAP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_通用音频配置文件（Common Audio Profile，CAP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用音频配置文件（Common Audio Profile，CAP）

<a id="details"></a>

通用音频配置文件（Common Audio Profile，CAP）。自（Since）3.2 起提供，版本（Version）0.8.0。CAP 使用基本音频配置文件（BAP）的流程，提供在单个或成组设备上启动、更新和停止单播及广播音频流的流程。它还使用音量控制配置文件（VCP）和麦克风控制配置文件（MICP）的流程，提供控制设备组音量和设备输入的流程。此配置文件规范也引用通用音频服务（Common Audio Service，CAS）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fcap_5Finitiator_5Fcb"></a>

```c
struct bt_cap_initiator_cb
```

相关声明：[bt_cap_initiator_cb](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md)。

通用音频配置文件（Common Audio Profile，CAP）过程的回调结构体。

<a id="r_bt_5Fcap_5Fset_5Fmember"></a>

```c
union bt_cap_set_member
```

相关声明：[bt_cap_set_member](../bluetooth_service_model_reference/P188_bt_cap_set_member_联合体.md)。

表示通用音频集合（Common Audio Set）的成员，该成员属于协调集合（Coordinated Set）或临时集合（Ad-hoc Set）。

<a id="r_bt_5Fcap_5Fstream"></a>

```c
struct bt_cap_stream
```

相关声明：[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)。

通用音频配置文件（Common Audio Profile，CAP）流结构体。

<a id="r_bt_5Fcap_5Funicast_5Fgroup_5Fstream_5Fparam"></a>

```c
struct bt_cap_unicast_group_stream_param
```

相关声明：[bt_cap_unicast_group_stream_param](../bluetooth_service_model_reference/P049_bt_cap_unicast_group_stream_param_结构体.md)。

单播组中每条流的参数结构体。

<a id="r_bt_5Fcap_5Funicast_5Fgroup_5Fstream_5Fpair_5Fparam"></a>

```c
struct bt_cap_unicast_group_stream_pair_param
```

相关声明：[bt_cap_unicast_group_stream_pair_param](../bluetooth_service_model_reference/P048_bt_cap_unicast_group_stream_pair_param_结构体.md)。

单播组函数使用的参数结构体。

<a id="r_bt_5Fcap_5Funicast_5Fgroup_5Fparam"></a>

```c
struct bt_cap_unicast_group_param
```

相关声明：[bt_cap_unicast_group_param](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md)。

使用 `bt_cap_unicast_group_create()` 创建单播组的参数。

<a id="r_bt_5Fcap_5Funicast_5Fgroup_5Finfo"></a>

```c
struct bt_cap_unicast_group_info
```

相关声明：[bt_cap_unicast_group_info](../bluetooth_service_model_reference/P046_bt_cap_unicast_group_info_结构体.md)。

保存音频流端点信息的结构体。

<a id="r_bt_5Fcap_5Funicast_5Faudio_5Fstart_5Fstream_5Fparam"></a>

```c
struct bt_cap_unicast_audio_start_stream_param
```

相关声明：[bt_cap_unicast_audio_start_stream_param](../bluetooth_service_model_reference/P041_bt_cap_unicast_audio_start_stream_param_结构体.md)。

`bt_cap_initiator_unicast_audio_start()` 函数的流专用参数（Stream Specific Parameters）。

<a id="r_bt_5Fcap_5Funicast_5Faudio_5Fstart_5Fparam"></a>

```c
struct bt_cap_unicast_audio_start_param
```

相关声明：[bt_cap_unicast_audio_start_param](../bluetooth_service_model_reference/P040_bt_cap_unicast_audio_start_param_结构体.md)。

`bt_cap_initiator_unicast_audio_start()` 函数的参数（Parameters）。

<a id="r_bt_5Fcap_5Funicast_5Faudio_5Fupdate_5Fstream_5Fparam"></a>

```c
struct bt_cap_unicast_audio_update_stream_param
```

相关声明：[bt_cap_unicast_audio_update_stream_param](../bluetooth_service_model_reference/P044_bt_cap_unicast_audio_update_stream_param_结构体.md)。

`bt_cap_initiator_unicast_audio_update()` 函数的流专用参数（Stream Specific Parameters）。

<a id="r_bt_5Fcap_5Funicast_5Faudio_5Fupdate_5Fparam"></a>

```c
struct bt_cap_unicast_audio_update_param
```

相关声明：[bt_cap_unicast_audio_update_param](../bluetooth_service_model_reference/P043_bt_cap_unicast_audio_update_param_结构体.md)。

`bt_cap_initiator_unicast_audio_update()` 函数的参数（Parameters）。

<a id="r_bt_5Fcap_5Funicast_5Faudio_5Fstop_5Fparam"></a>

```c
struct bt_cap_unicast_audio_stop_param
```

相关声明：[bt_cap_unicast_audio_stop_param](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md)。

`bt_cap_initiator_unicast_audio_stop()` 函数的参数（Parameters）。

<a id="r_bt_5Fcap_5Finitiator_5Fbroadcast_5Fstream_5Fparam"></a>

```c
struct bt_cap_initiator_broadcast_stream_param
```

相关声明：[bt_cap_initiator_broadcast_stream_param](../bluetooth_service_model_reference/P036_bt_cap_initiator_broadcast_stream_param_结构体.md)。

`bt_cap_initiator_broadcast_subgroup_param` 中供 `bt_cap_initiator_broadcast_audio_create()` 使用的参数部分。

<a id="r_bt_5Fcap_5Finitiator_5Fbroadcast_5Fsubgroup_5Fparam"></a>

```c
struct bt_cap_initiator_broadcast_subgroup_param
```

相关声明：[bt_cap_initiator_broadcast_subgroup_param](../bluetooth_service_model_reference/P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md)。

`bt_cap_initiator_broadcast_create_param` 中供 `bt_cap_initiator_broadcast_audio_create()` 使用的参数部分。

<a id="r_bt_5Fcap_5Finitiator_5Fbroadcast_5Fcreate_5Fparam"></a>

```c
struct bt_cap_initiator_broadcast_create_param
```

相关声明：[bt_cap_initiator_broadcast_create_param](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md)。

`bt_cap_initiator_broadcast_audio_create()` 的参数。

<a id="r_bt_5Fcap_5Fhandover_5Funicast_5Fto_5Fbroadcast_5Fparam"></a>

```c
struct bt_cap_handover_unicast_to_broadcast_param
```

相关声明：[bt_cap_handover_unicast_to_broadcast_param](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md)。

`bt_cap_handover_unicast_to_broadcast()` 的参数（Parameters）。

<a id="r_bt_5Fcap_5Fhandover_5Fcb"></a>

```c
struct bt_cap_handover_cb
```

相关声明：[bt_cap_handover_cb](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md)。

通用音频配置文件（Common Audio Profile，CAP）过程的回调结构体。

<a id="r_bt_5Fcap_5Fhandover_5Fbroadcast_5Fto_5Funicast_5Fparam"></a>

```c
struct bt_cap_handover_broadcast_to_unicast_param
```

相关声明：[bt_cap_handover_broadcast_to_unicast_param](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md)。

`bt_cap_handover_broadcast_to_unicast()` 的参数（Parameters）。

<a id="r_bt_5Fcap_5Fcommander_5Fcb"></a>

```c
struct bt_cap_commander_cb
```

相关声明：[bt_cap_commander_cb](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md)。

通用音频配置文件（Common Audio Profile，CAP）过程的回调结构体。

<a id="r_bt_5Fcap_5Fcommander_5Fbroadcast_5Freception_5Fstart_5Fmember_5Fparam"></a>

```c
struct bt_cap_commander_broadcast_reception_start_member_param
```

相关声明：[bt_cap_commander_broadcast_reception_start_member_param](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md)。

`bt_cap_commander_broadcast_reception_start_param` 中供 `bt_cap_commander_broadcast_reception_start()` 使用的参数部分。

<a id="r_bt_5Fcap_5Fcommander_5Fbroadcast_5Freception_5Fstart_5Fparam"></a>

```c
struct bt_cap_commander_broadcast_reception_start_param
```

相关声明：[bt_cap_commander_broadcast_reception_start_param](../bluetooth_service_model_reference/P019_bt_cap_commander_broadcast_reception_start_param_结构体.md)。

启动广播接收（Broadcast Reception）的参数。

<a id="r_bt_5Fcap_5Fcommander_5Fbroadcast_5Freception_5Fstop_5Fmember_5Fparam"></a>

```c
struct bt_cap_commander_broadcast_reception_stop_member_param
```

相关声明：[bt_cap_commander_broadcast_reception_stop_member_param](../bluetooth_service_model_reference/P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md)。

停止广播接收的成员参数（Member Parameters）。

<a id="r_bt_5Fcap_5Fcommander_5Fbroadcast_5Freception_5Fstop_5Fparam"></a>

```c
struct bt_cap_commander_broadcast_reception_stop_param
```

相关声明：[bt_cap_commander_broadcast_reception_stop_param](../bluetooth_service_model_reference/P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md)。

停止广播接收的参数。

<a id="r_bt_5Fcap_5Fcommander_5Fdistribute_5Fbroadcast_5Fcode_5Fmember_5Fparam"></a>

```c
struct bt_cap_commander_distribute_broadcast_code_member_param
```

相关声明：[bt_cap_commander_distribute_broadcast_code_member_param](../bluetooth_service_model_reference/P030_bt_cap_commander_distribute_broadcast_code_member_param_结构体.md)。

分发广播码（Broadcast Code）的成员参数。

<a id="r_bt_5Fcap_5Fcommander_5Fdistribute_5Fbroadcast_5Fcode_5Fparam"></a>

```c
struct bt_cap_commander_distribute_broadcast_code_param
```

相关声明：[bt_cap_commander_distribute_broadcast_code_param](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md)。

分发广播码的参数。

<a id="r_bt_5Fcap_5Fcommander_5Fchange_5Fvolume_5Fparam"></a>

```c
struct bt_cap_commander_change_volume_param
```

相关声明：[bt_cap_commander_change_volume_param](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md)。

更改绝对音量（Absolute Volume）的参数。

<a id="r_bt_5Fcap_5Fcommander_5Fchange_5Fvolume_5Foffset_5Fmember_5Fparam"></a>

```c
struct bt_cap_commander_change_volume_offset_member_param
```

相关声明：[bt_cap_commander_change_volume_offset_member_param](../bluetooth_service_model_reference/P027_bt_cap_commander_change_volume_offset_member_param_结构体.md)。

`bt_cap_commander_change_volume_offset_param` 中供 `bt_cap_commander_change_volume_offset()` 使用的参数部分。

<a id="r_bt_5Fcap_5Fcommander_5Fchange_5Fvolume_5Foffset_5Fparam"></a>

```c
struct bt_cap_commander_change_volume_offset_param
```

相关声明：[bt_cap_commander_change_volume_offset_param](../bluetooth_service_model_reference/P028_bt_cap_commander_change_volume_offset_param_结构体.md)。

更改音量偏移（Volume Offset）的参数。

<a id="r_bt_5Fcap_5Fcommander_5Fchange_5Fvolume_5Fmute_5Fstate_5Fparam"></a>

```c
struct bt_cap_commander_change_volume_mute_state_param
```

相关声明：[bt_cap_commander_change_volume_mute_state_param](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md)。

更改音量静音状态（Volume Mute State）的参数。

<a id="r_bt_5Fcap_5Fcommander_5Fchange_5Fmicrophone_5Fmute_5Fstate_5Fparam"></a>

```c
struct bt_cap_commander_change_microphone_mute_state_param
```

相关声明：[bt_cap_commander_change_microphone_mute_state_param](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md)。

更改麦克风静音状态（Microphone Mute State）的参数。

<a id="r_bt_5Fcap_5Fcommander_5Fchange_5Fmicrophone_5Fgain_5Fsetting_5Fmember_5Fparam"></a>

```c
struct bt_cap_commander_change_microphone_gain_setting_member_param
```

相关声明：[bt_cap_commander_change_microphone_gain_setting_member_param](../bluetooth_service_model_reference/P023_bt_cap_commander_change_microphone_gain_setting_member_param_结构体.md)。

`bt_cap_commander_change_microphone_gain_setting_param` 中供 `bt_cap_commander_change_microphone_gain_setting()` 使用的参数部分。

<a id="r_bt_5Fcap_5Fcommander_5Fchange_5Fmicrophone_5Fgain_5Fsetting_5Fparam"></a>

```c
struct bt_cap_commander_change_microphone_gain_setting_param
```

相关声明：[bt_cap_commander_change_microphone_gain_setting_param](../bluetooth_service_model_reference/P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md)。

更改麦克风静音状态（Microphone Mute State）的参数。

<a id="r_bt_5Fcap_5Fbroadcast_5Fsource"></a>

```c
struct bt_cap_broadcast_source
```

相关声明：[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)。

抽象音频广播源结构体（Abstract Audio Broadcast Source Structure）。

<a id="r_bt_5Fcap_5Funicast_5Fgroup"></a>

```c
struct bt_cap_unicast_group
```

相关声明：[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)。

抽象 CAP 单播组（Unicast Group）结构体。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.2\_类型定义（Typedefs）

<a id="r_gaeaad4ea5142afe5dca741b72795ae3aa"></a>

```c
typedef bool(* bt_cap_unicast_group_foreach_stream_func_t) (struct bt_cap_stream *stream, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_cap_unicast_group_foreach_stream_func_t](#gaeaad4ea5142afe5dca741b72795ae3aa)、[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)。

bt_cap_unicast_group_foreach_stream() 的回调函数（Callback Function）。

<a id="r_ga2c6dc73fb44bca1f5bf8d39d46690b30"></a>

```c
typedef bool(* bt_cap_initiator_broadcast_foreach_stream_func_t) (struct bt_cap_stream *stream, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_cap_initiator_broadcast_foreach_stream_func_t](#ga2c6dc73fb44bca1f5bf8d39d46690b30)、[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)。

bt_cap_initiator_broadcast_foreach_stream() 的回调函数（Callback Function）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.3\_枚举（Enumerations）

<a id="r_gac9d750d0a22fab7852f0a04757feab6a"></a>

```c
enum bt_cap_set_type { BT_CAP_SET_TYPE_AD_HOC , BT_CAP_SET_TYPE_CSIP }
```

相关声明：[bt_cap_set_type](#gac9d750d0a22fab7852f0a04757feab6a)、[BT_CAP_SET_TYPE_AD_HOC](#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468)、[BT_CAP_SET_TYPE_CSIP](#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4)。

通用音频配置文件集合类型（CAP Set Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_gafcb9ea2122ff8058321cf85a22326abe"></a>

```c
int bt_cap_acceptor_register (const struct bt_csip_set_member_register_param *param, struct bt_csip_set_member_svc_inst **svc_inst)
```

相关声明：[bt_cap_acceptor_register](#gafcb9ea2122ff8058321cf85a22326abe)、[bt_csip_set_member_register_param](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)。

注册通用音频服务（Common Audio Service）。

<a id="r_gab7b273d06abf9a3cb43afdd4e3c30c8d"></a>

```c
int bt_cap_initiator_unicast_discover (struct bt_conn *conn)
```

相关声明：[bt_cap_initiator_unicast_discover](#gab7b273d06abf9a3cb43afdd4e3c30c8d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现远端设备的音频支持（Audio Support）。

<a id="r_gac909b00d53cf35103382f0e1d9f426b7"></a>

```c
void bt_cap_stream_ops_register (struct bt_cap_stream *stream, struct bt_bap_stream_ops *ops)
```

相关声明：[bt_cap_stream_ops_register](#gac909b00d53cf35103382f0e1d9f426b7)、[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)、[bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)。

为通用音频配置文件（Common Audio Profile）流注册音频操作（Audio Operations）。

<a id="r_ga2d8b15543105078b793462b762e27741"></a>

```c
int bt_cap_stream_send (struct bt_cap_stream *stream, struct net_buf *buf, uint16_t seq_num)
```

相关声明：[bt_cap_stream_send](#ga2d8b15543105078b793462b762e27741)、[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向通用音频配置文件（Common Audio Profile）流发送不带时间戳（Timestamp）的数据。

<a id="r_ga23618d1ab7690c4d3a567228c857c89e"></a>

```c
int bt_cap_stream_send_ts (struct bt_cap_stream *stream, struct net_buf *buf, uint16_t seq_num, uint32_t ts)
```

相关声明：[bt_cap_stream_send_ts](#ga23618d1ab7690c4d3a567228c857c89e)、[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向通用音频配置文件（Common Audio Profile）流发送带时间戳（Timestamp）的数据。

<a id="r_ga7f3f6e98e7720a4711b658c4b7c85235"></a>

```c
int bt_cap_stream_get_tx_sync (struct bt_cap_stream *stream, struct bt_iso_tx_info *info)
```

相关声明：[bt_cap_stream_get_tx_sync](#ga7f3f6e98e7720a4711b658c4b7c85235)、[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)、[bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)。

获取通用音频配置文件（Common Audio Profile）流的等时传输时序信息（ISO Transmission Timing Info）。

<a id="r_gab49e8c2032a824516dc8d5f2f880dd8f"></a>

```c
int bt_cap_unicast_group_create (const struct bt_cap_unicast_group_param *param, struct bt_cap_unicast_group **out_unicast_group)
```

相关声明：[bt_cap_unicast_group_create](#gab49e8c2032a824516dc8d5f2f880dd8f)、[bt_cap_unicast_group_param](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md)、[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)。

创建单播组（Unicast Group）。

<a id="r_ga6c862b49aa1339225aeb05fad32c2f06"></a>

```c
int bt_cap_unicast_group_reconfig (struct bt_cap_unicast_group *unicast_group, const struct bt_cap_unicast_group_param *param)
```

相关声明：[bt_cap_unicast_group_reconfig](#ga6c862b49aa1339225aeb05fad32c2f06)、[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)、[bt_cap_unicast_group_param](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md)。

重新配置单播组（Unicast Group）。

<a id="r_ga7b5d30c07e57f4db23f72836a3b12b2b"></a>

```c
int bt_cap_unicast_group_add_streams (struct bt_cap_unicast_group *unicast_group, const struct bt_cap_unicast_group_stream_pair_param params[], size_t num_param)
```

相关声明：[bt_cap_unicast_group_add_streams](#ga7b5d30c07e57f4db23f72836a3b12b2b)、[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)、[bt_cap_unicast_group_stream_pair_param](../bluetooth_service_model_reference/P048_bt_cap_unicast_group_stream_pair_param_结构体.md)。

以单播客户端（Unicast Client）身份向单播组添加流（Streams）。

<a id="r_ga9af37b30b6c858c24892eb1739b5330a"></a>

```c
int bt_cap_unicast_group_delete (struct bt_cap_unicast_group *unicast_group)
```

相关声明：[bt_cap_unicast_group_delete](#ga9af37b30b6c858c24892eb1739b5330a)、[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)。

删除音频单播组（Audio Unicast Group）。

<a id="r_ga6c13996298c3e3aa33eb40f74b7bfe44"></a>

```c
int bt_cap_unicast_group_foreach_stream (struct bt_cap_unicast_group *unicast_group, bt_cap_unicast_group_foreach_stream_func_t func, void *user_data)
```

相关声明：[bt_cap_unicast_group_foreach_stream](#ga6c13996298c3e3aa33eb40f74b7bfe44)、[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)、[bt_cap_unicast_group_foreach_stream_func_t](#gaeaad4ea5142afe5dca741b72795ae3aa)。

遍历单播组（Unicast Group）中的全部流。

<a id="r_ga86aca9c7f2f8658f4486925c68148850"></a>

```c
int bt_cap_unicast_group_get_info (const struct bt_cap_unicast_group *unicast_group, struct bt_cap_unicast_group_info *info)
```

相关声明：[bt_cap_unicast_group_get_info](#ga86aca9c7f2f8658f4486925c68148850)、[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)、[bt_cap_unicast_group_info](../bluetooth_service_model_reference/P046_bt_cap_unicast_group_info_结构体.md)。

返回保存单播组信息（Unicast Group Information）的结构体。

<a id="r_ga54d7ad68f376998510aad9c3702e9364"></a>

```c
int bt_cap_initiator_register_cb (const struct bt_cap_initiator_cb *cb)
```

相关声明：[bt_cap_initiator_register_cb](#ga54d7ad68f376998510aad9c3702e9364)、[bt_cap_initiator_cb](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md)。

注册通用音频配置文件发起方（Common Audio Profile Initiator）的回调。

<a id="r_gaa7286837f37da38afec8c5c955306b61"></a>

```c
int bt_cap_initiator_unregister_cb (const struct bt_cap_initiator_cb *cb)
```

相关声明：[bt_cap_initiator_unregister_cb](#gaa7286837f37da38afec8c5c955306b61)、[bt_cap_initiator_cb](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md)。

注销通用音频配置文件发起方（Common Audio Profile Initiator）的回调。

<a id="r_gae19686be7f8aef1cc92c70fea93e1184"></a>

```c
int bt_cap_initiator_unicast_audio_start (const struct bt_cap_unicast_audio_start_param *param)
```

相关声明：[bt_cap_initiator_unicast_audio_start](#gae19686be7f8aef1cc92c70fea93e1184)、[bt_cap_unicast_audio_start_param](../bluetooth_service_model_reference/P040_bt_cap_unicast_audio_start_param_结构体.md)。

为一组设备建立并启动单播音频流（Unicast Audio Streams）。

<a id="r_ga92e4e2c12720ec25c4050cde307cd639"></a>

```c
int bt_cap_initiator_unicast_audio_update (const struct bt_cap_unicast_audio_update_param *param)
```

相关声明：[bt_cap_initiator_unicast_audio_update](#ga92e4e2c12720ec25c4050cde307cd639)、[bt_cap_unicast_audio_update_param](../bluetooth_service_model_reference/P043_bt_cap_unicast_audio_update_param_结构体.md)。

更新单播音频流（Unicast Audio Streams）。

<a id="r_gafdf6f1656249ab3ae6296272dc36b66f"></a>

```c
int bt_cap_initiator_unicast_audio_stop (const struct bt_cap_unicast_audio_stop_param *param)
```

相关声明：[bt_cap_initiator_unicast_audio_stop](#gafdf6f1656249ab3ae6296272dc36b66f)、[bt_cap_unicast_audio_stop_param](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md)。

停止单播音频流（Unicast Audio Streams）。

<a id="r_ga9fbddf102e29e8e969eade40fd60da4f"></a>

```c
int bt_cap_initiator_unicast_audio_cancel (void)
```

相关声明：[bt_cap_initiator_unicast_audio_cancel](#ga9fbddf102e29e8e969eade40fd60da4f)。

取消当前任何通用音频配置文件发起方过程（Common Audio Profile Initiator Procedure）。

<a id="r_ga78697225c6b1291dfc016e20fd605fc4"></a>

```c
int bt_cap_initiator_broadcast_audio_create (const struct bt_cap_initiator_broadcast_create_param *param, struct bt_cap_broadcast_source **broadcast_source)
```

相关声明：[bt_cap_initiator_broadcast_audio_create](#ga78697225c6b1291dfc016e20fd605fc4)、[bt_cap_initiator_broadcast_create_param](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)。

创建通用音频配置文件广播源（Common Audio Profile Broadcast Source）。

<a id="r_ga2bd5f9c9de719a14ffc69827dbd4fa24"></a>

```c
int bt_cap_initiator_broadcast_audio_start (struct bt_cap_broadcast_source *broadcast_source, struct bt_le_ext_adv *adv)
```

相关声明：[bt_cap_initiator_broadcast_audio_start](#ga2bd5f9c9de719a14ffc69827dbd4fa24)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

启动通用音频配置文件广播源（Common Audio Profile Broadcast Source）。

<a id="r_ga92336c4a56c667b608a86e45eb8d5073"></a>

```c
int bt_cap_initiator_broadcast_audio_update (struct bt_cap_broadcast_source *broadcast_source, const uint8_t meta[], size_t meta_len)
```

相关声明：[bt_cap_initiator_broadcast_audio_update](#ga92336c4a56c667b608a86e45eb8d5073)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新通用音频配置文件广播源（Common Audio Profile Broadcast Source）的广播音频流（Broadcast Audio Streams）。

<a id="r_gae4e348f74e3c12e73879082d00cdb17e"></a>

```c
int bt_cap_initiator_broadcast_audio_stop (struct bt_cap_broadcast_source *broadcast_source)
```

相关声明：[bt_cap_initiator_broadcast_audio_stop](#gae4e348f74e3c12e73879082d00cdb17e)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)。

停止通用音频配置文件广播源（Common Audio Profile Broadcast Source）的广播音频流（Broadcast Audio Streams）。

<a id="r_gac98ed5112d0ce0659bde86d149ea7b4c"></a>

```c
int bt_cap_initiator_broadcast_audio_delete (struct bt_cap_broadcast_source *broadcast_source)
```

相关声明：[bt_cap_initiator_broadcast_audio_delete](#gac98ed5112d0ce0659bde86d149ea7b4c)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)。

删除通用音频配置文件广播源（Common Audio Profile Broadcast Source）。

<a id="r_ga71b1a73b9fd4b1be8a63a79e05c1c0aa"></a>

```c
int bt_cap_initiator_broadcast_get_base (struct bt_cap_broadcast_source *broadcast_source, struct net_buf_simple *base_buf)
```

相关声明：[bt_cap_initiator_broadcast_get_base](#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

获取通用音频配置文件广播源（Common Audio Profile Broadcast Source）的广播音频流端点（Broadcast Audio Stream Endpoint）。

<a id="r_ga45fa73b787bb4fefc73928acf3592e20"></a>

```c
int bt_cap_initiator_broadcast_foreach_stream (struct bt_cap_broadcast_source *broadcast_source, bt_cap_initiator_broadcast_foreach_stream_func_t func, void *user_data)
```

相关声明：[bt_cap_initiator_broadcast_foreach_stream](#ga45fa73b787bb4fefc73928acf3592e20)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)、[bt_cap_initiator_broadcast_foreach_stream_func_t](#ga2c6dc73fb44bca1f5bf8d39d46690b30)。

遍历广播源中的所有流（Streams）。

<a id="r_ga5d8c66b3890e051b838d123a1911cfd6"></a>

```c
int bt_cap_handover_register_cb (const struct bt_cap_handover_cb *cb)
```

相关声明：[bt_cap_handover_register_cb](#ga5d8c66b3890e051b838d123a1911cfd6)、[bt_cap_handover_cb](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md)。

注册通用音频配置文件切换（Common Audio Profile Handover）的回调。

<a id="r_ga808f0e5b671689196ba6f0fc1aea7427"></a>

```c
int bt_cap_handover_unregister_cb (const struct bt_cap_handover_cb *cb)
```

相关声明：[bt_cap_handover_unregister_cb](#ga808f0e5b671689196ba6f0fc1aea7427)、[bt_cap_handover_cb](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md)。

注销通用音频配置文件切换（Common Audio Profile Handover）的回调。

<a id="r_gaae56deae3792740bc3e8074882c87837"></a>

```c
int bt_cap_handover_unicast_to_broadcast (const struct bt_cap_handover_unicast_to_broadcast_param *param)
```

相关声明：[bt_cap_handover_unicast_to_broadcast](#gaae56deae3792740bc3e8074882c87837)、[bt_cap_handover_unicast_to_broadcast_param](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md)。

将单播组（Unicast Group）中的接收端流（Sink Streams）切换到广播源（Broadcast Source）。

<a id="r_ga92ff8b3133b8f5cb3d3029b5d556fe77"></a>

```c
int bt_cap_handover_broadcast_to_unicast (const struct bt_cap_handover_broadcast_to_unicast_param *param)
```

相关声明：[bt_cap_handover_broadcast_to_unicast](#ga92ff8b3133b8f5cb3d3029b5d556fe77)、[bt_cap_handover_broadcast_to_unicast_param](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md)。

将广播源（Broadcast Source）中的数据流切换到单播组（Unicast Group）。

<a id="r_gacd17de17ac1d96ff17ae15a63f43ad03"></a>

```c
int bt_cap_handover_cancel (void)
```

相关声明：[bt_cap_handover_cancel](#gacd17de17ac1d96ff17ae15a63f43ad03)。

取消当前任何通用音频配置文件切换过程（Common Audio Profile Handover Procedure）。

<a id="r_gab6239c91b9d210872396860619fb8687"></a>

```c
int bt_cap_commander_register_cb (const struct bt_cap_commander_cb *cb)
```

相关声明：[bt_cap_commander_register_cb](#gab6239c91b9d210872396860619fb8687)、[bt_cap_commander_cb](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md)。

注册通用音频配置文件指挥方（Common Audio Profile Commander）的回调。

<a id="r_ga38928945e67835983de3fc639c8f2764"></a>

```c
int bt_cap_commander_unregister_cb (const struct bt_cap_commander_cb *cb)
```

相关声明：[bt_cap_commander_unregister_cb](#ga38928945e67835983de3fc639c8f2764)、[bt_cap_commander_cb](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md)。

注销通用音频配置文件指挥方（Common Audio Profile Commander）的回调。

<a id="r_ga165c67bddcbe220050293a4c73fb6ede"></a>

```c
int bt_cap_commander_discover (struct bt_conn *conn)
```

相关声明：[bt_cap_commander_discover](#ga165c67bddcbe220050293a4c73fb6ede)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现远端设备的音频支持（Audio Support）。

<a id="r_ga7abf029533fed391930257605f3c752c"></a>

```c
int bt_cap_commander_cancel (void)
```

相关声明：[bt_cap_commander_cancel](#ga7abf029533fed391930257605f3c752c)。

取消当前任何通用音频配置文件指挥方过程（Common Audio Profile Commander Procedure）。

<a id="r_ga25be83bb53c8e2ab76f311eaf4f615b9"></a>

```c
int bt_cap_commander_broadcast_reception_start (const struct bt_cap_commander_broadcast_reception_start_param *param)
```

相关声明：[bt_cap_commander_broadcast_reception_start](#ga25be83bb53c8e2ab76f311eaf4f615b9)、[bt_cap_commander_broadcast_reception_start_param](../bluetooth_service_model_reference/P019_bt_cap_commander_broadcast_reception_start_param_结构体.md)。

在一个或多个远端通用音频配置文件接受方（Common Audio Profile Acceptors）上启动广播音频接收。

<a id="r_gac5b2b6d617a092fb98b23c41b2f52d15"></a>

```c
int bt_cap_commander_broadcast_reception_stop (const struct bt_cap_commander_broadcast_reception_stop_param *param)
```

相关声明：[bt_cap_commander_broadcast_reception_stop](#gac5b2b6d617a092fb98b23c41b2f52d15)、[bt_cap_commander_broadcast_reception_stop_param](../bluetooth_service_model_reference/P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md)。

在一个或多个远端通用音频配置文件接受方（Common Audio Profile Acceptors）上停止广播音频接收。

<a id="r_gaf86582ad529b6ee801d1154db7e33827"></a>

```c
int bt_cap_commander_distribute_broadcast_code (const struct bt_cap_commander_distribute_broadcast_code_param *param)
```

相关声明：[bt_cap_commander_distribute_broadcast_code](#gaf86582ad529b6ee801d1154db7e33827)、[bt_cap_commander_distribute_broadcast_code_param](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md)。

向一个或多个远端通用音频配置文件接受方（Common Audio Profile Acceptors）分发广播码（Broadcast Code）。

<a id="r_gaff96953334eab1a38b30720b41c0d1a6"></a>

```c
int bt_cap_commander_change_volume (const struct bt_cap_commander_change_volume_param *param)
```

相关声明：[bt_cap_commander_change_volume](#gaff96953334eab1a38b30720b41c0d1a6)、[bt_cap_commander_change_volume_param](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md)。

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的音量（Volume）。

<a id="r_gae2cd451b387659b0a2021a9023d74dfa"></a>

```c
int bt_cap_commander_change_volume_offset (const struct bt_cap_commander_change_volume_offset_param *param)
```

相关声明：[bt_cap_commander_change_volume_offset](#gae2cd451b387659b0a2021a9023d74dfa)、[bt_cap_commander_change_volume_offset_param](../bluetooth_service_model_reference/P028_bt_cap_commander_change_volume_offset_param_结构体.md)。

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的音量偏移（Volume Offset）。

<a id="r_gac5f94baa82fa6deade6f83346a56b5e4"></a>

```c
int bt_cap_commander_change_volume_mute_state (const struct bt_cap_commander_change_volume_mute_state_param *param)
```

相关声明：[bt_cap_commander_change_volume_mute_state](#gac5f94baa82fa6deade6f83346a56b5e4)、[bt_cap_commander_change_volume_mute_state_param](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md)。

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的音量静音状态（Volume Mute State）。

<a id="r_ga19cc7ed5992a528a7795b76e7add6d54"></a>

```c
int bt_cap_commander_change_microphone_mute_state (const struct bt_cap_commander_change_microphone_mute_state_param *param)
```

相关声明：[bt_cap_commander_change_microphone_mute_state](#ga19cc7ed5992a528a7795b76e7add6d54)、[bt_cap_commander_change_microphone_mute_state_param](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md)。

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的麦克风静音状态（Microphone Mute State）。

<a id="r_ga958cd5925699624d23479ad2ace6b55b"></a>

```c
int bt_cap_commander_change_microphone_gain_setting (const struct bt_cap_commander_change_microphone_gain_setting_param *param)
```

相关声明：[bt_cap_commander_change_microphone_gain_setting](#ga958cd5925699624d23479ad2ace6b55b)、[bt_cap_commander_change_microphone_gain_setting_param](../bluetooth_service_model_reference/P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md)。

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的麦克风增益设置（Microphone Gain Setting）。

## 2.5\_详细说明（Detailed Documentation）

<a id="ga2c6dc73fb44bca1f5bf8d39d46690b30"></a>

### `bt_cap_initiator_broadcast_foreach_stream_func_t`

```c
typedef bool(* bt_cap_initiator_broadcast_foreach_stream_func_t) (struct bt_cap_stream *stream, void *user_data)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

bt_cap_initiator_broadcast_foreach_stream() 的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 音频流（Audio Stream） |
| `user_data` | 用户数据（User Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 继续遍历（Continue Iterating）。 |
| `false` | 停止遍历（Stop Iterating）。 |

<a id="gaeaad4ea5142afe5dca741b72795ae3aa"></a>

### `bt_cap_unicast_group_foreach_stream_func_t`

```c
typedef bool(* bt_cap_unicast_group_foreach_stream_func_t) (struct bt_cap_stream *stream, void *user_data)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

bt_cap_unicast_group_foreach_stream() 的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 音频流（Audio Stream） |
| `user_data` | 用户数据（User Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 继续遍历（Continue Iterating）。 |
| `false` | 停止遍历（Stop Iterating）。 |

<a id="gac9d750d0a22fab7852f0a04757feab6a"></a>

### `bt_cap_set_type`

```c
enum bt_cap_set_type
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

通用音频配置文件集合类型（CAP Set Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CAP_SET_TYPE_AD_HOC` | 该集合为临时集合（Ad-Hoc Set）。 |
| `BT_CAP_SET_TYPE_CSIP` | 该集合为 CSIP 协同集（Coordinated Set）。 |

<a id="gafcb9ea2122ff8058321cf85a22326abe"></a>

### `bt_cap_acceptor_register()`

```c
int bt_cap_acceptor_register ( const struct bt_csip_set_member_register_param * param, struct bt_csip_set_member_svc_inst ** svc_inst )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

注册通用音频服务（Common Audio Service）。

这会注册并启用服务，使客户端能够发现它；同时还会注册一个协同集标识服务（Coordinated Set Identification Service）实例。

此操作只能以服务器身份执行，并要求启用 `CONFIG_BT_CAP_ACCEPTOR_SET_MEMBER`。未启用此选项时，通用音频服务（CAS）将静态注册。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] param` | 协同集标识服务（Coordinated Set Identification Service）的注册参数。 |
| `[out] svc_inst` | 指向已注册的协同集标识服务（Coordinated Set Identification Service）的指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga25be83bb53c8e2ab76f311eaf4f615b9"></a>

### `bt_cap_commander_broadcast_reception_start()`

```c
int bt_cap_commander_broadcast_reception_start ( const struct bt_cap_commander_broadcast_reception_start_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

在一个或多个远端通用音频配置文件接受方（Common Audio Profile Acceptors）上启动广播音频接收。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 用于启动广播音频（Broadcast Audio）的参数。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="gac5b2b6d617a092fb98b23c41b2f52d15"></a>

### `bt_cap_commander_broadcast_reception_stop()`

```c
int bt_cap_commander_broadcast_reception_stop ( const struct bt_cap_commander_broadcast_reception_stop_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

在一个或多个远端通用音频配置文件接受方（Common Audio Profile Acceptors）上停止广播音频接收。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 用于停止广播音频（Broadcast Audio）的参数。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga7abf029533fed391930257605f3c752c"></a>

### `bt_cap_commander_cancel()`

```c
int bt_cap_commander_cancel ( void )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

取消当前任何通用音频配置文件指挥方过程（Common Audio Profile Commander Procedure）。

这会阻止当前流程继续执行，使得新的通用音频配置文件（CAP）流程可以运行。

现有流程耗时超过预期时，建议这样处理，因为这可能表明通用音频配置文件接受方（CAP Acceptor）缺少应答。

此操作不会向参与当前流程的任何 CAP 接受方（Acceptor）发送请求，因此调用后仍可能收到这些接受方的通知。为避免收到已取消流程的通知，建议仅在流程停滞时使用，或者在调用后稍等一段时间再启动新的 CAP 流程。等待时长取决于连接间隔、先前流程涉及的设备数量和接受方的行为。

此操作会调用该流程的相应回调，其中连接指针设为 `NULL`，`err` 值设为 `-ECANCELED`。

使用 `bt_cap_initiator_unicast_audio_cancel()` 取消 CAP 发起方（Initiator）流程；使用 `bt_cap_handover_cancel()` 取消 CAP 切换（Handover）流程。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EALREADY` | 没有活动流程时。 |
| `-EOPNOTSUPP` | 存在活动流程，但不是指挥方（Commander）流程。 |

<a id="ga958cd5925699624d23479ad2ace6b55b"></a>

### `bt_cap_commander_change_microphone_gain_setting()`

```c
int bt_cap_commander_change_microphone_gain_setting ( const struct bt_cap_commander_change_microphone_gain_setting_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的麦克风增益设置（Microphone Gain Setting）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 用于更改麦克风增益设置（Microphone Gain Setting）的参数。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga19cc7ed5992a528a7795b76e7add6d54"></a>

### `bt_cap_commander_change_microphone_mute_state()`

```c
int bt_cap_commander_change_microphone_mute_state ( const struct bt_cap_commander_change_microphone_mute_state_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的麦克风静音状态（Microphone Mute State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 用于更改麦克风静音状态（Microphone Mute State）的参数。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="gaff96953334eab1a38b30720b41c0d1a6"></a>

### `bt_cap_commander_change_volume()`

```c
int bt_cap_commander_change_volume ( const struct bt_cap_commander_change_volume_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的音量（Volume）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 用于更改音量（Volume）的参数。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="gac5f94baa82fa6deade6f83346a56b5e4"></a>

### `bt_cap_commander_change_volume_mute_state()`

```c
int bt_cap_commander_change_volume_mute_state ( const struct bt_cap_commander_change_volume_mute_state_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的音量静音状态（Volume Mute State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 用于更改音量静音状态（Volume Mute State）的参数。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="gae2cd451b387659b0a2021a9023d74dfa"></a>

### `bt_cap_commander_change_volume_offset()`

```c
int bt_cap_commander_change_volume_offset ( const struct bt_cap_commander_change_volume_offset_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的音量偏移（Volume Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 用于更改音量偏移（Volume Offset）的参数。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga165c67bddcbe220050293a4c73fb6ede"></a>

### `bt_cap_commander_discover()`

```c
int bt_cap_commander_discover ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

发现远端设备的音频支持（Audio Support）。

这会发现远端设备上的通用音频服务（CAS），以验证该设备是否支持通用音频配置文件（CAP）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端服务器的连接（Connection）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `conn` 为 `NULL`。 |
| `-ENOTCONN` | conn 未连接。 |
| `-ENOMEM` | 无法为请求分配内存。 |
| `-EBUSY` | 已在对 conn 执行发现（Discovery）。 |

**说明（Note）**：注（Note）：此函数要求启用 `CONFIG_BT_CAP_COMMANDER`。若同时启用 `CONFIG_BT_CAP_INITIATOR`，则使用 `bt_cap_commander_discover()` 或 `bt_cap_initiator_unicast_discover()` 均可。

<a id="gaf86582ad529b6ee801d1154db7e33827"></a>

### `bt_cap_commander_distribute_broadcast_code()`

```c
int bt_cap_commander_distribute_broadcast_code ( const struct bt_cap_commander_distribute_broadcast_code_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

向一个或多个远端通用音频配置文件接受方（Common Audio Profile Acceptors）分发广播码（Broadcast Code）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 用于分发广播码（Broadcast Code）的参数。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="gab6239c91b9d210872396860619fb8687"></a>

### `bt_cap_commander_register_cb()`

```c
int bt_cap_commander_register_cb ( const struct bt_cap_commander_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

注册通用音频配置文件指挥方（Common Audio Profile Commander）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Structure），必须保持静态存续。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | cb 为 NULL。 |
| `-EALREADY` | 回调已经注册。 |

<a id="ga38928945e67835983de3fc639c8f2764"></a>

### `bt_cap_commander_unregister_cb()`

```c
int bt_cap_commander_unregister_cb ( const struct bt_cap_commander_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

注销通用音频配置文件指挥方（Common Audio Profile Commander）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 先前注册的回调结构体（Callback Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | cb 为 NULL，或 cb 未注册。 |

<a id="ga92ff8b3133b8f5cb3d3029b5d556fe77"></a>

### `bt_cap_handover_broadcast_to_unicast()`

```c
int bt_cap_handover_broadcast_to_unicast ( const struct bt_cap_handover_broadcast_to_unicast_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

将广播源（Broadcast Source）中的数据流切换到单播组（Unicast Group）。

广播源（Broadcast Source）中的流将被停止，并删除该广播源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] param` | 切换（Handover）参数。 |

**注意（Attention）**：注意（Attention）：仅在启用以下 Kconfig 选项时可用：`CONFIG_BT_CAP_HANDOVER`。

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="gacd17de17ac1d96ff17ae15a63f43ad03"></a>

### `bt_cap_handover_cancel()`

```c
int bt_cap_handover_cancel ( void )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

取消当前任何通用音频配置文件切换过程（Common Audio Profile Handover Procedure）。

这会阻止当前流程继续执行，使得新的通用音频配置文件（CAP）流程可以运行。

现有流程耗时超过预期时，建议这样处理，因为这可能表明通用音频配置文件接受方（CAP Acceptor）缺少应答。

此操作不会向参与当前流程的任何 CAP 接受方（Acceptor）发送请求，因此调用后仍可能收到这些接受方的通知。为避免收到已取消流程的通知，建议仅在流程停滞时使用，或者在调用后稍等一段时间再启动新的 CAP 流程。等待时长取决于连接间隔、先前流程涉及的设备数量和接受方的行为。

此操作会调用该流程的相应回调，其中连接指针设为 0，`err` 值设为 `-ECANCELED`。

使用 `bt_cap_commander_cancel()` 取消 CAP 指挥方（Commander）流程；使用 `bt_cap_initiator_unicast_audio_cancel()` 取消 CAP 发起方（Initiator）流程。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EALREADY` | 没有活动流程时。 |
| `-EOPNOTSUPP` | 存在活动流程，但不是切换（Handover）流程。 |

<a id="ga5d8c66b3890e051b838d123a1911cfd6"></a>

### `bt_cap_handover_register_cb()`

```c
int bt_cap_handover_register_cb ( const struct bt_cap_handover_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

注册通用音频配置文件切换（Common Audio Profile Handover）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Structure），必须保持静态存续。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="gaae56deae3792740bc3e8074882c87837"></a>

### `bt_cap_handover_unicast_to_broadcast()`

```c
int bt_cap_handover_unicast_to_broadcast ( const struct bt_cap_handover_unicast_to_broadcast_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

将单播组（Unicast Group）中的接收端流（Sink Streams）切换到广播源（Broadcast Source）。

所提供单播组（Unicast Group）中的所有流都将停止并释放。接收端流（Sink Streams）将转移到广播源（Broadcast Source），广播源信息将共享给所有当前正在接收音频的接受方。任何不处于流传输状态（Streaming State）的流都只会被释放。

启动此流程前，必须已对 `param` 中所有成员成功执行 `bt_bap_broadcast_assistant_discover()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 切换（Handover）参数。 |

**注意（Attention）**：注意（Attention）：仅在启用以下 Kconfig 选项时可用：`CONFIG_BT_CAP_HANDOVER`。

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga808f0e5b671689196ba6f0fc1aea7427"></a>

### `bt_cap_handover_unregister_cb()`

```c
int bt_cap_handover_unregister_cb ( const struct bt_cap_handover_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

注销通用音频配置文件切换（Common Audio Profile Handover）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 先前注册的回调结构体（Callback Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | cb 为 NULL，或 cb 未注册。 |

<a id="ga78697225c6b1291dfc016e20fd605fc4"></a>

### `bt_cap_initiator_broadcast_audio_create()`

```c
int bt_cap_initiator_broadcast_audio_create ( const struct bt_cap_initiator_broadcast_create_param * param, struct bt_cap_broadcast_source ** broadcast_source )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

创建通用音频配置文件广播源（Common Audio Profile Broadcast Source）。

创建包含一个或多个音频流（Audio Streams）的新音频广播源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] param` | 用于启动音频流（Audio Streams）的参数。 |
| `[out] broadcast_source` | 指向已创建广播源的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `param` 无效，或 `broadcast_source` 为 `NULL`。 |
| `-ENOMEM` | 无法分配更多广播源（Broadcast Sources）、子组（Subgroups）或等时流（ISO Streams），或者合并 BIS 与子组配置数据时，提供的编解码器配置数据过大。 |
| `-ENOEXEC` | 因其他原因未能创建广播源（Broadcast Source）。 |

**说明（Note）**：注（Note）：启用此函数必须同时启用 `CONFIG_BT_CAP_INITIATOR` 和 `CONFIG_BT_BAP_BROADCAST_SOURCE`。

<a id="gac98ed5112d0ce0659bde86d149ea7b4c"></a>

### `bt_cap_initiator_broadcast_audio_delete()`

```c
int bt_cap_initiator_broadcast_audio_delete ( struct bt_cap_broadcast_source * broadcast_source)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

删除通用音频配置文件广播源（Common Audio Profile Broadcast Source）。

只有在调用 `bt_cap_initiator_broadcast_audio_stop()` 停止广播源，并且广播源中所有流的 `bt_bap_stream_ops.stopped()` 回调均已被调用后，才能执行此操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `broadcast_source` | 要删除的广播源（Broadcast Source）。`broadcast_source` 将失效。 |

**说明（Note）**：注（Note）：启用此函数必须同时启用 `CONFIG_BT_CAP_INITIATOR` 和 `CONFIG_BT_BAP_BROADCAST_SOURCE`。

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga2bd5f9c9de719a14ffc69827dbd4fa24"></a>

### `bt_cap_initiator_broadcast_audio_start()`

```c
int bt_cap_initiator_broadcast_audio_start ( struct bt_cap_broadcast_source * broadcast_source, struct bt_le_ext_adv * adv )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

启动通用音频配置文件广播源（Common Audio Profile Broadcast Source）。

调用后，扫描器即可发现广播源，设备开始广播音频公告（Audio Announcements）。

这将允许广播源（Broadcast Source）中的流通过调用 `bt_bap_stream_send()` 发送音频。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `broadcast_source` | 指向广播源（Broadcast Source）的指针。 |
| `adv` | 指向已配置周期广播（Periodic Advertising）的扩展广播集（Extended Advertising Set）的指针。 |

**说明（Note）**：注（Note）：启用此函数必须同时启用 `CONFIG_BT_CAP_INITIATOR` 和 `CONFIG_BT_BAP_BROADCAST_SOURCE`。

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="gae4e348f74e3c12e73879082d00cdb17e"></a>

### `bt_cap_initiator_broadcast_audio_stop()`

```c
int bt_cap_initiator_broadcast_audio_stop ( struct bt_cap_broadcast_source * broadcast_source)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

停止通用音频配置文件广播源（Common Audio Profile Broadcast Source）的广播音频流（Broadcast Audio Streams）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `broadcast_source` | 要停止的广播源（Broadcast Source）。其中的音频流将被停止并重置。 |

**说明（Note）**：注（Note）：启用此函数必须同时启用 `CONFIG_BT_CAP_INITIATOR` 和 `CONFIG_BT_BAP_BROADCAST_SOURCE`。

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga92336c4a56c667b608a86e45eb8d5073"></a>

### `bt_cap_initiator_broadcast_audio_update()`

```c
int bt_cap_initiator_broadcast_audio_update ( struct bt_cap_broadcast_source * broadcast_source, const uint8_t meta[], size_t meta_len )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

更新通用音频配置文件广播源（Common Audio Profile Broadcast Source）的广播音频流（Broadcast Audio Streams）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `broadcast_source` | 要更新的广播源（Broadcast Source）。 |
| `meta` | 新的元数据（Metadata）。必须包含 CCID 列表和非零的上下文位字段（Context Bitfield）。 |
| `meta_len` | `meta` 的长度（Length）。 |

**说明（Note）**：注（Note）：启用此函数必须同时启用 `CONFIG_BT_CAP_INITIATOR` 和 `CONFIG_BT_BAP_BROADCAST_SOURCE`。

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga45fa73b787bb4fefc73928acf3592e20"></a>

### `bt_cap_initiator_broadcast_foreach_stream()`

```c
int bt_cap_initiator_broadcast_foreach_stream ( struct bt_cap_broadcast_source * broadcast_source, bt_cap_initiator_broadcast_foreach_stream_func_t func, void * user_data )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

遍历广播源中的所有流（Streams）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `broadcast_source` | 广播源（Broadcast Source） |
| `func` | 回调函数。 |
| `user_data` | 发送给回调函数的用户指定数据 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功，即使组中没有流也视为成功。 |
| `-ECANCELED` | func 返回 false 并停止遍历。 |
| `-EINVAL` | `broadcast_source` 或 `func` 为 `NULL`。 |

<a id="ga71b1a73b9fd4b1be8a63a79e05c1c0aa"></a>

### `bt_cap_initiator_broadcast_get_base()`

```c
int bt_cap_initiator_broadcast_get_base ( struct bt_cap_broadcast_source * broadcast_source, struct net_buf_simple * base_buf )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

获取通用音频配置文件广播源（Common Audio Profile Broadcast Source）的广播音频流端点（Broadcast Audio Stream Endpoint）。

将广播源的 BASE 编码到缓冲区，以用于广播（Advertisement）。BASE 采用小端字节序（Little-endian）编码，必须放入周期广播数据（Periodic Advertising Data）；参见 bt_le_per_adv_set_data()。

结构见基本音频规范（Basic Audio Profile）v1.0.1 表 3.15。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `broadcast_source` | 指向广播源（Broadcast Source）的指针。 |
| `base_buf` | 指向将写入 BASE 的缓冲区的指针。 |

**返回（Returns）**：返回值（Returns）：`int`；成功时为 0，出错时为 `errno`。

<a id="ga54d7ad68f376998510aad9c3702e9364"></a>

### `bt_cap_initiator_register_cb()`

```c
int bt_cap_initiator_register_cb ( const struct bt_cap_initiator_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

注册通用音频配置文件发起方（Common Audio Profile Initiator）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Structure），必须保持静态存续。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga9fbddf102e29e8e969eade40fd60da4f"></a>

### `bt_cap_initiator_unicast_audio_cancel()`

```c
int bt_cap_initiator_unicast_audio_cancel ( void )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

取消当前任何通用音频配置文件发起方过程（Common Audio Profile Initiator Procedure）。

这会阻止当前流程继续执行，使得新的通用音频配置文件（CAP）流程可以运行。

现有流程耗时超过预期时，建议这样处理，因为这可能表明通用音频配置文件接受方（CAP Acceptor）缺少应答。

此操作不会向参与当前流程的任何 CAP 接受方（Acceptor）发送请求，因此调用后仍可能收到这些接受方的通知。为避免收到已取消流程的通知，建议仅在流程停滞时使用，或者在调用后稍等一段时间再启动新的 CAP 流程。等待时长取决于连接间隔、先前流程涉及的设备数量和接受方的行为。

此操作会调用该流程的相应回调，其中连接指针设为 0，`err` 值设为 `-ECANCELED`。

使用 `bt_cap_commander_cancel()` 取消 CAP 指挥方（Commander）流程；使用 `bt_cap_handover_cancel()` 取消 CAP 切换（Handover）流程。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EALREADY` | 没有活动流程时。 |
| `-EOPNOTSUPP` | 存在活动流程，但不是发起方（Initiator）流程。 |

<a id="gae19686be7f8aef1cc92c70fea93e1184"></a>

### `bt_cap_initiator_unicast_audio_start()`

```c
int bt_cap_initiator_unicast_audio_start ( const struct bt_cap_unicast_audio_start_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

为一组设备建立并启动单播音频流（Unicast Audio Streams）。

此操作将初始化 `param` 中的流，使其可以传输音频数据。可使用 `unicast_group` 值来更新和停止这些流。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 用于启动音频流（Audio Streams）的参数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EBUSY` | 已有 CAP 流程正在进行时。 |
| `-EINVAL` | 任一参数无效时。 |
| `-EALREADY` | 所有流均已处于流传输状态（Streaming State）。 |

**说明（Note）**：注（Note）：启用此函数必须同时启用 `CONFIG_BT_CAP_INITIATOR` 和 `CONFIG_BT_BAP_UNICAST_CLIENT`。

<a id="gafdf6f1656249ab3ae6296272dc36b66f"></a>

### `bt_cap_initiator_unicast_audio_stop()`

```c
int bt_cap_initiator_unicast_audio_stop ( const struct bt_cap_unicast_audio_stop_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

停止单播音频流（Unicast Audio Streams）。

这会停止一个或多个流（Streams）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 停止参数（Stop Parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EBUSY` | 已有 CAP 流程正在进行时。 |
| `-EINVAL` | 任一参数无效时。 |
| `-EALREADY` | 不会发生状态变化时。 |

**说明（Note）**：注（Note）：启用此函数必须同时启用 `CONFIG_BT_CAP_INITIATOR` 和 `CONFIG_BT_BAP_UNICAST_CLIENT`。

返回（Returns）：成功为0。

<a id="ga92e4e2c12720ec25c4050cde307cd639"></a>

### `bt_cap_initiator_unicast_audio_update()`

```c
int bt_cap_initiator_unicast_audio_update ( const struct bt_cap_unicast_audio_update_param * param)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

更新单播音频流（Unicast Audio Streams）。

这会更新一个或多个流的元数据（Metadata）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 更新参数（Update Parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EBUSY` | CAP 流程已在进行。 |
| `-EINVAL` | `param` 包含无效参数。 |
| `-EALREADY` | 所有流都已经设置了该元数据（Metadata）。 |

**说明（Note）**：注（Note）：启用此函数必须同时启用 `CONFIG_BT_CAP_INITIATOR` 和 `CONFIG_BT_BAP_UNICAST_CLIENT`。

<a id="gab7b273d06abf9a3cb43afdd4e3c30c8d"></a>

### `bt_cap_initiator_unicast_discover()`

```c
int bt_cap_initiator_unicast_discover ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

发现远端设备的音频支持（Audio Support）。

这会发现远端设备上的通用音频服务（CAS），以验证该设备是否支持通用音频配置文件（CAP）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端服务器的连接（Connection）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `conn` 为 `NULL`。 |
| `-ENOTCONN` | conn 未连接。 |
| `-ENOMEM` | 无法为请求分配内存。 |

<a id="gaa7286837f37da38afec8c5c955306b61"></a>

### `bt_cap_initiator_unregister_cb()`

```c
int bt_cap_initiator_unregister_cb ( const struct bt_cap_initiator_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

注销通用音频配置文件发起方（Common Audio Profile Initiator）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 先前注册的回调结构体（Callback Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | cb 为 NULL，或 cb 未注册。 |

<a id="ga7f3f6e98e7720a4711b658c4b7c85235"></a>

### `bt_cap_stream_get_tx_sync()`

```c
int bt_cap_stream_get_tx_sync ( struct bt_cap_stream * stream, struct bt_iso_tx_info * info )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

获取通用音频配置文件（Common Audio Profile）流的等时传输时序信息（ISO Transmission Timing Info）。

更多信息参见 `bt_bap_stream_get_tx_sync()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 流对象（Stream Object）。 |
| `[out] info` | 发送信息对象（Transmit Info Object）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `stream` 对象为 `NULL` 时。 |
| `Any` | 来自 `bt_bap_stream_get_tx_sync()` 的返回值。 |

**说明（Note）**：注（Note）：必须支持发送，该能力由 `CONFIG_BT_AUDIO_TX` 决定。

<a id="gac909b00d53cf35103382f0e1d9f426b7"></a>

### `bt_cap_stream_ops_register()`

```c
void bt_cap_stream_ops_register ( struct bt_cap_stream * stream, struct bt_bap_stream_ops * ops )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

为通用音频配置文件（Common Audio Profile）流注册音频操作（Audio Operations）。

为流注册音频操作（Audio Operations）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |
| `ops` | 流操作结构体（Stream Operations Structure）。 |

<a id="ga2d8b15543105078b793462b762e27741"></a>

### `bt_cap_stream_send()`

```c
int bt_cap_stream_send ( struct bt_cap_stream * stream, struct net_buf * buf, uint16_t seq_num )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

向通用音频配置文件（Common Audio Profile）流发送不带时间戳（Timestamp）的数据。

更多信息参见 `bt_bap_stream_send()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |
| `buf` | 包含待发送数据的缓冲区。 |
| `seq_num` | 分组序列号（Packet Sequence Number）。对此函数的每次调用都必须递增该值；对于特定通道，每个 SDU 间隔内至少递增一次。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `stream` 对象为 `NULL` 时。 |
| `Any` | 来自 `bt_bap_stream_send()` 的返回值。 |

**说明（Note）**：注（Note）：必须支持发送，该能力由 `CONFIG_BT_AUDIO_TX` 决定。

<a id="ga23618d1ab7690c4d3a567228c857c89e"></a>

### `bt_cap_stream_send_ts()`

```c
int bt_cap_stream_send_ts ( struct bt_cap_stream * stream, struct net_buf * buf, uint16_t seq_num, uint32_t ts )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

向通用音频配置文件（Common Audio Profile）流发送带时间戳（Timestamp）的数据。

更多信息参见 `bt_bap_stream_send()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |
| `buf` | 包含待发送数据的缓冲区。 |
| `seq_num` | 分组序列号（Packet Sequence Number）。对此函数的每次调用都必须递增该值；对于特定通道，每个 SDU 间隔内至少递增一次。 |
| `ts` | 服务数据单元（SDU）的时间戳，单位为微秒（µs）。可使用此值，在连接等时组（CIG）或广播等时组（BIG）的同一个 SDU 间隔内发送多个 SDU。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `stream` 对象为 `NULL` 时。 |
| `Any` | 来自 `bt_bap_stream_send()` 的返回值。 |

**说明（Note）**：注（Note）：必须支持发送，该能力由 `CONFIG_BT_AUDIO_TX` 决定。

<a id="ga7b5d30c07e57f4db23f72836a3b12b2b"></a>

### `bt_cap_unicast_group_add_streams()`

```c
int bt_cap_unicast_group_add_streams ( struct bt_cap_unicast_group * unicast_group, const struct bt_cap_unicast_group_stream_pair_param params[], size_t num_param )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

以单播客户端（Unicast Client）身份向单播组添加流（Streams）。

此函数可向 `bt_cap_unicast_group` 添加更多流（Streams）。

可以在组中任何流启动之前调用，参见 bt_bap_stream_ops.started()；也可以在流停止之后调用，参见 bt_bap_stream_ops.stopped()。

流加入单播组（Unicast Group）后便不能移除。若要从组中移除流，必须先释放组内所有流，再使用 `bt_cap_unicast_group_delete()` 删除该组。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `unicast_group` | 指向单播组（Unicast Group）的指针。 |
| `params` | 流参数数组（Stream Parameters Array），其中的流将被添加到组中。 |
| `num_param` | params 中的参数数量。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gab49e8c2032a824516dc8d5f2f880dd8f"></a>

### `bt_cap_unicast_group_create()`

```c
int bt_cap_unicast_group_create ( const struct bt_cap_unicast_group_param * param, struct bt_cap_unicast_group ** out_unicast_group )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

创建单播组（Unicast Group）。

以单播客户端（Unicast Client）身份创建包含一个或多个音频流的新音频单播组（Audio Unicast Group）。所有流必须使用相同的成帧方式（Framing）；同一方向的所有流必须使用相同的间隔（Interval）和延迟（Latency），参见 bt_bap_qos_cfg。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] param` | 单播组创建参数（Unicast Group Create Parameters）。 |
| `[out] out_unicast_group` | 指向已创建单播组（Unicast Group）的指针。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga9af37b30b6c858c24892eb1739b5330a"></a>

### `bt_cap_unicast_group_delete()`

```c
int bt_cap_unicast_group_delete ( struct bt_cap_unicast_group * unicast_group)
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

删除音频单播组（Audio Unicast Group）。

以客户端身份删除音频单播组（Audio Unicast Group）。组中的所有流都必须处于空闲状态（Idle）或已配置状态（Configured）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `unicast_group` | 指向待删除单播组（Unicast Group）的指针。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga6c13996298c3e3aa33eb40f74b7bfe44"></a>

### `bt_cap_unicast_group_foreach_stream()`

```c
int bt_cap_unicast_group_foreach_stream ( struct bt_cap_unicast_group * unicast_group, bt_cap_unicast_group_foreach_stream_func_t func, void * user_data )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

遍历单播组（Unicast Group）中的全部流。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `unicast_group` | 单播组（Unicast Group）。 |
| `func` | 回调函数。 |
| `user_data` | 发送给回调函数的用户指定数据 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功，即使组中没有流也视为成功。 |
| `-ECANCELED` | func 返回 false 并停止遍历。 |
| `-EINVAL` | unicast_group 或 func 为 NULL。 |

<a id="ga86aca9c7f2f8658f4486925c68148850"></a>

### `bt_cap_unicast_group_get_info()`

```c
int bt_cap_unicast_group_get_info ( const struct bt_cap_unicast_group * unicast_group, struct bt_cap_unicast_group_info * info )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

返回保存单播组信息（Unicast Group Information）的结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `unicast_group` | 单播组对象（Unicast Group Object）。 |
| `info` | 要用信息填充的结构体对象（Structure Object）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | unicast_group 或 info 为 NULL。 |

<a id="ga6c862b49aa1339225aeb05fad32c2f06"></a>

### `bt_cap_unicast_group_reconfig()`

```c
int bt_cap_unicast_group_reconfig ( struct bt_cap_unicast_group * unicast_group, const struct bt_cap_unicast_group_param * param )
```

```c
#include <zephyr/bluetooth/audio/cap.h>
```

重新配置单播组（Unicast Group）。

以单播客户端（Unicast Client）身份，使用一个或多个音频流重新配置单播组。所有流必须使用相同的成帧方式（Framing）；同一方向的所有流必须具有相同的间隔和延迟，参见 `bt_bap_qos_cfg`。`param` 中的所有流都必须已经属于 `unicast_group`；添加额外流请使用 `bt_cap_unicast_group_add_streams()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `unicast_group` | 指向已创建单播组（Unicast Group）的指针。 |
| `param` | 单播组重新配置参数（Unicast Group Reconfigure Parameters）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。


## 2.6\_原页交叉引用（Cross References）

- [bt_cap_initiator_cb](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md)
- [bt_cap_set_member](../bluetooth_service_model_reference/P188_bt_cap_set_member_联合体.md)
- [bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)
- [bt_cap_unicast_group_stream_param](../bluetooth_service_model_reference/P049_bt_cap_unicast_group_stream_param_结构体.md)
- [bt_cap_unicast_group_stream_pair_param](../bluetooth_service_model_reference/P048_bt_cap_unicast_group_stream_pair_param_结构体.md)
- [bt_cap_unicast_group_param](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md)
- [bt_cap_unicast_group_info](../bluetooth_service_model_reference/P046_bt_cap_unicast_group_info_结构体.md)
- [bt_cap_unicast_audio_start_stream_param](../bluetooth_service_model_reference/P041_bt_cap_unicast_audio_start_stream_param_结构体.md)
- [bt_cap_unicast_audio_start_param](../bluetooth_service_model_reference/P040_bt_cap_unicast_audio_start_param_结构体.md)
- [bt_cap_unicast_audio_update_stream_param](../bluetooth_service_model_reference/P044_bt_cap_unicast_audio_update_stream_param_结构体.md)
- [bt_cap_unicast_audio_update_param](../bluetooth_service_model_reference/P043_bt_cap_unicast_audio_update_param_结构体.md)
- [bt_cap_unicast_audio_stop_param](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md)
- [bt_cap_initiator_broadcast_stream_param](../bluetooth_service_model_reference/P036_bt_cap_initiator_broadcast_stream_param_结构体.md)
- [bt_cap_initiator_broadcast_subgroup_param](../bluetooth_service_model_reference/P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md)
- [bt_cap_initiator_broadcast_create_param](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md)
- [bt_cap_handover_unicast_to_broadcast_param](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md)
- [bt_cap_handover_cb](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md)
- [bt_cap_handover_broadcast_to_unicast_param](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md)
- [bt_cap_commander_cb](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md)
- [bt_cap_commander_broadcast_reception_start_member_param](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md)
- [bt_cap_commander_broadcast_reception_start_param](../bluetooth_service_model_reference/P019_bt_cap_commander_broadcast_reception_start_param_结构体.md)
- [bt_cap_commander_broadcast_reception_stop_member_param](../bluetooth_service_model_reference/P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md)
- [bt_cap_commander_broadcast_reception_stop_param](../bluetooth_service_model_reference/P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md)
- [bt_cap_commander_distribute_broadcast_code_member_param](../bluetooth_service_model_reference/P030_bt_cap_commander_distribute_broadcast_code_member_param_结构体.md)
- [bt_cap_commander_distribute_broadcast_code_param](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md)
- [bt_cap_commander_change_volume_param](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md)
- [bt_cap_commander_change_volume_offset_member_param](../bluetooth_service_model_reference/P027_bt_cap_commander_change_volume_offset_member_param_结构体.md)
- [bt_cap_commander_change_volume_offset_param](../bluetooth_service_model_reference/P028_bt_cap_commander_change_volume_offset_param_结构体.md)
- [bt_cap_commander_change_volume_mute_state_param](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md)
- [bt_cap_commander_change_microphone_mute_state_param](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md)
- [bt_cap_commander_change_microphone_gain_setting_member_param](../bluetooth_service_model_reference/P023_bt_cap_commander_change_microphone_gain_setting_member_param_结构体.md)
- [bt_cap_commander_change_microphone_gain_setting_param](../bluetooth_service_model_reference/P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md)
- [bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)
- [bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_csip_set_member_register_param](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md)
- [bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [zephyr/bluetooth/audio/cap.h](../api_file_audio_test_reference/P004_zephyr__bluetooth__audio__cap.h_文件参考.md)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [CONFIG_BT_CAP_ACCEPTOR_SET_MEMBER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CAP_ACCEPTOR_SET_MEMBER)
- [CONFIG_BT_CAP_COMMANDER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CAP_COMMANDER)
- [CONFIG_BT_CAP_INITIATOR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CAP_INITIATOR)
- [CONFIG_BT_CAP_HANDOVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CAP_HANDOVER)
- [bt_bap_broadcast_assistant_discover()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gab59c5ebc4fef28da34d8a54b1244c33b)
- [CONFIG_BT_BAP_BROADCAST_SOURCE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_BROADCAST_SOURCE)
- [bt_bap_stream_ops.stopped()](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#ab50ea295069a2cd1ab6f4353052262f5)
- [bt_bap_stream_send()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga63b69967aa92224a2bd9cf79eb41773e)
- [bt_le_per_adv_set_data()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gafd0e7ccca93a8347a4ca6cca88e77899)
- [CONFIG_BT_BAP_UNICAST_CLIENT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_UNICAST_CLIENT)
- [bt_bap_stream_get_tx_sync()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga47eb6219d730d75ddc4f49dceac7e928)
- [CONFIG_BT_AUDIO_TX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUDIO_TX)
- [bt_bap_stream_ops.started()](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a7f595e37d40b94510bf09c1f82b479f3)
- [bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468"></a>
<a id="ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md) · [返回大纲](大纲.md) · [下一章](P003_嵌入式控制器主机命令接口（EC Host Command Interface）.md)
