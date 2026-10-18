---
id: learning.zephyr-docs.system-service-model-reference.page-17
title: elf32_rel_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structelf32__rel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_elf32\_rel\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structelf32__rel.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

32位ELF的重定位条目（Relocation Entry）。

```c
#include <zephyr/llext/elf.h>
```

<a id="details"></a>

32 位 ELF 的重定位条目（relocation entry）。此结构体保存描述待执行重定位的信息；附加重定位信息保存在 `r_offset` 指向的位置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_a2bea1d7ef2a0c148cd9ae21386721f40"></a>

```c
elf32_addr r_offset
```

相关声明：[elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)、[r_offset](#a2bea1d7ef2a0c148cd9ae21386721f40)。

在节内执行重定位的位置偏移量。

<a id="r_ac93ab16d071b87719651f517893bba97"></a>

```c
elf32_word r_info
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[r_info](#ac93ab16d071b87719651f517893bba97)。

有关重定位、关联符号及类型的信息。

## 17.2\_详细说明（Detailed Documentation）

<a id="ac93ab16d071b87719651f517893bba97"></a>

### `r_info`

```c
elf32_word elf32_rel::r_info
```

有关重定位、关联符号及类型的信息。

<a id="a2bea1d7ef2a0c148cd9ae21386721f40"></a>

### `r_offset`

```c
elf32_addr elf32_rel::r_offset
```

在节内执行重定位的位置偏移量。

本数据类型文档由以下文件生成：

- `zephyr/llext/elf.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/llext/elf.h](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h_source.html)
- [elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)
- [elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_elf32_ehdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_elf32_rela_结构体.md)
