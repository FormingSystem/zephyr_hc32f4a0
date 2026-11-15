---
id: learning.zephyr-docs.api-file-system-device-reference.page-50
title: zephyr__llext__symbol.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/symbol_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_zephyr\_\_llext\_\_symbol.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/symbol_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可链接可加载扩展（Linkable Loadable Extension）的符号定义。

<a id="details"></a>

```c
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>
#include <stddef.h>
#include <stdint.h>
```

查看此文件的源码。

可链接的可加载扩展（Linkable Loadable Extension）符号定义。本文件提供一组宏和结构体，用于在基础映像（base image）与扩展之间双向定义和导出符号，使二者能够正确链接。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 50.1\_数据结构（Data Structures）

<a id="r_llext_5Fconst_5Fsymbol"></a>

```c
struct llext_const_symbol
```

相关声明：[llext_const_symbol](../llext/P022_常量符号.md)。

常量符号（Constant Symbols）是不可更改的具名内存地址。

<a id="r_llext_5Fsymbol"></a>

```c
struct llext_symbol
```

相关声明：[llext_symbol](../llext/P027_动态符号.md)。

符号（Symbols）是具名内存地址。

<a id="r_llext_5Fsymtable"></a>

```c
struct llext_symtable
```

相关声明：[llext_symtable](../llext/P028_符号表.md)。

符号表（Symbol Table）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 50.2\_宏定义（Macros）

<a id="r_ga7ee2d88028ae89dee9bf4bf83274807f"></a>

```c
#define LL_EXTENSION_SYMBOL_NAMED(sym_ident, sym_name)
```

相关声明：[LL_EXTENSION_SYMBOL_NAMED](../llext/P015_导出符号API.md#ga7ee2d88028ae89dee9bf4bf83274807f)。

使用自定义名称，将符号从扩展导出到基础映像。

<a id="r_ga2e05a6082a3ee50fbc74e14a48056626"></a>

```c
#define LL_EXTENSION_SYMBOL(x)
```

相关声明：[LL_EXTENSION_SYMBOL](../llext/P015_导出符号API.md#ga2e05a6082a3ee50fbc74e14a48056626)。

将符号从扩展导出到基础映像。

<a id="r_ga9822b90952597e6acd993999a7228aa1"></a>

```c
#define EXPORT_SYMBOL_NAMED(sym_ident, sym_name)
```

相关声明：[EXPORT_SYMBOL_NAMED](../llext/P015_导出符号API.md#ga9822b90952597e6acd993999a7228aa1)。

使用自定义名称，从当前构建导出常量符号（constant symbol）。

<a id="r_ga0188531646d69e784eccf85bd4fb34aa"></a>

```c
#define EXPORT_SYMBOL(x)
```

相关声明：[EXPORT_SYMBOL](../llext/P015_导出符号API.md#ga0188531646d69e784eccf85bd4fb34aa)。

从当前构建导出常量符号。

<a id="r_ga2da450c08c6b3dc8ebcf2f9d3f783006"></a>

```c
#define EXPORT_GROUP_SYMBOL_NAMED(group, sym_ident, sym_name)
```

相关声明：[EXPORT_GROUP_SYMBOL_NAMED](../llext/P015_导出符号API.md#ga2da450c08c6b3dc8ebcf2f9d3f783006)、[group](../posix_system_model_reference/P003_group_结构体.md)。

使用自定义名称和分组导出常量符号。

<a id="r_gad7e83af3c134d5eaabd1e1fad6689947"></a>

```c
#define EXPORT_GROUP_SYMBOL(group, sym_ident)
```

相关声明：[EXPORT_GROUP_SYMBOL](../llext/P015_导出符号API.md#gad7e83af3c134d5eaabd1e1fad6689947)、[group](../posix_system_model_reference/P003_group_结构体.md)。

在自定义分组中导出常量符号。


## 50.3\_原页交叉引用（Cross References）

- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_transport_clock_reference/P025_symbol.h_源码浏览.md)
- [llext_const_symbol](../llext/P022_常量符号.md)
- [llext_symbol](../llext/P027_动态符号.md)
- [llext_symtable](../llext/P028_符号表.md)
- [LL_EXTENSION_SYMBOL_NAMED](../llext/P015_导出符号API.md#ga7ee2d88028ae89dee9bf4bf83274807f)
- [LL_EXTENSION_SYMBOL](../llext/P015_导出符号API.md#ga2e05a6082a3ee50fbc74e14a48056626)
- [EXPORT_SYMBOL_NAMED](../llext/P015_导出符号API.md#ga9822b90952597e6acd993999a7228aa1)
- [EXPORT_SYMBOL](../llext/P015_导出符号API.md#ga0188531646d69e784eccf85bd4fb34aa)
- [EXPORT_GROUP_SYMBOL_NAMED](../llext/P015_导出符号API.md#ga2da450c08c6b3dc8ebcf2f9d3f783006)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [EXPORT_GROUP_SYMBOL](../llext/P015_导出符号API.md#gad7e83af3c134d5eaabd1e1fad6689947)

<a id="header-details"></a>

---

[上一章](P049_zephyr__dt-bindings__sensor__stts22h.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P051_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__tc_util.h_文件参考.md)
