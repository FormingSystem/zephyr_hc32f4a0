---
id: learning.zephyr-docs.api-source-http-wifi-reference.page-2
title: amebadplus_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/amebadplus__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_amebadplus\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/amebadplus__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/amebadplus__clock_8h.html)。

## 2.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00179"></a>
<a id="foldopen00188"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="foldopen00203"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="foldopen00213"></a>
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
<a id="foldopen00226"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="foldopen00233"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="foldopen00240"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="foldopen00247"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="foldopen00254"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="foldopen00261"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="foldopen00268"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="foldopen00354"></a>
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
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>

```c
/*
 * Copyright (c) 2024 Realtek Semiconductor Corp.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_AMEBADPLUS_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_AMEBADPLUS_CLOCK_H_

#ifdef __cplusplus
extern "C" {
#endif



#define AMEBA_ATIM_CLK 1

#define AMEBA_RTC_CLK  2



#define AMEBA_PWM0_CLK    3

#define AMEBA_PWM1_CLK    4

#define AMEBA_HTIM0_CLK   5

#define AMEBA_HTIM1_CLK   6

#define AMEBA_LEDC_CLK    7

#define AMEBA_UART0_CLK   8

#define AMEBA_UART1_CLK   9

#define AMEBA_UART2_CLK   10

#define AMEBA_LOGUART_CLK 11

#define AMEBA_DTIM_CLK    12

#define AMEBA_ADC_CLK     13

#define AMEBA_GPIO_CLK    14

#define AMEBA_LTIM0_CLK   15

#define AMEBA_LTIM1_CLK   16

#define AMEBA_LTIM2_CLK   17

#define AMEBA_LTIM3_CLK   18

#define AMEBA_LTIM4_CLK   19

#define AMEBA_LTIM5_CLK   20

#define AMEBA_LTIM6_CLK   21

#define AMEBA_LTIM7_CLK   22

#define AMEBA_PTIM0_CLK   23

#define AMEBA_PTIM1_CLK   24

#define AMEBA_KSCAN_CLK   25



#define AMEBA_DMAC_CLK   26

#define AMEBA_SDIO_CLK   27

#define AMEBA_SPI0_CLK   28

#define AMEBA_SPI1_CLK   29

#define AMEBA_USB_CLK    30

#define AMEBA_FLASH_CLK  31

#define AMEBA_PSRAM_CLK  32

#define AMEBA_SPORT0_CLK 33

#define AMEBA_SPORT1_CLK 34

#define AMEBA_AC_CLK     35

#define AMEBA_IRDA_CLK   36

#define AMEBA_I2C0_CLK   37

#define AMEBA_I2C1_CLK   38

#define AMEBA_TRNG_CLK   39



#define AMEBA_BTON_CLK 40

#define AMEBA_AES_CLK  42

#define AMEBA_CLK_MAX 43 /* clk idx max */



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

#define AMEBA_LTIM_PERIPHS                                                                 \
        AMEBA_NUMERICAL_PERIPH(LTIM, 0) /* AMEBA_LTIM0_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(LTIM, 1) /* AMEBA_LTIM1_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(LTIM, 2) /* AMEBA_LTIM2_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(LTIM, 3) /* AMEBA_LTIM3_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(LTIM, 4) /* AMEBA_LTIM4_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(LTIM, 5) /* AMEBA_LTIM5_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(LTIM, 6) /* AMEBA_LTIM6_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(LTIM, 7) /* AMEBA_LTIM7_CLK */

#define AMEBA_PTIM_PERIPHS                                                                 \
        AMEBA_NUMERICAL_PERIPH(PTIM, 0) /* AMEBA_PTIM0_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(PTIM, 1) /* AMEBA_PTIM1_CLK */

#define AMEBA_SPI_PERIPHS                                                                  \
        AMEBA_NUMERICAL_PERIPH(SPI, 0) /* AMEBA_SPI0_CLK */                                \
        AMEBA_NUMERICAL_PERIPH(SPI, 1) /* AMEBA_SPI1_CLK */

#define AMEBA_SPORT_PERIPHS                                                                \
        AMEBA_NUMERICAL_PERIPH(SPORT, 0) /* AMEBA_SPORT0_CLK */                            \
        AMEBA_NUMERICAL_PERIPH(SPORT, 1) /* AMEBA_SPORT1_CLK */

#define AMEBA_I2C_PERIPHS                                                                  \
        AMEBA_NUMERICAL_PERIPH(I2C, 0) /* AMEBA_I2C0_CLK */                                \
        AMEBA_NUMERICAL_PERIPH(I2C, 1) /* AMEBA_I2C1_CLK */

#define AMEBA_PWM_PERIPHS                                                                  \
        AMEBA_NUMERICAL_PERIPH(PWM, 0) /* AMEBA_PWM0_CLK */                                \
        AMEBA_NUMERICAL_PERIPH(PWM, 1) /* AMEBA_PWM1_CLK */

#define AMEBA_HTIM_PERIPHS                                                                 \
        AMEBA_NUMERICAL_PERIPH(HTIM, 0) /* AMEBA_HTIM0_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(HTIM, 1) /* AMEBA_HTIM1_CLK */

#define AMEBA_UART_PERIPHS                                                                 \
        AMEBA_NUMERICAL_PERIPH(UART, 0) /* AMEBA_UART0_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(UART, 1) /* AMEBA_UART1_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(UART, 2) /* AMEBA_UART2_CLK */

#define AMEBA_LOGUART_PERIPHS AMEBA_SINGLE_PERIPH(LOGUART) /* AMEBA_LOGUART_CLK */

#define AMEBA_KSCAN_PERIPHS   AMEBA_SINGLE_PERIPH(KSCAN)   /* AMEBA_KSCAN_CLK */

#define AMEBA_DMAC_PERIPHS    AMEBA_SINGLE_PERIPH(DMAC)    /* AMEBA_DMAC_CLK */

#define AMEBA_SDIO_PERIPHS    AMEBA_SINGLE_PERIPH(SDIO)    /* AMEBA_SDIO_CLK */

#define AMEBA_USB_PERIPHS     AMEBA_SINGLE_PERIPH(USB)     /* AMEBA_USB_CLK */

#define AMEBA_FLASH_PERIPHS   AMEBA_SINGLE_PERIPH(FLASH)   /* AMEBA_FLASH_CLK */

#define AMEBA_PSRAM_PERIPHS   AMEBA_SINGLE_PERIPH(PSRAM)   /* AMEBA_PSRAM_CLK */

#define AMEBA_AC_PERIPHS      AMEBA_SINGLE_PERIPH(AC)      /* AMEBA_AC_CLK */

#define AMEBA_IRDA_PERIPHS    AMEBA_SINGLE_PERIPH(IRDA)    /* AMEBA_IRDA_CLK */

#define AMEBA_TRNG_PERIPHS    AMEBA_SINGLE_PERIPH(TRNG)    /* AMEBA_TRNG_CLK */

#define AMEBA_RTC_PERIPHS     AMEBA_SINGLE_PERIPH(RTC)     /* AMEBA_RTC_CLK */

#define AMEBA_LEDC_PERIPHS    AMEBA_SINGLE_PERIPH(LEDC)    /* AMEBA_LEDC_CLK */

#define AMEBA_ADC_PERIPHS     AMEBA_SINGLE_PERIPH(ADC)     /* AMEBA_ADC_CLK */

#define AMEBA_GPIO_PERIPHS    AMEBA_SINGLE_PERIPH(GPIO)    /* AMEBA_GPIO_CLK */

#define AMEBA_BTON_PERIPHS    AMEBA_SINGLE_PERIPH(BTON)    /* AMEBA_BTON_CLK */

#define AMEBA_CORE_PERIPHS                                                                 \
        AMEBA_RTC_PERIPHS                                                                  \
        AMEBA_PWM_PERIPHS                                                                  \
        AMEBA_HTIM_PERIPHS                                                                 \
        AMEBA_LEDC_PERIPHS                                                                 \
        AMEBA_UART_PERIPHS                                                                 \
        AMEBA_LOGUART_PERIPHS                                                              \
        AMEBA_ADC_PERIPHS                                                                  \
        AMEBA_GPIO_PERIPHS                                                                 \
        AMEBA_LTIM_PERIPHS                                                                 \
        AMEBA_PTIM_PERIPHS                                                                 \
        AMEBA_KSCAN_PERIPHS                                                                \
        AMEBA_DMAC_PERIPHS                                                                 \
        AMEBA_SDIO_PERIPHS                                                                 \
        AMEBA_SPI_PERIPHS                                                                  \
        AMEBA_USB_PERIPHS                                                                  \
        AMEBA_FLASH_PERIPHS                                                                \
        AMEBA_SPORT_PERIPHS                                                                \
        AMEBA_AC_PERIPHS                                                                   \
        AMEBA_I2C_PERIPHS                                                                  \
        AMEBA_TRNG_PERIPHS                                                                 \
        AMEBA_BTON_PERIPHS


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_AMEBADPLUS_CLOCK_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Realtek Semiconductor Corp.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 171 行

时钟索引（clock index）的最大值。

### 注释 3：原第 214 行

时钟标识（Clock Identifier）：`AMEBA_LTIM0_CLK`。

### 注释 4：原第 215 行

时钟标识（Clock Identifier）：`AMEBA_LTIM1_CLK`。

### 注释 5：原第 216 行

时钟标识（Clock Identifier）：`AMEBA_LTIM2_CLK`。

### 注释 6：原第 217 行

时钟标识（Clock Identifier）：`AMEBA_LTIM3_CLK`。

### 注释 7：原第 218 行

时钟标识（Clock Identifier）：`AMEBA_LTIM4_CLK`。

### 注释 8：原第 219 行

时钟标识（Clock Identifier）：`AMEBA_LTIM5_CLK`。

### 注释 9：原第 220 行

时钟标识（Clock Identifier）：`AMEBA_LTIM6_CLK`。

### 注释 10：原第 221 行

时钟标识（Clock Identifier）：`AMEBA_LTIM7_CLK`。

### 注释 11：原第 227 行

时钟标识（Clock Identifier）：`AMEBA_PTIM0_CLK`。

### 注释 12：原第 228 行

时钟标识（Clock Identifier）：`AMEBA_PTIM1_CLK`。

### 注释 13：原第 234 行

`AMEBA_SPI0_CLK` 时钟标识。

### 注释 14：原第 235 行

`AMEBA_SPI1_CLK` 时钟标识。

### 注释 15：原第 241 行

时钟标识（Clock Identifier）：`AMEBA_SPORT0_CLK`。

### 注释 16：原第 242 行

时钟标识（Clock Identifier）：`AMEBA_SPORT1_CLK`。

### 注释 17：原第 248 行

`AMEBA_I2C0_CLK` 时钟标识。

### 注释 18：原第 249 行

时钟标识（Clock Identifier）：`AMEBA_I2C1_CLK`。

### 注释 19：原第 255 行

时钟标识（Clock Identifier）：`AMEBA_PWM0_CLK`。

### 注释 20：原第 256 行

时钟标识（Clock Identifier）：`AMEBA_PWM1_CLK`。

### 注释 21：原第 262 行

时钟标识（Clock Identifier）：`AMEBA_HTIM0_CLK`。

### 注释 22：原第 263 行

时钟标识（Clock Identifier）：`AMEBA_HTIM1_CLK`。

### 注释 23：原第 269 行

`AMEBA_UART0_CLK` 时钟标识。

### 注释 24：原第 270 行

时钟标识（Clock Identifier）：`AMEBA_UART1_CLK`。

### 注释 25：原第 271 行

时钟标识（Clock Identifier）：`AMEBA_UART2_CLK`。

### 注释 26：原第 276 行

时钟标识（Clock Identifier）：`AMEBA_LOGUART_CLK`。

### 注释 27：原第 281 行

时钟标识（Clock Identifier）：`AMEBA_KSCAN_CLK`。

### 注释 28：原第 286 行

时钟标识（Clock Identifier）：`AMEBA_DMAC_CLK`。

### 注释 29：原第 291 行

时钟标识（Clock Identifier）：`AMEBA_SDIO_CLK`。

### 注释 30：原第 296 行

时钟标识（Clock Identifier）：`AMEBA_USB_CLK`。

### 注释 31：原第 301 行

时钟标识（Clock Identifier）：`AMEBA_FLASH_CLK`。

### 注释 32：原第 306 行

`AMEBA_PSRAM_CLK` 时钟标识。

### 注释 33：原第 311 行

时钟标识（Clock Identifier）：`AMEBA_AC_CLK`。

### 注释 34：原第 316 行

时钟标识（Clock Identifier）：`AMEBA_IRDA_CLK`。

### 注释 35：原第 321 行

时钟标识（Clock Identifier）：`AMEBA_TRNG_CLK`。

### 注释 36：原第 326 行

`AMEBA_RTC_CLK` 时钟标识。

### 注释 37：原第 331 行

时钟标识（Clock Identifier）：`AMEBA_LEDC_CLK`。

### 注释 38：原第 336 行

时钟标识（Clock Identifier）：`AMEBA_ADC_CLK`。

### 注释 39：原第 341 行

时钟标识（Clock Identifier）：`AMEBA_GPIO_CLK`。

### 注释 40：原第 346 行

时钟标识（Clock Identifier）：`AMEBA_BTON_CLK`。

### 注释 41：原第 383 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_AMEBADPLUS_CLOCK_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/amebadplus__clock_8h.html)

---

[上一章](P001_adi-sdp-120.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_ifx_clock_source_cyt4dnxx.h_源码浏览.md)
