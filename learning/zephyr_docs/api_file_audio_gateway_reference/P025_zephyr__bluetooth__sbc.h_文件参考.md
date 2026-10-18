---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-25
title: zephyr__bluetooth__sbc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_bluetooth\_\_sbc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sbc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <zephyr/toolchain.h>
#include "sbc_encoder.h"
#include "oi_codec_sbc.h"
#include "oi_status.h"
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 25.1\_数据结构（Data Structures）

<a id="r_sbc_5Fencoder"></a>

```c
struct sbc_encoder
```

相关声明：[sbc_encoder](../audio_video_model_reference/P046_sbc_encoder_结构体.md)。

子带编解码器（SBC）的编码器。

<a id="r_sbc_5Fencoder_5Finit_5Fparam"></a>

```c
struct sbc_encoder_init_param
```

相关声明：[sbc_encoder_init_param](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md)。

编码器初始化参数（Encoder Initialization Parameters）。

<a id="r_sbc_5Fdecoder"></a>

```c
struct sbc_decoder
```

相关声明：[sbc_decoder](../audio_video_model_reference/P045_sbc_decoder_结构体.md)。

子带编解码器（SBC）的解码器。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 25.2\_枚举（Enumerations）

<a id="r_a0513bb34588f5c6d428b141f34c234f6"></a>

```c
enum sbc_ch_mode { SBC_CH_MODE_MONO , SBC_CH_MODE_DUAL_CHANNEL , SBC_CH_MODE_STEREO , SBC_CH_MODE_JOINT_STEREO }
```

相关声明：[sbc_ch_mode](#a0513bb34588f5c6d428b141f34c234f6)、[SBC_CH_MODE_MONO](#a0513bb34588f5c6d428b141f34c234f6a1001ed03373ad85bfe498c51e763e608)、[SBC_CH_MODE_DUAL_CHANNEL](#a0513bb34588f5c6d428b141f34c234f6a4b4a5407b69d6d3ce4713791596b42dc)、[SBC_CH_MODE_STEREO](#a0513bb34588f5c6d428b141f34c234f6a30c7c23457ab3de5c293c654077d9e7e)、[SBC_CH_MODE_JOINT_STEREO](#a0513bb34588f5c6d428b141f34c234f6a234fe60a35e743c4feeda0bb26e940d3)。

SBC 通道模式（Channel Mode）。

<a id="r_a43b42f96c2d87bbcea4fb230fd8f3a5f"></a>

```c
enum sbc_alloc_mthd { SBC_ALLOC_MTHD_LOUDNESS , SBC_ALLOC_MTHD_SNR }
```

相关声明：[sbc_alloc_mthd](#a43b42f96c2d87bbcea4fb230fd8f3a5f)、[SBC_ALLOC_MTHD_LOUDNESS](#a43b42f96c2d87bbcea4fb230fd8f3a5fa0fe0046f999213dec1f7aa9186eb13c5)、[SBC_ALLOC_MTHD_SNR](#a43b42f96c2d87bbcea4fb230fd8f3a5fa8bd17f97e15ad2c95c2a2886db56c91c)。

SBC 分配方法（Allocation Method）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.3\_函数（Functions）

<a id="r_a542096b8adb98ef03f2381d3aa4c159e"></a>

```c
int sbc_setup_encoder (struct sbc_encoder *encoder, struct sbc_encoder_init_param *param)
```

相关声明：[sbc_setup_encoder](#a542096b8adb98ef03f2381d3aa4c159e)、[sbc_encoder](../audio_video_model_reference/P046_sbc_encoder_结构体.md)、[sbc_encoder_init_param](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md)。

设置编码器（Encoder）。

<a id="r_a652a6c40ae296c63d7a31104c3fea007"></a>

```c
uint32_t sbc_encode (struct sbc_encoder *encoder, const void *in_data, void *out_data)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sbc_encode](#a652a6c40ae296c63d7a31104c3fea007)、[sbc_encoder](../audio_video_model_reference/P046_sbc_encoder_结构体.md)。

编码一帧（Encode a Frame）。

<a id="r_a8b850a924dfee57a001e041164de6eb7"></a>

```c
int sbc_frame_samples (struct sbc_encoder *encoder)
```

相关声明：[sbc_frame_samples](#a8b850a924dfee57a001e041164de6eb7)、[sbc_encoder](../audio_video_model_reference/P046_sbc_encoder_结构体.md)。

返回一帧中的 PCM 采样数（Number of PCM Samples）。

<a id="r_a46d8d7671567d93a9cd28faedb14c050"></a>

```c
int sbc_frame_bytes (struct sbc_encoder *encoder)
```

相关声明：[sbc_frame_bytes](#a46d8d7671567d93a9cd28faedb14c050)、[sbc_encoder](../audio_video_model_reference/P046_sbc_encoder_结构体.md)。

返回一帧中的 PCM 字节数。

<a id="r_a99bfc2a65061e3bbd02095593478761e"></a>

```c
int sbc_frame_encoded_bytes (struct sbc_encoder *encoder)
```

相关声明：[sbc_frame_encoded_bytes](#a99bfc2a65061e3bbd02095593478761e)、[sbc_encoder](../audio_video_model_reference/P046_sbc_encoder_结构体.md)。

返回一帧的编码大小（Encoded Size）。

<a id="r_aaf6292a3340023ea26566f9c9d5862e9"></a>

```c
int sbc_setup_decoder (struct sbc_decoder *decoder)
```

相关声明：[sbc_setup_decoder](#aaf6292a3340023ea26566f9c9d5862e9)、[sbc_decoder](../audio_video_model_reference/P045_sbc_decoder_结构体.md)。

设置 SBC 解码器（Decoder）。

<a id="r_acb546af83d4e748959a40a552c8d498e"></a>

```c
int sbc_decode (struct sbc_decoder *decoder, const void **in_data, uint32_t *in_size, void *out_data, uint32_t *out_size)
```

相关声明：[sbc_decode](#acb546af83d4e748959a40a552c8d498e)、[sbc_decoder](../audio_video_model_reference/P045_sbc_decoder_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

解码一帧（Decode a Frame）。

## 25.4\_详细说明（Detailed Documentation）

<a id="a43b42f96c2d87bbcea4fb230fd8f3a5f"></a>

### `sbc_alloc_mthd`

```c
enum sbc_alloc_mthd
```

SBC 分配方法（Allocation Method）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SBC_ALLOC_MTHD_LOUDNESS` | 响度分配方法（Loudness Allocation Method）。 |
| `SBC_ALLOC_MTHD_SNR` | 信噪比分配方法（SNR Allocation Method）。 |

<a id="a0513bb34588f5c6d428b141f34c234f6"></a>

### `sbc_ch_mode`

```c
enum sbc_ch_mode
```

SBC 通道模式（Channel Mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SBC_CH_MODE_MONO` | 单声道（Mono Channel）。 |
| `SBC_CH_MODE_DUAL_CHANNEL` | 双通道（Dual Channel）。 |
| `SBC_CH_MODE_STEREO` | 立体声通道（Stereo Channel）。 |
| `SBC_CH_MODE_JOINT_STEREO` | 联合立体声通道（Joint Stereo Channel）。 |

<a id="acb546af83d4e748959a40a552c8d498e"></a>

### `sbc_decode()`

```c
int sbc_decode ( struct sbc_decoder * decoder, const void ** in_data, uint32_t * in_size, void * out_data, uint32_t * out_size )
```

解码一帧（Decode a Frame）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `decoder` | 解码器句柄（Decoder Handle）。 |
| `in_data` | 输入比特流（Input Bitstream），解码一帧后此指针向前递增。 |
| `in_size` | 输入数据大小，以字节为单位；解码一帧后减小。 |
| `out_data` | 输出 PCM 采样（Output PCM Samples） |
| `out_size` | 输出数据大小，以字节为单位 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="a652a6c40ae296c63d7a31104c3fea007"></a>

### `sbc_encode()`

```c
uint32_t sbc_encode ( struct sbc_encoder * encoder, const void * in_data, void * out_data )
```

编码一帧（Encode a Frame）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `encoder` | 编码器句柄（Encoder Handle）。 |
| `in_data` | 输入 PCM 采样（Input PCM Samples）。 |
| `out_data` | 编码后的 SBC 帧（Encoded SBC Frame）。 |

**返回（Returns）**：返回值（Returns）：此帧的编码大小，以字节为单位。

<a id="a46d8d7671567d93a9cd28faedb14c050"></a>

### `sbc_frame_bytes()`

```c
int sbc_frame_bytes ( struct sbc_encoder * encoder)
```

返回一帧中的 PCM 字节数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `encoder` | 编码器句柄（Encoder Handle）。 |

**返回（Returns）**：返回值（Returns）：PCM 字节数，出错时返回负错误码。

<a id="a99bfc2a65061e3bbd02095593478761e"></a>

### `sbc_frame_encoded_bytes()`

```c
int sbc_frame_encoded_bytes ( struct sbc_encoder * encoder)
```

返回一帧的编码大小（Encoded Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `encoder` | 编码器句柄（Encoder Handle）。 |

**返回（Returns）**：返回值（Returns）：一帧的编码字节数，出错时返回负错误码。

<a id="a8b850a924dfee57a001e041164de6eb7"></a>

### `sbc_frame_samples()`

```c
int sbc_frame_samples ( struct sbc_encoder * encoder)
```

返回一帧中的 PCM 采样数（Number of PCM Samples）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `encoder` | 编码器句柄（Encoder Handle）。 |

**返回（Returns）**：返回值（Returns）：PCM 采样数，出错时返回负错误码。

<a id="aaf6292a3340023ea26566f9c9d5862e9"></a>

### `sbc_setup_decoder()`

```c
int sbc_setup_decoder ( struct sbc_decoder * decoder)
```

设置 SBC 解码器（Decoder）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `decoder` | 解码器句柄（Decoder Handle）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="a542096b8adb98ef03f2381d3aa4c159e"></a>

### `sbc_setup_encoder()`

```c
int sbc_setup_encoder ( struct sbc_encoder * encoder, struct sbc_encoder_init_param * param )
```

设置编码器（Encoder）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `encoder` | 编码器句柄（Encoder Handle）。 |
| `param` | 初始化编码器的参数 sbc_encoder_init_param。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。


## 25.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [string.h](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P747_sbc.h_源码浏览.md)
- [sbc_encoder](../audio_video_model_reference/P046_sbc_encoder_结构体.md)
- [sbc_encoder_init_param](../audio_video_model_reference/P047_sbc_encoder_init_param_结构体.md)
- [sbc_decoder](../audio_video_model_reference/P045_sbc_decoder_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a43b42f96c2d87bbcea4fb230fd8f3a5fa0fe0046f999213dec1f7aa9186eb13c5"></a>
<a id="a43b42f96c2d87bbcea4fb230fd8f3a5fa8bd17f97e15ad2c95c2a2886db56c91c"></a>
<a id="a0513bb34588f5c6d428b141f34c234f6a1001ed03373ad85bfe498c51e763e608"></a>
<a id="a0513bb34588f5c6d428b141f34c234f6a4b4a5407b69d6d3ce4713791596b42dc"></a>
<a id="a0513bb34588f5c6d428b141f34c234f6a30c7c23457ab3de5c293c654077d9e7e"></a>
<a id="a0513bb34588f5c6d428b141f34c234f6a234fe60a35e743c4feeda0bb26e940d3"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P024_zephyr__bluetooth__classic__rfcomm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__sd__sdmmc.h_文件参考.md)
