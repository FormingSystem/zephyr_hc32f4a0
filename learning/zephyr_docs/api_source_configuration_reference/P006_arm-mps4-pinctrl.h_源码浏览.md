---
id: learning.zephyr-docs.api-source-configuration-reference.page-6
title: arm-mps4-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arm-mps4-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_arm-mps4-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/arm-mps4-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/arm-mps4-pinctrl_8h.html)。

## 6.1\_原始可见代码（Source Code）

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
<a id="foldopen00021"></a>
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

```c
/*
 * Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ARM_MPS4_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ARM_MPS4_PINCTRL_H_

#define MPS4_ALT_FUNC_POS 0
#define MPS4_ALT_FUNC_MASK 0x7

#define MPS4_EXP_NUM_POS 3
#define MPS4_EXP_NUM_MASK 0x1F8

#define MPS4_PINCTRL_FUNC_UART 0
#define MPS4_PINCTRL_FUNC_GPIO 1
#define MPS4_PINCTRL_FUNC_I2C 2
#define MPS4_PINCTRL_FUNC_SPI 3

#define MPS4_PINMUX(alt_func, exp_num) (exp_num << MPS4_EXP_NUM_POS | \
        alt_func << MPS4_ALT_FUNC_POS)

/* GPIO 0 */
#define UART3_RXD_EXP  MPS4_PINMUX(MPS4_PINCTRL_FUNC_UART, 0)
#define UART3_TXD_EXP  MPS4_PINMUX(MPS4_PINCTRL_FUNC_UART, 1)
#define SPI3_SS_EXP    MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 10)
#define SPI3_MOSI_EXP  MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 11)
#define SPI3_MISO_EXP  MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 12)
#define SPI3_SCK_EXP   MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI, 13)
#define SBCON2_SDA_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_I2C, 14)
#define SBCON2_SCL_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_I2C, 15)


/* GPIO 1 */
#define UART4_RXD_EXP  MPS4_PINMUX(MPS4_PINCTRL_FUNC_UART, 16)
#define UART4_TXD_EXP  MPS4_PINMUX(MPS4_PINCTRL_FUNC_UART, 17)
#define SPI4_SS_EXP    MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI,  26)
#define SPI4_MOSI_EXP  MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI,  27)
#define SPI4_MISO_EXP  MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI,  28)
#define SPI4_SCK_EXP   MPS4_PINMUX(MPS4_PINCTRL_FUNC_SPI,  29)
#define SBCON3_SDA_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_I2C,  30)
#define SBCON3_SCL_EXP MPS4_PINMUX(MPS4_PINCTRL_FUNC_I2C,  31)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ARM_MPS4_PINCTRL_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 Arm Limited and/or its affiliates <open-source-office@arm.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 24 行

GPIO 0。

### 注释 3：原第 35 行

GPIO 1。

### 注释 4：原第 45 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ARM_MPS4_PINCTRL_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/arm-mps4-pinctrl_8h.html)

---

[上一章](P005_arm-mps3-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_arm-v2m_beetle-pinctrl.h_源码浏览.md)
