---
id: learning.zephyr-docs.api-file-configuration-reference.page-45
title: zephyr__llext__loader.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/loader_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_zephyr\_\_llext\_\_loader.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/loader_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可链接可加载扩展（LLEXT）的ELF加载器上下文类型。

<a id="details"></a>

```c
#include <zephyr/llext/elf.h>
#include <stddef.h>
#include <zephyr/llext/llext.h>
```

查看此文件的源码。

可加载链接扩展 ELF 加载器上下文类型（LLEXT ELF Loader Context Types）。下列类型用于定义 `llext` 子系统使用的 ELF 加载器（ELF Loader）的上下文（Context）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 45.1\_数据结构（Data Structures）

<a id="r_llext_5Floader"></a>

```c
struct llext_loader
```

相关声明：[llext_loader](../llext/P025_扩展加载器上下文.md)。

可链接可加载扩展（Linkable Loadable Extension）的加载器上下文。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 45.2\_枚举（Enumerations）

<a id="r_ga8e04f364aef19cf45843cc97cc702f24"></a>

```c
enum llext_storage_type { LLEXT_STORAGE_TEMPORARY , LLEXT_STORAGE_PERSISTENT , LLEXT_STORAGE_WRITABLE }
```

相关声明：[llext_storage_type](../llext/P014_ELF加载器API.md#ga8e04f364aef19cf45843cc97cc702f24)、[LLEXT_STORAGE_TEMPORARY](../llext/P014_ELF加载器API.md#gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6)、[LLEXT_STORAGE_PERSISTENT](../llext/P014_ELF加载器API.md#gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0)、[LLEXT_STORAGE_WRITABLE](../llext/P014_ELF加载器API.md#gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b)。

待加载 ELF 数据（ELF Data）的存储类型（Storage Type）。


## 45.3\_原页交叉引用（Cross References）

- [zephyr/llext/elf.h](../api_source_reference/P221_elf.h_源码浏览.md)
- [zephyr/llext/llext.h](../llext/P017_扩展管理头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P100_loader.h_源码浏览.md)
- [llext_loader](../llext/P025_扩展加载器上下文.md)
- [llext_storage_type](../llext/P014_ELF加载器API.md#ga8e04f364aef19cf45843cc97cc702f24)
- [LLEXT_STORAGE_TEMPORARY](../llext/P014_ELF加载器API.md#gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6)
- [LLEXT_STORAGE_PERSISTENT](../llext/P014_ELF加载器API.md#gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0)
- [LLEXT_STORAGE_WRITABLE](../llext/P014_ELF加载器API.md#gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b)
- [llext](../llext/P020_扩展对象.md)

<a id="header-details"></a>

---

[上一章](P044_zephyr__input__input_pmw3610.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P046_zephyr__net__lwm2m_path.h_文件参考.md)
