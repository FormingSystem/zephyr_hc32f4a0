---
id: learning.zephyr-docs.device-power-control-model-reference.page-26
title: mb_image_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmb__image.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_mb\_image\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmb__image.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BBC micro:bit显示图像（Display Image）的表示。

```c
#include <zephyr/display/mb_display.h>
```

<a id="details"></a>

BBC micro:bit 显示图像的表示结构。通常不应直接使用此结构体，而应通过 `MB_IMAGE()` 宏创建。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

```c
union {
```

```c
struct {
```

<a id="r_ae56068e91ef3551b6ba558393b203308"></a>

```c
uint8_t c1:1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c1](#a044fee7be7fb1e5b3e2c2dab74011d9a)。

<a id="r_a103b353273a866e1bdf7f0e9c28eb230"></a>

```c
uint8_t c2:1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c2](#ad7eb096bb15a0bb8378bae32804fe6c6)。

<a id="r_ab9ddca3102f3eb43ffe1d82a22c33cff"></a>

```c
uint8_t c3:1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c3](#a88455e59017a73533e727671019f6ea0)。

<a id="r_a16fdb9ff59684db098af93e10e3000df"></a>

```c
uint8_t c4:1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c4](#a506e5ac82c7229ba7e89f67de8fbcbe2)。

<a id="r_a78491d4994120ddfa85cfdef48b626fd"></a>

```c
uint8_t c5:1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c5](#a2af8f97c0ddc8cf463cf83a483e3025b)。

<a id="r_a7dd73c3d6a87f2159c31380826036668"></a>

```c
} r [5]
```

相关声明：[r](#a93ec1bb1c0cdc09de75d00976bd23eeb)。

<a id="r_a0386ed5d741d7d4d119019e553246c83"></a>

```c
uint8_t row [5]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[row](#a158f0bdbb7d135da0dcf5c6b997d0ff5)。

<a id="r_ad557daa0c80ebb2e3c314ecf1da234c5"></a>

```c
};
```

## 26.2\_详细说明（Detailed Documentation）

<a id="ad557daa0c80ebb2e3c314ecf1da234c5"></a>

### `[union]`

```c
union { ... } mb_image
```

<a id="a044fee7be7fb1e5b3e2c2dab74011d9a"></a>

### `c1`

```c
uint8_t mb_image::c1
```

<a id="ad7eb096bb15a0bb8378bae32804fe6c6"></a>

### `c2`

```c
uint8_t mb_image::c2
```

<a id="a88455e59017a73533e727671019f6ea0"></a>

### `c3`

```c
uint8_t mb_image::c3
```

<a id="a506e5ac82c7229ba7e89f67de8fbcbe2"></a>

### `c4`

```c
uint8_t mb_image::c4
```

<a id="a2af8f97c0ddc8cf463cf83a483e3025b"></a>

### `c5`

```c
uint8_t mb_image::c5
```

<a id="a93ec1bb1c0cdc09de75d00976bd23eeb"></a>

### `[struct]`

```c
struct { ... } mb_image::r[5]
```

<a id="a158f0bdbb7d135da0dcf5c6b997d0ff5"></a>

### `row`

```c
uint8_t mb_image::row[5]
```

本数据类型文档由以下文件生成：

- `zephyr/display/mb_display.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/display/mb_display.h](https://docs.zephyrproject.org/latest/doxygen/html/mb__display_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [MB_IMAGE()](https://docs.zephyrproject.org/latest/doxygen/html/group__mb__display.html#ga529a5650acaf699b23b4b4234127cf2c)
- [mb_image](P026_mb_image_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_max32_perclk_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_media_element_item_attr_结构体.md)
