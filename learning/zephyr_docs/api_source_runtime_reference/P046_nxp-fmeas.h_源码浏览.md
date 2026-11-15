---
id: learning.zephyr-docs.api-source-runtime-reference.page-46
title: nxp-fmeas.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp-fmeas_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_nxp-fmeas.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp-fmeas_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp-fmeas_8h.html)。

## 46.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>

```c
/*
 * SPDX-FileCopyrightText: 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MONITOR_NXP_FMEAS_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MONITOR_NXP_FMEAS_H_

#define NXP_FMEAS_PMUX_ID    0x700U
#define NXP_FMEAS_PMUX_SHIFT 20U

#define NXP_FMEAS_CONNECTION(sel) \
        (((sel) & ((1U << NXP_FMEAS_PMUX_SHIFT) - 1U)) | \
         (NXP_FMEAS_PMUX_ID << NXP_FMEAS_PMUX_SHIFT))

/* RT6xx (MIMXRT685S) - see RT600 fsl_inputmux_connections.h */
#define NXP_FMEAS_RT6XX_XTALIN          NXP_FMEAS_CONNECTION(0)
#define NXP_FMEAS_RT6XX_SFRO            NXP_FMEAS_CONNECTION(1)
#define NXP_FMEAS_RT6XX_FFRO            NXP_FMEAS_CONNECTION(2)
#define NXP_FMEAS_RT6XX_LPOSC          NXP_FMEAS_CONNECTION(3)
#define NXP_FMEAS_RT6XX_RTC_32KHZ      NXP_FMEAS_CONNECTION(4)
#define NXP_FMEAS_RT6XX_MAIN_SYS_CLK   NXP_FMEAS_CONNECTION(5)
#define NXP_FMEAS_RT6XX_FREQME_GPIO_CLK NXP_FMEAS_CONNECTION(6)

/* RT5xx (MIMXRT595S) - see RT500 fsl_inputmux_connections.h */
#define NXP_FMEAS_RT5XX_XTALIN          NXP_FMEAS_CONNECTION(0)
#define NXP_FMEAS_RT5XX_FRO_12M         NXP_FMEAS_CONNECTION(1)
#define NXP_FMEAS_RT5XX_FRO_192M        NXP_FMEAS_CONNECTION(2)
#define NXP_FMEAS_RT5XX_LPOSC          NXP_FMEAS_CONNECTION(3)
#define NXP_FMEAS_RT5XX_OSC_32KHZ      NXP_FMEAS_CONNECTION(4)
#define NXP_FMEAS_RT5XX_MAIN_SYS_CLK   NXP_FMEAS_CONNECTION(5)
#define NXP_FMEAS_RT5XX_FREQME_GPIO_CLK NXP_FMEAS_CONNECTION(6)
#define NXP_FMEAS_RT5XX_CLOCK_OUT      NXP_FMEAS_CONNECTION(11)

/* RW6xx (RW612) - see RW612 fsl_inputmux_connections.h */
#define NXP_FMEAS_RW6XX_SYSOSC          NXP_FMEAS_CONNECTION(0)
#define NXP_FMEAS_RW6XX_SFRO            NXP_FMEAS_CONNECTION(1)
#define NXP_FMEAS_RW6XX_FFRO            NXP_FMEAS_CONNECTION(2)
#define NXP_FMEAS_RW6XX_LPOSC          NXP_FMEAS_CONNECTION(3)
#define NXP_FMEAS_RW6XX_XTAL_32K       NXP_FMEAS_CONNECTION(4)
#define NXP_FMEAS_RW6XX_C0_FR_HCLK     NXP_FMEAS_CONNECTION(5)
#define NXP_FMEAS_RW6XX_FREQME_GPIO_CLK NXP_FMEAS_CONNECTION(6)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MONITOR_NXP_FMEAS_H_ */
```

## 46.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 40 行

RT6xx（MIMXRT685S）：参见 RT600 的 `fsl_inputmux_connections.h`。

### 注释 3：原第 56 行

RT5xx（MIMXRT595S）：参见 RT500 的 `fsl_inputmux_connections.h`。

### 注释 4：原第 74 行

RW6xx（RW612）：参见 RW612 的 `fsl_inputmux_connections.h`。

### 注释 5：原第 90 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MONITOR_NXP_FMEAS_H_`。

## 46.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp-fmeas_8h.html)

---

[上一章](P045_ppp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P047_parser_state.h_源码浏览.md)
