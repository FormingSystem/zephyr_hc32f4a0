---
id: learning.zephyr-docs.system-service-model-reference.page-21
title: elf64_ehdr_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structelf64__ehdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_elf64\_ehdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structelf64__ehdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

64位可执行与可链接格式（ELF）的文件头。

```c
#include <zephyr/llext/elf.h>
```

<a id="details"></a>

64位可执行与可链接格式（ELF）的文件头。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_acfc6d7c908c9a9864cca2eb0e5a2c023"></a>

```c
unsigned char e_ident [16]
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[e_ident](#acfc6d7c908c9a9864cca2eb0e5a2c023)。

标识可执行与可链接格式（ELF）二进制文件的魔数字符串（magic string）。

<a id="r_aa30814b4908ab8f0008f8b6a68686127"></a>

```c
elf64_half e_type
```

相关声明：[elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)、[e_type](#aa30814b4908ab8f0008f8b6a68686127)。

ELF 类型。

<a id="r_ac1c3b8c0f2b01d0edf07c0e3d1d8220b"></a>

```c
elf64_half e_machine
```

相关声明：[elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)、[e_machine](#ac1c3b8c0f2b01d0edf07c0e3d1d8220b)。

机器类型（Machine type）。

<a id="r_a8d406a8c636ad09b96af62001b9b1785"></a>

```c
elf64_word e_version
```

相关声明：[elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)、[e_version](#a8d406a8c636ad09b96af62001b9b1785)。

目标文件版本（Object file version）。

<a id="r_a26fa9b30280c40d71227cd8dc68cc042"></a>

```c
elf64_addr e_entry
```

相关声明：[elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)、[e_entry](#a26fa9b30280c40d71227cd8dc68cc042)。

入口的虚拟地址（virtual address）。

<a id="r_ab41df1d736aabf7b810339d579e51663"></a>

```c
elf64_off e_phoff
```

相关声明：[elf64_off](../llext/P012_ELF常量与类型.md#ga7f982d835a34713a84907873f9e058a9)、[e_phoff](#ab41df1d736aabf7b810339d579e51663)。

程序头表（program header table）偏移量。

<a id="r_a3566424cae4237c11dc781929e9d2396"></a>

```c
elf64_off e_shoff
```

相关声明：[elf64_off](../llext/P012_ELF常量与类型.md#ga7f982d835a34713a84907873f9e058a9)、[e_shoff](#a3566424cae4237c11dc781929e9d2396)。

节头表（section header table）偏移量。

<a id="r_a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9"></a>

```c
elf64_word e_flags
```

相关声明：[elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)、[e_flags](#a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9)。

处理器专用标志。

<a id="r_a7ee0e5959ca93262320c545a4ab11649"></a>

```c
elf64_half e_ehsize
```

相关声明：[elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)、[e_ehsize](#a7ee0e5959ca93262320c545a4ab11649)。

ELF 头部大小。

<a id="r_a688f9d25b4f2678f0e9a313a8c8cf074"></a>

```c
elf64_half e_phentsize
```

相关声明：[elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)、[e_phentsize](#a688f9d25b4f2678f0e9a313a8c8cf074)。

程序头大小。

<a id="r_a4a3b62575f891b59851b36f478e95c32"></a>

```c
elf64_half e_phnum
```

相关声明：[elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)、[e_phnum](#a4a3b62575f891b59851b36f478e95c32)。

程序头数量。

<a id="r_a419a672788fb33eaffc5f7eb7c9f9acd"></a>

```c
elf64_half e_shentsize
```

相关声明：[elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)、[e_shentsize](#a419a672788fb33eaffc5f7eb7c9f9acd)。

节头大小。

<a id="r_ad46c9c2047e61617d5d52394e9c42d65"></a>

```c
elf64_half e_shnum
```

相关声明：[elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)、[e_shnum](#ad46c9c2047e61617d5d52394e9c42d65)。

节头数量。

<a id="r_a6214fd0ea2f0d3e8151a304d5c4302b2"></a>

```c
elf64_half e_shstrndx
```

相关声明：[elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)、[e_shstrndx](#a6214fd0ea2f0d3e8151a304d5c4302b2)。

包含节头字符串表（section header string table）的节头。

## 21.2\_详细说明（Detailed Documentation）

<a id="a7ee0e5959ca93262320c545a4ab11649"></a>

### `e_ehsize`

```c
elf64_half elf64_ehdr::e_ehsize
```

ELF 头部大小。

<a id="a26fa9b30280c40d71227cd8dc68cc042"></a>

### `e_entry`

```c
elf64_addr elf64_ehdr::e_entry
```

入口的虚拟地址（virtual address）。

<a id="a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9"></a>

### `e_flags`

```c
elf64_word elf64_ehdr::e_flags
```

处理器专用标志。

<a id="acfc6d7c908c9a9864cca2eb0e5a2c023"></a>

### `e_ident`

```c
unsigned char elf64_ehdr::e_ident[16]
```

标识可执行与可链接格式（ELF）二进制文件的魔数字符串（magic string）。

<a id="ac1c3b8c0f2b01d0edf07c0e3d1d8220b"></a>

### `e_machine`

```c
elf64_half elf64_ehdr::e_machine
```

机器类型（Machine type）。

<a id="a688f9d25b4f2678f0e9a313a8c8cf074"></a>

### `e_phentsize`

```c
elf64_half elf64_ehdr::e_phentsize
```

程序头大小。

<a id="a4a3b62575f891b59851b36f478e95c32"></a>

### `e_phnum`

```c
elf64_half elf64_ehdr::e_phnum
```

程序头数量。

<a id="ab41df1d736aabf7b810339d579e51663"></a>

### `e_phoff`

```c
elf64_off elf64_ehdr::e_phoff
```

程序头表（program header table）偏移量。

<a id="a419a672788fb33eaffc5f7eb7c9f9acd"></a>

### `e_shentsize`

```c
elf64_half elf64_ehdr::e_shentsize
```

节头大小。

<a id="ad46c9c2047e61617d5d52394e9c42d65"></a>

### `e_shnum`

```c
elf64_half elf64_ehdr::e_shnum
```

节头数量。

<a id="a3566424cae4237c11dc781929e9d2396"></a>

### `e_shoff`

```c
elf64_off elf64_ehdr::e_shoff
```

节头表（section header table）偏移量。

<a id="a6214fd0ea2f0d3e8151a304d5c4302b2"></a>

### `e_shstrndx`

```c
elf64_half elf64_ehdr::e_shstrndx
```

包含节头字符串表（section header string table）的节头。

<a id="aa30814b4908ab8f0008f8b6a68686127"></a>

### `e_type`

```c
elf64_half elf64_ehdr::e_type
```

ELF 类型。

<a id="a8d406a8c636ad09b96af62001b9b1785"></a>

### `e_version`

```c
elf64_word elf64_ehdr::e_version
```

目标文件版本（Object file version）。

本数据类型文档由以下文件生成：

- `zephyr/llext/elf.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/llext/elf.h](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)
- [elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)
- [elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)
- [elf64_off](../llext/P012_ELF常量与类型.md#ga7f982d835a34713a84907873f9e058a9)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_elf32_sym_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_elf64_rel_结构体.md)
