---
id: learning.zephyr-docs.system-service-model-reference.page-20
title: elf32_sym_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structelf32__sym.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_elf32\_sym\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structelf32__sym.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

32位符号表条目（Symbol Table Entry）。

```c
#include <zephyr/llext/elf.h>
```

<a id="details"></a>

32位符号表条目（Symbol Table Entry）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_a14545ec8738f87d6ac8da1d4a601d024"></a>

```c
elf32_word st_name
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[st_name](#a14545ec8738f87d6ac8da1d4a601d024)。

符号名称，以符号字符串表中的索引表示。

<a id="r_a39b94d141bae73d0c1d8f6df5695ea2d"></a>

```c
elf32_addr st_value
```

相关声明：[elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)、[st_value](#a39b94d141bae73d0c1d8f6df5695ea2d)。

符号的值或位置。

<a id="r_aef3af325acfa8080431f06de9267c662"></a>

```c
elf32_word st_size
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[st_size](#aef3af325acfa8080431f06de9267c662)。

符号大小。

<a id="r_aeef86f71df370cf183e2d03afe4d8812"></a>

```c
unsigned char st_info
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[st_info](#aeef86f71df370cf183e2d03afe4d8812)。

符号绑定（binding）及类型信息。

<a id="r_a5ce8408912eda365e2e3246f81f98360"></a>

```c
unsigned char st_other
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[st_other](#a5ce8408912eda365e2e3246f81f98360)。

符号可见性（visibility）。

<a id="r_a03dbc7e19d4f2f9aac76bf99d218658b"></a>

```c
elf32_half st_shndx
```

相关声明：[elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)、[st_shndx](#a03dbc7e19d4f2f9aac76bf99d218658b)。

符号关联的节，以节头索引表示。

## 20.2\_详细说明（Detailed Documentation）

<a id="aeef86f71df370cf183e2d03afe4d8812"></a>

### `st_info`

```c
unsigned char elf32_sym::st_info
```

符号绑定（binding）及类型信息。

<a id="a14545ec8738f87d6ac8da1d4a601d024"></a>

### `st_name`

```c
elf32_word elf32_sym::st_name
```

符号名称，以符号字符串表中的索引表示。

<a id="a5ce8408912eda365e2e3246f81f98360"></a>

### `st_other`

```c
unsigned char elf32_sym::st_other
```

符号可见性（visibility）。

<a id="a03dbc7e19d4f2f9aac76bf99d218658b"></a>

### `st_shndx`

```c
elf32_half elf32_sym::st_shndx
```

符号关联的节，以节头索引表示。

<a id="aef3af325acfa8080431f06de9267c662"></a>

### `st_size`

```c
elf32_word elf32_sym::st_size
```

符号大小。

<a id="a39b94d141bae73d0c1d8f6df5695ea2d"></a>

### `st_value`

```c
elf32_addr elf32_sym::st_value
```

符号的值或位置。

本数据类型文档由以下文件生成：

- `zephyr/llext/elf.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/llext/elf.h](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h_source.html)
- [elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)
- [elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_elf32_shdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_elf64_ehdr_结构体.md)
