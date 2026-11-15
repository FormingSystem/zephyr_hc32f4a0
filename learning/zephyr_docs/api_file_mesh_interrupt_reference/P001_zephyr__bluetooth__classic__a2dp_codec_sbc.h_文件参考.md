---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-1
title: zephyr__bluetooth__classic__a2dp_codec_sbc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_classic\_\_a2dp\_codec\_sbc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

高级音频分发配置文件（Advanced Audio Distribution Profile）的SBC编解码器头文件。

查看此文件的源码。

<a id="details"></a>

高级音频分发配置文件（Advanced Audio Distribution Profile）的SBC编解码器头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Fa2dp_5Fcodec_5Fsbc_5Fparams"></a>

```c
struct bt_a2dp_codec_sbc_params
```

相关声明：[bt_a2dp_codec_sbc_params](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md)。

子带编解码器（Subband Codec，SBC）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_a054dbbaf58ccc3b64142008e3da31ca5"></a>

```c
#define A2DP_SBC_SAMP_FREQ_16000 BIT(7)
```

相关声明：[A2DP_SBC_SAMP_FREQ_16000](#a054dbbaf58ccc3b64142008e3da31ca5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8e4b5399fb5366770a42fd4dfeece220"></a>

```c
#define A2DP_SBC_SAMP_FREQ_32000 BIT(6)
```

相关声明：[A2DP_SBC_SAMP_FREQ_32000](#a8e4b5399fb5366770a42fd4dfeece220)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a57d7b85560b36603651fae6c055c32c6"></a>

```c
#define A2DP_SBC_SAMP_FREQ_44100 BIT(5)
```

相关声明：[A2DP_SBC_SAMP_FREQ_44100](#a57d7b85560b36603651fae6c055c32c6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a0ebafbef2cddd4b6c7c7990ca77db0f9"></a>

```c
#define A2DP_SBC_SAMP_FREQ_48000 BIT(4)
```

相关声明：[A2DP_SBC_SAMP_FREQ_48000](#a0ebafbef2cddd4b6c7c7990ca77db0f9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aa9b58737fa1561b684a20980ea0b6feb"></a>

```c
#define A2DP_SBC_CH_MODE_MONO BIT(3)
```

相关声明：[A2DP_SBC_CH_MODE_MONO](#aa9b58737fa1561b684a20980ea0b6feb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aab5ab0b151f0a150c392be2f4cc82def"></a>

```c
#define A2DP_SBC_CH_MODE_DUAL BIT(2)
```

相关声明：[A2DP_SBC_CH_MODE_DUAL](#aab5ab0b151f0a150c392be2f4cc82def)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5557b7681eeaeb6f6fc78b3be84fc5cf"></a>

```c
#define A2DP_SBC_CH_MODE_STEREO BIT(1)
```

相关声明：[A2DP_SBC_CH_MODE_STEREO](#a5557b7681eeaeb6f6fc78b3be84fc5cf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_afcf64fa599e4d820dccdf40990f5ba39"></a>

```c
#define A2DP_SBC_CH_MODE_JOINT BIT(0)
```

相关声明：[A2DP_SBC_CH_MODE_JOINT](#afcf64fa599e4d820dccdf40990f5ba39)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a3abfc1c5202d2659055fc3480c2d3cc2"></a>

```c
#define A2DP_SBC_BLK_LEN_4 BIT(7)
```

相关声明：[A2DP_SBC_BLK_LEN_4](#a3abfc1c5202d2659055fc3480c2d3cc2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aeb90df4a33ce9ebdfc38d873fd54abab"></a>

```c
#define A2DP_SBC_BLK_LEN_8 BIT(6)
```

相关声明：[A2DP_SBC_BLK_LEN_8](#aeb90df4a33ce9ebdfc38d873fd54abab)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a9890a0cb8a813e010855c10fc4d22bf8"></a>

```c
#define A2DP_SBC_BLK_LEN_12 BIT(5)
```

相关声明：[A2DP_SBC_BLK_LEN_12](#a9890a0cb8a813e010855c10fc4d22bf8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1cb9425713c325442652fb406557e52a"></a>

```c
#define A2DP_SBC_BLK_LEN_16 BIT(4)
```

相关声明：[A2DP_SBC_BLK_LEN_16](#a1cb9425713c325442652fb406557e52a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad5916cf243e40e5a674ceed13477023e"></a>

```c
#define A2DP_SBC_SUBBAND_4 BIT(3)
```

相关声明：[A2DP_SBC_SUBBAND_4](#ad5916cf243e40e5a674ceed13477023e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a6b4bd1ef891c14c4f863c9623dcb63f7"></a>

```c
#define A2DP_SBC_SUBBAND_8 BIT(2)
```

相关声明：[A2DP_SBC_SUBBAND_8](#a6b4bd1ef891c14c4f863c9623dcb63f7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a7e54f1c971e1fd63e52f0322e7f85105"></a>

```c
#define A2DP_SBC_ALLOC_MTHD_SNR BIT(1)
```

相关声明：[A2DP_SBC_ALLOC_MTHD_SNR](#a7e54f1c971e1fd63e52f0322e7f85105)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a27d905ddf0fdb3dea4d3c12dd3ca33fe"></a>

```c
#define A2DP_SBC_ALLOC_MTHD_LOUDNESS BIT(0)
```

相关声明：[A2DP_SBC_ALLOC_MTHD_LOUDNESS](#a27d905ddf0fdb3dea4d3c12dd3ca33fe)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5b9313959439cc91be71efa214383ef7"></a>

```c
#define BT_A2DP_SBC_SAMP_FREQ(cap)
```

相关声明：[BT_A2DP_SBC_SAMP_FREQ](#a5b9313959439cc91be71efa214383ef7)。

<a id="r_a8d058052eb87cf22314395cc2581ac5d"></a>

```c
#define BT_A2DP_SBC_CHAN_MODE(cap)
```

相关声明：[BT_A2DP_SBC_CHAN_MODE](#a8d058052eb87cf22314395cc2581ac5d)。

<a id="r_a1721d8cc832b5a74306943074132369a"></a>

```c
#define BT_A2DP_SBC_BLK_LEN(cap)
```

相关声明：[BT_A2DP_SBC_BLK_LEN](#a1721d8cc832b5a74306943074132369a)。

<a id="r_aa4eb6816559e80400f1767e230d0efdf"></a>

```c
#define BT_A2DP_SBC_SUB_BAND(cap)
```

相关声明：[BT_A2DP_SBC_SUB_BAND](#aa4eb6816559e80400f1767e230d0efdf)。

<a id="r_a58878ea86ed87c6c5bfede0fe217ade8"></a>

```c
#define BT_A2DP_SBC_ALLOC_MTHD(cap)
```

相关声明：[BT_A2DP_SBC_ALLOC_MTHD](#a58878ea86ed87c6c5bfede0fe217ade8)。

<a id="r_a1937d233b15e4ddef71d2f4d433c61f1"></a>

```c
#define BT_A2DP_SBC_MIN_BITPOOL_VALUE 2
```

相关声明：[BT_A2DP_SBC_MIN_BITPOOL_VALUE](#a1937d233b15e4ddef71d2f4d433c61f1)。

<a id="r_a98d61864df5c48ed5ccab75b91938af9"></a>

```c
#define BT_A2DP_SBC_MAX_BITPOOL_VALUE 250
```

相关声明：[BT_A2DP_SBC_MAX_BITPOOL_VALUE](#a98d61864df5c48ed5ccab75b91938af9)。

<a id="r_a5d79c5a628c9740a81d5fe9626e14463"></a>

```c
#define BT_A2DP_SBC_MEDIA_HDR_NUM_FRAMES_GET(hdr)
```

相关声明：[BT_A2DP_SBC_MEDIA_HDR_NUM_FRAMES_GET](#a5d79c5a628c9740a81d5fe9626e14463)。

若 F 位为 0，此字段表示该数据包包含的帧数（Number of Frames）。

<a id="r_ab84850ce399e236f10ef80f0d2d2acde"></a>

```c
#define BT_A2DP_SBC_MEDIA_HDR_L_GET(hdr)
```

相关声明：[BT_A2DP_SBC_MEDIA_HDR_L_GET](#ab84850ce399e236f10ef80f0d2d2acde)。

对于已分片的 SBC 帧，最后一个数据包设为 1，否则设为 0。

<a id="r_a164ada24748d1fb21248274a02d11301"></a>

```c
#define BT_A2DP_SBC_MEDIA_HDR_S_GET(hdr)
```

相关声明：[BT_A2DP_SBC_MEDIA_HDR_S_GET](#a164ada24748d1fb21248274a02d11301)。

对于已分片的 SBC 帧，起始数据包设为 1，否则设为 0。

<a id="r_aaf18a29764a148b007f10e9a9f1a5437"></a>

```c
#define BT_A2DP_SBC_MEDIA_HDR_F_GET(hdr)
```

相关声明：[BT_A2DP_SBC_MEDIA_HDR_F_GET](#aaf18a29764a148b007f10e9a9f1a5437)。

SBC 帧已分片（Fragmented）时设为 1，否则设为 0。

<a id="r_af8da63e80785a6fa5a53fd29c6da5b9c"></a>

```c
#define BT_A2DP_SBC_MEDIA_HDR_NUM_FRAMES_SET(hdr, val)
```

相关声明：[BT_A2DP_SBC_MEDIA_HDR_NUM_FRAMES_SET](#af8da63e80785a6fa5a53fd29c6da5b9c)。

若 F 位为 0，此字段表示该数据包包含的帧数（Number of Frames）。

<a id="r_a7f00326a7dcd0839da6ea8557303c45f"></a>

```c
#define BT_A2DP_SBC_MEDIA_HDR_L_SET(hdr, val)
```

相关声明：[BT_A2DP_SBC_MEDIA_HDR_L_SET](#a7f00326a7dcd0839da6ea8557303c45f)。

对于已分片的 SBC 帧，最后一个数据包设为 1，否则设为 0。

<a id="r_a85bb7d78a1d654a68812517ddcebf76a"></a>

```c
#define BT_A2DP_SBC_MEDIA_HDR_S_SET(hdr, val)
```

相关声明：[BT_A2DP_SBC_MEDIA_HDR_S_SET](#a85bb7d78a1d654a68812517ddcebf76a)。

对于已分片的 SBC 帧，起始数据包设为 1，否则设为 0。

<a id="r_ab007b2c51612b05f9edc127bd9090536"></a>

```c
#define BT_A2DP_SBC_MEDIA_HDR_F_SET(hdr, val)
```

相关声明：[BT_A2DP_SBC_MEDIA_HDR_F_SET](#ab007b2c51612b05f9edc127bd9090536)。

SBC 帧已分片（Fragmented）时设为 1，否则设为 0。

<a id="r_aa9a0484c4eefe685c0cbde87ce781734"></a>

```c
#define BT_A2DP_SBC_MEDIA_HDR_ENCODE(num_frames, l, s, f)
```

相关声明：[BT_A2DP_SBC_MEDIA_HDR_ENCODE](#aa9a0484c4eefe685c0cbde87ce781734)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_a8791ff3f4f02b46ea879df5e20ba5dd6"></a>

```c
uint8_t bt_a2dp_sbc_get_channel_num (struct bt_a2dp_codec_sbc_params *sbc_codec)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_a2dp_sbc_get_channel_num](#a8791ff3f4f02b46ea879df5e20ba5dd6)、[bt_a2dp_codec_sbc_params](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md)。

获取高级音频分发配置文件（A2DP）的 SBC 配置中的声道数（Channel Number）。

<a id="r_a3b02634c61ba25cf678e57fa587fca64"></a>

```c
enum sbc_ch_mode bt_a2dp_sbc_get_channel_mode (struct bt_a2dp_codec_sbc_params *sbc_codec)
```

相关声明：[sbc_ch_mode](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a0513bb34588f5c6d428b141f34c234f6)、[bt_a2dp_sbc_get_channel_mode](#a3b02634c61ba25cf678e57fa587fca64)、[bt_a2dp_codec_sbc_params](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md)。

获取 A2DP SBC 配置中的声道模式（Channel Mode）。

<a id="r_a7af2c05d2605d7d21e656222238922c1"></a>

```c
uint32_t bt_a2dp_sbc_get_sampling_frequency (struct bt_a2dp_codec_sbc_params *sbc_codec)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bt_a2dp_sbc_get_sampling_frequency](#a7af2c05d2605d7d21e656222238922c1)、[bt_a2dp_codec_sbc_params](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md)。

获取 A2DP SBC 配置中的采样率（Sample Rate）。

<a id="r_ae670124fb972e097e8c0f99767d7aa0f"></a>

```c
uint8_t bt_a2dp_sbc_get_subband_num (struct bt_a2dp_codec_sbc_params *sbc_codec)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_a2dp_sbc_get_subband_num](#ae670124fb972e097e8c0f99767d7aa0f)、[bt_a2dp_codec_sbc_params](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md)。

获取 A2DP SBC 配置中的子带数（Subband Number）。

<a id="r_ae176b825b7c476ec1dc256a6eb5d16fd"></a>

```c
uint8_t bt_a2dp_sbc_get_block_length (struct bt_a2dp_codec_sbc_params *sbc_codec)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_a2dp_sbc_get_block_length](#ae176b825b7c476ec1dc256a6eb5d16fd)、[bt_a2dp_codec_sbc_params](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md)。

获取 A2DP SBC 配置中的块长度（Block Length）。

<a id="r_a50d294df6ebf62cc642d08d9b0b45a83"></a>

```c
enum sbc_alloc_mthd bt_a2dp_sbc_get_allocation_method (struct bt_a2dp_codec_sbc_params *sbc_codec)
```

相关声明：[sbc_alloc_mthd](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a43b42f96c2d87bbcea4fb230fd8f3a5f)、[bt_a2dp_sbc_get_allocation_method](#a50d294df6ebf62cc642d08d9b0b45a83)、[bt_a2dp_codec_sbc_params](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md)。

获取 A2DP SBC 配置中的分配方法（Allocation Method）。

## 1.4\_详细说明（Detailed Documentation）

<a id="a27d905ddf0fdb3dea4d3c12dd3ca33fe"></a>

### `A2DP_SBC_ALLOC_MTHD_LOUDNESS`

```c
#define A2DP_SBC_ALLOC_MTHD_LOUDNESS BIT(0)
```

<a id="a7e54f1c971e1fd63e52f0322e7f85105"></a>

### `A2DP_SBC_ALLOC_MTHD_SNR`

```c
#define A2DP_SBC_ALLOC_MTHD_SNR BIT(1)
```

<a id="a9890a0cb8a813e010855c10fc4d22bf8"></a>

### `A2DP_SBC_BLK_LEN_12`

```c
#define A2DP_SBC_BLK_LEN_12 BIT(5)
```

<a id="a1cb9425713c325442652fb406557e52a"></a>

### `A2DP_SBC_BLK_LEN_16`

```c
#define A2DP_SBC_BLK_LEN_16 BIT(4)
```

<a id="a3abfc1c5202d2659055fc3480c2d3cc2"></a>

### `A2DP_SBC_BLK_LEN_4`

```c
#define A2DP_SBC_BLK_LEN_4 BIT(7)
```

<a id="aeb90df4a33ce9ebdfc38d873fd54abab"></a>

### `A2DP_SBC_BLK_LEN_8`

```c
#define A2DP_SBC_BLK_LEN_8 BIT(6)
```

<a id="aab5ab0b151f0a150c392be2f4cc82def"></a>

### `A2DP_SBC_CH_MODE_DUAL`

```c
#define A2DP_SBC_CH_MODE_DUAL BIT(2)
```

<a id="afcf64fa599e4d820dccdf40990f5ba39"></a>

### `A2DP_SBC_CH_MODE_JOINT`

```c
#define A2DP_SBC_CH_MODE_JOINT BIT(0)
```

<a id="aa9b58737fa1561b684a20980ea0b6feb"></a>

### `A2DP_SBC_CH_MODE_MONO`

```c
#define A2DP_SBC_CH_MODE_MONO BIT(3)
```

<a id="a5557b7681eeaeb6f6fc78b3be84fc5cf"></a>

### `A2DP_SBC_CH_MODE_STEREO`

```c
#define A2DP_SBC_CH_MODE_STEREO BIT(1)
```

<a id="a054dbbaf58ccc3b64142008e3da31ca5"></a>

### `A2DP_SBC_SAMP_FREQ_16000`

```c
#define A2DP_SBC_SAMP_FREQ_16000 BIT(7)
```

<a id="a8e4b5399fb5366770a42fd4dfeece220"></a>

### `A2DP_SBC_SAMP_FREQ_32000`

```c
#define A2DP_SBC_SAMP_FREQ_32000 BIT(6)
```

<a id="a57d7b85560b36603651fae6c055c32c6"></a>

### `A2DP_SBC_SAMP_FREQ_44100`

```c
#define A2DP_SBC_SAMP_FREQ_44100 BIT(5)
```

<a id="a0ebafbef2cddd4b6c7c7990ca77db0f9"></a>

### `A2DP_SBC_SAMP_FREQ_48000`

```c
#define A2DP_SBC_SAMP_FREQ_48000 BIT(4)
```

<a id="ad5916cf243e40e5a674ceed13477023e"></a>

### `A2DP_SBC_SUBBAND_4`

```c
#define A2DP_SBC_SUBBAND_4 BIT(3)
```

<a id="a6b4bd1ef891c14c4f863c9623dcb63f7"></a>

### `A2DP_SBC_SUBBAND_8`

```c
#define A2DP_SBC_SUBBAND_8 BIT(2)
```

<a id="a58878ea86ed87c6c5bfede0fe217ade8"></a>

### `BT_A2DP_SBC_ALLOC_MTHD`

```c
#define BT_A2DP_SBC_ALLOC_MTHD ( cap)
```

展开值（Value）：

```c
((cap->config[1]) & 0x03)
```

<a id="a1721d8cc832b5a74306943074132369a"></a>

### `BT_A2DP_SBC_BLK_LEN`

```c
#define BT_A2DP_SBC_BLK_LEN ( cap)
```

展开值（Value）：

```c
((cap->config[1] >> 4) & 0x0f)
```

<a id="a8d058052eb87cf22314395cc2581ac5d"></a>

### `BT_A2DP_SBC_CHAN_MODE`

```c
#define BT_A2DP_SBC_CHAN_MODE ( cap)
```

展开值（Value）：

```c
((cap->config[0]) & 0x0f)
```

<a id="a98d61864df5c48ed5ccab75b91938af9"></a>

### `BT_A2DP_SBC_MAX_BITPOOL_VALUE`

```c
#define BT_A2DP_SBC_MAX_BITPOOL_VALUE 250
```

<a id="aa9a0484c4eefe685c0cbde87ce781734"></a>

### `BT_A2DP_SBC_MEDIA_HDR_ENCODE`

```c
#define BT_A2DP_SBC_MEDIA_HDR_ENCODE ( num_frames, l, s, f )
```

展开值（Value）：

```c
FIELD_PREP(GENMASK(3, 0), num_frames) | FIELD_PREP(BIT(5), l) |\
FIELD_PREP(BIT(6), s) | FIELD_PREP(BIT(7), f)
```

<a id="aaf18a29764a148b007f10e9a9f1a5437"></a>

### `BT_A2DP_SBC_MEDIA_HDR_F_GET`

```c
#define BT_A2DP_SBC_MEDIA_HDR_F_GET ( hdr)
```

展开值（Value）：

```c
FIELD_GET(BIT(7), (hdr))
```

SBC 帧已分片（Fragmented）时设为 1，否则设为 0。

<a id="ab007b2c51612b05f9edc127bd9090536"></a>

### `BT_A2DP_SBC_MEDIA_HDR_F_SET`

```c
#define BT_A2DP_SBC_MEDIA_HDR_F_SET ( hdr, val )
```

展开值（Value）：

```c
hdr = ((hdr) & ~BIT(7)) | FIELD_PREP(BIT(7), (val))
```

SBC 帧已分片（Fragmented）时设为 1，否则设为 0。

<a id="ab84850ce399e236f10ef80f0d2d2acde"></a>

### `BT_A2DP_SBC_MEDIA_HDR_L_GET`

```c
#define BT_A2DP_SBC_MEDIA_HDR_L_GET ( hdr)
```

展开值（Value）：

```c
FIELD_GET(BIT(5), (hdr))
```

对于已分片的 SBC 帧，最后一个数据包设为 1，否则设为 0。

<a id="a7f00326a7dcd0839da6ea8557303c45f"></a>

### `BT_A2DP_SBC_MEDIA_HDR_L_SET`

```c
#define BT_A2DP_SBC_MEDIA_HDR_L_SET ( hdr, val )
```

展开值（Value）：

```c
hdr = ((hdr) & ~BIT(5)) | FIELD_PREP(BIT(5), (val))
```

对于已分片的 SBC 帧，最后一个数据包设为 1，否则设为 0。

<a id="a5d79c5a628c9740a81d5fe9626e14463"></a>

### `BT_A2DP_SBC_MEDIA_HDR_NUM_FRAMES_GET`

```c
#define BT_A2DP_SBC_MEDIA_HDR_NUM_FRAMES_GET ( hdr)
```

展开值（Value）：

```c
FIELD_GET(GENMASK(3, 0), (hdr))
```

若 F 位为 0，此字段表示该数据包包含的帧数（Number of Frames）。

若 F 位为 1，此字段表示剩余分片（Remaining Fragments）的数量，包括当前分片。因此，最后一次的计数值必须为 1。

<a id="af8da63e80785a6fa5a53fd29c6da5b9c"></a>

### `BT_A2DP_SBC_MEDIA_HDR_NUM_FRAMES_SET`

```c
#define BT_A2DP_SBC_MEDIA_HDR_NUM_FRAMES_SET ( hdr, val )
```

展开值（Value）：

```c
hdr = ((hdr) & ~GENMASK(3, 0)) | FIELD_PREP(GENMASK(3, 0), (val))
```

若 F 位为 0，此字段表示该数据包包含的帧数（Number of Frames）。

若 F 位为 1，此字段表示剩余分片（Remaining Fragments）的数量，包括当前分片。因此，最后一次的计数值必须为 1。

<a id="a164ada24748d1fb21248274a02d11301"></a>

### `BT_A2DP_SBC_MEDIA_HDR_S_GET`

```c
#define BT_A2DP_SBC_MEDIA_HDR_S_GET ( hdr)
```

展开值（Value）：

```c
FIELD_GET(BIT(6), (hdr))
```

对于已分片的 SBC 帧，起始数据包设为 1，否则设为 0。

<a id="a85bb7d78a1d654a68812517ddcebf76a"></a>

### `BT_A2DP_SBC_MEDIA_HDR_S_SET`

```c
#define BT_A2DP_SBC_MEDIA_HDR_S_SET ( hdr, val )
```

展开值（Value）：

```c
hdr = ((hdr) & ~BIT(6)) | FIELD_PREP(BIT(6), (val))
```

对于已分片的 SBC 帧，起始数据包设为 1，否则设为 0。

<a id="a1937d233b15e4ddef71d2f4d433c61f1"></a>

### `BT_A2DP_SBC_MIN_BITPOOL_VALUE`

```c
#define BT_A2DP_SBC_MIN_BITPOOL_VALUE 2
```

<a id="a5b9313959439cc91be71efa214383ef7"></a>

### `BT_A2DP_SBC_SAMP_FREQ`

```c
#define BT_A2DP_SBC_SAMP_FREQ ( cap)
```

展开值（Value）：

```c
((cap->config[0] >> 4) & 0x0f)
```

<a id="aa4eb6816559e80400f1767e230d0efdf"></a>

### `BT_A2DP_SBC_SUB_BAND`

```c
#define BT_A2DP_SBC_SUB_BAND ( cap)
```

展开值（Value）：

```c
((cap->config[1] >> 2) & 0x03)
```

<a id="a50d294df6ebf62cc642d08d9b0b45a83"></a>

### `bt_a2dp_sbc_get_allocation_method()`

```c
enum sbc_alloc_mthd bt_a2dp_sbc_get_allocation_method ( struct bt_a2dp_codec_sbc_params * sbc_codec)
```

获取 A2DP SBC 配置中的分配方法（Allocation Method）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sbc_codec` | A2DP SBC 参数（Parameter）。 |

**返回（Returns）**：返回值：分配方法（Allocation Method）。

<a id="ae176b825b7c476ec1dc256a6eb5d16fd"></a>

### `bt_a2dp_sbc_get_block_length()`

```c
uint8_t bt_a2dp_sbc_get_block_length ( struct bt_a2dp_codec_sbc_params * sbc_codec)
```

获取 A2DP SBC 配置中的块长度（Block Length）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sbc_codec` | A2DP SBC 参数（Parameter）。 |

**返回（Returns）**：返回值：块长度（Block Length）。

<a id="a3b02634c61ba25cf678e57fa587fca64"></a>

### `bt_a2dp_sbc_get_channel_mode()`

```c
enum sbc_ch_mode bt_a2dp_sbc_get_channel_mode ( struct bt_a2dp_codec_sbc_params * sbc_codec)
```

获取 A2DP SBC 配置中的声道模式（Channel Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sbc_codec` | A2DP SBC 参数（Parameter）。 |

**返回（Returns）**：返回值：声道模式（Channel Mode）。

<a id="a8791ff3f4f02b46ea879df5e20ba5dd6"></a>

### `bt_a2dp_sbc_get_channel_num()`

```c
uint8_t bt_a2dp_sbc_get_channel_num ( struct bt_a2dp_codec_sbc_params * sbc_codec)
```

获取高级音频分发配置文件（A2DP）的 SBC 配置中的声道数（Channel Number）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sbc_codec` | A2DP SBC 参数（Parameter）。 |

**返回（Returns）**：返回值：声道数（Channel Number）。

<a id="a7af2c05d2605d7d21e656222238922c1"></a>

### `bt_a2dp_sbc_get_sampling_frequency()`

```c
uint32_t bt_a2dp_sbc_get_sampling_frequency ( struct bt_a2dp_codec_sbc_params * sbc_codec)
```

获取 A2DP SBC 配置中的采样率（Sample Rate）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sbc_codec` | A2DP SBC 参数（Parameter）。 |

**返回（Returns）**：返回值：采样率（Sample Rate）。

<a id="ae670124fb972e097e8c0f99767d7aa0f"></a>

### `bt_a2dp_sbc_get_subband_num()`

```c
uint8_t bt_a2dp_sbc_get_subband_num ( struct bt_a2dp_codec_sbc_params * sbc_codec)
```

获取 A2DP SBC 配置中的子带数（Subband Number）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sbc_codec` | A2DP SBC 参数（Parameter）。 |

**返回（Returns）**：返回值：子带数（Subband Number）。


## 1.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_architecture_reference/P001_a2dp_codec_sbc.h_源码浏览.md)
- [bt_a2dp_codec_sbc_params](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sbc_ch_mode](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a0513bb34588f5c6d428b141f34c234f6)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [sbc_alloc_mthd](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a43b42f96c2d87bbcea4fb230fd8f3a5f)
- [FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [FIELD_GET](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa49a456f06f7bdbedfcf3517e461947e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys-util_html_ga58530d20924859d16358c7400c37738d"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa03c8b31bf67a097dd9f8153a04ef86b"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa49a456f06f7bdbedfcf3517e461947e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__clock__alif-balletto-clocks.h_文件参考.md)
