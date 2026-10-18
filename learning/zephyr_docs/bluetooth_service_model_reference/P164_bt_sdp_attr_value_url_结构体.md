---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-164
title: bt_sdp_attr_value_url_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attr__value__url.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第164章\_bt\_sdp\_attr\_value\_url\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attr__value__url.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务发现协议（SDP）URL字符串类型的属性值。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

URL 字符串类型的 SDP 属性值。此结构体保存从 SDP 属性中解析出的 URL 字符串值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 164.1\_数据成员（Data Fields）

<a id="r_a7ff5d8b06952b873f6b5c60129fa346f"></a>

```c
uint32_t len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[len](#a7ff5d8b06952b873f6b5c60129fa346f)。

URL 字符串的长度，单位为字节。

<a id="r_aed7f8929167df11bb0db2249fc5957d9"></a>

```c
uint8_t * url
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[url](#aed7f8929167df11bb0db2249fc5957d9)。

指向 URL 字符串数据的指针。

## 164.2\_详细说明（Detailed Documentation）

<a id="a7ff5d8b06952b873f6b5c60129fa346f"></a>

### `len`

```c
uint32_t bt_sdp_attr_value_url::len
```

URL 字符串的长度，单位为字节。

<a id="aed7f8929167df11bb0db2249fc5957d9"></a>

### `url`

```c
uint8_t* bt_sdp_attr_value_url::url
```

指向 URL 字符串数据的指针。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 164.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P163_bt_sdp_attr_value_uint_结构体.md) · [返回大纲](大纲.md) · [下一章](P165_bt_sdp_attribute_结构体.md)
