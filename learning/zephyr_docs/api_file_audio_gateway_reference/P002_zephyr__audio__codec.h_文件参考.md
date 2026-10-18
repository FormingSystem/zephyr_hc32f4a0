---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-2
title: zephyr__audio__codec.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/codec_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_audio\_\_codec.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/codec_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音频编解码器（Audio Codec）的公共API头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/drivers/i2s.h>
```

查看此文件的源码。

音频编解码器（Audio Codec）的公共 API 头文件。本文件包含音频编解码器 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

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

<a id="r_audio_5Fcodec_5Fdriver_5Fapi"></a>

```c
struct audio_codec_driver_api
```

相关声明：[audio_codec_driver_api](../driver_model_reference/P017_音频编解码器驱动接口.md)。

驱动操作（Driver Operations）：音频编解码器（Audio Codec）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga52ea7c9b5c0358f68223709291c60328"></a>

```c
#define AUDIO_DAI_DIR_TX BIT(0)
```

相关声明：[AUDIO_DAI_DIR_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga52ea7c9b5c0358f68223709291c60328)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

发送数据（Transmit Data）。

<a id="r_gabd90b781156540cb1b6922a57a3ff265"></a>

```c
#define AUDIO_DAI_DIR_RX BIT(1)
```

相关声明：[AUDIO_DAI_DIR_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gabd90b781156540cb1b6922a57a3ff265)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

接收数据（Receive Data）。

<a id="r_ga810df470210d28a0eb0d7a12e8fde72f"></a>

```c
#define AUDIO_DAI_DIR_TXRX (AUDIO_DAI_DIR_TX | AUDIO_DAI_DIR_RX)
```

相关声明：[AUDIO_DAI_DIR_TXRX](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga810df470210d28a0eb0d7a12e8fde72f)、[AUDIO_DAI_DIR_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga52ea7c9b5c0358f68223709291c60328)、[AUDIO_DAI_DIR_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gabd90b781156540cb1b6922a57a3ff265)。

同时接收和发送数据（Receive and Transmit）。

<a id="r_gac5af3f04f8428891d0d0d20371c57c9c"></a>

```c
#define audio_codec_api audio_codec_driver_api __DEPRECATED_MACRO
```

相关声明：[audio_codec_api](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#gac5af3f04f8428891d0d0d20371c57c9c)、[audio_codec_driver_api](../driver_model_reference/P017_音频编解码器驱动接口.md)。

audio_codec_driver_api 的旧版结构体标签别名（Legacy Struct Tag Alias），用于尚未将后端结构体更新为 audio_codec_driver_api 的音频编解码器驱动。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.3\_类型定义（Typedefs）

<a id="r_gad3a2ec4622f9a7b0eb1b4d0a463e20d5"></a>

```c
typedef uint8_t audio_dai_dir_t
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[audio_dai_dir_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)。

数字音频接口方向位图（DAI Direction Bitmap）。

<a id="r_ga13ecf277fdf4cfaaa424402587a1a7ad"></a>

```c
typedef void(* audio_codec_error_callback_t) (const struct device *dev, uint32_t errors)
```

相关声明：[audio_codec_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga13ecf277fdf4cfaaa424402587a1a7ad)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

错误中断（Error Interrupt）的回调。

<a id="r_ga5365e64b28a7fd33d359eb020cd7f366"></a>

```c
typedef void(* audio_codec_tx_done_callback_t) (const struct device *dev, void *user_data)
```

相关声明：[audio_codec_tx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5365e64b28a7fd33d359eb020cd7f366)、[device](../device_reference/P002_设备对象结构.md)。

一帧，即一个内存块大小的数据发送完成时的回调（Callback）。

<a id="r_ga56e51f3a24b7fef4ce4fcb212b5807d9"></a>

```c
typedef void(* audio_codec_rx_done_callback_t) (const struct device *dev, uint8_t *buf, uint32_t len, void *user_data)
```

相关声明：[audio_codec_rx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga56e51f3a24b7fef4ce4fcb212b5807d9)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

一帧大小的数据到达时的回调（Callback）。

<a id="r_ga751115a5ab2d9ca3f3362c76684743c0"></a>

```c
typedef int(* audio_codec_configure_t) (const struct device *dev, struct audio_codec_cfg *cfg)
```

相关声明：[audio_codec_configure_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga751115a5ab2d9ca3f3362c76684743c0)、[device](../device_reference/P002_设备对象结构.md)、[audio_codec_cfg](../driver_model_reference/P016_音频编解码器配置.md)。

配置音频编解码器设备（Audio Codec Device）的回调 API。

<a id="r_ga0bba1b85f9f55389c5e52e8589947cc3"></a>

```c
typedef void(* audio_codec_start_output_t) (const struct device *dev)
```

相关声明：[audio_codec_start_output_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga0bba1b85f9f55389c5e52e8589947cc3)、[device](../device_reference/P002_设备对象结构.md)。

启动输出音频播放（Audio Playback）的回调 API。

<a id="r_gab05f39f6aedd5ddaef911eeb0e8923cd"></a>

```c
typedef void(* audio_codec_stop_output_t) (const struct device *dev)
```

相关声明：[audio_codec_stop_output_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#gab05f39f6aedd5ddaef911eeb0e8923cd)、[device](../device_reference/P002_设备对象结构.md)。

停止输出音频播放（Audio Playback）的回调 API。

<a id="r_ga1aa7dff0874ce441560a567a1a6d2389"></a>

```c
typedef int(* audio_codec_set_property_t) (const struct device *dev, audio_property_t property, audio_channel_t channel, audio_property_value_t val)
```

相关声明：[audio_codec_set_property_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga1aa7dff0874ce441560a567a1a6d2389)、[device](../device_reference/P002_设备对象结构.md)、[audio_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5411b79fa217b0f9c63dc6890323804c)、[audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)、[audio_property_value_t](../audio_video_model_reference/P067_audio_property_value_t_联合体.md)。

设置音频编解码器属性（Property）的回调 API。

<a id="r_gabe3ce7aa1275f171856157716796ee94"></a>

```c
typedef int(* audio_codec_apply_properties_t) (const struct device *dev)
```

相关声明：[audio_codec_apply_properties_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#gabe3ce7aa1275f171856157716796ee94)、[device](../device_reference/P002_设备对象结构.md)。

应用缓存的音频编解码器属性（Cached Properties）的回调 API。

<a id="r_ga3998c4fade7829c14a8044c6efc3166c"></a>

```c
typedef int(* audio_codec_clear_errors_t) (const struct device *dev)
```

相关声明：[audio_codec_clear_errors_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga3998c4fade7829c14a8044c6efc3166c)、[device](../device_reference/P002_设备对象结构.md)。

清除音频编解码器错误（Errors）的回调 API。

<a id="r_ga6db1b3cf16e013ad5d59eef50acb4b78"></a>

```c
typedef int(* audio_codec_register_error_callback_t) (const struct device *dev, audio_codec_error_callback_t cb)
```

相关声明：[audio_codec_register_error_callback_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga6db1b3cf16e013ad5d59eef50acb4b78)、[device](../device_reference/P002_设备对象结构.md)、[audio_codec_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga13ecf277fdf4cfaaa424402587a1a7ad)。

注册音频编解码器错误回调（Error Callback）的回调 API。

<a id="r_ga00729fd4ff9c7bb25ab0a44691b15fcd"></a>

```c
typedef int(* audio_codec_route_input_t) (const struct device *dev, audio_channel_t channel, uint32_t input)
```

相关声明：[audio_codec_route_input_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga00729fd4ff9c7bb25ab0a44691b15fcd)、[device](../device_reference/P002_设备对象结构.md)、[audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

路由音频编解码器输入（Input Routing）的回调 API。

<a id="r_ga16647c5337af251140a9fa70e78b4d34"></a>

```c
typedef int(* audio_codec_route_output_t) (const struct device *dev, audio_channel_t channel, uint32_t output)
```

相关声明：[audio_codec_route_output_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga16647c5337af251140a9fa70e78b4d34)、[device](../device_reference/P002_设备对象结构.md)、[audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

路由音频编解码器输出（Output Routing）的回调 API。

<a id="r_gaf15768e53d0d5cec90f8489302c19227"></a>

```c
typedef int(* audio_codec_start_t) (const struct device *dev, audio_dai_dir_t dir)
```

相关声明：[audio_codec_start_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#gaf15768e53d0d5cec90f8489302c19227)、[device](../device_reference/P002_设备对象结构.md)、[audio_dai_dir_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)。

启动音频编解码器播放或采集（Playback or Capture）的回调 API。

<a id="r_ga4a283340b9ab266c8db97033b6e64865"></a>

```c
typedef int(* audio_codec_stop_t) (const struct device *dev, audio_dai_dir_t dir)
```

相关声明：[audio_codec_stop_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga4a283340b9ab266c8db97033b6e64865)、[device](../device_reference/P002_设备对象结构.md)、[audio_dai_dir_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)。

停止音频编解码器播放或采集（Playback or Capture）的回调 API。

<a id="r_gabe62bf451dd9cb4bfa68e6a016415668"></a>

```c
typedef int(* audio_codec_write_t) (const struct device *dev, uint8_t *data, size_t data_size)
```

相关声明：[audio_codec_write_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#gabe62bf451dd9cb4bfa68e6a016415668)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提交音频编解码器播放数据（Playback Data）的回调 API。

<a id="r_gac37a03bca2c70f7608a41910df70d4e2"></a>

```c
typedef int(* audio_codec_register_done_callback_t) (const struct device *dev, audio_codec_tx_done_callback_t tx_cb, void *tx_cb_user_data, audio_codec_rx_done_callback_t rx_cb, void *rx_cb_user_data)
```

相关声明：[audio_codec_register_done_callback_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#gac37a03bca2c70f7608a41910df70d4e2)、[device](../device_reference/P002_设备对象结构.md)、[audio_codec_tx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5365e64b28a7fd33d359eb020cd7f366)、[audio_codec_rx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga56e51f3a24b7fef4ce4fcb212b5807d9)。

注册音频编解码器 DMA 完成回调（Completion Callbacks）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.4\_枚举（Enumerations）

<a id="r_ga8fd2079e6128c8a6da59c2dee58101ca"></a>

```c
enum audio_pcm_rate_t { AUDIO_PCM_RATE_8K = 8000 , AUDIO_PCM_RATE_11P025K = 11025 , AUDIO_PCM_RATE_16K = 16000 , AUDIO_PCM_RATE_22P05K = 22050 , AUDIO_PCM_RATE_24K = 24000 , AUDIO_PCM_RATE_32K = 32000 , AUDIO_PCM_RATE_44P1K = 44100 , AUDIO_PCM_RATE_48K = 48000 , AUDIO_PCM_RATE_96K = 96000 , AUDIO_PCM_RATE_192K = 192000 }
```

相关声明：[audio_pcm_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga8fd2079e6128c8a6da59c2dee58101ca)、[AUDIO_PCM_RATE_8K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8)、[AUDIO_PCM_RATE_11P025K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caa534b2e8dfa910c18b0617c236fa18c4d)、[AUDIO_PCM_RATE_16K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3)、[AUDIO_PCM_RATE_22P05K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caa77fab8d698408449f11d0974bfebaa0b)、[AUDIO_PCM_RATE_24K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945)、[AUDIO_PCM_RATE_32K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90)、[AUDIO_PCM_RATE_44P1K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad)、[AUDIO_PCM_RATE_48K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913)、[AUDIO_PCM_RATE_96K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811)、[AUDIO_PCM_RATE_192K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9)。

脉冲编码调制音频采样率（PCM Audio Sample Rates）。

<a id="r_ga1898dae0fac2e2bf34596453037bff7e"></a>

```c
enum audio_pcm_width_t { AUDIO_PCM_WIDTH_16_BITS = 16 , AUDIO_PCM_WIDTH_20_BITS = 20 , AUDIO_PCM_WIDTH_24_BITS = 24 , AUDIO_PCM_WIDTH_32_BITS = 32 }
```

相关声明：[audio_pcm_width_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga1898dae0fac2e2bf34596453037bff7e)、[AUDIO_PCM_WIDTH_16_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e)、[AUDIO_PCM_WIDTH_20_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638)、[AUDIO_PCM_WIDTH_24_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa)、[AUDIO_PCM_WIDTH_32_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f)。

脉冲编码调制音频采样位宽（PCM Audio Sample Bit Widths）。

<a id="r_ga147094be4c7c5d62df695673d293f12d"></a>

```c
enum audio_dai_type_t { AUDIO_DAI_TYPE_I2S , AUDIO_DAI_TYPE_LEFT_JUSTIFIED , AUDIO_DAI_TYPE_RIGHT_JUSTIFIED , AUDIO_DAI_TYPE_PCMA , AUDIO_DAI_TYPE_PCMB , AUDIO_DAI_TYPE_PCM , AUDIO_DAI_TYPE_INVALID }
```

相关声明：[audio_dai_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga147094be4c7c5d62df695673d293f12d)、[AUDIO_DAI_TYPE_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac)、[AUDIO_DAI_TYPE_LEFT_JUSTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da3cac1ab007667ecc477f493cb74ca504)、[AUDIO_DAI_TYPE_RIGHT_JUSTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da94fdc805aec7c34da2de990d1b1bef6e)、[AUDIO_DAI_TYPE_PCMA](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da0376329aa4700f6b6aed798a13cb1efe)、[AUDIO_DAI_TYPE_PCMB](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12daa578a69e94a460428e0d09f29cbf9ade)、[AUDIO_DAI_TYPE_PCM](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12dad32b311e083c62d10b20a4028295d192)、[AUDIO_DAI_TYPE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c)。

数字音频接口类型（Digital Audio Interface，DAI）。

<a id="r_ga5411b79fa217b0f9c63dc6890323804c"></a>

```c
enum audio_property_t { AUDIO_PROPERTY_OUTPUT_VOLUME , AUDIO_PROPERTY_OUTPUT_MUTE , AUDIO_PROPERTY_INPUT_VOLUME , AUDIO_PROPERTY_INPUT_MUTE , AUDIO_PROPERTY_EQ_GAIN }
```

相关声明：[audio_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5411b79fa217b0f9c63dc6890323804c)、[AUDIO_PROPERTY_OUTPUT_VOLUME](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8)、[AUDIO_PROPERTY_OUTPUT_MUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb)、[AUDIO_PROPERTY_INPUT_VOLUME](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804ca0608dca9fec8160429d17d1d7dac0026)、[AUDIO_PROPERTY_INPUT_MUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804ca9b4548cfe663072a98db20ea0da377c1)、[AUDIO_PROPERTY_EQ_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804ca22cc7ebf7a5c7732fd507835c32aa642)。

可由 audio_codec_set_property() 设置的编解码器属性（Codec Properties）。

<a id="r_ga966cf980ce24855830e24b5de4d884d6"></a>

```c
enum audio_channel_t { AUDIO_CHANNEL_FRONT_LEFT , AUDIO_CHANNEL_FRONT_RIGHT , AUDIO_CHANNEL_LFE , AUDIO_CHANNEL_FRONT_CENTER , AUDIO_CHANNEL_REAR_LEFT , AUDIO_CHANNEL_REAR_RIGHT , AUDIO_CHANNEL_REAR_CENTER , AUDIO_CHANNEL_SIDE_LEFT , AUDIO_CHANNEL_SIDE_RIGHT , AUDIO_CHANNEL_HEADPHONE_LEFT , AUDIO_CHANNEL_HEADPHONE_RIGHT , AUDIO_CHANNEL_ALL , AUDIO_CHANNEL_COMMON_COUNT , AUDIO_CHANNEL_PRIV_START = AUDIO_CHANNEL_COMMON_COUNT , AUDIO_CHANNEL_MAX = INT16_MAX }
```

相关声明：[audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)、[AUDIO_CHANNEL_FRONT_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18)、[AUDIO_CHANNEL_FRONT_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75)、[AUDIO_CHANNEL_LFE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6)、[AUDIO_CHANNEL_FRONT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8)、[AUDIO_CHANNEL_REAR_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc)、[AUDIO_CHANNEL_REAR_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9)、[AUDIO_CHANNEL_REAR_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04)、[AUDIO_CHANNEL_SIDE_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba)、[AUDIO_CHANNEL_SIDE_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec)、[AUDIO_CHANNEL_HEADPHONE_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6affc38ea2d76af83e6b06a1471dd68cfa)、[AUDIO_CHANNEL_HEADPHONE_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a7b8d80478453df358cbdb7064f7a656d)、[AUDIO_CHANNEL_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878)、[AUDIO_CHANNEL_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a1a35205e5a757748b3cf2f2048956cfe)、[AUDIO_CHANNEL_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a3ad5430c80ae5a55ecbaf9246bd3ae93)、[AUDIO_CHANNEL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a5370ff516a32a36a9f643d5906461817)。

在 audio_codec_set_property() 中使用的音频通道标识符（Audio Channel Identifiers）。

<a id="r_ga3b21ded95eb16d2c5f9f8da3c580a411"></a>

```c
enum audio_route_t { AUDIO_ROUTE_BYPASS , AUDIO_ROUTE_PLAYBACK , AUDIO_ROUTE_PLAYBACK_CAPTURE , AUDIO_ROUTE_CAPTURE }
```

相关声明：[audio_route_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga3b21ded95eb16d2c5f9f8da3c580a411)、[AUDIO_ROUTE_BYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga3b21ded95eb16d2c5f9f8da3c580a411a68af44d32f8c5e46a962fe0fc0fe0323)、[AUDIO_ROUTE_PLAYBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga3b21ded95eb16d2c5f9f8da3c580a411a726898c5bfe3cbb217e3bca2fd1cdf7e)、[AUDIO_ROUTE_PLAYBACK_CAPTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga3b21ded95eb16d2c5f9f8da3c580a411aa105c5914186aa9fbbd81af4e754ff0d)、[AUDIO_ROUTE_CAPTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga3b21ded95eb16d2c5f9f8da3c580a411a31ebeb6337049a1ccea29ede230ad28a)。

数字音频接口路由类型（DAI Route Types）。

<a id="r_ga2923c9aca9b8656ba3e3741d5860279a"></a>

```c
enum audio_codec_error_type { AUDIO_CODEC_ERROR_OVERCURRENT = (1UL << (0)) , AUDIO_CODEC_ERROR_OVERTEMPERATURE = (1UL << (1)) , AUDIO_CODEC_ERROR_UNDERVOLTAGE = (1UL << (2)) , AUDIO_CODEC_ERROR_OVERVOLTAGE = (1UL << (3)) , AUDIO_CODEC_ERROR_DC = (1UL << (4)) }
```

相关声明：[audio_codec_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga2923c9aca9b8656ba3e3741d5860279a)、[AUDIO_CODEC_ERROR_OVERCURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1)、[AUDIO_CODEC_ERROR_OVERTEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f)、[AUDIO_CODEC_ERROR_UNDERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba)、[AUDIO_CODEC_ERROR_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6)、[AUDIO_CODEC_ERROR_DC](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35)。

编解码器错误类型（Codec Error Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.5\_函数（Functions）

<a id="r_ga0c3344ea62fe994203315a0a7c20616c"></a>

```c
static int audio_codec_configure (const struct device *dev, struct audio_codec_cfg *cfg)
```

相关声明：[audio_codec_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga0c3344ea62fe994203315a0a7c20616c)、[device](../device_reference/P002_设备对象结构.md)、[audio_codec_cfg](../driver_model_reference/P016_音频编解码器配置.md)。

配置音频编解码器（Audio Codec）。

<a id="r_ga186e9c63c792072280558b953ced1cf7"></a>

```c
static void audio_codec_start_output (const struct device *dev)
```

相关声明：[audio_codec_start_output](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga186e9c63c792072280558b953ced1cf7)、[device](../device_reference/P002_设备对象结构.md)。

设置编解码器，启动输出音频播放（Audio Playback）。

<a id="r_ga6faba1d52c8d93e5ab5ec9954bf52f4a"></a>

```c
static void audio_codec_stop_output (const struct device *dev)
```

相关声明：[audio_codec_stop_output](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga6faba1d52c8d93e5ab5ec9954bf52f4a)、[device](../device_reference/P002_设备对象结构.md)。

设置编解码器，停止输出音频播放（Audio Playback）。

<a id="r_ga6d28af0279eb8e4b693ea35f5235f189"></a>

```c
static int audio_codec_set_property (const struct device *dev, audio_property_t property, audio_channel_t channel, audio_property_value_t val)
```

相关声明：[audio_codec_set_property](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga6d28af0279eb8e4b693ea35f5235f189)、[device](../device_reference/P002_设备对象结构.md)、[audio_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5411b79fa217b0f9c63dc6890323804c)、[audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)、[audio_property_value_t](../audio_video_model_reference/P067_audio_property_value_t_联合体.md)。

设置由 audio_property_t 定义的编解码器属性（Codec Property）。

<a id="r_gadd16956b1160388a17c23d6cc84218b3"></a>

```c
static int audio_codec_apply_properties (const struct device *dev)
```

相关声明：[audio_codec_apply_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gadd16956b1160388a17c23d6cc84218b3)、[device](../device_reference/P002_设备对象结构.md)。

原子地（Atomically）应用所有已缓存属性。

<a id="r_ga550f86c43f7d96a1d826330d9da2d1af"></a>

```c
static int audio_codec_clear_errors (const struct device *dev)
```

相关声明：[audio_codec_clear_errors](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga550f86c43f7d96a1d826330d9da2d1af)、[device](../device_reference/P002_设备对象结构.md)。

清除所有编解码器错误（Codec Errors）。

<a id="r_ga90f86f013dd46bad33bc95b2a7c8e1c9"></a>

```c
static int audio_codec_register_error_callback (const struct device *dev, audio_codec_error_callback_t cb)
```

相关声明：[audio_codec_register_error_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga90f86f013dd46bad33bc95b2a7c8e1c9)、[device](../device_reference/P002_设备对象结构.md)、[audio_codec_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga13ecf277fdf4cfaaa424402587a1a7ad)。

注册编解码器错误的回调函数（Callback Function）。

<a id="r_ga92dc9ce48ff0785dbf002f52afcef254"></a>

```c
static int audio_codec_route_input (const struct device *dev, audio_channel_t channel, uint32_t input)
```

相关声明：[audio_codec_route_input](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga92dc9ce48ff0785dbf002f52afcef254)、[device](../device_reference/P002_设备对象结构.md)、[audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为指定输入通道设置信号路由（Signal Routing）。

<a id="r_gadaa36aabb932903c725007c2005a7304"></a>

```c
static int audio_codec_route_output (const struct device *dev, audio_channel_t channel, uint32_t output)
```

相关声明：[audio_codec_route_output](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gadaa36aabb932903c725007c2005a7304)、[device](../device_reference/P002_设备对象结构.md)、[audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为指定输出通道设置信号路由（Signal Routing）。

<a id="r_ga445f95326d5bcf51c355dfc128f1e862"></a>

```c
static int audio_codec_start (const struct device *dev, audio_dai_dir_t dir)
```

相关声明：[audio_codec_start](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga445f95326d5bcf51c355dfc128f1e862)、[device](../device_reference/P002_设备对象结构.md)、[audio_dai_dir_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)。

设置编解码器，启动音频播放或采集（Playback or Capture）。

<a id="r_ga3fa574a02bc12c578ea306202a222d32"></a>

```c
static int audio_codec_stop (const struct device *dev, audio_dai_dir_t dir)
```

相关声明：[audio_codec_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga3fa574a02bc12c578ea306202a222d32)、[device](../device_reference/P002_设备对象结构.md)、[audio_dai_dir_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)。

设置编解码器，停止音频播放或采集（Playback or Capture）。

<a id="r_gab6b430783bba55d30a2b99b4bf25a040"></a>

```c
static int audio_codec_write (const struct device *dev, uint8_t *data, size_t data_size)
```

相关声明：[audio_codec_write](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gab6b430783bba55d30a2b99b4bf25a040)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入一个块大小的数据以供音频播放（Audio Playback）。

<a id="r_ga5e64f3537a4b0345f82e3e73992ee46a"></a>

```c
static int audio_codec_register_done_callback (const struct device *dev, audio_codec_tx_done_callback_t tx_cb, void *tx_cb_user_data, audio_codec_rx_done_callback_t rx_cb, void *rx_cb_user_data)
```

相关声明：[audio_codec_register_done_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5e64f3537a4b0345f82e3e73992ee46a)、[device](../device_reference/P002_设备对象结构.md)、[audio_codec_tx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5365e64b28a7fd33d359eb020cd7f366)、[audio_codec_rx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga56e51f3a24b7fef4ce4fcb212b5807d9)。

注册编解码器一帧数据发送／接收完成的回调函数（TX/RX Done Callback）。


## 2.6\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/drivers/i2s.h](../api_source_supplement_reference/P089_i2s.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P032_codec.h_源码浏览.md)
- [pcm_config](../audio_video_model_reference/P041_pcm_config_结构体.md)
- [audio_dai_cfg_t](../audio_video_model_reference/P066_audio_dai_cfg_t_联合体.md)
- [audio_codec_cfg](../driver_model_reference/P016_音频编解码器配置.md)
- [audio_codec_eq_cfg](../driver_model_reference/P018_音频编解码器均衡配置.md)
- [audio_property_value_t](../audio_video_model_reference/P067_audio_property_value_t_联合体.md)
- [audio_codec_driver_api](../driver_model_reference/P017_音频编解码器驱动接口.md)
- [AUDIO_DAI_DIR_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga52ea7c9b5c0358f68223709291c60328)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [AUDIO_DAI_DIR_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gabd90b781156540cb1b6922a57a3ff265)
- [AUDIO_DAI_DIR_TXRX](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga810df470210d28a0eb0d7a12e8fde72f)
- [audio_codec_api](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#gac5af3f04f8428891d0d0d20371c57c9c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [audio_dai_dir_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)
- [audio_codec_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga13ecf277fdf4cfaaa424402587a1a7ad)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [audio_codec_tx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5365e64b28a7fd33d359eb020cd7f366)
- [audio_codec_rx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga56e51f3a24b7fef4ce4fcb212b5807d9)
- [audio_codec_configure_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga751115a5ab2d9ca3f3362c76684743c0)
- [audio_codec_start_output_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga0bba1b85f9f55389c5e52e8589947cc3)
- [audio_codec_stop_output_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#gab05f39f6aedd5ddaef911eeb0e8923cd)
- [audio_codec_set_property_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga1aa7dff0874ce441560a567a1a6d2389)
- [audio_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5411b79fa217b0f9c63dc6890323804c)
- [audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)
- [audio_codec_apply_properties_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#gabe3ce7aa1275f171856157716796ee94)
- [audio_codec_clear_errors_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga3998c4fade7829c14a8044c6efc3166c)
- [audio_codec_register_error_callback_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga6db1b3cf16e013ad5d59eef50acb4b78)
- [audio_codec_route_input_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga00729fd4ff9c7bb25ab0a44691b15fcd)
- [audio_codec_route_output_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga16647c5337af251140a9fa70e78b4d34)
- [audio_codec_start_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#gaf15768e53d0d5cec90f8489302c19227)
- [audio_codec_stop_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#ga4a283340b9ab266c8db97033b6e64865)
- [audio_codec_write_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#gabe62bf451dd9cb4bfa68e6a016415668)
- [audio_codec_register_done_callback_t](../api_buffer_paging_topic_reference/P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md#gac37a03bca2c70f7608a41910df70d4e2)
- [audio_pcm_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga8fd2079e6128c8a6da59c2dee58101ca)
- [AUDIO_PCM_RATE_8K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8)
- [AUDIO_PCM_RATE_11P025K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caa534b2e8dfa910c18b0617c236fa18c4d)
- [AUDIO_PCM_RATE_16K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3)
- [AUDIO_PCM_RATE_22P05K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caa77fab8d698408449f11d0974bfebaa0b)
- [AUDIO_PCM_RATE_24K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945)
- [AUDIO_PCM_RATE_32K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90)
- [AUDIO_PCM_RATE_44P1K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad)
- [AUDIO_PCM_RATE_48K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913)
- [AUDIO_PCM_RATE_96K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811)
- [AUDIO_PCM_RATE_192K](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9)
- [audio_pcm_width_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga1898dae0fac2e2bf34596453037bff7e)
- [AUDIO_PCM_WIDTH_16_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e)
- [AUDIO_PCM_WIDTH_20_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638)
- [AUDIO_PCM_WIDTH_24_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa)
- [AUDIO_PCM_WIDTH_32_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f)
- [audio_dai_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga147094be4c7c5d62df695673d293f12d)
- [AUDIO_DAI_TYPE_I2S](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac)
- [AUDIO_DAI_TYPE_LEFT_JUSTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da3cac1ab007667ecc477f493cb74ca504)
- [AUDIO_DAI_TYPE_RIGHT_JUSTIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da94fdc805aec7c34da2de990d1b1bef6e)
- [AUDIO_DAI_TYPE_PCMA](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da0376329aa4700f6b6aed798a13cb1efe)
- [AUDIO_DAI_TYPE_PCMB](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12daa578a69e94a460428e0d09f29cbf9ade)
- [AUDIO_DAI_TYPE_PCM](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12dad32b311e083c62d10b20a4028295d192)
- [AUDIO_DAI_TYPE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c)
- [AUDIO_PROPERTY_OUTPUT_VOLUME](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8)
- [AUDIO_PROPERTY_OUTPUT_MUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb)
- [AUDIO_PROPERTY_INPUT_VOLUME](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804ca0608dca9fec8160429d17d1d7dac0026)
- [AUDIO_PROPERTY_INPUT_MUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804ca9b4548cfe663072a98db20ea0da377c1)
- [AUDIO_PROPERTY_EQ_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga5411b79fa217b0f9c63dc6890323804ca22cc7ebf7a5c7732fd507835c32aa642)
- [audio_codec_set_property()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga6d28af0279eb8e4b693ea35f5235f189)
- [AUDIO_CHANNEL_FRONT_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18)
- [AUDIO_CHANNEL_FRONT_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75)
- [AUDIO_CHANNEL_LFE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6)
- [AUDIO_CHANNEL_FRONT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8)
- [AUDIO_CHANNEL_REAR_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc)
- [AUDIO_CHANNEL_REAR_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9)
- [AUDIO_CHANNEL_REAR_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04)
- [AUDIO_CHANNEL_SIDE_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba)
- [AUDIO_CHANNEL_SIDE_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec)
- [AUDIO_CHANNEL_HEADPHONE_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6affc38ea2d76af83e6b06a1471dd68cfa)
- [AUDIO_CHANNEL_HEADPHONE_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a7b8d80478453df358cbdb7064f7a656d)
- [AUDIO_CHANNEL_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878)
- [AUDIO_CHANNEL_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a1a35205e5a757748b3cf2f2048956cfe)
- [AUDIO_CHANNEL_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a3ad5430c80ae5a55ecbaf9246bd3ae93)
- [AUDIO_CHANNEL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga966cf980ce24855830e24b5de4d884d6a5370ff516a32a36a9f643d5906461817)
- [audio_route_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga3b21ded95eb16d2c5f9f8da3c580a411)
- [AUDIO_ROUTE_BYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga3b21ded95eb16d2c5f9f8da3c580a411a68af44d32f8c5e46a962fe0fc0fe0323)
- [AUDIO_ROUTE_PLAYBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga3b21ded95eb16d2c5f9f8da3c580a411a726898c5bfe3cbb217e3bca2fd1cdf7e)
- [AUDIO_ROUTE_PLAYBACK_CAPTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga3b21ded95eb16d2c5f9f8da3c580a411aa105c5914186aa9fbbd81af4e754ff0d)
- [AUDIO_ROUTE_CAPTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga3b21ded95eb16d2c5f9f8da3c580a411a31ebeb6337049a1ccea29ede230ad28a)
- [audio_codec_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga2923c9aca9b8656ba3e3741d5860279a)
- [AUDIO_CODEC_ERROR_OVERCURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1)
- [AUDIO_CODEC_ERROR_OVERTEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f)
- [AUDIO_CODEC_ERROR_UNDERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba)
- [AUDIO_CODEC_ERROR_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6)
- [AUDIO_CODEC_ERROR_DC](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35)
- [audio_codec_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga0c3344ea62fe994203315a0a7c20616c)
- [audio_codec_start_output](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga186e9c63c792072280558b953ced1cf7)
- [audio_codec_stop_output](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga6faba1d52c8d93e5ab5ec9954bf52f4a)
- [audio_codec_apply_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gadd16956b1160388a17c23d6cc84218b3)
- [audio_codec_clear_errors](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga550f86c43f7d96a1d826330d9da2d1af)
- [audio_codec_register_error_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga90f86f013dd46bad33bc95b2a7c8e1c9)
- [audio_codec_route_input](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga92dc9ce48ff0785dbf002f52afcef254)
- [audio_codec_route_output](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gadaa36aabb932903c725007c2005a7304)
- [audio_codec_start](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga445f95326d5bcf51c355dfc128f1e862)
- [audio_codec_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga3fa574a02bc12c578ea306202a222d32)
- [audio_codec_write](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gab6b430783bba55d30a2b99b4bf25a040)
- [audio_codec_register_done_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5e64f3537a4b0345f82e3e73992ee46a)

<a id="header-details"></a>

---

[上一章](P001_zephyr__drivers__clock_control__clock_control_ifx_cat1.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__drivers__bluetooth.h_文件参考.md)
