---
id: learning.zephyr-docs.api-source-supplement-reference.page-243
title: word_granular_access.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/word__granular__access_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第243章\_word\_granular\_access.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/word__granular__access_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/word__granular__access_8h.html)。

## 243.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00051"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="agroup__word__granular__access_html_ga65d008216186bbcfa2bc39493bf42325"></a>
<a id="agroup__word__granular__access_html_ga9834656071d5aa892b4de9b3d47183c8"></a>
<a id="agroup__word__granular__access_html_gad4ed45c6f5a03556730b10945625879b"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SYS_WORD_GRANULAR_ACCESS_H_
#define ZEPHYR_INCLUDE_SYS_WORD_GRANULAR_ACCESS_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/sys/util.h>



#ifndef __sys_mem_word_t_defined
#define __sys_mem_word_t_defined

typedef uintptr_t __attribute__((may_alias)) sys_mem_word_t;

#define Z_MEM_WORD_T_WIDTH __INTPTR_WIDTH__
#endif /* __sys_mem_word_t_defined */

BUILD_ASSERT(Z_MEM_WORD_T_WIDTH == 32, "Unsupported word width for access to "
                                       "word granular access memory");


void *sys_memset_word_granular_access(void *buf, int c, size_t n);

void *sys_memcpy_to_word_granular_access(void *d, const void *s, size_t n);

void *sys_memcpy_from_word_granular_access(void *d, const void *s, size_t n);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SYS_WORD_GRANULAR_ACCESS_H_ */
```

## 243.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 43 行

类型定义保护标记：`__sys_mem_word_t_defined`。

### 注释 3：原第 108 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SYS_WORD_GRANULAR_ACCESS_H_`。

## 243.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/word__granular__access_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [sys_memset_word_granular_access](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html#gad4ed45c6f5a03556730b10945625879b)
- [sys_memcpy_to_word_granular_access](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html#ga9834656071d5aa892b4de9b3d47183c8)
- [sys_memcpy_from_word_granular_access](https://docs.zephyrproject.org/latest/doxygen/html/group__word__granular__access.html#ga65d008216186bbcfa2bc39493bf42325)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P242_virtqueue.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P244_worldsemi_ws2812c.h_源码浏览.md)
