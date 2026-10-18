---
id: learning.zephyr-docs.api-bluetooth-service-control-reference.page-1
title: 通用音频分配编号（Generic Audio Assigned Numbers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_通用音频分配编号（Generic Audio Assigned Numbers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用音频分配编号（Generic Audio Assigned Numbers）

<a id="details"></a>

通用音频分配编号（Generic Audio Assigned Numbers）

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_gac1251f8a35b5e343eeeff87f22f8ab10"></a>

```c
#define BT_AUDIO_CODEC_CAP_CHAN_COUNT_MIN 1
```

相关声明：[BT_AUDIO_CODEC_CAP_CHAN_COUNT_MIN](#gac1251f8a35b5e343eeeff87f22f8ab10)。

支持的最小声道数（Channel Count）。

<a id="r_gad91341739d394f92ffc4988b614f47b6"></a>

```c
#define BT_AUDIO_CODEC_CAP_CHAN_COUNT_MAX 8
```

相关声明：[BT_AUDIO_CODEC_CAP_CHAN_COUNT_MAX](#gad91341739d394f92ffc4988b614f47b6)。

支持的最大声道数（Channel Count）。

<a id="r_gaa3bf677a479a90793f28a5a3ed69c7e0"></a>

```c
#define BT_AUDIO_BROADCAST_NAME_LEN_MIN 4U
```

相关声明：[BT_AUDIO_BROADCAST_NAME_LEN_MIN](#gaa3bf677a479a90793f28a5a3ed69c7e0)。

广播名称（Broadcast Name）的最小长度，单位为八位字节（Octet）。

<a id="r_gaa2fafcbb6a826c3f4cee16ebb545dad6"></a>

```c
#define BT_AUDIO_BROADCAST_NAME_LEN_MAX 128U
```

相关声明：[BT_AUDIO_BROADCAST_NAME_LEN_MAX](#gaa2fafcbb6a826c3f4cee16ebb545dad6)。

广播名称（Broadcast Name）的最大长度，单位为八位字节（Octet）。

<a id="r_gaaf50689c66f41dee1f4fab02893c4a1b"></a>

```c
#define BT_AUDIO_BROADCAST_NAME_CHAR_MIN 4U
```

相关声明：[BT_AUDIO_BROADCAST_NAME_CHAR_MIN](#gaaf50689c66f41dee1f4fab02893c4a1b)。

广播名称（Broadcast Name）的最少字符数。

<a id="r_gaaabef5f2a77ea0ca60156eef80175311"></a>

```c
#define BT_AUDIO_BROADCAST_NAME_CHAR_MAX 32U
```

相关声明：[BT_AUDIO_BROADCAST_NAME_CHAR_MAX](#gaaabef5f2a77ea0ca60156eef80175311)。

广播名称（Broadcast Name）的最多字符数。

<a id="r_ga6320f86aab9b227385bdf52a9ff3985b"></a>

```c
#define BT_AUDIO_CONTEXT_TYPE_ANY
```

相关声明：[BT_AUDIO_CONTEXT_TYPE_ANY](#ga6320f86aab9b227385bdf52a9ff3985b)。

任意已知上下文（Context）。

<a id="r_ga90688f158fe999ed3aa9c759c8245fcc"></a>

```c
#define BT_AUDIO_LOCATION_ANY
```

相关声明：[BT_AUDIO_LOCATION_ANY](#ga90688f158fe999ed3aa9c759c8245fcc)。

任意已知位置（Location）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.2\_枚举（Enumerations）

<a id="r_ga4bf3f820b493361a9a3b393d0282420f"></a>

```c
enum bt_bearer_tech { BT_BEARER_TECH_3G = 0x01 , BT_BEARER_TECH_4G = 0x02 , BT_BEARER_TECH_LTE = 0x03 , BT_BEARER_TECH_WIFI = 0x04 , BT_BEARER_TECH_5G = 0x05 , BT_BEARER_TECH_GSM = 0x06 , BT_BEARER_TECH_CDMA = 0x07 , BT_BEARER_TECH_2G = 0x08 , BT_BEARER_TECH_WCDMA = 0x09 }
```

相关声明：[bt_bearer_tech](#ga4bf3f820b493361a9a3b393d0282420f)、[BT_BEARER_TECH_3G](#gga4bf3f820b493361a9a3b393d0282420fa62dfe9fe5ac51927efef815b9ce6874e)、[BT_BEARER_TECH_4G](#gga4bf3f820b493361a9a3b393d0282420fa231fe012027b8d279e325231d804ed29)、[BT_BEARER_TECH_LTE](#gga4bf3f820b493361a9a3b393d0282420fa1bd25e0325ebefc57bdac0968e84fd64)、[BT_BEARER_TECH_WIFI](#gga4bf3f820b493361a9a3b393d0282420fab74491db769e0ab918809ab244e2ad1c)、[BT_BEARER_TECH_5G](#gga4bf3f820b493361a9a3b393d0282420faf6494f280fa28f202ce28bb7bc66ee24)、[BT_BEARER_TECH_GSM](#gga4bf3f820b493361a9a3b393d0282420fac6789c1a3127b92c1d9c6a5ee6f02c8a)、[BT_BEARER_TECH_CDMA](#gga4bf3f820b493361a9a3b393d0282420fa1ab62f67902936349103d33f1475a328)、[BT_BEARER_TECH_2G](#gga4bf3f820b493361a9a3b393d0282420face445f78f84de0ef7c6d3ef23e3172b8)、[BT_BEARER_TECH_WCDMA](#gga4bf3f820b493361a9a3b393d0282420fac6fad482035f2eab235dac4dffe77baa)。

有效承载技术（Bearer Technology）值的枚举。

<a id="r_gaf58823a56eb36cfd22e582ab1ea3d015"></a>

```c
enum bt_audio_codec_cap_type { BT_AUDIO_CODEC_CAP_TYPE_FREQ = 0x01 , BT_AUDIO_CODEC_CAP_TYPE_DURATION = 0x02 , BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT = 0x03 , BT_AUDIO_CODEC_CAP_TYPE_FRAME_LEN = 0x04 , BT_AUDIO_CODEC_CAP_TYPE_FRAME_COUNT = 0x05 }
```

相关声明：[bt_audio_codec_cap_type](#gaf58823a56eb36cfd22e582ab1ea3d015)、[BT_AUDIO_CODEC_CAP_TYPE_FREQ](#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b)、[BT_AUDIO_CODEC_CAP_TYPE_DURATION](#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510)、[BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT](#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191)、[BT_AUDIO_CODEC_CAP_TYPE_FRAME_LEN](#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46)、[BT_AUDIO_CODEC_CAP_TYPE_FRAME_COUNT](#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41)。

编解码器能力（Codec Capability）类型。

<a id="r_gaafc1106d5d305874ee2f540c850ff5b4"></a>

```c
enum bt_audio_codec_cap_freq { BT_AUDIO_CODEC_CAP_FREQ_8KHZ = (1UL << (0)) , BT_AUDIO_CODEC_CAP_FREQ_11KHZ = (1UL << (1)) , BT_AUDIO_CODEC_CAP_FREQ_16KHZ = (1UL << (2)) , BT_AUDIO_CODEC_CAP_FREQ_22KHZ = (1UL << (3)) , BT_AUDIO_CODEC_CAP_FREQ_24KHZ = (1UL << (4)) , BT_AUDIO_CODEC_CAP_FREQ_32KHZ = (1UL << (5)) , BT_AUDIO_CODEC_CAP_FREQ_44KHZ = (1UL << (6)) , BT_AUDIO_CODEC_CAP_FREQ_48KHZ = (1UL << (7)) , BT_AUDIO_CODEC_CAP_FREQ_88KHZ = (1UL << (8)) , BT_AUDIO_CODEC_CAP_FREQ_96KHZ = (1UL << (9)) , BT_AUDIO_CODEC_CAP_FREQ_176KHZ = (1UL << (10)) , BT_AUDIO_CODEC_CAP_FREQ_192KHZ = (1UL << (11)) , BT_AUDIO_CODEC_CAP_FREQ_384KHZ = (1UL << (12)) , BT_AUDIO_CODEC_CAP_FREQ_ANY }
```

相关声明：[bt_audio_codec_cap_freq](#gaafc1106d5d305874ee2f540c850ff5b4)、[BT_AUDIO_CODEC_CAP_FREQ_8KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83)、[BT_AUDIO_CODEC_CAP_FREQ_11KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81)、[BT_AUDIO_CODEC_CAP_FREQ_16KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361)、[BT_AUDIO_CODEC_CAP_FREQ_22KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982)、[BT_AUDIO_CODEC_CAP_FREQ_24KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956)、[BT_AUDIO_CODEC_CAP_FREQ_32KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c)、[BT_AUDIO_CODEC_CAP_FREQ_44KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3)、[BT_AUDIO_CODEC_CAP_FREQ_48KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91)、[BT_AUDIO_CODEC_CAP_FREQ_88KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211)、[BT_AUDIO_CODEC_CAP_FREQ_96KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663)、[BT_AUDIO_CODEC_CAP_FREQ_176KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b)、[BT_AUDIO_CODEC_CAP_FREQ_192KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890)、[BT_AUDIO_CODEC_CAP_FREQ_384KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2)、[BT_AUDIO_CODEC_CAP_FREQ_ANY](#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02)。

支持的频率（Frequency）位域。

<a id="r_gaf37e8e19f956afb3c3a413cbaa1a21f5"></a>

```c
enum bt_audio_codec_cap_frame_dur { BT_AUDIO_CODEC_CAP_DURATION_7_5 = (1UL << (0)) , BT_AUDIO_CODEC_CAP_DURATION_10 = (1UL << (1)) , BT_AUDIO_CODEC_CAP_DURATION_ANY , BT_AUDIO_CODEC_CAP_DURATION_PREFER_7_5 = (1UL << (4)) , BT_AUDIO_CODEC_CAP_DURATION_PREFER_10 = (1UL << (5)) }
```

相关声明：[bt_audio_codec_cap_frame_dur](#gaf37e8e19f956afb3c3a413cbaa1a21f5)、[BT_AUDIO_CODEC_CAP_DURATION_7_5](#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441)、[BT_AUDIO_CODEC_CAP_DURATION_10](#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b)、[BT_AUDIO_CODEC_CAP_DURATION_ANY](#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a)、[BT_AUDIO_CODEC_CAP_DURATION_PREFER_7_5](#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91)、[BT_AUDIO_CODEC_CAP_DURATION_PREFER_10](#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e)。

支持的帧时长（Frame Duration）位域。

<a id="r_gae695b5d17359967703f2509db1671fa5"></a>

```c
enum bt_audio_codec_cap_chan_count { BT_AUDIO_CODEC_CAP_CHAN_COUNT_1 = (1UL << (0)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_2 = (1UL << (1)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_3 = (1UL << (2)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_4 = (1UL << (3)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_5 = (1UL << (4)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_6 = (1UL << (5)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_7 = (1UL << (6)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_8 = (1UL << (7)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_ANY }
```

相关声明：[bt_audio_codec_cap_chan_count](#gae695b5d17359967703f2509db1671fa5)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_1](#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_2](#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_3](#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_4](#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_5](#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_6](#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_7](#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_8](#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_ANY](#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219)。

音频能力（Audio Capability）支持的声道数位域。

<a id="r_ga9230ec4d7518bd243207ba2decb1a974"></a>

```c
enum bt_audio_codec_cfg_type { BT_AUDIO_CODEC_CFG_FREQ = 0x01 , BT_AUDIO_CODEC_CFG_DURATION = 0x02 , BT_AUDIO_CODEC_CFG_CHAN_ALLOC = 0x03 , BT_AUDIO_CODEC_CFG_FRAME_LEN = 0x04 , BT_AUDIO_CODEC_CFG_FRAME_BLKS_PER_SDU = 0x05 }
```

相关声明：[bt_audio_codec_cfg_type](#ga9230ec4d7518bd243207ba2decb1a974)、[BT_AUDIO_CODEC_CFG_FREQ](#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3)、[BT_AUDIO_CODEC_CFG_DURATION](#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223)、[BT_AUDIO_CODEC_CFG_CHAN_ALLOC](#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2)、[BT_AUDIO_CODEC_CFG_FRAME_LEN](#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2)、[BT_AUDIO_CODEC_CFG_FRAME_BLKS_PER_SDU](#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8)。

编解码器配置（Codec Configuration）类型。

<a id="r_ga8e99fb678cc011bb8c9f6e1858bae0d7"></a>

```c
enum bt_audio_codec_cfg_freq { BT_AUDIO_CODEC_CFG_FREQ_8KHZ = 0x01 , BT_AUDIO_CODEC_CFG_FREQ_11KHZ = 0x02 , BT_AUDIO_CODEC_CFG_FREQ_16KHZ = 0x03 , BT_AUDIO_CODEC_CFG_FREQ_22KHZ = 0x04 , BT_AUDIO_CODEC_CFG_FREQ_24KHZ = 0x05 , BT_AUDIO_CODEC_CFG_FREQ_32KHZ = 0x06 , BT_AUDIO_CODEC_CFG_FREQ_44KHZ = 0x07 , BT_AUDIO_CODEC_CFG_FREQ_48KHZ = 0x08 , BT_AUDIO_CODEC_CFG_FREQ_88KHZ = 0x09 , BT_AUDIO_CODEC_CFG_FREQ_96KHZ = 0x0a , BT_AUDIO_CODEC_CFG_FREQ_176KHZ = 0x0b , BT_AUDIO_CODEC_CFG_FREQ_192KHZ = 0x0c , BT_AUDIO_CODEC_CFG_FREQ_384KHZ = 0x0d }
```

相关声明：[bt_audio_codec_cfg_freq](#ga8e99fb678cc011bb8c9f6e1858bae0d7)、[BT_AUDIO_CODEC_CFG_FREQ_8KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a)、[BT_AUDIO_CODEC_CFG_FREQ_11KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8)、[BT_AUDIO_CODEC_CFG_FREQ_16KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245)、[BT_AUDIO_CODEC_CFG_FREQ_22KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048)、[BT_AUDIO_CODEC_CFG_FREQ_24KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275)、[BT_AUDIO_CODEC_CFG_FREQ_32KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e)、[BT_AUDIO_CODEC_CFG_FREQ_44KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84)、[BT_AUDIO_CODEC_CFG_FREQ_48KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11)、[BT_AUDIO_CODEC_CFG_FREQ_88KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409)、[BT_AUDIO_CODEC_CFG_FREQ_96KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60)、[BT_AUDIO_CODEC_CFG_FREQ_176KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126)、[BT_AUDIO_CODEC_CFG_FREQ_192KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7)、[BT_AUDIO_CODEC_CFG_FREQ_384KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4)。

编解码器配置的采样频率（Sampling Frequency）。

<a id="r_ga83701b5eadfcbc9b84dc0b1a85ebeb74"></a>

```c
enum bt_audio_codec_cfg_frame_dur { BT_AUDIO_CODEC_CFG_DURATION_7_5 = 0x00 , BT_AUDIO_CODEC_CFG_DURATION_10 = 0x01 }
```

相关声明：[bt_audio_codec_cfg_frame_dur](#ga83701b5eadfcbc9b84dc0b1a85ebeb74)、[BT_AUDIO_CODEC_CFG_DURATION_7_5](#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272)、[BT_AUDIO_CODEC_CFG_DURATION_10](#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7)。

编解码器配置的帧时长（Frame Duration）。

<a id="r_gafb379ffa88388cc1397960155bbb2ab3"></a>

```c
enum bt_audio_context { BT_AUDIO_CONTEXT_TYPE_NONE = 0 , BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED = (1UL << (0)) , BT_AUDIO_CONTEXT_TYPE_CONVERSATIONAL = (1UL << (1)) , BT_AUDIO_CONTEXT_TYPE_MEDIA = (1UL << (2)) , BT_AUDIO_CONTEXT_TYPE_GAME = (1UL << (3)) , BT_AUDIO_CONTEXT_TYPE_INSTRUCTIONAL = (1UL << (4)) , BT_AUDIO_CONTEXT_TYPE_VOICE_ASSISTANTS = (1UL << (5)) , BT_AUDIO_CONTEXT_TYPE_LIVE = (1UL << (6)) , BT_AUDIO_CONTEXT_TYPE_SOUND_EFFECTS = (1UL << (7)) , BT_AUDIO_CONTEXT_TYPE_NOTIFICATIONS = (1UL << (8)) , BT_AUDIO_CONTEXT_TYPE_RINGTONE = (1UL << (9)) , BT_AUDIO_CONTEXT_TYPE_ALERTS = (1UL << (10)) , BT_AUDIO_CONTEXT_TYPE_EMERGENCY_ALARM = (1UL << (11)) }
```

相关声明：[bt_audio_context](#gafb379ffa88388cc1397960155bbb2ab3)、[BT_AUDIO_CONTEXT_TYPE_NONE](#ggafb379ffa88388cc1397960155bbb2ab3a890d2723c8b23127ab4a1cb8b6b1118d)、[BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED](#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5)、[BT_AUDIO_CONTEXT_TYPE_CONVERSATIONAL](#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e)、[BT_AUDIO_CONTEXT_TYPE_MEDIA](#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e)、[BT_AUDIO_CONTEXT_TYPE_GAME](#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730)、[BT_AUDIO_CONTEXT_TYPE_INSTRUCTIONAL](#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4)、[BT_AUDIO_CONTEXT_TYPE_VOICE_ASSISTANTS](#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e)、[BT_AUDIO_CONTEXT_TYPE_LIVE](#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55)、[BT_AUDIO_CONTEXT_TYPE_SOUND_EFFECTS](#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9)、[BT_AUDIO_CONTEXT_TYPE_NOTIFICATIONS](#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377)、[BT_AUDIO_CONTEXT_TYPE_RINGTONE](#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3)、[BT_AUDIO_CONTEXT_TYPE_ALERTS](#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6)、[BT_AUDIO_CONTEXT_TYPE_EMERGENCY_ALARM](#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1)。

通用音频（Generic Audio）的音频上下文类型（Audio Context Type）。

<a id="r_ga6d4aff1f93dc0b902e4b5d1355f15760"></a>

```c
enum bt_audio_parental_rating { BT_AUDIO_PARENTAL_RATING_NO_RATING = 0x00 , BT_AUDIO_PARENTAL_RATING_AGE_ANY = 0x01 , BT_AUDIO_PARENTAL_RATING_AGE_5_OR_ABOVE = 0x02 , BT_AUDIO_PARENTAL_RATING_AGE_6_OR_ABOVE = 0x03 , BT_AUDIO_PARENTAL_RATING_AGE_7_OR_ABOVE = 0x04 , BT_AUDIO_PARENTAL_RATING_AGE_8_OR_ABOVE = 0x05 , BT_AUDIO_PARENTAL_RATING_AGE_9_OR_ABOVE = 0x06 , BT_AUDIO_PARENTAL_RATING_AGE_10_OR_ABOVE = 0x07 , BT_AUDIO_PARENTAL_RATING_AGE_11_OR_ABOVE = 0x08 , BT_AUDIO_PARENTAL_RATING_AGE_12_OR_ABOVE = 0x09 , BT_AUDIO_PARENTAL_RATING_AGE_13_OR_ABOVE = 0x0A , BT_AUDIO_PARENTAL_RATING_AGE_14_OR_ABOVE = 0x0B , BT_AUDIO_PARENTAL_RATING_AGE_15_OR_ABOVE = 0x0C , BT_AUDIO_PARENTAL_RATING_AGE_16_OR_ABOVE = 0x0D , BT_AUDIO_PARENTAL_RATING_AGE_17_OR_ABOVE = 0x0E , BT_AUDIO_PARENTAL_RATING_AGE_18_OR_ABOVE = 0x0F }
```

相关声明：[bt_audio_parental_rating](#ga6d4aff1f93dc0b902e4b5d1355f15760)、[BT_AUDIO_PARENTAL_RATING_NO_RATING](#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c)、[BT_AUDIO_PARENTAL_RATING_AGE_ANY](#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1)、[BT_AUDIO_PARENTAL_RATING_AGE_5_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526)、[BT_AUDIO_PARENTAL_RATING_AGE_6_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc)、[BT_AUDIO_PARENTAL_RATING_AGE_7_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a)、[BT_AUDIO_PARENTAL_RATING_AGE_8_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4)、[BT_AUDIO_PARENTAL_RATING_AGE_9_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd)、[BT_AUDIO_PARENTAL_RATING_AGE_10_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2)、[BT_AUDIO_PARENTAL_RATING_AGE_11_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0)、[BT_AUDIO_PARENTAL_RATING_AGE_12_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7)、[BT_AUDIO_PARENTAL_RATING_AGE_13_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d)、[BT_AUDIO_PARENTAL_RATING_AGE_14_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86)、[BT_AUDIO_PARENTAL_RATING_AGE_15_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077)、[BT_AUDIO_PARENTAL_RATING_AGE_16_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92)、[BT_AUDIO_PARENTAL_RATING_AGE_17_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff)、[BT_AUDIO_PARENTAL_RATING_AGE_18_OR_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071)。

通用音频分配编号（Generic Audio Assigned Numbers，bluetooth.com）定义的家长分级（Parental Rating）。

<a id="r_ga16d403ec4db7be997682331ad365ff5f"></a>

```c
enum bt_audio_active_state { BT_AUDIO_ACTIVE_STATE_DISABLED = 0x00 , BT_AUDIO_ACTIVE_STATE_ENABLED = 0x01 }
```

相关声明：[bt_audio_active_state](#ga16d403ec4db7be997682331ad365ff5f)、[BT_AUDIO_ACTIVE_STATE_DISABLED](#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3)、[BT_AUDIO_ACTIVE_STATE_ENABLED](#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940)。

通用音频分配编号（Generic Audio Assigned Numbers，bluetooth.com）定义的音频活动状态（Audio Active State）。

<a id="r_ga207fbf0fbca9b24cba02c7f1d184e7f5"></a>

```c
enum bt_audio_assisted_listening_stream { BT_AUDIO_ASSISTED_LISTENING_STREAM_UNSPECIFIED = 0x00 }
```

相关声明：[bt_audio_assisted_listening_stream](#ga207fbf0fbca9b24cba02c7f1d184e7f5)、[BT_AUDIO_ASSISTED_LISTENING_STREAM_UNSPECIFIED](#gga207fbf0fbca9b24cba02c7f1d184e7f5ab1714206feaa04b3be586ddb33ed5285)。

通用音频分配编号（Generic Audio Assigned Numbers，bluetooth.com）定义的辅助聆听流（Assisted Listening Stream）。

<a id="r_gab53d0dd62bceff97cf8eed7d8cf80354"></a>

```c
enum bt_audio_metadata_type { BT_AUDIO_METADATA_TYPE_PREF_CONTEXT = 0x01 , BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT = 0x02 , BT_AUDIO_METADATA_TYPE_PROGRAM_INFO = 0x03 , BT_AUDIO_METADATA_TYPE_LANG = 0x04 , BT_AUDIO_METADATA_TYPE_CCID_LIST = 0x05 , BT_AUDIO_METADATA_TYPE_PARENTAL_RATING = 0x06 , BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI = 0x07 , BT_AUDIO_METADATA_TYPE_AUDIO_STATE = 0x08 , BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE = 0x09 , BT_AUDIO_METADATA_TYPE_ASSISTED_LISTENING_STREAM = 0x0A , BT_AUDIO_METADATA_TYPE_BROADCAST_NAME = 0x0B , BT_AUDIO_METADATA_TYPE_EXTENDED = 0xFE , BT_AUDIO_METADATA_TYPE_VENDOR = 0xFF }
```

相关声明：[bt_audio_metadata_type](#gab53d0dd62bceff97cf8eed7d8cf80354)、[BT_AUDIO_METADATA_TYPE_PREF_CONTEXT](#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a)、[BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT](#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa)、[BT_AUDIO_METADATA_TYPE_PROGRAM_INFO](#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7)、[BT_AUDIO_METADATA_TYPE_LANG](#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1)、[BT_AUDIO_METADATA_TYPE_CCID_LIST](#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b)、[BT_AUDIO_METADATA_TYPE_PARENTAL_RATING](#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613)、[BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI](#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922)、[BT_AUDIO_METADATA_TYPE_AUDIO_STATE](#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc)、[BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE](#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1)、[BT_AUDIO_METADATA_TYPE_ASSISTED_LISTENING_STREAM](#ggab53d0dd62bceff97cf8eed7d8cf80354a40aad5cb3574e6e4e7bc955bc12760bf)、[BT_AUDIO_METADATA_TYPE_BROADCAST_NAME](#ggab53d0dd62bceff97cf8eed7d8cf80354ada34d453c8ce75a155c59c371a67d8a6)、[BT_AUDIO_METADATA_TYPE_EXTENDED](#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39)、[BT_AUDIO_METADATA_TYPE_VENDOR](#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286)。

编解码器元数据（Codec Metadata）类型 ID。

<a id="r_ga61230848c02098352320fe751332c4e8"></a>

```c
enum bt_audio_location { BT_AUDIO_LOCATION_MONO_AUDIO = 0 , BT_AUDIO_LOCATION_FRONT_LEFT = (1UL << (0)) , BT_AUDIO_LOCATION_FRONT_RIGHT = (1UL << (1)) , BT_AUDIO_LOCATION_FRONT_CENTER = (1UL << (2)) , BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_1 = (1UL << (3)) , BT_AUDIO_LOCATION_BACK_LEFT = (1UL << (4)) , BT_AUDIO_LOCATION_BACK_RIGHT = (1UL << (5)) , BT_AUDIO_LOCATION_FRONT_LEFT_OF_CENTER = (1UL << (6)) , BT_AUDIO_LOCATION_FRONT_RIGHT_OF_CENTER = (1UL << (7)) , BT_AUDIO_LOCATION_BACK_CENTER = (1UL << (8)) , BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_2 = (1UL << (9)) , BT_AUDIO_LOCATION_SIDE_LEFT = (1UL << (10)) , BT_AUDIO_LOCATION_SIDE_RIGHT = (1UL << (11)) , BT_AUDIO_LOCATION_TOP_FRONT_LEFT = (1UL << (12)) , BT_AUDIO_LOCATION_TOP_FRONT_RIGHT = (1UL << (13)) , BT_AUDIO_LOCATION_TOP_FRONT_CENTER = (1UL << (14)) , BT_AUDIO_LOCATION_TOP_CENTER = (1UL << (15)) , BT_AUDIO_LOCATION_TOP_BACK_LEFT = (1UL << (16)) , BT_AUDIO_LOCATION_TOP_BACK_RIGHT = (1UL << (17)) , BT_AUDIO_LOCATION_TOP_SIDE_LEFT = (1UL << (18)) , BT_AUDIO_LOCATION_TOP_SIDE_RIGHT = (1UL << (19)) , BT_AUDIO_LOCATION_TOP_BACK_CENTER = (1UL << (20)) , BT_AUDIO_LOCATION_BOTTOM_FRONT_CENTER = (1UL << (21)) , BT_AUDIO_LOCATION_BOTTOM_FRONT_LEFT = (1UL << (22)) , BT_AUDIO_LOCATION_BOTTOM_FRONT_RIGHT = (1UL << (23)) , BT_AUDIO_LOCATION_FRONT_LEFT_WIDE = (1UL << (24)) , BT_AUDIO_LOCATION_FRONT_RIGHT_WIDE = (1UL << (25)) , BT_AUDIO_LOCATION_LEFT_SURROUND = (1UL << (26)) , BT_AUDIO_LOCATION_RIGHT_SURROUND = (1UL << (27)) }
```

相关声明：[bt_audio_location](#ga61230848c02098352320fe751332c4e8)、[BT_AUDIO_LOCATION_MONO_AUDIO](#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df)、[BT_AUDIO_LOCATION_FRONT_LEFT](#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b)、[BT_AUDIO_LOCATION_FRONT_RIGHT](#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3)、[BT_AUDIO_LOCATION_FRONT_CENTER](#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337)、[BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_1](#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6)、[BT_AUDIO_LOCATION_BACK_LEFT](#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896)、[BT_AUDIO_LOCATION_BACK_RIGHT](#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa)、[BT_AUDIO_LOCATION_FRONT_LEFT_OF_CENTER](#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e)、[BT_AUDIO_LOCATION_FRONT_RIGHT_OF_CENTER](#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692)、[BT_AUDIO_LOCATION_BACK_CENTER](#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983)、[BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_2](#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b)、[BT_AUDIO_LOCATION_SIDE_LEFT](#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064)、[BT_AUDIO_LOCATION_SIDE_RIGHT](#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd)、[BT_AUDIO_LOCATION_TOP_FRONT_LEFT](#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9)、[BT_AUDIO_LOCATION_TOP_FRONT_RIGHT](#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d)、[BT_AUDIO_LOCATION_TOP_FRONT_CENTER](#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e)、[BT_AUDIO_LOCATION_TOP_CENTER](#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f)、[BT_AUDIO_LOCATION_TOP_BACK_LEFT](#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06)、[BT_AUDIO_LOCATION_TOP_BACK_RIGHT](#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69)、[BT_AUDIO_LOCATION_TOP_SIDE_LEFT](#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6)、[BT_AUDIO_LOCATION_TOP_SIDE_RIGHT](#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59)、[BT_AUDIO_LOCATION_TOP_BACK_CENTER](#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd)、[BT_AUDIO_LOCATION_BOTTOM_FRONT_CENTER](#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376)、[BT_AUDIO_LOCATION_BOTTOM_FRONT_LEFT](#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29)、[BT_AUDIO_LOCATION_BOTTOM_FRONT_RIGHT](#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8)、[BT_AUDIO_LOCATION_FRONT_LEFT_WIDE](#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d)、[BT_AUDIO_LOCATION_FRONT_RIGHT_WIDE](#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71)、[BT_AUDIO_LOCATION_LEFT_SURROUND](#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6)、[BT_AUDIO_LOCATION_RIGHT_SURROUND](#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e)。

蓝牙音频（BT Audio）的位置（Location）值。

## 1.3\_详细说明（Detailed Documentation）

<a id="gaaabef5f2a77ea0ca60156eef80175311"></a>

### `BT_AUDIO_BROADCAST_NAME_CHAR_MAX`

```c
#define BT_AUDIO_BROADCAST_NAME_CHAR_MAX 32U
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

广播名称（Broadcast Name）的最多字符数。

<a id="gaaf50689c66f41dee1f4fab02893c4a1b"></a>

### `BT_AUDIO_BROADCAST_NAME_CHAR_MIN`

```c
#define BT_AUDIO_BROADCAST_NAME_CHAR_MIN 4U
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

广播名称（Broadcast Name）的最少字符数。

<a id="gaa2fafcbb6a826c3f4cee16ebb545dad6"></a>

### `BT_AUDIO_BROADCAST_NAME_LEN_MAX`

```c
#define BT_AUDIO_BROADCAST_NAME_LEN_MAX 128U
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

广播名称（Broadcast Name）的最大长度，单位为八位字节（Octet）。

<a id="gaa3bf677a479a90793f28a5a3ed69c7e0"></a>

### `BT_AUDIO_BROADCAST_NAME_LEN_MIN`

```c
#define BT_AUDIO_BROADCAST_NAME_LEN_MIN 4U
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

广播名称（Broadcast Name）的最小长度，单位为八位字节（Octet）。

<a id="gad91341739d394f92ffc4988b614f47b6"></a>

### `BT_AUDIO_CODEC_CAP_CHAN_COUNT_MAX`

```c
#define BT_AUDIO_CODEC_CAP_CHAN_COUNT_MAX 8
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

支持的最大声道数（Channel Count）。

<a id="gac1251f8a35b5e343eeeff87f22f8ab10"></a>

### `BT_AUDIO_CODEC_CAP_CHAN_COUNT_MIN`

```c
#define BT_AUDIO_CODEC_CAP_CHAN_COUNT_MIN 1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

支持的最小声道数（Channel Count）。

<a id="ga6320f86aab9b227385bdf52a9ff3985b"></a>

### `BT_AUDIO_CONTEXT_TYPE_ANY`

```c
#define BT_AUDIO_CONTEXT_TYPE_ANY
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

展开值（Value）：

```c
(BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED | \
BT_AUDIO_CONTEXT_TYPE_CONVERSATIONAL | \
BT_AUDIO_CONTEXT_TYPE_MEDIA | \
BT_AUDIO_CONTEXT_TYPE_GAME | \
BT_AUDIO_CONTEXT_TYPE_INSTRUCTIONAL | \
BT_AUDIO_CONTEXT_TYPE_VOICE_ASSISTANTS | \
BT_AUDIO_CONTEXT_TYPE_LIVE | \
BT_AUDIO_CONTEXT_TYPE_SOUND_EFFECTS | \
BT_AUDIO_CONTEXT_TYPE_NOTIFICATIONS | \
BT_AUDIO_CONTEXT_TYPE_RINGTONE | \
BT_AUDIO_CONTEXT_TYPE_ALERTS | \
BT_AUDIO_CONTEXT_TYPE_EMERGENCY_ALARM)
```

任意已知上下文（Context）。

<a id="ga90688f158fe999ed3aa9c759c8245fcc"></a>

### `BT_AUDIO_LOCATION_ANY`

```c
#define BT_AUDIO_LOCATION_ANY
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

展开值（Value）：

```c
(BT_AUDIO_LOCATION_FRONT_LEFT | \
BT_AUDIO_LOCATION_FRONT_RIGHT | \
BT_AUDIO_LOCATION_FRONT_CENTER | \
BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_1 | \
BT_AUDIO_LOCATION_BACK_LEFT | \
BT_AUDIO_LOCATION_BACK_RIGHT | \
BT_AUDIO_LOCATION_FRONT_LEFT_OF_CENTER | \
BT_AUDIO_LOCATION_FRONT_RIGHT_OF_CENTER | \
BT_AUDIO_LOCATION_BACK_CENTER | \
BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_2 | \
BT_AUDIO_LOCATION_SIDE_LEFT | \
BT_AUDIO_LOCATION_SIDE_RIGHT | \
BT_AUDIO_LOCATION_TOP_FRONT_LEFT | \
BT_AUDIO_LOCATION_TOP_FRONT_RIGHT | \
BT_AUDIO_LOCATION_TOP_FRONT_CENTER | \
BT_AUDIO_LOCATION_TOP_CENTER | \
BT_AUDIO_LOCATION_TOP_BACK_LEFT | \
BT_AUDIO_LOCATION_TOP_BACK_RIGHT | \
BT_AUDIO_LOCATION_TOP_SIDE_LEFT | \
BT_AUDIO_LOCATION_TOP_SIDE_RIGHT | \
BT_AUDIO_LOCATION_TOP_BACK_CENTER | \
BT_AUDIO_LOCATION_BOTTOM_FRONT_CENTER | \
BT_AUDIO_LOCATION_BOTTOM_FRONT_LEFT | \
BT_AUDIO_LOCATION_BOTTOM_FRONT_RIGHT | \
BT_AUDIO_LOCATION_FRONT_LEFT_WIDE | \
BT_AUDIO_LOCATION_FRONT_RIGHT_WIDE | \
BT_AUDIO_LOCATION_LEFT_SURROUND | \
BT_AUDIO_LOCATION_RIGHT_SURROUND)
```

任意已知位置（Location）。

<a id="ga16d403ec4db7be997682331ad365ff5f"></a>

### `bt_audio_active_state`

```c
enum bt_audio_active_state
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用音频分配编号（Generic Audio Assigned Numbers，bluetooth.com）定义的音频活动状态（Audio Active State）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_ACTIVE_STATE_DISABLED` | 当前没有传输音频数据（Audio Data）。 |
| `BT_AUDIO_ACTIVE_STATE_ENABLED` | 当前正在传输音频数据（Audio Data）。 |

<a id="ga207fbf0fbca9b24cba02c7f1d184e7f5"></a>

### `bt_audio_assisted_listening_stream`

```c
enum bt_audio_assisted_listening_stream
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用音频分配编号（Generic Audio Assigned Numbers，bluetooth.com）定义的辅助聆听流（Assisted Listening Stream）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_ASSISTED_LISTENING_STREAM_UNSPECIFIED` | 未指定的音频增强（Audio Enhancement）。 |

<a id="gae695b5d17359967703f2509db1671fa5"></a>

### `bt_audio_codec_cap_chan_count`

```c
enum bt_audio_codec_cap_chan_count
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

音频能力（Audio Capability）支持的声道数位域。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_CODEC_CAP_CHAN_COUNT_1` | 支持 1 个声道（Channel）。 |
| `BT_AUDIO_CODEC_CAP_CHAN_COUNT_2` | 支持 2 个声道（Channel）。 |
| `BT_AUDIO_CODEC_CAP_CHAN_COUNT_3` | 支持 3 个声道（Channel）。 |
| `BT_AUDIO_CODEC_CAP_CHAN_COUNT_4` | 支持 4 个声道（Channel）。 |
| `BT_AUDIO_CODEC_CAP_CHAN_COUNT_5` | 支持 5 个声道（Channel）。 |
| `BT_AUDIO_CODEC_CAP_CHAN_COUNT_6` | 支持 6 个声道（Channel）。 |
| `BT_AUDIO_CODEC_CAP_CHAN_COUNT_7` | 支持 7 个声道（Channel）。 |
| `BT_AUDIO_CODEC_CAP_CHAN_COUNT_8` | 支持 8 个声道（Channel）。 |
| `BT_AUDIO_CODEC_CAP_CHAN_COUNT_ANY` | 支持所有声道（Channel）。 |

<a id="gaf37e8e19f956afb3c3a413cbaa1a21f5"></a>

### `bt_audio_codec_cap_frame_dur`

```c
enum bt_audio_codec_cap_frame_dur
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

支持的帧时长（Frame Duration）位域。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_CODEC_CAP_DURATION_7_5` | 支持 7.5 ms 帧时长（Frame Duration）的能力。 |
| `BT_AUDIO_CODEC_CAP_DURATION_10` | 支持 10 ms 帧时长（Frame Duration）的能力。 |
| `BT_AUDIO_CODEC_CAP_DURATION_ANY` | 支持任意帧时长（Frame Duration）的能力。 |
| `BT_AUDIO_CODEC_CAP_DURATION_PREFER_7_5` | 首选 7.5 ms 帧时长（Frame Duration）的能力。仅当同时设置 `BT_AUDIO_CODEC_CAP_DURATION_7_5` 且未设置 `BT_AUDIO_CODEC_CAP_DURATION_PREFER_10` 时，才允许设置此项。 |
| `BT_AUDIO_CODEC_CAP_DURATION_PREFER_10` | 首选 10 ms 帧时长（Frame Duration）的能力。仅当同时设置 `BT_AUDIO_CODEC_CAP_DURATION_10` 且未设置 `BT_AUDIO_CODEC_CAP_DURATION_PREFER_7_5` 时，才允许设置此项。 |

<a id="gaafc1106d5d305874ee2f540c850ff5b4"></a>

### `bt_audio_codec_cap_freq`

```c
enum bt_audio_codec_cap_freq
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

支持的频率（Frequency）位域。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_CODEC_CAP_FREQ_8KHZ` | 8 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_11KHZ` | 11.025 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_16KHZ` | 16 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_22KHZ` | 22.05 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_24KHZ` | 24 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_32KHZ` | 32 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_44KHZ` | 44.1 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_48KHZ` | 48 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_88KHZ` | 88.2 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_96KHZ` | 96 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_176KHZ` | 176.4 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_192KHZ` | 192 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_384KHZ` | 384 kHz 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CAP_FREQ_ANY` | 支持任意频率（Frequency）的能力。 |

<a id="gaf58823a56eb36cfd22e582ab1ea3d015"></a>

### `bt_audio_codec_cap_type`

```c
enum bt_audio_codec_cap_type
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

编解码器能力（Codec Capability）类型。

用于按 PAC 规范构造和解析编解码器能力（Codec Capabilities）。来源为 bluetooth.com 的通用音频分配编号（Generic Audio Assigned Numbers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_CODEC_CAP_TYPE_FREQ` | 支持的采样频率（Sampling Frequencies）。 |
| `BT_AUDIO_CODEC_CAP_TYPE_DURATION` | 支持的帧时长（Frame Durations）。 |
| `BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT` | 支持的音频声道数（Audio Channel Counts）。 |
| `BT_AUDIO_CODEC_CAP_TYPE_FRAME_LEN` | 支持的每编解码器帧八位字节数（Octets per Codec Frame）。 |
| `BT_AUDIO_CODEC_CAP_TYPE_FRAME_COUNT` | 每个服务数据单元（SDU）支持的最大编解码器帧（Codec Frames）数量。 |

<a id="ga83701b5eadfcbc9b84dc0b1a85ebeb74"></a>

### `bt_audio_codec_cfg_frame_dur`

```c
enum bt_audio_codec_cfg_frame_dur
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

编解码器配置的帧时长（Frame Duration）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_CODEC_CFG_DURATION_7_5` | 7.5 ms 帧时长（Frame Duration）配置。 |
| `BT_AUDIO_CODEC_CFG_DURATION_10` | 10 ms 帧时长（Frame Duration）配置。 |

<a id="ga8e99fb678cc011bb8c9f6e1858bae0d7"></a>

### `bt_audio_codec_cfg_freq`

```c
enum bt_audio_codec_cfg_freq
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

编解码器配置的采样频率（Sampling Frequency）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_CODEC_CFG_FREQ_8KHZ` | 8 kHz 编解码器采样频率（Codec Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_FREQ_11KHZ` | 11.025 kHz 编解码器采样频率（Codec Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_FREQ_16KHZ` | 16 kHz 编解码器采样频率（Codec Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_FREQ_22KHZ` | 22.05 kHz 编解码器采样频率（Codec Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_FREQ_24KHZ` | 24 kHz 编解码器采样频率（Codec Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_FREQ_32KHZ` | 32 kHz 编解码器采样频率（Codec Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_FREQ_44KHZ` | 44.1 kHz 编解码器采样频率（Codec Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_FREQ_48KHZ` | 48 kHz 编解码器采样频率（Codec Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_FREQ_88KHZ` | 88.2 kHz 编解码器采样频率（Codec Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_FREQ_96KHZ` | 96 kHz 编解码器采样频率（Codec Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_FREQ_176KHZ` | 176.4 kHz 编解码器采样频率（Codec Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_FREQ_192KHZ` | 192 kHz 编解码器采样频率（Codec Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_FREQ_384KHZ` | 384 kHz 编解码器采样频率（Codec Sampling Frequency）。 |

<a id="ga9230ec4d7518bd243207ba2decb1a974"></a>

### `bt_audio_codec_cfg_type`

```c
enum bt_audio_codec_cfg_type
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

编解码器配置（Codec Configuration）类型。

用于按 ASCS 和 BAP 规范构造和解析编解码器配置（Codec Configurations）。来源为 bluetooth.com 的通用音频分配编号（Generic Audio Assigned Numbers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_CODEC_CFG_FREQ` | 采样频率（Sampling Frequency）。 |
| `BT_AUDIO_CODEC_CFG_DURATION` | 帧时长（Frame Duration）。 |
| `BT_AUDIO_CODEC_CFG_CHAN_ALLOC` | 音频声道分配（Audio Channel Allocation）。 |
| `BT_AUDIO_CODEC_CFG_FRAME_LEN` | 每编解码器帧的八位字节数（Octets per Codec Frame）。 |
| `BT_AUDIO_CODEC_CFG_FRAME_BLKS_PER_SDU` | 每个服务数据单元（SDU）的编解码器帧块（Codec Frame Blocks）数。 |

<a id="gafb379ffa88388cc1397960155bbb2ab3"></a>

### `bt_audio_context`

```c
enum bt_audio_context
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用音频（Generic Audio）的音频上下文类型（Audio Context Type）。

这些值由 bluetooth.com 的通用音频分配编号（Generic Audio Assigned Numbers）定义。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_CONTEXT_TYPE_NONE` | 无上下文类型（Context Type）。 |
| `BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED` | 标识使用场景上下文（Use Case Context）不匹配其他已定义值，或上下文未知、无法确定的音频。 |
| `BT_AUDIO_CONTEXT_TYPE_CONVERSATIONAL` | 人与人之间的对话（Conversation），例如电话或视频通话，包括传统蜂窝通信、IP 语音（VoIP）和一键通（Push-to-Talk）。 |
| `BT_AUDIO_CONTEXT_TYPE_MEDIA` | 媒体（Media），例如音乐播放、广播、播客、电影配乐或电视音频。 |
| `BT_AUDIO_CONTEXT_TYPE_GAME` | 与电子游戏相关的音频（Gaming），例如游戏媒体、游戏音效、音乐、参与者之间的游戏内语音聊天，或以上内容的混合。 |
| `BT_AUDIO_CONTEXT_TYPE_INSTRUCTIONAL` | 指导性音频（Instructional Audio），例如导航、公告或用户引导。 |
| `BT_AUDIO_CONTEXT_TYPE_VOICE_ASSISTANTS` | 人机通信（Man-machine Communication），例如语音识别或虚拟助手。 |
| `BT_AUDIO_CONTEXT_TYPE_LIVE` | 实况音频（Live Audio），例如来自麦克风的音频，听者可同时通过直接声学路径和低功耗音频流（LE Audio Stream）感知它。 |
| `BT_AUDIO_CONTEXT_TYPE_SOUND_EFFECTS` | 音效（Sound Effects），包括键盘和触摸反馈、菜单和用户界面声音，以及其他系统声音。 |
| `BT_AUDIO_CONTEXT_TYPE_NOTIFICATIONS` | 通知和提醒声音（Notification and Reminder Sounds）；用于引起注意的音频，例如提示消息到达的蜂鸣声。 |
| `BT_AUDIO_CONTEXT_TYPE_RINGTONE` | 来电提示（Incoming Call），例如电话或视频来电，包括传统蜂窝通信、IP 语音（VoIP）和一键通（Push-to-Talk）。 |
| `BT_AUDIO_CONTEXT_TYPE_ALERTS` | 闹铃和定时器（Alarms and Timers）；即时提醒，例如严重低电量警报、定时器到期、闹钟，以及烤面包机、炊具、水壶、微波炉等的提醒。 |
| `BT_AUDIO_CONTEXT_TYPE_EMERGENCY_ALARM` | 紧急警报（Emergency Alarm）：紧急声音，例如火灾警报或其他紧急提醒。 |

<a id="ga61230848c02098352320fe751332c4e8"></a>

### `bt_audio_location`

```c
enum bt_audio_location
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

蓝牙音频（BT Audio）的位置（Location）值。

这些值由 bluetooth.com 的通用音频分配编号（Generic Audio Assigned Numbers）定义。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_LOCATION_MONO_AUDIO` | 单声道音频（Mono Audio），未指定音频位置（Audio Location）。 |
| `BT_AUDIO_LOCATION_FRONT_LEFT` | 前左（Front Left）。 |
| `BT_AUDIO_LOCATION_FRONT_RIGHT` | 前右（Front Right）。 |
| `BT_AUDIO_LOCATION_FRONT_CENTER` | 前中（Front Center）。 |
| `BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_1` | 低频效果 1（Low Frequency Effects 1）。 |
| `BT_AUDIO_LOCATION_BACK_LEFT` | 后左（Back Left）。 |
| `BT_AUDIO_LOCATION_BACK_RIGHT` | 后右（Back Right）。 |
| `BT_AUDIO_LOCATION_FRONT_LEFT_OF_CENTER` | 前方中央偏左（Front Left of Center）。 |
| `BT_AUDIO_LOCATION_FRONT_RIGHT_OF_CENTER` | 前方中央偏右（Front Right of Center）。 |
| `BT_AUDIO_LOCATION_BACK_CENTER` | 后中（Back Center）。 |
| `BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_2` | 低频效果 2（Low Frequency Effects 2）。 |
| `BT_AUDIO_LOCATION_SIDE_LEFT` | 侧左（Side Left）。 |
| `BT_AUDIO_LOCATION_SIDE_RIGHT` | 侧右（Side Right）。 |
| `BT_AUDIO_LOCATION_TOP_FRONT_LEFT` | 顶部前左（Top Front Left）。 |
| `BT_AUDIO_LOCATION_TOP_FRONT_RIGHT` | 顶部前右（Top Front Right）。 |
| `BT_AUDIO_LOCATION_TOP_FRONT_CENTER` | 顶部前中（Top Front Center）。 |
| `BT_AUDIO_LOCATION_TOP_CENTER` | 顶部中央（Top Center）。 |
| `BT_AUDIO_LOCATION_TOP_BACK_LEFT` | 顶部后左（Top Back Left）。 |
| `BT_AUDIO_LOCATION_TOP_BACK_RIGHT` | 顶部后右（Top Back Right）。 |
| `BT_AUDIO_LOCATION_TOP_SIDE_LEFT` | 顶部侧左（Top Side Left）。 |
| `BT_AUDIO_LOCATION_TOP_SIDE_RIGHT` | 顶部侧右（Top Side Right）。 |
| `BT_AUDIO_LOCATION_TOP_BACK_CENTER` | 顶部后中（Top Back Center）。 |
| `BT_AUDIO_LOCATION_BOTTOM_FRONT_CENTER` | 底部前中（Bottom Front Center）。 |
| `BT_AUDIO_LOCATION_BOTTOM_FRONT_LEFT` | 底部前左（Bottom Front Left）。 |
| `BT_AUDIO_LOCATION_BOTTOM_FRONT_RIGHT` | 底部前右（Bottom Front Right）。 |
| `BT_AUDIO_LOCATION_FRONT_LEFT_WIDE` | 前左宽声道（Front Left Wide）。 |
| `BT_AUDIO_LOCATION_FRONT_RIGHT_WIDE` | 前右宽声道（Front Right Wide）。 |
| `BT_AUDIO_LOCATION_LEFT_SURROUND` | 左环绕（Left Surround）。 |
| `BT_AUDIO_LOCATION_RIGHT_SURROUND` | 右环绕（Right Surround）。 |

<a id="gab53d0dd62bceff97cf8eed7d8cf80354"></a>

### `bt_audio_metadata_type`

```c
enum bt_audio_metadata_type
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

编解码器元数据（Codec Metadata）类型 ID。

通用音频分配编号（Generic Audio Assigned Numbers，bluetooth.com）定义的元数据类型（Metadata Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_METADATA_TYPE_PREF_CONTEXT` | 首选音频上下文（Preferred Audio Context）：首选音频上下文的位域。如果为 0，此上下文类型不是该编解码器配置的首选使用场景。有效值参见 `BT_AUDIO_CONTEXT_*`。 |
| `BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT` | 流式音频上下文（Streaming Audio Context）：流式音频上下文的位域。如果为 0，此上下文类型不是该编解码器配置的首选使用场景。有效值参见 `BT_AUDIO_CONTEXT_*`。 |
| `BT_AUDIO_METADATA_TYPE_PROGRAM_INFO` | 以 UTF-8 编码的流内容（Stream Content）标题或摘要。 |
| `BT_AUDIO_METADATA_TYPE_LANG` | 语言（Language）：ISO 639-3 定义的 3 个八位字节的小写语言代码。可用值见 https://iso639-3.sil.org/code_tables/639/data 。 译注：2026-10-17 核验时，该官方外部代码表返回 HTTP 403；原链接保留，但本次未能读取其内容。 |
| `BT_AUDIO_METADATA_TYPE_CCID_LIST` | 由 8 位 CCID 值组成的数组。 |
| `BT_AUDIO_METADATA_TYPE_PARENTAL_RATING` | 家长分级（Parental Rating）。有效值参见 `bt_audio_parental_rating`。 |
| `BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI` | 以 UTF-8 编码的 URI，用于提供额外节目信息（Program Information）。 |
| `BT_AUDIO_METADATA_TYPE_AUDIO_STATE` | 音频活动状态（Audio Active State）。有效值参见 `bt_audio_active_state`。 |
| `BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE` | 广播音频立即呈现（Broadcast Audio Immediate Rendering）标志。 |
| `BT_AUDIO_METADATA_TYPE_ASSISTED_LISTENING_STREAM` | 辅助聆听流（Assisted Listening Stream）。有效值参见 `bt_audio_assisted_listening_stream`。 |
| `BT_AUDIO_METADATA_TYPE_BROADCAST_NAME` | 以 UTF-8 编码的广播名称（Broadcast Name）。 |
| `BT_AUDIO_METADATA_TYPE_EXTENDED` | 扩展元数据（Extended Metadata）。 |
| `BT_AUDIO_METADATA_TYPE_VENDOR` | 厂商专用元数据（Vendor Specific Metadata）。 |

<a id="ga6d4aff1f93dc0b902e4b5d1355f15760"></a>

### `bt_audio_parental_rating`

```c
enum bt_audio_parental_rating
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用音频分配编号（Generic Audio Assigned Numbers，bluetooth.com）定义的家长分级（Parental Rating）。

编号方案与 EN 300 707 v1.2.1 附录 F 一致；该附录定义了供观看内容使用的家长分级（Parental Rating）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_PARENTAL_RATING_NO_RATING` | 无分级（No Rating）。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_ANY` | 适合所有年龄（For All Ages）。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_5_OR_ABOVE` | 建议 5 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_6_OR_ABOVE` | 建议 6 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_7_OR_ABOVE` | 建议 7 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_8_OR_ABOVE` | 建议 8 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_9_OR_ABOVE` | 建议 9 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_10_OR_ABOVE` | 建议 10 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_11_OR_ABOVE` | 建议 11 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_12_OR_ABOVE` | 建议 12 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_13_OR_ABOVE` | 建议 13 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_14_OR_ABOVE` | 建议 14 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_15_OR_ABOVE` | 建议 15 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_16_OR_ABOVE` | 建议 16 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_17_OR_ABOVE` | 建议 17 岁及以上听众收听。 |
| `BT_AUDIO_PARENTAL_RATING_AGE_18_OR_ABOVE` | 建议 18 岁及以上听众收听。 |

<a id="ga4bf3f820b493361a9a3b393d0282420f"></a>

### `bt_bearer_tech`

```c
enum bt_bearer_tech
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

有效承载技术（Bearer Technology）值的枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BEARER_TECH_3G` | 第三代移动通信（3G）。 |
| `BT_BEARER_TECH_4G` | 第四代移动通信（4G）。 |
| `BT_BEARER_TECH_LTE` | 长期演进（Long-term Evolution，LTE）。 |
| `BT_BEARER_TECH_WIFI` | 无线局域网（Wi-Fi）。 |
| `BT_BEARER_TECH_5G` | 第五代移动通信（5G）。 |
| `BT_BEARER_TECH_GSM` | 全球移动通信系统（Global System for Mobile Communications，GSM）。 |
| `BT_BEARER_TECH_CDMA` | 码分多址（Code-Division Multiple Access，CDMA）。 |
| `BT_BEARER_TECH_2G` | 第二代移动通信（2G）。 |
| `BT_BEARER_TECH_WCDMA` | 宽带码分多址（Wideband Code-Division Multiple Access，WCDMA）。 |


## 1.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [https://iso639-3.sil.org/code_tables/639/data](https://iso639-3.sil.org/code_tables/639/data)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd"></a>
<a id="agroup__bt__assigned__numbers__audio_html_gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3"></a>
<a id="gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940"></a>
<a id="gga207fbf0fbca9b24cba02c7f1d184e7f5ab1714206feaa04b3be586ddb33ed5285"></a>
<a id="ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc"></a>
<a id="ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd"></a>
<a id="ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39"></a>
<a id="ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2"></a>
<a id="ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51"></a>
<a id="ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8"></a>
<a id="ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82"></a>
<a id="ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943"></a>
<a id="ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219"></a>
<a id="ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441"></a>
<a id="ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b"></a>
<a id="ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a"></a>
<a id="ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91"></a>
<a id="ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2"></a>
<a id="ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02"></a>
<a id="ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b"></a>
<a id="ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510"></a>
<a id="ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191"></a>
<a id="ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46"></a>
<a id="ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41"></a>
<a id="gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272"></a>
<a id="gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7"></a>
<a id="gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4"></a>
<a id="gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3"></a>
<a id="gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223"></a>
<a id="gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2"></a>
<a id="gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2"></a>
<a id="gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3a890d2723c8b23127ab4a1cb8b6b1118d"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6"></a>
<a id="ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1"></a>
<a id="gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df"></a>
<a id="gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b"></a>
<a id="gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3"></a>
<a id="gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337"></a>
<a id="gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6"></a>
<a id="gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896"></a>
<a id="gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa"></a>
<a id="gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e"></a>
<a id="gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692"></a>
<a id="gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983"></a>
<a id="gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b"></a>
<a id="gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064"></a>
<a id="gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd"></a>
<a id="gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9"></a>
<a id="gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d"></a>
<a id="gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e"></a>
<a id="gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f"></a>
<a id="gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06"></a>
<a id="gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69"></a>
<a id="gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6"></a>
<a id="gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59"></a>
<a id="gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd"></a>
<a id="gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376"></a>
<a id="gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29"></a>
<a id="gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8"></a>
<a id="gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d"></a>
<a id="gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71"></a>
<a id="gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6"></a>
<a id="gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354a40aad5cb3574e6e4e7bc955bc12760bf"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354ada34d453c8ce75a155c59c371a67d8a6"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39"></a>
<a id="ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff"></a>
<a id="gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071"></a>
<a id="gga4bf3f820b493361a9a3b393d0282420fa62dfe9fe5ac51927efef815b9ce6874e"></a>
<a id="gga4bf3f820b493361a9a3b393d0282420fa231fe012027b8d279e325231d804ed29"></a>
<a id="gga4bf3f820b493361a9a3b393d0282420fa1bd25e0325ebefc57bdac0968e84fd64"></a>
<a id="gga4bf3f820b493361a9a3b393d0282420fab74491db769e0ab918809ab244e2ad1c"></a>
<a id="gga4bf3f820b493361a9a3b393d0282420faf6494f280fa28f202ce28bb7bc66ee24"></a>
<a id="gga4bf3f820b493361a9a3b393d0282420fac6789c1a3127b92c1d9c6a5ee6f02c8a"></a>
<a id="gga4bf3f820b493361a9a3b393d0282420fa1ab62f67902936349103d33f1475a328"></a>
<a id="gga4bf3f820b493361a9a3b393d0282420face445f78f84de0ef7c6d3ef23e3172b8"></a>
<a id="gga4bf3f820b493361a9a3b393d0282420fac6fad482035f2eab235dac4dffe77baa"></a>

---

[返回大纲](大纲.md) · [下一章](P002_音频_视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP）.md)
