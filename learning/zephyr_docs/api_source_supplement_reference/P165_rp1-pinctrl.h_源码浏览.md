---
id: learning.zephyr-docs.api-source-supplement-reference.page-165
title: rp1-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rp1-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第165章\_rp1-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rp1-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rp1-pinctrl_8h.html)。

## 165.1\_原始可见代码（Source Code）

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
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00073"></a>
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
<a id="l00114"></a>
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
<a id="l00154"></a>
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
<a id="l00194"></a>
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
<a id="l00232"></a>
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
<a id="l00265"></a>
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
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00305"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00345"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00385"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00425"></a>
<a id="l00429"></a>
<a id="l00430"></a>

```c
/*
 * Copyright (c) 2025 TOKITA Hiroshi
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_DT_BINDINGS_PINCTRL_RP1_PINCTRL_H_
#define ZEPHYR_DT_BINDINGS_PINCTRL_RP1_PINCTRL_H_


#define RP1_ALT_FUNC_POS  0
#define RP1_ALT_FUNC_MASK 0x1f

#define RP1_PIN_NUM_POS  5
#define RP1_PIN_NUM_MASK 0x1f

/* RP1 pinmux encoding does not include a bank selector. */
#define RP1_BANK_POS  0
#define RP1_BANK_MASK 0x0

#define RP1_FUNC_ALT0 0
#define RP1_FUNC_ALT1 1
#define RP1_FUNC_ALT2 2
#define RP1_FUNC_ALT3 3
#define RP1_FUNC_ALT4 4
#define RP1_FUNC_ALT5 5
#define RP1_FUNC_ALT6 6
#define RP1_FUNC_ALT7 7
#define RP1_FUNC_ALT8 8
#define RP1_FUNC_NULL 31

#define RP1_PINMUX(pin, func) (((pin) << RP1_PIN_NUM_POS) | ((func) << RP1_ALT_FUNC_POS))

#define RP1_GET_BANK(pinctrl) (((pinctrl) >> RP1_BANK_POS) & RP1_BANK_MASK)
#define RP1_GET_PIN(pinctrl)  (((pinctrl) >> RP1_PIN_NUM_POS) & RP1_PIN_NUM_MASK)
#define RP1_GET_FUNC(pinctrl) (((pinctrl) >> RP1_ALT_FUNC_POS) & RP1_ALT_FUNC_MASK)

#define RP1_GPIO_OVERRIDE_NORMAL 0
#define RP1_GPIO_OVERRIDE_INVERT 1
#define RP1_GPIO_OVERRIDE_LOW    2
#define RP1_GPIO_OVERRIDE_HIGH   3



#define RP1_SPI0_SIO3_P0      RP1_PINMUX(0, RP1_FUNC_ALT0)
#define RP1_SPI0_SIO2_P1      RP1_PINMUX(1, RP1_FUNC_ALT0)
#define RP1_SPI0_CSN3_P2      RP1_PINMUX(2, RP1_FUNC_ALT0)
#define RP1_SPI0_CSN2_P3      RP1_PINMUX(3, RP1_FUNC_ALT0)
#define RP1_GPCLK0_P4         RP1_PINMUX(4, RP1_FUNC_ALT0)
#define RP1_GPCLK1_P5         RP1_PINMUX(5, RP1_FUNC_ALT0)
#define RP1_GPCLK2_P6         RP1_PINMUX(6, RP1_FUNC_ALT0)
#define RP1_SPI0_CSN1_P7      RP1_PINMUX(7, RP1_FUNC_ALT0)
#define RP1_SPI0_CSN0_P8      RP1_PINMUX(8, RP1_FUNC_ALT0)
#define RP1_SPI0_SIO1_P9      RP1_PINMUX(9, RP1_FUNC_ALT0)
#define RP1_SPI0_SIO0_P10     RP1_PINMUX(10, RP1_FUNC_ALT0)
#define RP1_SPI0_SCLK_P11     RP1_PINMUX(11, RP1_FUNC_ALT0)
#define RP1_PWM00_P12         RP1_PINMUX(12, RP1_FUNC_ALT0)
#define RP1_PWM01_P13         RP1_PINMUX(13, RP1_FUNC_ALT0)
#define RP1_PWM02_P14         RP1_PINMUX(14, RP1_FUNC_ALT0)
#define RP1_PWM03_P15         RP1_PINMUX(15, RP1_FUNC_ALT0)
#define RP1_SPI1_CSN2_P16     RP1_PINMUX(16, RP1_FUNC_ALT0)
#define RP1_SPI1_CSN1_P17     RP1_PINMUX(17, RP1_FUNC_ALT0)
#define RP1_SPI1_CSN0_P18     RP1_PINMUX(18, RP1_FUNC_ALT0)
#define RP1_SPI1_SIO1_P19     RP1_PINMUX(19, RP1_FUNC_ALT0)
#define RP1_SPI1_SIO0_P20     RP1_PINMUX(20, RP1_FUNC_ALT0)
#define RP1_SPI1_SCLK_P21     RP1_PINMUX(21, RP1_FUNC_ALT0)
#define RP1_SDIO0_CLK_P22     RP1_PINMUX(22, RP1_FUNC_ALT0)
#define RP1_SDIO0_CMD_P23     RP1_PINMUX(23, RP1_FUNC_ALT0)
#define RP1_SDIO0_DAT0_P24    RP1_PINMUX(24, RP1_FUNC_ALT0)
#define RP1_SDIO0_DAT1_P25    RP1_PINMUX(25, RP1_FUNC_ALT0)
#define RP1_SDIO0_DAT2_P26    RP1_PINMUX(26, RP1_FUNC_ALT0)
#define RP1_SDIO0_DAT3_P27    RP1_PINMUX(27, RP1_FUNC_ALT0)


#define RP1_UART1_TX_P0       RP1_PINMUX(0, RP1_FUNC_ALT2)
#define RP1_UART1_RX_P1       RP1_PINMUX(1, RP1_FUNC_ALT2)
#define RP1_UART1_CTS_P2      RP1_PINMUX(2, RP1_FUNC_ALT2)
#define RP1_UART1_RTS_P3      RP1_PINMUX(3, RP1_FUNC_ALT2)
#define RP1_UART2_TX_P4       RP1_PINMUX(4, RP1_FUNC_ALT2)
#define RP1_UART2_RX_P5       RP1_PINMUX(5, RP1_FUNC_ALT2)
#define RP1_UART2_CTS_P6      RP1_PINMUX(6, RP1_FUNC_ALT2)
#define RP1_UART2_RTS_P7      RP1_PINMUX(7, RP1_FUNC_ALT2)
#define RP1_UART3_TX_P8       RP1_PINMUX(8, RP1_FUNC_ALT2)
#define RP1_UART3_RX_P9       RP1_PINMUX(9, RP1_FUNC_ALT2)
#define RP1_UART3_CTS_P10     RP1_PINMUX(10, RP1_FUNC_ALT2)
#define RP1_UART3_RTS_P11     RP1_PINMUX(11, RP1_FUNC_ALT2)
#define RP1_UART4_TX_P12      RP1_PINMUX(12, RP1_FUNC_ALT2)
#define RP1_UART4_RX_P13      RP1_PINMUX(13, RP1_FUNC_ALT2)
#define RP1_UART4_CTS_P14     RP1_PINMUX(14, RP1_FUNC_ALT2)
#define RP1_UART4_RTS_P15     RP1_PINMUX(15, RP1_FUNC_ALT2)
#define RP1_MIPI0_DSI_TE_P16  RP1_PINMUX(16, RP1_FUNC_ALT2)
#define RP1_MIPI1_DSI_TE_P17  RP1_PINMUX(17, RP1_FUNC_ALT2)
#define RP1_I2S0_SCLK_P18     RP1_PINMUX(18, RP1_FUNC_ALT2)
#define RP1_I2S0_WS_P19       RP1_PINMUX(19, RP1_FUNC_ALT2)
#define RP1_I2S0_SDI0_P20     RP1_PINMUX(20, RP1_FUNC_ALT2)
#define RP1_I2S0_SDO0_P21     RP1_PINMUX(21, RP1_FUNC_ALT2)
#define RP1_I2S0_SDI1_P22     RP1_PINMUX(22, RP1_FUNC_ALT2)
#define RP1_I2S0_SDO1_P23     RP1_PINMUX(23, RP1_FUNC_ALT2)
#define RP1_I2S0_SDI2_P24     RP1_PINMUX(24, RP1_FUNC_ALT2)
#define RP1_I2S0_SDO2_P25     RP1_PINMUX(25, RP1_FUNC_ALT2)
#define RP1_I2S0_SDI3_P26     RP1_PINMUX(26, RP1_FUNC_ALT2)
#define RP1_I2S0_SDO3_P27     RP1_PINMUX(27, RP1_FUNC_ALT2)


#define RP1_DPI_PCLK_P0       RP1_PINMUX(0, RP1_FUNC_ALT1)
#define RP1_DPI_DE_P1         RP1_PINMUX(1, RP1_FUNC_ALT1)
#define RP1_DPI_VSYNC_P2      RP1_PINMUX(2, RP1_FUNC_ALT1)
#define RP1_DPI_HSYNC_P3      RP1_PINMUX(3, RP1_FUNC_ALT1)
#define RP1_DPI_D0_P4         RP1_PINMUX(4, RP1_FUNC_ALT1)
#define RP1_DPI_D1_P5         RP1_PINMUX(5, RP1_FUNC_ALT1)
#define RP1_DPI_D2_P6         RP1_PINMUX(6, RP1_FUNC_ALT1)
#define RP1_DPI_D3_P7         RP1_PINMUX(7, RP1_FUNC_ALT1)
#define RP1_DPI_D4_P8         RP1_PINMUX(8, RP1_FUNC_ALT1)
#define RP1_DPI_D5_P9         RP1_PINMUX(9, RP1_FUNC_ALT1)
#define RP1_DPI_D6_P10        RP1_PINMUX(10, RP1_FUNC_ALT1)
#define RP1_DPI_D7_P11        RP1_PINMUX(11, RP1_FUNC_ALT1)
#define RP1_DPI_D8_P12        RP1_PINMUX(12, RP1_FUNC_ALT1)
#define RP1_DPI_D9_P13        RP1_PINMUX(13, RP1_FUNC_ALT1)
#define RP1_DPI_D10_P14       RP1_PINMUX(14, RP1_FUNC_ALT1)
#define RP1_DPI_D11_P15       RP1_PINMUX(15, RP1_FUNC_ALT1)
#define RP1_DPI_D12_P16       RP1_PINMUX(16, RP1_FUNC_ALT1)
#define RP1_DPI_D13_P17       RP1_PINMUX(17, RP1_FUNC_ALT1)
#define RP1_DPI_D14_P18       RP1_PINMUX(18, RP1_FUNC_ALT1)
#define RP1_DPI_D15_P19       RP1_PINMUX(19, RP1_FUNC_ALT1)
#define RP1_DPI_D16_P20       RP1_PINMUX(20, RP1_FUNC_ALT1)
#define RP1_DPI_D17_P21       RP1_PINMUX(21, RP1_FUNC_ALT1)
#define RP1_DPI_D18_P22       RP1_PINMUX(22, RP1_FUNC_ALT1)
#define RP1_DPI_D19_P23       RP1_PINMUX(23, RP1_FUNC_ALT1)
#define RP1_DPI_D20_P24       RP1_PINMUX(24, RP1_FUNC_ALT1)
#define RP1_DPI_D21_P25       RP1_PINMUX(25, RP1_FUNC_ALT1)
#define RP1_DPI_D22_P26       RP1_PINMUX(26, RP1_FUNC_ALT1)
#define RP1_DPI_D23_P27       RP1_PINMUX(27, RP1_FUNC_ALT1)


#define RP1_I2C0_SDA_P0       RP1_PINMUX(0, RP1_FUNC_ALT3)
#define RP1_I2C0_SCL_P1       RP1_PINMUX(1, RP1_FUNC_ALT3)
#define RP1_I2C1_SDA_P2       RP1_PINMUX(2, RP1_FUNC_ALT3)
#define RP1_I2C1_SCL_P3       RP1_PINMUX(3, RP1_FUNC_ALT3)
#define RP1_I2C2_SDA_P4       RP1_PINMUX(4, RP1_FUNC_ALT3)
#define RP1_I2C2_SCL_P5       RP1_PINMUX(5, RP1_FUNC_ALT3)
#define RP1_I2C3_SDA_P6       RP1_PINMUX(6, RP1_FUNC_ALT3)
#define RP1_I2C3_SCL_P7       RP1_PINMUX(7, RP1_FUNC_ALT3)
#define RP1_I2C0_SDA_P8       RP1_PINMUX(8, RP1_FUNC_ALT3)
#define RP1_I2C0_SCL_P9       RP1_PINMUX(9, RP1_FUNC_ALT3)
#define RP1_I2C1_SDA_P10      RP1_PINMUX(10, RP1_FUNC_ALT3)
#define RP1_I2C1_SCL_P11      RP1_PINMUX(11, RP1_FUNC_ALT3)
#define RP1_I2C2_SDA_P12      RP1_PINMUX(12, RP1_FUNC_ALT3)
#define RP1_I2C2_SCL_P13      RP1_PINMUX(13, RP1_FUNC_ALT3)
#define RP1_I2C3_SDA_P14      RP1_PINMUX(14, RP1_FUNC_ALT3)
#define RP1_I2C3_SCL_P15      RP1_PINMUX(15, RP1_FUNC_ALT3)
#define RP1_PWM02_P18         RP1_PINMUX(18, RP1_FUNC_ALT3)
#define RP1_PWM03_P19         RP1_PINMUX(19, RP1_FUNC_ALT3)
#define RP1_GPCLK0_P20        RP1_PINMUX(20, RP1_FUNC_ALT3)
#define RP1_GPCLK1_P21        RP1_PINMUX(21, RP1_FUNC_ALT3)
#define RP1_I2C3_SDA_P22      RP1_PINMUX(22, RP1_FUNC_ALT3)
#define RP1_I2C3_SCL_P23      RP1_PINMUX(23, RP1_FUNC_ALT3)
#define RP1_I2S1_SDI2_P24     RP1_PINMUX(24, RP1_FUNC_ALT3)
#define RP1_AUDIO_IN_CLK_P25  RP1_PINMUX(25, RP1_FUNC_ALT3)
#define RP1_AUDIO_IN_DAT0_P26 RP1_PINMUX(26, RP1_FUNC_ALT3)
#define RP1_AUDIO_IN_DAT1_P27 RP1_PINMUX(27, RP1_FUNC_ALT3)


#define RP1_UART0_IR_RX_P2    RP1_PINMUX(2, RP1_FUNC_ALT4)
#define RP1_UART0_IR_TX_P3    RP1_PINMUX(3, RP1_FUNC_ALT4)
#define RP1_UART0_RI_P4       RP1_PINMUX(4, RP1_FUNC_ALT4)
#define RP1_UART0_DTR_P5      RP1_PINMUX(5, RP1_FUNC_ALT4)
#define RP1_UART0_DCD_P6      RP1_PINMUX(6, RP1_FUNC_ALT4)
#define RP1_UART0_DSR_P7      RP1_PINMUX(7, RP1_FUNC_ALT4)
#define RP1_AUDIO_OUT_L_P12   RP1_PINMUX(12, RP1_FUNC_ALT4)
#define RP1_AUDIO_OUT_R_P13   RP1_PINMUX(13, RP1_FUNC_ALT4)
#define RP1_UART0_TX_P14      RP1_PINMUX(14, RP1_FUNC_ALT4)
#define RP1_UART0_RX_P15      RP1_PINMUX(15, RP1_FUNC_ALT4)
#define RP1_UART0_CTS_P16     RP1_PINMUX(16, RP1_FUNC_ALT4)
#define RP1_UART0_RTS_P17     RP1_PINMUX(17, RP1_FUNC_ALT4)
#define RP1_I2S1_SCLK_P18     RP1_PINMUX(18, RP1_FUNC_ALT4)
#define RP1_I2S1_WS_P19       RP1_PINMUX(19, RP1_FUNC_ALT4)
#define RP1_I2S1_SDI0_P20     RP1_PINMUX(20, RP1_FUNC_ALT4)
#define RP1_I2S1_SDO0_P21     RP1_PINMUX(21, RP1_FUNC_ALT4)
#define RP1_I2S1_SDI1_P22     RP1_PINMUX(22, RP1_FUNC_ALT4)
#define RP1_I2S1_SDO1_P23     RP1_PINMUX(23, RP1_FUNC_ALT4)
#define RP1_I2S1_SDO2_P25     RP1_PINMUX(25, RP1_FUNC_ALT4)
#define RP1_I2S1_SDI3_P26     RP1_PINMUX(26, RP1_FUNC_ALT4)
#define RP1_I2S1_SDO3_P27     RP1_PINMUX(27, RP1_FUNC_ALT4)


#define RP1_SYS_RIO0_P0       RP1_PINMUX(0, RP1_FUNC_ALT5)
#define RP1_SYS_RIO1_P1       RP1_PINMUX(1, RP1_FUNC_ALT5)
#define RP1_SYS_RIO2_P2       RP1_PINMUX(2, RP1_FUNC_ALT5)
#define RP1_SYS_RIO3_P3       RP1_PINMUX(3, RP1_FUNC_ALT5)
#define RP1_SYS_RIO4_P4       RP1_PINMUX(4, RP1_FUNC_ALT5)
#define RP1_SYS_RIO5_P5       RP1_PINMUX(5, RP1_FUNC_ALT5)
#define RP1_SYS_RIO6_P6       RP1_PINMUX(6, RP1_FUNC_ALT5)
#define RP1_SYS_RIO7_P7       RP1_PINMUX(7, RP1_FUNC_ALT5)
#define RP1_SYS_RIO8_P8       RP1_PINMUX(8, RP1_FUNC_ALT5)
#define RP1_SYS_RIO9_P9       RP1_PINMUX(9, RP1_FUNC_ALT5)
#define RP1_SYS_RIO10_P10     RP1_PINMUX(10, RP1_FUNC_ALT5)
#define RP1_SYS_RIO11_P11     RP1_PINMUX(11, RP1_FUNC_ALT5)
#define RP1_SYS_RIO12_P12     RP1_PINMUX(12, RP1_FUNC_ALT5)
#define RP1_SYS_RIO13_P13     RP1_PINMUX(13, RP1_FUNC_ALT5)
#define RP1_SYS_RIO14_P14     RP1_PINMUX(14, RP1_FUNC_ALT5)
#define RP1_SYS_RIO15_P15     RP1_PINMUX(15, RP1_FUNC_ALT5)
#define RP1_SYS_RIO16_P16     RP1_PINMUX(16, RP1_FUNC_ALT5)
#define RP1_SYS_RIO17_P17     RP1_PINMUX(17, RP1_FUNC_ALT5)
#define RP1_SYS_RIO18_P18     RP1_PINMUX(18, RP1_FUNC_ALT5)
#define RP1_SYS_RIO19_P19     RP1_PINMUX(19, RP1_FUNC_ALT5)
#define RP1_SYS_RIO20_P20     RP1_PINMUX(20, RP1_FUNC_ALT5)
#define RP1_SYS_RIO21_P21     RP1_PINMUX(21, RP1_FUNC_ALT5)
#define RP1_SYS_RIO22_P22     RP1_PINMUX(22, RP1_FUNC_ALT5)
#define RP1_SYS_RIO23_P23     RP1_PINMUX(23, RP1_FUNC_ALT5)
#define RP1_SYS_RIO24_P24     RP1_PINMUX(24, RP1_FUNC_ALT5)
#define RP1_SYS_RIO25_P25     RP1_PINMUX(25, RP1_FUNC_ALT5)
#define RP1_SYS_RIO26_P26     RP1_PINMUX(26, RP1_FUNC_ALT5)
#define RP1_SYS_RIO27_P27     RP1_PINMUX(27, RP1_FUNC_ALT5)


#define RP1_PROC_RIO0_P0      RP1_PINMUX(0, RP1_FUNC_ALT6)
#define RP1_PROC_RIO1_P1      RP1_PINMUX(1, RP1_FUNC_ALT6)
#define RP1_PROC_RIO2_P2      RP1_PINMUX(2, RP1_FUNC_ALT6)
#define RP1_PROC_RIO3_P3      RP1_PINMUX(3, RP1_FUNC_ALT6)
#define RP1_PROC_RIO4_P4      RP1_PINMUX(4, RP1_FUNC_ALT6)
#define RP1_PROC_RIO5_P5      RP1_PINMUX(5, RP1_FUNC_ALT6)
#define RP1_PROC_RIO6_P6      RP1_PINMUX(6, RP1_FUNC_ALT6)
#define RP1_PROC_RIO7_P7      RP1_PINMUX(7, RP1_FUNC_ALT6)
#define RP1_PROC_RIO8_P8      RP1_PINMUX(8, RP1_FUNC_ALT6)
#define RP1_PROC_RIO9_P9      RP1_PINMUX(9, RP1_FUNC_ALT6)
#define RP1_PROC_RIO10_P10    RP1_PINMUX(10, RP1_FUNC_ALT6)
#define RP1_PROC_RIO11_P11    RP1_PINMUX(11, RP1_FUNC_ALT6)
#define RP1_PROC_RIO12_P12    RP1_PINMUX(12, RP1_FUNC_ALT6)
#define RP1_PROC_RIO13_P13    RP1_PINMUX(13, RP1_FUNC_ALT6)
#define RP1_PROC_RIO14_P14    RP1_PINMUX(14, RP1_FUNC_ALT6)
#define RP1_PROC_RIO15_P15    RP1_PINMUX(15, RP1_FUNC_ALT6)
#define RP1_PROC_RIO16_P16    RP1_PINMUX(16, RP1_FUNC_ALT6)
#define RP1_PROC_RIO17_P17    RP1_PINMUX(17, RP1_FUNC_ALT6)
#define RP1_PROC_RIO18_P18    RP1_PINMUX(18, RP1_FUNC_ALT6)
#define RP1_PROC_RIO19_P19    RP1_PINMUX(19, RP1_FUNC_ALT6)
#define RP1_PROC_RIO20_P20    RP1_PINMUX(20, RP1_FUNC_ALT6)
#define RP1_PROC_RIO21_P21    RP1_PINMUX(21, RP1_FUNC_ALT6)
#define RP1_PROC_RIO22_P22    RP1_PINMUX(22, RP1_FUNC_ALT6)
#define RP1_PROC_RIO23_P23    RP1_PINMUX(23, RP1_FUNC_ALT6)
#define RP1_PROC_RIO24_P24    RP1_PINMUX(24, RP1_FUNC_ALT6)
#define RP1_PROC_RIO25_P25    RP1_PINMUX(25, RP1_FUNC_ALT6)
#define RP1_PROC_RIO26_P26    RP1_PINMUX(26, RP1_FUNC_ALT6)
#define RP1_PROC_RIO27_P27    RP1_PINMUX(27, RP1_FUNC_ALT6)


#define RP1_PIO0_P0           RP1_PINMUX(0, RP1_FUNC_ALT7)
#define RP1_PIO1_P1           RP1_PINMUX(1, RP1_FUNC_ALT7)
#define RP1_PIO2_P2           RP1_PINMUX(2, RP1_FUNC_ALT7)
#define RP1_PIO3_P3           RP1_PINMUX(3, RP1_FUNC_ALT7)
#define RP1_PIO4_P4           RP1_PINMUX(4, RP1_FUNC_ALT7)
#define RP1_PIO5_P5           RP1_PINMUX(5, RP1_FUNC_ALT7)
#define RP1_PIO6_P6           RP1_PINMUX(6, RP1_FUNC_ALT7)
#define RP1_PIO7_P7           RP1_PINMUX(7, RP1_FUNC_ALT7)
#define RP1_PIO8_P8           RP1_PINMUX(8, RP1_FUNC_ALT7)
#define RP1_PIO9_P9           RP1_PINMUX(9, RP1_FUNC_ALT7)
#define RP1_PIO10_P10         RP1_PINMUX(10, RP1_FUNC_ALT7)
#define RP1_PIO11_P11         RP1_PINMUX(11, RP1_FUNC_ALT7)
#define RP1_PIO12_P12         RP1_PINMUX(12, RP1_FUNC_ALT7)
#define RP1_PIO13_P13         RP1_PINMUX(13, RP1_FUNC_ALT7)
#define RP1_PIO14_P14         RP1_PINMUX(14, RP1_FUNC_ALT7)
#define RP1_PIO15_P15         RP1_PINMUX(15, RP1_FUNC_ALT7)
#define RP1_PIO16_P16         RP1_PINMUX(16, RP1_FUNC_ALT7)
#define RP1_PIO17_P17         RP1_PINMUX(17, RP1_FUNC_ALT7)
#define RP1_PIO18_P18         RP1_PINMUX(18, RP1_FUNC_ALT7)
#define RP1_PIO19_P19         RP1_PINMUX(19, RP1_FUNC_ALT7)
#define RP1_PIO20_P20         RP1_PINMUX(20, RP1_FUNC_ALT7)
#define RP1_PIO21_P21         RP1_PINMUX(21, RP1_FUNC_ALT7)
#define RP1_PIO22_P22         RP1_PINMUX(22, RP1_FUNC_ALT7)
#define RP1_PIO23_P23         RP1_PINMUX(23, RP1_FUNC_ALT7)
#define RP1_PIO24_P24         RP1_PINMUX(24, RP1_FUNC_ALT7)
#define RP1_PIO25_P25         RP1_PINMUX(25, RP1_FUNC_ALT7)
#define RP1_PIO26_P26         RP1_PINMUX(26, RP1_FUNC_ALT7)
#define RP1_PIO27_P27         RP1_PINMUX(27, RP1_FUNC_ALT7)


#define RP1_SPI2_CSN0_P0      RP1_PINMUX(0, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN1_P1      RP1_PINMUX(1, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN2_P2      RP1_PINMUX(2, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN3_P3      RP1_PINMUX(3, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN4_P4      RP1_PINMUX(4, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN5_P5      RP1_PINMUX(5, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN6_P6      RP1_PINMUX(6, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN7_P7      RP1_PINMUX(7, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN8_P8      RP1_PINMUX(8, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN9_P9      RP1_PINMUX(9, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN10_P10    RP1_PINMUX(10, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN11_P11    RP1_PINMUX(11, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN12_P12    RP1_PINMUX(12, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN13_P13    RP1_PINMUX(13, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN14_P14    RP1_PINMUX(14, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN15_P15    RP1_PINMUX(15, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN16_P16    RP1_PINMUX(16, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN17_P17    RP1_PINMUX(17, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN18_P18    RP1_PINMUX(18, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN19_P19    RP1_PINMUX(19, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN20_P20    RP1_PINMUX(20, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN21_P21    RP1_PINMUX(21, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN22_P22    RP1_PINMUX(22, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN23_P23    RP1_PINMUX(23, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN24_P24    RP1_PINMUX(24, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN25_P25    RP1_PINMUX(25, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN26_P26    RP1_PINMUX(26, RP1_FUNC_ALT8)
#define RP1_SPI2_CSN27_P27    RP1_PINMUX(27, RP1_FUNC_ALT8)



#endif /* ZEPHYR_DT_BINDINGS_PINCTRL_RP1_PINCTRL_H_ */
```

## 165.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 TOKITA Hiroshi。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 23 行

RP1 引脚复用编码（Pinmux encoding）不包含引脚组选择器（Bank selector）。

### 注释 3：原第 430 行

头文件保护宏（Header guard）标记：`ZEPHYR_DT_BINDINGS_PINCTRL_RP1_PINCTRL_H_`。

## 165.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rp1-pinctrl_8h.html)

---

[上一章](P164_rk3588-cru.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P166_rpi-pico-dma-common.h_源码浏览.md)
