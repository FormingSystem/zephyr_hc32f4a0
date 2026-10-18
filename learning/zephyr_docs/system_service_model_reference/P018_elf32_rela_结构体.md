---
id: learning.zephyr-docs.system-service-model-reference.page-18
title: elf32_rela_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structelf32__rela.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_elf32\_rela\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structelf32__rela.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

32位ELF中带加数（Addend）的重定位条目。

```c
#include <zephyr/llext/elf.h>
```

<a id="details"></a>

带加数（addend）的 32 位 ELF 重定位条目。此结构体保存描述待执行重定位的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_a4ef1961410f1b9ffea15615e03b3917b"></a>

```c
elf32_addr r_offset
```

相关声明：[elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)、[r_offset](#a4ef1961410f1b9ffea15615e03b3917b)。

在节内执行重定位的位置偏移量。

<a id="r_a4c3494d4b7abfec309895dff1891a466"></a>

```c
elf32_word r_info
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[r_info](#a4c3494d4b7abfec309895dff1891a466)。

有关重定位、关联符号及类型的信息。

<a id="r_a37fce330c497dba2ca15c69cc58b83b8"></a>

```c
elf32_sword r_addend
```

相关声明：[elf32_sword](../llext/P012_ELF常量与类型.md#ga1325c85290908b89a9c2b9bdd1aa2efd)、[r_addend](#a37fce330c497dba2ca15c69cc58b83b8)。

要加到符号地址上的偏移量。

## 18.2\_详细说明（Detailed Documentation）

<a id="a37fce330c497dba2ca15c69cc58b83b8"></a>

### `r_addend`

```c
elf32_sword elf32_rela::r_addend
```

要加到符号地址上的偏移量。

<a id="a4c3494d4b7abfec309895dff1891a466"></a>

### `r_info`

```c
elf32_word elf32_rela::r_info
```

有关重定位、关联符号及类型的信息。

<a id="a4ef1961410f1b9ffea15615e03b3917b"></a>

### `r_offset`

```c
elf32_addr elf32_rela::r_offset
```

在节内执行重定位的位置偏移量。

本数据类型文档由以下文件生成：

- `zephyr/llext/elf.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/llext/elf.h](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h_source.html)
- [elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)
- [elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)
- [elf32_sword](../llext/P012_ELF常量与类型.md#ga1325c85290908b89a9c2b9bdd1aa2efd)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_elf32_rel_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_elf32_shdr_结构体.md)
