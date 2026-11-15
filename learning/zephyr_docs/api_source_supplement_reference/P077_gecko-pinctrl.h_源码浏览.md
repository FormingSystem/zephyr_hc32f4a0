---
id: learning.zephyr-docs.api-source-supplement-reference.page-77
title: gecko-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_gecko-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl_8h.html)。

## 77.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
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
<a id="l00075"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="foldopen00094"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>

```c
/*
 * Copyright (c) 2022 Silicon Labs
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_GECKO_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_GECKO_PINCTRL_H_

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
#define GECKO_FUN_UART_LOC 4U

#define GECKO_FUN_SPI_MISO 5U
#define GECKO_FUN_SPI_MOSI 6U
#define GECKO_FUN_SPI_CSN  7U
#define GECKO_FUN_SPI_SCK  8U

#define GECKO_FUN_I2C_SDA 9U
#define GECKO_FUN_I2C_SCL 10U
#define GECKO_FUN_I2C_SDA_LOC 11U
#define GECKO_FUN_I2C_SCL_LOC 12U


#define GECKO_PSEL(fun, port, pin)                                                                 \
        (((GECKO_PORT_##port & GECKO_PORT_MSK) << GECKO_PORT_POS) |                                \
         ((GECKO_PIN(##pin##) & GECKO_PIN_MSK) << GECKO_PIN_POS) |                                 \
         ((GECKO_FUN_##fun & GECKO_FUN_MSK) << GECKO_FUN_POS))

#define GECKO_LOC(fun, loc)                                                                        \
        (((GECKO_LOCATION(##loc##) & GECKO_LOC_MSK) << GECKO_LOC_POS) |                            \
         ((GECKO_FUN_##fun##_LOC & GECKO_FUN_MSK) << GECKO_FUN_POS))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_GECKO_PINCTRL_H_ */
```

## 77.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Silicon Labs。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 9 行

全部 `GECKO_pin` 配置信息编码在一个 32 位位域（Bitfield）中，组织如下：

- `31..24`：引脚功能。
- `23..16`：保留。
- `15..8`：用于 `UART_RX`/`UART_TX` 功能的端口。
- `7..0`：用于 `UART_RX`/`UART_TX` 功能的引脚编号。
- `15..8`：用于 `UART_LOC` 功能时保留。
- `7..0`：用于 `UART_LOC` 功能的位置（Loc）。

### 注释 3：原第 98 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_GECKO_PINCTRL_H_`。

## 77.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gecko-pinctrl_8h.html)

---

[上一章](P076_gecko-pinctrl-s1.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P078_generic.h_源码浏览.md)
