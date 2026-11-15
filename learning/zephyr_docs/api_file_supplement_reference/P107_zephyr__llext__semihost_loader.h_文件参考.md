---
id: learning.zephyr-docs.api-file-supplement-reference.page-107
title: zephyr__llext__semihost_loader.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/semihost__loader_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第107章\_zephyr\_\_llext\_\_semihost\_loader.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/semihost__loader_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可链接可加载扩展（LLEXT）的半主机加载器（Semihost Loader）实现。

<a id="details"></a>

```c
#include <zephyr/llext/loader.h>
```

查看此文件的源码。

可链接可加载扩展（LLEXT）的半主机加载器（Semihost Loader）实现。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 107.1\_数据结构（Data Structures）

<a id="r_llext_5Fsemihost_5Floader"></a>

```c
struct llext_semihost_loader
```

相关声明：[llext_semihost_loader](../llext/P026_半主机加载器.md)。

通过半主机机制（Semihosting）读取的llext_loader实现。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 107.2\_宏定义（Macros）

<a id="r_ga28c2ad64c0b54fdea6130916ca35aec5"></a>

```c
#define LLEXT_SEMIHOST_LOADER(_filename)
```

相关声明：[LLEXT_SEMIHOST_LOADER](../llext/P014_ELF加载器API.md#ga28c2ad64c0b54fdea6130916ca35aec5)。

`llext_semihost_loader` 结构体的初始化器（Initializer）。


## 107.3\_原页交叉引用（Cross References）

- [zephyr/llext/loader.h](../api_source_supplement_reference/P100_loader.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P755_semihost_loader.h_源码浏览.md)
- [llext_semihost_loader](../llext/P026_半主机加载器.md)
- [llext_loader](../llext/P025_扩展加载器上下文.md)
- [LLEXT_SEMIHOST_LOADER](../llext/P014_ELF加载器API.md#ga28c2ad64c0b54fdea6130916ca35aec5)

<a id="header-details"></a>

---

[上一章](P106_zephyr__linker__sections.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P108_zephyr__drivers__sensor__bd8lb600fs.h_文件参考.md)
