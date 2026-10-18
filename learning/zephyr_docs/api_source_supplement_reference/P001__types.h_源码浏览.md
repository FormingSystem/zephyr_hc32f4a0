---
id: learning.zephyr-docs.api-source-supplement-reference.page-1
title: _types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/__types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/__types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/__types_8h.html)。

## 1.1\_原始可见代码（Source Code）

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
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>

```c
/*
 * Copyright (c) 2019 Peter Bigot Consulting, LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/* Common header used to define underlying types for typedefs that
 * must appear in multiple headers independently.
 */
#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SYS_XTYPES_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SYS_XTYPES_H_

#include <stdint.h>

typedef int64_t _TIME_T_;
typedef int32_t _SUSECONDS_T_;

#endif /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SYS_XTYPES_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Peter Bigot Consulting, LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 7 行

公共头文件，用于定义底层类型，供必须在多个头文件中独立出现的类型别名（typedef）使用。

### 注释 3：原第 18 行

头文件保护宏（Header guard）标记：`ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SYS_XTYPES_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/__types_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)

---

[返回大纲](大纲.md) · [下一章](P002_addr_types.h_源码浏览.md)
