---
id: learning.zephyr-docs.api-file-display-management-reference.page-14
title: zephyr__mpipe__mpipe_structure.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_mpipe\_\_mpipe\_structure.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

结构（Structure）：按值保存的一项媒体能力。

<a id="details"></a>

```c
#include <zephyr/sys/clock.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>
#include <zephyr/mpipe/mpipe_value.h>
```

查看此文件的源码。

结构（Structure）：按值保存的一项媒体能力。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fstructure"></a>

```c
struct mpipe_structure
```

相关声明：[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

保存一项能力（Capability）各字段的固定大小容器。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="r_ga7dbe4e58b6341ace2fcde09c07a66dde"></a>

```c
#define MPIPE_STRUCTURE_FLAG_ANY BIT(0)
```

相关声明：[MPIPE_STRUCTURE_FLAG_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga7dbe4e58b6341ace2fcde09c07a66dde)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此结构体不施加任何约束（Constraints），并可与任何结构体求交（Intersect）。

<a id="r_gac63999f3f00bec42196165cfe1694874"></a>

```c
#define MPIPE_FRAME_INTERVAL_FROM_FPS(fps)
```

相关声明：[MPIPE_FRAME_INTERVAL_FROM_FPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gac63999f3f00bec42196165cfe1694874)。

将以每秒帧数（Frames Per Second）表示的帧率转换为以微秒表示的帧间隔（Frame Interval）。

<a id="r_gaa967e963ad810470b92727eeb4bc35d2"></a>

```c
#define MPIPE_STRUCTURE_DEFINE(name, media, fields)
```

相关声明：[MPIPE_STRUCTURE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gaa967e963ad810470b92727eeb4bc35d2)。

在 `.rodata` 中定义只读能力结构体（Read-only Capability Structure）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.3\_枚举（Enumerations）

<a id="r_ga4e2bcc7f5152bfde2579bd92618b7b1c"></a>

```c
enum mpipe_media_type { MPIPE_MEDIA_UNKNOWN = 0 , MPIPE_MEDIA_AUDIO_PCM , MPIPE_MEDIA_VIDEO , MPIPE_MEDIA_END }
```

相关声明：[mpipe_media_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga4e2bcc7f5152bfde2579bd92618b7b1c)、[MPIPE_MEDIA_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga4e2bcc7f5152bfde2579bd92618b7b1cac04c4bf302809da5ab5c6b8e78f26535)、[MPIPE_MEDIA_AUDIO_PCM](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga4e2bcc7f5152bfde2579bd92618b7b1cac073e563bbcd3df377182d86c6034238)、[MPIPE_MEDIA_VIDEO](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga4e2bcc7f5152bfde2579bd92618b7b1cae995eeebf430d56b51874dee59dfc229)、[MPIPE_MEDIA_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga4e2bcc7f5152bfde2579bd92618b7b1ca2e9e6d0b91c736d215cad5006c18e129)。

某项能力描述的媒体类型（Media Type）。

<a id="r_ga0165db3d65894c7832dc455e8014deb5"></a>

```c
enum mpipe_caps_field { MPIPE_CAPS_PIXEL_FORMAT = 0 , MPIPE_CAPS_IMAGE_WIDTH , MPIPE_CAPS_IMAGE_HEIGHT , MPIPE_CAPS_SAMPLE_RATE , MPIPE_CAPS_BIT_WIDTH , MPIPE_CAPS_NUM_CHANNELS , MPIPE_CAPS_INTERLEAVED , MPIPE_CAPS_FRAME_INTERVAL , MPIPE_CAPS_END }
```

相关声明：[mpipe_caps_field](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga0165db3d65894c7832dc455e8014deb5)、[MPIPE_CAPS_PIXEL_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5af6df871bfb3ef1eef9dfdd9688258618)、[MPIPE_CAPS_IMAGE_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5aee7394620f9cbe4286d81bc545379972)、[MPIPE_CAPS_IMAGE_HEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5ae38a51f8e24ed04612cbdd979b971611)、[MPIPE_CAPS_SAMPLE_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5ae3a26714ff3ddc7be070f9ce441e2e12)、[MPIPE_CAPS_BIT_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5a874c070db9ce6b7fde39fcc46f570190)、[MPIPE_CAPS_NUM_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5a237a9bcffe2ef8db7f4a3480275b2982)、[MPIPE_CAPS_INTERLEAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5aad9b61026d7e0713f36a7ccce47772b6)、[MPIPE_CAPS_FRAME_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5a36e899225b9f8d28b237c9230490d266)、[MPIPE_CAPS_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5a4e15c96bb5c63b61a7588f772fda3820)。

能力字段标识符（Caps Field Identifiers）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.4\_函数（Functions）

<a id="r_ga2b80afbbed288b46f8586f8ddc37cfde"></a>

```c
int mpipe_structure_init (struct mpipe_structure *structure, uint8_t media_type_id)
```

相关声明：[mpipe_structure_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga2b80afbbed288b46f8586f8ddc37cfde)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化能力结构体（Capability Structure）。

<a id="r_ga80b32dcb5bfd7de40323302c950a76d7"></a>

```c
int mpipe_structure_init_fields (struct mpipe_structure *structure, uint8_t media_type_id,...)
```

相关声明：[mpipe_structure_init_fields](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga80b32dcb5bfd7de40323302c950a76d7)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用媒体类型（Media Type）和字段列表初始化能力结构体（Capability Structure）。

<a id="r_ga51192c54b880d8a20c8d3d74c83482bd"></a>

```c
int mpipe_structure_init_any (struct mpipe_structure *structure)
```

相关声明：[mpipe_structure_init_any](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga51192c54b880d8a20c8d3d74c83482bd)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

初始化不施加任何约束的结构体（Structure）。

<a id="r_ga7c612e79af6a7c600af5a32b9ee36a7b"></a>

```c
bool mpipe_structure_is_any (const struct mpipe_structure *structure)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mpipe_structure_is_any](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga7c612e79af6a7c600af5a32b9ee36a7b)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

检查结构体是否为 `ANY`，即不施加任何约束（Constraints）。

<a id="r_gad0e14518c25e189a2f52383af6d56f66"></a>

```c
bool mpipe_structure_is_empty (const struct mpipe_structure *structure)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mpipe_structure_is_empty](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gad0e14518c25e189a2f52383af6d56f66)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

检查能力结构体（Capability Structure）是否不匹配任何内容。

<a id="r_ga50d3ad084dceffbff34dbd427fe65580"></a>

```c
int mpipe_structure_append_value (struct mpipe_structure *structure, uint8_t field_id, const struct mpipe_value *value)
```

相关声明：[mpipe_structure_append_value](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga50d3ad084dceffbff34dbd427fe65580)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

使用调用方拥有的存储（Caller-owned Storage），向能力结构体（Capability Structure）追加字段。

<a id="r_ga2d00586a6073ec63775e6f690c1738dc"></a>

```c
int mpipe_structure_copy_field (const struct mpipe_structure *src, struct mpipe_structure *dst, uint8_t field_id)
```

相关声明：[mpipe_structure_copy_field](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga2d00586a6073ec63775e6f690c1738dc)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将字段从一个能力结构体（Capability Structure）复制到另一个。

<a id="r_ga39287529dd4f6a3ad41d379cc99758fc"></a>

```c
int mpipe_structure_clear (struct mpipe_structure *structure)
```

相关声明：[mpipe_structure_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga39287529dd4f6a3ad41d379cc99758fc)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

清空能力结构体（Capability Structure），移除其携带的所有字段。

<a id="r_ga4c3f662227ccbf343d69e2db0597cb0b"></a>

```c
bool mpipe_structure_is_fixed (const struct mpipe_structure *structure)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mpipe_structure_is_fixed](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga4c3f662227ccbf343d69e2db0597cb0b)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

检查能力结构体（Capability Structure）是否已固定（Fixed）。

<a id="r_ga20cd6955b0e18fedccc784705a52a34e"></a>

```c
const struct mpipe_value * mpipe_structure_get_value (const struct mpipe_structure *structure, uint8_t field_id)
```

相关声明：[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)、[mpipe_structure_get_value](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga20cd6955b0e18fedccc784705a52a34e)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取能力结构体（Capability Structure）中某字段的值。

<a id="r_ga3c5ec431967b07d00bf2ad85dfbd22b4"></a>

```c
int mpipe_structure_remove_field (struct mpipe_structure *structure, uint8_t field_id)
```

相关声明：[mpipe_structure_remove_field](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga3c5ec431967b07d00bf2ad85dfbd22b4)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

移除能力结构体（Capability Structure）中的字段。

<a id="r_ga9e4df6b974dab5d79fb84eff549eb2c1"></a>

```c
int mpipe_structure_intersect (const struct mpipe_structure *struct1, const struct mpipe_structure *struct2, struct mpipe_structure *out)
```

相关声明：[mpipe_structure_intersect](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga9e4df6b974dab5d79fb84eff549eb2c1)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

对两个结构体求交（Intersect），结果写入调用方提供的存储。

<a id="r_ga7876dc8e926adb6bd229882ead04ac54"></a>

```c
int mpipe_structure_fixate (const struct mpipe_structure *src, struct mpipe_structure *out)
```

相关声明：[mpipe_structure_fixate](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga7876dc8e926adb6bd229882ead04ac54)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

将结构体的能力取值固定化（Fixate），结果写入调用方提供的存储。

<a id="r_gaf2a980631b57b9199d7f85cb2499a4e1"></a>

```c
void mpipe_structure_print (const struct mpipe_structure *structure)
```

相关声明：[mpipe_structure_print](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gaf2a980631b57b9199d7f85cb2499a4e1)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

打印能力结构体（Capability Structure）。


## 14.5\_原页交叉引用（Cross References）

- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [zephyr/mpipe/mpipe_value.h](../api_source_reference/P564_mpipe_value.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P560_mpipe_structure.h_源码浏览.md)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [MPIPE_STRUCTURE_FLAG_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga7dbe4e58b6341ace2fcde09c07a66dde)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [MPIPE_FRAME_INTERVAL_FROM_FPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gac63999f3f00bec42196165cfe1694874)
- [MPIPE_STRUCTURE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gaa967e963ad810470b92727eeb4bc35d2)
- [能力结构（Capability Structure）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html)
- [mpipe_media_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga4e2bcc7f5152bfde2579bd92618b7b1c)
- [MPIPE_MEDIA_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga4e2bcc7f5152bfde2579bd92618b7b1cac04c4bf302809da5ab5c6b8e78f26535)
- [MPIPE_MEDIA_AUDIO_PCM](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga4e2bcc7f5152bfde2579bd92618b7b1cac073e563bbcd3df377182d86c6034238)
- [MPIPE_MEDIA_VIDEO](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga4e2bcc7f5152bfde2579bd92618b7b1cae995eeebf430d56b51874dee59dfc229)
- [MPIPE_MEDIA_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga4e2bcc7f5152bfde2579bd92618b7b1ca2e9e6d0b91c736d215cad5006c18e129)
- [mpipe_caps_field](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga0165db3d65894c7832dc455e8014deb5)
- [MPIPE_CAPS_PIXEL_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5af6df871bfb3ef1eef9dfdd9688258618)
- [MPIPE_CAPS_IMAGE_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5aee7394620f9cbe4286d81bc545379972)
- [MPIPE_CAPS_IMAGE_HEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5ae38a51f8e24ed04612cbdd979b971611)
- [MPIPE_CAPS_SAMPLE_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5ae3a26714ff3ddc7be070f9ce441e2e12)
- [MPIPE_CAPS_BIT_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5a874c070db9ce6b7fde39fcc46f570190)
- [MPIPE_CAPS_NUM_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5a237a9bcffe2ef8db7f4a3480275b2982)
- [MPIPE_CAPS_INTERLEAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5aad9b61026d7e0713f36a7ccce47772b6)
- [MPIPE_CAPS_FRAME_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5a36e899225b9f8d28b237c9230490d266)
- [MPIPE_CAPS_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gga0165db3d65894c7832dc455e8014deb5a4e15c96bb5c63b61a7588f772fda3820)
- [mpipe_structure_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga2b80afbbed288b46f8586f8ddc37cfde)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_structure_init_fields](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga80b32dcb5bfd7de40323302c950a76d7)
- [mpipe_structure_init_any](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga51192c54b880d8a20c8d3d74c83482bd)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mpipe_structure_is_any](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga7c612e79af6a7c600af5a32b9ee36a7b)
- [mpipe_structure_is_empty](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gad0e14518c25e189a2f52383af6d56f66)
- [mpipe_structure_append_value](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga50d3ad084dceffbff34dbd427fe65580)
- [mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)
- [mpipe_structure_copy_field](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga2d00586a6073ec63775e6f690c1738dc)
- [mpipe_structure_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga39287529dd4f6a3ad41d379cc99758fc)
- [mpipe_structure_is_fixed](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga4c3f662227ccbf343d69e2db0597cb0b)
- [mpipe_structure_get_value](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga20cd6955b0e18fedccc784705a52a34e)
- [mpipe_structure_remove_field](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga3c5ec431967b07d00bf2ad85dfbd22b4)
- [mpipe_structure_intersect](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga9e4df6b974dab5d79fb84eff549eb2c1)
- [mpipe_structure_fixate](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga7876dc8e926adb6bd229882ead04ac54)
- [mpipe_structure_print](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#gaf2a980631b57b9199d7f85cb2499a4e1)

<a id="header-details"></a>

---

[上一章](P013_zephyr__bluetooth__audio__micp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__drivers__uart__serial_test.h_文件参考.md)
