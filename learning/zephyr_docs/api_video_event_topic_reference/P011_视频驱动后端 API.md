---
id: learning.zephyr-docs.api-video-event-topic-reference.page-11
title: 视频驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_视频驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

此组包含实现视频驱动（Video Driver）所需的 API 类型定义、回调签名（Callback Signatures）及其他辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_video_5Fdriver_5Fapi"></a>

```c
struct video_driver_api
```

相关声明：[video_driver_api](../audio_video_model_reference/P058_video_driver_api_结构体.md)。

驱动操作（Driver Operations）：视频（Video）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.2\_类型定义（Typedefs）

<a id="r_ga964b301e45a42aa78799a1d9c9297ab1"></a>

```c
typedef int(* video_api_format_t) (const struct device *dev, struct video_format *fmt)
```

相关声明：[video_api_format_t](#ga964b301e45a42aa78799a1d9c9297ab1)、[device](../device_reference/P002_设备对象结构.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

设置或获取视频格式（Video Format）的回调 API。

<a id="r_gaf63180944041a9e934c9f7567bdc1b88"></a>

```c
typedef int(* video_api_frmival_t) (const struct device *dev, struct video_frmival *frmival)
```

相关声明：[video_api_frmival_t](#gaf63180944041a9e934c9f7567bdc1b88)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

设置或获取视频帧间隔（Video Frame Interval）的回调 API。

<a id="r_ga026c9a4531a125339e69b81f75343555"></a>

```c
typedef int(* video_api_enum_frmival_t) (const struct device *dev, struct video_frmival_enum *fie)
```

相关声明：[video_api_enum_frmival_t](#ga026c9a4531a125339e69b81f75343555)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)。

枚举某种格式支持的帧间隔（Frame Intervals）的回调 API。

<a id="r_gae6849a22140b3507bab219b579bc3d40"></a>

```c
typedef int(* video_api_enqueue_t) (const struct device *dev, struct video_buffer *buf)
```

相关声明：[video_api_enqueue_t](#gae6849a22140b3507bab219b579bc3d40)、[device](../device_reference/P002_设备对象结构.md)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)。

向驱动入站队列（Incoming Queue）加入缓冲区的回调 API。

<a id="r_ga4265087c8faf62bbc36e88c0587022a1"></a>

```c
typedef int(* video_api_dequeue_t) (const struct device *dev, struct video_buffer **buf, k_timeout_t timeout)
```

相关声明：[video_api_dequeue_t](#ga4265087c8faf62bbc36e88c0587022a1)、[device](../device_reference/P002_设备对象结构.md)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从驱动出站队列（Outgoing Queue）取出缓冲区的回调 API。

<a id="r_ga990ba001531c7300a06ca02d64c31eaa"></a>

```c
typedef int(* video_api_flush_t) (const struct device *dev, bool cancel)
```

相关声明：[video_api_flush_t](#ga990ba001531c7300a06ca02d64c31eaa)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

清理端点缓冲区（Flush Endpoint Buffers）的回调 API。

<a id="r_gacda90bacb17a53e0bd11e5bfd37be57a"></a>

```c
typedef int(* video_api_set_stream_t) (const struct device *dev, bool enable, enum video_buf_type type)
```

相关声明：[video_api_set_stream_t](#gacda90bacb17a53e0bd11e5bfd37be57a)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)。

控制数据流状态（Stream Status）的回调 API。

<a id="r_ga522b4027fc6f22bf59f4face3c97e303"></a>

```c
typedef int(* video_api_ctrl_t) (const struct device *dev, uint32_t cid)
```

相关声明：[video_api_ctrl_t](#ga522b4027fc6f22bf59f4face3c97e303)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置或获取视频控件值（Video Control Value）的回调 API。

<a id="r_ga070cb5f5bf35b98e2e7dda3378114780"></a>

```c
typedef int(* video_api_get_caps_t) (const struct device *dev, struct video_caps *caps)
```

相关声明：[video_api_get_caps_t](#ga070cb5f5bf35b98e2e7dda3378114780)、[device](../device_reference/P002_设备对象结构.md)、[video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)。

获取视频端点能力（Video Endpoint Capabilities）的回调 API。

<a id="r_ga0a9e2ed76720f172b1b668e79220e968"></a>

```c
typedef int(* video_api_transform_cap_t) (const struct device *const dev, const struct video_format_cap *const cap, struct video_format_cap *const res_cap, enum video_buf_type type, uint16_t ind)
```

相关声明：[video_api_transform_cap_t](#ga0a9e2ed76720f172b1b668e79220e968)、[device](../device_reference/P002_设备对象结构.md)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在内存到内存（m2m）设备端点之间转换格式能力（Format Capability）的回调 API。

<a id="r_gad5aacb1386785a3587d41844c7854f83"></a>

```c
typedef int(* video_api_set_signal_t) (const struct device *dev, struct k_poll_signal *sig)
```

相关声明：[video_api_set_signal_t](#gad5aacb1386785a3587d41844c7854f83)、[device](../device_reference/P002_设备对象结构.md)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

为缓冲区事件（Buffer Events）注册或注销轮询信号（Poll Signal）的回调 API。

<a id="r_gab4d2eb34f8ccc95fa6dcda7848f4408a"></a>

```c
typedef int(* video_api_selection_t) (const struct device *dev, struct video_selection *sel)
```

相关声明：[video_api_selection_t](#gab4d2eb34f8ccc95fa6dcda7848f4408a)、[device](../device_reference/P002_设备对象结构.md)、[video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)。

设置或获取视频选区（Video Selection），即裁剪／合成（Crop/Compose）的回调 API。

## 11.3\_详细说明（Detailed Documentation）

<a id="ga522b4027fc6f22bf59f4face3c97e303"></a>

### `video_api_ctrl_t`

```c
typedef int(* video_api_ctrl_t) (const struct device *dev, uint32_t cid)
```

```c
#include <zephyr/drivers/video.h>
```

设置或获取视频控件值（Video Control Value）的回调 API。

参数说明参见 `video_driver_set_ctrl()` 和 `video_driver_get_volatile_ctrl()`。

<a id="ga4265087c8faf62bbc36e88c0587022a1"></a>

### `video_api_dequeue_t`

```c
typedef int(* video_api_dequeue_t) (const struct device *dev, struct video_buffer **buf, k_timeout_t timeout)
```

```c
#include <zephyr/drivers/video.h>
```

从驱动出站队列（Outgoing Queue）取出缓冲区的回调 API。

参数说明参见 `video_driver_dequeue()`。

<a id="gae6849a22140b3507bab219b579bc3d40"></a>

### `video_api_enqueue_t`

```c
typedef int(* video_api_enqueue_t) (const struct device *dev, struct video_buffer *buf)
```

```c
#include <zephyr/drivers/video.h>
```

向驱动入站队列（Incoming Queue）加入缓冲区的回调 API。

参数说明参见 `video_driver_enqueue()`。

<a id="ga026c9a4531a125339e69b81f75343555"></a>

### `video_api_enum_frmival_t`

```c
typedef int(* video_api_enum_frmival_t) (const struct device *dev, struct video_frmival_enum *fie)
```

```c
#include <zephyr/drivers/video.h>
```

枚举某种格式支持的帧间隔（Frame Intervals）的回调 API。

参数说明参见 `video_driver_enum_frmival()`。

<a id="ga990ba001531c7300a06ca02d64c31eaa"></a>

### `video_api_flush_t`

```c
typedef int(* video_api_flush_t) (const struct device *dev, bool cancel)
```

```c
#include <zephyr/drivers/video.h>
```

清理端点缓冲区（Flush Endpoint Buffers）的回调 API。

参数说明参见 `video_driver_flush()`。

<a id="ga964b301e45a42aa78799a1d9c9297ab1"></a>

### `video_api_format_t`

```c
typedef int(* video_api_format_t) (const struct device *dev, struct video_format *fmt)
```

```c
#include <zephyr/drivers/video.h>
```

设置或获取视频格式（Video Format）的回调 API。

参数说明参见 `video_driver_set_format()` 和 `video_driver_get_format()`。

<a id="gaf63180944041a9e934c9f7567bdc1b88"></a>

### `video_api_frmival_t`

```c
typedef int(* video_api_frmival_t) (const struct device *dev, struct video_frmival *frmival)
```

```c
#include <zephyr/drivers/video.h>
```

设置或获取视频帧间隔（Video Frame Interval）的回调 API。

参数说明参见 `video_driver_set_frmival()` 和 `video_driver_get_frmival()`。

<a id="ga070cb5f5bf35b98e2e7dda3378114780"></a>

### `video_api_get_caps_t`

```c
typedef int(* video_api_get_caps_t) (const struct device *dev, struct video_caps *caps)
```

```c
#include <zephyr/drivers/video.h>
```

获取视频端点能力（Video Endpoint Capabilities）的回调 API。

参数说明参见 `video_get_caps()`。

<a id="gab4d2eb34f8ccc95fa6dcda7848f4408a"></a>

### `video_api_selection_t`

```c
typedef int(* video_api_selection_t) (const struct device *dev, struct video_selection *sel)
```

```c
#include <zephyr/drivers/video.h>
```

设置或获取视频选区（Video Selection），即裁剪／合成（Crop/Compose）的回调 API。

参数说明参见 `video_driver_set_selection()` 和 `video_driver_get_selection()`。

<a id="gad5aacb1386785a3587d41844c7854f83"></a>

### `video_api_set_signal_t`

```c
typedef int(* video_api_set_signal_t) (const struct device *dev, struct k_poll_signal *sig)
```

```c
#include <zephyr/drivers/video.h>
```

为缓冲区事件（Buffer Events）注册或注销轮询信号（Poll Signal）的回调 API。

参数说明参见 `video_set_signal()`。

<a id="gacda90bacb17a53e0bd11e5bfd37be57a"></a>

### `video_api_set_stream_t`

```c
typedef int(* video_api_set_stream_t) (const struct device *dev, bool enable, enum video_buf_type type)
```

```c
#include <zephyr/drivers/video.h>
```

控制数据流状态（Stream Status）的回调 API。

参数说明参见 `video_driver_set_stream()`。

<a id="ga0a9e2ed76720f172b1b668e79220e968"></a>

### `video_api_transform_cap_t`

```c
typedef int(* video_api_transform_cap_t) (const struct device *const dev, const struct video_format_cap *const cap, struct video_format_cap *const res_cap, enum video_buf_type type, uint16_t ind)
```

```c
#include <zephyr/drivers/video.h>
```

在内存到内存（m2m）设备端点之间转换格式能力（Format Capability）的回调 API。

参数说明参见 `video_transform_cap()`。


## 11.4\_原页交叉引用（Cross References）

- [video_driver_api](../audio_video_model_reference/P058_video_driver_api_结构体.md)
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
- [zephyr/drivers/video.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h.html)
- [video_driver_set_ctrl()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga211f219e42890a6788b448c1c23fcd84)
- [video_driver_get_volatile_ctrl()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga15d602806f0c30a1c28bcba7cf1fe82a)
- [video_driver_dequeue()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gaaf4610cbab1caaf95070b7366cb4c4c6)
- [video_driver_enqueue()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gae73ac504f2d726ab9a88bc35e0e25b09)
- [video_driver_enum_frmival()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga26d096ae93185ed1157a75d429dd145d)
- [video_driver_flush()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga8ddced08604291df2eec55aadc3c217c)
- [video_driver_set_format()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga9a29705addc34c59eb6406dd37519eaf)
- [video_driver_get_format()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gabd3ca5bdb2915a78fd12182fde435c30)
- [video_driver_set_frmival()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga57016218645ba4d98bab320545b80f1c)
- [video_driver_get_frmival()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga4eb2460636e70ddfa1b6f5187d882bfe)
- [video_get_caps()](../api_lifecycle_capability_topic_reference/P026_视频能力（Video Capabilities）.md#ga1bf94d7b435524d0face3f713c4dca9d)
- [video_driver_set_selection()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gafc494071abdfb4c38dff515bda316379)
- [video_driver_get_selection()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga2037f560bb9a7a83d6cb23787d7bf167)
- [video_set_signal()](P008_视频缓冲区（Video Buffers）.md#ga8ec3f0b83ba64947570dfe06ad5e2cbd)
- [video_driver_set_stream()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga8c19eb99330402975f6e6630e1b91436)
- [video_transform_cap()](../api_lifecycle_capability_topic_reference/P026_视频能力（Video Capabilities）.md#ga3d2d1692e4adab02948b11f38407610f)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P010_视频帧间隔（Video Frame Interval）.md) · [返回大纲](大纲.md) · [下一章](P012_Xen 设备模型（Device model）.md)
