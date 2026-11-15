---
id: learning.zephyr-docs.llext.api-13
title: ELF检查API
kind: reference
status: maintained
domains: [zephyr, llext, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__llext__inspect__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_ELF检查API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__llext__inspect__apis.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 13.1\_概述

本页提供 `ELF` 检查接口（`ELF` Inspection APIs），用于查询扩展的节与内存区域。

## 13.2\_llext\_get\_region\_info()

<a id="gabef549f07291126f39b5065be3f73599"></a>
<a id="r_gabef549f07291126f39b5065be3f73599"></a>

```c
static inline int llext_get_region_info ( const struct llext_loader * ldr, const struct llext * ext, enum llext_mem region, const elf_shdr_t ** hdr, const void ** addr, size_t * size )
```

```c
#include <zephyr/llext/inspect.h>
```

取得指定扩展某个内存区域的信息。

取得扩展中某个区域的信息；区域由一组相似的节合并而成。对于不需要的信息，可把对应输出参数设为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ldr` | 加载器。 |
| `[in] ext` | 扩展。 |
| `[in] region` | 要查询的区域。 |
| `[out] hdr` | 保存区域头指针的变量。 |
| `[out] addr` | 保存区域加载地址（Load Address）的变量。 |
| `[out] size` | 保存区域大小的变量。 |

**返回（Returns）**：成功返回 0；区域无效时返回 -EINVAL。

## 13.3\_llext\_get\_section\_info()

<a id="ga23121962662f057da004ac1c527716e3"></a>
<a id="r_ga23121962662f057da004ac1c527716e3"></a>

```c
static inline int llext_get_section_info ( const struct llext_loader * ldr, const struct llext * ext, unsigned int shndx, const elf_shdr_t ** hdr, enum llext_mem * region, size_t * offset )
```

```c
#include <zephyr/llext/inspect.h>
```

取得指定扩展某个节的信息。

取得扩展中某个 `ELF` 节的信息。对于不需要的信息，可把对应输出参数设为 `NULL`。

要求加载扩展时设置 `llext_load_param::keep_section_info` 标志。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ldr` | 加载器。 |
| `[in] ext` | 扩展。 |
| `[in] shndx` | 节索引（Section Index）。 |
| `[out] hdr` | 保存节头指针的变量。 |
| `[out] region` | 保存该节所属区域的变量。 |
| `[out] offset` | 保存节在区域内偏移量的变量。 |

**返回（Returns）**：成功返回 0；节索引无效返回 -EINVAL；节数据不可用返回 -ENOTSUP。

## 13.4\_llext\_section\_shndx()

<a id="ga655023e915eb0ef60e76c0c1625c63c9"></a>
<a id="r_ga655023e915eb0ef60e76c0c1625c63c9"></a>

```c
int llext_section_shndx ( const struct llext_loader * ldr, const struct llext * ext, const char * section_name )
```

```c
#include <zephyr/llext/inspect.h>
```

取得指定名称的节的索引。

要求加载扩展时设置 `llext_load_param::keep_section_info` 标志。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ldr` | 加载器。 |
| `[in] ext` | 扩展。 |
| `[in] section_name` | 要查找的节名称。 |

**返回（Returns）**：成功返回节索引；未找到节返回 -ENOENT；节数据不可用返回 -ENOTSUP。

## 13.5\_源码对照与相关阅读

译注：本仓库的[inspect.h](../../../include/zephyr/llext/inspect.h)可用于跟踪声明与实现。此相对路径从本文位置解析，不绑定盘符或用户名；本仓库参照源码不自动等同于网页 latest 的版本。

[加载流程](P004_加载扩展.md) · [管理API](P011_扩展管理API.md) · [ELF检查接口](P013_ELF检查API.md) · [加载器上下文](P025_扩展加载器上下文.md) · [符号表](P028_符号表.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P012_ELF常量与类型.md) · [返回大纲](大纲.md) · [下一章](P014_ELF加载器API.md)
