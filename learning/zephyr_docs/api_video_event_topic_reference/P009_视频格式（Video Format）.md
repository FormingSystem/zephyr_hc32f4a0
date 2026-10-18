---
id: learning.zephyr-docs.api-video-event-topic-reference.page-9
title: 视频格式（Video Format）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_视频格式（Video Format）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频格式 API。

<a id="details"></a>

视频格式 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.1\_函数（Functions）

<a id="r_ga774ef89a7321a6842890005ad53c1594"></a>

```c
int video_estimate_fmt_size (struct video_format *fmt)
```

相关声明：[video_estimate_fmt_size](#ga774ef89a7321a6842890005ad53c1594)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

估算 `video_format` 的大小和行跨度（Pitch），单位为字节。

<a id="r_ga9de739567bff0a8ce915d389294e35ec"></a>

```c
int video_set_compose_format (const struct device *dev, struct video_format *fmt)
```

相关声明：[video_set_compose_format](#ga9de739567bff0a8ce915d389294e35ec)、[device](../device_reference/P002_设备对象结构.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

设置格式前先设置合成矩形（Compose Rectangle），如果适用。

<a id="r_ga1deb2dbafd7f4eeb602a3f78aaeb5e33"></a>

```c
int video_set_format (const struct device *dev, struct video_format *fmt)
```

相关声明：[video_set_format](#ga1deb2dbafd7f4eeb602a3f78aaeb5e33)、[device](../device_reference/P002_设备对象结构.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

设置视频格式（Video Format）。

<a id="r_ga8db8c17f3cb418e44620816e9a5cf706"></a>

```c
int video_get_format (const struct device *dev, struct video_format *fmt)
```

相关声明：[video_get_format](#ga8db8c17f3cb418e44620816e9a5cf706)、[device](../device_reference/P002_设备对象结构.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

获取驱动的视频格式（Video Format）。

<a id="r_ga6ea31432d37e0f8f46e0f6c2690ee3e9"></a>

```c
int video_set_selection (const struct device *dev, struct video_selection *sel)
```

相关声明：[video_set_selection](#ga6ea31432d37e0f8f46e0f6c2690ee3e9)、[device](../device_reference/P002_设备对象结构.md)、[video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)。

设置视频选区（Video Selection），即裁剪／合成（Crop/Compose）。

<a id="r_ga0c30d2802c82b28cbb5029e7bc52b5b4"></a>

```c
int video_get_selection (const struct device *dev, struct video_selection *sel)
```

相关声明：[video_get_selection](#ga0c30d2802c82b28cbb5029e7bc52b5b4)、[device](../device_reference/P002_设备对象结构.md)、[video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)。

获取视频选区（Video Selection），即裁剪／合成（Crop/Compose）。

## 9.2\_详细说明（Detailed Documentation）

<a id="ga774ef89a7321a6842890005ad53c1594"></a>

### `video_estimate_fmt_size()`

```c
int video_estimate_fmt_size ( struct video_format * fmt)
```

```c
#include <zephyr/video/video.h>
```

估算 `video_format` 的大小和行跨度（Pitch），单位为字节。

仅支持完整图像帧（Whole Image Frame）的驱动应使用此辅助函数。

对于未压缩格式（Uncompressed Formats），返回整个原始图像的实际大小和行跨度（Pitch），不包含任何填充（Padding）。

对于压缩格式（Compressed Formats），返回一个完整压缩帧大小的粗略估计。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fmt` | 指向视频格式结构体（Video Format Structure）的指针。 |

**返回（Returns）**：返回值：成功返回 0，否则返回负 errno 错误码。

<a id="ga8db8c17f3cb418e44620816e9a5cf706"></a>

### `video_get_format()`

```c
int video_get_format ( const struct device * dev, struct video_format * fmt )
```

```c
#include <zephyr/video/video.h>
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
| `pointer` | 指向视频格式（Video Format）。 |

<a id="ga0c30d2802c82b28cbb5029e7bc52b5b4"></a>

### `video_get_selection()`

```c
int video_get_selection ( const struct device * dev, struct video_selection * sel )
```

```c
#include <zephyr/video/video.h>
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
| `0` | 成功时。 |
| `-EINVAL` | 参数无效（Invalid Parameters）时。 |
| `-ENOTSUP` | 不支持该格式（Format）时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |

<a id="ga9de739567bff0a8ce915d389294e35ec"></a>

### `video_set_compose_format()`

```c
int video_set_compose_format ( const struct device * dev, struct video_format * fmt )
```

```c
#include <zephyr/video/video.h>
```

设置格式前先设置合成矩形（Compose Rectangle），如果适用。

某些设备提供合成能力（Compose Capabilities），可对帧进行缩小／放大（Downscale/Upscale）变换。对于这些设备，必须先设置合成矩形（Compose Rectangle），然后才能应用帧格式；帧格式的宽／高必须与合成矩形的宽／高相同。为使不了解合成机制的应用也能控制这类设备，提供此辅助函数：若设备支持，先应用合成矩形，再设置格式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向要设置格式的视频设备结构体（Video Device Struct）的指针。 |
| `fmt` | 指向视频格式结构体（Video Format Struct）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时（Successful）。 |
| `-EINVAL` | 参数无效（Invalid Parameters）时。 |
| `-ENOTSUP` | 不支持该格式（Format）时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |

<a id="ga1deb2dbafd7f4eeb602a3f78aaeb5e33"></a>

### `video_set_format()`

```c
int video_set_format ( const struct device * dev, struct video_format * fmt )
```

```c
#include <zephyr/video/video.h>
```

设置视频格式（Video Format）。

将视频设备配置为指定格式（Format）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `fmt` | 指向视频格式结构体（Video Format Struct）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 参数无效（Invalid Parameters）时。 |
| `-ENOTSUP` | 不支持该格式（Format）时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |

<a id="ga6ea31432d37e0f8f46e0f6c2690ee3e9"></a>

### `video_set_selection()`

```c
int video_set_selection ( const struct device * dev, struct video_selection * sel )
```

```c
#include <zephyr/video/video.h>
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
| `0` | 成功时。 |
| `-EINVAL` | 参数无效（Invalid Parameters）时。 |
| `-ENOTSUP` | 不支持该格式（Format）时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |


## 9.3\_原页交叉引用（Cross References）

- [video_format](../audio_video_model_reference/P059_video_format_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [video_selection](../audio_video_model_reference/P065_video_selection_结构体.md)
- [zephyr/video/video.h](../api_file_host_video_reference/P012_zephyr__video__video.h_文件参考.md)
- [VIDEO_SEL_TGT_CROP](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#ggae375c0586e3505632cc69348935c9b54aa42c3de3eeefb5340a2a1877ec8c4b17)
- [VIDEO_SEL_TGT_COMPOSE](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#ggae375c0586e3505632cc69348935c9b54a0558ad68bff086cd3ff3f82b53946f49)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_视频缓冲区（Video Buffers）.md) · [返回大纲](大纲.md) · [下一章](P010_视频帧间隔（Video Frame Interval）.md)
