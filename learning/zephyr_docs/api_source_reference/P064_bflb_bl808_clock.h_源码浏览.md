---
id: learning.zephyr-docs.api-source-reference.page-64
title: bflb_bl808_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl808__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_bflb\_bl808\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl808__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl808__clock_8h.html)。

## 64.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="abflb__clock__common_8h_html"></a>

```c
/*
 * Copyright The Zephyr Project Contributors
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_BFLB_BL808_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_BFLB_BL808_CLOCK_H_

#include "bflb_clock_common.h"


#define BL808_CLKID_CLK_ROOT    BFLB_CLKID_CLK_ROOT
#define BL808_CLKID_CLK_RC32M   BFLB_CLKID_CLK_RC32M
#define BL808_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
#define BL808_CLKID_CLK_BCLK    BFLB_CLKID_CLK_BCLK
#define BL808_CLKID_CLK_F32K    BFLB_CLKID_CLK_F32K
#define BL808_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
#define BL808_CLKID_CLK_RC32K   BFLB_CLKID_CLK_RC32K
#define BL808_CLKID_CLK_WIFIPLL (BFLB_CLKID_CLK_PRIVATE + 0)
#define BL808_CLKID_CLK_AUPLL   (BFLB_CLKID_CLK_PRIVATE + 1)
#define BL808_CLKID_CLK_CPUPLL  (BFLB_CLKID_CLK_PRIVATE + 2)
#define BL808_CLKID_CLK_160M    (BFLB_CLKID_CLK_PRIVATE + 3)
#define BL808_CLKID_CLK_UHSPLL  (BFLB_CLKID_CLK_PRIVATE + 4)

#define BL808_CPUPLL_ID_DIV1    0
#define BL808_AUPLL_ID_DIV1     1
#define BL808_WIFIPLL_ID_DIV3_4 2
#define BL808_WIFIPLL_ID_DIV1   3

#define BL808_WIFIPLL_TOP_FREQ DT_FREQ_M(320)
#define BL808_AUPLL_TOP_FREQ       442368000
#define BL808_AUPLL_TOP_FREQ_44K1  451584000

#define BL808_WIFIPLL_TOP_FREQ_OC1 DT_FREQ_M(480)
#define BL808_WIFIPLL_TOP_FREQ_OC2 DT_FREQ_M(640)

#define BL808_CPUPLL_TOP_FREQ DT_FREQ_M(480)

#define BL808_UHSPLL_TOP_FREQ DT_FREQ_M(2300)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_BFLB_BL808_CLOCK_H_ */
```

## 64.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 69 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_BFLB_BL808_CLOCK_H_`。

## 64.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl808__clock_8h.html)
- [bflb_clock_common.h](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html)

---

[上一章](P063_bflb_bl70xl_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P065_bflb_clock_common.h_源码浏览.md)
