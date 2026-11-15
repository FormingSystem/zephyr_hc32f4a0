---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-20
title: 视频控制项（Video Controls）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_视频控制项（Video Controls）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__ctrls.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

访问驱动程序视频控制项时使用的类型。

<a id="details"></a>

访问驱动程序视频控制项时使用的类型。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 20.1\_数据结构（Data Structures）

<a id="r_video_5Fctrl"></a>

```c
struct video_ctrl
```

相关声明：[video_ctrl](../audio_video_model_reference/P054_video_ctrl_结构体.md)。

视频控制项（Video Controls）的存储类型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.2\_宏定义（Macros）

<a id="r_gac5b71618fa28d839fcca8a3aba2588e3"></a>

```c
#define VIDEO_CTRL_FLAG_READ_ONLY BIT(0)
```

相关声明：[VIDEO_CTRL_FLAG_READ_ONLY](#gac5b71618fa28d839fcca8a3aba2588e3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控件（Control）为只读（Read-only）。

<a id="r_ga9c09aef246638ff0a81bcfdbc83f14b5"></a>

```c
#define VIDEO_CTRL_FLAG_WRITE_ONLY BIT(1)
```

相关声明：[VIDEO_CTRL_FLAG_WRITE_ONLY](#ga9c09aef246638ff0a81bcfdbc83f14b5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控件（Control）为只写（Write-only）。

<a id="r_ga379d50aa61ccc522e3051fb249ecb404"></a>

```c
#define VIDEO_CTRL_FLAG_VOLATILE BIT(2)
```

相关声明：[VIDEO_CTRL_FLAG_VOLATILE](#ga379d50aa61ccc522e3051fb249ecb404)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

由硬件持续更新、因而每次都需要重新读取的控件（Control）。

<a id="r_ga2dc6cfe5e71aa00a54bca525995fc8dc"></a>

```c
#define VIDEO_CTRL_FLAG_INACTIVE BIT(3)
```

相关声明：[VIDEO_CTRL_FLAG_INACTIVE](#ga2dc6cfe5e71aa00a54bca525995fc8dc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控件（Control）处于非活动状态（Inactive），例如：

<a id="r_ga301ff065c2ebe9a39ff8a5aafbe25d5f"></a>

```c
#define VIDEO_CTRL_FLAG_UPDATE BIT(4)
```

相关声明：[VIDEO_CTRL_FLAG_UPDATE](#ga301ff065c2ebe9a39ff8a5aafbe25d5f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

会影响其他控件的控件（Control），例如：

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 20.3\_枚举（Enumerations）

<a id="r_gaf6e4edb13feb3bd422e19c438b435687"></a>

```c
enum video_ctrl_type { VIDEO_CTRL_TYPE_BOOLEAN = 1 , VIDEO_CTRL_TYPE_INTEGER = 2 , VIDEO_CTRL_TYPE_INTEGER64 = 3 , VIDEO_CTRL_TYPE_MENU = 4 , VIDEO_CTRL_TYPE_STRING = 5 , VIDEO_CTRL_TYPE_INTEGER_MENU = 6 }
```

相关声明：[video_ctrl_type](#gaf6e4edb13feb3bd422e19c438b435687)、[VIDEO_CTRL_TYPE_BOOLEAN](#ggaf6e4edb13feb3bd422e19c438b435687a7568dcc1abd061f4eaadd5f487523736)、[VIDEO_CTRL_TYPE_INTEGER](#ggaf6e4edb13feb3bd422e19c438b435687a0a353803ba2af5f06c363b8d630e93bc)、[VIDEO_CTRL_TYPE_INTEGER64](#ggaf6e4edb13feb3bd422e19c438b435687ab2f378c2985335e39648fa200d9b7a13)、[VIDEO_CTRL_TYPE_MENU](#ggaf6e4edb13feb3bd422e19c438b435687a05a03f70b04c1ee7e05547cda9917950)、[VIDEO_CTRL_TYPE_STRING](#ggaf6e4edb13feb3bd422e19c438b435687a06666e95282ce67b10a46ee8d32309a3)、[VIDEO_CTRL_TYPE_INTEGER_MENU](#ggaf6e4edb13feb3bd422e19c438b435687a13da0d22cf3e12652424ca0d35f09071)。

视频控件（Video Control）的类型。

## 20.4\_详细说明（Detailed Documentation）

<a id="ga2dc6cfe5e71aa00a54bca525995fc8dc"></a>

### `VIDEO_CTRL_FLAG_INACTIVE`

```c
#define VIDEO_CTRL_FLAG_INACTIVE BIT(3)
```

```c
#include <zephyr/drivers/video.h>
```

控件（Control）处于非活动状态（Inactive），例如：

处于自动模式（Automatic Mode）的自动控件簇（Autocluster）中的手动控件（Manual Controls）。

<a id="gac5b71618fa28d839fcca8a3aba2588e3"></a>

### `VIDEO_CTRL_FLAG_READ_ONLY`

```c
#define VIDEO_CTRL_FLAG_READ_ONLY BIT(0)
```

```c
#include <zephyr/drivers/video.h>
```

控件（Control）为只读（Read-only）。

<a id="ga301ff065c2ebe9a39ff8a5aafbe25d5f"></a>

### `VIDEO_CTRL_FLAG_UPDATE`

```c
#define VIDEO_CTRL_FLAG_UPDATE BIT(4)
```

```c
#include <zephyr/drivers/video.h>
```

会影响其他控件的控件（Control），例如：

控件簇（Cluster）的主控件（Primary Control）。

<a id="ga379d50aa61ccc522e3051fb249ecb404"></a>

### `VIDEO_CTRL_FLAG_VOLATILE`

```c
#define VIDEO_CTRL_FLAG_VOLATILE BIT(2)
```

```c
#include <zephyr/drivers/video.h>
```

由硬件持续更新、因而每次都需要重新读取的控件（Control）。

<a id="ga9c09aef246638ff0a81bcfdbc83f14b5"></a>

### `VIDEO_CTRL_FLAG_WRITE_ONLY`

```c
#define VIDEO_CTRL_FLAG_WRITE_ONLY BIT(1)
```

```c
#include <zephyr/drivers/video.h>
```

控件（Control）为只写（Write-only）。

<a id="gaf6e4edb13feb3bd422e19c438b435687"></a>

### `video_ctrl_type`

```c
enum video_ctrl_type
```

```c
#include <zephyr/drivers/video.h>
```

视频控件（Video Control）的类型。

这也会影响大小（32 位或 64 位）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VIDEO_CTRL_TYPE_BOOLEAN` | 布尔类型（Boolean Type）。 |
| `VIDEO_CTRL_TYPE_INTEGER` | 整数类型（Integer Type）。 |
| `VIDEO_CTRL_TYPE_INTEGER64` | 64 位整数类型（64-bit Integer Type）。 |
| `VIDEO_CTRL_TYPE_MENU` | 菜单字符串类型（Menu String Type），使用标准菜单或驱动定义的菜单。 |
| `VIDEO_CTRL_TYPE_STRING` | 字符串类型（String Type）。 |
| `VIDEO_CTRL_TYPE_INTEGER_MENU` | 菜单整数类型（Menu Integer Type），使用标准菜单或驱动定义的菜单。 |


## 20.5\_原页交叉引用（Cross References）

- [video_ctrl](../audio_video_model_reference/P054_video_ctrl_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [zephyr/drivers/video.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaf6e4edb13feb3bd422e19c438b435687a7568dcc1abd061f4eaadd5f487523736"></a>
<a id="ggaf6e4edb13feb3bd422e19c438b435687a0a353803ba2af5f06c363b8d630e93bc"></a>
<a id="ggaf6e4edb13feb3bd422e19c438b435687ab2f378c2985335e39648fa200d9b7a13"></a>
<a id="ggaf6e4edb13feb3bd422e19c438b435687a05a03f70b04c1ee7e05547cda9917950"></a>
<a id="ggaf6e4edb13feb3bd422e19c438b435687a06666e95282ce67b10a46ee8d32309a3"></a>
<a id="ggaf6e4edb13feb3bd422e19c438b435687a13da0d22cf3e12652424ca0d35f09071"></a>

---

[上一章](P019_TMP451 API主题.md) · [返回大纲](大纲.md)
