---
id: learning.zephyr-docs.api-file-service-interface-reference.page-40
title: zephyr__mpipe__mpipe_buffer.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_zephyr\_\_mpipe\_\_mpipe\_buffer.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

缓冲区和缓冲池（Buffer and Buffer Pool）的API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/net_buf.h>
```

查看此文件的源码。

缓冲区和缓冲池（Buffer and Buffer Pool）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 40.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fbuffer_5Fpool_5Fconfig"></a>

```c
struct mpipe_buffer_pool_config
```

相关声明：[mpipe_buffer_pool_config](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md)。

缓冲池（Buffer Pool）的配置结构。

<a id="r_mpipe_5Fbuffer_5Fpool"></a>

```c
struct mpipe_buffer_pool
```

相关声明：[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)。

缓冲池（Buffer Pool）结构。

<a id="r_mpipe_5Fbuffer_5Fmeta"></a>

```c
struct mpipe_buffer_meta
```

相关声明：[mpipe_buffer_meta](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md)。

存储在net_buf user_data中的通用缓冲区元数据（Buffer Metadata）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 40.2\_函数（Functions）

<a id="r_gaa7c45d601a5891ad7a19d2b107086947"></a>

```c
static struct mpipe_buffer_meta * mpipe_buffer_get_meta (const struct net_buf *buf)
```

相关声明：[mpipe_buffer_meta](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md)、[mpipe_buffer_get_meta](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gaa7c45d601a5891ad7a19d2b107086947)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取缓冲区承载的 mpipe 元数据（Metadata）。

<a id="r_gad0509018241d2b69c8188b22a61530c1"></a>

```c
void mpipe_buffer_destroy (struct net_buf *buf)
```

相关声明：[mpipe_buffer_destroy](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gad0509018241d2b69c8188b22a61530c1)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

`net_buf` 的销毁回调（Destroy Callback）。

<a id="r_gaca82ba8fed0f9b21281e9d89a8715378"></a>

```c
int mpipe_buffer_pool_configure (struct mpipe_buffer_pool *pool, const struct mpipe_structure *caps)
```

相关声明：[mpipe_buffer_pool_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gaca82ba8fed0f9b21281e9d89a8715378)、[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

配置缓冲池（Buffer Pool）。

<a id="r_ga8a80231824e6cbb7748e80df8d504e93"></a>

```c
int mpipe_buffer_pool_set_req_config (struct mpipe_buffer_pool *pool, const struct mpipe_buffer_pool_config *cfg)
```

相关声明：[mpipe_buffer_pool_set_req_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#ga8a80231824e6cbb7748e80df8d504e93)、[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)、[mpipe_buffer_pool_config](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md)。

声明缓冲池（Buffer Pool）自身提出的要求。

<a id="r_gab718120f2a3c3f2a13107fd14d9385ec"></a>

```c
int mpipe_buffer_pool_set_config (struct mpipe_buffer_pool *pool, const struct mpipe_buffer_pool_config *cfg)
```

相关声明：[mpipe_buffer_pool_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gab718120f2a3c3f2a13107fd14d9385ec)、[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)、[mpipe_buffer_pool_config](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md)。

将协商后的配置（Negotiated Configuration）应用到缓冲池。

<a id="r_ga74d5d359f4880059485689e085887b74"></a>

```c
int mpipe_buffer_pool_start (struct mpipe_buffer_pool *pool)
```

相关声明：[mpipe_buffer_pool_start](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#ga74d5d359f4880059485689e085887b74)、[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)。

启动缓冲池（Buffer Pool）。

<a id="r_ga7ed6b0b1108097583138a61402c077ff"></a>

```c
int mpipe_buffer_pool_stop (struct mpipe_buffer_pool *pool)
```

相关声明：[mpipe_buffer_pool_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#ga7ed6b0b1108097583138a61402c077ff)、[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)。

停止缓冲池（Buffer Pool）。

<a id="r_gabdb544b2a289a767976ecb9d97357eca"></a>

```c
void mpipe_buffer_pool_init (struct mpipe_buffer_pool *pool)
```

相关声明：[mpipe_buffer_pool_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gabdb544b2a289a767976ecb9d97357eca)、[mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)。

初始化缓冲池（Buffer Pool）。


## 40.3\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P546_mpipe_buffer.h_源码浏览.md)
- [mpipe_buffer_pool_config](../audio_video_model_reference/P018_mpipe_buffer_pool_config_结构体.md)
- [mpipe_buffer_pool](../audio_video_model_reference/P017_mpipe_buffer_pool_结构体.md)
- [mpipe_buffer_meta](../audio_video_model_reference/P016_mpipe_buffer_meta_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [mpipe_buffer_get_meta](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gaa7c45d601a5891ad7a19d2b107086947)
- [mpipe_buffer_destroy](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gad0509018241d2b69c8188b22a61530c1)
- [mpipe_buffer_pool_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gaca82ba8fed0f9b21281e9d89a8715378)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [mpipe_buffer_pool_set_req_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#ga8a80231824e6cbb7748e80df8d504e93)
- [mpipe_buffer_pool_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gab718120f2a3c3f2a13107fd14d9385ec)
- [mpipe_buffer_pool_start](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#ga74d5d359f4880059485689e085887b74)
- [mpipe_buffer_pool_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#ga7ed6b0b1108097583138a61402c077ff)
- [mpipe_buffer_pool_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gabdb544b2a289a767976ecb9d97357eca)

<a id="header-details"></a>

---

[上一章](P039_zephyr__net__midi2.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P041_zephyr__dt-bindings__gpio__nordic-npm13xx-gpio.h_文件参考.md)
