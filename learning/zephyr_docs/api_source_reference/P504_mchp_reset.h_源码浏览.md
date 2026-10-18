---
id: learning.zephyr-docs.api-source-reference.page-504
title: mchp_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第504章\_mchp\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__reset_8h.html)。

## 504.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="amchp__rstc__g1_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef INCLUDE_ZEPHYR_DRIVERS_RESET_MCHP_RESET_H_
#define INCLUDE_ZEPHYR_DRIVERS_RESET_MCHP_RESET_H_

#if defined(CONFIG_RESET_MCHP_RSTC_G1)
#include "mchp_rstc_g1.h"
#endif

#endif /* INCLUDE_ZEPHYR_DRIVERS_RESET_MCHP_RESET_H_ */
```

## 504.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 20 行

头文件保护宏（Header guard）标记：`INCLUDE_ZEPHYR_DRIVERS_RESET_MCHP_RESET_H_`。

## 504.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__reset_8h.html)
- [mchp_rstc_g1.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__rstc__g1_8h.html)

---

[上一章](P503_mchp_pic32cz_ca_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P505_mchp_sam_pmc.h_源码浏览.md)
