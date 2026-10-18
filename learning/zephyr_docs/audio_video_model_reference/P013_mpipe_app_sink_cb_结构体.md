---
id: learning.zephyr-docs.audio-video-model-reference.page-13
title: mpipe_app_sink_cb_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__app__sink__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_mpipe\_app\_sink\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__app__sink__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MPIPE_PROP_BASE_APP_SINK_CB的回调注册。

```c
#include <zephyr/mpipe/base/mpipe_app_sink.h>
```

<a id="details"></a>

MPIPE_PROP_BASE_APP_SINK_CB的回调注册。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_a90c7a21725790e1e4790d78dac9b207e"></a>

```c
mpipe_app_sink_cb_t fn
```

相关声明：[mpipe_app_sink_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ga8bd213256bc8867364864eff4e9b0d55)、[fn](#a90c7a21725790e1e4790d78dac9b207e)。

为每个缓冲区调用的函数。

<a id="r_a51c6b2ef1d60e8d7d7cb644467865365"></a>

```c
void * user_data
```

相关声明：[user_data](#a51c6b2ef1d60e8d7d7cb644467865365)。

原样传递给回调。

## 13.2\_详细说明（Detailed Documentation）

<a id="a90c7a21725790e1e4790d78dac9b207e"></a>

### `fn`

```c
mpipe_app_sink_cb_t mpipe_app_sink_cb::fn
```

为每个缓冲区调用的函数。

<a id="a51c6b2ef1d60e8d7d7cb644467865365"></a>

### `user_data`

```c
void* mpipe_app_sink_cb::user_data
```

原样传递给回调。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/base/mpipe_app_sink.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/base/mpipe_app_sink.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__sink_8h_source.html)
- [mpipe_app_sink_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__app__sink.html#ga8bd213256bc8867364864eff4e9b0d55)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_mpipe_app_sink_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_mpipe_app_src_结构体.md)
