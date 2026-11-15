---
id: learning.zephyr-docs.api-source-reference.page-93
title: ch32v10x-clocks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ch32v10x-clocks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第93章\_ch32v10x-clocks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ch32v10x-clocks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ch32v10x-clocks_8h.html)。

## 93.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00014"></a>
<a id="l00016"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>

```c
/*
 * Copyright (c) 2026 Lucy Wong
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_CH32V10X_CLOCKS_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_CH32V10X_CLOCKS_H_


#define CH32V10X_AHB_PCENR_OFFSET  0
#define CH32V10X_APB2_PCENR_OFFSET 1
#define CH32V10X_APB1_PCENR_OFFSET 2

#define CH32V10X_CLOCK_CONFIG(bus, bit) (((CH32V10X_##bus##_PCENR_OFFSET) << 5) | (bit))

#define CH32V10X_CLOCK_DMA1  CH32V10X_CLOCK_CONFIG(AHB, 0)
#define CH32V10X_CLOCK_SRAM  CH32V10X_CLOCK_CONFIG(AHB, 2)
#define CH32V10X_CLOCK_FLITF CH32V10X_CLOCK_CONFIG(AHB, 4)
#define CH32V10X_CLOCK_CRC   CH32V10X_CLOCK_CONFIG(AHB, 6)
#define CH32V10X_CLOCK_FSMC  CH32V10X_CLOCK_CONFIG(AHB, 8)
#define CH32V10X_CLOCK_USBHD CH32V10X_CLOCK_CONFIG(AHB, 12)

#define CH32V10X_CLOCK_AFIO   CH32V10X_CLOCK_CONFIG(APB2, 0)
#define CH32V10X_CLOCK_IOPA   CH32V10X_CLOCK_CONFIG(APB2, 2)
#define CH32V10X_CLOCK_IOPB   CH32V10X_CLOCK_CONFIG(APB2, 3)
#define CH32V10X_CLOCK_IOPC   CH32V10X_CLOCK_CONFIG(APB2, 4)
#define CH32V10X_CLOCK_IOPD   CH32V10X_CLOCK_CONFIG(APB2, 5)
#define CH32V10X_CLOCK_ADC1   CH32V10X_CLOCK_CONFIG(APB2, 9)
#define CH32V10X_CLOCK_TIM1   CH32V10X_CLOCK_CONFIG(APB2, 11)
#define CH32V10X_CLOCK_SPI1   CH32V10X_CLOCK_CONFIG(APB2, 12)
#define CH32V10X_CLOCK_USART1 CH32V10X_CLOCK_CONFIG(APB2, 14)

#define CH32V10X_CLOCK_TIM2   CH32V10X_CLOCK_CONFIG(APB1, 0)
#define CH32V10X_CLOCK_TIM3   CH32V10X_CLOCK_CONFIG(APB1, 1)
#define CH32V10X_CLOCK_TIM4   CH32V10X_CLOCK_CONFIG(APB1, 2)
#define CH32V10X_CLOCK_WWDG   CH32V10X_CLOCK_CONFIG(APB1, 11)
#define CH32V10X_CLOCK_SPI2   CH32V10X_CLOCK_CONFIG(APB1, 14)
#define CH32V10X_CLOCK_USART2 CH32V10X_CLOCK_CONFIG(APB1, 17)
#define CH32V10X_CLOCK_USART3 CH32V10X_CLOCK_CONFIG(APB1, 18)
#define CH32V10X_CLOCK_I2C1   CH32V10X_CLOCK_CONFIG(APB1, 21)
#define CH32V10X_CLOCK_I2C2   CH32V10X_CLOCK_CONFIG(APB1, 22)
#define CH32V10X_CLOCK_USBD   CH32V10X_CLOCK_CONFIG(APB1, 23)
#define CH32V10X_CLOCK_CAN1   CH32V10X_CLOCK_CONFIG(APB1, 25)
#define CH32V10X_CLOCK_BKP    CH32V10X_CLOCK_CONFIG(APB1, 27)
#define CH32V10X_CLOCK_PWR    CH32V10X_CLOCK_CONFIG(APB1, 28)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_CH32V10X_CLOCKS_H_ */
```

## 93.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Lucy Wong。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 86 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_CH32V10X_CLOCKS_H_`。

## 93.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ch32v10x-clocks_8h.html)

---

[上一章](P092_ch32v00x-clocks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P094_ch32v20x_30x-clocks.h_源码浏览.md)
