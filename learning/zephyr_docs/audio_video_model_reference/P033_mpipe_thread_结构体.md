---
id: learning.zephyr-docs.audio-video-model-reference.page-33
title: mpipe_thread_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__thread.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_mpipe\_thread\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__thread.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对k_thread的简单封装（Wrapper）。

```c
#include <zephyr/mpipe/mpipe_thread.h>
```

<a id="details"></a>

对 `k_thread` 的简单封装。元素嵌入一个此结构体并设置优先级；其他成员均属于内部实现。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_a4f75d45bd330b68366bbdeb0a32f8295"></a>

```c
int priority
```

相关声明：[priority](#a4f75d45bd330b68366bbdeb0a32f8295)。

线程优先级。

## 33.2\_详细说明（Detailed Documentation）

<a id="a4f75d45bd330b68366bbdeb0a32f8295"></a>

### `priority`

```c
int mpipe_thread::priority
```

线程优先级。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_thread.h`

## 33.3\_原页交叉引用（Cross References）

- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [zephyr/mpipe/mpipe_thread.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__thread_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_mpipe_tee_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_mpipe_transform_结构体.md)
