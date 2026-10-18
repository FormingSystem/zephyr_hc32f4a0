---
id: learning.zephyr-docs.api-source-configuration-reference.page-3
title: amebad-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/amebad-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_amebad-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/amebad-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/amebad-pinctrl_8h.html)。

## 3.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2024 Realtek Semiconductor Corp.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMEBAD_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMEBAD_PINCTRL_H_

/* PINMUX Function definitions */
#define AMEBA_GPIO        0
#define AMEBA_UART        1
#define AMEBA_UART_RTSCTS 2
#define AMEBA_LOGUART     2
#define AMEBA_SPIM        3
#define AMEBA_SPIS        3
#define AMEBA_RTC         4
#define AMEBA_TIMINPUT    4
#define AMEBA_IR          5
#define AMEBA_SPIF        6
#define AMEBA_I2C         7
#define AMEBA_SDIOD       8
#define AMEBA_SDIOH       8
#define AMEBA_PWM         9
#define AMEBA_PWM_HS      9
#define AMEBA_PWM_LP      10
#define AMEBA_SWD         11
#define AMEBA_I2S         12
#define AMEBA_DMIC        12
#define AMEBA_LCD         13
#define AMEBA_USB         14
#define AMEBA_QDEC        15
#define AMEBA_SGPIO       16
#define AMEBA_RFE         18
#define AMEBA_BTCOEX      19
#define AMEBA_WIFIFW      20
#define AMEBA_EXT_PCM     20
#define AMEBA_EXT_BT      20
#define AMEBA_BB_PIN      21
#define AMEBA_SIC         22
#define AMEBA_TIMINPUT_HS 22
#define AMEBA_DBGPORT     23
#define AMEBA_BBDBG       25
#define AMEBA_EXT32K      28
#define AMEBA_RTCOUT      28
#define AMEBA_KEYSCAN_ROW 29
#define AMEBA_KEYSCAN_COL 30
#define AMEBA_WAKEUP      31

/* Define pins number: bit[14:13] port, bit[12:8] pin, bit[7:0] function ID */
#define AMEBA_PORT_PIN(port, line)       ((((port) - 'A') << 5) + (line))
#define AMEBA_PINMUX(port, line, funcid) (((AMEBA_PORT_PIN(port, line)) << 8) | (funcid))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMEBAD_PINCTRL_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Realtek Semiconductor Corp.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

引脚复用功能定义（PINMUX Function definitions）。

### 注释 3：原第 50 行

引脚编号定义：`bit[14:13]` 为端口，`bit[12:8]` 为引脚，`bit[7:0]` 为功能标识符（Function ID）。

### 注释 4：原第 54 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMEBAD_PINCTRL_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/amebad-pinctrl_8h.html)

---

[上一章](P002_adp5585.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_amebadplus-pinctrl.h_源码浏览.md)
