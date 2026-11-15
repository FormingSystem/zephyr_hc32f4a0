---
id: learning.zephyr-docs.api-source-reference.page-351
title: imx952_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx952__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第351章\_imx952\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/imx952__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/imx952__clock_8h.html)。

## 351.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
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
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
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
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00272"></a>
<a id="l00274"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00302"></a>
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
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00362"></a>
<a id="l00364"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00370"></a>
<a id="l00372"></a>
<a id="l00374"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00379"></a>
<a id="l00380"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX952_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX952_CLOCK_H_


#define IMX952_CLK_EXT                  0
#define IMX952_CLK_32K                  1
#define IMX952_CLK_24M                  2
#define IMX952_CLK_FRO                  3
#define IMX952_CLK_SYSPLL1_VCO          4
#define IMX952_CLK_SYSPLL1_PFD0_UNGATED 5
#define IMX952_CLK_SYSPLL1_PFD0         6
#define IMX952_CLK_SYSPLL1_PFD0_DIV2    7
#define IMX952_CLK_SYSPLL1_PFD1_UNGATED 8
#define IMX952_CLK_SYSPLL1_PFD1         9
#define IMX952_CLK_SYSPLL1_PFD1_DIV2    10
#define IMX952_CLK_SYSPLL1_PFD2_UNGATED 11
#define IMX952_CLK_SYSPLL1_PFD2         12
#define IMX952_CLK_SYSPLL1_PFD2_DIV2    13
#define IMX952_CLK_AUDIOPLL1_VCO        14
#define IMX952_CLK_AUDIOPLL1            15
#define IMX952_CLK_AUDIOPLL2_VCO        16
#define IMX952_CLK_AUDIOPLL2            17
#define IMX952_CLK_VIDEOPLL1_VCO        18
#define IMX952_CLK_VIDEOPLL1            19
#define IMX952_CLK_SRC_RESERVED20       20
#define IMX952_CLK_SYSPLL1_PFD3_UNGATED 21
#define IMX952_CLK_SYSPLL1_PFD3         22
#define IMX952_CLK_SYSPLL1_PFD3_DIV2    23
#define IMX952_CLK_ARMPLL_VCO           24
#define IMX952_CLK_ARMPLL_PFD0_UNGATED  25
#define IMX952_CLK_ARMPLL_PFD0          26
#define IMX952_CLK_ARMPLL_PFD1_UNGATED  27
#define IMX952_CLK_ARMPLL_PFD1          28
#define IMX952_CLK_ARMPLL_PFD2_UNGATED  29
#define IMX952_CLK_ARMPLL_PFD2          30
#define IMX952_CLK_ARMPLL_PFD3_UNGATED  31
#define IMX952_CLK_ARMPLL_PFD3          32
#define IMX952_CLK_DRAMPLL_VCO          33
#define IMX952_CLK_DRAMPLL              34
#define IMX952_CLK_HSIOPLL_VCO          35
#define IMX952_CLK_HSIOPLL              36
#define IMX952_CLK_LDBPLL_VCO           37
#define IMX952_CLK_LDBPLL               38
#define IMX952_CLK_EXT1                 39
#define IMX952_CLK_EXT2                 40


#define IMX952_CCM_NUM_CLK_SRC 41


#define IMX952_CLK_ADC              (IMX952_CCM_NUM_CLK_SRC + 0)
#define IMX952_CLK_RESERVED1        (IMX952_CCM_NUM_CLK_SRC + 1)
#define IMX952_CLK_BUSAON           (IMX952_CCM_NUM_CLK_SRC + 2)
#define IMX952_CLK_CAN1             (IMX952_CCM_NUM_CLK_SRC + 3)
#define IMX952_CLK_RESERVED4        (IMX952_CCM_NUM_CLK_SRC + 4)
#define IMX952_CLK_I3C1SLOW         (IMX952_CCM_NUM_CLK_SRC + 5)
#define IMX952_CLK_LPI2C1           (IMX952_CCM_NUM_CLK_SRC + 6)
#define IMX952_CLK_LPI2C2           (IMX952_CCM_NUM_CLK_SRC + 7)
#define IMX952_CLK_LPSPI1           (IMX952_CCM_NUM_CLK_SRC + 8)
#define IMX952_CLK_LPSPI2           (IMX952_CCM_NUM_CLK_SRC + 9)
#define IMX952_CLK_LPTMR1           (IMX952_CCM_NUM_CLK_SRC + 10)
#define IMX952_CLK_LPUART1          (IMX952_CCM_NUM_CLK_SRC + 11)
#define IMX952_CLK_LPUART2          (IMX952_CCM_NUM_CLK_SRC + 12)
#define IMX952_CLK_M33              (IMX952_CCM_NUM_CLK_SRC + 13)
#define IMX952_CLK_M33SYSTICK       (IMX952_CCM_NUM_CLK_SRC + 14)
#define IMX952_CLK_RESERVED15       (IMX952_CCM_NUM_CLK_SRC + 15)
#define IMX952_CLK_PDM              (IMX952_CCM_NUM_CLK_SRC + 16)
#define IMX952_CLK_SAI1             (IMX952_CCM_NUM_CLK_SRC + 17)
#define IMX952_CLK_RESERVED18       (IMX952_CCM_NUM_CLK_SRC + 18)
#define IMX952_CLK_TPM2             (IMX952_CCM_NUM_CLK_SRC + 19)
#define IMX952_CLK_RESERVED20       (IMX952_CCM_NUM_CLK_SRC + 20)
#define IMX952_CLK_CAMAPB           (IMX952_CCM_NUM_CLK_SRC + 21)
#define IMX952_CLK_CAMAXI           (IMX952_CCM_NUM_CLK_SRC + 22)
#define IMX952_CLK_CAMCM0           (IMX952_CCM_NUM_CLK_SRC + 23)
#define IMX952_CLK_CAMISI           (IMX952_CCM_NUM_CLK_SRC + 24)
#define IMX952_CLK_CAMPHYCFG        (IMX952_CCM_NUM_CLK_SRC + 25)
#define IMX952_CLK_MIPIPHYPLLBYPASS (IMX952_CCM_NUM_CLK_SRC + 26)
#define IMX952_CLK_RESERVED27       (IMX952_CCM_NUM_CLK_SRC + 27)
#define IMX952_CLK_MIPITESTBYTE     (IMX952_CCM_NUM_CLK_SRC + 28)
#define IMX952_CLK_A55              (IMX952_CCM_NUM_CLK_SRC + 29)
#define IMX952_CLK_A55MTRBUS        (IMX952_CCM_NUM_CLK_SRC + 30)
#define IMX952_CLK_A55PERIPH        (IMX952_CCM_NUM_CLK_SRC + 31)
#define IMX952_CLK_DRAMALT          (IMX952_CCM_NUM_CLK_SRC + 32)
#define IMX952_CLK_DRAMAPB          (IMX952_CCM_NUM_CLK_SRC + 33)
#define IMX952_CLK_DISPAPB          (IMX952_CCM_NUM_CLK_SRC + 34)
#define IMX952_CLK_DISPAXI          (IMX952_CCM_NUM_CLK_SRC + 35)
#define IMX952_CLK_DISPLPSPI        (IMX952_CCM_NUM_CLK_SRC + 36)
#define IMX952_CLK_DISPOCRAM        (IMX952_CCM_NUM_CLK_SRC + 37)
#define IMX952_CLK_DISPHYCFG        (IMX952_CCM_NUM_CLK_SRC + 38)
#define IMX952_CLK_DISP1PIX         (IMX952_CCM_NUM_CLK_SRC + 39)
#define IMX952_CLK_DISPCDPHYAPB     (IMX952_CCM_NUM_CLK_SRC + 40)
#define IMX952_CLK_RESERVED41       (IMX952_CCM_NUM_CLK_SRC + 41)
#define IMX952_CLK_GPUAPB           (IMX952_CCM_NUM_CLK_SRC + 42)
#define IMX952_CLK_GPU              (IMX952_CCM_NUM_CLK_SRC + 43)
#define IMX952_CLK_HSIOACSCAN480M   (IMX952_CCM_NUM_CLK_SRC + 44)
#define IMX952_CLK_HSIOACSCAN80M    (IMX952_CCM_NUM_CLK_SRC + 45)
#define IMX952_CLK_HSIO             (IMX952_CCM_NUM_CLK_SRC + 46)
#define IMX952_CLK_HSIOPCIEAUX      (IMX952_CCM_NUM_CLK_SRC + 47)
#define IMX952_CLK_HSIOPCIETEST160M (IMX952_CCM_NUM_CLK_SRC + 48)
#define IMX952_CLK_HSIOPCIETEST400M (IMX952_CCM_NUM_CLK_SRC + 49)
#define IMX952_CLK_HSIOPCIETEST500M (IMX952_CCM_NUM_CLK_SRC + 50)
#define IMX952_CLK_HSIOUSBTEST50M   (IMX952_CCM_NUM_CLK_SRC + 51)
#define IMX952_CLK_HSIOUSBTEST60M   (IMX952_CCM_NUM_CLK_SRC + 52)
#define IMX952_CLK_BUSM7            (IMX952_CCM_NUM_CLK_SRC + 53)
#define IMX952_CLK_M7               (IMX952_CCM_NUM_CLK_SRC + 54)
#define IMX952_CLK_M7SYSTICK        (IMX952_CCM_NUM_CLK_SRC + 55)
#define IMX952_CLK_BUSNETCMIX       (IMX952_CCM_NUM_CLK_SRC + 56)
#define IMX952_CLK_ENET             (IMX952_CCM_NUM_CLK_SRC + 57)
#define IMX952_CLK_ENETPHYTEST200M  (IMX952_CCM_NUM_CLK_SRC + 58)
#define IMX952_CLK_ENETPHYTEST500M  (IMX952_CCM_NUM_CLK_SRC + 59)
#define IMX952_CLK_ENETPHYTEST667M  (IMX952_CCM_NUM_CLK_SRC + 60)
#define IMX952_CLK_ENETREF          (IMX952_CCM_NUM_CLK_SRC + 61)
#define IMX952_CLK_ENETTIMER1       (IMX952_CCM_NUM_CLK_SRC + 62)
#define IMX952_CLK_RESERVED63       (IMX952_CCM_NUM_CLK_SRC + 63)
#define IMX952_CLK_SAI2             (IMX952_CCM_NUM_CLK_SRC + 64)
#define IMX952_CLK_NOCAPB           (IMX952_CCM_NUM_CLK_SRC + 65)
#define IMX952_CLK_NOC              (IMX952_CCM_NUM_CLK_SRC + 66)
#define IMX952_CLK_NPUAPB           (IMX952_CCM_NUM_CLK_SRC + 67)
#define IMX952_CLK_NPU              (IMX952_CCM_NUM_CLK_SRC + 68)
#define IMX952_CLK_CCMCKO1          (IMX952_CCM_NUM_CLK_SRC + 69)
#define IMX952_CLK_CCMCKO2          (IMX952_CCM_NUM_CLK_SRC + 70)
#define IMX952_CLK_CCMCKO3          (IMX952_CCM_NUM_CLK_SRC + 71)
#define IMX952_CLK_CCMCKO4          (IMX952_CCM_NUM_CLK_SRC + 72)
#define IMX952_CLK_VPUAPB           (IMX952_CCM_NUM_CLK_SRC + 73)
#define IMX952_CLK_VPU              (IMX952_CCM_NUM_CLK_SRC + 74)
#define IMX952_CLK_RESERVED75       (IMX952_CCM_NUM_CLK_SRC + 75)
#define IMX952_CLK_RESERVED76       (IMX952_CCM_NUM_CLK_SRC + 76)
#define IMX952_CLK_AUDIOXCVR        (IMX952_CCM_NUM_CLK_SRC + 77)
#define IMX952_CLK_BUSWAKEUP        (IMX952_CCM_NUM_CLK_SRC + 78)
#define IMX952_CLK_CAN2             (IMX952_CCM_NUM_CLK_SRC + 79)
#define IMX952_CLK_CAN3             (IMX952_CCM_NUM_CLK_SRC + 80)
#define IMX952_CLK_CAN4             (IMX952_CCM_NUM_CLK_SRC + 81)
#define IMX952_CLK_CAN5             (IMX952_CCM_NUM_CLK_SRC + 82)
#define IMX952_CLK_FLEXIO1          (IMX952_CCM_NUM_CLK_SRC + 83)
#define IMX952_CLK_FLEXIO2          (IMX952_CCM_NUM_CLK_SRC + 84)
#define IMX952_CLK_XSPI1            (IMX952_CCM_NUM_CLK_SRC + 85)
#define IMX952_CLK_RESERVED86       (IMX952_CCM_NUM_CLK_SRC + 86)
#define IMX952_CLK_I3C2SLOW         (IMX952_CCM_NUM_CLK_SRC + 87)
#define IMX952_CLK_LPI2C3           (IMX952_CCM_NUM_CLK_SRC + 88)
#define IMX952_CLK_LPI2C4           (IMX952_CCM_NUM_CLK_SRC + 89)
#define IMX952_CLK_LPI2C5           (IMX952_CCM_NUM_CLK_SRC + 90)
#define IMX952_CLK_LPI2C6           (IMX952_CCM_NUM_CLK_SRC + 91)
#define IMX952_CLK_LPI2C7           (IMX952_CCM_NUM_CLK_SRC + 92)
#define IMX952_CLK_LPI2C8           (IMX952_CCM_NUM_CLK_SRC + 93)
#define IMX952_CLK_LPSPI3           (IMX952_CCM_NUM_CLK_SRC + 94)
#define IMX952_CLK_LPSPI4           (IMX952_CCM_NUM_CLK_SRC + 95)
#define IMX952_CLK_LPSPI5           (IMX952_CCM_NUM_CLK_SRC + 96)
#define IMX952_CLK_LPSPI6           (IMX952_CCM_NUM_CLK_SRC + 97)
#define IMX952_CLK_LPSPI7           (IMX952_CCM_NUM_CLK_SRC + 98)
#define IMX952_CLK_LPSPI8           (IMX952_CCM_NUM_CLK_SRC + 99)
#define IMX952_CLK_LPTMR2           (IMX952_CCM_NUM_CLK_SRC + 100)
#define IMX952_CLK_LPUART3          (IMX952_CCM_NUM_CLK_SRC + 101)
#define IMX952_CLK_LPUART4          (IMX952_CCM_NUM_CLK_SRC + 102)
#define IMX952_CLK_LPUART5          (IMX952_CCM_NUM_CLK_SRC + 103)
#define IMX952_CLK_LPUART6          (IMX952_CCM_NUM_CLK_SRC + 104)
#define IMX952_CLK_LPUART7          (IMX952_CCM_NUM_CLK_SRC + 105)
#define IMX952_CLK_LPUART8          (IMX952_CCM_NUM_CLK_SRC + 106)
#define IMX952_CLK_SAI3             (IMX952_CCM_NUM_CLK_SRC + 107)
#define IMX952_CLK_SAI4             (IMX952_CCM_NUM_CLK_SRC + 108)
#define IMX952_CLK_SAI5             (IMX952_CCM_NUM_CLK_SRC + 109)
#define IMX952_CLK_SPDIF            (IMX952_CCM_NUM_CLK_SRC + 110)
#define IMX952_CLK_SWOTRACE         (IMX952_CCM_NUM_CLK_SRC + 111)
#define IMX952_CLK_TPM4             (IMX952_CCM_NUM_CLK_SRC + 112)
#define IMX952_CLK_TPM5             (IMX952_CCM_NUM_CLK_SRC + 113)
#define IMX952_CLK_TPM6             (IMX952_CCM_NUM_CLK_SRC + 114)
#define IMX952_CLK_TSTMR2           (IMX952_CCM_NUM_CLK_SRC + 115)
#define IMX952_CLK_USBPHYBURUNIN    (IMX952_CCM_NUM_CLK_SRC + 116)
#define IMX952_CLK_USDHC1           (IMX952_CCM_NUM_CLK_SRC + 117)
#define IMX952_CLK_USDHC2           (IMX952_CCM_NUM_CLK_SRC + 118)
#define IMX952_CLK_USDHC3           (IMX952_CCM_NUM_CLK_SRC + 119)
#define IMX952_CLK_V2XPK            (IMX952_CCM_NUM_CLK_SRC + 120)
#define IMX952_CLK_WAKEUPAXI        (IMX952_CCM_NUM_CLK_SRC + 121)
#define IMX952_CLK_XSPISLVROOT      (IMX952_CCM_NUM_CLK_SRC + 122)
#define IMX952_CLK_AUDMIX1          (IMX952_CCM_NUM_CLK_SRC + 123)
#define IMX952_CLK_ASRC1            (IMX952_CCM_NUM_CLK_SRC + 124)
#define IMX952_CLK_ASRC2            (IMX952_CCM_NUM_CLK_SRC + 125)
#define IMX952_CLK_GPT2             (IMX952_CCM_NUM_CLK_SRC + 126)
#define IMX952_CLK_GPT3             (IMX952_CCM_NUM_CLK_SRC + 127)
#define IMX952_CLK_GPT4             (IMX952_CCM_NUM_CLK_SRC + 128)
#define IMX952_CLK_GPT5             (IMX952_CCM_NUM_CLK_SRC + 129)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX952_CLOCK_H_ */
```

## 351.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright 2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 380 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX952_CLOCK_H_`。

## 351.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/imx952__clock_8h.html)

---

[上一章](P350_imx943_power.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P352_imx952_power.h_源码浏览.md)
