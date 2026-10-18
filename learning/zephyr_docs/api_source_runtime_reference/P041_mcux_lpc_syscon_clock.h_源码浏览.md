---
id: learning.zephyr-docs.api-source-runtime-reference.page-41
title: mcux_lpc_syscon_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpc__syscon__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_mcux\_lpc\_syscon\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpc__syscon__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpc__syscon__clock_8h.html)。

## 41.1\_原始可见代码（Source Code）

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
<a id="l00103"></a>
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
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00195"></a>
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
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>

```c
/*
 * Copyright 2020-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCUX_LPC_SYSCON_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCUX_LPC_SYSCON_CLOCK_H_

/* Note- clock identifiers in this file must be unique,
 * as the driver uses them in a switch case
 */

#define MCUX_LPC_CLK_ID(high, low) ((high << 8) | (low))

/* These IDs are used within SOC macros, and thus cannot be defined
 * using the standard MCUX_LPC_CLK_ID form
 */
#define MCUX_CTIMER0_CLK 0
#define MCUX_CTIMER1_CLK 1
#define MCUX_CTIMER2_CLK 2
#define MCUX_CTIMER3_CLK 3
#define MCUX_CTIMER4_CLK 4
#define MCUX_CTIMER5_CLK 5
#define MCUX_CTIMER6_CLK 6
#define MCUX_CTIMER7_CLK 7

#define MCUX_FLEXCOMM0_CLK  MCUX_LPC_CLK_ID(0x01, 0x00)
#define MCUX_FLEXCOMM1_CLK  MCUX_LPC_CLK_ID(0x01, 0x01)
#define MCUX_FLEXCOMM2_CLK  MCUX_LPC_CLK_ID(0x01, 0x02)
#define MCUX_FLEXCOMM3_CLK  MCUX_LPC_CLK_ID(0x01, 0x03)
#define MCUX_FLEXCOMM4_CLK  MCUX_LPC_CLK_ID(0x01, 0x04)
#define MCUX_FLEXCOMM0_LP_CLK  MCUX_LPC_CLK_ID(0x01, 0x80)
#define MCUX_FLEXCOMM1_LP_CLK  MCUX_LPC_CLK_ID(0x01, 0x81)
#define MCUX_FLEXCOMM2_LP_CLK  MCUX_LPC_CLK_ID(0x01, 0x82)
#define MCUX_FLEXCOMM3_LP_CLK  MCUX_LPC_CLK_ID(0x01, 0x83)
#define MCUX_FLEXCOMM5_CLK  MCUX_LPC_CLK_ID(0x01, 0x05)
#define MCUX_FLEXCOMM6_CLK  MCUX_LPC_CLK_ID(0x01, 0x06)
#define MCUX_FLEXCOMM7_CLK  MCUX_LPC_CLK_ID(0x01, 0x07)
#define MCUX_FLEXCOMM8_CLK  MCUX_LPC_CLK_ID(0x01, 0x08)
#define MCUX_FLEXCOMM9_CLK  MCUX_LPC_CLK_ID(0x01, 0x09)
#define MCUX_FLEXCOMM10_CLK MCUX_LPC_CLK_ID(0x01, 0x0A)
#define MCUX_FLEXCOMM11_CLK MCUX_LPC_CLK_ID(0x01, 0x0B)
#define MCUX_FLEXCOMM12_CLK MCUX_LPC_CLK_ID(0x01, 0x0C)
#define MCUX_FLEXCOMM13_CLK MCUX_LPC_CLK_ID(0x01, 0x0D)
#define MCUX_HS_SPI_CLK     MCUX_LPC_CLK_ID(0x01, 0x0E)
#define MCUX_FLEXCOMM14_CLK MCUX_HS_SPI_CLK
#define MCUX_PMIC_I2C_CLK   MCUX_LPC_CLK_ID(0x01, 0x0F)
#define MCUX_HS_SPI1_CLK    MCUX_LPC_CLK_ID(0x01, 0x10)
#define MCUX_FLEXCOMM17_CLK MCUX_LPC_CLK_ID(0x01, 0x11)
#define MCUX_FLEXCOMM18_CLK MCUX_LPC_CLK_ID(0x01, 0x12)
#define MCUX_FLEXCOMM19_CLK MCUX_LPC_CLK_ID(0x01, 0x13)
#define MCUX_FLEXCOMM20_CLK MCUX_LPC_CLK_ID(0x01, 0x14)
/* On RT7xx, flexcomm14 and 16 only can be LPSPI, flexcomm15 only can be I2C. */
#define MCUX_LPSPI14_CLK    MCUX_LPC_CLK_ID(0x01, 0x24)
#define MCUX_LPI2C15_CLK    MCUX_LPC_CLK_ID(0x01, 0x25)
#define MCUX_LPSPI16_CLK    MCUX_LPC_CLK_ID(0x01, 0x26)
#define MCUX_USDHC1_CLK     MCUX_LPC_CLK_ID(0x02, 0x00)
#define MCUX_USDHC2_CLK     MCUX_LPC_CLK_ID(0x02, 0x01)

#define MCUX_MCAN_CLK MCUX_LPC_CLK_ID(0x03, 0x00)
#define MCUX_MCAN1_CLK MCUX_LPC_CLK_ID(0x03, 0x01)

#define MCUX_BUS_CLK MCUX_LPC_CLK_ID(0x04, 0x00)

#define MCUX_SDIF_CLK MCUX_LPC_CLK_ID(0x05, 0x00)

#define MCUX_I3C_CLK MCUX_LPC_CLK_ID(0x06, 0x00)
#define MCUX_I3C2_CLK MCUX_LPC_CLK_ID(0x06, 0x01)
#define MCUX_I3C3_CLK MCUX_LPC_CLK_ID(0x06, 0x02)
#define MCUX_I3C4_CLK MCUX_LPC_CLK_ID(0x06, 0x03)

#define MCUX_MIPI_DSI_DPHY_CLK MCUX_LPC_CLK_ID(0x07, 0x00)
#define MCUX_MIPI_DSI_ESC_CLK  MCUX_LPC_CLK_ID(0x07, 0x01)

#define MCUX_LCDIF_PIXEL_CLK MCUX_LPC_CLK_ID(0x08, 0x00)

#define MCUX_SCTIMER_CLK MCUX_LPC_CLK_ID(0x09, 0x00)

#define MCUX_DMIC_CLK MCUX_LPC_CLK_ID(0x0A, 0x00)

#define MCUX_MRT_CLK     MCUX_LPC_CLK_ID(0x0B, 0x00)
#define MCUX_FREEMRT_CLK MCUX_LPC_CLK_ID(0x0B, 0x01)

#define MCUX_PORT0_CLK MCUX_LPC_CLK_ID(0x0C, 0x00)
#define MCUX_PORT1_CLK MCUX_LPC_CLK_ID(0x0C, 0x01)
#define MCUX_PORT2_CLK MCUX_LPC_CLK_ID(0x0C, 0x02)
#define MCUX_PORT3_CLK MCUX_LPC_CLK_ID(0x0C, 0x03)
#define MCUX_PORT4_CLK MCUX_LPC_CLK_ID(0x0C, 0x04)
#define MCUX_PORT5_CLK MCUX_LPC_CLK_ID(0x0C, 0x05)

#define MCUX_ENET_QOS_CLK MCUX_LPC_CLK_ID(0x0D, 0x00)

#define MCUX_ENET_CLK MCUX_LPC_CLK_ID(0x0D, 0x80)
#define MCUX_ENET_PLL MCUX_LPC_CLK_ID(0x0D, 0x81)

#define MCUX_LCDIC_CLK MCUX_LPC_CLK_ID(0x0E, 0x00)

#define MCUX_LPADC1_CLK MCUX_LPC_CLK_ID(0x0F, 0x00)
#define MCUX_LPADC2_CLK MCUX_LPC_CLK_ID(0x0F, 0x01)
#define MCUX_LPADC3_CLK MCUX_LPC_CLK_ID(0x0F, 0x02)
#define MCUX_LPADC4_CLK MCUX_LPC_CLK_ID(0x0F, 0x03)

#define MCUX_FLEXCAN0_CLK MCUX_LPC_CLK_ID(0x10, 0x00)
#define MCUX_FLEXCAN1_CLK MCUX_LPC_CLK_ID(0x10, 0x01)

#define MCUX_FLEXIO0_CLK MCUX_LPC_CLK_ID(0x11, 0x00)

#define MCUX_AUDIO_MCLK MCUX_LPC_CLK_ID(0x12, 0x00)

#define MCUX_LPUART0_CLK MCUX_LPC_CLK_ID(0x13, 0x00)
#define MCUX_LPUART1_CLK MCUX_LPC_CLK_ID(0x13, 0x01)
#define MCUX_LPUART2_CLK MCUX_LPC_CLK_ID(0x13, 0x02)
#define MCUX_LPUART3_CLK MCUX_LPC_CLK_ID(0x13, 0x03)
#define MCUX_LPUART4_CLK MCUX_LPC_CLK_ID(0x13, 0x04)
#define MCUX_LPUART5_CLK MCUX_LPC_CLK_ID(0x13, 0x05)

#define MCUX_LPI2C0_CLK MCUX_LPC_CLK_ID(0x14, 0x00)
#define MCUX_LPI2C1_CLK MCUX_LPC_CLK_ID(0x14, 0x01)
#define MCUX_LPI2C2_CLK MCUX_LPC_CLK_ID(0x14, 0x02)
#define MCUX_LPI2C3_CLK MCUX_LPC_CLK_ID(0x14, 0x03)
#define MCUX_LPI2C4_CLK MCUX_LPC_CLK_ID(0x14, 0x04)

#define MCUX_XSPI_CLK  MCUX_LPC_CLK_ID(0x15, 0x00)
#define MCUX_XSPI0_CLK MCUX_LPC_CLK_ID(0x15, 0x00)
#define MCUX_XSPI1_CLK MCUX_LPC_CLK_ID(0x15, 0x01)
#define MCUX_XSPI2_CLK MCUX_LPC_CLK_ID(0x15, 0x02)

#define MCUX_SAI0_CLK MCUX_LPC_CLK_ID(0x16, 0x00)
#define MCUX_SAI1_CLK MCUX_LPC_CLK_ID(0x16, 0x01)
#define MCUX_SAI2_CLK MCUX_LPC_CLK_ID(0x16, 0x02)

#define MCUX_LPSPI0_CLK MCUX_LPC_CLK_ID(0x17, 0x00)
#define MCUX_LPSPI1_CLK MCUX_LPC_CLK_ID(0x17, 0x01)
#define MCUX_LPSPI2_CLK MCUX_LPC_CLK_ID(0x17, 0x02)
#define MCUX_LPSPI3_CLK MCUX_LPC_CLK_ID(0x17, 0x03)
#define MCUX_LPSPI4_CLK MCUX_LPC_CLK_ID(0x17, 0x04)
#define MCUX_LPSPI5_CLK MCUX_LPC_CLK_ID(0x17, 0x05)

#define MCUX_OPAMP0_CLK MCUX_LPC_CLK_ID(0x18, 0x00)
#define MCUX_OPAMP1_CLK MCUX_LPC_CLK_ID(0x18, 0x01)
#define MCUX_OPAMP2_CLK MCUX_LPC_CLK_ID(0x18, 0x02)
#define MCUX_OPAMP3_CLK MCUX_LPC_CLK_ID(0x18, 0x03)

#define MCUX_ELS_CLK MCUX_LPC_CLK_ID(0x19, 0x0)

#define MCUX_TRNG_CLK MCUX_LPC_CLK_ID(0x1A, 0x0)

#define MCUX_MICFIL_CLK MCUX_LPC_CLK_ID(0x20, 0x00)

#define MCUX_HSCMP0_CLK MCUX_LPC_CLK_ID(0x21, 0x00)
#define MCUX_HSCMP1_CLK MCUX_LPC_CLK_ID(0x21, 0x01)
#define MCUX_HSCMP2_CLK MCUX_LPC_CLK_ID(0x21, 0x02)

#define MCUX_LPCMP0_CLK MCUX_LPC_CLK_ID(0x22, 0x00)
#define MCUX_LPCMP1_CLK MCUX_LPC_CLK_ID(0x22, 0x01)
#define MCUX_LPCMP2_CLK MCUX_LPC_CLK_ID(0x22, 0x02)

#define MCUX_SEMA42_CLK MCUX_LPC_CLK_ID(0x23, 0x00)

#define MCUX_FLEXSPI_CLK  MCUX_LPC_CLK_ID(0x24, 0x00)
#define MCUX_FLEXSPI2_CLK MCUX_LPC_CLK_ID(0x24, 0x01)

#define MCUX_TSI_CLK MCUX_LPC_CLK_ID(0x25, 0x0)

#define MCUX_WWDT0_CLK MCUX_LPC_CLK_ID(0x26, 0x00)
#define MCUX_WWDT1_CLK MCUX_LPC_CLK_ID(0x26, 0x01)

#define MCUX_ENET_QOS_PTP_CLK MCUX_LPC_CLK_ID(0x27, 0x00)

#define MCUX_USB0_CLK MCUX_LPC_CLK_ID(0x28, 0x00)
#define MCUX_USB1_CLK MCUX_LPC_CLK_ID(0x28, 0x01)
#define MCUX_USBPHY_REF_CLK MCUX_LPC_CLK_ID(0x28, 0x02)

#define MCUX_EDMA0_CLK MCUX_LPC_CLK_ID(0x29, 0x00)
#define MCUX_EDMA1_CLK MCUX_LPC_CLK_ID(0x29, 0x01)

#define MCUX_ACMP0_CLK MCUX_LPC_CLK_ID(0x30, 0x00)

#define MCUX_LCDIF_CLK MCUX_LPC_CLK_ID(0x31, 0x00)

#define MCUX_GPIO0_CLK MCUX_LPC_CLK_ID(0x32, 0x00)
#define MCUX_GPIO1_CLK MCUX_LPC_CLK_ID(0x32, 0x01)
#define MCUX_GPIO2_CLK MCUX_LPC_CLK_ID(0x32, 0x02)
#define MCUX_GPIO3_CLK MCUX_LPC_CLK_ID(0x32, 0x03)
#define MCUX_GPIO4_CLK MCUX_LPC_CLK_ID(0x32, 0x04)
#define MCUX_GPIO5_CLK MCUX_LPC_CLK_ID(0x32, 0x05)
#define MCUX_GPIO6_CLK MCUX_LPC_CLK_ID(0x32, 0x06)
#define MCUX_GPIO7_CLK MCUX_LPC_CLK_ID(0x32, 0x07)
#define MCUX_GPIO8_CLK MCUX_LPC_CLK_ID(0x32, 0x08)
#define MCUX_GPIO9_CLK MCUX_LPC_CLK_ID(0x32, 0x09)
#define MCUX_GPIO10_CLK MCUX_LPC_CLK_ID(0x32, 0x0A)

#define MCUX_IOCON0_CLK MCUX_LPC_CLK_ID(0x33, 0x00)
#define MCUX_IOCON1_CLK MCUX_LPC_CLK_ID(0x33, 0x01)
#define MCUX_IOCON2_CLK MCUX_LPC_CLK_ID(0x33, 0x02)

#define MCUX_SLCD_CLK MCUX_LPC_CLK_ID(0x34, 0x00)

#define MCUX_CRC_CLK MCUX_LPC_CLK_ID(0x35, 0x00)

#define MCUX_SYSTEM_CLK MCUX_LPC_CLK_ID(0x36, 0x00)

#define MCUX_EQDC_CLK MCUX_LPC_CLK_ID(0x37, 0x00)
#define MCUX_EQDC0_CLK MCUX_LPC_CLK_ID(0x38, 0x00)
#define MCUX_EQDC1_CLK MCUX_LPC_CLK_ID(0x38, 0x01)

#define MCUX_POWERQUAD_CLK MCUX_LPC_CLK_ID(0x39, 0x00)

#define MCUX_AON_LPADC_CLK MCUX_LPC_CLK_ID(0x3A, 0x00)

#define MCUX_LPACMP_CLK MCUX_LPC_CLK_ID(0x3B, 0x00)

#define MCUX_FRO_HF_CLK MCUX_LPC_CLK_ID(0x40, 0x00)

#define MCUX_FRO_HF_DIV_CLK MCUX_LPC_CLK_ID(0x41, 0x00)

#define MCUX_FRO_12M_CLK MCUX_LPC_CLK_ID(0x42, 0x00)

#define MCUX_FREQME_CLK MCUX_LPC_CLK_ID(0x43, 0x00)

#define MCUX_CPU_AHB_CLK MCUX_LPC_CLK_ID(0x44, 0x00)

#define MCUX_EXT_CLK MCUX_LPC_CLK_ID(0x45, 0x00)

#define MCUX_ESPI0_CLK MCUX_LPC_CLK_ID(0x46, 0x00)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCUX_LPC_SYSCON_CLOCK_H_ */
```

## 41.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2020-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

注意：本文件中的时钟标识符必须唯一，因为驱动会在 `switch case` 中使用它们。

### 注释 3：原第 16 行

这些 ID 在 SoC 宏内部使用，因此不能采用标准 `MCUX_LPC_CLK_ID` 形式定义。

### 注释 4：原第 54 行

在 RT7xx 上，flexcomm14 和 flexcomm16 只能作为 LPSPI，flexcomm15 只能作为 I2C。

### 注释 5：原第 273 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MCUX_LPC_SYSCON_CLOCK_H_`。

## 41.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpc__syscon__clock_8h.html)

---

[上一章](P040_lwm2m.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P042_media_proxy.h_源码浏览.md)
