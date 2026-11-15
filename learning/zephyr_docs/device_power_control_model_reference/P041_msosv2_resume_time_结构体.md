---
id: learning.zephyr-docs.device-power-control-model-reference.page-41
title: msosv2_resume_time_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__resume__time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_msosv2\_resume\_time\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__resume__time.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/usb/msos_desc.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_a95a1ba0d9e5d0019dfeabfea0ddaf205"></a>

```c
uint16_t wLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wLength](#a95a1ba0d9e5d0019dfeabfea0ddaf205)。

<a id="r_a22fc11df55af95324cfeb2459a544bd4"></a>

```c
uint16_t wDescriptorType
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wDescriptorType](#a22fc11df55af95324cfeb2459a544bd4)。

<a id="r_a33ff93b8c7d97dc9732158b2293cd377"></a>

```c
uint8_t bResumeRecoveryTime
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bResumeRecoveryTime](#a33ff93b8c7d97dc9732158b2293cd377)。

<a id="r_a1a08a4ec1b884a68ffc6b52a84e747aa"></a>

```c
uint8_t bResumeSignalingTime
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bResumeSignalingTime](#a1a08a4ec1b884a68ffc6b52a84e747aa)。

## 41.2\_详细说明（Detailed Documentation）

<a id="a33ff93b8c7d97dc9732158b2293cd377"></a>

### `bResumeRecoveryTime`

```c
uint8_t msosv2_resume_time::bResumeRecoveryTime
```

<a id="a1a08a4ec1b884a68ffc6b52a84e747aa"></a>

### `bResumeSignalingTime`

```c
uint8_t msosv2_resume_time::bResumeSignalingTime
```

<a id="a22fc11df55af95324cfeb2459a544bd4"></a>

### `wDescriptorType`

```c
uint16_t msosv2_resume_time::wDescriptorType
```

<a id="a95a1ba0d9e5d0019dfeabfea0ddaf205"></a>

### `wLength`

```c
uint16_t msosv2_resume_time::wLength
```

本数据类型文档由以下文件生成：

- `zephyr/usb/msos_desc.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/usb/msos_desc.h](https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_msosv2_model_id_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_msosv2_vendor_revision_结构体.md)
