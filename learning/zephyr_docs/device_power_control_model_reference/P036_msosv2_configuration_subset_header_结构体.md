---
id: learning.zephyr-docs.device-power-control-model-reference.page-36
title: msosv2_configuration_subset_header_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__configuration__subset__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_msosv2\_configuration\_subset\_header\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__configuration__subset__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/usb/msos_desc.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_a7468f6428046553abf5e97172b52d477"></a>

```c
uint16_t wLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wLength](#a7468f6428046553abf5e97172b52d477)。

<a id="r_ada03982dd6680a45d7cd2ba9e791c54e"></a>

```c
uint16_t wDescriptorType
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wDescriptorType](#ada03982dd6680a45d7cd2ba9e791c54e)。

<a id="r_a044e9d3a0ec479564406f04d895e353c"></a>

```c
uint8_t bConfigurationValue
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bConfigurationValue](#a044e9d3a0ec479564406f04d895e353c)。

<a id="r_aa063ff78775c00edde1de6e274a2b817"></a>

```c
uint8_t bReserved
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bReserved](#aa063ff78775c00edde1de6e274a2b817)。

<a id="r_a044cf7d76fa93bfaa265bd5c24d8d413"></a>

```c
uint16_t wTotalLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wTotalLength](#a044cf7d76fa93bfaa265bd5c24d8d413)。

## 36.2\_详细说明（Detailed Documentation）

<a id="a044e9d3a0ec479564406f04d895e353c"></a>

### `bConfigurationValue`

```c
uint8_t msosv2_configuration_subset_header::bConfigurationValue
```

<a id="aa063ff78775c00edde1de6e274a2b817"></a>

### `bReserved`

```c
uint8_t msosv2_configuration_subset_header::bReserved
```

<a id="ada03982dd6680a45d7cd2ba9e791c54e"></a>

### `wDescriptorType`

```c
uint16_t msosv2_configuration_subset_header::wDescriptorType
```

<a id="a7468f6428046553abf5e97172b52d477"></a>

### `wLength`

```c
uint16_t msosv2_configuration_subset_header::wLength
```

<a id="a044cf7d76fa93bfaa265bd5c24d8d413"></a>

### `wTotalLength`

```c
uint16_t msosv2_configuration_subset_header::wTotalLength
```

本数据类型文档由以下文件生成：

- `zephyr/usb/msos_desc.h`

## 36.3\_原页交叉引用（Cross References）

- [zephyr/usb/msos_desc.h](https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_msosv2_compatible_id_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_msosv2_descriptor_set_header_结构体.md)
