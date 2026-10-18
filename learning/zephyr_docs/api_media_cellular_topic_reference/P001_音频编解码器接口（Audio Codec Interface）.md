---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-1
title: 音频编解码器接口（Audio Codec Interface）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_音频编解码器接口（Audio Codec Interface）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音频编解码器的抽象（Abstraction）。

<a id="details"></a>

音频编解码器抽象（Abstraction for Audio Codecs）。自 1.13 引入，版本 0.3.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_audio_5Fcodec_5Finterface_5Fbackend"></a>

相关声明：[音频编解码器驱动后端 API（Audio Codec Driver Backend API）](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md)。

<a id="r_audio_5Fcodec_5Finterface_5Fext"></a>

相关声明：[设备专用音频编解码器 API 扩展（Device-specific audio codec API extensions）。](../api_topic_reference/P003_设备专用音频编解码器 API 扩展（Device-specific audio codec API extensions）。.md)。

<a id="header-files"></a>
<a id="files"></a>

## 1.2\_文件（Files）

<a id="r_codec_2Eh"></a>

```c
file codec.h
```

相关声明：[codec.h](../api_file_audio_gateway_reference/P002_zephyr__audio__codec.h_文件参考.md)。

音频编解码器（Audio Codec）的公共API头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.3\_数据结构（Data Structures）

<a id="r_pcm_5Fconfig"></a>

```c
struct pcm_config
```

相关声明：[pcm_config](../audio_video_model_reference/P041_pcm_config_结构体.md)。

脉冲编码调制（PCM）的配置选项。

<a id="r_audio_5Fdai_5Fcfg_5Ft"></a>

```c
union audio_dai_cfg_t
```

相关声明：[audio_dai_cfg_t](../audio_video_model_reference/P066_audio_dai_cfg_t_联合体.md)。

数字音频接口（Digital Audio Interface，DAI）配置。

<a id="r_audio_5Fcodec_5Fcfg"></a>

```c
struct audio_codec_cfg
```

相关声明：[audio_codec_cfg](../driver_model_reference/P016_音频编解码器配置.md)。

音频编解码器（Codec）配置参数。

<a id="r_audio_5Fcodec_5Feq_5Fcfg"></a>

```c
struct audio_codec_eq_cfg
```

相关声明：[audio_codec_eq_cfg](../driver_model_reference/P018_音频编解码器均衡配置.md)。

编解码器均衡器（Equalizer，EQ）属性值。

<a id="r_audio_5Fproperty_5Fvalue_5Ft"></a>

```c
union audio_property_value_t
```

相关声明：[audio_property_value_t](../audio_video_model_reference/P067_audio_property_value_t_联合体.md)。

编解码器属性值（Codec Property Values）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.4\_宏定义（Macros）

<a id="r_ga52ea7c9b5c0358f68223709291c60328"></a>

```c
#define AUDIO_DAI_DIR_TX BIT(0)
```

相关声明：[AUDIO_DAI_DIR_TX](#ga52ea7c9b5c0358f68223709291c60328)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

发送数据（Transmit Data）。

<a id="r_gabd90b781156540cb1b6922a57a3ff265"></a>

```c
#define AUDIO_DAI_DIR_RX BIT(1)
```

相关声明：[AUDIO_DAI_DIR_RX](#gabd90b781156540cb1b6922a57a3ff265)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

接收数据（Receive Data）。

<a id="r_ga810df470210d28a0eb0d7a12e8fde72f"></a>

```c
#define AUDIO_DAI_DIR_TXRX (AUDIO_DAI_DIR_TX | AUDIO_DAI_DIR_RX)
```

相关声明：[AUDIO_DAI_DIR_TXRX](#ga810df470210d28a0eb0d7a12e8fde72f)、[AUDIO_DAI_DIR_TX](#ga52ea7c9b5c0358f68223709291c60328)、[AUDIO_DAI_DIR_RX](#gabd90b781156540cb1b6922a57a3ff265)。

同时接收和发送数据（Receive and Transmit）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.5\_类型定义（Typedefs）

<a id="r_gad3a2ec4622f9a7b0eb1b4d0a463e20d5"></a>

```c
typedef uint8_t audio_dai_dir_t
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[audio_dai_dir_t](#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)。

数字音频接口方向位图（DAI Direction Bitmap）。

<a id="r_ga13ecf277fdf4cfaaa424402587a1a7ad"></a>

```c
typedef void(* audio_codec_error_callback_t) (const struct device *dev, uint32_t errors)
```

相关声明：[audio_codec_error_callback_t](#ga13ecf277fdf4cfaaa424402587a1a7ad)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

错误中断（Error Interrupt）的回调。

<a id="r_ga5365e64b28a7fd33d359eb020cd7f366"></a>

```c
typedef void(* audio_codec_tx_done_callback_t) (const struct device *dev, void *user_data)
```

相关声明：[audio_codec_tx_done_callback_t](#ga5365e64b28a7fd33d359eb020cd7f366)、[device](../device_reference/P002_设备对象结构.md)。

一帧，即一个内存块大小的数据发送完成时的回调（Callback）。

<a id="r_ga56e51f3a24b7fef4ce4fcb212b5807d9"></a>

```c
typedef void(* audio_codec_rx_done_callback_t) (const struct device *dev, uint8_t *buf, uint32_t len, void *user_data)
```

相关声明：[audio_codec_rx_done_callback_t](#ga56e51f3a24b7fef4ce4fcb212b5807d9)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

一帧大小的数据到达时的回调（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.6\_枚举（Enumerations）

<a id="r_ga8fd2079e6128c8a6da59c2dee58101ca"></a>

```c
enum audio_pcm_rate_t { AUDIO_PCM_RATE_8K = 8000 , AUDIO_PCM_RATE_11P025K = 11025 , AUDIO_PCM_RATE_16K = 16000 , AUDIO_PCM_RATE_22P05K = 22050 , AUDIO_PCM_RATE_24K = 24000 , AUDIO_PCM_RATE_32K = 32000 , AUDIO_PCM_RATE_44P1K = 44100 , AUDIO_PCM_RATE_48K = 48000 , AUDIO_PCM_RATE_96K = 96000 , AUDIO_PCM_RATE_192K = 192000 }
```

相关声明：[audio_pcm_rate_t](#ga8fd2079e6128c8a6da59c2dee58101ca)、[AUDIO_PCM_RATE_8K](#gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8)、[AUDIO_PCM_RATE_11P025K](#gga8fd2079e6128c8a6da59c2dee58101caa534b2e8dfa910c18b0617c236fa18c4d)、[AUDIO_PCM_RATE_16K](#gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3)、[AUDIO_PCM_RATE_22P05K](#gga8fd2079e6128c8a6da59c2dee58101caa77fab8d698408449f11d0974bfebaa0b)、[AUDIO_PCM_RATE_24K](#gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945)、[AUDIO_PCM_RATE_32K](#gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90)、[AUDIO_PCM_RATE_44P1K](#gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad)、[AUDIO_PCM_RATE_48K](#gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913)、[AUDIO_PCM_RATE_96K](#gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811)、[AUDIO_PCM_RATE_192K](#gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9)。

脉冲编码调制音频采样率（PCM Audio Sample Rates）。

<a id="r_ga1898dae0fac2e2bf34596453037bff7e"></a>

```c
enum audio_pcm_width_t { AUDIO_PCM_WIDTH_16_BITS = 16 , AUDIO_PCM_WIDTH_20_BITS = 20 , AUDIO_PCM_WIDTH_24_BITS = 24 , AUDIO_PCM_WIDTH_32_BITS = 32 }
```

相关声明：[audio_pcm_width_t](#ga1898dae0fac2e2bf34596453037bff7e)、[AUDIO_PCM_WIDTH_16_BITS](#gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e)、[AUDIO_PCM_WIDTH_20_BITS](#gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638)、[AUDIO_PCM_WIDTH_24_BITS](#gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa)、[AUDIO_PCM_WIDTH_32_BITS](#gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f)。

脉冲编码调制音频采样位宽（PCM Audio Sample Bit Widths）。

<a id="r_ga147094be4c7c5d62df695673d293f12d"></a>

```c
enum audio_dai_type_t { AUDIO_DAI_TYPE_I2S , AUDIO_DAI_TYPE_LEFT_JUSTIFIED , AUDIO_DAI_TYPE_RIGHT_JUSTIFIED , AUDIO_DAI_TYPE_PCMA , AUDIO_DAI_TYPE_PCMB , AUDIO_DAI_TYPE_PCM , AUDIO_DAI_TYPE_INVALID }
```

相关声明：[audio_dai_type_t](#ga147094be4c7c5d62df695673d293f12d)、[AUDIO_DAI_TYPE_I2S](#gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac)、[AUDIO_DAI_TYPE_LEFT_JUSTIFIED](#gga147094be4c7c5d62df695673d293f12da3cac1ab007667ecc477f493cb74ca504)、[AUDIO_DAI_TYPE_RIGHT_JUSTIFIED](#gga147094be4c7c5d62df695673d293f12da94fdc805aec7c34da2de990d1b1bef6e)、[AUDIO_DAI_TYPE_PCMA](#gga147094be4c7c5d62df695673d293f12da0376329aa4700f6b6aed798a13cb1efe)、[AUDIO_DAI_TYPE_PCMB](#gga147094be4c7c5d62df695673d293f12daa578a69e94a460428e0d09f29cbf9ade)、[AUDIO_DAI_TYPE_PCM](#gga147094be4c7c5d62df695673d293f12dad32b311e083c62d10b20a4028295d192)、[AUDIO_DAI_TYPE_INVALID](#gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c)。

数字音频接口类型（Digital Audio Interface，DAI）。

<a id="r_ga5411b79fa217b0f9c63dc6890323804c"></a>

```c
enum audio_property_t { AUDIO_PROPERTY_OUTPUT_VOLUME , AUDIO_PROPERTY_OUTPUT_MUTE , AUDIO_PROPERTY_INPUT_VOLUME , AUDIO_PROPERTY_INPUT_MUTE , AUDIO_PROPERTY_EQ_GAIN }
```

相关声明：[audio_property_t](#ga5411b79fa217b0f9c63dc6890323804c)、[AUDIO_PROPERTY_OUTPUT_VOLUME](#gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8)、[AUDIO_PROPERTY_OUTPUT_MUTE](#gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb)、[AUDIO_PROPERTY_INPUT_VOLUME](#gga5411b79fa217b0f9c63dc6890323804ca0608dca9fec8160429d17d1d7dac0026)、[AUDIO_PROPERTY_INPUT_MUTE](#gga5411b79fa217b0f9c63dc6890323804ca9b4548cfe663072a98db20ea0da377c1)、[AUDIO_PROPERTY_EQ_GAIN](#gga5411b79fa217b0f9c63dc6890323804ca22cc7ebf7a5c7732fd507835c32aa642)。

可由 audio_codec_set_property() 设置的编解码器属性（Codec Properties）。

<a id="r_ga966cf980ce24855830e24b5de4d884d6"></a>

```c
enum audio_channel_t { AUDIO_CHANNEL_FRONT_LEFT , AUDIO_CHANNEL_FRONT_RIGHT , AUDIO_CHANNEL_LFE , AUDIO_CHANNEL_FRONT_CENTER , AUDIO_CHANNEL_REAR_LEFT , AUDIO_CHANNEL_REAR_RIGHT , AUDIO_CHANNEL_REAR_CENTER , AUDIO_CHANNEL_SIDE_LEFT , AUDIO_CHANNEL_SIDE_RIGHT , AUDIO_CHANNEL_HEADPHONE_LEFT , AUDIO_CHANNEL_HEADPHONE_RIGHT , AUDIO_CHANNEL_ALL , AUDIO_CHANNEL_COMMON_COUNT , AUDIO_CHANNEL_PRIV_START = AUDIO_CHANNEL_COMMON_COUNT , AUDIO_CHANNEL_MAX = INT16_MAX }
```

相关声明：[audio_channel_t](#ga966cf980ce24855830e24b5de4d884d6)、[AUDIO_CHANNEL_FRONT_LEFT](#gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18)、[AUDIO_CHANNEL_FRONT_RIGHT](#gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75)、[AUDIO_CHANNEL_LFE](#gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6)、[AUDIO_CHANNEL_FRONT_CENTER](#gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8)、[AUDIO_CHANNEL_REAR_LEFT](#gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc)、[AUDIO_CHANNEL_REAR_RIGHT](#gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9)、[AUDIO_CHANNEL_REAR_CENTER](#gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04)、[AUDIO_CHANNEL_SIDE_LEFT](#gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba)、[AUDIO_CHANNEL_SIDE_RIGHT](#gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec)、[AUDIO_CHANNEL_HEADPHONE_LEFT](#gga966cf980ce24855830e24b5de4d884d6affc38ea2d76af83e6b06a1471dd68cfa)、[AUDIO_CHANNEL_HEADPHONE_RIGHT](#gga966cf980ce24855830e24b5de4d884d6a7b8d80478453df358cbdb7064f7a656d)、[AUDIO_CHANNEL_ALL](#gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878)、[AUDIO_CHANNEL_COMMON_COUNT](#gga966cf980ce24855830e24b5de4d884d6a1a35205e5a757748b3cf2f2048956cfe)、[AUDIO_CHANNEL_PRIV_START](#gga966cf980ce24855830e24b5de4d884d6a3ad5430c80ae5a55ecbaf9246bd3ae93)、[AUDIO_CHANNEL_MAX](#gga966cf980ce24855830e24b5de4d884d6a5370ff516a32a36a9f643d5906461817)。

在 audio_codec_set_property() 中使用的音频通道标识符（Audio Channel Identifiers）。

<a id="r_ga3b21ded95eb16d2c5f9f8da3c580a411"></a>

```c
enum audio_route_t { AUDIO_ROUTE_BYPASS , AUDIO_ROUTE_PLAYBACK , AUDIO_ROUTE_PLAYBACK_CAPTURE , AUDIO_ROUTE_CAPTURE }
```

相关声明：[audio_route_t](#ga3b21ded95eb16d2c5f9f8da3c580a411)、[AUDIO_ROUTE_BYPASS](#gga3b21ded95eb16d2c5f9f8da3c580a411a68af44d32f8c5e46a962fe0fc0fe0323)、[AUDIO_ROUTE_PLAYBACK](#gga3b21ded95eb16d2c5f9f8da3c580a411a726898c5bfe3cbb217e3bca2fd1cdf7e)、[AUDIO_ROUTE_PLAYBACK_CAPTURE](#gga3b21ded95eb16d2c5f9f8da3c580a411aa105c5914186aa9fbbd81af4e754ff0d)、[AUDIO_ROUTE_CAPTURE](#gga3b21ded95eb16d2c5f9f8da3c580a411a31ebeb6337049a1ccea29ede230ad28a)。

数字音频接口路由类型（DAI Route Types）。

<a id="r_ga2923c9aca9b8656ba3e3741d5860279a"></a>

```c
enum audio_codec_error_type { AUDIO_CODEC_ERROR_OVERCURRENT = (1UL << (0)) , AUDIO_CODEC_ERROR_OVERTEMPERATURE = (1UL << (1)) , AUDIO_CODEC_ERROR_UNDERVOLTAGE = (1UL << (2)) , AUDIO_CODEC_ERROR_OVERVOLTAGE = (1UL << (3)) , AUDIO_CODEC_ERROR_DC = (1UL << (4)) }
```

相关声明：[audio_codec_error_type](#ga2923c9aca9b8656ba3e3741d5860279a)、[AUDIO_CODEC_ERROR_OVERCURRENT](#gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1)、[AUDIO_CODEC_ERROR_OVERTEMPERATURE](#gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f)、[AUDIO_CODEC_ERROR_UNDERVOLTAGE](#gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba)、[AUDIO_CODEC_ERROR_OVERVOLTAGE](#gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6)、[AUDIO_CODEC_ERROR_DC](#gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35)。

编解码器错误类型（Codec Error Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.7\_函数（Functions）

<a id="r_ga0c3344ea62fe994203315a0a7c20616c"></a>

```c
static int audio_codec_configure (const struct device *dev, struct audio_codec_cfg *cfg)
```

相关声明：[audio_codec_configure](#ga0c3344ea62fe994203315a0a7c20616c)、[device](../device_reference/P002_设备对象结构.md)、[audio_codec_cfg](../driver_model_reference/P016_音频编解码器配置.md)。

配置音频编解码器（Audio Codec）。

<a id="r_ga186e9c63c792072280558b953ced1cf7"></a>

```c
static void audio_codec_start_output (const struct device *dev)
```

相关声明：[audio_codec_start_output](#ga186e9c63c792072280558b953ced1cf7)、[device](../device_reference/P002_设备对象结构.md)。

设置编解码器，启动输出音频播放（Audio Playback）。

<a id="r_ga6faba1d52c8d93e5ab5ec9954bf52f4a"></a>

```c
static void audio_codec_stop_output (const struct device *dev)
```

相关声明：[audio_codec_stop_output](#ga6faba1d52c8d93e5ab5ec9954bf52f4a)、[device](../device_reference/P002_设备对象结构.md)。

设置编解码器，停止输出音频播放（Audio Playback）。

<a id="r_ga6d28af0279eb8e4b693ea35f5235f189"></a>

```c
static int audio_codec_set_property (const struct device *dev, audio_property_t property, audio_channel_t channel, audio_property_value_t val)
```

相关声明：[audio_codec_set_property](#ga6d28af0279eb8e4b693ea35f5235f189)、[device](../device_reference/P002_设备对象结构.md)、[audio_property_t](#ga5411b79fa217b0f9c63dc6890323804c)、[audio_channel_t](#ga966cf980ce24855830e24b5de4d884d6)、[audio_property_value_t](../audio_video_model_reference/P067_audio_property_value_t_联合体.md)。

设置由 audio_property_t 定义的编解码器属性（Codec Property）。

<a id="r_gadd16956b1160388a17c23d6cc84218b3"></a>

```c
static int audio_codec_apply_properties (const struct device *dev)
```

相关声明：[audio_codec_apply_properties](#gadd16956b1160388a17c23d6cc84218b3)、[device](../device_reference/P002_设备对象结构.md)。

原子地（Atomically）应用所有已缓存属性。

<a id="r_ga550f86c43f7d96a1d826330d9da2d1af"></a>

```c
static int audio_codec_clear_errors (const struct device *dev)
```

相关声明：[audio_codec_clear_errors](#ga550f86c43f7d96a1d826330d9da2d1af)、[device](../device_reference/P002_设备对象结构.md)。

清除所有编解码器错误（Codec Errors）。

<a id="r_ga90f86f013dd46bad33bc95b2a7c8e1c9"></a>

```c
static int audio_codec_register_error_callback (const struct device *dev, audio_codec_error_callback_t cb)
```

相关声明：[audio_codec_register_error_callback](#ga90f86f013dd46bad33bc95b2a7c8e1c9)、[device](../device_reference/P002_设备对象结构.md)、[audio_codec_error_callback_t](#ga13ecf277fdf4cfaaa424402587a1a7ad)。

注册编解码器错误的回调函数（Callback Function）。

<a id="r_ga92dc9ce48ff0785dbf002f52afcef254"></a>

```c
static int audio_codec_route_input (const struct device *dev, audio_channel_t channel, uint32_t input)
```

相关声明：[audio_codec_route_input](#ga92dc9ce48ff0785dbf002f52afcef254)、[device](../device_reference/P002_设备对象结构.md)、[audio_channel_t](#ga966cf980ce24855830e24b5de4d884d6)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为指定输入通道设置信号路由（Signal Routing）。

<a id="r_gadaa36aabb932903c725007c2005a7304"></a>

```c
static int audio_codec_route_output (const struct device *dev, audio_channel_t channel, uint32_t output)
```

相关声明：[audio_codec_route_output](#gadaa36aabb932903c725007c2005a7304)、[device](../device_reference/P002_设备对象结构.md)、[audio_channel_t](#ga966cf980ce24855830e24b5de4d884d6)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为指定输出通道设置信号路由（Signal Routing）。

<a id="r_ga445f95326d5bcf51c355dfc128f1e862"></a>

```c
static int audio_codec_start (const struct device *dev, audio_dai_dir_t dir)
```

相关声明：[audio_codec_start](#ga445f95326d5bcf51c355dfc128f1e862)、[device](../device_reference/P002_设备对象结构.md)、[audio_dai_dir_t](#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)。

设置编解码器，启动音频播放或采集（Playback or Capture）。

<a id="r_ga3fa574a02bc12c578ea306202a222d32"></a>

```c
static int audio_codec_stop (const struct device *dev, audio_dai_dir_t dir)
```

相关声明：[audio_codec_stop](#ga3fa574a02bc12c578ea306202a222d32)、[device](../device_reference/P002_设备对象结构.md)、[audio_dai_dir_t](#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)。

设置编解码器，停止音频播放或采集（Playback or Capture）。

<a id="r_gab6b430783bba55d30a2b99b4bf25a040"></a>

```c
static int audio_codec_write (const struct device *dev, uint8_t *data, size_t data_size)
```

相关声明：[audio_codec_write](#gab6b430783bba55d30a2b99b4bf25a040)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入一个块大小的数据以供音频播放（Audio Playback）。

<a id="r_ga5e64f3537a4b0345f82e3e73992ee46a"></a>

```c
static int audio_codec_register_done_callback (const struct device *dev, audio_codec_tx_done_callback_t tx_cb, void *tx_cb_user_data, audio_codec_rx_done_callback_t rx_cb, void *rx_cb_user_data)
```

相关声明：[audio_codec_register_done_callback](#ga5e64f3537a4b0345f82e3e73992ee46a)、[device](../device_reference/P002_设备对象结构.md)、[audio_codec_tx_done_callback_t](#ga5365e64b28a7fd33d359eb020cd7f366)、[audio_codec_rx_done_callback_t](#ga56e51f3a24b7fef4ce4fcb212b5807d9)。

注册编解码器一帧数据发送／接收完成的回调函数（TX/RX Done Callback）。

## 1.8\_详细说明（Detailed Documentation）

<a id="gabd90b781156540cb1b6922a57a3ff265"></a>

### `AUDIO_DAI_DIR_RX`

```c
#define AUDIO_DAI_DIR_RX BIT(1)
```

```c
#include <zephyr/audio/codec.h>
```

接收数据（Receive Data）。

<a id="ga52ea7c9b5c0358f68223709291c60328"></a>

### `AUDIO_DAI_DIR_TX`

```c
#define AUDIO_DAI_DIR_TX BIT(0)
```

```c
#include <zephyr/audio/codec.h>
```

发送数据（Transmit Data）。

<a id="ga810df470210d28a0eb0d7a12e8fde72f"></a>

### `AUDIO_DAI_DIR_TXRX`

```c
#define AUDIO_DAI_DIR_TXRX (AUDIO_DAI_DIR_TX | AUDIO_DAI_DIR_RX)
```

```c
#include <zephyr/audio/codec.h>
```

同时接收和发送数据（Receive and Transmit）。

<a id="ga13ecf277fdf4cfaaa424402587a1a7ad"></a>

### `audio_codec_error_callback_t`

```c
typedef void(* audio_codec_error_callback_t) (const struct device *dev, uint32_t errors)
```

```c
#include <zephyr/audio/codec.h>
```

错误中断（Error Interrupt）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向编解码器设备（Codec Device）的指针。 |
| `errors` | 设备错误（Device Errors），以 audio_codec_error_type 值组成的位掩码表示。 |

<a id="ga56e51f3a24b7fef4ce4fcb212b5807d9"></a>

### `audio_codec_rx_done_callback_t`

```c
typedef void(* audio_codec_rx_done_callback_t) (const struct device *dev, uint8_t *buf, uint32_t len, void *user_data)
```

```c
#include <zephyr/audio/codec.h>
```

一帧大小的数据到达时的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向编解码器设备（Codec Device）的指针。 |
| `buf` | 指向已接收数据（Received Data）的指针。 |
| `len` | 已接收数据的大小，单位为字节。 |
| `user_data` | 指向用户数据的指针。 |

<a id="ga5365e64b28a7fd33d359eb020cd7f366"></a>

### `audio_codec_tx_done_callback_t`

```c
typedef void(* audio_codec_tx_done_callback_t) (const struct device *dev, void *user_data)
```

```c
#include <zephyr/audio/codec.h>
```

一帧，即一个内存块大小的数据发送完成时的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向编解码器设备（Codec Device）的指针。 |
| `user_data` | 指向用户数据的指针。 |

<a id="gad3a2ec4622f9a7b0eb1b4d0a463e20d5"></a>

### `audio_dai_dir_t`

```c
typedef uint8_t audio_dai_dir_t
```

```c
#include <zephyr/audio/codec.h>
```

数字音频接口方向位图（DAI Direction Bitmap）。

<a id="ga966cf980ce24855830e24b5de4d884d6"></a>

### `audio_channel_t`

```c
enum audio_channel_t
```

```c
#include <zephyr/audio/codec.h>
```

在 audio_codec_set_property() 中使用的音频通道标识符（Audio Channel Identifiers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `AUDIO_CHANNEL_FRONT_LEFT` | 左前声道（Front Left Channel）。 |
| `AUDIO_CHANNEL_FRONT_RIGHT` | 右前声道（Front Right Channel）。 |
| `AUDIO_CHANNEL_LFE` | 低频效果声道（Low Frequency Effect Channel）。 |
| `AUDIO_CHANNEL_FRONT_CENTER` | 前中置声道（Front Center Channel）。 |
| `AUDIO_CHANNEL_REAR_LEFT` | 左后声道（Rear Left Channel）。 |
| `AUDIO_CHANNEL_REAR_RIGHT` | 右后声道（Rear Right Channel）。 |
| `AUDIO_CHANNEL_REAR_CENTER` | 后中置声道（Rear Center Channel）。 |
| `AUDIO_CHANNEL_SIDE_LEFT` | 左侧声道（Side Left Channel）。 |
| `AUDIO_CHANNEL_SIDE_RIGHT` | 右侧声道（Side Right Channel）。 |
| `AUDIO_CHANNEL_HEADPHONE_LEFT` | 耳机左声道（Headphone Left）。 |
| `AUDIO_CHANNEL_HEADPHONE_RIGHT` | 耳机右声道（Headphone Right）。 |
| `AUDIO_CHANNEL_ALL` | 全部声道（All Channels）。 |
| `AUDIO_CHANNEL_COMMON_COUNT` | 全部通用声道标识符（Common Channel Identifiers）的数量。 |
| `AUDIO_CHANNEL_PRIV_START` | 此值及更大值由编解码器自行定义（Codec Specific），参见编解码器的头文件。 |
| `AUDIO_CHANNEL_MAX` | 音频编解码器声道标识符（Audio Codec Channel Identifier）的最大值。 |

<a id="ga2923c9aca9b8656ba3e3741d5860279a"></a>

### `audio_codec_error_type`

```c
enum audio_codec_error_type
```

```c
#include <zephyr/audio/codec.h>
```

编解码器错误类型（Codec Error Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `AUDIO_CODEC_ERROR_OVERCURRENT` | 输出过流（Output Over-current）。 |
| `AUDIO_CODEC_ERROR_OVERTEMPERATURE` | 编解码器过温（Codec Over-temperature）。 |
| `AUDIO_CODEC_ERROR_UNDERVOLTAGE` | 电源欠压（Power Low Voltage）。 |
| `AUDIO_CODEC_ERROR_OVERVOLTAGE` | 电源过压（Power High Voltage）。 |
| `AUDIO_CODEC_ERROR_DC` | 输出直流（Output Direct-current）。 |

<a id="ga147094be4c7c5d62df695673d293f12d"></a>

### `audio_dai_type_t`

```c
enum audio_dai_type_t
```

```c
#include <zephyr/audio/codec.h>
```

数字音频接口类型（Digital Audio Interface，DAI）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `AUDIO_DAI_TYPE_I2S` | I2S 接口（Interface）。 |
| `AUDIO_DAI_TYPE_LEFT_JUSTIFIED` | 左对齐 I2S 接口（Left Justified）。 |
| `AUDIO_DAI_TYPE_RIGHT_JUSTIFIED` | 右对齐 I2S 接口（Right Justified）。 |
| `AUDIO_DAI_TYPE_PCMA` | 脉冲编码调制（PCM）接口，变体 A。 |
| `AUDIO_DAI_TYPE_PCMB` | 脉冲编码调制（PCM）接口，变体 B。 |
| `AUDIO_DAI_TYPE_PCM` | 脉冲编码调制（PCM）接口。 |
| `AUDIO_DAI_TYPE_INVALID` | 可在此添加其他接口（Interfaces）。 |

<a id="ga8fd2079e6128c8a6da59c2dee58101ca"></a>

### `audio_pcm_rate_t`

```c
enum audio_pcm_rate_t
```

```c
#include <zephyr/audio/codec.h>
```

脉冲编码调制音频采样率（PCM Audio Sample Rates）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `AUDIO_PCM_RATE_8K` | 8 kHz 采样率（Sample Rate）。 |
| `AUDIO_PCM_RATE_11P025K` | 11.025 kHz 采样率（Sample Rate）。 |
| `AUDIO_PCM_RATE_16K` | 16 kHz 采样率（Sample Rate）。 |
| `AUDIO_PCM_RATE_22P05K` | 22.05 kHz 采样率（Sample Rate）。 |
| `AUDIO_PCM_RATE_24K` | 24 kHz 采样率（Sample Rate）。 |
| `AUDIO_PCM_RATE_32K` | 32 kHz 采样率（Sample Rate）。 |
| `AUDIO_PCM_RATE_44P1K` | 44.1 kHz 采样率（Sample Rate）。 |
| `AUDIO_PCM_RATE_48K` | 48 kHz 采样率（Sample Rate）。 |
| `AUDIO_PCM_RATE_96K` | 96 kHz 采样率（Sample Rate）。 |
| `AUDIO_PCM_RATE_192K` | 192 kHz 采样率（Sample Rate）。 |

<a id="ga1898dae0fac2e2bf34596453037bff7e"></a>

### `audio_pcm_width_t`

```c
enum audio_pcm_width_t
```

```c
#include <zephyr/audio/codec.h>
```

脉冲编码调制音频采样位宽（PCM Audio Sample Bit Widths）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `AUDIO_PCM_WIDTH_16_BITS` | 16 位采样宽度（Sample Width）。 |
| `AUDIO_PCM_WIDTH_20_BITS` | 20 位采样宽度（Sample Width）。 |
| `AUDIO_PCM_WIDTH_24_BITS` | 24 位采样宽度（Sample Width）。 |
| `AUDIO_PCM_WIDTH_32_BITS` | 32 位采样宽度（Sample Width）。 |

<a id="ga5411b79fa217b0f9c63dc6890323804c"></a>

### `audio_property_t`

```c
enum audio_property_t
```

```c
#include <zephyr/audio/codec.h>
```

可由 audio_codec_set_property() 设置的编解码器属性（Codec Properties）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `AUDIO_PROPERTY_OUTPUT_VOLUME` | 输出音量（Output Volume）。 |
| `AUDIO_PROPERTY_OUTPUT_MUTE` | 输出静音／取消静音（Output Mute/Unmute）。 |
| `AUDIO_PROPERTY_INPUT_VOLUME` | 输入音量（Input Volume）。 |
| `AUDIO_PROPERTY_INPUT_MUTE` | 输入静音／取消静音（Input Mute/Unmute）。 |
| `AUDIO_PROPERTY_EQ_GAIN` | 输出均衡器增益（Output Equalizer Gain）。 |

<a id="ga3b21ded95eb16d2c5f9f8da3c580a411"></a>

### `audio_route_t`

```c
enum audio_route_t
```

```c
#include <zephyr/audio/codec.h>
```

数字音频接口路由类型（DAI Route Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `AUDIO_ROUTE_BYPASS` | 旁路（Bypass），既不配置播放路径，也不配置采集路径。 |
| `AUDIO_ROUTE_PLAYBACK` | 仅播放路径（Playback Path）。 |
| `AUDIO_ROUTE_PLAYBACK_CAPTURE` | 播放路径（Playback Path）和采集路径（Capture Path）两者。 |
| `AUDIO_ROUTE_CAPTURE` | 仅采集路径（Capture Path）。 |

<a id="gadd16956b1160388a17c23d6cc84218b3"></a>

### `audio_codec_apply_properties()`

```c
int audio_codec_apply_properties ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

原子地（Atomically）应用所有已缓存属性。

调用一次或多次 audio_codec_set_property 后，驱动可能已缓存这些设置；此时可调用 audio_codec_apply_properties，以尽可能原子的方式（As Atomic as Possible）应用全部属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向编解码器驱动实例的设备结构体（Device Structure）的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga550f86c43f7d96a1d826330d9da2d1af"></a>

### `audio_codec_clear_errors()`

```c
int audio_codec_clear_errors ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

清除所有编解码器错误（Codec Errors）。

清除全部编解码器错误（Codec Errors）。如果存在错误中断，将撤销其中断有效状态。

函数未实现（Function Not Implemented；原文带有前导符号 `<`）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向编解码器驱动实例的设备结构体（Device Structure）的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga0c3344ea62fe994203315a0a7c20616c"></a>

### `audio_codec_configure()`

```c
int audio_codec_configure ( const struct device * dev, struct audio_codec_cfg * cfg )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

配置音频编解码器（Audio Codec）。

根据作为输入提供的配置参数（Configuration Parameters）配置音频编解码器设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向编解码器驱动实例的设备结构体（Device Structure）的指针。 |
| `cfg` | 指向包含编解码器配置（Codec Configuration）的结构体的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga5e64f3537a4b0345f82e3e73992ee46a"></a>

### `audio_codec_register_done_callback()`

```c
int audio_codec_register_done_callback ( const struct device * dev, audio_codec_tx_done_callback_t tx_cb, void * tx_cb_user_data, audio_codec_rx_done_callback_t rx_cb, void * rx_cb_user_data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

注册编解码器一帧数据发送／接收完成的回调函数（TX/RX Done Callback）。

回调从 DMA 中断服务例程上下文（ISR Context）调用，因此回调必须：

- 保持非常简短，避免深层调用栈或大量栈分配，因为中断服务例程栈（ISR Stack）大小有限。
- 不得睡眠或阻塞（Sleep / Block），例如不得等待信号量、互斥量或队列。
- 只调用明确说明可安全用于 IRQ／ISR 的 API（IRQ/ISR-safe APIs）。
- 避免繁重处理或大量日志输出，将这类工作延后在线程或工作队列上下文（Thread / Workqueue Context）中执行，例如提交工作项（Work Item）。

函数未实现（Function Not Implemented；原文带有前导符号 `<`）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向音频编解码器设备（Audio Codec Device）的指针。 |
| `tx_cb` | 发送一个 DMA 帧（DMA Frame）时应调用的函数。 |
| `tx_cb_user_data` | 传给 tx_cb 的用户数据（User Data）。 |
| `rx_cb` | 接收一个 DMA 帧（DMA Frame）时应调用的函数。 |
| `rx_cb_user_data` | 传给 rx_cb 的用户数据（User Data）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga90f86f013dd46bad33bc95b2a7c8e1c9"></a>

### `audio_codec_register_error_callback()`

```c
int audio_codec_register_error_callback ( const struct device * dev, audio_codec_error_callback_t cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

注册编解码器错误的回调函数（Callback Function）。

回调从线程（Thread）中调用，因此执行 I2C 或 SPI 操作是安全的。不过，该线程的栈大小有限，由驱动定义；目前由调用者负责保证回调不会导致栈溢出（Stack Overflow）。

函数未实现（Function Not Implemented；原文带有前导符号 `<`）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向音频编解码器设备（Audio Codec Device）的指针。 |
| `cb` | 检测到错误时应调用的函数。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga92dc9ce48ff0785dbf002f52afcef254"></a>

### `audio_codec_route_input()`

```c
int audio_codec_route_input ( const struct device * dev, audio_channel_t channel, uint32_t input )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

为指定输入通道设置信号路由（Signal Routing）。

某些编解码器可从一组选定的物理输入中进行输入路由，即多路复用（Multiplexing）。此函数将给定音频流声道（Audio Stream Channel）映射到给定物理输入端子（Physical Input Terminal）。

函数未实现（Function Not Implemented；原文带有前导符号 `<`）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向音频编解码器设备（Audio Codec Device）的指针。 |
| `channel` | 要映射的声道（Channel）。 |
| `input` | 输入端子索引（Input Terminal Index），由编解码器定义。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gadaa36aabb932903c725007c2005a7304"></a>

### `audio_codec_route_output()`

```c
int audio_codec_route_output ( const struct device * dev, audio_channel_t channel, uint32_t output )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

为指定输出通道设置信号路由（Signal Routing）。

某些编解码器可从一组选定的物理输出中进行输出路由，即多路复用（Multiplexing）。此函数将给定音频流声道（Audio Stream Channel）映射到给定物理输出端子（Physical Output Terminal）。

函数未实现（Function Not Implemented；原文带有前导符号 `<`）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向音频编解码器设备（Audio Codec Device）的指针。 |
| `channel` | 要映射的声道（Channel）。 |
| `output` | 输出端子索引（Output Terminal Index），由编解码器定义。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga6d28af0279eb8e4b693ea35f5235f189"></a>

### `audio_codec_set_property()`

```c
int audio_codec_set_property ( const struct device * dev, audio_property_t property, audio_channel_t channel, audio_property_value_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

设置由 audio_property_t 定义的编解码器属性（Codec Property）。

设置属性（Property），例如音量、时钟配置等。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向编解码器驱动实例的设备结构体（Device Structure）的指针。 |
| `property` | 要设置的编解码器属性（Codec Property）。 |
| `channel` | 要设置该属性的音频声道（Audio Channel）。 |
| `val` | 指向 audio_codec_property_value_t 类型属性值（Property Value）的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga445f95326d5bcf51c355dfc128f1e862"></a>

### `audio_codec_start()`

```c
int audio_codec_start ( const struct device * dev, audio_dai_dir_t dir )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

设置编解码器，启动音频播放或采集（Playback or Capture）。

设置音频编解码器设备，以开始音频播放或采集（Playback / Capture）。

函数未实现（Function Not Implemented；原文带有前导符号 `<`）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向编解码器驱动实例的设备结构体（Device Structure）的指针。 |
| `dir` | 设备的音频播放与采集选择（Playback and Capture Selection）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga186e9c63c792072280558b953ced1cf7"></a>

### `audio_codec_start_output()`

```c
void audio_codec_start_output ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

设置编解码器，启动输出音频播放（Audio Playback）。

设置音频编解码器设备，以开始音频播放（Playback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向编解码器驱动实例的设备结构体（Device Structure）的指针。 |

<a id="ga3fa574a02bc12c578ea306202a222d32"></a>

### `audio_codec_stop()`

```c
int audio_codec_stop ( const struct device * dev, audio_dai_dir_t dir )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

设置编解码器，停止音频播放或采集（Playback or Capture）。

设置音频编解码器设备，以停止音频播放或采集（Playback / Capture）。

函数未实现（Function Not Implemented；原文带有前导符号 `<`）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向编解码器驱动实例的设备结构体（Device Structure）的指针。 |
| `dir` | 设备的音频播放与采集选择（Playback and Capture Selection）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga6faba1d52c8d93e5ab5ec9954bf52f4a"></a>

### `audio_codec_stop_output()`

```c
void audio_codec_stop_output ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

设置编解码器，停止输出音频播放（Audio Playback）。

设置音频编解码器设备，以停止音频播放（Playback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向编解码器驱动实例的设备结构体（Device Structure）的指针。 |

<a id="gab6b430783bba55d30a2b99b4bf25a040"></a>

### `audio_codec_write()`

```c
int audio_codec_write ( const struct device * dev, uint8_t * data, size_t data_size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/codec.h>
```

写入一个块大小的数据以供音频播放（Audio Playback）。

将音频数据写入设备供播放使用，不等待数据发送完成。这是非阻塞 API（Non-blocking API）：驱动一旦接受或拒绝缓冲区，函数便返回，不会等到音频数据实际播放完毕。

函数未实现（Function Not Implemented；原文带有前导符号 `<`）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向编解码器驱动实例的设备结构体（Device Structure）的指针。 |
| `data` | 数据指针。 |
| `data_size` | 数据大小，单位为字节。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。


## 1.9\_原页交叉引用（Cross References）

- [音频编解码器驱动后端 API（Audio Codec Driver Backend API）](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md)
- [设备专用音频编解码器 API 扩展（Device-specific audio codec API extensions）。](../api_topic_reference/P003_设备专用音频编解码器 API 扩展（Device-specific audio codec API extensions）。.md)
- [codec.h](../api_file_audio_gateway_reference/P002_zephyr__audio__codec.h_文件参考.md)
- [pcm_config](../audio_video_model_reference/P041_pcm_config_结构体.md)
- [audio_dai_cfg_t](../audio_video_model_reference/P066_audio_dai_cfg_t_联合体.md)
- [audio_codec_cfg](../driver_model_reference/P016_音频编解码器配置.md)
- [audio_codec_eq_cfg](../driver_model_reference/P018_音频编解码器均衡配置.md)
- [audio_property_value_t](../audio_video_model_reference/P067_audio_property_value_t_联合体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6affc38ea2d76af83e6b06a1471dd68cfa"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6a7b8d80478453df358cbdb7064f7a656d"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6a1a35205e5a757748b3cf2f2048956cfe"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6a3ad5430c80ae5a55ecbaf9246bd3ae93"></a>
<a id="gga966cf980ce24855830e24b5de4d884d6a5370ff516a32a36a9f643d5906461817"></a>
<a id="gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1"></a>
<a id="gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f"></a>
<a id="gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba"></a>
<a id="gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6"></a>
<a id="gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35"></a>
<a id="gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac"></a>
<a id="gga147094be4c7c5d62df695673d293f12da3cac1ab007667ecc477f493cb74ca504"></a>
<a id="gga147094be4c7c5d62df695673d293f12da94fdc805aec7c34da2de990d1b1bef6e"></a>
<a id="gga147094be4c7c5d62df695673d293f12da0376329aa4700f6b6aed798a13cb1efe"></a>
<a id="gga147094be4c7c5d62df695673d293f12daa578a69e94a460428e0d09f29cbf9ade"></a>
<a id="gga147094be4c7c5d62df695673d293f12dad32b311e083c62d10b20a4028295d192"></a>
<a id="gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c"></a>
<a id="gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8"></a>
<a id="gga8fd2079e6128c8a6da59c2dee58101caa534b2e8dfa910c18b0617c236fa18c4d"></a>
<a id="gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3"></a>
<a id="gga8fd2079e6128c8a6da59c2dee58101caa77fab8d698408449f11d0974bfebaa0b"></a>
<a id="gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945"></a>
<a id="gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90"></a>
<a id="gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad"></a>
<a id="gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913"></a>
<a id="gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811"></a>
<a id="gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9"></a>
<a id="gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e"></a>
<a id="gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638"></a>
<a id="gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa"></a>
<a id="gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f"></a>
<a id="gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8"></a>
<a id="gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb"></a>
<a id="gga5411b79fa217b0f9c63dc6890323804ca0608dca9fec8160429d17d1d7dac0026"></a>
<a id="gga5411b79fa217b0f9c63dc6890323804ca9b4548cfe663072a98db20ea0da377c1"></a>
<a id="gga5411b79fa217b0f9c63dc6890323804ca22cc7ebf7a5c7732fd507835c32aa642"></a>
<a id="gga3b21ded95eb16d2c5f9f8da3c580a411a68af44d32f8c5e46a962fe0fc0fe0323"></a>
<a id="gga3b21ded95eb16d2c5f9f8da3c580a411a726898c5bfe3cbb217e3bca2fd1cdf7e"></a>
<a id="gga3b21ded95eb16d2c5f9f8da3c580a411aa105c5914186aa9fbbd81af4e754ff0d"></a>
<a id="gga3b21ded95eb16d2c5f9f8da3c580a411a31ebeb6337049a1ccea29ede230ad28a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_定义与分配编号（Defines and Assigned Numbers）.md)
