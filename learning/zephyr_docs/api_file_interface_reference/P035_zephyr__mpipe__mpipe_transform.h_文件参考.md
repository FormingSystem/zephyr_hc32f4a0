---
id: learning.zephyr-docs.api-file-interface-reference.page-35
title: zephyr__mpipe__mpipe_transform.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_zephyr\_\_mpipe\_\_mpipe\_transform.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

变换（Transform）：将输入缓冲区转换为输出缓冲区的元素。

<a id="details"></a>

```c
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_pad.h>
#include <zephyr/mpipe/mpipe_structure.h>
```

查看此文件的源码。

变换（Transform）：将输入缓冲区转换为输出缓冲区的元素。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 35.1\_数据结构（Data Structures）

<a id="r_mpipe_5Ftransform"></a>

```c
struct mpipe_transform
```

相关声明：[mpipe_transform](../audio_video_model_reference/P034_mpipe_transform_结构体.md)。

变换元素（Transform Element）的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 35.2\_枚举（Enumerations）

<a id="r_ga1710f61119b47e057d957b56ab690dfe"></a>

```c
enum mpipe_prop_transform { MPIPE_PROP_TRANSFORM_LAST }
```

相关声明：[mpipe_prop_transform](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga1710f61119b47e057d957b56ab690dfe)、[MPIPE_PROP_TRANSFORM_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga1710f61119b47e057d957b56ab690dfeacfa117280b8cda0493183451f21570c7)。

变换元素（transform element）的属性。

<a id="r_ga53de93e6bf6ca6cc2e4a7be14ff76652"></a>

```c
enum mpipe_transform_mode { MPIPE_TRANSFORM_MODE_PASSTHROUGH = 0 , MPIPE_TRANSFORM_MODE_INPLACE = 1 , MPIPE_TRANSFORM_MODE_NORMAL = 2 }
```

相关声明：[mpipe_transform_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga53de93e6bf6ca6cc2e4a7be14ff76652)、[MPIPE_TRANSFORM_MODE_PASSTHROUGH](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga53de93e6bf6ca6cc2e4a7be14ff76652aca06f29cd96b7d8e8de6424f4a7d4d7b)、[MPIPE_TRANSFORM_MODE_INPLACE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga53de93e6bf6ca6cc2e4a7be14ff76652a0472bf057ab05107d7dfd38c996dedea)、[MPIPE_TRANSFORM_MODE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga53de93e6bf6ca6cc2e4a7be14ff76652a204d168b2efe7c3779194eab1ff2ee0c)。

变换元素的运行模式（operating modes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 35.3\_函数（Functions）

<a id="r_gaecc6d5f2c8fb0d033977ecb1d5edeb5a"></a>

```c
int mpipe_transform_init (struct mpipe_transform *transform, uint8_t id)
```

相关声明：[mpipe_transform_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gaecc6d5f2c8fb0d033977ecb1d5edeb5a)、[mpipe_transform](../audio_video_model_reference/P034_mpipe_transform_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化变换元素。

<a id="r_ga24c1be1b0231360f5f192d142975efd9"></a>

```c
int mpipe_transform_set_caps (struct mpipe_transform *transform, enum mpipe_pad_direction direction, const struct mpipe_structure *caps)
```

相关声明：[mpipe_transform_set_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga24c1be1b0231360f5f192d142975efd9)、[mpipe_transform](../audio_video_model_reference/P034_mpipe_transform_结构体.md)、[mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

在变换元素的连接端（pad）上设置一项能力（capability）。

<a id="r_ga4a80bc07f3cab770a42bf73a510e1aad"></a>

```c
int mpipe_transform_change_state (struct mpipe_element *self, enum mpipe_state_change transition)
```

相关声明：[mpipe_transform_change_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga4a80bc07f3cab770a42bf73a510e1aad)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)。

基础变换元素（base transform element）的状态变更函数。


## 35.4\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_element.h](../api_source_reference/P550_mpipe_element.h_源码浏览.md)
- [zephyr/mpipe/mpipe_pad.h](../api_source_reference/P554_mpipe_pad.h_源码浏览.md)
- [zephyr/mpipe/mpipe_structure.h](../api_source_reference/P560_mpipe_structure.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P562_mpipe_transform.h_源码浏览.md)
- [mpipe_transform](../audio_video_model_reference/P034_mpipe_transform_结构体.md)
- [mpipe_prop_transform](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga1710f61119b47e057d957b56ab690dfe)
- [MPIPE_PROP_TRANSFORM_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga1710f61119b47e057d957b56ab690dfeacfa117280b8cda0493183451f21570c7)
- [mpipe_transform_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga53de93e6bf6ca6cc2e4a7be14ff76652)
- [MPIPE_TRANSFORM_MODE_PASSTHROUGH](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga53de93e6bf6ca6cc2e4a7be14ff76652aca06f29cd96b7d8e8de6424f4a7d4d7b)
- [MPIPE_TRANSFORM_MODE_INPLACE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga53de93e6bf6ca6cc2e4a7be14ff76652a0472bf057ab05107d7dfd38c996dedea)
- [MPIPE_TRANSFORM_MODE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga53de93e6bf6ca6cc2e4a7be14ff76652a204d168b2efe7c3779194eab1ff2ee0c)
- [mpipe_transform_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gaecc6d5f2c8fb0d033977ecb1d5edeb5a)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_transform_set_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga24c1be1b0231360f5f192d142975efd9)
- [mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [mpipe_transform_change_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga4a80bc07f3cab770a42bf73a510e1aad)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)

<a id="header-details"></a>

---

[上一章](P034_zephyr__mpipe__mpipe_thread.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P036_zephyr__drivers__mfd__nct38xx.h_文件参考.md)
