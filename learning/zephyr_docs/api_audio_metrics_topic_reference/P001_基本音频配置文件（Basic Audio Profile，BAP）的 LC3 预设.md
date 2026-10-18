---
id: learning.zephyr-docs.api-audio-metrics-topic-reference.page-1
title: 基本音频配置文件（Basic Audio Profile，BAP）的 LC3 预设
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_基本音频配置文件（Basic Audio Profile，BAP）的 LC3 预设

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基本音频配置文件（Basic Audio Profile，BAP）的 LC3 预设

<a id="details"></a>

基本音频配置文件（Basic Audio Profile，BAP）的 LC3 预设（Presets）。自（Since）3.0 起提供，版本（Version）0.8.0。这些 API 根据 BAP 规范中编解码器配置表给出的值，提供编解码器配置（Codec Configuration）和服务质量（QoS）预设。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Fbap_5Flc3_5Fpreset"></a>

```c
struct bt_bap_lc3_preset
```

相关声明：[bt_bap_lc3_preset](../bluetooth_le_audio_model_reference/P026_bt_bap_lc3_preset_结构体.md)。

保存 BAP 定义的低复杂度通信编解码器（Low Complexity Communication Codec，LC3）预设的结构体。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_ga9f2075cd5019d356bc7ccf7f9cbc63bb"></a>

```c
#define BT_BAP_LC3_PRESET(_codec, _qos)
```

相关声明：[BT_BAP_LC3_PRESET](#ga9f2075cd5019d356bc7ccf7f9cbc63bb)。

用于声明 LC3 预设结构体（Preset Structure）的辅助宏。

<a id="r_gac1a211ed3116a0b7f0b181abd0ae6e8a"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_8_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_8_1_1](#gac1a211ed3116a0b7f0b181abd0ae6e8a)。

用于声明 LC3 单播（Unicast） `8_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga8caa6c9cf34f45ac36f6450d9f076126"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_8_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_8_2_1](#ga8caa6c9cf34f45ac36f6450d9f076126)。

用于声明 LC3 单播（Unicast） `8_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaac67456c95c688b83b460bdcc0c696f1"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_16_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_16_1_1](#gaac67456c95c688b83b460bdcc0c696f1)。

用于声明 LC3 单播（Unicast） `16_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaf5b1892e96c1f63c73dddfeda0843eeb"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_16_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_16_2_1](#gaf5b1892e96c1f63c73dddfeda0843eeb)。

用于声明 LC3 单播（Unicast） `16_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gabb43386a22cd9415c491a846aef85310"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_24_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_24_1_1](#gabb43386a22cd9415c491a846aef85310)。

用于声明 LC3 单播（Unicast） `24_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga24555bc6189ad58f584be0bbbf085e24"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_24_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_24_2_1](#ga24555bc6189ad58f584be0bbbf085e24)。

用于声明 LC3 单播（Unicast） `24_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga39de4252e742ce815633ae7a50062f98"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_32_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_32_1_1](#ga39de4252e742ce815633ae7a50062f98)。

用于声明 LC3 单播（Unicast） `32_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga93a1fbdf0feba790464c41e362aea307"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_32_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_32_2_1](#ga93a1fbdf0feba790464c41e362aea307)。

用于声明 LC3 单播（Unicast） `32_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gae9795a9dc12aa60c74a4aad0c35b18ac"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_441_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_441_1_1](#gae9795a9dc12aa60c74a4aad0c35b18ac)。

用于声明 LC3 单播（Unicast） `441_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga5508e46240176f5b054467609b635f0d"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_441_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_441_2_1](#ga5508e46240176f5b054467609b635f0d)。

用于声明 LC3 单播（Unicast） `441_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaf2ad00922314b8ee06d3a001d1eafd94"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_1_1](#gaf2ad00922314b8ee06d3a001d1eafd94)。

用于声明 LC3 单播（Unicast） `48_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaea3354a3c92d889324f48260216c15bf"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_2_1](#gaea3354a3c92d889324f48260216c15bf)。

用于声明 LC3 单播（Unicast） `48_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gabe085646c5709fcaa2ec830f006105c0"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_3_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_3_1](#gabe085646c5709fcaa2ec830f006105c0)。

用于声明 LC3 单播（Unicast） `48_3_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga5a2c91592853163f3c88d490a8b6bd49"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_4_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_4_1](#ga5a2c91592853163f3c88d490a8b6bd49)。

用于声明 LC3 单播（Unicast） `48_4_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga9dbd2e240b5a733044ab78ec73e6532e"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_5_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_5_1](#ga9dbd2e240b5a733044ab78ec73e6532e)。

用于声明 LC3 单播（Unicast） `48_5_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaa4ee0f200c3484b1708a10ba5f5185a4"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_6_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_6_1](#gaa4ee0f200c3484b1708a10ba5f5185a4)。

用于声明 LC3 单播（Unicast） `48_6_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga332cb00a9cfbf31444b9ca86ecb69cae"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_8_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_8_1_2](#ga332cb00a9cfbf31444b9ca86ecb69cae)。

用于声明 LC3 单播（Unicast） `8_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga945c808feda5dd50d47f78a420c90768"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_8_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_8_2_2](#ga945c808feda5dd50d47f78a420c90768)。

用于声明 LC3 单播（Unicast） `8_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga0191f12d56220dd5ef0842ccd5acbc2c"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_16_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_16_1_2](#ga0191f12d56220dd5ef0842ccd5acbc2c)。

用于声明 LC3 单播（Unicast） `16_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gac4bb73b877cb170ad24f16d422d5752e"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_16_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_16_2_2](#gac4bb73b877cb170ad24f16d422d5752e)。

用于声明 LC3 单播（Unicast） `16_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga9055c137e206deab6c9d756db6dc24b5"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_24_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_24_1_2](#ga9055c137e206deab6c9d756db6dc24b5)。

用于声明 LC3 单播（Unicast） `24_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga3d044b67ae42487129e9df35a79e099e"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_24_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_24_2_2](#ga3d044b67ae42487129e9df35a79e099e)。

用于声明 LC3 单播（Unicast） `24_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga8e99870c84c8fc3bc7f294f534ee9b9d"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_32_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_32_1_2](#ga8e99870c84c8fc3bc7f294f534ee9b9d)。

用于声明 LC3 单播（Unicast） `32_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga01eb8a840451b914b8152f4d90a493c9"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_32_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_32_2_2](#ga01eb8a840451b914b8152f4d90a493c9)。

用于声明 LC3 单播（Unicast） `32_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga70f32a61655cfc1bdd73164902b8b436"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_441_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_441_1_2](#ga70f32a61655cfc1bdd73164902b8b436)。

用于声明 LC3 单播（Unicast） `441_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga66ea64d32c6b28bcf65e991e677f0567"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_441_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_441_2_2](#ga66ea64d32c6b28bcf65e991e677f0567)。

用于声明 LC3 单播（Unicast） `441_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga4efe7f4016a829e3d301108eef8ef93c"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_1_2](#ga4efe7f4016a829e3d301108eef8ef93c)。

用于声明 LC3 单播（Unicast） `48_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga178d09a96e9e0823aed7c8965794ffe3"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_2_2](#ga178d09a96e9e0823aed7c8965794ffe3)。

用于声明 LC3 单播（Unicast） `48_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gabfba888ded2aa54c044e8862d0b95da0"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_3_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_3_2](#gabfba888ded2aa54c044e8862d0b95da0)。

用于声明 LC3 单播（Unicast） `48_3_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga7624cdd35f1eec81c17acf41dd9c85f3"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_4_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_4_2](#ga7624cdd35f1eec81c17acf41dd9c85f3)。

用于声明 LC3 单播（Unicast） `48_4_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gacd6af79c79e587e9c0f858672ec79f49"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_5_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_5_2](#gacd6af79c79e587e9c0f858672ec79f49)。

用于声明 LC3 单播（Unicast） `48_5_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaea427c1bb97174941d7feae359e7f8fd"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_6_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_6_2](#gaea427c1bb97174941d7feae359e7f8fd)。

用于声明 LC3 单播（Unicast） `48_6_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga71551e9a3382c4c3391cdbe3f3b155eb"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_8_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_8_1_1](#ga71551e9a3382c4c3391cdbe3f3b155eb)。

用于声明 LC3 广播（Broadcast） `8_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga09a29e1a76185dfd783d428f862ea8dd"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_8_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_8_2_1](#ga09a29e1a76185dfd783d428f862ea8dd)。

用于声明 LC3 广播（Broadcast） `8_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaa17732bcb085e97856bd5e7a65a3255c"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_16_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_16_1_1](#gaa17732bcb085e97856bd5e7a65a3255c)。

用于声明 LC3 广播（Broadcast） `16_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga8ded042093c310e84ccc76c4d9a67b9c"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_16_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_16_2_1](#ga8ded042093c310e84ccc76c4d9a67b9c)。

用于声明 LC3 广播（Broadcast） `16_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga2a4ccfe1ce99443f2e07ec629e22a1af"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_24_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_24_1_1](#ga2a4ccfe1ce99443f2e07ec629e22a1af)。

用于声明 LC3 广播（Broadcast） `24_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga38c76ab52c627c2d1622b9fd2511367a"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_24_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_24_2_1](#ga38c76ab52c627c2d1622b9fd2511367a)。

用于声明 LC3 广播（Broadcast） `24_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga3842c0a4531a087830d133924542282f"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_32_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_32_1_1](#ga3842c0a4531a087830d133924542282f)。

用于声明 LC3 广播（Broadcast） `32_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga883b0d45657ae3a4902d2c9df3392447"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_32_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_32_2_1](#ga883b0d45657ae3a4902d2c9df3392447)。

用于声明 LC3 广播（Broadcast） `32_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga31f25a4a4549659370bd2d3040aca84a"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_441_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_441_1_1](#ga31f25a4a4549659370bd2d3040aca84a)。

用于声明 LC3 广播（Broadcast） `441_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga09345dd8d9afecfae24aecf760576aeb"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_441_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_441_2_1](#ga09345dd8d9afecfae24aecf760576aeb)。

用于声明 LC3 广播（Broadcast） `441_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gab22a08b23523b080340727261213c8fc"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_1_1](#gab22a08b23523b080340727261213c8fc)。

用于声明 LC3 广播（Broadcast） `48_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga7d280583165d63be595af48fed07309a"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_2_1](#ga7d280583165d63be595af48fed07309a)。

用于声明 LC3 广播（Broadcast） `48_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga8046777cdace9ed5c29d4ce347396c41"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_3_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_3_1](#ga8046777cdace9ed5c29d4ce347396c41)。

用于声明 LC3 广播（Broadcast） `48_3_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gace016322c5fda54a55fa60af45250191"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_4_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_4_1](#gace016322c5fda54a55fa60af45250191)。

用于声明 LC3 广播（Broadcast） `48_4_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaa1c10f0cf98a707e73cb86b05838b60b"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_5_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_5_1](#gaa1c10f0cf98a707e73cb86b05838b60b)。

用于声明 LC3 广播（Broadcast） `48_5_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga729a73a1c6484d7538dd469b2b0f8e5e"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_6_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_6_1](#ga729a73a1c6484d7538dd469b2b0f8e5e)。

用于声明 LC3 广播（Broadcast） `48_6_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga8038c67898c42e0671fb341eedd416d1"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_8_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_8_1_2](#ga8038c67898c42e0671fb341eedd416d1)。

用于声明 LC3 广播（Broadcast） `8_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gac24afbdcea6eadac1123ba4553d79b8b"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_8_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_8_2_2](#gac24afbdcea6eadac1123ba4553d79b8b)。

用于声明 LC3 广播（Broadcast） `8_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaa87f899e5205e7513a2d480ae8e8f448"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_16_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_16_1_2](#gaa87f899e5205e7513a2d480ae8e8f448)。

用于声明 LC3 广播（Broadcast） `16_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga1c0bd6076e559c349bcf3c511d4d5e03"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_16_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_16_2_2](#ga1c0bd6076e559c349bcf3c511d4d5e03)。

用于声明 LC3 广播（Broadcast） `16_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gabc3b1b68ea7da77de6720679084c69db"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_24_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_24_1_2](#gabc3b1b68ea7da77de6720679084c69db)。

用于声明 LC3 广播（Broadcast） `24_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gad435c834787acf0634e4fab408f8965f"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_24_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_24_2_2](#gad435c834787acf0634e4fab408f8965f)。

用于声明 LC3 广播（Broadcast） `24_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga2e89f8a6c6410057c7e5de2a56535e14"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_32_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_32_1_2](#ga2e89f8a6c6410057c7e5de2a56535e14)。

用于声明 LC3 广播（Broadcast） `32_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga2c92af221ebc679c8fdab5ce96b3457c"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_32_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_32_2_2](#ga2c92af221ebc679c8fdab5ce96b3457c)。

用于声明 LC3 广播（Broadcast） `32_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gae2d56f56ad6fbc074dcd7443f4c7d460"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_441_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_441_1_2](#gae2d56f56ad6fbc074dcd7443f4c7d460)。

用于声明 LC3 广播（Broadcast） `441_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gae4ee9d2021680837e3565a0efe4dc500"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_441_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_441_2_2](#gae4ee9d2021680837e3565a0efe4dc500)。

用于声明 LC3 广播（Broadcast） `441_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaa26017b9af7f3cf272b691a636af7ee4"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_1_2](#gaa26017b9af7f3cf272b691a636af7ee4)。

用于声明 LC3 广播（Broadcast） `48_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaca9c3e309005396ccad12aa61b76b84b"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_2_2](#gaca9c3e309005396ccad12aa61b76b84b)。

用于声明 LC3 广播（Broadcast） `48_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaa165b8b8ee72a23734d5f0b0a601e545"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_3_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_3_2](#gaa165b8b8ee72a23734d5f0b0a601e545)。

用于声明 LC3 广播（Broadcast） `48_3_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga309020ab3bfd78b6ce0c2e6b2bf8d556"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_4_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_4_2](#ga309020ab3bfd78b6ce0c2e6b2bf8d556)。

用于声明 LC3 广播（Broadcast） `48_4_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaacf70e1663e6a2d3418e3daae804a6c0"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_5_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_5_2](#gaacf70e1663e6a2d3418e3daae804a6c0)。

用于声明 LC3 广播（Broadcast） `48_5_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga6e3b3a3869024ba1fe4ea8f9047a225d"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_6_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_6_2](#ga6e3b3a3869024ba1fe4ea8f9047a225d)。

用于声明 LC3 广播（Broadcast） `48_6_2` 编解码器配置（Codec Configuration）的辅助宏。

## 1.3\_详细说明（Detailed Documentation）

<a id="gaa17732bcb085e97856bd5e7a65a3255c"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_16_1_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_16_1_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 30U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 30u, 2u, 8u, 40000u))
```

用于声明 LC3 广播（Broadcast） `16_1_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gaa87f899e5205e7513a2d480ae8e8f448"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_16_1_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_16_1_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 30U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 30u, 4u, 45u, 40000u))
```

用于声明 LC3 广播（Broadcast） `16_1_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga8ded042093c310e84ccc76c4d9a67b9c"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_16_2_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_16_2_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 40U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 40u, 2u, 10u, 40000u))
```

用于声明 LC3 广播（Broadcast） `16_2_1` 编解码器配置（Codec Configuration）的辅助宏。

广播源（Broadcast Source）和广播接收端（Broadcast Sink）都必须支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga1c0bd6076e559c349bcf3c511d4d5e03"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_16_2_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_16_2_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 40U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 40u, 4u, 60u, 40000u))
```

用于声明 LC3 广播（Broadcast） `16_2_2` 编解码器配置（Codec Configuration）的辅助宏。

广播源（Broadcast Source）和广播接收端（Broadcast Sink）都必须支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga2a4ccfe1ce99443f2e07ec629e22a1af"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_24_1_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_24_1_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 45U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 45u, 2u, 8u, 40000u))
```

用于声明 LC3 广播（Broadcast） `24_1_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gabc3b1b68ea7da77de6720679084c69db"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_24_1_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_24_1_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 45U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 45u, 4u, 45u, 40000u))
```

用于声明 LC3 广播（Broadcast） `24_1_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga38c76ab52c627c2d1622b9fd2511367a"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_24_2_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_24_2_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 60U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 60u, 2u, 10u, 40000u))
```

用于声明 LC3 广播（Broadcast） `24_2_1` 编解码器配置（Codec Configuration）的辅助宏。

广播接收端（Broadcast Sink）必须支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gad435c834787acf0634e4fab408f8965f"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_24_2_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_24_2_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 60U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 60u, 4u, 60u, 40000u))
```

用于声明 LC3 广播（Broadcast） `24_2_2` 编解码器配置（Codec Configuration）的辅助宏。

广播接收端（Broadcast Sink）必须支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga3842c0a4531a087830d133924542282f"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_32_1_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_32_1_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 60U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 60u, 2u, 8u, 40000u))
```

用于声明 LC3 广播（Broadcast） `32_1_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga2e89f8a6c6410057c7e5de2a56535e14"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_32_1_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_32_1_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 60U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 60u, 4u, 45u, 40000u))
```

用于声明 LC3 广播（Broadcast） `32_1_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga883b0d45657ae3a4902d2c9df3392447"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_32_2_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_32_2_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 80U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 80u, 2u, 10u, 40000u))
```

用于声明 LC3 广播（Broadcast） `32_2_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga2c92af221ebc679c8fdab5ce96b3457c"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_32_2_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_32_2_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 80U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 80u, 4u, 60u, 40000u))
```

用于声明 LC3 广播（Broadcast） `32_2_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga31f25a4a4549659370bd2d3040aca84a"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_441_1_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_441_1_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 97U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_FRAMED(8163u, 97u, 4u, 24u, 40000u))
```

用于声明 LC3 广播（Broadcast） `441_1_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gae2d56f56ad6fbc074dcd7443f4c7d460"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_441_1_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_441_1_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 97U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_FRAMED(8163u, 97u, 4u, 54u, 40000u))
```

用于声明 LC3 广播（Broadcast） `441_1_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga09345dd8d9afecfae24aecf760576aeb"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_441_2_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_441_2_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 130U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_FRAMED(10884u, 130u, 4u, 31u, 40000u))
```

用于声明 LC3 广播（Broadcast） `441_2_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gae4ee9d2021680837e3565a0efe4dc500"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_441_2_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_441_2_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 130U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_FRAMED(10884u, 130u, 4u, 60u, 40000u))
```

用于声明 LC3 广播（Broadcast） `441_2_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gab22a08b23523b080340727261213c8fc"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_48_1_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_1_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 75U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 75u, 4u, 15u, 40000u))
```

用于声明 LC3 广播（Broadcast） `48_1_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gaa26017b9af7f3cf272b691a636af7ee4"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_48_1_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_1_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 75U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 75u, 4u, 50u, 40000u))
```

用于声明 LC3 广播（Broadcast） `48_1_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga7d280583165d63be595af48fed07309a"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_48_2_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_2_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 100U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 100u, 4u, 20u, 40000u))
```

用于声明 LC3 广播（Broadcast） `48_2_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gaca9c3e309005396ccad12aa61b76b84b"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_48_2_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_2_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 100U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 100u, 4u, 65u, 40000u))
```

用于声明 LC3 广播（Broadcast） `48_2_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga8046777cdace9ed5c29d4ce347396c41"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_48_3_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_3_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 90U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 90u, 4u, 15u, 40000u))
```

用于声明 LC3 广播（Broadcast） `48_3_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gaa165b8b8ee72a23734d5f0b0a601e545"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_48_3_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_3_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 90U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 90u, 4u, 50u, 40000u))
```

用于声明 LC3 广播（Broadcast） `48_3_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gace016322c5fda54a55fa60af45250191"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_48_4_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_4_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 120u, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 120u, 4u, 20u, 40000u))
```

用于声明 LC3 广播（Broadcast） `48_4_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga309020ab3bfd78b6ce0c2e6b2bf8d556"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_48_4_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_4_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 120u, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 120u, 4u, 65u, 40000u))
```

用于声明 LC3 广播（Broadcast） `48_4_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gaa1c10f0cf98a707e73cb86b05838b60b"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_48_5_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_5_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 117u,   \
                                            1, _stream_context),                           \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 117u, 4u, 15u, 40000u))
```

用于声明 LC3 广播（Broadcast） `48_5_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gaacf70e1663e6a2d3418e3daae804a6c0"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_48_5_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_5_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 117u,   \
                                            1, _stream_context),                           \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 117u, 4u, 50u, 40000u))
```

用于声明 LC3 广播（Broadcast） `48_5_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga729a73a1c6484d7538dd469b2b0f8e5e"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_48_6_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_6_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 155u, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 155u, 4u, 20u, 40000u))
```

用于声明 LC3 广播（Broadcast） `48_6_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga6e3b3a3869024ba1fe4ea8f9047a225d"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_48_6_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_6_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 155u, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 155u, 4u, 65u, 40000u))
```

用于声明 LC3 广播（Broadcast） `48_6_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga71551e9a3382c4c3391cdbe3f3b155eb"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_8_1_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_8_1_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 26u, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 26u, 2u, 8u, 40000u))
```

用于声明 LC3 广播（Broadcast） `8_1_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga8038c67898c42e0671fb341eedd416d1"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_8_1_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_8_1_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 26u, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 26u, 4u, 45u, 40000u))
```

用于声明 LC3 广播（Broadcast） `8_1_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga09a29e1a76185dfd783d428f862ea8dd"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_8_2_1`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_8_2_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 30U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 30u, 2u, 10u, 40000u))
```

用于声明 LC3 广播（Broadcast） `8_2_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gac24afbdcea6eadac1123ba4553d79b8b"></a>

### `BT_BAP_LC3_BROADCAST_PRESET_8_2_2`

```c
#define BT_BAP_LC3_BROADCAST_PRESET_8_2_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 30U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 30u, 4u, 60u, 40000u))
```

用于声明 LC3 广播（Broadcast） `8_2_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga9f2075cd5019d356bc7ccf7f9cbc63bb"></a>

### `BT_BAP_LC3_PRESET`

```c
#define BT_BAP_LC3_PRESET ( _codec, _qos )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
{                                                                                          \
        .codec_cfg = _codec, .qos = _qos,                                                  \
}
```

用于声明 LC3 预设结构体（Preset Structure）的辅助宏。

<a id="gaac67456c95c688b83b460bdcc0c696f1"></a>

### `BT_BAP_LC3_UNICAST_PRESET_16_1_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_16_1_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 30U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 30u, 2u, 8u, 40000u))
```

用于声明 LC3 单播（Unicast） `16_1_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga0191f12d56220dd5ef0842ccd5acbc2c"></a>

### `BT_BAP_LC3_UNICAST_PRESET_16_1_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_16_1_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 30U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 30u, 13u, 75u, 40000u))
```

用于声明 LC3 单播（Unicast） `16_1_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gaf5b1892e96c1f63c73dddfeda0843eeb"></a>

### `BT_BAP_LC3_UNICAST_PRESET_16_2_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_16_2_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 40U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 40u, 2u, 10u, 40000u))
```

用于声明 LC3 单播（Unicast） `16_2_1` 编解码器配置（Codec Configuration）的辅助宏。

单播客户端和服务器（Unicast Client and Server）均必须支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gac4bb73b877cb170ad24f16d422d5752e"></a>

### `BT_BAP_LC3_UNICAST_PRESET_16_2_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_16_2_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_16KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 40U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 40u, 13u, 95u, 40000u))
```

用于声明 LC3 单播（Unicast） `16_2_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gabb43386a22cd9415c491a846aef85310"></a>

### `BT_BAP_LC3_UNICAST_PRESET_24_1_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_24_1_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 45U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 45u, 2u, 8u, 40000u))
```

用于声明 LC3 单播（Unicast） `24_1_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga9055c137e206deab6c9d756db6dc24b5"></a>

### `BT_BAP_LC3_UNICAST_PRESET_24_1_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_24_1_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 45U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 45u, 13u, 75u, 40000u))
```

用于声明 LC3 单播（Unicast） `24_1_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga24555bc6189ad58f584be0bbbf085e24"></a>

### `BT_BAP_LC3_UNICAST_PRESET_24_2_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_24_2_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 60U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 60u, 2u, 10u, 40000u))
```

用于声明 LC3 单播（Unicast） `24_2_1` 编解码器配置（Codec Configuration）的辅助宏。

单播服务器（Unicast Server）必须支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga3d044b67ae42487129e9df35a79e099e"></a>

### `BT_BAP_LC3_UNICAST_PRESET_24_2_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_24_2_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_24KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 60U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 60u, 13u, 95u, 40000u))
```

用于声明 LC3 单播（Unicast） `24_2_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga39de4252e742ce815633ae7a50062f98"></a>

### `BT_BAP_LC3_UNICAST_PRESET_32_1_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_32_1_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 60U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 60u, 2u, 8u, 40000u))
```

用于声明 LC3 单播（Unicast） `32_1_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga8e99870c84c8fc3bc7f294f534ee9b9d"></a>

### `BT_BAP_LC3_UNICAST_PRESET_32_1_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_32_1_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 60U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 60u, 13u, 75u, 40000u))
```

用于声明 LC3 单播（Unicast） `32_1_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga93a1fbdf0feba790464c41e362aea307"></a>

### `BT_BAP_LC3_UNICAST_PRESET_32_2_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_32_2_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 80U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 80u, 2u, 10u, 40000u))
```

用于声明 LC3 单播（Unicast） `32_2_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga01eb8a840451b914b8152f4d90a493c9"></a>

### `BT_BAP_LC3_UNICAST_PRESET_32_2_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_32_2_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_32KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 80U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 80u, 13u, 95u, 40000u))
```

用于声明 LC3 单播（Unicast） `32_2_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gae9795a9dc12aa60c74a4aad0c35b18ac"></a>

### `BT_BAP_LC3_UNICAST_PRESET_441_1_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_441_1_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 97U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_FRAMED(8163u, 97u, 5u, 24u, 40000u))
```

用于声明 LC3 单播（Unicast） `441_1_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga70f32a61655cfc1bdd73164902b8b436"></a>

### `BT_BAP_LC3_UNICAST_PRESET_441_1_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_441_1_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 97U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_FRAMED(8163u, 97u, 13u, 80u, 40000u))
```

用于声明 LC3 单播（Unicast） `441_1_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga5508e46240176f5b054467609b635f0d"></a>

### `BT_BAP_LC3_UNICAST_PRESET_441_2_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_441_2_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 130U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_FRAMED(10884u, 130u, 5u, 31u, 40000u))
```

用于声明 LC3 单播（Unicast） `441_2_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga66ea64d32c6b28bcf65e991e677f0567"></a>

### `BT_BAP_LC3_UNICAST_PRESET_441_2_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_441_2_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_44KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 130U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_FRAMED(10884u, 130u, 13u, 85u, 40000u))
```

用于声明 LC3 单播（Unicast） `441_2_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gaf2ad00922314b8ee06d3a001d1eafd94"></a>

### `BT_BAP_LC3_UNICAST_PRESET_48_1_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_1_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 75U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 75u, 5u, 15u, 40000u))
```

用于声明 LC3 单播（Unicast） `48_1_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga4efe7f4016a829e3d301108eef8ef93c"></a>

### `BT_BAP_LC3_UNICAST_PRESET_48_1_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_1_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 75U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 75u, 13u, 75u, 40000u))
```

用于声明 LC3 单播（Unicast） `48_1_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gaea3354a3c92d889324f48260216c15bf"></a>

### `BT_BAP_LC3_UNICAST_PRESET_48_2_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_2_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 100U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 100u, 5u, 20u, 40000u))
```

用于声明 LC3 单播（Unicast） `48_2_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga178d09a96e9e0823aed7c8965794ffe3"></a>

### `BT_BAP_LC3_UNICAST_PRESET_48_2_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_2_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 100U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 100u, 13u, 95u, 40000u))
```

用于声明 LC3 单播（Unicast） `48_2_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gabe085646c5709fcaa2ec830f006105c0"></a>

### `BT_BAP_LC3_UNICAST_PRESET_48_3_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_3_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 90U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 90u, 5u, 15u, 40000u))
```

用于声明 LC3 单播（Unicast） `48_3_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gabfba888ded2aa54c044e8862d0b95da0"></a>

### `BT_BAP_LC3_UNICAST_PRESET_48_3_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_3_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 90U, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 90u, 13u, 75u, 40000u))
```

用于声明 LC3 单播（Unicast） `48_3_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga5a2c91592853163f3c88d490a8b6bd49"></a>

### `BT_BAP_LC3_UNICAST_PRESET_48_4_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_4_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 120u, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 120u, 5u, 20u, 40000u))
```

用于声明 LC3 单播（Unicast） `48_4_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga7624cdd35f1eec81c17acf41dd9c85f3"></a>

### `BT_BAP_LC3_UNICAST_PRESET_48_4_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_4_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 120u, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 120u, 13u, 100u, 40000u))
```

用于声明 LC3 单播（Unicast） `48_4_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga9dbd2e240b5a733044ab78ec73e6532e"></a>

### `BT_BAP_LC3_UNICAST_PRESET_48_5_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_5_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 117u,   \
                                            1, _stream_context),                           \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 117u, 5u, 15u, 40000u))
```

用于声明 LC3 单播（Unicast） `48_5_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gacd6af79c79e587e9c0f858672ec79f49"></a>

### `BT_BAP_LC3_UNICAST_PRESET_48_5_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_5_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 117u,   \
                                            1, _stream_context),                           \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 117u, 13u, 75u, 40000u))
```

用于声明 LC3 单播（Unicast） `48_5_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gaa4ee0f200c3484b1708a10ba5f5185a4"></a>

### `BT_BAP_LC3_UNICAST_PRESET_48_6_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_6_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 155u, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 155u, 5u, 20u, 40000u))
```

用于声明 LC3 单播（Unicast） `48_6_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gaea427c1bb97174941d7feae359e7f8fd"></a>

### `BT_BAP_LC3_UNICAST_PRESET_48_6_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_6_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_48KHZ,                 \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 155u, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 155u, 13u, 100u, 40000u))
```

用于声明 LC3 单播（Unicast） `48_6_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="gac1a211ed3116a0b7f0b181abd0ae6e8a"></a>

### `BT_BAP_LC3_UNICAST_PRESET_8_1_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_8_1_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 26u, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 26u, 2u, 8u, 40000u))
```

用于声明 LC3 单播（Unicast） `8_1_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga332cb00a9cfbf31444b9ca86ecb69cae"></a>

### `BT_BAP_LC3_UNICAST_PRESET_8_1_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_8_1_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                            BT_AUDIO_CODEC_CFG_DURATION_7_5, _loc, 26u, 1, \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(7500u, 26u, 13u, 75u, 40000u))
```

用于声明 LC3 单播（Unicast） `8_1_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga8caa6c9cf34f45ac36f6450d9f076126"></a>

### `BT_BAP_LC3_UNICAST_PRESET_8_2_1`

```c
#define BT_BAP_LC3_UNICAST_PRESET_8_2_1 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 30U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 30u, 2u, 10u, 40000u))
```

用于声明 LC3 单播（Unicast） `8_2_1` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |

<a id="ga945c808feda5dd50d47f78a420c90768"></a>

### `BT_BAP_LC3_UNICAST_PRESET_8_2_2`

```c
#define BT_BAP_LC3_UNICAST_PRESET_8_2_2 ( _loc, _stream_context )
```

```c
#include <zephyr/bluetooth/audio/bap_lc3_preset.h>
```

展开值（Value）：

```c
BT_BAP_LC3_PRESET(BT_AUDIO_CODEC_LC3_CONFIG(BT_AUDIO_CODEC_CFG_FREQ_8KHZ,                  \
                                            BT_AUDIO_CODEC_CFG_DURATION_10, _loc, 30U, 1,  \
                                            _stream_context),                              \
                  BT_BAP_QOS_CFG_UNFRAMED(10000u, 30u, 13u, 95u, 40000u))
```

用于声明 LC3 单播（Unicast） `8_2_2` 编解码器配置（Codec Configuration）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_loc` | 音频通道位置位域（Audio Channel Location Bitfield），即 `bt_audio_location`。 |
| `_stream_context` | 流上下文（Stream Context），即 `BT_AUDIO_CONTEXT_*`。 |


## 1.4\_原页交叉引用（Cross References）

- [bt_bap_lc3_preset](../bluetooth_le_audio_model_reference/P026_bt_bap_lc3_preset_结构体.md)
- [zephyr/bluetooth/audio/bap_lc3_preset.h](../api_file_gap_modem_reference/P001_zephyr__bluetooth__audio__bap_lc3_preset.h_文件参考.md)
- [BT_AUDIO_CODEC_LC3_CONFIG](../api_transport_control_topic_reference/P003_蓝牙 LC3 编解码器（Bluetooth LC3 codec）.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)
- [BT_AUDIO_CODEC_CFG_FREQ_16KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245)
- [BT_AUDIO_CODEC_CFG_DURATION_7_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272)
- [BT_BAP_QOS_CFG_UNFRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gae578c78a10df4d1e4e6d1781ca48e1f5)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [BT_AUDIO_CODEC_CFG_DURATION_10](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7)
- [BT_AUDIO_CODEC_CFG_FREQ_24KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275)
- [BT_AUDIO_CODEC_CFG_FREQ_32KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e)
- [BT_AUDIO_CODEC_CFG_FREQ_44KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84)
- [BT_BAP_QOS_CFG_FRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa91c55ca2de3ddf09620948fd4914b14)
- [BT_AUDIO_CODEC_CFG_FREQ_48KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11)
- [BT_AUDIO_CODEC_CFG_FREQ_8KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245"></a>
<a id="agroup__bt__bap__lc3__preset_html_ga9f2075cd5019d356bc7ccf7f9cbc63bb"></a>
<a id="agroup__bt__bap_html_gae578c78a10df4d1e4e6d1781ca48e1f5"></a>
<a id="agroup__bt__lc3_html_ga2c5f1f9e6d80a2eef93f7b08a19ea245"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84"></a>
<a id="agroup__bt__bap_html_gaa91c55ca2de3ddf09620948fd4914b14"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a"></a>

---

[返回大纲](大纲.md) · [下一章](P002_免提配置文件（Hands Free Profile，HFP）.md)
