---
id: learning.zephyr-docs.api-source-configuration-reference.page-67
title: pinctrl-ra0.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-ra0_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_pinctrl-ra0.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-ra0_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-ra0_8h.html)。

## 67.1\_原始可见代码（Source Code）

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
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00241"></a>
<a id="l00243"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00301"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00306"></a>
<a id="l00308"></a>
<a id="l00310"></a>
<a id="l00312"></a>
<a id="l00314"></a>
<a id="l00316"></a>
<a id="l00318"></a>
<a id="l00320"></a>
<a id="l00322"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00328"></a>
<a id="l00330"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00337"></a>
<a id="l00339"></a>
<a id="l00341"></a>
<a id="l00343"></a>
<a id="l00345"></a>
<a id="l00347"></a>
<a id="l00349"></a>
<a id="l00351"></a>
<a id="l00353"></a>
<a id="l00355"></a>
<a id="l00357"></a>
<a id="l00359"></a>
<a id="l00361"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00373"></a>
<a id="l00375"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00380"></a>
<a id="foldopen00388"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00392"></a>
<a id="l00393"></a>

```c
/*
 * Copyright (c) 2026 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RA0_H__
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RA0_H__




/* Pin configuration bit field positions and masks. */
#define RA_PORT_NUM_POS  0
#define RA_PORT_NUM_MASK 0xf
#define RA_PIN_NUM_POS   4
#define RA_PIN_NUM_MASK  0xf
#define RA_PSEL_POS      8
#define RA_PSEL_MASK     0x1f

/* Per-port peripheral-function selector (PSEL) values. */

#define RA_PSEL_P1nPFS_SWDIO    0x1
#define RA_PSEL_P1nPFS_TI04A    0x1
#define RA_PSEL_P1nPFS_TO04A    0x1
#define RA_PSEL_P1nPFS_TI07A    0x1
#define RA_PSEL_P1nPFS_TO07A    0x1
#define RA_PSEL_P1nPFS_TI06A    0x1
#define RA_PSEL_P1nPFS_TO06A    0x1
#define RA_PSEL_P1nPFS_TI05A    0x1
#define RA_PSEL_P1nPFS_TO05A    0x1
#define RA_PSEL_P1nPFS_TI02D    0x1
#define RA_PSEL_P1nPFS_TO02D    0x1
#define RA_PSEL_P1nPFS_TI01D    0x1
#define RA_PSEL_P1nPFS_TO01D    0x1
#define RA_PSEL_P1nPFS_TI02A    0x1
#define RA_PSEL_P1nPFS_TO02A    0x1
#define RA_PSEL_P1nPFS_TI01A    0x1
#define RA_PSEL_P1nPFS_TO01A    0x1
#define RA_PSEL_P1nPFS_TI07B    0x1
#define RA_PSEL_P1nPFS_TO07B    0x1
#define RA_PSEL_P1nPFS_TI03A    0x1
#define RA_PSEL_P1nPFS_TO03A    0x1
#define RA_PSEL_P1nPFS_TI01B    0x2
#define RA_PSEL_P1nPFS_TO01B    0x2
#define RA_PSEL_P1nPFS_TI00C    0x2
#define RA_PSEL_P1nPFS_TO00C    0x2
#define RA_PSEL_P1nPFS_SSI00A   0x2
#define RA_PSEL_P1nPFS_TI00D    0x2
#define RA_PSEL_P1nPFS_TO00D    0x2
#define RA_PSEL_P1nPFS_TI03B    0x2
#define RA_PSEL_P1nPFS_TO03B    0x2
#define RA_PSEL_P1nPFS_TXD2A    0x2
#define RA_PSEL_P1nPFS_SO20A    0x2
#define RA_PSEL_P1nPFS_RXD2A    0x2
#define RA_PSEL_P1nPFS_SI20A    0x2
#define RA_PSEL_P1nPFS_SDA20A   0x2
#define RA_PSEL_P1nPFS_SCK20A   0x2
#define RA_PSEL_P1nPFS_SCL20A   0x2
#define RA_PSEL_P1nPFS_RXD0A    0x3
#define RA_PSEL_P1nPFS_SI00A    0x3
#define RA_PSEL_P1nPFS_SDA00A   0x3
#define RA_PSEL_P1nPFS_TXD0A    0x3
#define RA_PSEL_P1nPFS_SO00A    0x3
#define RA_PSEL_P1nPFS_SCK00A   0x3
#define RA_PSEL_P1nPFS_SCL00A   0x3
#define RA_PSEL_P1nPFS_SCK10A   0x3
#define RA_PSEL_P1nPFS_SCL10A   0x3
#define RA_PSEL_P1nPFS_SI10A    0x3
#define RA_PSEL_P1nPFS_SDA10A   0x3
#define RA_PSEL_P1nPFS_SO10A    0x3
#define RA_PSEL_P1nPFS_SDAA0C   0x3
#define RA_PSEL_P1nPFS_SCLA0C   0x3
#define RA_PSEL_P1nPFS_SSI00C   0x3
#define RA_PSEL_P1nPFS_SCLA0D   0x4
#define RA_PSEL_P1nPFS_SDAA0D   0x4
#define RA_PSEL_P1nPFS_RTCOUNTC 0x4
#define RA_PSEL_P1nPFS_RXDA1B   0x4
#define RA_PSEL_P1nPFS_TXDA1B   0x4
#define RA_PSEL_P1nPFS_TXDA0C   0x4
#define RA_PSEL_P1nPFS_RXDA0C   0x4
#define RA_PSEL_P1nPFS_RXDA0D   0x5
#define RA_PSEL_P1nPFS_TXDA0D   0x5
#define RA_PSEL_P1nPFS_PCLBUZ0B 0x5
#define RA_PSEL_P1nPFS_PCLBUZ1B 0x5
#define RA_PSEL_P1nPFS_SCLA1G   0x6
#define RA_PSEL_P1nPFS_SDAA1G   0x6
#define RA_PSEL_P1nPFS_SCLA1B   0x6
#define RA_PSEL_P1nPFS_SDAA1B   0x6
#define RA_PSEL_P1nPFS_RXDA1A   0x7
#define RA_PSEL_P1nPFS_TXDA1A   0x7
#define RA_PSEL_P1nPFS_TS11     0xC
#define RA_PSEL_P1nPFS_TS10     0xC
#define RA_PSEL_P1nPFS_TS9      0xC
#define RA_PSEL_P1nPFS_TS8      0xC
#define RA_PSEL_P1nPFS_TS7      0xC
#define RA_PSEL_P1nPFS_TS6      0xC
#define RA_PSEL_P1nPFS_TS5      0xC
#define RA_PSEL_P1nPFS_TS2      0xC
#define RA_PSEL_P1nPFS_TS3      0xC
#define RA_PSEL_P1nPFS_TS4      0xC
#define RA_PSEL_P1nPFS_TSCAP    0xC

#define RA_PSEL_P2nPFS_TI05B    0x1
#define RA_PSEL_P2nPFS_TO05B    0x1
#define RA_PSEL_P2nPFS_TO00B    0x1
#define RA_PSEL_P2nPFS_TI00B    0x1
#define RA_PSEL_P2nPFS_TO00A    0x1
#define RA_PSEL_P2nPFS_TI00A    0x1
#define RA_PSEL_P2nPFS_SSI00B   0x2
#define RA_PSEL_P2nPFS_RXDA0A   0x2
#define RA_PSEL_P2nPFS_TXDA0A   0x2
#define RA_PSEL_P2nPFS_TI03C    0x2
#define RA_PSEL_P2nPFS_TO03C    0x2
#define RA_PSEL_P2nPFS_TI02B    0x2
#define RA_PSEL_P2nPFS_TO02B    0x2
#define RA_PSEL_P2nPFS_SCK11B   0x3
#define RA_PSEL_P2nPFS_SCL11B   0x3
#define RA_PSEL_P2nPFS_SI01B    0x3
#define RA_PSEL_P2nPFS_SDA01B   0x3
#define RA_PSEL_P2nPFS_SCK01B   0x3
#define RA_PSEL_P2nPFS_SCL01B   0x3
#define RA_PSEL_P2nPFS_RXD1A    0x3
#define RA_PSEL_P2nPFS_TXD1A    0x3
#define RA_PSEL_P2nPFS_RTCOUTB  0x4
#define RA_PSEL_P2nPFS_SCLA1A   0x4
#define RA_PSEL_P2nPFS_SDAA1A   0x4
#define RA_PSEL_P2nPFS_SI11A    0x4
#define RA_PSEL_P2nPFS_SDA11A   0x4
#define RA_PSEL_P2nPFS_SO11A    0x4
#define RA_PSEL_P2nPFS_PCLBUZ0A 0x5
#define RA_PSEL_P2nPFS_SCLA0B   0x5
#define RA_PSEL_P2nPFS_SDAA0B   0x5
#define RA_PSEL_P2nPFS_RXDA0B   0x6
#define RA_PSEL_P2nPFS_TXDA0B   0x6

#define RA_PSEL_P3nPFS_SWCLK  0x1
#define RA_PSEL_P3nPFS_TI06B  0x1
#define RA_PSEL_P3nPFS_TO06B  0x1
#define RA_PSEL_P3nPFS_TI05C  0x1
#define RA_PSEL_P3nPFS_TO05C  0x1
#define RA_PSEL_P3nPFS_TI04B  0x2
#define RA_PSEL_P3nPFS_TO04B  0x2
#define RA_PSEL_P3nPFS_SDA21A 0x2
#define RA_PSEL_P3nPFS_SCL21A 0x2
#define RA_PSEL_P3nPFS_SCLA1C 0x3
#define RA_PSEL_P3nPFS_SDAA1C 0x3
#define RA_PSEL_P3nPFS_RXDA1C 0x4
#define RA_PSEL_P3nPFS_TXDA1C 0x4
#define RA_PSEL_P3nPFS_TS1    0xC
#define RA_PSEL_P3nPFS_TS0    0xC

#define RA_PSEL_P4nPFS_SCLA1D   0x1
#define RA_PSEL_P4nPFS_SDAA1D   0x1
#define RA_PSEL_P4nPFS_SCK11A   0x1
#define RA_PSEL_P4nPFS_SCL11A   0x1
#define RA_PSEL_P4nPFS_SCK11C   0x1
#define RA_PSEL_P4nPFS_SCL11C   0x1
#define RA_PSEL_P4nPFS_RTCOUTA  0x2
#define RA_PSEL_P4nPFS_TI04C    0x2
#define RA_PSEL_P4nPFS_TO04C    0x2
#define RA_PSEL_P4nPFS_TI03E    0x2
#define RA_PSEL_P4nPFS_TO03E    0x2
#define RA_PSEL_P4nPFS_PCLBUZ0C 0x3
#define RA_PSEL_P4nPFS_SDAA1F   0x4
#define RA_PSEL_P4nPFS_SCLA1F   0x4

#define RA_PSEL_P5nPFS_TI03D 0x1
#define RA_PSEL_P5nPFS_TO03D 0x1
#define RA_PSEL_P5nPFS_TS12  0xC

#define RA_PSEL_P9nPFS_SDAA0A 0x1
#define RA_PSEL_P9nPFS_SCLA0A 0x1
#define RA_PSEL_P9nPFS_SO01B  0x3


#define RA_PSEL(psel, port_num, pin_num)                                                           \
        (psel << RA_PSEL_POS | port_num << RA_PORT_NUM_POS | pin_num << RA_PIN_NUM_POS)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RA0_H__ */
```

## 67.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 63 行

引脚配置位域的位置和掩码。

### 注释 3：原第 77 行

每个端口的外设功能选择器（PSEL）取值。

### 注释 4：原第 393 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RA0_H__`。

## 67.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-ra0_8h.html)

---

[上一章](P066_pinctrl-r8a779g0.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P068_pinctrl-rx.h_源码浏览.md)
