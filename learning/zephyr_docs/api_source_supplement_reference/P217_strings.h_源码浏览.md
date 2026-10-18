---
id: learning.zephyr-docs.api-source-supplement-reference.page-217
title: strings.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/strings_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第217章\_strings.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/strings_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/strings_8h.html)。

## 217.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="astrings_8h_html_a674b7f779fec84cb1a3be8222b5c381a"></a>

```c
/* strings.h */

/*
 * Copyright (c) 2014 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STRINGS_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STRINGS_H_

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

extern int strncasecmp(const char *s1, const char *s2, size_t n);

#ifdef __cplusplus
}
#endif

#endif  /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STRINGS_H_ */
```

## 217.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`strings.h` 头文件。

### 注释 2：原第 3 行

版权（Copyright）：© 2014 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 24 行

头文件保护宏（Header guard）标记：`ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STRINGS_H_`。

## 217.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/strings_8h.html)
- [strncasecmp](https://docs.zephyrproject.org/latest/doxygen/html/strings_8h.html#a674b7f779fec84cb1a3be8222b5c381a)

---

[上一章](P216_string.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P218_common.h_源码浏览.md)
