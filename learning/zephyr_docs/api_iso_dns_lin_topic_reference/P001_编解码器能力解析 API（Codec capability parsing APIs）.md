---
id: learning.zephyr-docs.api-iso-dns-lin-topic-reference.page-1
title: 编解码器能力解析 API（Codec capability parsing APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_编解码器能力解析 API（Codec capability parsing APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音频编解码器能力 API（Audio codec capabilities APIs）

<a id="details"></a>

音频编解码器能力 API（Audio Codec Capabilities APIs）。用于解析长度－类型－值（LTV）格式的编解码器能力数据的函数，封装于编解码器能力解析 API 中。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.1\_函数（Functions）

<a id="r_gac3bf5dd414271bb1dcbc6590994cff6b"></a>

```c
int bt_audio_codec_cap_get_val (const struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_type type, const uint8_t **data)
```

相关声明：[bt_audio_codec_cap_get_val](#gac3bf5dd414271bb1dcbc6590994cff6b)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_cap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf58823a56eb36cfd22e582ab1ea3d015)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据类型查找指定值。

<a id="r_ga0c2c816b0b2b85aa5dd38f21caceea40"></a>

```c
int bt_audio_codec_cap_set_val (struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_type type, const uint8_t *data, size_t data_len)
```

相关声明：[bt_audio_codec_cap_set_val](#ga0c2c816b0b2b85aa5dd38f21caceea40)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_cap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf58823a56eb36cfd22e582ab1ea3d015)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置或添加指定的编解码器能力值（Codec Capability Value）。

<a id="r_gabc9962212ad65339ff02ba1389d5f9f8"></a>

```c
int bt_audio_codec_cap_unset_val (struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_type type)
```

相关声明：[bt_audio_codec_cap_unset_val](#gabc9962212ad65339ff02ba1389d5f9f8)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_cap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf58823a56eb36cfd22e582ab1ea3d015)。

取消设置指定的编解码器能力值（Codec Capability Value）。

<a id="r_gaa1dbf81c437c983af0144bf62433666c"></a>

```c
int bt_audio_codec_cap_get_freq (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_get_freq](#gaa1dbf81c437c983af0144bf62433666c)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

从编解码器能力（Codec Capability）中提取频率（Frequency）。

<a id="r_gac0655c0bd6552ab8a265076d7d0cd1b2"></a>

```c
int bt_audio_codec_cap_set_freq (struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_freq freq)
```

相关声明：[bt_audio_codec_cap_set_freq](#gac0655c0bd6552ab8a265076d7d0cd1b2)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_cap_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaafc1106d5d305874ee2f540c850ff5b4)。

设置编解码器能力（Codec Capability）中的支持的频率（Supported Frequencies）。

<a id="r_ga12336de7d908bda94427caee4dc080e0"></a>

```c
int bt_audio_codec_cap_get_frame_dur (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_get_frame_dur](#ga12336de7d908bda94427caee4dc080e0)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

从编解码器能力（Codec Capability）中提取帧时长（Frame Duration）。

<a id="r_ga53e5df6cc4cfbed12b59a6a506657772"></a>

```c
int bt_audio_codec_cap_set_frame_dur (struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_frame_dur frame_dur)
```

相关声明：[bt_audio_codec_cap_set_frame_dur](#ga53e5df6cc4cfbed12b59a6a506657772)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_cap_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf37e8e19f956afb3c3a413cbaa1a21f5)。

设置编解码器能力（Codec Capability）中的帧时长（Frame Duration）。

<a id="r_ga63d5e083f03ec06939ee1cd0355c8c2a"></a>

```c
int bt_audio_codec_cap_get_supported_audio_chan_counts (const struct bt_audio_codec_cap *codec_cap, bool fallback_to_default)
```

相关声明：[bt_audio_codec_cap_get_supported_audio_chan_counts](#ga63d5e083f03ec06939ee1cd0355c8c2a)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

从编解码器能力（Codec Capability）中提取支持的音频声道数量（Audio Channel Counts）。

<a id="r_gaf6b2717823f9f3136237ed6a6515449e"></a>

```c
int bt_audio_codec_cap_set_supported_audio_chan_counts (struct bt_audio_codec_cap *codec_cap, enum bt_audio_codec_cap_chan_count chan_count)
```

相关声明：[bt_audio_codec_cap_set_supported_audio_chan_counts](#gaf6b2717823f9f3136237ed6a6515449e)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_cap_chan_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gae695b5d17359967703f2509db1671fa5)。

设置编解码器能力（Codec Capability）中的声道数量（Channel Count）。

<a id="r_gaa949089f2c6c143041e6cb61338e0ddc"></a>

```c
int bt_audio_codec_cap_get_octets_per_frame (const struct bt_audio_codec_cap *codec_cap, struct bt_audio_codec_octets_per_codec_frame *codec_frame)
```

相关声明：[bt_audio_codec_cap_get_octets_per_frame](#gaa949089f2c6c143041e6cb61338e0ddc)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_octets_per_codec_frame](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md)。

从编解码器能力（Codec Capability）中提取支持的每个编解码器帧的八位组数（Octets per Codec Frame）。

<a id="r_gac1c42460cd3c55bbfbd467f84ab2d78d"></a>

```c
int bt_audio_codec_cap_set_octets_per_frame (struct bt_audio_codec_cap *codec_cap, const struct bt_audio_codec_octets_per_codec_frame *codec_frame)
```

相关声明：[bt_audio_codec_cap_set_octets_per_frame](#gac1c42460cd3c55bbfbd467f84ab2d78d)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_codec_octets_per_codec_frame](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md)。

设置编解码器能力（Codec Capability）中的每个编解码器帧的八位组数（Octets per Codec Frame）。

<a id="r_ga194d938896ee65601bdce96d68c84885"></a>

```c
int bt_audio_codec_cap_get_max_codec_frames_per_sdu (const struct bt_audio_codec_cap *codec_cap, bool fallback_to_default)
```

相关声明：[bt_audio_codec_cap_get_max_codec_frames_per_sdu](#ga194d938896ee65601bdce96d68c84885)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

从编解码器能力（Codec Capability）中提取每个服务数据单元（SDU）的最大编解码器帧数。

<a id="r_ga3785bc41f56f8f2a09248396dadb31da"></a>

```c
int bt_audio_codec_cap_set_max_codec_frames_per_sdu (struct bt_audio_codec_cap *codec_cap, uint8_t codec_frames_per_sdu)
```

相关声明：[bt_audio_codec_cap_set_max_codec_frames_per_sdu](#ga3785bc41f56f8f2a09248396dadb31da)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力（Codec Capability）中的每个服务数据单元的最大编解码器帧数（Maximum Codec Frames per SDU）。

<a id="r_ga5c2ecbb4d0cef26dd2cc5d023e70a163"></a>

```c
int bt_audio_codec_cap_meta_get_val (const struct bt_audio_codec_cap *codec_cap, uint8_t type, const uint8_t **data)
```

相关声明：[bt_audio_codec_cap_meta_get_val](#ga5c2ecbb4d0cef26dd2cc5d023e70a163)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据类型查找指定的元数据值（Metadata Value）。

<a id="r_ga1fdfd8c36f4131bcf4ffd2b7f176b631"></a>

```c
int bt_audio_codec_cap_meta_set_val (struct bt_audio_codec_cap *codec_cap, enum bt_audio_metadata_type type, const uint8_t *data, size_t data_len)
```

相关声明：[bt_audio_codec_cap_meta_set_val](#ga1fdfd8c36f4131bcf4ffd2b7f176b631)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置或添加指定的编解码器能力元数据值（Codec Capability Metadata Value）。

<a id="r_ga40848f5375d1e58622c580112c282f2e"></a>

```c
int bt_audio_codec_cap_meta_unset_val (struct bt_audio_codec_cap *codec_cap, enum bt_audio_metadata_type type)
```

相关声明：[bt_audio_codec_cap_meta_unset_val](#ga40848f5375d1e58622c580112c282f2e)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)。

取消设置指定的编解码器能力元数据值（Codec Capability Metadata Value）。

<a id="r_gaaa8c6783241b1b70349354b3e36c696c"></a>

```c
int bt_audio_codec_cap_meta_get_pref_context (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_get_pref_context](#gaaa8c6783241b1b70349354b3e36c696c)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

提取首选上下文（Preferred Contexts）。

<a id="r_ga7fe0d4553d6accf5c89645cbf86149bf"></a>

```c
int bt_audio_codec_cap_meta_set_pref_context (struct bt_audio_codec_cap *codec_cap, enum bt_audio_context ctx)
```

相关声明：[bt_audio_codec_cap_meta_set_pref_context](#ga7fe0d4553d6accf5c89645cbf86149bf)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置编解码器能力元数据（Codec Capability Metadata）中的首选上下文（Preferred Context）。

<a id="r_ga88ee657b5bd3f847bb75c9620ddb142f"></a>

```c
int bt_audio_codec_cap_meta_get_stream_context (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_get_stream_context](#ga88ee657b5bd3f847bb75c9620ddb142f)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

提取流上下文（Stream Contexts）。

<a id="r_ga5cc7f360049c38c8de631ea33dbc44ab"></a>

```c
int bt_audio_codec_cap_meta_set_stream_context (struct bt_audio_codec_cap *codec_cap, enum bt_audio_context ctx)
```

相关声明：[bt_audio_codec_cap_meta_set_stream_context](#ga5cc7f360049c38c8de631ea33dbc44ab)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置编解码器能力元数据（Codec Capability Metadata）中的流上下文（Stream Context）。

<a id="r_ga33725c3b2c06d6c22030bb5a77d702b0"></a>

```c
int bt_audio_codec_cap_meta_get_program_info (const struct bt_audio_codec_cap *codec_cap, const uint8_t **program_info)
```

相关声明：[bt_audio_codec_cap_meta_get_program_info](#ga33725c3b2c06d6c22030bb5a77d702b0)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取节目信息（Program Info）。

<a id="r_ga43d2ec3a4d621c26843de82db7fd2189"></a>

```c
int bt_audio_codec_cap_meta_set_program_info (struct bt_audio_codec_cap *codec_cap, const uint8_t *program_info, size_t program_info_len)
```

相关声明：[bt_audio_codec_cap_meta_set_program_info](#ga43d2ec3a4d621c26843de82db7fd2189)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的节目信息（Program Info）。

<a id="r_gafb631b55b69b256c60b9cf3c7f418ff8"></a>

```c
int bt_audio_codec_cap_meta_get_lang (const struct bt_audio_codec_cap *codec_cap, const uint8_t **lang)
```

相关声明：[bt_audio_codec_cap_meta_get_lang](#gafb631b55b69b256c60b9cf3c7f418ff8)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取语言（Language）。

<a id="r_ga555db1eff71a3bc79a5bcb959c0198cc"></a>

```c
int bt_audio_codec_cap_meta_set_lang (struct bt_audio_codec_cap *codec_cap, const uint8_t lang[3U])
```

相关声明：[bt_audio_codec_cap_meta_set_lang](#ga555db1eff71a3bc79a5bcb959c0198cc)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的语言（Language）。

<a id="r_ga3095dea36e60e75cbfe786d3c2f11866"></a>

```c
int bt_audio_codec_cap_meta_get_ccid_list (const struct bt_audio_codec_cap *codec_cap, const uint8_t **ccid_list)
```

相关声明：[bt_audio_codec_cap_meta_get_ccid_list](#ga3095dea36e60e75cbfe786d3c2f11866)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取内容控制标识符列表（CCID List）。

<a id="r_ga00a8ad22713dab761c81d1b8481c037d"></a>

```c
int bt_audio_codec_cap_meta_set_ccid_list (struct bt_audio_codec_cap *codec_cap, const uint8_t *ccid_list, size_t ccid_list_len)
```

相关声明：[bt_audio_codec_cap_meta_set_ccid_list](#ga00a8ad22713dab761c81d1b8481c037d)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的内容控制标识符列表（CCID List）。

<a id="r_gab34d0369ce08efcd407d33956d32632e"></a>

```c
int bt_audio_codec_cap_meta_get_parental_rating (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_get_parental_rating](#gab34d0369ce08efcd407d33956d32632e)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

提取家长分级（Parental Rating）。

<a id="r_ga5e267dfad978cd3d52be9c31a4fac0be"></a>

```c
int bt_audio_codec_cap_meta_set_parental_rating (struct bt_audio_codec_cap *codec_cap, enum bt_audio_parental_rating parental_rating)
```

相关声明：[bt_audio_codec_cap_meta_set_parental_rating](#ga5e267dfad978cd3d52be9c31a4fac0be)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga6d4aff1f93dc0b902e4b5d1355f15760)。

设置编解码器能力元数据（Codec Capability Metadata）中的家长分级（Parental Rating）。

<a id="r_gadb39b0ee1f65cdd2457fdf2c3142c040"></a>

```c
int bt_audio_codec_cap_meta_get_program_info_uri (const struct bt_audio_codec_cap *codec_cap, const uint8_t **program_info_uri)
```

相关声明：[bt_audio_codec_cap_meta_get_program_info_uri](#gadb39b0ee1f65cdd2457fdf2c3142c040)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取节目信息 URI（Program Info URI）。

<a id="r_gafbb0d6282d989e8bc70caada2845b337"></a>

```c
int bt_audio_codec_cap_meta_set_program_info_uri (struct bt_audio_codec_cap *codec_cap, const uint8_t *program_info_uri, size_t program_info_uri_len)
```

相关声明：[bt_audio_codec_cap_meta_set_program_info_uri](#gafbb0d6282d989e8bc70caada2845b337)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的节目信息 URI（Program Info URI）。

<a id="r_ga88bb1da63b7ea0f95dd236aa1024cfb8"></a>

```c
int bt_audio_codec_cap_meta_get_audio_active_state (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_get_audio_active_state](#ga88bb1da63b7ea0f95dd236aa1024cfb8)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

提取音频活动状态（Audio Active State）。

<a id="r_gacd3de0306a22d1a1d9ba09b4ac4f4e09"></a>

```c
int bt_audio_codec_cap_meta_set_audio_active_state (struct bt_audio_codec_cap *codec_cap, enum bt_audio_active_state state)
```

相关声明：[bt_audio_codec_cap_meta_set_audio_active_state](#gacd3de0306a22d1a1d9ba09b4ac4f4e09)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga16d403ec4db7be997682331ad365ff5f)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置编解码器能力元数据（Codec Capability Metadata）中的音频活动状态（Audio Active State）。

<a id="r_gab4ccc7cb7d779acb20185ae808dd8bbe"></a>

```c
int bt_audio_codec_cap_meta_get_bcast_audio_immediate_rend_flag (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_get_bcast_audio_immediate_rend_flag](#gab4ccc7cb7d779acb20185ae808dd8bbe)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

提取广播音频立即呈现标志（Broadcast Audio Immediate Rendering Flag）。

<a id="r_gaa1d382b4fa53f7cbe8426df53a3317ce"></a>

```c
int bt_audio_codec_cap_meta_set_bcast_audio_immediate_rend_flag (struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_set_bcast_audio_immediate_rend_flag](#gaa1d382b4fa53f7cbe8426df53a3317ce)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

设置编解码器能力元数据（Codec Capability Metadata）中的广播音频立即呈现标志（Broadcast Audio Immediate Rendering Flag）。

<a id="r_ga4f1ea56f2c1c21420f078d35081ceee5"></a>

```c
int bt_audio_codec_cap_meta_get_assisted_listening_stream (const struct bt_audio_codec_cap *codec_cap)
```

相关声明：[bt_audio_codec_cap_meta_get_assisted_listening_stream](#ga4f1ea56f2c1c21420f078d35081ceee5)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)。

提取辅助收听流（Assisted Listening Stream）。

<a id="r_ga3346db1f59cb35b9b9e5255424adb6e4"></a>

```c
int bt_audio_codec_cap_meta_set_assisted_listening_stream (struct bt_audio_codec_cap *codec_cap, enum bt_audio_assisted_listening_stream val)
```

相关声明：[bt_audio_codec_cap_meta_set_assisted_listening_stream](#ga3346db1f59cb35b9b9e5255424adb6e4)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[bt_audio_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga207fbf0fbca9b24cba02c7f1d184e7f5)。

设置编解码器能力元数据（Codec Capability Metadata）中的辅助收听流值（Assisted Listening Stream Value）。

<a id="r_ga3c8df3fe79f0bb96c4e15e7c2502bf89"></a>

```c
int bt_audio_codec_cap_meta_get_broadcast_name (const struct bt_audio_codec_cap *codec_cap, const uint8_t **broadcast_name)
```

相关声明：[bt_audio_codec_cap_meta_get_broadcast_name](#ga3c8df3fe79f0bb96c4e15e7c2502bf89)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取广播名称（Broadcast Name）。

<a id="r_ga461add2808a1eca8993222d2b31d5a5f"></a>

```c
int bt_audio_codec_cap_meta_set_broadcast_name (struct bt_audio_codec_cap *codec_cap, const uint8_t *broadcast_name, size_t broadcast_name_len)
```

相关声明：[bt_audio_codec_cap_meta_set_broadcast_name](#ga461add2808a1eca8993222d2b31d5a5f)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的广播名称（Broadcast Name）。

<a id="r_ga69aecd7e98f90a5162ff8ea3373b43d4"></a>

```c
int bt_audio_codec_cap_meta_get_extended (const struct bt_audio_codec_cap *codec_cap, const uint8_t **extended_meta)
```

相关声明：[bt_audio_codec_cap_meta_get_extended](#ga69aecd7e98f90a5162ff8ea3373b43d4)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取扩展元数据（Extended Metadata）。

<a id="r_gac00aabc7329027852a7caf5cdff2bc26"></a>

```c
int bt_audio_codec_cap_meta_set_extended (struct bt_audio_codec_cap *codec_cap, const uint8_t *extended_meta, size_t extended_meta_len)
```

相关声明：[bt_audio_codec_cap_meta_set_extended](#gac00aabc7329027852a7caf5cdff2bc26)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的扩展元数据（Extended Metadata）。

<a id="r_gab8c80a0f55041f026d453fd88cdeb727"></a>

```c
int bt_audio_codec_cap_meta_get_vendor (const struct bt_audio_codec_cap *codec_cap, const uint8_t **vendor_meta)
```

相关声明：[bt_audio_codec_cap_meta_get_vendor](#gab8c80a0f55041f026d453fd88cdeb727)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取厂商特定元数据（Vendor Specific Metadata）。

<a id="r_ga1f06789782541beab9aab4914f91bb57"></a>

```c
int bt_audio_codec_cap_meta_set_vendor (struct bt_audio_codec_cap *codec_cap, const uint8_t *vendor_meta, size_t vendor_meta_len)
```

相关声明：[bt_audio_codec_cap_meta_set_vendor](#ga1f06789782541beab9aab4914f91bb57)、[bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器能力元数据（Codec Capability Metadata）中的厂商特定元数据（Vendor Specific Metadata）。

## 1.2\_详细说明（Detailed Documentation）

<a id="ga12336de7d908bda94427caee4dc080e0"></a>

### `bt_audio_codec_cap_get_frame_dur()`

```c
int bt_audio_codec_cap_get_frame_dur ( const struct bt_audio_codec_cap * codec_cap)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

从编解码器能力（Codec Capability）中提取帧时长（Frame Duration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要从中提取数据的编解码器能力（Codec Capabilities）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `durations` | 返回值为 0 或正数时，表示所支持帧时长（Frame Duration）的位域。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值具有无效的大小或取值。 |

<a id="gaa1dbf81c437c983af0144bf62433666c"></a>

### `bt_audio_codec_cap_get_freq()`

```c
int bt_audio_codec_cap_get_freq ( const struct bt_audio_codec_cap * codec_cap)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

从编解码器能力（Codec Capability）中提取频率（Frequency）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要从中提取数据的编解码器能力（Codec Capabilities）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `frequencies` | 返回值为 0 或正数时，表示所支持频率（bt_audio_codec_cap_freq）的位域。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值具有无效的大小或取值。 |

<a id="ga194d938896ee65601bdce96d68c84885"></a>

### `bt_audio_codec_cap_get_max_codec_frames_per_sdu()`

```c
int bt_audio_codec_cap_get_max_codec_frames_per_sdu ( const struct bt_audio_codec_cap * codec_cap, bool fallback_to_default )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

从编解码器能力（Codec Capability）中提取每个服务数据单元（SDU）的最大编解码器帧数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要从中提取数据的编解码器能力（Codec Capabilities）。 |
| `fallback_to_default` | 若为 true，当 codec_cap.id 为 BT_HCI_CODING_FORMAT_LC3 且未找到该类型时，此函数将提供默认值 1。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_frames_per_sdu` | 每个服务数据单元（SDU）支持的编解码器帧数上限。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值具有无效的大小或取值。 |

<a id="gaa949089f2c6c143041e6cb61338e0ddc"></a>

### `bt_audio_codec_cap_get_octets_per_frame()`

```c
int bt_audio_codec_cap_get_octets_per_frame ( const struct bt_audio_codec_cap * codec_cap, struct bt_audio_codec_octets_per_codec_frame * codec_frame )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

从编解码器能力（Codec Capability）中提取支持的每个编解码器帧的八位组数（Octets per Codec Frame）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cap` | 要从中提取数据的编解码器能力（Codec Capabilities）。 |
| `[out] codec_frame` | 用于存放结果值的结构体（Struct）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值具有无效的大小或取值。 |

<a id="ga63d5e083f03ec06939ee1cd0355c8c2a"></a>

### `bt_audio_codec_cap_get_supported_audio_chan_counts()`

```c
int bt_audio_codec_cap_get_supported_audio_chan_counts ( const struct bt_audio_codec_cap * codec_cap, bool fallback_to_default )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

从编解码器能力（Codec Capability）中提取支持的音频声道数量（Audio Channel Counts）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要从中提取数据的编解码器能力（Codec Capabilities）。 |
| `fallback_to_default` | 若为 true，当 codec_cap.id 为 BT_HCI_CODING_FORMAT_LC3 且未找到该类型时，此函数将提供默认值 1。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel_counts` | 返回值为 0 或正数时，表示支持的声道数（Channel Count）的数量。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值具有无效的大小或取值。 |

<a id="gac3bf5dd414271bb1dcbc6590994cff6b"></a>

### `bt_audio_codec_cap_get_val()`

```c
int bt_audio_codec_cap_get_val ( const struct bt_audio_codec_cap * codec_cap, enum bt_audio_codec_cap_type type, const uint8_t ** data )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

根据类型查找指定值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[in] type` | 要查找的类型 ID（Type ID）。 |
| `[out] data` | 指向数据指针的指针；找到条目时更新该数据指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | 找到的数据长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="ga4f1ea56f2c1c21420f078d35081ceee5"></a>

### `bt_audio_codec_cap_meta_get_assisted_listening_stream()`

```c
int bt_audio_codec_cap_meta_get_assisted_listening_stream ( const struct bt_audio_codec_cap * codec_cap)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取辅助收听流（Assisted Listening Stream）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_ASSISTED_LISTENING_STREAM`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `value` | 返回值为正数或 0 时，表示辅助聆听流（Assisted Listening Stream）的值。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值大小无效。 |

<a id="ga88bb1da63b7ea0f95dd236aa1024cfb8"></a>

### `bt_audio_codec_cap_meta_get_audio_active_state()`

```c
int bt_audio_codec_cap_meta_get_audio_active_state ( const struct bt_audio_codec_cap * codec_cap)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取音频活动状态（Audio Active State）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_AUDIO_STATE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 返回值为正数或 0 时，表示首选上下文类型（Preferred Context Type）。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值大小无效。 |

<a id="gab4ccc7cb7d779acb20185ae808dd8bbe"></a>

### `bt_audio_codec_cap_meta_get_bcast_audio_immediate_rend_flag()`

```c
int bt_audio_codec_cap_meta_get_bcast_audio_immediate_rend_flag ( const struct bt_audio_codec_cap * codec_cap)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取广播音频立即呈现标志（Broadcast Audio Immediate Rendering Flag）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 找到了该标志（Flag）。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到该标志（Flag）。 |

<a id="ga3c8df3fe79f0bb96c4e15e7c2502bf89"></a>

### `bt_audio_codec_cap_meta_get_broadcast_name()`

```c
int bt_audio_codec_cap_meta_get_broadcast_name ( const struct bt_audio_codec_cap * codec_cap, const uint8_t ** broadcast_name )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取广播名称（Broadcast Name）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_BROADCAST_NAME`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] broadcast_name` | 指向 UTF-8 格式广播名称（Broadcast Name）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `length` | broadcast_name 的长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="ga3095dea36e60e75cbfe786d3c2f11866"></a>

### `bt_audio_codec_cap_meta_get_ccid_list()`

```c
int bt_audio_codec_cap_meta_get_ccid_list ( const struct bt_audio_codec_cap * codec_cap, const uint8_t ** ccid_list )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取内容控制标识符列表（CCID List）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_CCID_LIST`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] ccid_list` | 指向包含 8 位内容控制标识符（CCID）的数组的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | ccid_list 的长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="ga69aecd7e98f90a5162ff8ea3373b43d4"></a>

### `bt_audio_codec_cap_meta_get_extended()`

```c
int bt_audio_codec_cap_meta_get_extended ( const struct bt_audio_codec_cap * codec_cap, const uint8_t ** extended_meta )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取扩展元数据（Extended Metadata）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_EXTENDED`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] extended_meta` | 指向扩展元数据（Extended Metadata）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | extended_meta 的长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="gafb631b55b69b256c60b9cf3c7f418ff8"></a>

### `bt_audio_codec_cap_meta_get_lang()`

```c
int bt_audio_codec_cap_meta_get_lang ( const struct bt_audio_codec_cap * codec_cap, const uint8_t ** lang )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取语言（Language）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_LANG`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] lang` | 指向语言字节（Language Bytes）的指针，长度为 BT_AUDIO_LANG_SIZE。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值大小无效。 |

<a id="gab34d0369ce08efcd407d33956d32632e"></a>

### `bt_audio_codec_cap_meta_get_parental_rating()`

```c
int bt_audio_codec_cap_meta_get_parental_rating ( const struct bt_audio_codec_cap * codec_cap)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取家长分级（Parental Rating）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_PARENTAL_RATING`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `The` | 返回值为正数或 0 时，表示家长分级（Parental Rating）。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值大小无效。 |

<a id="gaaa8c6783241b1b70349354b3e36c696c"></a>

### `bt_audio_codec_cap_meta_get_pref_context()`

```c
int bt_audio_codec_cap_meta_get_pref_context ( const struct bt_audio_codec_cap * codec_cap)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取首选上下文（Preferred Contexts）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_PREF_CONTEXT`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `The` | 返回值为正数或 0 时，表示首选上下文类型（Preferred Context Type）。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值大小无效。 |

<a id="ga33725c3b2c06d6c22030bb5a77d702b0"></a>

### `bt_audio_codec_cap_meta_get_program_info()`

```c
int bt_audio_codec_cap_meta_get_program_info ( const struct bt_audio_codec_cap * codec_cap, const uint8_t ** program_info )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取节目信息（Program Info）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_PROGRAM_INFO`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] program_info` | 指向 UTF-8 格式节目信息（Program Info）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | program_info 的长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="gadb39b0ee1f65cdd2457fdf2c3142c040"></a>

### `bt_audio_codec_cap_meta_get_program_info_uri()`

```c
int bt_audio_codec_cap_meta_get_program_info_uri ( const struct bt_audio_codec_cap * codec_cap, const uint8_t ** program_info_uri )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取节目信息 URI（Program Info URI）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] program_info_uri` | 指向 UTF-8 格式节目信息 URI（Program Info URI）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | program_info_uri 的长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="ga88ee657b5bd3f847bb75c9620ddb142f"></a>

### `bt_audio_codec_cap_meta_get_stream_context()`

```c
int bt_audio_codec_cap_meta_get_stream_context ( const struct bt_audio_codec_cap * codec_cap)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取流上下文（Stream Contexts）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 返回值为正数或 0 时，表示流上下文类型（Stream Context Type）。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值大小无效。 |

<a id="ga5c2ecbb4d0cef26dd2cc5d023e70a163"></a>

### `bt_audio_codec_cap_meta_get_val()`

```c
int bt_audio_codec_cap_meta_get_val ( const struct bt_audio_codec_cap * codec_cap, uint8_t type, const uint8_t ** data )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

根据类型查找指定的元数据值（Metadata Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[in] type` | 要查找的类型 ID（Type ID）。 |
| `[out] data` | 指向数据指针的指针；找到条目时更新该数据指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | 找到的数据长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="gab8c80a0f55041f026d453fd88cdeb727"></a>

### `bt_audio_codec_cap_meta_get_vendor()`

```c
int bt_audio_codec_cap_meta_get_vendor ( const struct bt_audio_codec_cap * codec_cap, const uint8_t ** vendor_meta )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取厂商特定元数据（Vendor Specific Metadata）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_VENDOR`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cap` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] vendor_meta` | 指向厂商专用元数据（Vendor Specific Metadata）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | vendor_meta 的长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="ga3346db1f59cb35b9b9e5255424adb6e4"></a>

### `bt_audio_codec_cap_meta_set_assisted_listening_stream()`

```c
int bt_audio_codec_cap_meta_set_assisted_listening_stream ( struct bt_audio_codec_cap * codec_cap, enum bt_audio_assisted_listening_stream val )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的辅助收听流值（Assisted Listening Stream Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |
| `val` | 要设置的辅助聆听流（Assisted Listening Stream）的值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gacd3de0306a22d1a1d9ba09b4ac4f4e09"></a>

### `bt_audio_codec_cap_meta_set_audio_active_state()`

```c
int bt_audio_codec_cap_meta_set_audio_active_state ( struct bt_audio_codec_cap * codec_cap, enum bt_audio_active_state state )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的音频活动状态（Audio Active State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |
| `state` | 要设置的音频活动状态（Audio Active State）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gaa1d382b4fa53f7cbe8426df53a3317ce"></a>

### `bt_audio_codec_cap_meta_set_bcast_audio_immediate_rend_flag()`

```c
int bt_audio_codec_cap_meta_set_bcast_audio_immediate_rend_flag ( struct bt_audio_codec_cap * codec_cap)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的广播音频立即呈现标志（Broadcast Audio Immediate Rendering Flag）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga461add2808a1eca8993222d2b31d5a5f"></a>

### `bt_audio_codec_cap_meta_set_broadcast_name()`

```c
int bt_audio_codec_cap_meta_set_broadcast_name ( struct bt_audio_codec_cap * codec_cap, const uint8_t * broadcast_name, size_t broadcast_name_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的广播名称（Broadcast Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |
| `broadcast_name` | 要设置的广播名称（Broadcast Name）。字符数须介于 BT_AUDIO_BROADCAST_NAME_CHAR_MIN 和 BT_AUDIO_BROADCAST_NAME_CHAR_MAX 之间。 |
| `broadcast_name_len` | broadcast_name 的长度。须介于 BT_AUDIO_BROADCAST_NAME_LEN_MIN 和 BT_AUDIO_BROADCAST_NAME_LEN_MAX 之间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga00a8ad22713dab761c81d1b8481c037d"></a>

### `bt_audio_codec_cap_meta_set_ccid_list()`

```c
int bt_audio_codec_cap_meta_set_ccid_list ( struct bt_audio_codec_cap * codec_cap, const uint8_t * ccid_list, size_t ccid_list_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的内容控制标识符列表（CCID List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |
| `ccid_list` | 要设置的节目信息（Program Info）。 |
| `ccid_list_len` | ccid_list 的长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gac00aabc7329027852a7caf5cdff2bc26"></a>

### `bt_audio_codec_cap_meta_set_extended()`

```c
int bt_audio_codec_cap_meta_set_extended ( struct bt_audio_codec_cap * codec_cap, const uint8_t * extended_meta, size_t extended_meta_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的扩展元数据（Extended Metadata）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |
| `extended_meta` | 要设置的扩展元数据（Extended Metadata）。 |
| `extended_meta_len` | extended_meta 的长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga555db1eff71a3bc79a5bcb959c0198cc"></a>

### `bt_audio_codec_cap_meta_set_lang()`

```c
int bt_audio_codec_cap_meta_set_lang ( struct bt_audio_codec_cap * codec_cap, const uint8_t lang[3U] )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的语言（Language）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |
| `lang` | 要设置的 24 位语言（Language）值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga5e267dfad978cd3d52be9c31a4fac0be"></a>

### `bt_audio_codec_cap_meta_set_parental_rating()`

```c
int bt_audio_codec_cap_meta_set_parental_rating ( struct bt_audio_codec_cap * codec_cap, enum bt_audio_parental_rating parental_rating )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的家长分级（Parental Rating）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |
| `parental_rating` | 要设置的家长分级（Parental Rating）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga7fe0d4553d6accf5c89645cbf86149bf"></a>

### `bt_audio_codec_cap_meta_set_pref_context()`

```c
int bt_audio_codec_cap_meta_set_pref_context ( struct bt_audio_codec_cap * codec_cap, enum bt_audio_context ctx )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的首选上下文（Preferred Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |
| `ctx` | 要设置的首选上下文（Preferred Context）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga43d2ec3a4d621c26843de82db7fd2189"></a>

### `bt_audio_codec_cap_meta_set_program_info()`

```c
int bt_audio_codec_cap_meta_set_program_info ( struct bt_audio_codec_cap * codec_cap, const uint8_t * program_info, size_t program_info_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的节目信息（Program Info）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |
| `program_info` | 要设置的节目信息（Program Info）。 |
| `program_info_len` | program_info 的长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gafbb0d6282d989e8bc70caada2845b337"></a>

### `bt_audio_codec_cap_meta_set_program_info_uri()`

```c
int bt_audio_codec_cap_meta_set_program_info_uri ( struct bt_audio_codec_cap * codec_cap, const uint8_t * program_info_uri, size_t program_info_uri_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的节目信息 URI（Program Info URI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |
| `program_info_uri` | 要设置的节目信息 URI（Program Info URI）。 |
| `program_info_uri_len` | program_info_uri 的长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga5cc7f360049c38c8de631ea33dbc44ab"></a>

### `bt_audio_codec_cap_meta_set_stream_context()`

```c
int bt_audio_codec_cap_meta_set_stream_context ( struct bt_audio_codec_cap * codec_cap, enum bt_audio_context ctx )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的流上下文（Stream Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |
| `ctx` | 要设置的流上下文（Stream Context）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga1fdfd8c36f4131bcf4ffd2b7f176b631"></a>

### `bt_audio_codec_cap_meta_set_val()`

```c
int bt_audio_codec_cap_meta_set_val ( struct bt_audio_codec_cap * codec_cap, enum bt_audio_metadata_type type, const uint8_t * data, size_t data_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置或添加指定的编解码器能力元数据值（Codec Capability Metadata Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要在其中设置值的编解码器能力（Codec Capability）。 |
| `type` | 要设置的类型 ID（Type ID）。 |
| `data` | 指向要设置的数据指针的指针。 |
| `data_len` | 数据长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `meta_len` | 成功时返回 codec_cap.meta_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga1f06789782541beab9aab4914f91bb57"></a>

### `bt_audio_codec_cap_meta_set_vendor()`

```c
int bt_audio_codec_cap_meta_set_vendor ( struct bt_audio_codec_cap * codec_cap, const uint8_t * vendor_meta, size_t vendor_meta_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力元数据（Codec Capability Metadata）中的厂商特定元数据（Vendor Specific Metadata）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capability）。 |
| `vendor_meta` | 要设置的厂商专用元数据（Vendor Specific Metadata）。 |
| `vendor_meta_len` | vendor_meta 的长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga40848f5375d1e58622c580112c282f2e"></a>

### `bt_audio_codec_cap_meta_unset_val()`

```c
int bt_audio_codec_cap_meta_unset_val ( struct bt_audio_codec_cap * codec_cap, enum bt_audio_metadata_type type )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

取消设置指定的编解码器能力元数据值（Codec Capability Metadata Value）。

将从编解码器能力元数据（Codec Capability Metadata）中移除该类型及其值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要在其中设置值的编解码器数据（Codec Data）。 |
| `type` | 要取消设置的类型 ID（Type ID）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `meta_len` | 成功时返回 codec_cap.meta_len。（原文 “The of codec_cap.meta_len” 存在措辞缺漏。） |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |

<a id="ga53e5df6cc4cfbed12b59a6a506657772"></a>

### `bt_audio_codec_cap_set_frame_dur()`

```c
int bt_audio_codec_cap_set_frame_dur ( struct bt_audio_codec_cap * codec_cap, enum bt_audio_codec_cap_frame_dur frame_dur )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力（Codec Capability）中的帧时长（Frame Duration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capabilities）。 |
| `frame_dur` | 要设置的帧时长（Frame Duration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gac0655c0bd6552ab8a265076d7d0cd1b2"></a>

### `bt_audio_codec_cap_set_freq()`

```c
int bt_audio_codec_cap_set_freq ( struct bt_audio_codec_cap * codec_cap, enum bt_audio_codec_cap_freq freq )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力（Codec Capability）中的支持的频率（Supported Frequencies）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capabilities）。 |
| `freq` | 要设置的支持频率（Supported Frequencies）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga3785bc41f56f8f2a09248396dadb31da"></a>

### `bt_audio_codec_cap_set_max_codec_frames_per_sdu()`

```c
int bt_audio_codec_cap_set_max_codec_frames_per_sdu ( struct bt_audio_codec_cap * codec_cap, uint8_t codec_frames_per_sdu )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力（Codec Capability）中的每个服务数据单元的最大编解码器帧数（Maximum Codec Frames per SDU）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capabilities）。 |
| `codec_frames_per_sdu` | 要设置的每个 SDU 的编解码器帧数上限（Maximum Codec Frames per SDU）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gac1c42460cd3c55bbfbd467f84ab2d78d"></a>

### `bt_audio_codec_cap_set_octets_per_frame()`

```c
int bt_audio_codec_cap_set_octets_per_frame ( struct bt_audio_codec_cap * codec_cap, const struct bt_audio_codec_octets_per_codec_frame * codec_frame )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力（Codec Capability）中的每个编解码器帧的八位组数（Octets per Codec Frame）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capabilities）。 |
| `codec_frame` | 要设置的每个编解码器帧的八位字节数（Octets per Codec Frame）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gaf6b2717823f9f3136237ed6a6515449e"></a>

### `bt_audio_codec_cap_set_supported_audio_chan_counts()`

```c
int bt_audio_codec_cap_set_supported_audio_chan_counts ( struct bt_audio_codec_cap * codec_cap, enum bt_audio_codec_cap_chan_count chan_count )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器能力（Codec Capability）中的声道数量（Channel Count）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要为其设置数据的编解码器能力（Codec Capabilities）。 |
| `chan_count` | 要设置的声道数频率（Channel Count Frequency，原文用语）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga0c2c816b0b2b85aa5dd38f21caceea40"></a>

### `bt_audio_codec_cap_set_val()`

```c
int bt_audio_codec_cap_set_val ( struct bt_audio_codec_cap * codec_cap, enum bt_audio_codec_cap_type type, const uint8_t * data, size_t data_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置或添加指定的编解码器能力值（Codec Capability Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要在其中设置值的编解码器数据（Codec Data）。 |
| `type` | 要设置的类型 ID（Type ID）。 |
| `data` | 指向要设置的数据指针的指针。 |
| `data_len` | 数据长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gabc9962212ad65339ff02ba1389d5f9f8"></a>

### `bt_audio_codec_cap_unset_val()`

```c
int bt_audio_codec_cap_unset_val ( struct bt_audio_codec_cap * codec_cap, enum bt_audio_codec_cap_type type )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

取消设置指定的编解码器能力值（Codec Capability Value）。

将从编解码器能力（Codec Capability）中移除该类型及其值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cap` | 要在其中设置值的编解码器数据（Codec Data）。 |
| `type` | 要取消设置的类型 ID（Type ID）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |


## 1.3\_原页交叉引用（Cross References）

- [bt_audio_codec_cap](../bluetooth_le_audio_model_reference/P007_bt_audio_codec_cap_结构体.md)
- [bt_audio_codec_cap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf58823a56eb36cfd22e582ab1ea3d015)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_audio_codec_cap_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaafc1106d5d305874ee2f540c850ff5b4)
- [bt_audio_codec_cap_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaf37e8e19f956afb3c3a413cbaa1a21f5)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_audio_codec_cap_chan_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gae695b5d17359967703f2509db1671fa5)
- [bt_audio_codec_octets_per_codec_frame](../bluetooth_le_audio_model_reference/P009_bt_audio_codec_octets_per_codec_frame_结构体.md)
- [bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)
- [bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)
- [bt_audio_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga6d4aff1f93dc0b902e4b5d1355f15760)
- [bt_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga16d403ec4db7be997682331ad365ff5f)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_audio_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga207fbf0fbca9b24cba02c7f1d184e7f5)
- [编解码器能力解析 API（Codec capability parsing APIs）](P001_编解码器能力解析 API（Codec capability parsing APIs）.md)
- [zephyr/bluetooth/audio/audio.h](../api_file_mesh_acpi_reference/P003_zephyr__bluetooth__audio__audio.h_文件参考.md)
- [BT_HCI_CODING_FORMAT_LC3](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a1fa62d6f28ef56ebe9c18d5ab86fbf8e)
- [BT_AUDIO_METADATA_TYPE_ASSISTED_LISTENING_STREAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a40aad5cb3574e6e4e7bc955bc12760bf)
- [BT_AUDIO_METADATA_TYPE_AUDIO_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc)
- [BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1)
- [BT_AUDIO_METADATA_TYPE_BROADCAST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354ada34d453c8ce75a155c59c371a67d8a6)
- [BT_AUDIO_METADATA_TYPE_CCID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b)
- [BT_AUDIO_METADATA_TYPE_EXTENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39)
- [BT_AUDIO_METADATA_TYPE_LANG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1)
- [BT_AUDIO_METADATA_TYPE_PARENTAL_RATING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613)
- [BT_AUDIO_METADATA_TYPE_PREF_CONTEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a)
- [BT_AUDIO_METADATA_TYPE_PROGRAM_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7)
- [BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922)
- [BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa)
- [BT_AUDIO_METADATA_TYPE_VENDOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286)
- [BT_AUDIO_BROADCAST_NAME_CHAR_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaaf50689c66f41dee1f4fab02893c4a1b)
- [BT_AUDIO_BROADCAST_NAME_CHAR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaaabef5f2a77ea0ca60156eef80175311)
- [BT_AUDIO_BROADCAST_NAME_LEN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaa3bf677a479a90793f28a5a3ed69c7e0)
- [BT_AUDIO_BROADCAST_NAME_LEN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gaa2fafcbb6a826c3f4cee16ebb545dad6)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_编解码器配置解析 API（Codec config parsing APIs）.md)
