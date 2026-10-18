---
id: learning.zephyr-docs.llext.api-15
title: 导出符号API
kind: reference
status: maintained
domains: [zephyr, llext, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__llext__symbols.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_导出符号API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__llext__symbols.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 15.1\_概述

本页定义导出符号（Exported Symbol）的宏及其关联数据结构。

## 15.2\_关联声明与说明

<a id="r_llext_5Fconst_5Fsymbol"></a>

```c
struct llext_const_symbol
```

常量符号是不可更改的具名内存地址。

[详细说明](P022_常量符号.md)。

<a id="r_llext_5Fsymbol"></a>

```c
struct llext_symbol
```

符号是具名内存地址。

[详细说明](P027_动态符号.md)。

<a id="r_llext_5Fsymtable"></a>

```c
struct llext_symtable
```

一个符号表。

[详细说明](P028_符号表.md)。

## 15.3\_EXPORT\_GROUP\_SYMBOL

<a id="gad7e83af3c134d5eaabd1e1fad6689947"></a>
<a id="r_gad7e83af3c134d5eaabd1e1fad6689947"></a>

```c
#define EXPORT_GROUP_SYMBOL( group, sym_ident )
```

展开值（Value）：

```c
EXPORT_GROUP_SYMBOL_NAMED(group, sym_ident, sym_ident)
```

```c
#include <zephyr/llext/symbol.h>
```

在自定义分组中导出常量符号（Constant Symbol）。

这是允许把符号放入自定义分组的 [`EXPORT_SYMBOL`](#ga0188531646d69e784eccf85bd4fb34aa) 版本。

未启用 `CONFIG_LLEXT` 时，此宏不执行任何操作。

未启用 `CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_{group}` 时，此宏不执行任何操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group` | 符号导出到的分组，必须使用大写名称。 |
| `sym_ident` | 要导出的符号。 |

## 15.4\_EXPORT\_GROUP\_SYMBOL\_NAMED

<a id="ga2da450c08c6b3dc8ebcf2f9d3f783006"></a>
<a id="r_ga2da450c08c6b3dc8ebcf2f9d3f783006"></a>

```c
#define EXPORT_GROUP_SYMBOL_NAMED( group, sym_ident, sym_name )
```

展开值（Value）：

```c
Z_EXPORT_SYMBOL_NAMED_IN_GROUP(group, sym_ident, sym_name)
```

```c
#include <zephyr/llext/symbol.h>
```

以自定义名称和分组导出常量符号。

这是允许把符号放入自定义分组的 [`EXPORT_SYMBOL_NAMED`](#ga9822b90952597e6acd993999a7228aa1) 版本。

未启用 `CONFIG_LLEXT` 时，此宏不执行任何操作。

未启用 `CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_{group}` 时，此宏不执行任何操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group` | 符号导出到的分组，必须使用大写名称。 |
| `sym_ident` | 要导出的符号。 |
| `sym_name` | 与符号关联的名称。 |

## 15.5\_EXPORT\_SYMBOL

<a id="ga0188531646d69e784eccf85bd4fb34aa"></a>
<a id="r_ga0188531646d69e784eccf85bd4fb34aa"></a>

```c
#define EXPORT_SYMBOL( x)
```

展开值（Value）：

```c
EXPORT_SYMBOL_NAMED(x, x)
```

```c
#include <zephyr/llext/symbol.h>
```

从当前构建导出常量符号。

按符号名接收一个符号（函数或对象），将其名称和地址加入符号表。根据当前构建类型，扩展或基础镜像（Base Image）可以引用该符号表。该符号属于 UNASSIGNED 分组。

未启用 `CONFIG_LLEXT` 时，此宏不执行任何操作。

未启用 `CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_UNASSIGNED` 时，此宏不执行任何操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 要导出的符号。 |

## 15.6\_EXPORT\_SYMBOL\_NAMED

<a id="ga9822b90952597e6acd993999a7228aa1"></a>
<a id="r_ga9822b90952597e6acd993999a7228aa1"></a>

```c
#define EXPORT_SYMBOL_NAMED( sym_ident, sym_name )
```

展开值（Value）：

```c
Z_EXPORT_SYMBOL_NAMED_IN_GROUP(UNASSIGNED, sym_ident, sym_name)
```

```c
#include <zephyr/llext/symbol.h>
```

从当前构建以自定义名称导出常量符号。

这是允许为导出符号指定自定义名称的 [`EXPORT_SYMBOL`](#ga0188531646d69e784eccf85bd4fb34aa) 版本。该符号属于 UNASSIGNED 分组。

未启用 `CONFIG_LLEXT` 时，此宏不执行任何操作。

未启用 `CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_UNASSIGNED` 时，此宏不执行任何操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sym_ident` | 要导出的符号。 |
| `sym_name` | 与符号关联的名称。 |

## 15.7\_LL\_EXTENSION\_SYMBOL

<a id="ga2e05a6082a3ee50fbc74e14a48056626"></a>
<a id="r_ga2e05a6082a3ee50fbc74e14a48056626"></a>

```c
#define LL_EXTENSION_SYMBOL( x)
```

展开值（Value）：

```c
Z_LL_EXTENSION_SYMBOL_NAMED(x, x)
```

```c
#include <zephyr/llext/symbol.h>
```

从扩展向基础镜像导出符号。

扩展可用此宏将符号（函数或对象）加入扩展的导出符号表，以供基础镜像引用。

当前构建不是扩展时，此宏不执行任何操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 要向基础镜像导出的扩展符号。 |

## 15.8\_LL\_EXTENSION\_SYMBOL\_NAMED

<a id="ga7ee2d88028ae89dee9bf4bf83274807f"></a>
<a id="r_ga7ee2d88028ae89dee9bf4bf83274807f"></a>

```c
#define LL_EXTENSION_SYMBOL_NAMED( sym_ident, sym_name )
```

展开值（Value）：

```c
Z_LL_EXTENSION_SYMBOL_NAMED(sym_ident, sym_name)
```

```c
#include <zephyr/llext/symbol.h>
```

以自定义名称从扩展向基础镜像导出符号。

这是允许为导出符号指定自定义名称的 [`LL_EXTENSION_SYMBOL`](#ga2e05a6082a3ee50fbc74e14a48056626) 版本。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sym_ident` | 要向基础镜像导出的扩展符号。 |
| `sym_name` | 与符号关联的名称。 |

## 15.9\_源码对照与相关阅读

译注：本仓库的[symbol.h](../../../include/zephyr/llext/symbol.h)可用于跟踪声明与实现。此相对路径从本文位置解析，不绑定盘符或用户名；本仓库参照源码不自动等同于网页 latest 的版本。

[加载流程](P004_加载扩展.md) · [管理API](P011_扩展管理API.md) · [ELF检查接口](P013_ELF检查API.md) · [加载器上下文](P025_扩展加载器上下文.md) · [符号表](P028_符号表.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__llext__symbols_html_ga2da450c08c6b3dc8ebcf2f9d3f783006"></a>
<a id="astructgroup_html"></a>
<a id="agroup__llext__symbols_html_ga9822b90952597e6acd993999a7228aa1"></a>

[上一章](P014_ELF加载器API.md) · [返回大纲](大纲.md) · [下一章](P016_扩展管理头文件.md)
