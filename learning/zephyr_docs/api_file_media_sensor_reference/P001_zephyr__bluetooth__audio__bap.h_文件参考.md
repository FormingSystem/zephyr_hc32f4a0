---
id: learning.zephyr-docs.api-file-media-sensor-reference.page-1
title: zephyr__bluetooth__audio__bap.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_audio\_\_bap.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙基本音频配置文件（BAP）的头文件。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/audio/ascs.h>
#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/data.h>
#include <zephyr/bluetooth/gap.h>
#include <zephyr/bluetooth/iso.h>
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

蓝牙基本音频配置文件头文件（Bluetooth Basic Audio Profile，BAP）。

Copyright (c) 2020 Bose Corporation
Copyright (c) 2021-2026 Nordic Semiconductor ASA
SPDX-License-Identifier: Apache-2.0

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Fbap_5Fqos_5Fcfg"></a>

```c
struct bt_bap_qos_cfg
```

相关声明：[bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)。

服务质量（QoS）配置结构体。

<a id="r_bt_5Fbap_5Fbass_5Fsubgroup"></a>

```c
struct bt_bap_bass_subgroup
```

相关声明：[bt_bap_bass_subgroup](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md)。

保存接收状态中子组专用信息（Subgroup Specific Information）的结构体。

<a id="r_bt_5Fbap_5Fscan_5Fdelegator_5Frecv_5Fstate"></a>

```c
struct bt_bap_scan_delegator_recv_state
```

相关声明：[bt_bap_scan_delegator_recv_state](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md)。

表示广播音频扫描服务（BASS）的接收状态。

<a id="r_bt_5Fbap_5Fscan_5Fdelegator_5Fcb"></a>

```c
struct bt_bap_scan_delegator_cb
```

相关声明：[bt_bap_scan_delegator_cb](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md)。

保存基本音频配置文件（BAP）扫描委托端（Scan Delegator）回调的结构体。

<a id="r_bt_5Fbap_5Fep_5Finfo"></a>

```c
struct bt_bap_ep_info
```

相关声明：[bt_bap_ep_info](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md)。

保存音频流端点信息的结构体。

<a id="r_bt_5Fbap_5Fstream"></a>

```c
struct bt_bap_stream
```

相关声明：[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

基本音频配置文件（Basic Audio Profile，BAP）流结构体。

<a id="r_bt_5Fbap_5Fstream_5Fops"></a>

```c
struct bt_bap_stream_ops
```

相关声明：[bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)。

流操作（Stream Operation）。

<a id="r_bt_5Fbap_5Funicast_5Fserver_5Fregister_5Fparam"></a>

```c
struct bt_bap_unicast_server_register_param
```

相关声明：[bt_bap_unicast_server_register_param](../bluetooth_le_audio_model_reference/P042_bt_bap_unicast_server_register_param_结构体.md)。

用于注册单播服务器的结构体。

<a id="r_bt_5Fbap_5Funicast_5Fserver_5Fcb"></a>

```c
struct bt_bap_unicast_server_cb
```

相关声明：[bt_bap_unicast_server_cb](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md)。

单播服务器（Unicast Server）回调结构体。

<a id="r_bt_5Fbap_5Funicast_5Fgroup_5Fstream_5Fparam"></a>

```c
struct bt_bap_unicast_group_stream_param
```

相关声明：[bt_bap_unicast_group_stream_param](../bluetooth_le_audio_model_reference/P040_bt_bap_unicast_group_stream_param_结构体.md)。

单播组中每条流的参数结构体。

<a id="r_bt_5Fbap_5Funicast_5Fgroup_5Fstream_5Fpair_5Fparam"></a>

```c
struct bt_bap_unicast_group_stream_pair_param
```

相关声明：[bt_bap_unicast_group_stream_pair_param](../bluetooth_le_audio_model_reference/P039_bt_bap_unicast_group_stream_pair_param_结构体.md)。

单播组函数使用的参数结构体。

<a id="r_bt_5Fbap_5Funicast_5Fgroup_5Fparam"></a>

```c
struct bt_bap_unicast_group_param
```

相关声明：[bt_bap_unicast_group_param](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md)。

使用 `bt_bap_unicast_group_create()` 创建单播组的参数。

<a id="r_bt_5Fbap_5Funicast_5Fgroup_5Finfo"></a>

```c
struct bt_bap_unicast_group_info
```

相关声明：[bt_bap_unicast_group_info](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md)。

保存单播组（Unicast Group）信息的结构体。

<a id="r_bt_5Fbap_5Funicast_5Fclient_5Fcb"></a>

```c
struct bt_bap_unicast_client_cb
```

相关声明：[bt_bap_unicast_client_cb](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md)。

单播客户端（Unicast Client）回调结构体。

<a id="r_bt_5Fbap_5Fbase_5Fcodec_5Fid"></a>

```c
struct bt_bap_base_codec_id
```

相关声明：[bt_bap_base_codec_id](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md)。

广播音频源端点（Broadcast Audio Source Endpoint，BASE）的编解码器 ID 结构体。

<a id="r_bt_5Fbap_5Fbase_5Fsubgroup_5Fbis"></a>

```c
struct bt_bap_base_subgroup_bis
```

相关声明：[bt_bap_base_subgroup_bis](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md)。

广播音频源端点（BASE）子组中每个广播等时流（Broadcast Isochronous Stream，BIS）的结构体。

<a id="r_bt_5Fbap_5Fbroadcast_5Fsource_5Fcb"></a>

```c
struct bt_bap_broadcast_source_cb
```

相关声明：[bt_bap_broadcast_source_cb](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md)。

保存广播音频源（Broadcast Source）回调的结构体。

<a id="r_bt_5Fbap_5Fbroadcast_5Fsource_5Fstream_5Fparam"></a>

```c
struct bt_bap_broadcast_source_stream_param
```

相关声明：[bt_bap_broadcast_source_stream_param](../bluetooth_le_audio_model_reference/P022_bt_bap_broadcast_source_stream_param_结构体.md)。

广播音频源的流参数。

<a id="r_bt_5Fbap_5Fbroadcast_5Fsource_5Fsubgroup_5Fparam"></a>

```c
struct bt_bap_broadcast_source_subgroup_param
```

相关声明：[bt_bap_broadcast_source_subgroup_param](../bluetooth_le_audio_model_reference/P023_bt_bap_broadcast_source_subgroup_param_结构体.md)。

广播音频源的子组参数（Subgroup Parameters）。

<a id="r_bt_5Fbap_5Fbroadcast_5Fsource_5Fparam"></a>

```c
struct bt_bap_broadcast_source_param
```

相关声明：[bt_bap_broadcast_source_param](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md)。

广播音频源创建参数（Broadcast Source Create Parameters）。

<a id="r_bt_5Fbap_5Fbroadcast_5Fsink_5Fcb"></a>

```c
struct bt_bap_broadcast_sink_cb
```

相关声明：[bt_bap_broadcast_sink_cb](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md)。

广播音频接收端（Broadcast Audio Sink）回调结构体。

<a id="r_bt_5Fbap_5Fscan_5Fdelegator_5Fadd_5Fsrc_5Fparam"></a>

```c
struct bt_bap_scan_delegator_add_src_param
```

相关声明：[bt_bap_scan_delegator_add_src_param](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md)。

`bt_bap_scan_delegator_add_src()` 的参数。

<a id="r_bt_5Fbap_5Fscan_5Fdelegator_5Fmod_5Fsrc_5Fparam"></a>

```c
struct bt_bap_scan_delegator_mod_src_param
```

相关声明：[bt_bap_scan_delegator_mod_src_param](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md)。

`bt_bap_scan_delegator_mod_src()` 的参数。

<a id="r_bt_5Fbap_5Fbroadcast_5Fassistant_5Fcb"></a>

```c
struct bt_bap_broadcast_assistant_cb
```

相关声明：[bt_bap_broadcast_assistant_cb](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md)。

保存基本音频配置文件（Basic Audio Profile，BAP）广播助手（Broadcast Assistant）回调的结构体。

<a id="r_bt_5Fbap_5Fbroadcast_5Fassistant_5Fadd_5Fsrc_5Fparam"></a>

```c
struct bt_bap_broadcast_assistant_add_src_param
```

相关声明：[bt_bap_broadcast_assistant_add_src_param](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md)。

向广播音频扫描服务（Broadcast Audio Scan Service，BASS）服务器添加音频源的参数。

<a id="r_bt_5Fbap_5Fbroadcast_5Fassistant_5Fmod_5Fsrc_5Fparam"></a>

```c
struct bt_bap_broadcast_assistant_mod_src_param
```

相关声明：[bt_bap_broadcast_assistant_mod_src_param](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md)。

修改音频源的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_ga443c212a736852305715452e7f165a9e"></a>

```c
#define BT_BAP_BASS_MAX_SUBGROUPS COND_CODE_1(CONFIG_BT_AUDIO, (CONFIG_BT_BAP_BASS_MAX_SUBGROUPS), (0))
```

相关声明：[BT_BAP_BASS_MAX_SUBGROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga443c212a736852305715452e7f165a9e)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

BAP 扫描委托端 API（Scan Delegator API）支持的最大子组数（Maximum Number of Subgroups）。

<a id="r_ga1ebca62521cf4a6973d1fa8136e54be1"></a>

```c
#define BT_BASE_MAX_SIZE (UINT8_MAX - 1 /* type */ - BT_UUID_SIZE_16)
```

相关声明：[BT_BASE_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga1ebca62521cf4a6973d1fa8136e54be1)、[UINT8_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#aeb4e270a084ee26fe73e799861bd0252)、[BT_UUID_SIZE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d3506fd135b5cd8763446f572c161da)。

不含服务数据头部（Service Data Header）的 BASE 最大大小。

<a id="r_ga83cfb2a817e0db6d78c300dc5dea2d8a"></a>

```c
#define BT_BAP_INVALID_BROADCAST_ID 0xFFFFFFFFU
```

相关声明：[BT_BAP_INVALID_BROADCAST_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga83cfb2a817e0db6d78c300dc5dea2d8a)。

无效的广播标识符（Broadcast ID）。

<a id="r_ga3fb8ca6b5722cad7027553db40c4a94b"></a>

```c
#define BT_BAP_PD_UNSET 0xFFFFFFFFU
```

相关声明：[BT_BAP_PD_UNSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga3fb8ca6b5722cad7027553db40c4a94b)。

表示尚未设置呈现延迟（Presentation Delay）的值。

<a id="r_gac290c620aa1861ea717dee37e1e83bfe"></a>

```c
#define BT_BAP_ADV_PARAM_CONN_QUICK
```

相关声明：[BT_BAP_ADV_PARAM_CONN_QUICK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac290c620aa1861ea717dee37e1e83bfe)。

建议的可连接广播参数（Connectable Advertising Parameters）。

<a id="r_gaf1883b2596f793ef24913ef7f165c5dd"></a>

```c
#define BT_BAP_ADV_PARAM_CONN_REDUCED
```

相关声明：[BT_BAP_ADV_PARAM_CONN_REDUCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf1883b2596f793ef24913ef7f165c5dd)。

缩减的可连接广播参数（Reduced Connectable Advertising Parameters）。

<a id="r_ga5d90920dfc8d554d0cd345edd0c36c66"></a>

```c
#define BT_BAP_CONN_PARAM_SHORT_7_5
```

相关声明：[BT_BAP_CONN_PARAM_SHORT_7_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga5d90920dfc8d554d0cd345edd0c36c66)。

适用于 7.5 ms 服务数据单元间隔（SDU Interval）的初始连接请求建议连接参数（Connection Parameters）。

<a id="r_ga0469f86dc34ab738fbbcdf45cc105194"></a>

```c
#define BT_BAP_CONN_PARAM_SHORT_10
```

相关声明：[BT_BAP_CONN_PARAM_SHORT_10](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0469f86dc34ab738fbbcdf45cc105194)。

适用于 10 ms 服务数据单元间隔（SDU Interval）的初始连接请求建议连接参数（Connection Parameters）。

<a id="r_gad4a19588129f8cbf085dca166f0bc486"></a>

```c
#define BT_BAP_CONN_PARAM_RELAXED
```

相关声明：[BT_BAP_CONN_PARAM_RELAXED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gad4a19588129f8cbf085dca166f0bc486)。

用于 ACL 与 ISO 共存（Coexistence）的建议连接参数（Connection Parameters）。

<a id="r_gaf2e44d06b8b7aba57a80b1f04e65d7de"></a>

```c
#define BT_BAP_ADV_PARAM_BROADCAST_FAST
```

相关声明：[BT_BAP_ADV_PARAM_BROADCAST_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf2e44d06b8b7aba57a80b1f04e65d7de)。

广播音频的快速广播参数（Fast Advertising Parameters）。

<a id="r_gaa11e0195a02baa656085f305d911042d"></a>

```c
#define BT_BAP_ADV_PARAM_BROADCAST_SLOW
```

相关声明：[BT_BAP_ADV_PARAM_BROADCAST_SLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa11e0195a02baa656085f305d911042d)。

广播音频的慢速广播参数（Slow Advertising Parameters）。

<a id="r_ga0f17a828720504892ff36447a4e3f7c3"></a>

```c
#define BT_BAP_PER_ADV_PARAM_BROADCAST_FAST
```

相关声明：[BT_BAP_PER_ADV_PARAM_BROADCAST_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0f17a828720504892ff36447a4e3f7c3)。

广播音频的快速广播参数（Fast Advertising Parameters）。

<a id="r_gaf71bf639a2fca0c4d5ab61bfd6354668"></a>

```c
#define BT_BAP_PER_ADV_PARAM_BROADCAST_SLOW
```

相关声明：[BT_BAP_PER_ADV_PARAM_BROADCAST_SLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf71bf639a2fca0c4d5ab61bfd6354668)。

广播音频的慢速广播参数（Slow Advertising Parameters）。

<a id="r_ga91adb24c76c0d14757c5eec0146caebb"></a>

```c
#define BT_BAP_BASS_VALID_BIT_BITFIELD(_bis_bitfield)
```

相关声明：[BT_BAP_BASS_VALID_BIT_BITFIELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga91adb24c76c0d14757c5eec0146caebb)。

检查 BAP BASS 的 `BIS_Sync` 位字段（Bitfield）是否有效。

<a id="r_ga7bd804c68e67d0b4bfe391d80d33a6c7"></a>

```c
#define BT_BAP_QOS_CFG(_interval, _framing, _phy, _sdu, _rtn, _latency, _pd)
```

相关声明：[BT_BAP_QOS_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga7bd804c68e67d0b4bfe391d80d33a6c7)。

用于声明 `bt_bap_qos_cfg` 元素（Elements）的辅助宏。

<a id="r_gae578c78a10df4d1e4e6d1781ca48e1f5"></a>

```c
#define BT_BAP_QOS_CFG_UNFRAMED(_interval, _sdu, _rtn, _latency, _pd)
```

相关声明：[BT_BAP_QOS_CFG_UNFRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gae578c78a10df4d1e4e6d1781ca48e1f5)。

用于声明非成帧输入（Input Unframed）`bt_bap_qos_cfg` 的辅助宏。

<a id="r_gaa91c55ca2de3ddf09620948fd4914b14"></a>

```c
#define BT_BAP_QOS_CFG_FRAMED(_interval, _sdu, _rtn, _latency, _pd)
```

相关声明：[BT_BAP_QOS_CFG_FRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa91c55ca2de3ddf09620948fd4914b14)。

用于声明成帧输入（Input Framed）`bt_bap_qos_cfg` 的辅助宏。

<a id="r_ga357079ef00ce6f250e72a37103926c64"></a>

```c
#define BT_BAP_PA_INTERVAL_UNKNOWN 0xFFFFU
```

相关声明：[BT_BAP_PA_INTERVAL_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga357079ef00ce6f250e72a37103926c64)。

表示周期广播间隔（Periodic Advertising Interval）未知的值。

<a id="r_ga799f1417272e9b545c1e30ed4616b988"></a>

```c
#define BT_BAP_BIS_SYNC_NO_PREF 0xFFFFFFFFU
```

相关声明：[BT_BAP_BIS_SYNC_NO_PREF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga799f1417272e9b545c1e30ed4616b988)。

广播助理（Broadcast Assistant）没有 BIS 同步偏好（BIS Sync Preference）。

<a id="r_ga2a2e4a06f6e39360458fe2e4d0b66833"></a>

```c
#define BT_BAP_BIS_SYNC_FAILED 0xFFFFFFFFU
```

相关声明：[BT_BAP_BIS_SYNC_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga2a2e4a06f6e39360458fe2e4d0b66833)。

表示 BIG 同步（BIG Sync）因任意原因失败的 BIS 同步值（BIS Sync Value）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_gabb2b96d8de285dff7cbade83768d9aff"></a>

```c
typedef bool(* bt_bap_ep_func_t) (struct bt_bap_ep *ep, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_bap_ep_func_t](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#gabb2b96d8de285dff7cbade83768d9aff)、[bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)。

为每个端点（Endpoint）调用的回调函数。

<a id="r_gaf0e5a38208e90176292e745933b5e29e"></a>

```c
typedef bool(* bt_bap_unicast_group_foreach_stream_func_t) (struct bt_bap_stream *stream, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_bap_unicast_group_foreach_stream_func_t](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gaf0e5a38208e90176292e745933b5e29e)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

bt_bap_unicast_group_foreach_stream() 的回调函数（Callback Function）。

<a id="r_ga173ddb24e554afc1b16305cca69ad923"></a>

```c
typedef bool(* bt_bap_broadcast_source_foreach_stream_func_t) (struct bt_bap_stream *stream, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_bap_broadcast_source_foreach_stream_func_t](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#ga173ddb24e554afc1b16305cca69ad923)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

bt_bap_broadcast_source_foreach_stream() 的回调函数（Callback Function）。

<a id="r_gaf236a87ae461ad48ec59f487780b4824"></a>

```c
typedef bool(* bt_bap_scan_delegator_state_func_t) (const struct bt_bap_scan_delegator_recv_state *recv_state, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_bap_scan_delegator_state_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf236a87ae461ad48ec59f487780b4824)、[bt_bap_scan_delegator_recv_state](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md)。

用于扫描委托端接收状态搜索函数（Scan Delegator Receive State Search Functions）的回调函数（Callback Function）。

<a id="r_ga496c8a2f599d997a7e6e033bda5f0c36"></a>

```c
typedef void(* bt_bap_broadcast_assistant_write_cb) (struct bt_conn *conn, int err)
```

相关声明：[bt_bap_broadcast_assistant_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga496c8a2f599d997a7e6e033bda5f0c36)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

写入操作的回调函数（Callback Function）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_ga37a5f9d7198739eef8bde6764da30de9"></a>

```c
enum bt_bap_qos_cfg_framing { BT_BAP_QOS_CFG_FRAMING_UNFRAMED = 0x00 , BT_BAP_QOS_CFG_FRAMING_FRAMED = 0x01 }
```

相关声明：[bt_bap_qos_cfg_framing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga37a5f9d7198739eef8bde6764da30de9)、[BT_BAP_QOS_CFG_FRAMING_UNFRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga37a5f9d7198739eef8bde6764da30de9afe1ffd5db8e36f8082a2ef7545e04a94)、[BT_BAP_QOS_CFG_FRAMING_FRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga37a5f9d7198739eef8bde6764da30de9a406ad3527d9d92e4e8b213fe52794298)。

QoS 成帧方式（Framing）。

<a id="r_ga5e8ebf4db88f94f44828bb6f41e81d44"></a>

```c
enum { BT_BAP_QOS_CFG_1M = (1UL << (0U)) , BT_BAP_QOS_CFG_2M = (1UL << (1U)) , BT_BAP_QOS_CFG_CODED = (1UL << (2U)) }
```

相关声明：[BT_BAP_QOS_CFG_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e8ebf4db88f94f44828bb6f41e81d44af5bc162fe51c445cb3c77bcf640bbe28)、[BT_BAP_QOS_CFG_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147)、[BT_BAP_QOS_CFG_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e8ebf4db88f94f44828bb6f41e81d44ab41e06fe31c57bb7dac5a77acb53be73)。

服务质量首选物理层（QoS Preferred PHY）。

<a id="r_gac551e9b0d53fd50f3a9e9c08447f0296"></a>

```c
enum bt_bap_pa_state { BT_BAP_PA_STATE_NOT_SYNCED = 0x00 , BT_BAP_PA_STATE_INFO_REQ = 0x01 , BT_BAP_PA_STATE_SYNCED = 0x02 , BT_BAP_PA_STATE_FAILED = 0x03 , BT_BAP_PA_STATE_NO_PAST = 0x04 }
```

相关声明：[bt_bap_pa_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac551e9b0d53fd50f3a9e9c08447f0296)、[BT_BAP_PA_STATE_NOT_SYNCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf)、[BT_BAP_PA_STATE_INFO_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb)、[BT_BAP_PA_STATE_SYNCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc)、[BT_BAP_PA_STATE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647)、[BT_BAP_PA_STATE_NO_PAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d)。

扫描委托端（Scan Delegator）报告的周期广播状态（Periodic Advertising State）。

<a id="r_ga5e0b0f70d247e131fa542fae16826a22"></a>

```c
enum bt_bap_big_enc_state { BT_BAP_BIG_ENC_STATE_NO_ENC = 0x00 , BT_BAP_BIG_ENC_STATE_BCODE_REQ = 0x01 , BT_BAP_BIG_ENC_STATE_DEC = 0x02 , BT_BAP_BIG_ENC_STATE_BAD_CODE = 0x03 }
```

相关声明：[bt_bap_big_enc_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga5e0b0f70d247e131fa542fae16826a22)、[BT_BAP_BIG_ENC_STATE_NO_ENC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4)、[BT_BAP_BIG_ENC_STATE_BCODE_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2)、[BT_BAP_BIG_ENC_STATE_DEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10)、[BT_BAP_BIG_ENC_STATE_BAD_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b)。

扫描委托端（Scan Delegator）报告的广播等时组加密状态（Broadcast Isochronous Group Encryption State）。

<a id="r_ga13e9b6d571a613d689b8ba58bae64ae3"></a>

```c
enum bt_bap_bass_att_err { BT_BAP_BASS_ERR_OPCODE_NOT_SUPPORTED = 0x80 , BT_BAP_BASS_ERR_INVALID_SRC_ID = 0x81 }
```

相关声明：[bt_bap_bass_att_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga13e9b6d571a613d689b8ba58bae64ae3)、[BT_BAP_BASS_ERR_OPCODE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c)、[BT_BAP_BASS_ERR_INVALID_SRC_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202)。

广播音频扫描服务（Broadcast Audio Scan Service，BASS）特定的 ATT 错误码（Error Code）。

<a id="r_gaf210a91e1ff11d9bf7792ba47d1e1b4a"></a>

```c
enum bt_bap_ep_state { BT_BAP_EP_STATE_IDLE = 0x00 , BT_BAP_EP_STATE_CODEC_CONFIGURED = 0x01 , BT_BAP_EP_STATE_QOS_CONFIGURED = 0x02 , BT_BAP_EP_STATE_ENABLING = 0x03 , BT_BAP_EP_STATE_STREAMING = 0x04 , BT_BAP_EP_STATE_DISABLING = 0x05 , BT_BAP_EP_STATE_RELEASING = 0x06 }
```

相关声明：[bt_bap_ep_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf210a91e1ff11d9bf7792ba47d1e1b4a)、[BT_BAP_EP_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961)、[BT_BAP_EP_STATE_CODEC_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688)、[BT_BAP_EP_STATE_QOS_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523)、[BT_BAP_EP_STATE_ENABLING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332)、[BT_BAP_EP_STATE_STREAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710)、[BT_BAP_EP_STATE_DISABLING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8)、[BT_BAP_EP_STATE_RELEASING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c)。

端点状态（Endpoint States）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_gaf15e5ec5bca364f6a3e7a43b1f27da68"></a>

```c
int bt_bap_ep_get_info (const struct bt_bap_ep *ep, struct bt_bap_ep_info *info)
```

相关声明：[bt_bap_ep_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf15e5ec5bca364f6a3e7a43b1f27da68)、[bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)、[bt_bap_ep_info](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md)。

返回包含音频流端点信息（Audio Stream Endpoint Information）的结构体。

<a id="r_ga575a109efb0fd1644634ce6e0288499b"></a>

```c
struct bt_conn * bt_bap_ep_get_conn (const struct bt_bap_ep *ep)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_ep_get_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga575a109efb0fd1644634ce6e0288499b)、[bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)。

获取指向端点 ACL 连接（ACL Connection）的指针。

<a id="r_gab29c1e134156dceaa6c67abae9239378"></a>

```c
void bt_bap_stream_cb_register (struct bt_bap_stream *stream, struct bt_bap_stream_ops *ops)
```

相关声明：[bt_bap_stream_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gab29c1e134156dceaa6c67abae9239378)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)。

为流（Stream）注册音频回调（Audio Callbacks）。

<a id="r_gaaecbb590e5d073829d4c150e4fd2d8aa"></a>

```c
int bt_bap_stream_config (struct bt_conn *conn, struct bt_bap_stream *stream, struct bt_bap_ep *ep, const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_bap_stream_config](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaaecbb590e5d073829d4c150e4fd2d8aa)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

配置音频流（Audio Stream）。

<a id="r_gaa7df3f6b906241ad5291295a6ddcf1e4"></a>

```c
int bt_bap_stream_reconfig (struct bt_bap_stream *stream, const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_bap_stream_reconfig](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa7df3f6b906241ad5291295a6ddcf1e4)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

重新配置音频流（Audio Stream）。

<a id="r_gac878ed89242cac9a8514e8e4f1da4d9d"></a>

```c
int bt_bap_stream_qos (struct bt_conn *conn, struct bt_bap_unicast_group *group)
```

相关声明：[bt_bap_stream_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac878ed89242cac9a8514e8e4f1da4d9d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

配置音频流服务质量（Audio Stream QoS）。

<a id="r_ga13a859b31b0310ec22339ec7ed0754f8"></a>

```c
int bt_bap_stream_enable (struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len)
```

相关声明：[bt_bap_stream_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga13a859b31b0310ec22339ec7ed0754f8)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启用音频流（Audio Stream）。

<a id="r_ga0afe6c927729697e2f984cefcbc7c0f1"></a>

```c
int bt_bap_stream_metadata (struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len)
```

相关声明：[bt_bap_stream_metadata](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0afe6c927729697e2f984cefcbc7c0f1)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更改音频流元数据（Audio Stream Metadata）。

<a id="r_ga0fd2bb35909fc19e3e9cff068ba9e9aa"></a>

```c
int bt_bap_stream_disable (struct bt_bap_stream *stream)
```

相关声明：[bt_bap_stream_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0fd2bb35909fc19e3e9cff068ba9e9aa)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

禁用音频流（Audio Stream）。

<a id="r_gaa75f2cd2c36fdaef04a62c95bec6e2e3"></a>

```c
int bt_bap_stream_connect (struct bt_bap_stream *stream)
```

相关声明：[bt_bap_stream_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa75f2cd2c36fdaef04a62c95bec6e2e3)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

连接单播音频流（Unicast Audio Stream）。

<a id="r_ga8f2dc67c35299334d21c7dee7b8664ae"></a>

```c
int bt_bap_stream_start (struct bt_bap_stream *stream)
```

相关声明：[bt_bap_stream_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga8f2dc67c35299334d21c7dee7b8664ae)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

启动音频流（Audio Stream）。

<a id="r_gada72bcd3951eff2bc6b70c02dcaed98b"></a>

```c
int bt_bap_stream_stop (struct bt_bap_stream *stream)
```

相关声明：[bt_bap_stream_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gada72bcd3951eff2bc6b70c02dcaed98b)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

停止音频流（Audio Stream）。

<a id="r_gaaf94f1f0dda7ef356c0f9ae79b5c60e4"></a>

```c
int bt_bap_stream_release (struct bt_bap_stream *stream)
```

相关声明：[bt_bap_stream_release](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaaf94f1f0dda7ef356c0f9ae79b5c60e4)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

释放音频流（Audio Stream）。

<a id="r_ga63b69967aa92224a2bd9cf79eb41773e"></a>

```c
int bt_bap_stream_send (struct bt_bap_stream *stream, struct net_buf *buf, uint16_t seq_num)
```

相关声明：[bt_bap_stream_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga63b69967aa92224a2bd9cf79eb41773e)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向音频流（Audio Stream）发送不带时间戳（Timestamp）的数据。

<a id="r_gaa0e012446238c916abc84d6c0de89bf3"></a>

```c
int bt_bap_stream_send_ts (struct bt_bap_stream *stream, struct net_buf *buf, uint16_t seq_num, uint32_t ts)
```

相关声明：[bt_bap_stream_send_ts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa0e012446238c916abc84d6c0de89bf3)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向音频流（Audio Stream）发送带时间戳（Timestamp）的数据。

<a id="r_ga47eb6219d730d75ddc4f49dceac7e928"></a>

```c
int bt_bap_stream_get_tx_sync (struct bt_bap_stream *stream, struct bt_iso_tx_info *info)
```

相关声明：[bt_bap_stream_get_tx_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga47eb6219d730d75ddc4f49dceac7e928)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)。

获取基本音频配置文件流（Basic Audio Profile Stream）的等时传输时序信息（ISO Transmission Timing Info）。

<a id="r_gab3ea6014854e6290f058c87e866c3191"></a>

```c
int bt_bap_unicast_server_register (const struct bt_bap_unicast_server_register_param *param)
```

相关声明：[bt_bap_unicast_server_register](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#gab3ea6014854e6290f058c87e866c3191)、[bt_bap_unicast_server_register_param](../bluetooth_le_audio_model_reference/P042_bt_bap_unicast_server_register_param_结构体.md)。

注册单播服务器（Unicast Server）。

<a id="r_ga6ef3b9e877ffdc04cc48fda6713a0209"></a>

```c
int bt_bap_unicast_server_unregister (void)
```

相关声明：[bt_bap_unicast_server_unregister](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#ga6ef3b9e877ffdc04cc48fda6713a0209)。

注销单播服务器（Unicast Server）。

<a id="r_ga7669133936bc13f7ab38817db9ce69c0"></a>

```c
int bt_bap_unicast_server_register_cb (const struct bt_bap_unicast_server_cb *cb)
```

相关声明：[bt_bap_unicast_server_register_cb](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#ga7669133936bc13f7ab38817db9ce69c0)、[bt_bap_unicast_server_cb](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md)。

注册单播服务器回调（Unicast Server Callbacks）。

<a id="r_gadf984f12bdeadcfc814dc2fc770cb7bf"></a>

```c
int bt_bap_unicast_server_unregister_cb (const struct bt_bap_unicast_server_cb *cb)
```

相关声明：[bt_bap_unicast_server_unregister_cb](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#gadf984f12bdeadcfc814dc2fc770cb7bf)、[bt_bap_unicast_server_cb](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md)。

注销单播服务器回调（Unicast Server Callbacks）。

<a id="r_gafe7640d6269ec95c8af6d7549fac785d"></a>

```c
int bt_bap_unicast_server_foreach_ep (struct bt_conn *conn, bt_bap_ep_func_t func, void *user_data)
```

相关声明：[bt_bap_unicast_server_foreach_ep](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#gafe7640d6269ec95c8af6d7549fac785d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_ep_func_t](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#gabb2b96d8de285dff7cbade83768d9aff)。

遍历所给连接的全部端点（Endpoints）。

<a id="r_ga98b170c9f371d7d60c3dde9aff3f6d6b"></a>

```c
int bt_bap_unicast_server_config_ase (struct bt_conn *conn, struct bt_bap_stream *stream, const struct bt_audio_codec_cfg *codec_cfg, const struct bt_bap_qos_cfg_pref *qos_pref)
```

相关声明：[bt_bap_unicast_server_config_ase](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#ga98b170c9f371d7d60c3dde9aff3f6d6b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_bap_qos_cfg_pref](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md)。

初始化并配置新的音频流端点（ASE）。

<a id="r_gaafd53b5f45d998b44e94a1b58e93ba21"></a>

```c
int bt_bap_unicast_group_create (struct bt_bap_unicast_group_param *param, struct bt_bap_unicast_group **unicast_group)
```

相关声明：[bt_bap_unicast_group_create](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gaafd53b5f45d998b44e94a1b58e93ba21)、[bt_bap_unicast_group_param](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)。

创建单播组（Unicast Group）。

<a id="r_gacd684504c8127ff4f8d038cc06718e5e"></a>

```c
int bt_bap_unicast_group_reconfig (struct bt_bap_unicast_group *unicast_group, const struct bt_bap_unicast_group_param *param)
```

相关声明：[bt_bap_unicast_group_reconfig](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gacd684504c8127ff4f8d038cc06718e5e)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)、[bt_bap_unicast_group_param](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md)。

重新配置单播组（Unicast Group）。

<a id="r_ga9cc792cd1eaaa79d56f3df0e2341cbf6"></a>

```c
int bt_bap_unicast_group_add_streams (struct bt_bap_unicast_group *unicast_group, struct bt_bap_unicast_group_stream_pair_param params[], size_t num_param)
```

相关声明：[bt_bap_unicast_group_add_streams](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#ga9cc792cd1eaaa79d56f3df0e2341cbf6)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)、[bt_bap_unicast_group_stream_pair_param](../bluetooth_le_audio_model_reference/P039_bt_bap_unicast_group_stream_pair_param_结构体.md)。

以单播客户端（Unicast Client）身份向单播组添加流（Streams）。

<a id="r_ga34dbdce6133f8366df453ec937fb47d2"></a>

```c
int bt_bap_unicast_group_delete (struct bt_bap_unicast_group *unicast_group)
```

相关声明：[bt_bap_unicast_group_delete](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#ga34dbdce6133f8366df453ec937fb47d2)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)。

删除音频单播组（Audio Unicast Group）。

<a id="r_gad608ee07c8a50abf586a3bc31921f032"></a>

```c
int bt_bap_unicast_group_foreach_stream (struct bt_bap_unicast_group *unicast_group, bt_bap_unicast_group_foreach_stream_func_t func, void *user_data)
```

相关声明：[bt_bap_unicast_group_foreach_stream](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gad608ee07c8a50abf586a3bc31921f032)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)、[bt_bap_unicast_group_foreach_stream_func_t](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gaf0e5a38208e90176292e745933b5e29e)。

遍历单播组（Unicast Group）中的全部流。

<a id="r_ga4ba0e4c3fa7ec3a36a64a19c80027504"></a>

```c
int bt_bap_unicast_group_get_info (const struct bt_bap_unicast_group *unicast_group, struct bt_bap_unicast_group_info *info)
```

相关声明：[bt_bap_unicast_group_get_info](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#ga4ba0e4c3fa7ec3a36a64a19c80027504)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)、[bt_bap_unicast_group_info](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md)。

返回保存单播组信息（Unicast Group Information）的结构体。

<a id="r_gade70f04ae1a828b43b3b44fa8933f674"></a>

```c
int bt_bap_unicast_client_register_cb (struct bt_bap_unicast_client_cb *cb)
```

相关声明：[bt_bap_unicast_client_register_cb](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gade70f04ae1a828b43b3b44fa8933f674)、[bt_bap_unicast_client_cb](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md)。

注册单播客户端回调（Unicast Client Callbacks）。

<a id="r_gaee092a4e918a67bb5fd94cb78cc21141"></a>

```c
int bt_bap_unicast_client_unregister_cb (struct bt_bap_unicast_client_cb *cb)
```

相关声明：[bt_bap_unicast_client_unregister_cb](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gaee092a4e918a67bb5fd94cb78cc21141)、[bt_bap_unicast_client_cb](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md)。

注销单播客户端回调（Unicast Client Callbacks）。

<a id="r_gacef9c88f66762e8de19303d20dafa0bb"></a>

```c
int bt_bap_unicast_client_discover (struct bt_conn *conn, enum bt_audio_dir dir)
```

相关声明：[bt_bap_unicast_client_discover](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gacef9c88f66762e8de19303d20dafa0bb)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)。

发现远端能力（Remote Capabilities）和端点（Endpoints）。

<a id="r_gad963bdda290df96036a68b00cc940eca"></a>

```c
int bt_bap_unicast_client_qos_from_group (const struct bt_bap_stream *stream, struct bt_bap_qos_cfg *qos)
```

相关声明：[bt_bap_unicast_client_qos_from_group](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gad963bdda290df96036a68b00cc940eca)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)。

获取为该流所属组配置的服务质量（QoS）副本。

<a id="r_gad106ae43201100940d9145d291fe9ca3"></a>

```c
bool bt_bap_qos_cfg_eq (const struct bt_bap_qos_cfg *a, const struct bt_bap_qos_cfg *b)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_bap_qos_cfg_eq](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gad106ae43201100940d9145d291fe9ca3)、[bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)、[bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)。

比较两个 bt_bap_qos_cfg，并返回它们是否相等。

<a id="r_ga29423a39d76ad16f0586d82a23c07ba7"></a>

```c
const struct bt_bap_base * bt_bap_base_get_base_from_ad (const struct bt_data *ad)
```

相关声明：[bt_bap_base_get_base_from_ad](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga29423a39d76ad16f0586d82a23c07ba7)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

根据周期广播数据（Periodic Advertising Data）生成指向 BASE 的指针。

<a id="r_ga539f92b71ec34f0551ef6240d83b972e"></a>

```c
int bt_bap_base_get_size (const struct bt_bap_base *base)
```

相关声明：[bt_bap_base_get_size](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga539f92b71ec34f0551ef6240d83b972e)。

获取 BASE 的大小。

<a id="r_gaf91f45bcf7df2f368c5abeb116b65dd0"></a>

```c
int bt_bap_base_get_pres_delay (const struct bt_bap_base *base)
```

相关声明：[bt_bap_base_get_pres_delay](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#gaf91f45bcf7df2f368c5abeb116b65dd0)。

获取 BASE 的呈现延迟值（Presentation Delay）。

<a id="r_gadcae0230168564da1ee8b3c577ce27d7"></a>

```c
int bt_bap_base_get_subgroup_count (const struct bt_bap_base *base)
```

相关声明：[bt_bap_base_get_subgroup_count](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#gadcae0230168564da1ee8b3c577ce27d7)。

获取 BASE 的子组数量（Subgroup Count）。

<a id="r_ga6deab5a8b7a16ddf0c3685d4003694e1"></a>

```c
int bt_bap_base_get_bis_indexes (const struct bt_bap_base *base, uint32_t *bis_indexes)
```

相关声明：[bt_bap_base_get_bis_indexes](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga6deab5a8b7a16ddf0c3685d4003694e1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 BASE 的所有广播等时流索引（BIS Indexes）。

<a id="r_ga5e6e0b758409cbdde93c0f648ef5e5e8"></a>

```c
int bt_bap_base_foreach_subgroup (const struct bt_bap_base *base, bool(*func)(const struct bt_bap_base_subgroup *subgroup, void *user_data), void *user_data)
```

相关声明：[bt_bap_base_foreach_subgroup](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga5e6e0b758409cbdde93c0f648ef5e5e8)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

遍历 BASE 中的所有子组（Subgroups）。

<a id="r_gae75e05a002dee8336eb066ae8231ea0c"></a>

```c
int bt_bap_base_get_subgroup_codec_id (const struct bt_bap_base_subgroup *subgroup, struct bt_bap_base_codec_id *codec_id)
```

相关声明：[bt_bap_base_get_subgroup_codec_id](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#gae75e05a002dee8336eb066ae8231ea0c)、[bt_bap_base_codec_id](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md)。

获取子组的编解码器 ID（Codec ID）。

<a id="r_ga10e2e32dc2802ba55d55c77148331f6a"></a>

```c
int bt_bap_base_get_subgroup_codec_data (const struct bt_bap_base_subgroup *subgroup, uint8_t **data)
```

相关声明：[bt_bap_base_get_subgroup_codec_data](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga10e2e32dc2802ba55d55c77148331f6a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取子组的编解码器配置数据（Codec Configuration Data）。

<a id="r_gafb9d9544f38c7ad2613fff1679eb1f0c"></a>

```c
int bt_bap_base_get_subgroup_codec_meta (const struct bt_bap_base_subgroup *subgroup, uint8_t **meta)
```

相关声明：[bt_bap_base_get_subgroup_codec_meta](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#gafb9d9544f38c7ad2613fff1679eb1f0c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取子组的编解码器元数据（Codec Metadata）。

<a id="r_ga920e3409f1978b803bcf6bc8d05ac8f6"></a>

```c
int bt_bap_base_subgroup_codec_to_codec_cfg (const struct bt_bap_base_subgroup *subgroup, struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_bap_base_subgroup_codec_to_codec_cfg](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga920e3409f1978b803bcf6bc8d05ac8f6)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

将子组编解码器数据存入编解码器配置解析 API（Codec Config Parsing APIs）使用的对象。

<a id="r_ga051e1f8aa2faf3ba7a973356138fd2d3"></a>

```c
int bt_bap_base_get_subgroup_bis_count (const struct bt_bap_base_subgroup *subgroup)
```

相关声明：[bt_bap_base_get_subgroup_bis_count](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga051e1f8aa2faf3ba7a973356138fd2d3)。

获取子组的广播等时流数量（BIS Count）。

<a id="r_ga37df3bf1e18d2d8e9388541217b2e366"></a>

```c
int bt_bap_base_subgroup_get_bis_indexes (const struct bt_bap_base_subgroup *subgroup, uint32_t *bis_indexes)
```

相关声明：[bt_bap_base_subgroup_get_bis_indexes](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga37df3bf1e18d2d8e9388541217b2e366)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取子组的所有广播等时流索引（BIS Indexes）。

<a id="r_ga4f85ee43984cb2f3139b41da7b9b1aee"></a>

```c
int bt_bap_base_subgroup_foreach_bis (const struct bt_bap_base_subgroup *subgroup, bool(*func)(const struct bt_bap_base_subgroup_bis *bis, void *user_data), void *user_data)
```

相关声明：[bt_bap_base_subgroup_foreach_bis](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga4f85ee43984cb2f3139b41da7b9b1aee)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_bap_base_subgroup_bis](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md)。

遍历子组中的所有广播等时流（BIS）。

<a id="r_gaa5cb191df7807ea87f1fba1871ca8ebe"></a>

```c
int bt_bap_base_subgroup_bis_codec_to_codec_cfg (const struct bt_bap_base_subgroup_bis *bis, struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_bap_base_subgroup_bis_codec_to_codec_cfg](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#gaa5cb191df7807ea87f1fba1871ca8ebe)、[bt_bap_base_subgroup_bis](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

将 BIS 编解码器配置数据存入编解码器配置解析 API（Codec Config Parsing APIs）使用的对象。

<a id="r_gac75ad00b8f9a1cd7048677a33b17acda"></a>

```c
int bt_bap_broadcast_source_register_cb (struct bt_bap_broadcast_source_cb *cb)
```

相关声明：[bt_bap_broadcast_source_register_cb](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gac75ad00b8f9a1cd7048677a33b17acda)、[bt_bap_broadcast_source_cb](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md)。

注册广播源（Broadcast Sources）的回调。

<a id="r_gacc8d26c42c6b4ae6dc11af84ec4af616"></a>

```c
int bt_bap_broadcast_source_unregister_cb (struct bt_bap_broadcast_source_cb *cb)
```

相关声明：[bt_bap_broadcast_source_unregister_cb](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gacc8d26c42c6b4ae6dc11af84ec4af616)、[bt_bap_broadcast_source_cb](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md)。

注销广播源（Broadcast Sources）的回调。

<a id="r_gacdebfc435eebd47cf9cd05099a5f78e0"></a>

```c
int bt_bap_broadcast_source_create (struct bt_bap_broadcast_source_param *param, struct bt_bap_broadcast_source **source)
```

相关声明：[bt_bap_broadcast_source_create](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gacdebfc435eebd47cf9cd05099a5f78e0)、[bt_bap_broadcast_source_param](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)。

创建音频广播源（Audio Broadcast Source）。

<a id="r_gabecaa9db7be5cb03ed997ba478878d40"></a>

```c
int bt_bap_broadcast_source_reconfig (struct bt_bap_broadcast_source *source, struct bt_bap_broadcast_source_param *param)
```

相关声明：[bt_bap_broadcast_source_reconfig](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gabecaa9db7be5cb03ed997ba478878d40)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)、[bt_bap_broadcast_source_param](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md)。

重新配置音频广播源（Audio Broadcast Source）。

<a id="r_gaff2cfdadbff3ebe1e2efb660dee56f02"></a>

```c
int bt_bap_broadcast_source_update_metadata (struct bt_bap_broadcast_source *source, const uint8_t meta[], size_t meta_len)
```

相关声明：[bt_bap_broadcast_source_update_metadata](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gaff2cfdadbff3ebe1e2efb660dee56f02)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

修改音频广播源的元数据（Metadata）。

<a id="r_gac4640f5207599d51c1a63ff47f3c1d5a"></a>

```c
int bt_bap_broadcast_source_start (struct bt_bap_broadcast_source *source, struct bt_le_ext_adv *adv)
```

相关声明：[bt_bap_broadcast_source_start](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gac4640f5207599d51c1a63ff47f3c1d5a)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

启动音频广播源（Audio Broadcast Source）。

<a id="r_ga36a885581eec5cab8b3f652db19b9aba"></a>

```c
int bt_bap_broadcast_source_stop (struct bt_bap_broadcast_source *source)
```

相关声明：[bt_bap_broadcast_source_stop](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#ga36a885581eec5cab8b3f652db19b9aba)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)。

停止音频广播源（Audio Broadcast Source）。

<a id="r_ga12e0a4856115a8eb297fe2d1fc130155"></a>

```c
int bt_bap_broadcast_source_delete (struct bt_bap_broadcast_source *source)
```

相关声明：[bt_bap_broadcast_source_delete](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#ga12e0a4856115a8eb297fe2d1fc130155)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)。

删除音频广播源（Audio Broadcast Source）。

<a id="r_gafe07e4c6962858500fcf66415a173be8"></a>

```c
int bt_bap_broadcast_source_get_base (struct bt_bap_broadcast_source *source, struct net_buf_simple *base_buf)
```

相关声明：[bt_bap_broadcast_source_get_base](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gafe07e4c6962858500fcf66415a173be8)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

获取广播源的广播音频流端点（Broadcast Audio Stream Endpoint，BASE）。

<a id="r_ga9d543b9282e0dadca3afe3a97e385b15"></a>

```c
int bt_bap_broadcast_source_foreach_stream (struct bt_bap_broadcast_source *source, bt_bap_broadcast_source_foreach_stream_func_t func, void *user_data)
```

相关声明：[bt_bap_broadcast_source_foreach_stream](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#ga9d543b9282e0dadca3afe3a97e385b15)、[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)、[bt_bap_broadcast_source_foreach_stream_func_t](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#ga173ddb24e554afc1b16305cca69ad923)。

遍历广播源中的所有流（Streams）。

<a id="r_ga1b83ead634d990e954f233d0208c5a85"></a>

```c
int bt_bap_broadcast_sink_register_cb (struct bt_bap_broadcast_sink_cb *cb)
```

相关声明：[bt_bap_broadcast_sink_register_cb](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md#ga1b83ead634d990e954f233d0208c5a85)、[bt_bap_broadcast_sink_cb](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md)。

注册广播接收端回调（Broadcast Sink Callbacks）。

<a id="r_ga0637d1957db70ad39e0608ed07e75166"></a>

```c
int bt_bap_broadcast_sink_create (struct bt_le_per_adv_sync *pa_sync, uint32_t broadcast_id, struct bt_bap_broadcast_sink **sink)
```

相关声明：[bt_bap_broadcast_sink_create](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md#ga0637d1957db70ad39e0608ed07e75166)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)。

从周期广播同步（Periodic Advertising Sync）创建广播接收端（Broadcast Sink）。

<a id="r_gacadebb5ce8aab5f5b8f1ff7e0fa57805"></a>

```c
int bt_bap_broadcast_sink_sync (struct bt_bap_broadcast_sink *sink, uint32_t indexes_bitfield, struct bt_bap_stream *streams[], const uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE])
```

相关声明：[bt_bap_broadcast_sink_sync](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md#gacadebb5ce8aab5f5b8f1ff7e0fa57805)、[bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)。

同步到广播端的音频（Broadcaster's Audio）。

<a id="r_ga1020b21bfb4195aeb5823197145b1fe9"></a>

```c
int bt_bap_broadcast_sink_stop (struct bt_bap_broadcast_sink *sink)
```

相关声明：[bt_bap_broadcast_sink_stop](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md#ga1020b21bfb4195aeb5823197145b1fe9)、[bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)。

停止音频广播接收端（Audio Broadcast Sink）。

<a id="r_ga8b9d6cb409a3671654e053475ada3fda"></a>

```c
int bt_bap_broadcast_sink_delete (struct bt_bap_broadcast_sink *sink)
```

相关声明：[bt_bap_broadcast_sink_delete](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md#ga8b9d6cb409a3671654e053475ada3fda)、[bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)。

释放广播接收端（Broadcast Sink）。

<a id="r_ga7632ab444dbf99387871f7d0c90b11ba"></a>

```c
int bt_bap_scan_delegator_register (struct bt_bap_scan_delegator_cb *cb)
```

相关声明：[bt_bap_scan_delegator_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga7632ab444dbf99387871f7d0c90b11ba)、[bt_bap_scan_delegator_cb](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md)。

注册基本音频配置文件扫描委托端（Basic Audio Profile Scan Delegator）和广播音频扫描服务（BASS）。

<a id="r_ga6f52e58767303ded16cb6289f094895a"></a>

```c
int bt_bap_scan_delegator_unregister (void)
```

相关声明：[bt_bap_scan_delegator_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga6f52e58767303ded16cb6289f094895a)。

注销基本音频配置文件扫描委托端（Basic Audio Profile Scan Delegator）和广播音频扫描服务（BASS）。

<a id="r_ga381c1f3b386ecbdfd570eb125882161e"></a>

```c
int bt_bap_scan_delegator_set_pa_state (uint8_t src_id, enum bt_bap_pa_state pa_state)
```

相关声明：[bt_bap_scan_delegator_set_pa_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga381c1f3b386ecbdfd570eb125882161e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_bap_pa_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac551e9b0d53fd50f3a9e9c08447f0296)。

将周期广播同步状态（Periodic Advertising Sync State）设为正在同步（Syncing）。

<a id="r_gaf610cd6cddd52622f95cfd35b19ee841"></a>

```c
int bt_bap_scan_delegator_set_bis_sync_state (uint8_t src_id, uint32_t bis_synced[0])
```

相关声明：[bt_bap_scan_delegator_set_bis_sync_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf610cd6cddd52622f95cfd35b19ee841)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置服务器中某个接收状态（Receive State）的同步状态（Sync State）。

<a id="r_ga6eb2a782d761da12d112356cfe723ff0"></a>

```c
int bt_bap_scan_delegator_add_src (const struct bt_bap_scan_delegator_add_src_param *param)
```

相关声明：[bt_bap_scan_delegator_add_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga6eb2a782d761da12d112356cfe723ff0)、[bt_bap_scan_delegator_add_src_param](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md)。

在本地添加接收状态源（Receive State Source）。

<a id="r_gac022f38269742f16ff6887840ef5ba9a"></a>

```c
int bt_bap_scan_delegator_mod_src (const struct bt_bap_scan_delegator_mod_src_param *param)
```

相关声明：[bt_bap_scan_delegator_mod_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac022f38269742f16ff6887840ef5ba9a)、[bt_bap_scan_delegator_mod_src_param](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md)。

在本地添加接收状态源（Receive State Source）。

<a id="r_ga6c240f1cdb33945197700e4fe106ef2c"></a>

```c
int bt_bap_scan_delegator_rem_src (uint8_t src_id)
```

相关声明：[bt_bap_scan_delegator_rem_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga6c240f1cdb33945197700e4fe106ef2c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

移除接收状态源（Receive State Source）。

<a id="r_gab6f1a12699a9437c6575c70df33d5be0"></a>

```c
void bt_bap_scan_delegator_foreach_state (bt_bap_scan_delegator_state_func_t func, void *user_data)
```

相关声明：[bt_bap_scan_delegator_foreach_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gab6f1a12699a9437c6575c70df33d5be0)、[bt_bap_scan_delegator_state_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf236a87ae461ad48ec59f487780b4824)。

遍历全部现有接收状态（Receive State）。

<a id="r_gabec9fd0a2966e1811fd4770855050510"></a>

```c
const struct bt_bap_scan_delegator_recv_state * bt_bap_scan_delegator_find_state (bt_bap_scan_delegator_state_func_t func, void *user_data)
```

相关声明：[bt_bap_scan_delegator_recv_state](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md)、[bt_bap_scan_delegator_find_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gabec9fd0a2966e1811fd4770855050510)、[bt_bap_scan_delegator_state_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf236a87ae461ad48ec59f487780b4824)。

依据比较函数（Compare Function）查找并返回接收状态（Receive State）。

<a id="r_gab59c5ebc4fef28da34d8a54b1244c33b"></a>

```c
int bt_bap_broadcast_assistant_discover (struct bt_conn *conn)
```

相关声明：[bt_bap_broadcast_assistant_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gab59c5ebc4fef28da34d8a54b1244c33b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现服务器上的广播音频扫描服务（Broadcast Audio Scan Service）。

<a id="r_ga98ac067e66d263aa41fc6f8df6bb9126"></a>

```c
int bt_bap_broadcast_assistant_scan_start (struct bt_conn *conn, bool start_scan)
```

相关声明：[bt_bap_broadcast_assistant_scan_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga98ac067e66d263aa41fc6f8df6bb9126)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为远端服务器启动广播等时流（BIS）扫描。

<a id="r_ga76cae35df980b78a10551811050b2760"></a>

```c
int bt_bap_broadcast_assistant_scan_stop (struct bt_conn *conn)
```

相关声明：[bt_bap_broadcast_assistant_scan_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga76cae35df980b78a10551811050b2760)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

停止针对服务器的远端广播等时流（BIS）扫描。

<a id="r_gabab24c44e9833029965475ad7b149e6e"></a>

```c
int bt_bap_broadcast_assistant_register_cb (struct bt_bap_broadcast_assistant_cb *cb)
```

相关声明：[bt_bap_broadcast_assistant_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gabab24c44e9833029965475ad7b149e6e)、[bt_bap_broadcast_assistant_cb](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md)。

注册广播音频扫描服务客户端（Broadcast Audio Scan Service Client）使用的回调（Callback）。

<a id="r_ga679cdeb6e555bfc9ce20f38e493000ee"></a>

```c
int bt_bap_broadcast_assistant_unregister_cb (struct bt_bap_broadcast_assistant_cb *cb)
```

相关声明：[bt_bap_broadcast_assistant_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga679cdeb6e555bfc9ce20f38e493000ee)、[bt_bap_broadcast_assistant_cb](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md)。

注销广播音频扫描服务客户端（Broadcast Audio Scan Service Client）使用的回调（Callback）。

<a id="r_gac93cb4cab33d0b937e752bc0b71cad9e"></a>

```c
int bt_bap_broadcast_assistant_add_src (struct bt_conn *conn, const struct bt_bap_broadcast_assistant_add_src_param *param)
```

相关声明：[bt_bap_broadcast_assistant_add_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac93cb4cab33d0b937e752bc0b71cad9e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_broadcast_assistant_add_src_param](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md)。

在服务器上添加源（Source）。

<a id="r_gaa9c292a7dcb470926d8d7d4be699a0c7"></a>

```c
int bt_bap_broadcast_assistant_mod_src (struct bt_conn *conn, const struct bt_bap_broadcast_assistant_mod_src_param *param)
```

相关声明：[bt_bap_broadcast_assistant_mod_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa9c292a7dcb470926d8d7d4be699a0c7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_broadcast_assistant_mod_src_param](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md)。

修改服务器上的源（Source）。

<a id="r_gabcec07689c13a996bcb9d2d417347dbb"></a>

```c
int bt_bap_broadcast_assistant_set_broadcast_code (struct bt_conn *conn, uint8_t src_id, const uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE])
```

相关声明：[bt_bap_broadcast_assistant_set_broadcast_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gabcec07689c13a996bcb9d2d417347dbb)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)。

为指定接收状态（Receive State）设置广播码（Broadcast Code）。

<a id="r_ga09785690db551677a043fcaa2fdb7f29"></a>

```c
int bt_bap_broadcast_assistant_rem_src (struct bt_conn *conn, uint8_t src_id)
```

相关声明：[bt_bap_broadcast_assistant_rem_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga09785690db551677a043fcaa2fdb7f29)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从服务器移除源（Source）。

<a id="r_ga94fce2b4346b1026d53e0b860ca7fbf2"></a>

```c
int bt_bap_broadcast_assistant_read_recv_state (struct bt_conn *conn, uint8_t idx)
```

相关声明：[bt_bap_broadcast_assistant_read_recv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga94fce2b4346b1026d53e0b860ca7fbf2)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从服务器读取指定接收状态（Receive State）。


## 1.6\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/addr.h](../api_source_visible_fragment_reference/P001_addr.h_源码浏览.md)
- [zephyr/bluetooth/assigned_numbers.h](../api_source_socket_ethernet_reference/P001_assigned_numbers.h_源码浏览.md)
- [zephyr/bluetooth/audio/ascs.h](../api_source_supplement_reference/P017_ascs.h_源码浏览.md)
- [zephyr/bluetooth/audio/audio.h](../api_source_compiler_device_reference/P002_audio.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/bluetooth/data.h](../api_source_reference/P121_data.h_源码浏览.md)
- [zephyr/bluetooth/gap.h](../api_source_transport_clock_reference/P016_gap.h_源码浏览.md)
- [zephyr/bluetooth/iso.h](../api_source_reference/P415_iso.h_源码浏览.md)
- [zephyr/bluetooth/uuid.h](../api_source_supplement_reference/P020_uuid.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_transport_clock_reference/P003_bap.h_源码浏览.md)
- [bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)
- [bt_bap_bass_subgroup](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md)
- [bt_bap_scan_delegator_recv_state](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md)
- [bt_bap_scan_delegator_cb](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md)
- [bt_bap_ep_info](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md)
- [bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)
- [bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)
- [bt_bap_unicast_server_register_param](../bluetooth_le_audio_model_reference/P042_bt_bap_unicast_server_register_param_结构体.md)
- [bt_bap_unicast_server_cb](../bluetooth_le_audio_model_reference/P041_bt_bap_unicast_server_cb_结构体.md)
- [bt_bap_unicast_group_stream_param](../bluetooth_le_audio_model_reference/P040_bt_bap_unicast_group_stream_param_结构体.md)
- [bt_bap_unicast_group_stream_pair_param](../bluetooth_le_audio_model_reference/P039_bt_bap_unicast_group_stream_pair_param_结构体.md)
- [bt_bap_unicast_group_param](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md)
- [bt_bap_unicast_group_create()](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gaafd53b5f45d998b44e94a1b58e93ba21)
- [bt_bap_unicast_group_info](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md)
- [bt_bap_unicast_client_cb](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md)
- [bt_bap_base_codec_id](../bluetooth_le_audio_model_reference/P011_bt_bap_base_codec_id_结构体.md)
- [bt_bap_base_subgroup_bis](../bluetooth_le_audio_model_reference/P012_bt_bap_base_subgroup_bis_结构体.md)
- [bt_bap_broadcast_source_cb](../bluetooth_le_audio_model_reference/P020_bt_bap_broadcast_source_cb_结构体.md)
- [bt_bap_broadcast_source_stream_param](../bluetooth_le_audio_model_reference/P022_bt_bap_broadcast_source_stream_param_结构体.md)
- [bt_bap_broadcast_source_subgroup_param](../bluetooth_le_audio_model_reference/P023_bt_bap_broadcast_source_subgroup_param_结构体.md)
- [bt_bap_broadcast_source_param](../bluetooth_le_audio_model_reference/P021_bt_bap_broadcast_source_param_结构体.md)
- [bt_bap_broadcast_sink_cb](../bluetooth_le_audio_model_reference/P018_bt_bap_broadcast_sink_cb_结构体.md)
- [bt_bap_scan_delegator_add_src_param](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md)
- [bt_bap_scan_delegator_add_src()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga6eb2a782d761da12d112356cfe723ff0)
- [bt_bap_scan_delegator_mod_src_param](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md)
- [bt_bap_scan_delegator_mod_src()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac022f38269742f16ff6887840ef5ba9a)
- [bt_bap_broadcast_assistant_cb](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md)
- [bt_bap_broadcast_assistant_add_src_param](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md)
- [bt_bap_broadcast_assistant_mod_src_param](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md)
- [BT_BAP_BASS_MAX_SUBGROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga443c212a736852305715452e7f165a9e)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [BT_BASE_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga1ebca62521cf4a6973d1fa8136e54be1)
- [UINT8_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#aeb4e270a084ee26fe73e799861bd0252)
- [BT_UUID_SIZE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d3506fd135b5cd8763446f572c161da)
- [BT_BAP_INVALID_BROADCAST_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga83cfb2a817e0db6d78c300dc5dea2d8a)
- [BT_BAP_PD_UNSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga3fb8ca6b5722cad7027553db40c4a94b)
- [BT_BAP_ADV_PARAM_CONN_QUICK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac290c620aa1861ea717dee37e1e83bfe)
- [BT_BAP_ADV_PARAM_CONN_REDUCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf1883b2596f793ef24913ef7f165c5dd)
- [BT_BAP_CONN_PARAM_SHORT_7_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga5d90920dfc8d554d0cd345edd0c36c66)
- [BT_BAP_CONN_PARAM_SHORT_10](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0469f86dc34ab738fbbcdf45cc105194)
- [BT_BAP_CONN_PARAM_RELAXED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gad4a19588129f8cbf085dca166f0bc486)
- [BT_BAP_ADV_PARAM_BROADCAST_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf2e44d06b8b7aba57a80b1f04e65d7de)
- [BT_BAP_ADV_PARAM_BROADCAST_SLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa11e0195a02baa656085f305d911042d)
- [BT_BAP_PER_ADV_PARAM_BROADCAST_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0f17a828720504892ff36447a4e3f7c3)
- [BT_BAP_PER_ADV_PARAM_BROADCAST_SLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf71bf639a2fca0c4d5ab61bfd6354668)
- [BT_BAP_BASS_VALID_BIT_BITFIELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga91adb24c76c0d14757c5eec0146caebb)
- [BT_BAP_QOS_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga7bd804c68e67d0b4bfe391d80d33a6c7)
- [BT_BAP_QOS_CFG_UNFRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gae578c78a10df4d1e4e6d1781ca48e1f5)
- [BT_BAP_QOS_CFG_FRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa91c55ca2de3ddf09620948fd4914b14)
- [BT_BAP_PA_INTERVAL_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga357079ef00ce6f250e72a37103926c64)
- [BT_BAP_BIS_SYNC_NO_PREF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga799f1417272e9b545c1e30ed4616b988)
- [BT_BAP_BIS_SYNC_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga2a2e4a06f6e39360458fe2e4d0b66833)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_bap_ep_func_t](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#gabb2b96d8de285dff7cbade83768d9aff)
- [bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)
- [bt_bap_unicast_group_foreach_stream_func_t](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gaf0e5a38208e90176292e745933b5e29e)
- [bt_bap_unicast_group_foreach_stream()](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gad608ee07c8a50abf586a3bc31921f032)
- [bt_bap_broadcast_source_foreach_stream_func_t](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#ga173ddb24e554afc1b16305cca69ad923)
- [bt_bap_broadcast_source_foreach_stream()](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#ga9d543b9282e0dadca3afe3a97e385b15)
- [bt_bap_scan_delegator_state_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf236a87ae461ad48ec59f487780b4824)
- [bt_bap_broadcast_assistant_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga496c8a2f599d997a7e6e033bda5f0c36)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_bap_qos_cfg_framing](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga37a5f9d7198739eef8bde6764da30de9)
- [BT_BAP_QOS_CFG_FRAMING_UNFRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga37a5f9d7198739eef8bde6764da30de9afe1ffd5db8e36f8082a2ef7545e04a94)
- [BT_BAP_QOS_CFG_FRAMING_FRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga37a5f9d7198739eef8bde6764da30de9a406ad3527d9d92e4e8b213fe52794298)
- [BT_BAP_QOS_CFG_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e8ebf4db88f94f44828bb6f41e81d44af5bc162fe51c445cb3c77bcf640bbe28)
- [BT_BAP_QOS_CFG_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147)
- [BT_BAP_QOS_CFG_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e8ebf4db88f94f44828bb6f41e81d44ab41e06fe31c57bb7dac5a77acb53be73)
- [bt_bap_pa_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac551e9b0d53fd50f3a9e9c08447f0296)
- [BT_BAP_PA_STATE_NOT_SYNCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf)
- [BT_BAP_PA_STATE_INFO_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb)
- [BT_BAP_PA_STATE_SYNCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc)
- [BT_BAP_PA_STATE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647)
- [BT_BAP_PA_STATE_NO_PAST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d)
- [bt_bap_big_enc_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga5e0b0f70d247e131fa542fae16826a22)
- [BT_BAP_BIG_ENC_STATE_NO_ENC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4)
- [BT_BAP_BIG_ENC_STATE_BCODE_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2)
- [BT_BAP_BIG_ENC_STATE_DEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10)
- [BT_BAP_BIG_ENC_STATE_BAD_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b)
- [bt_bap_bass_att_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga13e9b6d571a613d689b8ba58bae64ae3)
- [BT_BAP_BASS_ERR_OPCODE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c)
- [BT_BAP_BASS_ERR_INVALID_SRC_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202)
- [bt_bap_ep_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf210a91e1ff11d9bf7792ba47d1e1b4a)
- [BT_BAP_EP_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961)
- [BT_BAP_EP_STATE_CODEC_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688)
- [BT_BAP_EP_STATE_QOS_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523)
- [BT_BAP_EP_STATE_ENABLING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332)
- [BT_BAP_EP_STATE_STREAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710)
- [BT_BAP_EP_STATE_DISABLING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8)
- [BT_BAP_EP_STATE_RELEASING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c)
- [bt_bap_ep_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf15e5ec5bca364f6a3e7a43b1f27da68)
- [bt_bap_ep_get_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga575a109efb0fd1644634ce6e0288499b)
- [bt_bap_stream_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gab29c1e134156dceaa6c67abae9239378)
- [bt_bap_stream_config](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaaecbb590e5d073829d4c150e4fd2d8aa)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [bt_bap_stream_reconfig](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa7df3f6b906241ad5291295a6ddcf1e4)
- [bt_bap_stream_qos](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac878ed89242cac9a8514e8e4f1da4d9d)
- [bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [bt_bap_stream_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga13a859b31b0310ec22339ec7ed0754f8)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_bap_stream_metadata](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0afe6c927729697e2f984cefcbc7c0f1)
- [bt_bap_stream_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0fd2bb35909fc19e3e9cff068ba9e9aa)
- [bt_bap_stream_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa75f2cd2c36fdaef04a62c95bec6e2e3)
- [bt_bap_stream_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga8f2dc67c35299334d21c7dee7b8664ae)
- [bt_bap_stream_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gada72bcd3951eff2bc6b70c02dcaed98b)
- [bt_bap_stream_release](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaaf94f1f0dda7ef356c0f9ae79b5c60e4)
- [bt_bap_stream_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga63b69967aa92224a2bd9cf79eb41773e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_bap_stream_send_ts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa0e012446238c916abc84d6c0de89bf3)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_bap_stream_get_tx_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga47eb6219d730d75ddc4f49dceac7e928)
- [bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)
- [bt_bap_unicast_server_register](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#gab3ea6014854e6290f058c87e866c3191)
- [bt_bap_unicast_server_unregister](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#ga6ef3b9e877ffdc04cc48fda6713a0209)
- [bt_bap_unicast_server_register_cb](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#ga7669133936bc13f7ab38817db9ce69c0)
- [bt_bap_unicast_server_unregister_cb](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#gadf984f12bdeadcfc814dc2fc770cb7bf)
- [bt_bap_unicast_server_foreach_ep](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#gafe7640d6269ec95c8af6d7549fac785d)
- [bt_bap_unicast_server_config_ase](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md#ga98b170c9f371d7d60c3dde9aff3f6d6b)
- [bt_bap_qos_cfg_pref](../bluetooth_le_audio_model_reference/P028_bt_bap_qos_cfg_pref_结构体.md)
- [bt_bap_unicast_group_reconfig](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gacd684504c8127ff4f8d038cc06718e5e)
- [bt_bap_unicast_group_add_streams](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#ga9cc792cd1eaaa79d56f3df0e2341cbf6)
- [bt_bap_unicast_group_delete](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#ga34dbdce6133f8366df453ec937fb47d2)
- [bt_bap_unicast_group_get_info](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#ga4ba0e4c3fa7ec3a36a64a19c80027504)
- [bt_bap_unicast_client_register_cb](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gade70f04ae1a828b43b3b44fa8933f674)
- [bt_bap_unicast_client_unregister_cb](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gaee092a4e918a67bb5fd94cb78cc21141)
- [bt_bap_unicast_client_discover](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gacef9c88f66762e8de19303d20dafa0bb)
- [bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)
- [bt_bap_unicast_client_qos_from_group](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gad963bdda290df96036a68b00cc940eca)
- [bt_bap_qos_cfg_eq](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md#gad106ae43201100940d9145d291fe9ca3)
- [bt_bap_base_get_base_from_ad](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga29423a39d76ad16f0586d82a23c07ba7)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [bt_bap_base_get_size](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga539f92b71ec34f0551ef6240d83b972e)
- [bt_bap_base_get_pres_delay](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#gaf91f45bcf7df2f368c5abeb116b65dd0)
- [bt_bap_base_get_subgroup_count](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#gadcae0230168564da1ee8b3c577ce27d7)
- [bt_bap_base_get_bis_indexes](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga6deab5a8b7a16ddf0c3685d4003694e1)
- [bt_bap_base_foreach_subgroup](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga5e6e0b758409cbdde93c0f648ef5e5e8)
- [bt_bap_base_get_subgroup_codec_id](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#gae75e05a002dee8336eb066ae8231ea0c)
- [bt_bap_base_get_subgroup_codec_data](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga10e2e32dc2802ba55d55c77148331f6a)
- [bt_bap_base_get_subgroup_codec_meta](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#gafb9d9544f38c7ad2613fff1679eb1f0c)
- [bt_bap_base_subgroup_codec_to_codec_cfg](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga920e3409f1978b803bcf6bc8d05ac8f6)
- [编解码器配置解析 API（Codec config parsing APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html)
- [bt_bap_base_get_subgroup_bis_count](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga051e1f8aa2faf3ba7a973356138fd2d3)
- [bt_bap_base_subgroup_get_bis_indexes](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga37df3bf1e18d2d8e9388541217b2e366)
- [bt_bap_base_subgroup_foreach_bis](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#ga4f85ee43984cb2f3139b41da7b9b1aee)
- [bt_bap_base_subgroup_bis_codec_to_codec_cfg](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md#gaa5cb191df7807ea87f1fba1871ca8ebe)
- [bt_bap_broadcast_source_register_cb](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gac75ad00b8f9a1cd7048677a33b17acda)
- [bt_bap_broadcast_source_unregister_cb](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gacc8d26c42c6b4ae6dc11af84ec4af616)
- [bt_bap_broadcast_source_create](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gacdebfc435eebd47cf9cd05099a5f78e0)
- [bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)
- [bt_bap_broadcast_source_reconfig](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gabecaa9db7be5cb03ed997ba478878d40)
- [bt_bap_broadcast_source_update_metadata](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gaff2cfdadbff3ebe1e2efb660dee56f02)
- [bt_bap_broadcast_source_start](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gac4640f5207599d51c1a63ff47f3c1d5a)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_bap_broadcast_source_stop](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#ga36a885581eec5cab8b3f652db19b9aba)
- [bt_bap_broadcast_source_delete](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#ga12e0a4856115a8eb297fe2d1fc130155)
- [bt_bap_broadcast_source_get_base](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gafe07e4c6962858500fcf66415a173be8)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_bap_broadcast_sink_register_cb](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md#ga1b83ead634d990e954f233d0208c5a85)
- [bt_bap_broadcast_sink_create](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md#ga0637d1957db70ad39e0608ed07e75166)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)
- [bt_bap_broadcast_sink_sync](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md#gacadebb5ce8aab5f5b8f1ff7e0fa57805)
- [BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)
- [bt_bap_broadcast_sink_stop](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md#ga1020b21bfb4195aeb5823197145b1fe9)
- [bt_bap_broadcast_sink_delete](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md#ga8b9d6cb409a3671654e053475ada3fda)
- [bt_bap_scan_delegator_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga7632ab444dbf99387871f7d0c90b11ba)
- [bt_bap_scan_delegator_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga6f52e58767303ded16cb6289f094895a)
- [bt_bap_scan_delegator_set_pa_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga381c1f3b386ecbdfd570eb125882161e)
- [bt_bap_scan_delegator_set_bis_sync_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf610cd6cddd52622f95cfd35b19ee841)
- [bt_bap_scan_delegator_rem_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga6c240f1cdb33945197700e4fe106ef2c)
- [bt_bap_scan_delegator_foreach_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gab6f1a12699a9437c6575c70df33d5be0)
- [bt_bap_scan_delegator_find_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gabec9fd0a2966e1811fd4770855050510)
- [bt_bap_broadcast_assistant_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gab59c5ebc4fef28da34d8a54b1244c33b)
- [bt_bap_broadcast_assistant_scan_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga98ac067e66d263aa41fc6f8df6bb9126)
- [bt_bap_broadcast_assistant_scan_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga76cae35df980b78a10551811050b2760)
- [bt_bap_broadcast_assistant_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gabab24c44e9833029965475ad7b149e6e)
- [bt_bap_broadcast_assistant_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga679cdeb6e555bfc9ce20f38e493000ee)
- [bt_bap_broadcast_assistant_add_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac93cb4cab33d0b937e752bc0b71cad9e)
- [bt_bap_broadcast_assistant_mod_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa9c292a7dcb470926d8d7d4be699a0c7)
- [bt_bap_broadcast_assistant_set_broadcast_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gabcec07689c13a996bcb9d2d417347dbb)
- [bt_bap_broadcast_assistant_rem_src](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga09785690db551677a043fcaa2fdb7f29)
- [bt_bap_broadcast_assistant_read_recv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga94fce2b4346b1026d53e0b860ca7fbf2)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__bluetooth__classic__map.h_文件参考.md)
