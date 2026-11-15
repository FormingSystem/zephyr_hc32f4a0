---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-10
title: zephyr__audio__dmic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dmic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_audio\_\_dmic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dmic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字麦克风（Digital Microphones）的公共API头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
```

查看此文件的源码。

数字麦克风（Digital Microphone）公共 API 头文件，包含数字麦克风 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_pdm_5Fio_5Fcfg"></a>

```c
struct pdm_io_cfg
```

相关声明：[pdm_io_cfg](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md)。

脉冲密度调制（PDM）的输入输出信号配置。

<a id="r_pcm_5Fstream_5Fcfg"></a>

```c
struct pcm_stream_cfg
```

相关声明：[pcm_stream_cfg](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md)。

由脉冲密度调制（PDM）硬件输出的PCM流配置。

<a id="r_pdm_5Fchan_5Fcfg"></a>

```c
struct pdm_chan_cfg
```

相关声明：[pdm_chan_cfg](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md)。

PDM通道到逻辑PCM输出通道的映射/排列（Mapping / Ordering）。

<a id="r_dmic_5Fcfg"></a>

```c
struct dmic_cfg
```

相关声明：[dmic_cfg](../audio_video_model_reference/P006_dmic_cfg_结构体.md)。

数字麦克风（DMIC）配置API的输入配置结构。

<a id="r_dmic_5Fdriver_5Fapi"></a>

```c
struct dmic_driver_api
```

相关声明：[dmic_driver_api](../audio_video_model_reference/P007_dmic_driver_api_结构体.md)。

驱动操作（Driver Operations）：数字麦克风（Digital Microphone）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.2\_宏定义（Macros）

<a id="r_ga61b191e55cffb65950e151cf1f67aed4"></a>

```c
#define PDM_DT_IO_CFG_GET(node_id)
```

相关声明：[PDM_DT_IO_CFG_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga61b191e55cffb65950e151cf1f67aed4)。

根据设备树描述（Devicetree Description）构造 `pdm_io_cfg`。

<a id="r_ga0cd5bf8dad26b9315619e13c4c74f300"></a>

```c
#define PDM_DT_HAS_LEFT_CHANNEL(node_id)
```

相关声明：[PDM_DT_HAS_LEFT_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga0cd5bf8dad26b9315619e13c4c74f300)。

检查麦克风是否有可用的左声道（Left Channel）。

<a id="r_ga0984dc3e571fd79f4700467e7305e5c6"></a>

```c
#define PDM_DT_HAS_RIGHT_CHANNEL(node_id)
```

相关声明：[PDM_DT_HAS_RIGHT_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga0984dc3e571fd79f4700467e7305e5c6)。

检查麦克风是否有可用的右声道（Right Channel）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.3\_类型定义（Typedefs）

<a id="r_gaf8f2d714a8e93df2178b19ba46533909"></a>

```c
typedef int(* dmic_configure_t) (const struct device *dev, struct dmic_cfg *config)
```

相关声明：[dmic_configure_t](../api_device_topic_reference/P002_数字麦克风驱动后端 API（Digital Microphone Driver Backend API）.md#gaf8f2d714a8e93df2178b19ba46533909)、[device](../device_reference/P002_设备对象结构.md)、[dmic_cfg](../audio_video_model_reference/P006_dmic_cfg_结构体.md)。

用于配置数字麦克风（DMIC）设备的回调 API。

<a id="r_ga777e407deafee37c7f26039dd3144c4a"></a>

```c
typedef int(* dmic_trigger_t) (const struct device *dev, enum dmic_trigger cmd)
```

相关声明：[dmic_trigger_t](../api_device_topic_reference/P002_数字麦克风驱动后端 API（Digital Microphone Driver Backend API）.md#ga777e407deafee37c7f26039dd3144c4a)、[device](../device_reference/P002_设备对象结构.md)、[dmic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga24aae0a7871b3bd31b130061feeefc14)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

用于向 DMIC 设备发送命令的回调 API。

<a id="r_gab53ad4a4dddc12cdc7d012774f0ef63a"></a>

```c
typedef int(* dmic_read_t) (const struct device *dev, uint8_t stream, void **buffer, size_t *size, int32_t timeout)
```

相关声明：[dmic_read_t](../api_device_topic_reference/P002_数字麦克风驱动后端 API（Digital Microphone Driver Backend API）.md#gab53ad4a4dddc12cdc7d012774f0ef63a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

用于从 DMIC 设备读取脉冲编码调制（PCM）数据的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.4\_枚举（Enumerations）

<a id="r_gac99a4f579b6aa45bb6cce1f797247a23"></a>

```c
enum dmic_state { DMIC_STATE_UNINIT , DMIC_STATE_INITIALIZED , DMIC_STATE_CONFIGURED , DMIC_STATE_ACTIVE , DMIC_STATE_PAUSED , DMIC_STATE_ERROR }
```

相关声明：[dmic_state](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gac99a4f579b6aa45bb6cce1f797247a23)、[DMIC_STATE_UNINIT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a45b37076808ed30994ed02ca0581b1be)、[DMIC_STATE_INITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a733caa2b8a49d4b2f78698b810cbdbc1)、[DMIC_STATE_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a70d47513a9c0ff07cdf4d814ac78a826)、[DMIC_STATE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23ae3f1d62885d522598ced88089f4ae8b4)、[DMIC_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a14306a41b9a832343c8b6e1fcb971c81)、[DMIC_STATE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a8b6622df75d7c4205c11db2f26619eba)。

数字麦克风（DMIC）驱动状态（Driver States）。

<a id="r_ga24aae0a7871b3bd31b130061feeefc14"></a>

```c
enum dmic_trigger { DMIC_TRIGGER_STOP , DMIC_TRIGGER_START , DMIC_TRIGGER_PAUSE , DMIC_TRIGGER_RELEASE , DMIC_TRIGGER_RESET }
```

相关声明：[dmic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga24aae0a7871b3bd31b130061feeefc14)、[DMIC_TRIGGER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14ab3f5cdba100516563098e659adee2e23)、[DMIC_TRIGGER_START](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14a031d6c7646642d4858a22c853d6d6eaa)、[DMIC_TRIGGER_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14a6077bf984fd654947ff36e1bc66e98e5)、[DMIC_TRIGGER_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14a69b5be548e54589e03645baf2ab80804)、[DMIC_TRIGGER_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14aa6dca65941d65845383209c081173a79)。

数字麦克风（DMIC）驱动触发命令（Trigger Commands）。

<a id="r_ga7c2067bbb1e07fa8afe315f91a127991"></a>

```c
enum pdm_lr { PDM_CHAN_LEFT , PDM_CHAN_RIGHT }
```

相关声明：[pdm_lr](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga7c2067bbb1e07fa8afe315f91a127991)、[PDM_CHAN_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga7c2067bbb1e07fa8afe315f91a127991acca80c04de225e35ae2bdfafcca6e345)、[PDM_CHAN_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga7c2067bbb1e07fa8afe315f91a127991a0c746475a2b5873aa863058358d8e7d0)。

脉冲密度调制（PDM）左／右通道（LEFT/RIGHT Channels）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.5\_函数（Functions）

<a id="r_ga5d1fcefaf085962d779b8082b3480cbd"></a>

```c
static uint32_t dmic_build_channel_map (uint8_t channel, uint8_t pdm, enum pdm_lr lr)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[dmic_build_channel_map](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga5d1fcefaf085962d779b8082b3480cbd)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pdm_lr](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga7c2067bbb1e07fa8afe315f91a127991)。

构造通道映射（Channel Map），用于填充 `struct pdm_chan_cfg`。

<a id="r_gaa1fded235751a71632965011a62ddead"></a>

```c
static void dmic_parse_channel_map (uint32_t channel_map_lo, uint32_t channel_map_hi, uint8_t channel, uint8_t *pdm, enum pdm_lr *lr)
```

相关声明：[dmic_parse_channel_map](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gaa1fded235751a71632965011a62ddead)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pdm_lr](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga7c2067bbb1e07fa8afe315f91a127991)。

解析 `pdm_chan_cfg` 中通道映射（Channel Map）的辅助函数。

<a id="r_gaf5abf489fe6ed18c2daea5d918aa2f80"></a>

```c
static uint32_t dmic_build_clk_skew_map (uint8_t pdm, uint8_t skew)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[dmic_build_clk_skew_map](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gaf5abf489fe6ed18c2daea5d918aa2f80)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

构造位图（Bit Map），记录各 PDM 通道的时钟偏斜值（Clock Skew Values）。

<a id="r_ga09fc7074323c2f3115b06c5212d21fc7"></a>

```c
static int dmic_configure (const struct device *dev, struct dmic_cfg *cfg)
```

相关声明：[dmic_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga09fc7074323c2f3115b06c5212d21fc7)、[device](../device_reference/P002_设备对象结构.md)、[dmic_cfg](../audio_video_model_reference/P006_dmic_cfg_结构体.md)。

配置 DMIC 驱动和控制器（Driver and Controllers）。

<a id="r_ga051e82f30b76f0fca789ba0147054184"></a>

```c
static int dmic_trigger (const struct device *dev, enum dmic_trigger cmd)
```

相关声明：[dmic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga051e82f30b76f0fca789ba0147054184)、[device](../device_reference/P002_设备对象结构.md)、[dmic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga24aae0a7871b3bd31b130061feeefc14)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

向 DMIC 驱动发送命令（Command）。

<a id="r_ga74b51bddaa175c518d45211f936d08e6"></a>

```c
static int dmic_read (const struct device *dev, uint8_t stream, void **buffer, size_t *size, int32_t timeout)
```

相关声明：[dmic_read](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga74b51bddaa175c518d45211f936d08e6)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

读取接收并抽取后的 PCM 数据流（Decimated PCM Data Stream）。


## 10.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P040_dmic.h_源码浏览.md)
- [pdm_io_cfg](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md)
- [pcm_stream_cfg](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md)
- [pdm_chan_cfg](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md)
- [dmic_cfg](../audio_video_model_reference/P006_dmic_cfg_结构体.md)
- [dmic_driver_api](../audio_video_model_reference/P007_dmic_driver_api_结构体.md)
- [PDM_DT_IO_CFG_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga61b191e55cffb65950e151cf1f67aed4)
- [PDM_DT_HAS_LEFT_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga0cd5bf8dad26b9315619e13c4c74f300)
- [PDM_DT_HAS_RIGHT_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga0984dc3e571fd79f4700467e7305e5c6)
- [dmic_configure_t](../api_device_topic_reference/P002_数字麦克风驱动后端 API（Digital Microphone Driver Backend API）.md#gaf8f2d714a8e93df2178b19ba46533909)
- [device](../device_reference/P002_设备对象结构.md)
- [dmic_trigger_t](../api_device_topic_reference/P002_数字麦克风驱动后端 API（Digital Microphone Driver Backend API）.md#ga777e407deafee37c7f26039dd3144c4a)
- [dmic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga24aae0a7871b3bd31b130061feeefc14)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [dmic_read_t](../api_device_topic_reference/P002_数字麦克风驱动后端 API（Digital Microphone Driver Backend API）.md#gab53ad4a4dddc12cdc7d012774f0ef63a)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [dmic_state](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gac99a4f579b6aa45bb6cce1f797247a23)
- [DMIC_STATE_UNINIT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a45b37076808ed30994ed02ca0581b1be)
- [DMIC_STATE_INITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a733caa2b8a49d4b2f78698b810cbdbc1)
- [DMIC_STATE_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a70d47513a9c0ff07cdf4d814ac78a826)
- [DMIC_STATE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23ae3f1d62885d522598ced88089f4ae8b4)
- [DMIC_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a14306a41b9a832343c8b6e1fcb971c81)
- [DMIC_STATE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a8b6622df75d7c4205c11db2f26619eba)
- [DMIC_TRIGGER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14ab3f5cdba100516563098e659adee2e23)
- [DMIC_TRIGGER_START](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14a031d6c7646642d4858a22c853d6d6eaa)
- [DMIC_TRIGGER_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14a6077bf984fd654947ff36e1bc66e98e5)
- [DMIC_TRIGGER_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14a69b5be548e54589e03645baf2ab80804)
- [DMIC_TRIGGER_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14aa6dca65941d65845383209c081173a79)
- [pdm_lr](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga7c2067bbb1e07fa8afe315f91a127991)
- [PDM_CHAN_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga7c2067bbb1e07fa8afe315f91a127991acca80c04de225e35ae2bdfafcca6e345)
- [PDM_CHAN_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga7c2067bbb1e07fa8afe315f91a127991a0c746475a2b5873aa863058358d8e7d0)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [dmic_build_channel_map](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga5d1fcefaf085962d779b8082b3480cbd)
- [dmic_parse_channel_map](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gaa1fded235751a71632965011a62ddead)
- [dmic_build_clk_skew_map](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gaf5abf489fe6ed18c2daea5d918aa2f80)
- [dmic_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga09fc7074323c2f3115b06c5212d21fc7)
- [dmic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga051e82f30b76f0fca789ba0147054184)
- [dmic_read](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga74b51bddaa175c518d45211f936d08e6)

<a id="header-details"></a>

---

[上一章](P009_zephyr__data__cobs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__drivers__crc.h_文件参考.md)
