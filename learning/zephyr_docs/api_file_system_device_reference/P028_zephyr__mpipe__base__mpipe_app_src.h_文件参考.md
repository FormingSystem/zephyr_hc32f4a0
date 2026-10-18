---
id: learning.zephyr-docs.api-file-system-device-reference.page-28
title: zephyr__mpipe__base__mpipe_app_src.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__src_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_mpipe\_\_base\_\_mpipe\_app\_src.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__src_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

应用源元素（Application Source Element）。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_src.h>
#include <zephyr/mpipe/mpipe_structure.h>
```

查看此文件的源码。

应用源元素（Application source element）。`app_src` 元素允许应用程序向管线（pipeline）注入数据：应用程序按自己的节奏推送有效载荷（payloads），并显式声明流结束。管线线程以与其他源相同的方式消费这些缓冲区。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 28.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fapp_5Fsrc"></a>

```c
struct mpipe_app_src
```

相关声明：[mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)。

应用源元素（Application Source Element）的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 28.2\_枚举（Enumerations）

<a id="r_gaee1930383745bc07d8734dfeac317f89"></a>

```c
enum { MPIPE_PROP_BASE_APP_SRC_CAPS = MPIPE_PROP_SRC_LAST }
```

相关声明：[MPIPE_PROP_BASE_APP_SRC_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ggaee1930383745bc07d8734dfeac317f89ab1e24989a31b21a248e4ff49bb04bcef)。

应用源（application source）的属性标识符。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 28.3\_函数（Functions）

<a id="r_ga36d2f33b184a21b4bc81c3851da09231"></a>

```c
int mpipe_app_src_init (struct mpipe_app_src *app_src, uint8_t id)
```

相关声明：[mpipe_app_src_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga36d2f33b184a21b4bc81c3851da09231)、[mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化应用源元素。

<a id="r_ga38b11181f864200dc78a742e1627367a"></a>

```c
int mpipe_app_src_alloc (struct mpipe_app_src *app_src, uint32_t size, k_timeout_t timeout, struct net_buf **buf)
```

相关声明：[mpipe_app_src_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga38b11181f864200dc78a742e1627367a)、[mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从元素的缓冲池获取一个缓冲区，以便就地填充。

<a id="r_ga6b367eef2ce6e91ca66ceb9040a71d1f"></a>

```c
int mpipe_app_src_push_buf (struct mpipe_app_src *app_src, struct net_buf *buf, uint32_t size, k_timeout_t timeout)
```

相关声明：[mpipe_app_src_push_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga6b367eef2ce6e91ca66ceb9040a71d1f)、[mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

将已填充的缓冲区加入管线队列。

<a id="r_ga3b30d456b8b1812f98a753012618906b"></a>

```c
int mpipe_app_src_push (struct mpipe_app_src *app_src, const void *data, uint32_t size, k_timeout_t timeout)
```

相关声明：[mpipe_app_src_push](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga3b30d456b8b1812f98a753012618906b)、[mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

通过复制方式向管线推送一份有效载荷（payload）。

<a id="r_ga7e0d167ba0017e1952b455c9e269ca37"></a>

```c
int mpipe_app_src_eos (struct mpipe_app_src *app_src, k_timeout_t timeout)
```

相关声明：[mpipe_app_src_eos](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga7e0d167ba0017e1952b455c9e269ca37)、[mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

声明流结束（end of stream）。


## 28.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/mpipe/mpipe_buffer.h](../api_source_reference/P546_mpipe_buffer.h_源码浏览.md)
- [zephyr/mpipe/mpipe_element.h](../api_source_reference/P550_mpipe_element.h_源码浏览.md)
- [zephyr/mpipe/mpipe_src.h](../api_source_reference/P559_mpipe_src.h_源码浏览.md)
- [zephyr/mpipe/mpipe_structure.h](../api_source_reference/P560_mpipe_structure.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P544_mpipe_app_src.h_源码浏览.md)
- [mpipe_app_src](../audio_video_model_reference/P014_mpipe_app_src_结构体.md)
- [MPIPE_PROP_BASE_APP_SRC_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ggaee1930383745bc07d8734dfeac317f89ab1e24989a31b21a248e4ff49bb04bcef)
- [mpipe_app_src_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga36d2f33b184a21b4bc81c3851da09231)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_app_src_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga38b11181f864200dc78a742e1627367a)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [mpipe_app_src_push_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga6b367eef2ce6e91ca66ceb9040a71d1f)
- [mpipe_app_src_push](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga3b30d456b8b1812f98a753012618906b)
- [mpipe_app_src_eos](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__src.html#ga7e0d167ba0017e1952b455c9e269ca37)

<a id="header-details"></a>

---

[上一章](P027_zephyr__modem__ppp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__net__net_linkaddr.h_文件参考.md)
