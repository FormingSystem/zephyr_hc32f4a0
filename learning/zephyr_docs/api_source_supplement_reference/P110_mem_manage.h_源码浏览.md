---
id: learning.zephyr-docs.api-source-supplement-reference.page-110
title: mem_manage.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mem__manage_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第110章\_mem\_manage.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mem__manage_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mem__manage_8h.html)。

## 110.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="agroup__memory__management_html_ga1a4b707eae142c8f871a198b865e3d16"></a>
<a id="agroup__memory__management_html_gaef71defc60c1d898d5ece56c6826a2e1"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>

```c
/*
 * Copyright (c) 2020 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SYS_MEM_MANAGE_H
#define ZEPHYR_INCLUDE_SYS_MEM_MANAGE_H


#ifndef _ASMLANGUAGE
#include <stdbool.h>
#include <stdint.h>

bool sys_mm_is_phys_addr_in_range(uintptr_t phys);

bool sys_mm_is_virt_addr_in_range(void *virt);


#endif /* !_ASMLANGUAGE */
#endif /* ZEPHYR_INCLUDE_SYS_MEM_MANAGE_H */
```

## 110.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 67 行

条件编译表达式：`!_ASMLANGUAGE`。

### 注释 3：原第 68 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SYS_MEM_MANAGE_H`。

## 110.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mem__manage_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [sys_mm_is_phys_addr_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__management.html#gaef71defc60c1d898d5ece56c6826a2e1)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [sys_mm_is_virt_addr_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__management.html#ga1a4b707eae142c8f871a198b865e3d16)

---

[上一章](P109_mdns_responder.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P111_method.h_源码浏览.md)
