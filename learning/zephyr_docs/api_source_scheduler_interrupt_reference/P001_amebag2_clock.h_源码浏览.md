---
id: learning.zephyr-docs.api-source-scheduler-interrupt-reference.page-1
title: amebag2_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/amebag2__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_amebag2\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/amebag2__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/amebag2__clock_8h.html)。

## 1.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00189"></a>
<a id="foldopen00198"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="foldopen00213"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="foldopen00227"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="foldopen00237"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="foldopen00246"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="foldopen00253"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="foldopen00260"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="foldopen00267"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="foldopen00277"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="foldopen00286"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="foldopen00396"></a>
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
<a id="l00422"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>

```c
/*
 * Copyright (c) 2024 Realtek Semiconductor Corp.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_AMEBAG2_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_AMEBAG2_CLOCK_H_

#ifdef __cplusplus
extern "C" {
#endif




#define AMEBA_ATIM_CLK 1

#define AMEBA_RTC_CLK  2

#define AMEBA_LEDC_CLK 3



#define AMEBA_PWM0_CLK 4

#define AMEBA_PWM1_CLK 5

#define AMEBA_PWM2_CLK 6

#define AMEBA_PWM3_CLK 7

#define AMEBA_PWM4_CLK 8

#define AMEBA_UART0_CLK   9

#define AMEBA_UART1_CLK   10

#define AMEBA_UART2_CLK   11

#define AMEBA_UART3_CLK   12

#define AMEBA_LOGUART_CLK 13

#define AMEBA_DTIM_CLK    14

#define AMEBA_ADC_CLK     15

#define AMEBA_GPIO_CLK    16

#define AMEBA_LTIM0_CLK 17

#define AMEBA_LTIM1_CLK 18

#define AMEBA_LTIM2_CLK 19

#define AMEBA_LTIM3_CLK 20

#define AMEBA_PTIM0_CLK 21

#define AMEBA_PTIM1_CLK 22



#define AMEBA_DMAC_CLK  23

#define AMEBA_SDH_CLK   24

#define AMEBA_SDD_CLK   25

#define AMEBA_SPI0_CLK  26

#define AMEBA_SPI1_CLK  27

#define AMEBA_USB_CLK   28

#define AMEBA_FLASH_CLK 29

#define AMEBA_PSRAM_CLK 30

#define AMEBA_SPORT_CLK 31

#define AMEBA_AC_CLK    32

#define AMEBA_IRDA_CLK  33

#define AMEBA_I2C0_CLK  34

#define AMEBA_I2C1_CLK  35

#define AMEBA_TRNG_CLK  36

#define AMEBA_LCDC_CLK  37

#define AMEBA_A2C0_CLK  38

#define AMEBA_A2C1_CLK  39

#define AMEBA_GMAC_CLK  40

#define AMEBA_PPE_CLK   41

#define AMEBA_MJPEG_CLK 42



#define AMEBA_BTON_CLK 43

#define AMEBA_PKE_CLK  44

#define AMEBA_CLK_MAX 45 /* clk idx max */



#define AMEBA_NUMERICAL_PERIPH(name, n)                                                    \
        [AMEBA_##name##n##_CLK] = {                                                        \
                .parent = AMEBA_RCC_NO_PARENT,                                             \
                .cke = APBPeriph_##name##n##_CLOCK,                                        \
                .fen = APBPeriph_##name##n,                                                \
        },

#define AMEBA_SINGLE_PERIPH(name)                                                          \
        [AMEBA_##name##_CLK] = {                                                           \
                .parent = AMEBA_RCC_NO_PARENT,                                             \
                .cke = APBPeriph_##name##_CLOCK,                                           \
                .fen = APBPeriph_##name,                                                   \
        },

#define AMEBA_SINGLE_PERIPH_NO_FEN(name)                                                   \
        [AMEBA_##name##_CLK] = {                                                           \
                .parent = AMEBA_RCC_NO_PARENT,                                             \
                .cke = APBPeriph_##name##_CLOCK,                                           \
                .fen = APBPeriph_NULL,                                                     \
        },

#define AMEBA_LTIM_PERIPHS                                                                 \
        AMEBA_NUMERICAL_PERIPH(LTIM, 0) /* AMEBA_LTIM0_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(LTIM, 1) /* AMEBA_LTIM1_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(LTIM, 2) /* AMEBA_LTIM2_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(LTIM, 3) /* AMEBA_LTIM3_CLK */

#define AMEBA_PTIM_PERIPHS                                                                 \
        AMEBA_NUMERICAL_PERIPH(PTIM, 0) /* AMEBA_PTIM0_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(PTIM, 1) /* AMEBA_PTIM1_CLK */

#define AMEBA_SPI_PERIPHS                                                                  \
        AMEBA_NUMERICAL_PERIPH(SPI, 0) /* AMEBA_SPI0_CLK */                                \
        AMEBA_NUMERICAL_PERIPH(SPI, 1) /* AMEBA_SPI1_CLK */

#define AMEBA_I2C_PERIPHS                                                                  \
        AMEBA_NUMERICAL_PERIPH(I2C, 0) /* AMEBA_I2C0_CLK */                                \
        AMEBA_NUMERICAL_PERIPH(I2C, 1) /* AMEBA_I2C1_CLK */

#define AMEBA_PWM_PERIPHS                                                                  \
        AMEBA_NUMERICAL_PERIPH(PWM, 0) /* AMEBA_PWM0_CLK */                                \
        AMEBA_NUMERICAL_PERIPH(PWM, 1) /* AMEBA_PWM1_CLK */                                \
        AMEBA_NUMERICAL_PERIPH(PWM, 2) /* AMEBA_PWM2_CLK */                                \
        AMEBA_NUMERICAL_PERIPH(PWM, 3) /* AMEBA_PWM3_CLK */                                \
        AMEBA_NUMERICAL_PERIPH(PWM, 4) /* AMEBA_PWM4_CLK */

#define AMEBA_UART_PERIPHS                                                                 \
        AMEBA_NUMERICAL_PERIPH(UART, 0) /* AMEBA_UART0_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(UART, 1) /* AMEBA_UART1_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(UART, 2) /* AMEBA_UART2_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(UART, 3) /* AMEBA_UART3_CLK */

#define AMEBA_A2C_PERIPHS                                                                  \
        AMEBA_NUMERICAL_PERIPH(A2C, 0) /* AMEBA_A2C0_CLK */                                \
        AMEBA_NUMERICAL_PERIPH(A2C, 1) /* AMEBA_A2C1_CLK */

#define AMEBA_LOGUART_PERIPHS AMEBA_SINGLE_PERIPH(LOGUART)    /* AMEBA_LOGUART_CLK */

#define AMEBA_DMAC_PERIPHS    AMEBA_SINGLE_PERIPH(DMAC)       /* AMEBA_DMAC_CLK */

#define AMEBA_SDH_PERIPHS     AMEBA_SINGLE_PERIPH(SDH)        /* AMEBA_SDH_CLK */

#define AMEBA_SDD_PERIPHS     AMEBA_SINGLE_PERIPH(SDD)        /* AMEBA_SDD_CLK */

#define AMEBA_USB_PERIPHS     AMEBA_SINGLE_PERIPH(USB)        /* AMEBA_USB_CLK */

#define AMEBA_FLASH_PERIPHS   AMEBA_SINGLE_PERIPH(FLASH)      /* AMEBA_FLASH_CLK */

#define AMEBA_PSRAM_PERIPHS   AMEBA_SINGLE_PERIPH(PSRAM)      /* AMEBA_PSRAM_CLK */

#define AMEBA_AC_PERIPHS      AMEBA_SINGLE_PERIPH(AC)         /* AMEBA_AC_CLK */

#define AMEBA_IRDA_PERIPHS    AMEBA_SINGLE_PERIPH(IRDA)       /* AMEBA_IRDA_CLK */

#define AMEBA_TRNG_PERIPHS    AMEBA_SINGLE_PERIPH(TRNG)       /* AMEBA_TRNG_CLK */

#define AMEBA_LCDC_PERIPHS    AMEBA_SINGLE_PERIPH(LCDC)       /* AMEBA_LCDC_CLK */

#define AMEBA_RTC_PERIPHS     AMEBA_SINGLE_PERIPH_NO_FEN(RTC) /* AMEBA_RTC_CLK */

#define AMEBA_LEDC_PERIPHS    AMEBA_SINGLE_PERIPH(LEDC)       /* AMEBA_LEDC_CLK */

#define AMEBA_ADC_PERIPHS     AMEBA_SINGLE_PERIPH(ADC)        /* AMEBA_ADC_CLK */

#define AMEBA_GPIO_PERIPHS    AMEBA_SINGLE_PERIPH(GPIO)       /* AMEBA_GPIO_CLK */

#define AMEBA_BTON_PERIPHS    AMEBA_SINGLE_PERIPH(BTON)       /* AMEBA_BTON_CLK */

#define AMEBA_SPORT_PERIPHS   AMEBA_SINGLE_PERIPH(SPORT)      /* AMEBA_SPORT_CLK */

#define AMEBA_GMAC_PERIPHS    AMEBA_SINGLE_PERIPH(GMAC)       /* AMEBA_GMAC_CLK */

#define AMEBA_PPE_PERIPHS     AMEBA_SINGLE_PERIPH(PPE)        /* AMEBA_PPE_CLK */

#define AMEBA_MJPEG_PERIPHS   AMEBA_SINGLE_PERIPH(MJPEG)      /* AMEBA_MJPEG_CLK */

#define AMEBA_CORE_PERIPHS                                                                 \
        AMEBA_RTC_PERIPHS                                                                  \
        AMEBA_PWM_PERIPHS                                                                  \
        AMEBA_LEDC_PERIPHS                                                                 \
        AMEBA_UART_PERIPHS                                                                 \
        AMEBA_LOGUART_PERIPHS                                                              \
        AMEBA_ADC_PERIPHS                                                                  \
        AMEBA_GPIO_PERIPHS                                                                 \
        AMEBA_LTIM_PERIPHS                                                                 \
        AMEBA_PTIM_PERIPHS                                                                 \
        AMEBA_DMAC_PERIPHS                                                                 \
        AMEBA_SDH_PERIPHS                                                                  \
        AMEBA_SDD_PERIPHS                                                                  \
        AMEBA_SPI_PERIPHS                                                                  \
        AMEBA_USB_PERIPHS                                                                  \
        AMEBA_FLASH_PERIPHS                                                                \
        AMEBA_SPORT_PERIPHS                                                                \
        AMEBA_AC_PERIPHS                                                                   \
        AMEBA_I2C_PERIPHS                                                                  \
        AMEBA_TRNG_PERIPHS                                                                 \
        AMEBA_LCDC_PERIPHS                                                                 \
        AMEBA_A2C_PERIPHS                                                                  \
        AMEBA_GMAC_PERIPHS                                                                 \
        AMEBA_PPE_PERIPHS                                                                  \
        AMEBA_MJPEG_PERIPHS                                                                \
        AMEBA_BTON_PERIPHS


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_AMEBAG2_CLOCK_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Realtek Semiconductor Corp.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 181 行

时钟索引（clock index）的最大值。

### 注释 3：原第 238 行

时钟标识（Clock Identifier）：`AMEBA_LTIM0_CLK`。

### 注释 4：原第 239 行

时钟标识（Clock Identifier）：`AMEBA_LTIM1_CLK`。

### 注释 5：原第 240 行

时钟标识（Clock Identifier）：`AMEBA_LTIM2_CLK`。

### 注释 6：原第 241 行

时钟标识（Clock Identifier）：`AMEBA_LTIM3_CLK`。

### 注释 7：原第 247 行

时钟标识（Clock Identifier）：`AMEBA_PTIM0_CLK`。

### 注释 8：原第 248 行

时钟标识（Clock Identifier）：`AMEBA_PTIM1_CLK`。

### 注释 9：原第 254 行

`AMEBA_SPI0_CLK` 时钟标识。

### 注释 10：原第 255 行

`AMEBA_SPI1_CLK` 时钟标识。

### 注释 11：原第 261 行

`AMEBA_I2C0_CLK` 时钟标识。

### 注释 12：原第 262 行

时钟标识（Clock Identifier）：`AMEBA_I2C1_CLK`。

### 注释 13：原第 268 行

时钟标识（Clock Identifier）：`AMEBA_PWM0_CLK`。

### 注释 14：原第 269 行

时钟标识（Clock Identifier）：`AMEBA_PWM1_CLK`。

### 注释 15：原第 270 行

时钟标识（Clock Identifier）：`AMEBA_PWM2_CLK`。

### 注释 16：原第 271 行

时钟标识（Clock Identifier）：`AMEBA_PWM3_CLK`。

### 注释 17：原第 272 行

时钟标识（Clock Identifier）：`AMEBA_PWM4_CLK`。

### 注释 18：原第 278 行

`AMEBA_UART0_CLK` 时钟标识。

### 注释 19：原第 279 行

时钟标识（Clock Identifier）：`AMEBA_UART1_CLK`。

### 注释 20：原第 280 行

时钟标识（Clock Identifier）：`AMEBA_UART2_CLK`。

### 注释 21：原第 281 行

`AMEBA_UART3_CLK` 时钟标识。

### 注释 22：原第 287 行

时钟标识（Clock Identifier）：`AMEBA_A2C0_CLK`。

### 注释 23：原第 288 行

时钟标识（Clock Identifier）：`AMEBA_A2C1_CLK`。

### 注释 24：原第 293 行

时钟标识（Clock Identifier）：`AMEBA_LOGUART_CLK`。

### 注释 25：原第 298 行

时钟标识（Clock Identifier）：`AMEBA_DMAC_CLK`。

### 注释 26：原第 303 行

时钟标识（Clock Identifier）：`AMEBA_SDH_CLK`。

### 注释 27：原第 308 行

时钟标识（Clock Identifier）：`AMEBA_SDD_CLK`。

### 注释 28：原第 313 行

时钟标识（Clock Identifier）：`AMEBA_USB_CLK`。

### 注释 29：原第 318 行

时钟标识（Clock Identifier）：`AMEBA_FLASH_CLK`。

### 注释 30：原第 323 行

`AMEBA_PSRAM_CLK` 时钟标识。

### 注释 31：原第 328 行

时钟标识（Clock Identifier）：`AMEBA_AC_CLK`。

### 注释 32：原第 333 行

时钟标识（Clock Identifier）：`AMEBA_IRDA_CLK`。

### 注释 33：原第 338 行

时钟标识（Clock Identifier）：`AMEBA_TRNG_CLK`。

### 注释 34：原第 343 行

时钟标识（Clock Identifier）：`AMEBA_LCDC_CLK`。

### 注释 35：原第 348 行

`AMEBA_RTC_CLK` 时钟标识。

### 注释 36：原第 353 行

时钟标识（Clock Identifier）：`AMEBA_LEDC_CLK`。

### 注释 37：原第 358 行

时钟标识（Clock Identifier）：`AMEBA_ADC_CLK`。

### 注释 38：原第 363 行

时钟标识（Clock Identifier）：`AMEBA_GPIO_CLK`。

### 注释 39：原第 368 行

时钟标识（Clock Identifier）：`AMEBA_BTON_CLK`。

### 注释 40：原第 373 行

时钟标识（Clock Identifier）：`AMEBA_SPORT_CLK`。

### 注释 41：原第 378 行

时钟标识（Clock Identifier）：`AMEBA_GMAC_CLK`。

### 注释 42：原第 383 行

时钟标识（Clock Identifier）：`AMEBA_PPE_CLK`。

### 注释 43：原第 388 行

时钟标识（Clock Identifier）：`AMEBA_MJPEG_CLK`。

### 注释 44：原第 429 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_AMEBAG2_CLOCK_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/amebag2__clock_8h.html)

---

[返回大纲](大纲.md) · [下一章](P002_esp-esp32c6-intmux.h_源码浏览.md)
