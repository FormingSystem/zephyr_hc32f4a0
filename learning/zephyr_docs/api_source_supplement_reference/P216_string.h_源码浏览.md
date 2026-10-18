---
id: learning.zephyr-docs.api-source-supplement-reference.page-216
title: string.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/string_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第216章\_string.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/string_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)。

## 216.1\_原始可见代码（Source Code）

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
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aposix_2sys_2socket_8h_html_a66e3de379c18201b21c889035ec54864"></a>
<a id="astring_8h_html_a07f4a84c11c106e95c32b6ab509346ef"></a>
<a id="astring_8h_html_a080c6052ea267026d0baa316f8610b46"></a>
<a id="astring_8h_html_a0a3e4af1b88f5d51a32fe7dcbf753b38"></a>
<a id="astring_8h_html_a11bd144d7d44914099a3aeddf1c8567d"></a>
<a id="astring_8h_html_a22af6fcfed68749460181f2077c34813"></a>
<a id="astring_8h_html_a32dff100d3a0806b158b13bbe60710af"></a>
<a id="astring_8h_html_a4137694174d4ca2fad886a1db355015c"></a>
<a id="astring_8h_html_a4bc5f273980fb0e81e0fc7a4dd3de87e"></a>
<a id="astring_8h_html_a6d729a7b6396b8508060821c56f4adbc"></a>
<a id="astring_8h_html_a71a1afb093b0af8298df8a745b1b1f5c"></a>
<a id="astring_8h_html_a85c0f130f91a3121ee06207f42554572"></a>
<a id="astring_8h_html_a900a0edfa51f601d479244f7451cedd1"></a>
<a id="astring_8h_html_aa383452fe445bfae989358c9d7d96f4f"></a>
<a id="astring_8h_html_aa7003ae2e637e6eb92a4c5e7523848a5"></a>
<a id="astring_8h_html_ad7c16a2447154107d5ecd28434993443"></a>
<a id="astring_8h_html_ad8bfbfa1e4ad284ded921dd775735521"></a>
<a id="astring_8h_html_adef2d6284e392701fd4149b344188ceb"></a>
<a id="astring_8h_html_aeb6c449e5d77477c057abf00eaaf88fe"></a>
<a id="astring_8h_html_af0f01bffcd16daa9143f6014d10a25ad"></a>
<a id="astring_8h_html_af87bb1cdc3d71abcd9aa0bd6d36e50a8"></a>
<a id="astring_8h_html_afc92d2231e45d19988c7894aa2a07f0c"></a>
<a id="atoolchain_8h_html"></a>

```c
/* string.h */

/*
 * Copyright (c) 2014 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STRING_H_
#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STRING_H_

#include <stddef.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif

extern char  *strcpy(char *ZRESTRICT d, const char *ZRESTRICT s);
extern char  *strerror(int errnum);
extern int   strerror_r(int errnum, char *strerrbuf, size_t buflen);
extern char  *strncpy(char *ZRESTRICT d, const char *ZRESTRICT s,
                      size_t n);
extern char  *strchr(const char *s, int c);
extern char  *strrchr(const char *s, int c);
extern size_t strlen(const char *s);
extern size_t strnlen(const char *s, size_t maxlen);
extern int    strcmp(const char *s1, const char *s2);
extern int    strncmp(const char *s1, const char *s2, size_t n);
extern char  *strtok_r(char *str, const char *sep, char **state);
extern char *strcat(char *ZRESTRICT dest,
                    const char *ZRESTRICT src);
extern char  *strncat(char *ZRESTRICT dest, const char *ZRESTRICT src,
                      size_t n);
extern char *strstr(const char *s, const char *find);

extern size_t strspn(const char *s, const char *accept);
extern size_t strcspn(const char *s, const char *reject);

extern int    memcmp(const void *m1, const void *m2, size_t n);
extern void  *memmove(void *d, const void *s, size_t n);
extern void  *memcpy(void *ZRESTRICT d, const void *ZRESTRICT s,
                     size_t n);
extern void  *memset(void *buf, int c, size_t n);
extern void  *memchr(const void *s, int c, size_t n);

#ifdef __cplusplus
}
#endif

#endif  /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STRING_H_ */
```

## 216.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`string.h` 头文件。

### 注释 2：原第 3 行

版权（Copyright）：© 2014 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 51 行

头文件保护宏（Header guard）标记：`ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_STRING_H_`。

## 216.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [strcpy](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a6d729a7b6396b8508060821c56f4adbc)
- [strerror](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a4bc5f273980fb0e81e0fc7a4dd3de87e)
- [strerror_r](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a080c6052ea267026d0baa316f8610b46)
- [strncpy](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#aa7003ae2e637e6eb92a4c5e7523848a5)
- [strchr](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#ad7c16a2447154107d5ecd28434993443)
- [strrchr](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#af87bb1cdc3d71abcd9aa0bd6d36e50a8)
- [strlen](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#aa383452fe445bfae989358c9d7d96f4f)
- [strnlen](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#afc92d2231e45d19988c7894aa2a07f0c)
- [strcmp](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a11bd144d7d44914099a3aeddf1c8567d)
- [strncmp](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a07f4a84c11c106e95c32b6ab509346ef)
- [strtok_r](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a22af6fcfed68749460181f2077c34813)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [strcat](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a85c0f130f91a3121ee06207f42554572)
- [strncat](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a32dff100d3a0806b158b13bbe60710af)
- [strstr](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#adef2d6284e392701fd4149b344188ceb)
- [strspn](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a900a0edfa51f601d479244f7451cedd1)
- [accept](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a66e3de379c18201b21c889035ec54864)
- [strcspn](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#aeb6c449e5d77477c057abf00eaaf88fe)
- [memcmp](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#ad8bfbfa1e4ad284ded921dd775735521)
- [memmove](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a71a1afb093b0af8298df8a745b1b1f5c)
- [memcpy](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#af0f01bffcd16daa9143f6014d10a25ad)
- [memset](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a4137694174d4ca2fad886a1db355015c)
- [memchr](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a0a3e4af1b88f5d51a32fe7dcbf753b38)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P215_stm32wl3_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P217_strings.h_源码浏览.md)
