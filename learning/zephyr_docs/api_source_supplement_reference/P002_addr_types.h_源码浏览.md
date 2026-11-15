---
id: learning.zephyr-docs.api-source-supplement-reference.page-2
title: addr_types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/addr__types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_addr\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/addr__types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/addr__types_8h.html)。

## 2.1\_原始可见代码（Source Code）

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
<a id="aaddr__types_8h_html_a59897e9d2af1ab86597c1f4cfa994365"></a>
<a id="aaddr__types_8h_html_a96329c9b2410bdd79046e2529238a30f"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>

```c
/* Address types (virtual, physical, etc) definitions */

/*
 * Copyright (c) 2015 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ARCH_COMMON_ADDR_TYPES_H_
#define ZEPHYR_INCLUDE_ARCH_COMMON_ADDR_TYPES_H_

#ifndef _ASMLANGUAGE
typedef uintptr_t paddr_t;
typedef void *vaddr_t;
#endif

#endif /* ZEPHYR_INCLUDE_ARCH_COMMON_ADDR_TYPES_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

地址类型（Address types）的定义，例如虚拟地址、物理地址等。

### 注释 2：原第 3 行

版权（Copyright）：© 2015 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 17 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_COMMON_ADDR_TYPES_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/addr__types_8h.html)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [paddr_t](https://docs.zephyrproject.org/latest/doxygen/html/addr__types_8h.html#a59897e9d2af1ab86597c1f4cfa994365)
- [vaddr_t](https://docs.zephyrproject.org/latest/doxygen/html/addr__types_8h.html#a96329c9b2410bdd79046e2529238a30f)

---

[上一章](P001__types.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_addresses.h_源码浏览.md)
