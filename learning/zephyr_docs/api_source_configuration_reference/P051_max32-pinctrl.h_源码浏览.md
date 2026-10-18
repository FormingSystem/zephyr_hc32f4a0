---
id: learning.zephyr-docs.api-source-configuration-reference.page-51
title: max32-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/max32-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_max32-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/max32-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/max32-pinctrl_8h.html)。

## 51.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00043"></a>
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

```c
/*
 * Copyright (c) 2023-2024 Analog Devices, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MAX32_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MAX32_PINCTRL_H_

#define MAX32_MODE_GPIO 0x00
#define MAX32_MODE_AF1  0x01
#define MAX32_MODE_AF2  0x02
#define MAX32_MODE_AF3  0x03
#define MAX32_MODE_AF4  0x04
#define MAX32_MODE_AF5  0x05

#define MAX32_MODE_SHIFT 0U
#define MAX32_MODE_MASK  0x0FU
#define MAX32_PORT_SHIFT 4U
#define MAX32_PORT_MASK  0x0FU
#define MAX32_PIN_SHIFT  8U
#define MAX32_PIN_MASK   0xFFU

#define MAX32_PINMUX(port, pin, mode)                                                              \
        ((((port)&MAX32_PORT_MASK) << MAX32_PORT_SHIFT) |                                          \
         (((pin)&MAX32_PIN_MASK) << MAX32_PIN_SHIFT) |                                             \
         (((MAX32_MODE_##mode) & MAX32_MODE_MASK) << MAX32_MODE_SHIFT))

#define MAX32_PINMUX_PORT(pinmux) (((pinmux) >> MAX32_PORT_SHIFT) & MAX32_PORT_MASK)
#define MAX32_PINMUX_PIN(pinmux)  (((pinmux) >> MAX32_PIN_SHIFT) & MAX32_PIN_MASK)
#define MAX32_PINMUX_MODE(pinmux) (((pinmux) >> MAX32_MODE_SHIFT) & MAX32_MODE_MASK)

/* Selects the voltage rail used for the pin */
#define MAX32_VSEL_VDDIO  0
#define MAX32_VSEL_VDDIOH 1

#define MAX32_INPUT_ENABLE_SHIFT   0x00
#define MAX32_BIAS_PULL_UP_SHIFT   0x01
#define MAX32_BIAS_PULL_DOWN_SHIFT 0x02
#define MAX32_OUTPUT_ENABLE_SHIFT  0x03
#define MAX32_POWER_SOURCE_SHIFT   0x04
#define MAX32_OUTPUT_HIGH_SHIFT    0x05
#define MAX32_DRV_STRENGTH_SHIFT   0x06 /* 2 bits */
#define MAX32_DRV_STRENGTH_MASK    0x03

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MAX32_PINCTRL_H_ */
```

## 51.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023-2024 Analog Devices, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

选择该引脚使用的电压轨（Voltage rail）。

### 注释 3：原第 65 行

2 位。

### 注释 4：原第 68 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MAX32_PINCTRL_H_`。

## 51.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/max32-pinctrl_8h.html)

---

[上一章](P050_math.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P052_mchp_pic32cm_pl_clock.h_源码浏览.md)
