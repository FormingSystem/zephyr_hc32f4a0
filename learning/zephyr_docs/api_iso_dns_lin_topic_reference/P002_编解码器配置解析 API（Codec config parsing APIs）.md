---
id: learning.zephyr-docs.api-iso-dns-lin-topic-reference.page-2
title: 编解码器配置解析 API（Codec config parsing APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_编解码器配置解析 API（Codec config parsing APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音频编解码器配置 API（Audio codec Config APIs）

<a id="details"></a>

音频编解码器配置 API（Audio Codec Config APIs）。用于解析长度－类型－值（LTV）格式的编解码器配置数据的函数，封装于编解码器配置解析 API 中。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.1\_函数（Functions）

<a id="r_ga2e557fe726a49dc99754da16f7cc60af"></a>

```c
int bt_audio_codec_cfg_freq_to_freq_hz (enum bt_audio_codec_cfg_freq freq)
```

相关声明：[bt_audio_codec_cfg_freq_to_freq_hz](#ga2e557fe726a49dc99754da16f7cc60af)、[bt_audio_codec_cfg_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga8e99fb678cc011bb8c9f6e1858bae0d7)。

将分配编号（Assigned Numbers）中的频率编码转换为频率值。

<a id="r_ga99ab4f6d2a18f2a9b4e3da47f63fc9e0"></a>

```c
int bt_audio_codec_cfg_freq_hz_to_freq (uint32_t freq_hz)
```

相关声明：[bt_audio_codec_cfg_freq_hz_to_freq](#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将频率值转换为分配编号（Assigned Numbers）中的频率编码。

<a id="r_gad8525a57d35e3e34ea591f7e20e2512d"></a>

```c
int bt_audio_codec_cfg_get_freq (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_get_freq](#gad8525a57d35e3e34ea591f7e20e2512d)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

从编解码器配置（Codec Configuration）中提取频率（Frequency）。

<a id="r_gac119989d5dcfa36becf4edd0ae7c6138"></a>

```c
int bt_audio_codec_cfg_set_freq (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_codec_cfg_freq freq)
```

相关声明：[bt_audio_codec_cfg_set_freq](#gac119989d5dcfa36becf4edd0ae7c6138)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_codec_cfg_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga8e99fb678cc011bb8c9f6e1858bae0d7)。

设置编解码器配置（Codec Configuration）中的频率（Frequency）。

<a id="r_ga225e05df1f0d1efb709c972187901495"></a>

```c
int bt_audio_codec_cfg_frame_dur_to_frame_dur_us (enum bt_audio_codec_cfg_frame_dur frame_dur)
```

相关声明：[bt_audio_codec_cfg_frame_dur_to_frame_dur_us](#ga225e05df1f0d1efb709c972187901495)、[bt_audio_codec_cfg_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga83701b5eadfcbc9b84dc0b1a85ebeb74)。

将分配编号（Assigned Numbers）中的帧时长编码转换为以微秒表示的时长。

<a id="r_ga0782a3d9254fb76b441c6c2492571556"></a>

```c
int bt_audio_codec_cfg_frame_dur_us_to_frame_dur (uint32_t frame_dur_us)
```

相关声明：[bt_audio_codec_cfg_frame_dur_us_to_frame_dur](#ga0782a3d9254fb76b441c6c2492571556)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将以微秒表示的帧时长转换为分配编号（Assigned Numbers）中的帧时长编码。

<a id="r_ga2dd3afe41b22e989fb46614f89550007"></a>

```c
int bt_audio_codec_cfg_get_frame_dur (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_get_frame_dur](#ga2dd3afe41b22e989fb46614f89550007)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

从蓝牙编解码器配置（BT Codec Config）中提取帧时长（Frame Duration）。

<a id="r_ga7d8306f98cb00f06e68a1df417825f0d"></a>

```c
int bt_audio_codec_cfg_set_frame_dur (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_codec_cfg_frame_dur frame_dur)
```

相关声明：[bt_audio_codec_cfg_set_frame_dur](#ga7d8306f98cb00f06e68a1df417825f0d)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_codec_cfg_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga83701b5eadfcbc9b84dc0b1a85ebeb74)。

设置编解码器配置（Codec Configuration）中的帧时长（Frame Duration）。

<a id="r_gae712e0f8e84aeb4ad2528da34907e29d"></a>

```c
int bt_audio_codec_cfg_get_chan_allocation (const struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_location *chan_allocation, bool fallback_to_default)
```

相关声明：[bt_audio_codec_cfg_get_chan_allocation](#gae712e0f8e84aeb4ad2528da34907e29d)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

从蓝牙编解码器配置（BT Codec Config）中提取声道分配（Channel Allocation）。

<a id="r_gafbbcd69fac18ed0201a5e0156209b049"></a>

```c
int bt_audio_codec_cfg_set_chan_allocation (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_location chan_allocation)
```

相关声明：[bt_audio_codec_cfg_set_chan_allocation](#gafbbcd69fac18ed0201a5e0156209b049)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)。

设置编解码器配置（Codec Configuration）中的声道分配（Channel Allocation）。

<a id="r_ga503be053422217502d6108b045791e02"></a>

```c
int bt_audio_codec_cfg_get_octets_per_frame (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_get_octets_per_frame](#ga503be053422217502d6108b045791e02)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

从蓝牙编解码器配置（BT Codec Config）中提取以八位组（Octets）表示的帧大小。

<a id="r_ga866cdec28194056dc9e274d0436b45c2"></a>

```c
int bt_audio_codec_cfg_set_octets_per_frame (struct bt_audio_codec_cfg *codec_cfg, uint16_t octets_per_frame)
```

相关声明：[bt_audio_codec_cfg_set_octets_per_frame](#ga866cdec28194056dc9e274d0436b45c2)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置编解码器配置（Codec Configuration）中的每个编解码器帧的八位组数（Octets per Codec Frame）。

<a id="r_gadba0723f9d8a9546b659fba139051374"></a>

```c
int bt_audio_codec_cfg_get_frame_blocks_per_sdu (const struct bt_audio_codec_cfg *codec_cfg, bool fallback_to_default)
```

相关声明：[bt_audio_codec_cfg_get_frame_blocks_per_sdu](#gadba0723f9d8a9546b659fba139051374)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

从蓝牙编解码器配置（BT Codec Config）中提取每个服务数据单元（SDU）包含的音频帧块数量。

<a id="r_gac9cf20bafbe24b34034bfb6ee7aaf03e"></a>

```c
int bt_audio_codec_cfg_set_frame_blocks_per_sdu (struct bt_audio_codec_cfg *codec_cfg, uint8_t frame_blocks)
```

相关声明：[bt_audio_codec_cfg_set_frame_blocks_per_sdu](#gac9cf20bafbe24b34034bfb6ee7aaf03e)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置（Codec Configuration）中的每个服务数据单元的帧块数（Frame Blocks per SDU）。

<a id="r_ga707c679db0193197b56acabfb08f8d1f"></a>

```c
int bt_audio_codec_cfg_get_val (const struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_codec_cfg_type type, const uint8_t **data)
```

相关声明：[bt_audio_codec_cfg_get_val](#ga707c679db0193197b56acabfb08f8d1f)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_codec_cfg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga9230ec4d7518bd243207ba2decb1a974)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

查找指定的编解码器配置值（Codec Configuration Value）。

<a id="r_gab10f22938780530b1d1b95695382902e"></a>

```c
int bt_audio_codec_cfg_set_val (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_codec_cfg_type type, const uint8_t *data, size_t data_len)
```

相关声明：[bt_audio_codec_cfg_set_val](#gab10f22938780530b1d1b95695382902e)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_codec_cfg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga9230ec4d7518bd243207ba2decb1a974)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置或添加指定的编解码器配置值（Codec Configuration Value）。

<a id="r_gad3857d0ca008854df5966501caa261ba"></a>

```c
int bt_audio_codec_cfg_unset_val (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_codec_cfg_type type)
```

相关声明：[bt_audio_codec_cfg_unset_val](#gad3857d0ca008854df5966501caa261ba)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_codec_cfg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga9230ec4d7518bd243207ba2decb1a974)。

取消设置指定的编解码器配置值（Codec Configuration Value）。

<a id="r_gae98335e87394a491b4a311d867a5e32d"></a>

```c
int bt_audio_codec_cfg_meta_get_val (const struct bt_audio_codec_cfg *codec_cfg, uint8_t type, const uint8_t **data)
```

相关声明：[bt_audio_codec_cfg_meta_get_val](#gae98335e87394a491b4a311d867a5e32d)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据类型查找指定的元数据值（Metadata Value）。

<a id="r_ga3e24c2ba8de502600e647cb2f84e3ec4"></a>

```c
int bt_audio_codec_cfg_meta_set_val (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_metadata_type type, const uint8_t *data, size_t data_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_val](#ga3e24c2ba8de502600e647cb2f84e3ec4)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置或添加指定的编解码器配置元数据值（Codec Configuration Metadata Value）。

<a id="r_gab46f830daa1d9a907f47eb2a9eed7337"></a>

```c
int bt_audio_codec_cfg_meta_unset_val (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_metadata_type type)
```

相关声明：[bt_audio_codec_cfg_meta_unset_val](#gab46f830daa1d9a907f47eb2a9eed7337)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)。

取消设置指定的编解码器配置元数据值（Codec Configuration Metadata Value）。

<a id="r_gaea087663426a49bb6ff4859800aecb84"></a>

```c
int bt_audio_codec_cfg_meta_get_pref_context (const struct bt_audio_codec_cfg *codec_cfg, bool fallback_to_default)
```

相关声明：[bt_audio_codec_cfg_meta_get_pref_context](#gaea087663426a49bb6ff4859800aecb84)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

提取首选上下文（Preferred Contexts）。

<a id="r_gab40bad609f17d24e7e0e9ffcebe4e912"></a>

```c
int bt_audio_codec_cfg_meta_set_pref_context (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_context ctx)
```

相关声明：[bt_audio_codec_cfg_meta_set_pref_context](#gab40bad609f17d24e7e0e9ffcebe4e912)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置编解码器配置元数据（Codec Configuration Metadata）中的首选上下文（Preferred Context）。

<a id="r_ga4cc4e1bb941206e7f1541a57fc92b8e9"></a>

```c
int bt_audio_codec_cfg_meta_get_stream_context (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_meta_get_stream_context](#ga4cc4e1bb941206e7f1541a57fc92b8e9)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

提取流上下文（Stream Contexts）。

<a id="r_ga5cd2af1bb44c6eb5bafe824f005a77f0"></a>

```c
int bt_audio_codec_cfg_meta_set_stream_context (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_context ctx)
```

相关声明：[bt_audio_codec_cfg_meta_set_stream_context](#ga5cd2af1bb44c6eb5bafe824f005a77f0)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置编解码器配置元数据（Codec Configuration Metadata）中的流上下文（Stream Context）。

<a id="r_ga03284b8474d65443d7ecc8bdfc6f04c6"></a>

```c
int bt_audio_codec_cfg_meta_get_program_info (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **program_info)
```

相关声明：[bt_audio_codec_cfg_meta_get_program_info](#ga03284b8474d65443d7ecc8bdfc6f04c6)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取节目信息（Program Info）。

<a id="r_ga2ca9e616d20d7513c60ce905f046ac7b"></a>

```c
int bt_audio_codec_cfg_meta_set_program_info (struct bt_audio_codec_cfg *codec_cfg, const uint8_t *program_info, size_t program_info_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_program_info](#ga2ca9e616d20d7513c60ce905f046ac7b)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的节目信息（Program Info）。

<a id="r_ga55e3cbaeacf15fcb1f24a16eb28db99c"></a>

```c
int bt_audio_codec_cfg_meta_get_lang (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **lang)
```

相关声明：[bt_audio_codec_cfg_meta_get_lang](#ga55e3cbaeacf15fcb1f24a16eb28db99c)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取语言（Language）。

<a id="r_ga93052db14c857097e7cf9abc34b7fc39"></a>

```c
int bt_audio_codec_cfg_meta_set_lang (struct bt_audio_codec_cfg *codec_cfg, const uint8_t lang[3U])
```

相关声明：[bt_audio_codec_cfg_meta_set_lang](#ga93052db14c857097e7cf9abc34b7fc39)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的语言（Language）。

<a id="r_gaa0f9b9f608c7af881d5a928a3ae397b2"></a>

```c
int bt_audio_codec_cfg_meta_get_ccid_list (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **ccid_list)
```

相关声明：[bt_audio_codec_cfg_meta_get_ccid_list](#gaa0f9b9f608c7af881d5a928a3ae397b2)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取内容控制标识符列表（CCID List）。

<a id="r_ga59716b95fcea3404ff8c078564b0e29c"></a>

```c
int bt_audio_codec_cfg_meta_set_ccid_list (struct bt_audio_codec_cfg *codec_cfg, const uint8_t *ccid_list, size_t ccid_list_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_ccid_list](#ga59716b95fcea3404ff8c078564b0e29c)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的内容控制标识符列表（CCID List）。

<a id="r_gaf0eecb02a05f0cc2b75ae9fb32c03913"></a>

```c
int bt_audio_codec_cfg_meta_get_parental_rating (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_meta_get_parental_rating](#gaf0eecb02a05f0cc2b75ae9fb32c03913)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

提取家长分级（Parental Rating）。

<a id="r_gab5d8b5877de4fe16c0e06a1d4f0d15ce"></a>

```c
int bt_audio_codec_cfg_meta_set_parental_rating (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_parental_rating parental_rating)
```

相关声明：[bt_audio_codec_cfg_meta_set_parental_rating](#gab5d8b5877de4fe16c0e06a1d4f0d15ce)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga6d4aff1f93dc0b902e4b5d1355f15760)。

设置编解码器配置元数据（Codec Configuration Metadata）中的家长分级（Parental Rating）。

<a id="r_ga6bdbc0a0b929fdbdc75db479aec858df"></a>

```c
int bt_audio_codec_cfg_meta_get_program_info_uri (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **program_info_uri)
```

相关声明：[bt_audio_codec_cfg_meta_get_program_info_uri](#ga6bdbc0a0b929fdbdc75db479aec858df)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取节目信息 URI（Program Info URI）。

<a id="r_ga99163729034e816eaef7195505d5ae20"></a>

```c
int bt_audio_codec_cfg_meta_set_program_info_uri (struct bt_audio_codec_cfg *codec_cfg, const uint8_t *program_info_uri, size_t program_info_uri_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_program_info_uri](#ga99163729034e816eaef7195505d5ae20)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的节目信息 URI（Program Info URI）。

<a id="r_ga0fd6e6baf1b4f22d60768aaed6f42e8e"></a>

```c
int bt_audio_codec_cfg_meta_get_audio_active_state (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_meta_get_audio_active_state](#ga0fd6e6baf1b4f22d60768aaed6f42e8e)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

提取音频活动状态（Audio Active State）。

<a id="r_gaf869e7ce0c9dd467fb03e8503d36c58a"></a>

```c
int bt_audio_codec_cfg_meta_set_audio_active_state (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_active_state state)
```

相关声明：[bt_audio_codec_cfg_meta_set_audio_active_state](#gaf869e7ce0c9dd467fb03e8503d36c58a)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga16d403ec4db7be997682331ad365ff5f)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置编解码器配置元数据（Codec Configuration Metadata）中的音频活动状态（Audio Active State）。

<a id="r_ga66143aa7dcc726e06a12660b8f90fc5a"></a>

```c
int bt_audio_codec_cfg_meta_get_bcast_audio_immediate_rend_flag (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_meta_get_bcast_audio_immediate_rend_flag](#ga66143aa7dcc726e06a12660b8f90fc5a)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

提取广播音频立即呈现标志（Broadcast Audio Immediate Rendering Flag）。

<a id="r_gaede61b65d2037c7fbf6c4c4e090990be"></a>

```c
int bt_audio_codec_cfg_meta_set_bcast_audio_immediate_rend_flag (struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_meta_set_bcast_audio_immediate_rend_flag](#gaede61b65d2037c7fbf6c4c4e090990be)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

设置编解码器配置元数据（Codec Configuration Metadata）中的广播音频立即呈现标志（Broadcast Audio Immediate Rendering Flag）。

<a id="r_ga22ae14fce65b757e31f391c4bdcae328"></a>

```c
int bt_audio_codec_cfg_meta_get_assisted_listening_stream (const struct bt_audio_codec_cfg *codec_cfg)
```

相关声明：[bt_audio_codec_cfg_meta_get_assisted_listening_stream](#ga22ae14fce65b757e31f391c4bdcae328)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)。

提取辅助收听流（Assisted Listening Stream）。

<a id="r_ga67d83559cbe6cfab235f2e588cbc398c"></a>

```c
int bt_audio_codec_cfg_meta_set_assisted_listening_stream (struct bt_audio_codec_cfg *codec_cfg, enum bt_audio_assisted_listening_stream val)
```

相关声明：[bt_audio_codec_cfg_meta_set_assisted_listening_stream](#ga67d83559cbe6cfab235f2e588cbc398c)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[bt_audio_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga207fbf0fbca9b24cba02c7f1d184e7f5)。

设置编解码器配置元数据（Codec Configuration Metadata）中的辅助收听流值（Assisted Listening Stream Value）。

<a id="r_ga5d80babcd6f381014e1fae98a755e1d3"></a>

```c
int bt_audio_codec_cfg_meta_get_broadcast_name (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **broadcast_name)
```

相关声明：[bt_audio_codec_cfg_meta_get_broadcast_name](#ga5d80babcd6f381014e1fae98a755e1d3)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取广播名称（Broadcast Name）。

<a id="r_ga4f5cbacebedc8d7df02d1c47b140bf3c"></a>

```c
int bt_audio_codec_cfg_meta_set_broadcast_name (struct bt_audio_codec_cfg *codec_cfg, const uint8_t *broadcast_name, size_t broadcast_name_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_broadcast_name](#ga4f5cbacebedc8d7df02d1c47b140bf3c)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的广播名称（Broadcast Name）。

<a id="r_ga1f76f82bff63b876eb761a0bf0377428"></a>

```c
int bt_audio_codec_cfg_meta_get_extended (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **extended_meta)
```

相关声明：[bt_audio_codec_cfg_meta_get_extended](#ga1f76f82bff63b876eb761a0bf0377428)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取扩展元数据（Extended Metadata）。

<a id="r_gade9cb53287ab3356fb57ba8a454a3aad"></a>

```c
int bt_audio_codec_cfg_meta_set_extended (struct bt_audio_codec_cfg *codec_cfg, const uint8_t *extended_meta, size_t extended_meta_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_extended](#gade9cb53287ab3356fb57ba8a454a3aad)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的扩展元数据（Extended Metadata）。

<a id="r_ga4a4982e3bd0e8c944b584196ef146f6c"></a>

```c
int bt_audio_codec_cfg_meta_get_vendor (const struct bt_audio_codec_cfg *codec_cfg, const uint8_t **vendor_meta)
```

相关声明：[bt_audio_codec_cfg_meta_get_vendor](#ga4a4982e3bd0e8c944b584196ef146f6c)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提取厂商特定元数据（Vendor Specific Metadata）。

<a id="r_ga6935d1c40b3178b0c8fa877ee93d1e53"></a>

```c
int bt_audio_codec_cfg_meta_set_vendor (struct bt_audio_codec_cfg *codec_cfg, const uint8_t *vendor_meta, size_t vendor_meta_len)
```

相关声明：[bt_audio_codec_cfg_meta_set_vendor](#ga6935d1c40b3178b0c8fa877ee93d1e53)、[bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置编解码器配置元数据（Codec Configuration Metadata）中的厂商特定元数据（Vendor Specific Metadata）。

## 2.2\_详细说明（Detailed Documentation）

<a id="ga225e05df1f0d1efb709c972187901495"></a>

### `bt_audio_codec_cfg_frame_dur_to_frame_dur_us()`

```c
int bt_audio_codec_cfg_frame_dur_to_frame_dur_us ( enum bt_audio_codec_cfg_frame_dur frame_dur)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

将分配编号（Assigned Numbers）中的帧时长编码转换为以微秒表示的时长。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `frame_dur` | 要转换的、采用分配编号（Assigned Numbers）表示的帧时长。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `duration` | 转换后的帧时长（Frame Duration），单位为微秒。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |

<a id="ga0782a3d9254fb76b441c6c2492571556"></a>

### `bt_audio_codec_cfg_frame_dur_us_to_frame_dur()`

```c
int bt_audio_codec_cfg_frame_dur_us_to_frame_dur ( uint32_t frame_dur_us)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

将以微秒表示的帧时长转换为分配编号（Assigned Numbers）中的帧时长编码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `frame_dur_us` | 要转换的帧时长（Frame Duration），单位为微秒。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `duration` | 采用分配编号（Assigned Numbers）表示的帧时长，类型为 bt_audio_codec_cfg_frame_dur。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |

<a id="ga99ab4f6d2a18f2a9b4e3da47f63fc9e0"></a>

### `bt_audio_codec_cfg_freq_hz_to_freq()`

```c
int bt_audio_codec_cfg_freq_hz_to_freq ( uint32_t freq_hz)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

将频率值转换为分配编号（Assigned Numbers）中的频率编码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `freq_hz` | 要转换的频率值（Frequency Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `frequency` | 采用分配编号（Assigned Numbers）表示的频率，类型为 bt_audio_codec_cfg_freq。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |

<a id="ga2e557fe726a49dc99754da16f7cc60af"></a>

### `bt_audio_codec_cfg_freq_to_freq_hz()`

```c
int bt_audio_codec_cfg_freq_to_freq_hz ( enum bt_audio_codec_cfg_freq freq)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

将分配编号（Assigned Numbers）中的频率编码转换为频率值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `freq` | 要转换的、采用分配编号（Assigned Numbers）表示的频率。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `frequency` | 转换后的频率值（Frequency Value），单位为 Hz。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |

<a id="gae712e0f8e84aeb4ad2528da34907e29d"></a>

### `bt_audio_codec_cfg_get_chan_allocation()`

```c
int bt_audio_codec_cfg_get_chan_allocation ( const struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_location * chan_allocation, bool fallback_to_default )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

从蓝牙编解码器配置（BT Codec Config）中提取声道分配（Channel Allocation）。

返回值是一个位域（Bit Field），表示 bt_audio_location 指定的一个或多个音频位置（Audio Locations）。须匹配 BT_PAC_SNK_LOC／BT_PAC_SRC_LOC 中设置的一个或多个位。

可包含的声道数（Channels）不超过配置的 BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要从中提取数据的编解码器配置（Codec Configuration）。 |
| `chan_allocation` | 指向用于保存提取值的变量的指针。 |
| `fallback_to_default` | 若为 true，当 codec_cfg.id 为 BT_HCI_CODING_FORMAT_LC3 且未找到该类型时，此函数将提供默认值 BT_AUDIO_LOCATION_MONO_AUDIO。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已找到值，并将其保存在所提供指针指向的位置。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值具有无效的大小或取值。 |

<a id="gadba0723f9d8a9546b659fba139051374"></a>

### `bt_audio_codec_cfg_get_frame_blocks_per_sdu()`

```c
int bt_audio_codec_cfg_get_frame_blocks_per_sdu ( const struct bt_audio_codec_cfg * codec_cfg, bool fallback_to_default )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

从蓝牙编解码器配置（BT Codec Config）中提取每个服务数据单元（SDU）包含的音频帧块数量。

服务数据单元（SDU）的总大小为 `octets_per_frame * frame_blocks_per_sdu * number-of-channels`。

如果没有此值，须使用默认值 1。

帧块（Frame Block）由一个或多个帧组成，这些帧表示同一时间段内不同声道的数据。如果流有两个音频声道且此值为 2，则 SDU 中会有 4 个帧。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要从中提取数据的编解码器配置（Codec Configuration）。 |
| `fallback_to_default` | 若为 true，当 codec_cfg.id 为 BT_HCI_CODING_FORMAT_LC3 且未找到该类型时，此函数将返回默认值 1。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `frame_blocks_per_sdu` | 每个服务数据单元（SDU）中的编解码器帧块（Codec Frame Blocks）数量。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值具有无效的大小或取值。 |

<a id="ga2dd3afe41b22e989fb46614f89550007"></a>

### `bt_audio_codec_cfg_get_frame_dur()`

```c
int bt_audio_codec_cfg_get_frame_dur ( const struct bt_audio_codec_cfg * codec_cfg)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

从蓝牙编解码器配置（BT Codec Config）中提取帧时长（Frame Duration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要从中提取数据的编解码器配置（Codec Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `frequency` | 一个 bt_audio_codec_cfg_frame_dur 值。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值具有无效的大小或取值。 |

<a id="gad8525a57d35e3e34ea591f7e20e2512d"></a>

### `bt_audio_codec_cfg_get_freq()`

```c
int bt_audio_codec_cfg_get_freq ( const struct bt_audio_codec_cfg * codec_cfg)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

从编解码器配置（Codec Configuration）中提取频率（Frequency）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要从中提取数据的编解码器配置（Codec Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `frequency` | 一个 bt_audio_codec_cfg_freq 值。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值具有无效的大小或取值。 |

<a id="ga503be053422217502d6108b045791e02"></a>

### `bt_audio_codec_cfg_get_octets_per_frame()`

```c
int bt_audio_codec_cfg_get_octets_per_frame ( const struct bt_audio_codec_cfg * codec_cfg)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

从蓝牙编解码器配置（BT Codec Config）中提取以八位组（Octets）表示的帧大小。

服务数据单元（SDU）的总大小为 `octets_per_frame * blocks_per_sdu`。

蓝牙规范（Bluetooth Specifications）对该值的规定不明确，没有说明编解码器只能使用此 SDU 大小。LC3 等编解码器支持逐 SDU 的可变比特率（Variable Bit-rate），因此编码器可能允许将帧大小减小到此值以下。建议使用接收到的 SDU 大小除以 blocks_per_sdu，而不要依赖此 octets_per_sdu 值固定不变。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要从中提取数据的编解码器配置（Codec Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `frame_length` | 帧长度（Frame Length），单位为八位字节。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值具有无效的大小或取值。 |

<a id="ga707c679db0193197b56acabfb08f8d1f"></a>

### `bt_audio_codec_cfg_get_val()`

```c
int bt_audio_codec_cfg_get_val ( const struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_codec_cfg_type type, const uint8_t ** data )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

查找指定的编解码器配置值（Codec Configuration Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[in] type` | 要查找的类型 ID（Type ID）。 |
| `[out] data` | 指向数据指针的指针；找到条目时更新该数据指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | 找到的数据长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="ga22ae14fce65b757e31f391c4bdcae328"></a>

### `bt_audio_codec_cfg_meta_get_assisted_listening_stream()`

```c
int bt_audio_codec_cfg_meta_get_assisted_listening_stream ( const struct bt_audio_codec_cfg * codec_cfg)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取辅助收听流（Assisted Listening Stream）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_ASSISTED_LISTENING_STREAM`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `value` | 返回值为正数或 0 时，表示辅助聆听流（Assisted Listening Stream）的值。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值大小无效。 |

<a id="ga0fd6e6baf1b4f22d60768aaed6f42e8e"></a>

### `bt_audio_codec_cfg_meta_get_audio_active_state()`

```c
int bt_audio_codec_cfg_meta_get_audio_active_state ( const struct bt_audio_codec_cfg * codec_cfg)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取音频活动状态（Audio Active State）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_AUDIO_STATE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 返回值为正数或 0 时，表示首选上下文类型（Preferred Context Type）。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值大小无效。 |

<a id="ga66143aa7dcc726e06a12660b8f90fc5a"></a>

### `bt_audio_codec_cfg_meta_get_bcast_audio_immediate_rend_flag()`

```c
int bt_audio_codec_cfg_meta_get_bcast_audio_immediate_rend_flag ( const struct bt_audio_codec_cfg * codec_cfg)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取广播音频立即呈现标志（Broadcast Audio Immediate Rendering Flag）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 找到了该标志（Flag）。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到该标志（Flag）。 |

<a id="ga5d80babcd6f381014e1fae98a755e1d3"></a>

### `bt_audio_codec_cfg_meta_get_broadcast_name()`

```c
int bt_audio_codec_cfg_meta_get_broadcast_name ( const struct bt_audio_codec_cfg * codec_cfg, const uint8_t ** broadcast_name )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取广播名称（Broadcast Name）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_BROADCAST_NAME`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] broadcast_name` | 指向 UTF-8 格式广播名称（Broadcast Name）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `length` | broadcast_name 的长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 已找到数据，但广播名称（Broadcast Name）无效。 |

<a id="gaa0f9b9f608c7af881d5a928a3ae397b2"></a>

### `bt_audio_codec_cfg_meta_get_ccid_list()`

```c
int bt_audio_codec_cfg_meta_get_ccid_list ( const struct bt_audio_codec_cfg * codec_cfg, const uint8_t ** ccid_list )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取内容控制标识符列表（CCID List）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_CCID_LIST`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] ccid_list` | 指向包含 8 位内容控制标识符（CCID）的数组的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | ccid_list 的长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="ga1f76f82bff63b876eb761a0bf0377428"></a>

### `bt_audio_codec_cfg_meta_get_extended()`

```c
int bt_audio_codec_cfg_meta_get_extended ( const struct bt_audio_codec_cfg * codec_cfg, const uint8_t ** extended_meta )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取扩展元数据（Extended Metadata）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_EXTENDED`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] extended_meta` | 指向扩展元数据（Extended Metadata）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | extended_meta 的长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="ga55e3cbaeacf15fcb1f24a16eb28db99c"></a>

### `bt_audio_codec_cfg_meta_get_lang()`

```c
int bt_audio_codec_cfg_meta_get_lang ( const struct bt_audio_codec_cfg * codec_cfg, const uint8_t ** lang )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取语言（Language）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_LANG`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] lang` | 指向语言字节（Language Bytes）的指针，长度为 BT_AUDIO_LANG_SIZE。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值大小无效。 |

<a id="gaf0eecb02a05f0cc2b75ae9fb32c03913"></a>

### `bt_audio_codec_cfg_meta_get_parental_rating()`

```c
int bt_audio_codec_cfg_meta_get_parental_rating ( const struct bt_audio_codec_cfg * codec_cfg)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取家长分级（Parental Rating）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_PARENTAL_RATING`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `parental_rating` | 返回值为正数或 0 时，表示家长分级（Parental Rating）。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值大小无效。 |

<a id="gaea087663426a49bb6ff4859800aecb84"></a>

### `bt_audio_codec_cfg_meta_get_pref_context()`

```c
int bt_audio_codec_cfg_meta_get_pref_context ( const struct bt_audio_codec_cfg * codec_cfg, bool fallback_to_default )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取首选上下文（Preferred Contexts）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_PREF_CONTEXT`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `fallback_to_default` | 若为 true，当 codec_cfg.id 为 BT_HCI_CODING_FORMAT_LC3 且未找到该类型时，此函数将提供默认值 BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 返回值为正数或 0 时，表示首选上下文类型（Preferred Context Type）。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值大小无效。 |

<a id="ga03284b8474d65443d7ecc8bdfc6f04c6"></a>

### `bt_audio_codec_cfg_meta_get_program_info()`

```c
int bt_audio_codec_cfg_meta_get_program_info ( const struct bt_audio_codec_cfg * codec_cfg, const uint8_t ** program_info )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取节目信息（Program Info）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_PROGRAM_INFO`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] program_info` | 指向 UTF-8 格式节目信息（Program Info）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | program_info 的长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="ga6bdbc0a0b929fdbdc75db479aec858df"></a>

### `bt_audio_codec_cfg_meta_get_program_info_uri()`

```c
int bt_audio_codec_cfg_meta_get_program_info_uri ( const struct bt_audio_codec_cfg * codec_cfg, const uint8_t ** program_info_uri )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取节目信息 URI（Program Info URI）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] program_info_uri` | 指向 UTF-8 格式节目信息 URI（Program Info URI）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | program_info_uri 的长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="ga4cc4e1bb941206e7f1541a57fc92b8e9"></a>

### `bt_audio_codec_cfg_meta_get_stream_context()`

```c
int bt_audio_codec_cfg_meta_get_stream_context ( const struct bt_audio_codec_cfg * codec_cfg)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取流上下文（Stream Contexts）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `context` | 返回值为正数或 0 时，表示流上下文类型（Stream Context Type）。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |
| `-EBADMSG` | 找到的值大小无效。 |

<a id="gae98335e87394a491b4a311d867a5e32d"></a>

### `bt_audio_codec_cfg_meta_get_val()`

```c
int bt_audio_codec_cfg_meta_get_val ( const struct bt_audio_codec_cfg * codec_cfg, uint8_t type, const uint8_t ** data )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

根据类型查找指定的元数据值（Metadata Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[in] type` | 要查找的类型 ID（Type ID）。 |
| `[out] data` | 指向数据指针的指针；找到条目时更新该数据指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | 找到的数据长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="ga4a4982e3bd0e8c944b584196ef146f6c"></a>

### `bt_audio_codec_cfg_meta_get_vendor()`

```c
int bt_audio_codec_cfg_meta_get_vendor ( const struct bt_audio_codec_cfg * codec_cfg, const uint8_t ** vendor_meta )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

提取厂商特定元数据（Vendor Specific Metadata）。

有关该值的更多信息，参见 `BT_AUDIO_METADATA_TYPE_VENDOR`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] codec_cfg` | 要在其中搜索的编解码器数据（Codec Data）。 |
| `[out] vendor_meta` | 指向厂商专用元数据（Vendor Specific Metadata）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `len` | vendor_meta 的长度，可能为 0。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENODATA` | 未找到数据（Data Not Found）。 |

<a id="ga67d83559cbe6cfab235f2e588cbc398c"></a>

### `bt_audio_codec_cfg_meta_set_assisted_listening_stream()`

```c
int bt_audio_codec_cfg_meta_set_assisted_listening_stream ( struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_assisted_listening_stream val )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的辅助收听流值（Assisted Listening Stream Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `val` | 要设置的辅助聆听流（Assisted Listening Stream）的值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cap.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gaf869e7ce0c9dd467fb03e8503d36c58a"></a>

### `bt_audio_codec_cfg_meta_set_audio_active_state()`

```c
int bt_audio_codec_cfg_meta_set_audio_active_state ( struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_active_state state )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的音频活动状态（Audio Active State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `state` | 要设置的音频活动状态（Audio Active State）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gaede61b65d2037c7fbf6c4c4e090990be"></a>

### `bt_audio_codec_cfg_meta_set_bcast_audio_immediate_rend_flag()`

```c
int bt_audio_codec_cfg_meta_set_bcast_audio_immediate_rend_flag ( struct bt_audio_codec_cfg * codec_cfg)
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的广播音频立即呈现标志（Broadcast Audio Immediate Rendering Flag）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga4f5cbacebedc8d7df02d1c47b140bf3c"></a>

### `bt_audio_codec_cfg_meta_set_broadcast_name()`

```c
int bt_audio_codec_cfg_meta_set_broadcast_name ( struct bt_audio_codec_cfg * codec_cfg, const uint8_t * broadcast_name, size_t broadcast_name_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的广播名称（Broadcast Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `broadcast_name` | 要设置的广播名称（Broadcast Name）。字符数须介于 BT_AUDIO_BROADCAST_NAME_CHAR_MIN 和 BT_AUDIO_BROADCAST_NAME_CHAR_MAX 之间。 |
| `broadcast_name_len` | broadcast_name 的长度。须介于 BT_AUDIO_BROADCAST_NAME_LEN_MIN 和 BT_AUDIO_BROADCAST_NAME_LEN_MAX 之间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga59716b95fcea3404ff8c078564b0e29c"></a>

### `bt_audio_codec_cfg_meta_set_ccid_list()`

```c
int bt_audio_codec_cfg_meta_set_ccid_list ( struct bt_audio_codec_cfg * codec_cfg, const uint8_t * ccid_list, size_t ccid_list_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的内容控制标识符列表（CCID List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `ccid_list` | 要设置的节目信息（Program Info）。 |
| `ccid_list_len` | ccid_list 的长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gade9cb53287ab3356fb57ba8a454a3aad"></a>

### `bt_audio_codec_cfg_meta_set_extended()`

```c
int bt_audio_codec_cfg_meta_set_extended ( struct bt_audio_codec_cfg * codec_cfg, const uint8_t * extended_meta, size_t extended_meta_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的扩展元数据（Extended Metadata）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `extended_meta` | 要设置的扩展元数据（Extended Metadata）。 |
| `extended_meta_len` | extended_meta 的长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga93052db14c857097e7cf9abc34b7fc39"></a>

### `bt_audio_codec_cfg_meta_set_lang()`

```c
int bt_audio_codec_cfg_meta_set_lang ( struct bt_audio_codec_cfg * codec_cfg, const uint8_t lang[3U] )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的语言（Language）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `lang` | 要设置的 24 位语言（Language）值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gab5d8b5877de4fe16c0e06a1d4f0d15ce"></a>

### `bt_audio_codec_cfg_meta_set_parental_rating()`

```c
int bt_audio_codec_cfg_meta_set_parental_rating ( struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_parental_rating parental_rating )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的家长分级（Parental Rating）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `parental_rating` | 要设置的家长分级（Parental Rating）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gab40bad609f17d24e7e0e9ffcebe4e912"></a>

### `bt_audio_codec_cfg_meta_set_pref_context()`

```c
int bt_audio_codec_cfg_meta_set_pref_context ( struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_context ctx )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的首选上下文（Preferred Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `ctx` | 要设置的首选上下文（Preferred Context）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga2ca9e616d20d7513c60ce905f046ac7b"></a>

### `bt_audio_codec_cfg_meta_set_program_info()`

```c
int bt_audio_codec_cfg_meta_set_program_info ( struct bt_audio_codec_cfg * codec_cfg, const uint8_t * program_info, size_t program_info_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的节目信息（Program Info）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `program_info` | 要设置的节目信息（Program Info）。 |
| `program_info_len` | program_info 的长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga99163729034e816eaef7195505d5ae20"></a>

### `bt_audio_codec_cfg_meta_set_program_info_uri()`

```c
int bt_audio_codec_cfg_meta_set_program_info_uri ( struct bt_audio_codec_cfg * codec_cfg, const uint8_t * program_info_uri, size_t program_info_uri_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的节目信息 URI（Program Info URI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `program_info_uri` | 要设置的节目信息 URI（Program Info URI）。 |
| `program_info_uri_len` | program_info_uri 的长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga5cd2af1bb44c6eb5bafe824f005a77f0"></a>

### `bt_audio_codec_cfg_meta_set_stream_context()`

```c
int bt_audio_codec_cfg_meta_set_stream_context ( struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_context ctx )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的流上下文（Stream Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `ctx` | 要设置的流上下文（Stream Context）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga3e24c2ba8de502600e647cb2f84e3ec4"></a>

### `bt_audio_codec_cfg_meta_set_val()`

```c
int bt_audio_codec_cfg_meta_set_val ( struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_metadata_type type, const uint8_t * data, size_t data_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置或添加指定的编解码器配置元数据值（Codec Configuration Metadata Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要在其中设置值的编解码器配置（Codec Configuration）。 |
| `type` | 要设置的类型 ID（Type ID）。 |
| `data` | 指向要设置的数据指针的指针。 |
| `data_len` | 数据长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `meta_len` | 成功时返回 codec_cfg.meta_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga6935d1c40b3178b0c8fa877ee93d1e53"></a>

### `bt_audio_codec_cfg_meta_set_vendor()`

```c
int bt_audio_codec_cfg_meta_set_vendor ( struct bt_audio_codec_cfg * codec_cfg, const uint8_t * vendor_meta, size_t vendor_meta_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置元数据（Codec Configuration Metadata）中的厂商特定元数据（Vendor Specific Metadata）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `vendor_meta` | 要设置的厂商专用元数据（Vendor Specific Metadata）。 |
| `vendor_meta_len` | vendor_meta 的长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gab46f830daa1d9a907f47eb2a9eed7337"></a>

### `bt_audio_codec_cfg_meta_unset_val()`

```c
int bt_audio_codec_cfg_meta_unset_val ( struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_metadata_type type )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

取消设置指定的编解码器配置元数据值（Codec Configuration Metadata Value）。

将从编解码器配置元数据（Codec Configuration Metadata）中移除该类型及其值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要在其中设置值的编解码器数据（Codec Data）。 |
| `type` | 要取消设置的类型 ID（Type ID）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `meta_len` | 成功时返回 codec_cfg.meta_len。（原文 “The of codec_cfg.meta_len success” 存在措辞缺漏。） |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |

<a id="gafbbcd69fac18ed0201a5e0156209b049"></a>

### `bt_audio_codec_cfg_set_chan_allocation()`

```c
int bt_audio_codec_cfg_set_chan_allocation ( struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_location chan_allocation )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置（Codec Configuration）中的声道分配（Channel Allocation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `chan_allocation` | 要设置的声道分配（Channel Allocation）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gac9cf20bafbe24b34034bfb6ee7aaf03e"></a>

### `bt_audio_codec_cfg_set_frame_blocks_per_sdu()`

```c
int bt_audio_codec_cfg_set_frame_blocks_per_sdu ( struct bt_audio_codec_cfg * codec_cfg, uint8_t frame_blocks )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置（Codec Configuration）中的每个服务数据单元的帧块数（Frame Blocks per SDU）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `frame_blocks` | 要设置的每个 SDU 的帧块数（Frame Blocks per SDU）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga7d8306f98cb00f06e68a1df417825f0d"></a>

### `bt_audio_codec_cfg_set_frame_dur()`

```c
int bt_audio_codec_cfg_set_frame_dur ( struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_codec_cfg_frame_dur frame_dur )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置（Codec Configuration）中的帧时长（Frame Duration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `frame_dur` | 要设置的、采用分配编号（Assigned Numbers）表示的帧时长。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gac119989d5dcfa36becf4edd0ae7c6138"></a>

### `bt_audio_codec_cfg_set_freq()`

```c
int bt_audio_codec_cfg_set_freq ( struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_codec_cfg_freq freq )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置（Codec Configuration）中的频率（Frequency）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `freq` | 要设置的、采用分配编号（Assigned Numbers）表示的频率。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="ga866cdec28194056dc9e274d0436b45c2"></a>

### `bt_audio_codec_cfg_set_octets_per_frame()`

```c
int bt_audio_codec_cfg_set_octets_per_frame ( struct bt_audio_codec_cfg * codec_cfg, uint16_t octets_per_frame )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置编解码器配置（Codec Configuration）中的每个编解码器帧的八位组数（Octets per Codec Frame）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要为其设置数据的编解码器配置（Codec Configuration）。 |
| `octets_per_frame` | 要设置的每个编解码器帧的八位字节数（Octets per Codec Frame）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gab10f22938780530b1d1b95695382902e"></a>

### `bt_audio_codec_cfg_set_val()`

```c
int bt_audio_codec_cfg_set_val ( struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_codec_cfg_type type, const uint8_t * data, size_t data_len )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

设置或添加指定的编解码器配置值（Codec Configuration Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要在其中设置值的编解码器数据（Codec Data）。 |
| `type` | 要设置的类型 ID（Type ID）。 |
| `data` | 指向要设置的数据指针的指针。 |
| `data_len` | 数据长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 由于内存不足，无法设置或添加新值。 |

<a id="gad3857d0ca008854df5966501caa261ba"></a>

### `bt_audio_codec_cfg_unset_val()`

```c
int bt_audio_codec_cfg_unset_val ( struct bt_audio_codec_cfg * codec_cfg, enum bt_audio_codec_cfg_type type )
```

```c
#include <zephyr/bluetooth/audio/audio.h>
```

取消设置指定的编解码器配置值（Codec Configuration Value）。

将从编解码器配置（Codec Configuration）中移除该类型及其值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `codec_cfg` | 要在其中设置值的编解码器数据（Codec Data）。 |
| `type` | 要取消设置的类型 ID（Type ID）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `data_len` | 成功时返回 codec_cfg.data_len。 |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |


## 2.3\_原页交叉引用（Cross References）

- [bt_audio_codec_cfg_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga8e99fb678cc011bb8c9f6e1858bae0d7)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_audio_codec_cfg](../bluetooth_le_audio_model_reference/P008_bt_audio_codec_cfg_结构体.md)
- [bt_audio_codec_cfg_frame_dur](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga83701b5eadfcbc9b84dc0b1a85ebeb74)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_audio_codec_cfg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga9230ec4d7518bd243207ba2decb1a974)
- [bt_audio_metadata_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gab53d0dd62bceff97cf8eed7d8cf80354)
- [bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)
- [bt_audio_parental_rating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga6d4aff1f93dc0b902e4b5d1355f15760)
- [bt_audio_active_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga16d403ec4db7be997682331ad365ff5f)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_audio_assisted_listening_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga207fbf0fbca9b24cba02c7f1d184e7f5)
- [编解码器配置解析 API（Codec config parsing APIs）](P002_编解码器配置解析 API（Codec config parsing APIs）.md)
- [zephyr/bluetooth/audio/audio.h](../api_file_mesh_acpi_reference/P003_zephyr__bluetooth__audio__audio.h_文件参考.md)
- [BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191)
- [BT_AUDIO_LOCATION_MONO_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df)
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
- [BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5)
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

[上一章](P001_编解码器能力解析 API（Codec capability parsing APIs）.md) · [返回大纲](大纲.md) · [下一章](P003_等时通道（Isochronous channels，ISO）.md)
