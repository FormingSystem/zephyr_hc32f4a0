---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-18
title: sys_mm_drv_region_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsys__mm__drv__region.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_sys\_mm\_drv\_region\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsys__mm__drv__region.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示可用内存区域（Available Memory Region）。

```c
#include <zephyr/drivers/mm/system_mm.h>
```

<a id="details"></a>

表示可用内存区域（Available Memory Region），可供分配器使用。驱动定义的属性可用于指导各区域的正确使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_a8dfa465f83cf5f6115094b6b5727f418"></a>

```c
void * addr
```

相关声明：[addr](#a8dfa465f83cf5f6115094b6b5727f418)。

内存区域（Memory Region）的地址。

<a id="r_a5b48a908a5393fec377edcd3760c18ad"></a>

```c
size_t size
```

相关声明：[size](#a5b48a908a5393fec377edcd3760c18ad)。

内存区域（Memory Region）的大小。

<a id="r_a6838fe4bd4daab440152c4d666a4597d"></a>

```c
uint32_t attr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[attr](#a6838fe4bd4daab440152c4d666a4597d)。

驱动定义的内存区域（Memory Region）属性。

## 18.2\_详细说明（Detailed Documentation）

<a id="a8dfa465f83cf5f6115094b6b5727f418"></a>

### `addr`

```c
void* sys_mm_drv_region::addr
```

内存区域（Memory Region）的地址。

<a id="a6838fe4bd4daab440152c4d666a4597d"></a>

### `attr`

```c
uint32_t sys_mm_drv_region::attr
```

驱动定义的内存区域（Memory Region）属性。

<a id="a5b48a908a5393fec377edcd3760c18ad"></a>

### `size`

```c
size_t sys_mm_drv_region::size
```

内存区域（Memory Region）的大小。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mm/system_mm.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mm/system_mm.h](https://docs.zephyrproject.org/latest/doxygen/html/system__mm_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_sys_mm_drv_bank_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_sys_winstream_结构体.md)
