---
id: learning.zephyr-docs.network-service-model-reference.page-24
title: http2_settings_field_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp2__settings__field.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_http2\_settings\_field\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp2__settings__field.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP/2设置字段（Settings Field）。

```c
#include <zephyr/net/http/frame.h>
```

<a id="details"></a>

HTTP/2设置字段（Settings Field）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_a66561355ba380a09c0ca8df583c085b8"></a>

```c
uint16_t id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id](#a66561355ba380a09c0ca8df583c085b8)。

字段 ID。

<a id="r_a3093b8f2b69ae06972fecbe89a18c342"></a>

```c
uint32_t value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[value](#a3093b8f2b69ae06972fecbe89a18c342)。

字段值。

## 24.2\_详细说明（Detailed Documentation）

<a id="a66561355ba380a09c0ca8df583c085b8"></a>

### `id`

```c
uint16_t http2_settings_field::id
```

字段 ID。

<a id="a3093b8f2b69ae06972fecbe89a18c342"></a>

### `value`

```c
uint32_t http2_settings_field::value
```

字段值。

本数据类型文档由以下文件生成：

- `zephyr/net/http/frame.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/net/http/frame.h](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_hdlc_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_igmp_param_结构体.md)
