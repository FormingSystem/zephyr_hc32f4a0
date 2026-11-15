---
id: learning.zephyr-docs.device-power-control-model-reference.page-42
title: msosv2_vendor_revision_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__vendor__revision.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_msosv2\_vendor\_revision\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmsosv2__vendor__revision.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/usb/msos_desc.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_a4b29a145268e89c416f50cddc28f0ff4"></a>

```c
uint16_t wLength
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wLength](#a4b29a145268e89c416f50cddc28f0ff4)。

<a id="r_a6ad0f9afb827947e4e2bfca339b70ceb"></a>

```c
uint16_t wDescriptorType
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wDescriptorType](#a6ad0f9afb827947e4e2bfca339b70ceb)。

<a id="r_aebed4cce3752a96a82fb25e3071a021c"></a>

```c
uint16_t VendorRevision
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[VendorRevision](#aebed4cce3752a96a82fb25e3071a021c)。

## 42.2\_详细说明（Detailed Documentation）

<a id="aebed4cce3752a96a82fb25e3071a021c"></a>

### `VendorRevision`

```c
uint16_t msosv2_vendor_revision::VendorRevision
```

<a id="a6ad0f9afb827947e4e2bfca339b70ceb"></a>

### `wDescriptorType`

```c
uint16_t msosv2_vendor_revision::wDescriptorType
```

<a id="a4b29a145268e89c416f50cddc28f0ff4"></a>

### `wLength`

```c
uint16_t msosv2_vendor_revision::wLength
```

本数据类型文档由以下文件生成：

- `zephyr/usb/msos_desc.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/usb/msos_desc.h](https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_msosv2_resume_time_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_mspm0_sys_clock_结构体.md)
