---
id: learning.zephyr-docs.api-source-reference.page-734
title: rtl8752h-clocks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-clocks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第734章\_rtl8752h-clocks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-clocks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-clocks_8h.html)。

## 734.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
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
<a id="l00059"></a>
<a id="l00060"></a>

```c
/*
 * Copyright (c) 2026, Realtek Semiconductor Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RTL8752H_CLOCKS_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RTL8752H_CLOCKS_H_


#define APB_CLK(peri) APB_PERIPH_##peri##_CLOCK


#define APB_PERIPH_I2S0_CLOCK     0U
#define APB_PERIPH_I2S1_CLOCK     1U
#define APB_PERIPH_CODEC_CLOCK    2U
#define APB_PERIPH_GPIO_CLOCK     3U
#define APB_PERIPH_GDMA_CLOCK     4U
#define APB_PERIPH_TIMER_CLOCK    5U
#define APB_PERIPH_ENHTIMER_CLOCK 6U
#define APB_PERIPH_UART2_CLOCK    7U
#define APB_PERIPH_UART0_CLOCK    8U
#define APB_PERIPH_FLASH_CLOCK    9U
#define APB_PERIPH_PKE_CLOCK      10U
#define APB_PERIPH_SHA256_CLOCK   11U
#define APB_PERIPH_FLASH1_CLOCK   12U
#define APB_PERIPH_FLH_SEC_CLOCK  13U
#define APB_PERIPH_IR_CLOCK       14U
#define APB_PERIPH_SPI1_CLOCK     15U
#define APB_PERIPH_SPI0_CLOCK     16U
#define APB_PERIPH_UART1_CLOCK    17U
#define APB_PERIPH_IF8080_CLOCK   18U
#define APB_PERIPH_ADC_CLOCK      19U
#define APB_PERIPH_SPI2W_CLOCK    20U
#define APB_PERIPH_MODEM_CLOCK    21U
#define APB_PERIPH_BLUEWIZ_CLOCK  22U
#define APB_PERIPH_ZIGBEE_CLOCK   23U
#define APB_PERIPH_KEYSCAN_CLOCK  24U
#define APB_PERIPH_QDEC_CLOCK     25U
#define APB_PERIPH_I2C1_CLOCK     26U
#define APB_PERIPH_I2C0_CLOCK     27U


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RTL8752H_CLOCKS_H_ */
```

## 734.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026, Realtek Semiconductor Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 60 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RTL8752H_CLOCKS_H_`。

## 734.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-clocks_8h.html)

---

[上一章](P733_rtk.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P735_rtl87x2g-clocks.h_源码浏览.md)
