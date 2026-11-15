---
id: learning.zephyr-docs.system-service-model-reference.page-16
title: elf32_ehdr_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structelf32__ehdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_elf32\_ehdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structelf32__ehdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

32位可执行与可链接格式（ELF）的文件头。

```c
#include <zephyr/llext/elf.h>
```

<a id="details"></a>

32位可执行与可链接格式（ELF）的文件头。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_acef0ea640d4fd75562b7412eaf8e2226"></a>

```c
unsigned char e_ident [16]
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[e_ident](#acef0ea640d4fd75562b7412eaf8e2226)。

标识可执行与可链接格式（ELF）二进制文件的魔数字符串（magic string）。

<a id="r_ae26a4d5cc90917ec13689060695833e5"></a>

```c
elf32_half e_type
```

相关声明：[elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)、[e_type](#ae26a4d5cc90917ec13689060695833e5)。

ELF 类型。

<a id="r_a09a134b6c6b711458673ddc8601af4c5"></a>

```c
elf32_half e_machine
```

相关声明：[elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)、[e_machine](#a09a134b6c6b711458673ddc8601af4c5)。

机器类型（Machine type）。

<a id="r_a4f73aa6711f379fb70a483e99d47f108"></a>

```c
elf32_word e_version
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[e_version](#a4f73aa6711f379fb70a483e99d47f108)。

目标文件版本（Object file version）。

<a id="r_a2322a1ac85ac7962cd05152588f8bf8f"></a>

```c
elf32_addr e_entry
```

相关声明：[elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)、[e_entry](#a2322a1ac85ac7962cd05152588f8bf8f)。

入口的虚拟地址（virtual address）。

<a id="r_af25dd95c6c2b2e8aeecdfb130ed4bfc6"></a>

```c
elf32_off e_phoff
```

相关声明：[elf32_off](../llext/P012_ELF常量与类型.md#gabb40eb5ffbe88010885da1c8c7b869e3)、[e_phoff](#af25dd95c6c2b2e8aeecdfb130ed4bfc6)。

程序头表（program header table）偏移量。

<a id="r_a085432a071a923e4fe1d3a4a3dfa665b"></a>

```c
elf32_off e_shoff
```

相关声明：[elf32_off](../llext/P012_ELF常量与类型.md#gabb40eb5ffbe88010885da1c8c7b869e3)、[e_shoff](#a085432a071a923e4fe1d3a4a3dfa665b)。

节头表（section header table）偏移量。

<a id="r_a1533636f5162a1f5a6e501a4129a5954"></a>

```c
elf32_word e_flags
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[e_flags](#a1533636f5162a1f5a6e501a4129a5954)。

处理器专用标志。

<a id="r_a33698f57f4f73a4f7659633fc11114fb"></a>

```c
elf32_half e_ehsize
```

相关声明：[elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)、[e_ehsize](#a33698f57f4f73a4f7659633fc11114fb)。

ELF 头部大小。

<a id="r_a0deea8c06b17aff924a86adf23206dd7"></a>

```c
elf32_half e_phentsize
```

相关声明：[elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)、[e_phentsize](#a0deea8c06b17aff924a86adf23206dd7)。

程序头数量。

<a id="r_a24ad42f294e548d54ff91ae9de5bb729"></a>

```c
elf32_half e_phnum
```

相关声明：[elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)、[e_phnum](#a24ad42f294e548d54ff91ae9de5bb729)。

程序头数量。

<a id="r_a2b8ae6d098c44146579dbe4c8e2d11c8"></a>

```c
elf32_half e_shentsize
```

相关声明：[elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)、[e_shentsize](#a2b8ae6d098c44146579dbe4c8e2d11c8)。

节头大小。

<a id="r_a5f795d38ed810bad582d88c35b474cbf"></a>

```c
elf32_half e_shnum
```

相关声明：[elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)、[e_shnum](#a5f795d38ed810bad582d88c35b474cbf)。

节头数量。

<a id="r_a4537e3831f136b81a7a0d6260ad497a6"></a>

```c
elf32_half e_shstrndx
```

相关声明：[elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)、[e_shstrndx](#a4537e3831f136b81a7a0d6260ad497a6)。

包含节头字符串表（section header string table）的节头。

## 16.2\_详细说明（Detailed Documentation）

<a id="a33698f57f4f73a4f7659633fc11114fb"></a>

### `e_ehsize`

```c
elf32_half elf32_ehdr::e_ehsize
```

ELF 头部大小。

<a id="a2322a1ac85ac7962cd05152588f8bf8f"></a>

### `e_entry`

```c
elf32_addr elf32_ehdr::e_entry
```

入口的虚拟地址（virtual address）。

<a id="a1533636f5162a1f5a6e501a4129a5954"></a>

### `e_flags`

```c
elf32_word elf32_ehdr::e_flags
```

处理器专用标志。

<a id="acef0ea640d4fd75562b7412eaf8e2226"></a>

### `e_ident`

```c
unsigned char elf32_ehdr::e_ident[16]
```

标识可执行与可链接格式（ELF）二进制文件的魔数字符串（magic string）。

<a id="a09a134b6c6b711458673ddc8601af4c5"></a>

### `e_machine`

```c
elf32_half elf32_ehdr::e_machine
```

机器类型（Machine type）。

<a id="a0deea8c06b17aff924a86adf23206dd7"></a>

### `e_phentsize`

```c
elf32_half elf32_ehdr::e_phentsize
```

程序头数量。

<a id="a24ad42f294e548d54ff91ae9de5bb729"></a>

### `e_phnum`

```c
elf32_half elf32_ehdr::e_phnum
```

程序头数量。

<a id="af25dd95c6c2b2e8aeecdfb130ed4bfc6"></a>

### `e_phoff`

```c
elf32_off elf32_ehdr::e_phoff
```

程序头表（program header table）偏移量。

<a id="a2b8ae6d098c44146579dbe4c8e2d11c8"></a>

### `e_shentsize`

```c
elf32_half elf32_ehdr::e_shentsize
```

节头大小。

<a id="a5f795d38ed810bad582d88c35b474cbf"></a>

### `e_shnum`

```c
elf32_half elf32_ehdr::e_shnum
```

节头数量。

<a id="a085432a071a923e4fe1d3a4a3dfa665b"></a>

### `e_shoff`

```c
elf32_off elf32_ehdr::e_shoff
```

节头表（section header table）偏移量。

<a id="a4537e3831f136b81a7a0d6260ad497a6"></a>

### `e_shstrndx`

```c
elf32_half elf32_ehdr::e_shstrndx
```

包含节头字符串表（section header string table）的节头。

<a id="ae26a4d5cc90917ec13689060695833e5"></a>

### `e_type`

```c
elf32_half elf32_ehdr::e_type
```

ELF 类型。

<a id="a4f73aa6711f379fb70a483e99d47f108"></a>

### `e_version`

```c
elf32_word elf32_ehdr::e_version
```

目标文件版本（Object file version）。

本数据类型文档由以下文件生成：

- `zephyr/llext/elf.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/llext/elf.h](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [elf32_half](../llext/P012_ELF常量与类型.md#ga141d58f50804ef53e0d9bd13fcb36424)
- [elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)
- [elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)
- [elf32_off](../llext/P012_ELF常量与类型.md#gabb40eb5ffbe88010885da1c8c7b869e3)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_ec_host_cmd_tx_buf_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_elf32_rel_结构体.md)
