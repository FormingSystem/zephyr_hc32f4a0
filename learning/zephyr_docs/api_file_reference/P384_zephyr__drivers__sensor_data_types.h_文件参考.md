---
id: learning.zephyr-docs.api-file-reference.page-384
title: zephyr__drivers__sensor_data_types.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第384章\_zephyr\_\_drivers\_\_sensor\_data\_types.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dsp/types.h>
#include <zephyr/dsp/print_format.h>
#include <inttypes.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 384.1\_数据结构（Data Structures）

<a id="r_sensor_5Fdata_5Fheader"></a>

```c
struct sensor_data_header
```

相关声明：[sensor_data_header](../sensor_navigation_model_reference/P037_sensor_data_header_结构体.md)。

<a id="r_sensor_5Fthree_5Faxis_5Fdata"></a>

```c
struct sensor_three_axis_data
```

相关声明：[sensor_three_axis_data](../sensor_navigation_model_reference/P050_sensor_three_axis_data_结构体.md)。

报告三轴（Three Axes）信息的传感器通道数据。

<a id="r_sensor_5Fthree_5Faxis_5Fdata_3A_3Asensor_5Fthree_5Faxis_5Fsample_5Fdata"></a>

```c
struct sensor_three_axis_data::sensor_three_axis_sample_data
```

相关声明：[sensor_three_axis_data::sensor_three_axis_sample_data](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md)。

<a id="r_sensor_5Fgame_5Frotation_5Fvector_5Fdata"></a>

```c
struct sensor_game_rotation_vector_data
```

相关声明：[sensor_game_rotation_vector_data](../sensor_navigation_model_reference/P041_sensor_game_rotation_vector_data_结构体.md)。

报告游戏旋转向量（Game Rotation Vector）数据的传感器通道数据。

<a id="r_sensor_5Fgame_5Frotation_5Fvector_5Fdata_3A_3Asensor_5Fgame_5Frotation_5Fvector_5Fsample_5Fdata"></a>

```c
struct sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data
```

相关声明：[sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md)。

<a id="r_sensor_5Foccurrence_5Fdata"></a>

```c
struct sensor_occurrence_data
```

相关声明：[sensor_occurrence_data](../sensor_navigation_model_reference/P043_sensor_occurrence_data_结构体.md)。

仅关心事件是否发生的传感器所提供的数据。

<a id="r_sensor_5Foccurrence_5Fdata_3A_3Asensor_5Foccurrence_5Fsample_5Fdata"></a>

```c
struct sensor_occurrence_data::sensor_occurrence_sample_data
```

相关声明：[sensor_occurrence_data::sensor_occurrence_sample_data](../sensor_navigation_model_reference/P044_sensor_occurrence_data__sensor_occurrence_sample_data_结构体.md)。

<a id="r_sensor_5Fq31_5Fdata"></a>

```c
struct sensor_q31_data
```

相关声明：[sensor_q31_data](../sensor_navigation_model_reference/P045_sensor_q31_data_结构体.md)。

报告标量数据（Scalar Data）的传感器通道数据。

<a id="r_sensor_5Fq31_5Fdata_3A_3Asensor_5Fq31_5Fsample_5Fdata"></a>

```c
struct sensor_q31_data::sensor_q31_sample_data
```

相关声明：[sensor_q31_data::sensor_q31_sample_data](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md)。

<a id="r_sensor_5Fbyte_5Fdata"></a>

```c
struct sensor_byte_data
```

相关声明：[sensor_byte_data](../sensor_navigation_model_reference/P033_sensor_byte_data_结构体.md)。

产生单字节数据的传感器所提供的数据。

<a id="r_sensor_5Fbyte_5Fdata_3A_3Asensor_5Fbyte_5Fsample_5Fdata"></a>

```c
struct sensor_byte_data::sensor_byte_sample_data
```

相关声明：[sensor_byte_data::sensor_byte_sample_data](../sensor_navigation_model_reference/P034_sensor_byte_data__sensor_byte_sample_data_结构体.md)。

<a id="r_sensor_5Fuint64_5Fdata"></a>

```c
struct sensor_uint64_data
```

相关声明：[sensor_uint64_data](../sensor_navigation_model_reference/P053_sensor_uint64_data_结构体.md)。

产生类似计数值（Count-Like Value）的传感器所提供的数据。

<a id="r_sensor_5Fuint64_5Fdata_3A_3Asensor_5Fuint64_5Fsample_5Fdata"></a>

```c
struct sensor_uint64_data::sensor_uint64_sample_data
```

相关声明：[sensor_uint64_data::sensor_uint64_sample_data](../sensor_navigation_model_reference/P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 384.2\_宏定义（Macros）

<a id="r_a0c6a78118f9360ed97b1327cf3a3fa9a"></a>

```c
#define PRIsensor_three_axis_data PRIu64 "ns, (%" PRIq(6) ", %" PRIq(6) ", %" PRIq(6) ")"
```

相关声明：[PRIsensor_three_axis_data](#a0c6a78118f9360ed97b1327cf3a3fa9a)、[PRIu64](P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md#ac582131d7a7c8ee57e73180d1714f9d5)、[PRIq](https://docs.zephyrproject.org/latest/doxygen/html/group__math__printing.html#ga08618ad8449ee21f0a57c151541e8ef8)、[PRIq](https://docs.zephyrproject.org/latest/doxygen/html/group__math__printing.html#ga08618ad8449ee21f0a57c151541e8ef8)。

<a id="r_af8c5897a6515c73ec1795b800590a7b4"></a>

```c
#define PRIsensor_three_axis_data_arg(data_, readings_offset_)
```

相关声明：[PRIsensor_three_axis_data_arg](#af8c5897a6515c73ec1795b800590a7b4)。

<a id="r_a25faf87afbedf805a056ae103e98aa75"></a>

```c
#define PRIsensor_game_rotation_vector_data
```

相关声明：[PRIsensor_game_rotation_vector_data](#a25faf87afbedf805a056ae103e98aa75)。

<a id="r_a416ce85d29265cc6b9993a50656b2cb2"></a>

```c
#define PRIsensor_game_rotation_vector_data_arg(data_, readings_offset_)
```

相关声明：[PRIsensor_game_rotation_vector_data_arg](#a416ce85d29265cc6b9993a50656b2cb2)。

<a id="r_a9862e4197bb6146b3e41958f427c9f9a"></a>

```c
#define PRIsensor_occurrence_data PRIu64 "ns"
```

相关声明：[PRIsensor_occurrence_data](#a9862e4197bb6146b3e41958f427c9f9a)、[PRIu64](P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md#ac582131d7a7c8ee57e73180d1714f9d5)。

<a id="r_a3f8a660a28578bbb7baf08fefbca7ac4"></a>

```c
#define PRIsensor_occurrence_data_arg(data_, readings_offset_)
```

相关声明：[PRIsensor_occurrence_data_arg](#a3f8a660a28578bbb7baf08fefbca7ac4)。

<a id="r_a92ae9197089ece9de51db496c9ed5ed6"></a>

```c
#define PRIsensor_q31_data PRIu64 "ns (%" PRIq(6) ")"
```

相关声明：[PRIsensor_q31_data](#a92ae9197089ece9de51db496c9ed5ed6)、[PRIu64](P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md#ac582131d7a7c8ee57e73180d1714f9d5)。

<a id="r_aac3d2a0c462c05c26f7dee0fa0e1ef62"></a>

```c
#define PRIsensor_q31_data_arg(data_, readings_offset_)
```

相关声明：[PRIsensor_q31_data_arg](#aac3d2a0c462c05c26f7dee0fa0e1ef62)。

<a id="r_af73f68f6b94dc1251dfeeb5caf141e94"></a>

```c
#define PRIsensor_byte_data(field_name_)
```

相关声明：[PRIsensor_byte_data](#af73f68f6b94dc1251dfeeb5caf141e94)。

<a id="r_a36cfa50e20150d44c6a254afc149eb5b"></a>

```c
#define PRIsensor_byte_data_arg(data_, readings_offset_, field_name_)
```

相关声明：[PRIsensor_byte_data_arg](#a36cfa50e20150d44c6a254afc149eb5b)。

<a id="r_abc9a284dcd602d240f9bd9b097703634"></a>

```c
#define PRIsensor_uint64_data PRIu64 "ns (%" PRIu64 ")"
```

相关声明：[PRIsensor_uint64_data](#abc9a284dcd602d240f9bd9b097703634)、[PRIu64](P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md#ac582131d7a7c8ee57e73180d1714f9d5)。

<a id="r_a06ef9de1e3821289cd22575410edc80f"></a>

```c
#define PRIsensor_uint64_data_arg(data_, readings_offset_)
```

相关声明：[PRIsensor_uint64_data_arg](#a06ef9de1e3821289cd22575410edc80f)。

## 384.3\_详细说明（Detailed Documentation）

<a id="af73f68f6b94dc1251dfeeb5caf141e94"></a>

### `PRIsensor_byte_data`

```c
#define PRIsensor_byte_data ( field_name_)
```

展开值（Value）：

```c
PRIu64 "ns (" STRINGIFY(field_name_) " = %" PRIu8 ")"
```

<a id="a36cfa50e20150d44c6a254afc149eb5b"></a>

### `PRIsensor_byte_data_arg`

```c
#define PRIsensor_byte_data_arg ( data_, readings_offset_, field_name_ )
```

展开值（Value）：

```c
(data_).header.base_timestamp_ns + (data_).readings[(readings_offset_)].timestamp_delta,   \
        (data_).readings[(readings_offset_)].field_name_
```

<a id="a25faf87afbedf805a056ae103e98aa75"></a>

### `PRIsensor_game_rotation_vector_data`

```c
#define PRIsensor_game_rotation_vector_data
```

展开值（Value）：

```c
PRIu64                                                 \
"ns, (%" PRIq(6) ", %" PRIq(6) ", %" PRIq(6)  ", %" PRIq(6) ")"
```

<a id="a416ce85d29265cc6b9993a50656b2cb2"></a>

### `PRIsensor_game_rotation_vector_data_arg`

```c
#define PRIsensor_game_rotation_vector_data_arg ( data_, readings_offset_ )
```

展开值（Value）：

```c
(data_).header.base_timestamp_ns + (data_).readings[(readings_offset_)].timestamp_delta,   \
        PRIq_arg((data_).readings[(readings_offset_)].x, 6, (data_).shift),                \
        PRIq_arg((data_).readings[(readings_offset_)].y, 6, (data_).shift),                \
        PRIq_arg((data_).readings[(readings_offset_)].z, 6, (data_).shift),                \
        PRIq_arg((data_).readings[(readings_offset_)].w, 6, (data_).shift)
```

<a id="a9862e4197bb6146b3e41958f427c9f9a"></a>

### `PRIsensor_occurrence_data`

```c
#define PRIsensor_occurrence_data PRIu64 "ns"
```

<a id="a3f8a660a28578bbb7baf08fefbca7ac4"></a>

### `PRIsensor_occurrence_data_arg`

```c
#define PRIsensor_occurrence_data_arg ( data_, readings_offset_ )
```

展开值（Value）：

```c
(data_).header.base_timestamp_ns + (data_).readings[(readings_offset_)].timestamp_delta
```

<a id="a92ae9197089ece9de51db496c9ed5ed6"></a>

### `PRIsensor_q31_data`

```c
#define PRIsensor_q31_data PRIu64 "ns (%" PRIq(6) ")"
```

<a id="aac3d2a0c462c05c26f7dee0fa0e1ef62"></a>

### `PRIsensor_q31_data_arg`

```c
#define PRIsensor_q31_data_arg ( data_, readings_offset_ )
```

展开值（Value）：

```c
(data_).header.base_timestamp_ns + (data_).readings[(readings_offset_)].timestamp_delta,   \
        PRIq_arg((data_).readings[(readings_offset_)].value, 6, (data_).shift)
```

<a id="a0c6a78118f9360ed97b1327cf3a3fa9a"></a>

### `PRIsensor_three_axis_data`

```c
#define PRIsensor_three_axis_data PRIu64 "ns, (%" PRIq(6) ", %" PRIq(6) ", %" PRIq(6) ")"
```

<a id="af8c5897a6515c73ec1795b800590a7b4"></a>

### `PRIsensor_three_axis_data_arg`

```c
#define PRIsensor_three_axis_data_arg ( data_, readings_offset_ )
```

展开值（Value）：

```c
(data_).header.base_timestamp_ns + (data_).readings[(readings_offset_)].timestamp_delta,   \
        PRIq_arg((data_).readings[(readings_offset_)].x, 6, (data_).shift),                \
        PRIq_arg((data_).readings[(readings_offset_)].y, 6, (data_).shift),                \
        PRIq_arg((data_).readings[(readings_offset_)].z, 6, (data_).shift)
```

<a id="abc9a284dcd602d240f9bd9b097703634"></a>

### `PRIsensor_uint64_data`

```c
#define PRIsensor_uint64_data PRIu64 "ns (%" PRIu64 ")"
```

<a id="a06ef9de1e3821289cd22575410edc80f"></a>

### `PRIsensor_uint64_data_arg`

```c
#define PRIsensor_uint64_data_arg ( data_, readings_offset_ )
```

展开值（Value）：

```c
(data_).header.base_timestamp_ns + (data_).readings[(readings_offset_)].timestamp_delta,   \
        (data_).readings[(readings_offset_)].value
```


## 384.4\_原页交叉引用（Cross References）

- [zephyr/dsp/types.h](../api_source_reference/P364_types.h_源码浏览.md)
- [zephyr/dsp/print_format.h](../api_source_reference/P670_print_format.h_源码浏览.md)
- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P768_sensor_data_types.h_源码浏览.md)
- [sensor_data_header](../sensor_navigation_model_reference/P037_sensor_data_header_结构体.md)
- [sensor_three_axis_data](../sensor_navigation_model_reference/P050_sensor_three_axis_data_结构体.md)
- [sensor_three_axis_data::sensor_three_axis_sample_data](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md)
- [sensor_game_rotation_vector_data](../sensor_navigation_model_reference/P041_sensor_game_rotation_vector_data_结构体.md)
- [sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md)
- [sensor_occurrence_data](../sensor_navigation_model_reference/P043_sensor_occurrence_data_结构体.md)
- [sensor_occurrence_data::sensor_occurrence_sample_data](../sensor_navigation_model_reference/P044_sensor_occurrence_data__sensor_occurrence_sample_data_结构体.md)
- [sensor_q31_data](../sensor_navigation_model_reference/P045_sensor_q31_data_结构体.md)
- [sensor_q31_data::sensor_q31_sample_data](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md)
- [sensor_byte_data](../sensor_navigation_model_reference/P033_sensor_byte_data_结构体.md)
- [sensor_byte_data::sensor_byte_sample_data](../sensor_navigation_model_reference/P034_sensor_byte_data__sensor_byte_sample_data_结构体.md)
- [sensor_uint64_data](../sensor_navigation_model_reference/P053_sensor_uint64_data_结构体.md)
- [sensor_uint64_data::sensor_uint64_sample_data](../sensor_navigation_model_reference/P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md)
- [PRIu64](P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md#ac582131d7a7c8ee57e73180d1714f9d5)
- [PRIq](https://docs.zephyrproject.org/latest/doxygen/html/group__math__printing.html#ga08618ad8449ee21f0a57c151541e8ef8)
- [PRIu8](P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md#a8673208d2d48018fcce020ef59f8ec4f)
- [PRIq_arg](https://docs.zephyrproject.org/latest/doxygen/html/group__math__printing.html#gad0393d2bb183784a9c09f2c05d7987f9)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="ainttypes_8h_html_a8673208d2d48018fcce020ef59f8ec4f"></a>
<a id="ainttypes_8h_html_ac582131d7a7c8ee57e73180d1714f9d5"></a>
<a id="agroup__math__printing_html_ga08618ad8449ee21f0a57c151541e8ef8"></a>
<a id="agroup__math__printing_html_gad0393d2bb183784a9c09f2c05d7987f9"></a>

---

[上一章](P383_zephyr__drivers__sensor_attribute_types.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P385_zephyr__dt-bindings__dma__sf32lb-dma-config.h_文件参考.md)
