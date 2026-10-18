---
id: learning.zephyr-docs.api-source-configuration-reference.page-15
title: ctype.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_ctype.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html)。

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
<a id="foldopen00016"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="foldopen00021"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="actype_8h_html_a0152b6658f63acfdd96a9409d0142719"></a>
<a id="actype_8h_html_a05d9ca901946ee2f2078c351163dc015"></a>
<a id="actype_8h_html_a20359f43d3eb2382afa4efdeb3f66dcf"></a>
<a id="actype_8h_html_a5d4143d99c571ef986ffc4a88df64097"></a>
<a id="actype_8h_html_a7c84919af75ed5a47fab36e2fa13775f"></a>
<a id="actype_8h_html_a825ff84641e11035f0b6aa8f86eacbfd"></a>
<a id="actype_8h_html_a9318513eb3136e55002d65bf602f74a7"></a>
<a id="actype_8h_html_a9ad6bca8b20d91ab6ee00b58d8c46475"></a>
<a id="actype_8h_html_ab14b97a75cf7392a543f89b5530e0ad7"></a>
<a id="actype_8h_html_ab208778249f6c2cf8339e187e21e11bd"></a>
<a id="actype_8h_html_ab5088a2e14096e665c030d72508e2e9d"></a>
<a id="actype_8h_html_aba67c74e5652a4544dbb92a46704cca3"></a>
<a id="actype_8h_html_abfe63aca83a67be16cf7b8636260b018"></a>
<a id="actype_8h_html_ac4c06d14f1ed4d340b63aaeea1a830af"></a>

```c
/* ctype.h */

/*
 * Copyright (c) 2015 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_CTYPE_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_CTYPE_H_

#ifdef __cplusplus
extern "C" {
#endif

static inline int isupper(int a)
{
        return (('A' <= a) && (a <= 'Z'));
}

static inline int isalpha(int c)
{
        /* force to lowercase */
        c |= 32;

        return (('a' <= c) && (c <= 'z'));
}

static inline int isblank(int c)
{
        return ((c == ' ') || (c == '\t'));
}

static inline int isspace(int c)
{
        return ((c == ' ') || (('\t' <= c) && (c <= '\r')));
}

static inline int isgraph(int c)
{
        return ((' ' < c) && (c <= '~'));
}

static inline int isprint(int c)
{
        return ((' ' <= c) && (c <= '~'));
}

static inline int isdigit(int a)
{
        return (('0' <= a) && (a <= '9'));
}

static inline int islower(int c)
{
        return (('a' <= c) && (c <= 'z'));
}

static inline int isxdigit(int a)
{
        if (isdigit(a) != 0) {
                return 1;
        }

        /* force to lowercase */
        a |= 32;

        return (('a' <= a) && (a <= 'f'));
}

static inline int tolower(int chr)
{
        return (chr >= 'A' && chr <= 'Z') ? (chr + 32) : (chr);
}

static inline int toupper(int chr)
{
        return ((chr >= 'a' && chr <= 'z') ? (chr - 32) : (chr));
}

static inline int isalnum(int chr)
{
        return (isalpha(chr) || isdigit(chr));
}

static inline int ispunct(int c)
{
        return (isgraph(c) && !isalnum(c));
}

static inline int iscntrl(int c)
{
        return ((((unsigned int)c) <= 31U) || (((unsigned int)c) == 127U));
}

#ifdef __cplusplus
}
#endif

#endif  /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_CTYPE_H_ */
```

## 15.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`ctype.h` 头文件。

### 注释 2：原第 3 行

版权（Copyright）：© 2015 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 23 行

强制转换为小写。

### 注释 4：原第 65 行

强制转换为小写。

### 注释 5：原第 100 行

头文件保护宏（Header guard）标记：`ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_CTYPE_H_`。

## 15.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html)
- [isupper](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#a05d9ca901946ee2f2078c351163dc015)
- [isalpha](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#ab208778249f6c2cf8339e187e21e11bd)
- [isblank](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#a9ad6bca8b20d91ab6ee00b58d8c46475)
- [isspace](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#a9318513eb3136e55002d65bf602f74a7)
- [isgraph](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#a825ff84641e11035f0b6aa8f86eacbfd)
- [isprint](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#ab14b97a75cf7392a543f89b5530e0ad7)
- [isdigit](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#a7c84919af75ed5a47fab36e2fa13775f)
- [islower](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#a20359f43d3eb2382afa4efdeb3f66dcf)
- [isxdigit](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#a0152b6658f63acfdd96a9409d0142719)
- [tolower](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#ab5088a2e14096e665c030d72508e2e9d)
- [toupper](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#abfe63aca83a67be16cf7b8636260b018)
- [isalnum](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#ac4c06d14f1ed4d340b63aaeea1a830af)
- [ispunct](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#aba67c74e5652a4544dbb92a46704cca3)
- [iscntrl](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html#a5d4143d99c571ef986ffc4a88df64097)

---

[上一章](P014_csip.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P016_dfu_srv.h_源码浏览.md)
