---
id: learning.zephyr-docs.api-file-interface-reference.page-32
title: zephyr__mpipe__base__mpipe_app_sink.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__sink_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_zephyr\_\_mpipe\_\_base\_\_mpipe\_app\_sink.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__sink_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

应用接收端元素（Application Sink Element）。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_sink.h>
#include <zephyr/mpipe/mpipe_structure.h>
```

查看此文件的源码。

应用接收端元素（Application sink element）。`app_sink` 元素将到达管线（pipeline）末端的缓冲区交给应用程序：既可通过运行于管线流处理上下文（streaming context）的回调交付，也可通过拉取 API（pull API）让应用程序按自己的节奏获取。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 32.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fapp_5Fsink_5Fcb"></a>

```c
struct mpipe_app_sink_cb
```

相关声明：[mpipe_app_sink_cb](../audio_video_model_reference/P013_mpipe_app_sink_cb_结构体.md)。

MPIPE_PROP_BASE_APP_SINK_CB的回调注册。

<a id="r_mpipe_5Fapp_5Fsink"></a>

```c
struct mpipe_app_sink
```

相关声明：[mpipe_app_sink](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md)。

应用接收端元素（Application Sink Element）的结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 32.2\_类型定义（Typedefs）

<a id="r_ga8bd213256bc8867364864eff4e9b0d55"></a>

```c
typedef void(* mpipe_app_sink_cb_t) (const struct net_buf *buf, void *user_data)
```

相关声明：[mpipe_app_sink_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ga8bd213256bc8867364864eff4e9b0d55)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

缓冲区回调（buffer callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 32.3\_枚举（Enumerations）

<a id="r_gab996263656e57f425230376ecdd838de"></a>

```c
enum { MPIPE_PROP_BASE_APP_SINK_CAPS = MPIPE_PROP_SINK_LAST , MPIPE_PROP_BASE_APP_SINK_CB }
```

相关声明：[MPIPE_PROP_BASE_APP_SINK_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ggab996263656e57f425230376ecdd838deac9e61be01787df7e978c00c91e68583b)、[MPIPE_PROP_BASE_APP_SINK_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ggab996263656e57f425230376ecdd838dea2dd7456ad7e1306258b259634c4d66a7)。

应用接收端（application sink）的属性标识符。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 32.4\_函数（Functions）

<a id="r_ga6ab7e49f03e81d49a32988f996760af1"></a>

```c
int mpipe_app_sink_init (struct mpipe_app_sink *app_sink, uint8_t id)
```

相关声明：[mpipe_app_sink_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ga6ab7e49f03e81d49a32988f996760af1)、[mpipe_app_sink](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化应用接收端元素。

<a id="r_ga2f62c9d0d779686aeb62ee6a393ed36b"></a>

```c
int mpipe_app_sink_pull (struct mpipe_app_sink *app_sink, struct net_buf **buf, k_timeout_t timeout)
```

相关声明：[mpipe_app_sink_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ga2f62c9d0d779686aeb62ee6a393ed36b)、[mpipe_app_sink](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

拉取下一个缓冲区。


## 32.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/mpipe/mpipe_element.h](../api_source_reference/P550_mpipe_element.h_源码浏览.md)
- [zephyr/mpipe/mpipe_sink.h](../api_source_reference/P558_mpipe_sink.h_源码浏览.md)
- [zephyr/mpipe/mpipe_structure.h](../api_source_reference/P560_mpipe_structure.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P543_mpipe_app_sink.h_源码浏览.md)
- [mpipe_app_sink_cb](../audio_video_model_reference/P013_mpipe_app_sink_cb_结构体.md)
- [mpipe_app_sink](../audio_video_model_reference/P012_mpipe_app_sink_结构体.md)
- [mpipe_app_sink_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ga8bd213256bc8867364864eff4e9b0d55)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [MPIPE_PROP_BASE_APP_SINK_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ggab996263656e57f425230376ecdd838deac9e61be01787df7e978c00c91e68583b)
- [MPIPE_PROP_BASE_APP_SINK_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ggab996263656e57f425230376ecdd838dea2dd7456ad7e1306258b259634c4d66a7)
- [mpipe_app_sink_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ga6ab7e49f03e81d49a32988f996760af1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_app_sink_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ga2f62c9d0d779686aeb62ee6a393ed36b)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)

<a id="header-details"></a>

---

[上一章](P031_zephyr__drivers__clock_control__mchp_clock_pic32cm_pl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P033_zephyr__mpipe__mpipe_src.h_文件参考.md)
