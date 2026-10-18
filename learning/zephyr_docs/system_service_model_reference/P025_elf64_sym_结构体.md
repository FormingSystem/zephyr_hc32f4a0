---
id: learning.zephyr-docs.system-service-model-reference.page-25
title: elf64_sym_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structelf64__sym.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_elf64\_sym\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structelf64__sym.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

64位符号表条目（Symbol Table Entry）。

```c
#include <zephyr/llext/elf.h>
```

<a id="details"></a>

64位符号表条目（Symbol Table Entry）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_aee1394841b7752ed58b47da46f83c0a5"></a>

```c
elf64_word st_name
```

相关声明：[elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)、[st_name](#aee1394841b7752ed58b47da46f83c0a5)。

符号名称，以符号字符串表中的索引表示。

<a id="r_a48d593f11ef3d04b1f5d46f92aaa9839"></a>

```c
unsigned char st_info
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[st_info](#a48d593f11ef3d04b1f5d46f92aaa9839)。

符号绑定（binding）及类型信息。

<a id="r_a47a54908caddb43875d6a167bec370c7"></a>

```c
unsigned char st_other
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[st_other](#a47a54908caddb43875d6a167bec370c7)。

符号可见性（visibility）。

<a id="r_a285d9d47f979f7c0a3ae9ed18408d191"></a>

```c
elf64_half st_shndx
```

相关声明：[elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)、[st_shndx](#a285d9d47f979f7c0a3ae9ed18408d191)。

符号关联的节，以节头索引表示。

<a id="r_a3037b0fbaf250e2e711ed5ad6b39fc88"></a>

```c
elf64_addr st_value
```

相关声明：[elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)、[st_value](#a3037b0fbaf250e2e711ed5ad6b39fc88)。

符号的值或位置。

<a id="r_a73ba49c8bee2c11229f48756dccea886"></a>

```c
elf64_xword st_size
```

相关声明：[elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)、[st_size](#a73ba49c8bee2c11229f48756dccea886)。

符号大小。

## 25.2\_详细说明（Detailed Documentation）

<a id="a48d593f11ef3d04b1f5d46f92aaa9839"></a>

### `st_info`

```c
unsigned char elf64_sym::st_info
```

符号绑定（binding）及类型信息。

<a id="aee1394841b7752ed58b47da46f83c0a5"></a>

### `st_name`

```c
elf64_word elf64_sym::st_name
```

符号名称，以符号字符串表中的索引表示。

<a id="a47a54908caddb43875d6a167bec370c7"></a>

### `st_other`

```c
unsigned char elf64_sym::st_other
```

符号可见性（visibility）。

<a id="a285d9d47f979f7c0a3ae9ed18408d191"></a>

### `st_shndx`

```c
elf64_half elf64_sym::st_shndx
```

符号关联的节，以节头索引表示。

<a id="a73ba49c8bee2c11229f48756dccea886"></a>

### `st_size`

```c
elf64_xword elf64_sym::st_size
```

符号大小。

<a id="a3037b0fbaf250e2e711ed5ad6b39fc88"></a>

### `st_value`

```c
elf64_addr elf64_sym::st_value
```

符号的值或位置。

本数据类型文档由以下文件生成：

- `zephyr/llext/elf.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/llext/elf.h](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h_source.html)
- [elf64_word](../llext/P012_ELF常量与类型.md#gaabf3a740e51b02fbaf40bedfba35e476)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [elf64_half](../llext/P012_ELF常量与类型.md#ga3358e1392fd861af8a7c8248519717a0)
- [elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)
- [elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_elf64_shdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_enum_mgmt_detail_output_结构体.md)
