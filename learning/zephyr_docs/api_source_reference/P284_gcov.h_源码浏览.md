---
id: learning.zephyr-docs.api-source-reference.page-284
title: gcov.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gcov_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第284章\_gcov.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gcov_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gcov_8h.html)。

## 284.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="agcov_8h_html_a05ec5d137639a269c6df6188caf7bbc8"></a>
<a id="agcov_8h_html_a3868770b5770d928f0c90584f5e66188"></a>
<a id="agcov_8h_html_a4112c617905e6881b552f641fbf3ff2f"></a>
<a id="agcov_8h_html_ac743263c4f10905987df4c67eafecc44"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DEBUG_GCOV_H_
#define ZEPHYR_INCLUDE_DEBUG_GCOV_H_

#if defined(CONFIG_COVERAGE_GCOV) || defined(__DOXYGEN__)

void gcov_coverage_dump(void);

void gcov_coverage_dump_tagged(const char *tag);

void gcov_coverage_semihost(void);

void gcov_static_init(void);

#else
static inline void gcov_coverage_dump(void) { }
static inline void gcov_coverage_dump_tagged(const char *tag) { (void)tag; }
static inline void gcov_static_init(void) { }

#endif  /* CONFIG_COVERAGE_GCOV */

#endif  /* ZEPHYR_INCLUDE_DEBUG_GCOV_H_ */
```

## 284.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 76 行

条件编译配置（Configuration）标记：`CONFIG_COVERAGE_GCOV`。

### 注释 3：原第 78 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DEBUG_GCOV_H_`。

## 284.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gcov_8h.html)
- [gcov_coverage_dump](https://docs.zephyrproject.org/latest/doxygen/html/gcov_8h.html#ac743263c4f10905987df4c67eafecc44)
- [gcov_coverage_dump_tagged](https://docs.zephyrproject.org/latest/doxygen/html/gcov_8h.html#a4112c617905e6881b552f641fbf3ff2f)
- [gcov_coverage_semihost](https://docs.zephyrproject.org/latest/doxygen/html/gcov_8h.html#a3868770b5770d928f0c90584f5e66188)
- [gcov_static_init](https://docs.zephyrproject.org/latest/doxygen/html/gcov_8h.html#a05ec5d137639a269c6df6188caf7bbc8)

---

[上一章](P283_gauge.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P285_gd32-clocks-common.h_源码浏览.md)
