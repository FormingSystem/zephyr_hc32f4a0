---
id: learning.zephyr-docs.api-file-supplement-reference.page-33
title: zephyr__llext__fs_loader.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fs__loader_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_zephyr\_\_llext\_\_fs\_loader.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fs__loader_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可链接可加载扩展（LLEXT）的文件系统加载器实现。

<a id="details"></a>

```c
#include <zephyr/llext/loader.h>
#include <zephyr/fs/fs.h>
```

查看此文件的源码。

可链接可加载扩展（LLEXT）的文件系统加载器实现。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 33.1\_数据结构（Data Structures）

<a id="r_llext_5Ffs_5Floader"></a>

```c
struct llext_fs_loader
```

相关声明：[llext_fs_loader](../llext/P023_文件系统加载器.md)。

从文件系统读取的llext_loader实现。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 33.2\_宏定义（Macros）

<a id="r_ga25a394fb7f7f93cfe3ab92d8ed4a6bff"></a>

```c
#define LLEXT_FS_LOADER(_filename)
```

相关声明：[LLEXT_FS_LOADER](../llext/P014_ELF加载器API.md#ga25a394fb7f7f93cfe3ab92d8ed4a6bff)。

`llext_fs_loader` 结构体的初始化器（Initializer）。


## 33.3\_原页交叉引用（Cross References）

- [zephyr/llext/loader.h](../api_source_supplement_reference/P100_loader.h_源码浏览.md)
- [zephyr/fs/fs.h](../api_source_supplement_reference/P074_fs.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P273_fs_loader.h_源码浏览.md)
- [llext_fs_loader](../llext/P023_文件系统加载器.md)
- [llext_loader](../llext/P025_扩展加载器上下文.md)
- [LLEXT_FS_LOADER](../llext/P014_ELF加载器API.md#ga25a394fb7f7f93cfe3ab92d8ed4a6bff)

<a id="header-details"></a>

---

[上一章](P032_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__fff_extensions.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P034_zephyr__drivers__clock_control__gd32.h_文件参考.md)
