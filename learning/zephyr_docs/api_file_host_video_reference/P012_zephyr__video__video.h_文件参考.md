---
id: learning.zephyr-docs.api-file-host-video-reference.page-12
title: zephyr__video__video.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/video_2video_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_video\_\_video.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/video_2video_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频（Video）的公共API。

<a id="details"></a>

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/video/controls.h>
#include <zephyr/video/formats.h>
#include <zephyr/video/types.h>
```

查看此文件的源码。

视频（Video）的公共API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.1\_函数（Functions）

<a id="r_ga036c42c1e7dbaa97eb2789dfc3a3c1d7"></a>

```c
int video_enqueue (const struct device *dev, struct video_buffer *buf)
```

相关声明：[video_enqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga036c42c1e7dbaa97eb2789dfc3a3c1d7)、[device](../device_reference/P002_设备对象结构.md)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)。

将视频缓冲区（Video Buffer）交给视频设备。

<a id="r_gaba208d8f4747952acbec5b84f474e31b"></a>

```c
int video_dequeue (const struct device *dev, struct video_buffer **vbuf, k_timeout_t timeout)
```

相关声明：[video_dequeue](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaba208d8f4747952acbec5b84f474e31b)、[device](../device_reference/P002_设备对象结构.md)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从视频设备获取视频缓冲区（Video Buffer）。

<a id="r_ga195914c7f03f2241702c77d41d1ab750"></a>

```c
struct video_buffer * video_buffer_aligned_alloc (size_t size, size_t align, k_timeout_t timeout)
```

相关声明：[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)、[video_buffer_aligned_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga195914c7f03f2241702c77d41d1ab750)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

分配对齐的视频缓冲区（Aligned Video Buffer）。

<a id="r_gaee6eb26310a40d3f18161b3567f9e0a9"></a>

```c
struct video_buffer * video_buffer_alloc (size_t size, k_timeout_t timeout)
```

相关声明：[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)、[video_buffer_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaee6eb26310a40d3f18161b3567f9e0a9)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

分配视频缓冲区（Video Buffer）。

<a id="r_gaa65b69cdc4271a07ad26c4850ff96e45"></a>

```c
struct video_buffer * video_import_buffer (uint8_t *mem, size_t sz)
```

相关声明：[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)、[video_import_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaa65b69cdc4271a07ad26c4850ff96e45)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将外部内存（External Memory）导入视频缓冲池（Video Buffer Pool）。

<a id="r_gaae3a7eee506e77dd130fae74107f6533"></a>

```c
int video_buffer_release (struct video_buffer *buf)
```

相关声明：[video_buffer_release](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaae3a7eee506e77dd130fae74107f6533)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)。

释放视频缓冲区（Video Buffer）。

<a id="r_ga4d3c1458b8c30cff9ac5e6a62d6391c9"></a>

```c
int video_transfer_buffer (const struct device *src, const struct device *sink, enum video_buf_type src_type, enum video_buf_type sink_type, k_timeout_t timeout)
```

相关声明：[video_transfer_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga4d3c1458b8c30cff9ac5e6a62d6391c9)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

在两个视频设备之间转移缓冲区（Transfer a Buffer）。

<a id="r_ga8ec3f0b83ba64947570dfe06ad5e2cbd"></a>

```c
int video_set_signal (const struct device *dev, struct k_poll_signal *sig)
```

相关声明：[video_set_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga8ec3f0b83ba64947570dfe06ad5e2cbd)、[device](../device_reference/P002_设备对象结构.md)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

为视频端点（Video Endpoint）注册／注销 `k_poll` 信号。

<a id="r_ga1cce17a3dfc881a1080708c7bc417aac"></a>

```c
int video_set_ctrl (const struct device *dev, struct video_control *control)
```

相关声明：[video_set_ctrl](../api_input_runtime_topic_reference/P020_视频控制项（Video Controls）.md#ga1cce17a3dfc881a1080708c7bc417aac)、[device](../device_reference/P002_设备对象结构.md)、[video_control](../audio_video_model_reference/P053_video_control_结构体.md)。

设置控件值（Control Value）。

<a id="r_ga71853c720e6df1def4c945e23d103298"></a>

```c
int video_get_ctrl (const struct device *dev, struct video_control *control)
```

相关声明：[video_get_ctrl](../api_input_runtime_topic_reference/P020_视频控制项（Video Controls）.md#ga71853c720e6df1def4c945e23d103298)、[device](../device_reference/P002_设备对象结构.md)、[video_control](../audio_video_model_reference/P053_video_control_结构体.md)。

获取控件当前值（Current Control Value）。

<a id="r_ga8813a656a66adc6bfb10fb7f27194898"></a>

```c
int video_query_ctrl (struct video_ctrl_query *cq)
```

相关声明：[video_query_ctrl](../api_input_runtime_topic_reference/P020_视频控制项（Video Controls）.md#ga8813a656a66adc6bfb10fb7f27194898)、[video_ctrl_query](../audio_video_model_reference/P055_video_ctrl_query_结构体.md)。

查询控件信息（Control Information）。

<a id="r_ga2bff04c6abc344350d6b0036289a701e"></a>

```c
void video_print_ctrl (const struct video_ctrl_query *const cq)
```

相关声明：[video_print_ctrl](../api_input_runtime_topic_reference/P020_视频控制项（Video Controls）.md#ga2bff04c6abc344350d6b0036289a701e)、[video_ctrl_query](../audio_video_model_reference/P055_video_ctrl_query_结构体.md)。

打印控件的全部信息（Control Information）。

<a id="r_ga41e450607b4dc062fac682728ec7a79d"></a>

```c
int64_t video_get_csi_link_freq (const struct device *dev, uint8_t bpp, uint8_t lane_nb)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[video_get_csi_link_freq](../api_input_runtime_topic_reference/P020_视频控制项（Video Controls）.md#ga41e450607b4dc062fac682728ec7a79d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

返回设备通告的链路频率（Link Frequency）。

<a id="r_gaa4d62da5137d0392ce8a19f794478610"></a>

```c
int video_stream_start (const struct device *dev, enum video_buf_type type)
```

相关声明：[video_stream_start](../api_device_topic_reference/P023_视频流（Video Stream）.md#gaa4d62da5137d0392ce8a19f794478610)、[device](../device_reference/P002_设备对象结构.md)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)。

启动视频设备功能（video device function）。

<a id="r_ga77c694bfc3ff8d51a5a74dcd211b2563"></a>

```c
int video_stream_stop (const struct device *dev, enum video_buf_type type)
```

相关声明：[video_stream_stop](../api_device_topic_reference/P023_视频流（Video Stream）.md#ga77c694bfc3ff8d51a5a74dcd211b2563)、[device](../device_reference/P002_设备对象结构.md)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)。

停止视频设备功能。

<a id="r_ga09efb2f6e1f56075cf0c44871266d634"></a>

```c
int video_enum_frmival (const struct device *dev, struct video_frmival_enum *fie)
```

相关声明：[video_enum_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga09efb2f6e1f56075cf0c44871266d634)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)。

列出视频帧间隔（Video Frame Intervals）。

<a id="r_ga46c5bca5cd3caf762f9dd4998b6e21de"></a>

```c
int video_set_frmival (const struct device *dev, struct video_frmival *frmival)
```

相关声明：[video_set_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga46c5bca5cd3caf762f9dd4998b6e21de)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

设置视频帧间隔（Video Frame Interval）。

<a id="r_ga2834be95778244a2446b62e673bbb187"></a>

```c
int video_get_frmival (const struct device *dev, struct video_frmival *frmival)
```

相关声明：[video_get_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga2834be95778244a2446b62e673bbb187)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

获取驱动的视频帧间隔（Video Frame Interval）。

<a id="r_ga6b3c7456b2527cc441a100ff50787dc2"></a>

```c
static uint64_t video_frmival_nsec (const struct video_frmival *frmival)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[video_frmival_nsec](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga6b3c7456b2527cc441a100ff50787dc2)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

计算两个帧间隔（Frame Intervals）的差值。

<a id="r_gafa448552f4257d761d96976cbe3da928"></a>

```c
int video_closest_frmival_stepwise (const struct video_frmival_stepwise *stepwise, const struct video_frmival *desired, struct video_frmival *match)
```

相关声明：[video_closest_frmival_stepwise](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#gafa448552f4257d761d96976cbe3da928)、[video_frmival_stepwise](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

在按步长变化的帧间隔范围（Stepwise Frame Interval）内，查找与给定帧间隔值最接近的匹配。

<a id="r_ga99722c1e31aa6b73f443c22593b76e87"></a>

```c
int video_closest_frmival (const struct device *dev, struct video_frmival_enum *match)
```

相关声明：[video_closest_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga99722c1e31aa6b73f443c22593b76e87)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)。

在视频设备（Video Device）支持的范围内，查找与给定帧间隔值最接近的匹配。

<a id="r_ga774ef89a7321a6842890005ad53c1594"></a>

```c
int video_estimate_fmt_size (struct video_format *fmt)
```

相关声明：[video_estimate_fmt_size](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga774ef89a7321a6842890005ad53c1594)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

估算 `video_format` 的大小和行跨度（Pitch），单位为字节。

<a id="r_ga9de739567bff0a8ce915d389294e35ec"></a>

```c
int video_set_compose_format (const struct device *dev, struct video_format *fmt)
```

相关声明：[video_set_compose_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga9de739567bff0a8ce915d389294e35ec)、[device](../device_reference/P002_设备对象结构.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

设置格式前先设置合成矩形（Compose Rectangle），如果适用。

<a id="r_ga1deb2dbafd7f4eeb602a3f78aaeb5e33"></a>

```c
int video_set_format (const struct device *dev, struct video_format *fmt)
```

相关声明：[video_set_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga1deb2dbafd7f4eeb602a3f78aaeb5e33)、[device](../device_reference/P002_设备对象结构.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

设置视频格式（Video Format）。

<a id="r_ga8db8c17f3cb418e44620816e9a5cf706"></a>

```c
int video_get_format (const struct device *dev, struct video_format *fmt)
```

相关声明：[video_get_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga8db8c17f3cb418e44620816e9a5cf706)、[device](../device_reference/P002_设备对象结构.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

获取驱动的视频格式（Video Format）。

<a id="r_ga6ea31432d37e0f8f46e0f6c2690ee3e9"></a>

```c
int video_set_selection (const struct device *dev, struct video_selection *sel)
```

相关声明：[video_set_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga6ea31432d37e0f8f46e0f6c2690ee3e9)、[device](../device_reference/P002_设备对象结构.md)、[video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)。

设置视频选区（Video Selection），即裁剪／合成（Crop/Compose）。

<a id="r_ga0c30d2802c82b28cbb5029e7bc52b5b4"></a>

```c
int video_get_selection (const struct device *dev, struct video_selection *sel)
```

相关声明：[video_get_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga0c30d2802c82b28cbb5029e7bc52b5b4)、[device](../device_reference/P002_设备对象结构.md)、[video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)。

获取视频选区（Video Selection），即裁剪／合成（Crop/Compose）。

<a id="r_ga1bf94d7b435524d0face3f713c4dca9d"></a>

```c
int video_get_caps (const struct device *dev, struct video_caps *caps)
```

相关声明：[video_get_caps](../api_lifecycle_capability_topic_reference/P026_视频能力（Video Capabilities）.md#ga1bf94d7b435524d0face3f713c4dca9d)、[device](../device_reference/P002_设备对象结构.md)、[video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)。

获取视频端点能力（Video Endpoint Capabilities）。

<a id="r_ga3d2d1692e4adab02948b11f38407610f"></a>

```c
int video_transform_cap (const struct device *const dev, const struct video_format_cap *const cap, struct video_format_cap *const res_cap, enum video_buf_type type, uint16_t ind)
```

相关声明：[video_transform_cap](../api_lifecycle_capability_topic_reference/P026_视频能力（Video Capabilities）.md#ga3d2d1692e4adab02948b11f38407610f)、[device](../device_reference/P002_设备对象结构.md)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将视频格式能力（Video Format Capability）从内存到内存（M2M）视频设备的一端转换到另一端。

<a id="r_gadbf59fd2d77b3d164cacf56bd4ae81ce"></a>

```c
int video_format_caps_index (const struct video_format_cap *fmts, const struct video_format *fmt, size_t *idx)
```

相关声明：[video_format_caps_index](../api_lifecycle_capability_topic_reference/P026_视频能力（Video Capabilities）.md#gadbf59fd2d77b3d164cacf56bd4ae81ce)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

在能力列表（Capabilities List）中搜索匹配的格式（Format）。


## 12.2\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/video/controls.h](../api_source_reference/P117_controls.h_源码浏览.md)
- [zephyr/video/formats.h](../api_source_supplement_reference/P073_formats.h_源码浏览.md)
- [zephyr/video/types.h](../api_source_supplement_reference/P094_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P908_video.h_源码浏览.md)
- [video_enqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga036c42c1e7dbaa97eb2789dfc3a3c1d7)
- [device](../device_reference/P002_设备对象结构.md)
- [video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)
- [video_dequeue](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaba208d8f4747952acbec5b84f474e31b)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [video_buffer_aligned_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga195914c7f03f2241702c77d41d1ab750)
- [video_buffer_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaee6eb26310a40d3f18161b3567f9e0a9)
- [video_import_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaa65b69cdc4271a07ad26c4850ff96e45)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [video_buffer_release](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaae3a7eee506e77dd130fae74107f6533)
- [video_transfer_buffer](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga4d3c1458b8c30cff9ac5e6a62d6391c9)
- [video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)
- [video_set_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga8ec3f0b83ba64947570dfe06ad5e2cbd)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [video_set_ctrl](../api_input_runtime_topic_reference/P020_视频控制项（Video Controls）.md#ga1cce17a3dfc881a1080708c7bc417aac)
- [video_control](../audio_video_model_reference/P053_video_control_结构体.md)
- [video_get_ctrl](../api_input_runtime_topic_reference/P020_视频控制项（Video Controls）.md#ga71853c720e6df1def4c945e23d103298)
- [video_query_ctrl](../api_input_runtime_topic_reference/P020_视频控制项（Video Controls）.md#ga8813a656a66adc6bfb10fb7f27194898)
- [video_ctrl_query](../audio_video_model_reference/P055_video_ctrl_query_结构体.md)
- [video_print_ctrl](../api_input_runtime_topic_reference/P020_视频控制项（Video Controls）.md#ga2bff04c6abc344350d6b0036289a701e)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [video_get_csi_link_freq](../api_input_runtime_topic_reference/P020_视频控制项（Video Controls）.md#ga41e450607b4dc062fac682728ec7a79d)
- [video_stream_start](../api_device_topic_reference/P023_视频流（Video Stream）.md#gaa4d62da5137d0392ce8a19f794478610)
- [video_stream_stop](../api_device_topic_reference/P023_视频流（Video Stream）.md#ga77c694bfc3ff8d51a5a74dcd211b2563)
- [video_enum_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga09efb2f6e1f56075cf0c44871266d634)
- [video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)
- [video_set_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga46c5bca5cd3caf762f9dd4998b6e21de)
- [video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)
- [video_get_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga2834be95778244a2446b62e673bbb187)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [video_frmival_nsec](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga6b3c7456b2527cc441a100ff50787dc2)
- [video_closest_frmival_stepwise](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#gafa448552f4257d761d96976cbe3da928)
- [video_frmival_stepwise](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md)
- [video_closest_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga99722c1e31aa6b73f443c22593b76e87)
- [video_estimate_fmt_size](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga774ef89a7321a6842890005ad53c1594)
- [video_format](../audio_video_model_reference/P059_video_format_结构体.md)
- [video_set_compose_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga9de739567bff0a8ce915d389294e35ec)
- [video_set_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga1deb2dbafd7f4eeb602a3f78aaeb5e33)
- [video_get_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga8db8c17f3cb418e44620816e9a5cf706)
- [video_set_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga6ea31432d37e0f8f46e0f6c2690ee3e9)
- [video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)
- [video_get_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga0c30d2802c82b28cbb5029e7bc52b5b4)
- [video_get_caps](../api_lifecycle_capability_topic_reference/P026_视频能力（Video Capabilities）.md#ga1bf94d7b435524d0face3f713c4dca9d)
- [video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)
- [video_transform_cap](../api_lifecycle_capability_topic_reference/P026_视频能力（Video Capabilities）.md#ga3d2d1692e4adab02948b11f38407610f)
- [video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [video_format_caps_index](../api_lifecycle_capability_topic_reference/P026_视频能力（Video Capabilities）.md#gadbf59fd2d77b3d164cacf56bd4ae81ce)

<a id="header-details"></a>

---

[上一章](P011_zephyr__drivers__mfd__rv3032.h_文件参考.md) · [返回大纲](大纲.md)
