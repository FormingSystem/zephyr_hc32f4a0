---
id: learning.zephyr-docs.api-source-supplement-reference.page-76
title: gecko-pinctrl-s1.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_gecko-pinctrl-s1.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html)。

## 76.1\_原始可见代码（Source Code）

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
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
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
<a id="l00111"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>

```c
/*
 * Copyright (c) 2023 Silicon Labs
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_GECKO_PINCTRL_S1_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_GECKO_PINCTRL_S1_H_


#define GECKO_PORT_A                 0
#define GECKO_PORT_B                 1
#define GECKO_PORT_C                 2
#define GECKO_PORT_D                 3
#define GECKO_PORT_E                 4
#define GECKO_PORT_F                 5
#define GECKO_PORT_G                 6
#define GECKO_PORT_H                 7
#define GECKO_PORT_I                 8
#define GECKO_PORT_J                 9
#define GECKO_PORT_K                10

#define GECKO_PIN(n)                (n)
#define GECKO_LOCATION(n)           (n)

/*
 * The whole GECKO_pin configuration information is encoded in a 32-bit bitfield
 * organized as follows:
 *
 * - 31..24: Pin function.
 * - 23..16: Reserved.
 * - 15..8:  Port for UART_RX/UART_TX functions.
 * - 7..0:   Pin number for UART_RX/UART_TX functions.
 * - 15..8:  Reserved for UART_LOC function.
 * - 7..0:   Loc for UART_LOC function.
 */


#define GECKO_FUN_POS 24U
#define GECKO_FUN_MSK 0xFFU

#define GECKO_PIN_POS 0U
#define GECKO_PIN_MSK 0xFFU

#define GECKO_PORT_POS 8U
#define GECKO_PORT_MSK 0xFFU

#define GECKO_LOC_POS 0U
#define GECKO_LOC_MSK 0xFFU



#define GECKO_FUN_UART_TX  0U
#define GECKO_FUN_UART_RX  1U
#define GECKO_FUN_UART_RTS 2U
#define GECKO_FUN_UART_CTS 3U
#define GECKO_FUN_UART_RX_LOC 4U
#define GECKO_FUN_UART_TX_LOC 5U
#define GECKO_FUN_UART_RTS_LOC 6U
#define GECKO_FUN_UART_CTS_LOC 7U

#define GECKO_FUN_SPIM_MISO 8U
#define GECKO_FUN_SPIM_MOSI 9U
#define GECKO_FUN_SPIM_CS  10U
#define GECKO_FUN_SPIM_SCK  11U

#define GECKO_FUN_LEUART_RX_LOC 12U
#define GECKO_FUN_LEUART_TX_LOC 13U

#define GECKO_FUN_SPIS_MISO 14U
#define GECKO_FUN_SPIS_MOSI 15U
#define GECKO_FUN_SPIS_CS  16U
#define GECKO_FUN_SPIS_SCK  17U

#define GECKO_FUN_SPI_MISO_LOC 18U
#define GECKO_FUN_SPI_MOSI_LOC 19U
#define GECKO_FUN_SPI_CS_LOC  20U
#define GECKO_FUN_SPI_SCK_LOC  21U

#define GECKO_FUN_I2C_SDA 22U
#define GECKO_FUN_I2C_SCL 23U
#define GECKO_FUN_I2C_SDA_LOC 24U
#define GECKO_FUN_I2C_SCL_LOC 25U



#define GECKO_PSEL(fun, port, pin)                                                                 \
        (((GECKO_PORT_##port & GECKO_PORT_MSK) << GECKO_PORT_POS) |                                \
         ((GECKO_PIN(##pin##) & GECKO_PIN_MSK) << GECKO_PIN_POS) |                                 \
         ((GECKO_FUN_##fun & GECKO_FUN_MSK) << GECKO_FUN_POS))

#define GECKO_LOC(fun, loc)                                                                        \
        (((GECKO_LOCATION(##loc##) & GECKO_LOC_MSK) << GECKO_LOC_POS) |                            \
         ((GECKO_FUN_##fun##_LOC & GECKO_FUN_MSK) << GECKO_FUN_POS))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_GECKO_PINCTRL_S1_H_ */
```

## 76.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Silicon Labs。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 25 行

全部 `GECKO_pin` 配置信息编码在一个 32 位位域（Bitfield）中，组织如下：

- `31..24`：引脚功能。
- `23..16`：保留。
- `15..8`：用于 `UART_RX`/`UART_TX` 功能的端口。
- `7..0`：用于 `UART_RX`/`UART_TX` 功能的引脚编号。
- `15..8`：用于 `UART_LOC` 功能时保留。
- `7..0`：用于 `UART_LOC` 功能的位置（Loc）。

### 注释 3：原第 134 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_GECKO_PINCTRL_S1_H_`。

## 76.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl-s1_8h.html)

---

[上一章](P075_gcc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P077_gecko-pinctrl.h_源码浏览.md)
