---
id: learning.zephyr-docs.api-source-reference.page-342
title: ifx_clock_source_boards.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__boards_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第342章\_ifx\_clock\_source\_boards.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__boards_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__boards_8h.html)。

## 342.1\_原始可见代码（Source Code）

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
<a id="aifx__clock__source__psc3xx_8h_html"></a>
<a id="aifx__clock__source__pse8xx_8h_html"></a>
<a id="aifx__clock__source__psoc4xx_8h_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_BOARDS_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_BOARDS_H_

#if defined(CONFIG_SOC_SERIES_PSE84)
#include "ifx_clock_source_pse8xx.h"
#elif defined(CONFIG_SOC_SERIES_PSC3)
#include "ifx_clock_source_psc3xx.h"
#elif defined(CONFIG_SOC_FAMILY_INFINEON_PSOC4)
#include "ifx_clock_source_psoc4xx.h"
#endif

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_BOARDS_H_ */
```

## 342.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 19 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_BOARDS_H_`。

## 342.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__boards_8h.html)
- [ifx_clock_source_pse8xx.h](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__pse8xx_8h.html)
- [ifx_clock_source_psc3xx.h](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__psc3xx_8h.html)
- [ifx_clock_source_psoc4xx.h](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__psoc4xx_8h.html)

---

[上一章](P341_if.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P343_ifx_cyw20829.h_源码浏览.md)
