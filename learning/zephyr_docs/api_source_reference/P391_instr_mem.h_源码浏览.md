---
id: learning.zephyr-docs.api-source-reference.page-391
title: instr_mem.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/instr__mem_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第391章\_instr\_mem.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/instr__mem_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/instr__mem_8h.html)。

## 391.1\_原始可见代码（Source Code）

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
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="agroup__instr__mem_html_ga03af01659004f2d96438b948f8c065a9"></a>
<a id="agroup__instr__mem_html_ga506986b790b95fca0423e4c47690b1fe"></a>
<a id="agroup__instr__mem_html_ga61c79df57849b7e914cd33e0de4316a3"></a>
<a id="agroup__instr__mem_html_gae80e1083bf80acaf0466d0bc2fe96bb4"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ARCH_COMMON_INSTR_MEM_H_
#define ZEPHYR_INCLUDE_ARCH_COMMON_INSTR_MEM_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/sys/util.h>


bool arch_is_instr_mem(const void *addr, size_t len);

void *arch_memset_instr(void *buf, int c, size_t n);

void *arch_memcpy_to_instr(void *d, const void *s, size_t n);

void *arch_memcpy_from_instr(void *d, const void *s, size_t n);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_ARCH_COMMON_INSTR_MEM_H_ */
```

## 391.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 82 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_COMMON_INSTR_MEM_H_`。

## 391.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/instr__mem_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [arch_is_instr_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html#ga61c79df57849b7e914cd33e0de4316a3)
- [arch_memset_instr](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html#gae80e1083bf80acaf0466d0bc2fe96bb4)
- [arch_memcpy_to_instr](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html#ga506986b790b95fca0423e4c47690b1fe)
- [arch_memcpy_from_instr](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html#ga03af01659004f2d96438b948f8c065a9)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P390_inst.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P392_intc_bcm283x.h_源码浏览.md)
