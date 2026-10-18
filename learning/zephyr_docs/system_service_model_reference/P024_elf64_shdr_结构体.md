---
id: learning.zephyr-docs.system-service-model-reference.page-24
title: elf64_shdr_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structelf64__shdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_elf64\_shdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structelf64__shdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

64位节头（Section Header）。

```c
#include <zephyr/llext/elf.h>
```

<a id="details"></a>

64位节头（Section Header）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_af58da5c7c3e7712c51396eb937e1e783"></a>

```c
elf64_word sh_name
```

相关声明：[elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)、[sh_name](#af58da5c7c3e7712c51396eb937e1e783)。

节头名称在节头字符串表中的索引。

<a id="r_adf7c73f78f13d52220246e1ae6f99129"></a>

```c
elf64_word sh_type
```

相关声明：[elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)、[sh_type](#adf7c73f78f13d52220246e1ae6f99129)。

节类型（Section type）。

<a id="r_abd91eb8261ee67e50232e3682dc43267"></a>

```c
elf64_xword sh_flags
```

相关声明：[elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)、[sh_flags](#abd91eb8261ee67e50232e3682dc43267)。

节头属性（Section header attributes）。

<a id="r_a58c125037ae69e35f1f18c3e7aeef222"></a>

```c
elf64_addr sh_addr
```

相关声明：[elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)、[sh_addr](#a58c125037ae69e35f1f18c3e7aeef222)。

节在映像中的地址。

<a id="r_a855b2f814e5b1127f3766ae44b1ded10"></a>

```c
elf64_off sh_offset
```

相关声明：[elf64_off](../llext/P012_ELF常量与类型.md#ga7f982d835a34713a84907873f9e058a9)、[sh_offset](#a855b2f814e5b1127f3766ae44b1ded10)。

节在 ELF 二进制文件中的位置，以字节计。

<a id="r_a283192781f8777274e0ed155b8caa52b"></a>

```c
elf64_xword sh_size
```

相关声明：[elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)、[sh_size](#a283192781f8777274e0ed155b8caa52b)。

节大小，单位为字节。

<a id="r_a437c734872924c69bf3ea02723bfb50c"></a>

```c
elf64_word sh_link
```

相关声明：[elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)、[sh_link](#a437c734872924c69bf3ea02723bfb50c)。

节头表链接索引（link index），具体含义取决于节类型。

<a id="r_ab2d5b6d2b41c4b956917d2206b804335"></a>

```c
elf64_word sh_info
```

相关声明：[elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)、[sh_info](#ab2d5b6d2b41c4b956917d2206b804335)。

节信息（Section info），具体含义取决于节类型。

<a id="r_a978b62673b2b26f9d6333f0a3ccd7cb2"></a>

```c
elf64_xword sh_addralign
```

相关声明：[elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)、[sh_addralign](#a978b62673b2b26f9d6333f0a3ccd7cb2)。

节地址对齐（alignment）。

<a id="r_a41f5b8340cd4cb90b14cba348684d73b"></a>

```c
elf64_xword sh_entsize
```

相关声明：[elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)、[sh_entsize](#a41f5b8340cd4cb90b14cba348684d73b)。

此节包含固定大小条目的表，每个条目大小为 `sh_entsize` 字节。

## 24.2\_详细说明（Detailed Documentation）

<a id="a58c125037ae69e35f1f18c3e7aeef222"></a>

### `sh_addr`

```c
elf64_addr elf64_shdr::sh_addr
```

节在映像中的地址。

<a id="a978b62673b2b26f9d6333f0a3ccd7cb2"></a>

### `sh_addralign`

```c
elf64_xword elf64_shdr::sh_addralign
```

节地址对齐（alignment）。

<a id="a41f5b8340cd4cb90b14cba348684d73b"></a>

### `sh_entsize`

```c
elf64_xword elf64_shdr::sh_entsize
```

此节包含固定大小条目的表，每个条目大小为 `sh_entsize` 字节。

<a id="abd91eb8261ee67e50232e3682dc43267"></a>

### `sh_flags`

```c
elf64_xword elf64_shdr::sh_flags
```

节头属性（Section header attributes）。

<a id="ab2d5b6d2b41c4b956917d2206b804335"></a>

### `sh_info`

```c
elf64_word elf64_shdr::sh_info
```

节信息（Section info），具体含义取决于节类型。

<a id="a437c734872924c69bf3ea02723bfb50c"></a>

### `sh_link`

```c
elf64_word elf64_shdr::sh_link
```

节头表链接索引（link index），具体含义取决于节类型。

<a id="af58da5c7c3e7712c51396eb937e1e783"></a>

### `sh_name`

```c
elf64_word elf64_shdr::sh_name
```

节头名称在节头字符串表中的索引。

<a id="a855b2f814e5b1127f3766ae44b1ded10"></a>

### `sh_offset`

```c
elf64_off elf64_shdr::sh_offset
```

节在 ELF 二进制文件中的位置，以字节计。

<a id="a283192781f8777274e0ed155b8caa52b"></a>

### `sh_size`

```c
elf64_xword elf64_shdr::sh_size
```

节大小，单位为字节。

<a id="adf7c73f78f13d52220246e1ae6f99129"></a>

### `sh_type`

```c
elf64_word elf64_shdr::sh_type
```

节类型（Section type）。

本数据类型文档由以下文件生成：

- `zephyr/llext/elf.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/llext/elf.h](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h_source.html)
- [elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)
- [elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)
- [elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)
- [elf64_off](../llext/P012_ELF常量与类型.md#ga7f982d835a34713a84907873f9e058a9)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_elf64_rela_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_elf64_sym_结构体.md)
