---
id: learning.zephyr-docs.device-power-control-model-reference.page-40
title: msosv2_model_id_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__model__id.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_msosv2\_model\_id\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__model__id.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/usb/msos_desc.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_a2355b2ab759e661462d61ffbdb7c29cd"></a>

```c
uint16_t wLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wLength](#a2355b2ab759e661462d61ffbdb7c29cd)。

<a id="r_af03a88860ff6086b0cda956f2ccff824"></a>

```c
uint16_t wDescriptorType
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wDescriptorType](#af03a88860ff6086b0cda956f2ccff824)。

<a id="r_ae87e515d83e0f979c993ef24d2486d08"></a>

```c
uint8_t ModelID [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ModelID](#ae87e515d83e0f979c993ef24d2486d08)。

## 40.2\_详细说明（Detailed Documentation）

<a id="ae87e515d83e0f979c993ef24d2486d08"></a>

### `ModelID`

```c
uint8_t msosv2_model_id::ModelID[16]
```

<a id="af03a88860ff6086b0cda956f2ccff824"></a>

### `wDescriptorType`

```c
uint16_t msosv2_model_id::wDescriptorType
```

<a id="a2355b2ab759e661462d61ffbdb7c29cd"></a>

### `wLength`

```c
uint16_t msosv2_model_id::wLength
```

本数据类型文档由以下文件生成：

- `zephyr/usb/msos_desc.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/usb/msos_desc.h](https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_msosv2_guids_property_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_msosv2_resume_time_结构体.md)
