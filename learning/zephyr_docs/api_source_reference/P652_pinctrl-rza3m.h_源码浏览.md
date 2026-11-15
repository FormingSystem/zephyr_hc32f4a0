---
id: learning.zephyr-docs.api-source-reference.page-652
title: pinctrl-rza3m.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rza3m_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第652章\_pinctrl-rza3m.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rza3m_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rza3m_8h.html)。

## 652.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00019"></a>
<a id="l00061"></a>
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
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZA3M_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZA3M_H_




#define PORT_00 0x0F00
#define PORT_01 0x1000
#define PORT_02 0x1100
#define PORT_03 0x1200
#define PORT_04 0x1300
#define PORT_05 0x1400
#define PORT_06 0x1500
#define PORT_07 0x1600
#define PORT_08 0x1700
#define PORT_09 0x1800
#define PORT_10 0x1900
#define PORT_11 0x1A00
#define PORT_12 0x1B00
#define PORT_20 0x0000
#define PORT_21 0x0100
#define PORT_22 0x0300
#define PORT_23 0x0400


#define RZA_PINMUX(port, pin, func) (port | pin | (((func) - 1) << 4))


#define BSP_IO_NMI            0xFFFF0001
#define BSP_IO_TMS_SWDIO      0xFFFF0200
#define BSP_IO_SD0_CLK        0xFFFF0400
#define BSP_IO_QSPI0_SPCLK    0xFFFF0500
#define BSP_IO_QSPI0_IO0      0xFFFF0501
#define BSP_IO_QSPI0_IO1      0xFFFF0502
#define BSP_IO_QSPI0_SSL      0xFFFF0505
#define BSP_IO_WDTOVF_PERROUT 0xFFFF0600
#define BSP_IO_RIIC0_SDA      0xFFFF0700
#define BSP_IO_RIIC0_SCL      0xFFFF0701



#define RZA_FILNUM_4_STAGE  0
#define RZA_FILNUM_8_STAGE  1
#define RZA_FILNUM_12_STAGE 2
#define RZA_FILNUM_16_STAGE 3

#define RZA_FILCLKSEL_NOT_DIV   0
#define RZA_FILCLKSEL_DIV_9000  1
#define RZA_FILCLKSEL_DIV_18000 2
#define RZA_FILCLKSEL_DIV_36000 3


#define RZA_FILTER_SET(filnum, filclksel) ((((filnum) & 0x3) << 0x2) | ((filclksel) & 0x3))


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZA3M_H_ */
```

## 652.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 146 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZA3M_H_`。

## 652.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rza3m_8h.html)

---

[上一章](P651_pinctrl-rx-pfs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P653_pinctrl-rzg3e.h_源码浏览.md)
