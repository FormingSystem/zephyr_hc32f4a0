---
id: learning.zephyr-docs.api-source-configuration-reference.page-66
title: pinctrl-r8a779g0.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a779g0_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_pinctrl-r8a779g0.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a779g0_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a779g0_8h.html)。

## 66.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
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
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="apinctrl-rcar-common_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A779G0_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A779G0_H_

#include "pinctrl-rcar-common.h"

/* Pins declaration */
#define PIN_NONE -1

#define PIN_GP0_00      RCAR_GP_PIN(0, 0)
#define PIN_GP0_01      RCAR_GP_PIN(0, 1)
#define PIN_GP0_02      RCAR_GP_PIN(0, 2)
#define PIN_IRQ3        RCAR_GP_PIN(0, 3)
#define PIN_IRQ2        RCAR_GP_PIN(0, 4)
#define PIN_IRQ1        RCAR_GP_PIN(0, 5)
#define PIN_IRQ0        RCAR_GP_PIN(0, 6)
#define PIN_MSIOF5_SS2  RCAR_GP_PIN(0, 7)
#define PIN_MSIOF5_SS1  RCAR_GP_PIN(0, 8)
#define PIN_MSIOF5_SYNC RCAR_GP_PIN(0, 9)
#define PIN_MSIOF5_TXD  RCAR_GP_PIN(0, 10)
#define PIN_MSIOF5_SCK  RCAR_GP_PIN(0, 11)
#define PIN_MSIOF5_RXD  RCAR_GP_PIN(0, 12)
#define PIN_MSIOF2_SS2  RCAR_GP_PIN(0, 13)
#define PIN_MSIOF2_SS1  RCAR_GP_PIN(0, 14)
#define PIN_MSIOF2_SYNC RCAR_GP_PIN(0, 15)
#define PIN_MSIOF2_TXD  RCAR_GP_PIN(0, 16)
#define PIN_MSIOF2_SCK  RCAR_GP_PIN(0, 17)
#define PIN_MSIOF2_RXD  RCAR_GP_PIN(0, 18)

#define PIN_MSIOF1_SS2   RCAR_GP_PIN(1, 0)
#define PIN_MSIOF1_SS1   RCAR_GP_PIN(1, 1)
#define PIN_MSIOF1_SYNC  RCAR_GP_PIN(1, 2)
#define PIN_MSIOF1_SCK   RCAR_GP_PIN(1, 3)
#define PIN_MSIOF1_TXD   RCAR_GP_PIN(1, 4)
#define PIN_MSIOF1_RXD   RCAR_GP_PIN(1, 5)
#define PIN_MSIOF0_SS2   RCAR_GP_PIN(1, 6)
#define PIN_MSIOF0_SS1   RCAR_GP_PIN(1, 7)
#define PIN_MSIOF0_SYNC  RCAR_GP_PIN(1, 8)
#define PIN_MSIOF0_TXD   RCAR_GP_PIN(1, 9)
#define PIN_MSIOF0_SCK   RCAR_GP_PIN(1, 10)
#define PIN_MSIOF0_RXD   RCAR_GP_PIN(1, 11)
#define PIN_HTX0         RCAR_GP_PIN(1, 12)
#define PIN_HCTS0_N      RCAR_GP_PIN(1, 13)
#define PIN_HRTS0_N      RCAR_GP_PIN(1, 14)
#define PIN_HSCK0        RCAR_GP_PIN(1, 15)
#define PIN_HRX0         RCAR_GP_PIN(1, 16)
#define PIN_SCIF_CLK     RCAR_GP_PIN(1, 17)
#define PIN_SSI_SCK      RCAR_GP_PIN(1, 18)
#define PIN_SSI_WS       RCAR_GP_PIN(1, 19)
#define PIN_SSI_SD       RCAR_GP_PIN(1, 20)
#define PIN_AUDIO_CLKOUT RCAR_GP_PIN(1, 21)
#define PIN_AUDIO_CLKIN  RCAR_GP_PIN(1, 22)
#define PIN_GP1_23       RCAR_GP_PIN(1, 23)
#define PIN_HRX3         RCAR_GP_PIN(1, 24)
#define PIN_HSCK3        RCAR_GP_PIN(1, 25)
#define PIN_HRTS3_N      RCAR_GP_PIN(1, 26)
#define PIN_HCTS3_N      RCAR_GP_PIN(1, 27)
#define PIN_HTX3         RCAR_GP_PIN(1, 28)

#define PIN_FXR_TXDA    RCAR_GP_PIN(2, 0)
#define PIN_FXR_TXENA_N RCAR_GP_PIN(2, 1)
#define PIN_RXDA_EXTFXR RCAR_GP_PIN(2, 2)
#define PIN_CLK_EXTFXR  RCAR_GP_PIN(2, 3)
#define PIN_RXDB_EXTFXR RCAR_GP_PIN(2, 4)
#define PIN_FXR_TXENB_N RCAR_GP_PIN(2, 5)
#define PIN_FXR_TXDB    RCAR_GP_PIN(2, 6)
#define PIN_TPU0T01     RCAR_GP_PIN(2, 7)
#define PIN_TPU0T00     RCAR_GP_PIN(2, 8)
#define PIN_CAN_CLK     RCAR_GP_PIN(2, 9)
#define PIN_CANFD0_TX   RCAR_GP_PIN(2, 10)
#define PIN_CANFD0_RX   RCAR_GP_PIN(2, 11)
#define PIN_CANFD2_TX   RCAR_GP_PIN(2, 12)
#define PIN_CANFD2_RX   RCAR_GP_PIN(2, 13)
#define PIN_CANFD3_TX   RCAR_GP_PIN(2, 14)
#define PIN_CANFD3_RX   RCAR_GP_PIN(2, 15)
#define PIN_CANFD4_TX   RCAR_GP_PIN(2, 16)
#define PIN_CANFD4_RX   RCAR_GP_PIN(2, 17)
#define PIN_CANFD7_TX   RCAR_GP_PIN(2, 18)
#define PIN_CANFD7_RX   RCAR_GP_PIN(2, 19)

#define PIN_MMC_SD_D1      RCAR_GP_PIN(3, 0)
#define PIN_MMC_SD_D0      RCAR_GP_PIN(3, 1)
#define PIN_MMC_SD_D2      RCAR_GP_PIN(3, 2)
#define PIN_MMC_SD_CLK     RCAR_GP_PIN(3, 3)
#define PIN_MMC_DS         RCAR_GP_PIN(3, 4)
#define PIN_MMC_SD_D3      RCAR_GP_PIN(3, 5)
#define PIN_MMC_D5         RCAR_GP_PIN(3, 6)
#define PIN_MMC_D4         RCAR_GP_PIN(3, 7)
#define PIN_MMC_D7         RCAR_GP_PIN(3, 8)
#define PIN_MMC_D6         RCAR_GP_PIN(3, 9)
#define PIN_MMC_SD_CMD     RCAR_GP_PIN(3, 10)
#define PIN_SD_CD          RCAR_GP_PIN(3, 11)
#define PIN_SD_WP          RCAR_GP_PIN(3, 12)
#define PIN_IPC_CLKIN      RCAR_GP_PIN(3, 13)
#define PIN_IPC_CLKOUT     RCAR_GP_PIN(3, 14)
#define PIN_QSPI0_SSL      RCAR_GP_PIN(3, 15)
#define PIN_QSPI0_IO3      RCAR_GP_PIN(3, 16)
#define PIN_QSPI0_IO2      RCAR_GP_PIN(3, 17)
#define PIN_QSPI0_MISO_IO1 RCAR_GP_PIN(3, 18)
#define PIN_QSPI0_MOSI_IO0 RCAR_GP_PIN(3, 19)
#define PIN_QSPI0_SPCLK    RCAR_GP_PIN(3, 20)
#define PIN_QSPI1_MOSI_IO0 RCAR_GP_PIN(3, 21)
#define PIN_QSPI1_SPCLK    RCAR_GP_PIN(3, 22)
#define PIN_QSPI1_MISO_IO1 RCAR_GP_PIN(3, 23)
#define PIN_QSPI1_IO2      RCAR_GP_PIN(3, 24)
#define PIN_QSPI1_SSL      RCAR_GP_PIN(3, 25)
#define PIN_QSPI1_IO3      RCAR_GP_PIN(3, 26)
#define PIN_RPC_RESET_N    RCAR_GP_PIN(3, 27)
#define PIN_RPC_WP_N       RCAR_GP_PIN(3, 28)
#define PIN_RPC_INT_N      RCAR_GP_PIN(3, 29)

#define PIN_TSN0_MDIO         RCAR_GP_PIN(4, 0)
#define PIN_TSN0_MDC          RCAR_GP_PIN(4, 1)
#define PIN_TSN0_AVTP_PPS1    RCAR_GP_PIN(4, 2)
#define PIN_TSN0_PHY_INT      RCAR_GP_PIN(4, 3)
#define PIN_TSN0_LINK         RCAR_GP_PIN(4, 4)
#define PIN_TSN0_AVTP_MATCH   RCAR_GP_PIN(4, 5)
#define PIN_TSN0_AVTP_CAPTURE RCAR_GP_PIN(4, 6)
#define PIN_TSN0_RX_CTL       RCAR_GP_PIN(4, 7)
#define PIN_TSN0_AVTP_PPS0    RCAR_GP_PIN(4, 8)
#define PIN_TSN0_TX_CTL       RCAR_GP_PIN(4, 9)
#define PIN_TSN0_RD0          RCAR_GP_PIN(4, 10)
#define PIN_TSN0_RXC          RCAR_GP_PIN(4, 11)
#define PIN_TSN0_TXC          RCAR_GP_PIN(4, 12)
#define PIN_TSN0_RD1          RCAR_GP_PIN(4, 13)
#define PIN_TSN0_TD1          RCAR_GP_PIN(4, 14)
#define PIN_TSN0_TD0          RCAR_GP_PIN(4, 15)
#define PIN_TSN0_RD3          RCAR_GP_PIN(4, 16)
#define PIN_TSN0_RD2          RCAR_GP_PIN(4, 17)
#define PIN_TSN0_TD3          RCAR_GP_PIN(4, 18)
#define PIN_TSN0_TD2          RCAR_GP_PIN(4, 19)
#define PIN_TSN0_TXCREFCLK    RCAR_GP_PIN(4, 20)
#define PIN_PCIE0_CLKREQ_N    RCAR_GP_PIN(4, 21)
#define PIN_PCIE1_CLKREQ_N    RCAR_GP_PIN(4, 22)
#define PIN_AVS0              RCAR_GP_PIN(4, 23)
#define PIN_AVS1              RCAR_GP_PIN(4, 24)

#define PIN_AVB2_AVTP_PPS     RCAR_GP_PIN(5, 0)
#define PIN_AVB2_AVTP_CAPTURE RCAR_GP_PIN(5, 1)
#define PIN_AVB2_AVTP_MATCH   RCAR_GP_PIN(5, 2)
#define PIN_AVB2_LINK         RCAR_GP_PIN(5, 3)
#define PIN_AVB2_PHY_INT      RCAR_GP_PIN(5, 4)
#define PIN_AVB2_MAGIC        RCAR_GP_PIN(5, 5)
#define PIN_AVB2_MDC          RCAR_GP_PIN(5, 6)
#define PIN_AVB2_TXCREFCLK    RCAR_GP_PIN(5, 7)
#define PIN_AVB2_TD3          RCAR_GP_PIN(5, 8)
#define PIN_AVB2_RD3          RCAR_GP_PIN(5, 9)
#define PIN_AVB2_MDIO         RCAR_GP_PIN(5, 10)
#define PIN_AVB2_TD2          RCAR_GP_PIN(5, 11)
#define PIN_AVB2_TD1          RCAR_GP_PIN(5, 12)
#define PIN_AVB2_RD1          RCAR_GP_PIN(5, 13)
#define PIN_AVB2_RD2          RCAR_GP_PIN(5, 14)
#define PIN_AVB2_TD0          RCAR_GP_PIN(5, 15)
#define PIN_AVB2_TXC          RCAR_GP_PIN(5, 16)
#define PIN_AVB2_RD0          RCAR_GP_PIN(5, 17)
#define PIN_AVB2_RXC          RCAR_GP_PIN(5, 18)
#define PIN_AVB2_TX_CTL       RCAR_GP_PIN(5, 19)
#define PIN_AVB2_RX_CTL       RCAR_GP_PIN(5, 20)

#define PIN_SCL0   RCAR_GP_PIN(8, 0)
#define PIN_SDA0   RCAR_GP_PIN(8, 1)
#define PIN_SCL1   RCAR_GP_PIN(8, 2)
#define PIN_SDA1   RCAR_GP_PIN(8, 3)
#define PIN_SCL2   RCAR_GP_PIN(8, 4)
#define PIN_SDA2   RCAR_GP_PIN(8, 5)
#define PIN_SCL3   RCAR_GP_PIN(8, 6)
#define PIN_SDA3   RCAR_GP_PIN(8, 7)
#define PIN_SCL4   RCAR_GP_PIN(8, 8)
#define PIN_SDA4   RCAR_GP_PIN(8, 9)
#define PIN_SCL5   RCAR_GP_PIN(8, 10)
#define PIN_SDA5   RCAR_GP_PIN(8, 11)
#define PIN_GP8_12 RCAR_GP_PIN(8, 12)
#define PIN_GP8_13 RCAR_GP_PIN(8, 13)

/* Pinmux function declarations */
#define FUNC_HTX1              IP1SR0(24, 0x1)
#define FUNC_HRX1              IP1SR0(28, 0x1)
#define FUNC_HCTS1             IP2SR0(0, 0x1)
#define FUNC_HRTS1             IP2SR0(4, 0x1)
#define FUNC_MSIOF1_SYNC       IP0SR1(8, 0x0)
#define FUNC_MSIOF1_SCK        IP0SR1(12, 0x0)
#define FUNC_MSIOF1_TXD        IP0SR1(16, 0x0)
#define FUNC_MSIOF1_RXD        IP0SR1(20, 0x0)
#define FUNC_MSIOF0_SS1        IP0SR1(28, 0x0)
#define FUNC_MSIOF0_SYNC       IP1SR1(0, 0x0)
#define FUNC_MSIOF0_TXD        IP1SR1(4, 0x0)
#define FUNC_MSIOF0_SCK        IP1SR1(8, 0x0)
#define FUNC_MSIOF0_RXD        IP1SR1(12, 0x0)
#define FUNC_TX0               IP1SR1(16, 0x1)
#define FUNC_HTX0              IP1SR1(16, 0x0)
#define FUNC_HCTS0             IP1SR1(20, 0x1)
#define FUNC_HRTS0             IP1SR1(24, 0x1)
#define FUNC_PWM0              IP1SR1(28, 0x2)
#define FUNC_HRX0              IP2SR1(0, 0x0)
#define FUNC_RX0               IP2SR1(0, 0x1)
#define FUNC_SCIF_CLK          IP2SR1(4, 0x0)
#define FUNC_AUDIO_CLKOUT      IP2SR1(20, 0x0)
#define FUNC_TPU0TO0           IP3SR1(4, 0x3)
#define FUNC_TPU0TO1           IP3SR1(8, 0x3)
#define FUNC_CAN_CLK           IP1SR2(4, 0x0)
#define FUNC_CANFD3_TX         IP1SR2(24, 0x0)
#define FUNC_CANFD3_RX         IP1SR2(28, 0x0)
#define FUNC_CANFD4_TX         IP2SR2(0, 0x0)
#define FUNC_CANFD4_RX         IP2SR2(4, 0x0)
#define FUNC_MMC_SD_D1         IP0SR3(0, 0x0)
#define FUNC_MMC_SD_D0         IP0SR3(4, 0x0)
#define FUNC_MMC_SD_D2         IP0SR3(8, 0x0)
#define FUNC_MMC_SD_CLK        IP0SR3(12, 0x0)
#define FUNC_MMC_DS            IP0SR3(16, 0x0)
#define FUNC_MMC_SD_D3         IP0SR3(20, 0x0)
#define FUNC_MMC_D5            IP0SR3(24, 0x0)
#define FUNC_MMC_D4            IP0SR3(28, 0x0)
#define FUNC_MMC_D7            IP1SR3(0, 0x0)
#define FUNC_MMC_D6            IP1SR3(4, 0x0)
#define FUNC_MMC_SD_CMD        IP1SR3(8, 0x0)
#define FUNC_SD_CD             IP1SR3(12, 0x0)
#define FUNC_SD_WP             IP1SR3(16, 0x0)
#define FUNC_QSPI0_SSL         IP1SR3(28, 0x0)
#define FUNC_QSPI0_IO3         IP2SR3(0, 0x0)
#define FUNC_QSPI0_IO2         IP2SR3(4, 0x0)
#define FUNC_QSPI0_MISO_IO1    IP2SR3(8, 0x0)
#define FUNC_QSPI0_MOSI_IO0    IP2SR3(12, 0x0)
#define FUNC_QSPI0_SPCLK       IP2SR3(16, 0x0)
#define FUNC_QSPI1_MOSI_IO0    IP2SR3(20, 0x0)
#define FUNC_QSPI1_SPCLK       IP2SR3(24, 0x0)
#define FUNC_QSPI1_MISO_IO1    IP2SR3(28, 0x0)
#define FUNC_QSPI1_IO2         IP3SR3(0, 0x0)
#define FUNC_QSPI1_SSL         IP3SR3(4, 0x0)
#define FUNC_QSPI1_IO3         IP3SR3(8, 0x0)
#define FUNC_RPC_RESET         IP3SR3(12, 0x0)
#define FUNC_RPC_WP            IP3SR3(16, 0x0)
#define FUNC_RPC_INT           IP3SR3(20, 0x0)
#define FUNC_PCIE0_CLKREQ      IP2SR4(20, 0x0)
#define FUNC_PCIE1_CLKREQ      IP2SR4(24, 0x0)
#define FUNC_AVS0              IP2SR4(28, 0x0)
#define FUNC_AVS1              IP3SR4(0, 0x0)
#define FUNC_AVB0_AVTP_PPS     IP0SR7(0, 0x0)
#define FUNC_AVB0_AVTP_CAPTURE IP0SR7(4, 0x0)
#define FUNC_AVB0_AVTP_MATCH   IP0SR7(8, 0x0)
#define FUNC_AVB0_TD3          IP0SR7(12, 0x0)
#define FUNC_AVB0_LINK         IP0SR7(16, 0x0)
#define FUNC_AVB0_PHY_INT      IP0SR7(20, 0x0)
#define FUNC_AVB0_TD2          IP0SR7(24, 0x0)
#define FUNC_AVB0_TD1          IP0SR7(28, 0x0)
#define FUNC_AVB0_RD3          IP1SR7(0, 0x0)
#define FUNC_AVB0_TXCREFCLK    IP1SR7(4, 0x0)
#define FUNC_AVB0_MAGIC        IP1SR7(8, 0x0)
#define FUNC_AVB0_TD0          IP1SR7(12, 0x0)
#define FUNC_AVB0_RD2          IP1SR7(16, 0x0)
#define FUNC_AVB0_MDC          IP1SR7(20, 0x0)
#define FUNC_AVB0_MDIO         IP1SR7(24, 0x0)
#define FUNC_AVB0_TXC          IP1SR7(28, 0x0)
#define FUNC_AVB0_TX_CTL       IP2SR7(0, 0x0)
#define FUNC_AVB0_RD1          IP2SR7(4, 0x0)
#define FUNC_AVB0_RD0          IP2SR7(8, 0x0)
#define FUNC_AVB0_RXC          IP2SR7(12, 0x0)
#define FUNC_AVB0_RX_CTL       IP2SR7(16, 0x0)
#define FUNC_SCL0              IP0SR8(0, 0x0)
#define FUNC_SDA0              IP0SR8(4, 0x0)
#define FUNC_SCL1              IP0SR8(8, 0x0)
#define FUNC_SDA1              IP0SR8(12, 0x0)
#define FUNC_SCL2              IP0SR8(16, 0x0)
#define FUNC_SDA2              IP0SR8(20, 0x0)
#define FUNC_SCL3              IP0SR8(24, 0x0)
#define FUNC_SDA3              IP0SR8(28, 0x0)
#define FUNC_SCL4              IP1SR8(0, 0x0)
#define FUNC_SDA4              IP1SR8(4, 0x0)
#define FUNC_SCL5              IP1SR8(8, 0x0)
#define FUNC_SDA5              IP1SR8(12, 0x0)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A779G0_H_ */
```

## 66.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 23 行

引脚声明（Pins declaration）。

### 注释 3：原第 191 行

引脚复用功能声明（Pinmux function declarations）。

### 注释 4：原第 288 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_R8A779G0_H_`。

## 66.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-r8a779g0_8h.html)
- [pinctrl-rcar-common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rcar-common_8h.html)

---

[上一章](P065_pinctrl-r8a779f0.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P067_pinctrl-ra0.h_源码浏览.md)
