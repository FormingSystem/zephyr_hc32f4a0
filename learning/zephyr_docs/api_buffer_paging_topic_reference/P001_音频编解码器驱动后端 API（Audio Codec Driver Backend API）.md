---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-1
title: 音频编解码器驱动后端 API（Audio Codec Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_音频编解码器驱动后端 API（Audio Codec Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现音频编解码器驱动（Audio Codec Driver）所需的 API 类型定义、回调签名及其他辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_audio_5Fcodec_5Fdriver_5Fapi"></a>

```c
struct audio_codec_driver_api
```

相关声明：[audio_codec_driver_api](../driver_model_reference/P017_音频编解码器驱动接口.md)。

驱动操作（Driver Operations）：音频编解码器（Audio Codec）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_gac5af3f04f8428891d0d0d20371c57c9c"></a>

```c
#define audio_codec_api audio_codec_driver_api __DEPRECATED_MACRO
```

相关声明：[audio_codec_api](#gac5af3f04f8428891d0d0d20371c57c9c)、[audio_codec_driver_api](../driver_model_reference/P017_音频编解码器驱动接口.md)。

audio_codec_driver_api 的旧版结构体标签别名（Legacy Struct Tag Alias），用于尚未将后端结构体更新为 audio_codec_driver_api 的音频编解码器驱动。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_ga751115a5ab2d9ca3f3362c76684743c0"></a>

```c
typedef int(* audio_codec_configure_t) (const struct device *dev, struct audio_codec_cfg *cfg)
```

相关声明：[audio_codec_configure_t](#ga751115a5ab2d9ca3f3362c76684743c0)、[device](../device_reference/P002_设备对象结构.md)、[audio_codec_cfg](../driver_model_reference/P016_音频编解码器配置.md)。

配置音频编解码器设备（Audio Codec Device）的回调 API。

<a id="r_ga0bba1b85f9f55389c5e52e8589947cc3"></a>

```c
typedef void(* audio_codec_start_output_t) (const struct device *dev)
```

相关声明：[audio_codec_start_output_t](#ga0bba1b85f9f55389c5e52e8589947cc3)、[device](../device_reference/P002_设备对象结构.md)。

启动输出音频播放（Audio Playback）的回调 API。

<a id="r_gab05f39f6aedd5ddaef911eeb0e8923cd"></a>

```c
typedef void(* audio_codec_stop_output_t) (const struct device *dev)
```

相关声明：[audio_codec_stop_output_t](#gab05f39f6aedd5ddaef911eeb0e8923cd)、[device](../device_reference/P002_设备对象结构.md)。

停止输出音频播放（Audio Playback）的回调 API。

<a id="r_ga1aa7dff0874ce441560a567a1a6d2389"></a>

```c
typedef int(* audio_codec_set_property_t) (const struct device *dev, audio_property_t property, audio_channel_t channel, audio_property_value_t val)
```

相关声明：[audio_codec_set_property_t](#ga1aa7dff0874ce441560a567a1a6d2389)、[device](../device_reference/P002_设备对象结构.md)、[audio_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5411b79fa217b0f9c63dc6890323804c)、[audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)、[audio_property_value_t](../audio_video_model_reference/P067_audio_property_value_t_联合体.md)。

设置音频编解码器属性（Property）的回调 API。

<a id="r_gabe3ce7aa1275f171856157716796ee94"></a>

```c
typedef int(* audio_codec_apply_properties_t) (const struct device *dev)
```

相关声明：[audio_codec_apply_properties_t](#gabe3ce7aa1275f171856157716796ee94)、[device](../device_reference/P002_设备对象结构.md)。

应用缓存的音频编解码器属性（Cached Properties）的回调 API。

<a id="r_ga3998c4fade7829c14a8044c6efc3166c"></a>

```c
typedef int(* audio_codec_clear_errors_t) (const struct device *dev)
```

相关声明：[audio_codec_clear_errors_t](#ga3998c4fade7829c14a8044c6efc3166c)、[device](../device_reference/P002_设备对象结构.md)。

清除音频编解码器错误（Errors）的回调 API。

<a id="r_ga6db1b3cf16e013ad5d59eef50acb4b78"></a>

```c
typedef int(* audio_codec_register_error_callback_t) (const struct device *dev, audio_codec_error_callback_t cb)
```

相关声明：[audio_codec_register_error_callback_t](#ga6db1b3cf16e013ad5d59eef50acb4b78)、[device](../device_reference/P002_设备对象结构.md)、[audio_codec_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga13ecf277fdf4cfaaa424402587a1a7ad)。

注册音频编解码器错误回调（Error Callback）的回调 API。

<a id="r_ga00729fd4ff9c7bb25ab0a44691b15fcd"></a>

```c
typedef int(* audio_codec_route_input_t) (const struct device *dev, audio_channel_t channel, uint32_t input)
```

相关声明：[audio_codec_route_input_t](#ga00729fd4ff9c7bb25ab0a44691b15fcd)、[device](../device_reference/P002_设备对象结构.md)、[audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

路由音频编解码器输入（Input Routing）的回调 API。

<a id="r_ga16647c5337af251140a9fa70e78b4d34"></a>

```c
typedef int(* audio_codec_route_output_t) (const struct device *dev, audio_channel_t channel, uint32_t output)
```

相关声明：[audio_codec_route_output_t](#ga16647c5337af251140a9fa70e78b4d34)、[device](../device_reference/P002_设备对象结构.md)、[audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

路由音频编解码器输出（Output Routing）的回调 API。

<a id="r_gaf15768e53d0d5cec90f8489302c19227"></a>

```c
typedef int(* audio_codec_start_t) (const struct device *dev, audio_dai_dir_t dir)
```

相关声明：[audio_codec_start_t](#gaf15768e53d0d5cec90f8489302c19227)、[device](../device_reference/P002_设备对象结构.md)、[audio_dai_dir_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)。

启动音频编解码器播放或采集（Playback or Capture）的回调 API。

<a id="r_ga4a283340b9ab266c8db97033b6e64865"></a>

```c
typedef int(* audio_codec_stop_t) (const struct device *dev, audio_dai_dir_t dir)
```

相关声明：[audio_codec_stop_t](#ga4a283340b9ab266c8db97033b6e64865)、[device](../device_reference/P002_设备对象结构.md)、[audio_dai_dir_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)。

停止音频编解码器播放或采集（Playback or Capture）的回调 API。

<a id="r_gabe62bf451dd9cb4bfa68e6a016415668"></a>

```c
typedef int(* audio_codec_write_t) (const struct device *dev, uint8_t *data, size_t data_size)
```

相关声明：[audio_codec_write_t](#gabe62bf451dd9cb4bfa68e6a016415668)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

提交音频编解码器播放数据（Playback Data）的回调 API。

<a id="r_gac37a03bca2c70f7608a41910df70d4e2"></a>

```c
typedef int(* audio_codec_register_done_callback_t) (const struct device *dev, audio_codec_tx_done_callback_t tx_cb, void *tx_cb_user_data, audio_codec_rx_done_callback_t rx_cb, void *rx_cb_user_data)
```

相关声明：[audio_codec_register_done_callback_t](#gac37a03bca2c70f7608a41910df70d4e2)、[device](../device_reference/P002_设备对象结构.md)、[audio_codec_tx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5365e64b28a7fd33d359eb020cd7f366)、[audio_codec_rx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga56e51f3a24b7fef4ce4fcb212b5807d9)。

注册音频编解码器 DMA 完成回调（Completion Callbacks）的回调 API。

## 1.4\_详细说明（Detailed Documentation）

<a id="gac5af3f04f8428891d0d0d20371c57c9c"></a>

### `audio_codec_api`

```c
#define audio_codec_api audio_codec_driver_api __DEPRECATED_MACRO
```

```c
#include <zephyr/audio/codec.h>
```

audio_codec_driver_api 的旧版结构体标签别名（Legacy Struct Tag Alias），用于尚未将后端结构体更新为 audio_codec_driver_api 的音频编解码器驱动。

**已弃用（Deprecated）**：已弃用（Deprecated）：音频编解码器驱动应使用 DEVICE_API() 宏声明其驱动 API。

<a id="gabe3ce7aa1275f171856157716796ee94"></a>

### `audio_codec_apply_properties_t`

```c
typedef int(* audio_codec_apply_properties_t) (const struct device *dev)
```

```c
#include <zephyr/audio/codec.h>
```

应用缓存的音频编解码器属性（Cached Properties）的回调 API。

参数说明参见 audio_codec_apply_properties()。

<a id="ga3998c4fade7829c14a8044c6efc3166c"></a>

### `audio_codec_clear_errors_t`

```c
typedef int(* audio_codec_clear_errors_t) (const struct device *dev)
```

```c
#include <zephyr/audio/codec.h>
```

清除音频编解码器错误（Errors）的回调 API。

参数说明参见 audio_codec_clear_errors()。

<a id="ga751115a5ab2d9ca3f3362c76684743c0"></a>

### `audio_codec_configure_t`

```c
typedef int(* audio_codec_configure_t) (const struct device *dev, struct audio_codec_cfg *cfg)
```

```c
#include <zephyr/audio/codec.h>
```

配置音频编解码器设备（Audio Codec Device）的回调 API。

参数说明参见 audio_codec_configure()。

<a id="gac37a03bca2c70f7608a41910df70d4e2"></a>

### `audio_codec_register_done_callback_t`

```c
typedef int(* audio_codec_register_done_callback_t) (const struct device *dev, audio_codec_tx_done_callback_t tx_cb, void *tx_cb_user_data, audio_codec_rx_done_callback_t rx_cb, void *rx_cb_user_data)
```

```c
#include <zephyr/audio/codec.h>
```

注册音频编解码器 DMA 完成回调（Completion Callbacks）的回调 API。

参数说明参见 audio_codec_register_done_callback()。

<a id="ga6db1b3cf16e013ad5d59eef50acb4b78"></a>

### `audio_codec_register_error_callback_t`

```c
typedef int(* audio_codec_register_error_callback_t) (const struct device *dev, audio_codec_error_callback_t cb)
```

```c
#include <zephyr/audio/codec.h>
```

注册音频编解码器错误回调（Error Callback）的回调 API。

参数说明参见 audio_codec_register_error_callback()。

<a id="ga00729fd4ff9c7bb25ab0a44691b15fcd"></a>

### `audio_codec_route_input_t`

```c
typedef int(* audio_codec_route_input_t) (const struct device *dev, audio_channel_t channel, uint32_t input)
```

```c
#include <zephyr/audio/codec.h>
```

路由音频编解码器输入（Input Routing）的回调 API。

参数说明参见 audio_codec_route_input()。

<a id="ga16647c5337af251140a9fa70e78b4d34"></a>

### `audio_codec_route_output_t`

```c
typedef int(* audio_codec_route_output_t) (const struct device *dev, audio_channel_t channel, uint32_t output)
```

```c
#include <zephyr/audio/codec.h>
```

路由音频编解码器输出（Output Routing）的回调 API。

参数说明参见 audio_codec_route_output()。

<a id="ga1aa7dff0874ce441560a567a1a6d2389"></a>

### `audio_codec_set_property_t`

```c
typedef int(* audio_codec_set_property_t) (const struct device *dev, audio_property_t property, audio_channel_t channel, audio_property_value_t val)
```

```c
#include <zephyr/audio/codec.h>
```

设置音频编解码器属性（Property）的回调 API。

参数说明参见 audio_codec_set_property()。

<a id="ga0bba1b85f9f55389c5e52e8589947cc3"></a>

### `audio_codec_start_output_t`

```c
typedef void(* audio_codec_start_output_t) (const struct device *dev)
```

```c
#include <zephyr/audio/codec.h>
```

启动输出音频播放（Audio Playback）的回调 API。

参数说明参见 audio_codec_start_output()。

<a id="gaf15768e53d0d5cec90f8489302c19227"></a>

### `audio_codec_start_t`

```c
typedef int(* audio_codec_start_t) (const struct device *dev, audio_dai_dir_t dir)
```

```c
#include <zephyr/audio/codec.h>
```

启动音频编解码器播放或采集（Playback or Capture）的回调 API。

参数说明参见 audio_codec_start()。

<a id="gab05f39f6aedd5ddaef911eeb0e8923cd"></a>

### `audio_codec_stop_output_t`

```c
typedef void(* audio_codec_stop_output_t) (const struct device *dev)
```

```c
#include <zephyr/audio/codec.h>
```

停止输出音频播放（Audio Playback）的回调 API。

参数说明参见 audio_codec_stop_output()。

<a id="ga4a283340b9ab266c8db97033b6e64865"></a>

### `audio_codec_stop_t`

```c
typedef int(* audio_codec_stop_t) (const struct device *dev, audio_dai_dir_t dir)
```

```c
#include <zephyr/audio/codec.h>
```

停止音频编解码器播放或采集（Playback or Capture）的回调 API。

参数说明参见 audio_codec_stop()。

<a id="gabe62bf451dd9cb4bfa68e6a016415668"></a>

### `audio_codec_write_t`

```c
typedef int(* audio_codec_write_t) (const struct device *dev, uint8_t *data, size_t data_size)
```

```c
#include <zephyr/audio/codec.h>
```

提交音频编解码器播放数据（Playback Data）的回调 API。

参数说明参见 audio_codec_write()。


## 1.5\_原页交叉引用（Cross References）

- [audio_codec_driver_api](../driver_model_reference/P017_音频编解码器驱动接口.md)
- [device](../device_reference/P002_设备对象结构.md)
- [audio_codec_cfg](../driver_model_reference/P016_音频编解码器配置.md)
- [audio_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5411b79fa217b0f9c63dc6890323804c)
- [audio_channel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga966cf980ce24855830e24b5de4d884d6)
- [audio_property_value_t](../audio_video_model_reference/P067_audio_property_value_t_联合体.md)
- [audio_codec_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga13ecf277fdf4cfaaa424402587a1a7ad)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [audio_dai_dir_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gad3a2ec4622f9a7b0eb1b4d0a463e20d5)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [audio_codec_tx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5365e64b28a7fd33d359eb020cd7f366)
- [audio_codec_rx_done_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga56e51f3a24b7fef4ce4fcb212b5807d9)
- [zephyr/audio/codec.h](https://docs.zephyrproject.org/latest/doxygen/html/codec_8h.html)
- [Deprecated](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000135)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)
- [audio_codec_apply_properties()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gadd16956b1160388a17c23d6cc84218b3)
- [audio_codec_clear_errors()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga550f86c43f7d96a1d826330d9da2d1af)
- [audio_codec_configure()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga0c3344ea62fe994203315a0a7c20616c)
- [audio_codec_register_done_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga5e64f3537a4b0345f82e3e73992ee46a)
- [audio_codec_register_error_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga90f86f013dd46bad33bc95b2a7c8e1c9)
- [audio_codec_route_input()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga92dc9ce48ff0785dbf002f52afcef254)
- [audio_codec_route_output()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gadaa36aabb932903c725007c2005a7304)
- [audio_codec_set_property()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga6d28af0279eb8e4b693ea35f5235f189)
- [audio_codec_start_output()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga186e9c63c792072280558b953ced1cf7)
- [audio_codec_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga445f95326d5bcf51c355dfc128f1e862)
- [audio_codec_stop_output()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga6faba1d52c8d93e5ab5ec9954bf52f4a)
- [audio_codec_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga3fa574a02bc12c578ea306202a222d32)
- [audio_codec_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#gab6b430783bba55d30a2b99b4bf25a040)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_数据缓冲区（Data buffers）.md)
