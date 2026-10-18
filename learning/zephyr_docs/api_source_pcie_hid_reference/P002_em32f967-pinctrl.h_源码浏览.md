---
id: learning.zephyr-docs.api-source-pcie-hid-reference.page-2
title: em32f967-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/em32f967-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_em32f967-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/em32f967-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/em32f967-pinctrl_8h.html)。

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00053"></a>
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
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00143"></a>
<a id="l00151"></a>
<a id="l00160"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>

```c
/*
 * SPDX-FileCopyrightText: 2024 ELAN Microelectronics Corp.
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_EM32F967_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_EM32F967_PINCTRL_H_

/*
 * EM32F967 Pin Control Definitions (EM32-style)
 */

/* Pin multiplexing values for EM32F967 - based on CSV specification */
#define EM32F967_GPIO 0 /* 000: GPIO function */
#define EM32F967_AF1  1 /* 001: Alternate function 1 (SPI1, etc.) */
#define EM32F967_AF2  2 /* 010: Alternate function 2 (UART, etc.) */
#define EM32F967_AF3  3 /* 011: Alternate function 3 (Timer, 7816, etc.) */
#define EM32F967_AF4  4 /* 100: Alternate function 4 (I2C, etc.) */
#define EM32F967_AF5  5 /* 101: Alternate function 5 (I2C, WKUP, etc.) */
#define EM32F967_AF6  6 /* 110: Alternate function 6 (SSP2, etc.) */
#define EM32F967_AF7  7 /* 111: Alternate function 7 (PWM, etc.) */

#define EM32F967_MUX_SHIFT  0U
#define EM32F967_MUX_MASK   0x7U
#define EM32F967_PIN_SHIFT  3U
#define EM32F967_PIN_MASK   0xFU
#define EM32F967_PORT_SHIFT 7U
#define EM32F967_PORT_MASK  0x1U

#define EM32F967_PINMUX(port, pin, mux)                                                            \
        (((((port) - 'A') & EM32F967_PORT_MASK) << EM32F967_PORT_SHIFT) |                          \
         (((pin) & EM32F967_PIN_MASK) << EM32F967_PIN_SHIFT) |                                     \
         (((EM32F967_##mux) & EM32F967_MUX_MASK) << EM32F967_MUX_SHIFT))

/* Helper macros to extract fields from encoded pinmux value */
#define EM32F967_DT_PINMUX_PORT(pinmux) (((pinmux) >> EM32F967_PORT_SHIFT) & EM32F967_PORT_MASK)

#define EM32F967_DT_PINMUX_PIN(pinmux) (((pinmux) >> EM32F967_PIN_SHIFT) & EM32F967_PIN_MASK)

#define EM32F967_DT_PINMUX_MUX(pinmux) (((pinmux) >> EM32F967_MUX_SHIFT) & EM32F967_MUX_MASK)

/* Pull-up/Pull-down definitions for 5V tolerant pins (PA0-PA6) */
#define EM32F967_PULL_NONE_5V 0 /* 00: Floating */
#define EM32F967_PULL_UP0_5V  1 /* 01: PU0 (66KΩ@5V, 101KΩ@3.3V, 238KΩ@1.8V) */
#define EM32F967_PULL_UP1_5V  2 /* 10: PU1 (4.7KΩ@5V, 6.41KΩ@3.3V, 12.7KΩ@1.8V) */
#define EM32F967_PULL_DOWN_5V 3 /* 11: PD (15KΩ@5V, 21.8KΩ@3.3V, 49.6KΩ@1.8V) */

/* Pull-up/Pull-down definitions for 3V pins (PA11-PA15, PB0-PB15) */
#define EM32F967_PULL_NONE_3V 0 /* 00: Floating */
#define EM32F967_PULL_UP0_3V  1 /* 01: PU0 (66KΩ@3.3V, 140KΩ@1.8V) */
#define EM32F967_PULL_UP1_3V  2 /* 10: PU1 (4.7KΩ@3.3V, 8.53KΩ@1.8V) */
#define EM32F967_PULL_DOWN_3V 3 /* 11: PD (15KΩ@3.3V, 25.2KΩ@1.8V) */

/* Drive strength definitions */
#define EM32F967_DRIVE_NORMAL 0 /* Normal drive strength */
#define EM32F967_DRIVE_HIGH   1 /* High drive strength (Load=30pF) */

#define EM32F967_IO_NONE 0U

/* Explicit op builders (shift = bit position, width = field width in bits) */
#define EM32F967_IO1(shift, width, val)                                                            \
        ((1U << 8) | (((shift) & 0x1FU) << 9) | ((((width) - 1U) & 0x3U) << 14) |                  \
         (((val) & 0xFU) << 16))

#define EM32F967_IO2(shift, width, val)                                                            \
        ((1U << 20) | (((shift) & 0x1FU) << 21) | ((((width) - 1U) & 0x3U) << 26) |                \
         (((val) & 0xFU) << 28))

/* Convenience helpers for slot 1 (combine with EM32F967_IO2() via bitwise OR) */
#define EM32F967_IO_SET_BIT(pos)       EM32F967_IO1((pos), 1U, 1U)
#define EM32F967_IO_CLR_BIT(pos)       EM32F967_IO1((pos), 1U, 0U)
#define EM32F967_IO_SET_2BIT(pos, val) EM32F967_IO1((pos), 2U, (val))
#define EM32F967_IO_CLR_2BIT(pos)      EM32F967_IO1((pos), 2U, 0U)

#define EM32F967_PINMUX_IO(port, pin, mux, ioshare) (EM32F967_PINMUX(port, pin, mux) | (ioshare))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_EM32F967_PINCTRL_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：2024 ELAN Microelectronics Corp.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 9 行

EM32F967 引脚控制定义（Pin Control Definitions），采用 EM32 风格。

### 注释 3：原第 13 行

EM32F967 引脚复用值（Pin Multiplexing Values），依据 CSV 规格定义。

### 注释 4：原第 20 行

`000`：通用输入输出（GPIO）功能。

### 注释 5：原第 21 行

`001`：复用功能 1（Alternate Function 1），例如 SPI1。

### 注释 6：原第 22 行

`010`：复用功能 2（Alternate Function 2），例如 UART。

### 注释 7：原第 23 行

`011`：复用功能 3（Alternate Function 3），例如定时器、7816。

### 注释 8：原第 24 行

`100`：复用功能 4（Alternate Function 4），例如 I2C。

### 注释 9：原第 25 行

`101`：复用功能 5（Alternate Function 5），例如 I2C、WKUP。

### 注释 10：原第 26 行

`110`：复用功能 6（Alternate Function 6），例如 SSP2。

### 注释 11：原第 27 行

`111`：复用功能 7（Alternate Function 7），例如 PWM。

### 注释 12：原第 58 行

从编码后的引脚复用值（Pinmux Value）中提取字段的辅助宏。

### 注释 13：原第 65 行

耐受 5 V 的引脚（PA0–PA6）的上拉／下拉（Pull-up/Pull-down）定义。

### 注释 14：原第 66 行

`00`：浮空（Floating）。

### 注释 15：原第 67 行

`01`：上拉 PU0，5 V 时为 66 kΩ，3.3 V 时为 101 kΩ，1.8 V 时为 238 kΩ。

### 注释 16：原第 68 行

`10`：上拉 PU1，5 V 时为 4.7 kΩ，3.3 V 时为 6.41 kΩ，1.8 V 时为 12.7 kΩ。

### 注释 17：原第 69 行

`11`：下拉 PD，5 V 时为 15 kΩ，3.3 V 时为 21.8 kΩ，1.8 V 时为 49.6 kΩ。

### 注释 18：原第 71 行

3 V 引脚（PA11–PA15、PB0–PB15）的上拉／下拉（Pull-up/Pull-down）定义。

### 注释 19：原第 72 行

`00`：浮空（Floating）。

### 注释 20：原第 73 行

`01`：上拉 PU0，3.3 V 时为 66 kΩ，1.8 V 时为 140 kΩ。

### 注释 21：原第 74 行

`10`：上拉 PU1，3.3 V 时为 4.7 kΩ，1.8 V 时为 8.53 kΩ。

### 注释 22：原第 75 行

`11`：下拉 PD，3.3 V 时为 15 kΩ，1.8 V 时为 25.2 kΩ。

### 注释 23：原第 77 行

驱动能力定义（Drive Strength Definitions）。

### 注释 24：原第 78 行

正常驱动能力（Normal Drive Strength）。

### 注释 25：原第 79 行

高驱动能力（High Drive Strength），负载为 30 pF。

### 注释 26：原第 103 行

显式操作构造器（Explicit Op Builders），`shift` 为位位置，`width` 为字段位宽。

### 注释 27：原第 135 行

槽 1（Slot 1）的便捷辅助宏，通过按位或（Bitwise OR）与 `EM32F967_IO2()` 组合。

### 注释 28：原第 181 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_EM32F967_PINCTRL_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/em32f967-pinctrl_8h.html)

---

[上一章](P001_pcie.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_esp32c5-gpio-sigmap.h_源码浏览.md)
