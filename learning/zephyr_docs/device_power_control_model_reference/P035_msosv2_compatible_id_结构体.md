---
id: learning.zephyr-docs.device-power-control-model-reference.page-35
title: msosv2_compatible_id_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__compatible__id.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_msosv2\_compatible\_id\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__compatible__id.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/usb/msos_desc.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_ad2fabcbcfe86dd7f6c7e21607392ed9f"></a>

```c
uint16_t wLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wLength](#ad2fabcbcfe86dd7f6c7e21607392ed9f)。

<a id="r_adfb121211a3e2519cdbf3afa91cd48e3"></a>

```c
uint16_t wDescriptorType
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wDescriptorType](#adfb121211a3e2519cdbf3afa91cd48e3)。

<a id="r_a213f32b16fda92bc5526abee2d5922b5"></a>

```c
uint8_t CompatibleID [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[CompatibleID](#a213f32b16fda92bc5526abee2d5922b5)。

<a id="r_affc8c55b00ddcc20841054ac8d8c6844"></a>

```c
uint8_t SubCompatibleID [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[SubCompatibleID](#affc8c55b00ddcc20841054ac8d8c6844)。

## 35.2\_详细说明（Detailed Documentation）

<a id="a213f32b16fda92bc5526abee2d5922b5"></a>

### `CompatibleID`

```c
uint8_t msosv2_compatible_id::CompatibleID[8]
```

<a id="affc8c55b00ddcc20841054ac8d8c6844"></a>

### `SubCompatibleID`

```c
uint8_t msosv2_compatible_id::SubCompatibleID[8]
```

<a id="adfb121211a3e2519cdbf3afa91cd48e3"></a>

### `wDescriptorType`

```c
uint16_t msosv2_compatible_id::wDescriptorType
```

<a id="ad2fabcbcfe86dd7f6c7e21607392ed9f"></a>

### `wLength`

```c
uint16_t msosv2_compatible_id::wLength
```

本数据类型文档由以下文件生成：

- `zephyr/usb/msos_desc.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/usb/msos_desc.h](https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_msosv2_ccgp_device_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_msosv2_configuration_subset_header_结构体.md)
