---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-37
title: mspi_callback_context_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__callback__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_mspi\_callback\_context\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__callback__context.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI回调上下文（Callback Context）。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

MSPI回调上下文（Callback Context）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_a5649bddfac23544522969fc9e500eb0c"></a>

```c
struct mspi_event mspi_evt
```

相关声明：[mspi_event](P045_mspi_event_结构体.md)、[mspi_evt](#a5649bddfac23544522969fc9e500eb0c)。

MSPI事件（Event）。

<a id="r_ab2225b77f4d9e0403192c0ab11482e2e"></a>

```c
void * ctx
```

相关声明：[ctx](#ab2225b77f4d9e0403192c0ab11482e2e)。

用户定义的上下文（Context）。

## 37.2\_详细说明（Detailed Documentation）

<a id="ab2225b77f4d9e0403192c0ab11482e2e"></a>

### `ctx`

```c
void* mspi_callback_context::ctx
```

用户定义的上下文（Context）。

<a id="a5649bddfac23544522969fc9e500eb0c"></a>

### `mspi_evt`

```c
struct mspi_event mspi_callback_context::mspi_evt
```

MSPI事件（Event）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [mspi_event](P045_mspi_event_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_mspi_cadence_timing_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_mspi_ce_control_结构体.md)
