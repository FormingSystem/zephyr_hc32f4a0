---
id: learning.zephyr-docs.api-source-architecture-reference.page-1
title: a2dp_codec_sbc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_a2dp\_codec\_sbc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h.html)。

## 1.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00090"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="foldopen00099"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00102"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="aa2dp__codec__sbc_8h_html_a3b02634c61ba25cf678e57fa587fca64"></a>
<a id="aa2dp__codec__sbc_8h_html_a50d294df6ebf62cc642d08d9b0b45a83"></a>
<a id="aa2dp__codec__sbc_8h_html_a7af2c05d2605d7d21e656222238922c1"></a>
<a id="aa2dp__codec__sbc_8h_html_a8791ff3f4f02b46ea879df5e20ba5dd6"></a>
<a id="aa2dp__codec__sbc_8h_html_ae176b825b7c476ec1dc256a6eb5d16fd"></a>
<a id="aa2dp__codec__sbc_8h_html_ae670124fb972e097e8c0f99767d7aa0f"></a>
<a id="asbc_8h_html_a0513bb34588f5c6d428b141f34c234f6"></a>
<a id="asbc_8h_html_a43b42f96c2d87bbcea4fb230fd8f3a5f"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__a2dp__codec__sbc__params_html"></a>
<a id="astructbt__a2dp__codec__sbc__params_html_a026f28b42a3e8b41a2597cfa4ca01f95"></a>
<a id="astructbt__a2dp__codec__sbc__params_html_a34319bc3d168e5eb7d3ef2cae521ca96"></a>
<a id="astructbt__a2dp__codec__sbc__params_html_a80b0705befa9c573e4653a5f88f81e8d"></a>

```c

/*
 * SPDX-License-Identifier: Apache-2.0
 * Copyright (c) 2015-2016 Intel Corporation
 * Copyright (c) 2021 NXP
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_A2DP_CODEC_SBC_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_A2DP_CODEC_SBC_H_

#ifdef __cplusplus
extern "C" {
#endif

/* Sampling Frequency */
#define A2DP_SBC_SAMP_FREQ_16000 BIT(7)
#define A2DP_SBC_SAMP_FREQ_32000 BIT(6)
#define A2DP_SBC_SAMP_FREQ_44100 BIT(5)
#define A2DP_SBC_SAMP_FREQ_48000 BIT(4)

/* Channel Mode */
#define A2DP_SBC_CH_MODE_MONO   BIT(3)
#define A2DP_SBC_CH_MODE_DUAL   BIT(2)
#define A2DP_SBC_CH_MODE_STEREO BIT(1)
#define A2DP_SBC_CH_MODE_JOINT  BIT(0)

/* Block Length */
#define A2DP_SBC_BLK_LEN_4  BIT(7)
#define A2DP_SBC_BLK_LEN_8  BIT(6)
#define A2DP_SBC_BLK_LEN_12 BIT(5)
#define A2DP_SBC_BLK_LEN_16 BIT(4)

/* Subbands */
#define A2DP_SBC_SUBBAND_4 BIT(3)
#define A2DP_SBC_SUBBAND_8 BIT(2)

/* Allocation Method */
#define A2DP_SBC_ALLOC_MTHD_SNR      BIT(1)
#define A2DP_SBC_ALLOC_MTHD_LOUDNESS BIT(0)

#define BT_A2DP_SBC_SAMP_FREQ(cap)    ((cap->config[0] >> 4) & 0x0f)
#define BT_A2DP_SBC_CHAN_MODE(cap)    ((cap->config[0]) & 0x0f)
#define BT_A2DP_SBC_BLK_LEN(cap)      ((cap->config[1] >> 4) & 0x0f)
#define BT_A2DP_SBC_SUB_BAND(cap)     ((cap->config[1] >> 2) & 0x03)
#define BT_A2DP_SBC_ALLOC_MTHD(cap)   ((cap->config[1]) & 0x03)
#define BT_A2DP_SBC_MIN_BITPOOL_VALUE  2
#define BT_A2DP_SBC_MAX_BITPOOL_VALUE  250

struct bt_a2dp_codec_sbc_params {
        uint8_t config[2];
        uint8_t min_bitpool;
        uint8_t max_bitpool;
} __packed;

#define BT_A2DP_SBC_MEDIA_HDR_NUM_FRAMES_GET(hdr) FIELD_GET(GENMASK(3, 0), (hdr))
#define BT_A2DP_SBC_MEDIA_HDR_L_GET(hdr)          FIELD_GET(BIT(5), (hdr))
#define BT_A2DP_SBC_MEDIA_HDR_S_GET(hdr)          FIELD_GET(BIT(6), (hdr))
#define BT_A2DP_SBC_MEDIA_HDR_F_GET(hdr)          FIELD_GET(BIT(7), (hdr))

#define BT_A2DP_SBC_MEDIA_HDR_NUM_FRAMES_SET(hdr, val)\
        hdr = ((hdr) & ~GENMASK(3, 0)) | FIELD_PREP(GENMASK(3, 0), (val))

#define BT_A2DP_SBC_MEDIA_HDR_L_SET(hdr, val)\
        hdr = ((hdr) & ~BIT(5)) | FIELD_PREP(BIT(5), (val))

#define BT_A2DP_SBC_MEDIA_HDR_S_SET(hdr, val)\
        hdr = ((hdr) & ~BIT(6)) | FIELD_PREP(BIT(6), (val))

#define BT_A2DP_SBC_MEDIA_HDR_F_SET(hdr, val)\
        hdr = ((hdr) & ~BIT(7)) | FIELD_PREP(BIT(7), (val))

#define BT_A2DP_SBC_MEDIA_HDR_ENCODE(num_frames, l, s, f)\
        FIELD_PREP(GENMASK(3, 0), num_frames) | FIELD_PREP(BIT(5), l) |\
        FIELD_PREP(BIT(6), s) | FIELD_PREP(BIT(7), f)

uint8_t bt_a2dp_sbc_get_channel_num(struct bt_a2dp_codec_sbc_params *sbc_codec);

enum sbc_ch_mode bt_a2dp_sbc_get_channel_mode(struct bt_a2dp_codec_sbc_params *sbc_codec);

uint32_t bt_a2dp_sbc_get_sampling_frequency(struct bt_a2dp_codec_sbc_params *sbc_codec);

uint8_t bt_a2dp_sbc_get_subband_num(struct bt_a2dp_codec_sbc_params *sbc_codec);

uint8_t bt_a2dp_sbc_get_block_length(struct bt_a2dp_codec_sbc_params *sbc_codec);

enum sbc_alloc_mthd bt_a2dp_sbc_get_allocation_method(struct bt_a2dp_codec_sbc_params *sbc_codec);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_A2DP_CODEC_SBC_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 4 行

SPDX-License-Identifier: Apache-2.0。
版权所有（Copyright）2015～2016 Intel Corporation。
版权所有（Copyright）2021 NXP。

本文件依据 Apache 许可证 2.0 版（Apache License, Version 2.0，以下简称“许可证”）授权；除非遵守许可证，否则不得使用本文件。可在以下地址获取许可证副本：
<http://www.apache.org/licenses/LICENSE-2.0>

除非适用法律另有要求或以书面形式另行约定，依据许可证分发的软件均按“原样”（AS IS）提供，不附带任何明示或默示的保证或条件。有关许可证授予的具体权限及限制，请参阅许可证。

### 注释 2：原第 28 行

采样频率（Sampling Frequency）。

### 注释 3：原第 34 行

通道模式（Channel Mode）。

### 注释 4：原第 40 行

块长度（Block Length）。

### 注释 5：原第 46 行

子带（Subbands）。

### 注释 6：原第 50 行

分配方法（Allocation Method）。

### 注释 7：原第 158 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_A2DP_CODEC_SBC_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h.html)
- [bt_a2dp_codec_sbc_params](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [config](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md#a80b0705befa9c573e4653a5f88f81e8d)
- [min_bitpool](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md#a026f28b42a3e8b41a2597cfa4ca01f95)
- [max_bitpool](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md#a34319bc3d168e5eb7d3ef2cae521ca96)
- [bt_a2dp_sbc_get_channel_num](https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h.html#a8791ff3f4f02b46ea879df5e20ba5dd6)
- [sbc_ch_mode](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a0513bb34588f5c6d428b141f34c234f6)
- [bt_a2dp_sbc_get_channel_mode](https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h.html#a3b02634c61ba25cf678e57fa587fca64)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_a2dp_sbc_get_sampling_frequency](https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h.html#a7af2c05d2605d7d21e656222238922c1)
- [bt_a2dp_sbc_get_subband_num](https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h.html#ae670124fb972e097e8c0f99767d7aa0f)
- [bt_a2dp_sbc_get_block_length](https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h.html#ae176b825b7c476ec1dc256a6eb5d16fd)
- [sbc_alloc_mthd](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a43b42f96c2d87bbcea4fb230fd8f3a5f)
- [bt_a2dp_sbc_get_allocation_method](https://docs.zephyrproject.org/latest/doxygen/html/a2dp__codec__sbc_8h.html#a50d294df6ebf62cc642d08d9b0b45a83)
- [bt_a2dp_codec_sbc_params::min_bitpool](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md#a026f28b42a3e8b41a2597cfa4ca01f95)
- [bt_a2dp_codec_sbc_params::max_bitpool](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md#a34319bc3d168e5eb7d3ef2cae521ca96)
- [bt_a2dp_codec_sbc_params::config](../bluetooth_classic_model_reference/P005_bt_a2dp_codec_sbc_params_结构体.md#a80b0705befa9c573e4653a5f88f81e8d)

---

[返回大纲](大纲.md) · [下一章](P002_b91-pinctrl.h_源码浏览.md)
