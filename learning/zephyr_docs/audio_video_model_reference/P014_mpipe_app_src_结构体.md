---
id: learning.zephyr-docs.audio-video-model-reference.page-14
title: mpipe_app_src_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__app__src.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_mpipe\_app\_src\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__app__src.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

应用源元素（Application Source Element）的结构。

```c
#include <zephyr/mpipe/base/mpipe_app_src.h>
```

<a id="details"></a>

应用源元素（Application Source Element）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_ae1027603257aecb656c175acc6f57fbe"></a>

```c
struct mpipe_src src
```

相关声明：[mpipe_src](P030_mpipe_src_结构体.md)、[src](#ae1027603257aecb656c175acc6f57fbe)。

基础源元素（base source element），必须是第一个成员。

<a id="r_adc96d20cf76b13694c00370c3d30ba73"></a>

```c
struct mpipe_structure caps
```

相关声明：[mpipe_structure](P031_mpipe_structure_结构体.md)、[caps](#adc96d20cf76b13694c00370c3d30ba73)。

所生成数据流的能力（capability），在每次协商时提供。

<a id="r_a4f578e934ae856ef6ae93f3e41949831"></a>

```c
struct mpipe_buffer_pool pool
```

相关声明：[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)、[pool](#a4f578e934ae856ef6ae93f3e41949831)。

承载载荷传输的缓冲池（buffer pool）。

<a id="r_ac13f9d17dac184228947e42f0ca71b5c"></a>

```c
struct k_msgq msgq
```

相关声明：[k_msgq](../msgstack_reference/P002_内核消息队列结构.md)、[msgq](#ac13f9d17dac184228947e42f0ca71b5c)。

已推入的缓冲区队列，由管线线程消费。

<a id="r_a0face8d4e3aaa965ce39df4a32be67b5"></a>

```c
char msgq_buffer [(CONFIG_MPIPE_BASE_APP_SRC_QUEUE_DEPTH+1) *sizeof(void *)]
```

相关声明：[msgq_buffer](#a0face8d4e3aaa965ce39df4a32be67b5)。

后备存储空间：配置的队列深度，外加一个哨兵（sentinel）槽位。

## 14.2\_详细说明（Detailed Documentation）

<a id="adc96d20cf76b13694c00370c3d30ba73"></a>

### `caps`

```c
struct mpipe_structure mpipe_app_src::caps
```

所生成数据流的能力（capability），在每次协商时提供。

<a id="ac13f9d17dac184228947e42f0ca71b5c"></a>

### `msgq`

```c
struct k_msgq mpipe_app_src::msgq
```

已推入的缓冲区队列，由管线线程消费。

<a id="a0face8d4e3aaa965ce39df4a32be67b5"></a>

### `msgq_buffer`

```c
char mpipe_app_src::msgq_buffer[(CONFIG_MPIPE_BASE_APP_SRC_QUEUE_DEPTH+1) *sizeof(void *)]
```

后备存储空间：配置的队列深度，外加一个哨兵（sentinel）槽位。

<a id="a4f578e934ae856ef6ae93f3e41949831"></a>

### `pool`

```c
struct mpipe_buffer_pool mpipe_app_src::pool
```

承载载荷传输的缓冲池（buffer pool）。

<a id="ae1027603257aecb656c175acc6f57fbe"></a>

### `src`

```c
struct mpipe_src mpipe_app_src::src
```

基础源元素（base source element），必须是第一个成员。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/base/mpipe_app_src.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/base/mpipe_app_src.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__app__src_8h_source.html)
- [mpipe_src](P030_mpipe_src_结构体.md)
- [mpipe_structure](P031_mpipe_structure_结构体.md)
- [mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_mpipe_app_sink_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_mpipe_bin_结构体.md)
