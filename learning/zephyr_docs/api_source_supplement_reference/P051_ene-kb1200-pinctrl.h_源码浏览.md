---
id: learning.zephyr-docs.api-source-supplement-reference.page-51
title: ene-kb1200-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ene-kb1200-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_ene-kb1200-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ene-kb1200-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ene-kb1200-pinctrl_8h.html)。

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
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) ENE Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ENE_KB1200_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ENE_KB1200_PINCTRL_H_

#include <zephyr/dt-bindings/dt-util.h>

#define PINMUX_FUNC_GPIO 0x00
#define PINMUX_FUNC_A    0x00
#define PINMUX_FUNC_B    0x01
#define PINMUX_FUNC_C    0x02
#define PINMUX_FUNC_D    0x03
#define PINMUX_FUNC_MAX  0x04

#define ENE_KB1200_NO_PUD_POS        12
#define ENE_KB1200_PD_POS            13
#define ENE_KB1200_PU_POS            14
#define ENE_KB1200_PUSH_PULL_POS     15
#define ENE_KB1200_OPEN_DRAIN_POS    16
#define ENE_KB1200_OUT_DIS_POS       17
#define ENE_KB1200_OUT_EN_POS        18
#define ENE_KB1200_OUT_HI_POS        19
#define ENE_KB1200_OUT_LO_POS        20
#define ENE_KB1200_PIN_LOW_POWER_POS 21

#define ENE_KB1200_PINMUX_PORT_POS 5
#define ENE_KB1200_PINMUX_PORT_MSK 0x7
#define ENE_KB1200_PINMUX_PIN_POS  0
#define ENE_KB1200_PINMUX_PIN_MSK  0x1f
#define ENE_KB1200_PINMUX_FUNC_POS 8
#define ENE_KB1200_PINMUX_FUNC_MSK 0xf

/*
 * f is function number
 * b[7:5] = pin bank
 * b[4:0] = pin position in bank
 * b[11:8] = function
 */
#define ENE_KB1200_PINMUX(n, f)                                                                    \
        (((((n) >> 5) & ENE_KB1200_PINMUX_PORT_MSK) << ENE_KB1200_PINMUX_PORT_POS) |               \
         (((n) & ENE_KB1200_PINMUX_PIN_MSK) << ENE_KB1200_PINMUX_PIN_POS) |                        \
         (((f) & ENE_KB1200_PINMUX_FUNC_MSK) << ENE_KB1200_PINMUX_FUNC_POS))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ENE_KB1200_PINCTRL_H_ */
```

## 51.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© ENE Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 37 行

`f` 为功能编号（Function number）。

- `b[7:5]`：引脚组（Pin bank）。
- `b[4:0]`：引脚在组内的位置。
- `b[11:8]`：功能。

### 注释 3：原第 48 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ENE_KB1200_PINCTRL_H_`。

## 51.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ene-kb1200-pinctrl_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P050_ene-kb106x-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P052_esp-esp32c5-intmux.h_源码浏览.md)
