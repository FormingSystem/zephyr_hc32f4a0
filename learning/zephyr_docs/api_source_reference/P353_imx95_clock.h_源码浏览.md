---
id: learning.zephyr-docs.api-source-reference.page-353
title: imx95_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx95__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第353章\_imx95\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/imx95__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/imx95__clock_8h.html)。

## 353.1\_原始可见代码（Source Code）

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
<a id="l00054"></a>
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
<a id="l00116"></a>
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
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>

```c
/*
 * Copyright 2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX95_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX95_CLOCK_H_

#define IMX95_CLK_32K                  1
#define IMX95_CLK_24M                  2
#define IMX95_CLK_FRO                  3
#define IMX95_CLK_SYSPLL1_VCO          4
#define IMX95_CLK_SYSPLL1_PFD0_UNGATED 5
#define IMX95_CLK_SYSPLL1_PFD0         6
#define IMX95_CLK_SYSPLL1_PFD0_DIV2    7
#define IMX95_CLK_SYSPLL1_PFD1_UNGATED 8
#define IMX95_CLK_SYSPLL1_PFD1         9
#define IMX95_CLK_SYSPLL1_PFD1_DIV2    10
#define IMX95_CLK_SYSPLL1_PFD2_UNGATED 11
#define IMX95_CLK_SYSPLL1_PFD2         12
#define IMX95_CLK_SYSPLL1_PFD2_DIV2    13
#define IMX95_CLK_AUDIOPLL1_VCO        14
#define IMX95_CLK_AUDIOPLL1            15
#define IMX95_CLK_AUDIOPLL2_VCO        16
#define IMX95_CLK_AUDIOPLL2            17
#define IMX95_CLK_VIDEOPLL1_VCO        18
#define IMX95_CLK_VIDEOPLL1            19
#define IMX95_CLK_RESERVED20           20
#define IMX95_CLK_RESERVED21           21
#define IMX95_CLK_RESERVED22           22
#define IMX95_CLK_RESERVED23           23
#define IMX95_CLK_ARMPLL_VCO           24
#define IMX95_CLK_ARMPLL_PFD0_UNGATED  25
#define IMX95_CLK_ARMPLL_PFD0          26
#define IMX95_CLK_ARMPLL_PFD1_UNGATED  27
#define IMX95_CLK_ARMPLL_PFD1          28
#define IMX95_CLK_ARMPLL_PFD2_UNGATED  29
#define IMX95_CLK_ARMPLL_PFD2          30
#define IMX95_CLK_ARMPLL_PFD3_UNGATED  31
#define IMX95_CLK_ARMPLL_PFD3          32
#define IMX95_CLK_DRAMPLL_VCO          33
#define IMX95_CLK_DRAMPLL              34
#define IMX95_CLK_HSIOPLL_VCO          35
#define IMX95_CLK_HSIOPLL              36
#define IMX95_CLK_LDBPLL_VCO           37
#define IMX95_CLK_LDBPLL               38
#define IMX95_CLK_EXT1                 39
#define IMX95_CLK_EXT2                 40

#define IMX95_CCM_NUM_CLK_SRC 41

#define IMX95_CLK_ADC              (IMX95_CCM_NUM_CLK_SRC + 0)
#define IMX95_CLK_TMU              (IMX95_CCM_NUM_CLK_SRC + 1)
#define IMX95_CLK_BUSAON           (IMX95_CCM_NUM_CLK_SRC + 2)
#define IMX95_CLK_CAN1             (IMX95_CCM_NUM_CLK_SRC + 3)
#define IMX95_CLK_I3C1             (IMX95_CCM_NUM_CLK_SRC + 4)
#define IMX95_CLK_I3C1SLOW         (IMX95_CCM_NUM_CLK_SRC + 5)
#define IMX95_CLK_LPI2C1           (IMX95_CCM_NUM_CLK_SRC + 6)
#define IMX95_CLK_LPI2C2           (IMX95_CCM_NUM_CLK_SRC + 7)
#define IMX95_CLK_LPSPI1           (IMX95_CCM_NUM_CLK_SRC + 8)
#define IMX95_CLK_LPSPI2           (IMX95_CCM_NUM_CLK_SRC + 9)
#define IMX95_CLK_LPTMR1           (IMX95_CCM_NUM_CLK_SRC + 10)
#define IMX95_CLK_LPUART1          (IMX95_CCM_NUM_CLK_SRC + 11)
#define IMX95_CLK_LPUART2          (IMX95_CCM_NUM_CLK_SRC + 12)
#define IMX95_CLK_M33              (IMX95_CCM_NUM_CLK_SRC + 13)
#define IMX95_CLK_M33SYSTICK       (IMX95_CCM_NUM_CLK_SRC + 14)
#define IMX95_CLK_MQS1             (IMX95_CCM_NUM_CLK_SRC + 15)
#define IMX95_CLK_PDM              (IMX95_CCM_NUM_CLK_SRC + 16)
#define IMX95_CLK_SAI1             (IMX95_CCM_NUM_CLK_SRC + 17)
#define IMX95_CLK_SENTINEL         (IMX95_CCM_NUM_CLK_SRC + 18)
#define IMX95_CLK_TPM2             (IMX95_CCM_NUM_CLK_SRC + 19)
#define IMX95_CLK_TSTMR1           (IMX95_CCM_NUM_CLK_SRC + 20)
#define IMX95_CLK_CAMAPB           (IMX95_CCM_NUM_CLK_SRC + 21)
#define IMX95_CLK_CAMAXI           (IMX95_CCM_NUM_CLK_SRC + 22)
#define IMX95_CLK_CAMCM0           (IMX95_CCM_NUM_CLK_SRC + 23)
#define IMX95_CLK_CAMISI           (IMX95_CCM_NUM_CLK_SRC + 24)
#define IMX95_CLK_MIPIPHYCFG       (IMX95_CCM_NUM_CLK_SRC + 25)
#define IMX95_CLK_MIPIPHYPLLBYPASS (IMX95_CCM_NUM_CLK_SRC + 26)
#define IMX95_CLK_MIPIPHYPLLREF    (IMX95_CCM_NUM_CLK_SRC + 27)
#define IMX95_CLK_MIPITESTBYTE     (IMX95_CCM_NUM_CLK_SRC + 28)
#define IMX95_CLK_A55              (IMX95_CCM_NUM_CLK_SRC + 29)
#define IMX95_CLK_A55MTRBUS        (IMX95_CCM_NUM_CLK_SRC + 30)
#define IMX95_CLK_A55PERIPH        (IMX95_CCM_NUM_CLK_SRC + 31)
#define IMX95_CLK_DRAMALT          (IMX95_CCM_NUM_CLK_SRC + 32)
#define IMX95_CLK_DRAMAPB          (IMX95_CCM_NUM_CLK_SRC + 33)
#define IMX95_CLK_DISPAPB          (IMX95_CCM_NUM_CLK_SRC + 34)
#define IMX95_CLK_DISPAXI          (IMX95_CCM_NUM_CLK_SRC + 35)
#define IMX95_CLK_DISPDP           (IMX95_CCM_NUM_CLK_SRC + 36)
#define IMX95_CLK_DISPOCRAM        (IMX95_CCM_NUM_CLK_SRC + 37)
#define IMX95_CLK_DISPUSB31        (IMX95_CCM_NUM_CLK_SRC + 38)
#define IMX95_CLK_DISP1PIX         (IMX95_CCM_NUM_CLK_SRC + 39)
#define IMX95_CLK_DISP2PIX         (IMX95_CCM_NUM_CLK_SRC + 40)
#define IMX95_CLK_DISP3PIX         (IMX95_CCM_NUM_CLK_SRC + 41)
#define IMX95_CLK_GPUAPB           (IMX95_CCM_NUM_CLK_SRC + 42)
#define IMX95_CLK_GPU              (IMX95_CCM_NUM_CLK_SRC + 43)
#define IMX95_CLK_HSIOACSCAN480M   (IMX95_CCM_NUM_CLK_SRC + 44)
#define IMX95_CLK_HSIOACSCAN80M    (IMX95_CCM_NUM_CLK_SRC + 45)
#define IMX95_CLK_HSIO             (IMX95_CCM_NUM_CLK_SRC + 46)
#define IMX95_CLK_HSIOPCIEAUX      (IMX95_CCM_NUM_CLK_SRC + 47)
#define IMX95_CLK_HSIOPCIETEST160M (IMX95_CCM_NUM_CLK_SRC + 48)
#define IMX95_CLK_HSIOPCIETEST400M (IMX95_CCM_NUM_CLK_SRC + 49)
#define IMX95_CLK_HSIOPCIETEST500M (IMX95_CCM_NUM_CLK_SRC + 50)
#define IMX95_CLK_HSIOUSBTEST50M   (IMX95_CCM_NUM_CLK_SRC + 51)
#define IMX95_CLK_HSIOUSBTEST60M   (IMX95_CCM_NUM_CLK_SRC + 52)
#define IMX95_CLK_BUSM7            (IMX95_CCM_NUM_CLK_SRC + 53)
#define IMX95_CLK_M7               (IMX95_CCM_NUM_CLK_SRC + 54)
#define IMX95_CLK_M7SYSTICK        (IMX95_CCM_NUM_CLK_SRC + 55)
#define IMX95_CLK_BUSNETCMIX       (IMX95_CCM_NUM_CLK_SRC + 56)
#define IMX95_CLK_ENET             (IMX95_CCM_NUM_CLK_SRC + 57)
#define IMX95_CLK_ENETPHYTEST200M  (IMX95_CCM_NUM_CLK_SRC + 58)
#define IMX95_CLK_ENETPHYTEST500M  (IMX95_CCM_NUM_CLK_SRC + 59)
#define IMX95_CLK_ENETPHYTEST667M  (IMX95_CCM_NUM_CLK_SRC + 60)
#define IMX95_CLK_ENETREF          (IMX95_CCM_NUM_CLK_SRC + 61)
#define IMX95_CLK_ENETTIMER1       (IMX95_CCM_NUM_CLK_SRC + 62)
#define IMX95_CLK_MQS2             (IMX95_CCM_NUM_CLK_SRC + 63)
#define IMX95_CLK_SAI2             (IMX95_CCM_NUM_CLK_SRC + 64)
#define IMX95_CLK_NOCAPB           (IMX95_CCM_NUM_CLK_SRC + 65)
#define IMX95_CLK_NOC              (IMX95_CCM_NUM_CLK_SRC + 66)
#define IMX95_CLK_NPUAPB           (IMX95_CCM_NUM_CLK_SRC + 67)
#define IMX95_CLK_NPU              (IMX95_CCM_NUM_CLK_SRC + 68)
#define IMX95_CLK_CCMCKO1          (IMX95_CCM_NUM_CLK_SRC + 69)
#define IMX95_CLK_CCMCKO2          (IMX95_CCM_NUM_CLK_SRC + 70)
#define IMX95_CLK_CCMCKO3          (IMX95_CCM_NUM_CLK_SRC + 71)
#define IMX95_CLK_CCMCKO4          (IMX95_CCM_NUM_CLK_SRC + 72)
#define IMX95_CLK_VPUAPB           (IMX95_CCM_NUM_CLK_SRC + 73)
#define IMX95_CLK_VPU              (IMX95_CCM_NUM_CLK_SRC + 74)
#define IMX95_CLK_VPUDSP           (IMX95_CCM_NUM_CLK_SRC + 75)
#define IMX95_CLK_VPUJPEG          (IMX95_CCM_NUM_CLK_SRC + 76)
#define IMX95_CLK_AUDIOXCVR        (IMX95_CCM_NUM_CLK_SRC + 77)
#define IMX95_CLK_BUSWAKEUP        (IMX95_CCM_NUM_CLK_SRC + 78)
#define IMX95_CLK_CAN2             (IMX95_CCM_NUM_CLK_SRC + 79)
#define IMX95_CLK_CAN3             (IMX95_CCM_NUM_CLK_SRC + 80)
#define IMX95_CLK_CAN4             (IMX95_CCM_NUM_CLK_SRC + 81)
#define IMX95_CLK_CAN5             (IMX95_CCM_NUM_CLK_SRC + 82)
#define IMX95_CLK_FLEXIO1          (IMX95_CCM_NUM_CLK_SRC + 83)
#define IMX95_CLK_FLEXIO2          (IMX95_CCM_NUM_CLK_SRC + 84)
#define IMX95_CLK_FLEXSPI1         (IMX95_CCM_NUM_CLK_SRC + 85)
#define IMX95_CLK_I3C2             (IMX95_CCM_NUM_CLK_SRC + 86)
#define IMX95_CLK_I3C2SLOW         (IMX95_CCM_NUM_CLK_SRC + 87)
#define IMX95_CLK_LPI2C3           (IMX95_CCM_NUM_CLK_SRC + 88)
#define IMX95_CLK_LPI2C4           (IMX95_CCM_NUM_CLK_SRC + 89)
#define IMX95_CLK_LPI2C5           (IMX95_CCM_NUM_CLK_SRC + 90)
#define IMX95_CLK_LPI2C6           (IMX95_CCM_NUM_CLK_SRC + 91)
#define IMX95_CLK_LPI2C7           (IMX95_CCM_NUM_CLK_SRC + 92)
#define IMX95_CLK_LPI2C8           (IMX95_CCM_NUM_CLK_SRC + 93)
#define IMX95_CLK_LPSPI3           (IMX95_CCM_NUM_CLK_SRC + 94)
#define IMX95_CLK_LPSPI4           (IMX95_CCM_NUM_CLK_SRC + 95)
#define IMX95_CLK_LPSPI5           (IMX95_CCM_NUM_CLK_SRC + 96)
#define IMX95_CLK_LPSPI6           (IMX95_CCM_NUM_CLK_SRC + 97)
#define IMX95_CLK_LPSPI7           (IMX95_CCM_NUM_CLK_SRC + 98)
#define IMX95_CLK_LPSPI8           (IMX95_CCM_NUM_CLK_SRC + 99)
#define IMX95_CLK_LPTMR2           (IMX95_CCM_NUM_CLK_SRC + 100)
#define IMX95_CLK_LPUART3          (IMX95_CCM_NUM_CLK_SRC + 101)
#define IMX95_CLK_LPUART4          (IMX95_CCM_NUM_CLK_SRC + 102)
#define IMX95_CLK_LPUART5          (IMX95_CCM_NUM_CLK_SRC + 103)
#define IMX95_CLK_LPUART6          (IMX95_CCM_NUM_CLK_SRC + 104)
#define IMX95_CLK_LPUART7          (IMX95_CCM_NUM_CLK_SRC + 105)
#define IMX95_CLK_LPUART8          (IMX95_CCM_NUM_CLK_SRC + 106)
#define IMX95_CLK_SAI3             (IMX95_CCM_NUM_CLK_SRC + 107)
#define IMX95_CLK_SAI4             (IMX95_CCM_NUM_CLK_SRC + 108)
#define IMX95_CLK_SAI5             (IMX95_CCM_NUM_CLK_SRC + 109)
#define IMX95_CLK_SPDIF            (IMX95_CCM_NUM_CLK_SRC + 110)
#define IMX95_CLK_SWOTRACE         (IMX95_CCM_NUM_CLK_SRC + 111)
#define IMX95_CLK_TPM4             (IMX95_CCM_NUM_CLK_SRC + 112)
#define IMX95_CLK_TPM5             (IMX95_CCM_NUM_CLK_SRC + 113)
#define IMX95_CLK_TPM6             (IMX95_CCM_NUM_CLK_SRC + 114)
#define IMX95_CLK_TSTMR2           (IMX95_CCM_NUM_CLK_SRC + 115)
#define IMX95_CLK_USBPHYBURUNIN    (IMX95_CCM_NUM_CLK_SRC + 116)
#define IMX95_CLK_USDHC1           (IMX95_CCM_NUM_CLK_SRC + 117)
#define IMX95_CLK_USDHC2           (IMX95_CCM_NUM_CLK_SRC + 118)
#define IMX95_CLK_USDHC3           (IMX95_CCM_NUM_CLK_SRC + 119)
#define IMX95_CLK_V2XPK            (IMX95_CCM_NUM_CLK_SRC + 120)
#define IMX95_CLK_WAKEUPAXI        (IMX95_CCM_NUM_CLK_SRC + 121)
#define IMX95_CLK_XSPISLVROOT      (IMX95_CCM_NUM_CLK_SRC + 122)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX95_CLOCK_H_ */
```

## 353.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 177 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX95_CLOCK_H_`。

## 353.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/imx95__clock_8h.html)

---

[上一章](P352_imx952_power.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P354_imx95_power.h_源码浏览.md)
