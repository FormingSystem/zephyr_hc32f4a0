---
id: learning.zephyr-docs.api-file-runtime-reference.page-75
title: zephyr__sys__word_granular_access.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/word__granular__access_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_zephyr\_\_sys\_\_word\_granular\_access.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/word__granular__access_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

按字粒度访问内存（Word Granular Access Memory）的公共API。

<a id="details"></a>

```c
#include <zephyr/sys/util.h>
```

查看此文件的源码。

按字粒度访问内存（Word Granular Access Memory）的公共API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 75.1\_函数（Functions）

<a id="r_gad4ed45c6f5a03556730b10945625879b"></a>

```c
void * sys_memset_word_granular_access (void *buf, int c, size_t n)
```

相关声明：[sys_memset_word_granular_access](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html#gad4ed45c6f5a03556730b10945625879b)。

在以字为访问粒度的内存（Word Granular Access Memory）中，对缓冲区执行内存填充（Memset）。

<a id="r_ga9834656071d5aa892b4de9b3d47183c8"></a>

```c
void * sys_memcpy_to_word_granular_access (void *d, const void *s, size_t n)
```

相关声明：[sys_memcpy_to_word_granular_access](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html#ga9834656071d5aa892b4de9b3d47183c8)。

将缓冲区内容复制（Memcpy）到以字为访问粒度的内存（Word Granular Access Memory）。

<a id="r_ga65d008216186bbcfa2bc39493bf42325"></a>

```c
void * sys_memcpy_from_word_granular_access (void *d, const void *s, size_t n)
```

相关声明：[sys_memcpy_from_word_granular_access](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html#ga65d008216186bbcfa2bc39493bf42325)。

从以字为访问粒度的内存（Word Granular Access Memory）复制（Memcpy）缓冲区内容。


## 75.2\_原页交叉引用（Cross References）

- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P243_word_granular_access.h_源码浏览.md)
- [sys_memset_word_granular_access](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html#gad4ed45c6f5a03556730b10945625879b)
- [sys_memcpy_to_word_granular_access](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html#ga9834656071d5aa892b4de9b3d47183c8)
- [sys_memcpy_from_word_granular_access](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html#ga65d008216186bbcfa2bc39493bf42325)

<a id="header-details"></a>

---

[上一章](P074_zephyr__drivers__sensor__veml60xx-common.h_文件参考.md) · [返回大纲](大纲.md)
