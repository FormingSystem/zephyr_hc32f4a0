---
id: learning.zephyr-docs.api-socket-lora-topic-reference.page-4
title: 蓝牙基本音频配置文件（Bluetooth Basic Audio Profile）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_蓝牙基本音频配置文件（Bluetooth Basic Audio Profile）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙基本音频配置文件（Bluetooth Basic Audio Profile，BAP）

<a id="details"></a>

蓝牙基本音频配置文件（Basic Audio Profile，BAP）。起始版本（Since）：3.0。版本（Version）：0.8.0。BAP 支持单播（Unicast）和广播（Broadcast）音频流（Audio Stream）控制。

<a id="header-groups"></a>
<a id="groups"></a>

## 4.1\_主题（Topics）

<a id="r_bt_5Fbap_5Fbroadcast"></a>

相关声明：[BAP 广播 API（Broadcast APIs）](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md)。

BAP 广播 API（Broadcast APIs）

<a id="r_bt_5Fbap_5Fbroadcast_5Fsink"></a>

相关声明：[BAP 广播接收端 API（Broadcast Sink APIs）](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md)。

BAP 广播接收端 API（Broadcast Sink APIs）

<a id="r_bt_5Fbap_5Fbroadcast_5Fsource"></a>

相关声明：[BAP 广播源 API（Broadcast Source APIs）](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md)。

BAP 广播源 API（Broadcast Source APIs）

<a id="r_bt_5Fbap_5Funicast_5Fclient"></a>

相关声明：[BAP 单播客户端 API（Unicast Client APIs）](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md)。

<a id="r_bt_5Fbap_5Funicast_5Fserver"></a>

相关声明：[BAP 单播服务器 API（Unicast Server APIs）](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.2\_数据结构（Data Structures）

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

```c
struct bt_bap_broadcast_source
```

相关声明：[bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)。

抽象音频广播源结构体（Abstract Audio Broadcast Source Structure）。

```c
struct bt_bap_broadcast_sink
```

相关声明：[bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)。

抽象音频广播接收端结构体（Abstract Audio Broadcast Sink Structure）。

<a id="r_bt_5Fbap_5Funicast_5Fgroup"></a>

```c
struct bt_bap_unicast_group
```

相关声明：[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)。

抽象音频单播组结构体（Abstract Audio Unicast Group Structure）。

<a id="r_bt_5Fbap_5Fep"></a>

```c
struct bt_bap_ep
```

相关声明：[bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)。

抽象音频端点结构体（Abstract Audio Endpoint Structure）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.3\_宏定义（Macros）

<a id="r_ga443c212a736852305715452e7f165a9e"></a>

```c
#define BT_BAP_BASS_MAX_SUBGROUPS COND_CODE_1(CONFIG_BT_AUDIO, (CONFIG_BT_BAP_BASS_MAX_SUBGROUPS), (0))
```

相关声明：[BT_BAP_BASS_MAX_SUBGROUPS](#ga443c212a736852305715452e7f165a9e)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

BAP 扫描委托端 API（Scan Delegator API）支持的最大子组数（Maximum Number of Subgroups）。

<a id="r_ga1ebca62521cf4a6973d1fa8136e54be1"></a>

```c
#define BT_BASE_MAX_SIZE (UINT8_MAX - 1 /* type */ - BT_UUID_SIZE_16)
```

相关声明：[BT_BASE_MAX_SIZE](#ga1ebca62521cf4a6973d1fa8136e54be1)、[UINT8_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#aeb4e270a084ee26fe73e799861bd0252)、[BT_UUID_SIZE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d3506fd135b5cd8763446f572c161da)。

不含服务数据头部（Service Data Header）的 BASE 最大大小。

<a id="r_ga83cfb2a817e0db6d78c300dc5dea2d8a"></a>

```c
#define BT_BAP_INVALID_BROADCAST_ID 0xFFFFFFFFU
```

相关声明：[BT_BAP_INVALID_BROADCAST_ID](#ga83cfb2a817e0db6d78c300dc5dea2d8a)。

无效的广播标识符（Broadcast ID）。

<a id="r_ga3fb8ca6b5722cad7027553db40c4a94b"></a>

```c
#define BT_BAP_PD_UNSET 0xFFFFFFFFU
```

相关声明：[BT_BAP_PD_UNSET](#ga3fb8ca6b5722cad7027553db40c4a94b)。

表示尚未设置呈现延迟（Presentation Delay）的值。

<a id="r_gac290c620aa1861ea717dee37e1e83bfe"></a>

```c
#define BT_BAP_ADV_PARAM_CONN_QUICK
```

相关声明：[BT_BAP_ADV_PARAM_CONN_QUICK](#gac290c620aa1861ea717dee37e1e83bfe)。

建议的可连接广播参数（Connectable Advertising Parameters）。

<a id="r_gaf1883b2596f793ef24913ef7f165c5dd"></a>

```c
#define BT_BAP_ADV_PARAM_CONN_REDUCED
```

相关声明：[BT_BAP_ADV_PARAM_CONN_REDUCED](#gaf1883b2596f793ef24913ef7f165c5dd)。

缩减的可连接广播参数（Reduced Connectable Advertising Parameters）。

<a id="r_ga5d90920dfc8d554d0cd345edd0c36c66"></a>

```c
#define BT_BAP_CONN_PARAM_SHORT_7_5
```

相关声明：[BT_BAP_CONN_PARAM_SHORT_7_5](#ga5d90920dfc8d554d0cd345edd0c36c66)。

适用于 7.5 ms 服务数据单元间隔（SDU Interval）的初始连接请求建议连接参数（Connection Parameters）。

<a id="r_ga0469f86dc34ab738fbbcdf45cc105194"></a>

```c
#define BT_BAP_CONN_PARAM_SHORT_10
```

相关声明：[BT_BAP_CONN_PARAM_SHORT_10](#ga0469f86dc34ab738fbbcdf45cc105194)。

适用于 10 ms 服务数据单元间隔（SDU Interval）的初始连接请求建议连接参数（Connection Parameters）。

<a id="r_gad4a19588129f8cbf085dca166f0bc486"></a>

```c
#define BT_BAP_CONN_PARAM_RELAXED
```

相关声明：[BT_BAP_CONN_PARAM_RELAXED](#gad4a19588129f8cbf085dca166f0bc486)。

用于 ACL 与 ISO 共存（Coexistence）的建议连接参数（Connection Parameters）。

<a id="r_gaf2e44d06b8b7aba57a80b1f04e65d7de"></a>

```c
#define BT_BAP_ADV_PARAM_BROADCAST_FAST
```

相关声明：[BT_BAP_ADV_PARAM_BROADCAST_FAST](#gaf2e44d06b8b7aba57a80b1f04e65d7de)。

广播音频的快速广播参数（Fast Advertising Parameters）。

<a id="r_gaa11e0195a02baa656085f305d911042d"></a>

```c
#define BT_BAP_ADV_PARAM_BROADCAST_SLOW
```

相关声明：[BT_BAP_ADV_PARAM_BROADCAST_SLOW](#gaa11e0195a02baa656085f305d911042d)。

广播音频的慢速广播参数（Slow Advertising Parameters）。

<a id="r_ga0f17a828720504892ff36447a4e3f7c3"></a>

```c
#define BT_BAP_PER_ADV_PARAM_BROADCAST_FAST
```

相关声明：[BT_BAP_PER_ADV_PARAM_BROADCAST_FAST](#ga0f17a828720504892ff36447a4e3f7c3)。

广播音频的快速广播参数（Fast Advertising Parameters）。

<a id="r_gaf71bf639a2fca0c4d5ab61bfd6354668"></a>

```c
#define BT_BAP_PER_ADV_PARAM_BROADCAST_SLOW
```

相关声明：[BT_BAP_PER_ADV_PARAM_BROADCAST_SLOW](#gaf71bf639a2fca0c4d5ab61bfd6354668)。

广播音频的慢速广播参数（Slow Advertising Parameters）。

<a id="r_ga91adb24c76c0d14757c5eec0146caebb"></a>

```c
#define BT_BAP_BASS_VALID_BIT_BITFIELD(_bis_bitfield)
```

相关声明：[BT_BAP_BASS_VALID_BIT_BITFIELD](#ga91adb24c76c0d14757c5eec0146caebb)。

检查 BAP BASS 的 `BIS_Sync` 位字段（Bitfield）是否有效。

<a id="r_ga7bd804c68e67d0b4bfe391d80d33a6c7"></a>

```c
#define BT_BAP_QOS_CFG(_interval, _framing, _phy, _sdu, _rtn, _latency, _pd)
```

相关声明：[BT_BAP_QOS_CFG](#ga7bd804c68e67d0b4bfe391d80d33a6c7)。

用于声明 `bt_bap_qos_cfg` 元素（Elements）的辅助宏。

<a id="r_gae578c78a10df4d1e4e6d1781ca48e1f5"></a>

```c
#define BT_BAP_QOS_CFG_UNFRAMED(_interval, _sdu, _rtn, _latency, _pd)
```

相关声明：[BT_BAP_QOS_CFG_UNFRAMED](#gae578c78a10df4d1e4e6d1781ca48e1f5)。

用于声明非成帧输入（Input Unframed）`bt_bap_qos_cfg` 的辅助宏。

<a id="r_gaa91c55ca2de3ddf09620948fd4914b14"></a>

```c
#define BT_BAP_QOS_CFG_FRAMED(_interval, _sdu, _rtn, _latency, _pd)
```

相关声明：[BT_BAP_QOS_CFG_FRAMED](#gaa91c55ca2de3ddf09620948fd4914b14)。

用于声明成帧输入（Input Framed）`bt_bap_qos_cfg` 的辅助宏。

<a id="r_ga357079ef00ce6f250e72a37103926c64"></a>

```c
#define BT_BAP_PA_INTERVAL_UNKNOWN 0xFFFFU
```

相关声明：[BT_BAP_PA_INTERVAL_UNKNOWN](#ga357079ef00ce6f250e72a37103926c64)。

表示周期广播间隔（Periodic Advertising Interval）未知的值。

<a id="r_ga799f1417272e9b545c1e30ed4616b988"></a>

```c
#define BT_BAP_BIS_SYNC_NO_PREF 0xFFFFFFFFU
```

相关声明：[BT_BAP_BIS_SYNC_NO_PREF](#ga799f1417272e9b545c1e30ed4616b988)。

广播助理（Broadcast Assistant）没有 BIS 同步偏好（BIS Sync Preference）。

<a id="r_ga2a2e4a06f6e39360458fe2e4d0b66833"></a>

```c
#define BT_BAP_BIS_SYNC_FAILED 0xFFFFFFFFU
```

相关声明：[BT_BAP_BIS_SYNC_FAILED](#ga2a2e4a06f6e39360458fe2e4d0b66833)。

表示 BIG 同步（BIG Sync）因任意原因失败的 BIS 同步值（BIS Sync Value）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.4\_类型定义（Typedefs）

<a id="r_gaf236a87ae461ad48ec59f487780b4824"></a>

```c
typedef bool(* bt_bap_scan_delegator_state_func_t) (const struct bt_bap_scan_delegator_recv_state *recv_state, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_bap_scan_delegator_state_func_t](#gaf236a87ae461ad48ec59f487780b4824)、[bt_bap_scan_delegator_recv_state](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md)。

用于扫描委托端接收状态搜索函数（Scan Delegator Receive State Search Functions）的回调函数（Callback Function）。

<a id="r_ga496c8a2f599d997a7e6e033bda5f0c36"></a>

```c
typedef void(* bt_bap_broadcast_assistant_write_cb) (struct bt_conn *conn, int err)
```

相关声明：[bt_bap_broadcast_assistant_write_cb](#ga496c8a2f599d997a7e6e033bda5f0c36)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

写入操作的回调函数（Callback Function）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.5\_枚举（Enumerations）

<a id="r_ga37a5f9d7198739eef8bde6764da30de9"></a>

```c
enum bt_bap_qos_cfg_framing { BT_BAP_QOS_CFG_FRAMING_UNFRAMED = 0x00 , BT_BAP_QOS_CFG_FRAMING_FRAMED = 0x01 }
```

相关声明：[bt_bap_qos_cfg_framing](#ga37a5f9d7198739eef8bde6764da30de9)、[BT_BAP_QOS_CFG_FRAMING_UNFRAMED](#gga37a5f9d7198739eef8bde6764da30de9afe1ffd5db8e36f8082a2ef7545e04a94)、[BT_BAP_QOS_CFG_FRAMING_FRAMED](#gga37a5f9d7198739eef8bde6764da30de9a406ad3527d9d92e4e8b213fe52794298)。

QoS 成帧方式（Framing）。

<a id="r_ga5e8ebf4db88f94f44828bb6f41e81d44"></a>

```c
enum { BT_BAP_QOS_CFG_1M = (1UL << (0U)) , BT_BAP_QOS_CFG_2M = (1UL << (1U)) , BT_BAP_QOS_CFG_CODED = (1UL << (2U)) }
```

相关声明：[BT_BAP_QOS_CFG_1M](#gga5e8ebf4db88f94f44828bb6f41e81d44af5bc162fe51c445cb3c77bcf640bbe28)、[BT_BAP_QOS_CFG_2M](#gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147)、[BT_BAP_QOS_CFG_CODED](#gga5e8ebf4db88f94f44828bb6f41e81d44ab41e06fe31c57bb7dac5a77acb53be73)。

服务质量首选物理层（QoS Preferred PHY）。

<a id="r_gac551e9b0d53fd50f3a9e9c08447f0296"></a>

```c
enum bt_bap_pa_state { BT_BAP_PA_STATE_NOT_SYNCED = 0x00 , BT_BAP_PA_STATE_INFO_REQ = 0x01 , BT_BAP_PA_STATE_SYNCED = 0x02 , BT_BAP_PA_STATE_FAILED = 0x03 , BT_BAP_PA_STATE_NO_PAST = 0x04 }
```

相关声明：[bt_bap_pa_state](#gac551e9b0d53fd50f3a9e9c08447f0296)、[BT_BAP_PA_STATE_NOT_SYNCED](#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf)、[BT_BAP_PA_STATE_INFO_REQ](#ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb)、[BT_BAP_PA_STATE_SYNCED](#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc)、[BT_BAP_PA_STATE_FAILED](#ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647)、[BT_BAP_PA_STATE_NO_PAST](#ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d)。

扫描委托端（Scan Delegator）报告的周期广播状态（Periodic Advertising State）。

<a id="r_ga5e0b0f70d247e131fa542fae16826a22"></a>

```c
enum bt_bap_big_enc_state { BT_BAP_BIG_ENC_STATE_NO_ENC = 0x00 , BT_BAP_BIG_ENC_STATE_BCODE_REQ = 0x01 , BT_BAP_BIG_ENC_STATE_DEC = 0x02 , BT_BAP_BIG_ENC_STATE_BAD_CODE = 0x03 }
```

相关声明：[bt_bap_big_enc_state](#ga5e0b0f70d247e131fa542fae16826a22)、[BT_BAP_BIG_ENC_STATE_NO_ENC](#gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4)、[BT_BAP_BIG_ENC_STATE_BCODE_REQ](#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2)、[BT_BAP_BIG_ENC_STATE_DEC](#gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10)、[BT_BAP_BIG_ENC_STATE_BAD_CODE](#gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b)。

扫描委托端（Scan Delegator）报告的广播等时组加密状态（Broadcast Isochronous Group Encryption State）。

<a id="r_ga13e9b6d571a613d689b8ba58bae64ae3"></a>

```c
enum bt_bap_bass_att_err { BT_BAP_BASS_ERR_OPCODE_NOT_SUPPORTED = 0x80 , BT_BAP_BASS_ERR_INVALID_SRC_ID = 0x81 }
```

相关声明：[bt_bap_bass_att_err](#ga13e9b6d571a613d689b8ba58bae64ae3)、[BT_BAP_BASS_ERR_OPCODE_NOT_SUPPORTED](#gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c)、[BT_BAP_BASS_ERR_INVALID_SRC_ID](#gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202)。

广播音频扫描服务（Broadcast Audio Scan Service，BASS）特定的 ATT 错误码（Error Code）。

<a id="r_gaf210a91e1ff11d9bf7792ba47d1e1b4a"></a>

```c
enum bt_bap_ep_state { BT_BAP_EP_STATE_IDLE = 0x00 , BT_BAP_EP_STATE_CODEC_CONFIGURED = 0x01 , BT_BAP_EP_STATE_QOS_CONFIGURED = 0x02 , BT_BAP_EP_STATE_ENABLING = 0x03 , BT_BAP_EP_STATE_STREAMING = 0x04 , BT_BAP_EP_STATE_DISABLING = 0x05 , BT_BAP_EP_STATE_RELEASING = 0x06 }
```

相关声明：[bt_bap_ep_state](#gaf210a91e1ff11d9bf7792ba47d1e1b4a)、[BT_BAP_EP_STATE_IDLE](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961)、[BT_BAP_EP_STATE_CODEC_CONFIGURED](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688)、[BT_BAP_EP_STATE_QOS_CONFIGURED](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523)、[BT_BAP_EP_STATE_ENABLING](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332)、[BT_BAP_EP_STATE_STREAMING](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710)、[BT_BAP_EP_STATE_DISABLING](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8)、[BT_BAP_EP_STATE_RELEASING](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c)。

端点状态（Endpoint States）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.6\_函数（Functions）

<a id="r_gaf15e5ec5bca364f6a3e7a43b1f27da68"></a>

```c
int bt_bap_ep_get_info (const struct bt_bap_ep *ep, struct bt_bap_ep_info *info)
```

相关声明：[bt_bap_ep_get_info](#gaf15e5ec5bca364f6a3e7a43b1f27da68)、[bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)、[bt_bap_ep_info](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md)。

返回包含音频流端点信息（Audio Stream Endpoint Information）的结构体。

<a id="r_ga575a109efb0fd1644634ce6e0288499b"></a>

```c
struct bt_conn * bt_bap_ep_get_conn (const struct bt_bap_ep *ep)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_ep_get_conn](#ga575a109efb0fd1644634ce6e0288499b)、[bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)。

获取指向端点 ACL 连接（ACL Connection）的指针。

<a id="r_gab29c1e134156dceaa6c67abae9239378"></a>

```c
void bt_bap_stream_cb_register (struct bt_bap_stream *stream, struct bt_bap_stream_ops *ops)
```

相关声明：[bt_bap_stream_cb_register](#gab29c1e134156dceaa6c67abae9239378)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)。

为流（Stream）注册音频回调（Audio Callbacks）。

<a id="r_gaaecbb590e5d073829d4c150e4fd2d8aa"></a>

```c
int bt_bap_stream_config (struct bt_conn *conn, struct bt_bap_stream *stream, struct bt_bap_ep *ep, const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_bap_stream_config](#gaaecbb590e5d073829d4c150e4fd2d8aa)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

配置音频流（Audio Stream）。

<a id="r_gaa7df3f6b906241ad5291295a6ddcf1e4"></a>

```c
int bt_bap_stream_reconfig (struct bt_bap_stream *stream, const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_bap_stream_reconfig](#gaa7df3f6b906241ad5291295a6ddcf1e4)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

重新配置音频流（Audio Stream）。

<a id="r_gac878ed89242cac9a8514e8e4f1da4d9d"></a>

```c
int bt_bap_stream_qos (struct bt_conn *conn, struct bt_bap_unicast_group *group)
```

相关声明：[bt_bap_stream_qos](#gac878ed89242cac9a8514e8e4f1da4d9d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

配置音频流服务质量（Audio Stream QoS）。

<a id="r_ga13a859b31b0310ec22339ec7ed0754f8"></a>

```c
int bt_bap_stream_enable (struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len)
```

相关声明：[bt_bap_stream_enable](#ga13a859b31b0310ec22339ec7ed0754f8)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启用音频流（Audio Stream）。

<a id="r_ga0afe6c927729697e2f984cefcbc7c0f1"></a>

```c
int bt_bap_stream_metadata (struct bt_bap_stream *stream, const uint8_t meta[], size_t meta_len)
```

相关声明：[bt_bap_stream_metadata](#ga0afe6c927729697e2f984cefcbc7c0f1)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更改音频流元数据（Audio Stream Metadata）。

<a id="r_ga0fd2bb35909fc19e3e9cff068ba9e9aa"></a>

```c
int bt_bap_stream_disable (struct bt_bap_stream *stream)
```

相关声明：[bt_bap_stream_disable](#ga0fd2bb35909fc19e3e9cff068ba9e9aa)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

禁用音频流（Audio Stream）。

<a id="r_gaa75f2cd2c36fdaef04a62c95bec6e2e3"></a>

```c
int bt_bap_stream_connect (struct bt_bap_stream *stream)
```

相关声明：[bt_bap_stream_connect](#gaa75f2cd2c36fdaef04a62c95bec6e2e3)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

连接单播音频流（Unicast Audio Stream）。

<a id="r_ga8f2dc67c35299334d21c7dee7b8664ae"></a>

```c
int bt_bap_stream_start (struct bt_bap_stream *stream)
```

相关声明：[bt_bap_stream_start](#ga8f2dc67c35299334d21c7dee7b8664ae)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

启动音频流（Audio Stream）。

<a id="r_gada72bcd3951eff2bc6b70c02dcaed98b"></a>

```c
int bt_bap_stream_stop (struct bt_bap_stream *stream)
```

相关声明：[bt_bap_stream_stop](#gada72bcd3951eff2bc6b70c02dcaed98b)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

停止音频流（Audio Stream）。

<a id="r_gaaf94f1f0dda7ef356c0f9ae79b5c60e4"></a>

```c
int bt_bap_stream_release (struct bt_bap_stream *stream)
```

相关声明：[bt_bap_stream_release](#gaaf94f1f0dda7ef356c0f9ae79b5c60e4)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

释放音频流（Audio Stream）。

<a id="r_ga63b69967aa92224a2bd9cf79eb41773e"></a>

```c
int bt_bap_stream_send (struct bt_bap_stream *stream, struct net_buf *buf, uint16_t seq_num)
```

相关声明：[bt_bap_stream_send](#ga63b69967aa92224a2bd9cf79eb41773e)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向音频流（Audio Stream）发送不带时间戳（Timestamp）的数据。

<a id="r_gaa0e012446238c916abc84d6c0de89bf3"></a>

```c
int bt_bap_stream_send_ts (struct bt_bap_stream *stream, struct net_buf *buf, uint16_t seq_num, uint32_t ts)
```

相关声明：[bt_bap_stream_send_ts](#gaa0e012446238c916abc84d6c0de89bf3)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向音频流（Audio Stream）发送带时间戳（Timestamp）的数据。

<a id="r_ga47eb6219d730d75ddc4f49dceac7e928"></a>

```c
int bt_bap_stream_get_tx_sync (struct bt_bap_stream *stream, struct bt_iso_tx_info *info)
```

相关声明：[bt_bap_stream_get_tx_sync](#ga47eb6219d730d75ddc4f49dceac7e928)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)。

获取基本音频配置文件流（Basic Audio Profile Stream）的等时传输时序信息（ISO Transmission Timing Info）。

<a id="r_ga7632ab444dbf99387871f7d0c90b11ba"></a>

```c
int bt_bap_scan_delegator_register (struct bt_bap_scan_delegator_cb *cb)
```

相关声明：[bt_bap_scan_delegator_register](#ga7632ab444dbf99387871f7d0c90b11ba)、[bt_bap_scan_delegator_cb](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md)。

注册基本音频配置文件扫描委托端（Basic Audio Profile Scan Delegator）和广播音频扫描服务（BASS）。

<a id="r_ga6f52e58767303ded16cb6289f094895a"></a>

```c
int bt_bap_scan_delegator_unregister (void)
```

相关声明：[bt_bap_scan_delegator_unregister](#ga6f52e58767303ded16cb6289f094895a)。

注销基本音频配置文件扫描委托端（Basic Audio Profile Scan Delegator）和广播音频扫描服务（BASS）。

<a id="r_ga381c1f3b386ecbdfd570eb125882161e"></a>

```c
int bt_bap_scan_delegator_set_pa_state (uint8_t src_id, enum bt_bap_pa_state pa_state)
```

相关声明：[bt_bap_scan_delegator_set_pa_state](#ga381c1f3b386ecbdfd570eb125882161e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_bap_pa_state](#gac551e9b0d53fd50f3a9e9c08447f0296)。

将周期广播同步状态（Periodic Advertising Sync State）设为正在同步（Syncing）。

<a id="r_gaf610cd6cddd52622f95cfd35b19ee841"></a>

```c
int bt_bap_scan_delegator_set_bis_sync_state (uint8_t src_id, uint32_t bis_synced[0])
```

相关声明：[bt_bap_scan_delegator_set_bis_sync_state](#gaf610cd6cddd52622f95cfd35b19ee841)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置服务器中某个接收状态（Receive State）的同步状态（Sync State）。

<a id="r_ga6eb2a782d761da12d112356cfe723ff0"></a>

```c
int bt_bap_scan_delegator_add_src (const struct bt_bap_scan_delegator_add_src_param *param)
```

相关声明：[bt_bap_scan_delegator_add_src](#ga6eb2a782d761da12d112356cfe723ff0)、[bt_bap_scan_delegator_add_src_param](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md)。

在本地添加接收状态源（Receive State Source）。

<a id="r_gac022f38269742f16ff6887840ef5ba9a"></a>

```c
int bt_bap_scan_delegator_mod_src (const struct bt_bap_scan_delegator_mod_src_param *param)
```

相关声明：[bt_bap_scan_delegator_mod_src](#gac022f38269742f16ff6887840ef5ba9a)、[bt_bap_scan_delegator_mod_src_param](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md)。

在本地添加接收状态源（Receive State Source）。

<a id="r_ga6c240f1cdb33945197700e4fe106ef2c"></a>

```c
int bt_bap_scan_delegator_rem_src (uint8_t src_id)
```

相关声明：[bt_bap_scan_delegator_rem_src](#ga6c240f1cdb33945197700e4fe106ef2c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

移除接收状态源（Receive State Source）。

<a id="r_gab6f1a12699a9437c6575c70df33d5be0"></a>

```c
void bt_bap_scan_delegator_foreach_state (bt_bap_scan_delegator_state_func_t func, void *user_data)
```

相关声明：[bt_bap_scan_delegator_foreach_state](#gab6f1a12699a9437c6575c70df33d5be0)、[bt_bap_scan_delegator_state_func_t](#gaf236a87ae461ad48ec59f487780b4824)。

遍历全部现有接收状态（Receive State）。

<a id="r_gabec9fd0a2966e1811fd4770855050510"></a>

```c
const struct bt_bap_scan_delegator_recv_state * bt_bap_scan_delegator_find_state (bt_bap_scan_delegator_state_func_t func, void *user_data)
```

相关声明：[bt_bap_scan_delegator_recv_state](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md)、[bt_bap_scan_delegator_find_state](#gabec9fd0a2966e1811fd4770855050510)、[bt_bap_scan_delegator_state_func_t](#gaf236a87ae461ad48ec59f487780b4824)。

依据比较函数（Compare Function）查找并返回接收状态（Receive State）。

<a id="r_gab59c5ebc4fef28da34d8a54b1244c33b"></a>

```c
int bt_bap_broadcast_assistant_discover (struct bt_conn *conn)
```

相关声明：[bt_bap_broadcast_assistant_discover](#gab59c5ebc4fef28da34d8a54b1244c33b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现服务器上的广播音频扫描服务（Broadcast Audio Scan Service）。

<a id="r_ga98ac067e66d263aa41fc6f8df6bb9126"></a>

```c
int bt_bap_broadcast_assistant_scan_start (struct bt_conn *conn, bool start_scan)
```

相关声明：[bt_bap_broadcast_assistant_scan_start](#ga98ac067e66d263aa41fc6f8df6bb9126)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为远端服务器启动广播等时流（BIS）扫描。

<a id="r_ga76cae35df980b78a10551811050b2760"></a>

```c
int bt_bap_broadcast_assistant_scan_stop (struct bt_conn *conn)
```

相关声明：[bt_bap_broadcast_assistant_scan_stop](#ga76cae35df980b78a10551811050b2760)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

停止针对服务器的远端广播等时流（BIS）扫描。

<a id="r_gabab24c44e9833029965475ad7b149e6e"></a>

```c
int bt_bap_broadcast_assistant_register_cb (struct bt_bap_broadcast_assistant_cb *cb)
```

相关声明：[bt_bap_broadcast_assistant_register_cb](#gabab24c44e9833029965475ad7b149e6e)、[bt_bap_broadcast_assistant_cb](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md)。

注册广播音频扫描服务客户端（Broadcast Audio Scan Service Client）使用的回调（Callback）。

<a id="r_ga679cdeb6e555bfc9ce20f38e493000ee"></a>

```c
int bt_bap_broadcast_assistant_unregister_cb (struct bt_bap_broadcast_assistant_cb *cb)
```

相关声明：[bt_bap_broadcast_assistant_unregister_cb](#ga679cdeb6e555bfc9ce20f38e493000ee)、[bt_bap_broadcast_assistant_cb](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md)。

注销广播音频扫描服务客户端（Broadcast Audio Scan Service Client）使用的回调（Callback）。

<a id="r_gac93cb4cab33d0b937e752bc0b71cad9e"></a>

```c
int bt_bap_broadcast_assistant_add_src (struct bt_conn *conn, const struct bt_bap_broadcast_assistant_add_src_param *param)
```

相关声明：[bt_bap_broadcast_assistant_add_src](#gac93cb4cab33d0b937e752bc0b71cad9e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_broadcast_assistant_add_src_param](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md)。

在服务器上添加源（Source）。

<a id="r_gaa9c292a7dcb470926d8d7d4be699a0c7"></a>

```c
int bt_bap_broadcast_assistant_mod_src (struct bt_conn *conn, const struct bt_bap_broadcast_assistant_mod_src_param *param)
```

相关声明：[bt_bap_broadcast_assistant_mod_src](#gaa9c292a7dcb470926d8d7d4be699a0c7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_bap_broadcast_assistant_mod_src_param](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md)。

修改服务器上的源（Source）。

<a id="r_gabcec07689c13a996bcb9d2d417347dbb"></a>

```c
int bt_bap_broadcast_assistant_set_broadcast_code (struct bt_conn *conn, uint8_t src_id, const uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE])
```

相关声明：[bt_bap_broadcast_assistant_set_broadcast_code](#gabcec07689c13a996bcb9d2d417347dbb)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[BT_ISO_BROADCAST_CODE_SIZE](../api_iso_dns_lin_topic_reference/P003_等时通道（Isochronous channels，ISO）.md#ga5551cab9896764eec39b8e6102e561e5)。

为指定接收状态（Receive State）设置广播码（Broadcast Code）。

<a id="r_ga09785690db551677a043fcaa2fdb7f29"></a>

```c
int bt_bap_broadcast_assistant_rem_src (struct bt_conn *conn, uint8_t src_id)
```

相关声明：[bt_bap_broadcast_assistant_rem_src](#ga09785690db551677a043fcaa2fdb7f29)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从服务器移除源（Source）。

<a id="r_ga94fce2b4346b1026d53e0b860ca7fbf2"></a>

```c
int bt_bap_broadcast_assistant_read_recv_state (struct bt_conn *conn, uint8_t idx)
```

相关声明：[bt_bap_broadcast_assistant_read_recv_state](#ga94fce2b4346b1026d53e0b860ca7fbf2)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从服务器读取指定接收状态（Receive State）。

## 4.7\_详细说明（Detailed Documentation）

<a id="gaf2e44d06b8b7aba57a80b1f04e65d7de"></a>

### `BT_BAP_ADV_PARAM_BROADCAST_FAST`

```c
#define BT_BAP_ADV_PARAM_BROADCAST_FAST
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV, BT_GAP_MS_TO_ADV_INTERVAL(60),                      \
                BT_GAP_MS_TO_ADV_INTERVAL(60), NULL)
```

广播音频的快速广播参数（Fast Advertising Parameters）。

适用于 7.5 ms 和 10 ms 的服务数据单元（SDU）间隔，但优先缩短同步时间，而非优先考虑与等时传输（ISO）的共存及功耗。

<a id="gaa11e0195a02baa656085f305d911042d"></a>

### `BT_BAP_ADV_PARAM_BROADCAST_SLOW`

```c
#define BT_BAP_ADV_PARAM_BROADCAST_SLOW
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV, BT_GAP_MS_TO_ADV_INTERVAL(150),                     \
                BT_GAP_MS_TO_ADV_INTERVAL(150), NULL)
```

广播音频的慢速广播参数（Slow Advertising Parameters）。

适用于 7.5 ms 和 10 ms 的服务数据单元（SDU）间隔，但优先考虑与等时传输（ISO）的共存及功耗，而非优先缩短同步时间。

<a id="gac290c620aa1861ea717dee37e1e83bfe"></a>

### `BT_BAP_ADV_PARAM_CONN_QUICK`

```c
#define BT_BAP_ADV_PARAM_CONN_QUICK
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_CONN | BT_LE_ADV_OPT_EXT_ADV, BT_GAP_MS_TO_ADV_INTERVAL(20), \
                BT_GAP_MS_TO_ADV_INTERVAL(30), NULL)
```

建议的可连接广播参数（Connectable Advertising Parameters）。

如果 30 秒后仍未建立连接，设备应切换到 `BT_BAP_ADV_PARAM_CONN_REDUCED`。

由 BAP 1.0.2 的表 8.1 定义。

<a id="gaf1883b2596f793ef24913ef7f165c5dd"></a>

### `BT_BAP_ADV_PARAM_CONN_REDUCED`

```c
#define BT_BAP_ADV_PARAM_CONN_REDUCED
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_CONN | BT_LE_ADV_OPT_EXT_ADV,                                \
                BT_GAP_MS_TO_ADV_INTERVAL(150), BT_GAP_MS_TO_ADV_INTERVAL(150), NULL)
```

缩减的可连接广播参数（Reduced Connectable Advertising Parameters）。

由 BAP 1.0.2 的表 8.1 定义。

<a id="ga443c212a736852305715452e7f165a9e"></a>

### `BT_BAP_BASS_MAX_SUBGROUPS`

```c
#define BT_BAP_BASS_MAX_SUBGROUPS COND_CODE_1(CONFIG_BT_AUDIO, (CONFIG_BT_BAP_BASS_MAX_SUBGROUPS), (0))
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

BAP 扫描委托端 API（Scan Delegator API）支持的最大子组数（Maximum Number of Subgroups）。

<a id="ga91adb24c76c0d14757c5eec0146caebb"></a>

### `BT_BAP_BASS_VALID_BIT_BITFIELD`

```c
#define BT_BAP_BASS_VALID_BIT_BITFIELD ( _bis_bitfield)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
((_bis_bitfield) == 0U || (_bis_bitfield) == BT_BAP_BIS_SYNC_NO_PREF ||                    \
 BT_ISO_VALID_BIS_BITFIELD(_bis_bitfield))
```

检查 BAP BASS 的 `BIS_Sync` 位字段（Bitfield）是否有效。

有效选项可以是有效广播等时流（BIS）索引的位掩码（Bitmask），包括不选择任何索引（`0x00000000`），也可以是 `BT_BAP_BIS_SYNC_NO_PREF`（`0xFFFFFFFF`）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_bis_bitfield` | `BIS_Sync` 位字段（Bitfield），类型为 `uint32`。 |

<a id="ga2a2e4a06f6e39360458fe2e4d0b66833"></a>

### `BT_BAP_BIS_SYNC_FAILED`

```c
#define BT_BAP_BIS_SYNC_FAILED 0xFFFFFFFFU
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

表示 BIG 同步（BIG Sync）因任意原因失败的 BIS 同步值（BIS Sync Value）。

<a id="ga799f1417272e9b545c1e30ed4616b988"></a>

### `BT_BAP_BIS_SYNC_NO_PREF`

```c
#define BT_BAP_BIS_SYNC_NO_PREF 0xFFFFFFFFU
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

广播助理（Broadcast Assistant）没有 BIS 同步偏好（BIS Sync Preference）。

此值表示广播助手（Broadcast Assistant）不限定扫描委托器（Scan Delegator）应同步到哪一条广播等时流（BIS）。

<a id="gad4a19588129f8cbf085dca166f0bc486"></a>

### `BT_BAP_CONN_PARAM_RELAXED`

```c
#define BT_BAP_CONN_PARAM_RELAXED
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
BT_LE_CONN_PARAM(BT_GAP_MS_TO_CONN_INTERVAL(50), BT_GAP_MS_TO_CONN_INTERVAL(70), 0,        \
                 BT_GAP_MS_TO_CONN_TIMEOUT(4000))
```

用于 ACL 与 ISO 共存（Coexistence）的建议连接参数（Connection Parameters）。

由 BAP 1.0.2 的表 8.4 定义。

<a id="ga0469f86dc34ab738fbbcdf45cc105194"></a>

### `BT_BAP_CONN_PARAM_SHORT_10`

```c
#define BT_BAP_CONN_PARAM_SHORT_10
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
BT_LE_CONN_PARAM(BT_GAP_MS_TO_CONN_INTERVAL(10), BT_GAP_MS_TO_CONN_INTERVAL(30), 0,        \
                 BT_GAP_MS_TO_CONN_TIMEOUT(4000))
```

适用于 10 ms 服务数据单元间隔（SDU Interval）的初始连接请求建议连接参数（Connection Parameters）。

服务发现（Service Discovery）完成并建立流（Stream）后，建议切换到 `BT_BAP_CONN_PARAM_RELAXED`。

由 BAP 1.0.2 的表 8.3 定义。

<a id="ga5d90920dfc8d554d0cd345edd0c36c66"></a>

### `BT_BAP_CONN_PARAM_SHORT_7_5`

```c
#define BT_BAP_CONN_PARAM_SHORT_7_5
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
BT_LE_CONN_PARAM(BT_GAP_US_TO_CONN_INTERVAL(7500), BT_GAP_MS_TO_CONN_INTERVAL(30), 0,      \
                 BT_GAP_MS_TO_CONN_TIMEOUT(4000))
```

适用于 7.5 ms 服务数据单元间隔（SDU Interval）的初始连接请求建议连接参数（Connection Parameters）。

服务发现（Service Discovery）完成并建立流（Stream）后，建议切换到 `BT_BAP_CONN_PARAM_RELAXED`。

由 BAP 1.0.2 的表 8.3 定义。

<a id="ga83cfb2a817e0db6d78c300dc5dea2d8a"></a>

### `BT_BAP_INVALID_BROADCAST_ID`

```c
#define BT_BAP_INVALID_BROADCAST_ID 0xFFFFFFFFU
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

无效的广播标识符（Broadcast ID）。

<a id="ga357079ef00ce6f250e72a37103926c64"></a>

### `BT_BAP_PA_INTERVAL_UNKNOWN`

```c
#define BT_BAP_PA_INTERVAL_UNKNOWN 0xFFFFU
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

表示周期广播间隔（Periodic Advertising Interval）未知的值。

<a id="ga3fb8ca6b5722cad7027553db40c4a94b"></a>

### `BT_BAP_PD_UNSET`

```c
#define BT_BAP_PD_UNSET 0xFFFFFFFFU
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

表示尚未设置呈现延迟（Presentation Delay）的值。

<a id="ga0f17a828720504892ff36447a4e3f7c3"></a>

### `BT_BAP_PER_ADV_PARAM_BROADCAST_FAST`

```c
#define BT_BAP_PER_ADV_PARAM_BROADCAST_FAST
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
BT_LE_PER_ADV_PARAM(BT_GAP_MS_TO_PER_ADV_INTERVAL(60), BT_GAP_MS_TO_PER_ADV_INTERVAL(60),  \
                    BT_LE_PER_ADV_OPT_NONE)
```

广播音频的快速广播参数（Fast Advertising Parameters）。

适用于 7.5 ms 和 10 ms 的服务数据单元（SDU）间隔，但优先缩短同步时间，而非优先考虑与等时传输（ISO）的共存及功耗。

<a id="gaf71bf639a2fca0c4d5ab61bfd6354668"></a>

### `BT_BAP_PER_ADV_PARAM_BROADCAST_SLOW`

```c
#define BT_BAP_PER_ADV_PARAM_BROADCAST_SLOW
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
BT_LE_PER_ADV_PARAM(BT_GAP_MS_TO_PER_ADV_INTERVAL(150),                                    \
                    BT_GAP_MS_TO_PER_ADV_INTERVAL(150), BT_LE_PER_ADV_OPT_NONE)
```

广播音频的慢速广播参数（Slow Advertising Parameters）。

适用于 7.5 ms 和 10 ms 的服务数据单元（SDU）间隔，但优先考虑与等时传输（ISO）的共存及功耗，而非优先缩短同步时间。

<a id="ga7bd804c68e67d0b4bfe391d80d33a6c7"></a>

### `BT_BAP_QOS_CFG`

```c
#define BT_BAP_QOS_CFG ( _interval, _framing, _phy, _sdu, _rtn, _latency, _pd )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
((struct bt_bap_qos_cfg){                                                                  \
        .interval = _interval,                                                             \
        .framing = _framing,                                                               \
        .phy = _phy,                                                                       \
        .sdu = _sdu,                                                                       \
        .rtn = _rtn,                                                                       \
        IF_ENABLED(UTIL_OR(IS_ENABLED(CONFIG_BT_BAP_BROADCAST_SOURCE),                     \
                           IS_ENABLED(CONFIG_BT_BAP_UNICAST)),                             \
                   (.latency = _latency,))                                                 \
        .pd = _pd,                                                                         \
})
```

用于声明 `bt_bap_qos_cfg` 元素（Elements）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_interval` | 服务数据单元间隔（SDU Interval），单位为微秒。 |
| `_framing` | 成帧（Framing）。 |
| `_phy` | 目标物理层（Target PHY）。 |
| `_sdu` | 最大服务数据单元大小（Maximum SDU Size）。 |
| `_rtn` | 重传次数（Retransmission Number）。 |
| `_latency` | 最大传输时延（Maximum Transport Latency），单位为毫秒。 |
| `_pd` | 呈现延迟（Presentation Delay），单位为微秒。 |

<a id="gaa91c55ca2de3ddf09620948fd4914b14"></a>

### `BT_BAP_QOS_CFG_FRAMED`

```c
#define BT_BAP_QOS_CFG_FRAMED ( _interval, _sdu, _rtn, _latency, _pd )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
BT_BAP_QOS_CFG(_interval, BT_BAP_QOS_CFG_FRAMING_FRAMED, BT_BAP_QOS_CFG_2M, _sdu, _rtn,    \
               _latency, _pd)
```

用于声明成帧输入（Input Framed）`bt_bap_qos_cfg` 的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_interval` | 服务数据单元间隔（SDU Interval），单位为微秒。 |
| `_sdu` | 最大服务数据单元大小（Maximum SDU Size）。 |
| `_rtn` | 重传次数（Retransmission Number）。 |
| `_latency` | 最大传输时延（Maximum Transport Latency），单位为毫秒。 |
| `_pd` | 呈现延迟（Presentation Delay），单位为微秒。 |

<a id="gae578c78a10df4d1e4e6d1781ca48e1f5"></a>

### `BT_BAP_QOS_CFG_UNFRAMED`

```c
#define BT_BAP_QOS_CFG_UNFRAMED ( _interval, _sdu, _rtn, _latency, _pd )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

展开值（Value）：

```c
BT_BAP_QOS_CFG(_interval, BT_BAP_QOS_CFG_FRAMING_UNFRAMED, BT_BAP_QOS_CFG_2M, _sdu, _rtn,  \
               _latency, _pd)
```

用于声明非成帧输入（Input Unframed）`bt_bap_qos_cfg` 的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_interval` | 服务数据单元间隔（SDU Interval），单位为微秒。 |
| `_sdu` | 最大服务数据单元大小（Maximum SDU Size）。 |
| `_rtn` | 重传次数（Retransmission Number）。 |
| `_latency` | 最大传输时延（Maximum Transport Latency），单位为毫秒。 |
| `_pd` | 呈现延迟（Presentation Delay），单位为微秒。 |

<a id="ga1ebca62521cf4a6973d1fa8136e54be1"></a>

### `BT_BASE_MAX_SIZE`

```c
#define BT_BASE_MAX_SIZE (UINT8_MAX - 1 /* type */ - BT_UUID_SIZE_16)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

不含服务数据头部（Service Data Header）的 BASE 最大大小。

<a id="ga496c8a2f599d997a7e6e033bda5f0c36"></a>

### `bt_bap_broadcast_assistant_write_cb`

```c
typedef void(* bt_bap_broadcast_assistant_write_cb) (struct bt_conn *conn, int err)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

写入操作的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与对端设备的连接。 |
| `err` | 错误值。成功时为 0，失败时为 GATT 错误。 |

<a id="gaf236a87ae461ad48ec59f487780b4824"></a>

### `bt_bap_scan_delegator_state_func_t`

```c
typedef bool(* bt_bap_scan_delegator_state_func_t) (const struct bt_bap_scan_delegator_recv_state *recv_state, void *user_data)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

用于扫描委托端接收状态搜索函数（Scan Delegator Receive State Search Functions）的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `recv_state` | 接收状态（Receive State）。 |
| `user_data` | 用户数据（User Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 停止迭代（Iteration）。在 `bt_bap_scan_delegator_find_state()` 上下文中使用时，`bt_bap_scan_delegator_find_state()` 将返回 `recv_state`。 |
| `false` | 继续迭代（Iteration）。 |

<a id="ga5e8ebf4db88f94f44828bb6f41e81d44"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

服务质量首选物理层（QoS Preferred PHY）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAP_QOS_CFG_1M` | LE 1M 物理层（LE 1M PHY）。 |
| `BT_BAP_QOS_CFG_2M` | LE 2M 物理层（LE 2M PHY）。 |
| `BT_BAP_QOS_CFG_CODED` | LE 编码物理层（LE Coded PHY）。 |

<a id="ga13e9b6d571a613d689b8ba58bae64ae3"></a>

### `bt_bap_bass_att_err`

```c
enum bt_bap_bass_att_err
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

广播音频扫描服务（Broadcast Audio Scan Service，BASS）特定的 ATT 错误码（Error Code）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAP_BASS_ERR_OPCODE_NOT_SUPPORTED` | 不支持该操作码（Opcode）。 |
| `BT_BAP_BASS_ERR_INVALID_SRC_ID` | 提供的源标识符（Source ID）无效。 |

<a id="ga5e0b0f70d247e131fa542fae16826a22"></a>

### `bt_bap_big_enc_state`

```c
enum bt_bap_big_enc_state
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

扫描委托端（Scan Delegator）报告的广播等时组加密状态（Broadcast Isochronous Group Encryption State）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAP_BIG_ENC_STATE_NO_ENC` | 广播等时组（Broadcast Isochronous Group）未加密。 |
| `BT_BAP_BIG_ENC_STATE_BCODE_REQ` | 已请求广播等时组（Broadcast Isochronous Group）的广播码（Broadcast Code）。 |
| `BT_BAP_BIG_ENC_STATE_DEC` | 广播等时组（Broadcast Isochronous Group）已解密。 |
| `BT_BAP_BIG_ENC_STATE_BAD_CODE` | 广播等时组（Broadcast Isochronous Group）的广播码（Broadcast Code）错误。 |

<a id="gaf210a91e1ff11d9bf7792ba47d1e1b4a"></a>

### `bt_bap_ep_state`

```c
enum bt_bap_ep_state
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

端点状态（Endpoint States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAP_EP_STATE_IDLE` | 音频流端点（Audio Stream Endpoint）的空闲状态（Idle）。 |
| `BT_BAP_EP_STATE_CODEC_CONFIGURED` | 音频流端点（Audio Stream Endpoint）的编解码器已配置状态（Codec Configured）。 |
| `BT_BAP_EP_STATE_QOS_CONFIGURED` | 音频流端点（Audio Stream Endpoint）的服务质量已配置状态（QoS Configured）。 |
| `BT_BAP_EP_STATE_ENABLING` | 音频流端点（Audio Stream Endpoint）的正在启用状态（Enabling）。 |
| `BT_BAP_EP_STATE_STREAMING` | 音频流端点（Audio Stream Endpoint）的流传输状态（Streaming）。 |
| `BT_BAP_EP_STATE_DISABLING` | 音频流端点（Audio Stream Endpoint）的正在禁用状态（Disabling）。 |
| `BT_BAP_EP_STATE_RELEASING` | 音频流端点（Audio Stream Endpoint）的正在释放状态（Releasing）。 |

<a id="gac551e9b0d53fd50f3a9e9c08447f0296"></a>

### `bt_bap_pa_state`

```c
enum bt_bap_pa_state
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

扫描委托端（Scan Delegator）报告的周期广播状态（Periodic Advertising State）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAP_PA_STATE_NOT_SYNCED` | 尚未同步到周期广播（Periodic Advertising）。 |
| `BT_BAP_PA_STATE_INFO_REQ` | 正在等待广播助手（Broadcast Assistant）提供同步信息（SyncInfo）。 |
| `BT_BAP_PA_STATE_SYNCED` | 已同步到周期广播（Periodic Advertising）。 |
| `BT_BAP_PA_STATE_FAILED` | 同步到周期广播（Periodic Advertising）失败。 |
| `BT_BAP_PA_STATE_NO_PAST` | 未从广播助手（Broadcast Assistant）接收到周期广播同步传输（Periodic Advertising Sync Transfer）。 |

<a id="ga37a5f9d7198739eef8bde6764da30de9"></a>

### `bt_bap_qos_cfg_framing`

```c
enum bt_bap_qos_cfg_framing
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

QoS 成帧方式（Framing）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAP_QOS_CFG_FRAMING_UNFRAMED` | 分组可以成帧（Framed），也可以不成帧（Unframed）。 |
| `BT_BAP_QOS_CFG_FRAMING_FRAMED` | 分组始终成帧（Framed）。 |

<a id="gac93cb4cab33d0b937e752bc0b71cad9e"></a>

### `bt_bap_broadcast_assistant_add_src()`

```c
int bt_bap_broadcast_assistant_add_src ( struct bt_conn * conn, const struct bt_bap_broadcast_assistant_add_src_param * param )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

在服务器上添加源（Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与服务器（Server）的连接。 |
| `param` | 参数结构体（Parameter Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `conn` 为 `NULL`、`conn` 尚未完成发现（Discovery），或 `param` 无效时。译注：原文的 `p conn` 按参数 `conn` 处理。 |
| `-EBUSY` | 此 conn 已有另一项操作正在进行。 |
| `-ENOTCONN` | conn 未连接。 |
| `-ENOMEM` | 无法为请求分配内存。 |
| `-ENOEXEC` | 意外的扫描（Scan）或 GATT 错误。 |

<a id="gab59c5ebc4fef28da34d8a54b1244c33b"></a>

### `bt_bap_broadcast_assistant_discover()`

```c
int bt_bap_broadcast_assistant_discover ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

发现服务器上的广播音频扫描服务（Broadcast Audio Scan Service）。

警告（Warning）：任一时刻只能有一个活动连接；为新连接执行发现（Discovery）会删除此前的全部数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | ACL 连接（ACL Connection），必须已满足基本音频配置文件（Basic Audio Profile）的安全要求。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `conn` 为 `NULL`，或不符合安全要求（Security Requirements）时。 |
| `-EBUSY` | 此 conn 已有另一项操作正在进行。 |
| `-ENOTCONN` | conn 未连接。 |
| `-ENOMEM` | 无法为请求分配内存（Allocate Memory）。 |
| `-ENOEXEC` | 非预期的 GATT 错误（Unexpected GATT Error）。 |

<a id="gaa9c292a7dcb470926d8d7d4be699a0c7"></a>

### `bt_bap_broadcast_assistant_mod_src()`

```c
int bt_bap_broadcast_assistant_mod_src ( struct bt_conn * conn, const struct bt_bap_broadcast_assistant_mod_src_param * param )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

修改服务器上的源（Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与服务器（Server）的连接。 |
| `param` | 参数结构体（Parameter Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `conn` 为 `NULL`、`conn` 尚未完成发现（Discovery），或 `param` 无效时。译注：原文的 `p conn` 按参数 `conn` 处理。 |
| `-EBUSY` | 此 conn 已有另一项操作正在进行。 |
| `-ENOTCONN` | conn 未连接。 |
| `-ENOMEM` | 无法为请求分配内存。 |
| `-ENOEXEC` | 意外的扫描（Scan）或 GATT 错误。 |

<a id="ga94fce2b4346b1026d53e0b860ca7fbf2"></a>

### `bt_bap_broadcast_assistant_read_recv_state()`

```c
int bt_bap_broadcast_assistant_read_recv_state ( struct bt_conn * conn, uint8_t idx )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

从服务器读取指定接收状态（Receive State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与服务器（Server）的连接。 |
| `idx` | 接收状态（Receive State）的索引，从 `0` 到 `bt_bap_broadcast_assistant_discover_cb` 提供的值。译注：原文写作 “receive start”，此处按上下文译为接收状态。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `conn` 为 `NULL`、`conn` 尚未完成发现（Discovery），或 `src_id` 无效时。译注：原文的 `p conn` 按参数 `conn` 处理。 |
| `-EBUSY` | 此 conn 已有另一项操作正在进行。 |
| `-ENOTCONN` | conn 未连接。 |
| `-ENOMEM` | 无法为请求分配内存。 |
| `-ENOEXEC` | 意外的扫描（Scan）或 GATT 错误。 |

<a id="gabab24c44e9833029965475ad7b149e6e"></a>

### `bt_bap_broadcast_assistant_register_cb()`

```c
int bt_bap_broadcast_assistant_register_cb ( struct bt_bap_broadcast_assistant_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注册广播音频扫描服务客户端（Broadcast Audio Scan Service Client）使用的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（callback structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `cb` 为 `NULL` 时。 |
| `-EALREADY` | `cb` 已注册（Registered）时。 |

<a id="ga09785690db551677a043fcaa2fdb7f29"></a>

### `bt_bap_broadcast_assistant_rem_src()`

```c
int bt_bap_broadcast_assistant_rem_src ( struct bt_conn * conn, uint8_t src_id )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

从服务器移除源（Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与服务器（Server）的连接。 |
| `src_id` | 接收状态的音频源 ID（Source ID）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `conn` 为 `NULL`、`conn` 尚未完成发现（Discovery），或 `src_id` 无效时。译注：原文的 `p conn` 按参数 `conn` 处理。 |
| `-EBUSY` | 此 conn 已有另一项操作正在进行。 |
| `-ENOTCONN` | conn 未连接。 |
| `-ENOMEM` | 无法为请求分配内存。 |
| `-ENOEXEC` | 意外的扫描（Scan）或 GATT 错误。 |

<a id="ga98ac067e66d263aa41fc6f8df6bb9126"></a>

### `bt_bap_broadcast_assistant_scan_start()`

```c
int bt_bap_broadcast_assistant_scan_start ( struct bt_conn * conn, bool start_scan )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

为远端服务器启动广播等时流（BIS）扫描。

此函数通知广播音频扫描服务（Broadcast Audio Scan Service）服务器：本设备正在主动扫描广播源（Broadcast Source）。如果调用者不希望自行启动扫描，也可以让此函数启动扫描。

如果 `start_scan` 为 `true`，扫描结果（Scan Results）会传递给 `bt_bap_broadcast_assistant_scan_cb` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与广播音频扫描服务（Broadcast Audio Scan Service）服务器的连接，用于通知服务器本设备正在扫描。 |
| `start_scan` | `true` 表示启动扫描（Scanning）；为 `false` 时，应用程序应自行启用扫描。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `conn` 为 `NULL`，或 `conn` 尚未完成发现（Discovery）时。 |
| `-EBUSY` | 此 conn 已有另一项操作正在进行。 |
| `-EAGAIN` | 尚未启用蓝牙（Bluetooth）。 |
| `-ENOTCONN` | conn 未连接。 |
| `-ENOMEM` | 无法为请求分配内存。 |
| `-ENOEXEC` | 意外的扫描（Scan）或 GATT 错误。 |

<a id="ga76cae35df980b78a10551811050b2760"></a>

### `bt_bap_broadcast_assistant_scan_stop()`

```c
int bt_bap_broadcast_assistant_scan_stop ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

停止针对服务器的远端广播等时流（BIS）扫描。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与服务器（Server）的连接。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `conn` 为 `NULL`，或 `conn` 尚未完成发现（Discovery）时。 |
| `-EBUSY` | 此 conn 已有另一项操作正在进行。 |
| `-EAGAIN` | 尚未启用蓝牙（Bluetooth）。 |
| `-ENOTCONN` | conn 未连接。 |
| `-ENOMEM` | 无法为请求分配内存。 |
| `-ENOEXEC` | 意外的扫描（Scan）或 GATT 错误。 |

<a id="gabcec07689c13a996bcb9d2d417347dbb"></a>

### `bt_bap_broadcast_assistant_set_broadcast_code()`

```c
int bt_bap_broadcast_assistant_set_broadcast_code ( struct bt_conn * conn, uint8_t src_id, const uint8_t broadcast_code[BT_ISO_BROADCAST_CODE_SIZE] )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

为指定接收状态（Receive State）设置广播码（Broadcast Code）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与服务器（Server）的连接。 |
| `src_id` | 接收状态的音频源 ID（Source ID）。 |
| `broadcast_code` | 广播码（Broadcast Code）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `conn` 为 `NULL`、`conn` 尚未完成发现（Discovery），或 `src_id` 无效时。译注：原文的 `p conn` 按参数 `conn` 处理。 |
| `-EBUSY` | 此 conn 已有另一项操作正在进行。 |
| `-ENOTCONN` | conn 未连接。 |
| `-ENOMEM` | 无法为请求分配内存。 |
| `-ENOEXEC` | 意外的扫描（Scan）或 GATT 错误。 |

<a id="ga679cdeb6e555bfc9ce20f38e493000ee"></a>

### `bt_bap_broadcast_assistant_unregister_cb()`

```c
int bt_bap_broadcast_assistant_unregister_cb ( struct bt_bap_broadcast_assistant_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注销广播音频扫描服务客户端（Broadcast Audio Scan Service Client）使用的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（callback structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `cb` 为 `NULL` 时。 |
| `-EALREADY` | `cb` 未注册（Registered）时。 |

<a id="ga575a109efb0fd1644634ce6e0288499b"></a>

### `bt_bap_ep_get_conn()`

```c
struct bt_conn * bt_bap_ep_get_conn ( const struct bt_bap_ep * ep)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取指向端点 ACL 连接（ACL Connection）的指针。

如果返回值不为 `NULL`，调用者会取得连接对象（Connection Object）的一个新引用；使用完毕后，必须通过 `bt_conn_unref()` 释放该引用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ep` | 要获取其异步面向连接逻辑传输（ACL）连接的端点（Endpoint）。 |

**返回（Returns）**：返回值（Returns）：ACL 连接指针。以下情况返回 `NULL`：`ep` 为 `NULL`；`ep` 是广播端点（Broadcast Endpoint）；`ep` 是尚未由远端客户端配置的单播服务器端点（Unicast Server Endpoint）；或 `ep` 是尚未在远端服务器上发现的单播客户端端点（Unicast Client Endpoint）。

<a id="gaf15e5ec5bca364f6a3e7a43b1f27da68"></a>

### `bt_bap_ep_get_info()`

```c
int bt_bap_ep_get_info ( const struct bt_bap_ep * ep, struct bt_bap_ep_info * info )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

返回包含音频流端点信息（Audio Stream Endpoint Information）的结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ep` | 音频流端点对象（Audio Stream Endpoint Object）。 |
| `info` | 要用信息填充的结构体对象（Structure Object）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | `ep` 或 `info` 为 `NULL` 时。 |

<a id="ga6eb2a782d761da12d112356cfe723ff0"></a>

### `bt_bap_scan_delegator_add_src()`

```c
int bt_bap_scan_delegator_add_src ( const struct bt_bap_scan_delegator_add_src_param * param)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

在本地添加接收状态源（Receive State Source）。

此操作会向所有已连接客户端通知新源（Source），允许客户端修改甚至删除该源。

如果启用了 `CONFIG_BT_BAP_BROADCAST_SINK`，所有广播接收端源（Broadcast Sink Sources）都会被自动添加。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 添加新源（Source）所用的参数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EAGAIN` | 尚未通过 `bt_bap_scan_delegator_register()` 注册服务（Service）。 |
| `-EINVAL` | 参数无效（Invalid Parameters）。 |
| `-ENOMEM` | 无法再添加接收状态（Receive State）。 |
| `-EALREADY` | 已存在具有相同广播者地址类型（Advertiser Address Type）、SID 和广播标识符（Broadcast ID）的接收状态（Receive State）。 |

**返回（Returns）**：返回值（Returns）：返回值大于或等于 `0` 时，为新状态的源标识符（Source ID）。

<a id="gabec9fd0a2966e1811fd4770855050510"></a>

### `bt_bap_scan_delegator_find_state()`

```c
const struct bt_bap_scan_delegator_recv_state * bt_bap_scan_delegator_find_state ( bt_bap_scan_delegator_state_func_t func, void * user_data )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

依据比较函数（Compare Function）查找并返回接收状态（Receive State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 比较回调函数（Compare Callback Function）。 |
| `user_data` | 传给回调函数的用户指定数据（User-specified Data）。 |

**返回（Returns）**：返回值（Returns）：第一个使 `func` 返回 `true` 的接收状态（Receive State），或者 `NULL`。

<a id="gab6f1a12699a9437c6575c70df33d5be0"></a>

### `bt_bap_scan_delegator_foreach_state()`

```c
void bt_bap_scan_delegator_foreach_state ( bt_bap_scan_delegator_state_func_t func, void * user_data )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

遍历全部现有接收状态（Receive State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 回调函数。 |
| `user_data` | 传给回调函数的用户指定数据（User-specified Data）。 |

<a id="gac022f38269742f16ff6887840ef5ba9a"></a>

### `bt_bap_scan_delegator_mod_src()`

```c
int bt_bap_scan_delegator_mod_src ( const struct bt_bap_scan_delegator_mod_src_param * param)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

在本地添加接收状态源（Receive State Source）。

此操作会向所有已连接客户端通知新源（Source），允许客户端修改甚至删除该源。

如果启用了 `CONFIG_BT_BAP_BROADCAST_SINK`，所有广播接收端源（Broadcast Sink Sources）都会被自动修改。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 添加新源（Source）所用的参数。 |

**返回（Returns）**：返回值（Returns）：`int` 类型；失败时为错误码（errno），成功时为源标识符（Source ID）。

<a id="ga7632ab444dbf99387871f7d0c90b11ba"></a>

### `bt_bap_scan_delegator_register()`

```c
int bt_bap_scan_delegator_register ( struct bt_bap_scan_delegator_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注册基本音频配置文件扫描委托端（Basic Audio Profile Scan Delegator）和广播音频扫描服务（BASS）。

在运行时动态注册扫描委托器（Scan Delegator）和广播音频扫描服务（Broadcast Audio Scan Service，BASS）。

任一时刻只能注册一组回调（Callbacks）；多次调用此函数会覆盖之前注册的所有回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga6c240f1cdb33945197700e4fe106ef2c"></a>

### `bt_bap_scan_delegator_rem_src()`

```c
int bt_bap_scan_delegator_rem_src ( uint8_t src_id)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

移除接收状态源（Receive State Source）。

此操作会移除接收状态（Receive State）。如果该接收状态已同步到周期广播（Periodic Advertising），将调用 `bt_bap_scan_delegator_cb.pa_sync_term_req()`。

如果启用了 `CONFIG_BT_BAP_BROADCAST_SINK`，所有广播接收端源（Broadcast Sink Sources）都会被自动移除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src_id` | 待移除的源标识符（Source ID）。 |

**返回（Returns）**：返回值（Returns）：`int` 类型错误值；成功时为 `0`，失败时为错误码（errno）。

<a id="gaf610cd6cddd52622f95cfd35b19ee841"></a>

### `bt_bap_scan_delegator_set_bis_sync_state()`

```c
int bt_bap_scan_delegator_set_bis_sync_state ( uint8_t src_id, uint32_t bis_synced[0] )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

设置服务器中某个接收状态（Receive State）的同步状态（Sync State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src_id` | 用于标识接收状态（Receive State）的源标识符（Source ID）。 |
| `bis_synced` | 位字段数组（Array of Bitfields），用于设置各子组（Subgroup）的 BIS 同步状态（Sync State）。 |

**返回（Returns）**：返回值（Returns）：`int` 类型错误值；成功时为 `0`，失败时为错误码（ERRNO）。

<a id="ga381c1f3b386ecbdfd570eb125882161e"></a>

### `bt_bap_scan_delegator_set_pa_state()`

```c
int bt_bap_scan_delegator_set_pa_state ( uint8_t src_id, enum bt_bap_pa_state pa_state )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

将周期广播同步状态（Periodic Advertising Sync State）设为正在同步（Syncing）。

将接收状态（Receive State）的周期广播同步状态（Periodic Advertising Sync State）设为正在同步（Syncing），并通知广播助手（Broadcast Assistants）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src_id` | 用于标识接收状态（Receive State）的源标识符（Source ID）。 |
| `pa_state` | 要设置的周期广播同步状态（Periodic Advertising Sync State）。 |

**返回（Returns）**：返回值（Returns）：`int` 类型错误值；成功时为 `0`，失败时为错误码（errno）。

<a id="ga6f52e58767303ded16cb6289f094895a"></a>

### `bt_bap_scan_delegator_unregister()`

```c
int bt_bap_scan_delegator_unregister ( void )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注销基本音频配置文件扫描委托端（Basic Audio Profile Scan Delegator）和广播音频扫描服务（BASS）。

在运行时动态注销扫描委托器（Scan Delegator）和广播音频扫描服务（Broadcast Audio Scan Service，BASS）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EALREADY` | 已经在注销（Unregistering）。 |
| `-EAGAIN` | 尚未注册（Not Registered）。 |

<a id="gab29c1e134156dceaa6c67abae9239378"></a>

### `bt_bap_stream_cb_register()`

```c
void bt_bap_stream_cb_register ( struct bt_bap_stream * stream, struct bt_bap_stream_ops * ops )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

为流（Stream）注册音频回调（Audio Callbacks）。

为流（Stream）注册音频回调（Audio Callbacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |
| `ops` | 流操作结构体（Stream Operations Structure）。 |

<a id="gaaecbb590e5d073829d4c150e4fd2d8aa"></a>

### `bt_bap_stream_config()`

```c
int bt_bap_stream_config ( struct bt_conn * conn, struct bt_bap_stream * stream, struct bt_bap_ep * ep, const struct bt_audio_codec_cfg * codec_cfg )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

配置音频流（Audio Stream）。

客户端（Client）使用此过程，根据远端端点（Remote Endpoint）、本地能力（Local Capability）和编解码器配置（Codec Configuration）来配置新流（Stream）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `stream` | 正在配置的流对象（Stream Object）。 |
| `ep` | 正在配置的远端音频端点（Remote Audio Endpoint）。 |
| `codec_cfg` | 编解码器配置（Codec Configuration）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaa75f2cd2c36fdaef04a62c95bec6e2e3"></a>

### `bt_bap_stream_connect()`

```c
int bt_bap_stream_connect ( struct bt_bap_stream * stream)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

连接单播音频流（Unicast Audio Stream）。

单播客户端（Unicast Client）使用此过程，连接与音频流关联的连接等时流（Connected Isochronous Stream，CIS）。如果两个音频流共享一条 CIS，只需为这两个流执行一次。仅可对处于服务质量已配置（QoS Configured）或已启用（Enabled）状态的流执行此操作。

此过程完成后，将对相应流调用 `bt_bap_stream_ops.connected()` 回调。

只能对单播流（Unicast Stream）调用，且调用方只能是单播客户端（`CONFIG_BT_BAP_UNICAST_CLIENT`）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 流（Stream）、端点（Endpoint）、ISO 通道或连接为 `NULL` 时。 |
| `-EBADMSG` | 流（Stream）或 ISO 通道的状态不允许连接时。 |
| `-EOPNOTSUPP` | 流（Stream）的角色不是 `BT_CONN_ROLE_CENTRAL` 时。 |
| `-EALREADY` | ISO 通道已经在连接或已经连接时。 |
| `-EBUSY` | 另一个 ISO 通道正在连接时。 |
| `-ENOEXEC` | 因其他原因被等时传输层（ISO Layer）拒绝时。 |

<a id="ga0fd2bb35909fc19e3e9cff068ba9e9aa"></a>

### `bt_bap_stream_disable()`

```c
int bt_bap_stream_disable ( struct bt_bap_stream * stream)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

禁用音频流（Audio Stream）。

单播客户端（Unicast Client）或单播服务器（Unicast Server）使用此过程禁用流（Stream）。

只能对单播流（Unicast Stream）调用，因为广播流（Broadcast Stream）一经创建就始终处于启用状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga13a859b31b0310ec22339ec7ed0754f8"></a>

### `bt_bap_stream_enable()`

```c
int bt_bap_stream_enable ( struct bt_bap_stream * stream, const uint8_t meta[], size_t meta_len )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

启用音频流（Audio Stream）。

客户端（Client）使用此过程启用流（Stream）。

只能对单播流（Unicast Stream）调用，因为广播流（Broadcast Stream）一经创建就始终处于启用状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |
| `meta` | 元数据（Metadata）。 |
| `meta_len` | 元数据长度（Metadata Length）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga47eb6219d730d75ddc4f49dceac7e928"></a>

### `bt_bap_stream_get_tx_sync()`

```c
int bt_bap_stream_get_tx_sync ( struct bt_bap_stream * stream, struct bt_iso_tx_info * info )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取基本音频配置文件流（Basic Audio Profile Stream）的等时传输时序信息（ISO Transmission Timing Info）。

读取 ISO 信道（ISO Channel）上已发送 ISO 数据包的时序信息（Timing Information）。通过 HCI_LE_Read_ISO_TX_Sync HCI 命令从控制器获取此信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 流对象（Stream Object）。 |
| `[out] info` | 发送信息对象（Transmit Info Object）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 流（Stream）无效、未配置为发送，或未与等时流（Isochronous Stream）连接时。 |
| `Any` | `bt_iso_chan_get_tx_sync()` 的返回值。 |

**说明（Note）**：注意（Note）：要使此函数成功返回，必须已经在该 ISO 通道上成功发送过一个服务数据单元（SDU）。还必须支持发送功能，该支持由 `CONFIG_BT_AUDIO_TX` 决定。

<a id="ga0afe6c927729697e2f984cefcbc7c0f1"></a>

### `bt_bap_stream_metadata()`

```c
int bt_bap_stream_metadata ( struct bt_bap_stream * stream, const uint8_t meta[], size_t meta_len )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

更改音频流元数据（Audio Stream Metadata）。

单播客户端（Unicast Client）或单播服务器（Unicast Server）使用此过程修改流（Stream）的元数据（Metadata）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |
| `meta` | 元数据（Metadata）。 |
| `meta_len` | 元数据长度（Metadata Length）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gac878ed89242cac9a8514e8e4f1da4d9d"></a>

### `bt_bap_stream_qos()`

```c
int bt_bap_stream_qos ( struct bt_conn * conn, struct bt_bap_unicast_group * group )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

配置音频流服务质量（Audio Stream QoS）。

客户端（Client）使用此过程配置单播组（Unicast Group）内流的服务质量（Quality of Service）。组内属于指定 `conn` 的所有流都会被配置服务质量。此过程只能用于配置单播流。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `group` | 单播组对象（Unicast Group Object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaa7df3f6b906241ad5291295a6ddcf1e4"></a>

### `bt_bap_stream_reconfig()`

```c
int bt_bap_stream_reconfig ( struct bt_bap_stream * stream, const struct bt_audio_codec_cfg * codec_cfg )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

重新配置音频流（Audio Stream）。

单播客户端（Unicast Client）或单播服务器（Unicast Server）使用此过程重新配置流（Stream），使其采用不同的本地编解码器配置（Local Codec Configuration）。

仅可对单播流（Unicast Stream）执行此操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 正在重新配置的流对象。 |
| `codec_cfg` | 编解码器配置（Codec Configuration）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaaf94f1f0dda7ef356c0f9ae79b5c60e4"></a>

### `bt_bap_stream_release()`

```c
int bt_bap_stream_release ( struct bt_bap_stream * stream)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

释放音频流（Audio Stream）。

单播客户端（Unicast Client）或单播服务器（Unicast Server）使用此过程释放单播流（Unicast Stream）。

广播接收端流（Broadcast Sink Stream）不能被释放，但可以通过 `bt_bap_broadcast_sink_delete()` 删除。广播源流（Broadcast Source Stream）不能被释放，但可以通过 `bt_bap_broadcast_source_delete()` 删除。

如果流的端点（Endpoint）不为 `NULL`，且状态为 `BT_BAP_EP_STATE_IDLE`，则此函数在返回 `0` 时会在本地重置流和端点，但不会发送释放命令（Release Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga63b69967aa92224a2bd9cf79eb41773e"></a>

### `bt_bap_stream_send()`

```c
int bt_bap_stream_send ( struct bt_bap_stream * stream, struct net_buf * buf, uint16_t seq_num )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

向音频流（Audio Stream）发送不带时间戳（Timestamp）的数据。

将缓冲区（Buffer）中的数据发送到流（Stream）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |
| `buf` | 包含待发送数据的缓冲区。 |
| `seq_num` | 分组序列号（Packet Sequence Number）。对此函数的每次调用都必须递增该值；对于特定通道，每个 SDU 间隔内至少递增一次。 |

**说明（Note）**：注（Note）：必须支持发送，该能力由 `CONFIG_BT_AUDIO_TX` 决定。

**返回（Returns）**：返回值（Returns）：成功返回已发送字节数，错误返回负值。

<a id="gaa0e012446238c916abc84d6c0de89bf3"></a>

### `bt_bap_stream_send_ts()`

```c
int bt_bap_stream_send_ts ( struct bt_bap_stream * stream, struct net_buf * buf, uint16_t seq_num, uint32_t ts )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

向音频流（Audio Stream）发送带时间戳（Timestamp）的数据。

将缓冲区（Buffer）中的数据发送到流（Stream）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |
| `buf` | 包含待发送数据的缓冲区。 |
| `seq_num` | 分组序列号（Packet Sequence Number）。对此函数的每次调用都必须递增该值；对于特定通道，每个 SDU 间隔内至少递增一次。 |
| `ts` | 服务数据单元（SDU）的时间戳，单位为微秒（µs）。可使用此值，在连接等时组（CIG）或广播等时组（BIG）的同一个 SDU 间隔内发送多个 SDU。 |

**说明（Note）**：注（Note）：必须支持发送，该能力由 `CONFIG_BT_AUDIO_TX` 决定。

**返回（Returns）**：返回值（Returns）：成功返回已发送字节数，错误返回负值。

<a id="ga8f2dc67c35299334d21c7dee7b8664ae"></a>

### `bt_bap_stream_start()`

```c
int bt_bap_stream_start ( struct bt_bap_stream * stream)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

启动音频流（Audio Stream）。

单播客户端（Unicast Client）或单播服务器（Unicast Server）使用此过程，使流（Stream）开始流传输（Streaming）。

对于单播客户端（Unicast Client），此过程会针对 `BT_AUDIO_DIR_SOURCE` 音频流端点（ASE），向单播服务器发送接收方启动就绪命令（Receiver Start Ready）。发送命令前，必须先通过 `bt_bap_stream_connect()` 连接 CIS。

对于单播服务器（Unicast Server），此过程会针对 `BT_AUDIO_DIR_SINK` 音频流端点（ASE），在单播服务器上执行接收方启动就绪命令（Receiver Start Ready）。如果 CIS 尚未连接，则 CIS 一旦连接，流就会进入流传输状态（Streaming）。

只能对单播流（Unicast Stream）调用。

广播接收端（Broadcast Sink）一旦同步就始终启动；广播源流（Broadcast Source Stream）应通过 `bt_bap_broadcast_source_start()` 启动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gada72bcd3951eff2bc6b70c02dcaed98b"></a>

### `bt_bap_stream_stop()`

```c
int bt_bap_stream_stop ( struct bt_bap_stream * stream)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

停止音频流（Audio Stream）。

客户端（Client）使用此过程，使流（Stream）停止流传输（Streaming）。

只能对单播流（Unicast Stream）调用。广播接收端（Broadcast Sink）不能停止；广播源（Broadcast Source）应通过 `bt_bap_broadcast_source_stop()` 停止。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 流对象（Stream Object）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 流（Stream）没有端点或连接，或者流所用连接的角色不是 `BT_CONN_ROLE_CENTRAL`。 |
| `-EBADMSG` | 流端点（Stream Endpoint）的状态不是 `BT_BAP_EP_STATE_DISABLING`。 |
| `-EALREADY` | CIS 状态不是已连接（Connected），因此已经在停止。 |
| `-EBUSY` | 流（Stream）正在忙于其他操作。 |
| `-ENOTCONN` | 流（Stream）的 ACL 连接未连接。 |
| `-ENOMEM` | 没有可用于发送请求（Request）的内存。 |
| `-ENOEXEC` | 请求（Request）被 GATT 拒绝。 |

**返回（Returns）**：成功返回 0，出错时返回负值。


## 4.8\_原页交叉引用（Cross References）

- [BAP 广播 API（Broadcast APIs）](../api_memory_network_topic_reference/P003_BAP 广播 API（Broadcast APIs）.md)
- [BAP 广播接收端 API（Broadcast Sink APIs）](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md)
- [BAP 广播源 API（Broadcast Source APIs）](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md)
- [BAP 单播客户端 API（Unicast Client APIs）](../api_memory_timer_topic_reference/P002_BAP 单播客户端 API（Unicast Client APIs）.md)
- [BAP 单播服务器 API（Unicast Server APIs）](../api_video_event_topic_reference/P002_BAP 单播服务器 API（Unicast Server APIs）.md)
- [bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)
- [bt_bap_bass_subgroup](../bluetooth_le_audio_model_reference/P013_bt_bap_bass_subgroup_结构体.md)
- [bt_bap_scan_delegator_recv_state](../bluetooth_le_audio_model_reference/P032_bt_bap_scan_delegator_recv_state_结构体.md)
- [bt_bap_scan_delegator_cb](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md)
- [bt_bap_ep_info](../bluetooth_le_audio_model_reference/P025_bt_bap_ep_info_结构体.md)
- [bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)
- [bt_bap_stream_ops](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md)
- [bt_bap_unicast_server_register_param](../bluetooth_le_audio_model_reference/P042_bt_bap_unicast_server_register_param_结构体.md)
- [bt_bap_scan_delegator_add_src_param](../bluetooth_le_audio_model_reference/P029_bt_bap_scan_delegator_add_src_param_结构体.md)
- [bt_bap_scan_delegator_mod_src_param](../bluetooth_le_audio_model_reference/P031_bt_bap_scan_delegator_mod_src_param_结构体.md)
- [bt_bap_broadcast_assistant_cb](../bluetooth_le_audio_model_reference/P015_bt_bap_broadcast_assistant_cb_结构体.md)
- [bt_bap_broadcast_assistant_add_src_param](../bluetooth_le_audio_model_reference/P014_bt_bap_broadcast_assistant_add_src_param_结构体.md)
- [bt_bap_broadcast_assistant_mod_src_param](../bluetooth_le_audio_model_reference/P016_bt_bap_broadcast_assistant_mod_src_param_结构体.md)
- [bt_bap_broadcast_source](../bluetooth_le_audio_model_reference/P019_bt_bap_broadcast_source_结构体.md)
- [bt_bap_broadcast_sink](../bluetooth_le_audio_model_reference/P017_bt_bap_broadcast_sink_结构体.md)
- [bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)
- [bt_bap_ep](../bluetooth_le_audio_model_reference/P024_bt_bap_ep_结构体.md)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [UINT8_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#aeb4e270a084ee26fe73e799861bd0252)
- [BT_UUID_SIZE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d3506fd135b5cd8763446f572c161da)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)
- [BT_ISO_BROADCAST_CODE_SIZE](../api_iso_dns_lin_topic_reference/P003_等时通道（Isochronous channels，ISO）.md#ga5551cab9896764eec39b8e6102e561e5)
- [zephyr/bluetooth/audio/bap.h](../api_file_media_sensor_reference/P001_zephyr__bluetooth__audio__bap.h_文件参考.md)
- [BT_LE_ADV_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9557269dd36b624b49e76c511c3a0cc1)
- [BT_LE_ADV_OPT_EXT_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab)
- [BT_GAP_MS_TO_ADV_INTERVAL](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#gaef9c34f229f1b8b06d3e6cd44a1014ef)
- [BT_LE_ADV_OPT_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169)
- [BT_LE_CONN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga940d55c0d84c0cb8f09bc41074ae50d0)
- [BT_GAP_MS_TO_CONN_INTERVAL](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga75985e2c444da7b2426cc746c9781c8c)
- [BT_GAP_MS_TO_CONN_TIMEOUT](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga24f79cacceeea262987f3cdaf2ef6bc3)
- [BT_GAP_US_TO_CONN_INTERVAL](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#gab12ba919a5a389b4c342d142d3a9ce6e)
- [BT_LE_PER_ADV_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf46e54f8fcda7b65b659685bb225d243)
- [BT_GAP_MS_TO_PER_ADV_INTERVAL](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga15ec0bc7c9bab797d6c5595269a33ea4)
- [BT_LE_PER_ADV_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggae60a45dde6b4d9f4c54a2a6070254f11aa2c689d726eacfb18d87655b1f587518)
- [UTIL_OR](../util_reference/P001_通用工具公共接口.md#ga50cfdf948906976562c3f0625c84c2b2)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [bt_conn_unref()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b18c6b22a9f02be0d7d078b2ce51ff6)
- [CONFIG_BT_BAP_BROADCAST_SINK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_BROADCAST_SINK)
- [bt_bap_scan_delegator_cb.pa_sync_term_req()](../bluetooth_le_audio_model_reference/P030_bt_bap_scan_delegator_cb_结构体.md#a5b918538cfe0edaa69155f891981eeae)
- [bt_bap_stream_ops.connected()](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a533d5ea96aa67b9b74b19c55afd43df1)
- [CONFIG_BT_BAP_UNICAST_CLIENT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_UNICAST_CLIENT)
- [BT_CONN_ROLE_CENTRAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30)
- [CONFIG_BT_AUDIO_TX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUDIO_TX)
- [bt_iso_chan_get_tx_sync()](../api_iso_dns_lin_topic_reference/P003_等时通道（Isochronous channels，ISO）.md#gaa3942147fdeebc36039cc35c4e984411)
- [bt_bap_broadcast_sink_delete()](../api_audio_path_topic_reference/P002_BAP 广播接收端 API（Broadcast Sink APIs）.md#ga8b9d6cb409a3671654e053475ada3fda)
- [bt_bap_broadcast_source_delete()](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#ga12e0a4856115a8eb297fe2d1fc130155)
- [BT_AUDIO_DIR_SOURCE](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c)
- [BT_AUDIO_DIR_SINK](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8)
- [bt_bap_broadcast_source_start()](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#gac4640f5207599d51c1a63ff47f3c1d5a)
- [bt_bap_broadcast_source_stop()](../api_memory_network_topic_reference/P004_BAP 广播源 API（Broadcast Source APIs）.md#ga36a885581eec5cab8b3f652db19b9aba)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__gap__defines_html_gaef9c34f229f1b8b06d3e6cd44a1014ef"></a>
<a id="agroup__bt__gap_html_ga9557269dd36b624b49e76c511c3a0cc1"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169"></a>
<a id="agroup__bt__bap_html_ga799f1417272e9b545c1e30ed4616b988"></a>
<a id="agroup__bt__conn_html_ga940d55c0d84c0cb8f09bc41074ae50d0"></a>
<a id="agroup__bt__gap__defines_html_ga24f79cacceeea262987f3cdaf2ef6bc3"></a>
<a id="agroup__bt__gap__defines_html_ga75985e2c444da7b2426cc746c9781c8c"></a>
<a id="agroup__bt__gap__defines_html_gab12ba919a5a389b4c342d142d3a9ce6e"></a>
<a id="agroup__bt__gap__defines_html_ga15ec0bc7c9bab797d6c5595269a33ea4"></a>
<a id="agroup__bt__gap_html_gaf46e54f8fcda7b65b659685bb225d243"></a>
<a id="agroup__bt__gap_html_ggae60a45dde6b4d9f4c54a2a6070254f11aa2c689d726eacfb18d87655b1f587518"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="agroup__sys-util_html_ga50cfdf948906976562c3f0625c84c2b2"></a>
<a id="astructbt__bap__qos__cfg_html"></a>
<a id="agroup__bt__bap_html_ga7bd804c68e67d0b4bfe391d80d33a6c7"></a>
<a id="agroup__bt__bap_html_gga37a5f9d7198739eef8bde6764da30de9a406ad3527d9d92e4e8b213fe52794298"></a>
<a id="agroup__bt__bap_html_gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147"></a>
<a id="agroup__bt__bap_html_gga37a5f9d7198739eef8bde6764da30de9afe1ffd5db8e36f8082a2ef7545e04a94"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga5e8ebf4db88f94f44828bb6f41e81d44af5bc162fe51c445cb3c77bcf640bbe28"></a>
<a id="gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147"></a>
<a id="gga5e8ebf4db88f94f44828bb6f41e81d44ab41e06fe31c57bb7dac5a77acb53be73"></a>
<a id="gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c"></a>
<a id="gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202"></a>
<a id="gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4"></a>
<a id="gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2"></a>
<a id="gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10"></a>
<a id="gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b"></a>
<a id="ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961"></a>
<a id="ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688"></a>
<a id="ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523"></a>
<a id="ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332"></a>
<a id="ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710"></a>
<a id="ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8"></a>
<a id="ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c"></a>
<a id="ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf"></a>
<a id="ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb"></a>
<a id="ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc"></a>
<a id="ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647"></a>
<a id="ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d"></a>
<a id="gga37a5f9d7198739eef8bde6764da30de9afe1ffd5db8e36f8082a2ef7545e04a94"></a>
<a id="gga37a5f9d7198739eef8bde6764da30de9a406ad3527d9d92e4e8b213fe52794298"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_分配编号（Assigned Numbers）.md) · [返回大纲](大纲.md) · [下一章](P005_GATT 客户端 API.md)
