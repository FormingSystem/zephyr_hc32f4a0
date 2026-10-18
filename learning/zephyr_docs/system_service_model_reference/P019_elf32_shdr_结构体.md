---
id: learning.zephyr-docs.system-service-model-reference.page-19
title: elf32_shdr_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structelf32__shdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_elf32\_shdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structelf32__shdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

32位节头（Section Header）。

```c
#include <zephyr/llext/elf.h>
```

<a id="details"></a>

32位节头（Section Header）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_a397da5153b2f7605b1ff1de6aefa6d72"></a>

```c
elf32_word sh_name
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[sh_name](#a397da5153b2f7605b1ff1de6aefa6d72)。

节头名称在节头字符串表中的索引。

<a id="r_a575fd441213a3a2c01a2b9f8d76ae91a"></a>

```c
elf32_word sh_type
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[sh_type](#a575fd441213a3a2c01a2b9f8d76ae91a)。

节类型（Section type）。

<a id="r_a812f8d63ce30897a2aafc8eecca004af"></a>

```c
elf32_word sh_flags
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[sh_flags](#a812f8d63ce30897a2aafc8eecca004af)。

节头属性（Section header attributes）。

<a id="r_a2f5302ddbc6ae2e7adc9d0747029ac07"></a>

```c
elf32_addr sh_addr
```

相关声明：[elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)、[sh_addr](#a2f5302ddbc6ae2e7adc9d0747029ac07)。

节在映像中的地址。

<a id="r_ac7185a5c368b86d7c5bde4261472d3ea"></a>

```c
elf32_off sh_offset
```

相关声明：[elf32_off](../llext/P012_ELF常量与类型.md#gabb40eb5ffbe88010885da1c8c7b869e3)、[sh_offset](#ac7185a5c368b86d7c5bde4261472d3ea)。

节在 ELF 二进制文件中的位置，以字节计。

<a id="r_a99ef99ad56321d429d78a0d51fa55bc5"></a>

```c
elf32_word sh_size
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[sh_size](#a99ef99ad56321d429d78a0d51fa55bc5)。

节大小，单位为字节。

<a id="r_afc854954cb010c23281293399a58c200"></a>

```c
elf32_word sh_link
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[sh_link](#afc854954cb010c23281293399a58c200)。

节头表链接索引（link index），具体含义取决于节类型。

<a id="r_aa01fa67d235a73d8f05a1082ff639825"></a>

```c
elf32_word sh_info
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[sh_info](#aa01fa67d235a73d8f05a1082ff639825)。

节信息（Section info），具体含义取决于节类型。

<a id="r_ab0d2f72391dd49af989bc4a96320e510"></a>

```c
elf32_word sh_addralign
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[sh_addralign](#ab0d2f72391dd49af989bc4a96320e510)。

节地址对齐（alignment）。

<a id="r_af97a639e2da493a81e104447e327b574"></a>

```c
elf32_word sh_entsize
```

相关声明：[elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)、[sh_entsize](#af97a639e2da493a81e104447e327b574)。

此节包含固定大小条目的表，每个条目大小为 `sh_entsize` 字节。

## 19.2\_详细说明（Detailed Documentation）

<a id="a2f5302ddbc6ae2e7adc9d0747029ac07"></a>

### `sh_addr`

```c
elf32_addr elf32_shdr::sh_addr
```

节在映像中的地址。

<a id="ab0d2f72391dd49af989bc4a96320e510"></a>

### `sh_addralign`

```c
elf32_word elf32_shdr::sh_addralign
```

节地址对齐（alignment）。

<a id="af97a639e2da493a81e104447e327b574"></a>

### `sh_entsize`

```c
elf32_word elf32_shdr::sh_entsize
```

此节包含固定大小条目的表，每个条目大小为 `sh_entsize` 字节。

<a id="a812f8d63ce30897a2aafc8eecca004af"></a>

### `sh_flags`

```c
elf32_word elf32_shdr::sh_flags
```

节头属性（Section header attributes）。

<a id="aa01fa67d235a73d8f05a1082ff639825"></a>

### `sh_info`

```c
elf32_word elf32_shdr::sh_info
```

节信息（Section info），具体含义取决于节类型。

<a id="afc854954cb010c23281293399a58c200"></a>

### `sh_link`

```c
elf32_word elf32_shdr::sh_link
```

节头表链接索引（link index），具体含义取决于节类型。

<a id="a397da5153b2f7605b1ff1de6aefa6d72"></a>

### `sh_name`

```c
elf32_word elf32_shdr::sh_name
```

节头名称在节头字符串表中的索引。

<a id="ac7185a5c368b86d7c5bde4261472d3ea"></a>

### `sh_offset`

```c
elf32_off elf32_shdr::sh_offset
```

节在 ELF 二进制文件中的位置，以字节计。

<a id="a99ef99ad56321d429d78a0d51fa55bc5"></a>

### `sh_size`

```c
elf32_word elf32_shdr::sh_size
```

节大小，单位为字节。

<a id="a575fd441213a3a2c01a2b9f8d76ae91a"></a>

### `sh_type`

```c
elf32_word elf32_shdr::sh_type
```

节类型（Section type）。

本数据类型文档由以下文件生成：

- `zephyr/llext/elf.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/llext/elf.h](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h_source.html)
- [elf32_word](../llext/P012_ELF常量与类型.md#gac786571f50a02299b19c1a16d658ea72)
- [elf32_addr](../llext/P012_ELF常量与类型.md#ga55f1dc601c95381307fddd5969969634)
- [elf32_off](../llext/P012_ELF常量与类型.md#gabb40eb5ffbe88010885da1c8c7b869e3)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_elf32_rela_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_elf32_sym_结构体.md)
