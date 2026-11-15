---
id: learning.zephyr-docs.api-source-reference.page-725
title: rpi-pico-rp2040-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-rp2040-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第725章\_rpi-pico-rp2040-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-rp2040-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-rp2040-pinctrl_8h.html)。

## 725.1\_原始可见代码（Source Code）

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
<a id="arpi-pico-pinctrl-common_8h_html"></a>

```c
/*
 * Copyright (c) 2021, Yonatan Schachter
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RPI_PICO_RP2040_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RPI_PICO_RP2040_PINCTRL_H_

#define RP2_PINCTRL_GPIO_FUNC_XIP  0
#define RP2_PINCTRL_GPIO_FUNC_GPCK 8
#define RP2_PINCTRL_GPIO_FUNC_USB  9
#define RP2_PINCTRL_GPIO_FUNC_NULL 0xf

#include "rpi-pico-pinctrl-common.h"

#define ADC_CH0_P26 RP2XXX_PINMUX(26, RP2_PINCTRL_GPIO_FUNC_NULL)
#define ADC_CH1_P27 RP2XXX_PINMUX(27, RP2_PINCTRL_GPIO_FUNC_NULL)
#define ADC_CH2_P28 RP2XXX_PINMUX(28, RP2_PINCTRL_GPIO_FUNC_NULL)
#define ADC_CH3_P29 RP2XXX_PINMUX(29, RP2_PINCTRL_GPIO_FUNC_NULL)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RPI_PICO_RP2040_PINCTRL_H_ */
```

## 725.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021, Yonatan Schachter。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 22 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RPI_PICO_RP2040_PINCTRL_H_`。

## 725.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-rp2040-pinctrl_8h.html)
- [rpi-pico-pinctrl-common.h](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-pinctrl-common_8h.html)

---

[上一章](P724_rpi-pico-dma-rp2350.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P726_rpi-pico-rp2350-pinctrl-common.h_源码浏览.md)
