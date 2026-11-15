---
id: learning.zephyr-docs.api-file-service-reference.page-17
title: zephyr__llext__inspect.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/inspect_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_llext\_\_inspect.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/inspect_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可链接可加载扩展（LLEXT）的ELF检查例程。

<a id="details"></a>

```c
#include <stddef.h>
#include <zephyr/llext/llext.h>
#include <zephyr/llext/loader.h>
#include <zephyr/llext/llext_internal.h>
```

查看此文件的源码。

可加载链接扩展 ELF 检查例程（LLEXT ELF Inspection Routines）。本文件包含检查 ELF 文件内容的例程，供需要高级访问已加载扩展（Loaded Extension）之 ELF 文件结构（File Structures）的应用程序使用。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.1\_函数（Functions）

<a id="r_gabef549f07291126f39b5065be3f73599"></a>

```c
static int llext_get_region_info (const struct llext_loader *ldr, const struct llext *ext, enum llext_mem region, const elf_shdr_t **hdr, const void **addr, size_t *size)
```

相关声明：[llext_get_region_info](../llext/P013_ELF检查API.md#gabef549f07291126f39b5065be3f73599)、[llext_loader](../llext/P025_扩展加载器上下文.md)、[llext](../llext/P020_扩展对象.md)、[llext_mem](../llext/P011_扩展管理API.md#ga9258a6fe4a45aa5dd48c80c7aa07b953)、[elf_shdr_t](../llext/P012_ELF常量与类型.md#gab3695edd628cf868dc4f0d618f86bcbd)。

获取指定扩展（Extension）的内存区域信息（Memory Region Information）。

<a id="r_ga655023e915eb0ef60e76c0c1625c63c9"></a>

```c
int llext_section_shndx (const struct llext_loader *ldr, const struct llext *ext, const char *section_name)
```

相关声明：[llext_section_shndx](../llext/P013_ELF检查API.md#ga655023e915eb0ef60e76c0c1625c63c9)、[llext_loader](../llext/P025_扩展加载器上下文.md)、[llext](../llext/P020_扩展对象.md)。

获取具有指定名称的区段索引（Section Index）。

<a id="r_ga23121962662f057da004ac1c527716e3"></a>

```c
static int llext_get_section_info (const struct llext_loader *ldr, const struct llext *ext, unsigned int shndx, const elf_shdr_t **hdr, enum llext_mem *region, size_t *offset)
```

相关声明：[llext_get_section_info](../llext/P013_ELF检查API.md#ga23121962662f057da004ac1c527716e3)、[llext_loader](../llext/P025_扩展加载器上下文.md)、[llext](../llext/P020_扩展对象.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[elf_shdr_t](../llext/P012_ELF常量与类型.md#gab3695edd628cf868dc4f0d618f86bcbd)、[llext_mem](../llext/P011_扩展管理API.md#ga9258a6fe4a45aa5dd48c80c7aa07b953)。

获取指定扩展（Extension）的区段信息（Section Information）。


## 17.2\_原页交叉引用（Cross References）

- [zephyr/llext/llext.h](../llext/P017_扩展管理头文件源码.md)
- [zephyr/llext/loader.h](../api_source_supplement_reference/P100_loader.h_源码浏览.md)
- [zephyr/llext/llext_internal.h](../llext/P019_扩展内部头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P038_inspect.h_源码浏览.md)
- [llext_get_region_info](../llext/P013_ELF检查API.md#gabef549f07291126f39b5065be3f73599)
- [llext_loader](../llext/P025_扩展加载器上下文.md)
- [llext](../llext/P020_扩展对象.md)
- [llext_mem](../llext/P011_扩展管理API.md#ga9258a6fe4a45aa5dd48c80c7aa07b953)
- [elf_shdr_t](../llext/P012_ELF常量与类型.md#gab3695edd628cf868dc4f0d618f86bcbd)
- [llext_section_shndx](../llext/P013_ELF检查API.md#ga655023e915eb0ef60e76c0c1625c63c9)
- [llext_get_section_info](../llext/P013_ELF检查API.md#ga23121962662f057da004ac1c527716e3)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)

<a id="header-details"></a>

---

[上一章](P016_zephyr__input__input_nunchuk.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__arch__common__instr_mem.h_文件参考.md)
