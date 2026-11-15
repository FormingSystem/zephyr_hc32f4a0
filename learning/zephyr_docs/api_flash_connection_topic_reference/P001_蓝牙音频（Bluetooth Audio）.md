---
id: learning.zephyr-docs.api-flash-connection-topic-reference.page-1
title: 蓝牙音频（Bluetooth Audio）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_蓝牙音频（Bluetooth Audio）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙音频（Bluetooth Audio）

<a id="details"></a>

蓝牙音频（Bluetooth Audio）。起始版本（Since）：3.1。接口版本（Version）：0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_bt_5Faudio_5Fto_5Fstr"></a>

相关声明：[分配编号转字符串 API（Assigned numbers to string API）](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md)。

分配编号转字符串 API（Assigned numbers to string API）

<a id="r_bt_5Faudio_5Fcodec_5Fcap"></a>

相关声明：[编解码器能力解析 API（Codec capability parsing APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html)。

音频编解码器能力 API（Audio codec capabilities APIs）

<a id="r_bt_5Faudio_5Fcodec_5Fcfg"></a>

相关声明：[编解码器配置解析 API（Codec config parsing APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html)。

音频编解码器配置 API（Audio codec Config APIs）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.2\_数据结构（Data Structures）

<a id="r_bt_5Faudio_5Fcodec_5Foctets_5Fper_5Fcodec_5Fframe"></a>

```c
struct bt_audio_codec_octets_per_codec_frame
```

相关声明：[bt_audio_codec_octets_per_codec_frame](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md)。

保存所支持编解码器帧大小的最小值和最大值的结构体。

```c
struct bt_audio_codec_cap
```

相关声明：[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

编解码器能力结构体（Codec Capability Structure）。

```c
struct bt_audio_codec_cfg
```

相关声明：[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

编解码器专用配置结构体（Codec Specific Configuration Structure）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.3\_宏定义（Macros）

<a id="r_ga18dd9f4a4af7716dd01497309ff9c87c"></a>

```c
#define BT_AUDIO_BROADCAST_ID_SIZE 3U
```

相关声明：[BT_AUDIO_BROADCAST_ID_SIZE](#ga18dd9f4a4af7716dd01497309ff9c87c)。

广播标识符（Broadcast ID）的大小，以八位字节（Octet）为单位。

<a id="r_ga3ed5ba09ab4c1ab7a59f8a1b4deee791"></a>

```c
#define BT_AUDIO_BROADCAST_ID_MAX 0xFFFFFFU
```

相关声明：[BT_AUDIO_BROADCAST_ID_MAX](#ga3ed5ba09ab4c1ab7a59f8a1b4deee791)。

广播标识符（Broadcast ID）的最大值。

<a id="r_ga663ab7bf74d56f36ee6cc80b369cbc16"></a>

```c
#define BT_AUDIO_PD_PREF_NONE 0x000000U
```

相关声明：[BT_AUDIO_PD_PREF_NONE](#ga663ab7bf74d56f36ee6cc80b369cbc16)。

表示服务器对呈现延迟（Presentation Delay）没有偏好。

<a id="r_gaaa0414a4baef5a867fd1c6b1865d2dbc"></a>

```c
#define BT_AUDIO_PD_MAX 0xFFFFFFU
```

相关声明：[BT_AUDIO_PD_MAX](#gaaa0414a4baef5a867fd1c6b1865d2dbc)。

最大呈现延迟（Maximum Presentation Delay），以微秒为单位。

<a id="r_ga4a5fd440b96f4e4acbb791badef8c255"></a>

```c
#define BT_AUDIO_RTN_PREF_NONE 0xFFU
```

相关声明：[BT_AUDIO_RTN_PREF_NONE](#ga4a5fd440b96f4e4acbb791badef8c255)。

表示单播服务器（Unicast Server）对重传次数（Retransmission Number）没有偏好。

<a id="r_gab6e5f793d514626deca21940d35d8f21"></a>

```c
#define BT_AUDIO_LANG_SIZE 3U
```

相关声明：[BT_AUDIO_LANG_SIZE](#gab6e5f793d514626deca21940d35d8f21)。

流语言值（Stream Language Value）的大小，例如：

<a id="r_ga8f835266fabd6461216fe13e1b3b3a0f"></a>

```c
#define BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT(...)
```

相关声明：[BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT](#ga8f835266fabd6461216fe13e1b3b3a0f)。

声道数支持能力（Channel Count Support Capability）。

<a id="r_ga86a7e9ca661a3b13b7c59d41d206156e"></a>

```c
#define BT_AUDIO_METADATA_TYPE_IS_KNOWN(_type)
```

相关声明：[BT_AUDIO_METADATA_TYPE_IS_KNOWN](#ga86a7e9ca661a3b13b7c59d41d206156e)。

用于检查元数据类型（Metadata Type）是否为协议栈已知类型的辅助宏。

<a id="r_gaddc49e39465798ae4c0cbe345e0b50d7"></a>

```c
#define BT_AUDIO_CODEC_DATA(_type, _bytes...)
```

相关声明：[BT_AUDIO_CODEC_DATA](#gaddc49e39465798ae4c0cbe345e0b50d7)。

用于声明 `bt_audio_codec_cap` 数组元素的辅助宏。

<a id="r_gaefed7a013e282c63c9b5cbbdcdc67448"></a>

```c
#define BT_AUDIO_CODEC_CFG(_id, _cid, _vid, _data, _meta)
```

相关声明：[BT_AUDIO_CODEC_CFG](#gaefed7a013e282c63c9b5cbbdcdc67448)。

用于声明编解码器配置解析 API（Codec Config Parsing APIs）的辅助宏。

<a id="r_ga6b99f589f6cdcd9e48a83f729a7a4698"></a>

```c
#define BT_AUDIO_CODEC_CAP(_id, _cid, _vid, _data, _meta)
```

相关声明：[BT_AUDIO_CODEC_CAP](#ga6b99f589f6cdcd9e48a83f729a7a4698)。

用于声明编解码器能力解析 API 结构体（Codec Capability Parsing APIs Structure）的辅助宏。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_ga62108a3dcc3e35f7b31a99f7a33679e6"></a>

```c
enum bt_audio_codec_cfg_target_latency { BT_AUDIO_CODEC_CFG_TARGET_LATENCY_LOW = 0x01 , BT_AUDIO_CODEC_CFG_TARGET_LATENCY_BALANCED = 0x02 , BT_AUDIO_CODEC_CFG_TARGET_LATENCY_HIGH = 0x03 }
```

相关声明：[bt_audio_codec_cfg_target_latency](#ga62108a3dcc3e35f7b31a99f7a33679e6)、[BT_AUDIO_CODEC_CFG_TARGET_LATENCY_LOW](#gga62108a3dcc3e35f7b31a99f7a33679e6aec4cf0f851e64e034ead8a075c93eda8)、[BT_AUDIO_CODEC_CFG_TARGET_LATENCY_BALANCED](#gga62108a3dcc3e35f7b31a99f7a33679e6a971aeaf3e2df14f5ed75965a31188f80)、[BT_AUDIO_CODEC_CFG_TARGET_LATENCY_HIGH](#gga62108a3dcc3e35f7b31a99f7a33679e6a93ec0567d248d4cfc9cd60c26cbc50ef)。

编解码器配置目标延迟（Codec Configuration Target Latency）。

<a id="r_ga640af4e254e73f5c4646e9be4e99f3d1"></a>

```c
enum bt_audio_codec_cfg_target_phy { BT_AUDIO_CODEC_CFG_TARGET_PHY_1M = 0x01 , BT_AUDIO_CODEC_CFG_TARGET_PHY_2M = 0x02 , BT_AUDIO_CODEC_CFG_TARGET_PHY_CODED = 0x03 }
```

相关声明：[bt_audio_codec_cfg_target_phy](#ga640af4e254e73f5c4646e9be4e99f3d1)、[BT_AUDIO_CODEC_CFG_TARGET_PHY_1M](#gga640af4e254e73f5c4646e9be4e99f3d1acd5c965423632650196768589a75bd95)、[BT_AUDIO_CODEC_CFG_TARGET_PHY_2M](#gga640af4e254e73f5c4646e9be4e99f3d1a0b7e1713ff85524953baeb4e7e085d96)、[BT_AUDIO_CODEC_CFG_TARGET_PHY_CODED](#gga640af4e254e73f5c4646e9be4e99f3d1a3793a0bbbb7daa399086ce7db0a24a38)。

编解码器配置目标物理层（Codec Configuration Target PHY）。

<a id="r_ga5bd899fb5e4d844058184913866e462f"></a>

```c
enum bt_audio_dir { BT_AUDIO_DIR_SINK = 0x01 , BT_AUDIO_DIR_SOURCE = 0x02 }
```

相关声明：[bt_audio_dir](#ga5bd899fb5e4d844058184913866e462f)、[BT_AUDIO_DIR_SINK](#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8)、[BT_AUDIO_DIR_SOURCE](#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c)。

从 BAP 单播服务器（Unicast Server）／BAP 广播接收端（Broadcast Sink）的视角定义的音频方向（Audio Direction）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_gafd8574b16141162c95653f0aa2bf6ff7"></a>

```c
int bt_audio_data_parse (const uint8_t ltv[], size_t size, bool(*func)(struct bt_data *data, void *user_data), void *user_data)
```

相关声明：[bt_audio_data_parse](#gafd8574b16141162c95653f0aa2bf6ff7)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

用于解析长度—类型—值数据（Length-Type-Value Data，LTV）的辅助函数。

<a id="r_gabbd1b9c46caa9a19de6c95b08c31e5b5"></a>

```c
int bt_audio_data_get_val (const uint8_t ltv_data[], size_t size, uint8_t type, const uint8_t **data)
```

相关声明：[bt_audio_data_get_val](#gabbd1b9c46caa9a19de6c95b08c31e5b5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从长度—类型—值数据数组（LTV Data Array）中获取特定数据类型的值。

<a id="r_ga87415f8dddd38b3f5641c96e9722a44a"></a>

```c
uint8_t bt_audio_get_chan_count (enum bt_audio_location chan_allocation)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_audio_get_chan_count](#ga87415f8dddd38b3f5641c96e9722a44a)、[bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)。

根据声道分配（Channel Allocation）获取声道数（Number of Channels）的函数。

<a id="r_gaf629628fc13be7a1693ceb1d32b743f2"></a>

```c
static const char * bt_audio_dir_to_str (enum bt_audio_dir dir)
```

相关声明：[bt_audio_dir_to_str](#gaf629628fc13be7a1693ceb1d32b743f2)、[bt_audio_dir](#ga5bd899fb5e4d844058184913866e462f)。

返回特定 `bt_audio_dir` 方向（Direction）的字符串表示。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.6\_单播公告类型（Unicast Announcement Type）

<a id="r_ga41db714fa87e85896a52427399633bb4"></a>

```c
#define BT_AUDIO_UNICAST_ANNOUNCEMENT_GENERAL 0x00U
```

相关声明：[BT_AUDIO_UNICAST_ANNOUNCEMENT_GENERAL](#ga41db714fa87e85896a52427399633bb4)。

单播服务器（Unicast Server）可连接，且未请求连接。

<a id="r_ga56c14acb7f182a413fdecac4e271c5cc"></a>

```c
#define BT_AUDIO_UNICAST_ANNOUNCEMENT_TARGETED 0x01U
```

相关声明：[BT_AUDIO_UNICAST_ANNOUNCEMENT_TARGETED](#ga56c14acb7f182a413fdecac4e271c5cc)。

单播服务器（Unicast Server）可连接，但正在请求连接。

## 1.7\_详细说明（Detailed Documentation）

<a id="ga3ed5ba09ab4c1ab7a59f8a1b4deee791"></a>

### `BT_AUDIO_BROADCAST_ID_MAX`

```c
#define BT_AUDIO_BROADCAST_ID_MAX 0xFFFFFFU
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

广播标识符（Broadcast ID）的最大值。

<a id="ga18dd9f4a4af7716dd01497309ff9c87c"></a>

### `BT_AUDIO_BROADCAST_ID_SIZE`

```c
#define BT_AUDIO_BROADCAST_ID_SIZE 3U
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

广播标识符（Broadcast ID）的大小，以八位字节（Octet）为单位。

<a id="ga6b99f589f6cdcd9e48a83f729a7a4698"></a>

### `BT_AUDIO_CODEC_CAP`

```c
#define BT_AUDIO_CODEC_CAP ( _id, _cid, _vid, _data, _meta )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

展开值（Value）：

```c
((struct bt_audio_codec_cap){                                                              \
        /* Use HCI data path as default, can be overwritten by application */              \
        .path_id = BT_ISO_DATA_PATH_HCI,                                                   \
        .ctlr_transcode = false,                                                           \
        .id = (_id),                                                                       \
        .cid = (_cid),                                                                     \
        .vid = (_vid),                                                                     \
        .data_len = sizeof((uint8_t[])_data),                                              \
        .data = _data,                                                                     \
        .meta_len = sizeof((uint8_t[])_meta),                                              \
        .meta = _meta,                                                                     \
})
```

用于声明编解码器能力解析 API 结构体（Codec Capability Parsing APIs Structure）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_id` | 编解码器 ID（Codec ID）。 |
| `_cid` | 公司标识符（Company ID）。 |
| `_vid` | 厂商标识符（Vendor ID）。 |
| `_data` | 采用 LVT 格式的编解码器特定数据（Codec Specific Data，原文写作 LVT）。 |
| `_meta` | 采用 LVT 格式的编解码器特定元数据（Codec Specific Metadata，原文写作 LVT）。 |

<a id="ga8f835266fabd6461216fe13e1b3b3a0f"></a>

### `BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT`

```c
#define BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT ( ...)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

展开值（Value）：

```c
((enum bt_audio_codec_cap_chan_count)((FOR_EACH(BIT, (|), __VA_ARGS__)) >> 1))
```

声道数支持能力（Channel Count Support Capability）。

本宏接受数量可变的声道数（Channel Count）参数。允许的声道数由规范定义，必须位于 `BT_AUDIO_CODEC_CAP_CHAN_COUNT_MIN` 至 `BT_AUDIO_CODEC_CAP_CHAN_COUNT_MAX` 的闭区间内。

支持 1 声道和 3 声道的示例（Example）：`BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT(1, 3)`。

<a id="gaefed7a013e282c63c9b5cbbdcdc67448"></a>

### `BT_AUDIO_CODEC_CFG`

```c
#define BT_AUDIO_CODEC_CFG ( _id, _cid, _vid, _data, _meta )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

展开值（Value）：

```c
((struct bt_audio_codec_cfg){                                                              \
        /* Use HCI data path as default, can be overwritten by application */              \
        .path_id = BT_ISO_DATA_PATH_HCI,                                                   \
        .ctlr_transcode = false,                                                           \
        COND_CODE_1(IS_ENABLED(CONFIG_BT_BAP_UNICAST),                                     \
                    (.target_latency = BT_AUDIO_CODEC_CFG_TARGET_LATENCY_BALANCED,         \
                     .target_phy = BT_AUDIO_CODEC_CFG_TARGET_PHY_2M,),                     \
                    ())                                                                    \
        .id = _id,                                                                         \
        .cid = _cid,                                                                       \
        .vid = _vid,                                                                       \
        .data_len = sizeof((uint8_t[])_data),                                              \
        .data = _data,                                                                     \
        .meta_len = sizeof((uint8_t[])_meta),                                              \
        .meta = _meta,                                                                     \
})
```

用于声明编解码器配置解析 API（Codec Config Parsing APIs）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_id` | 编解码器 ID（Codec ID）。 |
| `_cid` | 公司标识符（Company ID）。 |
| `_vid` | 厂商标识符（Vendor ID）。 |
| `_data` | 采用 LVT 格式的编解码器特定数据（Codec Specific Data，原文写作 LVT）。 |
| `_meta` | 采用 LVT 格式的编解码器特定元数据（Codec Specific Metadata，原文写作 LVT）。 |

<a id="gaddc49e39465798ae4c0cbe345e0b50d7"></a>

### `BT_AUDIO_CODEC_DATA`

```c
#define BT_AUDIO_CODEC_DATA ( _type, _bytes... )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

展开值（Value）：

```c
(sizeof((uint8_t)_type) + sizeof((uint8_t[]){_bytes})), (_type), _bytes
```

用于声明 `bt_audio_codec_cap` 数组元素的辅助宏。

本宏主要用于创建由 `struct bt_audio_codec_cap` 数据数组组成的数组。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_type` | 广播数据字段类型（Advertising Data Field Type）。 |
| `_bytes` | 数量可变的单字节参数（Single-byte Parameters）。 |

<a id="gab6e5f793d514626deca21940d35d8f21"></a>

### `BT_AUDIO_LANG_SIZE`

```c
#define BT_AUDIO_LANG_SIZE 3U
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

流语言值（Stream Language Value）的大小，例如：

`"eng"`。

<a id="ga86a7e9ca661a3b13b7c59d41d206156e"></a>

### `BT_AUDIO_METADATA_TYPE_IS_KNOWN`

```c
#define BT_AUDIO_METADATA_TYPE_IS_KNOWN ( _type)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

展开值（Value）：

```c
(IN_RANGE((_type), BT_AUDIO_METADATA_TYPE_PREF_CONTEXT,                                    \
          BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE) ||                                   \
 (_type) == BT_AUDIO_METADATA_TYPE_EXTENDED || (_type) == BT_AUDIO_METADATA_TYPE_VENDOR)
```

用于检查元数据类型（Metadata Type）是否为协议栈已知类型的辅助宏。

**说明（Note）**：注意（Note）：`_type` 会求值三次（Evaluated Thrice）。

<a id="gaaa0414a4baef5a867fd1c6b1865d2dbc"></a>

### `BT_AUDIO_PD_MAX`

```c
#define BT_AUDIO_PD_MAX 0xFFFFFFU
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

最大呈现延迟（Maximum Presentation Delay），以微秒为单位。

<a id="ga663ab7bf74d56f36ee6cc80b369cbc16"></a>

### `BT_AUDIO_PD_PREF_NONE`

```c
#define BT_AUDIO_PD_PREF_NONE 0x000000U
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

表示服务器对呈现延迟（Presentation Delay）没有偏好。

<a id="ga4a5fd440b96f4e4acbb791badef8c255"></a>

### `BT_AUDIO_RTN_PREF_NONE`

```c
#define BT_AUDIO_RTN_PREF_NONE 0xFFU
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

表示单播服务器（Unicast Server）对重传次数（Retransmission Number）没有偏好。

<a id="ga41db714fa87e85896a52427399633bb4"></a>

### `BT_AUDIO_UNICAST_ANNOUNCEMENT_GENERAL`

```c
#define BT_AUDIO_UNICAST_ANNOUNCEMENT_GENERAL 0x00U
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

单播服务器（Unicast Server）可连接，且未请求连接。

<a id="ga56c14acb7f182a413fdecac4e271c5cc"></a>

### `BT_AUDIO_UNICAST_ANNOUNCEMENT_TARGETED`

```c
#define BT_AUDIO_UNICAST_ANNOUNCEMENT_TARGETED 0x01U
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

单播服务器（Unicast Server）可连接，但正在请求连接。

<a id="ga62108a3dcc3e35f7b31a99f7a33679e6"></a>

### `bt_audio_codec_cfg_target_latency`

```c
enum bt_audio_codec_cfg_target_latency
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

编解码器配置目标延迟（Codec Configuration Target Latency）。

由 BAP 单播客户端（Unicast Client）设置，为 BAP 单播服务器（Unicast Server）提供上下文，以便服务器设置其服务质量偏好（QoS Preferences）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_CODEC_CFG_TARGET_LATENCY_LOW` | 目标为低延迟（Low Latency）。 |
| `BT_AUDIO_CODEC_CFG_TARGET_LATENCY_BALANCED` | 目标为均衡延迟（Balanced Latency）。 |
| `BT_AUDIO_CODEC_CFG_TARGET_LATENCY_HIGH` | 目标为高延迟（High Latency）。 |

<a id="ga640af4e254e73f5c4646e9be4e99f3d1"></a>

### `bt_audio_codec_cfg_target_phy`

```c
enum bt_audio_codec_cfg_target_phy
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

编解码器配置目标物理层（Codec Configuration Target PHY）。

用于达到目标延迟（`bt_audio_codec_cfg_target_latency`）的目标物理层（Target PHY）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_CODEC_CFG_TARGET_PHY_1M` | LE 1M 物理层（LE 1M PHY）。 |
| `BT_AUDIO_CODEC_CFG_TARGET_PHY_2M` | LE 2M 物理层（LE 2M PHY）。 |
| `BT_AUDIO_CODEC_CFG_TARGET_PHY_CODED` | LE 编码物理层（LE Coded PHY）。 |

<a id="ga5bd899fb5e4d844058184913866e462f"></a>

### `bt_audio_dir`

```c
enum bt_audio_dir
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

从 BAP 单播服务器（Unicast Server）／BAP 广播接收端（Broadcast Sink）的视角定义的音频方向（Audio Direction）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_DIR_SINK` | 音频方向为接收端（Sink）。对于 BAP 单播客户端（Unicast Client）或广播源（Broadcast Source），这表示输出音频（TX）；对于 BAP 单播服务器（Unicast Server）或广播接收端（Broadcast Sink），这表示输入音频（RX）。 |
| `BT_AUDIO_DIR_SOURCE` | 音频方向为源端（Source）。对于 BAP 单播客户端（Unicast Client）或广播源（Broadcast Source），这表示输入音频（RX）；对于 BAP 单播服务器（Unicast Server）或广播接收端（Broadcast Sink），这表示输出音频（TX）。 |

<a id="gabbd1b9c46caa9a19de6c95b08c31e5b5"></a>

### `bt_audio_data_get_val()`

```c
int bt_audio_data_get_val ( const uint8_t ltv_data[], size_t size, uint8_t type, const uint8_t ** data )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

从长度—类型—值数据数组（LTV Data Array）中获取特定数据类型的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ltv_data` | 包含长度—类型—值元组（Length-Type-Value Tuples）的数组。 |
| `[in] size` | `ltv_data` 的大小（Size）。 |
| `[in] type` | 要获取其值的类型（Type）。可以是任何类型，但通常为 `bt_audio_codec_cap_type`、`bt_audio_codec_cfg_type` 或 `bt_audio_metadata_type`。 |
| `[out] data` | 指向数据指针的指针，找到条目（Item）时更新该数据指针。找到的所有数据均采用小端序（Little Endian）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `length` | 找到的数据长度（Data Length），可以为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="gafd8574b16141162c95653f0aa2bf6ff7"></a>

### `bt_audio_data_parse()`

```c
int bt_audio_data_parse ( const uint8_t ltv[], size_t size, bool(* func )(struct bt_data *data, void *user_data), void * user_data )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

用于解析长度—类型—值数据（Length-Type-Value Data，LTV）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ltv` | 采用长度—类型—值编码的数据（LTV-encoded Data）。 |
| `size` | LTV 数据的大小（Size）。 |
| `func` | 每找到一个数据元素（Element）就会调用的回调函数（Callback Function）。回调应返回 `true` 继续解析，或返回 `false` 停止解析。 |
| `user_data` | 要传递给回调（Callback）的用户数据（User Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 所有条目（Entries）均已解析。 |
| `-EINVAL` | 数据编码不正确（Incorrectly Encoded）。 |
| `-ECANCELED` | 解析（Parsing）被回调提前取消。 |

<a id="gaf629628fc13be7a1693ceb1d32b743f2"></a>

### `bt_audio_dir_to_str()`

```c
const char * bt_audio_dir_to_str ( enum bt_audio_dir dir)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/audio/audio.h>
```

返回特定 `bt_audio_dir` 方向（Direction）的字符串表示。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dir` | 要转换为字符串的方向（Direction）。 |

**返回（Returns）**：返回值（Returns）：所给方向（Direction）的字符串表示。

<a id="ga87415f8dddd38b3f5641c96e9722a44a"></a>

### `bt_audio_get_chan_count()`

```c
uint8_t bt_audio_get_chan_count ( enum bt_audio_location chan_allocation)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

根据声道分配（Channel Allocation）获取声道数（Number of Channels）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan_allocation` | 声道分配（Channel Allocation）。 |

**返回（Returns）**：返回值（Returns）：声道数（Number of Channels）。


## 1.8\_原页交叉引用（Cross References）

- [分配编号转字符串 API（Assigned numbers to string API）](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md)
- [编解码器能力解析 API（Codec capability parsing APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html)
- [编解码器配置解析 API（Codec config parsing APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html)
- [bt_audio_codec_octets_per_codec_frame](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md)
- [bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)
- [BT_ISO_DATA_PATH_HCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gadd421c69edccfd695d728ded5feb6862)
- [bt_audio_codec_cap_chan_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gae695b5d17359967703f2509db1671fa5)
- [FOR_EACH](../util_reference/P001_通用工具公共接口.md#ga278c8b7cbbea2f585e371d3568f3cb12)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gac1251f8a35b5e343eeeff87f22f8ab10)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gad91341739d394f92ffc4988b614f47b6)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [IN_RANGE](../util_reference/P001_通用工具公共接口.md#gaea00fb0c11b73f77da8884374e2121b4)
- [BT_AUDIO_METADATA_TYPE_PREF_CONTEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a)
- [BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1)
- [BT_AUDIO_METADATA_TYPE_EXTENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39)
- [BT_AUDIO_METADATA_TYPE_VENDOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286)
- [bt_audio_codec_cap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf58823a56eb36cfd22e582ab1ea3d015)
- [bt_audio_codec_cfg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga9230ec4d7518bd243207ba2decb1a974)
- [bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__iso_html_gadd421c69edccfd695d728ded5feb6862"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__audio__codec__cap_html"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gae695b5d17359967703f2509db1671fa5"></a>
<a id="agroup__sys-util_html_ga278c8b7cbbea2f585e371d3568f3cb12"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__bt__audio_html_gga62108a3dcc3e35f7b31a99f7a33679e6a971aeaf3e2df14f5ed75965a31188f80"></a>
<a id="agroup__bt__audio_html_gga640af4e254e73f5c4646e9be4e99f3d1a0b7e1713ff85524953baeb4e7e085d96"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="astructbt__audio__codec__cfg_html"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a"></a>
<a id="agroup__sys-util_html_gaea00fb0c11b73f77da8884374e2121b4"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga62108a3dcc3e35f7b31a99f7a33679e6aec4cf0f851e64e034ead8a075c93eda8"></a>
<a id="gga62108a3dcc3e35f7b31a99f7a33679e6a971aeaf3e2df14f5ed75965a31188f80"></a>
<a id="gga62108a3dcc3e35f7b31a99f7a33679e6a93ec0567d248d4cfc9cd60c26cbc50ef"></a>
<a id="gga640af4e254e73f5c4646e9be4e99f3d1acd5c965423632650196768589a75bd95"></a>
<a id="gga640af4e254e73f5c4646e9be4e99f3d1a0b7e1713ff85524953baeb4e7e085d96"></a>
<a id="gga640af4e254e73f5c4646e9be4e99f3d1a3793a0bbbb7daa399086ce7db0a24a38"></a>
<a id="gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8"></a>
<a id="gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）.md)
