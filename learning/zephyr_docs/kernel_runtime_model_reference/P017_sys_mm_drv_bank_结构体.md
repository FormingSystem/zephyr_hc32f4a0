---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-17
title: sys_mm_drv_bank_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsys__mm__drv__bank.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_sys\_mm\_drv\_bank\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsys__mm__drv__bank.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内存组（Memory Banks）的信息。

```c
#include <zephyr/drivers/mm/mm_drv_bank.h>
```

<a id="details"></a>

内存组（Memory Banks）的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_a8fd91db4f69c273b2d26bb770292cd83"></a>

```c
uint32_t unmapped_pages
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[unmapped_pages](#a8fd91db4f69c273b2d26bb770292cd83)。

未映射页面（Unmapped Pages）的数量。

<a id="r_a2e84b41e42b801825aa694e569e8ad6c"></a>

```c
uint32_t mapped_pages
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mapped_pages](#a2e84b41e42b801825aa694e569e8ad6c)。

已映射页面（Mapped Pages）的数量。

<a id="r_a69f4b9f6a7fed6403e7271a4ecbe5ad1"></a>

```c
uint32_t max_mapped_pages
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_mapped_pages](#a69f4b9f6a7fed6403e7271a4ecbe5ad1)。

自上次计数器复位以来已映射页面（Mapped Pages）数量的最大值。

## 17.2\_详细说明（Detailed Documentation）

<a id="a2e84b41e42b801825aa694e569e8ad6c"></a>

### `mapped_pages`

```c
uint32_t sys_mm_drv_bank::mapped_pages
```

已映射页面（Mapped Pages）的数量。

<a id="a69f4b9f6a7fed6403e7271a4ecbe5ad1"></a>

### `max_mapped_pages`

```c
uint32_t sys_mm_drv_bank::max_mapped_pages
```

自上次计数器复位以来已映射页面（Mapped Pages）数量的最大值。

<a id="a8fd91db4f69c273b2d26bb770292cd83"></a>

### `unmapped_pages`

```c
uint32_t sys_mm_drv_bank::unmapped_pages
```

未映射页面（Unmapped Pages）的数量。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mm/mm_drv_bank.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mm/mm_drv_bank.h](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__bank_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_sys_getopt_state_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_sys_mm_drv_region_结构体.md)
