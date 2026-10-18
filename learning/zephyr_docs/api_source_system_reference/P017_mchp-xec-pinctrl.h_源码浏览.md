---
id: learning.zephyr-docs.api-source-system-reference.page-17
title: mchp-xec-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_mchp-xec-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P211_zephyr__dt-bindings__pinctrl__mchp-xec-pinctrl.h_文件参考.md)。

## 17.1\_原始可见代码（Source Code）

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
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2021 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MCHP_XEC_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MCHP_XEC_PINCTRL_H_

#include <zephyr/dt-bindings/dt-util.h>

#define MCHP_GPIO       0x0
#define MCHP_AF0        0x0
#define MCHP_AF1        0x1
#define MCHP_AF2        0x2
#define MCHP_AF3        0x3
#define MCHP_AF4        0x4
#define MCHP_AF5        0x5
#define MCHP_AF6        0x6
#define MCHP_AF7        0x7
#define MCHP_AFMAX      0x8

#define MCHP_XEC_SLEW_RATE_NO_CHANGE    0
#define MCHP_XEC_SLEW_RATE_FAST         1
#define MCHP_XEC_SLEW_RATE_SLOW         2

#define MCHP_XEC_DRV_STR_NO_CHANGE      0
#define MCHP_XEC_DRV_STR_1X             1 /* 2 or 4(PIO-24) mA */
#define MCHP_XEC_DRV_STR_2X             2 /* 4 or 8(PIO-24) mA */
#define MCHP_XEC_DRV_STR_4X             3 /* 8 or 16(PIO-24) mA */
#define MCHP_XEC_DRV_STR_6X             4 /* 12 or 24(PIO-24) mA */

#define MCHP_XEC_PINMUX_PORT_POS        0
#define MCHP_XEC_PINMUX_PORT_MSK        0xf
#define MCHP_XEC_PINMUX_PIN_POS         4
#define MCHP_XEC_PINMUX_PIN_MSK         0x1f
#define MCHP_XEC_PINMUX_FUNC_POS        9
#define MCHP_XEC_PINMUX_FUNC_MSK        0x7

/* n is octal pin number or equivalent in another base.
 * MCHP XEC documentation specifies pin numbers in octal.
 * f is function number
 * b[3:0] = pin bank
 * b[8:4] = pin position in bank
 * b[11:9] = function
 */
#define MCHP_XEC_PINMUX(n, f)                                                     \
        (((((n) >> 5) & MCHP_XEC_PINMUX_PORT_MSK) << MCHP_XEC_PINMUX_PORT_POS)  | \
         (((n) & MCHP_XEC_PINMUX_PIN_MSK) << MCHP_XEC_PINMUX_PIN_POS)           | \
         (((f) & MCHP_XEC_PINMUX_FUNC_MSK) << MCHP_XEC_PINMUX_FUNC_POS))


#define MCHP_XEC_PINMUX_PORT(p)                                         \
        (((p) >> MCHP_XEC_PINMUX_PORT_POS) & MCHP_XEC_PINMUX_PORT_MSK)

#define MCHP_XEC_PINMUX_PIN(p)                                          \
        (((p) >> MCHP_XEC_PINMUX_PIN_POS) & MCHP_XEC_PINMUX_PIN_MSK)

#define MCHP_XEC_PINMUX_FUNC(p)                                         \
        (((p) >> MCHP_XEC_PINMUX_FUNC_POS) & MCHP_XEC_PINMUX_FUNC_MSK)

#define MEC_XEC_PINMUX_PORT_PIN(p)                                      \
        ((p) & ((MCHP_XEC_PINMUX_PORT_MSK << MCHP_XEC_PINMUX_PORT_POS) | \
                (MCHP_XEC_PINMUX_PIN_MSK << MCHP_XEC_PINMUX_PIN_POS)))

#endif  /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MCHP_XEC_PINCTRL_H_ */
```

## 17.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 28 行

2 mA，或在 PIO-24 情况下为 4 mA。

### 注释 3：原第 29 行

4 mA，或在 PIO-24 情况下为 8 mA。

### 注释 4：原第 30 行

8 mA，或在 PIO-24 情况下为 16 mA。

### 注释 5：原第 31 行

12 mA，或在 PIO-24 情况下为 24 mA。

### 注释 6：原第 40 行

`n` 是八进制引脚编号（Octal Pin Number），也可使用其他进制表示的等价值。MCHP XEC 文档采用八进制引脚编号。`f` 是功能编号（Function Number）。

- `b[3:0]`：引脚组（Pin Bank）。
- `b[8:4]`：引脚在组内的位置（Pin Position in Bank）。
- `b[11:9]`：功能（Function）。

### 注释 7：原第 66 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MCHP_XEC_PINCTRL_H_`。

## 17.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P211_zephyr__dt-bindings__pinctrl__mchp-xec-pinctrl.h_文件参考.md)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P016_l2cap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P018_smp.h_源码浏览.md)
