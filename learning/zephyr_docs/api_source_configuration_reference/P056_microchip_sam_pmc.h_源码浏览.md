---
id: learning.zephyr-docs.api-source-configuration-reference.page-56
title: microchip_sam_pmc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/microchip__sam__pmc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_microchip\_sam\_pmc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/microchip__sam__pmc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/microchip__sam__pmc_8h.html)。

## 56.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MICROCHIP_SAM_PMC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MICROCHIP_SAM_PMC_H_

#define PMC_TYPE_CORE           0
#define PMC_TYPE_SYSTEM         1
#define PMC_TYPE_PERIPHERAL     2
#define PMC_TYPE_GCK            3
#define PMC_TYPE_PROGRAMMABLE   4

#define PMC_SLOW                0
#define PMC_MCK                 1
#define PMC_UTMI                2
#define PMC_MAIN                3

/* SAMA7G5 */
#define PMC_CPUPLL              (PMC_MAIN + 1)
#define PMC_SYSPLL              (PMC_MAIN + 2)
#define PMC_DDRPLL              (PMC_MAIN + 3)
#define PMC_IMGPLL              (PMC_MAIN + 4)
#define PMC_BAUDPLL             (PMC_MAIN + 5)
#define PMC_AUDIOPMCPLL         (PMC_MAIN + 6)
#define PMC_AUDIOIOPLL          (PMC_MAIN + 7)
#define PMC_ETHPLL              (PMC_MAIN + 8)
#define PMC_CPU                 (PMC_MAIN + 9)
#define PMC_MCK1                (PMC_MAIN + 10)
#define UTMI1                   0
#define UTMI2                   1
#define UTMI3                   2

/* SAMA7D65 */
#define PMC_LVDSPLL             (PMC_MAIN + 12)
#define PMC_MCK3                (PMC_MAIN + 20)
#define PMC_MCK5                (PMC_MAIN + 21)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MICROCHIP_SAM_PMC_H_ */
```

## 56.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：(C) 2025 Microchip Technology Inc. and its subsidiaries。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 21 行

SAMA7G5。

### 注释 3：原第 36 行

SAMA7D65。

### 注释 4：原第 41 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MICROCHIP_SAM_PMC_H_`。

## 56.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/microchip__sam__pmc_8h.html)

---

[上一章](P055_mctp_i3c_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P057_mm.h_源码浏览.md)
