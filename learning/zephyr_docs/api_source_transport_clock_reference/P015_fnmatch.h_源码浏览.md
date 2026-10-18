---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-15
title: fnmatch.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fnmatch_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_fnmatch.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fnmatch_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P113_zephyr__posix__fnmatch.h_文件参考.md)。

## 15.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="afnmatch_8h_html_a088b414f40eb0ce3dad9e5243816f68f"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>

```c
/* SPDX-License-Identifier: BSD-3-Clause */

/*    $NetBSD: fnmatch.h,v 1.12.50.1 2011/02/08 16:18:55 bouyer Exp $    */

/*-
 * Copyright (c) 1992, 1993
 *    The Regents of the University of California.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the University nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 *
 *    @(#)fnmatch.h    8.1 (Berkeley) 6/2/93
 */

#ifndef ZEPHYR_INCLUDE_POSIX_FNMATCH_H_
#define ZEPHYR_INCLUDE_POSIX_FNMATCH_H_

#define FNM_NOMATCH 1 /* Match failed. */
#define FNM_NOSYS   2 /* Function not implemented. */
#define FNM_NORES   3 /* Out of resources */

#define FNM_NOESCAPE    0x01 /* Disable backslash escaping. */
#define FNM_PATHNAME    0x02 /* Slash must be matched by slash. */
#define FNM_PERIOD      0x04 /* Period must be matched by period. */
#define FNM_CASEFOLD    0x08 /* Pattern is matched case-insensitive */
#define FNM_LEADING_DIR 0x10 /* Ignore /<tail> after Imatch. */

#ifdef __cplusplus
extern "C" {
#endif

int fnmatch(const char *pattern, const char *string, int flags);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_FNMATCH_H_ */
```

## 15.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`BSD-3-Clause`。

### 注释 2：原第 3 行

NetBSD 源文件版本标识：`$NetBSD: fnmatch.h,v 1.12.50.1 2011/02/08 16:18:55 bouyer Exp $`。

### 注释 3：原第 5 行

版权（Copyright）© 1992、1993 加利福尼亚大学董事会（The Regents of the University of California）。保留所有权利。

允许以源代码和二进制形式重新分发和使用本软件，无论是否修改，但必须满足以下条件：

1. 重新分发源代码时，必须保留上述版权声明、本条件列表以及以下免责声明。
2. 以二进制形式重新分发时，必须在随分发提供的文档和／或其他材料中重现上述版权声明、本条件列表以及以下免责声明。
3. 未经事先明确的书面许可，不得使用大学名称或其贡献者姓名，为基于本软件派生的产品背书或进行推广。

本软件由董事会和贡献者按“原样”（AS IS）提供，不提供任何明示或默示保证，包括但不限于适销性及特定用途适用性的默示保证。对于以任何方式因使用本软件而产生的任何直接、间接、附带、特殊、惩罚性或后果性损害（包括但不限于采购替代商品或服务、使用权损失、数据或利润损失，或业务中断），无论原因如何，也无论依据何种责任理论——合同责任、严格责任或侵权责任（包括疏忽或其他情形）——即使已被告知此类损害的可能性，董事会及贡献者也均不承担责任。

原文件版本标识：`@(#)fnmatch.h    8.1 (Berkeley) 6/2/93`。

### 注释 4：原第 39 行

匹配失败（match failed）。

### 注释 5：原第 40 行

函数未实现（Function Not Implemented）。

### 注释 6：原第 41 行

资源不足（out of resources）。

### 注释 7：原第 43 行

禁用反斜杠转义（backslash escaping）。

### 注释 8：原第 44 行

斜杠必须由斜杠匹配。

### 注释 9：原第 45 行

句点必须由句点匹配。

### 注释 10：原第 46 行

匹配模式时不区分大小写（case-insensitive）。

### 注释 11：原第 47 行

在匹配后忽略 `/<tail>`。译注：原文写作 `after Imatch`，此处按其匹配语境翻译，原始注释保留在代码中。

### 注释 12：原第 59 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_FNMATCH_H_`。

## 15.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P113_zephyr__posix__fnmatch.h_文件参考.md)
- [fnmatch](../api_file_reference/P113_zephyr__posix__fnmatch.h_文件参考.md#a088b414f40eb0ce3dad9e5243816f68f)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

---

[上一章](P014_esp32p4_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P016_gap.h_源码浏览.md)
