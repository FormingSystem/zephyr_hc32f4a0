---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-26
title: 视频能力（Video Capabilities）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__caps.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_视频能力（Video Capabilities）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__caps.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频能力 API。

<a id="details"></a>

视频能力 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 26.1\_函数（Functions）

<a id="r_ga1bf94d7b435524d0face3f713c4dca9d"></a>

```c
int video_get_caps (const struct device *dev, struct video_caps *caps)
```

相关声明：[video_get_caps](#ga1bf94d7b435524d0face3f713c4dca9d)、[device](../device_reference/P002_设备对象结构.md)、[video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)。

获取视频端点能力（Video Endpoint Capabilities）。

<a id="r_ga3d2d1692e4adab02948b11f38407610f"></a>

```c
int video_transform_cap (const struct device *const dev, const struct video_format_cap *const cap, struct video_format_cap *const res_cap, enum video_buf_type type, uint16_t ind)
```

相关声明：[video_transform_cap](#ga3d2d1692e4adab02948b11f38407610f)、[device](../device_reference/P002_设备对象结构.md)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将视频格式能力（Video Format Capability）从内存到内存（M2M）视频设备的一端转换到另一端。

<a id="r_gadbf59fd2d77b3d164cacf56bd4ae81ce"></a>

```c
int video_format_caps_index (const struct video_format_cap *fmts, const struct video_format *fmt, size_t *idx)
```

相关声明：[video_format_caps_index](#gadbf59fd2d77b3d164cacf56bd4ae81ce)、[video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)、[video_format](../audio_video_model_reference/P059_video_format_结构体.md)。

在能力列表（Capabilities List）中搜索匹配的格式（Format）。

## 26.2\_详细说明（Detailed Documentation）

<a id="gadbf59fd2d77b3d164cacf56bd4ae81ce"></a>

### `video_format_caps_index()`

```c
int video_format_caps_index ( const struct video_format_cap * fmts, const struct video_format * fmt, size_t * idx )
```

```c
#include <zephyr/video/video.h>
```

在能力列表（Capabilities List）中搜索匹配的格式（Format）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fmts` | 要搜索的格式能力列表（Format Capability List）。 |
| `fmt` | 要在列表中查找的格式（Format）。 |
| `idx` | 用于存储首个匹配格式编号（Number of the First Matching Format）的指针。 |

**返回（Returns）**：**返回值（Returns）：**找到格式时返回 `0`；未找到匹配格式时返回 `-ENOENT`。

<a id="ga1bf94d7b435524d0face3f713c4dca9d"></a>

### `video_get_caps()`

```c
int video_get_caps ( const struct device * dev, struct video_caps * caps )
```

```c
#include <zephyr/video/video.h>
```

获取视频端点能力（Video Endpoint Capabilities）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `caps` | 指向待填充的 `video_caps` 结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；否则返回 `-ERRNO` 错误码。 |
| `-ENOSYS` | API 尚未实现（Not Implemented）。 |

<a id="ga3d2d1692e4adab02948b11f38407610f"></a>

### `video_transform_cap()`

```c
int video_transform_cap ( const struct device *const dev, const struct video_format_cap *const cap, struct video_format_cap *const res_cap, enum video_buf_type type, uint16_t ind )
```

```c
#include <zephyr/video/video.h>
```

将视频格式能力（Video Format Capability）从内存到内存（M2M）视频设备的一端转换到另一端。

本函数将 `video_format_cap` 从内存到内存（M2M）视频设备的一端转换到另一端。给定一端的单个输入能力（Input Capability），应用可迭代获取设备另一端支持的全部能力。

应用向函数传入单个输入 `cap` 和单个结果 `res_cap` 的地址，以及 `res_cap` 的类型和从 `0` 开始的迭代索引（Index）。驱动每次填充 `res_cap` 结构体并返回 `0`。逐次递增索引获取下一个 `res_cap`，直到函数返回错误码（Errno），例如 `-EINVAL`。示例如下：

原始示例（Example）：

```c
struct video_format_cap cap = {.pixelformat = VIDEO_PIX_FMT_RGB565};
struct video_format_cap res_cap = {0};
uint8_t ind = 0;
while (video_transform_cap(dev, &cap, &res_cap, VIDEO_BUF_TYPE_OUTPUT, ind) == 0) {
     // Process output_cap here
     ind++;
}
```

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


## 26.3\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [video_caps](../audio_video_model_reference/P052_video_caps_结构体.md)
- [video_format_cap](../audio_video_model_reference/P060_video_format_cap_结构体.md)
- [video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [video_format](../audio_video_model_reference/P059_video_format_结构体.md)
- [zephyr/video/video.h](https://docs.zephyrproject.org/latest/doxygen/html/video_2video_8h.html)
- [VIDEO_PIX_FMT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf009d0eb7dbdb3bfd8883da03478c1ec)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [VIDEO_BUF_TYPE_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#ggad386b2994b56844ebe713f156b9dfe4eab51085ffb7e0d7a003dcb6b55a093083)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__video__api__caps_html_ga3d2d1692e4adab02948b11f38407610f"></a>
<a id="agroup__video__formats_html_gaf009d0eb7dbdb3bfd8883da03478c1ec"></a>
<a id="agroup__video__types_html_ggad386b2994b56844ebe713f156b9dfe4eab51085ffb7e0d7a003dcb6b55a093083"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructvideo__format__cap_html"></a>

---

[上一章](P025_VEML60XX API主题.md) · [返回大纲](大纲.md)
