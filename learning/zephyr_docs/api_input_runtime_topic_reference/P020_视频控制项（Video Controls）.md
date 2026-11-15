---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-20
title: 视频控制项（Video Controls）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_视频控制项（Video Controls）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

操作视频控制项的 API。

<a id="details"></a>

操作视频控制项的 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.1\_函数（Functions）

<a id="r_ga1cce17a3dfc881a1080708c7bc417aac"></a>

```c
int video_set_ctrl (const struct device *dev, struct video_control *control)
```

相关声明：[video_set_ctrl](#ga1cce17a3dfc881a1080708c7bc417aac)、[device](../device_reference/P002_设备对象结构.md)、[video_control](../audio_video_model_reference/P053_video_control_结构体.md)。

设置控件值（Control Value）。

<a id="r_ga71853c720e6df1def4c945e23d103298"></a>

```c
int video_get_ctrl (const struct device *dev, struct video_control *control)
```

相关声明：[video_get_ctrl](#ga71853c720e6df1def4c945e23d103298)、[device](../device_reference/P002_设备对象结构.md)、[video_control](../audio_video_model_reference/P053_video_control_结构体.md)。

获取控件当前值（Current Control Value）。

<a id="r_ga8813a656a66adc6bfb10fb7f27194898"></a>

```c
int video_query_ctrl (struct video_ctrl_query *cq)
```

相关声明：[video_query_ctrl](#ga8813a656a66adc6bfb10fb7f27194898)、[video_ctrl_query](../audio_video_model_reference/P055_video_ctrl_query_结构体.md)。

查询控件信息（Control Information）。

<a id="r_ga2bff04c6abc344350d6b0036289a701e"></a>

```c
void video_print_ctrl (const struct video_ctrl_query *const cq)
```

相关声明：[video_print_ctrl](#ga2bff04c6abc344350d6b0036289a701e)、[video_ctrl_query](../audio_video_model_reference/P055_video_ctrl_query_结构体.md)。

打印控件的全部信息（Control Information）。

<a id="r_ga41e450607b4dc062fac682728ec7a79d"></a>

```c
int64_t video_get_csi_link_freq (const struct device *dev, uint8_t bpp, uint8_t lane_nb)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[video_get_csi_link_freq](#ga41e450607b4dc062fac682728ec7a79d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

返回设备通告的链路频率（Link Frequency）。

## 20.2\_详细说明（Detailed Documentation）

<a id="ga41e450607b4dc062fac682728ec7a79d"></a>

### `video_get_csi_link_freq()`

```c
int64_t video_get_csi_link_freq ( const struct device * dev, uint8_t bpp, uint8_t lane_nb )
```

```c
#include <zephyr/video/video.h>
```

返回设备通告的链路频率（Link Frequency）。

提供摄像机串行接口（CSI）链路的设备应至少通告下列两个控件之一：

- `VIDEO_CID_LINK_FREQ`（链路频率）。
- `VIDEO_CID_PIXEL_RATE`（像素速率）。

辅助函数先尝试读取 `VIDEO_CID_LINK_FREQ`。如果不可用，则结合格式的每像素位数（Bits per Pixel）和通道数量（Number of Lanes），根据 `VIDEO_CID_PIXEL_RATE` 估算链路频率（Link Frequency）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 要查询的视频设备（Video Device）。 |
| `bpp` | 设备输出像素格式的每像素位数（Bits per Pixel）。 |
| `lane_nb` | 使用的 CSI-2 通道数量（Number of Lanes）。 |

<a id="ga71853c720e6df1def4c945e23d103298"></a>

### `video_get_ctrl()`

```c
int video_get_ctrl ( const struct device * dev, struct video_control * control )
```

```c
#include <zephyr/video/video.h>
```

获取控件当前值（Current Control Value）。

获取视频控件值（Video Control Value）。值类型取决于控件 ID，必须据此解释。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `control` | 指向视频控件结构体（Video Control Struct）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 参数无效（invalid parameters）。 |
| `-ENOTSUP` | 不支持该格式（Format）。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |

<a id="ga2bff04c6abc344350d6b0036289a701e"></a>

### `video_print_ctrl()`

```c
void video_print_ctrl ( const struct video_ctrl_query *const cq)
```

```c
#include <zephyr/video/video.h>
```

打印控件的全部信息（Control Information）。

以人类可读形式（Human-readable Format）打印控件的全部信息，包括名称、类型、标志、范围、菜单（如有）和当前值；当前值通过调用 `video_get_ctrl()` 获取。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cq` | 指向控件查询结构体（Control Query Struct）的指针。 |

<a id="ga8813a656a66adc6bfb10fb7f27194898"></a>

### `video_query_ctrl()`

```c
int video_query_ctrl ( struct video_ctrl_query * cq)
```

```c
#include <zephyr/video/video.h>
```

查询控件信息（Control Information）。

应用设置查询结构体的 `id` 字段，本函数填充其余字段。可使用从 `VIDEO_CID_BASE` 开始、到 `VIDEO_CID_LASTP1` 之前的连续 ID 调用本函数，枚举基类控件（Base Class Controls，即 `VIDEO_CID_BASE + x`）。若该范围内某控件不受支持，函数可能返回 `-ENOTSUP`。应用还可从 `VIDEO_CID_PRIVATE_BASE` 开始递增 ID，直到驱动返回 `-ENOTSUP`，以枚举私有控件（Private Controls）。其他控件类别更难按此方式处理，因此枚举设备全部受支持控件的最佳方式是使用 `VIDEO_CTRL_FLAG_NEXT_CTRL` 迭代。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cq` | 指向控件查询结构体（Control Query Struct）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 控件 ID（Control ID）无效。 |
| `-ENOTSUP` | 不支持该控件 ID（Control ID）。 |

<a id="ga1cce17a3dfc881a1080708c7bc417aac"></a>

### `video_set_ctrl()`

```c
int video_set_ctrl ( const struct device * dev, struct video_control * control )
```

```c
#include <zephyr/video/video.h>
```

设置控件值（Control Value）。

设置视频控件值（Video Control Value）。值类型取决于控件 ID，必须据此解释。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `control` | 指向视频控件结构体（Video Control Struct）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 参数无效（invalid parameters）。 |
| `-ENOTSUP` | 不支持该格式（Format）。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |


## 20.3\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [video_control](../audio_video_model_reference/P053_video_control_结构体.md)
- [video_ctrl_query](../audio_video_model_reference/P055_video_ctrl_query_结构体.md)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/video/video.h](https://docs.zephyrproject.org/latest/doxygen/html/video_2video_8h.html)
- [`VIDEO_CID_LINK_FREQ`（链路频率）。](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga2142e2819c445b70d82067a3cfb193c8)
- [`VIDEO_CID_PIXEL_RATE`（像素速率）。](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga6f6eaed7defdbb5f440874c7c6d0a6eb)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P019_TMC6460 其他功能（MISC）.md) · [返回大纲](大纲.md) · [下一章](P021_基于模块的断言处理（Module based assert handling）.md)
