---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-26
title: zephyr__mpipe__mpipe_pad.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_zephyr\_\_mpipe\_\_mpipe\_pad.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

端口（Pad）：两个元素连接的位置。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/util.h>
#include <zephyr/kernel.h>
#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_structure.h>
#include <zephyr/mpipe/mpipe_object.h>
```

查看此文件的源码。

端口（Pad）：两个元素连接的位置。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 26.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fpad"></a>

```c
struct mpipe_pad
```

相关声明：[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)。

端口（Pad）结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 26.2\_枚举（Enumerations）

<a id="r_ga9de49691e139241133f231188671d4f2"></a>

```c
enum mpipe_pad_direction { MPIPE_PAD_UNKNOWN , MPIPE_PAD_SRC , MPIPE_PAD_SINK }
```

相关声明：[mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)、[MPIPE_PAD_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga9de49691e139241133f231188671d4f2ac78e4d56c5e4ef0c2fb540b96e768485)、[MPIPE_PAD_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga9de49691e139241133f231188671d4f2a2bec7e8ba42eb1bd310f64ac8b226eb1)、[MPIPE_PAD_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga9de49691e139241133f231188671d4f2a968c6b4c1354249e3c2edb90c2a9c6a4)。

衬垫方向（Pad Direction）。

<a id="r_ga6103c9bbb48a5b03a3805a561c19b9f5"></a>

```c
enum mpipe_pad_mode { MPIPE_PAD_MODE_NONE , MPIPE_PAD_MODE_PUSH , MPIPE_PAD_MODE_PULL }
```

相关声明：[mpipe_pad_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6103c9bbb48a5b03a3805a561c19b9f5)、[MPIPE_PAD_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga6103c9bbb48a5b03a3805a561c19b9f5ab733479f2e0ee43179b7c8f4a8e6fdbe)、[MPIPE_PAD_MODE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga6103c9bbb48a5b03a3805a561c19b9f5a66654014110056bdf7bf072ee47f6e24)、[MPIPE_PAD_MODE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga6103c9bbb48a5b03a3805a561c19b9f5a9c3c348be8f4820abc7290a6f3c2680b)。

衬垫运行模式（Pad Operating Mode）。

<a id="r_gae260b9597d59469fdd89cc9604d33646"></a>

```c
enum mpipe_pad_presence { MPIPE_PAD_ALWAYS , MPIPE_PAD_SOMETIMES , MPIPE_PAD_REQUEST }
```

相关声明：[mpipe_pad_presence](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gae260b9597d59469fdd89cc9604d33646)、[MPIPE_PAD_ALWAYS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ggae260b9597d59469fdd89cc9604d33646a94500ceecec6513ffec8589740432eb1)、[MPIPE_PAD_SOMETIMES](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ggae260b9597d59469fdd89cc9604d33646a9c1618c29a6b702aa7f88cb45f66b8e3)、[MPIPE_PAD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ggae260b9597d59469fdd89cc9604d33646ae1d7881588a59e12a13b68465f31ebdb)。

衬垫的存在性（Pad Presence）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 26.3\_函数（Functions）

<a id="r_ga6b05aca1580f37d8b65d8534b5ab9fa3"></a>

```c
int mpipe_pad_enum_caps (struct mpipe_pad *pad, uint32_t index, const struct mpipe_structure *filter, struct mpipe_structure *out)
```

相关声明：[mpipe_pad_enum_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6b05aca1580f37d8b65d8534b5ab9fa3)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

生成衬垫（Pad）支持的一项能力（Capability）。

<a id="r_ga6d217c7c0cf12e1f309839ccd3b30eb7"></a>

```c
int mpipe_pad_enum_first (struct mpipe_pad *pad, const struct mpipe_structure *filter, struct mpipe_structure *out)
```

相关声明：[mpipe_pad_enum_first](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6d217c7c0cf12e1f309839ccd3b30eb7)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

生成衬垫支持且被过滤器（Filter）接受的第一项能力（Capability）。

<a id="r_ga28ede4a47055d4a98aac21a15973714b"></a>

```c
int mpipe_pad_answer_caps_query (struct mpipe_pad *pad, struct mpipe_dispatch *query)
```

相关声明：[mpipe_pad_answer_caps_query](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga28ede4a47055d4a98aac21a15973714b)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)。

使用过滤器（Filter）接受的第一项能力回答能力查询（Caps Query）。

<a id="r_ga3a02138067490e72f3b36d3cfb3639bb"></a>

```c
int mpipe_pad_enum_filter (const struct mpipe_structure *candidate, const struct mpipe_structure *filter, struct mpipe_structure *out)
```

相关声明：[mpipe_pad_enum_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga3a02138067490e72f3b36d3cfb3639bb)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

通过枚举过滤器（Enumeration Filter）收窄一项已枚举能力（Enumerated Capability）。

<a id="r_ga6daef8b8fb359e5a8edada810d5136bc"></a>

```c
void mpipe_pad_init (struct mpipe_pad *pad, uint8_t id, enum mpipe_pad_direction direction, enum mpipe_pad_presence presence)
```

相关声明：[mpipe_pad_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6daef8b8fb359e5a8edada810d5136bc)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)、[mpipe_pad_presence](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gae260b9597d59469fdd89cc9604d33646)。

初始化衬垫（Pad）。

<a id="r_ga1249052f4192c3cc5c052c59fc120a82"></a>

```c
int mpipe_pad_set_caps (struct mpipe_pad *pad, const struct mpipe_structure *caps)
```

相关声明：[mpipe_pad_set_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga1249052f4192c3cc5c052c59fc120a82)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

设置衬垫能力（Pad Capability）。

<a id="r_gaf1210118ce75177f5950074acb5bfd4f"></a>

```c
void mpipe_pad_link (struct mpipe_pad *src_pad, struct mpipe_pad *sink_pad)
```

相关声明：[mpipe_pad_link](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gaf1210118ce75177f5950074acb5bfd4f)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)。

连接两个衬垫（Link Pads）。

<a id="r_ga867dff16bf63d21cab505f2b1f282ebc"></a>

```c
int mpipe_pad_send_event (struct mpipe_pad *pad, struct mpipe_dispatch *event)
```

相关声明：[mpipe_pad_send_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga867dff16bf63d21cab505f2b1f282ebc)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)。

向衬垫（Pad）发送事件（Event）。

<a id="r_ga1bc13e3d72c8daed41344d727766e830"></a>

```c
int mpipe_pad_send_event_default (struct mpipe_pad *pad, struct mpipe_dispatch *event)
```

相关声明：[mpipe_pad_send_event_default](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga1bc13e3d72c8daed41344d727766e830)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)。

衬垫（Pad）的默认事件处理程序（Default Event Handler）。

<a id="r_ga35b334800669dbe25a46c71d75afd775"></a>

```c
int mpipe_pad_query (struct mpipe_pad *pad, struct mpipe_dispatch *query)
```

相关声明：[mpipe_pad_query](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga35b334800669dbe25a46c71d75afd775)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)。

向衬垫（Pad）发送查询（Query）。


## 26.4\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/mpipe/mpipe_buffer.h](../api_source_reference/P546_mpipe_buffer.h_源码浏览.md)
- [zephyr/mpipe/mpipe_structure.h](../api_source_reference/P560_mpipe_structure.h_源码浏览.md)
- [zephyr/mpipe/mpipe_object.h](../api_source_reference/P553_mpipe_object.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P554_mpipe_pad.h_源码浏览.md)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)
- [MPIPE_PAD_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga9de49691e139241133f231188671d4f2ac78e4d56c5e4ef0c2fb540b96e768485)
- [MPIPE_PAD_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga9de49691e139241133f231188671d4f2a2bec7e8ba42eb1bd310f64ac8b226eb1)
- [MPIPE_PAD_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga9de49691e139241133f231188671d4f2a968c6b4c1354249e3c2edb90c2a9c6a4)
- [mpipe_pad_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6103c9bbb48a5b03a3805a561c19b9f5)
- [MPIPE_PAD_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga6103c9bbb48a5b03a3805a561c19b9f5ab733479f2e0ee43179b7c8f4a8e6fdbe)
- [MPIPE_PAD_MODE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga6103c9bbb48a5b03a3805a561c19b9f5a66654014110056bdf7bf072ee47f6e24)
- [MPIPE_PAD_MODE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gga6103c9bbb48a5b03a3805a561c19b9f5a9c3c348be8f4820abc7290a6f3c2680b)
- [连接端口（Pad）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html)
- [mpipe_pad_presence](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gae260b9597d59469fdd89cc9604d33646)
- [MPIPE_PAD_ALWAYS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ggae260b9597d59469fdd89cc9604d33646a94500ceecec6513ffec8589740432eb1)
- [MPIPE_PAD_SOMETIMES](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ggae260b9597d59469fdd89cc9604d33646a9c1618c29a6b702aa7f88cb45f66b8e3)
- [MPIPE_PAD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ggae260b9597d59469fdd89cc9604d33646ae1d7881588a59e12a13b68465f31ebdb)
- [mpipe_pad_enum_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6b05aca1580f37d8b65d8534b5ab9fa3)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [mpipe_pad_enum_first](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6d217c7c0cf12e1f309839ccd3b30eb7)
- [mpipe_pad_answer_caps_query](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga28ede4a47055d4a98aac21a15973714b)
- [mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)
- [mpipe_pad_enum_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga3a02138067490e72f3b36d3cfb3639bb)
- [mpipe_pad_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6daef8b8fb359e5a8edada810d5136bc)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_pad_set_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga1249052f4192c3cc5c052c59fc120a82)
- [mpipe_pad_link](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gaf1210118ce75177f5950074acb5bfd4f)
- [mpipe_pad_send_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga867dff16bf63d21cab505f2b1f282ebc)
- [mpipe_pad_send_event_default](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga1bc13e3d72c8daed41344d727766e830)
- [mpipe_pad_query](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga35b334800669dbe25a46c71d75afd775)

<a id="header-details"></a>

---

[上一章](P025_zephyr__mpipe__mpipe_element.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P027_zephyr__dt-bindings__sensor__qdec_stm32.h_文件参考.md)
