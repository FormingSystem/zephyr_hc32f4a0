---
id: learning.zephyr-docs.api-file-gap-modem-reference.page-1
title: zephyr__bluetooth__audio__bap_lc3_preset.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bap__lc3__preset_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_audio\_\_bap\_lc3\_preset.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bap__lc3__preset_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙BAP的LC3预设（Presets）的头文件。

<a id="details"></a>

```c
#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/audio/bap.h>
#include <zephyr/bluetooth/audio/lc3.h>
```

查看此文件的源码。

蓝牙基本音频配置文件（Basic Audio Profile，BAP）的 LC3 预设（Presets）头文件。Copyright (c) 2023-2024 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。

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

相关声明：[BT_BAP_LC3_PRESET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga9f2075cd5019d356bc7ccf7f9cbc63bb)。

用于声明 LC3 预设结构体（Preset Structure）的辅助宏。

<a id="r_gac1a211ed3116a0b7f0b181abd0ae6e8a"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_8_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_8_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gac1a211ed3116a0b7f0b181abd0ae6e8a)。

用于声明 LC3 单播（Unicast） `8_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga8caa6c9cf34f45ac36f6450d9f076126"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_8_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_8_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga8caa6c9cf34f45ac36f6450d9f076126)。

用于声明 LC3 单播（Unicast） `8_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaac67456c95c688b83b460bdcc0c696f1"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_16_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_16_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaac67456c95c688b83b460bdcc0c696f1)。

用于声明 LC3 单播（Unicast） `16_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaf5b1892e96c1f63c73dddfeda0843eeb"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_16_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_16_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaf5b1892e96c1f63c73dddfeda0843eeb)。

用于声明 LC3 单播（Unicast） `16_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gabb43386a22cd9415c491a846aef85310"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_24_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_24_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gabb43386a22cd9415c491a846aef85310)。

用于声明 LC3 单播（Unicast） `24_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga24555bc6189ad58f584be0bbbf085e24"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_24_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_24_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga24555bc6189ad58f584be0bbbf085e24)。

用于声明 LC3 单播（Unicast） `24_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga39de4252e742ce815633ae7a50062f98"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_32_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_32_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga39de4252e742ce815633ae7a50062f98)。

用于声明 LC3 单播（Unicast） `32_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga93a1fbdf0feba790464c41e362aea307"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_32_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_32_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga93a1fbdf0feba790464c41e362aea307)。

用于声明 LC3 单播（Unicast） `32_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gae9795a9dc12aa60c74a4aad0c35b18ac"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_441_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_441_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gae9795a9dc12aa60c74a4aad0c35b18ac)。

用于声明 LC3 单播（Unicast） `441_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga5508e46240176f5b054467609b635f0d"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_441_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_441_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga5508e46240176f5b054467609b635f0d)。

用于声明 LC3 单播（Unicast） `441_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaf2ad00922314b8ee06d3a001d1eafd94"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaf2ad00922314b8ee06d3a001d1eafd94)。

用于声明 LC3 单播（Unicast） `48_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaea3354a3c92d889324f48260216c15bf"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaea3354a3c92d889324f48260216c15bf)。

用于声明 LC3 单播（Unicast） `48_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gabe085646c5709fcaa2ec830f006105c0"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_3_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_3_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gabe085646c5709fcaa2ec830f006105c0)。

用于声明 LC3 单播（Unicast） `48_3_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga5a2c91592853163f3c88d490a8b6bd49"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_4_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_4_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga5a2c91592853163f3c88d490a8b6bd49)。

用于声明 LC3 单播（Unicast） `48_4_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga9dbd2e240b5a733044ab78ec73e6532e"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_5_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_5_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga9dbd2e240b5a733044ab78ec73e6532e)。

用于声明 LC3 单播（Unicast） `48_5_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaa4ee0f200c3484b1708a10ba5f5185a4"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_6_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_6_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaa4ee0f200c3484b1708a10ba5f5185a4)。

用于声明 LC3 单播（Unicast） `48_6_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga332cb00a9cfbf31444b9ca86ecb69cae"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_8_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_8_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga332cb00a9cfbf31444b9ca86ecb69cae)。

用于声明 LC3 单播（Unicast） `8_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga945c808feda5dd50d47f78a420c90768"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_8_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_8_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga945c808feda5dd50d47f78a420c90768)。

用于声明 LC3 单播（Unicast） `8_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga0191f12d56220dd5ef0842ccd5acbc2c"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_16_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_16_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga0191f12d56220dd5ef0842ccd5acbc2c)。

用于声明 LC3 单播（Unicast） `16_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gac4bb73b877cb170ad24f16d422d5752e"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_16_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_16_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gac4bb73b877cb170ad24f16d422d5752e)。

用于声明 LC3 单播（Unicast） `16_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga9055c137e206deab6c9d756db6dc24b5"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_24_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_24_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga9055c137e206deab6c9d756db6dc24b5)。

用于声明 LC3 单播（Unicast） `24_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga3d044b67ae42487129e9df35a79e099e"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_24_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_24_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga3d044b67ae42487129e9df35a79e099e)。

用于声明 LC3 单播（Unicast） `24_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga8e99870c84c8fc3bc7f294f534ee9b9d"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_32_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_32_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga8e99870c84c8fc3bc7f294f534ee9b9d)。

用于声明 LC3 单播（Unicast） `32_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga01eb8a840451b914b8152f4d90a493c9"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_32_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_32_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga01eb8a840451b914b8152f4d90a493c9)。

用于声明 LC3 单播（Unicast） `32_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga70f32a61655cfc1bdd73164902b8b436"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_441_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_441_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga70f32a61655cfc1bdd73164902b8b436)。

用于声明 LC3 单播（Unicast） `441_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga66ea64d32c6b28bcf65e991e677f0567"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_441_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_441_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga66ea64d32c6b28bcf65e991e677f0567)。

用于声明 LC3 单播（Unicast） `441_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga4efe7f4016a829e3d301108eef8ef93c"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga4efe7f4016a829e3d301108eef8ef93c)。

用于声明 LC3 单播（Unicast） `48_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga178d09a96e9e0823aed7c8965794ffe3"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga178d09a96e9e0823aed7c8965794ffe3)。

用于声明 LC3 单播（Unicast） `48_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gabfba888ded2aa54c044e8862d0b95da0"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_3_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_3_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gabfba888ded2aa54c044e8862d0b95da0)。

用于声明 LC3 单播（Unicast） `48_3_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga7624cdd35f1eec81c17acf41dd9c85f3"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_4_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_4_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga7624cdd35f1eec81c17acf41dd9c85f3)。

用于声明 LC3 单播（Unicast） `48_4_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gacd6af79c79e587e9c0f858672ec79f49"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_5_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_5_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gacd6af79c79e587e9c0f858672ec79f49)。

用于声明 LC3 单播（Unicast） `48_5_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaea427c1bb97174941d7feae359e7f8fd"></a>

```c
#define BT_BAP_LC3_UNICAST_PRESET_48_6_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_UNICAST_PRESET_48_6_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaea427c1bb97174941d7feae359e7f8fd)。

用于声明 LC3 单播（Unicast） `48_6_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga71551e9a3382c4c3391cdbe3f3b155eb"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_8_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_8_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga71551e9a3382c4c3391cdbe3f3b155eb)。

用于声明 LC3 广播（Broadcast） `8_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga09a29e1a76185dfd783d428f862ea8dd"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_8_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_8_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga09a29e1a76185dfd783d428f862ea8dd)。

用于声明 LC3 广播（Broadcast） `8_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaa17732bcb085e97856bd5e7a65a3255c"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_16_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_16_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaa17732bcb085e97856bd5e7a65a3255c)。

用于声明 LC3 广播（Broadcast） `16_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga8ded042093c310e84ccc76c4d9a67b9c"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_16_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_16_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga8ded042093c310e84ccc76c4d9a67b9c)。

用于声明 LC3 广播（Broadcast） `16_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga2a4ccfe1ce99443f2e07ec629e22a1af"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_24_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_24_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga2a4ccfe1ce99443f2e07ec629e22a1af)。

用于声明 LC3 广播（Broadcast） `24_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga38c76ab52c627c2d1622b9fd2511367a"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_24_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_24_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga38c76ab52c627c2d1622b9fd2511367a)。

用于声明 LC3 广播（Broadcast） `24_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga3842c0a4531a087830d133924542282f"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_32_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_32_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga3842c0a4531a087830d133924542282f)。

用于声明 LC3 广播（Broadcast） `32_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga883b0d45657ae3a4902d2c9df3392447"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_32_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_32_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga883b0d45657ae3a4902d2c9df3392447)。

用于声明 LC3 广播（Broadcast） `32_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga31f25a4a4549659370bd2d3040aca84a"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_441_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_441_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga31f25a4a4549659370bd2d3040aca84a)。

用于声明 LC3 广播（Broadcast） `441_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga09345dd8d9afecfae24aecf760576aeb"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_441_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_441_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga09345dd8d9afecfae24aecf760576aeb)。

用于声明 LC3 广播（Broadcast） `441_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gab22a08b23523b080340727261213c8fc"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_1_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gab22a08b23523b080340727261213c8fc)。

用于声明 LC3 广播（Broadcast） `48_1_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga7d280583165d63be595af48fed07309a"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_2_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga7d280583165d63be595af48fed07309a)。

用于声明 LC3 广播（Broadcast） `48_2_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga8046777cdace9ed5c29d4ce347396c41"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_3_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_3_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga8046777cdace9ed5c29d4ce347396c41)。

用于声明 LC3 广播（Broadcast） `48_3_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gace016322c5fda54a55fa60af45250191"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_4_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_4_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gace016322c5fda54a55fa60af45250191)。

用于声明 LC3 广播（Broadcast） `48_4_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaa1c10f0cf98a707e73cb86b05838b60b"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_5_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_5_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaa1c10f0cf98a707e73cb86b05838b60b)。

用于声明 LC3 广播（Broadcast） `48_5_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga729a73a1c6484d7538dd469b2b0f8e5e"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_6_1(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_6_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga729a73a1c6484d7538dd469b2b0f8e5e)。

用于声明 LC3 广播（Broadcast） `48_6_1` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga8038c67898c42e0671fb341eedd416d1"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_8_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_8_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga8038c67898c42e0671fb341eedd416d1)。

用于声明 LC3 广播（Broadcast） `8_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gac24afbdcea6eadac1123ba4553d79b8b"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_8_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_8_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gac24afbdcea6eadac1123ba4553d79b8b)。

用于声明 LC3 广播（Broadcast） `8_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaa87f899e5205e7513a2d480ae8e8f448"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_16_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_16_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaa87f899e5205e7513a2d480ae8e8f448)。

用于声明 LC3 广播（Broadcast） `16_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga1c0bd6076e559c349bcf3c511d4d5e03"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_16_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_16_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga1c0bd6076e559c349bcf3c511d4d5e03)。

用于声明 LC3 广播（Broadcast） `16_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gabc3b1b68ea7da77de6720679084c69db"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_24_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_24_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gabc3b1b68ea7da77de6720679084c69db)。

用于声明 LC3 广播（Broadcast） `24_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gad435c834787acf0634e4fab408f8965f"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_24_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_24_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gad435c834787acf0634e4fab408f8965f)。

用于声明 LC3 广播（Broadcast） `24_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga2e89f8a6c6410057c7e5de2a56535e14"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_32_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_32_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga2e89f8a6c6410057c7e5de2a56535e14)。

用于声明 LC3 广播（Broadcast） `32_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga2c92af221ebc679c8fdab5ce96b3457c"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_32_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_32_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga2c92af221ebc679c8fdab5ce96b3457c)。

用于声明 LC3 广播（Broadcast） `32_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gae2d56f56ad6fbc074dcd7443f4c7d460"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_441_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_441_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gae2d56f56ad6fbc074dcd7443f4c7d460)。

用于声明 LC3 广播（Broadcast） `441_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gae4ee9d2021680837e3565a0efe4dc500"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_441_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_441_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gae4ee9d2021680837e3565a0efe4dc500)。

用于声明 LC3 广播（Broadcast） `441_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaa26017b9af7f3cf272b691a636af7ee4"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_1_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaa26017b9af7f3cf272b691a636af7ee4)。

用于声明 LC3 广播（Broadcast） `48_1_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaca9c3e309005396ccad12aa61b76b84b"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_2_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaca9c3e309005396ccad12aa61b76b84b)。

用于声明 LC3 广播（Broadcast） `48_2_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaa165b8b8ee72a23734d5f0b0a601e545"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_3_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_3_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaa165b8b8ee72a23734d5f0b0a601e545)。

用于声明 LC3 广播（Broadcast） `48_3_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga309020ab3bfd78b6ce0c2e6b2bf8d556"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_4_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_4_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga309020ab3bfd78b6ce0c2e6b2bf8d556)。

用于声明 LC3 广播（Broadcast） `48_4_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_gaacf70e1663e6a2d3418e3daae804a6c0"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_5_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_5_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaacf70e1663e6a2d3418e3daae804a6c0)。

用于声明 LC3 广播（Broadcast） `48_5_2` 编解码器配置（Codec Configuration）的辅助宏。

<a id="r_ga6e3b3a3869024ba1fe4ea8f9047a225d"></a>

```c
#define BT_BAP_LC3_BROADCAST_PRESET_48_6_2(_loc, _stream_context)
```

相关声明：[BT_BAP_LC3_BROADCAST_PRESET_48_6_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga6e3b3a3869024ba1fe4ea8f9047a225d)。

用于声明 LC3 广播（Broadcast） `48_6_2` 编解码器配置（Codec Configuration）的辅助宏。


## 1.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/audio.h](../api_source_compiler_device_reference/P002_audio.h_源码浏览.md)
- [zephyr/bluetooth/audio/bap.h](../api_source_transport_clock_reference/P003_bap.h_源码浏览.md)
- [zephyr/bluetooth/audio/lc3.h](../api_source_reference/P437_lc3.h_源码浏览.md)
- [查看此文件的源码。](../api_source_device_reference/P001_bap_lc3_preset.h_源码浏览.md)
- [bt_bap_lc3_preset](../bluetooth_le_audio_model_reference/P026_bt_bap_lc3_preset_结构体.md)
- [BT_BAP_LC3_PRESET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga9f2075cd5019d356bc7ccf7f9cbc63bb)
- [BT_BAP_LC3_UNICAST_PRESET_8_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gac1a211ed3116a0b7f0b181abd0ae6e8a)
- [BT_BAP_LC3_UNICAST_PRESET_8_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga8caa6c9cf34f45ac36f6450d9f076126)
- [BT_BAP_LC3_UNICAST_PRESET_16_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaac67456c95c688b83b460bdcc0c696f1)
- [BT_BAP_LC3_UNICAST_PRESET_16_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaf5b1892e96c1f63c73dddfeda0843eeb)
- [BT_BAP_LC3_UNICAST_PRESET_24_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gabb43386a22cd9415c491a846aef85310)
- [BT_BAP_LC3_UNICAST_PRESET_24_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga24555bc6189ad58f584be0bbbf085e24)
- [BT_BAP_LC3_UNICAST_PRESET_32_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga39de4252e742ce815633ae7a50062f98)
- [BT_BAP_LC3_UNICAST_PRESET_32_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga93a1fbdf0feba790464c41e362aea307)
- [BT_BAP_LC3_UNICAST_PRESET_441_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gae9795a9dc12aa60c74a4aad0c35b18ac)
- [BT_BAP_LC3_UNICAST_PRESET_441_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga5508e46240176f5b054467609b635f0d)
- [BT_BAP_LC3_UNICAST_PRESET_48_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaf2ad00922314b8ee06d3a001d1eafd94)
- [BT_BAP_LC3_UNICAST_PRESET_48_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaea3354a3c92d889324f48260216c15bf)
- [BT_BAP_LC3_UNICAST_PRESET_48_3_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gabe085646c5709fcaa2ec830f006105c0)
- [BT_BAP_LC3_UNICAST_PRESET_48_4_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga5a2c91592853163f3c88d490a8b6bd49)
- [BT_BAP_LC3_UNICAST_PRESET_48_5_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga9dbd2e240b5a733044ab78ec73e6532e)
- [BT_BAP_LC3_UNICAST_PRESET_48_6_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaa4ee0f200c3484b1708a10ba5f5185a4)
- [BT_BAP_LC3_UNICAST_PRESET_8_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga332cb00a9cfbf31444b9ca86ecb69cae)
- [BT_BAP_LC3_UNICAST_PRESET_8_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga945c808feda5dd50d47f78a420c90768)
- [BT_BAP_LC3_UNICAST_PRESET_16_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga0191f12d56220dd5ef0842ccd5acbc2c)
- [BT_BAP_LC3_UNICAST_PRESET_16_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gac4bb73b877cb170ad24f16d422d5752e)
- [BT_BAP_LC3_UNICAST_PRESET_24_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga9055c137e206deab6c9d756db6dc24b5)
- [BT_BAP_LC3_UNICAST_PRESET_24_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga3d044b67ae42487129e9df35a79e099e)
- [BT_BAP_LC3_UNICAST_PRESET_32_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga8e99870c84c8fc3bc7f294f534ee9b9d)
- [BT_BAP_LC3_UNICAST_PRESET_32_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga01eb8a840451b914b8152f4d90a493c9)
- [BT_BAP_LC3_UNICAST_PRESET_441_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga70f32a61655cfc1bdd73164902b8b436)
- [BT_BAP_LC3_UNICAST_PRESET_441_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga66ea64d32c6b28bcf65e991e677f0567)
- [BT_BAP_LC3_UNICAST_PRESET_48_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga4efe7f4016a829e3d301108eef8ef93c)
- [BT_BAP_LC3_UNICAST_PRESET_48_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga178d09a96e9e0823aed7c8965794ffe3)
- [BT_BAP_LC3_UNICAST_PRESET_48_3_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gabfba888ded2aa54c044e8862d0b95da0)
- [BT_BAP_LC3_UNICAST_PRESET_48_4_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga7624cdd35f1eec81c17acf41dd9c85f3)
- [BT_BAP_LC3_UNICAST_PRESET_48_5_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gacd6af79c79e587e9c0f858672ec79f49)
- [BT_BAP_LC3_UNICAST_PRESET_48_6_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaea427c1bb97174941d7feae359e7f8fd)
- [BT_BAP_LC3_BROADCAST_PRESET_8_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga71551e9a3382c4c3391cdbe3f3b155eb)
- [BT_BAP_LC3_BROADCAST_PRESET_8_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga09a29e1a76185dfd783d428f862ea8dd)
- [BT_BAP_LC3_BROADCAST_PRESET_16_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaa17732bcb085e97856bd5e7a65a3255c)
- [BT_BAP_LC3_BROADCAST_PRESET_16_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga8ded042093c310e84ccc76c4d9a67b9c)
- [BT_BAP_LC3_BROADCAST_PRESET_24_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga2a4ccfe1ce99443f2e07ec629e22a1af)
- [BT_BAP_LC3_BROADCAST_PRESET_24_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga38c76ab52c627c2d1622b9fd2511367a)
- [BT_BAP_LC3_BROADCAST_PRESET_32_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga3842c0a4531a087830d133924542282f)
- [BT_BAP_LC3_BROADCAST_PRESET_32_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga883b0d45657ae3a4902d2c9df3392447)
- [BT_BAP_LC3_BROADCAST_PRESET_441_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga31f25a4a4549659370bd2d3040aca84a)
- [BT_BAP_LC3_BROADCAST_PRESET_441_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga09345dd8d9afecfae24aecf760576aeb)
- [BT_BAP_LC3_BROADCAST_PRESET_48_1_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gab22a08b23523b080340727261213c8fc)
- [BT_BAP_LC3_BROADCAST_PRESET_48_2_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga7d280583165d63be595af48fed07309a)
- [BT_BAP_LC3_BROADCAST_PRESET_48_3_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga8046777cdace9ed5c29d4ce347396c41)
- [BT_BAP_LC3_BROADCAST_PRESET_48_4_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gace016322c5fda54a55fa60af45250191)
- [BT_BAP_LC3_BROADCAST_PRESET_48_5_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaa1c10f0cf98a707e73cb86b05838b60b)
- [BT_BAP_LC3_BROADCAST_PRESET_48_6_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga729a73a1c6484d7538dd469b2b0f8e5e)
- [BT_BAP_LC3_BROADCAST_PRESET_8_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga8038c67898c42e0671fb341eedd416d1)
- [BT_BAP_LC3_BROADCAST_PRESET_8_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gac24afbdcea6eadac1123ba4553d79b8b)
- [BT_BAP_LC3_BROADCAST_PRESET_16_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaa87f899e5205e7513a2d480ae8e8f448)
- [BT_BAP_LC3_BROADCAST_PRESET_16_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga1c0bd6076e559c349bcf3c511d4d5e03)
- [BT_BAP_LC3_BROADCAST_PRESET_24_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gabc3b1b68ea7da77de6720679084c69db)
- [BT_BAP_LC3_BROADCAST_PRESET_24_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gad435c834787acf0634e4fab408f8965f)
- [BT_BAP_LC3_BROADCAST_PRESET_32_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga2e89f8a6c6410057c7e5de2a56535e14)
- [BT_BAP_LC3_BROADCAST_PRESET_32_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga2c92af221ebc679c8fdab5ce96b3457c)
- [BT_BAP_LC3_BROADCAST_PRESET_441_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gae2d56f56ad6fbc074dcd7443f4c7d460)
- [BT_BAP_LC3_BROADCAST_PRESET_441_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gae4ee9d2021680837e3565a0efe4dc500)
- [BT_BAP_LC3_BROADCAST_PRESET_48_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaa26017b9af7f3cf272b691a636af7ee4)
- [BT_BAP_LC3_BROADCAST_PRESET_48_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaca9c3e309005396ccad12aa61b76b84b)
- [BT_BAP_LC3_BROADCAST_PRESET_48_3_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaa165b8b8ee72a23734d5f0b0a601e545)
- [BT_BAP_LC3_BROADCAST_PRESET_48_4_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga309020ab3bfd78b6ce0c2e6b2bf8d556)
- [BT_BAP_LC3_BROADCAST_PRESET_48_5_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#gaacf70e1663e6a2d3418e3daae804a6c0)
- [BT_BAP_LC3_BROADCAST_PRESET_48_6_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html#ga6e3b3a3869024ba1fe4ea8f9047a225d)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__bluetooth__gap.h_文件参考.md)
