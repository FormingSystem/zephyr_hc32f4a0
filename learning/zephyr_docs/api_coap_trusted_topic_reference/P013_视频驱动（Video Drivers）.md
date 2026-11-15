---
id: learning.zephyr-docs.api-coap-trusted-topic-reference.page-13
title: 视频驱动（Video Drivers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_视频驱动（Video Drivers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

供视频子系统使用的视频驱动 API。

<a id="details"></a>

视频驱动 API（Video Driver APIs），供视频子系统（Video Subsystem）使用。自 2.1 起提供（Since 2.1），版本（Version）1.3.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 13.1\_主题（Topics）

<a id="r_video_5Finterface_5Fctrls"></a>

相关声明：[视频控制项（Video Controls）](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md)。

访问驱动程序视频控制项时使用的类型。

<a id="r_video_5Finterface_5Fbackend"></a>

相关声明：[视频驱动后端 API](../api_video_event_topic_reference/P011_视频驱动后端 API.md)。

<a id="r_video_5Finterface_5Fbus_5Ftypes"></a>

相关声明：[视频接口总线类型（Video interface bus types）](../api_device_topic_reference/P024_视频接口总线类型（Video interface bus types）.md)。

设备树 `bus-type` 属性使用的总线类型值。

<a id="header-files"></a>
<a id="files"></a>

## 13.2\_文件（Files）

<a id="r_video_2Eh"></a>

```c
file video.h
```

相关声明：[video.h](../api_file_display_chat_reference/P009_zephyr__drivers__video.h_文件参考.md)。

视频（Video）驱动API的主头文件。

<a id="r_arducam_5Fmega_2Eh"></a>

```c
file arducam_mega.h
```

相关声明：[arducam_mega.h](../api_file_runtime_reference/P002_zephyr__drivers__video__arducam_mega.h_文件参考.md)。

Copyright (c) 2023 Arducam Technology Co., Ltd.

<a id="r_stm32_5Fdcmi_2Eh"></a>

```c
file stm32_dcmi.h
```

相关声明：[stm32_dcmi.h](../api_file_supplement_reference/P120_zephyr__drivers__video__stm32_dcmi.h_文件参考.md)。

STM32数字摄像头接口（DCMI）的专用控制项。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.3\_数据结构（Data Structures）

<a id="r_video_5Fdevice"></a>

```c
struct video_device
```

相关声明：[video_device](../audio_video_model_reference/P057_video_device_结构体.md)。

视频设备封装类型（Wrapper Type）的存储类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.4\_函数（Functions）

<a id="r_ga3d31ffde89ef76e72855ded34c6deb3c"></a>

```c
struct video_device * video_find_vdev (const struct device *dev)
```

相关声明：[video_device](../audio_video_model_reference/P057_video_device_结构体.md)、[video_find_vdev](#ga3d31ffde89ef76e72855ded34c6deb3c)、[device](../device_reference/P002_设备对象结构.md)。

查找与视频设备（Video Device）关联的 video_device。

<a id="r_ga9a29705addc34c59eb6406dd37519eaf"></a>

```c
static int video_driver_set_format (const struct device *dev, struct video_format *fmt)
```

相关声明：[video_driver_set_format](#ga9a29705addc34c59eb6406dd37519eaf)、[device](../device_reference/P002_设备对象结构.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

设置驱动的视频格式（Video Format）。

<a id="r_gabd3ca5bdb2915a78fd12182fde435c30"></a>

```c
static int video_driver_get_format (const struct device *dev, struct video_format *fmt)
```

相关声明：[video_driver_get_format](#gabd3ca5bdb2915a78fd12182fde435c30)、[device](../device_reference/P002_设备对象结构.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

获取驱动的视频格式（Video Format）。

<a id="r_ga57016218645ba4d98bab320545b80f1c"></a>

```c
static int video_driver_set_frmival (const struct device *dev, struct video_frmival *frmival)
```

相关声明：[video_driver_set_frmival](#ga57016218645ba4d98bab320545b80f1c)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

向驱动应用视频帧间隔（Video Frame Interval）。

<a id="r_ga4eb2460636e70ddfa1b6f5187d882bfe"></a>

```c
static int video_driver_get_frmival (const struct device *dev, struct video_frmival *frmival)
```

相关声明：[video_driver_get_frmival](#ga4eb2460636e70ddfa1b6f5187d882bfe)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

获取驱动的视频帧间隔（Video Frame Interval）。

<a id="r_ga26d096ae93185ed1157a75d429dd145d"></a>

```c
static int video_driver_enum_frmival (const struct device *dev, struct video_frmival_enum *fie)
```

相关声明：[video_driver_enum_frmival](#ga26d096ae93185ed1157a75d429dd145d)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)。

列出视频帧间隔（Video Frame Intervals）。

<a id="r_gae73ac504f2d726ab9a88bc35e0e25b09"></a>

```c
static int video_driver_enqueue (const struct device *dev, struct video_buffer *vbuf)
```

相关声明：[video_driver_enqueue](#gae73ac504f2d726ab9a88bc35e0e25b09)、[device](../device_reference/P002_设备对象结构.md)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)。

向驱动传递视频缓冲区（Video Buffer）。

<a id="r_gaaf4610cbab1caaf95070b7366cb4c4c6"></a>

```c
static int video_driver_dequeue (const struct device *dev, struct video_buffer **vbuf, k_timeout_t timeout)
```

相关声明：[video_driver_dequeue](#gaaf4610cbab1caaf95070b7366cb4c4c6)、[device](../device_reference/P002_设备对象结构.md)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从驱动取出队列中的视频缓冲区（Dequeue a Video Buffer）。

<a id="r_ga8ddced08604291df2eec55aadc3c217c"></a>

```c
static int video_driver_flush (const struct device *dev, bool cancel)
```

相关声明：[video_driver_flush](#ga8ddced08604291df2eec55aadc3c217c)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

刷新驱动的端点缓冲区（Flush Endpoint Buffers）。

<a id="r_ga8c19eb99330402975f6e6630e1b91436"></a>

```c
static int video_driver_set_stream (const struct device *dev, bool enable, enum video_buf_type type)
```

相关声明：[video_driver_set_stream](#ga8c19eb99330402975f6e6630e1b91436)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)。

启动或停止视频驱动功能（Video Driver Function）。

<a id="r_ga15d602806f0c30a1c28bcba7cf1fe82a"></a>

```c
static int video_driver_get_volatile_ctrl (const struct device *dev, uint32_t cid)
```

相关声明：[video_driver_get_volatile_ctrl](#ga15d602806f0c30a1c28bcba7cf1fe82a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取驱动的视频控件易变值（Volatile Video Control Value）。

<a id="r_ga211f219e42890a6788b448c1c23fcd84"></a>

```c
static int video_driver_set_ctrl (const struct device *dev, uint32_t cid)
```

相关声明：[video_driver_set_ctrl](#ga211f219e42890a6788b448c1c23fcd84)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置驱动的视频控件值（Video Control Value）。

<a id="r_ga85a3064db275074f31494a364d17b51f"></a>

```c
static int video_driver_get_caps (const struct device *dev, struct video_caps *caps)
```

相关声明：[video_driver_get_caps](#ga85a3064db275074f31494a364d17b51f)、[device](../device_reference/P002_设备对象结构.md)、[video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)。

获取视频驱动端点的能力（Endpoint Capabilities）。

<a id="r_ga224e26d848ff68d10452dd4d2a44fba5"></a>

```c
static int video_driver_transform_cap (const struct device *const dev, const struct video_format_cap *const cap, struct video_format_cap *const res_cap, enum video_buf_type type, uint16_t ind)
```

相关声明：[video_driver_transform_cap](#ga224e26d848ff68d10452dd4d2a44fba5)、[device](../device_reference/P002_设备对象结构.md)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将视频格式能力（Video Format Capability）从内存到内存（M2M）视频设备的一端转换到另一端。

<a id="r_ga6f8b1924bf4a0ee1d7315a8e472614eb"></a>

```c
static int video_driver_set_signal (const struct device *dev, struct k_poll_signal *sig)
```

相关声明：[video_driver_set_signal](#ga6f8b1924bf4a0ee1d7315a8e472614eb)、[device](../device_reference/P002_设备对象结构.md)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

为视频端点（Video Endpoint）注册／注销 `k_poll` 信号。

<a id="r_gafc494071abdfb4c38dff515bda316379"></a>

```c
static int video_driver_set_selection (const struct device *dev, struct video_selection *sel)
```

相关声明：[video_driver_set_selection](#gafc494071abdfb4c38dff515bda316379)、[device](../device_reference/P002_设备对象结构.md)、[video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)。

设置视频选区（Video Selection），即裁剪／合成（Crop/Compose）。

<a id="r_ga2037f560bb9a7a83d6cb23787d7bf167"></a>

```c
static int video_driver_get_selection (const struct device *dev, struct video_selection *sel)
```

相关声明：[video_driver_get_selection](#ga2037f560bb9a7a83d6cb23787d7bf167)、[device](../device_reference/P002_设备对象结构.md)、[video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)。

获取视频选区（Video Selection），即裁剪／合成（Crop/Compose）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 13.5\_MIPI CSI-2 数据类型（Data Types）

用于相机传感器接口的标准 MIPI CSI-2 数据类型标识符（Data Type Identifiers）。

这些常量定义 MIPI CSI-2 数据包头中数据类型字段（Data Type Field）的值，用于标识所传输图像数据的格式和编码。数据类型字段宽度为 6 位，允许的值为 0x00 至 0x3F。

<a id="r_gac50ea4ef6af09f0a6f72315db2ccd2d9"></a>

```c
static uint8_t video_mipi_data_type (uint32_t pixfmt)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[video_mipi_data_type](#gac50ea4ef6af09f0a6f72315db2ccd2d9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将像素格式（Pixel Formats）映射为对应的 MIPI 数据类型（Data Type）。

<a id="r_ga59d6f35198b6412a9aa78c094ecfaa19"></a>

```c
#define VIDEO_MIPI_CSI2_DT_NULL 0x10
```

相关声明：[VIDEO_MIPI_CSI2_DT_NULL](#ga59d6f35198b6412a9aa78c094ecfaa19)。

NULL 数据类型：用于填充（Padding）或同步（Synchronization）。

<a id="r_gaede52c3391311b7cf931665afdeed720"></a>

```c
#define VIDEO_MIPI_CSI2_DT_BLANKING 0x11
```

相关声明：[VIDEO_MIPI_CSI2_DT_BLANKING](#gaede52c3391311b7cf931665afdeed720)。

消隐数据（Blanking Data）：水平／垂直消隐信息。

<a id="r_ga2b16d411ffcbcc7e74fa6aa2966b4b0d"></a>

```c
#define VIDEO_MIPI_CSI2_DT_EMBEDDED_8 0x12
```

相关声明：[VIDEO_MIPI_CSI2_DT_EMBEDDED_8](#ga2b16d411ffcbcc7e74fa6aa2966b4b0d)。

嵌入式 8 位数据（Embedded 8-bit Data）：传感器元数据或配置数据。

<a id="r_gab8001106ce7c91573012a895a4b3f1a8"></a>

```c
#define VIDEO_MIPI_CSI2_DT_YUV420_8 0x18
```

相关声明：[VIDEO_MIPI_CSI2_DT_YUV420_8](#gab8001106ce7c91573012a895a4b3f1a8)。

YUV 4:2:0 格式，每分量（Component）8 位。

<a id="r_ga65dac1b59e00cb26e9af9e39663b20f0"></a>

```c
#define VIDEO_MIPI_CSI2_DT_YUV420_10 0x19
```

相关声明：[VIDEO_MIPI_CSI2_DT_YUV420_10](#ga65dac1b59e00cb26e9af9e39663b20f0)。

YUV 4:2:0 格式，每分量（Component）10 位。

<a id="r_ga9c40ffb7a4042dd9d149e960eeddd14e"></a>

```c
#define VIDEO_MIPI_CSI2_DT_YUV420_CSPS_8 0x1c
```

相关声明：[VIDEO_MIPI_CSI2_DT_YUV420_CSPS_8](#ga9c40ffb7a4042dd9d149e960eeddd14e)。

YUV 4:2:0 色度移位像素采样（Chroma Shifted Pixel Sampling，CSPS）8 位格式。

<a id="r_gad1d445cd3b576e4c7062f0a06f8dc71e"></a>

```c
#define VIDEO_MIPI_CSI2_DT_YUV420_CSPS_10 0x1d
```

相关声明：[VIDEO_MIPI_CSI2_DT_YUV420_CSPS_10](#gad1d445cd3b576e4c7062f0a06f8dc71e)。

YUV 4:2:0 色度移位像素采样（Chroma Shifted Pixel Sampling，CSPS）10 位格式。

<a id="r_ga18dac33c3f8afd80e08d69ed78aee5a9"></a>

```c
#define VIDEO_MIPI_CSI2_DT_YUV422_8 0x1e
```

相关声明：[VIDEO_MIPI_CSI2_DT_YUV422_8](#ga18dac33c3f8afd80e08d69ed78aee5a9)。

YUV 4:2:2 格式，每分量（Component）8 位。

<a id="r_ga4b530659596536d30168161139cc46fb"></a>

```c
#define VIDEO_MIPI_CSI2_DT_YUV422_10 0x1f
```

相关声明：[VIDEO_MIPI_CSI2_DT_YUV422_10](#ga4b530659596536d30168161139cc46fb)。

YUV 4:2:2 格式，每分量（Component）10 位。

<a id="r_ga04efc97a4dab0af7c7266ab104b8d626"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RGB444 0x20
```

相关声明：[VIDEO_MIPI_CSI2_DT_RGB444](#ga04efc97a4dab0af7c7266ab104b8d626)。

RGB 格式，每颜色分量（Color Component）4 位。

<a id="r_ga351c2045810bb786d8232162f47fee7d"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RGB555 0x21
```

相关声明：[VIDEO_MIPI_CSI2_DT_RGB555](#ga351c2045810bb786d8232162f47fee7d)。

RGB 格式，每颜色分量（Color Component）5 位。

<a id="r_gad5f04e5dd3d5e0c5f67c64e28cd91c56"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RGB565 0x22
```

相关声明：[VIDEO_MIPI_CSI2_DT_RGB565](#gad5f04e5dd3d5e0c5f67c64e28cd91c56)。

RGB 格式，R、G、B 分量依次为 5、6、5 位。

<a id="r_gaa452375e0454fa314eb140bac3c07e67"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RGB666 0x23
```

相关声明：[VIDEO_MIPI_CSI2_DT_RGB666](#gaa452375e0454fa314eb140bac3c07e67)。

RGB 格式，每颜色分量（Color Component）6 位。

<a id="r_ga0d637375f7bf081967135139a8f6c5b6"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RGB888 0x24
```

相关声明：[VIDEO_MIPI_CSI2_DT_RGB888](#ga0d637375f7bf081967135139a8f6c5b6)。

RGB 格式，每颜色分量（Color Component）8 位。

<a id="r_gad251376f21a56d05742fcb68d228a677"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RAW6 0x28
```

相关声明：[VIDEO_MIPI_CSI2_DT_RAW6](#gad251376f21a56d05742fcb68d228a677)。

传感器原始数据（Raw Sensor Data），每像素 6 位。

<a id="r_ga384e8203e1bb7208a4bcb1e4931a929b"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RAW7 0x29
```

相关声明：[VIDEO_MIPI_CSI2_DT_RAW7](#ga384e8203e1bb7208a4bcb1e4931a929b)。

传感器原始数据（Raw Sensor Data），每像素 7 位。

<a id="r_ga6d3881edac75ba2c12185dc119311945"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RAW8 0x2a
```

相关声明：[VIDEO_MIPI_CSI2_DT_RAW8](#ga6d3881edac75ba2c12185dc119311945)。

传感器原始数据（Raw Sensor Data），每像素 8 位。

<a id="r_ga64a52402a6883cb1b23a5524418528a9"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RAW10 0x2b
```

相关声明：[VIDEO_MIPI_CSI2_DT_RAW10](#ga64a52402a6883cb1b23a5524418528a9)。

传感器原始数据（Raw Sensor Data），每像素 10 位。

<a id="r_gadadb66f582b5e014336e29c1dafc3631"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RAW12 0x2c
```

相关声明：[VIDEO_MIPI_CSI2_DT_RAW12](#gadadb66f582b5e014336e29c1dafc3631)。

传感器原始数据（Raw Sensor Data），每像素 12 位。

<a id="r_ga2ad6b8870c5dca6a8d19b1f80d83b81b"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RAW14 0x2d
```

相关声明：[VIDEO_MIPI_CSI2_DT_RAW14](#ga2ad6b8870c5dca6a8d19b1f80d83b81b)。

传感器原始数据（Raw Sensor Data），每像素 14 位。

<a id="r_ga98885f3584261947dd2b325bf12b2f3d"></a>

```c
#define VIDEO_MIPI_CSI2_DT_USER(n)
```

相关声明：[VIDEO_MIPI_CSI2_DT_USER](#ga98885f3584261947dd2b325bf12b2f3d)。

生成用户自定义数据类型（User-defined Data Type）的宏。

## 13.6\_详细说明（Detailed Documentation）

<a id="gaede52c3391311b7cf931665afdeed720"></a>

### `VIDEO_MIPI_CSI2_DT_BLANKING`

```c
#define VIDEO_MIPI_CSI2_DT_BLANKING 0x11
```

```c
#include <zephyr/drivers/video.h>
```

消隐数据（Blanking Data）：水平／垂直消隐信息。

<a id="ga2b16d411ffcbcc7e74fa6aa2966b4b0d"></a>

### `VIDEO_MIPI_CSI2_DT_EMBEDDED_8`

```c
#define VIDEO_MIPI_CSI2_DT_EMBEDDED_8 0x12
```

```c
#include <zephyr/drivers/video.h>
```

嵌入式 8 位数据（Embedded 8-bit Data）：传感器元数据或配置数据。

<a id="ga59d6f35198b6412a9aa78c094ecfaa19"></a>

### `VIDEO_MIPI_CSI2_DT_NULL`

```c
#define VIDEO_MIPI_CSI2_DT_NULL 0x10
```

```c
#include <zephyr/drivers/video.h>
```

NULL 数据类型：用于填充（Padding）或同步（Synchronization）。

<a id="ga64a52402a6883cb1b23a5524418528a9"></a>

### `VIDEO_MIPI_CSI2_DT_RAW10`

```c
#define VIDEO_MIPI_CSI2_DT_RAW10 0x2b
```

```c
#include <zephyr/drivers/video.h>
```

传感器原始数据（Raw Sensor Data），每像素 10 位。

<a id="gadadb66f582b5e014336e29c1dafc3631"></a>

### `VIDEO_MIPI_CSI2_DT_RAW12`

```c
#define VIDEO_MIPI_CSI2_DT_RAW12 0x2c
```

```c
#include <zephyr/drivers/video.h>
```

传感器原始数据（Raw Sensor Data），每像素 12 位。

<a id="ga2ad6b8870c5dca6a8d19b1f80d83b81b"></a>

### `VIDEO_MIPI_CSI2_DT_RAW14`

```c
#define VIDEO_MIPI_CSI2_DT_RAW14 0x2d
```

```c
#include <zephyr/drivers/video.h>
```

传感器原始数据（Raw Sensor Data），每像素 14 位。

<a id="gad251376f21a56d05742fcb68d228a677"></a>

### `VIDEO_MIPI_CSI2_DT_RAW6`

```c
#define VIDEO_MIPI_CSI2_DT_RAW6 0x28
```

```c
#include <zephyr/drivers/video.h>
```

传感器原始数据（Raw Sensor Data），每像素 6 位。

<a id="ga384e8203e1bb7208a4bcb1e4931a929b"></a>

### `VIDEO_MIPI_CSI2_DT_RAW7`

```c
#define VIDEO_MIPI_CSI2_DT_RAW7 0x29
```

```c
#include <zephyr/drivers/video.h>
```

传感器原始数据（Raw Sensor Data），每像素 7 位。

<a id="ga6d3881edac75ba2c12185dc119311945"></a>

### `VIDEO_MIPI_CSI2_DT_RAW8`

```c
#define VIDEO_MIPI_CSI2_DT_RAW8 0x2a
```

```c
#include <zephyr/drivers/video.h>
```

传感器原始数据（Raw Sensor Data），每像素 8 位。

<a id="ga04efc97a4dab0af7c7266ab104b8d626"></a>

### `VIDEO_MIPI_CSI2_DT_RGB444`

```c
#define VIDEO_MIPI_CSI2_DT_RGB444 0x20
```

```c
#include <zephyr/drivers/video.h>
```

RGB 格式，每颜色分量（Color Component）4 位。

<a id="ga351c2045810bb786d8232162f47fee7d"></a>

### `VIDEO_MIPI_CSI2_DT_RGB555`

```c
#define VIDEO_MIPI_CSI2_DT_RGB555 0x21
```

```c
#include <zephyr/drivers/video.h>
```

RGB 格式，每颜色分量（Color Component）5 位。

<a id="gad5f04e5dd3d5e0c5f67c64e28cd91c56"></a>

### `VIDEO_MIPI_CSI2_DT_RGB565`

```c
#define VIDEO_MIPI_CSI2_DT_RGB565 0x22
```

```c
#include <zephyr/drivers/video.h>
```

RGB 格式，R、G、B 分量依次为 5、6、5 位。

<a id="gaa452375e0454fa314eb140bac3c07e67"></a>

### `VIDEO_MIPI_CSI2_DT_RGB666`

```c
#define VIDEO_MIPI_CSI2_DT_RGB666 0x23
```

```c
#include <zephyr/drivers/video.h>
```

RGB 格式，每颜色分量（Color Component）6 位。

<a id="ga0d637375f7bf081967135139a8f6c5b6"></a>

### `VIDEO_MIPI_CSI2_DT_RGB888`

```c
#define VIDEO_MIPI_CSI2_DT_RGB888 0x24
```

```c
#include <zephyr/drivers/video.h>
```

RGB 格式，每颜色分量（Color Component）8 位。

<a id="ga98885f3584261947dd2b325bf12b2f3d"></a>

### `VIDEO_MIPI_CSI2_DT_USER`

```c
#define VIDEO_MIPI_CSI2_DT_USER ( n)
```

```c
#include <zephyr/drivers/video.h>
```

展开值（Value）：

```c
(0x30 + (n))
```

生成用户自定义数据类型（User-defined Data Type）的宏。

为自定义或专有格式生成用户自定义数据类型标识符（User-defined Data Type Identifier）。MIPI CSI-2 规范将数据类型 0x30 至 0x37 保留给用户特定实现。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `n` | 用户自定义类型索引（User-defined Type Index），范围为 0–7。 |

**说明（Note）**：注意（Note）：参数 n 必须位于 0–7 范围内，才能生成有效的用户自定义数据类型。

返回（Returns）：用户自定义范围（0x30–0x37）内的数据类型值（Data Type Value）。

<a id="ga65dac1b59e00cb26e9af9e39663b20f0"></a>

### `VIDEO_MIPI_CSI2_DT_YUV420_10`

```c
#define VIDEO_MIPI_CSI2_DT_YUV420_10 0x19
```

```c
#include <zephyr/drivers/video.h>
```

YUV 4:2:0 格式，每分量（Component）10 位。

<a id="gab8001106ce7c91573012a895a4b3f1a8"></a>

### `VIDEO_MIPI_CSI2_DT_YUV420_8`

```c
#define VIDEO_MIPI_CSI2_DT_YUV420_8 0x18
```

```c
#include <zephyr/drivers/video.h>
```

YUV 4:2:0 格式，每分量（Component）8 位。

<a id="gad1d445cd3b576e4c7062f0a06f8dc71e"></a>

### `VIDEO_MIPI_CSI2_DT_YUV420_CSPS_10`

```c
#define VIDEO_MIPI_CSI2_DT_YUV420_CSPS_10 0x1d
```

```c
#include <zephyr/drivers/video.h>
```

YUV 4:2:0 色度移位像素采样（Chroma Shifted Pixel Sampling，CSPS）10 位格式。

<a id="ga9c40ffb7a4042dd9d149e960eeddd14e"></a>

### `VIDEO_MIPI_CSI2_DT_YUV420_CSPS_8`

```c
#define VIDEO_MIPI_CSI2_DT_YUV420_CSPS_8 0x1c
```

```c
#include <zephyr/drivers/video.h>
```

YUV 4:2:0 色度移位像素采样（Chroma Shifted Pixel Sampling，CSPS）8 位格式。

<a id="ga4b530659596536d30168161139cc46fb"></a>

### `VIDEO_MIPI_CSI2_DT_YUV422_10`

```c
#define VIDEO_MIPI_CSI2_DT_YUV422_10 0x1f
```

```c
#include <zephyr/drivers/video.h>
```

YUV 4:2:2 格式，每分量（Component）10 位。

<a id="ga18dac33c3f8afd80e08d69ed78aee5a9"></a>

### `VIDEO_MIPI_CSI2_DT_YUV422_8`

```c
#define VIDEO_MIPI_CSI2_DT_YUV422_8 0x1e
```

```c
#include <zephyr/drivers/video.h>
```

YUV 4:2:2 格式，每分量（Component）8 位。

<a id="gaaf4610cbab1caaf95070b7366cb4c4c6"></a>

### `video_driver_dequeue()`

```c
int video_driver_dequeue ( const struct device * dev, struct video_buffer ** vbuf, k_timeout_t timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

从驱动取出队列中的视频缓冲区（Dequeue a Video Buffer）。

从驱动端点的输出队列（Outgoing Queue）中取出已填充（采集，Capturing）或已显示（输出，Output）的缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `vbuf` | 指向视频缓冲区指针（Video Buffer Pointer）的指针。 |
| `timeout` | 超时（Timeout） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="gae73ac504f2d726ab9a88bc35e0e25b09"></a>

### `video_driver_enqueue()`

```c
int video_driver_enqueue ( const struct device * dev, struct video_buffer * vbuf )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

向驱动传递视频缓冲区（Video Buffer）。

向驱动端点的入站队列（Incoming Queue）加入空的视频缓冲区（采集模式）或已填充的视频缓冲区（输出模式）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `vbuf` | 指向视频缓冲区（Video Buffer）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="ga26d096ae93185ed1157a75d429dd145d"></a>

### `video_driver_enum_frmival()`

```c
int video_driver_enum_frmival ( const struct device * dev, struct video_frmival_enum * fie )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

列出视频帧间隔（Video Frame Intervals）。

列出所给格式支持的全部视频帧间隔（Video Frame Intervals）。

调用者应先填写 video_frmival_enum 的 pixelformat、width 和 height 字段，构成查询条件；再使用 index 字段遍历所支持的帧间隔列表（Frame Intervals List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `fie` | 指向视频帧间隔枚举结构体（Video Frame Interval Enumeration Struct）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="ga8ddced08604291df2eec55aadc3c217c"></a>

### `video_driver_flush()`

```c
int video_driver_flush ( const struct device * dev, bool cancel )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

刷新驱动的端点缓冲区（Flush Endpoint Buffers）。

所有端点缓冲区均从输入队列（Incoming Queue）移到输出队列（Outgoing Queue）后，flush 调用才结束。移动的原因可以是处理被取消，也可以是视频功能已完成全部处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `cancel` | 为 true 时取消缓冲区处理（Cancel Buffer Processing），而不等待处理完成。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="ga85a3064db275074f31494a364d17b51f"></a>

### `video_driver_get_caps()`

```c
int video_driver_get_caps ( const struct device * dev, struct video_caps * caps )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

获取视频驱动端点的能力（Endpoint Capabilities）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `caps` | 指向待填充的 `video_caps` 结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="gabd3ca5bdb2915a78fd12182fde435c30"></a>

### `video_driver_get_format()`

```c
int video_driver_get_format ( const struct device * dev, struct video_format * fmt )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

获取驱动的视频格式（Video Format）。

获取视频设备的当前视频格式（Video Format）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `fmt` | 指向视频格式结构体（Video Format Struct）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="ga4eb2460636e70ddfa1b6f5187d882bfe"></a>

### `video_driver_get_frmival()`

```c
int video_driver_get_frmival ( const struct device * dev, struct video_frmival * frmival )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

获取驱动的视频帧间隔（Video Frame Interval）。

获取视频设备的当前帧间隔（Frame Interval）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `frmival` | 指向视频帧间隔结构体（Video Frame Interval Struct）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="ga2037f560bb9a7a83d6cb23787d7bf167"></a>

### `video_driver_get_selection()`

```c
int video_driver_get_selection ( const struct device * dev, struct video_selection * sel )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

获取视频选区（Video Selection），即裁剪／合成（Crop/Compose）。

获取视频设备当前与裁剪和合成（Crop and Compose）有关的设置。也可用于读取输入流的原生尺寸（Native Size），或在通过 `video_set_selection` API 配置前读取设备的裁剪／合成能力。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `sel` | 指向视频选区结构体（Video Selection Structure）的指针，`type` 和 `target` 由调用方设置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |
| `-ENOTSUP` | 不支持该格式（Format）。 |

<a id="ga15d602806f0c30a1c28bcba7cf1fe82a"></a>

### `video_driver_get_volatile_ctrl()`

```c
int video_driver_get_volatile_ctrl ( const struct device * dev, uint32_t cid )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

获取驱动的视频控件易变值（Volatile Video Control Value）。

向硬件请求 cid 对应的控件值（Control Value）以更新它；完成后，对应的 ctrl->val 包含更新后的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `cid` | 要设置／获取其值的控件标识符（Control ID）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="ga211f219e42890a6788b448c1c23fcd84"></a>

### `video_driver_set_ctrl()`

```c
int video_driver_set_ctrl ( const struct device * dev, uint32_t cid )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

设置驱动的视频控件值（Video Control Value）。

将 cid 对应的视频控件值（Video Control Value）应用到设备；该值取自对应的 ctrl->val。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `cid` | 要设置／获取其值的控件标识符（Control ID）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="ga9a29705addc34c59eb6406dd37519eaf"></a>

### `video_driver_set_format()`

```c
int video_driver_set_format ( const struct device * dev, struct video_format * fmt )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

设置驱动的视频格式（Video Format）。

将视频设备配置为指定格式（Format）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `fmt` | 指向视频格式结构体（Video Format Struct）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOTSUP` | 不支持该格式（Format）。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="ga57016218645ba4d98bab320545b80f1c"></a>

### `video_driver_set_frmival()`

```c
int video_driver_set_frmival ( const struct device * dev, struct video_frmival * frmival )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

向驱动应用视频帧间隔（Video Frame Interval）。

驱动不得仅因请求的帧间隔（Interval）不符合设备能力而返回错误，必须将该间隔调整为硬件能够提供的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `frmival` | 指向视频帧间隔结构体（Video Frame Interval Struct）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="gafc494071abdfb4c38dff515bda316379"></a>

### `video_driver_set_selection()`

```c
int video_driver_set_selection ( const struct device * dev, struct video_selection * sel )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

设置视频选区（Video Selection），即裁剪／合成（Crop/Compose）。

配置视频设备可选的裁剪与合成功能（Crop and Compose）。先对输入帧裁剪，再对裁剪结果执行合成。合成结果的宽／高等于传给 `video_set_format` 的格式宽／高。

某些目标（Targets）相互依赖。例如，设置 `VIDEO_SEL_TGT_CROP` 会将 `VIDEO_SEL_TGT_COMPOSE` 重置为相同大小。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `sel` | 指向视频选区结构体（Video Selection Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="ga6f8b1924bf4a0ee1d7315a8e472614eb"></a>

### `video_driver_set_signal()`

```c
int video_driver_set_signal ( const struct device * dev, struct k_poll_signal * sig )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

为视频端点（Video Endpoint）注册／注销 `k_poll` 信号。

为端点注册轮询信号（Poll Signal），帧完成时会触发信号，包括正常完成、中止及错误。注册 `NULL` 轮询信号会注销先前注册的任何信号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `sig` | 指向 `k_poll_signal` 的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="ga8c19eb99330402975f6e6630e1b91436"></a>

### `video_driver_set_stream()`

```c
int video_driver_set_stream ( const struct device * dev, bool enable, enum video_buf_type type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

启动或停止视频驱动功能（Video Driver Function）。

在视频设备上启动（enable == true）或停止（enable == false）流传输（Streaming）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `enable` | 为 true 时启动流传输（Streaming），否则停止。 |
| `type` | 要启动或停止的缓冲区流类型（Buffers Stream Type）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="ga224e26d848ff68d10452dd4d2a44fba5"></a>

### `video_driver_transform_cap()`

```c
int video_driver_transform_cap ( const struct device *const dev, const struct video_format_cap *const cap, struct video_format_cap *const res_cap, enum video_buf_type type, uint16_t ind )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

将视频格式能力（Video Format Capability）从内存到内存（M2M）视频设备的一端转换到另一端。

详细说明和用法参见 video_transform_cap。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `cap` | 指向源视频格式能力结构体（Source Video Format Capability Structure）的指针。 |
| `res_cap` | 指向结果视频格式能力结构体（Resulting Video Format Capability Structure）的指针，由驱动填充。 |
| `type` | 转换结果能力（Transformed Cap）的 `video_buf_type`。 |
| `ind` | 转换结果能力（Transformed Cap）的索引（Index）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |
| `-ENOTSUP` | 不支持该转换（Transformation）。 |

<a id="ga3d31ffde89ef76e72855ded34c6deb3c"></a>

### `video_find_vdev()`

```c
struct video_device * video_find_vdev ( const struct device * dev)
```

```c
#include <zephyr/drivers/video.h>
```

查找与视频设备（Video Device）关联的 video_device。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 将在全局视频设备列表（Global List of Video Devices）中查找的设备。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `NULL` | 未找到时。 |

返回（Returns）：找到时返回指向 video_device 的指针。

<a id="gac50ea4ef6af09f0a6f72315db2ccd2d9"></a>

### `video_mipi_data_type()`

```c
uint8_t video_mipi_data_type ( uint32_t pixfmt)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/video.h>
```

将像素格式（Pixel Formats）映射为对应的 MIPI 数据类型（Data Type）。

只有精确匹配的格式才会映射到等价的 MIPI 数据类型（Data Types）。驱动可能需要在调用此函数前自行处理非标准类型。

注意：尽管大多数接收器将 VIDEO_MIPI_CSI2_DT_YUV422_8 存储为 YUYV，但在 MIPI 数据通道（Lanes）上传输的实际格式是 UYVY。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pixfmt` | 要转换的像素格式（Pixel Format）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `the` | 找到时为匹配的 MIPI 数据类型（Data Type）。 |
| `VIDEO_MIPI_CSI2_DT_NULL` | 该格式没有已知的等价 MIPI 数据类型（Data Type）时。 |


## 13.7\_原页交叉引用（Cross References）

- [视频子系统（Video Subsystem）](../api_platform_topic_reference/P128_视频子系统（Video Subsystem）.md)
- [视频控制项（Video Controls）](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md)
- [视频驱动后端 API](../api_video_event_topic_reference/P011_视频驱动后端 API.md)
- [视频接口总线类型（Video interface bus types）](../api_device_topic_reference/P024_视频接口总线类型（Video interface bus types）.md)
- [video.h](../api_file_display_chat_reference/P009_zephyr__drivers__video.h_文件参考.md)
- [arducam_mega.h](../api_file_runtime_reference/P002_zephyr__drivers__video__arducam_mega.h_文件参考.md)
- [stm32_dcmi.h](../api_file_supplement_reference/P120_zephyr__drivers__video__stm32_dcmi.h_文件参考.md)
- [video_device](../audio_video_model_reference/P057_video_device_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [video_format](../audio_video_model_reference/P059_video_format_结构体.md)
- [video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)
- [video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)
- [video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)
- [video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [video_set_selection](../api_video_event_topic_reference/P009_视频格式（Video Format）.md#ga6ea31432d37e0f8f46e0f6c2690ee3e9)
- [video_set_format](../api_video_event_topic_reference/P009_视频格式（Video Format）.md#ga1deb2dbafd7f4eeb602a3f78aaeb5e33)
- [VIDEO_SEL_TGT_CROP](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#ggae375c0586e3505632cc69348935c9b54aa42c3de3eeefb5340a2a1877ec8c4b17)
- [VIDEO_SEL_TGT_COMPOSE](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#ggae375c0586e3505632cc69348935c9b54a0558ad68bff086cd3ff3f82b53946f49)
- [video_transform_cap](../api_lifecycle_capability_topic_reference/P026_视频能力（Video Capabilities）.md#ga3d2d1692e4adab02948b11f38407610f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_可信执行环境（TEE）.md) · [返回大纲](大纲.md) · [下一章](P014_WebSocket的API。.md)
