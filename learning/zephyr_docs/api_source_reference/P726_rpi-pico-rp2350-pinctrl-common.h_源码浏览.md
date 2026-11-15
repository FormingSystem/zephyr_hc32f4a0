---
id: learning.zephyr-docs.api-source-reference.page-726
title: rpi-pico-rp2350-pinctrl-common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-rp2350-pinctrl-common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第726章\_rpi-pico-rp2350-pinctrl-common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-rp2350-pinctrl-common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-rp2350-pinctrl-common_8h.html)。

## 726.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
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
<a id="l00074"></a>
<a id="l00075"></a>
<a id="arpi-pico-pinctrl-common_8h_html"></a>

```c
/*
 * Copyright (c) 2024, Andrew Featherstone
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RPI_PICO_RP2350_PINCTRL_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RPI_PICO_RP2350_PINCTRL_COMMON_H_


#define RP2_PINCTRL_GPIO_FUNC_HSTX 0

#define RP2_PINCTRL_GPIO_FUNC_PIO2     8
#define RP2_PINCTRL_GPIO_FUNC_GPCK     9
#define RP2_PINCTRL_GPIO_FUNC_USB      10
#define RP2_PINCTRL_GPIO_FUNC_UART_ALT 11
#define RP2_PINCTRL_GPIO_FUNC_NULL     0x1f

#include "rpi-pico-pinctrl-common.h"

#define PIO2_P0  RP2XXX_PINMUX(0, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P1  RP2XXX_PINMUX(1, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P2  RP2XXX_PINMUX(2, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P3  RP2XXX_PINMUX(3, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P4  RP2XXX_PINMUX(4, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P5  RP2XXX_PINMUX(5, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P6  RP2XXX_PINMUX(6, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P7  RP2XXX_PINMUX(7, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P8  RP2XXX_PINMUX(8, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P9  RP2XXX_PINMUX(9, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P10 RP2XXX_PINMUX(10, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P11 RP2XXX_PINMUX(11, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P12 RP2XXX_PINMUX(12, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P13 RP2XXX_PINMUX(13, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P14 RP2XXX_PINMUX(14, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P15 RP2XXX_PINMUX(15, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P16 RP2XXX_PINMUX(16, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P17 RP2XXX_PINMUX(17, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P18 RP2XXX_PINMUX(18, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P19 RP2XXX_PINMUX(19, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P20 RP2XXX_PINMUX(20, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P21 RP2XXX_PINMUX(21, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P22 RP2XXX_PINMUX(22, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P23 RP2XXX_PINMUX(23, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P24 RP2XXX_PINMUX(24, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P25 RP2XXX_PINMUX(25, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P26 RP2XXX_PINMUX(26, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P27 RP2XXX_PINMUX(27, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P28 RP2XXX_PINMUX(28, RP2_PINCTRL_GPIO_FUNC_PIO2)
#define PIO2_P29 RP2XXX_PINMUX(29, RP2_PINCTRL_GPIO_FUNC_PIO2)

#define GPIN0_P12  RP2XXX_PINMUX(20, RP2_PINCTRL_GPIO_FUNC_GPCK)
#define GPIN1_P14  RP2XXX_PINMUX(22, RP2_PINCTRL_GPIO_FUNC_GPCK)
#define GPOUT0_P13 RP2XXX_PINMUX(21, RP2_PINCTRL_GPIO_FUNC_GPCK)
#define GPOUT1_P15 RP2XXX_PINMUX(23, RP2_PINCTRL_GPIO_FUNC_GPCK)

#define UART0_TX_P2  RP2XXX_PINMUX(2, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART0_RX_P3  RP2XXX_PINMUX(3, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART1_TX_P6  RP2XXX_PINMUX(6, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART1_RX_P7  RP2XXX_PINMUX(7, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART1_TX_P10 RP2XXX_PINMUX(10, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART1_RX_P11 RP2XXX_PINMUX(11, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART0_TX_P14 RP2XXX_PINMUX(14, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART0_RX_P15 RP2XXX_PINMUX(15, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART0_TX_P18 RP2XXX_PINMUX(18, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART0_RX_P19 RP2XXX_PINMUX(19, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART1_TX_P22 RP2XXX_PINMUX(22, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART1_RX_P23 RP2XXX_PINMUX(23, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART1_TX_P26 RP2XXX_PINMUX(26, RP2_PINCTRL_GPIO_FUNC_UART_ALT)
#define UART1_RX_P27 RP2XXX_PINMUX(27, RP2_PINCTRL_GPIO_FUNC_UART_ALT)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RPI_PICO_RP2350_PINCTRL_COMMON_H_ */
```

## 726.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024, Andrew Featherstone。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 75 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RPI_PICO_RP2350_PINCTRL_COMMON_H_`。

## 726.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-rp2350-pinctrl-common_8h.html)
- [rpi-pico-pinctrl-common.h](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-pinctrl-common_8h.html)

---

[上一章](P725_rpi-pico-rp2040-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P727_rpi_bcm283x_power.h_源码浏览.md)
