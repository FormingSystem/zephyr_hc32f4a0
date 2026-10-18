---
id: learning.zephyr-docs.audio-video-model-reference.page-18
title: mpipe_buffer_pool_config_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__buffer__pool__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_mpipe\_buffer\_pool\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__buffer__pool__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

缓冲池（Buffer Pool）的配置结构。

```c
#include <zephyr/mpipe/mpipe_buffer.h>
```

<a id="details"></a>

缓冲池（Buffer Pool）的配置结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_a94e5cd9b983b5ca8cea2cba02f8b1ec2"></a>

```c
uint32_t size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[size](#a94e5cd9b983b5ca8cea2cba02f8b1ec2)。

每个缓冲区的大小，单位为字节。

<a id="r_a99176426b6d20ec18eb099be1416be24"></a>

```c
uint16_t align
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[align](#a99176426b6d20ec18eb099be1416be24)。

每个缓冲区的对齐要求，单位为字节。

<a id="r_ab8412341dbd0fe3404bcbbcdd2536258"></a>

```c
uint8_t min_buffers
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_buffers](#ab8412341dbd0fe3404bcbbcdd2536258)。

缓冲池正常工作所需的最少缓冲区数量。

<a id="r_ab5717d6793f8f7788edc0d4874a39cd5"></a>

```c
uint8_t max_buffers
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_buffers](#ab5717d6793f8f7788edc0d4874a39cd5)。

缓冲池中的最大缓冲区数量。

## 18.2\_详细说明（Detailed Documentation）

<a id="a99176426b6d20ec18eb099be1416be24"></a>

### `align`

```c
uint16_t mpipe_buffer_pool_config::align
```

每个缓冲区的对齐要求，单位为字节。

<a id="ab5717d6793f8f7788edc0d4874a39cd5"></a>

### `max_buffers`

```c
uint8_t mpipe_buffer_pool_config::max_buffers
```

缓冲池中的最大缓冲区数量。

<a id="ab8412341dbd0fe3404bcbbcdd2536258"></a>

### `min_buffers`

```c
uint8_t mpipe_buffer_pool_config::min_buffers
```

缓冲池正常工作所需的最少缓冲区数量。

<a id="a94e5cd9b983b5ca8cea2cba02f8b1ec2"></a>

### `size`

```c
uint32_t mpipe_buffer_pool_config::size
```

每个缓冲区的大小，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_buffer.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_mpipe_buffer_pool_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_mpipe_caps_filter_结构体.md)
