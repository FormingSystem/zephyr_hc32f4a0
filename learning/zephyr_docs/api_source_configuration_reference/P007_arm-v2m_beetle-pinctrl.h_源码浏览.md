---
id: learning.zephyr-docs.api-source-configuration-reference.page-7
title: arm-v2m_beetle-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arm-v2m__beetle-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_arm-v2m\_beetle-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/arm-v2m__beetle-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/arm-v2m__beetle-pinctrl_8h.html)。

## 7.1\_原始可见代码（Source Code）

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
<a id="foldopen00022"></a>
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

```c
/*
 * Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ARM_V2M_BEETLE_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ARM_V2M_BEETLE_PINCTRL_H_

#define V2M_BEETLE_ALT_FUNC_POS 0
#define V2M_BEETLE_ALT_FUNC_MASK 0x7

#define V2M_BEETLE_EXP_NUM_POS 3
#define V2M_BEETLE_EXP_NUM_MASK 0x1F8

#define V2M_BEETLE_PINCTRL_FUNC_UART 0
#define V2M_BEETLE_PINCTRL_FUNC_GPIO 1
#define V2M_BEETLE_PINCTRL_FUNC_I2C 2
#define V2M_BEETLE_PINCTRL_FUNC_SPI 3
#define V2M_BEETLE_PINCTRL_FUNC_QSPI 4

#define V2M_BEETLE_PINMUX(alt_func, exp_num) (exp_num << V2M_BEETLE_EXP_NUM_POS | \
        alt_func << V2M_BEETLE_ALT_FUNC_POS)



/* GPIO 0 */
#define UART0_RXD_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_UART, 0)
#define UART0_TXD_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_UART, 1)
#define SPI0_SS_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_SPI, 10)
#define SPI0_MOSI_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_SPI, 11)
#define SPI0_MISO_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_SPI, 12)
#define SPI0_SCK_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_SPI, 13)
#define SBCON0_SDA_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_I2C, 14)
#define SBCON0_SCL_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_I2C, 15)

/* GPIO 1 */
#define UART1_RXD_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_UART, 16)
#define UART1_TXD_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_UART, 17)
#define SPI1_SS_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_SPI, 18)
#define SPI1_MOSI_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_SPI, 19)
#define SPI1_MISO_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_SPI, 20)
#define SPI1_SCK_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_SPI, 21)
#define SBCON1_SDA_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_I2C, 22)
#define SBCON1_SCL_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_I2C, 23)
#define QSPI_CS2_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_QSPI, 24)
#define QSPI_CS1_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_QSPI, 25)
#define QSPI_IOF0_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_QSPI, 26)
#define QSPI_IOF1_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_QSPI, 27)
#define QSPI_IOF2_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_QSPI, 28)
#define QSPI_IOF3_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_QSPI, 29)
#define QSPI_SCK_EXP V2M_BEETLE_PINMUX(V2M_BEETLE_PINCTRL_FUNC_QSPI, 30)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ARM_V2M_BEETLE_PINCTRL_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 Arm Limited and/or its affiliates <open-source-office@arm.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 27 行

GPIO 0。

### 注释 3：原第 37 行

GPIO 1。

### 注释 4：原第 54 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ARM_V2M_BEETLE_PINCTRL_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/arm-v2m__beetle-pinctrl_8h.html)

---

[上一章](P006_arm-mps4-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_canbus.h_源码浏览.md)
