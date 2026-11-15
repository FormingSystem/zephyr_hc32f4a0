---
id: learning.zephyr-docs.api-source-supplement-reference.page-132
title: nrf-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第132章\_nrf-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nrf-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nrf-pinctrl_8h.html)。

## 132.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
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
<a id="l00213"></a>
<a id="l00215"></a>
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
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="foldopen00286"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="foldopen00298"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_NRF_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_NRF_PINCTRL_H_

/*
 * The whole nRF pin configuration information is encoded in a 32-bit bitfield
 * organized as follows:
 *
 * - 31..24: Pin function.
 * - 19-23:  Reserved.
 * - 18:     Associated peripheral belongs to GD FAST ACTIVE1 (nRF54H only)
 * - 17:     Clockpin enable.
 * - 16:     Pin inversion mode.
 * - 15:     Pin low power mode.
 * - 14..11: Pin output drive configuration.
 * - 10..9:  Pin pull configuration.
 * - 8..0:   Pin number (combination of port and pin).
 */


#define NRF_FUN_POS 24U
#define NRF_FUN_MSK 0xFFU
#define NRF_GPD_FAST_ACTIVE1_POS 18U
#define NRF_GPD_FAST_ACTIVE1_MSK 0x1U
#define NRF_CLOCKPIN_ENABLE_POS 17U
#define NRF_CLOCKPIN_ENABLE_MSK 0x1U
#define NRF_INVERT_POS 16U
#define NRF_INVERT_MSK 0x1U
#define NRF_LP_POS 15U
#define NRF_LP_MSK 0x1U
#define NRF_DRIVE_POS 11U
#define NRF_DRIVE_MSK 0xFU
#define NRF_PULL_POS 9U
#define NRF_PULL_MSK 0x3U
#define NRF_PIN_POS 0U
#define NRF_PIN_MSK 0x1FFU



#define NRF_FUN_UART_TX 0U
#define NRF_FUN_UART_RX 1U
#define NRF_FUN_UART_RTS 2U
#define NRF_FUN_UART_CTS 3U
#define NRF_FUN_SPIM_SCK 4U
#define NRF_FUN_SPIM_MOSI 5U
#define NRF_FUN_SPIM_MISO 6U
#define NRF_FUN_SPIS_SCK 7U
#define NRF_FUN_SPIS_MOSI 8U
#define NRF_FUN_SPIS_MISO 9U
#define NRF_FUN_SPIS_CSN 10U
#define NRF_FUN_TWIM_SCL 11U
#define NRF_FUN_TWIM_SDA 12U
#define NRF_FUN_I2S_SCK_M 13U
#define NRF_FUN_I2S_SCK_S 14U
#define NRF_FUN_I2S_LRCK_M 15U
#define NRF_FUN_I2S_LRCK_S 16U
#define NRF_FUN_I2S_SDIN 17U
#define NRF_FUN_I2S_SDOUT 18U
#define NRF_FUN_I2S_MCK 19U
#define NRF_FUN_PDM_CLK 20U
#define NRF_FUN_PDM_DIN 21U
#define NRF_FUN_PWM_OUT0 22U
#define NRF_FUN_PWM_OUT1 23U
#define NRF_FUN_PWM_OUT2 24U
#define NRF_FUN_PWM_OUT3 25U
#define NRF_FUN_QDEC_A 26U
#define NRF_FUN_QDEC_B 27U
#define NRF_FUN_QDEC_LED 28U
#define NRF_FUN_QSPI_SCK 29U
#define NRF_FUN_QSPI_CSN 30U
#define NRF_FUN_QSPI_IO0 31U
#define NRF_FUN_QSPI_IO1 32U
#define NRF_FUN_QSPI_IO2 33U
#define NRF_FUN_QSPI_IO3 34U
#define NRF_FUN_MSPI_SCK NRF_FUN_QSPI_SCK
#define NRF_FUN_MSPI_CSN NRF_FUN_QSPI_CSN
#define NRF_FUN_MSPI_IO0 NRF_FUN_QSPI_IO0
#define NRF_FUN_MSPI_IO1 NRF_FUN_QSPI_IO1
#define NRF_FUN_MSPI_IO2 NRF_FUN_QSPI_IO2
#define NRF_FUN_MSPI_IO3 NRF_FUN_QSPI_IO3
#define NRF_FUN_EXMIF_CK 35U
#define NRF_FUN_EXMIF_DQ0 36U
#define NRF_FUN_EXMIF_DQ1 37U
#define NRF_FUN_EXMIF_DQ2 38U
#define NRF_FUN_EXMIF_DQ3 39U
#define NRF_FUN_EXMIF_DQ4 40U
#define NRF_FUN_EXMIF_DQ5 41U
#define NRF_FUN_EXMIF_DQ6 42U
#define NRF_FUN_EXMIF_DQ7 43U
#define NRF_FUN_EXMIF_CS0 44U
#define NRF_FUN_EXMIF_CS1 45U
#define NRF_FUN_CAN_TX 46U
#define NRF_FUN_CAN_RX 47U
#define NRF_FUN_TWIS_SCL 48U
#define NRF_FUN_TWIS_SDA 49U
#define NRF_FUN_EXMIF_RWDS 50U
#define NRF_FUN_GRTC_CLKOUT_FAST 55U
#define NRF_FUN_GRTC_CLKOUT_32K  56U
#define NRF_FUN_TDM_SCK_M        71U
#define NRF_FUN_TDM_SCK_S        72U
#define NRF_FUN_TDM_FSYNC_M      73U
#define NRF_FUN_TDM_FSYNC_S      74U
#define NRF_FUN_TDM_SDIN         75U
#define NRF_FUN_TDM_SDOUT        76U
#define NRF_FUN_TDM_MCK          77U
#define NRF_FUN_SPIM_CSN         78U
#define NRF_FUN_TPIU_CLOCK       79U
#define NRF_FUN_TPIU_DATA0       80U
#define NRF_FUN_TPIU_DATA1       81U
#define NRF_FUN_TPIU_DATA2       82U
#define NRF_FUN_TPIU_DATA3       83U



#define NRF_DRIVE_S0S1 0U
#define NRF_DRIVE_H0S1 1U
#define NRF_DRIVE_S0H1 2U
#define NRF_DRIVE_H0H1 3U
#define NRF_DRIVE_D0S1 4U
#define NRF_DRIVE_D0H1 5U
#define NRF_DRIVE_S0D1 6U
#define NRF_DRIVE_H0D1 7U
#define NRF_DRIVE_E0E1 8U



#define NRF_PULL_NONE 0U
#define NRF_PULL_DOWN 1U
#define NRF_PULL_UP 3U



#define NRF_LP_DISABLE 0U
#define NRF_LP_ENABLE 1U



#define NRF_PIN_DISCONNECTED NRF_PIN_MSK


#define NRF_PSEL(fun, port, pin)                                                       \
        ((((((port) * 32U) + (pin)) & NRF_PIN_MSK) << NRF_PIN_POS) |                   \
         ((NRF_FUN_ ## fun & NRF_FUN_MSK) << NRF_FUN_POS))

#define NRF_PSEL_DISCONNECTED(fun)                                                     \
        (NRF_PIN_DISCONNECTED |                                                        \
         ((NRF_FUN_ ## fun & NRF_FUN_MSK) << NRF_FUN_POS))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_NRF_PINCTRL_H_ */
```

## 132.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 9 行

全部 nRF 引脚配置信息编码在一个 32 位位域（Bitfield）中，组织如下：

- `31..24`：引脚功能。
- `19-23`：保留。
- `18`：关联外设属于 GD FAST ACTIVE1，仅适用于 nRF54H。
- `17`：时钟引脚（Clockpin）使能。
- `16`：引脚反相模式。
- `15`：引脚低功耗模式。
- `14..11`：引脚输出驱动配置。
- `10..9`：引脚上拉/下拉配置。
- `8..0`：引脚编号，由端口和引脚组合而成。

### 注释 3：原第 302 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_NRF_PINCTRL_H_`。

## 132.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nrf-pinctrl_8h.html)

---

[上一章](P131_nrf-comp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P133_nrfs-audiopll.h_源码浏览.md)
