---
id: learning.zephyr-docs.api-source-reference.page-617
title: nxp_clock_controller_sources.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__clock__controller__sources_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第617章\_nxp\_clock\_controller\_sources.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp__clock__controller__sources_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp__clock__controller__sources_8h.html)。

## 617.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="aclock__control_8h_html"></a>

```c
/*
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_NXP_CLOCK_CONTROLLER_SOURCES_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_NXP_CLOCK_CONTROLLER_SOURCES_H_

#include <zephyr/drivers/clock_control.h>


#if DT_NODE_HAS_COMPAT_STATUS(DT_NODELABEL(firc), nxp_firc, okay)
#define NXP_FIRC_DIV DT_ENUM_IDX(DT_NODELABEL(firc), firc_div)
#endif

#if DT_NODE_HAS_COMPAT_STATUS(DT_NODELABEL(fxosc), nxp_fxosc, okay)
#define NXP_FXOSC_FREQ DT_PROP(DT_NODELABEL(fxosc), freq)
#define NXP_FXOSC_WORKMODE                                                                         \
        (DT_ENUM_IDX(DT_NODELABEL(fxosc), workmode) == 0 ? kFXOSC_ModeCrystal : kFXOSC_ModeBypass)
#define NXP_FXOSC_DELAY     DT_PROP(DT_NODELABEL(fxosc), delay)
#define NXP_FXOSC_OVERDRIVE DT_PROP(DT_NODELABEL(fxosc), overdrive)
#endif

#if DT_NODE_HAS_COMPAT_STATUS(DT_NODELABEL(pll), nxp_plldig, okay)
#define NXP_PLL_WORKMODE       DT_ENUM_IDX(DT_NODELABEL(pll), workmode)
#define NXP_PLL_PREDIV         DT_PROP(DT_NODELABEL(pll), prediv)
#define NXP_PLL_POSTDIV        DT_PROP(DT_NODELABEL(pll), postdiv)
#define NXP_PLL_MULTIPLIER     DT_PROP(DT_NODELABEL(pll), multiplier)
#define NXP_PLL_FRACLOOPDIV    DT_PROP(DT_NODELABEL(pll), fracloopdiv)
#define NXP_PLL_STEPSIZE       DT_PROP(DT_NODELABEL(pll), stepsize)
#define NXP_PLL_STEPNUM        DT_PROP(DT_NODELABEL(pll), stepnum)
#define NXP_PLL_ACCURACY       DT_ENUM_IDX(DT_NODELABEL(pll), accuracy)
#define NXP_PLL_OUTDIV_POINTER DT_PROP(DT_NODELABEL(pll), outdiv)
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_NXP_CLOCK_CONTROLLER_SOURCES_H_ */
```

## 617.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 64 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_NXP_CLOCK_CONTROLLER_SOURCES_H_`。

## 617.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp__clock__controller__sources_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)

---

[上一章](P616_nxp_clock_control.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P618_nxp_enet.h_源码浏览.md)
