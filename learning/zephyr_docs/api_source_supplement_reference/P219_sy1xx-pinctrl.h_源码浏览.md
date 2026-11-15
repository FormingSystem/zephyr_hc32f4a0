---
id: learning.zephyr-docs.api-source-supplement-reference.page-219
title: sy1xx-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sy1xx-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第219章\_sy1xx-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sy1xx-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sy1xx-pinctrl_8h.html)。

## 219.1\_原始可见代码（Source Code）

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

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 * Copyright (c) 2024 sensry.io
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SY1XX_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SY1XX_PINCTRL_H_

#define SY1XX_PAD(pad) (pad * 8)

#define SY1XX_UART0_PAD_CFG0 0x0020
#define SY1XX_UART1_PAD_CFG0 0x0024
#define SY1XX_UART2_PAD_CFG0 0x0028

#define SY1XX_SPI0_PAD_CFG0 0x002c
#define SY1XX_SPI0_PAD_CFG1 0x0030

#define SY1XX_SPI1_PAD_CFG0 0x0034
#define SY1XX_SPI1_PAD_CFG1 0x0038

#define SY1XX_SPI2_PAD_CFG0 0x003c
#define SY1XX_SPI2_PAD_CFG1 0x0040

#define SY1XX_SPI3_PAD_CFG0 0x0044
#define SY1XX_SPI3_PAD_CFG1 0x0048

#define SY1XX_SPI4_PAD_CFG0 0x004c
#define SY1XX_SPI4_PAD_CFG1 0x0050

#define SY1XX_SPI5_PAD_CFG0 0x0054
#define SY1XX_SPI5_PAD_CFG1 0x0058

#define SY1XX_SPI6_PAD_CFG0 0x005c
#define SY1XX_SPI6_PAD_CFG1 0x0060

#define SY1XX_I2C0_PAD_CFG0 0x0100
#define SY1XX_I2C1_PAD_CFG0 0x0104
#define SY1XX_I2C2_PAD_CFG0 0x0108
#define SY1XX_I2C3_PAD_CFG0 0x010c

#define SY1XX_GPIO0_PAD_CFG0 0x0110
#define SY1XX_GPIO0_PAD_CFG1 0x0114
#define SY1XX_GPIO0_PAD_CFG2 0x0118
#define SY1XX_GPIO0_PAD_CFG3 0x011c
#define SY1XX_GPIO0_PAD_CFG4 0x0120
#define SY1XX_GPIO0_PAD_CFG5 0x0124
#define SY1XX_GPIO0_PAD_CFG6 0x0128
#define SY1XX_GPIO0_PAD_CFG7 0x012c

#define SY1XX_RGMII0_PAD_CFG0 0x0130
#define SY1XX_RGMII0_PAD_CFG1 0x0134
#define SY1XX_RGMII0_PAD_CFG2 0x0138
#define SY1XX_RGMII0_PAD_CFG3 0x013c

#define SY1XX_CAN0_PAD_CFG0 0x0140

#define SY1XX_I2S0_PAD_CFG0 0x0144
#define SY1XX_I2S1_PAD_CFG0 0x0148
#define SY1XX_I2S2_PAD_CFG0 0x014c
#define SY1XX_I2S3_PAD_CFG0 0x0150

#define SY1XX_HBUS0_PAD_CFG0 0x0154
#define SY1XX_HBUS0_PAD_CFG1 0x0158
#define SY1XX_HBUS0_PAD_CFG2 0x015c
#define SY1XX_HBUS0_PAD_CFG3 0x0160

#define SY1XX_QSPI0_PAD_CFG0 0x0164
#define SY1XX_QSPI0_PAD_CFG1 0x0168

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SY1XX_PINCTRL_H_ */
```

## 219.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

版权（Copyright）：© 2024 sensry.io。

### 注释 2：原第 70 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SY1XX_PINCTRL_H_`。

## 219.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sy1xx-pinctrl_8h.html)

---

[上一章](P218_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P220_sysapic.h_源码浏览.md)
