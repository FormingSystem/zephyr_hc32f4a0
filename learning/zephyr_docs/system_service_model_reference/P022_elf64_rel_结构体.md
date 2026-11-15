---
id: learning.zephyr-docs.system-service-model-reference.page-22
title: elf64_rel_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structelf64__rel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_elf64\_rel\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structelf64__rel.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

64位ELF的重定位条目（Relocation Entry）。

```c
#include <zephyr/llext/elf.h>
```

<a id="details"></a>

64 位 ELF 的重定位条目（relocation entry）。此结构体保存描述待执行重定位的信息；附加重定位信息保存在 `r_offset` 指向的位置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_a4fdfdc207826e470ba8affcdf149acc9"></a>

```c
elf64_addr r_offset
```

相关声明：[elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)、[r_offset](#a4fdfdc207826e470ba8affcdf149acc9)。

在节内执行重定位的位置偏移量。

<a id="r_aa861a3f29f7bd9a78d527de69baba00c"></a>

```c
elf64_xword r_info
```

相关声明：[elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)、[r_info](#aa861a3f29f7bd9a78d527de69baba00c)。

有关重定位、关联符号及类型的信息。

## 22.2\_详细说明（Detailed Documentation）

<a id="aa861a3f29f7bd9a78d527de69baba00c"></a>

### `r_info`

```c
elf64_xword elf64_rel::r_info
```

有关重定位、关联符号及类型的信息。

<a id="a4fdfdc207826e470ba8affcdf149acc9"></a>

### `r_offset`

```c
elf64_addr elf64_rel::r_offset
```

在节内执行重定位的位置偏移量。

本数据类型文档由以下文件生成：

- `zephyr/llext/elf.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/llext/elf.h](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h_source.html)
- [elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)
- [elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_elf64_ehdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_elf64_rela_结构体.md)
