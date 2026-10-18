---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-1
title: amebad_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/amebad__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_amebad\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/amebad__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/amebad__clock_8h.html)。

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
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00109"></a>
<a id="foldopen00118"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00133"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="foldopen00148"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="foldopen00158"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="foldopen00172"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="foldopen00184"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="foldopen00243"></a>
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
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>

```c
/*
 * Copyright (c) 2024 Realtek Semiconductor Corp.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_AMEBAD_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_AMEBAD_CLOCK_H_

#ifdef __cplusplus
extern "C" {
#endif



#define AMEBA_ATIM_CLK 0

#define AMEBA_RTC_CLK  1



#define AMEBA_PWM0_CLK    2

#define AMEBA_UART0_CLK   3

#define AMEBA_LOGUART_CLK 4

#define AMEBA_UART3_CLK   5

#define AMEBA_ADC_CLK     6

#define AMEBA_GPIO_CLK    7

#define AMEBA_LTIM0_CLK   8

#define AMEBA_LTIM1_CLK   9

#define AMEBA_LTIM2_CLK   10

#define AMEBA_LTIM3_CLK   11



#define AMEBA_PERI_HCLK 12

#define AMEBA_GDMA0_CLK 13

#define AMEBA_SPI0_CLK  14

#define AMEBA_SPI1_CLK  15

#define AMEBA_FLASH_CLK 16

#define AMEBA_PSRAM_CLK 17

#define AMEBA_I2C0_CLK  18

#define AMEBA_PRNG_CLK  19

#define AMEBA_CLK_MAX 20 /* clk idx max */



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

#define AMEBA_REMAP_PERIPH(clk_index, remap_name)                                          \
        [clk_index] = {                                                                    \
                .parent = AMEBA_RCC_NO_PARENT,                                             \
                .cke = APBPeriph_##remap_name##_CLOCK,                                     \
                .fen = APBPeriph_##remap_name,                                             \
        },

#define AMEBA_LTIM_PERIPHS                                                                 \
        AMEBA_REMAP_PERIPH(AMEBA_LTIM0_CLK, GTIMER)                                        \
        AMEBA_REMAP_PERIPH(AMEBA_LTIM1_CLK, GTIMER)                                        \
        AMEBA_REMAP_PERIPH(AMEBA_LTIM2_CLK, GTIMER)                                        \
        AMEBA_REMAP_PERIPH(AMEBA_LTIM3_CLK, GTIMER)

#define AMEBA_PWM_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_PWM0_CLK, GTIMER)

#define AMEBA_SPI_PERIPHS                                                                  \
        AMEBA_NUMERICAL_PERIPH(SPI, 0) /* AMEBA_SPI0_CLK */                                \
        AMEBA_NUMERICAL_PERIPH(SPI, 1) /* AMEBA_SPI1_CLK */

#define AMEBA_I2C_PERIPHS AMEBA_NUMERICAL_PERIPH(I2C, 0) /* AMEBA_I2C0_CLK */

#define AMEBA_UART_PERIPHS                                                                 \
        AMEBA_NUMERICAL_PERIPH(UART, 0) /* AMEBA_UART0_CLK */                              \
        AMEBA_NUMERICAL_PERIPH(UART, 3) /* AMEBA_UART3_CLK */

#define AMEBA_GDMA0_PERIPHS AMEBA_SINGLE_PERIPH(GDMA0) /* AMEBA_GDMA0_CLK */

#define AMEBA_PSRAM_PERIPHS AMEBA_SINGLE_PERIPH(PSRAM) /* AMEBA_PSRAM_CLK */

#define AMEBA_RTC_PERIPHS   AMEBA_SINGLE_PERIPH(RTC)   /* AMEBA_RTC_CLK */

#define AMEBA_LOGUART_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_LOGUART_CLK, NULL)

#define AMEBA_FLASH_PERIPHS   AMEBA_REMAP_PERIPH(AMEBA_FLASH_CLK, NULL)

#define AMEBA_GPIO_PERIPHS    AMEBA_REMAP_PERIPH(AMEBA_GPIO_CLK, NULL)

#define AMEBA_ADC_PERIPHS     AMEBA_REMAP_PERIPH(AMEBA_ADC_CLK, NULL)

#define AMEBA_PRNG_PERIPHS    AMEBA_REMAP_PERIPH(AMEBA_PRNG_CLK, NULL)

#define APBPeriph_NULL_CLOCK APBPeriph_CLOCK_NULL

#define AMEBA_CORE_PERIPHS                                                                 \
        AMEBA_RTC_PERIPHS                                                                  \
        AMEBA_PWM_PERIPHS                                                                  \
        AMEBA_UART_PERIPHS                                                                 \
        AMEBA_LOGUART_PERIPHS                                                              \
        AMEBA_ADC_PERIPHS                                                                  \
        AMEBA_GPIO_PERIPHS                                                                 \
        AMEBA_LTIM_PERIPHS                                                                 \
        AMEBA_GDMA0_PERIPHS                                                                \
        AMEBA_SPI_PERIPHS                                                                  \
        AMEBA_FLASH_PERIPHS                                                                \
        AMEBA_I2C_PERIPHS                                                                  \
        AMEBA_PRNG_PERIPHS


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_AMEBAD_CLOCK_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Realtek Semiconductor Corp.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 101 行

时钟索引（clock index）的最大值。

### 注释 3：原第 173 行

`AMEBA_SPI0_CLK` 时钟标识。

### 注释 4：原第 174 行

`AMEBA_SPI1_CLK` 时钟标识。

### 注释 5：原第 179 行

`AMEBA_I2C0_CLK` 时钟标识。

### 注释 6：原第 185 行

`AMEBA_UART0_CLK` 时钟标识。

### 注释 7：原第 186 行

`AMEBA_UART3_CLK` 时钟标识。

### 注释 8：原第 191 行

`AMEBA_GDMA0_CLK` 时钟标识。

### 注释 9：原第 196 行

`AMEBA_PSRAM_CLK` 时钟标识。

### 注释 10：原第 201 行

`AMEBA_RTC_CLK` 时钟标识。

### 注释 11：原第 263 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_AMEBAD_CLOCK_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/amebad__clock_8h.html)

---

[返回大纲](大纲.md) · [下一章](P002_avrcp.h_源码浏览.md)
