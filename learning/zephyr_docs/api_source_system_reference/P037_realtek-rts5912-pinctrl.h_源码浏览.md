---
id: learning.zephyr-docs.api-source-system-reference.page-37
title: realtek-rts5912-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/realtek-rts5912-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_realtek-rts5912-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/realtek-rts5912-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md)。

## 37.1\_原始可见代码（Source Code）

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
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright (c) 2024 Realtek Semiconductor Corporation, SIBG-SD7
 * Author: Lin Yu-Cheng <lin_yu_cheng@realtek.com>
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_REALTEK_RTS5912_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_REALTEK_RTS5912_PINCTRL_H_

#include <zephyr/dt-bindings/dt-util.h>

#define REALTEK_RTS5912_GPIO_INOUT     BIT(0) /* IN/OUT : 0 input 1 output */
#define REALTEK_RTS5912_GPIO_PINON     BIT(1) /* Input_detect : 1 enable 0 disable */
#define REALTEK_RTS5912_GPIO_VOLT      BIT(2) /* Pin Volt : 1 1.8V 0 3.3V */
#define REALTEK_RTS5912_FUNC0          0      /* GPIO mode */
#define REALTEK_RTS5912_FUNC1          BIT(8) /* Function mode use BIT0~2 */
#define REALTEK_RTS5912_FUNC2          BIT(9)
#define REALTEK_RTS5912_FUNC3          ((BIT(8)) | (BIT(9)))
#define REALTEK_RTS5912_FUNC4          BIT(10)

#define REALTEK_RTS5912_INPUT_OUTPUT_POS    0
#define REALTEK_RTS5912_INPUT_DETECTION_POS 1
#define REALTEK_RTS5912_VOLTAGE_POS         2
#define REALTEK_RTS5912_DRV_STR_POS         11
#define REALTEK_RTS5912_SLEW_RATE_POS       12
#define REALTEK_RTS5912_PD_POS              13
#define REALTEK_RTS5912_PU_POS              14
#define REALTEK_RTS5912_SCHMITTER_POS       15
#define REALTEK_RTS5912_TYPE_POS            16
#define REALTEK_RTS5912_HIGH_LOW_POS        17

#define REALTEK_RTS5912_GPIO_HIGH_POS 18
#define REALTEK_RTS5912_GPIO_HIGH_MSK 0x3f
#define REALTEK_RTS5912_GPIO_LOW_POS  3
#define REALTEK_RTS5912_GPIO_LOW_MSK  0x1f

#define FUNC0 REALTEK_RTS5912_FUNC0
#define FUNC1 REALTEK_RTS5912_FUNC1
#define FUNC2 REALTEK_RTS5912_FUNC2
#define FUNC3 REALTEK_RTS5912_FUNC3
#define FUNC4 REALTEK_RTS5912_FUNC4

#define REALTEK_RTS5912_PINMUX(n, f)                                                               \
        (((((n) >> 5) & REALTEK_RTS5912_GPIO_HIGH_MSK) << REALTEK_RTS5912_GPIO_HIGH_POS) |         \
         (((n) & REALTEK_RTS5912_GPIO_LOW_MSK) << REALTEK_RTS5912_GPIO_LOW_POS) | (f))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_REALTEK_RTS5912_PINCTRL_H_ */
```

## 37.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

版权（Copyright）：© 2024 Realtek Semiconductor Corporation, SIBG-SD7。

作者（Author）：Lin Yu-Cheng <lin_yu_cheng@realtek.com>。

### 注释 2：原第 13 行

输入／输出（IN / OUT）：0 表示输入，1 表示输出。

### 注释 3：原第 14 行

输入检测（Input_detect）：1 表示启用，0 表示禁用。

### 注释 4：原第 15 行

引脚电压（Pin Volt）：1 表示 1.8 V，0 表示 3.3 V。

### 注释 5：原第 16 行

通用输入输出模式（GPIO Mode）。

### 注释 6：原第 17 行

功能模式（Function Mode）使用 `BIT0`～`BIT2`。

### 注释 7：原第 48 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_REALTEK_RTS5912_PINCTRL_H_`。

## 37.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P036_r8a7795_cpg_mssr.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P038_rv3032.h_源码浏览.md)
