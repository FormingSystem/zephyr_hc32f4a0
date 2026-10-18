---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-21
title: zephyr__sys__linear_range.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/linear__range_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_sys\_\_linear\_range.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/linear__range_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

将线性范围（Linear Range）内的值映射为范围索引。

<a id="details"></a>

```c
#include <errno.h>
#include <stdint.h>
#include <stdlib.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

将线性范围（Linear Range）内的值映射为范围索引。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 21.1\_数据结构（Data Structures）

<a id="r_linear_5Frange"></a>

```c
struct linear_range
```

相关声明：[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)。

线性范围（Linear Range）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.2\_宏定义（Macros）

<a id="r_ga3f936124e81ea46aa5f8dd4d9bde9ece"></a>

```c
#define LINEAR_RANGE_INIT(_min, _step, _min_idx, _max_idx)
```

相关声明：[LINEAR_RANGE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga3f936124e81ea46aa5f8dd4d9bde9ece)。

线性范围（Linear Range）的初始化器（Initializer）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.3\_函数（Functions）

<a id="r_gae02547c7922e5a36c815dc89bc1df128"></a>

```c
static uint32_t linear_range_values_count (const struct linear_range *r)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[linear_range_values_count](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#gae02547c7922e5a36c815dc89bc1df128)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)。

获取线性范围（Linear Range）可表示的值的数量。

<a id="r_ga67b24d9d6e7088daf39020c8c02f8d96"></a>

```c
static uint32_t linear_range_group_values_count (const struct linear_range *r, size_t r_cnt)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[linear_range_group_values_count](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga67b24d9d6e7088daf39020c8c02f8d96)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)。

获取一组线性范围（Group of Linear Ranges）可表示的值的数量。

<a id="r_gae6315858afa73945bc44d8c5c997645c"></a>

```c
static int32_t linear_range_get_max_value (const struct linear_range *r)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[linear_range_get_max_value](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#gae6315858afa73945bc44d8c5c997645c)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)。

获取线性范围（Linear Range）可表示的最大值。

<a id="r_ga72b800d1c6af44cb247130139176a59e"></a>

```c
static int linear_range_get_value (const struct linear_range *r, uint16_t idx, int32_t *val)
```

相关声明：[linear_range_get_value](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga72b800d1c6af44cb247130139176a59e)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

根据线性范围索引（Linear Range Index）获取值。

<a id="r_gac054f5cc2aad11de223fa968ebeaa55c"></a>

```c
static int linear_range_group_get_value (const struct linear_range *r, size_t r_cnt, uint16_t idx, int32_t *val)
```

相关声明：[linear_range_group_get_value](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#gac054f5cc2aad11de223fa968ebeaa55c)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

根据线性范围索引（Linear Range Index）获取一组范围中的值。

<a id="r_ga90610e42e63eb4290e5ae6187a53143f"></a>

```c
static int linear_range_get_index (const struct linear_range *r, int32_t val, uint16_t *idx)
```

相关声明：[linear_range_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga90610e42e63eb4290e5ae6187a53143f)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据给定值（Value）获取索引（Index）。

<a id="r_gab8b661f6ed1caba2ab4796a02c1b24a8"></a>

```c
static int linear_range_group_get_index (const struct linear_range *r, size_t r_cnt, int32_t val, uint16_t *idx)
```

相关声明：[linear_range_group_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#gab8b661f6ed1caba2ab4796a02c1b24a8)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据给定值（Value）获取一组范围中的索引（Index）。

<a id="r_ga6c06a26d629f4d7a195188e7c5df5db1"></a>

```c
static int linear_range_get_win_index (const struct linear_range *r, int32_t val_min, int32_t val_max, uint16_t *idx)
```

相关声明：[linear_range_get_win_index](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga6c06a26d629f4d7a195188e7c5df5db1)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据值窗口（Window of Values）获取索引（Index）。

<a id="r_ga11dc5408be53887e9ddf992b574aa16c"></a>

```c
static int linear_range_group_get_win_index (const struct linear_range *r, size_t r_cnt, int32_t val_min, int32_t val_max, uint16_t *idx)
```

相关声明：[linear_range_group_get_win_index](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga11dc5408be53887e9ddf992b574aa16c)、[linear_range](../system_service_model_reference/P060_linear_range_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在一组范围中，根据必须位于指定值窗口（Window of Values）内的值获取索引（Index）。


## 21.4\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdlib.h](../api_source_configuration_reference/P107_stdlib.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P440_linear_range.h_源码浏览.md)
- [linear_range](../system_service_model_reference/P060_linear_range_结构体.md)
- [LINEAR_RANGE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga3f936124e81ea46aa5f8dd4d9bde9ece)
- [线性范围（Linear Range）](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [linear_range_values_count](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#gae02547c7922e5a36c815dc89bc1df128)
- [linear_range_group_values_count](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga67b24d9d6e7088daf39020c8c02f8d96)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [linear_range_get_max_value](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#gae6315858afa73945bc44d8c5c997645c)
- [linear_range_get_value](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga72b800d1c6af44cb247130139176a59e)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [linear_range_group_get_value](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#gac054f5cc2aad11de223fa968ebeaa55c)
- [linear_range_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga90610e42e63eb4290e5ae6187a53143f)
- [linear_range_group_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#gab8b661f6ed1caba2ab4796a02c1b24a8)
- [linear_range_get_win_index](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga6c06a26d629f4d7a195188e7c5df5db1)
- [linear_range_group_get_win_index](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga11dc5408be53887e9ddf992b574aa16c)

<a id="header-details"></a>

---

[上一章](P020_zephyr__dt-bindings__clock__kinetis_sim.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__dt-bindings__lvgl__lvgl.h_文件参考.md)
