---
id: learning.zephyr-docs.api-source-system-reference.page-45
title: stm32mp2_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32mp2__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_stm32mp2\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32mp2__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P454_zephyr__dt-bindings__reset__stm32mp2_reset.h_文件参考.md)。

## 45.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00017"></a>
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
<a id="l00058"></a>
<a id="l00059"></a>

```c
/*
 * Copyright (C) 2025 Savoir-faire Linux, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_STM32MP2_RESET_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_STM32MP2_RESET_H_


#define STM32_RESET(per, bit) (((STM32_RESET_PERIPH_##per##) << 5U) | (bit))

/* Reset reg */
#define STM32_RST       0U

/* Timer Peripheral */
#define STM32_RESET_PERIPH_TIM12        0x728

/* USART/UART Peripheral */
#define STM32_RESET_PERIPH_USART1       0x77C
#define STM32_RESET_PERIPH_USART2       0x780
#define STM32_RESET_PERIPH_USART3       0x784
#define STM32_RESET_PERIPH_UART4        0x788
#define STM32_RESET_PERIPH_UART5        0x78C
#define STM32_RESET_PERIPH_USART6       0x790
#define STM32_RESET_PERIPH_UART7        0x794
#define STM32_RESET_PERIPH_UART8        0x798
#define STM32_RESET_PERIPH_UART9        0x79C

/* Camera peripherals */
#define STM32_RESET_PERIPH_CSI2         0x858
#define STM32_RESET_PERIPH_DCMIPP       0x85C

/* I3C Peripheral */
#define STM32_RESET_PERIPH_I3C1         0x8C8
#define STM32_RESET_PERIPH_I3C2         0x8CC
#define STM32_RESET_PERIPH_I3C3         0x8D0
#define STM32_RESET_PERIPH_I3C4         0x8D4


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESET_STM32MP2_RESET_H_ */
```

## 45.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：(C) 2025 Savoir-faire Linux, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 30 行

复位寄存器（Reset Register）。

### 注释 3：原第 33 行

定时器外设（Timer Peripheral）。

### 注释 4：原第 36 行

USART／UART 外设（Peripheral）。

### 注释 5：原第 47 行

摄像头外设（Camera Peripherals）。

### 注释 6：原第 51 行

I3C 外设（Peripheral）。

### 注释 7：原第 59 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESET_STM32MP2_RESET_H_`。

## 45.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P454_zephyr__dt-bindings__reset__stm32mp2_reset.h_文件参考.md)

---

[上一章](P044_stm32f4_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P046_stm32n6_clock.h_源码浏览.md)
