---
id: learning.zephyr-docs.device-power-control-model-reference.page-38
title: msosv2_function_subset_header_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__function__subset__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_msosv2\_function\_subset\_header\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__function__subset__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/usb/msos_desc.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_a10e00ccb02a6e2c9c4c5f4d634414a0c"></a>

```c
uint16_t wLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wLength](#a10e00ccb02a6e2c9c4c5f4d634414a0c)。

<a id="r_a4a93fdd2d9ea65b5b9097f921629c644"></a>

```c
uint16_t wDescriptorType
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wDescriptorType](#a4a93fdd2d9ea65b5b9097f921629c644)。

<a id="r_abf8bbff467411af8f259d2f16dc73649"></a>

```c
uint8_t bFirstInterface
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bFirstInterface](#abf8bbff467411af8f259d2f16dc73649)。

<a id="r_a07a64f2419014f41fa356fd85976985d"></a>

```c
uint8_t bReserved
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bReserved](#a07a64f2419014f41fa356fd85976985d)。

<a id="r_a7c3d3e7cd0577dc4ceab66615fefbe46"></a>

```c
uint16_t wSubsetLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wSubsetLength](#a7c3d3e7cd0577dc4ceab66615fefbe46)。

## 38.2\_详细说明（Detailed Documentation）

<a id="abf8bbff467411af8f259d2f16dc73649"></a>

### `bFirstInterface`

```c
uint8_t msosv2_function_subset_header::bFirstInterface
```

<a id="a07a64f2419014f41fa356fd85976985d"></a>

### `bReserved`

```c
uint8_t msosv2_function_subset_header::bReserved
```

<a id="a4a93fdd2d9ea65b5b9097f921629c644"></a>

### `wDescriptorType`

```c
uint16_t msosv2_function_subset_header::wDescriptorType
```

<a id="a10e00ccb02a6e2c9c4c5f4d634414a0c"></a>

### `wLength`

```c
uint16_t msosv2_function_subset_header::wLength
```

<a id="a7c3d3e7cd0577dc4ceab66615fefbe46"></a>

### `wSubsetLength`

```c
uint16_t msosv2_function_subset_header::wSubsetLength
```

本数据类型文档由以下文件生成：

- `zephyr/usb/msos_desc.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/usb/msos_desc.h](https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_msosv2_descriptor_set_header_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_msosv2_guids_property_结构体.md)
