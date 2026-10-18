---
id: learning.zephyr-docs.api-source-system-reference.page-27
title: numaker_m2l31x_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/numaker__m2l31x__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_numaker\_m2l31x\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/numaker__m2l31x__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P264_zephyr__dt-bindings__reset__numaker_m2l31x_reset.h_文件参考.md)。

## 27.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00034"></a>
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
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00194"></a>

```c
/*
 * Copyright (c) 2024 Nuvoton Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_NUMAKER_M2L31X_RESET_H
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_NUMAKER_M2L31X_RESET_H





/* Beginning of M2L31 BSP sys_reg.h reset module copy */

#define LPSCC_IPRST0_LPPDMA0RST_Pos      0
#define LPSCC_IPRST0_LPGPIORST_Pos       1
#define LPSCC_IPRST0_LPSRAMRST_Pos       2
#define LPSCC_IPRST0_WDTRST_Pos          16
#define LPSCC_IPRST0_LPSPI0RST_Pos       17
#define LPSCC_IPRST0_LPI2C0RST_Pos       18
#define LPSCC_IPRST0_LPUART0RST_Pos      19
#define LPSCC_IPRST0_LPTMR0RST_Pos       20
#define LPSCC_IPRST0_LPTMR1RST_Pos       21
#define LPSCC_IPRST0_TTMR0RST_Pos        22
#define LPSCC_IPRST0_TTMR1RST_Pos        23
#define LPSCC_IPRST0_LPADC0RST_Pos       24
#define LPSCC_IPRST0_OPARST_Pos          27
#define SYS_IPRST0_CHIPRST_Pos           0
#define SYS_IPRST0_CPURST_Pos            1
#define SYS_IPRST0_PDMA0RST_Pos          2
#define SYS_IPRST0_EBIRST_Pos            3
#define SYS_IPRST0_USBHRST_Pos           4
#define SYS_IPRST0_CRCRST_Pos            7
#define SYS_IPRST0_CRPTRST_Pos           12
#define SYS_IPRST0_CANFD0RST_Pos         20
#define SYS_IPRST0_CANFD1RST_Pos         21
#define SYS_IPRST1_GPIORST_Pos           1
#define SYS_IPRST1_TMR0RST_Pos           2
#define SYS_IPRST1_TMR1RST_Pos           3
#define SYS_IPRST1_TMR2RST_Pos           4
#define SYS_IPRST1_TMR3RST_Pos           5
#define SYS_IPRST1_ACMP01RST_Pos         7
#define SYS_IPRST1_I2C0RST_Pos           8
#define SYS_IPRST1_I2C1RST_Pos           9
#define SYS_IPRST1_I2C2RST_Pos           10
#define SYS_IPRST1_I2C3RST_Pos           11
#define SYS_IPRST1_QSPI0RST_Pos          12
#define SYS_IPRST1_SPI0RST_Pos           13
#define SYS_IPRST1_SPI1RST_Pos           14
#define SYS_IPRST1_SPI2RST_Pos           15
#define SYS_IPRST1_UART0RST_Pos          16
#define SYS_IPRST1_UART1RST_Pos          17
#define SYS_IPRST1_UART2RST_Pos          18
#define SYS_IPRST1_UART3RST_Pos          19
#define SYS_IPRST1_UART4RST_Pos          20
#define SYS_IPRST1_UART5RST_Pos          21
#define SYS_IPRST1_UART6RST_Pos          22
#define SYS_IPRST1_UART7RST_Pos          23
#define SYS_IPRST1_OTGRST_Pos            26
#define SYS_IPRST1_USBDRST_Pos           27
#define SYS_IPRST1_EADC0RST_Pos          28
#define SYS_IPRST1_TRNGRST_Pos           31
#define SYS_IPRST2_SPI3RST_Pos           6
#define SYS_IPRST2_USCI0RST_Pos          8
#define SYS_IPRST2_USCI1RST_Pos          9
#define SYS_IPRST2_WWDTRST_Pos           11
#define SYS_IPRST2_DACRST_Pos            12
#define SYS_IPRST2_EPWM0RST_Pos          16
#define SYS_IPRST2_EPWM1RST_Pos          17
#define SYS_IPRST2_EQEI0RST_Pos          22
#define SYS_IPRST2_EQEI1RST_Pos          23
#define SYS_IPRST2_TKRST_Pos             25
#define SYS_IPRST2_ECAP0RST_Pos          26
#define SYS_IPRST2_ECAP1RST_Pos          27
#define SYS_IPRST3_ACMP2RST_Pos          7
#define SYS_IPRST3_PWM0RST_Pos           8
#define SYS_IPRST3_PWM1RST_Pos           9
#define SYS_IPRST3_UTCPD0RST_Pos         15

/* End of M2L31 BSP sys_reg.h reset module copy */

/* Beginning of M2L31 BSP sys.h reset module copy */

/*---------------------------------------------------------------------
 *  Module Reset Control Resister constant definitions.
 *---------------------------------------------------------------------
 */

#define NUMAKER_PDMA0_RST       ((0UL<<24) | SYS_IPRST0_PDMA0RST_Pos)
#define NUMAKER_EBI_RST         ((0UL<<24) | SYS_IPRST0_EBIRST_Pos)
#define NUMAKER_USBH_RST        ((0UL<<24) | SYS_IPRST0_USBHRST_Pos)
#define NUMAKER_CRC_RST         ((0UL<<24) | SYS_IPRST0_CRCRST_Pos)
#define NUMAKER_CRPT_RST        ((0UL<<24) | SYS_IPRST0_CRPTRST_Pos)
#define NUMAKER_CANFD0_RST      ((0UL<<24) | SYS_IPRST0_CANFD0RST_Pos)
#define NUMAKER_CANFD1_RST      ((0UL<<24) | SYS_IPRST0_CANFD1RST_Pos)

#define NUMAKER_GPIO_RST        ((4UL<<24) | SYS_IPRST1_GPIORST_Pos)
#define NUMAKER_TMR0_RST        ((4UL<<24) | SYS_IPRST1_TMR0RST_Pos)
#define NUMAKER_TMR1_RST        ((4UL<<24) | SYS_IPRST1_TMR1RST_Pos)
#define NUMAKER_TMR2_RST        ((4UL<<24) | SYS_IPRST1_TMR2RST_Pos)
#define NUMAKER_TMR3_RST        ((4UL<<24) | SYS_IPRST1_TMR3RST_Pos)
#define NUMAKER_ACMP01_RST      ((4UL<<24) | SYS_IPRST1_ACMP01RST_Pos)
#define NUMAKER_I2C0_RST        ((4UL<<24) | SYS_IPRST1_I2C0RST_Pos)
#define NUMAKER_I2C1_RST        ((4UL<<24) | SYS_IPRST1_I2C1RST_Pos)
#define NUMAKER_I2C2_RST        ((4UL<<24) | SYS_IPRST1_I2C2RST_Pos)
#define NUMAKER_I2C3_RST        ((4UL<<24) | SYS_IPRST1_I2C3RST_Pos)
#define NUMAKER_QSPI0_RST       ((4UL<<24) | SYS_IPRST1_QSPI0RST_Pos)
#define NUMAKER_SPI0_RST        ((4UL<<24) | SYS_IPRST1_SPI0RST_Pos)
#define NUMAKER_SPI1_RST        ((4UL<<24) | SYS_IPRST1_SPI1RST_Pos)
#define NUMAKER_SPI2_RST        ((4UL<<24) | SYS_IPRST1_SPI2RST_Pos)
#define NUMAKER_UART0_RST       ((4UL<<24) | SYS_IPRST1_UART0RST_Pos)
#define NUMAKER_UART1_RST       ((4UL<<24) | SYS_IPRST1_UART1RST_Pos)
#define NUMAKER_UART2_RST       ((4UL<<24) | SYS_IPRST1_UART2RST_Pos)
#define NUMAKER_UART3_RST       ((4UL<<24) | SYS_IPRST1_UART3RST_Pos)
#define NUMAKER_UART4_RST       ((4UL<<24) | SYS_IPRST1_UART4RST_Pos)
#define NUMAKER_UART5_RST       ((4UL<<24) | SYS_IPRST1_UART5RST_Pos)
#define NUMAKER_UART6_RST       ((4UL<<24) | SYS_IPRST1_UART6RST_Pos)
#define NUMAKER_UART7_RST       ((4UL<<24) | SYS_IPRST1_UART7RST_Pos)
#define NUMAKER_OTG_RST         ((4UL<<24) | SYS_IPRST1_OTGRST_Pos)
#define NUMAKER_USBD_RST        ((4UL<<24) | SYS_IPRST1_USBDRST_Pos)
#define NUMAKER_EADC0_RST       ((4UL<<24) | SYS_IPRST1_EADC0RST_Pos)
#define NUMAKER_TRNG_RST        ((4UL<<24) | SYS_IPRST1_TRNGRST_Pos)

#define NUMAKER_SPI3_RST        ((8UL<<24) | SYS_IPRST2_SPI3RST_Pos)
#define NUMAKER_USCI0_RST       ((8UL<<24) | SYS_IPRST2_USCI0RST_Pos)
#define NUMAKER_USCI1_RST       ((8UL<<24) | SYS_IPRST2_USCI1RST_Pos)
#define NUMAKER_WWDT_RST        ((8UL<<24) | SYS_IPRST2_WWDTRST_Pos)
#define NUMAKER_DAC_RST         ((8UL<<24) | SYS_IPRST2_DACRST_Pos)
#define NUMAKER_EPWM0_RST       ((8UL<<24) | SYS_IPRST2_EPWM0RST_Pos)
#define NUMAKER_EPWM1_RST       ((8UL<<24) | SYS_IPRST2_EPWM1RST_Pos)
#define NUMAKER_EQEI0_RST       ((8UL<<24) | SYS_IPRST2_EQEI0RST_Pos)
#define NUMAKER_EQEI1_RST       ((8UL<<24) | SYS_IPRST2_EQEI1RST_Pos)
#define NUMAKER_TK_RST          ((8UL<<24) | SYS_IPRST2_TKRST_Pos)
#define NUMAKER_ECAP0_RST       ((8UL<<24) | SYS_IPRST2_ECAP0RST_Pos)
#define NUMAKER_ECAP1_RST       ((8UL<<24) | SYS_IPRST2_ECAP1RST_Pos)

#define NUMAKER_ACMP2_RST       ((0x18UL<<24) | SYS_IPRST3_ACMP2RST_Pos)
#define NUMAKER_PWM0_RST        ((0x18UL<<24) | SYS_IPRST3_PWM0RST_Pos)
#define NUMAKER_PWM1_RST        ((0x18UL<<24) | SYS_IPRST3_PWM1RST_Pos)
#define NUMAKER_UTCPD0_RST      ((0x18UL<<24) | SYS_IPRST3_UTCPD0RST_Pos)

#define NUMAKER_LPPDMA0_RST     ((0x80UL<<24) | LPSCC_IPRST0_LPPDMA0RST_Pos)
#define NUMAKER_LPGPIO_RST      ((0x80UL<<24) | LPSCC_IPRST0_LPGPIORST_Pos)
#define NUMAKER_LPSRAM_RST      ((0x80UL<<24) | LPSCC_IPRST0_LPSRAMRST_Pos)
#define NUMAKER_WDT_RST         ((0x80UL<<24) | LPSCC_IPRST0_WDTRST_Pos)
#define NUMAKER_LPSPI0_RST      ((0x80UL<<24) | LPSCC_IPRST0_LPSPI0RST_Pos)
#define NUMAKER_LPI2C0_RST      ((0x80UL<<24) | LPSCC_IPRST0_LPI2C0RST_Pos)
#define NUMAKER_LPUART0_RST     ((0x80UL<<24) | LPSCC_IPRST0_LPUART0RST_Pos)
#define NUMAKER_LPTMR0_RST      ((0x80UL<<24) | LPSCC_IPRST0_LPTMR0RST_Pos)
#define NUMAKER_LPTMR1_RST      ((0x80UL<<24) | LPSCC_IPRST0_LPTMR1RST_Pos)
#define NUMAKER_TTMR0_RST       ((0x80UL<<24) | LPSCC_IPRST0_TTMR0RST_Pos)
#define NUMAKER_TTMR1_RST       ((0x80UL<<24) | LPSCC_IPRST0_TTMR1RST_Pos)
#define NUMAKER_LPADC0_RST      ((0x80UL<<24) | LPSCC_IPRST0_LPADC0RST_Pos)
#define NUMAKER_OPA_RST         ((0x80UL<<24) | LPSCC_IPRST0_OPARST_Pos)

/* End of M2L31 BSP sys.h reset module copy */





#endif
```

## 27.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nuvoton Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 41 行

复制自 M2L31 板级支持包（BSP）`sys_reg.h` 的复位模块（Reset Module）开始（Beginning）。

### 注释 3：原第 108 行

复制自 M2L31 板级支持包（BSP）`sys_reg.h` 的复位模块（Reset Module）结束（End）。

### 注释 4：原第 110 行

复制自 M2L31 板级支持包（BSP）`sys.h` 的复位模块（Reset Module）开始（Beginning）。

### 注释 5：原第 112 行

模块复位控制寄存器常量定义（Module Reset Control Register Constant Definitions）。原注释以分隔线标示此段。

### 注释 6：原第 184 行

复制自 M2L31 板级支持包（BSP）`sys.h` 的复位模块（Reset Module）结束（End）。

## 27.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P264_zephyr__dt-bindings__reset__numaker_m2l31x_reset.h_文件参考.md)

---

[上一章](P026_numaker_m031x_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P028_numaker_m333x_reset.h_源码浏览.md)
