---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-4
title: FTDI FT8xx API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_FTDI FT8xx API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FTDI FT8xx 图形控制器接口。

<a id="details"></a>

FTDI FT8xx 图形控制器接口。

<a id="header-groups"></a>
<a id="groups"></a>

## 4.1\_主题（Topics）

<a id="r_ft8xx_5Fcopro"></a>

相关声明：[FT8xx 协处理器（Co-processor）](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html)。

FT8xx 协处理器引擎函数。

<a id="r_ft8xx_5Fcommon"></a>

相关声明：[FT8xx 通用函数](../api_device_topic_reference/P010_FT8xx 通用函数.md)。

FT8xx 内存读写函数。

<a id="r_ft8xx_5Fdl"></a>

相关声明：[FT8xx 显示列表（Display list）](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html)。

FT8xx 显示列表命令。

<a id="r_ft8xx_5Fmemory"></a>

相关声明：[FT8xx 内存映射（Memory map）](../api_service_topic_reference/P010_FT8xx 内存映射（Memory map）.md)。

FT8xx 内存地址。

<a id="r_ft8xx_5Freference_5Fapi"></a>

相关声明：[FT8xx 参考 API](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html)。

FT8xx 参考 API

<a id="header-files"></a>
<a id="files"></a>

## 4.2\_文件（Files）

<a id="r_ft8xx_2Eh"></a>

```c
file ft8xx.h
```

相关声明：[ft8xx.h](../api_file_management_reference/P016_zephyr__drivers__misc__ft8xx__ft8xx.h_文件参考.md)。

FT8XX公共API（Public API）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.3\_数据结构（Data Structures）

<a id="r_ft8xx_5Ftouch_5Ftransform"></a>

```c
struct ft8xx_touch_transform
```

相关声明：[ft8xx_touch_transform](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md)。

保存触摸屏校准数据（Touchscreen Calibration Data）的结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.4\_类型定义（Typedefs）

<a id="r_ga846a90d72b56f388d5b4f60cf6d658b0"></a>

```c
typedef void(* ft8xx_int_callback) (const struct device *dev, void *user_data)
```

相关声明：[ft8xx_int_callback](#ga846a90d72b56f388d5b4f60cf6d658b0)、[device](../device_reference/P002_设备对象结构.md)。

用于通知 API 用户 FT8xx 已触发中断的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.5\_函数（Functions）

<a id="r_ga586f6ff1eddd5b596d2e35fb5fdd8148"></a>

```c
void ft8xx_calibrate (const struct device *dev, struct ft8xx_touch_transform *data)
```

相关声明：[ft8xx_calibrate](#ga586f6ff1eddd5b596d2e35fb5fdd8148)、[device](../device_reference/P002_设备对象结构.md)、[ft8xx_touch_transform](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md)。

校准触摸屏（touchscreen calibration）。

<a id="r_ga1d74a13782c6ab9f8b07a28503058356"></a>

```c
void ft8xx_touch_transform_set (const struct device *dev, const struct ft8xx_touch_transform *data)
```

相关声明：[ft8xx_touch_transform_set](#ga1d74a13782c6ab9f8b07a28503058356)、[device](../device_reference/P002_设备对象结构.md)、[ft8xx_touch_transform](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md)。

设置触摸屏校准数据。

<a id="r_gaea3589b5a0aa34a09a81ea15c1595219"></a>

```c
int ft8xx_get_touch_tag (const struct device *dev)
```

相关声明：[ft8xx_get_touch_tag](#gaea3589b5a0aa34a09a81ea15c1595219)、[device](../device_reference/P002_设备对象结构.md)。

获取最近触摸元素的标签（tag）。

<a id="r_ga1c9ade4374b9619c68efa11dd1a56eae"></a>

```c
uint32_t ft8xx_get_tracker_value (const struct device *dev)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[ft8xx_get_tracker_value](#ga1c9ade4374b9619c68efa11dd1a56eae)、[device](../device_reference/P002_设备对象结构.md)。

获取被跟踪对象的标签及跟踪值（tracking value）。

<a id="r_gaf392199312ddb82451a4f31e2955079d"></a>

```c
void ft8xx_register_int (const struct device *dev, ft8xx_int_callback callback, void *user_data)
```

相关声明：[ft8xx_register_int](#gaf392199312ddb82451a4f31e2955079d)、[device](../device_reference/P002_设备对象结构.md)、[ft8xx_int_callback](#ga846a90d72b56f388d5b4f60cf6d658b0)。

设置 FT8xx 触发中断时执行的回调。

## 4.6\_详细说明（Detailed Documentation）

<a id="ga846a90d72b56f388d5b4f60cf6d658b0"></a>

### `ft8xx_int_callback`

```c
typedef void(* ft8xx_int_callback) (const struct device *dev, void *user_data)
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx.h>
```

用于通知 API 用户 FT8xx 已触发中断的回调 API。

在中断请求（IRQ）上下文调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `user_data` | 指向注册回调时提供的用户数据（User Data）的指针。 |

<a id="ga586f6ff1eddd5b596d2e35fb5fdd8148"></a>

### `ft8xx_calibrate()`

```c
void ft8xx_calibrate ( const struct device * dev, struct ft8xx_touch_transform * data )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx.h>
```

校准触摸屏（touchscreen calibration）。

执行触摸屏校准（Touchscreen Calibration），从触摸屏收集三次触摸。计算出的校准结果会自动应用到触摸屏处理流程，并通过 `data` 返回。

可以保存 `data` 内容，复位后通过 `ft8xx_touch_transform_set()` 使用，从而无需每次设备复位后重新校准触摸屏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `data` | 指向待填充的触摸屏变换结构体（Touchscreen Transform Structure）的指针。 |

<a id="gaea3589b5a0aa34a09a81ea15c1595219"></a>

### `ft8xx_get_touch_tag()`

```c
int ft8xx_get_touch_tag ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx.h>
```

获取最近触摸元素的标签（tag）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：**返回值（Returns）：**最近被触摸元素的标签（Tag）值，范围为 0–255。

<a id="ga1c9ade4374b9619c68efa11dd1a56eae"></a>

### `ft8xx_get_tracker_value()`

```c
uint32_t ft8xx_get_tracker_value ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx.h>
```

获取被跟踪对象的标签及跟踪值（tracking value）。

报告的标签（Tag）和跟踪值（Tracking Value）对应由协处理器通过 `ft8xx_copro_cmd_track()` 跟踪的对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：**返回值（Returns）：**跟踪寄存器（Track Register）的内容，最高两个字节（掩码 `0xffff0000`）表示跟踪值，最低两个字节（掩码 `0x0000ffff`）表示标签。

<a id="gaf392199312ddb82451a4f31e2955079d"></a>

### `ft8xx_register_int()`

```c
void ft8xx_register_int ( const struct device * dev, ft8xx_int_callback callback, void * user_data )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx.h>
```

设置 FT8xx 触发中断时执行的回调。

配置 FT8xx，使触摸事件改变标签值（Tag Value）时触发中断。

触摸事件改变标签值时，FT8xx 激活 INT 线路。该线路保持有效，直到调用 `ft8xx_get_touch_tag()`；因此，在调用此函数前，回调只会执行一次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `callback` | 指向 FT8xx 触发中断时调用的函数的指针。 |
| `user_data` | 指向将传给回调的用户数据（User Data）的指针。 |

<a id="ga1d74a13782c6ab9f8b07a28503058356"></a>

### `ft8xx_touch_transform_set()`

```c
void ft8xx_touch_transform_set ( const struct device * dev, const struct ft8xx_touch_transform * data )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx.h>
```

设置触摸屏校准数据。

将指定触摸屏变换数据（Touchscreen Transform Data）应用到触摸处理流程。数据应来自 `ft8xx_calibrate()` 启动的校准过程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `data` | 指向待应用的触摸屏变换结构体的指针。 |


## 4.7\_原页交叉引用（Cross References）

- [FT8xx 协处理器（Co-processor）](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html)
- [FT8xx 通用函数](../api_device_topic_reference/P010_FT8xx 通用函数.md)
- [FT8xx 显示列表（Display list）](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html)
- [FT8xx 内存映射（Memory map）](../api_service_topic_reference/P010_FT8xx 内存映射（Memory map）.md)
- [FT8xx 参考 API](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html)
- [ft8xx.h](../api_file_management_reference/P016_zephyr__drivers__misc__ft8xx__ft8xx.h_文件参考.md)
- [ft8xx_touch_transform](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ft8xx_copro_cmd_track()](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac946f044f2fbb6381ea4af268084d828)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_SYSRSTCR 复位控制（Reset Control）.md) · [返回大纲](大纲.md) · [下一章](P005_LVGL 键盘按键（Keypad keys）.md)
