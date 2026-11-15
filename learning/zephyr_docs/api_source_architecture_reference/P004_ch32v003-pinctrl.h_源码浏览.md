---
id: learning.zephyr-docs.api-source-architecture-reference.page-4
title: ch32v003-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ch32v003-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_ch32v003-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ch32v003-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P036_zephyr__dt-bindings__pinctrl__ch32v003-pinctrl.h_文件参考.md)。

## 4.1\_原始可见代码（Source Code）

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
<a id="foldopen00041"></a>
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

```c
/*
 * Copyright (c) 2024 Michael Hope
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CH32V003_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CH32V003_PINCTRL_H_

#define CH32V003_PINMUX_PORT_PA 0
#define CH32V003_PINMUX_PORT_PC 1
#define CH32V003_PINMUX_PORT_PD 2

/*
 * Defines the starting bit for the remap field. Note that the I2C1 and USART1 fields are not
 * contiguous.
 */
#define CH32V003_PINMUX_SPI1_RM    0
#define CH32V003_PINMUX_I2C1_RM    1
#define CH32V003_PINMUX_I2C1_RM1   22
#define CH32V003_PINMUX_USART1_RM  2
#define CH32V003_PINMUX_USART1_RM1 21
#define CH32V003_PINMUX_TIM1_RM    6
#define CH32V003_PINMUX_TIM1_RM1   23
#define CH32V003_PINMUX_TIM2_RM    8
/*
 * ADC1 is not remappable but re-uses the remap field to encode that the pin needs to use
 * analog input mode.
 */
#define CH32V003_PINMUX_ADC1_RM    3

/* Port number with 0-2 */
#define CH32V003_PINCTRL_PORT_SHIFT    0
/* Pin number 0-15 */
#define CH32V003_PINCTRL_PIN_SHIFT     2
/* Base remap bit 0-31 */
#define CH32V003_PINCTRL_RM_BASE_SHIFT 6
/* Function remapping ID 0-3 */
#define CH32V003_PINCTRL_RM_SHIFT      11

#define CH32V003_PINMUX_DEFINE(port, pin, rm, remapping)                                           \
        ((CH32V003_PINMUX_PORT_##port << CH32V003_PINCTRL_PORT_SHIFT) |                            \
         (pin << CH32V003_PINCTRL_PIN_SHIFT) |                                                     \
         (CH32V003_PINMUX_##rm##_RM << CH32V003_PINCTRL_RM_BASE_SHIFT) |                           \
         (remapping << CH32V003_PINCTRL_RM_SHIFT))

#define TIM1_ETR_PC5_0  CH32V003_PINMUX_DEFINE(PC, 5, TIM1, 0)
#define TIM1_ETR_PC5_1  CH32V003_PINMUX_DEFINE(PC, 5, TIM1, 1)
#define TIM1_ETR_PD4_2  CH32V003_PINMUX_DEFINE(PD, 4, TIM1, 2)
#define TIM1_ETR_PC2_3  CH32V003_PINMUX_DEFINE(PC, 2, TIM1, 3)
#define TIM1_CH1_PD2_0  CH32V003_PINMUX_DEFINE(PD, 2, TIM1, 0)
#define TIM1_CH1_PC6_1  CH32V003_PINMUX_DEFINE(PC, 6, TIM1, 1)
#define TIM1_CH1_PD2_2  CH32V003_PINMUX_DEFINE(PD, 2, TIM1, 2)
#define TIM1_CH1_PC4_3  CH32V003_PINMUX_DEFINE(PC, 4, TIM1, 3)
#define TIM1_CH2_PA1_0  CH32V003_PINMUX_DEFINE(PA, 1, TIM1, 0)
#define TIM1_CH2_PC7_1  CH32V003_PINMUX_DEFINE(PC, 7, TIM1, 1)
#define TIM1_CH2_PA1_2  CH32V003_PINMUX_DEFINE(PA, 1, TIM1, 2)
#define TIM1_CH2_PC7_3  CH32V003_PINMUX_DEFINE(PC, 7, TIM1, 3)
#define TIM1_CH3_PC3_0  CH32V003_PINMUX_DEFINE(PC, 3, TIM1, 0)
#define TIM1_CH3_PC0_1  CH32V003_PINMUX_DEFINE(PC, 0, TIM1, 1)
#define TIM1_CH3_PC3_2  CH32V003_PINMUX_DEFINE(PC, 3, TIM1, 2)
#define TIM1_CH3_PC5_3  CH32V003_PINMUX_DEFINE(PC, 5, TIM1, 3)
#define TIM1_CH4_PC4_0  CH32V003_PINMUX_DEFINE(PC, 4, TIM1, 0)
#define TIM1_CH4_PD3_1  CH32V003_PINMUX_DEFINE(PD, 3, TIM1, 1)
#define TIM1_CH4_PC4_2  CH32V003_PINMUX_DEFINE(PC, 4, TIM1, 2)
#define TIM1_CH4_PD4_3  CH32V003_PINMUX_DEFINE(PD, 4, TIM1, 3)
#define TIM1_BKIN_PC2_0 CH32V003_PINMUX_DEFINE(PC, 2, TIM1, 0)
#define TIM1_BKIN_PC1_1 CH32V003_PINMUX_DEFINE(PC, 1, TIM1, 1)
#define TIM1_BKIN_PC2_2 CH32V003_PINMUX_DEFINE(PC, 2, TIM1, 2)
#define TIM1_BKIN_PC1_3 CH32V003_PINMUX_DEFINE(PC, 1, TIM1, 3)
#define TIM1_CH1N_PD0_0 CH32V003_PINMUX_DEFINE(PD, 0, TIM1, 0)
#define TIM1_CH1N_PC3_1 CH32V003_PINMUX_DEFINE(PC, 3, TIM1, 1)
#define TIM1_CH1N_PD0_2 CH32V003_PINMUX_DEFINE(PD, 0, TIM1, 2)
#define TIM1_CH1N_PC3_3 CH32V003_PINMUX_DEFINE(PC, 3, TIM1, 3)
#define TIM1_CH2N_PA2_0 CH32V003_PINMUX_DEFINE(PA, 2, TIM1, 0)
#define TIM1_CH2N_PC4_1 CH32V003_PINMUX_DEFINE(PC, 4, TIM1, 1)
#define TIM1_CH2N_PA2_2 CH32V003_PINMUX_DEFINE(PA, 2, TIM1, 2)
#define TIM1_CH2N_PD2_3 CH32V003_PINMUX_DEFINE(PD, 2, TIM1, 3)
#define TIM1_CH3N_PD1_0 CH32V003_PINMUX_DEFINE(PD, 1, TIM1, 0)
#define TIM1_CH3N_PD1_1 CH32V003_PINMUX_DEFINE(PD, 1, TIM1, 1)
#define TIM1_CH3N_PD1_2 CH32V003_PINMUX_DEFINE(PD, 1, TIM1, 2)
#define TIM1_CH3N_PC6_3 CH32V003_PINMUX_DEFINE(PC, 6, TIM1, 3)

#define TIM2_ETR_PD4_0 CH32V003_PINMUX_DEFINE(PD, 4, TIM2, 0)
#define TIM2_ETR_PC5_1 CH32V003_PINMUX_DEFINE(PC, 5, TIM2, 1)
#define TIM2_ETR_PC1_2 CH32V003_PINMUX_DEFINE(PC, 1, TIM2, 2)
#define TIM2_ETR_PC1_3 CH32V003_PINMUX_DEFINE(PC, 1, TIM2, 3)
#define TIM2_CH1_PD4_0 CH32V003_PINMUX_DEFINE(PD, 4, TIM2, 0)
#define TIM2_CH1_PC5_1 CH32V003_PINMUX_DEFINE(PC, 5, TIM2, 1)
#define TIM2_CH1_PC1_2 CH32V003_PINMUX_DEFINE(PC, 1, TIM2, 2)
#define TIM2_CH1_PC1_3 CH32V003_PINMUX_DEFINE(PC, 1, TIM2, 3)
#define TIM2_CH2_PD3_0 CH32V003_PINMUX_DEFINE(PD, 3, TIM2, 0)
#define TIM2_CH2_PC2_1 CH32V003_PINMUX_DEFINE(PC, 2, TIM2, 1)
#define TIM2_CH2_PD3_2 CH32V003_PINMUX_DEFINE(PD, 3, TIM2, 2)
#define TIM2_CH2_PC7_3 CH32V003_PINMUX_DEFINE(PC, 7, TIM2, 3)
#define TIM2_CH3_PC0_0 CH32V003_PINMUX_DEFINE(PC, 0, TIM2, 0)
#define TIM2_CH3_PD2_1 CH32V003_PINMUX_DEFINE(PD, 2, TIM2, 1)
#define TIM2_CH3_PC0_2 CH32V003_PINMUX_DEFINE(PC, 0, TIM2, 2)
#define TIM2_CH3_PD6_3 CH32V003_PINMUX_DEFINE(PD, 6, TIM2, 3)
#define TIM2_CH4_PD7_0 CH32V003_PINMUX_DEFINE(PD, 7, TIM2, 0)
#define TIM2_CH4_PC1_1 CH32V003_PINMUX_DEFINE(PC, 1, TIM2, 1)
#define TIM2_CH4_PD7_2 CH32V003_PINMUX_DEFINE(PD, 7, TIM2, 2)
#define TIM2_CH4_PD5_3 CH32V003_PINMUX_DEFINE(PD, 5, TIM2, 3)

#define USART1_CK_PD4_0  CH32V003_PINMUX_DEFINE(PD, 4, USART1, 0)
#define USART1_CK_PD7_1  CH32V003_PINMUX_DEFINE(PD, 7, USART1, 1)
#define USART1_CK_PD7_2  CH32V003_PINMUX_DEFINE(PD, 7, USART1, 2)
#define USART1_CK_PC5_3  CH32V003_PINMUX_DEFINE(PC, 5, USART1, 3)
#define USART1_TX_PD5_0  CH32V003_PINMUX_DEFINE(PD, 5, USART1, 0)
#define USART1_TX_PD0_1  CH32V003_PINMUX_DEFINE(PD, 0, USART1, 1)
#define USART1_TX_PD6_2  CH32V003_PINMUX_DEFINE(PD, 6, USART1, 2)
#define USART1_TX_PC0_3  CH32V003_PINMUX_DEFINE(PC, 0, USART1, 3)
#define USART1_RX_PD6_0  CH32V003_PINMUX_DEFINE(PD, 6, USART1, 0)
#define USART1_RX_PD1_1  CH32V003_PINMUX_DEFINE(PD, 1, USART1, 1)
#define USART1_RX_PD5_2  CH32V003_PINMUX_DEFINE(PD, 5, USART1, 2)
#define USART1_RX_PC1_3  CH32V003_PINMUX_DEFINE(PC, 1, USART1, 3)
#define USART1_CTS_PD3_0 CH32V003_PINMUX_DEFINE(PD, 3, USART1, 0)
#define USART1_CTS_PC3_1 CH32V003_PINMUX_DEFINE(PC, 3, USART1, 1)
#define USART1_CTS_PC6_2 CH32V003_PINMUX_DEFINE(PC, 6, USART1, 2)
#define USART1_CTS_PC6_3 CH32V003_PINMUX_DEFINE(PC, 6, USART1, 3)
#define USART1_RTS_PC2_0 CH32V003_PINMUX_DEFINE(PC, 2, USART1, 0)
#define USART1_RTS_PC2_1 CH32V003_PINMUX_DEFINE(PC, 2, USART1, 1)
#define USART1_RTS_PC7_2 CH32V003_PINMUX_DEFINE(PC, 7, USART1, 2)
#define USART1_RTS_PC7_3 CH32V003_PINMUX_DEFINE(PC, 7, USART1, 3)

#define SPI1_NSS_PC1_0  CH32V003_PINMUX_DEFINE(PC, 1, SPI1, 0)
#define SPI1_NSS_PC0_1  CH32V003_PINMUX_DEFINE(PC, 0, SPI1, 1)
#define SPI1_SCK_PC5_0  CH32V003_PINMUX_DEFINE(PC, 5, SPI1, 0)
#define SPI1_SCK_PC5_1  CH32V003_PINMUX_DEFINE(PC, 5, SPI1, 1)
#define SPI1_MISO_PC7_0 CH32V003_PINMUX_DEFINE(PC, 7, SPI1, 0)
#define SPI1_MISO_PC7_1 CH32V003_PINMUX_DEFINE(PC, 7, SPI1, 1)
#define SPI1_MOSI_PC6_0 CH32V003_PINMUX_DEFINE(PC, 6, SPI1, 0)
#define SPI1_MOSI_PC6_1 CH32V003_PINMUX_DEFINE(PC, 6, SPI1, 1)

#define I2C1_SCL_PC2_0 CH32V003_PINMUX_DEFINE(PC, 2, I2C1, 0)
#define I2C1_SCL_PD1_1 CH32V003_PINMUX_DEFINE(PD, 1, I2C1, 1)
#define I2C1_SCL_PC5_2 CH32V003_PINMUX_DEFINE(PC, 5, I2C1, 2)
#define I2C1_SDA_PC1_0 CH32V003_PINMUX_DEFINE(PC, 1, I2C1, 0)
#define I2C1_SDA_PD0_1 CH32V003_PINMUX_DEFINE(PD, 0, I2C1, 1)
#define I2C1_SDA_PC6_2 CH32V003_PINMUX_DEFINE(PC, 6, I2C1, 2)

#define ADC1_A0_PA2_0 CH32V003_PINMUX_DEFINE(PA, 2, ADC1, 0)
#define ADC1_A1_PA1_0 CH32V003_PINMUX_DEFINE(PA, 1, ADC1, 0)
#define ADC1_A2_PC4_0 CH32V003_PINMUX_DEFINE(PC, 4, ADC1, 0)
#define ADC1_A4_PD3_0 CH32V003_PINMUX_DEFINE(PD, 3, ADC1, 0)
#define ADC1_A3_PD2_0 CH32V003_PINMUX_DEFINE(PD, 2, ADC1, 0)
#define ADC1_A5_PD5_0 CH32V003_PINMUX_DEFINE(PD, 5, ADC1, 0)
#define ADC1_A7_PD4_0 CH32V003_PINMUX_DEFINE(PD, 4, ADC1, 0)
#define ADC1_A6_PD6_0 CH32V003_PINMUX_DEFINE(PD, 6, ADC1, 0)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CH32V003_PINCTRL_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Michael Hope。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 14 行

定义重映射字段（Remap Field）的起始位（Starting Bit）。注意，I2C1 和 USART1 的字段并不连续（Not Contiguous）。

### 注释 3：原第 26 行

ADC1 不可重映射（Not Remappable），但复用重映射字段（Remap Field），用来编码该引脚需要使用模拟输入模式（Analog Input Mode）。

### 注释 4：原第 32 行

端口编号（Port Number）：0～2。

### 注释 5：原第 34 行

引脚编号（Pin Number）：0～15。

### 注释 6：原第 36 行

重映射基础位（Base Remap Bit）：0～31。

### 注释 7：原第 38 行

功能重映射标识（Function Remapping ID）：0～3。

### 注释 8：原第 151 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CH32V003_PINCTRL_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P036_zephyr__dt-bindings__pinctrl__ch32v003-pinctrl.h_文件参考.md)

---

[上一章](P003_blob_cli.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_ch32v00x-pinctrl.h_源码浏览.md)
