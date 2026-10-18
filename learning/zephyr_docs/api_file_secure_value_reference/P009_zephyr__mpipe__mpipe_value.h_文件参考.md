---
id: learning.zephyr-docs.api-file-secure-value-reference.page-9
title: zephyr__mpipe__mpipe_value.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__value_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_mpipe\_\_mpipe\_value.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__value_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

值（Value）：能力（Capability）中的一个带类型标量或范围。

<a id="details"></a>

```c
#include <stdarg.h>
#include <stdbool.h>
#include <stdint.h>
```

查看此文件的源码。

值（Value）：能力（Capability）中的一个带类型标量或范围。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 静态定义值的初始化器（Initializers for a Statically Defined Value）

每个宏展开为一个值容器（Value Container）的花括号初始化器（Braced Initializer），因此在构建时已知的能力可放入 `.rodata`，而无需在运行时构造。

它们是 `MPIPE_STRUCTURE_DEFINE` 为各字段接收的初始化项。范围形式（Range Forms）接收上下界以及相邻两个值之间的步长（Step）。

<a id="r_ga899a3751da2039ee1df0278bab421ce9"></a>

```c
#define MPIPE_VALUE_BOOLEAN(v)
```

相关声明：[MPIPE_VALUE_BOOLEAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga899a3751da2039ee1df0278bab421ce9)。

初始化 `MPIPE_TYPE_BOOLEAN` 类型的值（Value）。

<a id="r_ga4e18027d1456c56d43a03c6d09535abc"></a>

```c
#define MPIPE_VALUE_INT(v)
```

相关声明：[MPIPE_VALUE_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga4e18027d1456c56d43a03c6d09535abc)。

初始化 `MPIPE_TYPE_INT` 类型的值（Value）。

<a id="r_ga2b50ff2eb9cbfa01dec5576af493b316"></a>

```c
#define MPIPE_VALUE_UINT(v)
```

相关声明：[MPIPE_VALUE_UINT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga2b50ff2eb9cbfa01dec5576af493b316)。

初始化 `MPIPE_TYPE_UINT` 类型的值（Value）。

<a id="r_ga9d5943f8476565aa00faaaffe88e1333"></a>

```c
#define MPIPE_VALUE_INT_RANGE(lo, hi, st)
```

相关声明：[MPIPE_VALUE_INT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga9d5943f8476565aa00faaaffe88e1333)。

初始化 `MPIPE_TYPE_INT_RANGE` 类型的值（Value）。

<a id="r_gaf1293ecafc84321f2e9a3fab8e9a5966"></a>

```c
#define MPIPE_VALUE_UINT_RANGE(lo, hi, st)
```

相关声明：[MPIPE_VALUE_UINT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gaf1293ecafc84321f2e9a3fab8e9a5966)。

初始化 `MPIPE_TYPE_UINT_RANGE` 类型的值（Value）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.3\_枚举（Enumerations）

<a id="r_ga8b8b4952140ae9ef7e6e6f20aa99d8a2"></a>

```c
enum mpipe_value_type { MPIPE_TYPE_NONE = 0 , MPIPE_TYPE_BOOLEAN , MPIPE_TYPE_INT , MPIPE_TYPE_UINT , MPIPE_TYPE_INT_RANGE , MPIPE_TYPE_UINT_RANGE , MPIPE_TYPE_COUNT }
```

相关声明：[mpipe_value_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga8b8b4952140ae9ef7e6e6f20aa99d8a2)、[MPIPE_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9d90529abe23dd8b2346cc47212af483)、[MPIPE_TYPE_BOOLEAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9df697bcc6be8ac96ea9e8c862948f7b)、[MPIPE_TYPE_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a8d4de97628bb39128f353f54e62030f5)、[MPIPE_TYPE_UINT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a7efc72efde7c116938e3e4f3cc15da09)、[MPIPE_TYPE_INT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2afaa7d6005a03d2cb0d4077a40b77c583)、[MPIPE_TYPE_UINT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2aef1469edc9c29670a4fc061a84d9eea5)、[MPIPE_TYPE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a56d11878056a9b9bf4a805523be15817)。

值类型（Value Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.4\_函数（Functions）

<a id="r_gaf0d9692302ff03a82cd93f7a2d0d3361"></a>

```c
int mpipe_value_set (struct mpipe_value *value, int type,...)
```

相关声明：[mpipe_value_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gaf0d9692302ff03a82cd93f7a2d0d3361)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

设置值的类型与内容（Type and Contents）。

<a id="r_gaa48c169a0b95ee16e2f3ed34f01de2f6"></a>

```c
int mpipe_value_set_va_list (struct mpipe_value *value, enum mpipe_value_type type, va_list *args)
```

相关声明：[mpipe_value_set_va_list](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gaa48c169a0b95ee16e2f3ed34f01de2f6)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)、[mpipe_value_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga8b8b4952140ae9ef7e6e6f20aa99d8a2)。

通过 `va_list` 可变参数列表设置值（Value）。

<a id="r_ga1bfb3bbb99fb9cf85b8e31b4d96a8b99"></a>

```c
bool mpipe_value_get_boolean (const struct mpipe_value *value)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mpipe_value_get_boolean](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga1bfb3bbb99fb9cf85b8e31b4d96a8b99)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_BOOLEAN` 类型的布尔值（Boolean Value）。

<a id="r_ga83b18949361ddd68ff58f6558b2f8ecb"></a>

```c
int32_t mpipe_value_get_int (const struct mpipe_value *value)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mpipe_value_get_int](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga83b18949361ddd68ff58f6558b2f8ecb)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_INT` 类型的整数值（Int Value）。

<a id="r_ga2ba5453982763aa205afd9fba8cb5a14"></a>

```c
uint32_t mpipe_value_get_uint (const struct mpipe_value *value)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mpipe_value_get_uint](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga2ba5453982763aa205afd9fba8cb5a14)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_UINT` 类型的无符号整数值（Uint Value）。

<a id="r_gae2bd5aa3194993312a5bbaa66c452ba1"></a>

```c
int32_t mpipe_value_get_int_range_min (const struct mpipe_value *range)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mpipe_value_get_int_range_min](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gae2bd5aa3194993312a5bbaa66c452ba1)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_INT_RANGE` 类型的最小值（Minimum Value）。

<a id="r_ga2acf7f0283f0f9770e8feeae9d409c43"></a>

```c
int32_t mpipe_value_get_int_range_max (const struct mpipe_value *range)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mpipe_value_get_int_range_max](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga2acf7f0283f0f9770e8feeae9d409c43)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_INT_RANGE` 类型的最大值（Maximum Value）。

<a id="r_ga73ac34a14a3a829b2c643652c209ec0a"></a>

```c
int32_t mpipe_value_get_int_range_step (const struct mpipe_value *range)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[mpipe_value_get_int_range_step](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga73ac34a14a3a829b2c643652c209ec0a)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_INT_RANGE` 类型的步长值（Step Value）。

<a id="r_ga8fa023097fe09a526bd1304740010013"></a>

```c
uint32_t mpipe_value_get_uint_range_min (const struct mpipe_value *range)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mpipe_value_get_uint_range_min](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga8fa023097fe09a526bd1304740010013)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_UINT_RANGE` 类型的最小值（Minimum Value）。

<a id="r_ga35e81ced0e49dc6efc999a92d4b4b38b"></a>

```c
uint32_t mpipe_value_get_uint_range_max (const struct mpipe_value *range)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mpipe_value_get_uint_range_max](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga35e81ced0e49dc6efc999a92d4b4b38b)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_UINT_RANGE` 类型的最大值（Maximum Value）。

<a id="r_gabbc6cee1cdd20b0b7405a2e109677670"></a>

```c
uint32_t mpipe_value_get_uint_range_step (const struct mpipe_value *range)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mpipe_value_get_uint_range_step](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gabbc6cee1cdd20b0b7405a2e109677670)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

获取 `MPIPE_TYPE_UINT_RANGE` 类型的步长值（Step Value）。

<a id="r_gad2db6ace74e12e07bf7cb01320a3feb0"></a>

```c
int mpipe_value_intersect (const struct mpipe_value *val1, const struct mpipe_value *val2, struct mpipe_value *out)
```

相关声明：[mpipe_value_intersect](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gad2db6ace74e12e07bf7cb01320a3feb0)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

对两个值求交（Intersect），将结果写入调用方提供的存储。

<a id="r_ga4a39e21b247f3adb27da9d6f0248d9f9"></a>

```c
bool mpipe_value_is_primitive (const struct mpipe_value *value)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mpipe_value_is_primitive](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga4a39e21b247f3adb27da9d6f0248d9f9)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

检查某值是否持有单个布尔值或整数，而非范围（Range）。

<a id="r_ga13c68ab945becac3b8c05149abec8568"></a>

```c
void mpipe_value_print (const struct mpipe_value *value, bool new_line)
```

相关声明：[mpipe_value_print](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga13c68ab945becac3b8c05149abec8568)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

打印值（Print a Value）。


## 9.5\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P564_mpipe_value.h_源码浏览.md)
- [mpipe_value_bound](../audio_video_model_reference/P069_mpipe_value_bound_联合体.md)
- [mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)
- [值容器（Value Container）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html)
- [MPIPE_STRUCTURE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gaa967e963ad810470b92727eeb4bc35d2)
- [MPIPE_VALUE_BOOLEAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga899a3751da2039ee1df0278bab421ce9)
- [MPIPE_VALUE_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga4e18027d1456c56d43a03c6d09535abc)
- [MPIPE_VALUE_UINT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga2b50ff2eb9cbfa01dec5576af493b316)
- [MPIPE_VALUE_INT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga9d5943f8476565aa00faaaffe88e1333)
- [MPIPE_VALUE_UINT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gaf1293ecafc84321f2e9a3fab8e9a5966)
- [mpipe_value_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga8b8b4952140ae9ef7e6e6f20aa99d8a2)
- [MPIPE_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9d90529abe23dd8b2346cc47212af483)
- [MPIPE_TYPE_BOOLEAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a9df697bcc6be8ac96ea9e8c862948f7b)
- [MPIPE_TYPE_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a8d4de97628bb39128f353f54e62030f5)
- [MPIPE_TYPE_UINT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a7efc72efde7c116938e3e4f3cc15da09)
- [MPIPE_TYPE_INT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2afaa7d6005a03d2cb0d4077a40b77c583)
- [MPIPE_TYPE_UINT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2aef1469edc9c29670a4fc061a84d9eea5)
- [MPIPE_TYPE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a56d11878056a9b9bf4a805523be15817)
- [mpipe_value_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gaf0d9692302ff03a82cd93f7a2d0d3361)
- [mpipe_value_set_va_list](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gaa48c169a0b95ee16e2f3ed34f01de2f6)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mpipe_value_get_boolean](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga1bfb3bbb99fb9cf85b8e31b4d96a8b99)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [mpipe_value_get_int](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga83b18949361ddd68ff58f6558b2f8ecb)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mpipe_value_get_uint](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga2ba5453982763aa205afd9fba8cb5a14)
- [mpipe_value_get_int_range_min](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gae2bd5aa3194993312a5bbaa66c452ba1)
- [mpipe_value_get_int_range_max](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga2acf7f0283f0f9770e8feeae9d409c43)
- [mpipe_value_get_int_range_step](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga73ac34a14a3a829b2c643652c209ec0a)
- [mpipe_value_get_uint_range_min](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga8fa023097fe09a526bd1304740010013)
- [mpipe_value_get_uint_range_max](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga35e81ced0e49dc6efc999a92d4b4b38b)
- [mpipe_value_get_uint_range_step](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gabbc6cee1cdd20b0b7405a2e109677670)
- [mpipe_value_intersect](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#gad2db6ace74e12e07bf7cb01320a3feb0)
- [mpipe_value_is_primitive](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga4a39e21b247f3adb27da9d6f0248d9f9)
- [mpipe_value_print](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga13c68ab945becac3b8c05149abec8568)

<a id="header-details"></a>

---

[上一章](P008_zephyr__authentication__fido2__fido2_transport.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__net__net_pkt_filter.h_文件参考.md)
