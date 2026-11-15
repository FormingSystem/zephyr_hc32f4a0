---
id: learning.zephyr-docs.platform-security-model-reference.page-14
title: intel_adsp_tlb_api_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structintel__adsp__tlb__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_intel\_adsp\_tlb\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structintel__adsp__tlb__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/mm/mm_drv_intel_adsp_mtl_tlb.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_ad9788abb323e4c70c08178c9df98a62e"></a>

```c
mm_save_context save_context
```

相关声明：[mm_save_context](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h.html#aec3b78e74d53f6a9fe6ca029c7d776a5)、[save_context](#ad9788abb323e4c70c08178c9df98a62e)。

<a id="r_a49ce206e8ac75d0fad79af3bb5cd9447"></a>

```c
mm_get_storage_size get_storage_size
```

相关声明：[mm_get_storage_size](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h.html#a19135d221cf896eb1795c2f22f6679bc)、[get_storage_size](#a49ce206e8ac75d0fad79af3bb5cd9447)。

## 14.2\_详细说明（Detailed Documentation）

<a id="a49ce206e8ac75d0fad79af3bb5cd9447"></a>

### `get_storage_size`

```c
mm_get_storage_size intel_adsp_tlb_api::get_storage_size
```

<a id="ad9788abb323e4c70c08178c9df98a62e"></a>

### `save_context`

```c
mm_save_context intel_adsp_tlb_api::save_context
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/mm/mm_drv_intel_adsp_mtl_tlb.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mm/mm_drv_intel_adsp_mtl_tlb.h](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h_source.html)
- [mm_save_context](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h.html#aec3b78e74d53f6a9fe6ca029c7d776a5)
- [mm_get_storage_size](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h.html#a19135d221cf896eb1795c2f22f6679bc)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_intel_adsp_mic_priv_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_intr_handle_data_t_结构体.md)
