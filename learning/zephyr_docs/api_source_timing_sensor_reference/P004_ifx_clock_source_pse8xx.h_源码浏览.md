---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-4
title: ifx_clock_source_pse8xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__pse8xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_ifx\_clock\_source\_pse8xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__pse8xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P145_zephyr__dt-bindings__clock__ifx_clock_source_pse8xx.h_文件参考.md)。

## 4.1\_原始可见代码（Source Code）

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
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_PSE8XX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_PSE8XX_H_

/* Select the IHO as the output of the path mux */
#define IFX_CAT1_CLKPATH_IN_IHO 0

/* Select the EXT as the output of the path mux */
#define IFX_CAT1_CLKPATH_IN_EXT 1

/* Select the ECO as the output of the path mux */
#define IFX_CAT1_CLKPATH_IN_ECO 2

/* Select the IMO as the output of the path mux */
#define IFX_CAT1_CLKPATH_IN_IMO 3

/* Select the ALTHF0 as the output of the path mux */
#define IFX_CAT1_CLKPATH_IN_ALTHF0 4

/* Select the ALTHF1 as the output of the path mux */
#define IFX_CAT1_CLKPATH_IN_ALTHF1 5

/* Select the DSI MUX output as the output of the path mux */
#define IFX_CAT1_CLKPATH_IN_DSIMUX 7

/* Select a DSI signal (0 - 15) as the output of the DSI mux and path mux.
 * Make sure the DSI clock sources are available on used device.
 */
#define IFX_CAT1_CLKPATH_IN_DSI 0x100

/* Select the ILO (16) as the output of the DSI mux and path mux */
#define IFX_CAT1_CLKPATH_IN_ILO 0x110

/* Select the WCO (17) as the output of the DSI mux and path mux */
#define IFX_CAT1_CLKPATH_IN_WCO 0x111

/* Select the ALTLF (18) as the output of the DSI mux and path mux.
 * Make sure the ALTLF clock sources in available on used device.
 */
#define IFX_CAT1_CLKPATH_IN_ALTLF 0x112

/* Select the PILO (19) as the output of the DSI mux and path mux.
 * Make sure the PILO clock sources in available on used device.
 */
#define IFX_CAT1_CLKPATH_IN_PILO 0x113

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_PSE8XX_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

选择 IHO 作为路径多路选择器（path mux）的输出。

### 注释 3：原第 14 行

选择 EXT 作为路径多路选择器（path mux）的输出。

### 注释 4：原第 17 行

选择 ECO 作为路径多路选择器（path mux）的输出。

### 注释 5：原第 20 行

选择 IMO 作为路径多路选择器（path mux）的输出。

### 注释 6：原第 23 行

选择 ALTHF0 作为路径多路选择器（path mux）的输出。

### 注释 7：原第 26 行

选择 ALTHF1 作为路径多路选择器（path mux）的输出。

### 注释 8：原第 29 行

将 DSI 多路复用器（MUX）的输出选为路径多路复用器（Path mux）的输出。

### 注释 9：原第 32 行

选择 DSI 信号（0–15）作为 DSI 多路选择器和路径多路选择器的输出。请确保所用设备提供这些 DSI 时钟源。

### 注释 10：原第 37 行

选择 ILO（16）作为 DSI 多路选择器和路径多路选择器的输出。

### 注释 11：原第 40 行

选择 WCO（17）作为 DSI 多路选择器和路径多路选择器的输出。

### 注释 12：原第 43 行

选择 ALTLF（18）作为 DSI 多路选择器和路径多路选择器的输出。请确保所用设备提供 ALTLF 时钟源。

### 注释 13：原第 48 行

选择 PILO（19）作为 DSI 多路选择器和路径多路选择器的输出。请确保所用设备提供 PILO 时钟源。

### 注释 14：原第 53 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IFX_CLOCK_SOURCE_PSE8XX_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P145_zephyr__dt-bindings__clock__ifx_clock_source_pse8xx.h_文件参考.md)

---

[上一章](P003_cs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_interrupt_util.h_源码浏览.md)
