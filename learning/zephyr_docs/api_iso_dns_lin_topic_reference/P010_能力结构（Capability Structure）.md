---
id: learning.zephyr-docs.api-iso-dns-lin-topic-reference.page-10
title: 能力结构（Capability Structure）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_能力结构（Capability Structure）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述一种媒体能力的固定大小容器。

<a id="details"></a>

描述单项媒体能力（Media Capability）的固定大小容器（Fixed-size Container）。

mpipe_structure 保存一组字段，每个字段由一个 mpipe_caps_field 标识符与一个值容器（Value Container）配对组成。它是按值持有的固定大小类型，无需分配内存：字段占用两个并行数组的前若干个槽位，一个数组保存字段名称，另一个保存值。

下面的视频能力可直接在调用者的存储空间中构造：

```c
video, format=VIDEO_PIX_FMT_RGB565, width=[16, 1280, 2], height=[16, 720, 2]
```

```c
struct mpipe_structure s;

mpipe_structure_init_fields(&s, MPIPE_MEDIA_VIDEO,
    MPIPE_CAPS_PIXEL_FORMAT, MPIPE_TYPE_UINT, VIDEO_PIX_FMT_RGB565,
    MPIPE_CAPS_IMAGE_WIDTH, MPIPE_TYPE_UINT_RANGE, 16, 1280, 2,
    MPIPE_CAPS_IMAGE_HEIGHT, MPIPE_TYPE_UINT_RANGE, 16, 720, 2,
    MPIPE_CAPS_END);
```

原文示例的符号说明：`mpipe_structure_init_fields` 的声明为 `int mpipe_structure_init_fields(struct mpipe_structure *structure, uint8_t media_type_id,...)`，根据媒体类型和字段列表初始化能力结构（Capability Structure）。`MPIPE_CAPS_END` 是最后一个字段标识符之后的值，定义于 `mpipe_structure.h:130`；`MPIPE_CAPS_IMAGE_HEIGHT` 和 `MPIPE_CAPS_IMAGE_WIDTH` 分别是以像素为单位的图像高度和宽度，类型为 MPIPE_TYPE_UINT，定义于 `mpipe_structure.h:107` 和 `mpipe_structure.h:105`；`MPIPE_CAPS_PIXEL_FORMAT` 是以 VIDEO_PIX_FMT_* 四字符码（FourCC）表示的像素格式，类型为 MPIPE_TYPE_UINT，定义于 `mpipe_structure.h:103`。`MPIPE_MEDIA_VIDEO` 表示视频，包括原始、拜耳（Bayer）和压缩格式，定义于 `mpipe_structure.h:74`。`MPIPE_TYPE_UINT` 为无符号整数值，`MPIPE_TYPE_UINT_RANGE` 为无符号整数范围值，分别定义于 `mpipe_value.h:56` 和 `mpipe_value.h:58`。宏 `VIDEO_PIX_FMT_RGB565` 使用 5 个红色位 [15:11]、6 个绿色位 [10:5]、5 个蓝色位 [4:0]，定义于 `formats.h:676`。`mpipe_structure` 是保存单项能力字段的固定大小容器，定义于 `mpipe_structure.h:165`。

范围写作 `[min, max, step]`，所以上面的宽度允许 16 到 1280 之间所有 2 的倍数。两个结构只有在媒体类型相同、至少有一个公共字段标识符，且每个公共字段的值均有交集时，才存在交集（Intersection）。结果包含双方字段的并集（Union）：公共字段保存值的交集，只存在于一方的字段原样传递。后一规则使约束可以沿元素链传递，即使链中的元素自身并不关心该约束。

除非参数说明另有规定，传入此 API 的指针不得为 NULL。

<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_mpipe_5Fstructure_2Eh"></a>

```c
file mpipe_structure.h
```

相关声明：[mpipe_structure.h](../api_file_display_management_reference/P014_zephyr__mpipe__mpipe_structure.h_文件参考.md)。

结构（Structure）：按值保存的一项媒体能力。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fstructure"></a>

```c
struct mpipe_structure
```

相关声明：[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

保存一项能力（Capability）各字段的固定大小容器。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.3\_宏定义（Macros）

<a id="r_ga7dbe4e58b6341ace2fcde09c07a66dde"></a>

```c
#define MPIPE_STRUCTURE_FLAG_ANY BIT(0)
```

相关声明：[MPIPE_STRUCTURE_FLAG_ANY](#ga7dbe4e58b6341ace2fcde09c07a66dde)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此结构体不施加任何约束（Constraints），并可与任何结构体求交（Intersect）。

<a id="r_gac63999f3f00bec42196165cfe1694874"></a>

```c
#define MPIPE_FRAME_INTERVAL_FROM_FPS(fps)
```

相关声明：[MPIPE_FRAME_INTERVAL_FROM_FPS](#gac63999f3f00bec42196165cfe1694874)。

将以每秒帧数（Frames Per Second）表示的帧率转换为以微秒表示的帧间隔（Frame Interval）。

<a id="r_gaa967e963ad810470b92727eeb4bc35d2"></a>

```c
#define MPIPE_STRUCTURE_DEFINE(name, media, fields)
```

相关声明：[MPIPE_STRUCTURE_DEFINE](#gaa967e963ad810470b92727eeb4bc35d2)。

在 `.rodata` 中定义只读能力结构体（Read-only Capability Structure）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.4\_枚举（Enumerations）

<a id="r_ga4e2bcc7f5152bfde2579bd92618b7b1c"></a>

```c
enum mpipe_media_type { MPIPE_MEDIA_UNKNOWN = 0 , MPIPE_MEDIA_AUDIO_PCM , MPIPE_MEDIA_VIDEO , MPIPE_MEDIA_END }
```

相关声明：[mpipe_media_type](#ga4e2bcc7f5152bfde2579bd92618b7b1c)、[MPIPE_MEDIA_UNKNOWN](#gga4e2bcc7f5152bfde2579bd92618b7b1cac04c4bf302809da5ab5c6b8e78f26535)、[MPIPE_MEDIA_AUDIO_PCM](#gga4e2bcc7f5152bfde2579bd92618b7b1cac073e563bbcd3df377182d86c6034238)、[MPIPE_MEDIA_VIDEO](#gga4e2bcc7f5152bfde2579bd92618b7b1cae995eeebf430d56b51874dee59dfc229)、[MPIPE_MEDIA_END](#gga4e2bcc7f5152bfde2579bd92618b7b1ca2e9e6d0b91c736d215cad5006c18e129)。

某项能力描述的媒体类型（Media Type）。

<a id="r_ga0165db3d65894c7832dc455e8014deb5"></a>

```c
enum mpipe_caps_field { MPIPE_CAPS_PIXEL_FORMAT = 0 , MPIPE_CAPS_IMAGE_WIDTH , MPIPE_CAPS_IMAGE_HEIGHT , MPIPE_CAPS_SAMPLE_RATE , MPIPE_CAPS_BIT_WIDTH , MPIPE_CAPS_NUM_CHANNELS , MPIPE_CAPS_INTERLEAVED , MPIPE_CAPS_FRAME_INTERVAL , MPIPE_CAPS_END }
```

相关声明：[mpipe_caps_field](#ga0165db3d65894c7832dc455e8014deb5)、[MPIPE_CAPS_PIXEL_FORMAT](#gga0165db3d65894c7832dc455e8014deb5af6df871bfb3ef1eef9dfdd9688258618)、[MPIPE_CAPS_IMAGE_WIDTH](#gga0165db3d65894c7832dc455e8014deb5aee7394620f9cbe4286d81bc545379972)、[MPIPE_CAPS_IMAGE_HEIGHT](#gga0165db3d65894c7832dc455e8014deb5ae38a51f8e24ed04612cbdd979b971611)、[MPIPE_CAPS_SAMPLE_RATE](#gga0165db3d65894c7832dc455e8014deb5ae3a26714ff3ddc7be070f9ce441e2e12)、[MPIPE_CAPS_BIT_WIDTH](#gga0165db3d65894c7832dc455e8014deb5a874c070db9ce6b7fde39fcc46f570190)、[MPIPE_CAPS_NUM_CHANNELS](#gga0165db3d65894c7832dc455e8014deb5a237a9bcffe2ef8db7f4a3480275b2982)、[MPIPE_CAPS_INTERLEAVED](#gga0165db3d65894c7832dc455e8014deb5aad9b61026d7e0713f36a7ccce47772b6)、[MPIPE_CAPS_FRAME_INTERVAL](#gga0165db3d65894c7832dc455e8014deb5a36e899225b9f8d28b237c9230490d266)、[MPIPE_CAPS_END](#gga0165db3d65894c7832dc455e8014deb5a4e15c96bb5c63b61a7588f772fda3820)。

能力字段标识符（Caps Field Identifiers）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.5\_函数（Functions）

<a id="r_ga2b80afbbed288b46f8586f8ddc37cfde"></a>

```c
int mpipe_structure_init (struct mpipe_structure *structure, uint8_t media_type_id)
```

相关声明：[mpipe_structure_init](#ga2b80afbbed288b46f8586f8ddc37cfde)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化能力结构体（Capability Structure）。

<a id="r_ga80b32dcb5bfd7de40323302c950a76d7"></a>

```c
int mpipe_structure_init_fields (struct mpipe_structure *structure, uint8_t media_type_id,...)
```

相关声明：[mpipe_structure_init_fields](#ga80b32dcb5bfd7de40323302c950a76d7)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用媒体类型（Media Type）和字段列表初始化能力结构体（Capability Structure）。

<a id="r_ga51192c54b880d8a20c8d3d74c83482bd"></a>

```c
int mpipe_structure_init_any (struct mpipe_structure *structure)
```

相关声明：[mpipe_structure_init_any](#ga51192c54b880d8a20c8d3d74c83482bd)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

初始化不施加任何约束的结构体（Structure）。

<a id="r_ga7c612e79af6a7c600af5a32b9ee36a7b"></a>

```c
bool mpipe_structure_is_any (const struct mpipe_structure *structure)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mpipe_structure_is_any](#ga7c612e79af6a7c600af5a32b9ee36a7b)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

检查结构体是否为 `ANY`，即不施加任何约束（Constraints）。

<a id="r_gad0e14518c25e189a2f52383af6d56f66"></a>

```c
bool mpipe_structure_is_empty (const struct mpipe_structure *structure)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mpipe_structure_is_empty](#gad0e14518c25e189a2f52383af6d56f66)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

检查能力结构体（Capability Structure）是否不匹配任何内容。

<a id="r_ga50d3ad084dceffbff34dbd427fe65580"></a>

```c
int mpipe_structure_append_value (struct mpipe_structure *structure, uint8_t field_id, const struct mpipe_value *value)
```

相关声明：[mpipe_structure_append_value](#ga50d3ad084dceffbff34dbd427fe65580)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)。

使用调用方拥有的存储（Caller-owned Storage），向能力结构体（Capability Structure）追加字段。

<a id="r_ga2d00586a6073ec63775e6f690c1738dc"></a>

```c
int mpipe_structure_copy_field (const struct mpipe_structure *src, struct mpipe_structure *dst, uint8_t field_id)
```

相关声明：[mpipe_structure_copy_field](#ga2d00586a6073ec63775e6f690c1738dc)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将字段从一个能力结构体（Capability Structure）复制到另一个。

<a id="r_ga39287529dd4f6a3ad41d379cc99758fc"></a>

```c
int mpipe_structure_clear (struct mpipe_structure *structure)
```

相关声明：[mpipe_structure_clear](#ga39287529dd4f6a3ad41d379cc99758fc)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

清空能力结构体（Capability Structure），移除其携带的所有字段。

<a id="r_ga4c3f662227ccbf343d69e2db0597cb0b"></a>

```c
bool mpipe_structure_is_fixed (const struct mpipe_structure *structure)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mpipe_structure_is_fixed](#ga4c3f662227ccbf343d69e2db0597cb0b)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

检查能力结构体（Capability Structure）是否已固定（Fixed）。

<a id="r_ga20cd6955b0e18fedccc784705a52a34e"></a>

```c
const struct mpipe_value * mpipe_structure_get_value (const struct mpipe_structure *structure, uint8_t field_id)
```

相关声明：[mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)、[mpipe_structure_get_value](#ga20cd6955b0e18fedccc784705a52a34e)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取能力结构体（Capability Structure）中某字段的值。

<a id="r_ga3c5ec431967b07d00bf2ad85dfbd22b4"></a>

```c
int mpipe_structure_remove_field (struct mpipe_structure *structure, uint8_t field_id)
```

相关声明：[mpipe_structure_remove_field](#ga3c5ec431967b07d00bf2ad85dfbd22b4)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

移除能力结构体（Capability Structure）中的字段。

<a id="r_ga9e4df6b974dab5d79fb84eff549eb2c1"></a>

```c
int mpipe_structure_intersect (const struct mpipe_structure *struct1, const struct mpipe_structure *struct2, struct mpipe_structure *out)
```

相关声明：[mpipe_structure_intersect](#ga9e4df6b974dab5d79fb84eff549eb2c1)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

对两个结构体求交（Intersect），结果写入调用方提供的存储。

<a id="r_ga7876dc8e926adb6bd229882ead04ac54"></a>

```c
int mpipe_structure_fixate (const struct mpipe_structure *src, struct mpipe_structure *out)
```

相关声明：[mpipe_structure_fixate](#ga7876dc8e926adb6bd229882ead04ac54)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

将结构体的能力取值固定化（Fixate），结果写入调用方提供的存储。

<a id="r_gaf2a980631b57b9199d7f85cb2499a4e1"></a>

```c
void mpipe_structure_print (const struct mpipe_structure *structure)
```

相关声明：[mpipe_structure_print](#gaf2a980631b57b9199d7f85cb2499a4e1)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

打印能力结构体（Capability Structure）。

## 10.6\_详细说明（Detailed Documentation）

<a id="gac63999f3f00bec42196165cfe1694874"></a>

### `MPIPE_FRAME_INTERVAL_FROM_FPS`

```c
#define MPIPE_FRAME_INTERVAL_FROM_FPS ( fps)
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

展开值（Value）：

```c
DIV_ROUND_CLOSEST(USEC_PER_SEC, (fps))
```

将以每秒帧数（Frames Per Second）表示的帧率转换为以微秒表示的帧间隔（Frame Interval）。

给出 MPIPE_CAPS_FRAME_INTERVAL 保存的值。如果帧率（Frame Rate）不能整除 1000000，应在各处采用相同舍入方式，以确保其表示在整个系统中一致。使用 DIV_ROUND_CLOSEST() 也与视频子系统和驱动一致。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fps` | 帧率（Frame Rate），单位为帧／秒，不得为 0。 |

**返回（Returns）**：返回：帧间隔（Frame Interval），单位为微秒。

<a id="gaa967e963ad810470b92727eeb4bc35d2"></a>

### `MPIPE_STRUCTURE_DEFINE`

```c
#define MPIPE_STRUCTURE_DEFINE ( name, media, fields )
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

展开值（Value）：

```c
BUILD_ASSERT((fields(MPIPE_STRUCTURE_FIELD_COUNT) 0) <= CONFIG_MPIPE_STRUCTURE_MAX_FIELDS, \
             #name " has more fields than CONFIG_MPIPE_STRUCTURE_MAX_FIELDS");             \
static const struct mpipe_structure name = {                                               \
        .media_type_id = (media),                                                          \
        .flags = 0,                                                                        \
        .num_fields = fields(MPIPE_STRUCTURE_FIELD_COUNT) 0,                               \
        .ids = {fields(MPIPE_STRUCTURE_FIELD_ID)},                                         \
        .values = {fields(MPIPE_STRUCTURE_FIELD_VALUE)},                                   \
}
```

在 `.rodata` 中定义只读能力结构体（Read-only Capability Structure）。

能力在构建时（Build Time）已知的元素可在此保存能力，无需在运行时构造；枚举时只需通过普通结构体赋值复制出一项。

fields 是接受一个参数的宏，以 arg(field_id, value_initializer) 形式将此参数应用于每个字段。只列出一次字段可以保证标识符、值与数量一致，避免因不一致而静默丢失字段。定义的字段数超过 CONFIG_MPIPE_STRUCTURE_MAX_FIELDS 时，构建会失败。

原始示例（Example）：

```c
#define JPEG_SRC_FIELDS(X) X(MPIPE_CAPS_PIXEL_FORMAT, MPIPE_VALUE_UINT(VIDEO_PIX_FMT_JPEG))
MPIPE_STRUCTURE_DEFINE(jpeg_src, MPIPE_MEDIA_VIDEO, JPEG_SRC_FIELDS);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 要定义的结构名称（Structure Name）。 |
| `media` | 结构的媒体类型（media type），参见 `mpipe_media_type`。 |
| `fields` | 列出字段的宏（Macro），参见上文。 |

<a id="ga7dbe4e58b6341ace2fcde09c07a66dde"></a>

### `MPIPE_STRUCTURE_FLAG_ANY`

```c
#define MPIPE_STRUCTURE_FLAG_ANY BIT(0)
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

此结构体不施加任何约束（Constraints），并可与任何结构体求交（Intersect）。

这不同于未设置任何字段的空结构（Empty Structure）；空结构与任何对象都没有交集。

<a id="ga0165db3d65894c7832dc455e8014deb5"></a>

### `mpipe_caps_field`

```c
enum mpipe_caps_field
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

能力字段标识符（Caps Field Identifiers）。

能力结构（Capability Structure）的字段由下列标识符之一与一个值容器（Value Container）配对组成。下列各条目注明承载它的值类型。如果能力提供一个范围而不是单一设置，则使用对应的范围类型，例如条目写 MPIPE_TYPE_UINT 时使用 MPIPE_TYPE_UINT_RANGE；设备藉此通告 16 到 1280 之间的所有宽度，而非单个宽度。随后，协商（Negotiation）缩小范围，定值（Fixation）从中选出一个值。MPIPE_CAPS_PIXEL_FORMAT 和 MPIPE_CAPS_INTERLEAVED 等属于例外：它们没有有意义的范围形式，因此始终以固定值承载。

能力字段（Caps Field）描述从源端口（Source Pad）经链路传到接收端口（Sink Pad）的数据，因此两端必须对它达成一致；属性（Property）则配置单个元素，参见对象（Objects）。只有两个不同元素必须对某个值达成一致才能保证流正确时，才添加字段，例如 MPIPE_CAPS_IMAGE_WIDTH；优先采用整个领域共同认可的字段，因为结构同时最多只能保存 CONFIG_MPIPE_STRUCTURE_MAX_FIELDS 个字段。

将其添加在 MPIPE_CAPS_END 之前，并仿照下列条目说明单位（Unit）和值类型（Value Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_CAPS_PIXEL_FORMAT` | 像素格式（Pixel Format），以 VIDEO_PIX_FMT_* 四字符码（FourCC）表示，类型为 MPIPE_TYPE_UINT。 |
| `MPIPE_CAPS_IMAGE_WIDTH` | 图像宽度（Image Width），单位为像素，类型为 MPIPE_TYPE_UINT。 |
| `MPIPE_CAPS_IMAGE_HEIGHT` | 图像高度（Image Height），单位为像素，类型为 MPIPE_TYPE_UINT。 |
| `MPIPE_CAPS_SAMPLE_RATE` | 采样频率（Sampling Frequency），单位为 Hz，用于音频，类型为 MPIPE_TYPE_UINT。 |
| `MPIPE_CAPS_BIT_WIDTH` | 采样大小（Sample Size），单位为位，用于音频，类型为 MPIPE_TYPE_UINT。 |
| `MPIPE_CAPS_NUM_CHANNELS` | 声道数（Number of Channels），用于音频，类型为 MPIPE_TYPE_UINT。 |
| `MPIPE_CAPS_INTERLEAVED` | 缓冲区内的声道布局（Channel Layout），用于音频，类型为 MPIPE_TYPE_BOOLEAN：true 表示交错（Interleaved，LRLRLRLR），false 表示非交错（Non-interleaved，LLLLRRRR）。 |
| `MPIPE_CAPS_FRAME_INTERVAL` | 一帧覆盖的时间，单位为微秒，类型为 MPIPE_TYPE_UINT。供音频和视频领域共同使用；对于视频，它是帧间隔（Frame Interval），即帧率的倒数。 |
| `MPIPE_CAPS_END` | 最后一个字段标识符（Field Identifier）之后的值。界定有效标识符范围，并终止 mpipe_structure_init_fields 的字段列表。 |

<a id="ga4e2bcc7f5152bfde2579bd92618b7b1c"></a>

### `mpipe_media_type`

```c
enum mpipe_media_type
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

某项能力描述的媒体类型（Media Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_MEDIA_UNKNOWN` | 未知媒体类型（Unknown Media Type），由 ANY 结构使用。 |
| `MPIPE_MEDIA_AUDIO_PCM` | 脉冲编码调制（PCM）格式的音频。 |
| `MPIPE_MEDIA_VIDEO` | 视频（Video），包括原始、拜耳（Bayer）和压缩格式。 |
| `MPIPE_MEDIA_END` | 最后一个媒体类型（Media Type）之后的值；该值自身不可用作媒体类型。 |

<a id="ga50d3ad084dceffbff34dbd427fe65580"></a>

### `mpipe_structure_append_value()`

```c
int mpipe_structure_append_value ( struct mpipe_structure * structure, uint8_t field_id, const struct mpipe_value * value )
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

使用调用方拥有的存储（Caller-owned Storage），向能力结构体（Capability Structure）追加字段。

将 value 复制到下一个空闲槽位（Free Slot）；调用者保留自己的副本。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `structure` | 指向要追加字段的结构（Structure）的指针。 |
| `field_id` | 字段标识符（Field Identifier），参见 mpipe_caps_field。该字段必须尚未设置。 |
| `value` | 指向要复制进来的字段值（Field Value）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | field_id 不是字段标识符（Field Identifier）。 |
| `-EEXIST` | 该结构已含有 field_id。 |
| `-ENOSPC` | 该结构已保存 CONFIG_MPIPE_STRUCTURE_MAX_FIELDS 个字段。 |

<a id="ga39287529dd4f6a3ad41d379cc99758fc"></a>

### `mpipe_structure_clear()`

```c
int mpipe_structure_clear ( struct mpipe_structure * structure)
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

清空能力结构体（Capability Structure），移除其携带的所有字段。

结构保留其媒体类型（Media Type）和标志（Flags），因此无需先初始化便可重新填写。

这会使结构变空，与任何对象都没有交集；不会使它变为可与所有对象求交的 ANY。要得到 ANY，请使用 mpipe_structure_init_any。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `structure` | 指向要清空的结构（Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |

<a id="ga2d00586a6073ec63775e6f690c1738dc"></a>

### `mpipe_structure_copy_field()`

```c
int mpipe_structure_copy_field ( const struct mpipe_structure * src, struct mpipe_structure * dst, uint8_t field_id )
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

将字段从一个能力结构体（Capability Structure）复制到另一个。

当 src 不含该字段时，保持 dst 不变并报告 -ENOENT。因此，调用者从另一个能力构造能力时，可尝试传递希望保留的每个字段并忽略该错误码，无需先逐个检查字段是否存在。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` src` | 指向要从中读取字段的结构（Structure）的指针。 |
| `[in,out] dst` | 指向要追加字段的结构（Structure）的指针。 |
| ` field_id` | 字段标识符（Field Identifier），参见 mpipe_caps_field。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOENT` | src 不含该字段（Field）。 |
| `-EINVAL` | field_id 不是字段标识符（Field Identifier）。 |
| `-EEXIST` | dst 已含有该字段（Field）。 |
| `-ENOSPC` | dst 已满（Full）。 |

<a id="ga7876dc8e926adb6bd229882ead04ac54"></a>

### `mpipe_structure_fixate()`

```c
int mpipe_structure_fixate ( const struct mpipe_structure * src, struct mpipe_structure * out )
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

将结构体的能力取值固定化（Fixate），结果写入调用方提供的存储。

将每个字段缩减为单一值（Single Value）：范围缩减为其最小值，已固定的值保持不变。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` src` | 指向要定值（Fixate）的结构的指针。 |
| `[out] out` | 指向结果存储空间（Result Storage）的指针；失败时保持该空间不变。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOENT` | src 为 ANY 或空结构（Empty），没有可供定值的内容。 |
| `-EINVAL` | out 就是 src。 |

<a id="ga20cd6955b0e18fedccc784705a52a34e"></a>

### `mpipe_structure_get_value()`

```c
const struct mpipe_value * mpipe_structure_get_value ( const struct mpipe_structure * structure, uint8_t field_id )
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

获取能力结构体（Capability Structure）中某字段的值。

获取与指定字段 ID（Field ID）关联的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `structure` | 指向包含该字段的结构的指针，可以为 NULL。 |
| `field_id` | 字段标识符（Field Identifier），参见 mpipe_caps_field。 |

**返回（Returns）**：返回：指向字段值（Field Value）的指针；结构不含该字段或 structure 为 NULL 时，返回 NULL。

<a id="ga2b80afbbed288b46f8586f8ddc37cfde"></a>

### `mpipe_structure_init()`

```c
int mpipe_structure_init ( struct mpipe_structure * structure, uint8_t media_type_id )
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

初始化能力结构体（Capability Structure）。

使结构不再设置任何字段（Field）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `structure` | 指向要初始化的结构（Structure）的指针。 |
| `media_type_id` | 结构的媒体类型（media type），参见 `mpipe_media_type`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | media_type_id 不是媒体类型（Media Type）。 |

<a id="ga51192c54b880d8a20c8d3d74c83482bd"></a>

### `mpipe_structure_init_any()`

```c
int mpipe_structure_init_any ( struct mpipe_structure * structure)
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

初始化不施加任何约束的结构体（Structure）。

将其与另一个结构求交（Intersect）会得到另一个结构的副本；对其定值（Fixate）会报告 -ENOENT，因为没有可供选择的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `structure` | 指向要初始化的结构（Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |

<a id="ga80b32dcb5bfd7de40323302c950a76d7"></a>

### `mpipe_structure_init_fields()`

```c
int mpipe_structure_init_fields ( struct mpipe_structure * structure, uint8_t media_type_id, ... )
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

使用媒体类型（Media Type）和字段列表初始化能力结构体（Capability Structure）。

直接在调用者的存储空间中构造能力（Capability）：依次传入 field_id、type、value-args... 三元组，以 MPIPE_CAPS_END 结束；各类型的参数规则与 mpipe_value_set 相同。不会分配内存，因此可在栈上或调用者自己的槽位中描述能力。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `structure` | 指向要初始化的结构（Structure）的指针。 |
| `media_type_id` | 结构的媒体类型（media type），参见 `mpipe_media_type`。 |
| `...` | 字段三元组（Field Triples），以 MPIPE_CAPS_END 结束。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | media_type_id 不是媒体类型，或字段标识符／值类型无效。 |
| `-EEXIST` | 列表中同一个字段（Field）出现了两次。 |
| `-ENOSPC` | 列表中的字段数超过 CONFIG_MPIPE_STRUCTURE_MAX_FIELDS。 |

<a id="ga9e4df6b974dab5d79fb84eff549eb2c1"></a>

### `mpipe_structure_intersect()`

```c
int mpipe_structure_intersect ( const struct mpipe_structure * struct1, const struct mpipe_structure * struct2, struct mpipe_structure * out )
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

对两个结构体求交（Intersect），结果写入调用方提供的存储。

两个结构必须具有相同的媒体类型（Media Type）、至少一个公共字段标识符，且每个公共字段的值都必须存在交集（Intersection）。结果包含两个输入的字段并集（Union）：双方共有的字段保存值的交集，只存在于一方的字段原样复制，因此结果的字段数可能多于任何一个输入。与 ANY 结构求交时，得到另一个结构的副本。

out 按字段逐一写入，因此不能与任何输入是同一个对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` struct1` | 指向第一个结构（Structure）的指针。 |
| ` struct2` | 指向第二个结构（Structure）的指针。 |
| `[out] out` | 指向结果存储空间（Result Storage）的指针；返回 -EINVAL 时保持其不变，其他失败情况下将其清空。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOENT` | 两个结构没有公共字段，或某个公共字段没有公共值。 |
| `-EINVAL` | out 与某个输入指向同一对象，或媒体类型（Media Types）不同。 |
| `-ENOSPC` | 字段并集（Union）无法容纳于 CONFIG_MPIPE_STRUCTURE_MAX_FIELDS 的限制内。 |

<a id="ga7c612e79af6a7c600af5a32b9ee36a7b"></a>

### `mpipe_structure_is_any()`

```c
bool mpipe_structure_is_any ( const struct mpipe_structure * structure)
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

检查结构体是否为 `ANY`，即不施加任何约束（Constraints）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `structure` | 指向要检查的结构（Structure）的指针，可以为 NULL。 |

**返回（Returns）**：返回：结构为 ANY 时为 true，否则或 structure 为 NULL 时为 false。

<a id="gad0e14518c25e189a2f52383af6d56f66"></a>

### `mpipe_structure_is_empty()`

```c
bool mpipe_structure_is_empty ( const struct mpipe_structure * structure)
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

检查能力结构体（Capability Structure）是否不匹配任何内容。

mpipe_structure_is_any 的对应操作。空结构（Empty Structure）不含任何字段，与任何对象都没有交集；ANY 结构则可与所有对象求交。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `structure` | 指向要检查的结构（Structure）的指针，可以为 NULL。 |

**返回（Returns）**：返回：结构为空时为 true，否则或 structure 为 NULL 时为 false。

<a id="ga4c3f662227ccbf343d69e2db0597cb0b"></a>

### `mpipe_structure_is_fixed()`

```c
bool mpipe_structure_is_fixed ( const struct mpipe_structure * structure)
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

检查能力结构体（Capability Structure）是否已固定（Fixed）。

结构至少包含一个字段，且其中每个字段均保存单一值而不是范围时，结构才是固定的（Fixed）。ANY 或空结构始终不是固定的。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `structure` | 指向要检查的结构（Structure）的指针。 |

**返回（Returns）**：返回：结构为固定的（Fixed）时为 true，否则为 false。

<a id="gaf2a980631b57b9199d7f85cb2499a4e1"></a>

### `mpipe_structure_print()`

```c
void mpipe_structure_print ( const struct mpipe_structure * structure)
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

打印能力结构体（Capability Structure）。

输出结构内容以供调试或检查（Debugging or Inspection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `structure` | 指向要打印的结构（Structure）的指针。 |

<a id="ga3c5ec431967b07d00bf2ad85dfbd22b4"></a>

### `mpipe_structure_remove_field()`

```c
int mpipe_structure_remove_field ( struct mpipe_structure * structure, uint8_t field_id )
```

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

移除能力结构体（Capability Structure）中的字段。

从结构中删除具有指定 ID 的字段（Field）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `structure` | 指向包含待移除字段的结构（Structure）的指针。 |
| `field_id` | 字段标识符（Field Identifier），参见 mpipe_caps_field。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOENT` | 该结构不含此字段（Field）。 |


## 10.7\_原页交叉引用（Cross References）

- [mpipe_structure.h](../api_file_display_management_reference/P014_zephyr__mpipe__mpipe_structure.h_文件参考.md)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [能力结构（Capability Structure）](P010_能力结构（Capability Structure）.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mpipe_value](../audio_video_model_reference/P036_mpipe_value_结构体.md)
- [值容器（Value Container）](../api_coap_trusted_topic_reference/P011_值容器（Value Container）.md)
- [MPIPE_TYPE_UINT](../api_coap_trusted_topic_reference/P011_值容器（Value Container）.md#gga8b8b4952140ae9ef7e6e6f20aa99d8a2a7efc72efde7c116938e3e4f3cc15da09)
- [VIDEO_PIX_FMT_RGB565](../api_flash_connection_topic_reference/P011_视频格式（Video Formats）.md#gaf009d0eb7dbdb3bfd8883da03478c1ec)
- [MPIPE_TYPE_UINT_RANGE](../api_coap_trusted_topic_reference/P011_值容器（Value Container）.md#gga8b8b4952140ae9ef7e6e6f20aa99d8a2aef1469edc9c29670a4fc061a84d9eea5)
- [min](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [DIV_ROUND_CLOSEST](../util_reference/P001_通用工具公共接口.md#ga57fc13eb777500b3e22d3ff457cfd0d7)
- [USEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga6a69d6cbdab5f24c2e66959293f210c1)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [CONFIG_MPIPE_STRUCTURE_MAX_FIELDS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_STRUCTURE_MAX_FIELDS)
- [对象（Objects）](../api_security_memory_topic_reference/P008_对象（Objects）.md)
- [mpipe_value_set](../api_coap_trusted_topic_reference/P011_值容器（Value Container）.md#gaf0d9692302ff03a82cd93f7a2d0d3361)

<a id="header-details"></a>
<a id="agroup__mpipe__structure_html_ga80b32dcb5bfd7de40323302c950a76d7"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5a4e15c96bb5c63b61a7588f772fda3820"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5ae38a51f8e24ed04612cbdd979b971611"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5aee7394620f9cbe4286d81bc545379972"></a>
<a id="agroup__mpipe__structure_html_gga0165db3d65894c7832dc455e8014deb5af6df871bfb3ef1eef9dfdd9688258618"></a>
<a id="agroup__mpipe__structure_html_gga4e2bcc7f5152bfde2579bd92618b7b1cae995eeebf430d56b51874dee59dfc229"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2a7efc72efde7c116938e3e4f3cc15da09"></a>
<a id="agroup__mpipe__value_html_gga8b8b4952140ae9ef7e6e6f20aa99d8a2aef1469edc9c29670a4fc061a84d9eea5"></a>
<a id="agroup__video__formats_html_gaf009d0eb7dbdb3bfd8883da03478c1ec"></a>
<a id="astructmpipe__structure_html"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__clock__apis_html_ga6a69d6cbdab5f24c2e66959293f210c1"></a>
<a id="agroup__sys-util_html_ga57fc13eb777500b3e22d3ff457cfd0d7"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="agroup__mpipe__structure_html_gaa967e963ad810470b92727eeb4bc35d2"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga0165db3d65894c7832dc455e8014deb5af6df871bfb3ef1eef9dfdd9688258618"></a>
<a id="gga0165db3d65894c7832dc455e8014deb5aee7394620f9cbe4286d81bc545379972"></a>
<a id="gga0165db3d65894c7832dc455e8014deb5ae38a51f8e24ed04612cbdd979b971611"></a>
<a id="gga0165db3d65894c7832dc455e8014deb5ae3a26714ff3ddc7be070f9ce441e2e12"></a>
<a id="gga0165db3d65894c7832dc455e8014deb5a874c070db9ce6b7fde39fcc46f570190"></a>
<a id="gga0165db3d65894c7832dc455e8014deb5a237a9bcffe2ef8db7f4a3480275b2982"></a>
<a id="gga0165db3d65894c7832dc455e8014deb5aad9b61026d7e0713f36a7ccce47772b6"></a>
<a id="gga0165db3d65894c7832dc455e8014deb5a36e899225b9f8d28b237c9230490d266"></a>
<a id="gga0165db3d65894c7832dc455e8014deb5a4e15c96bb5c63b61a7588f772fda3820"></a>
<a id="gga4e2bcc7f5152bfde2579bd92618b7b1cac04c4bf302809da5ab5c6b8e78f26535"></a>
<a id="gga4e2bcc7f5152bfde2579bd92618b7b1cac073e563bbcd3df377182d86c6034238"></a>
<a id="gga4e2bcc7f5152bfde2579bd92618b7b1cae995eeebf430d56b51874dee59dfc229"></a>
<a id="gga4e2bcc7f5152bfde2579bd92618b7b1ca2e9e6d0b91c736d215cad5006c18e129"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_LIN 控制器（LIN Controller）.md) · [返回大纲](大纲.md)
