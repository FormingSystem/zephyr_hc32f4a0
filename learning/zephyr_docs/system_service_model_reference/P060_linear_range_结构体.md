---
id: learning.zephyr-docs.system-service-model-reference.page-60
title: linear_range_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlinear__range.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_linear\_range\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlinear__range.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

线性范围（Linear Range）。

```c
#include <zephyr/sys/linear_range.h>
```

<a id="details"></a>

线性范围（Linear Range）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_a4523369fa49fa1d6aa58f0d2634eb41d"></a>

```c
int32_t min
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[min](#a4523369fa49fa1d6aa58f0d2634eb41d)。

最小值。

<a id="r_a963889c27dd8541f7cd6528ac82401b3"></a>

```c
uint32_t step
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[step](#a963889c27dd8541f7cd6528ac82401b3)。

步长值（Step value）。

<a id="r_a705275f156fc4bcf5bb111be01aff6ef"></a>

```c
uint16_t min_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_idx](#a705275f156fc4bcf5bb111be01aff6ef)。

最小索引，必须小于或等于最大索引。

<a id="r_a84af63957a1b3e829cf1d53fa6342982"></a>

```c
uint16_t max_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_idx](#a84af63957a1b3e829cf1d53fa6342982)。

最大索引，必须大于或等于最小索引。

## 60.2\_详细说明（Detailed Documentation）

<a id="a84af63957a1b3e829cf1d53fa6342982"></a>

### `max_idx`

```c
uint16_t linear_range::max_idx
```

最大索引，必须大于或等于最小索引。

<a id="a4523369fa49fa1d6aa58f0d2634eb41d"></a>

### `min`

```c
int32_t linear_range::min
```

最小值。

<a id="a705275f156fc4bcf5bb111be01aff6ef"></a>

### `min_idx`

```c
uint16_t linear_range::min_idx
```

最小索引，必须小于或等于最大索引。

<a id="a963889c27dd8541f7cd6528ac82401b3"></a>

### `step`

```c
uint32_t linear_range::step
```

步长值（Step value）。

本数据类型文档由以下文件生成：

- `zephyr/sys/linear_range.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/sys/linear_range.h](https://docs.zephyrproject.org/latest/doxygen/html/linear__range_8h_source.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_kselacq_syntax_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_mcumgr_image_data_结构体.md)
