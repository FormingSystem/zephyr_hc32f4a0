---
id: learning.zephyr-docs.device-power-control-model-reference.page-37
title: msosv2_descriptor_set_header_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__descriptor__set__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_msosv2\_descriptor\_set\_header\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__descriptor__set__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/usb/msos_desc.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_a4281eeb2128138b597fb53577ec8d57f"></a>

```c
uint16_t wLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wLength](#a4281eeb2128138b597fb53577ec8d57f)。

<a id="r_ae4931afed75f035e9dff4856ddee8609"></a>

```c
uint16_t wDescriptorType
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wDescriptorType](#ae4931afed75f035e9dff4856ddee8609)。

<a id="r_acf91f874e365a7f8ef60eaa19da517b4"></a>

```c
uint32_t dwWindowsVersion
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dwWindowsVersion](#acf91f874e365a7f8ef60eaa19da517b4)。

<a id="r_a3bab654cec13541096f08b43adb55f40"></a>

```c
uint16_t wTotalLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wTotalLength](#a3bab654cec13541096f08b43adb55f40)。

## 37.2\_详细说明（Detailed Documentation）

<a id="acf91f874e365a7f8ef60eaa19da517b4"></a>

### `dwWindowsVersion`

```c
uint32_t msosv2_descriptor_set_header::dwWindowsVersion
```

<a id="ae4931afed75f035e9dff4856ddee8609"></a>

### `wDescriptorType`

```c
uint16_t msosv2_descriptor_set_header::wDescriptorType
```

<a id="a4281eeb2128138b597fb53577ec8d57f"></a>

### `wLength`

```c
uint16_t msosv2_descriptor_set_header::wLength
```

<a id="a3bab654cec13541096f08b43adb55f40"></a>

### `wTotalLength`

```c
uint16_t msosv2_descriptor_set_header::wTotalLength
```

本数据类型文档由以下文件生成：

- `zephyr/usb/msos_desc.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/usb/msos_desc.h](https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_msosv2_configuration_subset_header_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_msosv2_function_subset_header_结构体.md)
