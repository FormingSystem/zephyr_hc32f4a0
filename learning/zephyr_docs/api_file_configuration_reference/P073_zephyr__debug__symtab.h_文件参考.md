---
id: learning.zephyr-docs.api-file-configuration-reference.page-73
title: zephyr__debug__symtab.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/symtab_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_zephyr\_\_debug\_\_symtab.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/symtab_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 73.1\_数据结构（Data Structures）

<a id="r_symtab_5Finfo"></a>

```c
struct symtab_info
```

相关声明：[symtab_info](../observability/P056_符号表信息结构.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 73.2\_函数（Functions）

<a id="r_ga2f1c4fa3cc113c2e5f47c5bbcd337e32"></a>

```c
const struct symtab_info * symtab_get (void)
```

相关声明：[symtab_info](../observability/P056_符号表信息结构.md)、[symtab_get](https://docs.zephyrproject.org/latest/doxygen/html/group__symtab__apis.html#ga2f1c4fa3cc113c2e5f47c5bbcd337e32)。

获取指向符号表（Symbol Table）的指针（Pointer）。

<a id="r_gac5927cf3f4e0bf3e1b27b397290e44c5"></a>

```c
const char * symtab_find_symbol_name (uintptr_t addr, uint32_t *offset)
```

相关声明：[symtab_find_symbol_name](https://docs.zephyrproject.org/latest/doxygen/html/group__symtab__apis.html#gac5927cf3f4e0bf3e1b27b397290e44c5)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使用二分查找（Binary Search）查找符号名（Symbol Name）。


## 73.3\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](../api_source_runtime_reference/P062_symtab.h_源码浏览.md)
- [symtab_info](../observability/P056_符号表信息结构.md)
- [symtab_get](https://docs.zephyrproject.org/latest/doxygen/html/group__symtab__apis.html#ga2f1c4fa3cc113c2e5f47c5bbcd337e32)
- [symtab_find_symbol_name](https://docs.zephyrproject.org/latest/doxygen/html/group__symtab__apis.html#gac5927cf3f4e0bf3e1b27b397290e44c5)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

---

[上一章](P072_zephyr__drivers__flash__stm32_flash_api_extensions.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P074_zephyr__drivers__led_strip__tlc5971.h_文件参考.md)
