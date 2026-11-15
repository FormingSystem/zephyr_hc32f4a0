---
id: learning.zephyr-docs.audio-video-model-reference.page-68
title: mic_privacy_mask_联合体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionmic__privacy__mask.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_mic\_privacy\_mask\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionmic__privacy__mask.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/mic_privacy/intel/mic_privacy.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_a9ca8420acd33e12b2454457d4e626c03"></a>

```c
uint32_t value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[value](#a9ca8420acd33e12b2454457d4e626c03)。

```c
struct {
```

<a id="r_a0ae02b8d3ef9bc3d3249eb81a0c7d130"></a>

```c
uint32_t sndw:7
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sndw](#a7803afbf97e48fa202cbb40e96777437)。

<a id="r_a04b9ad7644d27a9a4e295d91dea382c5"></a>

```c
uint32_t dmic:1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dmic](#a074ae40d422faa6a338454ca5072c978)。

<a id="r_a8fd6e98bc1652ab1b81608f906572e92"></a>

```c
};
```

## 68.2\_详细说明（Detailed Documentation）

<a id="a8fd6e98bc1652ab1b81608f906572e92"></a>

### `[struct]`

```c
struct { ... } mic_privacy_mask
```

<a id="a074ae40d422faa6a338454ca5072c978"></a>

### `dmic`

```c
uint32_t mic_privacy_mask::dmic
```

<a id="a7803afbf97e48fa202cbb40e96777437"></a>

### `sndw`

```c
uint32_t mic_privacy_mask::sndw
```

<a id="a9ca8420acd33e12b2454457d4e626c03"></a>

### `value`

```c
uint32_t mic_privacy_mask::value
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/mic_privacy/intel/mic_privacy.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mic_privacy/intel/mic_privacy.h](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mic_privacy_mask](P068_mic_privacy_mask_联合体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_audio_property_value_t_联合体.md) · [返回大纲](大纲.md) · [下一章](P069_mpipe_value_bound_联合体.md)
