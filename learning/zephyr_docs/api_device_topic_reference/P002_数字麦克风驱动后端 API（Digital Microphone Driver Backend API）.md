---
id: learning.zephyr-docs.api-device-topic-reference.page-2
title: 数字麦克风驱动后端 API（Digital Microphone Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_数字麦克风驱动后端 API（Digital Microphone Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现数字麦克风（Digital Microphone）驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_dmic_5Fdriver_5Fapi"></a>

```c
struct dmic_driver_api
```

相关声明：[dmic_driver_api](../audio_video_model_reference/P007_dmic_driver_api_结构体.md)。

驱动操作（Driver Operations）：数字麦克风（Digital Microphone）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.2\_类型定义（Typedefs）

<a id="r_gaf8f2d714a8e93df2178b19ba46533909"></a>

```c
typedef int(* dmic_configure_t) (const struct device *dev, struct dmic_cfg *config)
```

相关声明：[dmic_configure_t](#gaf8f2d714a8e93df2178b19ba46533909)、[device](../device_reference/P002_设备对象结构.md)、[dmic_cfg](../audio_video_model_reference/P006_dmic_cfg_结构体.md)。

用于配置数字麦克风（DMIC）设备的回调 API。

<a id="r_ga777e407deafee37c7f26039dd3144c4a"></a>

```c
typedef int(* dmic_trigger_t) (const struct device *dev, enum dmic_trigger cmd)
```

相关声明：[dmic_trigger_t](#ga777e407deafee37c7f26039dd3144c4a)、[device](../device_reference/P002_设备对象结构.md)、[dmic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga24aae0a7871b3bd31b130061feeefc14)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

用于向 DMIC 设备发送命令的回调 API。

<a id="r_gab53ad4a4dddc12cdc7d012774f0ef63a"></a>

```c
typedef int(* dmic_read_t) (const struct device *dev, uint8_t stream, void **buffer, size_t *size, int32_t timeout)
```

相关声明：[dmic_read_t](#gab53ad4a4dddc12cdc7d012774f0ef63a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

用于从 DMIC 设备读取脉冲编码调制（PCM）数据的回调 API。

## 2.3\_详细说明（Detailed Documentation）

<a id="gaf8f2d714a8e93df2178b19ba46533909"></a>

### `dmic_configure_t`

```c
typedef int(* dmic_configure_t) (const struct device *dev, struct dmic_cfg *config)
```

```c
#include <zephyr/audio/dmic.h>
```

用于配置数字麦克风（DMIC）设备的回调 API。

参数说明参见 `dmic_configure()`。

<a id="gab53ad4a4dddc12cdc7d012774f0ef63a"></a>

### `dmic_read_t`

```c
typedef int(* dmic_read_t) (const struct device *dev, uint8_t stream, void **buffer, size_t *size, int32_t timeout)
```

```c
#include <zephyr/audio/dmic.h>
```

用于从 DMIC 设备读取脉冲编码调制（PCM）数据的回调 API。

参数说明参见 `dmic_read()`。

<a id="ga777e407deafee37c7f26039dd3144c4a"></a>

### `dmic_trigger_t`

```c
typedef int(* dmic_trigger_t) (const struct device *dev, enum dmic_trigger cmd)
```

```c
#include <zephyr/audio/dmic.h>
```

用于向 DMIC 设备发送命令的回调 API。

参数说明参见 `dmic_trigger()`。


## 2.4\_原页交叉引用（Cross References）

- [dmic_driver_api](../audio_video_model_reference/P007_dmic_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [dmic_cfg](../audio_video_model_reference/P006_dmic_cfg_结构体.md)
- [dmic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga24aae0a7871b3bd31b130061feeefc14)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [zephyr/audio/dmic.h](https://docs.zephyrproject.org/latest/doxygen/html/dmic_8h.html)
- [dmic_configure()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga09fc7074323c2f3115b06c5212d21fc7)
- [dmic_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga74b51bddaa175c518d45211f936d08e6)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P001_APDS9960 API主题.md) · [返回大纲](大纲.md) · [下一章](P003_BQ274XX API主题.md)
