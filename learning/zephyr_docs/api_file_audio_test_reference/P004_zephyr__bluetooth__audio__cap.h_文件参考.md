---
id: learning.zephyr-docs.api-file-audio-test-reference.page-4
title: zephyr__bluetooth__audio__cap.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_bluetooth\_\_audio\_\_cap.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙通用音频配置文件（Common Audio Profile，CAP）的API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/audio/bap.h>
#include <zephyr/bluetooth/audio/csip.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/iso.h>
#include <zephyr/net_buf.h>
```

查看此文件的源码。

蓝牙通用音频配置文件（Common Audio Profile，CAP）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

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

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.2\_类型定义（Typedefs）

<a id="r_gaeaad4ea5142afe5dca741b72795ae3aa"></a>

```c
typedef bool(* bt_cap_unicast_group_foreach_stream_func_t) (struct bt_cap_stream *stream, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_cap_unicast_group_foreach_stream_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaeaad4ea5142afe5dca741b72795ae3aa)、[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)。

bt_cap_unicast_group_foreach_stream() 的回调函数（Callback Function）。

<a id="r_ga2c6dc73fb44bca1f5bf8d39d46690b30"></a>

```c
typedef bool(* bt_cap_initiator_broadcast_foreach_stream_func_t) (struct bt_cap_stream *stream, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_cap_initiator_broadcast_foreach_stream_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga2c6dc73fb44bca1f5bf8d39d46690b30)、[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)。

bt_cap_initiator_broadcast_foreach_stream() 的回调函数（Callback Function）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.3\_枚举（Enumerations）

<a id="r_gac9d750d0a22fab7852f0a04757feab6a"></a>

```c
enum bt_cap_set_type { BT_CAP_SET_TYPE_AD_HOC , BT_CAP_SET_TYPE_CSIP }
```

相关声明：[bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)、[BT_CAP_SET_TYPE_AD_HOC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468)、[BT_CAP_SET_TYPE_CSIP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4)。

通用音频配置文件集合类型（CAP Set Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_gafcb9ea2122ff8058321cf85a22326abe"></a>

```c
int bt_cap_acceptor_register (const struct bt_csip_set_member_register_param *param, struct bt_csip_set_member_svc_inst **svc_inst)
```

相关声明：[bt_cap_acceptor_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gafcb9ea2122ff8058321cf85a22326abe)、[bt_csip_set_member_register_param](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md)、[bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)。

注册通用音频服务（Common Audio Service）。

<a id="r_gab7b273d06abf9a3cb43afdd4e3c30c8d"></a>

```c
int bt_cap_initiator_unicast_discover (struct bt_conn *conn)
```

相关声明：[bt_cap_initiator_unicast_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab7b273d06abf9a3cb43afdd4e3c30c8d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现远端设备的音频支持（Audio Support）。

<a id="r_gac909b00d53cf35103382f0e1d9f426b7"></a>

```c
void bt_cap_stream_ops_register (struct bt_cap_stream *stream, struct bt_bap_stream_ops *ops)
```

相关声明：[bt_cap_stream_ops_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac909b00d53cf35103382f0e1d9f426b7)、[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)、[bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)。

为通用音频配置文件（Common Audio Profile）流注册音频操作（Audio Operations）。

<a id="r_ga2d8b15543105078b793462b762e27741"></a>

```c
int bt_cap_stream_send (struct bt_cap_stream *stream, struct net_buf *buf, uint16_t seq_num)
```

相关声明：[bt_cap_stream_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga2d8b15543105078b793462b762e27741)、[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向通用音频配置文件（Common Audio Profile）流发送不带时间戳（Timestamp）的数据。

<a id="r_ga23618d1ab7690c4d3a567228c857c89e"></a>

```c
int bt_cap_stream_send_ts (struct bt_cap_stream *stream, struct net_buf *buf, uint16_t seq_num, uint32_t ts)
```

相关声明：[bt_cap_stream_send_ts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga23618d1ab7690c4d3a567228c857c89e)、[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向通用音频配置文件（Common Audio Profile）流发送带时间戳（Timestamp）的数据。

<a id="r_ga7f3f6e98e7720a4711b658c4b7c85235"></a>

```c
int bt_cap_stream_get_tx_sync (struct bt_cap_stream *stream, struct bt_iso_tx_info *info)
```

相关声明：[bt_cap_stream_get_tx_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga7f3f6e98e7720a4711b658c4b7c85235)、[bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)、[bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)。

获取通用音频配置文件（Common Audio Profile）流的等时传输时序信息（ISO Transmission Timing Info）。

<a id="r_gab49e8c2032a824516dc8d5f2f880dd8f"></a>

```c
int bt_cap_unicast_group_create (const struct bt_cap_unicast_group_param *param, struct bt_cap_unicast_group **out_unicast_group)
```

相关声明：[bt_cap_unicast_group_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab49e8c2032a824516dc8d5f2f880dd8f)、[bt_cap_unicast_group_param](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md)、[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)。

创建单播组（Unicast Group）。

<a id="r_ga6c862b49aa1339225aeb05fad32c2f06"></a>

```c
int bt_cap_unicast_group_reconfig (struct bt_cap_unicast_group *unicast_group, const struct bt_cap_unicast_group_param *param)
```

相关声明：[bt_cap_unicast_group_reconfig](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga6c862b49aa1339225aeb05fad32c2f06)、[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)、[bt_cap_unicast_group_param](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md)。

重新配置单播组（Unicast Group）。

<a id="r_ga7b5d30c07e57f4db23f72836a3b12b2b"></a>

```c
int bt_cap_unicast_group_add_streams (struct bt_cap_unicast_group *unicast_group, const struct bt_cap_unicast_group_stream_pair_param params[], size_t num_param)
```

相关声明：[bt_cap_unicast_group_add_streams](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga7b5d30c07e57f4db23f72836a3b12b2b)、[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)、[bt_cap_unicast_group_stream_pair_param](../bluetooth_service_model_reference/P048_bt_cap_unicast_group_stream_pair_param_结构体.md)。

以单播客户端（Unicast Client）身份向单播组添加流（Streams）。

<a id="r_ga9af37b30b6c858c24892eb1739b5330a"></a>

```c
int bt_cap_unicast_group_delete (struct bt_cap_unicast_group *unicast_group)
```

相关声明：[bt_cap_unicast_group_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga9af37b30b6c858c24892eb1739b5330a)、[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)。

删除音频单播组（Audio Unicast Group）。

<a id="r_ga6c13996298c3e3aa33eb40f74b7bfe44"></a>

```c
int bt_cap_unicast_group_foreach_stream (struct bt_cap_unicast_group *unicast_group, bt_cap_unicast_group_foreach_stream_func_t func, void *user_data)
```

相关声明：[bt_cap_unicast_group_foreach_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga6c13996298c3e3aa33eb40f74b7bfe44)、[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)、[bt_cap_unicast_group_foreach_stream_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaeaad4ea5142afe5dca741b72795ae3aa)。

遍历单播组（Unicast Group）中的全部流。

<a id="r_ga86aca9c7f2f8658f4486925c68148850"></a>

```c
int bt_cap_unicast_group_get_info (const struct bt_cap_unicast_group *unicast_group, struct bt_cap_unicast_group_info *info)
```

相关声明：[bt_cap_unicast_group_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga86aca9c7f2f8658f4486925c68148850)、[bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)、[bt_cap_unicast_group_info](../bluetooth_service_model_reference/P046_bt_cap_unicast_group_info_结构体.md)。

返回保存单播组信息（Unicast Group Information）的结构体。

<a id="r_ga54d7ad68f376998510aad9c3702e9364"></a>

```c
int bt_cap_initiator_register_cb (const struct bt_cap_initiator_cb *cb)
```

相关声明：[bt_cap_initiator_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga54d7ad68f376998510aad9c3702e9364)、[bt_cap_initiator_cb](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md)。

注册通用音频配置文件发起方（Common Audio Profile Initiator）的回调。

<a id="r_gaa7286837f37da38afec8c5c955306b61"></a>

```c
int bt_cap_initiator_unregister_cb (const struct bt_cap_initiator_cb *cb)
```

相关声明：[bt_cap_initiator_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaa7286837f37da38afec8c5c955306b61)、[bt_cap_initiator_cb](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md)。

注销通用音频配置文件发起方（Common Audio Profile Initiator）的回调。

<a id="r_gae19686be7f8aef1cc92c70fea93e1184"></a>

```c
int bt_cap_initiator_unicast_audio_start (const struct bt_cap_unicast_audio_start_param *param)
```

相关声明：[bt_cap_initiator_unicast_audio_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae19686be7f8aef1cc92c70fea93e1184)、[bt_cap_unicast_audio_start_param](../bluetooth_service_model_reference/P040_bt_cap_unicast_audio_start_param_结构体.md)。

为一组设备建立并启动单播音频流（Unicast Audio Streams）。

<a id="r_ga92e4e2c12720ec25c4050cde307cd639"></a>

```c
int bt_cap_initiator_unicast_audio_update (const struct bt_cap_unicast_audio_update_param *param)
```

相关声明：[bt_cap_initiator_unicast_audio_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92e4e2c12720ec25c4050cde307cd639)、[bt_cap_unicast_audio_update_param](../bluetooth_service_model_reference/P043_bt_cap_unicast_audio_update_param_结构体.md)。

更新单播音频流（Unicast Audio Streams）。

<a id="r_gafdf6f1656249ab3ae6296272dc36b66f"></a>

```c
int bt_cap_initiator_unicast_audio_stop (const struct bt_cap_unicast_audio_stop_param *param)
```

相关声明：[bt_cap_initiator_unicast_audio_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gafdf6f1656249ab3ae6296272dc36b66f)、[bt_cap_unicast_audio_stop_param](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md)。

停止单播音频流（Unicast Audio Streams）。

<a id="r_ga9fbddf102e29e8e969eade40fd60da4f"></a>

```c
int bt_cap_initiator_unicast_audio_cancel (void)
```

相关声明：[bt_cap_initiator_unicast_audio_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga9fbddf102e29e8e969eade40fd60da4f)。

取消当前任何通用音频配置文件发起方过程（Common Audio Profile Initiator Procedure）。

<a id="r_ga78697225c6b1291dfc016e20fd605fc4"></a>

```c
int bt_cap_initiator_broadcast_audio_create (const struct bt_cap_initiator_broadcast_create_param *param, struct bt_cap_broadcast_source **broadcast_source)
```

相关声明：[bt_cap_initiator_broadcast_audio_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga78697225c6b1291dfc016e20fd605fc4)、[bt_cap_initiator_broadcast_create_param](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)。

创建通用音频配置文件广播源（Common Audio Profile Broadcast Source）。

<a id="r_ga2bd5f9c9de719a14ffc69827dbd4fa24"></a>

```c
int bt_cap_initiator_broadcast_audio_start (struct bt_cap_broadcast_source *broadcast_source, struct bt_le_ext_adv *adv)
```

相关声明：[bt_cap_initiator_broadcast_audio_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga2bd5f9c9de719a14ffc69827dbd4fa24)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

启动通用音频配置文件广播源（Common Audio Profile Broadcast Source）。

<a id="r_ga92336c4a56c667b608a86e45eb8d5073"></a>

```c
int bt_cap_initiator_broadcast_audio_update (struct bt_cap_broadcast_source *broadcast_source, const uint8_t meta[], size_t meta_len)
```

相关声明：[bt_cap_initiator_broadcast_audio_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92336c4a56c667b608a86e45eb8d5073)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新通用音频配置文件广播源（Common Audio Profile Broadcast Source）的广播音频流（Broadcast Audio Streams）。

<a id="r_gae4e348f74e3c12e73879082d00cdb17e"></a>

```c
int bt_cap_initiator_broadcast_audio_stop (struct bt_cap_broadcast_source *broadcast_source)
```

相关声明：[bt_cap_initiator_broadcast_audio_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae4e348f74e3c12e73879082d00cdb17e)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)。

停止通用音频配置文件广播源（Common Audio Profile Broadcast Source）的广播音频流（Broadcast Audio Streams）。

<a id="r_gac98ed5112d0ce0659bde86d149ea7b4c"></a>

```c
int bt_cap_initiator_broadcast_audio_delete (struct bt_cap_broadcast_source *broadcast_source)
```

相关声明：[bt_cap_initiator_broadcast_audio_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac98ed5112d0ce0659bde86d149ea7b4c)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)。

删除通用音频配置文件广播源（Common Audio Profile Broadcast Source）。

<a id="r_ga71b1a73b9fd4b1be8a63a79e05c1c0aa"></a>

```c
int bt_cap_initiator_broadcast_get_base (struct bt_cap_broadcast_source *broadcast_source, struct net_buf_simple *base_buf)
```

相关声明：[bt_cap_initiator_broadcast_get_base](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

获取通用音频配置文件广播源（Common Audio Profile Broadcast Source）的广播音频流端点（Broadcast Audio Stream Endpoint）。

<a id="r_ga45fa73b787bb4fefc73928acf3592e20"></a>

```c
int bt_cap_initiator_broadcast_foreach_stream (struct bt_cap_broadcast_source *broadcast_source, bt_cap_initiator_broadcast_foreach_stream_func_t func, void *user_data)
```

相关声明：[bt_cap_initiator_broadcast_foreach_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga45fa73b787bb4fefc73928acf3592e20)、[bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)、[bt_cap_initiator_broadcast_foreach_stream_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga2c6dc73fb44bca1f5bf8d39d46690b30)。

遍历广播源中的所有流（Streams）。

<a id="r_ga5d8c66b3890e051b838d123a1911cfd6"></a>

```c
int bt_cap_handover_register_cb (const struct bt_cap_handover_cb *cb)
```

相关声明：[bt_cap_handover_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga5d8c66b3890e051b838d123a1911cfd6)、[bt_cap_handover_cb](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md)。

注册通用音频配置文件切换（Common Audio Profile Handover）的回调。

<a id="r_ga808f0e5b671689196ba6f0fc1aea7427"></a>

```c
int bt_cap_handover_unregister_cb (const struct bt_cap_handover_cb *cb)
```

相关声明：[bt_cap_handover_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga808f0e5b671689196ba6f0fc1aea7427)、[bt_cap_handover_cb](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md)。

注销通用音频配置文件切换（Common Audio Profile Handover）的回调。

<a id="r_gaae56deae3792740bc3e8074882c87837"></a>

```c
int bt_cap_handover_unicast_to_broadcast (const struct bt_cap_handover_unicast_to_broadcast_param *param)
```

相关声明：[bt_cap_handover_unicast_to_broadcast](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaae56deae3792740bc3e8074882c87837)、[bt_cap_handover_unicast_to_broadcast_param](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md)。

将单播组（Unicast Group）中的接收端流（Sink Streams）切换到广播源（Broadcast Source）。

<a id="r_ga92ff8b3133b8f5cb3d3029b5d556fe77"></a>

```c
int bt_cap_handover_broadcast_to_unicast (const struct bt_cap_handover_broadcast_to_unicast_param *param)
```

相关声明：[bt_cap_handover_broadcast_to_unicast](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92ff8b3133b8f5cb3d3029b5d556fe77)、[bt_cap_handover_broadcast_to_unicast_param](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md)。

将广播源（Broadcast Source）中的数据流切换到单播组（Unicast Group）。

<a id="r_gacd17de17ac1d96ff17ae15a63f43ad03"></a>

```c
int bt_cap_handover_cancel (void)
```

相关声明：[bt_cap_handover_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gacd17de17ac1d96ff17ae15a63f43ad03)。

取消当前任何通用音频配置文件切换过程（Common Audio Profile Handover Procedure）。

<a id="r_gab6239c91b9d210872396860619fb8687"></a>

```c
int bt_cap_commander_register_cb (const struct bt_cap_commander_cb *cb)
```

相关声明：[bt_cap_commander_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab6239c91b9d210872396860619fb8687)、[bt_cap_commander_cb](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md)。

注册通用音频配置文件指挥方（Common Audio Profile Commander）的回调。

<a id="r_ga38928945e67835983de3fc639c8f2764"></a>

```c
int bt_cap_commander_unregister_cb (const struct bt_cap_commander_cb *cb)
```

相关声明：[bt_cap_commander_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga38928945e67835983de3fc639c8f2764)、[bt_cap_commander_cb](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md)。

注销通用音频配置文件指挥方（Common Audio Profile Commander）的回调。

<a id="r_ga165c67bddcbe220050293a4c73fb6ede"></a>

```c
int bt_cap_commander_discover (struct bt_conn *conn)
```

相关声明：[bt_cap_commander_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga165c67bddcbe220050293a4c73fb6ede)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现远端设备的音频支持（Audio Support）。

<a id="r_ga7abf029533fed391930257605f3c752c"></a>

```c
int bt_cap_commander_cancel (void)
```

相关声明：[bt_cap_commander_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga7abf029533fed391930257605f3c752c)。

取消当前任何通用音频配置文件指挥方过程（Common Audio Profile Commander Procedure）。

<a id="r_ga25be83bb53c8e2ab76f311eaf4f615b9"></a>

```c
int bt_cap_commander_broadcast_reception_start (const struct bt_cap_commander_broadcast_reception_start_param *param)
```

相关声明：[bt_cap_commander_broadcast_reception_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga25be83bb53c8e2ab76f311eaf4f615b9)、[bt_cap_commander_broadcast_reception_start_param](../bluetooth_service_model_reference/P019_bt_cap_commander_broadcast_reception_start_param_结构体.md)。

在一个或多个远端通用音频配置文件接受方（Common Audio Profile Acceptors）上启动广播音频接收。

<a id="r_gac5b2b6d617a092fb98b23c41b2f52d15"></a>

```c
int bt_cap_commander_broadcast_reception_stop (const struct bt_cap_commander_broadcast_reception_stop_param *param)
```

相关声明：[bt_cap_commander_broadcast_reception_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac5b2b6d617a092fb98b23c41b2f52d15)、[bt_cap_commander_broadcast_reception_stop_param](../bluetooth_service_model_reference/P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md)。

在一个或多个远端通用音频配置文件接受方（Common Audio Profile Acceptors）上停止广播音频接收。

<a id="r_gaf86582ad529b6ee801d1154db7e33827"></a>

```c
int bt_cap_commander_distribute_broadcast_code (const struct bt_cap_commander_distribute_broadcast_code_param *param)
```

相关声明：[bt_cap_commander_distribute_broadcast_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaf86582ad529b6ee801d1154db7e33827)、[bt_cap_commander_distribute_broadcast_code_param](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md)。

向一个或多个远端通用音频配置文件接受方（Common Audio Profile Acceptors）分发广播码（Broadcast Code）。

<a id="r_gaff96953334eab1a38b30720b41c0d1a6"></a>

```c
int bt_cap_commander_change_volume (const struct bt_cap_commander_change_volume_param *param)
```

相关声明：[bt_cap_commander_change_volume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaff96953334eab1a38b30720b41c0d1a6)、[bt_cap_commander_change_volume_param](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md)。

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的音量（Volume）。

<a id="r_gae2cd451b387659b0a2021a9023d74dfa"></a>

```c
int bt_cap_commander_change_volume_offset (const struct bt_cap_commander_change_volume_offset_param *param)
```

相关声明：[bt_cap_commander_change_volume_offset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae2cd451b387659b0a2021a9023d74dfa)、[bt_cap_commander_change_volume_offset_param](../bluetooth_service_model_reference/P028_bt_cap_commander_change_volume_offset_param_结构体.md)。

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的音量偏移（Volume Offset）。

<a id="r_gac5f94baa82fa6deade6f83346a56b5e4"></a>

```c
int bt_cap_commander_change_volume_mute_state (const struct bt_cap_commander_change_volume_mute_state_param *param)
```

相关声明：[bt_cap_commander_change_volume_mute_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac5f94baa82fa6deade6f83346a56b5e4)、[bt_cap_commander_change_volume_mute_state_param](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md)。

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的音量静音状态（Volume Mute State）。

<a id="r_ga19cc7ed5992a528a7795b76e7add6d54"></a>

```c
int bt_cap_commander_change_microphone_mute_state (const struct bt_cap_commander_change_microphone_mute_state_param *param)
```

相关声明：[bt_cap_commander_change_microphone_mute_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga19cc7ed5992a528a7795b76e7add6d54)、[bt_cap_commander_change_microphone_mute_state_param](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md)。

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的麦克风静音状态（Microphone Mute State）。

<a id="r_ga958cd5925699624d23479ad2ace6b55b"></a>

```c
int bt_cap_commander_change_microphone_gain_setting (const struct bt_cap_commander_change_microphone_gain_setting_param *param)
```

相关声明：[bt_cap_commander_change_microphone_gain_setting](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga958cd5925699624d23479ad2ace6b55b)、[bt_cap_commander_change_microphone_gain_setting_param](../bluetooth_service_model_reference/P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md)。

更改一个或多个通用音频配置文件接受方（Common Audio Profile Acceptors）的麦克风增益设置（Microphone Gain Setting）。


## 4.5\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/audio/audio.h](../api_source_compiler_device_reference/P002_audio.h_源码浏览.md)
- [zephyr/bluetooth/audio/bap.h](../api_source_transport_clock_reference/P003_bap.h_源码浏览.md)
- [zephyr/bluetooth/audio/csip.h](../api_source_configuration_reference/P014_csip.h_源码浏览.md)
- [zephyr/bluetooth/addr.h](../api_source_visible_fragment_reference/P001_addr.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/bluetooth/iso.h](../api_source_reference/P415_iso.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P069_cap.h_源码浏览.md)
- [bt_cap_initiator_cb](../bluetooth_service_model_reference/P038_bt_cap_initiator_cb_结构体.md)
- [bt_cap_set_member](../bluetooth_service_model_reference/P188_bt_cap_set_member_联合体.md)
- [bt_cap_stream](../bluetooth_service_model_reference/P039_bt_cap_stream_结构体.md)
- [bt_cap_unicast_group_stream_param](../bluetooth_service_model_reference/P049_bt_cap_unicast_group_stream_param_结构体.md)
- [bt_cap_unicast_group_stream_pair_param](../bluetooth_service_model_reference/P048_bt_cap_unicast_group_stream_pair_param_结构体.md)
- [bt_cap_unicast_group_param](../bluetooth_service_model_reference/P047_bt_cap_unicast_group_param_结构体.md)
- [bt_cap_unicast_group_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab49e8c2032a824516dc8d5f2f880dd8f)
- [bt_cap_unicast_group_info](../bluetooth_service_model_reference/P046_bt_cap_unicast_group_info_结构体.md)
- [bt_cap_unicast_audio_start_stream_param](../bluetooth_service_model_reference/P041_bt_cap_unicast_audio_start_stream_param_结构体.md)
- [bt_cap_initiator_unicast_audio_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae19686be7f8aef1cc92c70fea93e1184)
- [bt_cap_unicast_audio_start_param](../bluetooth_service_model_reference/P040_bt_cap_unicast_audio_start_param_结构体.md)
- [bt_cap_unicast_audio_update_stream_param](../bluetooth_service_model_reference/P044_bt_cap_unicast_audio_update_stream_param_结构体.md)
- [bt_cap_initiator_unicast_audio_update()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92e4e2c12720ec25c4050cde307cd639)
- [bt_cap_unicast_audio_update_param](../bluetooth_service_model_reference/P043_bt_cap_unicast_audio_update_param_结构体.md)
- [bt_cap_unicast_audio_stop_param](../bluetooth_service_model_reference/P042_bt_cap_unicast_audio_stop_param_结构体.md)
- [bt_cap_initiator_unicast_audio_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gafdf6f1656249ab3ae6296272dc36b66f)
- [bt_cap_initiator_broadcast_stream_param](../bluetooth_service_model_reference/P036_bt_cap_initiator_broadcast_stream_param_结构体.md)
- [bt_cap_initiator_broadcast_subgroup_param](../bluetooth_service_model_reference/P037_bt_cap_initiator_broadcast_subgroup_param_结构体.md)
- [bt_cap_initiator_broadcast_audio_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga78697225c6b1291dfc016e20fd605fc4)
- [bt_cap_initiator_broadcast_create_param](../bluetooth_service_model_reference/P035_bt_cap_initiator_broadcast_create_param_结构体.md)
- [bt_cap_handover_unicast_to_broadcast_param](../bluetooth_service_model_reference/P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md)
- [bt_cap_handover_unicast_to_broadcast()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaae56deae3792740bc3e8074882c87837)
- [bt_cap_handover_cb](../bluetooth_service_model_reference/P033_bt_cap_handover_cb_结构体.md)
- [bt_cap_handover_broadcast_to_unicast_param](../bluetooth_service_model_reference/P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md)
- [bt_cap_handover_broadcast_to_unicast()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92ff8b3133b8f5cb3d3029b5d556fe77)
- [bt_cap_commander_cb](../bluetooth_service_model_reference/P022_bt_cap_commander_cb_结构体.md)
- [bt_cap_commander_broadcast_reception_start_member_param](../bluetooth_service_model_reference/P018_bt_cap_commander_broadcast_reception_start_member_param_结构体.md)
- [bt_cap_commander_broadcast_reception_start_param](../bluetooth_service_model_reference/P019_bt_cap_commander_broadcast_reception_start_param_结构体.md)
- [bt_cap_commander_broadcast_reception_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga25be83bb53c8e2ab76f311eaf4f615b9)
- [bt_cap_commander_broadcast_reception_stop_member_param](../bluetooth_service_model_reference/P020_bt_cap_commander_broadcast_reception_stop_member_param_结构体.md)
- [bt_cap_commander_broadcast_reception_stop_param](../bluetooth_service_model_reference/P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md)
- [bt_cap_commander_distribute_broadcast_code_member_param](../bluetooth_service_model_reference/P030_bt_cap_commander_distribute_broadcast_code_member_param_结构体.md)
- [bt_cap_commander_distribute_broadcast_code_param](../bluetooth_service_model_reference/P031_bt_cap_commander_distribute_broadcast_code_param_结构体.md)
- [bt_cap_commander_change_volume_param](../bluetooth_service_model_reference/P029_bt_cap_commander_change_volume_param_结构体.md)
- [bt_cap_commander_change_volume_offset_member_param](../bluetooth_service_model_reference/P027_bt_cap_commander_change_volume_offset_member_param_结构体.md)
- [bt_cap_commander_change_volume_offset_param](../bluetooth_service_model_reference/P028_bt_cap_commander_change_volume_offset_param_结构体.md)
- [bt_cap_commander_change_volume_offset()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae2cd451b387659b0a2021a9023d74dfa)
- [bt_cap_commander_change_volume_mute_state_param](../bluetooth_service_model_reference/P026_bt_cap_commander_change_volume_mute_state_param_结构体.md)
- [bt_cap_commander_change_microphone_mute_state_param](../bluetooth_service_model_reference/P025_bt_cap_commander_change_microphone_mute_state_param_结构体.md)
- [bt_cap_commander_change_microphone_gain_setting_member_param](../bluetooth_service_model_reference/P023_bt_cap_commander_change_microphone_gain_setting_member_param_结构体.md)
- [bt_cap_commander_change_microphone_gain_setting_param](../bluetooth_service_model_reference/P024_bt_cap_commander_change_microphone_gain_setting_param_结构体.md)
- [bt_cap_commander_change_microphone_gain_setting()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga958cd5925699624d23479ad2ace6b55b)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_cap_unicast_group_foreach_stream_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaeaad4ea5142afe5dca741b72795ae3aa)
- [bt_cap_unicast_group_foreach_stream()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga6c13996298c3e3aa33eb40f74b7bfe44)
- [bt_cap_initiator_broadcast_foreach_stream_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga2c6dc73fb44bca1f5bf8d39d46690b30)
- [bt_cap_initiator_broadcast_foreach_stream()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga45fa73b787bb4fefc73928acf3592e20)
- [bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)
- [BT_CAP_SET_TYPE_AD_HOC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468)
- [BT_CAP_SET_TYPE_CSIP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4)
- [bt_cap_acceptor_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gafcb9ea2122ff8058321cf85a22326abe)
- [bt_csip_set_member_register_param](../bluetooth_service_model_reference/P060_bt_csip_set_member_register_param_结构体.md)
- [bt_csip_set_member_svc_inst](../bluetooth_service_model_reference/P062_bt_csip_set_member_svc_inst_结构体.md)
- [bt_cap_initiator_unicast_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab7b273d06abf9a3cb43afdd4e3c30c8d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_cap_stream_ops_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac909b00d53cf35103382f0e1d9f426b7)
- [bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)
- [bt_cap_stream_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga2d8b15543105078b793462b762e27741)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_cap_stream_send_ts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga23618d1ab7690c4d3a567228c857c89e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_cap_stream_get_tx_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga7f3f6e98e7720a4711b658c4b7c85235)
- [bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)
- [bt_cap_unicast_group](../bluetooth_service_model_reference/P045_bt_cap_unicast_group_结构体.md)
- [bt_cap_unicast_group_reconfig](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga6c862b49aa1339225aeb05fad32c2f06)
- [bt_cap_unicast_group_add_streams](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga7b5d30c07e57f4db23f72836a3b12b2b)
- [bt_cap_unicast_group_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga9af37b30b6c858c24892eb1739b5330a)
- [bt_cap_unicast_group_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga86aca9c7f2f8658f4486925c68148850)
- [bt_cap_initiator_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga54d7ad68f376998510aad9c3702e9364)
- [bt_cap_initiator_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaa7286837f37da38afec8c5c955306b61)
- [bt_cap_initiator_unicast_audio_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga9fbddf102e29e8e969eade40fd60da4f)
- [bt_cap_broadcast_source](../bluetooth_service_model_reference/P017_bt_cap_broadcast_source_结构体.md)
- [bt_cap_initiator_broadcast_audio_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga2bd5f9c9de719a14ffc69827dbd4fa24)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_cap_initiator_broadcast_audio_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92336c4a56c667b608a86e45eb8d5073)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_cap_initiator_broadcast_audio_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gae4e348f74e3c12e73879082d00cdb17e)
- [bt_cap_initiator_broadcast_audio_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac98ed5112d0ce0659bde86d149ea7b4c)
- [bt_cap_initiator_broadcast_get_base](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_cap_handover_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga5d8c66b3890e051b838d123a1911cfd6)
- [bt_cap_handover_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga808f0e5b671689196ba6f0fc1aea7427)
- [bt_cap_handover_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gacd17de17ac1d96ff17ae15a63f43ad03)
- [bt_cap_commander_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab6239c91b9d210872396860619fb8687)
- [bt_cap_commander_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga38928945e67835983de3fc639c8f2764)
- [bt_cap_commander_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga165c67bddcbe220050293a4c73fb6ede)
- [bt_cap_commander_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga7abf029533fed391930257605f3c752c)
- [bt_cap_commander_broadcast_reception_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac5b2b6d617a092fb98b23c41b2f52d15)
- [bt_cap_commander_distribute_broadcast_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaf86582ad529b6ee801d1154db7e33827)
- [bt_cap_commander_change_volume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaff96953334eab1a38b30720b41c0d1a6)
- [bt_cap_commander_change_volume_mute_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac5f94baa82fa6deade6f83346a56b5e4)
- [bt_cap_commander_change_microphone_mute_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga19cc7ed5992a528a7795b76e7add6d54)

<a id="header-details"></a>

---

[上一章](P003_zephyr__bluetooth__classic__avdtp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__bluetooth__classic__classic.h_文件参考.md)
