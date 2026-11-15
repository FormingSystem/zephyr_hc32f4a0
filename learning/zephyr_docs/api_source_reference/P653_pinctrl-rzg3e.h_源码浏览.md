---
id: learning.zephyr-docs.api-source-reference.page-653
title: pinctrl-rzg3e.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzg3e_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第653章\_pinctrl-rzg3e.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzg3e_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzg3e_8h.html)。

## 653.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00020"></a>
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
<a id="l00050"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00085"></a>
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
<a id="l00097"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZG3E_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZG3E_H_



#define PORT_00 0x0000
#define PORT_01 0x0100
#define PORT_02 0x0200
#define PORT_03 0x0300
#define PORT_04 0x0400
#define PORT_05 0x0500
#define PORT_06 0x0600
#define PORT_07 0x0700
#define PORT_08 0x0800
#define PORT_10 0x0A00
#define PORT_11 0x0B00
#define PORT_12 0x0C00
#define PORT_13 0x0D00
#define PORT_14 0x0E00
#define PORT_15 0x0F00
#define PORT_16 0x1000
#define PORT_17 0x1100
#define PORT_19 0x1300
#define PORT_20 0x1400
#define PORT_21 0x1500
#define PORT_22 0x1600
#define PORT_28 0x1C00



#define BSP_IO_WDTUDFCA 0xFFFF0500
#define BSP_IO_WDTUDFCM 0xFFFF0501

#define BSP_IO_SCIF_RXD 0xFFFF0600
#define BSP_IO_SCIF_TXD 0xFFFF0601

#define BSP_IO_SD0CLK  0xFFFF0900
#define BSP_IO_SD0CMD  0xFFFF0901
#define BSP_IO_SD0RSTN 0xFFFF0902
#define BSP_IO_SD0PWEN 0xFFFF0903
#define BSP_IO_SD0IOVS 0xFFFF0904

#define BSP_IO_SD0DAT0 0xFFFF0A00
#define BSP_IO_SD0DAT1 0xFFFF0A01
#define BSP_IO_SD0DAT2 0xFFFF0A02
#define BSP_IO_SD0DAT3 0xFFFF0A03
#define BSP_IO_SD0DAT4 0xFFFF0A04
#define BSP_IO_SD0DAT5 0xFFFF0A05
#define BSP_IO_SD0DAT6 0xFFFF0A06
#define BSP_IO_SD0DAT7 0xFFFF0A07



#define RZG_FILNUM_4_STAGE  0
#define RZG_FILNUM_8_STAGE  1
#define RZG_FILNUM_12_STAGE 2
#define RZG_FILNUM_16_STAGE 3

#define RZG_FILCLKSEL_DIV_4   0
#define RZG_FILCLKSEL_DIV_32  1
#define RZG_FILCLKSEL_DIV_128 2
#define RZG_FILCLKSEL_DIV_256 3


#define RZG_PINMUX(port, pin, func) (port | pin | ((func) << 4))

#define RZG_FILTER_SET(filnum, filclksel) (((filnum) & 0x3) << 0x2) | (filclksel & 0x3)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZG3E_H_ */
```

## 653.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 125 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZG3E_H_`。

## 653.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzg3e_8h.html)

---

[上一章](P652_pinctrl-rza3m.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P654_pinctrl-rzn-common.h_源码浏览.md)
