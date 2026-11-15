---
id: learning.zephyr-docs.audio-video-model-reference.page-12
title: mpipe_app_sink_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__app__sink.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_mpipe\_app\_sink\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__app__sink.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

应用接收端元素（Application Sink Element）的结构。

```c
#include <zephyr/mpipe/base/mpipe_app_sink.h>
```

<a id="details"></a>

应用接收端元素（Application Sink Element）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_a0130d318174f6d1cbc9970a163886763"></a>

```c
struct mpipe_sink sink
```

相关声明：[mpipe_sink](P029_mpipe_sink_结构体.md)、[sink](#a0130d318174f6d1cbc9970a163886763)。

基础接收端元素（base sink element），必须是第一个成员。

<a id="r_a75db864f047d15bc7ea2bb9e0c67c3e7"></a>

```c
struct mpipe_structure caps
```

相关声明：[mpipe_structure](P031_mpipe_structure_结构体.md)、[caps](#a75db864f047d15bc7ea2bb9e0c67c3e7)。

接收端接受的能力（capability），在每次协商时提供。

<a id="r_a4fdd22f37571f00d27a311e39d408d34"></a>

```c
struct mpipe_app_sink_cb cb
```

相关声明：[mpipe_app_sink_cb](P013_mpipe_app_sink_cb_结构体.md)、[cb](#a4fdd22f37571f00d27a311e39d408d34)。

可选的缓冲区回调。

<a id="r_a194a07370e0f213e08862808b2a5878f"></a>

```c
struct k_msgq msgq
```

相关声明：[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)、[msgq](#a194a07370e0f213e08862808b2a5878f)。

等待拉取（pull）的缓冲区队列，在未设置回调时使用。

<a id="r_a91df7398dfd2b8af883871fdaf1e5947"></a>

```c
char msgq_buffer [CONFIG_MPIPE_BASE_APP_SINK_QUEUE_DEPTH *sizeof(void *)]
```

相关声明：[msgq_buffer](#a91df7398dfd2b8af883871fdaf1e5947)。

队列的后备存储空间（backing storage）。

## 12.2\_详细说明（Detailed Documentation）

<a id="a75db864f047d15bc7ea2bb9e0c67c3e7"></a>

### `caps`

```c
struct mpipe_structure mpipe_app_sink::caps
```

接收端接受的能力（capability），在每次协商时提供。

<a id="a4fdd22f37571f00d27a311e39d408d34"></a>

### `cb`

```c
struct mpipe_app_sink_cb mpipe_app_sink::cb
```

可选的缓冲区回调。

<a id="a194a07370e0f213e08862808b2a5878f"></a>

### `msgq`

```c
struct k_msgq mpipe_app_sink::msgq
```

等待拉取（pull）的缓冲区队列，在未设置回调时使用。

<a id="a91df7398dfd2b8af883871fdaf1e5947"></a>

### `msgq_buffer`

```c
char mpipe_app_sink::msgq_buffer[CONFIG_MPIPE_BASE_APP_SINK_QUEUE_DEPTH *sizeof(void *)]
```

队列的后备存储空间（backing storage）。

<a id="a0130d318174f6d1cbc9970a163886763"></a>

### `sink`

```c
struct mpipe_sink mpipe_app_sink::sink
```

基础接收端元素（base sink element），必须是第一个成员。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/base/mpipe_app_sink.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/base/mpipe_app_sink.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__sink_8h_source.html)
- [mpipe_sink](P029_mpipe_sink_结构体.md)
- [mpipe_structure](P031_mpipe_structure_结构体.md)
- [mpipe_app_sink_cb](P013_mpipe_app_sink_cb_结构体.md)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_mpipe_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_mpipe_app_sink_cb_结构体.md)
