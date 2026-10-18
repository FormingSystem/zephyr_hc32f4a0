---
id: learning.zephyr-docs.api-coap-trusted-topic-reference.page-11
title: 值容器（Value Container）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_值容器（Value Container）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

一个带类型的标量或范围，是能力描述中的最小组成部分。

<a id="details"></a>

一个带类型的标量（Typed Scalar）或范围（Range），是能力（Capability）的最小组成部分。能力结构体（Capability Structure）的字段保存一个值容器（Value Container）：布尔值、有符号或无符号整数，或者其中某种类型的 {min, max, step} 范围。范围用于表达设备接受的是一段取值而非单一设置，例如从 16 到 1280、步长为 2 的每个宽度；之后通过固定化（Fixation）从中选出单一值。它是一个带标签的联合体（Tagged Union），所有分支均不含指针，因此在所有目标平台上大小相同，复制只需普通赋值，也没有需要释放的内容。这使能力可以按值传递并放入 .rodata。类型集合刻意只保留这两种形态，因为它们对求交运算封闭（Closed under Intersection）：两个值的交集不会比输入更大，因此结果始终能装入调用者已有的存储空间。“备选项集合”类型会破坏这一性质，迫使实现重新引入分配操作，因此备选项改由枚举索引（Enumeration Index）承载，参见端口（Pad）。除非参数文档另有说明，传给此 API 的指针不得为 NULL。

<a id="header-files"></a>
<a id="files"></a>

## 11.1\_文件（Files）

<a id="r_mpipe_5Fvalue_2Eh"></a>

```c
file mpipe_value.h
```

相关声明：[mpipe_value.h](../api_file_secure_value_reference/P009_zephyr__mpipe__mpipe_value.h_文件参考.md)。

值（Value）：能力（Capability）中的一个带类型标量或范围。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fvalue_5Fbound"></a>

```c
union mpipe_value_bound
```

相关声明：[mpipe_value_bound](../audio_video_model_reference/P069_mpipe_value_bound_联合体.md)。

范围值（Range Value）的一个端点或其步长。

<a id="r_mpipe_5Fvalue"></a>

```c
struct mpipe_value
```

相关声明：[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

值结构（Value Structure）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.3\_枚举（Enumerations）

<a id="r_ga8b8b4952140ae9ef7e6e6f20aa99d8a2"></a>

```c
enum mpipe_value_type { MPIPE_TYPE_NONE = 0 , MPIPE_TYPE_BOOLEAN , MPIPE_TYPE_INT , MPIPE_TYPE_UINT , MPIPE_TYPE_INT_RANGE , MPIPE_TYPE_UINT_RANGE , MPIPE_TYPE_COUNT }
```

相关声明：[mpipe_value_type](#ga8b8b4952140ae9ef7e6e6f20aa99d8a2)、[MPIPE_TYPE_NONE](#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9d90529abe23dd8b2346cc47212af483)、[MPIPE_TYPE_BOOLEAN](#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9df697bcc6be8ac96ea9e8c862948f7b)、[MPIPE_TYPE_INT](#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a8d4de97628bb39128f353f54e62030f5)、[MPIPE_TYPE_UINT](#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a7efc72efde7c116938e3e4f3cc15da09)、[MPIPE_TYPE_INT_RANGE](#gga8b8b4952140ae9ef7e6e6f20aa99d8a2afaa7d6005a03d2cb0d4077a40b77c583)、[MPIPE_TYPE_UINT_RANGE](#gga8b8b4952140ae9ef7e6e6f20aa99d8a2aef1469edc9c29670a4fc061a84d9eea5)、[MPIPE_TYPE_COUNT](#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a56d11878056a9b9bf4a805523be15817)。

值类型（Value Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.4\_函数（Functions）

<a id="r_gaf0d9692302ff03a82cd93f7a2d0d3361"></a>

```c
int mpipe_value_set (struct mpipe_value *value, int type,...)
```

相关声明：[mpipe_value_set](#gaf0d9692302ff03a82cd93f7a2d0d3361)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

设置值的类型与内容（Type and Contents）。

<a id="r_gaa48c169a0b95ee16e2f3ed34f01de2f6"></a>

```c
int mpipe_value_set_va_list (struct mpipe_value *value, enum mpipe_value_type type, va_list *args)
```

相关声明：[mpipe_value_set_va_list](#gaa48c169a0b95ee16e2f3ed34f01de2f6)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)、[mpipe_value_type](#ga8b8b4952140ae9ef7e6e6f20aa99d8a2)。

通过 `va_list` 可变参数列表设置值（Value）。

<a id="r_ga1bfb3bbb99fb9cf85b8e31b4d96a8b99"></a>

```c
bool mpipe_value_get_boolean (const struct mpipe_value *value)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mpipe_value_get_boolean](#ga1bfb3bbb99fb9cf85b8e31b4d96a8b99)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_BOOLEAN` 类型的布尔值（Boolean Value）。

<a id="r_ga83b18949361ddd68ff58f6558b2f8ecb"></a>

```c
int32_t mpipe_value_get_int (const struct mpipe_value *value)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mpipe_value_get_int](#ga83b18949361ddd68ff58f6558b2f8ecb)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_INT` 类型的整数值（Int Value）。

<a id="r_ga2ba5453982763aa205afd9fba8cb5a14"></a>

```c
uint32_t mpipe_value_get_uint (const struct mpipe_value *value)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mpipe_value_get_uint](#ga2ba5453982763aa205afd9fba8cb5a14)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_UINT` 类型的无符号整数值（Uint Value）。

<a id="r_gae2bd5aa3194993312a5bbaa66c452ba1"></a>

```c
int32_t mpipe_value_get_int_range_min (const struct mpipe_value *range)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mpipe_value_get_int_range_min](#gae2bd5aa3194993312a5bbaa66c452ba1)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_INT_RANGE` 类型的最小值（Minimum Value）。

<a id="r_ga2acf7f0283f0f9770e8feeae9d409c43"></a>

```c
int32_t mpipe_value_get_int_range_max (const struct mpipe_value *range)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mpipe_value_get_int_range_max](#ga2acf7f0283f0f9770e8feeae9d409c43)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_INT_RANGE` 类型的最大值（Maximum Value）。

<a id="r_ga73ac34a14a3a829b2c643652c209ec0a"></a>

```c
int32_t mpipe_value_get_int_range_step (const struct mpipe_value *range)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mpipe_value_get_int_range_step](#ga73ac34a14a3a829b2c643652c209ec0a)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_INT_RANGE` 类型的步长值（Step Value）。

<a id="r_ga8fa023097fe09a526bd1304740010013"></a>

```c
uint32_t mpipe_value_get_uint_range_min (const struct mpipe_value *range)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mpipe_value_get_uint_range_min](#ga8fa023097fe09a526bd1304740010013)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_UINT_RANGE` 类型的最小值（Minimum Value）。

<a id="r_ga35e81ced0e49dc6efc999a92d4b4b38b"></a>

```c
uint32_t mpipe_value_get_uint_range_max (const struct mpipe_value *range)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mpipe_value_get_uint_range_max](#ga35e81ced0e49dc6efc999a92d4b4b38b)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_UINT_RANGE` 类型的最大值（Maximum Value）。

<a id="r_gabbc6cee1cdd20b0b7405a2e109677670"></a>

```c
uint32_t mpipe_value_get_uint_range_step (const struct mpipe_value *range)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mpipe_value_get_uint_range_step](#gabbc6cee1cdd20b0b7405a2e109677670)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_UINT_RANGE` 类型的步长值（Step Value）。

<a id="r_gad2db6ace74e12e07bf7cb01320a3feb0"></a>

```c
int mpipe_value_intersect (const struct mpipe_value *val1, const struct mpipe_value *val2, struct mpipe_value *out)
```

相关声明：[mpipe_value_intersect](#gad2db6ace74e12e07bf7cb01320a3feb0)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

对两个值求交（Intersect），将结果写入调用方提供的存储。

<a id="r_ga4a39e21b247f3adb27da9d6f0248d9f9"></a>

```c
bool mpipe_value_is_primitive (const struct mpipe_value *value)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mpipe_value_is_primitive](#ga4a39e21b247f3adb27da9d6f0248d9f9)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

检查某值是否持有单个布尔值或整数，而非范围（Range）。

<a id="r_ga13c68ab945becac3b8c05149abec8568"></a>

```c
void mpipe_value_print (const struct mpipe_value *value, bool new_line)
```

相关声明：[mpipe_value_print](#ga13c68ab945becac3b8c05149abec8568)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

打印值（Print a Value）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 11.5\_静态定义值的初始化器（Initializers for a Statically Defined Value）

每个宏展开为一个值容器（Value Container）的花括号初始化器（Braced Initializer），因此在构建时已知的能力可放入 `.rodata`，而无需在运行时构造。

它们是 `MPIPE_STRUCTURE_DEFINE` 为各字段接收的初始化项。范围形式（Range Forms）接收上下界以及相邻两个值之间的步长（Step）。

<a id="r_ga899a3751da2039ee1df0278bab421ce9"></a>

```c
#define MPIPE_VALUE_BOOLEAN(v)
```

相关声明：[MPIPE_VALUE_BOOLEAN](#ga899a3751da2039ee1df0278bab421ce9)。

初始化 `MPIPE_TYPE_BOOLEAN` 类型的值（Value）。

<a id="r_ga4e18027d1456c56d43a03c6d09535abc"></a>

```c
#define MPIPE_VALUE_INT(v)
```

相关声明：[MPIPE_VALUE_INT](#ga4e18027d1456c56d43a03c6d09535abc)。

初始化 `MPIPE_TYPE_INT` 类型的值（Value）。

<a id="r_ga2b50ff2eb9cbfa01dec5576af493b316"></a>

```c
#define MPIPE_VALUE_UINT(v)
```

相关声明：[MPIPE_VALUE_UINT](#ga2b50ff2eb9cbfa01dec5576af493b316)。

初始化 `MPIPE_TYPE_UINT` 类型的值（Value）。

<a id="r_ga9d5943f8476565aa00faaaffe88e1333"></a>

```c
#define MPIPE_VALUE_INT_RANGE(lo, hi, st)
```

相关声明：[MPIPE_VALUE_INT_RANGE](#ga9d5943f8476565aa00faaaffe88e1333)。

初始化 `MPIPE_TYPE_INT_RANGE` 类型的值（Value）。

<a id="r_gaf1293ecafc84321f2e9a3fab8e9a5966"></a>

```c
#define MPIPE_VALUE_UINT_RANGE(lo, hi, st)
```

相关声明：[MPIPE_VALUE_UINT_RANGE](#gaf1293ecafc84321f2e9a3fab8e9a5966)。

初始化 `MPIPE_TYPE_UINT_RANGE` 类型的值（Value）。

## 11.6\_详细说明（Detailed Documentation）

<a id="ga899a3751da2039ee1df0278bab421ce9"></a>

### `MPIPE_VALUE_BOOLEAN`

```c
#define MPIPE_VALUE_BOOLEAN ( v)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

展开值（Value）：

```c
{.type = MPIPE_TYPE_BOOLEAN, .v_boolean = (v)}
```

初始化 `MPIPE_TYPE_BOOLEAN` 类型的值（Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `v` | 该值保存的布尔值（Boolean）。 |

<a id="ga4e18027d1456c56d43a03c6d09535abc"></a>

### `MPIPE_VALUE_INT`

```c
#define MPIPE_VALUE_INT ( v)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

展开值（Value）：

```c
{.type = MPIPE_TYPE_INT, .v_int = (v)}
```

初始化 `MPIPE_TYPE_INT` 类型的值（Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `v` | 该值保存的有符号整数（Signed Integer）。 |

<a id="ga9d5943f8476565aa00faaaffe88e1333"></a>

### `MPIPE_VALUE_INT_RANGE`

```c
#define MPIPE_VALUE_INT_RANGE ( lo, hi, st )
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

展开值（Value）：

```c
{.type = MPIPE_TYPE_INT_RANGE, .range = MPIPE_VALUE_RANGE_INIT(v_int, lo, hi, st)}
```

初始化 `MPIPE_TYPE_INT_RANGE` 类型的值（Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lo` | 范围的最小值（Lowest Value），包含端点。 |
| `hi` | 范围的最大值（Highest Value），包含端点。 |
| `st` | 两个连续值之间的步长（Step）。 |

<a id="ga2b50ff2eb9cbfa01dec5576af493b316"></a>

### `MPIPE_VALUE_UINT`

```c
#define MPIPE_VALUE_UINT ( v)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

展开值（Value）：

```c
{.type = MPIPE_TYPE_UINT, .v_uint = (v)}
```

初始化 `MPIPE_TYPE_UINT` 类型的值（Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `v` | 该值保存的无符号整数（Unsigned Integer）。 |

<a id="gaf1293ecafc84321f2e9a3fab8e9a5966"></a>

### `MPIPE_VALUE_UINT_RANGE`

```c
#define MPIPE_VALUE_UINT_RANGE ( lo, hi, st )
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

展开值（Value）：

```c
{.type = MPIPE_TYPE_UINT_RANGE, .range = MPIPE_VALUE_RANGE_INIT(v_uint, lo, hi, st)}
```

初始化 `MPIPE_TYPE_UINT_RANGE` 类型的值（Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `lo` | 范围的最小值（Lowest Value），包含端点。 |
| `hi` | 范围的最大值（Highest Value），包含端点。 |
| `st` | 两个连续值之间的步长（Step）。 |

<a id="ga8b8b4952140ae9ef7e6e6f20aa99d8a2"></a>

### `mpipe_value_type`

```c
enum mpipe_value_type
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

值类型（Value Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_TYPE_NONE` | 无类型（No Type）。 |
| `MPIPE_TYPE_BOOLEAN` | 布尔值（Boolean Value）。 |
| `MPIPE_TYPE_INT` | 有符号整数值（Signed Integer Value）。 |
| `MPIPE_TYPE_UINT` | 无符号整数值（Unsigned Integer Value）。 |
| `MPIPE_TYPE_INT_RANGE` | 整数范围值（Integer Range Value）。 |
| `MPIPE_TYPE_UINT_RANGE` | 无符号整数范围值（Unsigned Integer Range Value）。 |
| `MPIPE_TYPE_COUNT` | 类型数量（Number of Types）。 |

<a id="ga1bfb3bbb99fb9cf85b8e31b4d96a8b99"></a>

### `mpipe_value_get_boolean()`

```c
bool mpipe_value_get_boolean ( const struct mpipe_value * value)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

获取 `MPIPE_TYPE_BOOLEAN` 类型的布尔值（Boolean Value）。

取值函数（Getters）读取所请求的成员时不检查类型，因此调用者负责传入类型匹配的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `value` | 指向值（Value）的指针。 |

返回（Returns）：该值保存的布尔值（Boolean）。

<a id="ga83b18949361ddd68ff58f6558b2f8ecb"></a>

### `mpipe_value_get_int()`

```c
int32_t mpipe_value_get_int ( const struct mpipe_value * value)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

获取 `MPIPE_TYPE_INT` 类型的整数值（Int Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `value` | 指向值（Value）的指针。 |

返回（Returns）：该值保存的整数（Integer）。

<a id="ga2acf7f0283f0f9770e8feeae9d409c43"></a>

### `mpipe_value_get_int_range_max()`

```c
int32_t mpipe_value_get_int_range_max ( const struct mpipe_value * range)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

获取 `MPIPE_TYPE_INT_RANGE` 类型的最大值（Maximum Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `range` | 指向范围值（Range Value）的指针。 |

返回（Returns）：范围的上界（Upper Bound）。

<a id="gae2bd5aa3194993312a5bbaa66c452ba1"></a>

### `mpipe_value_get_int_range_min()`

```c
int32_t mpipe_value_get_int_range_min ( const struct mpipe_value * range)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

获取 `MPIPE_TYPE_INT_RANGE` 类型的最小值（Minimum Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `range` | 指向范围值（Range Value）的指针。 |

返回（Returns）：范围的下界（Lower Bound）。

<a id="ga73ac34a14a3a829b2c643652c209ec0a"></a>

### `mpipe_value_get_int_range_step()`

```c
int32_t mpipe_value_get_int_range_step ( const struct mpipe_value * range)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

获取 `MPIPE_TYPE_INT_RANGE` 类型的步长值（Step Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `range` | 指向范围值（Range Value）的指针。 |

返回（Returns）：范围中两个连续值之间的步长（Step）。

<a id="ga2ba5453982763aa205afd9fba8cb5a14"></a>

### `mpipe_value_get_uint()`

```c
uint32_t mpipe_value_get_uint ( const struct mpipe_value * value)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

获取 `MPIPE_TYPE_UINT` 类型的无符号整数值（Uint Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `value` | 指向值（Value）的指针。 |

返回（Returns）：该值保存的无符号整数（Unsigned Integer）。

<a id="ga35e81ced0e49dc6efc999a92d4b4b38b"></a>

### `mpipe_value_get_uint_range_max()`

```c
uint32_t mpipe_value_get_uint_range_max ( const struct mpipe_value * range)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

获取 `MPIPE_TYPE_UINT_RANGE` 类型的最大值（Maximum Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `range` | 指向范围值（Range Value）的指针。 |

返回（Returns）：范围的上界（Upper Bound）。

<a id="ga8fa023097fe09a526bd1304740010013"></a>

### `mpipe_value_get_uint_range_min()`

```c
uint32_t mpipe_value_get_uint_range_min ( const struct mpipe_value * range)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

获取 `MPIPE_TYPE_UINT_RANGE` 类型的最小值（Minimum Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `range` | 指向范围值（Range Value）的指针。 |

返回（Returns）：范围的下界（Lower Bound）。

<a id="gabbc6cee1cdd20b0b7405a2e109677670"></a>

### `mpipe_value_get_uint_range_step()`

```c
uint32_t mpipe_value_get_uint_range_step ( const struct mpipe_value * range)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

获取 `MPIPE_TYPE_UINT_RANGE` 类型的步长值（Step Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `range` | 指向范围值（Range Value）的指针。 |

返回（Returns）：范围中两个连续值之间的步长（Step）。

<a id="gad2db6ace74e12e07bf7cb01320a3feb0"></a>

### `mpipe_value_intersect()`

```c
int mpipe_value_intersect ( const struct mpipe_value * val1, const struct mpipe_value * val2, struct mpipe_value * out )
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

对两个值求交（Intersect），将结果写入调用方提供的存储。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` val1` | 指向第一个值（First Value）的指针。 |
| ` val2` | 指向第二个值（Second Value）的指针。 |
| `[out] out` | 指向结果存储空间（Result Storage）的指针；除非返回 0，否则该空间不被修改。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOENT` | 交集（Intersection）为空。 |

<a id="ga4a39e21b247f3adb27da9d6f0248d9f9"></a>

### `mpipe_value_is_primitive()`

```c
bool mpipe_value_is_primitive ( const struct mpipe_value * value)
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

检查某值是否持有单个布尔值或整数，而非范围（Range）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `value` | 指向待检查值（Value）的指针。 |

返回（Returns）：布尔值、整数或无符号整数为 true，范围（Range）为 false。

<a id="ga13c68ab945becac3b8c05149abec8568"></a>

### `mpipe_value_print()`

```c
void mpipe_value_print ( const struct mpipe_value * value, bool new_line )
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

打印值（Print a Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `value` | 指向待打印值（Value）的指针。 |
| `new_line` | 打印后添加换行（Newline）。 |

<a id="gaf0d9692302ff03a82cd93f7a2d0d3361"></a>

### `mpipe_value_set()`

```c
int mpipe_value_set ( struct mpipe_value * value, int type, ... )
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

设置值的类型与内容（Type and Contents）。

BOOLEAN、INT 和 UINT 接受一个参数；范围类型（Range Types）接受 min、max 和 step。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] value` | 指向待设置值（Value）的指针。 |
| ` type` | 值的类型（Type），参见 mpipe_value_type。以 int 传递，因为 va_start() 需要一个宽度不小于 int 的参数。 |
| ` ...` | 按上述规则初始化该值的参数（Arguments）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | type 无效（Invalid Type）。 |

<a id="gaa48c169a0b95ee16e2f3ed34f01de2f6"></a>

### `mpipe_value_set_va_list()`

```c
int mpipe_value_set_va_list ( struct mpipe_value * value, enum mpipe_value_type type, va_list * args )
```

```c
#include <zephyr/mpipe/mpipe_value.h>
```

通过 `va_list` 可变参数列表设置值（Value）。

与 mpipe_value_set 相同，但接受 va_list 指针而非可变参数（Variadic Arguments），使解析自身参数列表的调用者能够就地构造值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] value` | 指向待设置值（Value）的指针。 |
| ` type` | 值的类型（Type），参见 mpipe_value_type。 |
| ` args` | 指向 va_list 的指针，该列表已定位到此值对应的参数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | type 无效（Invalid Type）。 |


## 11.7\_原页交叉引用（Cross References）

- [mpipe_value.h](../api_file_secure_value_reference/P009_zephyr__mpipe__mpipe_value.h_文件参考.md)
- [mpipe_value_bound](../audio_video_model_reference/P069_mpipe_value_bound_联合体.md)
- [mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [值容器（Value Container）](P011_值容器（Value Container）.md)
- [MPIPE_STRUCTURE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gaa967e963ad810470b92727eeb4bc35d2)
- [能力结构（Capability Structure）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html)
- [min](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [连接端口（Pad）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9df697bcc6be8ac96ea9e8c862948f7b"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2a8d4de97628bb39128f353f54e62030f5"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2afaa7d6005a03d2cb0d4077a40b77c583"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2a7efc72efde7c116938e3e4f3cc15da09"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2aef1469edc9c29670a4fc061a84d9eea5"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9d90529abe23dd8b2346cc47212af483"></a>
<a id="gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9df697bcc6be8ac96ea9e8c862948f7b"></a>
<a id="gga8b8b4952140ae9ef7e6e6f20aa99d8a2a8d4de97628bb39128f353f54e62030f5"></a>
<a id="gga8b8b4952140ae9ef7e6e6f20aa99d8a2a7efc72efde7c116938e3e4f3cc15da09"></a>
<a id="gga8b8b4952140ae9ef7e6e6f20aa99d8a2afaa7d6005a03d2cb0d4077a40b77c583"></a>
<a id="gga8b8b4952140ae9ef7e6e6f20aa99d8a2aef1469edc9c29670a4fc061a84d9eea5"></a>
<a id="gga8b8b4952140ae9ef7e6e6f20aa99d8a2a56d11878056a9b9bf4a805523be15817"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_传输管理（Transport management）.md) · [返回大纲](大纲.md) · [下一章](P012_可信执行环境（TEE）.md)
