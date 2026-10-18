---
id: learning.zephyr-docs.audio-video-model-reference.page-69
title: mpipe_value_bound_联合体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionmpipe__value__bound.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_mpipe\_value\_bound\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionmpipe__value__bound.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

范围值（Range Value）的一个端点或其步长。

```c
#include <zephyr/mpipe/mpipe_value.h>
```

<a id="details"></a>

范围值（Range Value）的一个端点或其步长。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

<a id="r_afe818d5dafd142fa89ca33aba7c5a671"></a>

```c
int32_t v_int
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[v_int](#afe818d5dafd142fa89ca33aba7c5a671)。

有符号整数范围类型：`MPIPE_TYPE_INT_RANGE`。

<a id="r_a30a5b23650704fa72a62ea9f3558a7b8"></a>

```c
uint32_t v_uint
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[v_uint](#a30a5b23650704fa72a62ea9f3558a7b8)。

无符号整数范围类型：`MPIPE_TYPE_UINT_RANGE`。

## 69.2\_详细说明（Detailed Documentation）

<a id="afe818d5dafd142fa89ca33aba7c5a671"></a>

### `v_int`

```c
int32_t mpipe_value_bound::v_int
```

有符号整数范围类型：`MPIPE_TYPE_INT_RANGE`。

<a id="a30a5b23650704fa72a62ea9f3558a7b8"></a>

### `v_uint`

```c
uint32_t mpipe_value_bound::v_uint
```

无符号整数范围类型：`MPIPE_TYPE_UINT_RANGE`。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_value.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_value.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__value_8h_source.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_mic_privacy_mask_联合体.md) · [返回大纲](大纲.md)
