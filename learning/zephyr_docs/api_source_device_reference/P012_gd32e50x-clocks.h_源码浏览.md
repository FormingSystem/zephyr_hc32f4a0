---
id: learning.zephyr-docs.api-source-device-reference.page-12
title: gd32e50x-clocks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gd32e50x-clocks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_gd32e50x-clocks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gd32e50x-clocks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P122_zephyr__dt-bindings__clock__gd32e50x-clocks.h_文件参考.md)。

## 12.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00023"></a>
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
<a id="l00098"></a>
<a id="l00099"></a>
<a id="agd32-clocks-common_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Teslabs Engineering S.L.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_GD32E50X_CLOCKS_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_GD32E50X_CLOCKS_H_

#include "gd32-clocks-common.h"


#define GD32_AHBEN_OFFSET        0x14U
#define GD32_APB1EN_OFFSET       0x1CU
#define GD32_APB2EN_OFFSET       0x18U
#define GD32_ADDAPB1EN_OFFSET    0xE4U



/* AHB peripherals */
#define GD32_CLOCK_DMA0       GD32_CLOCK_CONFIG(AHBEN, 0U)
#define GD32_CLOCK_DMA1       GD32_CLOCK_CONFIG(AHBEN, 1U)
#define GD32_CLOCK_SRAMSP     GD32_CLOCK_CONFIG(AHBEN, 2U)
#define GD32_CLOCK_FMCSP      GD32_CLOCK_CONFIG(AHBEN, 4U)
#define GD32_CLOCK_CRC        GD32_CLOCK_CONFIG(AHBEN, 6U)
#define GD32_CLOCK_EXMC       GD32_CLOCK_CONFIG(AHBEN, 8U)
#define GD32_CLOCK_USBHS      GD32_CLOCK_CONFIG(AHBEN, 12U)
#define GD32_CLOCK_ULPI       GD32_CLOCK_CONFIG(AHBEN, 13U)
#define GD32_CLOCK_ENET       GD32_CLOCK_CONFIG(AHBEN, 14U)
#define GD32_CLOCK_ENETTX     GD32_CLOCK_CONFIG(AHBEN, 15U)
#define GD32_CLOCK_ENETRX     GD32_CLOCK_CONFIG(AHBEN, 16U)
#define GD32_CLOCK_TMU        GD32_CLOCK_CONFIG(AHBEN, 30U)
#define GD32_CLOCK_SQPI       GD32_CLOCK_CONFIG(AHBEN, 31U)

/* APB1 peripherals */
#define GD32_CLOCK_TIMER1     GD32_CLOCK_CONFIG(APB1EN, 0U)
#define GD32_CLOCK_TIMER2     GD32_CLOCK_CONFIG(APB1EN, 1U)
#define GD32_CLOCK_TIMER3     GD32_CLOCK_CONFIG(APB1EN, 2U)
#define GD32_CLOCK_TIMER4     GD32_CLOCK_CONFIG(APB1EN, 3U)
#define GD32_CLOCK_TIMER5     GD32_CLOCK_CONFIG(APB1EN, 4U)
#define GD32_CLOCK_TIMER6     GD32_CLOCK_CONFIG(APB1EN, 5U)
#define GD32_CLOCK_TIMER11    GD32_CLOCK_CONFIG(APB1EN, 6U)
#define GD32_CLOCK_TIMER12    GD32_CLOCK_CONFIG(APB1EN, 7U)
#define GD32_CLOCK_TIMER13    GD32_CLOCK_CONFIG(APB1EN, 8U)
#define GD32_CLOCK_WWDGT      GD32_CLOCK_CONFIG(APB1EN, 11U)
#define GD32_CLOCK_SPI1       GD32_CLOCK_CONFIG(APB1EN, 14U)
#define GD32_CLOCK_SPI2       GD32_CLOCK_CONFIG(APB1EN, 15U)
#define GD32_CLOCK_USART1     GD32_CLOCK_CONFIG(APB1EN, 17U)
#define GD32_CLOCK_USART2     GD32_CLOCK_CONFIG(APB1EN, 18U)
#define GD32_CLOCK_UART3      GD32_CLOCK_CONFIG(APB1EN, 19U)
#define GD32_CLOCK_UART4      GD32_CLOCK_CONFIG(APB1EN, 20U)
#define GD32_CLOCK_I2C0       GD32_CLOCK_CONFIG(APB1EN, 21U)
#define GD32_CLOCK_I2C1       GD32_CLOCK_CONFIG(APB1EN, 22U)
#define GD32_CLOCK_I2C2       GD32_CLOCK_CONFIG(APB1EN, 24U)
#define GD32_CLOCK_CAN0       GD32_CLOCK_CONFIG(APB1EN, 25U)
#define GD32_CLOCK_CAN1       GD32_CLOCK_CONFIG(APB1EN, 26U)
#define GD32_CLOCK_BKPI       GD32_CLOCK_CONFIG(APB1EN, 27U)
#define GD32_CLOCK_PMU        GD32_CLOCK_CONFIG(APB1EN, 28U)
#define GD32_CLOCK_DAC        GD32_CLOCK_CONFIG(APB1EN, 29U)

/* APB2 peripherals */
#define GD32_CLOCK_AFIO       GD32_CLOCK_CONFIG(APB2EN, 0U)
#define GD32_CLOCK_GPIOA      GD32_CLOCK_CONFIG(APB2EN, 2U)
#define GD32_CLOCK_GPIOB      GD32_CLOCK_CONFIG(APB2EN, 3U)
#define GD32_CLOCK_GPIOC      GD32_CLOCK_CONFIG(APB2EN, 4U)
#define GD32_CLOCK_GPIOD      GD32_CLOCK_CONFIG(APB2EN, 5U)
#define GD32_CLOCK_GPIOE      GD32_CLOCK_CONFIG(APB2EN, 6U)
#define GD32_CLOCK_GPIOF      GD32_CLOCK_CONFIG(APB2EN, 7U)
#define GD32_CLOCK_GPIOG      GD32_CLOCK_CONFIG(APB2EN, 8U)
#define GD32_CLOCK_ADC0       GD32_CLOCK_CONFIG(APB2EN, 9U)
#define GD32_CLOCK_ADC1       GD32_CLOCK_CONFIG(APB2EN, 10U)
#define GD32_CLOCK_TIMER0     GD32_CLOCK_CONFIG(APB2EN, 11U)
#define GD32_CLOCK_SPI0       GD32_CLOCK_CONFIG(APB2EN, 12U)
#define GD32_CLOCK_TIMER7     GD32_CLOCK_CONFIG(APB2EN, 13U)
#define GD32_CLOCK_USART0     GD32_CLOCK_CONFIG(APB2EN, 14U)
#define GD32_CLOCK_ADC2       GD32_CLOCK_CONFIG(APB2EN, 15U)
#define GD32_CLOCK_TIMER8     GD32_CLOCK_CONFIG(APB2EN, 19U)
#define GD32_CLOCK_TIMER9     GD32_CLOCK_CONFIG(APB2EN, 20U)
#define GD32_CLOCK_TIMER10    GD32_CLOCK_CONFIG(APB2EN, 21U)
#define GD32_CLOCK_USART5     GD32_CLOCK_CONFIG(APB2EN, 28U)
#define GD32_CLOCK_SHRTIMER   GD32_CLOCK_CONFIG(APB2EN, 29U)
#define GD32_CLOCK_CMP        GD32_CLOCK_CONFIG(APB2EN, 31U)

/* APB1 additional peripherals */
#define GD32_CLOCK_CTC        GD32_CLOCK_CONFIG(ADDAPB1EN, 27U)
#define GD32_CLOCK_CAN2       GD32_CLOCK_CONFIG(ADDAPB1EN, 31U)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_GD32E50X_CLOCKS_H_ */
```

## 12.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Teslabs Engineering S.L.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 29 行

AHB 外设。

### 注释 3：原第 44 行

APB1 外设。

### 注释 4：原第 70 行

APB2 外设。

### 注释 5：原第 93 行

高级外设总线 1 的附加外设（APB1 Additional Peripherals）。

### 注释 6：原第 99 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_GD32E50X_CLOCKS_H_`。

## 12.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P122_zephyr__dt-bindings__clock__gd32e50x-clocks.h_文件参考.md)
- [gd32-clocks-common.h](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html)

---

[上一章](P011_gd32e10x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P013_gd32e50x.h_源码浏览.md)
