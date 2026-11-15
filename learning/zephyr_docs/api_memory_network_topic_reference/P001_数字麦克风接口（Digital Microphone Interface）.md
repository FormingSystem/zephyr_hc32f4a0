---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-1
title: 数字麦克风接口（Digital Microphone Interface）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_数字麦克风接口（Digital Microphone Interface）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字麦克风的抽象（Abstraction）。

<a id="details"></a>

数字麦克风抽象（Digital Microphone Abstraction）。引入版本（Since）：1.13；API 版本（Version）：0.2.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_audio_5Fdmic_5Finterface_5Fbackend"></a>

相关声明：[数字麦克风驱动后端 API（Digital Microphone Driver Backend API）](../api_device_topic_reference/P002_数字麦克风驱动后端 API（Digital Microphone Driver Backend API）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 1.2\_文件（Files）

<a id="r_dmic_2Eh"></a>

```c
file dmic.h
```

相关声明：[dmic.h](../api_file_protocol_service_reference/P010_zephyr__audio__dmic.h_文件参考.md)。

数字麦克风（Digital Microphones）的公共API头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.3\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.4\_宏定义（Macros）

<a id="r_ga61b191e55cffb65950e151cf1f67aed4"></a>

```c
#define PDM_DT_IO_CFG_GET(node_id)
```

相关声明：[PDM_DT_IO_CFG_GET](#ga61b191e55cffb65950e151cf1f67aed4)。

根据设备树描述（Devicetree Description）构造 `pdm_io_cfg`。

<a id="r_ga0cd5bf8dad26b9315619e13c4c74f300"></a>

```c
#define PDM_DT_HAS_LEFT_CHANNEL(node_id)
```

相关声明：[PDM_DT_HAS_LEFT_CHANNEL](#ga0cd5bf8dad26b9315619e13c4c74f300)。

检查麦克风是否有可用的左声道（Left Channel）。

<a id="r_ga0984dc3e571fd79f4700467e7305e5c6"></a>

```c
#define PDM_DT_HAS_RIGHT_CHANNEL(node_id)
```

相关声明：[PDM_DT_HAS_RIGHT_CHANNEL](#ga0984dc3e571fd79f4700467e7305e5c6)。

检查麦克风是否有可用的右声道（Right Channel）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.5\_枚举（Enumerations）

<a id="r_gac99a4f579b6aa45bb6cce1f797247a23"></a>

```c
enum dmic_state { DMIC_STATE_UNINIT , DMIC_STATE_INITIALIZED , DMIC_STATE_CONFIGURED , DMIC_STATE_ACTIVE , DMIC_STATE_PAUSED , DMIC_STATE_ERROR }
```

相关声明：[dmic_state](#gac99a4f579b6aa45bb6cce1f797247a23)、[DMIC_STATE_UNINIT](#ggac99a4f579b6aa45bb6cce1f797247a23a45b37076808ed30994ed02ca0581b1be)、[DMIC_STATE_INITIALIZED](#ggac99a4f579b6aa45bb6cce1f797247a23a733caa2b8a49d4b2f78698b810cbdbc1)、[DMIC_STATE_CONFIGURED](#ggac99a4f579b6aa45bb6cce1f797247a23a70d47513a9c0ff07cdf4d814ac78a826)、[DMIC_STATE_ACTIVE](#ggac99a4f579b6aa45bb6cce1f797247a23ae3f1d62885d522598ced88089f4ae8b4)、[DMIC_STATE_PAUSED](#ggac99a4f579b6aa45bb6cce1f797247a23a14306a41b9a832343c8b6e1fcb971c81)、[DMIC_STATE_ERROR](#ggac99a4f579b6aa45bb6cce1f797247a23a8b6622df75d7c4205c11db2f26619eba)。

数字麦克风（DMIC）驱动状态（Driver States）。

<a id="r_ga24aae0a7871b3bd31b130061feeefc14"></a>

```c
enum dmic_trigger { DMIC_TRIGGER_STOP , DMIC_TRIGGER_START , DMIC_TRIGGER_PAUSE , DMIC_TRIGGER_RELEASE , DMIC_TRIGGER_RESET }
```

相关声明：[dmic_trigger](#ga24aae0a7871b3bd31b130061feeefc14)、[DMIC_TRIGGER_STOP](#gga24aae0a7871b3bd31b130061feeefc14ab3f5cdba100516563098e659adee2e23)、[DMIC_TRIGGER_START](#gga24aae0a7871b3bd31b130061feeefc14a031d6c7646642d4858a22c853d6d6eaa)、[DMIC_TRIGGER_PAUSE](#gga24aae0a7871b3bd31b130061feeefc14a6077bf984fd654947ff36e1bc66e98e5)、[DMIC_TRIGGER_RELEASE](#gga24aae0a7871b3bd31b130061feeefc14a69b5be548e54589e03645baf2ab80804)、[DMIC_TRIGGER_RESET](#gga24aae0a7871b3bd31b130061feeefc14aa6dca65941d65845383209c081173a79)。

数字麦克风（DMIC）驱动触发命令（Trigger Commands）。

<a id="r_ga7c2067bbb1e07fa8afe315f91a127991"></a>

```c
enum pdm_lr { PDM_CHAN_LEFT , PDM_CHAN_RIGHT }
```

相关声明：[pdm_lr](#ga7c2067bbb1e07fa8afe315f91a127991)、[PDM_CHAN_LEFT](#gga7c2067bbb1e07fa8afe315f91a127991acca80c04de225e35ae2bdfafcca6e345)、[PDM_CHAN_RIGHT](#gga7c2067bbb1e07fa8afe315f91a127991a0c746475a2b5873aa863058358d8e7d0)。

脉冲密度调制（PDM）左／右通道（LEFT/RIGHT Channels）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.6\_函数（Functions）

<a id="r_ga5d1fcefaf085962d779b8082b3480cbd"></a>

```c
static uint32_t dmic_build_channel_map (uint8_t channel, uint8_t pdm, enum pdm_lr lr)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[dmic_build_channel_map](#ga5d1fcefaf085962d779b8082b3480cbd)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pdm_lr](#ga7c2067bbb1e07fa8afe315f91a127991)。

构造通道映射（Channel Map），用于填充 `struct pdm_chan_cfg`。

<a id="r_gaa1fded235751a71632965011a62ddead"></a>

```c
static void dmic_parse_channel_map (uint32_t channel_map_lo, uint32_t channel_map_hi, uint8_t channel, uint8_t *pdm, enum pdm_lr *lr)
```

相关声明：[dmic_parse_channel_map](#gaa1fded235751a71632965011a62ddead)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pdm_lr](#ga7c2067bbb1e07fa8afe315f91a127991)。

解析 `pdm_chan_cfg` 中通道映射（Channel Map）的辅助函数。

<a id="r_gaf5abf489fe6ed18c2daea5d918aa2f80"></a>

```c
static uint32_t dmic_build_clk_skew_map (uint8_t pdm, uint8_t skew)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[dmic_build_clk_skew_map](#gaf5abf489fe6ed18c2daea5d918aa2f80)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

构造位图（Bit Map），记录各 PDM 通道的时钟偏斜值（Clock Skew Values）。

<a id="r_ga09fc7074323c2f3115b06c5212d21fc7"></a>

```c
static int dmic_configure (const struct device *dev, struct dmic_cfg *cfg)
```

相关声明：[dmic_configure](#ga09fc7074323c2f3115b06c5212d21fc7)、[device](../device_reference/P002_设备对象结构.md)、[dmic_cfg](../audio_video_model_reference/P006_dmic_cfg_结构体.md)。

配置 DMIC 驱动和控制器（Driver and Controllers）。

<a id="r_ga051e82f30b76f0fca789ba0147054184"></a>

```c
static int dmic_trigger (const struct device *dev, enum dmic_trigger cmd)
```

相关声明：[dmic_trigger](#ga051e82f30b76f0fca789ba0147054184)、[device](../device_reference/P002_设备对象结构.md)、[dmic_trigger](#ga24aae0a7871b3bd31b130061feeefc14)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

向 DMIC 驱动发送命令（Command）。

<a id="r_ga74b51bddaa175c518d45211f936d08e6"></a>

```c
static int dmic_read (const struct device *dev, uint8_t stream, void **buffer, size_t *size, int32_t timeout)
```

相关声明：[dmic_read](#ga74b51bddaa175c518d45211f936d08e6)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

读取接收并抽取后的 PCM 数据流（Decimated PCM Data Stream）。

## 1.7\_详细说明（Detailed Documentation）

<a id="ga0cd5bf8dad26b9315619e13c4c74f300"></a>

### `PDM_DT_HAS_LEFT_CHANNEL`

```c
#define PDM_DT_HAS_LEFT_CHANNEL ( node_id)
```

```c
#include <zephyr/audio/dmic.h>
```

展开值（Value）：

```c
DT_PROP(node_id, channel_left)
```

检查麦克风是否有可用的左声道（Left Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 包含 pdm-dmic 的设备树节点（Devicetree Node）。 |

<a id="ga0984dc3e571fd79f4700467e7305e5c6"></a>

### `PDM_DT_HAS_RIGHT_CHANNEL`

```c
#define PDM_DT_HAS_RIGHT_CHANNEL ( node_id)
```

```c
#include <zephyr/audio/dmic.h>
```

展开值（Value）：

```c
DT_PROP(node_id, channel_right)
```

检查麦克风是否有可用的右声道（Right Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 包含 pdm-dmic 的设备树节点（Devicetree Node）。 |

<a id="ga61b191e55cffb65950e151cf1f67aed4"></a>

### `PDM_DT_IO_CFG_GET`

```c
#define PDM_DT_IO_CFG_GET ( node_id)
```

```c
#include <zephyr/audio/dmic.h>
```

展开值（Value）：

```c
{                                                                       \
        .min_pdm_clk_freq = DT_PROP(node_id, clk_frequency_min),        \
        .max_pdm_clk_freq = DT_PROP(node_id, clk_frequency_max),        \
        .min_pdm_clk_dc = DT_PROP(node_id, clk_duty_cycle_min),         \
        .max_pdm_clk_dc = DT_PROP(node_id, clk_duty_cycle_max),         \
}
```

根据设备树描述（Devicetree Description）构造 `pdm_io_cfg`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 包含 pdm-dmic 的设备树节点（Devicetree Node）。 |

<a id="gac99a4f579b6aa45bb6cce1f797247a23"></a>

### `dmic_state`

```c
enum dmic_state
```

```c
#include <zephyr/audio/dmic.h>
```

数字麦克风（DMIC）驱动状态（Driver States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DMIC_STATE_UNINIT` | 未初始化（Uninitialized）。 |
| `DMIC_STATE_INITIALIZED` | 已初始化（Initialized）。 |
| `DMIC_STATE_CONFIGURED` | 已配置（Configured）。 |
| `DMIC_STATE_ACTIVE` | 活动（Active）。 |
| `DMIC_STATE_PAUSED` | 已暂停（Paused）。 |
| `DMIC_STATE_ERROR` | 错误（Error）。 |

<a id="ga24aae0a7871b3bd31b130061feeefc14"></a>

### `dmic_trigger`

```c
enum dmic_trigger
```

```c
#include <zephyr/audio/dmic.h>
```

数字麦克风（DMIC）驱动触发命令（Trigger Commands）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DMIC_TRIGGER_STOP` | 停止流（Stop Stream）。 |
| `DMIC_TRIGGER_START` | 启动流（Start Stream）。 |
| `DMIC_TRIGGER_PAUSE` | 暂停流（Pause Stream）。 |
| `DMIC_TRIGGER_RELEASE` | 恢复已暂停的流（Release Paused Stream）。 |
| `DMIC_TRIGGER_RESET` | 重置流（Reset Stream）。 |

<a id="ga7c2067bbb1e07fa8afe315f91a127991"></a>

### `pdm_lr`

```c
enum pdm_lr
```

```c
#include <zephyr/audio/dmic.h>
```

脉冲密度调制（PDM）左／右通道（LEFT/RIGHT Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PDM_CHAN_LEFT` | 左通道（Left Channel）。 |
| `PDM_CHAN_RIGHT` | 右通道（Right Channel）。 |

<a id="ga5d1fcefaf085962d779b8082b3480cbd"></a>

### `dmic_build_channel_map()`

```c
uint32_t dmic_build_channel_map ( uint8_t channel, uint8_t pdm, enum pdm_lr lr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/dmic.h>
```

构造通道映射（Channel Map），用于填充 `struct pdm_chan_cfg`。

返回 PDM 控制器与左／右通道（LEFT/RIGHT Channel）的映射，按输入逻辑通道值对应的位位置移位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel` | 逻辑通道编号（Logical Channel Number） |
| `pdm` | PDM 硬件控制器编号（Hardware Controller Number） |
| `lr` | 所选 PDM 硬件控制器内的左／右通道（LEFT/RIGHT Channel） |

**返回（Returns）**：返回值（Returns）：包含 PDM 及左／右通道信息的位图（Bit-map）。

<a id="gaf5abf489fe6ed18c2daea5d918aa2f80"></a>

### `dmic_build_clk_skew_map()`

```c
uint32_t dmic_build_clk_skew_map ( uint8_t pdm, uint8_t skew )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/dmic.h>
```

构造位图（Bit Map），记录各 PDM 通道的时钟偏斜值（Clock Skew Values）。

返回时钟偏移值（Clock Skew）的位图，按输入 PDM 控制器值对应的位位置移位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pdm` | PDM 硬件控制器编号（Hardware Controller Number） |
| `skew` | 要施加到 PDM 控制器时钟输出的偏移（Skew） |

**返回（Returns）**：返回值（Returns）：包含时钟偏移信息的位图（Bit-map）。

<a id="ga09fc7074323c2f3115b06c5212d21fc7"></a>

### `dmic_configure()`

```c
int dmic_configure ( const struct device * dev, struct dmic_cfg * cfg )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/dmic.h>
```

配置 DMIC 驱动和控制器（Driver and Controllers）。

根据通道数量、通道映射（Channel Mapping）、PDM I/O 配置、PCM 流配置等，配置数字麦克风（DMIC）驱动设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 DMIC 驱动实例的设备结构体的指针 |
| `cfg` | 指向包含 DMIC 配置的结构体的指针 |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负错误码。

<a id="gaa1fded235751a71632965011a62ddead"></a>

### `dmic_parse_channel_map()`

```c
void dmic_parse_channel_map ( uint32_t channel_map_lo, uint32_t channel_map_hi, uint8_t channel, uint8_t * pdm, enum pdm_lr * lr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/dmic.h>
```

解析 `pdm_chan_cfg` 中通道映射（Channel Map）的辅助函数。

根据输入的通道映射（Channel Map）与逻辑通道，返回对应的 PDM 控制器和左／右通道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channel_map_lo` | 通道映射的低有效位（Lower Significant Bits） |
| `channel_map_hi` | 通道映射的高有效位（Higher Significant Bits） |
| `channel` | 逻辑通道编号（Logical Channel Number） |
| `pdm` | 指向 PDM 硬件控制器编号的指针 |
| `lr` | 指向 PDM 控制器内左／右通道的指针 |

<a id="ga74b51bddaa175c518d45211f936d08e6"></a>

### `dmic_read()`

```c
int dmic_read ( const struct device * dev, uint8_t stream, void ** buffer, size_t * size, int32_t timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/dmic.h>
```

读取接收并抽取后的 PCM 数据流（Decimated PCM Data Stream）。

可选择等待接收到音频，并提供所请求流的接收音频缓冲区（Audio Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 DMIC 驱动实例的设备结构体的指针 |
| `stream` | 流标识符（Stream Identifier） |
| `buffer` | 指向接收缓冲区地址的指针 |
| `size` | 指向接收缓冲区大小的指针 |
| `timeout` | 尚未收到音频时的等待超时（Timeout），单位为毫秒；或使用 SYS_FOREVER_MS。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负错误码。

<a id="ga051e82f30b76f0fca789ba0147054184"></a>

### `dmic_trigger()`

```c
int dmic_trigger ( const struct device * dev, enum dmic_trigger cmd )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/audio/dmic.h>
```

向 DMIC 驱动发送命令（Command）。

向驱动发送命令，执行特定操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 DMIC 驱动实例的设备结构体的指针 |
| `cmd` | 要发送给驱动实例的命令（Command） |

**返回（Returns）**：返回值（Returns）：成功返回 0，失败返回负错误码。


## 1.8\_原页交叉引用（Cross References）

- [数字麦克风驱动后端 API（Digital Microphone Driver Backend API）](../api_device_topic_reference/P002_数字麦克风驱动后端 API（Digital Microphone Driver Backend API）.md)
- [dmic.h](../api_file_protocol_service_reference/P010_zephyr__audio__dmic.h_文件参考.md)
- [pdm_io_cfg](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md)
- [pcm_stream_cfg](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md)
- [pdm_chan_cfg](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md)
- [dmic_cfg](../audio_video_model_reference/P006_dmic_cfg_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [device](../device_reference/P002_设备对象结构.md)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [SYS_FOREVER_MS](../timeutil_reference/P007_时间单位辅助接口.md#ga9f9c4c41f62c7578a30209475201efed)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggac99a4f579b6aa45bb6cce1f797247a23a45b37076808ed30994ed02ca0581b1be"></a>
<a id="ggac99a4f579b6aa45bb6cce1f797247a23a733caa2b8a49d4b2f78698b810cbdbc1"></a>
<a id="ggac99a4f579b6aa45bb6cce1f797247a23a70d47513a9c0ff07cdf4d814ac78a826"></a>
<a id="ggac99a4f579b6aa45bb6cce1f797247a23ae3f1d62885d522598ced88089f4ae8b4"></a>
<a id="ggac99a4f579b6aa45bb6cce1f797247a23a14306a41b9a832343c8b6e1fcb971c81"></a>
<a id="ggac99a4f579b6aa45bb6cce1f797247a23a8b6622df75d7c4205c11db2f26619eba"></a>
<a id="gga24aae0a7871b3bd31b130061feeefc14ab3f5cdba100516563098e659adee2e23"></a>
<a id="gga24aae0a7871b3bd31b130061feeefc14a031d6c7646642d4858a22c853d6d6eaa"></a>
<a id="gga24aae0a7871b3bd31b130061feeefc14a6077bf984fd654947ff36e1bc66e98e5"></a>
<a id="gga24aae0a7871b3bd31b130061feeefc14a69b5be548e54589e03645baf2ab80804"></a>
<a id="gga24aae0a7871b3bd31b130061feeefc14aa6dca65941d65845383209c081173a79"></a>
<a id="gga7c2067bbb1e07fa8afe315f91a127991acca80c04de225e35ae2bdfafcca6e345"></a>
<a id="gga7c2067bbb1e07fa8afe315f91a127991a0c746475a2b5873aa863058358d8e7d0"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_属性协议（Attribute Protocol，ATT）.md)
