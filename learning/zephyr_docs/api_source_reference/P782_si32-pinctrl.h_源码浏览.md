---
id: learning.zephyr-docs.api-source-reference.page-782
title: si32-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/si32-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第782章\_si32-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/si32-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/si32-pinctrl_8h.html)。

## 782.1\_原始可见代码（Source Code）

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
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>

```c
/*
 * Copyright (c) 2024 GARDENA GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SI32_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SI32_PINCTRL_H_

#define SI32_SIGNAL_USART0_TX   0
#define SI32_SIGNAL_USART0_RX   1
#define SI32_SIGNAL_USART0_RTS  2
#define SI32_SIGNAL_USART0_CTS  3
#define SI32_SIGNAL_USART0_UCLK 4

#define SI32_SIGNAL_SPI0_SCK  5
#define SI32_SIGNAL_SPI0_MISO 6
#define SI32_SIGNAL_SPI0_MOSI 7
#define SI32_SIGNAL_SPI0_NSS  8

#define SI32_SIGNAL_USART1_TX   9
#define SI32_SIGNAL_USART1_RX   10
#define SI32_SIGNAL_USART1_RTS  11
#define SI32_SIGNAL_USART1_CTS  12
#define SI32_SIGNAL_USART1_UCLK 13

#define SI32_SIGNAL_EPCA0_CEX0 14
#define SI32_SIGNAL_EPCA0_CEX1 15
#define SI32_SIGNAL_EPCA0_CEX2 16
#define SI32_SIGNAL_EPCA0_CEX3 17
#define SI32_SIGNAL_EPCA0_CEX4 18
#define SI32_SIGNAL_EPCA0_CEX4 19

#define SI32_SIGNAL_PCA0_CEX0 20
#define SI32_SIGNAL_PCA0_CEX1 21

#define SI32_SIGNAL_PCA1_CEX0 22
#define SI32_SIGNAL_PCA1_CEX1 23

#define SI32_SIGNAL_EPCA0_ECI 24

#define SI32_SIGNAL_PCA0_ECI 25

#define SI32_SIGNAL_PCA1_ECI 26

#define SI32_SIGNAL_I2S0_TX_WS  27
#define SI32_SIGNAL_I2S0_TX_SCK 28
#define SI32_SIGNAL_I2S0_TX_SD  29

#define SI32_SIGNAL_I2C0_SDA 30
#define SI32_SIGNAL_I2C0_SCL 31

#define SI32_SIGNAL_CMP0S 32
#define SI32_SIGNAL_CMP0A 33

#define SI32_SIGNAL_CMP1S 34
#define SI32_SIGNAL_CMP1A 35

#define SI32_SIGNAL_TIMER0_CT 36
#define SI32_SIGNAL_TIMER0_EX 37

#define SI32_SIGNAL_TIMER1_CT 38
#define SI32_SIGNAL_TIMER1_EX 39

#define SI32_SIGNAL_UART0_TX  40
#define SI32_SIGNAL_UART0_RX  41
#define SI32_SIGNAL_UART0_RTS 42
#define SI32_SIGNAL_UART0_CTS 43

#define SI32_SIGNAL_UART1_TX 44
#define SI32_SIGNAL_UART1_RX 45

#define SI32_SIGNAL_SPI1_SCK  46
#define SI32_SIGNAL_SPI1_MISO 47
#define SI32_SIGNAL_SPI1_MOSI 48
#define SI32_SIGNAL_SPI1_NSS  49

#define SI32_SIGNAL_SPI2_SCK  50
#define SI32_SIGNAL_SPI2_MISO 51
#define SI32_SIGNAL_SPI2_MOSI 52
#define SI32_SIGNAL_SPI2_NSS  53

#define SI32_SIGNAL_AHB_OUT 54

#define SI32_SIGNAL_SSG0_EX0 55
#define SI32_SIGNAL_SSG0_EX1 56
#define SI32_SIGNAL_SSG0_EX2 57
#define SI32_SIGNAL_SSG0_EX3 58

#define SI32_SIGNAL_RTC0_OUT 59

#define SI32_SIGNAL_I2S0_RX_WS  60
#define SI32_SIGNAL_I2S0_RX_SCK 61
#define SI32_SIGNAL_I2S0_RX_SD  62

#define SI32_SIGNAL_LPTIMER0_OUT 63

#define SI32_SIGNAL_I2C1_SDA 64
#define SI32_SIGNAL_I2C1_SCL 65

#define SI32_SIGNAL_PB_HDKILL 66

#define SI32_MUX(fun, port, pin)                                                                   \
        ((((port)&0x7)) | (((pin)&0xF) << 3) | ((SI32_SIGNAL_##fun & 0x7F) << 22))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SI32_PINCTRL_H_ */
```

## 782.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 GARDENA GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 113 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SI32_PINCTRL_H_`。

## 782.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/si32-pinctrl_8h.html)

---

[上一章](P781_sht4x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P783_sifive-pinctrl.h_源码浏览.md)
