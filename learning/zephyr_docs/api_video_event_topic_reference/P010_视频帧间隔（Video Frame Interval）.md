---
id: learning.zephyr-docs.api-video-event-topic-reference.page-10
title: 视频帧间隔（Video Frame Interval）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_视频帧间隔（Video Frame Interval）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频帧间隔 API。

<a id="details"></a>

视频帧间隔 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.1\_函数（Functions）

<a id="r_ga09efb2f6e1f56075cf0c44871266d634"></a>

```c
int video_enum_frmival (const struct device *dev, struct video_frmival_enum *fie)
```

相关声明：[video_enum_frmival](#ga09efb2f6e1f56075cf0c44871266d634)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)。

列出视频帧间隔（Video Frame Intervals）。

<a id="r_ga46c5bca5cd3caf762f9dd4998b6e21de"></a>

```c
int video_set_frmival (const struct device *dev, struct video_frmival *frmival)
```

相关声明：[video_set_frmival](#ga46c5bca5cd3caf762f9dd4998b6e21de)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

设置视频帧间隔（Video Frame Interval）。

<a id="r_ga2834be95778244a2446b62e673bbb187"></a>

```c
int video_get_frmival (const struct device *dev, struct video_frmival *frmival)
```

相关声明：[video_get_frmival](#ga2834be95778244a2446b62e673bbb187)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

获取驱动的视频帧间隔（Video Frame Interval）。

<a id="r_ga6b3c7456b2527cc441a100ff50787dc2"></a>

```c
static uint64_t video_frmival_nsec (const struct video_frmival *frmival)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[video_frmival_nsec](#ga6b3c7456b2527cc441a100ff50787dc2)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

计算两个帧间隔（Frame Intervals）的差值。

<a id="r_gafa448552f4257d761d96976cbe3da928"></a>

```c
int video_closest_frmival_stepwise (const struct video_frmival_stepwise *stepwise, const struct video_frmival *desired, struct video_frmival *match)
```

相关声明：[video_closest_frmival_stepwise](#gafa448552f4257d761d96976cbe3da928)、[video_frmival_stepwise](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)、[video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)。

在按步长变化的帧间隔范围（Stepwise Frame Interval）内，查找与给定帧间隔值最接近的匹配。

<a id="r_ga99722c1e31aa6b73f443c22593b76e87"></a>

```c
int video_closest_frmival (const struct device *dev, struct video_frmival_enum *match)
```

相关声明：[video_closest_frmival](#ga99722c1e31aa6b73f443c22593b76e87)、[device](../device_reference/P002_设备对象结构.md)、[video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)。

在视频设备（Video Device）支持的范围内，查找与给定帧间隔值最接近的匹配。

## 10.2\_详细说明（Detailed Documentation）

<a id="ga99722c1e31aa6b73f443c22593b76e87"></a>

### `video_closest_frmival()`

```c
int video_closest_frmival ( const struct device * dev, struct video_frmival_enum * match )
```

```c
#include <zephyr/video/video.h>
```

在视频设备（Video Device）支持的范围内，查找与给定帧间隔值最接近的匹配。

为计算最接近的匹配（Closest Match），请填充 `match` 的以下字段：

- 将 `match->format` 设为所关注的 `video_format` 视频格式。
- 将 `match->type` 设为 `VIDEO_FRMIVAL_TYPE_DISCRETE`。
- 将 `match->discrete` 设为所需帧间隔（Frame Interval）。

结果写入 `match`，并设置以下字段：

- 将 `match->discrete` 设为最接近帧间隔（Closest Frame Interval）的值。
- 将 `match->index` 设为最接近帧间隔的索引（Index）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 要查询的视频设备（Video Device）。 |
| `match` | 帧间隔枚举器（Frame Interval Enumerator），包含查询条件并接收结果。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="gafa448552f4257d761d96976cbe3da928"></a>

### `video_closest_frmival_stepwise()`

```c
int video_closest_frmival_stepwise ( const struct video_frmival_stepwise * stepwise, const struct video_frmival * desired, struct video_frmival * match )
```

```c
#include <zephyr/video/video.h>
```

在按步长变化的帧间隔范围（Stepwise Frame Interval）内，查找与给定帧间隔值最接近的匹配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stepwise` | 要搜索的步进帧间隔范围（Stepwise Frame Interval Range）。 |
| `desired` | 需要为其寻找最接近匹配的帧间隔（Frame Interval）。 |
| `match` | 与所需值最接近的结果帧间隔（Resulting Frame Interval）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 参数无效（Invalid Parameters）时。 |
| `-ERANGE` | 步长（Step）为 0，或结果无法以 32 位值表示时。 |

<a id="ga09efb2f6e1f56075cf0c44871266d634"></a>

### `video_enum_frmival()`

```c
int video_enum_frmival ( const struct device * dev, struct video_frmival_enum * fie )
```

```c
#include <zephyr/video/video.h>
```

列出视频帧间隔（Video Frame Intervals）。

列出所给格式支持的全部视频帧间隔（Video Frame Intervals）。

应用应先填充 `video_frmival_enum` 结构体的 `pixelformat`、`width` 和 `height` 字段，构成查询。然后使用 `index` 字段遍历受支持的帧间隔列表。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `fie` | 指向视频帧间隔枚举结构体（Video Frame Interval Enumeration Struct）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOSYS` | 未实现该 API 时。 |
| `-EINVAL` | 参数无效（Invalid Parameters）时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |

<a id="ga6b3c7456b2527cc441a100ff50787dc2"></a>

### `video_frmival_nsec()`

```c
uint64_t video_frmival_nsec ( const struct video_frmival * frmival)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/video/video.h>
```

计算两个帧间隔（Frame Intervals）的差值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `frmival` | 要转换为微秒的帧间隔（Frame Interval）。 |

**返回（Returns）**：返回值：以微秒表示的帧间隔（Frame Interval）值。

<a id="ga2834be95778244a2446b62e673bbb187"></a>

### `video_get_frmival()`

```c
int video_get_frmival ( const struct device * dev, struct video_frmival * frmival )
```

```c
#include <zephyr/video/video.h>
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
| `0` | 成功时。 |
| `-ENOSYS` | 未实现该 API 时。 |
| `-EINVAL` | 参数无效（Invalid Parameters）时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |

<a id="ga46c5bca5cd3caf762f9dd4998b6e21de"></a>

### `video_set_frmival()`

```c
int video_set_frmival ( const struct device * dev, struct video_frmival * frmival )
```

```c
#include <zephyr/video/video.h>
```

设置视频帧间隔（Video Frame Interval）。

为视频设备配置指定帧间隔（Frame Interval），使用驱动所能提供的最接近匹配值，并将实际应用到驱动的值回写到 `frmival`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `frmival` | 指向视频帧间隔结构体（Video Frame Interval Struct）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOSYS` | 未实现该 API 时。 |
| `-EINVAL` | 参数无效（Invalid Parameters）时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |


## 10.3\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [video_frmival_enum](../audio_video_model_reference/P062_video_frmival_enum_结构体.md)
- [video_frmival](../audio_video_model_reference/P061_video_frmival_结构体.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [video_frmival_stepwise](../audio_video_model_reference/P063_video_frmival_stepwise_结构体.md)
- [zephyr/video/video.h](../api_file_host_video_reference/P012_zephyr__video__video.h_文件参考.md)
- [video_format](../audio_video_model_reference/P059_video_format_结构体.md)
- [VIDEO_FRMIVAL_TYPE_DISCRETE](../api_power_policy_topic_reference/P012_视频类型（Video Types）.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_视频格式（Video Format）.md) · [返回大纲](大纲.md) · [下一章](P011_视频驱动后端 API.md)
