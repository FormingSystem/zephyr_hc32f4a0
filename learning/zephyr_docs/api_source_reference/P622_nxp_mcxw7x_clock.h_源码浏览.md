---
id: learning.zephyr-docs.api-source-reference.page-622
title: nxp_mcxw7x_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__mcxw7x__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第622章\_nxp\_mcxw7x\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp__mcxw7x__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp__mcxw7x__clock_8h.html)。

## 622.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00017"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00024"></a>
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
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00108"></a>
<a id="l00115"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00141"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="foldopen00163"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NXP_MCXW7X_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NXP_MCXW7X_CLOCK_H_


#define MCXW_CLK_OSC32K_DISABLE 0
#define MCXW_CLK_OSC32K_ENABLE  1
#define MCXW_CLK_OSC32K_BYPASS  3

#define MCXW_CLK_OSC32K_CAP_0PF  0
#define MCXW_CLK_OSC32K_CAP_2PF  1
#define MCXW_CLK_OSC32K_CAP_4PF  2
#define MCXW_CLK_OSC32K_CAP_6PF  3
#define MCXW_CLK_OSC32K_CAP_8PF  4
#define MCXW_CLK_OSC32K_CAP_10PF 5
#define MCXW_CLK_OSC32K_CAP_12PF 6
#define MCXW_CLK_OSC32K_CAP_14PF 7
#define MCXW_CLK_OSC32K_CAP_16PF 8
#define MCXW_CLK_OSC32K_CAP_18PF 9
#define MCXW_CLK_OSC32K_CAP_20PF 10
#define MCXW_CLK_OSC32K_CAP_22PF 11
#define MCXW_CLK_OSC32K_CAP_24PF 12
#define MCXW_CLK_OSC32K_CAP_26PF 13
#define MCXW_CLK_OSC32K_CAP_28PF 14
#define MCXW_CLK_OSC32K_CAP_30PF 15

#define MCXW_CLK_OSC32K_COARSE_RANGE0 0
#define MCXW_CLK_OSC32K_COARSE_RANGE1 1
#define MCXW_CLK_OSC32K_COARSE_RANGE2 2
#define MCXW_CLK_OSC32K_COARSE_RANGE3 3

#define MCXW_CLK_FIRC_DISABLE      0
#define MCXW_CLK_FIRC_ENABLE       1
#define MCXW_CLK_FIRC_ENABLE_IN_LP 2

#define MCXW_CLK_FIRC_RANGE_48MHZ  0
#define MCXW_CLK_FIRC_RANGE_64MHZ  1
#define MCXW_CLK_FIRC_RANGE_96MHZ  2
#define MCXW_CLK_FIRC_RANGE_192MHZ 3

#define MCXW_CLK_SYSTEM_CLK_SRC_SOSC 1
#define MCXW_CLK_SYSTEM_CLK_SRC_SIRC 2
#define MCXW_CLK_SYSTEM_CLK_SRC_FIRC 3
#define MCXW_CLK_SYSTEM_CLK_SRC_ROSC 4

#define MCXW_CLK_DIV_NONE  0
#define MCXW_CLK_DIV_BY_1  0
#define MCXW_CLK_DIV_BY_2  1
#define MCXW_CLK_DIV_BY_3  2
#define MCXW_CLK_DIV_BY_4  3
#define MCXW_CLK_DIV_BY_5  4
#define MCXW_CLK_DIV_BY_6  5
#define MCXW_CLK_DIV_BY_7  6
#define MCXW_CLK_DIV_BY_8  7
#define MCXW_CLK_DIV_BY_10 9
#define MCXW_CLK_DIV_BY_11 10
#define MCXW_CLK_DIV_BY_12 11
#define MCXW_CLK_DIV_BY_13 12
#define MCXW_CLK_DIV_BY_14 13
#define MCXW_CLK_DIV_BY_15 14
#define MCXW_CLK_DIV_BY_16 15

#define MCXW_CLK_IP_MUX_SLOW_CLK 1
#define MCXW_CLK_IP_MUX_FRO_6M   2
#define MCXW_CLK_IP_MUX_FRO_192M_DIV                                                               \
        3
#define MCXW_CLK_IP_MUX_SOSC         4
#define MCXW_CLK_IP_MUX_32K          5
#define MCXW_CLK_IP_MUX_FRO_200M_DIV 6
#define MCXW_CLK_IP_MUX_1M           7
#define MCXW_CLK_IP_MUX_NONE         0xFF

#define MCXW_CLK_CTRL_DISABLED 0
#define MCXW_CLK_CTRL_ENABLED  1U

#define MCXW_CLK_LP_STALL_ALLOWED 0U
#define MCXW_CLK_LP_NO_STALL      2U

#define MCXW_CLK_MODE_DISABLED (MCXW_CLK_CTRL_DISABLED)
#define MCXW_CLK_MODE_ENABLED_LP_STALL                                                             \
        (MCXW_CLK_CTRL_ENABLED | MCXW_CLK_LP_STALL_ALLOWED)
#define MCXW_CLK_MODE_ENABLED_LP_NO_STALL                                                          \
        (MCXW_CLK_CTRL_ENABLED | MCXW_CLK_LP_NO_STALL)


#define MCXW_CLOCK(mrcc_offset, clk_mux, clk_div, flag)                                            \
        ((((mrcc_offset) & 0xFFFF) << 16) | (((clk_mux) & 0xFF) << 8) | (((clk_div) & 0xF) << 4) | \
         (((flag) & 0xF)))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NXP_MCXW7X_CLOCK_H_ */
```

## 622.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 167 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NXP_MCXW7X_CLOCK_H_`。

## 622.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp__mcxw7x__clock_8h.html)

---

[上一章](P621_nxp_lp_flexcomm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P623_nxp_rw_pmu.h_源码浏览.md)
