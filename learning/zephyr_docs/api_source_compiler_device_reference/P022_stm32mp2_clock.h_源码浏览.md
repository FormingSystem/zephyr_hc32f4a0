---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-22
title: stm32mp2_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32mp2__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_stm32mp2\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32mp2__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P453_zephyr__dt-bindings__clock__stm32mp2_clock.h_文件参考.md)。

## 22.1\_原始可见代码（Source Code）

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
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
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
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (C) 2025 Savoir-faire Linux, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32MP2_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32MP2_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>


/* Undefine the common clocks macro */
#undef STM32_CLOCK

#define STM32_CLOCK(per, bit) (STM32_CLOCK_PERIPH_##per) (1 << bit)

/* Clock reg */
#define STM32_CLK               1U
#define STM32_LP_CLK            2U

/* GPIO Peripheral */
#define STM32_CLOCK_PERIPH_GPIOA        0x52C
#define STM32_CLOCK_PERIPH_GPIOB        0x530
#define STM32_CLOCK_PERIPH_GPIOC        0x534
#define STM32_CLOCK_PERIPH_GPIOD        0x538
#define STM32_CLOCK_PERIPH_GPIOE        0x53C
#define STM32_CLOCK_PERIPH_GPIOF        0x540
#define STM32_CLOCK_PERIPH_GPIOG        0x544
#define STM32_CLOCK_PERIPH_GPIOH        0x548
#define STM32_CLOCK_PERIPH_GPIOI        0x54C
#define STM32_CLOCK_PERIPH_GPIOJ        0x550
#define STM32_CLOCK_PERIPH_GPIOK        0x554
#define STM32_CLOCK_PERIPH_GPIOZ        0x558

/* Timer Peripheral */
#define STM32_CLOCK_PERIPH_TIM12        0x728

/* SPI Peripheral */
#define STM32_CLOCK_PERIPH_SPI1         0x758
#define STM32_CLOCK_PERIPH_SPI2         0x75C
#define STM32_CLOCK_PERIPH_SPI3         0x760
#define STM32_CLOCK_PERIPH_SPI4         0x764
#define STM32_CLOCK_PERIPH_SPI5         0x768
#define STM32_CLOCK_PERIPH_SPI6         0x76C
#define STM32_CLOCK_PERIPH_SPI7         0x770
#define STM32_CLOCK_PERIPH_SPI8         0x774

/* USART/UART Peripheral */
#define STM32_CLOCK_PERIPH_USART1       0x77C
#define STM32_CLOCK_PERIPH_USART2       0x780
#define STM32_CLOCK_PERIPH_USART3       0x784
#define STM32_CLOCK_PERIPH_UART4        0x788
#define STM32_CLOCK_PERIPH_UART5        0x78C
#define STM32_CLOCK_PERIPH_USART6       0x790
#define STM32_CLOCK_PERIPH_UART7        0x794
#define STM32_CLOCK_PERIPH_UART8        0x798
#define STM32_CLOCK_PERIPH_UART9        0x79C

/* I2C Peripheral */
#define STM32_CLOCK_PERIPH_I2C1         0x7A0
#define STM32_CLOCK_PERIPH_I2C2         0x7A8
#define STM32_CLOCK_PERIPH_I2C3         0x7AC
#define STM32_CLOCK_PERIPH_I2C4         0x7B0
#define STM32_CLOCK_PERIPH_I2C5         0x7B4
#define STM32_CLOCK_PERIPH_I2C6         0x7B8
#define STM32_CLOCK_PERIPH_I2C7         0x7BC
#define STM32_CLOCK_PERIPH_I2C8         0x7C0

/* FDCAN Peripheral */
#define STM32_CLOCK_PERIPH_FDCAN        0x7E0

/* Watchdog Peripheral */
#define STM32_CLOCK_PERIPH_IWDG4        0x894
#define STM32_CLOCK_PERIPH_WWDG1        0x89C

/* Camera peripherals */
#define STM32_CLOCK_PERIPH_CSI2         0x858
#define STM32_CLOCK_PERIPH_DCMIPP       0x85C

/* CRC peripheral */
#define STM32_CLOCK_PERIPH_CRC          0x8B4

/* I3C Peripheral */
#define STM32_CLOCK_PERIPH_I3C1         0x8C8
#define STM32_CLOCK_PERIPH_I3C2         0x8CC
#define STM32_CLOCK_PERIPH_I3C3         0x8D0
#define STM32_CLOCK_PERIPH_I3C4         0x8D4

#define STM32_CLOCK_PERIPH_MIN  STM32_CLOCK_PERIPH_GPIOA
#define STM32_CLOCK_PERIPH_MAX  STM32_CLOCK_PERIPH_I3C4


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32MP2_CLOCK_H_ */
```

## 22.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：(C) 2025 Savoir-faire Linux, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 14 行

取消定义公共时钟宏（common clocks macro）。

### 注释 3：原第 26 行

时钟寄存器（clock register）。

### 注释 4：原第 30 行

GPIO 外设（peripheral）。

### 注释 5：原第 44 行

定时器外设（Timer Peripheral）。

### 注释 6：原第 47 行

SPI 外设（peripheral）。

### 注释 7：原第 57 行

USART／UART 外设（Peripheral）。

### 注释 8：原第 68 行

I2C 外设（peripheral）。

### 注释 9：原第 78 行

FDCAN 外设（peripheral）。

### 注释 10：原第 81 行

看门狗外设（watchdog peripheral）。

### 注释 11：原第 85 行

摄像头外设（Camera Peripherals）。

### 注释 12：原第 89 行

CRC 外设（peripheral）。

### 注释 13：原第 92 行

I3C 外设（Peripheral）。

### 注释 14：原第 103 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32MP2_CLOCK_H_`。

## 22.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P453_zephyr__dt-bindings__clock__stm32mp2_clock.h_文件参考.md)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P021_stm32-fmc-sdram.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P023_toolchain.h_源码浏览.md)
