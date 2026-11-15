---
id: learning.zephyr-docs.api-source-system-reference.page-31
title: numaker_m55m1x_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/numaker__m55m1x__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_numaker\_m55m1x\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/numaker__m55m1x__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P272_zephyr__dt-bindings__reset__numaker_m55m1x_reset.h_文件参考.md)。

## 31.1\_原始可见代码（Source Code）

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
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00249"></a>

```c
/*
 * Copyright (c) 2025 Nuvoton Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_NUMAKER_M55M1X_RESET_H
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_NUMAKER_M55M1X_RESET_H





/* Beginning of M55M1 BSP sys_reg.h reset module copy */

#define SYS_RSTCTL_CHIPRST_Pos           0
#define SYS_RSTCTL_NPURST_Pos            6
#define SYS_ACMPRST_ACMP01RST_Pos        0
#define SYS_ACMPRST_ACMP23RST_Pos        1
#define SYS_AWFRST_AWF0RST_Pos           0
#define SYS_BPWMRST_BPWM0RST_Pos         0
#define SYS_BPWMRST_BPWM1RST_Pos         1
#define SYS_CANFDRST_CANFD0RST_Pos       0
#define SYS_CANFDRST_CANFD1RST_Pos       1
#define SYS_CCAPRST_CCAP0RST_Pos         0
#define SYS_CRCRST_CRC0RST_Pos           0
#define SYS_CRYPTORST_CRYPTO0RST_Pos     0
#define SYS_DACRST_DAC01RST_Pos          0
#define SYS_DMICRST_DMIC0RST_Pos         0
#define SYS_EADCRST_EADC0RST_Pos         0
#define SYS_EBIRST_EBI0RST_Pos           0
#define SYS_ECAPRST_ECAP0RST_Pos         0
#define SYS_ECAPRST_ECAP1RST_Pos         1
#define SYS_ECAPRST_ECAP2RST_Pos         2
#define SYS_ECAPRST_ECAP3RST_Pos         3
#define SYS_EMACRST_EMAC0RST_Pos         0
#define SYS_EPWMRST_EPWM0RST_Pos         0
#define SYS_EPWMRST_EPWM1RST_Pos         1
#define SYS_EQEIRST_EQEI0RST_Pos         0
#define SYS_EQEIRST_EQEI1RST_Pos         1
#define SYS_EQEIRST_EQEI2RST_Pos         2
#define SYS_EQEIRST_EQEI3RST_Pos         3
#define SYS_FMCRST_FMC0RST_Pos           0
#define SYS_GDMARST_GDMA0RST_Pos         0
#define SYS_GPIORST_GPIO0RST_Pos         0
#define SYS_HSOTGRST_HSOTG0RST_Pos       0
#define SYS_HSUSBDRST_HSUSBD0RST_Pos     0
#define SYS_HSUSBHRST_HSUSBH0RST_Pos     0
#define SYS_I2CRST_I2C0RST_Pos           0
#define SYS_I2CRST_I2C1RST_Pos           1
#define SYS_I2CRST_I2C2RST_Pos           2
#define SYS_I2CRST_I2C3RST_Pos           3
#define SYS_I2SRST_I2S0RST_Pos           0
#define SYS_I2SRST_I2S1RST_Pos           1
#define SYS_I3CRST_I3C0RST_Pos           0
#define SYS_KDFRST_KDF0RST_Pos           0
#define SYS_KPIRST_KPI0RST_Pos           0
#define SYS_KSRST_KS0RST_Pos             0
#define SYS_LPADCRST_LPADC0RST_Pos       0
#define SYS_LPPDMARST_LPPDMA0RST_Pos     0
#define SYS_LPGPIORST_LPGPIO0RST_Pos     0
#define SYS_LPI2CRST_LPI2C0RST_Pos       0
#define SYS_LPSPIRST_LPSPI0RST_Pos       0
#define SYS_LPTMRRST_LPTMR0RST_Pos       0
#define SYS_LPTMRRST_LPTMR1RST_Pos       1
#define SYS_LPUARTRST_LPUART0RST_Pos     0
#define SYS_OTFCRST_OTFC0RST_Pos         0
#define SYS_OTGRST_OTG0RST_Pos           0
#define SYS_PDMARST_PDMA0RST_Pos         0
#define SYS_PDMARST_PDMA1RST_Pos         1
#define SYS_PSIORST_PSIO0RST_Pos         0
#define SYS_QSPIRST_QSPI0RST_Pos         0
#define SYS_QSPIRST_QSPI1RST_Pos         1
#define SYS_RTCRST_RTC0RST_Pos           0
#define SYS_SCRST_SC0RST_Pos             0
#define SYS_SCRST_SC1RST_Pos             1
#define SYS_SCRST_SC2RST_Pos             2
#define SYS_SCURST_SCU0RST_Pos           0
#define SYS_SDHRST_SDH0RST_Pos           0
#define SYS_SDHRST_SDH1RST_Pos           1
#define SYS_SPIRST_SPI0RST_Pos           0
#define SYS_SPIRST_SPI1RST_Pos           1
#define SYS_SPIRST_SPI2RST_Pos           2
#define SYS_SPIRST_SPI3RST_Pos           3
#define SYS_SPIMRST_SPIM0RST_Pos         0
#define SYS_TMRRST_TMR0RST_Pos           0
#define SYS_TMRRST_TMR1RST_Pos           1
#define SYS_TMRRST_TMR2RST_Pos           2
#define SYS_TMRRST_TMR3RST_Pos           3
#define SYS_TRNGRST_TRNG0RST_Pos         0
#define SYS_TTMRRST_TTMR0RST_Pos         0
#define SYS_TTMRRST_TTMR1RST_Pos         1
#define SYS_UARTRST_UART0RST_Pos         0
#define SYS_UARTRST_UART1RST_Pos         1
#define SYS_UARTRST_UART2RST_Pos         2
#define SYS_UARTRST_UART3RST_Pos         3
#define SYS_UARTRST_UART4RST_Pos         4
#define SYS_UARTRST_UART5RST_Pos         5
#define SYS_UARTRST_UART6RST_Pos         6
#define SYS_UARTRST_UART7RST_Pos         7
#define SYS_UARTRST_UART8RST_Pos         8
#define SYS_UARTRST_UART9RST_Pos         9
#define SYS_USBDRST_USBD0RST_Pos         0
#define SYS_USBHRST_USBH0RST_Pos         0
#define SYS_USCIRST_USCI0RST_Pos         0
#define SYS_UTCPDRST_UTCPD0RST_Pos       0
#define SYS_WWDTRST_WWDT0RST_Pos         0
#define SYS_WWDTRST_WWDT1RST_Pos         1

/* End of M55M1 BSP sys_reg.h reset module copy */

/* Beginning of M55M1 BSP sys.h reset module copy */

/*---------------------------------------------------------------------
 *  Module Reset Control Resister constant definitions.
 *---------------------------------------------------------------------
 */

#define NUMAKER_SYS_ACMP01RST       ((0x200UL<<20) | SYS_ACMPRST_ACMP01RST_Pos)
#define NUMAKER_SYS_ACMP23RST       ((0x200UL<<20) | SYS_ACMPRST_ACMP23RST_Pos)
#define NUMAKER_SYS_AWF0RST         ((0x204UL<<20) | SYS_AWFRST_AWF0RST_Pos)
#define NUMAKER_SYS_BPWM0RST        ((0x208UL<<20) | SYS_BPWMRST_BPWM0RST_Pos)
#define NUMAKER_SYS_BPWM1RST        ((0x208UL<<20) | SYS_BPWMRST_BPWM1RST_Pos)
#define NUMAKER_SYS_CANFD0RST       ((0x20CUL<<20) | SYS_CANFDRST_CANFD0RST_Pos)
#define NUMAKER_SYS_CANFD1RST       ((0x20CUL<<20) | SYS_CANFDRST_CANFD1RST_Pos)
#define NUMAKER_SYS_CCAP0RST        ((0x210UL<<20) | SYS_CCAPRST_CCAP0RST_Pos)
#define NUMAKER_SYS_CRC0RST         ((0x214UL<<20) | SYS_CRCRST_CRC0RST_Pos)
#define NUMAKER_SYS_CRYPTO0RST      ((0x218UL<<20) | SYS_CRYPTORST_CRYPTO0RST_Pos)
#define NUMAKER_SYS_DAC01RST        ((0x21CUL<<20) | SYS_DACRST_DAC01RST_Pos)
#define NUMAKER_SYS_DMIC0RST        ((0x220UL<<20) | SYS_DMICRST_DMIC0RST_Pos)
#define NUMAKER_SYS_EADC0RST        ((0x224UL<<20) | SYS_EADCRST_EADC0RST_Pos)
#define NUMAKER_SYS_EBI0RST         ((0x228UL<<20) | SYS_EBIRST_EBI0RST_Pos)
#define NUMAKER_SYS_ECAP0RST        ((0x22CUL<<20) | SYS_ECAPRST_ECAP0RST_Pos)
#define NUMAKER_SYS_ECAP1RST        ((0x22CUL<<20) | SYS_ECAPRST_ECAP1RST_Pos)
#define NUMAKER_SYS_ECAP2RST        ((0x22CUL<<20) | SYS_ECAPRST_ECAP2RST_Pos)
#define NUMAKER_SYS_ECAP3RST        ((0x22CUL<<20) | SYS_ECAPRST_ECAP3RST_Pos)
#define NUMAKER_SYS_EMAC0RST        ((0x230UL<<20) | SYS_EMACRST_EMAC0RST_Pos)
#define NUMAKER_SYS_EPWM0RST        ((0x234UL<<20) | SYS_EPWMRST_EPWM0RST_Pos)
#define NUMAKER_SYS_EPWM1RST        ((0x234UL<<20) | SYS_EPWMRST_EPWM1RST_Pos)
#define NUMAKER_SYS_EQEI0RST        ((0x238UL<<20) | SYS_EQEIRST_EQEI0RST_Pos)
#define NUMAKER_SYS_EQEI1RST        ((0x238UL<<20) | SYS_EQEIRST_EQEI1RST_Pos)
#define NUMAKER_SYS_EQEI2RST        ((0x238UL<<20) | SYS_EQEIRST_EQEI2RST_Pos)
#define NUMAKER_SYS_EQEI3RST        ((0x238UL<<20) | SYS_EQEIRST_EQEI3RST_Pos)
#define NUMAKER_SYS_FMC0RST         ((0x23CUL<<20) | SYS_FMCRST_FMC0RST_Pos)
#define NUMAKER_SYS_GDMA0RST        ((0x240UL<<20) | SYS_GDMARST_GDMA0RST_Pos)
#define NUMAKER_SYS_GPIO0RST        ((0x244UL<<20) | SYS_GPIORST_GPIO0RST_Pos)
#define NUMAKER_SYS_HSOTG0RST       ((0x248UL<<20) | SYS_HSOTGRST_HSOTG0RST_Pos)
#define NUMAKER_SYS_HSUSBD0RST      ((0x24CUL<<20) | SYS_HSUSBDRST_HSUSBD0RST_Pos)
#define NUMAKER_SYS_HSUSBH0RST      ((0x250UL<<20) | SYS_HSUSBHRST_HSUSBH0RST_Pos)
#define NUMAKER_SYS_I2C0RST         ((0x254UL<<20) | SYS_I2CRST_I2C0RST_Pos)
#define NUMAKER_SYS_I2C1RST         ((0x254UL<<20) | SYS_I2CRST_I2C1RST_Pos)
#define NUMAKER_SYS_I2C2RST         ((0x254UL<<20) | SYS_I2CRST_I2C2RST_Pos)
#define NUMAKER_SYS_I2C3RST         ((0x254UL<<20) | SYS_I2CRST_I2C3RST_Pos)
#define NUMAKER_SYS_I2S0RST         ((0x258UL<<20) | SYS_I2SRST_I2S0RST_Pos)
#define NUMAKER_SYS_I2S1RST         ((0x258UL<<20) | SYS_I2SRST_I2S1RST_Pos)
#define NUMAKER_SYS_I3C0RST         ((0x25CUL<<20) | SYS_I3CRST_I3C0RST_Pos)
#define NUMAKER_SYS_KDF0RST         ((0x260UL<<20) | SYS_KDFRST_KDF0RST_Pos)
#define NUMAKER_SYS_KPI0RST         ((0x264UL<<20) | SYS_KPIRST_KPI0RST_Pos)
#define NUMAKER_SYS_KS0RST          ((0x268UL<<20) | SYS_KSRST_KS0RST_Pos)
#define NUMAKER_SYS_LPADC0RST       ((0x26CUL<<20) | SYS_LPADCRST_LPADC0RST_Pos)
#define NUMAKER_SYS_LPPDMA0RST      ((0x270UL<<20) | SYS_LPPDMARST_LPPDMA0RST_Pos)
#define NUMAKER_SYS_LPGPIO0RST      ((0x274UL<<20) | SYS_LPGPIORST_LPGPIO0RST_Pos)
#define NUMAKER_SYS_LPI2C0RST       ((0x278UL<<20) | SYS_LPI2CRST_LPI2C0RST_Pos)
#define NUMAKER_SYS_LPSPI0RST       ((0x27CUL<<20) | SYS_LPSPIRST_LPSPI0RST_Pos)
#define NUMAKER_SYS_LPTMR0RST       ((0x280UL<<20) | SYS_LPTMRRST_LPTMR0RST_Pos)
#define NUMAKER_SYS_LPTMR1RST       ((0x280UL<<20) | SYS_LPTMRRST_LPTMR1RST_Pos)
#define NUMAKER_SYS_LPUART0RST      ((0x284UL<<20) | SYS_LPUARTRST_LPUART0RST_Pos)
#define NUMAKER_SYS_NPURST          ((0x004UL<<20) | SYS_RSTCTL_NPURST_Pos)
#define NUMAKER_SYS_OTFC0RST        ((0x288UL<<20) | SYS_OTFCRST_OTFC0RST_Pos)
#define NUMAKER_SYS_OTG0RST         ((0x28CUL<<20) | SYS_OTGRST_OTG0RST_Pos)
#define NUMAKER_SYS_PDMA0RST        ((0x290UL<<20) | SYS_PDMARST_PDMA0RST_Pos)
#define NUMAKER_SYS_PDMA1RST        ((0x290UL<<20) | SYS_PDMARST_PDMA1RST_Pos)
#define NUMAKER_SYS_PSIO0RST        ((0x294UL<<20) | SYS_PSIORST_PSIO0RST_Pos)
#define NUMAKER_SYS_QSPI0RST        ((0x298UL<<20) | SYS_QSPIRST_QSPI0RST_Pos)
#define NUMAKER_SYS_QSPI1RST        ((0x298UL<<20) | SYS_QSPIRST_QSPI1RST_Pos)
#define NUMAKER_SYS_RTC0RST         ((0x29CUL<<20) | SYS_RTCRST_RTC0RST_Pos)
#define NUMAKER_SYS_SC0RST          ((0x2A0UL<<20) | SYS_SCRST_SC0RST_Pos)
#define NUMAKER_SYS_SC1RST          ((0x2A0UL<<20) | SYS_SCRST_SC1RST_Pos)
#define NUMAKER_SYS_SC2RST          ((0x2A0UL<<20) | SYS_SCRST_SC2RST_Pos)
#define NUMAKER_SYS_SCU0RST         ((0x2A4UL<<20) | SYS_SCURST_SCU0RST_Pos)
#define NUMAKER_SYS_SDH0RST         ((0x2A8UL<<20) | SYS_SDHRST_SDH0RST_Pos)
#define NUMAKER_SYS_SDH1RST         ((0x2A8UL<<20) | SYS_SDHRST_SDH1RST_Pos)
#define NUMAKER_SYS_SPI0RST         ((0x2ACUL<<20) | SYS_SPIRST_SPI0RST_Pos)
#define NUMAKER_SYS_SPI1RST         ((0x2ACUL<<20) | SYS_SPIRST_SPI1RST_Pos)
#define NUMAKER_SYS_SPI2RST         ((0x2ACUL<<20) | SYS_SPIRST_SPI2RST_Pos)
#define NUMAKER_SYS_SPI3RST         ((0x2ACUL<<20) | SYS_SPIRST_SPI3RST_Pos)
#define NUMAKER_SYS_SPIM0RST        ((0x2B0UL<<20) | SYS_SPIMRST_SPIM0RST_Pos)
#define NUMAKER_SYS_TMR0RST         ((0x2C0UL<<20) | SYS_TMRRST_TMR0RST_Pos)
#define NUMAKER_SYS_TMR1RST         ((0x2C0UL<<20) | SYS_TMRRST_TMR1RST_Pos)
#define NUMAKER_SYS_TMR2RST         ((0x2C0UL<<20) | SYS_TMRRST_TMR2RST_Pos)
#define NUMAKER_SYS_TMR3RST         ((0x2C0UL<<20) | SYS_TMRRST_TMR3RST_Pos)
#define NUMAKER_SYS_TRNG0RST        ((0x2C4UL<<20) | SYS_TRNGRST_TRNG0RST_Pos)
#define NUMAKER_SYS_TTMR0RST        ((0x2C8UL<<20) | SYS_TTMRRST_TTMR0RST_Pos)
#define NUMAKER_SYS_TTMR1RST        ((0x2C8UL<<20) | SYS_TTMRRST_TTMR1RST_Pos)
#define NUMAKER_SYS_UART0RST        ((0x2CCUL<<20) | SYS_UARTRST_UART0RST_Pos)
#define NUMAKER_SYS_UART1RST        ((0x2CCUL<<20) | SYS_UARTRST_UART1RST_Pos)
#define NUMAKER_SYS_UART2RST        ((0x2CCUL<<20) | SYS_UARTRST_UART2RST_Pos)
#define NUMAKER_SYS_UART3RST        ((0x2CCUL<<20) | SYS_UARTRST_UART3RST_Pos)
#define NUMAKER_SYS_UART4RST        ((0x2CCUL<<20) | SYS_UARTRST_UART4RST_Pos)
#define NUMAKER_SYS_UART5RST        ((0x2CCUL<<20) | SYS_UARTRST_UART5RST_Pos)
#define NUMAKER_SYS_UART6RST        ((0x2CCUL<<20) | SYS_UARTRST_UART6RST_Pos)
#define NUMAKER_SYS_UART7RST        ((0x2CCUL<<20) | SYS_UARTRST_UART7RST_Pos)
#define NUMAKER_SYS_UART8RST        ((0x2CCUL<<20) | SYS_UARTRST_UART8RST_Pos)
#define NUMAKER_SYS_UART9RST        ((0x2CCUL<<20) | SYS_UARTRST_UART9RST_Pos)
#define NUMAKER_SYS_USBD0RST        ((0x2D0UL<<20) | SYS_USBDRST_USBD0RST_Pos)
#define NUMAKER_SYS_USBH0RST        ((0x2D4UL<<20) | SYS_USBHRST_USBH0RST_Pos)
#define NUMAKER_SYS_USCI0RST        ((0x2D8UL<<20) | SYS_USCIRST_USCI0RST_Pos)
#define NUMAKER_SYS_UTCPD0RST       ((0x2DCUL<<20) | SYS_UTCPDRST_UTCPD0RST_Pos)
#define NUMAKER_SYS_WWDT0RST        ((0x2E0UL<<20) | SYS_WWDTRST_WWDT0RST_Pos)
#define NUMAKER_SYS_WWDT1RST        ((0x2E0UL<<20) | SYS_WWDTRST_WWDT1RST_Pos)

/* End of M55M1 BSP sys.h reset module copy */





#endif
```

## 31.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Nuvoton Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 41 行

复制自 M55M1 板级支持包（BSP）`sys_reg.h` 的复位模块（Reset Module）开始（Beginning）。

### 注释 3：原第 137 行

复制自 M55M1 板级支持包（BSP）`sys_reg.h` 的复位模块（Reset Module）结束（End）。

### 注释 4：原第 139 行

复制自 M55M1 板级支持包（BSP）`sys.h` 的复位模块（Reset Module）开始（Beginning）。

### 注释 5：原第 141 行

模块复位控制寄存器常量定义（Module Reset Control Register Constant Definitions）。原注释以分隔线标示此段。

### 注释 6：原第 239 行

复制自 M55M1 板级支持包（BSP）`sys.h` 的复位模块（Reset Module）结束（End）。

## 31.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P272_zephyr__dt-bindings__reset__numaker_m55m1x_reset.h_文件参考.md)

---

[上一章](P030_numaker_m46x_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P032_numicro_m48x_reset.h_源码浏览.md)
