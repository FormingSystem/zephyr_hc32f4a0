---
id: learning.zephyr-docs.audio-video-model-reference.page-23
title: mpipe_message_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__message.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_mpipe\_message\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__message.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

携带消息类型和来源的消息结构（Message Structure）。

```c
#include <zephyr/mpipe/mpipe_message.h>
```

<a id="details"></a>

携带消息类型和来源的消息结构体。`domain` 和 `code` 描述失败情况，仅对 `MPIPE_MESSAGE_ERROR` 消息有意义。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_abb655d25f900b38c77164962970a493f"></a>

```c
struct mpipe_element * origin
```

相关声明：[mpipe_element](P021_mpipe_element_结构体.md)、[origin](#abb655d25f900b38c77164962970a493f)。

发布此消息的元素。

<a id="r_a45622118757cf3df3271380752700b42"></a>

```c
uint32_t type
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[type](#a45622118757cf3df3271380752700b42)。

消息类型，参见 `mpipe_message_type`。

<a id="r_a8559ee9f5039c992ed46636e3d953c49"></a>

```c
int32_t code
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[code](#a8559ee9f5039c992ed46636e3d953c49)。

`errno` 风格的负值错误码；未设置时为 0。

<a id="r_a05db95499949220a3009d837a897bb9d"></a>

```c
uint8_t domain
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[domain](#a05db95499949220a3009d837a897bb9d)。

元素当时正在执行的操作，参见 `mpipe_error_domain`。

## 23.2\_详细说明（Detailed Documentation）

<a id="a8559ee9f5039c992ed46636e3d953c49"></a>

### `code`

```c
int32_t mpipe_message::code
```

`errno` 风格的负值错误码；未设置时为 0。

<a id="a05db95499949220a3009d837a897bb9d"></a>

### `domain`

```c
uint8_t mpipe_message::domain
```

元素当时正在执行的操作，参见 `mpipe_error_domain`。

<a id="abb655d25f900b38c77164962970a493f"></a>

### `origin`

```c
struct mpipe_element* mpipe_message::origin
```

发布此消息的元素。

<a id="a45622118757cf3df3271380752700b42"></a>

### `type`

```c
uint32_t mpipe_message::type
```

消息类型，参见 `mpipe_message_type`。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_message.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_message.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h_source.html)
- [mpipe_element](P021_mpipe_element_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mpipe_message_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#ga2cbfffc03b1b703e80f73c70207cf049)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_error_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#ga686a716e86c28adfbb11dc0c1e172c22)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_mpipe_fake_src_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_mpipe_object_结构体.md)
