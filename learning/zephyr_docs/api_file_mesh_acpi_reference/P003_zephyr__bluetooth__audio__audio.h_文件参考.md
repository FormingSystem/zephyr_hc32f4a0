---
id: learning.zephyr-docs.api-file-mesh-acpi-reference.page-3
title: zephyr__bluetooth__audio__audio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_bluetooth\_\_audio\_\_audio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙音频（Bluetooth Audio）的处理。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/audio/lc3.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/buf.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/data.h>
#include <zephyr/bluetooth/gatt.h>
#include <zephyr/bluetooth/hci.h>
#include <zephyr/bluetooth/iso.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

蓝牙音频（Bluetooth Audio）的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_bt_5Faudio_5Fcodec_5Foctets_5Fper_5Fcodec_5Fframe"></a>

```c
struct bt_audio_codec_octets_per_codec_frame
```

相关声明：[bt_audio_codec_octets_per_codec_frame](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md)。

保存所支持编解码器帧大小的最小值和最大值的结构体。

<a id="r_bt_5Faudio_5Fcodec_5Fcap"></a>

```c
struct bt_audio_codec_cap
```

相关声明：[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

编解码器能力结构体（Codec Capability Structure）。

<a id="r_bt_5Faudio_5Fcodec_5Fcfg"></a>

```c
struct bt_audio_codec_cfg
```

相关声明：[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

编解码器专用配置结构体（Codec Specific Configuration Structure）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga18dd9f4a4af7716dd01497309ff9c87c"></a>

```c
#define BT_AUDIO_BROADCAST_ID_SIZE 3U
```

相关声明：[BT_AUDIO_BROADCAST_ID_SIZE](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga18dd9f4a4af7716dd01497309ff9c87c)。

广播标识符（Broadcast ID）的大小，以八位字节（Octet）为单位。

<a id="r_ga3ed5ba09ab4c1ab7a59f8a1b4deee791"></a>

```c
#define BT_AUDIO_BROADCAST_ID_MAX 0xFFFFFFU
```

相关声明：[BT_AUDIO_BROADCAST_ID_MAX](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga3ed5ba09ab4c1ab7a59f8a1b4deee791)。

广播标识符（Broadcast ID）的最大值。

<a id="r_ga663ab7bf74d56f36ee6cc80b369cbc16"></a>

```c
#define BT_AUDIO_PD_PREF_NONE 0x000000U
```

相关声明：[BT_AUDIO_PD_PREF_NONE](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga663ab7bf74d56f36ee6cc80b369cbc16)。

表示服务器对呈现延迟（Presentation Delay）没有偏好。

<a id="r_gaaa0414a4baef5a867fd1c6b1865d2dbc"></a>

```c
#define BT_AUDIO_PD_MAX 0xFFFFFFU
```

相关声明：[BT_AUDIO_PD_MAX](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gaaa0414a4baef5a867fd1c6b1865d2dbc)。

最大呈现延迟（Maximum Presentation Delay），以微秒为单位。

<a id="r_ga4a5fd440b96f4e4acbb791badef8c255"></a>

```c
#define BT_AUDIO_RTN_PREF_NONE 0xFFU
```

相关声明：[BT_AUDIO_RTN_PREF_NONE](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga4a5fd440b96f4e4acbb791badef8c255)。

表示单播服务器（Unicast Server）对重传次数（Retransmission Number）没有偏好。

<a id="r_gab6e5f793d514626deca21940d35d8f21"></a>

```c
#define BT_AUDIO_LANG_SIZE 3U
```

相关声明：[BT_AUDIO_LANG_SIZE](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gab6e5f793d514626deca21940d35d8f21)。

流语言值（Stream Language Value）的大小，例如：

<a id="r_ga8f835266fabd6461216fe13e1b3b3a0f"></a>

```c
#define BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT(...)
```

相关声明：[BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga8f835266fabd6461216fe13e1b3b3a0f)。

声道数支持能力（Channel Count Support Capability）。

<a id="r_ga86a7e9ca661a3b13b7c59d41d206156e"></a>

```c
#define BT_AUDIO_METADATA_TYPE_IS_KNOWN(_type)
```

相关声明：[BT_AUDIO_METADATA_TYPE_IS_KNOWN](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga86a7e9ca661a3b13b7c59d41d206156e)。

用于检查元数据类型（Metadata Type）是否为协议栈已知类型的辅助宏。

<a id="r_gaddc49e39465798ae4c0cbe345e0b50d7"></a>

```c
#define BT_AUDIO_CODEC_DATA(_type, _bytes...)
```

相关声明：[BT_AUDIO_CODEC_DATA](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gaddc49e39465798ae4c0cbe345e0b50d7)。

用于声明 `bt_audio_codec_cap` 数组元素的辅助宏。

<a id="r_gaefed7a013e282c63c9b5cbbdcdc67448"></a>

```c
#define BT_AUDIO_CODEC_CFG(_id, _cid, _vid, _data, _meta)
```

相关声明：[BT_AUDIO_CODEC_CFG](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gaefed7a013e282c63c9b5cbbdcdc67448)。

用于声明编解码器配置解析 API（Codec Config Parsing APIs）的辅助宏。

<a id="r_ga6b99f589f6cdcd9e48a83f729a7a4698"></a>

```c
#define BT_AUDIO_CODEC_CAP(_id, _cid, _vid, _data, _meta)
```

相关声明：[BT_AUDIO_CODEC_CAP](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga6b99f589f6cdcd9e48a83f729a7a4698)。

用于声明编解码器能力解析 API 结构体（Codec Capability Parsing APIs Structure）的辅助宏。

<a id="define-members-0"></a>

### 单播公告类型（Unicast Announcement Type）

<a id="r_ga41db714fa87e85896a52427399633bb4"></a>

```c
#define BT_AUDIO_UNICAST_ANNOUNCEMENT_GENERAL 0x00U
```

相关声明：[BT_AUDIO_UNICAST_ANNOUNCEMENT_GENERAL](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga41db714fa87e85896a52427399633bb4)。

单播服务器（Unicast Server）可连接，且未请求连接。

<a id="r_ga56c14acb7f182a413fdecac4e271c5cc"></a>

```c
#define BT_AUDIO_UNICAST_ANNOUNCEMENT_TARGETED 0x01U
```

相关声明：[BT_AUDIO_UNICAST_ANNOUNCEMENT_TARGETED](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga56c14acb7f182a413fdecac4e271c5cc)。

单播服务器（Unicast Server）可连接，但正在请求连接。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.3\_枚举（Enumerations）

<a id="r_ga62108a3dcc3e35f7b31a99f7a33679e6"></a>

```c
enum bt_audio_codec_cfg_target_latency { BT_AUDIO_CODEC_CFG_TARGET_LATENCY_LOW = 0x01 , BT_AUDIO_CODEC_CFG_TARGET_LATENCY_BALANCED = 0x02 , BT_AUDIO_CODEC_CFG_TARGET_LATENCY_HIGH = 0x03 }
```

相关声明：[bt_audio_codec_cfg_target_latency](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga62108a3dcc3e35f7b31a99f7a33679e6)、[BT_AUDIO_CODEC_CFG_TARGET_LATENCY_LOW](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga62108a3dcc3e35f7b31a99f7a33679e6aec4cf0f851e64e034ead8a075c93eda8)、[BT_AUDIO_CODEC_CFG_TARGET_LATENCY_BALANCED](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga62108a3dcc3e35f7b31a99f7a33679e6a971aeaf3e2df14f5ed75965a31188f80)、[BT_AUDIO_CODEC_CFG_TARGET_LATENCY_HIGH](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga62108a3dcc3e35f7b31a99f7a33679e6a93ec0567d248d4cfc9cd60c26cbc50ef)。

编解码器配置目标延迟（Codec Configuration Target Latency）。

<a id="r_ga640af4e254e73f5c4646e9be4e99f3d1"></a>

```c
enum bt_audio_codec_cfg_target_phy { BT_AUDIO_CODEC_CFG_TARGET_PHY_1M = 0x01 , BT_AUDIO_CODEC_CFG_TARGET_PHY_2M = 0x02 , BT_AUDIO_CODEC_CFG_TARGET_PHY_CODED = 0x03 }
```

相关声明：[bt_audio_codec_cfg_target_phy](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga640af4e254e73f5c4646e9be4e99f3d1)、[BT_AUDIO_CODEC_CFG_TARGET_PHY_1M](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga640af4e254e73f5c4646e9be4e99f3d1acd5c965423632650196768589a75bd95)、[BT_AUDIO_CODEC_CFG_TARGET_PHY_2M](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga640af4e254e73f5c4646e9be4e99f3d1a0b7e1713ff85524953baeb4e7e085d96)、[BT_AUDIO_CODEC_CFG_TARGET_PHY_CODED](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga640af4e254e73f5c4646e9be4e99f3d1a3793a0bbbb7daa399086ce7db0a24a38)。

编解码器配置目标物理层（Codec Configuration Target PHY）。

<a id="r_ga5bd899fb5e4d844058184913866e462f"></a>

```c
enum bt_audio_dir { BT_AUDIO_DIR_SINK = 0x01 , BT_AUDIO_DIR_SOURCE = 0x02 }
```

相关声明：[bt_audio_dir](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga5bd899fb5e4d844058184913866e462f)、[BT_AUDIO_DIR_SINK](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8)、[BT_AUDIO_DIR_SOURCE](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c)。

从 BAP 单播服务器（Unicast Server）／BAP 广播接收端（Broadcast Sink）的视角定义的音频方向（Audio Direction）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_gafd8574b16141162c95653f0aa2bf6ff7"></a>

```c
int bt_audio_data_parse (const uint8_t ltv[], size_t size, bool(*func)(struct bt_data *data, void *user_data), void *user_data)
```

相关声明：[bt_audio_data_parse](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gafd8574b16141162c95653f0aa2bf6ff7)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

用于解析长度—类型—值数据（Length-Type-Value Data，LTV）的辅助函数。

<a id="r_gabbd1b9c46caa9a19de6c95b08c31e5b5"></a>

```c
int bt_audio_data_get_val (const uint8_t ltv_data[], size_t size, uint8_t type, const uint8_t **data)
```

相关声明：[bt_audio_data_get_val](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gabbd1b9c46caa9a19de6c95b08c31e5b5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从长度—类型—值数据数组（LTV Data Array）中获取特定数据类型的值。

<a id="r_ga87415f8dddd38b3f5641c96e9722a44a"></a>

```c
uint8_t bt_audio_get_chan_count (enum bt_audio_location chan_allocation)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_audio_get_chan_count](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga87415f8dddd38b3f5641c96e9722a44a)、[bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)。

根据声道分配（Channel Allocation）获取声道数（Number of Channels）的函数。

<a id="r_gaf629628fc13be7a1693ceb1d32b743f2"></a>

```c
static const char * bt_audio_dir_to_str (enum bt_audio_dir dir)
```

相关声明：[bt_audio_dir_to_str](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gaf629628fc13be7a1693ceb1d32b743f2)、[bt_audio_dir](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga5bd899fb5e4d844058184913866e462f)。

返回特定 `bt_audio_dir` 方向（Direction）的字符串表示。

<a id="r_ga2e557fe726a49dc99754da16f7cc60af"></a>

```c
int bt_audio_codec_cfg_freq_to_freq_hz (enum bt_audio_codec_cfg_freq freq)
```

相关声明：[bt_audio_codec_cfg_freq_to_freq_hz](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga2e557fe726a49dc99754da16f7cc60af)、[bt_audio_codec_cfg_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga8e99fb678cc011bb8c9f6e1858bae0d7)。

将分配编号（Assigned Numbers）中的频率编码转换为频率值。

<a id="r_ga99ab4f6d2a18f2a9b4e3da47f63fc9e0"></a>

```c
int bt_audio_codec_cfg_freq_hz_to_freq (uint32_t freq_hz)
```

相关声明：[bt_audio_codec_cfg_freq_hz_to_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将频率值转换为分配编号（Assigned Numbers）中的频率编码。

<a id="r_gad8525a57d35e3e34ea591f7e20e2512d"></a>

```c
int bt_audio_codec_cfg_get_freq (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_get_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gad8525a57d35e3e34ea591f7e20e2512d)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

从编解码器配置（Codec Configuration）中提取频率（Frequency）。

<a id="r_gac119989d5dcfa36becf4edd0ae7c6138"></a>

```c
int bt_audio_codec_cfg_set_freq (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_codec_cfg_freq freq)
```

相关声明：[bt_audio_codec_cfg_set_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gac119989d5dcfa36becf4edd0ae7c6138)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_codec_cfg_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga8e99fb678cc011bb8c9f6e1858bae0d7)。

设置编解码器配置（Codec Configuration）中的频率（Frequency）。

<a id="r_ga225e05df1f0d1efb709c972187901495"></a>

```c
int bt_audio_codec_cfg_frame_dur_to_frame_dur_us (enum bt_audio_codec_cfg_frame_dur frame_dur)
```

相关声明：[bt_audio_codec_cfg_frame_dur_to_frame_dur_us](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga225e05df1f0d1efb709c972187901495)、[bt_audio_codec_cfg_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga83701b5eadfcbc9b84dc0b1a85ebeb74)。

将分配编号（Assigned Numbers）中的帧时长编码转换为以微秒表示的时长。

<a id="r_ga0782a3d9254fb76b441c6c2492571556"></a>

```c
int bt_audio_codec_cfg_frame_dur_us_to_frame_dur (uint32_t frame_dur_us)
```

相关声明：[bt_audio_codec_cfg_frame_dur_us_to_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga0782a3d9254fb76b441c6c2492571556)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将以微秒表示的帧时长转换为分配编号（Assigned Numbers）中的帧时长编码。

<a id="r_ga2dd3afe41b22e989fb46614f89550007"></a>

```c
int bt_audio_codec_cfg_get_frame_dur (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_get_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga2dd3afe41b22e989fb46614f89550007)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

从蓝牙编解码器配置（BT Codec Config）中提取帧时长（Frame Duration）。

<a id="r_ga7d8306f98cb00f06e68a1df417825f0d"></a>

```c
int bt_audio_codec_cfg_set_frame_dur (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_codec_cfg_frame_dur frame_dur)
```

相关声明：[bt_audio_codec_cfg_set_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga7d8306f98cb00f06e68a1df417825f0d)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_codec_cfg_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga83701b5eadfcbc9b84dc0b1a85ebeb74)。

设置编解码器配置（Codec Configuration）中的帧时长（Frame Duration）。

<a id="r_gae712e0f8e84aeb4ad2528da34907e29d"></a>

```c
int bt_audio_codec_cfg_get_chan_allocation (const struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_location *chan_allocation, bool fallback_to_default)
```

相关声明：[bt_audio_codec_cfg_get_chan_allocation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gae712e0f8e84aeb4ad2528da34907e29d)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

从蓝牙编解码器配置（BT Codec Config）中提取声道分配（Channel Allocation）。

<a id="r_gafbbcd69fac18ed0201a5e0156209b049"></a>

```c
int bt_audio_codec_cfg_set_chan_allocation (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_location chan_allocation)
```

相关声明：[bt_audio_codec_cfg_set_chan_allocation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gafbbcd69fac18ed0201a5e0156209b049)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)。

设置编解码器配置（Codec Configuration）中的声道分配（Channel Allocation）。

<a id="r_ga503be053422217502d6108b045791e02"></a>

```c
int bt_audio_codec_cfg_get_octets_per_frame (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_get_octets_per_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga503be053422217502d6108b045791e02)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

从蓝牙编解码器配置（BT Codec Config）中提取以八位组（Octets）表示的帧大小。

<a id="r_ga866cdec28194056dc9e274d0436b45c2"></a>

```c
int bt_audio_codec_cfg_set_octets_per_frame (struct bt_audio_codec_cfg *codec_cfg, uint16_t octets_per_frame)
```

相关声明：[bt_audio_codec_cfg_set_octets_per_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga866cdec28194056dc9e274d0436b45c2)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置编解码器配置（Codec Configuration）中的每个编解码器帧的八位组数（Octets per Codec Frame）。

<a id="r_gadba0723f9d8a9546b659fba139051374"></a>

```c
int bt_audio_codec_cfg_get_frame_blocks_per_sdu (const struct bt_audio_codec_cfg *codec_cfg, bool fallback_to_default)
```

相关声明：[bt_audio_codec_cfg_get_frame_blocks_per_sdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gadba0723f9d8a9546b659fba139051374)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

从蓝牙编解码器配置（BT Codec Config）中提取每个服务数据单元（SDU）包含的音频帧块数量。

<a id="r_gac9cf20bafbe24b34034bfb6ee7aaf03e"></a>

```c
int bt_audio_codec_cfg_set_frame_blocks_per_sdu (struct bt_audio_codec_cfg *codec_cfg, uint8_t frame_blocks)
```

相关声明：[bt_audio_codec_cfg_set_frame_blocks_per_sdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gac9cf20bafbe24b34034bfb6ee7aaf03e)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置（Codec Configuration）中的每个服务数据单元的帧块数（Frame Blocks per SDU）。

<a id="r_ga707c679db0193197b56acabfb08f8d1f"></a>

```c
int bt_audio_codec_cfg_get_val (const struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_codec_cfg_type type, const uint8_t **data)
```

相关声明：[bt_audio_codec_cfg_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga707c679db0193197b56acabfb08f8d1f)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_codec_cfg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga9230ec4d7518bd243207ba2decb1a974)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

查找指定的编解码器配置值（Codec Configuration Value）。

<a id="r_gab10f22938780530b1d1b95695382902e"></a>

```c
int bt_audio_codec_cfg_set_val (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_codec_cfg_type type, const uint8_t *data, size_t data_len)
```

相关声明：[bt_audio_codec_cfg_set_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gab10f22938780530b1d1b95695382902e)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_codec_cfg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga9230ec4d7518bd243207ba2decb1a974)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置或添加指定的编解码器配置值（Codec Configuration Value）。

<a id="r_gad3857d0ca008854df5966501caa261ba"></a>

```c
int bt_audio_codec_cfg_unset_val (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_codec_cfg_type type)
```

相关声明：[bt_audio_codec_cfg_unset_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gad3857d0ca008854df5966501caa261ba)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_codec_cfg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga9230ec4d7518bd243207ba2decb1a974)。

取消设置指定的编解码器配置值（Codec Configuration Value）。

<a id="r_gae98335e87394a491b4a311d867a5e32d"></a>

```c
int bt_audio_codec_cfg_meta_get_val (const struct bt_audio_codec_cfg *codec_cfg, uint8_t type, const uint8_t **data)
```

相关声明：[bt_audio_codec_cfg_meta_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gae98335e87394a491b4a311d867a5e32d)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据类型查找指定的元数据值（Metadata Value）。

<a id="r_ga3e24c2ba8de502600e647cb2f84e3ec4"></a>

```c
int bt_audio_codec_cfg_meta_set_val (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_metadata_type type, const uint8_t *data, size_t data_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga3e24c2ba8de502600e647cb2f84e3ec4)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置或添加指定的编解码器配置元数据值（Codec Configuration Metadata Value）。

<a id="r_gab46f830daa1d9a907f47eb2a9eed7337"></a>

```c
int bt_audio_codec_cfg_meta_unset_val (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_metadata_type type)
```

相关声明：[bt_audio_codec_cfg_meta_unset_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gab46f830daa1d9a907f47eb2a9eed7337)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)。

取消设置指定的编解码器配置元数据值（Codec Configuration Metadata Value）。

<a id="r_gaea087663426a49bb6ff4859800aecb84"></a>

```c
int bt_audio_codec_cfg_meta_get_pref_context (const struct bt_audio_codec_cfg *codec_cfg, bool fallback_to_default)
```

相关声明：[bt_audio_codec_cfg_meta_get_pref_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaea087663426a49bb6ff4859800aecb84)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

提取首选上下文（Preferred Contexts）。

<a id="r_gab40bad609f17d24e7e0e9ffcebe4e912"></a>

```c
int bt_audio_codec_cfg_meta_set_pref_context (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_context ctx)
```

相关声明：[bt_audio_codec_cfg_meta_set_pref_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gab40bad609f17d24e7e0e9ffcebe4e912)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置编解码器配置元数据（Codec Configuration Metadata）中的首选上下文（Preferred Context）。

<a id="r_ga4cc4e1bb941206e7f1541a57fc92b8e9"></a>

```c
int bt_audio_codec_cfg_meta_get_stream_context (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_meta_get_stream_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga4cc4e1bb941206e7f1541a57fc92b8e9)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

提取流上下文（Stream Contexts）。

<a id="r_ga5cd2af1bb44c6eb5bafe824f005a77f0"></a>

```c
int bt_audio_codec_cfg_meta_set_stream_context (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_context ctx)
```

相关声明：[bt_audio_codec_cfg_meta_set_stream_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga5cd2af1bb44c6eb5bafe824f005a77f0)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置编解码器配置元数据（Codec Configuration Metadata）中的流上下文（Stream Context）。

<a id="r_ga03284b8474d65443d7ecc8bdfc6f04c6"></a>

```c
int bt_audio_codec_cfg_meta_get_program_info (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **program_info)
```

相关声明：[bt_audio_codec_cfg_meta_get_program_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga03284b8474d65443d7ecc8bdfc6f04c6)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取节目信息（Program Info）。

<a id="r_ga2ca9e616d20d7513c60ce905f046ac7b"></a>

```c
int bt_audio_codec_cfg_meta_set_program_info (struct bt_audio_codec_cfg *codec_cfg, const uint8_t *program_info, size_t program_info_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_program_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga2ca9e616d20d7513c60ce905f046ac7b)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的节目信息（Program Info）。

<a id="r_ga55e3cbaeacf15fcb1f24a16eb28db99c"></a>

```c
int bt_audio_codec_cfg_meta_get_lang (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **lang)
```

相关声明：[bt_audio_codec_cfg_meta_get_lang](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga55e3cbaeacf15fcb1f24a16eb28db99c)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取语言（Language）。

<a id="r_ga93052db14c857097e7cf9abc34b7fc39"></a>

```c
int bt_audio_codec_cfg_meta_set_lang (struct bt_audio_codec_cfg *codec_cfg, const uint8_t lang[3U])
```

相关声明：[bt_audio_codec_cfg_meta_set_lang](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga93052db14c857097e7cf9abc34b7fc39)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的语言（Language）。

<a id="r_gaa0f9b9f608c7af881d5a928a3ae397b2"></a>

```c
int bt_audio_codec_cfg_meta_get_ccid_list (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **ccid_list)
```

相关声明：[bt_audio_codec_cfg_meta_get_ccid_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaa0f9b9f608c7af881d5a928a3ae397b2)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取内容控制标识符列表（CCID List）。

<a id="r_ga59716b95fcea3404ff8c078564b0e29c"></a>

```c
int bt_audio_codec_cfg_meta_set_ccid_list (struct bt_audio_codec_cfg *codec_cfg, const uint8_t *ccid_list, size_t ccid_list_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_ccid_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga59716b95fcea3404ff8c078564b0e29c)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的内容控制标识符列表（CCID List）。

<a id="r_gaf0eecb02a05f0cc2b75ae9fb32c03913"></a>

```c
int bt_audio_codec_cfg_meta_get_parental_rating (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_meta_get_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaf0eecb02a05f0cc2b75ae9fb32c03913)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

提取家长分级（Parental Rating）。

<a id="r_gab5d8b5877de4fe16c0e06a1d4f0d15ce"></a>

```c
int bt_audio_codec_cfg_meta_set_parental_rating (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_parental_rating parental_rating)
```

相关声明：[bt_audio_codec_cfg_meta_set_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gab5d8b5877de4fe16c0e06a1d4f0d15ce)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga6d4aff1f93dc0b902e4b5d1355f15760)。

设置编解码器配置元数据（Codec Configuration Metadata）中的家长分级（Parental Rating）。

<a id="r_ga6bdbc0a0b929fdbdc75db479aec858df"></a>

```c
int bt_audio_codec_cfg_meta_get_program_info_uri (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **program_info_uri)
```

相关声明：[bt_audio_codec_cfg_meta_get_program_info_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga6bdbc0a0b929fdbdc75db479aec858df)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取节目信息 URI（Program Info URI）。

<a id="r_ga99163729034e816eaef7195505d5ae20"></a>

```c
int bt_audio_codec_cfg_meta_set_program_info_uri (struct bt_audio_codec_cfg *codec_cfg, const uint8_t *program_info_uri, size_t program_info_uri_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_program_info_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga99163729034e816eaef7195505d5ae20)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的节目信息 URI（Program Info URI）。

<a id="r_ga0fd6e6baf1b4f22d60768aaed6f42e8e"></a>

```c
int bt_audio_codec_cfg_meta_get_audio_active_state (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_meta_get_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga0fd6e6baf1b4f22d60768aaed6f42e8e)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

提取音频活动状态（Audio Active State）。

<a id="r_gaf869e7ce0c9dd467fb03e8503d36c58a"></a>

```c
int bt_audio_codec_cfg_meta_set_audio_active_state (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_active_state state)
```

相关声明：[bt_audio_codec_cfg_meta_set_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaf869e7ce0c9dd467fb03e8503d36c58a)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga16d403ec4db7be997682331ad365ff5f)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置编解码器配置元数据（Codec Configuration Metadata）中的音频活动状态（Audio Active State）。

<a id="r_ga66143aa7dcc726e06a12660b8f90fc5a"></a>

```c
int bt_audio_codec_cfg_meta_get_bcast_audio_immediate_rend_flag (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_meta_get_bcast_audio_immediate_rend_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga66143aa7dcc726e06a12660b8f90fc5a)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

提取广播音频立即呈现标志（Broadcast Audio Immediate Rendering Flag）。

<a id="r_gaede61b65d2037c7fbf6c4c4e090990be"></a>

```c
int bt_audio_codec_cfg_meta_set_bcast_audio_immediate_rend_flag (struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_meta_set_bcast_audio_immediate_rend_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaede61b65d2037c7fbf6c4c4e090990be)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

设置编解码器配置元数据（Codec Configuration Metadata）中的广播音频立即呈现标志（Broadcast Audio Immediate Rendering Flag）。

<a id="r_ga22ae14fce65b757e31f391c4bdcae328"></a>

```c
int bt_audio_codec_cfg_meta_get_assisted_listening_stream (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_meta_get_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga22ae14fce65b757e31f391c4bdcae328)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

提取辅助收听流（Assisted Listening Stream）。

<a id="r_ga67d83559cbe6cfab235f2e588cbc398c"></a>

```c
int bt_audio_codec_cfg_meta_set_assisted_listening_stream (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_assisted_listening_stream val)
```

相关声明：[bt_audio_codec_cfg_meta_set_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga67d83559cbe6cfab235f2e588cbc398c)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga207fbf0fbca9b24cba02c7f1d184e7f5)。

设置编解码器配置元数据（Codec Configuration Metadata）中的辅助收听流值（Assisted Listening Stream Value）。

<a id="r_ga5d80babcd6f381014e1fae98a755e1d3"></a>

```c
int bt_audio_codec_cfg_meta_get_broadcast_name (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **broadcast_name)
```

相关声明：[bt_audio_codec_cfg_meta_get_broadcast_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga5d80babcd6f381014e1fae98a755e1d3)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取广播名称（Broadcast Name）。

<a id="r_ga4f5cbacebedc8d7df02d1c47b140bf3c"></a>

```c
int bt_audio_codec_cfg_meta_set_broadcast_name (struct bt_audio_codec_cfg *codec_cfg, const uint8_t *broadcast_name, size_t broadcast_name_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_broadcast_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga4f5cbacebedc8d7df02d1c47b140bf3c)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的广播名称（Broadcast Name）。

<a id="r_ga1f76f82bff63b876eb761a0bf0377428"></a>

```c
int bt_audio_codec_cfg_meta_get_extended (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **extended_meta)
```

相关声明：[bt_audio_codec_cfg_meta_get_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga1f76f82bff63b876eb761a0bf0377428)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取扩展元数据（Extended Metadata）。

<a id="r_gade9cb53287ab3356fb57ba8a454a3aad"></a>

```c
int bt_audio_codec_cfg_meta_set_extended (struct bt_audio_codec_cfg *codec_cfg, const uint8_t *extended_meta, size_t extended_meta_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gade9cb53287ab3356fb57ba8a454a3aad)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的扩展元数据（Extended Metadata）。

<a id="r_ga4a4982e3bd0e8c944b584196ef146f6c"></a>

```c
int bt_audio_codec_cfg_meta_get_vendor (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **vendor_meta)
```

相关声明：[bt_audio_codec_cfg_meta_get_vendor](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga4a4982e3bd0e8c944b584196ef146f6c)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取厂商特定元数据（Vendor Specific Metadata）。

<a id="r_ga6935d1c40b3178b0c8fa877ee93d1e53"></a>

```c
int bt_audio_codec_cfg_meta_set_vendor (struct bt_audio_codec_cfg *codec_cfg, const uint8_t *vendor_meta, size_t vendor_meta_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_vendor](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga6935d1c40b3178b0c8fa877ee93d1e53)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的厂商特定元数据（Vendor Specific Metadata）。

<a id="r_gac3bf5dd414271bb1dcbc6590994cff6b"></a>

```c
int bt_audio_codec_cap_get_val (const struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_type type, const uint8_t **data)
```

相关声明：[bt_audio_codec_cap_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gac3bf5dd414271bb1dcbc6590994cff6b)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_cap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf58823a56eb36cfd22e582ab1ea3d015)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据类型查找指定值。

<a id="r_ga0c2c816b0b2b85aa5dd38f21caceea40"></a>

```c
int bt_audio_codec_cap_set_val (struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_type type, const uint8_t *data, size_t data_len)
```

相关声明：[bt_audio_codec_cap_set_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga0c2c816b0b2b85aa5dd38f21caceea40)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_cap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf58823a56eb36cfd22e582ab1ea3d015)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置或添加指定的编解码器能力值（Codec Capability Value）。

<a id="r_gabc9962212ad65339ff02ba1389d5f9f8"></a>

```c
int bt_audio_codec_cap_unset_val (struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_type type)
```

相关声明：[bt_audio_codec_cap_unset_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gabc9962212ad65339ff02ba1389d5f9f8)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_cap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf58823a56eb36cfd22e582ab1ea3d015)。

取消设置指定的编解码器能力值（Codec Capability Value）。

<a id="r_gaa1dbf81c437c983af0144bf62433666c"></a>

```c
int bt_audio_codec_cap_get_freq (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_get_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaa1dbf81c437c983af0144bf62433666c)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

从编解码器能力（Codec Capability）中提取频率（Frequency）。

<a id="r_gac0655c0bd6552ab8a265076d7d0cd1b2"></a>

```c
int bt_audio_codec_cap_set_freq (struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_freq freq)
```

相关声明：[bt_audio_codec_cap_set_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gac0655c0bd6552ab8a265076d7d0cd1b2)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_cap_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaafc1106d5d305874ee2f540c850ff5b4)。

设置编解码器能力（Codec Capability）中的支持的频率（Supported Frequencies）。

<a id="r_ga12336de7d908bda94427caee4dc080e0"></a>

```c
int bt_audio_codec_cap_get_frame_dur (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_get_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga12336de7d908bda94427caee4dc080e0)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

从编解码器能力（Codec Capability）中提取帧时长（Frame Duration）。

<a id="r_ga53e5df6cc4cfbed12b59a6a506657772"></a>

```c
int bt_audio_codec_cap_set_frame_dur (struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_frame_dur frame_dur)
```

相关声明：[bt_audio_codec_cap_set_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga53e5df6cc4cfbed12b59a6a506657772)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_cap_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf37e8e19f956afb3c3a413cbaa1a21f5)。

设置编解码器能力（Codec Capability）中的帧时长（Frame Duration）。

<a id="r_ga63d5e083f03ec06939ee1cd0355c8c2a"></a>

```c
int bt_audio_codec_cap_get_supported_audio_chan_counts (const struct bt_audio_codec_cap *codec_cap, bool fallback_to_default)
```

相关声明：[bt_audio_codec_cap_get_supported_audio_chan_counts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga63d5e083f03ec06939ee1cd0355c8c2a)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

从编解码器能力（Codec Capability）中提取支持的音频声道数量（Audio Channel Counts）。

<a id="r_gaf6b2717823f9f3136237ed6a6515449e"></a>

```c
int bt_audio_codec_cap_set_supported_audio_chan_counts (struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_chan_count chan_count)
```

相关声明：[bt_audio_codec_cap_set_supported_audio_chan_counts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaf6b2717823f9f3136237ed6a6515449e)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_cap_chan_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gae695b5d17359967703f2509db1671fa5)。

设置编解码器能力（Codec Capability）中的声道数量（Channel Count）。

<a id="r_gaa949089f2c6c143041e6cb61338e0ddc"></a>

```c
int bt_audio_codec_cap_get_octets_per_frame (const struct bt_audio_codec_cap *codec_cap, struct bt_audio_codec_octets_per_codec_frame *codec_frame)
```

相关声明：[bt_audio_codec_cap_get_octets_per_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaa949089f2c6c143041e6cb61338e0ddc)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_octets_per_codec_frame](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md)。

从编解码器能力（Codec Capability）中提取支持的每个编解码器帧的八位组数（Octets per Codec Frame）。

<a id="r_gac1c42460cd3c55bbfbd467f84ab2d78d"></a>

```c
int bt_audio_codec_cap_set_octets_per_frame (struct bt_audio_codec_cap *codec_cap, const struct bt_audio_codec_octets_per_codec_frame *codec_frame)
```

相关声明：[bt_audio_codec_cap_set_octets_per_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gac1c42460cd3c55bbfbd467f84ab2d78d)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_octets_per_codec_frame](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md)。

设置编解码器能力（Codec Capability）中的每个编解码器帧的八位组数（Octets per Codec Frame）。

<a id="r_ga194d938896ee65601bdce96d68c84885"></a>

```c
int bt_audio_codec_cap_get_max_codec_frames_per_sdu (const struct bt_audio_codec_cap *codec_cap, bool fallback_to_default)
```

相关声明：[bt_audio_codec_cap_get_max_codec_frames_per_sdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga194d938896ee65601bdce96d68c84885)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

从编解码器能力（Codec Capability）中提取每个服务数据单元（SDU）的最大编解码器帧数。

<a id="r_ga3785bc41f56f8f2a09248396dadb31da"></a>

```c
int bt_audio_codec_cap_set_max_codec_frames_per_sdu (struct bt_audio_codec_cap *codec_cap, uint8_t codec_frames_per_sdu)
```

相关声明：[bt_audio_codec_cap_set_max_codec_frames_per_sdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga3785bc41f56f8f2a09248396dadb31da)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力（Codec Capability）中的每个服务数据单元的最大编解码器帧数（Maximum Codec Frames per SDU）。

<a id="r_ga5c2ecbb4d0cef26dd2cc5d023e70a163"></a>

```c
int bt_audio_codec_cap_meta_get_val (const struct bt_audio_codec_cap *codec_cap, uint8_t type, const uint8_t **data)
```

相关声明：[bt_audio_codec_cap_meta_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga5c2ecbb4d0cef26dd2cc5d023e70a163)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据类型查找指定的元数据值（Metadata Value）。

<a id="r_ga1fdfd8c36f4131bcf4ffd2b7f176b631"></a>

```c
int bt_audio_codec_cap_meta_set_val (struct bt_audio_codec_cap *codec_cap, enum bt_audio_metadata_type type, const uint8_t *data, size_t data_len)
```

相关声明：[bt_audio_codec_cap_meta_set_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga1fdfd8c36f4131bcf4ffd2b7f176b631)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置或添加指定的编解码器能力元数据值（Codec Capability Metadata Value）。

<a id="r_ga40848f5375d1e58622c580112c282f2e"></a>

```c
int bt_audio_codec_cap_meta_unset_val (struct bt_audio_codec_cap *codec_cap, enum bt_audio_metadata_type type)
```

相关声明：[bt_audio_codec_cap_meta_unset_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga40848f5375d1e58622c580112c282f2e)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)。

取消设置指定的编解码器能力元数据值（Codec Capability Metadata Value）。

<a id="r_gaaa8c6783241b1b70349354b3e36c696c"></a>

```c
int bt_audio_codec_cap_meta_get_pref_context (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_get_pref_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaaa8c6783241b1b70349354b3e36c696c)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

提取首选上下文（Preferred Contexts）。

<a id="r_ga7fe0d4553d6accf5c89645cbf86149bf"></a>

```c
int bt_audio_codec_cap_meta_set_pref_context (struct bt_audio_codec_cap *codec_cap, enum bt_audio_context ctx)
```

相关声明：[bt_audio_codec_cap_meta_set_pref_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga7fe0d4553d6accf5c89645cbf86149bf)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置编解码器能力元数据（Codec Capability Metadata）中的首选上下文（Preferred Context）。

<a id="r_ga88ee657b5bd3f847bb75c9620ddb142f"></a>

```c
int bt_audio_codec_cap_meta_get_stream_context (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_get_stream_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga88ee657b5bd3f847bb75c9620ddb142f)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

提取流上下文（Stream Contexts）。

<a id="r_ga5cc7f360049c38c8de631ea33dbc44ab"></a>

```c
int bt_audio_codec_cap_meta_set_stream_context (struct bt_audio_codec_cap *codec_cap, enum bt_audio_context ctx)
```

相关声明：[bt_audio_codec_cap_meta_set_stream_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga5cc7f360049c38c8de631ea33dbc44ab)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置编解码器能力元数据（Codec Capability Metadata）中的流上下文（Stream Context）。

<a id="r_ga33725c3b2c06d6c22030bb5a77d702b0"></a>

```c
int bt_audio_codec_cap_meta_get_program_info (const struct bt_audio_codec_cap *codec_cap, const uint8_t **program_info)
```

相关声明：[bt_audio_codec_cap_meta_get_program_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga33725c3b2c06d6c22030bb5a77d702b0)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取节目信息（Program Info）。

<a id="r_ga43d2ec3a4d621c26843de82db7fd2189"></a>

```c
int bt_audio_codec_cap_meta_set_program_info (struct bt_audio_codec_cap *codec_cap, const uint8_t *program_info, size_t program_info_len)
```

相关声明：[bt_audio_codec_cap_meta_set_program_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga43d2ec3a4d621c26843de82db7fd2189)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的节目信息（Program Info）。

<a id="r_gafb631b55b69b256c60b9cf3c7f418ff8"></a>

```c
int bt_audio_codec_cap_meta_get_lang (const struct bt_audio_codec_cap *codec_cap, const uint8_t **lang)
```

相关声明：[bt_audio_codec_cap_meta_get_lang](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gafb631b55b69b256c60b9cf3c7f418ff8)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取语言（Language）。

<a id="r_ga555db1eff71a3bc79a5bcb959c0198cc"></a>

```c
int bt_audio_codec_cap_meta_set_lang (struct bt_audio_codec_cap *codec_cap, const uint8_t lang[3U])
```

相关声明：[bt_audio_codec_cap_meta_set_lang](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga555db1eff71a3bc79a5bcb959c0198cc)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的语言（Language）。

<a id="r_ga3095dea36e60e75cbfe786d3c2f11866"></a>

```c
int bt_audio_codec_cap_meta_get_ccid_list (const struct bt_audio_codec_cap *codec_cap, const uint8_t **ccid_list)
```

相关声明：[bt_audio_codec_cap_meta_get_ccid_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga3095dea36e60e75cbfe786d3c2f11866)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取内容控制标识符列表（CCID List）。

<a id="r_ga00a8ad22713dab761c81d1b8481c037d"></a>

```c
int bt_audio_codec_cap_meta_set_ccid_list (struct bt_audio_codec_cap *codec_cap, const uint8_t *ccid_list, size_t ccid_list_len)
```

相关声明：[bt_audio_codec_cap_meta_set_ccid_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga00a8ad22713dab761c81d1b8481c037d)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的内容控制标识符列表（CCID List）。

<a id="r_gab34d0369ce08efcd407d33956d32632e"></a>

```c
int bt_audio_codec_cap_meta_get_parental_rating (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_get_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gab34d0369ce08efcd407d33956d32632e)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

提取家长分级（Parental Rating）。

<a id="r_ga5e267dfad978cd3d52be9c31a4fac0be"></a>

```c
int bt_audio_codec_cap_meta_set_parental_rating (struct bt_audio_codec_cap *codec_cap, enum bt_audio_parental_rating parental_rating)
```

相关声明：[bt_audio_codec_cap_meta_set_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga5e267dfad978cd3d52be9c31a4fac0be)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga6d4aff1f93dc0b902e4b5d1355f15760)。

设置编解码器能力元数据（Codec Capability Metadata）中的家长分级（Parental Rating）。

<a id="r_gadb39b0ee1f65cdd2457fdf2c3142c040"></a>

```c
int bt_audio_codec_cap_meta_get_program_info_uri (const struct bt_audio_codec_cap *codec_cap, const uint8_t **program_info_uri)
```

相关声明：[bt_audio_codec_cap_meta_get_program_info_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gadb39b0ee1f65cdd2457fdf2c3142c040)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取节目信息 URI（Program Info URI）。

<a id="r_gafbb0d6282d989e8bc70caada2845b337"></a>

```c
int bt_audio_codec_cap_meta_set_program_info_uri (struct bt_audio_codec_cap *codec_cap, const uint8_t *program_info_uri, size_t program_info_uri_len)
```

相关声明：[bt_audio_codec_cap_meta_set_program_info_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gafbb0d6282d989e8bc70caada2845b337)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的节目信息 URI（Program Info URI）。

<a id="r_ga88bb1da63b7ea0f95dd236aa1024cfb8"></a>

```c
int bt_audio_codec_cap_meta_get_audio_active_state (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_get_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga88bb1da63b7ea0f95dd236aa1024cfb8)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

提取音频活动状态（Audio Active State）。

<a id="r_gacd3de0306a22d1a1d9ba09b4ac4f4e09"></a>

```c
int bt_audio_codec_cap_meta_set_audio_active_state (struct bt_audio_codec_cap *codec_cap, enum bt_audio_active_state state)
```

相关声明：[bt_audio_codec_cap_meta_set_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gacd3de0306a22d1a1d9ba09b4ac4f4e09)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga16d403ec4db7be997682331ad365ff5f)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置编解码器能力元数据（Codec Capability Metadata）中的音频活动状态（Audio Active State）。

<a id="r_gab4ccc7cb7d779acb20185ae808dd8bbe"></a>

```c
int bt_audio_codec_cap_meta_get_bcast_audio_immediate_rend_flag (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_get_bcast_audio_immediate_rend_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gab4ccc7cb7d779acb20185ae808dd8bbe)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

提取广播音频立即呈现标志（Broadcast Audio Immediate Rendering Flag）。

<a id="r_gaa1d382b4fa53f7cbe8426df53a3317ce"></a>

```c
int bt_audio_codec_cap_meta_set_bcast_audio_immediate_rend_flag (struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_set_bcast_audio_immediate_rend_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaa1d382b4fa53f7cbe8426df53a3317ce)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

设置编解码器能力元数据（Codec Capability Metadata）中的广播音频立即呈现标志（Broadcast Audio Immediate Rendering Flag）。

<a id="r_ga4f1ea56f2c1c21420f078d35081ceee5"></a>

```c
int bt_audio_codec_cap_meta_get_assisted_listening_stream (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_get_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga4f1ea56f2c1c21420f078d35081ceee5)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

提取辅助收听流（Assisted Listening Stream）。

<a id="r_ga3346db1f59cb35b9b9e5255424adb6e4"></a>

```c
int bt_audio_codec_cap_meta_set_assisted_listening_stream (struct bt_audio_codec_cap *codec_cap, enum bt_audio_assisted_listening_stream val)
```

相关声明：[bt_audio_codec_cap_meta_set_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga3346db1f59cb35b9b9e5255424adb6e4)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga207fbf0fbca9b24cba02c7f1d184e7f5)。

设置编解码器能力元数据（Codec Capability Metadata）中的辅助收听流值（Assisted Listening Stream Value）。

<a id="r_ga3c8df3fe79f0bb96c4e15e7c2502bf89"></a>

```c
int bt_audio_codec_cap_meta_get_broadcast_name (const struct bt_audio_codec_cap *codec_cap, const uint8_t **broadcast_name)
```

相关声明：[bt_audio_codec_cap_meta_get_broadcast_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga3c8df3fe79f0bb96c4e15e7c2502bf89)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取广播名称（Broadcast Name）。

<a id="r_ga461add2808a1eca8993222d2b31d5a5f"></a>

```c
int bt_audio_codec_cap_meta_set_broadcast_name (struct bt_audio_codec_cap *codec_cap, const uint8_t *broadcast_name, size_t broadcast_name_len)
```

相关声明：[bt_audio_codec_cap_meta_set_broadcast_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga461add2808a1eca8993222d2b31d5a5f)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的广播名称（Broadcast Name）。

<a id="r_ga69aecd7e98f90a5162ff8ea3373b43d4"></a>

```c
int bt_audio_codec_cap_meta_get_extended (const struct bt_audio_codec_cap *codec_cap, const uint8_t **extended_meta)
```

相关声明：[bt_audio_codec_cap_meta_get_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga69aecd7e98f90a5162ff8ea3373b43d4)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取扩展元数据（Extended Metadata）。

<a id="r_gac00aabc7329027852a7caf5cdff2bc26"></a>

```c
int bt_audio_codec_cap_meta_set_extended (struct bt_audio_codec_cap *codec_cap, const uint8_t *extended_meta, size_t extended_meta_len)
```

相关声明：[bt_audio_codec_cap_meta_set_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gac00aabc7329027852a7caf5cdff2bc26)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的扩展元数据（Extended Metadata）。

<a id="r_gab8c80a0f55041f026d453fd88cdeb727"></a>

```c
int bt_audio_codec_cap_meta_get_vendor (const struct bt_audio_codec_cap *codec_cap, const uint8_t **vendor_meta)
```

相关声明：[bt_audio_codec_cap_meta_get_vendor](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gab8c80a0f55041f026d453fd88cdeb727)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取厂商特定元数据（Vendor Specific Metadata）。

<a id="r_ga1f06789782541beab9aab4914f91bb57"></a>

```c
int bt_audio_codec_cap_meta_set_vendor (struct bt_audio_codec_cap *codec_cap, const uint8_t *vendor_meta, size_t vendor_meta_len)
```

相关声明：[bt_audio_codec_cap_meta_set_vendor](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga1f06789782541beab9aab4914f91bb57)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的厂商特定元数据（Vendor Specific Metadata）。

<a id="r_ga26436fc678423ff1cf3543d381359d0f"></a>

```c
static char * bt_audio_context_bit_to_str (enum bt_audio_context context)
```

相关声明：[bt_audio_context_bit_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#ga26436fc678423ff1cf3543d381359d0f)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

返回 `bt_audio_context` 中某个特定位的字符串表示（String Representation）。

<a id="r_ga6926c4e8bda0874769177a903276c072"></a>

```c
static char * bt_audio_parental_rating_to_str (enum bt_audio_parental_rating parental_rating)
```

相关声明：[bt_audio_parental_rating_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#ga6926c4e8bda0874769177a903276c072)、[bt_audio_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga6d4aff1f93dc0b902e4b5d1355f15760)。

返回 `bt_audio_parental_rating` 值的字符串表示（String Representation）。

<a id="r_ga1dd5865429e2438e0d4f88e891eda975"></a>

```c
static char * bt_audio_active_state_to_str (enum bt_audio_active_state state)
```

相关声明：[bt_audio_active_state_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#ga1dd5865429e2438e0d4f88e891eda975)、[bt_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga16d403ec4db7be997682331ad365ff5f)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

返回 `bt_audio_active_state` 值的字符串表示（String Representation）。

<a id="r_gadd3bac4f1f1b334cb60f5783fdc15c14"></a>

```c
static char * bt_audio_codec_cap_freq_bit_to_str (enum bt_audio_codec_cap_freq freq)
```

相关声明：[bt_audio_codec_cap_freq_bit_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#gadd3bac4f1f1b334cb60f5783fdc15c14)、[bt_audio_codec_cap_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaafc1106d5d305874ee2f540c850ff5b4)。

返回 `bt_audio_codec_cap_freq` 中某个特定位的字符串表示（String Representation）。

<a id="r_ga6b9cc74dafcf03056862ae9823bce58d"></a>

```c
static char * bt_audio_codec_cap_frame_dur_bit_to_str (enum bt_audio_codec_cap_frame_dur frame_dur)
```

相关声明：[bt_audio_codec_cap_frame_dur_bit_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#ga6b9cc74dafcf03056862ae9823bce58d)、[bt_audio_codec_cap_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf37e8e19f956afb3c3a413cbaa1a21f5)。

返回 `bt_audio_codec_cap_frame_dur` 中某个特定位的字符串表示（String Representation）。

<a id="r_ga795742ed8d91e2b675fbcdaeee7a71ec"></a>

```c
static char * bt_audio_codec_cap_chan_count_bit_to_str (enum bt_audio_codec_cap_chan_count chan_count)
```

相关声明：[bt_audio_codec_cap_chan_count_bit_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#ga795742ed8d91e2b675fbcdaeee7a71ec)、[bt_audio_codec_cap_chan_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gae695b5d17359967703f2509db1671fa5)。

返回 `bt_audio_codec_cap_chan_count` 中某个特定位的字符串表示（String Representation）。

<a id="r_gaa1b9f7166fd6e6797da65d9537357324"></a>

```c
static char * bt_audio_location_bit_to_str (enum bt_audio_location location)
```

相关声明：[bt_audio_location_bit_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#gaa1b9f7166fd6e6797da65d9537357324)、[bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)。

返回 `bt_audio_location` 中某个特定位的字符串表示（String Representation）。


## 3.5\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/assigned_numbers.h](../api_source_socket_ethernet_reference/P001_assigned_numbers.h_源码浏览.md)
- [zephyr/bluetooth/audio/lc3.h](../api_source_reference/P437_lc3.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/bluetooth/buf.h](../api_source_system_reference/P005_buf.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/bluetooth/data.h](../api_source_reference/P121_data.h_源码浏览.md)
- [zephyr/bluetooth/gatt.h](../api_source_runtime_reference/P021_gatt.h_源码浏览.md)
- [zephyr/bluetooth/hci.h](../api_source_supplement_reference/P085_hci.h_源码浏览.md)
- [zephyr/bluetooth/iso.h](../api_source_reference/P415_iso.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_compiler_device_reference/P002_audio.h_源码浏览.md)
- [bt_audio_codec_octets_per_codec_frame](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md)
- [bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [BT_AUDIO_BROADCAST_ID_SIZE](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga18dd9f4a4af7716dd01497309ff9c87c)
- [BT_AUDIO_BROADCAST_ID_MAX](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga3ed5ba09ab4c1ab7a59f8a1b4deee791)
- [BT_AUDIO_PD_PREF_NONE](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga663ab7bf74d56f36ee6cc80b369cbc16)
- [BT_AUDIO_PD_MAX](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gaaa0414a4baef5a867fd1c6b1865d2dbc)
- [BT_AUDIO_RTN_PREF_NONE](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga4a5fd440b96f4e4acbb791badef8c255)
- [BT_AUDIO_LANG_SIZE](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gab6e5f793d514626deca21940d35d8f21)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_SUPPORT](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga8f835266fabd6461216fe13e1b3b3a0f)
- [BT_AUDIO_METADATA_TYPE_IS_KNOWN](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga86a7e9ca661a3b13b7c59d41d206156e)
- [BT_AUDIO_CODEC_DATA](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gaddc49e39465798ae4c0cbe345e0b50d7)
- [BT_AUDIO_CODEC_CFG](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gaefed7a013e282c63c9b5cbbdcdc67448)
- [编解码器配置解析 API（Codec config parsing APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html)
- [BT_AUDIO_CODEC_CAP](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga6b99f589f6cdcd9e48a83f729a7a4698)
- [编解码器能力解析 API（Codec capability parsing APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html)
- [BT_AUDIO_UNICAST_ANNOUNCEMENT_GENERAL](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga41db714fa87e85896a52427399633bb4)
- [BT_AUDIO_UNICAST_ANNOUNCEMENT_TARGETED](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga56c14acb7f182a413fdecac4e271c5cc)
- [bt_audio_codec_cfg_target_latency](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga62108a3dcc3e35f7b31a99f7a33679e6)
- [BT_AUDIO_CODEC_CFG_TARGET_LATENCY_LOW](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga62108a3dcc3e35f7b31a99f7a33679e6aec4cf0f851e64e034ead8a075c93eda8)
- [BT_AUDIO_CODEC_CFG_TARGET_LATENCY_BALANCED](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga62108a3dcc3e35f7b31a99f7a33679e6a971aeaf3e2df14f5ed75965a31188f80)
- [BT_AUDIO_CODEC_CFG_TARGET_LATENCY_HIGH](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga62108a3dcc3e35f7b31a99f7a33679e6a93ec0567d248d4cfc9cd60c26cbc50ef)
- [bt_audio_codec_cfg_target_phy](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga640af4e254e73f5c4646e9be4e99f3d1)
- [BT_AUDIO_CODEC_CFG_TARGET_PHY_1M](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga640af4e254e73f5c4646e9be4e99f3d1acd5c965423632650196768589a75bd95)
- [BT_AUDIO_CODEC_CFG_TARGET_PHY_2M](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga640af4e254e73f5c4646e9be4e99f3d1a0b7e1713ff85524953baeb4e7e085d96)
- [BT_AUDIO_CODEC_CFG_TARGET_PHY_CODED](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga640af4e254e73f5c4646e9be4e99f3d1a3793a0bbbb7daa399086ce7db0a24a38)
- [bt_audio_dir](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga5bd899fb5e4d844058184913866e462f)
- [BT_AUDIO_DIR_SINK](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8)
- [BT_AUDIO_DIR_SOURCE](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c)
- [bt_audio_data_parse](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gafd8574b16141162c95653f0aa2bf6ff7)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [bt_audio_data_get_val](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gabbd1b9c46caa9a19de6c95b08c31e5b5)
- [bt_audio_get_chan_count](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#ga87415f8dddd38b3f5641c96e9722a44a)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [bt_audio_dir_to_str](../api_flash_connection_topic_reference/P001_蓝牙音频（Bluetooth Audio）.md#gaf629628fc13be7a1693ceb1d32b743f2)
- [bt_audio_codec_cfg_freq_to_freq_hz](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga2e557fe726a49dc99754da16f7cc60af)
- [bt_audio_codec_cfg_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga8e99fb678cc011bb8c9f6e1858bae0d7)
- [bt_audio_codec_cfg_freq_hz_to_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_audio_codec_cfg_get_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gad8525a57d35e3e34ea591f7e20e2512d)
- [bt_audio_codec_cfg_set_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gac119989d5dcfa36becf4edd0ae7c6138)
- [bt_audio_codec_cfg_frame_dur_to_frame_dur_us](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga225e05df1f0d1efb709c972187901495)
- [bt_audio_codec_cfg_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga83701b5eadfcbc9b84dc0b1a85ebeb74)
- [bt_audio_codec_cfg_frame_dur_us_to_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga0782a3d9254fb76b441c6c2492571556)
- [bt_audio_codec_cfg_get_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga2dd3afe41b22e989fb46614f89550007)
- [bt_audio_codec_cfg_set_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga7d8306f98cb00f06e68a1df417825f0d)
- [bt_audio_codec_cfg_get_chan_allocation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gae712e0f8e84aeb4ad2528da34907e29d)
- [bt_audio_codec_cfg_set_chan_allocation](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gafbbcd69fac18ed0201a5e0156209b049)
- [bt_audio_codec_cfg_get_octets_per_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga503be053422217502d6108b045791e02)
- [bt_audio_codec_cfg_set_octets_per_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga866cdec28194056dc9e274d0436b45c2)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_audio_codec_cfg_get_frame_blocks_per_sdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gadba0723f9d8a9546b659fba139051374)
- [bt_audio_codec_cfg_set_frame_blocks_per_sdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gac9cf20bafbe24b34034bfb6ee7aaf03e)
- [bt_audio_codec_cfg_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga707c679db0193197b56acabfb08f8d1f)
- [bt_audio_codec_cfg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga9230ec4d7518bd243207ba2decb1a974)
- [bt_audio_codec_cfg_set_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gab10f22938780530b1d1b95695382902e)
- [bt_audio_codec_cfg_unset_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gad3857d0ca008854df5966501caa261ba)
- [bt_audio_codec_cfg_meta_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gae98335e87394a491b4a311d867a5e32d)
- [bt_audio_codec_cfg_meta_set_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga3e24c2ba8de502600e647cb2f84e3ec4)
- [bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)
- [bt_audio_codec_cfg_meta_unset_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gab46f830daa1d9a907f47eb2a9eed7337)
- [bt_audio_codec_cfg_meta_get_pref_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaea087663426a49bb6ff4859800aecb84)
- [bt_audio_codec_cfg_meta_set_pref_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gab40bad609f17d24e7e0e9ffcebe4e912)
- [bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)
- [bt_audio_codec_cfg_meta_get_stream_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga4cc4e1bb941206e7f1541a57fc92b8e9)
- [bt_audio_codec_cfg_meta_set_stream_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga5cd2af1bb44c6eb5bafe824f005a77f0)
- [bt_audio_codec_cfg_meta_get_program_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga03284b8474d65443d7ecc8bdfc6f04c6)
- [bt_audio_codec_cfg_meta_set_program_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga2ca9e616d20d7513c60ce905f046ac7b)
- [bt_audio_codec_cfg_meta_get_lang](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga55e3cbaeacf15fcb1f24a16eb28db99c)
- [bt_audio_codec_cfg_meta_set_lang](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga93052db14c857097e7cf9abc34b7fc39)
- [bt_audio_codec_cfg_meta_get_ccid_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaa0f9b9f608c7af881d5a928a3ae397b2)
- [bt_audio_codec_cfg_meta_set_ccid_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga59716b95fcea3404ff8c078564b0e29c)
- [bt_audio_codec_cfg_meta_get_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaf0eecb02a05f0cc2b75ae9fb32c03913)
- [bt_audio_codec_cfg_meta_set_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gab5d8b5877de4fe16c0e06a1d4f0d15ce)
- [bt_audio_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga6d4aff1f93dc0b902e4b5d1355f15760)
- [bt_audio_codec_cfg_meta_get_program_info_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga6bdbc0a0b929fdbdc75db479aec858df)
- [bt_audio_codec_cfg_meta_set_program_info_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga99163729034e816eaef7195505d5ae20)
- [bt_audio_codec_cfg_meta_get_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga0fd6e6baf1b4f22d60768aaed6f42e8e)
- [bt_audio_codec_cfg_meta_set_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaf869e7ce0c9dd467fb03e8503d36c58a)
- [bt_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga16d403ec4db7be997682331ad365ff5f)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_audio_codec_cfg_meta_get_bcast_audio_immediate_rend_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga66143aa7dcc726e06a12660b8f90fc5a)
- [bt_audio_codec_cfg_meta_set_bcast_audio_immediate_rend_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaede61b65d2037c7fbf6c4c4e090990be)
- [bt_audio_codec_cfg_meta_get_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga22ae14fce65b757e31f391c4bdcae328)
- [bt_audio_codec_cfg_meta_set_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga67d83559cbe6cfab235f2e588cbc398c)
- [bt_audio_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga207fbf0fbca9b24cba02c7f1d184e7f5)
- [bt_audio_codec_cfg_meta_get_broadcast_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga5d80babcd6f381014e1fae98a755e1d3)
- [bt_audio_codec_cfg_meta_set_broadcast_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga4f5cbacebedc8d7df02d1c47b140bf3c)
- [bt_audio_codec_cfg_meta_get_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga1f76f82bff63b876eb761a0bf0377428)
- [bt_audio_codec_cfg_meta_set_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gade9cb53287ab3356fb57ba8a454a3aad)
- [bt_audio_codec_cfg_meta_get_vendor](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga4a4982e3bd0e8c944b584196ef146f6c)
- [bt_audio_codec_cfg_meta_set_vendor](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga6935d1c40b3178b0c8fa877ee93d1e53)
- [bt_audio_codec_cap_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gac3bf5dd414271bb1dcbc6590994cff6b)
- [bt_audio_codec_cap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf58823a56eb36cfd22e582ab1ea3d015)
- [bt_audio_codec_cap_set_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga0c2c816b0b2b85aa5dd38f21caceea40)
- [bt_audio_codec_cap_unset_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gabc9962212ad65339ff02ba1389d5f9f8)
- [bt_audio_codec_cap_get_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaa1dbf81c437c983af0144bf62433666c)
- [bt_audio_codec_cap_set_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gac0655c0bd6552ab8a265076d7d0cd1b2)
- [bt_audio_codec_cap_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaafc1106d5d305874ee2f540c850ff5b4)
- [bt_audio_codec_cap_get_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga12336de7d908bda94427caee4dc080e0)
- [bt_audio_codec_cap_set_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga53e5df6cc4cfbed12b59a6a506657772)
- [bt_audio_codec_cap_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf37e8e19f956afb3c3a413cbaa1a21f5)
- [bt_audio_codec_cap_get_supported_audio_chan_counts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga63d5e083f03ec06939ee1cd0355c8c2a)
- [bt_audio_codec_cap_set_supported_audio_chan_counts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaf6b2717823f9f3136237ed6a6515449e)
- [bt_audio_codec_cap_chan_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gae695b5d17359967703f2509db1671fa5)
- [bt_audio_codec_cap_get_octets_per_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaa949089f2c6c143041e6cb61338e0ddc)
- [bt_audio_codec_cap_set_octets_per_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gac1c42460cd3c55bbfbd467f84ab2d78d)
- [bt_audio_codec_cap_get_max_codec_frames_per_sdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga194d938896ee65601bdce96d68c84885)
- [bt_audio_codec_cap_set_max_codec_frames_per_sdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga3785bc41f56f8f2a09248396dadb31da)
- [bt_audio_codec_cap_meta_get_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga5c2ecbb4d0cef26dd2cc5d023e70a163)
- [bt_audio_codec_cap_meta_set_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga1fdfd8c36f4131bcf4ffd2b7f176b631)
- [bt_audio_codec_cap_meta_unset_val](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga40848f5375d1e58622c580112c282f2e)
- [bt_audio_codec_cap_meta_get_pref_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaaa8c6783241b1b70349354b3e36c696c)
- [bt_audio_codec_cap_meta_set_pref_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga7fe0d4553d6accf5c89645cbf86149bf)
- [bt_audio_codec_cap_meta_get_stream_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga88ee657b5bd3f847bb75c9620ddb142f)
- [bt_audio_codec_cap_meta_set_stream_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga5cc7f360049c38c8de631ea33dbc44ab)
- [bt_audio_codec_cap_meta_get_program_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga33725c3b2c06d6c22030bb5a77d702b0)
- [bt_audio_codec_cap_meta_set_program_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga43d2ec3a4d621c26843de82db7fd2189)
- [bt_audio_codec_cap_meta_get_lang](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gafb631b55b69b256c60b9cf3c7f418ff8)
- [bt_audio_codec_cap_meta_set_lang](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga555db1eff71a3bc79a5bcb959c0198cc)
- [bt_audio_codec_cap_meta_get_ccid_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga3095dea36e60e75cbfe786d3c2f11866)
- [bt_audio_codec_cap_meta_set_ccid_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga00a8ad22713dab761c81d1b8481c037d)
- [bt_audio_codec_cap_meta_get_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gab34d0369ce08efcd407d33956d32632e)
- [bt_audio_codec_cap_meta_set_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga5e267dfad978cd3d52be9c31a4fac0be)
- [bt_audio_codec_cap_meta_get_program_info_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gadb39b0ee1f65cdd2457fdf2c3142c040)
- [bt_audio_codec_cap_meta_set_program_info_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gafbb0d6282d989e8bc70caada2845b337)
- [bt_audio_codec_cap_meta_get_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga88bb1da63b7ea0f95dd236aa1024cfb8)
- [bt_audio_codec_cap_meta_set_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gacd3de0306a22d1a1d9ba09b4ac4f4e09)
- [bt_audio_codec_cap_meta_get_bcast_audio_immediate_rend_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gab4ccc7cb7d779acb20185ae808dd8bbe)
- [bt_audio_codec_cap_meta_set_bcast_audio_immediate_rend_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gaa1d382b4fa53f7cbe8426df53a3317ce)
- [bt_audio_codec_cap_meta_get_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga4f1ea56f2c1c21420f078d35081ceee5)
- [bt_audio_codec_cap_meta_set_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga3346db1f59cb35b9b9e5255424adb6e4)
- [bt_audio_codec_cap_meta_get_broadcast_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga3c8df3fe79f0bb96c4e15e7c2502bf89)
- [bt_audio_codec_cap_meta_set_broadcast_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga461add2808a1eca8993222d2b31d5a5f)
- [bt_audio_codec_cap_meta_get_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga69aecd7e98f90a5162ff8ea3373b43d4)
- [bt_audio_codec_cap_meta_set_extended](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gac00aabc7329027852a7caf5cdff2bc26)
- [bt_audio_codec_cap_meta_get_vendor](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gab8c80a0f55041f026d453fd88cdeb727)
- [bt_audio_codec_cap_meta_set_vendor](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga1f06789782541beab9aab4914f91bb57)
- [bt_audio_context_bit_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#ga26436fc678423ff1cf3543d381359d0f)
- [bt_audio_parental_rating_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#ga6926c4e8bda0874769177a903276c072)
- [bt_audio_active_state_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#ga1dd5865429e2438e0d4f88e891eda975)
- [bt_audio_codec_cap_freq_bit_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#gadd3bac4f1f1b334cb60f5783fdc15c14)
- [bt_audio_codec_cap_frame_dur_bit_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#ga6b9cc74dafcf03056862ae9823bce58d)
- [bt_audio_codec_cap_chan_count_bit_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#ga795742ed8d91e2b675fbcdaeee7a71ec)
- [bt_audio_location_bit_to_str](../api_audio_path_topic_reference/P001_分配编号转字符串 API（Assigned numbers to string API）.md#gaa1b9f7166fd6e6797da65d9537357324)

<a id="header-details"></a>

---

[上一章](P002_zephyr__acpi__acpi.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__bluetooth__mesh__cfg_cli.h_文件参考.md)
