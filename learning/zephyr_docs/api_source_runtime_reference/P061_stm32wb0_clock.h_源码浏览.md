---
id: learning.zephyr-docs.api-source-runtime-reference.page-61
title: stm32wb0_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32wb0__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_stm32wb0\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32wb0__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32wb0__clock_8h.html)。

## 61.1\_原始可见代码（Source Code）

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
<a id="l00012"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="astm32__common__clocks_8h_html"></a>

```c
/*
 * Copyright (c) 2024 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WB0_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WB0_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32_common_clocks.h>


#define STM32_SRC_CLKSLOWMUX            (STM32_SRC_LSI + 1)
#define STM32_SRC_CLK16MHZ              (STM32_SRC_CLKSLOWMUX + 1)
#define STM32_SRC_CLK32MHZ              (STM32_SRC_CLK16MHZ + 1)

#define STM32_CLOCK_BUS_AHB0    0x50
#define STM32_CLOCK_BUS_APB0    0x54
#define STM32_CLOCK_BUS_APB1    0x58
#define STM32_CLOCK_BUS_APB2    0x60

#define STM32_PERIPH_BUS_MIN    STM32_CLOCK_BUS_AHB0
#define STM32_PERIPH_BUS_MAX    STM32_CLOCK_BUS_APB2

#define CFGR_REG        0x08

#define APB2ENR_REG     0x60


/* WB05/WB09 only */
#define LPUART1_SEL(val)        STM32_DT_CLOCK_SELECT((val), 13, 13, CFGR_REG)
/* WB06/WB07 only */
#define SPI2_I2S2_SEL(val)      STM32_DT_CLOCK_SELECT((val), 22, 22, CFGR_REG)
/* `msb` is only 22 for WB06/WB07, but a single definition with msb=23 is acceptable */
#define SPI3_I2S3_SEL(val)      STM32_DT_CLOCK_SELECT((val), 23, 22, CFGR_REG)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WB0_CLOCK_H_ */
```

## 61.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 39 行

仅适用于 WB05/WB09。

### 注释 3：原第 41 行

仅适用于 WB06/WB07。

### 注释 4：原第 43 行

对 WB06/WB07，`msb` 仅为 22；但统一使用 `msb=23` 的单一定义也是可接受的。

### 注释 5：原第 48 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32WB0_CLOCK_H_`。

## 61.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32wb0__clock_8h.html)
- [zephyr/dt-bindings/clock/stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)
- [stm32_common_clocks.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)

---

[上一章](P060_stm32u5_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P062_symtab.h_源码浏览.md)
