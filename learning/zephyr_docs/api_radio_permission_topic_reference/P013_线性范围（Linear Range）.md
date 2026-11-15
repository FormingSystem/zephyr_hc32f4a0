---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-13
title: 线性范围（Linear Range）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_线性范围（Linear Range）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

引入版本（Since）：3.3；API 版本（Version）：1.0.0。线性范围 API（Linear Range API）将线性范围内的值映射为范围索引（Range Index）。四个参数即可完整定义一个线性范围：最小值（Minimum Value）、步长（Step Value）、最小索引值（Minimum Index Value）和最大索引值（Maximum Index Value）。例如，电压调节器支持的电压通常按下面的原始示例映射为寄存器索引。

- `1000uV: 0x00`
- `1250uV: 0x01`
- `1500uV: 0x02`
- `...`
- `3000uV: 0x08`

此例中，最小值为 1000uV，步长为 250uV，最小索引值为 0x00，最大索引值为 0x08。线性范围也可以是常量范围，即步长设为零。同一设备经常包含多个不连续的线性范围；API 也提供处理线性范围组（Groups of Linear Ranges）的辅助函数。实现使用固定位宽整数（Fixed-width Integers），数值范围限于 [INT32_MIN, INT32_MAX]，索引数量限于 UINT16_MAX。最初构想借鉴自 Linux。

<a id="header-files"></a>
<a id="files"></a>

## 13.1\_文件（Files）

<a id="r_linear_5Frange_2Eh"></a>

```c
file linear_range.h
```

相关声明：[linear_range.h](../api_file_transfer_device_reference/P021_zephyr__sys__linear_range.h_文件参考.md)。

将线性范围（Linear Range）内的值映射为范围索引。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.2\_数据结构（Data Structures）

<a id="r_linear_5Frange"></a>

```c
struct linear_range
```

相关声明：[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)。

线性范围（Linear Range）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.3\_宏定义（Macros）

<a id="r_ga3f936124e81ea46aa5f8dd4d9bde9ece"></a>

```c
#define LINEAR_RANGE_INIT(_min, _step, _min_idx, _max_idx)
```

相关声明：[LINEAR_RANGE_INIT](#ga3f936124e81ea46aa5f8dd4d9bde9ece)。

线性范围（Linear Range）的初始化器（Initializer）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.4\_函数（Functions）

<a id="r_gae02547c7922e5a36c815dc89bc1df128"></a>

```c
static uint32_t linear_range_values_count (const struct linear_range *r)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[linear_range_values_count](#gae02547c7922e5a36c815dc89bc1df128)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)。

获取线性范围（Linear Range）可表示的值的数量。

<a id="r_ga67b24d9d6e7088daf39020c8c02f8d96"></a>

```c
static uint32_t linear_range_group_values_count (const struct linear_range *r, size_t r_cnt)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[linear_range_group_values_count](#ga67b24d9d6e7088daf39020c8c02f8d96)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)。

获取一组线性范围（Group of Linear Ranges）可表示的值的数量。

<a id="r_gae6315858afa73945bc44d8c5c997645c"></a>

```c
static int32_t linear_range_get_max_value (const struct linear_range *r)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[linear_range_get_max_value](#gae6315858afa73945bc44d8c5c997645c)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)。

获取线性范围（Linear Range）可表示的最大值。

<a id="r_ga72b800d1c6af44cb247130139176a59e"></a>

```c
static int linear_range_get_value (const struct linear_range *r, uint16_t idx, int32_t *val)
```

相关声明：[linear_range_get_value](#ga72b800d1c6af44cb247130139176a59e)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

根据线性范围索引（Linear Range Index）获取值。

<a id="r_gac054f5cc2aad11de223fa968ebeaa55c"></a>

```c
static int linear_range_group_get_value (const struct linear_range *r, size_t r_cnt, uint16_t idx, int32_t *val)
```

相关声明：[linear_range_group_get_value](#gac054f5cc2aad11de223fa968ebeaa55c)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

根据线性范围索引（Linear Range Index）获取一组范围中的值。

<a id="r_ga90610e42e63eb4290e5ae6187a53143f"></a>

```c
static int linear_range_get_index (const struct linear_range *r, int32_t val, uint16_t *idx)
```

相关声明：[linear_range_get_index](#ga90610e42e63eb4290e5ae6187a53143f)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据给定值（Value）获取索引（Index）。

<a id="r_gab8b661f6ed1caba2ab4796a02c1b24a8"></a>

```c
static int linear_range_group_get_index (const struct linear_range *r, size_t r_cnt, int32_t val, uint16_t *idx)
```

相关声明：[linear_range_group_get_index](#gab8b661f6ed1caba2ab4796a02c1b24a8)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据给定值（Value）获取一组范围中的索引（Index）。

<a id="r_ga6c06a26d629f4d7a195188e7c5df5db1"></a>

```c
static int linear_range_get_win_index (const struct linear_range *r, int32_t val_min, int32_t val_max, uint16_t *idx)
```

相关声明：[linear_range_get_win_index](#ga6c06a26d629f4d7a195188e7c5df5db1)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据值窗口（Window of Values）获取索引（Index）。

<a id="r_ga11dc5408be53887e9ddf992b574aa16c"></a>

```c
static int linear_range_group_get_win_index (const struct linear_range *r, size_t r_cnt, int32_t val_min, int32_t val_max, uint16_t *idx)
```

相关声明：[linear_range_group_get_win_index](#ga11dc5408be53887e9ddf992b574aa16c)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在一组范围中，根据必须位于指定值窗口（Window of Values）内的值获取索引（Index）。

## 13.5\_详细说明（Detailed Documentation）

<a id="ga3f936124e81ea46aa5f8dd4d9bde9ece"></a>

### `LINEAR_RANGE_INIT`

```c
#define LINEAR_RANGE_INIT ( _min, _step, _min_idx, _max_idx )
```

```c
#include <zephyr/sys/linear_range.h>
```

展开值（Value）：

```c
{                                                                      \
        .min = (_min),                                                 \
        .step = (_step),                                               \
        .min_idx = (_min_idx),                                         \
        .max_idx = (_max_idx),                                         \
}
```

线性范围（Linear Range）的初始化器（Initializer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_min` | 范围内的最小值（Minimum Value）。 |
| `_step` | 步长值（Step value）。 |
| `_min_idx` | 最小索引（Minimum Index）。 |
| `_max_idx` | 最大索引（Maximum Index）。 |

<a id="ga90610e42e63eb4290e5ae6187a53143f"></a>

### `linear_range_get_index()`

```c
int linear_range_get_index ( const struct linear_range * r, int32_t val, uint16_t * idx )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/linear_range.h>
```

根据给定值（Value）获取索引（Index）。

数值超出范围时，存储最接近的索引并返回 -ERANGE。即数值低于或高于范围时，索引分别取最小值或最大值。对于常量范围（Constant Ranges），返回最小索引。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] r` | 线性范围实例（Linear Range Instance）。 |
| ` val` | 值（Value）。 |
| `[out] idx` | 索引的存储位置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 数值位于范围内时。 |
| `-ERANGE` | 数值超出范围时。 |

<a id="gae6315858afa73945bc44d8c5c997645c"></a>

### `linear_range_get_max_value()`

```c
int32_t linear_range_get_max_value ( const struct linear_range * r)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/linear_range.h>
```

获取线性范围（Linear Range）可表示的最大值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] r` | 线性范围实例（Linear Range Instance）。 |

**返回（Returns）**：返回值（Returns）：r 可表示的最大值。

<a id="ga72b800d1c6af44cb247130139176a59e"></a>

### `linear_range_get_value()`

```c
int linear_range_get_value ( const struct linear_range * r, uint16_t idx, int32_t * val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/linear_range.h>
```

根据线性范围索引（Linear Range Index）获取值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] r` | 线性范围实例（Linear Range Instance）。 |
| ` idx` | 范围索引（Range Index）。 |
| `[out] val` | 数值的存储位置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 索引超出范围时。 |

<a id="ga6c06a26d629f4d7a195188e7c5df5db1"></a>

### `linear_range_get_win_index()`

```c
int linear_range_get_win_index ( const struct linear_range * r, int32_t val_min, int32_t val_max, uint16_t * idx )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/linear_range.h>
```

根据值窗口（Window of Values）获取索引（Index）。

值窗口（Window of Values）与范围无交集时返回 -EINVAL。若仅部分相交，即窗口任一边界不在范围内，则存储最接近的索引并返回 -ERANGE。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] r` | 线性范围实例（Linear Range Instance）。 |
| ` val_min` | 窗口最小值（Minimum Window Value）。 |
| ` val_max` | 窗口最大值（Maximum Window Value）。 |
| `[out] idx` | 索引的存储位置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 在线性范围内找到有效索引时。 |
| `-ERANGE` | 给定值窗口部分超出线性范围时。 |
| `-EINVAL` | 给定值窗口与线性范围不相交，或窗口过窄时。 |

<a id="gab8b661f6ed1caba2ab4796a02c1b24a8"></a>

### `linear_range_group_get_index()`

```c
int linear_range_group_get_index ( const struct linear_range * r, size_t r_cnt, int32_t val, uint16_t * idx )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/linear_range.h>
```

根据给定值（Value）获取一组范围中的索引（Index）。

此函数与 linear_range_get_index() 工作方式相同，但会考虑组中的所有范围（Ranges）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] r` | 线性范围实例（Linear Range Instances）。 |
| ` r_cnt` | 线性范围实例的数量。 |
| ` val` | 值（Value）。 |
| `[out] idx` | 索引的存储位置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 数值位于范围组（Range Group）内时。 |
| `-ERANGE` | 数值超出范围组（Range Group）时。 |
| `-EINVAL` | 输入无效，例如组数为零时。 |

<a id="gac054f5cc2aad11de223fa968ebeaa55c"></a>

### `linear_range_group_get_value()`

```c
int linear_range_group_get_value ( const struct linear_range * r, size_t r_cnt, uint16_t idx, int32_t * val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/linear_range.h>
```

根据线性范围索引（Linear Range Index）获取一组范围中的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] r` | 线性范围实例数组（Array of Linear Range Instances）。 |
| ` r_cnt` | 线性范围实例的数量。 |
| ` idx` | 范围索引（Range Index）。 |
| `[out] val` | 数值的存储位置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 索引超出范围时。 |

<a id="ga11dc5408be53887e9ddf992b574aa16c"></a>

### `linear_range_group_get_win_index()`

```c
int linear_range_group_get_win_index ( const struct linear_range * r, size_t r_cnt, int32_t val_min, int32_t val_max, uint16_t * idx )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/linear_range.h>
```

在一组范围中，根据必须位于指定值窗口（Window of Values）内的值获取索引（Index）。

此函数与 linear_range_get_win_index() 工作方式相同，但会考虑组中的所有范围（Ranges）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] r` | 线性范围实例（Linear Range Instances）。 |
| ` r_cnt` | 线性范围实例的数量。 |
| ` val_min` | 窗口最小值（Minimum Window Value）。 |
| ` val_max` | 窗口最大值（Maximum Window Value）。 |
| `[out] idx` | 索引的存储位置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 在线性范围组（Linear Range Group）内找到有效索引时。 |
| `-ERANGE` | 给定值窗口部分超出线性范围组时。 |
| `-EINVAL` | 给定值窗口与线性范围组不相交、窗口过窄，或输入无效（例如组数为零）时。 |

<a id="ga67b24d9d6e7088daf39020c8c02f8d96"></a>

### `linear_range_group_values_count()`

```c
uint32_t linear_range_group_values_count ( const struct linear_range * r, size_t r_cnt )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/linear_range.h>
```

获取一组线性范围（Group of Linear Ranges）可表示的值的数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] r` | 线性范围实例数组（Array of Linear Range Instances）。 |
| ` r_cnt` | 线性范围实例的数量。 |

**返回（Returns）**：返回值（Returns）：r 组可表示的范围数量（Number of Ranges）。

<a id="gae02547c7922e5a36c815dc89bc1df128"></a>

### `linear_range_values_count()`

```c
uint32_t linear_range_values_count ( const struct linear_range * r)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/linear_range.h>
```

获取线性范围（Linear Range）可表示的值的数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] r` | 线性范围实例（Linear Range Instance）。 |

**返回（Returns）**：返回值（Returns）：r 可表示的范围数量（Number of Ranges）。


## 13.6\_原页交叉引用（Cross References）

- [linear_range.h](../api_file_transfer_device_reference/P021_zephyr__sys__linear_range.h_文件参考.md)
- [linear_range](../system_service_model_reference/P060_linear_range_结构体.md)
- [线性范围（Linear Range）](P013_线性范围（Linear Range）.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_IIS3DWB API主题.md) · [返回大纲](大纲.md) · [下一章](P014_LoRa 驱动后端 API.md)
