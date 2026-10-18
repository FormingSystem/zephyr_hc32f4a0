---
id: learning.zephyr-docs.platform-security-model-reference.page-15
title: intr_handle_data_t_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structintr__handle__data__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_intr\_handle\_data\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structintr__handle__data__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

中断处理程序（Interrupt Handler）的关联数据结构。

```c
#include <zephyr/drivers/interrupt_controller/intc_esp32.h>
```

<a id="details"></a>

中断处理程序（Interrupt Handler）的关联数据结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_a54ce22a2f0818180fbe25d0e9edf2036"></a>

```c
struct vector_desc_t * vector_desc
```

相关声明：[vector_desc_t](P073_vector_desc_t_结构体.md)、[vector_desc](#a54ce22a2f0818180fbe25d0e9edf2036)。

<a id="r_a86785e459328fac2f0758d588159bf3e"></a>

```c
struct shared_vector_desc_t * shared_vector_desc
```

相关声明：[shared_vector_desc_t](P055_shared_vector_desc_t_结构体.md)、[shared_vector_desc](#a86785e459328fac2f0758d588159bf3e)。

## 15.2\_详细说明（Detailed Documentation）

<a id="a86785e459328fac2f0758d588159bf3e"></a>

### `shared_vector_desc`

```c
struct shared_vector_desc_t* intr_handle_data_t::shared_vector_desc
```

<a id="a54ce22a2f0818180fbe25d0e9edf2036"></a>

### `vector_desc`

```c
struct vector_desc_t* intr_handle_data_t::vector_desc
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/interrupt_controller/intc_esp32.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/drivers/interrupt_controller/intc_esp32.h](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h_source.html)
- [vector_desc_t](P073_vector_desc_t_结构体.md)
- [shared_vector_desc_t](P055_shared_vector_desc_t_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_intel_adsp_tlb_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_its_driver_api_结构体.md)
