---
id: learning.zephyr-docs.api-source-reference.page-59
title: bflb_bl60x_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl60x__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_bflb\_bl60x\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl60x__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl60x__clock_8h.html)。

## 59.1\_原始可见代码（Source Code）

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
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="abflb__clock__common_8h_html"></a>

```c
/*
 * Copyright (c) 2025-2026 MASSDRIVER EI (massdriver.space)
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_BFLB_BL60X_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_BFLB_BL60X_CLOCK_H_

#include "bflb_clock_common.h"


#define BL60X_CLKID_CLK_ROOT    BFLB_CLKID_CLK_ROOT
#define BL60X_CLKID_CLK_RC32M   BFLB_CLKID_CLK_RC32M
#define BL60X_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
#define BL60X_CLKID_CLK_BCLK    BFLB_CLKID_CLK_BCLK
#define BL60X_CLKID_CLK_F32K    BFLB_CLKID_CLK_F32K
#define BL60X_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
#define BL60X_CLKID_CLK_RC32K   BFLB_CLKID_CLK_RC32K
#define BL60X_CLKID_CLK_PLL     BFLB_CLKID_CLK_PRIVATE

#define BL60X_PLL_TOP_FREQ      (DT_FREQ_M(192))

#define BL60X_PLL_ID_DIV4       0
#define BL60X_PLL_ID_DIV5_8     1
#define BL60X_PLL_ID_DIV5_3     2
#define BL60X_PLL_ID_DIV1       3

#define BL60X_PLL_TOP_FREQ_OC1  (DT_FREQ_M(240))

#define BL60X_PLL_TOP_FREQ_OC2  (DT_FREQ_M(320))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_BFLB_BL60X_CLOCK_H_ */
```

## 59.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025-2026 MASSDRIVER EI (massdriver.space)。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 101 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_BFLB_BL60X_CLOCK_H_`。

## 59.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl60x__clock_8h.html)
- [bflb_clock_common.h](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html)

---

[上一章](P058_bee_clock_control.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P060_bflb_bl616cl_clock.h_源码浏览.md)
