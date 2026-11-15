---
id: learning.zephyr-docs.system-service-model-reference.page-23
title: elf64_rela_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structelf64__rela.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_elf64\_rela\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structelf64__rela.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

64位ELF中带加数（Addend）的重定位条目。

```c
#include <zephyr/llext/elf.h>
```

<a id="details"></a>

带加数（addend）的 64 位 ELF 重定位条目。此结构体保存描述待执行重定位的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_a5fd82462e8b9c0eeaf84a00bc2aae3a4"></a>

```c
elf64_addr r_offset
```

相关声明：[elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)、[r_offset](#a5fd82462e8b9c0eeaf84a00bc2aae3a4)。

在节内执行重定位的位置偏移量。

<a id="r_aa58223032a48222e420b36b2fc5f27ab"></a>

```c
elf64_xword r_info
```

相关声明：[elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)、[r_info](#aa58223032a48222e420b36b2fc5f27ab)。

有关重定位、关联符号及类型的信息。

<a id="r_a3eda7390faab39b1974174cc839cfb22"></a>

```c
elf64_sxword r_addend
```

相关声明：[elf64_sxword](../llext/P012_ELF常量与类型.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e)、[r_addend](#a3eda7390faab39b1974174cc839cfb22)。

要加到符号地址上的偏移量。

## 23.2\_详细说明（Detailed Documentation）

<a id="a3eda7390faab39b1974174cc839cfb22"></a>

### `r_addend`

```c
elf64_sxword elf64_rela::r_addend
```

要加到符号地址上的偏移量。

<a id="aa58223032a48222e420b36b2fc5f27ab"></a>

### `r_info`

```c
elf64_xword elf64_rela::r_info
```

有关重定位、关联符号及类型的信息。

<a id="a5fd82462e8b9c0eeaf84a00bc2aae3a4"></a>

### `r_offset`

```c
elf64_addr elf64_rela::r_offset
```

在节内执行重定位的位置偏移量。

本数据类型文档由以下文件生成：

- `zephyr/llext/elf.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/llext/elf.h](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h_source.html)
- [elf64_addr](../llext/P012_ELF常量与类型.md#ga42c555ace34b21c1773c9e59228e9929)
- [elf64_xword](../llext/P012_ELF常量与类型.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)
- [elf64_sxword](../llext/P012_ELF常量与类型.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_elf64_rel_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_elf64_shdr_结构体.md)
