---
id: learning.zephyr-docs.api-file-display-chat-reference.page-9
title: zephyr__drivers__video.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_drivers\_\_video.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频（Video）驱动API的主头文件。

<a id="details"></a>

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/dlist.h>
#include <zephyr/types.h>
#include <zephyr/video/video.h>
```

查看此文件的源码。

视频（Video）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_video_5Fdevice"></a>

```c
struct video_device
```

相关声明：[video_device](../audio_video_model_reference/P057_video_device_结构体.md)。

视频设备封装类型（Wrapper Type）的存储类型。

<a id="r_video_5Fctrl"></a>

```c
struct video_ctrl
```

相关声明：[video_ctrl](../audio_video_model_reference/P054_video_ctrl_结构体.md)。

视频控制项（Video Controls）的存储类型。

<a id="r_video_5Fdriver_5Fapi"></a>

```c
struct video_driver_api
```

相关声明：[video_driver_api](../audio_video_model_reference/P058_video_driver_api_结构体.md)。

驱动操作（Driver Operations）：视频（Video）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_gac5b71618fa28d839fcca8a3aba2588e3"></a>

```c
#define VIDEO_CTRL_FLAG_READ_ONLY BIT(0)
```

相关声明：[VIDEO_CTRL_FLAG_READ_ONLY](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#gac5b71618fa28d839fcca8a3aba2588e3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控件（Control）为只读（Read-only）。

<a id="r_ga9c09aef246638ff0a81bcfdbc83f14b5"></a>

```c
#define VIDEO_CTRL_FLAG_WRITE_ONLY BIT(1)
```

相关声明：[VIDEO_CTRL_FLAG_WRITE_ONLY](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ga9c09aef246638ff0a81bcfdbc83f14b5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控件（Control）为只写（Write-only）。

<a id="r_ga379d50aa61ccc522e3051fb249ecb404"></a>

```c
#define VIDEO_CTRL_FLAG_VOLATILE BIT(2)
```

相关声明：[VIDEO_CTRL_FLAG_VOLATILE](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ga379d50aa61ccc522e3051fb249ecb404)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

由硬件持续更新、因而每次都需要重新读取的控件（Control）。

<a id="r_ga2dc6cfe5e71aa00a54bca525995fc8dc"></a>

```c
#define VIDEO_CTRL_FLAG_INACTIVE BIT(3)
```

相关声明：[VIDEO_CTRL_FLAG_INACTIVE](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ga2dc6cfe5e71aa00a54bca525995fc8dc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控件（Control）处于非活动状态（Inactive），例如：

<a id="r_ga301ff065c2ebe9a39ff8a5aafbe25d5f"></a>

```c
#define VIDEO_CTRL_FLAG_UPDATE BIT(4)
```

相关声明：[VIDEO_CTRL_FLAG_UPDATE](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ga301ff065c2ebe9a39ff8a5aafbe25d5f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

会影响其他控件的控件（Control），例如：

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.3\_类型定义（Typedefs）

<a id="r_ga964b301e45a42aa78799a1d9c9297ab1"></a>

```c
typedef int(* video_api_format_t) (const struct device *dev, struct video_format *fmt)
```

相关声明：[video_api_format_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga964b301e45a42aa78799a1d9c9297ab1)、[device](../device_reference/P002_设备对象结构.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

设置或获取视频格式（Video Format）的回调 API。

<a id="r_gaf63180944041a9e934c9f7567bdc1b88"></a>

```c
typedef int(* video_api_frmival_t) (const struct device *dev, struct video_frmival *frmival)
```

相关声明：[video_api_frmival_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#gaf63180944041a9e934c9f7567bdc1b88)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

设置或获取视频帧间隔（Video Frame Interval）的回调 API。

<a id="r_ga026c9a4531a125339e69b81f75343555"></a>

```c
typedef int(* video_api_enum_frmival_t) (const struct device *dev, struct video_frmival_enum *fie)
```

相关声明：[video_api_enum_frmival_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga026c9a4531a125339e69b81f75343555)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)。

枚举某种格式支持的帧间隔（Frame Intervals）的回调 API。

<a id="r_gae6849a22140b3507bab219b579bc3d40"></a>

```c
typedef int(* video_api_enqueue_t) (const struct device *dev, struct video_buffer *buf)
```

相关声明：[video_api_enqueue_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#gae6849a22140b3507bab219b579bc3d40)、[device](../device_reference/P002_设备对象结构.md)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)。

向驱动入站队列（Incoming Queue）加入缓冲区的回调 API。

<a id="r_ga4265087c8faf62bbc36e88c0587022a1"></a>

```c
typedef int(* video_api_dequeue_t) (const struct device *dev, struct video_buffer **buf, k_timeout_t timeout)
```

相关声明：[video_api_dequeue_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga4265087c8faf62bbc36e88c0587022a1)、[device](../device_reference/P002_设备对象结构.md)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从驱动出站队列（Outgoing Queue）取出缓冲区的回调 API。

<a id="r_ga990ba001531c7300a06ca02d64c31eaa"></a>

```c
typedef int(* video_api_flush_t) (const struct device *dev, bool cancel)
```

相关声明：[video_api_flush_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga990ba001531c7300a06ca02d64c31eaa)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

清理端点缓冲区（Flush Endpoint Buffers）的回调 API。

<a id="r_gacda90bacb17a53e0bd11e5bfd37be57a"></a>

```c
typedef int(* video_api_set_stream_t) (const struct device *dev, bool enable, enum video_buf_type type)
```

相关声明：[video_api_set_stream_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#gacda90bacb17a53e0bd11e5bfd37be57a)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)。

控制数据流状态（Stream Status）的回调 API。

<a id="r_ga522b4027fc6f22bf59f4face3c97e303"></a>

```c
typedef int(* video_api_ctrl_t) (const struct device *dev, uint32_t cid)
```

相关声明：[video_api_ctrl_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga522b4027fc6f22bf59f4face3c97e303)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置或获取视频控件值（Video Control Value）的回调 API。

<a id="r_ga070cb5f5bf35b98e2e7dda3378114780"></a>

```c
typedef int(* video_api_get_caps_t) (const struct device *dev, struct video_caps *caps)
```

相关声明：[video_api_get_caps_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga070cb5f5bf35b98e2e7dda3378114780)、[device](../device_reference/P002_设备对象结构.md)、[video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)。

获取视频端点能力（Video Endpoint Capabilities）的回调 API。

<a id="r_ga0a9e2ed76720f172b1b668e79220e968"></a>

```c
typedef int(* video_api_transform_cap_t) (const struct device *const dev, const struct video_format_cap *const cap, struct video_format_cap *const res_cap, enum video_buf_type type, uint16_t ind)
```

相关声明：[video_api_transform_cap_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga0a9e2ed76720f172b1b668e79220e968)、[device](../device_reference/P002_设备对象结构.md)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在内存到内存（m2m）设备端点之间转换格式能力（Format Capability）的回调 API。

<a id="r_gad5aacb1386785a3587d41844c7854f83"></a>

```c
typedef int(* video_api_set_signal_t) (const struct device *dev, struct k_poll_signal *sig)
```

相关声明：[video_api_set_signal_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#gad5aacb1386785a3587d41844c7854f83)、[device](../device_reference/P002_设备对象结构.md)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

为缓冲区事件（Buffer Events）注册或注销轮询信号（Poll Signal）的回调 API。

<a id="r_gab4d2eb34f8ccc95fa6dcda7848f4408a"></a>

```c
typedef int(* video_api_selection_t) (const struct device *dev, struct video_selection *sel)
```

相关声明：[video_api_selection_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#gab4d2eb34f8ccc95fa6dcda7848f4408a)、[device](../device_reference/P002_设备对象结构.md)、[video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)。

设置或获取视频选区（Video Selection），即裁剪／合成（Crop/Compose）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.4\_枚举（Enumerations）

<a id="r_gaf6e4edb13feb3bd422e19c438b435687"></a>

```c
enum video_ctrl_type { VIDEO_CTRL_TYPE_BOOLEAN = 1 , VIDEO_CTRL_TYPE_INTEGER = 2 , VIDEO_CTRL_TYPE_INTEGER64 = 3 , VIDEO_CTRL_TYPE_MENU = 4 , VIDEO_CTRL_TYPE_STRING = 5 , VIDEO_CTRL_TYPE_INTEGER_MENU = 6 }
```

相关声明：[video_ctrl_type](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#gaf6e4edb13feb3bd422e19c438b435687)、[VIDEO_CTRL_TYPE_BOOLEAN](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ggaf6e4edb13feb3bd422e19c438b435687a7568dcc1abd061f4eaadd5f487523736)、[VIDEO_CTRL_TYPE_INTEGER](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ggaf6e4edb13feb3bd422e19c438b435687a0a353803ba2af5f06c363b8d630e93bc)、[VIDEO_CTRL_TYPE_INTEGER64](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ggaf6e4edb13feb3bd422e19c438b435687ab2f378c2985335e39648fa200d9b7a13)、[VIDEO_CTRL_TYPE_MENU](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ggaf6e4edb13feb3bd422e19c438b435687a05a03f70b04c1ee7e05547cda9917950)、[VIDEO_CTRL_TYPE_STRING](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ggaf6e4edb13feb3bd422e19c438b435687a06666e95282ce67b10a46ee8d32309a3)、[VIDEO_CTRL_TYPE_INTEGER_MENU](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ggaf6e4edb13feb3bd422e19c438b435687a13da0d22cf3e12652424ca0d35f09071)。

视频控件（Video Control）的类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.5\_函数（Functions）

<a id="r_ga3d31ffde89ef76e72855ded34c6deb3c"></a>

```c
struct video_device * video_find_vdev (const struct device *dev)
```

相关声明：[video_device](../audio_video_model_reference/P057_video_device_结构体.md)、[video_find_vdev](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga3d31ffde89ef76e72855ded34c6deb3c)、[device](../device_reference/P002_设备对象结构.md)。

查找与视频设备（Video Device）关联的 video_device。

<a id="r_ga9a29705addc34c59eb6406dd37519eaf"></a>

```c
static int video_driver_set_format (const struct device *dev, struct video_format *fmt)
```

相关声明：[video_driver_set_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga9a29705addc34c59eb6406dd37519eaf)、[device](../device_reference/P002_设备对象结构.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

设置驱动的视频格式（Video Format）。

<a id="r_gabd3ca5bdb2915a78fd12182fde435c30"></a>

```c
static int video_driver_get_format (const struct device *dev, struct video_format *fmt)
```

相关声明：[video_driver_get_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gabd3ca5bdb2915a78fd12182fde435c30)、[device](../device_reference/P002_设备对象结构.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

获取驱动的视频格式（Video Format）。

<a id="r_ga57016218645ba4d98bab320545b80f1c"></a>

```c
static int video_driver_set_frmival (const struct device *dev, struct video_frmival *frmival)
```

相关声明：[video_driver_set_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga57016218645ba4d98bab320545b80f1c)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

向驱动应用视频帧间隔（Video Frame Interval）。

<a id="r_ga4eb2460636e70ddfa1b6f5187d882bfe"></a>

```c
static int video_driver_get_frmival (const struct device *dev, struct video_frmival *frmival)
```

相关声明：[video_driver_get_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga4eb2460636e70ddfa1b6f5187d882bfe)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

获取驱动的视频帧间隔（Video Frame Interval）。

<a id="r_ga26d096ae93185ed1157a75d429dd145d"></a>

```c
static int video_driver_enum_frmival (const struct device *dev, struct video_frmival_enum *fie)
```

相关声明：[video_driver_enum_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga26d096ae93185ed1157a75d429dd145d)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)。

列出视频帧间隔（Video Frame Intervals）。

<a id="r_gae73ac504f2d726ab9a88bc35e0e25b09"></a>

```c
static int video_driver_enqueue (const struct device *dev, struct video_buffer *vbuf)
```

相关声明：[video_driver_enqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gae73ac504f2d726ab9a88bc35e0e25b09)、[device](../device_reference/P002_设备对象结构.md)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)。

向驱动传递视频缓冲区（Video Buffer）。

<a id="r_gaaf4610cbab1caaf95070b7366cb4c4c6"></a>

```c
static int video_driver_dequeue (const struct device *dev, struct video_buffer **vbuf, k_timeout_t timeout)
```

相关声明：[video_driver_dequeue](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gaaf4610cbab1caaf95070b7366cb4c4c6)、[device](../device_reference/P002_设备对象结构.md)、[video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从驱动取出队列中的视频缓冲区（Dequeue a Video Buffer）。

<a id="r_ga8ddced08604291df2eec55aadc3c217c"></a>

```c
static int video_driver_flush (const struct device *dev, bool cancel)
```

相关声明：[video_driver_flush](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga8ddced08604291df2eec55aadc3c217c)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

刷新驱动的端点缓冲区（Flush Endpoint Buffers）。

<a id="r_ga8c19eb99330402975f6e6630e1b91436"></a>

```c
static int video_driver_set_stream (const struct device *dev, bool enable, enum video_buf_type type)
```

相关声明：[video_driver_set_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga8c19eb99330402975f6e6630e1b91436)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)。

启动或停止视频驱动功能（Video Driver Function）。

<a id="r_ga15d602806f0c30a1c28bcba7cf1fe82a"></a>

```c
static int video_driver_get_volatile_ctrl (const struct device *dev, uint32_t cid)
```

相关声明：[video_driver_get_volatile_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga15d602806f0c30a1c28bcba7cf1fe82a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取驱动的视频控件易变值（Volatile Video Control Value）。

<a id="r_ga211f219e42890a6788b448c1c23fcd84"></a>

```c
static int video_driver_set_ctrl (const struct device *dev, uint32_t cid)
```

相关声明：[video_driver_set_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga211f219e42890a6788b448c1c23fcd84)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置驱动的视频控件值（Video Control Value）。

<a id="r_ga85a3064db275074f31494a364d17b51f"></a>

```c
static int video_driver_get_caps (const struct device *dev, struct video_caps *caps)
```

相关声明：[video_driver_get_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga85a3064db275074f31494a364d17b51f)、[device](../device_reference/P002_设备对象结构.md)、[video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)。

获取视频驱动端点的能力（Endpoint Capabilities）。

<a id="r_ga224e26d848ff68d10452dd4d2a44fba5"></a>

```c
static int video_driver_transform_cap (const struct device *const dev, const struct video_format_cap *const cap, struct video_format_cap *const res_cap, enum video_buf_type type, uint16_t ind)
```

相关声明：[video_driver_transform_cap](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga224e26d848ff68d10452dd4d2a44fba5)、[device](../device_reference/P002_设备对象结构.md)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将视频格式能力（Video Format Capability）从内存到内存（M2M）视频设备的一端转换到另一端。

<a id="r_ga6f8b1924bf4a0ee1d7315a8e472614eb"></a>

```c
static int video_driver_set_signal (const struct device *dev, struct k_poll_signal *sig)
```

相关声明：[video_driver_set_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga6f8b1924bf4a0ee1d7315a8e472614eb)、[device](../device_reference/P002_设备对象结构.md)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

为视频端点（Video Endpoint）注册／注销 `k_poll` 信号。

<a id="r_gafc494071abdfb4c38dff515bda316379"></a>

```c
static int video_driver_set_selection (const struct device *dev, struct video_selection *sel)
```

相关声明：[video_driver_set_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gafc494071abdfb4c38dff515bda316379)、[device](../device_reference/P002_设备对象结构.md)、[video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)。

设置视频选区（Video Selection），即裁剪／合成（Crop/Compose）。

<a id="r_ga2037f560bb9a7a83d6cb23787d7bf167"></a>

```c
static int video_driver_get_selection (const struct device *dev, struct video_selection *sel)
```

相关声明：[video_driver_get_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga2037f560bb9a7a83d6cb23787d7bf167)、[device](../device_reference/P002_设备对象结构.md)、[video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)。

获取视频选区（Video Selection），即裁剪／合成（Crop/Compose）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 9.6\_MIPI CSI-2 数据类型（Data Types）

用于相机传感器接口的标准 MIPI CSI-2 数据类型标识符（Data Type Identifiers）。

这些常量定义 MIPI CSI-2 数据包头中数据类型字段（Data Type Field）的值，用于标识所传输图像数据的格式和编码。数据类型字段宽度为 6 位，允许的值为 0x00 至 0x3F。

<a id="r_ga59d6f35198b6412a9aa78c094ecfaa19"></a>

```c
#define VIDEO_MIPI_CSI2_DT_NULL 0x10
```

相关声明：[VIDEO_MIPI_CSI2_DT_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga59d6f35198b6412a9aa78c094ecfaa19)。

NULL 数据类型：用于填充（Padding）或同步（Synchronization）。

<a id="r_gaede52c3391311b7cf931665afdeed720"></a>

```c
#define VIDEO_MIPI_CSI2_DT_BLANKING 0x11
```

相关声明：[VIDEO_MIPI_CSI2_DT_BLANKING](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gaede52c3391311b7cf931665afdeed720)。

消隐数据（Blanking Data）：水平／垂直消隐信息。

<a id="r_ga2b16d411ffcbcc7e74fa6aa2966b4b0d"></a>

```c
#define VIDEO_MIPI_CSI2_DT_EMBEDDED_8 0x12
```

相关声明：[VIDEO_MIPI_CSI2_DT_EMBEDDED_8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga2b16d411ffcbcc7e74fa6aa2966b4b0d)。

嵌入式 8 位数据（Embedded 8-bit Data）：传感器元数据或配置数据。

<a id="r_gab8001106ce7c91573012a895a4b3f1a8"></a>

```c
#define VIDEO_MIPI_CSI2_DT_YUV420_8 0x18
```

相关声明：[VIDEO_MIPI_CSI2_DT_YUV420_8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gab8001106ce7c91573012a895a4b3f1a8)。

YUV 4:2:0 格式，每分量（Component）8 位。

<a id="r_ga65dac1b59e00cb26e9af9e39663b20f0"></a>

```c
#define VIDEO_MIPI_CSI2_DT_YUV420_10 0x19
```

相关声明：[VIDEO_MIPI_CSI2_DT_YUV420_10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga65dac1b59e00cb26e9af9e39663b20f0)。

YUV 4:2:0 格式，每分量（Component）10 位。

<a id="r_ga9c40ffb7a4042dd9d149e960eeddd14e"></a>

```c
#define VIDEO_MIPI_CSI2_DT_YUV420_CSPS_8 0x1c
```

相关声明：[VIDEO_MIPI_CSI2_DT_YUV420_CSPS_8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga9c40ffb7a4042dd9d149e960eeddd14e)。

YUV 4:2:0 色度移位像素采样（Chroma Shifted Pixel Sampling，CSPS）8 位格式。

<a id="r_gad1d445cd3b576e4c7062f0a06f8dc71e"></a>

```c
#define VIDEO_MIPI_CSI2_DT_YUV420_CSPS_10 0x1d
```

相关声明：[VIDEO_MIPI_CSI2_DT_YUV420_CSPS_10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gad1d445cd3b576e4c7062f0a06f8dc71e)。

YUV 4:2:0 色度移位像素采样（Chroma Shifted Pixel Sampling，CSPS）10 位格式。

<a id="r_ga18dac33c3f8afd80e08d69ed78aee5a9"></a>

```c
#define VIDEO_MIPI_CSI2_DT_YUV422_8 0x1e
```

相关声明：[VIDEO_MIPI_CSI2_DT_YUV422_8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga18dac33c3f8afd80e08d69ed78aee5a9)。

YUV 4:2:2 格式，每分量（Component）8 位。

<a id="r_ga4b530659596536d30168161139cc46fb"></a>

```c
#define VIDEO_MIPI_CSI2_DT_YUV422_10 0x1f
```

相关声明：[VIDEO_MIPI_CSI2_DT_YUV422_10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga4b530659596536d30168161139cc46fb)。

YUV 4:2:2 格式，每分量（Component）10 位。

<a id="r_ga04efc97a4dab0af7c7266ab104b8d626"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RGB444 0x20
```

相关声明：[VIDEO_MIPI_CSI2_DT_RGB444](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga04efc97a4dab0af7c7266ab104b8d626)。

RGB 格式，每颜色分量（Color Component）4 位。

<a id="r_ga351c2045810bb786d8232162f47fee7d"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RGB555 0x21
```

相关声明：[VIDEO_MIPI_CSI2_DT_RGB555](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga351c2045810bb786d8232162f47fee7d)。

RGB 格式，每颜色分量（Color Component）5 位。

<a id="r_gad5f04e5dd3d5e0c5f67c64e28cd91c56"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RGB565 0x22
```

相关声明：[VIDEO_MIPI_CSI2_DT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gad5f04e5dd3d5e0c5f67c64e28cd91c56)。

RGB 格式，R、G、B 分量依次为 5、6、5 位。

<a id="r_gaa452375e0454fa314eb140bac3c07e67"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RGB666 0x23
```

相关声明：[VIDEO_MIPI_CSI2_DT_RGB666](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gaa452375e0454fa314eb140bac3c07e67)。

RGB 格式，每颜色分量（Color Component）6 位。

<a id="r_ga0d637375f7bf081967135139a8f6c5b6"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RGB888 0x24
```

相关声明：[VIDEO_MIPI_CSI2_DT_RGB888](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga0d637375f7bf081967135139a8f6c5b6)。

RGB 格式，每颜色分量（Color Component）8 位。

<a id="r_gad251376f21a56d05742fcb68d228a677"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RAW6 0x28
```

相关声明：[VIDEO_MIPI_CSI2_DT_RAW6](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gad251376f21a56d05742fcb68d228a677)。

传感器原始数据（Raw Sensor Data），每像素 6 位。

<a id="r_ga384e8203e1bb7208a4bcb1e4931a929b"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RAW7 0x29
```

相关声明：[VIDEO_MIPI_CSI2_DT_RAW7](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga384e8203e1bb7208a4bcb1e4931a929b)。

传感器原始数据（Raw Sensor Data），每像素 7 位。

<a id="r_ga6d3881edac75ba2c12185dc119311945"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RAW8 0x2a
```

相关声明：[VIDEO_MIPI_CSI2_DT_RAW8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga6d3881edac75ba2c12185dc119311945)。

传感器原始数据（Raw Sensor Data），每像素 8 位。

<a id="r_ga64a52402a6883cb1b23a5524418528a9"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RAW10 0x2b
```

相关声明：[VIDEO_MIPI_CSI2_DT_RAW10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga64a52402a6883cb1b23a5524418528a9)。

传感器原始数据（Raw Sensor Data），每像素 10 位。

<a id="r_gadadb66f582b5e014336e29c1dafc3631"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RAW12 0x2c
```

相关声明：[VIDEO_MIPI_CSI2_DT_RAW12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gadadb66f582b5e014336e29c1dafc3631)。

传感器原始数据（Raw Sensor Data），每像素 12 位。

<a id="r_ga2ad6b8870c5dca6a8d19b1f80d83b81b"></a>

```c
#define VIDEO_MIPI_CSI2_DT_RAW14 0x2d
```

相关声明：[VIDEO_MIPI_CSI2_DT_RAW14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga2ad6b8870c5dca6a8d19b1f80d83b81b)。

传感器原始数据（Raw Sensor Data），每像素 14 位。

<a id="r_ga98885f3584261947dd2b325bf12b2f3d"></a>

```c
#define VIDEO_MIPI_CSI2_DT_USER(n)
```

相关声明：[VIDEO_MIPI_CSI2_DT_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga98885f3584261947dd2b325bf12b2f3d)。

生成用户自定义数据类型（User-defined Data Type）的宏。

<a id="r_gac50ea4ef6af09f0a6f72315db2ccd2d9"></a>

```c
static uint8_t video_mipi_data_type (uint32_t pixfmt)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[video_mipi_data_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gac50ea4ef6af09f0a6f72315db2ccd2d9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将像素格式（Pixel Formats）映射为对应的 MIPI 数据类型（Data Type）。


## 9.7\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/sys/dlist.h](../dlist_reference/P003_双向链表头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/video/video.h](../api_source_reference/P908_video.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P183_video.h_源码浏览.md)
- [video_device](../audio_video_model_reference/P057_video_device_结构体.md)
- [video_ctrl](../audio_video_model_reference/P054_video_ctrl_结构体.md)
- [video_driver_api](../audio_video_model_reference/P058_video_driver_api_结构体.md)
- [VIDEO_CTRL_FLAG_READ_ONLY](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#gac5b71618fa28d839fcca8a3aba2588e3)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [VIDEO_CTRL_FLAG_WRITE_ONLY](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ga9c09aef246638ff0a81bcfdbc83f14b5)
- [VIDEO_CTRL_FLAG_VOLATILE](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ga379d50aa61ccc522e3051fb249ecb404)
- [VIDEO_CTRL_FLAG_INACTIVE](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ga2dc6cfe5e71aa00a54bca525995fc8dc)
- [VIDEO_CTRL_FLAG_UPDATE](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ga301ff065c2ebe9a39ff8a5aafbe25d5f)
- [video_api_format_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga964b301e45a42aa78799a1d9c9297ab1)
- [device](../device_reference/P002_设备对象结构.md)
- [video_format](../audio_video_model_reference/P059_video_format_结构体.md)
- [video_api_frmival_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#gaf63180944041a9e934c9f7567bdc1b88)
- [video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)
- [video_api_enum_frmival_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga026c9a4531a125339e69b81f75343555)
- [video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)
- [video_api_enqueue_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#gae6849a22140b3507bab219b579bc3d40)
- [video_buffer](../audio_video_model_reference/P051_video_buffer_结构体.md)
- [video_api_dequeue_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga4265087c8faf62bbc36e88c0587022a1)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [video_api_flush_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga990ba001531c7300a06ca02d64c31eaa)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [video_api_set_stream_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#gacda90bacb17a53e0bd11e5bfd37be57a)
- [video_buf_type](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gad386b2994b56844ebe713f156b9dfe4e)
- [video_api_ctrl_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga522b4027fc6f22bf59f4face3c97e303)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [video_api_get_caps_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga070cb5f5bf35b98e2e7dda3378114780)
- [video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)
- [video_api_transform_cap_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#ga0a9e2ed76720f172b1b668e79220e968)
- [video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [video_api_set_signal_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#gad5aacb1386785a3587d41844c7854f83)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [video_api_selection_t](../api_video_event_topic_reference/P011_视频驱动后端 API.md#gab4d2eb34f8ccc95fa6dcda7848f4408a)
- [video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)
- [video_ctrl_type](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#gaf6e4edb13feb3bd422e19c438b435687)
- [VIDEO_CTRL_TYPE_BOOLEAN](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ggaf6e4edb13feb3bd422e19c438b435687a7568dcc1abd061f4eaadd5f487523736)
- [VIDEO_CTRL_TYPE_INTEGER](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ggaf6e4edb13feb3bd422e19c438b435687a0a353803ba2af5f06c363b8d630e93bc)
- [VIDEO_CTRL_TYPE_INTEGER64](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ggaf6e4edb13feb3bd422e19c438b435687ab2f378c2985335e39648fa200d9b7a13)
- [VIDEO_CTRL_TYPE_MENU](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ggaf6e4edb13feb3bd422e19c438b435687a05a03f70b04c1ee7e05547cda9917950)
- [VIDEO_CTRL_TYPE_STRING](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ggaf6e4edb13feb3bd422e19c438b435687a06666e95282ce67b10a46ee8d32309a3)
- [VIDEO_CTRL_TYPE_INTEGER_MENU](../api_interaction_transport_topic_reference/P020_视频控制项（Video Controls）.md#ggaf6e4edb13feb3bd422e19c438b435687a13da0d22cf3e12652424ca0d35f09071)
- [video_find_vdev](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga3d31ffde89ef76e72855ded34c6deb3c)
- [video_driver_set_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga9a29705addc34c59eb6406dd37519eaf)
- [video_driver_get_format](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gabd3ca5bdb2915a78fd12182fde435c30)
- [video_driver_set_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga57016218645ba4d98bab320545b80f1c)
- [video_driver_get_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga4eb2460636e70ddfa1b6f5187d882bfe)
- [video_driver_enum_frmival](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga26d096ae93185ed1157a75d429dd145d)
- [video_driver_enqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gae73ac504f2d726ab9a88bc35e0e25b09)
- [video_driver_dequeue](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gaaf4610cbab1caaf95070b7366cb4c4c6)
- [video_driver_flush](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga8ddced08604291df2eec55aadc3c217c)
- [video_driver_set_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga8c19eb99330402975f6e6630e1b91436)
- [video_driver_get_volatile_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga15d602806f0c30a1c28bcba7cf1fe82a)
- [video_driver_set_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga211f219e42890a6788b448c1c23fcd84)
- [video_driver_get_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga85a3064db275074f31494a364d17b51f)
- [video_driver_transform_cap](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga224e26d848ff68d10452dd4d2a44fba5)
- [video_driver_set_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga6f8b1924bf4a0ee1d7315a8e472614eb)
- [video_driver_set_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gafc494071abdfb4c38dff515bda316379)
- [video_driver_get_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga2037f560bb9a7a83d6cb23787d7bf167)
- [VIDEO_MIPI_CSI2_DT_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga59d6f35198b6412a9aa78c094ecfaa19)
- [VIDEO_MIPI_CSI2_DT_BLANKING](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gaede52c3391311b7cf931665afdeed720)
- [VIDEO_MIPI_CSI2_DT_EMBEDDED_8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga2b16d411ffcbcc7e74fa6aa2966b4b0d)
- [VIDEO_MIPI_CSI2_DT_YUV420_8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gab8001106ce7c91573012a895a4b3f1a8)
- [VIDEO_MIPI_CSI2_DT_YUV420_10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga65dac1b59e00cb26e9af9e39663b20f0)
- [VIDEO_MIPI_CSI2_DT_YUV420_CSPS_8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga9c40ffb7a4042dd9d149e960eeddd14e)
- [VIDEO_MIPI_CSI2_DT_YUV420_CSPS_10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gad1d445cd3b576e4c7062f0a06f8dc71e)
- [VIDEO_MIPI_CSI2_DT_YUV422_8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga18dac33c3f8afd80e08d69ed78aee5a9)
- [VIDEO_MIPI_CSI2_DT_YUV422_10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga4b530659596536d30168161139cc46fb)
- [VIDEO_MIPI_CSI2_DT_RGB444](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga04efc97a4dab0af7c7266ab104b8d626)
- [VIDEO_MIPI_CSI2_DT_RGB555](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga351c2045810bb786d8232162f47fee7d)
- [VIDEO_MIPI_CSI2_DT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gad5f04e5dd3d5e0c5f67c64e28cd91c56)
- [VIDEO_MIPI_CSI2_DT_RGB666](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gaa452375e0454fa314eb140bac3c07e67)
- [VIDEO_MIPI_CSI2_DT_RGB888](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga0d637375f7bf081967135139a8f6c5b6)
- [VIDEO_MIPI_CSI2_DT_RAW6](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gad251376f21a56d05742fcb68d228a677)
- [VIDEO_MIPI_CSI2_DT_RAW7](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga384e8203e1bb7208a4bcb1e4931a929b)
- [VIDEO_MIPI_CSI2_DT_RAW8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga6d3881edac75ba2c12185dc119311945)
- [VIDEO_MIPI_CSI2_DT_RAW10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga64a52402a6883cb1b23a5524418528a9)
- [VIDEO_MIPI_CSI2_DT_RAW12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gadadb66f582b5e014336e29c1dafc3631)
- [VIDEO_MIPI_CSI2_DT_RAW14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga2ad6b8870c5dca6a8d19b1f80d83b81b)
- [VIDEO_MIPI_CSI2_DT_USER](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga98885f3584261947dd2b325bf12b2f3d)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [video_mipi_data_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#gac50ea4ef6af09f0a6f72315db2ccd2d9)

<a id="header-details"></a>

---

[上一章](P008_zephyr__drivers__sensor__pac194x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__dt-bindings__pinctrl__em32f967-pinctrl.h_文件参考.md)
