---
id: learning.zephyr-docs.api-file-interface-reference.page-33
title: zephyr__mpipe__mpipe_src.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_zephyr\_\_mpipe\_\_mpipe\_src.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__src_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

源（Source）：产生缓冲区的元素。

<a id="details"></a>

```c
#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_pad.h>
```

查看此文件的源码。

源（Source）：产生缓冲区的元素。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 33.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fsrc"></a>

```c
struct mpipe_src
```

相关声明：[mpipe_src](../audio_video_model_reference/P030_mpipe_src_结构体.md)。

基础源元素（Base Source Element）的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 33.2\_枚举（Enumerations）

<a id="r_gae7fdcd5a2bfe2bfb28fa5f430349355e"></a>

```c
enum mpipe_prop_src { MPIPE_PROP_SRC_NUM_BUFS , MPIPE_PROP_SRC_LAST }
```

相关声明：[mpipe_prop_src](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#gae7fdcd5a2bfe2bfb28fa5f430349355e)、[MPIPE_PROP_SRC_NUM_BUFS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ggae7fdcd5a2bfe2bfb28fa5f430349355ea23225c0f2e18cb85fb0f054b5da50d0b)、[MPIPE_PROP_SRC_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ggae7fdcd5a2bfe2bfb28fa5f430349355ea7607aa8978e84a6b6e89fb9a8bf59e8e)。

基础源元素（base source element）的属性。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 33.3\_函数（Functions）

<a id="r_gab96ba2e8ce9cbe6bf2bb27587710bbf0"></a>

```c
int mpipe_src_init (struct mpipe_src *src, uint8_t id)
```

相关声明：[mpipe_src_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#gab96ba2e8ce9cbe6bf2bb27587710bbf0)、[mpipe_src](../audio_video_model_reference/P030_mpipe_src_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化源元素（source element）。

<a id="r_ga53dfd90c1a3942949337f1d222317700"></a>

```c
int mpipe_src_change_state (struct mpipe_element *self, enum mpipe_state_change transition)
```

相关声明：[mpipe_src_change_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ga53dfd90c1a3942949337f1d222317700)、[mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)、[mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)。

基础源元素的状态变更函数（change state function）。

<a id="r_ga867c427e847edb78082607cbe9d5a87b"></a>

```c
int mpipe_src_set_property (struct mpipe_object *obj, uint32_t key, const void *val)
```

相关声明：[mpipe_src_set_property](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ga867c427e847edb78082607cbe9d5a87b)、[mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置源元素的属性。

<a id="r_ga31c1f53bbb8ee29228766cf33f49f924"></a>

```c
int mpipe_src_get_property (struct mpipe_object *obj, uint32_t key, void *val)
```

相关声明：[mpipe_src_get_property](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ga31c1f53bbb8ee29228766cf33f49f924)、[mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取源元素的属性。


## 33.4\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_buffer.h](../api_source_reference/P546_mpipe_buffer.h_源码浏览.md)
- [zephyr/mpipe/mpipe_element.h](../api_source_reference/P550_mpipe_element.h_源码浏览.md)
- [zephyr/mpipe/mpipe_pad.h](../api_source_reference/P554_mpipe_pad.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P559_mpipe_src.h_源码浏览.md)
- [mpipe_src](../audio_video_model_reference/P030_mpipe_src_结构体.md)
- [mpipe_prop_src](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#gae7fdcd5a2bfe2bfb28fa5f430349355e)
- [MPIPE_PROP_SRC_NUM_BUFS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ggae7fdcd5a2bfe2bfb28fa5f430349355ea23225c0f2e18cb85fb0f054b5da50d0b)
- [MPIPE_PROP_SRC_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ggae7fdcd5a2bfe2bfb28fa5f430349355ea7607aa8978e84a6b6e89fb9a8bf59e8e)
- [mpipe_src_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#gab96ba2e8ce9cbe6bf2bb27587710bbf0)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_src_change_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ga53dfd90c1a3942949337f1d222317700)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [mpipe_src_set_property](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ga867c427e847edb78082607cbe9d5a87b)
- [mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mpipe_src_get_property](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ga31c1f53bbb8ee29228766cf33f49f924)

<a id="header-details"></a>

---

[上一章](P032_zephyr__mpipe__base__mpipe_app_sink.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P034_zephyr__mpipe__mpipe_thread.h_文件参考.md)
