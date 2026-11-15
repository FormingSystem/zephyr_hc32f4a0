---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-25
title: zephyr__mpipe__mpipe_element.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_mpipe\_\_mpipe\_element.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

元素（Element）：构成流水线的基本单元。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/sys/dlist.h>
#include <zephyr/sys/util.h>
#include <zephyr/mpipe/mpipe_object.h>
```

查看此文件的源码。

元素（Element）：构成流水线的基本单元。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 25.1\_数据结构（Data Structures）

<a id="r_mpipe_5Felement"></a>

```c
struct mpipe_element
```

相关声明：[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)。

元素基类（Element Base Class）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 25.2\_宏定义（Macros）

<a id="r_ga0d287bf9926308d665bab9038e5c73aa"></a>

```c
#define MPIPE_STATE_GET_NEXT(cur, target)
```

相关声明：[MPIPE_STATE_GET_NEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga0d287bf9926308d665bab9038e5c73aa)。

计算下一状态（Next State）。

<a id="r_gad20f56bd84d7767a2e5f854be7d34116"></a>

```c
#define MPIPE_STATE_TRANSITION(cur, next)
```

相关声明：[MPIPE_STATE_TRANSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gad20f56bd84d7767a2e5f854be7d34116)。

创建状态转换值（State Transition Value）。

<a id="r_ga4bc586dbe57b4465b1b1ad554d035fd2"></a>

```c
#define MPIPE_STATE_TRANSITION_CURRENT(trans)
```

相关声明：[MPIPE_STATE_TRANSITION_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga4bc586dbe57b4465b1b1ad554d035fd2)。

从状态转换（State Transition）中提取当前状态（Current State）。

<a id="r_ga2d6a4dd0a1cdf90dcc392ac9ae2cc764"></a>

```c
#define MPIPE_STATE_TRANSITION_NEXT(trans)
```

相关声明：[MPIPE_STATE_TRANSITION_NEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga2d6a4dd0a1cdf90dcc392ac9ae2cc764)。

从状态转换（State Transition）中提取下一状态（Next State）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 25.3\_枚举（Enumerations）

<a id="r_ga7ead9fea0963f40d4db49c8008cb3366"></a>

```c
enum mpipe_state { MPIPE_STATE_READY = 0 , MPIPE_STATE_PAUSED = 1 , MPIPE_STATE_PLAYING = 2 }
```

相关声明：[mpipe_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga7ead9fea0963f40d4db49c8008cb3366)、[MPIPE_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga7ead9fea0963f40d4db49c8008cb3366aade49a9842b3fa929d20c3c7c5fbba24)、[MPIPE_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga7ead9fea0963f40d4db49c8008cb3366a70edf5e9b37a699f5b2ca0f6a41b5544)、[MPIPE_STATE_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga7ead9fea0963f40d4db49c8008cb3366a565f1ca71525e156ade5a80b6dd28922)。

元素状态（Element States）。

<a id="r_ga219cea77697cda52503e88096029c287"></a>

```c
enum mpipe_state_change { MPIPE_STATE_CHANGE_READY_TO_PAUSED , MPIPE_STATE_CHANGE_PAUSED_TO_PLAYING , MPIPE_STATE_CHANGE_PLAYING_TO_PAUSED , MPIPE_STATE_CHANGE_PAUSED_TO_READY }
```

相关声明：[mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)、[MPIPE_STATE_CHANGE_READY_TO_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga219cea77697cda52503e88096029c287acf0326519ae7130fc6416cd6ba45a129)、[MPIPE_STATE_CHANGE_PAUSED_TO_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga219cea77697cda52503e88096029c287afe96cd696feb697f5fbeecf7be3c1492)、[MPIPE_STATE_CHANGE_PLAYING_TO_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga219cea77697cda52503e88096029c287a8fb4ec66001f447bca5dbfd32bf91a92)、[MPIPE_STATE_CHANGE_PAUSED_TO_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga219cea77697cda52503e88096029c287a0fe1848bff2d05ba1e9b7601537248a1)。

两个相邻状态之间的转换（Transition）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.4\_函数（Functions）

<a id="r_gaa571f5b8e78dafb71e2175f0df3c496a"></a>

```c
int mpipe_element_init (struct mpipe_element *self, uint8_t id)
```

相关声明：[mpipe_element_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gaa571f5b8e78dafb71e2175f0df3c496a)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化元素（Element）。

<a id="r_ga89e9dc38e2cff13b63e70177732773e9"></a>

```c
static void mpipe_element_set_name (struct mpipe_element *self, const char *name)
```

相关声明：[mpipe_element_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga89e9dc38e2cff13b63e70177732773e9)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)。

为元素命名，以便在流水线转储（Pipeline Dump）中使用。

<a id="r_ga4b7bea3b1e0995ceaaebc3f8ec4e0530"></a>

```c
void mpipe_element_reset_pad_caps (struct mpipe_element *element)
```

相关声明：[mpipe_element_reset_pad_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga4b7bea3b1e0995ceaaebc3f8ec4e0530)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)。

将元素的每个衬垫（Pad）重置为不施加任何约束（Constraints）的状态。

<a id="r_gaaadee8e87da20d947d8fc90e4533ef8b"></a>

```c
void mpipe_element_add_pad (struct mpipe_element *element, struct mpipe_pad *pad)
```

相关声明：[mpipe_element_add_pad](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gaaadee8e87da20d947d8fc90e4533ef8b)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)。

将衬垫（Pad）附加到元素（Element）。

<a id="r_ga5b478364e7baec25fef972ab3fee0807"></a>

```c
int mpipe_element_link (struct mpipe_element *element_1, struct mpipe_element *element_2,...)
```

相关声明：[mpipe_element_link](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga5b478364e7baec25fef972ab3fee0807)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)。

连接多个元素（Link Elements）。

<a id="r_gafb59f995c7a2bd799316d187ec252632"></a>

```c
int mpipe_element_set_state (struct mpipe_element *element, enum mpipe_state state)
```

相关声明：[mpipe_element_set_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gafb59f995c7a2bd799316d187ec252632)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga7ead9fea0963f40d4db49c8008cb3366)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置元素状态（Element State）。

<a id="r_gadd1c172f5ce2f4eb6fffeb40ecc931b6"></a>

```c
struct zbus_channel * mpipe_element_get_bus_chan (struct mpipe_element *element)
```

相关声明：[zbus_channel](../intercore_reference/P206_zbus通道结构.md)、[mpipe_element_get_bus_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gadd1c172f5ce2f4eb6fffeb40ecc931b6)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)。

获取元素的总线通道（Bus Channel）。


## 25.5\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/dlist.h](../dlist_reference/P003_双向链表头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/mpipe/mpipe_object.h](../api_source_reference/P553_mpipe_object.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P550_mpipe_element.h_源码浏览.md)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [MPIPE_STATE_GET_NEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga0d287bf9926308d665bab9038e5c73aa)
- [MPIPE_STATE_TRANSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gad20f56bd84d7767a2e5f854be7d34116)
- [MPIPE_STATE_TRANSITION_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga4bc586dbe57b4465b1b1ad554d035fd2)
- [MPIPE_STATE_TRANSITION_NEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga2d6a4dd0a1cdf90dcc392ac9ae2cc764)
- [mpipe_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga7ead9fea0963f40d4db49c8008cb3366)
- [MPIPE_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga7ead9fea0963f40d4db49c8008cb3366aade49a9842b3fa929d20c3c7c5fbba24)
- [MPIPE_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga7ead9fea0963f40d4db49c8008cb3366a70edf5e9b37a699f5b2ca0f6a41b5544)
- [MPIPE_STATE_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga7ead9fea0963f40d4db49c8008cb3366a565f1ca71525e156ade5a80b6dd28922)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [MPIPE_STATE_CHANGE_READY_TO_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga219cea77697cda52503e88096029c287acf0326519ae7130fc6416cd6ba45a129)
- [MPIPE_STATE_CHANGE_PAUSED_TO_PLAYING](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga219cea77697cda52503e88096029c287afe96cd696feb697f5fbeecf7be3c1492)
- [MPIPE_STATE_CHANGE_PLAYING_TO_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga219cea77697cda52503e88096029c287a8fb4ec66001f447bca5dbfd32bf91a92)
- [MPIPE_STATE_CHANGE_PAUSED_TO_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gga219cea77697cda52503e88096029c287a0fe1848bff2d05ba1e9b7601537248a1)
- [mpipe_element_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gaa571f5b8e78dafb71e2175f0df3c496a)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_element_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga89e9dc38e2cff13b63e70177732773e9)
- [mpipe_element_reset_pad_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga4b7bea3b1e0995ceaaebc3f8ec4e0530)
- [mpipe_element_add_pad](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gaaadee8e87da20d947d8fc90e4533ef8b)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [mpipe_element_link](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga5b478364e7baec25fef972ab3fee0807)
- [mpipe_element_set_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gafb59f995c7a2bd799316d187ec252632)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [zbus_channel](../intercore_reference/P206_zbus通道结构.md)
- [mpipe_element_get_bus_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gadd1c172f5ce2f4eb6fffeb40ecc931b6)

<a id="header-details"></a>

---

[上一章](P024_zephyr__psa__key_ids.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__mpipe__mpipe_pad.h_文件参考.md)
