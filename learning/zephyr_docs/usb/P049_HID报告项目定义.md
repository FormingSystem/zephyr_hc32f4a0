---
id: learning.zephyr-docs.usb.api-49
title: HID报告项目定义
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usb__hid__items.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_HID报告项目定义

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__hid__items.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 49.1\_阅读说明与来源

译注：本页属于[HID通用说明](P040_HID通用说明.md)及其设备接口参考，说明报告描述符、设备回调和报告传输。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第40至50章的全部字段参考。

## 49.2\_宏定义（Macros）

<a id="r_ga4e9dc6652402e0b87e1313c143737ed4"></a>

```c
#define HID_ITEM(bTag, bType, bSize)
```

定义 HID 短项目（Short Item）。

相关声明：[HID_ITEM](P049_HID报告项目定义.md#ga4e9dc6652402e0b87e1313c143737ed4)。

<a id="r_ga8646699330c45fb008d50b54be339c6c"></a>

```c
#define HID_INPUT(a)
```

定义数据长度为1字节的 HID 输入项目。

相关声明：[HID_INPUT](P049_HID报告项目定义.md#ga8646699330c45fb008d50b54be339c6c)。

<a id="r_ga6ef7aa576bf69f9ba5f93df500a1403c"></a>

```c
#define HID_OUTPUT(a)
```

定义数据长度为1字节的 HID 输出项目。

相关声明：[HID_OUTPUT](P049_HID报告项目定义.md#ga6ef7aa576bf69f9ba5f93df500a1403c)。

<a id="r_ga951a415e05e95492250d4fb43a37090d"></a>

```c
#define HID_FEATURE(a)
```

定义数据长度为1字节的 HID 特性项目。

相关声明：[HID_FEATURE](P049_HID报告项目定义.md#ga951a415e05e95492250d4fb43a37090d)。

<a id="r_gad010ed98662b0e653754caff1dfd352f"></a>

```c
#define HID_COLLECTION(a)
```

定义数据长度为1字节的 HID 集合项目。

相关声明：[HID_COLLECTION](P049_HID报告项目定义.md#gad010ed98662b0e653754caff1dfd352f)。

<a id="r_ga6cd6affb9d52e0bf98c7a5c83d03a764"></a>

```c
#define HID_END_COLLECTION HID_ITEM(HID_ITEM_TAG_COLLECTION_END, HID_ITEM_TYPE_MAIN, 0)
```

定义不带数据的 HID 集合结束项目。

相关声明：[HID_END_COLLECTION](P049_HID报告项目定义.md#ga6cd6affb9d52e0bf98c7a5c83d03a764)、[HID_ITEM](P049_HID报告项目定义.md#ga4e9dc6652402e0b87e1313c143737ed4)、[HID_ITEM_TAG_COLLECTION_END](P048_HID通用定义.md#ga3f4fe1817887966f0d05aa597cd0ab79)、[HID_ITEM_TYPE_MAIN](P048_HID通用定义.md#ga9a71248c522943951b5af70ec9c14c02)。

<a id="r_ga30dc3f62583822ba27edd984dc2dec39"></a>

```c
#define HID_USAGE_PAGE(page)
```

定义 HID 用途页项目。

相关声明：[HID_USAGE_PAGE](P049_HID报告项目定义.md#ga30dc3f62583822ba27edd984dc2dec39)。

<a id="r_ga4ab727e3407dc5c0b11d998314ab27de"></a>

```c
#define HID_USAGE_PAGE16(page)
```

定义数据长度为2字节的 HID 用途页项目。

相关声明：[HID_USAGE_PAGE16](P049_HID报告项目定义.md#ga4ab727e3407dc5c0b11d998314ab27de)。

<a id="r_gacd141f6ede5122f260cd50338649d458"></a>

```c
#define HID_LOGICAL_MIN8(a)
```

定义数据长度为1字节的 HID 逻辑最小值项目。

相关声明：[HID_LOGICAL_MIN8](P049_HID报告项目定义.md#gacd141f6ede5122f260cd50338649d458)。

<a id="r_ga2f6b809ae85b6716ade8c52da4fa56af"></a>

```c
#define HID_LOGICAL_MAX8(a)
```

定义数据长度为1字节的 HID 逻辑最大值项目。

相关声明：[HID_LOGICAL_MAX8](P049_HID报告项目定义.md#ga2f6b809ae85b6716ade8c52da4fa56af)。

<a id="r_ga5e290798d55bccd7474dbfb6bc2d1033"></a>

```c
#define HID_LOGICAL_MIN16(a, b)
```

定义数据长度为2字节的 HID 逻辑最小值项目。

相关声明：[HID_LOGICAL_MIN16](P049_HID报告项目定义.md#ga5e290798d55bccd7474dbfb6bc2d1033)。

<a id="r_ga9b804d676812dcfb0ec12f3aa887e37f"></a>

```c
#define HID_LOGICAL_MAX16(a, b)
```

定义数据长度为2字节的 HID 逻辑最大值项目。

相关声明：[HID_LOGICAL_MAX16](P049_HID报告项目定义.md#ga9b804d676812dcfb0ec12f3aa887e37f)。

<a id="r_gad4b2ff8642676d692fd0d56ab0cbeaa7"></a>

```c
#define HID_LOGICAL_MIN32(a, b, c, d)
```

定义数据长度为4字节的 HID 逻辑最小值项目。

相关声明：[HID_LOGICAL_MIN32](P049_HID报告项目定义.md#gad4b2ff8642676d692fd0d56ab0cbeaa7)。

<a id="r_gae9d17e753685b0df6c53f942ce9c95d2"></a>

```c
#define HID_LOGICAL_MAX32(a, b, c, d)
```

定义数据长度为4字节的 HID 逻辑最大值项目。

相关声明：[HID_LOGICAL_MAX32](P049_HID报告项目定义.md#gae9d17e753685b0df6c53f942ce9c95d2)。

<a id="r_ga3135a21a63c491daf8647fa771def0e7"></a>

```c
#define HID_REPORT_SIZE(size)
```

定义数据长度为1字节的 HID 报告字段大小项目。

相关声明：[HID_REPORT_SIZE](P049_HID报告项目定义.md#ga3135a21a63c491daf8647fa771def0e7)。

<a id="r_ga1b45fce2c7df2847b1326fca29cef389"></a>

```c
#define HID_REPORT_ID(id)
```

定义数据长度为1字节的 HID 报告 ID 项目。

相关声明：[HID_REPORT_ID](P049_HID报告项目定义.md#ga1b45fce2c7df2847b1326fca29cef389)。

<a id="r_ga71192f2a55f05456b893069ebfbc5b98"></a>

```c
#define HID_REPORT_COUNT(count)
```

定义数据长度为1字节的 HID 报告字段数量项目。

相关声明：[HID_REPORT_COUNT](P049_HID报告项目定义.md#ga71192f2a55f05456b893069ebfbc5b98)。

<a id="r_gac8429a70866a898887ead55664e04bd7"></a>

```c
#define HID_USAGE(idx)
```

定义数据长度为1字节的 HID 用途索引项目（Usage Index Item）。

相关声明：[HID_USAGE](P049_HID报告项目定义.md#gac8429a70866a898887ead55664e04bd7)。

<a id="r_gaf2e338747f22f75256e57de1cf055200"></a>

```c
#define HID_USAGE16(idx)
```

定义数据长度为2字节的 HID 用途索引项目。

相关声明：[HID_USAGE16](P049_HID报告项目定义.md#gaf2e338747f22f75256e57de1cf055200)。

<a id="r_gabf53f1e2eae6d686aeb7d62cc46b22ad"></a>

```c
#define HID_USAGE_MIN8(a)
```

定义数据长度为1字节的 HID 用途最小值项目。

相关声明：[HID_USAGE_MIN8](P049_HID报告项目定义.md#gabf53f1e2eae6d686aeb7d62cc46b22ad)。

<a id="r_gae7fc9684ef10f50d69df6f495cc09e91"></a>

```c
#define HID_USAGE_MAX8(a)
```

定义数据长度为1字节的 HID 用途最大值项目。

相关声明：[HID_USAGE_MAX8](P049_HID报告项目定义.md#gae7fc9684ef10f50d69df6f495cc09e91)。

<a id="r_ga0dbc847d11cf64676f7cfc51b54150fa"></a>

```c
#define HID_USAGE_MIN16(a, b)
```

定义数据长度为2字节的 HID 用途最小值项目。

相关声明：[HID_USAGE_MIN16](P049_HID报告项目定义.md#ga0dbc847d11cf64676f7cfc51b54150fa)。

<a id="r_gadd11a09546bc275c82e7a992cb9441cc"></a>

```c
#define HID_USAGE_MAX16(a, b)
```

定义数据长度为2字节的 HID 用途最大值项目。

相关声明：[HID_USAGE_MAX16](P049_HID报告项目定义.md#gadd11a09546bc275c82e7a992cb9441cc)。

<a id="r_ga2147820c08a9b4a18d3aa162460f3967"></a>

```c
#define HID_UNIT_EXPONENT(exp)
```

定义 HID 单位指数项目。

相关声明：[HID_UNIT_EXPONENT](P049_HID报告项目定义.md#ga2147820c08a9b4a18d3aa162460f3967)。

## 49.3\_详细说明（Detailed Documentation）

<a id="gad010ed98662b0e653754caff1dfd352f"></a>

### `HID_COLLECTION`

```c
#define HID_COLLECTION ( a)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_COLLECTION, HID_ITEM_TYPE_MAIN, 1), a
```

定义数据长度为1字节的 HID 集合项目。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 集合项目数据。 |

**返回（Returns）**：HID 集合项目。

<a id="ga6cd6affb9d52e0bf98c7a5c83d03a764"></a>

### `HID_END_COLLECTION`

```c
#define HID_END_COLLECTION HID_ITEM(HID_ITEM_TAG_COLLECTION_END, HID_ITEM_TYPE_MAIN, 0)
```

```c
#include <zephyr/usb/class/hid.h>
```

定义不带数据的 HID 集合结束项目。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**返回（Returns）**：HID 集合结束项目。

<a id="ga951a415e05e95492250d4fb43a37090d"></a>

### `HID_FEATURE`

```c
#define HID_FEATURE ( a)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_FEATURE, HID_ITEM_TYPE_MAIN, 1), a
```

定义数据长度为1字节的 HID 特性项目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 特性项目数据。 |

**返回（Returns）**：HID 特性项目。

<a id="ga8646699330c45fb008d50b54be339c6c"></a>

### `HID_INPUT`

```c
#define HID_INPUT ( a)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_INPUT, HID_ITEM_TYPE_MAIN, 1), a
```

定义数据长度为1字节的 HID 输入项目。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 输入项目数据。 |

**返回（Returns）**：HID 输入项目。

<a id="ga4e9dc6652402e0b87e1313c143737ed4"></a>

### `HID_ITEM`

```c
#define HID_ITEM ( bTag, bType, bSize )
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
(((bTag & 0xF) << 4) | \
((bType & 0x3) << 2) | (bSize & 0x3))
```

定义 HID 短项目（Short Item）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bTag` | 项目标签（Item Tag）。 |
| `bType` | 项目类型（Item Type）。 |
| `bSize` | 项目数据大小（Item Data Size）。 |

**返回（Returns）**：HID 输入项目。

> 译注（源码核对）：宏组合项目头字节，bSize是HID短项目的长度编码：0、1、2、3分别表示0、1、2、4字节，不能把4直接当成编码传入。下面的32位逻辑范围辅助宏传入3，并显式列出四个数据字节。

<a id="ga9b804d676812dcfb0ec12f3aa887e37f"></a>

### `HID_LOGICAL_MAX16`

```c
#define HID_LOGICAL_MAX16 ( a, b )
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_LOGICAL_MAX, HID_ITEM_TYPE_GLOBAL, 2), a, b
```

定义数据长度为2字节的 HID 逻辑最大值项目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 最大值的低字节。 |
| `b` | 最大值的高字节。 |

**返回（Returns）**：HID 逻辑最大值项目。

<a id="gae9d17e753685b0df6c53f942ce9c95d2"></a>

### `HID_LOGICAL_MAX32`

```c
#define HID_LOGICAL_MAX32 ( a, b, c, d )
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_LOGICAL_MAX, HID_ITEM_TYPE_GLOBAL, 3), a, b, c, d
```

定义数据长度为4字节的 HID 逻辑最大值项目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 最大值的低字节。 |
| `b` | 最大值的中低字节。 |
| `c` | 最大值的中高字节。 |
| `d` | 最大值的高字节。 |

**返回（Returns）**：HID 逻辑最大值项目。

<a id="ga2f6b809ae85b6716ade8c52da4fa56af"></a>

### `HID_LOGICAL_MAX8`

```c
#define HID_LOGICAL_MAX8 ( a)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_LOGICAL_MAX, HID_ITEM_TYPE_GLOBAL, 1), a
```

定义数据长度为1字节的 HID 逻辑最大值项目。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 以逻辑单位表示的最大值。 |

**返回（Returns）**：HID 逻辑最大值项目。

<a id="ga5e290798d55bccd7474dbfb6bc2d1033"></a>

### `HID_LOGICAL_MIN16`

```c
#define HID_LOGICAL_MIN16 ( a, b )
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_LOGICAL_MIN, HID_ITEM_TYPE_GLOBAL, 2), a, b
```

定义数据长度为2字节的 HID 逻辑最小值项目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 最小值的低字节。 |
| `b` | 最小值的高字节。 |

**返回（Returns）**：HID 逻辑最小值项目。

<a id="gad4b2ff8642676d692fd0d56ab0cbeaa7"></a>

### `HID_LOGICAL_MIN32`

```c
#define HID_LOGICAL_MIN32 ( a, b, c, d )
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_LOGICAL_MIN, HID_ITEM_TYPE_GLOBAL, 3), a, b, c, d
```

定义数据长度为4字节的 HID 逻辑最小值项目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 最小值的低字节。 |
| `b` | 最小值的中低字节。 |
| `c` | 最小值的中高字节。 |
| `d` | 最小值的高字节。 |

**返回（Returns）**：HID 逻辑最小值项目。

<a id="gacd141f6ede5122f260cd50338649d458"></a>

### `HID_LOGICAL_MIN8`

```c
#define HID_LOGICAL_MIN8 ( a)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_LOGICAL_MIN, HID_ITEM_TYPE_GLOBAL, 1), a
```

定义数据长度为1字节的 HID 逻辑最小值项目。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 以逻辑单位表示的最小值。 |

**返回（Returns）**：HID 逻辑最小值项目。

<a id="ga6ef7aa576bf69f9ba5f93df500a1403c"></a>

### `HID_OUTPUT`

```c
#define HID_OUTPUT ( a)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_OUTPUT, HID_ITEM_TYPE_MAIN, 1), a
```

定义数据长度为1字节的 HID 输出项目。

用法示例见 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 输出项目数据。 |

**返回（Returns）**：HID 输出项目。

<a id="ga71192f2a55f05456b893069ebfbc5b98"></a>

### `HID_REPORT_COUNT`

```c
#define HID_REPORT_COUNT ( count)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_REPORT_COUNT, HID_ITEM_TYPE_GLOBAL, 1), count
```

定义数据长度为1字节的 HID 报告字段数量项目。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `count` | 报告中包含的数据字段数量。 |

**返回（Returns）**：HID 报告字段数量项目。

<a id="ga1b45fce2c7df2847b1326fca29cef389"></a>

### `HID_REPORT_ID`

```c
#define HID_REPORT_ID ( id)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_REPORT_ID, HID_ITEM_TYPE_GLOBAL, 1), id
```

定义数据长度为1字节的 HID 报告 ID 项目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 报告 ID。 |

**返回（Returns）**：HID 报告 ID 项目。

<a id="ga3135a21a63c491daf8647fa771def0e7"></a>

### `HID_REPORT_SIZE`

```c
#define HID_REPORT_SIZE ( size)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_REPORT_SIZE, HID_ITEM_TYPE_GLOBAL, 1), size
```

定义数据长度为1字节的 HID 报告字段大小项目。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `size` | 报告字段大小，单位为位（bit）。 |

**返回（Returns）**：HID 报告字段大小项目。

> 译注（源码核对）：Report Size表示每个字段的位数，Report Count表示字段数量。它们用于描述报告布局，不是端点的最大包长或整个描述符的字节长度。

<a id="ga2147820c08a9b4a18d3aa162460f3967"></a>

### `HID_UNIT_EXPONENT`

```c
#define HID_UNIT_EXPONENT ( exp)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_UNIT_EXPONENT, HID_ITEM_TYPE_GLOBAL, 1), exp
```

定义 HID 单位指数项目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `exp` | 单位指数；用法参见规范中的 HID Unit Exponent 表。 |

**返回（Returns）**：HID 单位指数项目。

<a id="gac8429a70866a898887ead55664e04bd7"></a>

### `HID_USAGE`

```c
#define HID_USAGE ( idx)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_USAGE, HID_ITEM_TYPE_LOCAL, 1), idx
```

定义数据长度为1字节的 HID 用途索引项目（Usage Index Item）。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `idx` | HID 用途表（HID Usage Table）规定的用途 ID。 |

**返回（Returns）**：HID 用途索引项目。

<a id="gaf2e338747f22f75256e57de1cf055200"></a>

### `HID_USAGE16`

```c
#define HID_USAGE16 ( idx)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_USAGE, HID_ITEM_TYPE_LOCAL, 2), (uint8_t)idx, (idx >> 8)
```

定义数据长度为2字节的 HID 用途索引项目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `idx` | HID 用途表（HID Usage Table）规定的用途 ID。 |

**返回（Returns）**：HID 用途索引项目。

<a id="gadd11a09546bc275c82e7a992cb9441cc"></a>

### `HID_USAGE_MAX16`

```c
#define HID_USAGE_MAX16 ( a, b )
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_USAGE_MAX, HID_ITEM_TYPE_LOCAL, 2), a, b
```

定义数据长度为2字节的 HID 用途最大值项目。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 结束用途的低字节。 |
| `b` | 结束用途的高字节。 |

**返回（Returns）**：HID 用途最大值项目。

<a id="gae7fc9684ef10f50d69df6f495cc09e91"></a>

### `HID_USAGE_MAX8`

```c
#define HID_USAGE_MAX8 ( a)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_USAGE_MAX, HID_ITEM_TYPE_LOCAL, 1), a
```

定义数据长度为1字节的 HID 用途最大值项目。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 结束用途。 |

**返回（Returns）**：HID 用途最大值项目。

<a id="ga0dbc847d11cf64676f7cfc51b54150fa"></a>

### `HID_USAGE_MIN16`

```c
#define HID_USAGE_MIN16 ( a, b )
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_USAGE_MIN, HID_ITEM_TYPE_LOCAL, 2), a, b
```

定义数据长度为2字节的 HID 用途最小值项目。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 起始用途的低字节。 |
| `b` | 起始用途的高字节。 |

**返回（Returns）**：HID 用途最小值项目。

<a id="gabf53f1e2eae6d686aeb7d62cc46b22ad"></a>

### `HID_USAGE_MIN8`

```c
#define HID_USAGE_MIN8 ( a)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_USAGE_MIN, HID_ITEM_TYPE_LOCAL, 1), a
```

定义数据长度为1字节的 HID 用途最小值项目。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 起始用途。 |

**返回（Returns）**：HID 用途最小值项目。

<a id="ga30dc3f62583822ba27edd984dc2dec39"></a>

### `HID_USAGE_PAGE`

```c
#define HID_USAGE_PAGE ( page)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_USAGE_PAGE, HID_ITEM_TYPE_GLOBAL, 1), page
```

定义 HID 用途页项目。

用法示例见 HID_MOUSE_REPORT_DESC() 和 HID_KEYBOARD_REPORT_DESC()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `page` | 用途页。 |

**返回（Returns）**：HID 用途页项目。

<a id="ga4ab727e3407dc5c0b11d998314ab27de"></a>

### `HID_USAGE_PAGE16`

```c
#define HID_USAGE_PAGE16 ( page)
```

```c
#include <zephyr/usb/class/hid.h>
```

**宏展开值（Value）**

```c
HID_ITEM(HID_ITEM_TAG_USAGE_PAGE, HID_ITEM_TYPE_GLOBAL, 2), (uint8_t)page, (page >> 8)
```

定义数据长度为2字节的 HID 用途页项目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `page` | 用途页。 |

**返回（Returns）**：HID 用途页项目。

## 49.4\_源码跟踪与使用边界

通用项目及描述符见[hid.h](../../../include/zephyr/usb/class/hid.h)，新版接口见[usbd_hid.h](../../../include/zephyr/usb/class/usbd_hid.h)和[新版实现](../../../subsys/usb/device_next/class/usbd_hid.c)，旧接口见[usb_hid.h](../../../include/zephyr/usb/class/usb_hid.h)、[旧版实现](../../../subsys/usb/device/class/hid/core.c)及[新版兼容包装](../../../subsys/usb/device_next/class/usbd_hid_api.c)。本仓库版本可能与官方 latest 不同；译注依据保存的[官方通用头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/hid.h)、[新版头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_hid.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid.c)、[兼容包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid_api.c)和[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/hid/core.c)，摘要见[来源记录](../SOURCES.md)。本批未编译、运行或操作USB硬件。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__usb__hid__definitions_html_ga2c06052593b060466f4c338a88319485"></a>
<a id="agroup__usb__hid__definitions_html_ga9a71248c522943951b5af70ec9c14c02"></a>
<a id="agroup__usb__hid__items_html_ga4e9dc6652402e0b87e1313c143737ed4"></a>
<a id="agroup__usb__hid__definitions_html_gaeadcca849f0a0923d9a70605c44464a6"></a>
<a id="agroup__usb__hid__definitions_html_ga66e1c50fe814fd05d61dce12ce3888c1"></a>
<a id="agroup__usb__hid__definitions_html_ga8e56e8090f1af7aae473e8a8b6832fb8"></a>
<a id="agroup__usb__hid__definitions_html_gaab6aec72cca41670464605d6970ad553"></a>
<a id="agroup__usb__hid__definitions_html_ga034033b1ae6f4677aef82d4243c6f712"></a>
<a id="agroup__usb__hid__definitions_html_ga70c32518a6b538831e821ad30022679b"></a>
<a id="agroup__usb__hid__definitions_html_ga1847701703130ce8f57547811f28b2b4"></a>
<a id="agroup__usb__hid__definitions_html_ga76cd3a266ae5d5e29292d93caceece72"></a>
<a id="agroup__usb__hid__definitions_html_ga0e6d7a56593bd25a5e15683e9271bb19"></a>
<a id="agroup__usb__hid__definitions_html_ga7c6d81ee211814ec9b5d17f95e57639b"></a>
<a id="agroup__usb__hid__definitions_html_ga0bfb0e326d9a01072c029cba788d6456"></a>
<a id="agroup__usb__hid__definitions_html_gaefd616ecaa8fc8762e65ec9d7b01f0cd"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="agroup__usb__hid__definitions_html_gac2a0aff74caff6c03511fc0b6db6167b"></a>
<a id="agroup__usb__hid__definitions_html_ga4e6f4133f12276f4f9fa51ab06580676"></a>
<a id="agroup__usb__hid__definitions_html_ga73f58fa37c0bf6698463b9d31c8a511f"></a>

[上一章](P048_HID通用定义.md) · [返回大纲](大纲.md) · [下一章](P050_HID报告描述符构造宏.md)
