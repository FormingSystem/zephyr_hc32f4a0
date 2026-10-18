---
id: learning.zephyr-docs.api-power-policy-topic-reference.page-12
title: 视频类型（Video Types）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_视频类型（Video Types）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频类型定义。

<a id="details"></a>

视频类型定义（Video Type Definitions）。**引入版本（Since）：**4.4。**版本（Version）：**0.0.1。

<a id="header-files"></a>
<a id="files"></a>

## 12.1\_文件（Files）

<a id="r_types_2Eh"></a>

```c
file types.h
```

相关声明：[types.h](../api_file_interface_reference/P022_zephyr__video__types.h_文件参考.md)。

视频驱动与子系统共同使用的类型。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.2\_数据结构（Data Structures）

<a id="r_video_5Fbuffer"></a>

```c
struct video_buffer
```

相关声明：[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)。

视频缓冲区（Video Buffer）结构。

<a id="r_video_5Fformat"></a>

```c
struct video_format
```

相关声明：[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

视频格式（Video Format）结构。

<a id="r_video_5Fformat_5Fcap"></a>

```c
struct video_format_cap
```

相关声明：[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)。

视频格式能力（Video Format Capability）。

<a id="r_video_5Fcaps"></a>

```c
struct video_caps
```

相关声明：[video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)。

视频格式能力（Video Format Capabilities）。

<a id="r_video_5Fctrl_5Frange"></a>

```c
struct video_ctrl_range
```

相关声明：[video_ctrl_range](../audio_video_model_reference/P056_video_ctrl_range_结构体.md)。

视频控制范围（Video Control Range）结构。

<a id="r_video_5Fcontrol"></a>

```c
struct video_control
```

相关声明：[video_control](../audio_video_model_reference/P053_video_control_结构体.md)。

视频控制（Video Control）结构。

<a id="r_video_5Fctrl_5Fquery"></a>

```c
struct video_ctrl_query
```

相关声明：[video_ctrl_query](../audio_video_model_reference/P055_video_ctrl_query_结构体.md)。

视频控制查询（Video Control Query）结构。

<a id="r_video_5Frect"></a>

```c
struct video_rect
```

相关声明：[video_rect](../audio_video_model_reference/P064_video_rect_结构体.md)。

矩形区域（Rectangle Area）的描述。

<a id="r_video_5Fselection"></a>

```c
struct video_selection
```

相关声明：[video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)。

视频选择（裁剪/合成，Crop / Compose）结构。

<a id="r_video_5Ffrmival"></a>

```c
struct video_frmival
```

相关声明：[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

视频帧间隔（Video Frame Interval）结构。

<a id="r_video_5Ffrmival_5Fstepwise"></a>

```c
struct video_frmival_stepwise
```

相关声明：[video_frmival_stepwise](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md)。

视频帧间隔步进（Video Frame Interval Stepwise）结构。

<a id="r_video_5Ffrmival_5Fenum"></a>

```c
struct video_frmival_enum
```

相关声明：[video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)。

视频帧间隔枚举（Video Frame Interval Enumeration）结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.3\_枚举（Enumerations）

<a id="r_gad386b2994b56844ebe713f156b9dfe4e"></a>

```c
enum video_buf_type { VIDEO_BUF_TYPE_INPUT = 1 , VIDEO_BUF_TYPE_OUTPUT = 2 }
```

相关声明：[video_buf_type](#gad386b2994b56844ebe713f156b9dfe4e)、[VIDEO_BUF_TYPE_INPUT](#ggad386b2994b56844ebe713f156b9dfe4ea20b003de365a7e2c32bba889ae78a3a1)、[VIDEO_BUF_TYPE_OUTPUT](#ggad386b2994b56844ebe713f156b9dfe4eab51085ffb7e0d7a003dcb6b55a093083)。

`video_buf_type` 枚举。

<a id="r_ga43aa9bdc7283175df8165332a29c3f6c"></a>

```c
enum video_buf_memory { VIDEO_MEMORY_INTERNAL = 1 , VIDEO_MEMORY_EXTERNAL = 2 }
```

相关声明：[video_buf_memory](#ga43aa9bdc7283175df8165332a29c3f6c)、[VIDEO_MEMORY_INTERNAL](#gga43aa9bdc7283175df8165332a29c3f6cac00864424ada665a3c88d7fa0c1800c3)、[VIDEO_MEMORY_EXTERNAL](#gga43aa9bdc7283175df8165332a29c3f6caf2c2b2b000bd4685a429e5ff2c169425)。

`video_buf_memory` 枚举。

<a id="r_ga0f50f287c4075e992fbab6d8a990d7a8"></a>

```c
enum video_signal_result { VIDEO_BUF_DONE , VIDEO_BUF_ABORTED , VIDEO_BUF_ERROR }
```

相关声明：[video_signal_result](#ga0f50f287c4075e992fbab6d8a990d7a8)、[VIDEO_BUF_DONE](#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8)、[VIDEO_BUF_ABORTED](#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8)、[VIDEO_BUF_ERROR](#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3)。

视频信号结果（Video signal result）。

<a id="r_gae375c0586e3505632cc69348935c9b54"></a>

```c
enum video_selection_target { VIDEO_SEL_TGT_CROP , VIDEO_SEL_TGT_CROP_BOUND , VIDEO_SEL_TGT_NATIVE_SIZE , VIDEO_SEL_TGT_COMPOSE , VIDEO_SEL_TGT_COMPOSE_BOUND }
```

相关声明：[video_selection_target](#gae375c0586e3505632cc69348935c9b54)、[VIDEO_SEL_TGT_CROP](#ggae375c0586e3505632cc69348935c9b54aa42c3de3eeefb5340a2a1877ec8c4b17)、[VIDEO_SEL_TGT_CROP_BOUND](#ggae375c0586e3505632cc69348935c9b54ab1b1302e553daefb9c1017e0bed9d8f1)、[VIDEO_SEL_TGT_NATIVE_SIZE](#ggae375c0586e3505632cc69348935c9b54a7536f3626e44f03775f09a1813ec8b20)、[VIDEO_SEL_TGT_COMPOSE](#ggae375c0586e3505632cc69348935c9b54a0558ad68bff086cd3ff3f82b53946f49)、[VIDEO_SEL_TGT_COMPOSE_BOUND](#ggae375c0586e3505632cc69348935c9b54a038df16bad455f389f5c24fc91c8bd4f)。

视频选择目标（Video selection target）。

<a id="r_ga6abf1fc9c35cf1d1648cde7616e7cad1"></a>

```c
enum video_frmival_type { VIDEO_FRMIVAL_TYPE_DISCRETE = 1 , VIDEO_FRMIVAL_TYPE_STEPWISE = 2 }
```

相关声明：[video_frmival_type](#ga6abf1fc9c35cf1d1648cde7616e7cad1)、[VIDEO_FRMIVAL_TYPE_DISCRETE](#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4)、[VIDEO_FRMIVAL_TYPE_STEPWISE](#gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b)。

视频设备支持的帧间隔类型（frame interval type）。

## 12.4\_详细说明（Detailed Documentation）

<a id="ga43aa9bdc7283175df8165332a29c3f6c"></a>

### `video_buf_memory`

```c
enum video_buf_memory
```

```c
#include <zephyr/video/types.h>
```

`video_buf_memory` 枚举。

缓冲区内存类型（Buffer Memory Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VIDEO_MEMORY_INTERNAL` | 缓冲区从内部视频堆（Internal Video Heap）分配。 |
| `VIDEO_MEMORY_EXTERNAL` | 缓冲区从外部（Outside）分配。 |

<a id="gad386b2994b56844ebe713f156b9dfe4e"></a>

### `video_buf_type`

```c
enum video_buf_type
```

```c
#include <zephyr/video/types.h>
```

`video_buf_type` 枚举。

视频设备支持的视频缓冲区类型（Video Buffer Types）。输入／输出方向以设备视角定义：摄像头等设备只支持输出类型，编码器只支持输入类型，而 ISP、PxP 等内存到内存（M2M）设备同时支持输入与输出类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VIDEO_BUF_TYPE_INPUT` | 输入缓冲区类型（Input Buffer Type）。 |
| `VIDEO_BUF_TYPE_OUTPUT` | 输出缓冲区类型（Output Buffer Type）。 |

<a id="ga6abf1fc9c35cf1d1648cde7616e7cad1"></a>

### `video_frmival_type`

```c
enum video_frmival_type
```

```c
#include <zephyr/video/types.h>
```

视频设备支持的帧间隔类型（frame interval type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VIDEO_FRMIVAL_TYPE_DISCRETE` | 离散帧间隔类型（Discrete Frame Interval Type）。 |
| `VIDEO_FRMIVAL_TYPE_STEPWISE` | 步进帧间隔类型（Stepwise Frame Interval Type）。 |

<a id="gae375c0586e3505632cc69348935c9b54"></a>

### `video_selection_target`

```c
enum video_selection_target
```

```c
#include <zephyr/video/types.h>
```

视频选择目标（Video selection target）。

指示要查询或设置视频设备的哪一项选择（Selection）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VIDEO_SEL_TGT_CROP` | 当前裁剪设置（Crop Setting）。 |
| `VIDEO_SEL_TGT_CROP_BOUND` | 裁剪边界（Crop Bound），即能够实现的最大裁剪范围。 |
| `VIDEO_SEL_TGT_NATIVE_SIZE` | 输入帧的原生尺寸（Native Size）。 |
| `VIDEO_SEL_TGT_COMPOSE` | 当前合成设置（Compose Setting）。 |
| `VIDEO_SEL_TGT_COMPOSE_BOUND` | 合成边界（Compose Bound），即能够实现的最大合成范围。 |

<a id="ga0f50f287c4075e992fbab6d8a990d7a8"></a>

### `video_signal_result`

```c
enum video_signal_result
```

```c
#include <zephyr/video/types.h>
```

视频信号结果（Video signal result）。

标识视频事件（Video Event）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VIDEO_BUF_DONE` | 缓冲区已完成（Buffer Done）。 |
| `VIDEO_BUF_ABORTED` | 缓冲区已中止（Buffer Aborted）。 |
| `VIDEO_BUF_ERROR` | 缓冲区出错（Buffer in Error）。 |


## 12.5\_原页交叉引用（Cross References）

- [types.h](../api_file_interface_reference/P022_zephyr__video__types.h_文件参考.md)
- [video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)
- [video_format](../audio_video_model_reference/P059_video_format_结构体.md)
- [video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)
- [video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)
- [video_ctrl_range](../audio_video_model_reference/P056_video_ctrl_range_结构体.md)
- [video_control](../audio_video_model_reference/P053_video_control_结构体.md)
- [video_ctrl_query](../audio_video_model_reference/P055_video_ctrl_query_结构体.md)
- [video_rect](../audio_video_model_reference/P064_video_rect_结构体.md)
- [video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)
- [video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)
- [video_frmival_stepwise](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md)
- [video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga43aa9bdc7283175df8165332a29c3f6cac00864424ada665a3c88d7fa0c1800c3"></a>
<a id="gga43aa9bdc7283175df8165332a29c3f6caf2c2b2b000bd4685a429e5ff2c169425"></a>
<a id="ggad386b2994b56844ebe713f156b9dfe4ea20b003de365a7e2c32bba889ae78a3a1"></a>
<a id="ggad386b2994b56844ebe713f156b9dfe4eab51085ffb7e0d7a003dcb6b55a093083"></a>
<a id="gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4"></a>
<a id="gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b"></a>
<a id="ggae375c0586e3505632cc69348935c9b54aa42c3de3eeefb5340a2a1877ec8c4b17"></a>
<a id="ggae375c0586e3505632cc69348935c9b54ab1b1302e553daefb9c1017e0bed9d8f1"></a>
<a id="ggae375c0586e3505632cc69348935c9b54a7536f3626e44f03775f09a1813ec8b20"></a>
<a id="ggae375c0586e3505632cc69348935c9b54a0558ad68bff086cd3ff3f82b53946f49"></a>
<a id="ggae375c0586e3505632cc69348935c9b54a038df16bad455f389f5c24fc91c8bd4f"></a>
<a id="gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8"></a>
<a id="gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8"></a>
<a id="gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3"></a>

---

[上一章](P011_TEE 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P013_1-Wire 数据链路层（Data link layer）.md)
