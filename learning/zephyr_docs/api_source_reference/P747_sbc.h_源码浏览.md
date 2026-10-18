---
id: learning.zephyr-docs.api-source-reference.page-747
title: sbc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第747章\_sbc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html)。

## 747.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
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
<a id="foldopen00019"></a>
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00112"></a>
<a id="l00112"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="asbc_8h_html_a0513bb34588f5c6d428b141f34c234f6"></a>
<a id="asbc_8h_html_a0513bb34588f5c6d428b141f34c234f6a1001ed03373ad85bfe498c51e763e608"></a>
<a id="asbc_8h_html_a0513bb34588f5c6d428b141f34c234f6a234fe60a35e743c4feeda0bb26e940d3"></a>
<a id="asbc_8h_html_a0513bb34588f5c6d428b141f34c234f6a30c7c23457ab3de5c293c654077d9e7e"></a>
<a id="asbc_8h_html_a0513bb34588f5c6d428b141f34c234f6a4b4a5407b69d6d3ce4713791596b42dc"></a>
<a id="asbc_8h_html_a43b42f96c2d87bbcea4fb230fd8f3a5f"></a>
<a id="asbc_8h_html_a43b42f96c2d87bbcea4fb230fd8f3a5fa0fe0046f999213dec1f7aa9186eb13c5"></a>
<a id="asbc_8h_html_a43b42f96c2d87bbcea4fb230fd8f3a5fa8bd17f97e15ad2c95c2a2886db56c91c"></a>
<a id="asbc_8h_html_a46d8d7671567d93a9cd28faedb14c050"></a>
<a id="asbc_8h_html_a542096b8adb98ef03f2381d3aa4c159e"></a>
<a id="asbc_8h_html_a652a6c40ae296c63d7a31104c3fea007"></a>
<a id="asbc_8h_html_a8b850a924dfee57a001e041164de6eb7"></a>
<a id="asbc_8h_html_a99bfc2a65061e3bbd02095593478761e"></a>
<a id="asbc_8h_html_aaf6292a3340023ea26566f9c9d5862e9"></a>
<a id="asbc_8h_html_acb546af83d4e748959a40a552c8d498e"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astring_8h_html"></a>
<a id="astructsbc__decoder_html"></a>
<a id="astructsbc__encoder__init__param_html"></a>
<a id="astructsbc__encoder__init__param_html_a3b8a6758fc1ef3c1c5ef1348e4d12ca9"></a>
<a id="astructsbc__encoder__init__param_html_a5b537961f58be5b9b6df11f0afe4f990"></a>
<a id="astructsbc__encoder__init__param_html_a668a198600211325788a168efe15d016"></a>
<a id="astructsbc__encoder__init__param_html_a81742a0770d1f6e3723015baa2152edd"></a>
<a id="astructsbc__encoder__init__param_html_a96a0c9a9657a6dce6e08e0648d844379"></a>
<a id="astructsbc__encoder__init__param_html_a9a89d1044e10290e40265b64cd26067b"></a>
<a id="astructsbc__encoder__init__param_html_a9f2e03203a3ef41303c8de9c93198db1"></a>
<a id="astructsbc__encoder__init__param_html_ad1f099d0d03f0c0d10febf2f7b3502d7"></a>
<a id="astructsbc__encoder__init__param_html_afb951bb13f5ad27ea9bba9ebc82e9776"></a>
<a id="astructsbc__encoder_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright 2024 - 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_SBC_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_SBC_H_

#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <zephyr/toolchain.h>
#include "sbc_encoder.h"
#include "oi_codec_sbc.h"
#include "oi_status.h"

enum __packed sbc_ch_mode {
        SBC_CH_MODE_MONO,
        SBC_CH_MODE_DUAL_CHANNEL,
        SBC_CH_MODE_STEREO,
        SBC_CH_MODE_JOINT_STEREO,
};

enum __packed sbc_alloc_mthd {
        SBC_ALLOC_MTHD_LOUDNESS,
        SBC_ALLOC_MTHD_SNR,
};

struct sbc_encoder {
        SBC_ENC_PARAMS sbc_encoder_params;
};

struct sbc_encoder_init_param {
        uint32_t bit_rate;
        uint32_t samp_freq;
        uint8_t blk_len;
        uint8_t subband;
        enum sbc_alloc_mthd alloc_mthd;
        enum sbc_ch_mode ch_mode;
        uint8_t ch_num;
        uint8_t min_bitpool;
        uint8_t max_bitpool;
};

int sbc_setup_encoder(struct sbc_encoder *encoder, struct sbc_encoder_init_param *param);

uint32_t sbc_encode(struct sbc_encoder *encoder, const void *in_data, void *out_data);

int sbc_frame_samples(struct sbc_encoder *encoder);

int sbc_frame_bytes(struct sbc_encoder *encoder);

int sbc_frame_encoded_bytes(struct sbc_encoder *encoder);

struct sbc_decoder {
        OI_CODEC_SBC_DECODER_CONTEXT context;
        uint32_t context_data[CODEC_DATA_WORDS(2, SBC_CODEC_FAST_FILTER_BUFFERS)];
};

int sbc_setup_decoder(struct sbc_decoder *decoder);

int sbc_decode(struct sbc_decoder *decoder, const void **in_data, uint32_t *in_size,
                void *out_data, uint32_t *out_size);
#endif /* ZEPHYR_INCLUDE_BLUETOOTH_SBC_H_ */
```

## 747.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 - 2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 140 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_SBC_H_`。

## 747.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [sbc_ch_mode](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a0513bb34588f5c6d428b141f34c234f6)
- [SBC_CH_MODE_MONO](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a0513bb34588f5c6d428b141f34c234f6a1001ed03373ad85bfe498c51e763e608)
- [SBC_CH_MODE_DUAL_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a0513bb34588f5c6d428b141f34c234f6a4b4a5407b69d6d3ce4713791596b42dc)
- [SBC_CH_MODE_STEREO](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a0513bb34588f5c6d428b141f34c234f6a30c7c23457ab3de5c293c654077d9e7e)
- [SBC_CH_MODE_JOINT_STEREO](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a0513bb34588f5c6d428b141f34c234f6a234fe60a35e743c4feeda0bb26e940d3)
- [sbc_alloc_mthd](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a43b42f96c2d87bbcea4fb230fd8f3a5f)
- [SBC_ALLOC_MTHD_LOUDNESS](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a43b42f96c2d87bbcea4fb230fd8f3a5fa0fe0046f999213dec1f7aa9186eb13c5)
- [SBC_ALLOC_MTHD_SNR](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a43b42f96c2d87bbcea4fb230fd8f3a5fa8bd17f97e15ad2c95c2a2886db56c91c)
- [sbc_encoder](../audio_video_model_reference/P046_sbc_encoder_结构体.md)
- [sbc_encoder_init_param](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bit_rate](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a9a89d1044e10290e40265b64cd26067b)
- [samp_freq](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a81742a0770d1f6e3723015baa2152edd)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [blk_len](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a9f2e03203a3ef41303c8de9c93198db1)
- [subband](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#ad1f099d0d03f0c0d10febf2f7b3502d7)
- [alloc_mthd](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a3b8a6758fc1ef3c1c5ef1348e4d12ca9)
- [ch_mode](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#afb951bb13f5ad27ea9bba9ebc82e9776)
- [ch_num](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a668a198600211325788a168efe15d016)
- [min_bitpool](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a5b537961f58be5b9b6df11f0afe4f990)
- [max_bitpool](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a96a0c9a9657a6dce6e08e0648d844379)
- [sbc_setup_encoder](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a542096b8adb98ef03f2381d3aa4c159e)
- [sbc_encode](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a652a6c40ae296c63d7a31104c3fea007)
- [sbc_frame_samples](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a8b850a924dfee57a001e041164de6eb7)
- [sbc_frame_bytes](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a46d8d7671567d93a9cd28faedb14c050)
- [sbc_frame_encoded_bytes](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#a99bfc2a65061e3bbd02095593478761e)
- [sbc_decoder](../audio_video_model_reference/P045_sbc_decoder_结构体.md)
- [sbc_setup_decoder](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#aaf6292a3340023ea26566f9c9d5862e9)
- [sbc_decode](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html#acb546af83d4e748959a40a552c8d498e)
- [sbc_encoder_init_param::alloc_mthd](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a3b8a6758fc1ef3c1c5ef1348e4d12ca9)
- [sbc_encoder_init_param::min_bitpool](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a5b537961f58be5b9b6df11f0afe4f990)
- [sbc_encoder_init_param::ch_num](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a668a198600211325788a168efe15d016)
- [sbc_encoder_init_param::samp_freq](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a81742a0770d1f6e3723015baa2152edd)
- [sbc_encoder_init_param::max_bitpool](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a96a0c9a9657a6dce6e08e0648d844379)
- [sbc_encoder_init_param::bit_rate](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a9a89d1044e10290e40265b64cd26067b)
- [sbc_encoder_init_param::blk_len](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#a9f2e03203a3ef41303c8de9c93198db1)
- [sbc_encoder_init_param::subband](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#ad1f099d0d03f0c0d10febf2f7b3502d7)
- [sbc_encoder_init_param::ch_mode](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md#afb951bb13f5ad27ea9bba9ebc82e9776)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P746_sar_cfg_srv.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P748_scd4x.h_源码浏览.md)
