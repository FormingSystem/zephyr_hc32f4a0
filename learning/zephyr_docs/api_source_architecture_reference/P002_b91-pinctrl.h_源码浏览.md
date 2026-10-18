---
id: learning.zephyr-docs.api-source-architecture-reference.page-2
title: b91-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/b91-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_b91-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/b91-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P024_zephyr__dt-bindings__pinctrl__b91-pinctrl.h_文件参考.md)。

## 2.1\_原始可见代码（Source Code）

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
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>

```c
/*
 * Copyright (c) 2021 Telink Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_B91_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_B91_PINCTRL_H_

/* IDs for GPIO functions */

#define B91_FUNC_A       0x00
#define B91_FUNC_B       0x01
#define B91_FUNC_C       0x02

/* IDs for GPIO Ports  */

#define B91_PORT_A       0x00
#define B91_PORT_B       0x01
#define B91_PORT_C       0x02
#define B91_PORT_D       0x03
#define B91_PORT_E       0x04

/* IDs for GPIO Pins */

#define B91_PIN_0        0x01
#define B91_PIN_1        0x02
#define B91_PIN_2        0x04
#define B91_PIN_3        0x08
#define B91_PIN_4        0x10
#define B91_PIN_5        0x20
#define B91_PIN_6        0x40
#define B91_PIN_7        0x80

/* B91 pinctrl pull-up/down */

#define B91_PULL_NONE    0
#define B91_PULL_DOWN    2
#define B91_PULL_UP      3

/* Pin function positions */

#define B91_PIN_0_FUNC_POS    0x00
#define B91_PIN_1_FUNC_POS    0x02
#define B91_PIN_2_FUNC_POS    0x04
#define B91_PIN_3_FUNC_POS    0x06
#define B91_PIN_4_FUNC_POS    0x00
#define B91_PIN_5_FUNC_POS    0x02
#define B91_PIN_6_FUNC_POS    0x04
#define B91_PIN_7_FUNC_POS    0x06

/* B91 pin configuration bit field positions and masks */

#define B91_PULL_POS     19
#define B91_PULL_MSK     0x3
#define B91_FUNC_POS     16
#define B91_FUNC_MSK     0x3
#define B91_PORT_POS     8
#define B91_PORT_MSK     0xFF
#define B91_PIN_POS      0
#define B91_PIN_MSK      0xFFFF
#define B91_PIN_ID_MSK   0xFF

/* Setters and getters */

#define B91_PINMUX_SET(port, pin, func)   ((func << B91_FUNC_POS) | \
                                           (port << B91_PORT_POS) | \
                                           (pin << B91_PIN_POS))
#define B91_PINMUX_GET_PULL(pinmux)       ((pinmux >> B91_PULL_POS) & B91_PULL_MSK)
#define B91_PINMUX_GET_FUNC(pinmux)       ((pinmux >> B91_FUNC_POS) & B91_FUNC_MSK)
#define B91_PINMUX_GET_PIN(pinmux)        ((pinmux >> B91_PIN_POS) & B91_PIN_MSK)
#define B91_PINMUX_GET_PIN_ID(pinmux)     ((pinmux >> B91_PIN_POS) & B91_PIN_ID_MSK)

#endif  /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_B91_PINCTRL_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Telink Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

GPIO 功能标识（Function IDs）。

### 注释 3：原第 16 行

GPIO 端口标识（Port IDs）。

### 注释 4：原第 24 行

GPIO 引脚标识（Pin IDs）。

### 注释 5：原第 35 行

B91 引脚控制上拉／下拉（Pinctrl Pull-Up / Pull-Down）。

### 注释 6：原第 41 行

引脚功能位位置（Pin Function Positions）。

### 注释 7：原第 52 行

B91 引脚配置位域的位置与掩码（Bit Field Positions and Masks）。

### 注释 8：原第 64 行

设置与获取函数（Setters and getters）。

### 注释 9：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_B91_PINCTRL_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P024_zephyr__dt-bindings__pinctrl__b91-pinctrl.h_文件参考.md)

---

[上一章](P001_a2dp_codec_sbc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_blob_cli.h_源码浏览.md)
