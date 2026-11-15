---
id: learning.zephyr-docs.device-power-control-model-reference.page-39
title: msosv2_guids_property_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__guids__property.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_msosv2\_guids\_property\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__guids__property.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/usb/msos_desc.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_a500199bebfa7f8bf300be51310497a0c"></a>

```c
uint16_t wLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wLength](#a500199bebfa7f8bf300be51310497a0c)。

<a id="r_acaa81e6bbaaec95922a80ef5a6000cd9"></a>

```c
uint16_t wDescriptorType
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wDescriptorType](#acaa81e6bbaaec95922a80ef5a6000cd9)。

<a id="r_aee143372e2bd13a32ae61e68ab429fbe"></a>

```c
uint16_t wPropertyDataType
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wPropertyDataType](#aee143372e2bd13a32ae61e68ab429fbe)。

<a id="r_a815f24af18f726244a9ab7d9f67e1cab"></a>

```c
uint16_t wPropertyNameLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wPropertyNameLength](#a815f24af18f726244a9ab7d9f67e1cab)。

<a id="r_ac447835ec1446a2e190228cab2b7dca8"></a>

```c
uint8_t PropertyName [42]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[PropertyName](#ac447835ec1446a2e190228cab2b7dca8)。

<a id="r_a1740a7fb0134313dba90cf794f0218f1"></a>

```c
uint16_t wPropertyDataLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wPropertyDataLength](#a1740a7fb0134313dba90cf794f0218f1)。

<a id="r_abf28542190ae7fececadacd3e8dba58a"></a>

```c
uint8_t bPropertyData [80]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bPropertyData](#abf28542190ae7fececadacd3e8dba58a)。

## 39.2\_详细说明（Detailed Documentation）

<a id="abf28542190ae7fececadacd3e8dba58a"></a>

### `bPropertyData`

```c
uint8_t msosv2_guids_property::bPropertyData[80]
```

<a id="ac447835ec1446a2e190228cab2b7dca8"></a>

### `PropertyName`

```c
uint8_t msosv2_guids_property::PropertyName[42]
```

<a id="acaa81e6bbaaec95922a80ef5a6000cd9"></a>

### `wDescriptorType`

```c
uint16_t msosv2_guids_property::wDescriptorType
```

<a id="a500199bebfa7f8bf300be51310497a0c"></a>

### `wLength`

```c
uint16_t msosv2_guids_property::wLength
```

<a id="a1740a7fb0134313dba90cf794f0218f1"></a>

### `wPropertyDataLength`

```c
uint16_t msosv2_guids_property::wPropertyDataLength
```

<a id="aee143372e2bd13a32ae61e68ab429fbe"></a>

### `wPropertyDataType`

```c
uint16_t msosv2_guids_property::wPropertyDataType
```

<a id="a815f24af18f726244a9ab7d9f67e1cab"></a>

### `wPropertyNameLength`

```c
uint16_t msosv2_guids_property::wPropertyNameLength
```

本数据类型文档由以下文件生成：

- `zephyr/usb/msos_desc.h`

## 39.3\_原页交叉引用（Cross References）

- [zephyr/usb/msos_desc.h](https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_msosv2_function_subset_header_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_msosv2_model_id_结构体.md)
