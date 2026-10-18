---
id: learning.zephyr-docs.api-source-reference.page-650
title: pinctrl-ra.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-ra_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第650章\_pinctrl-ra.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-ra_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-ra_8h.html)。

## 650.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
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
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00151"></a>

```c
/*
 * Copyright (c) 2024-2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RA_H__
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RA_H__




#define RA_PORT_NUM_POS  0
#define RA_PORT_NUM_MASK 0xf

#define RA_PIN_NUM_POS  4
#define RA_PIN_NUM_MASK 0xf


#define RA_PSEL_HIZ_JTAG_SWD 0x0
#define RA_PSEL_ADC          0x0
#define RA_PSEL_DAC          0x0
#define RA_PSEL_ACMPHS       0x0
#define RA_PSEL_AGT          0x1
#define RA_PSEL_GPT0         0x2
#define RA_PSEL_GPT1         0x3
#define RA_PSEL_SCI_0        0x4
#define RA_PSEL_SCI_2        0x4
#define RA_PSEL_SCI_4        0x4
#define RA_PSEL_SCI_6        0x4
#define RA_PSEL_SCI_8        0x4
#define RA_PSEL_SCI_1        0x5
#define RA_PSEL_SCI_3        0x5
#define RA_PSEL_SCI_5        0x5
#define RA_PSEL_SCI_7        0x5
#define RA_PSEL_SCI_9        0x5
#define RA_PSEL_SPI          0x6
#define RA_PSEL_I2C          0x7
#define RA_PSEL_I3C          0x7
#define RA_PSEL_CLKOUT_RTC   0x9
#define RA_PSEL_ACMPHS_VCOUT 0x9
#define RA_PSEL_ETHPHYCLK    0x9
#define RA_PSEL_CAC_ADC      0xa
#define RA_PSEL_CAC_DAC      0xa
#define RA_PSEL_BUS          0xb
#define RA_PSEL_CANFD        0x10
#define RA_PSEL_QSPI         0x11
#define RA_PSEL_SSIE         0x12
#define RA_PSEL_USBFS        0x13
#define RA_PSEL_USBHS        0x14
#define RA_PSEL_SDHI         0x15
#define RA_PSEL_ETH_MII      0x16
#define RA_PSEL_ETH_RMII     0x17
#define RA_PSEL_ETH_RGMII    0x18
#define RA_PSEL_GLCDC        0x19
#define RA_PSEL_OSPI         0x1c
#define RA_PSEL_CTSU         0x0c
#define RA_PSEL_CEU          0xf
#define RA_PSEL_PDM          0x1b


#define RA_PSEL_POS 8

#define RA_PSEL_MASK 0x1f

#define RA_MODE_POS 13

#define RA_MODE_MASK 0x1


#define RA_PSEL(psel, port_num, pin_num)                                                           \
        (1 << RA_MODE_POS | psel << RA_PSEL_POS | port_num << RA_PORT_NUM_POS |                    \
         pin_num << RA_PIN_NUM_POS)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RA_H__ */
```

## 650.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024-2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 151 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RA_H__`。

## 650.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-ra_8h.html)

---

[上一章](P649_pcnt_esp32.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P651_pinctrl-rx-pfs.h_源码浏览.md)
