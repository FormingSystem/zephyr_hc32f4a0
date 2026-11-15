---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-7
title: esp32c2_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32c2__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_esp32c2\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp32c2__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp32c2__clock_8h.html)。

## 7.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2024 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ESP32C2_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ESP32C2_CLOCK_H_

/* Supported CPU clock Sources */
#define ESP32_CPU_CLK_SRC_XTAL 0U
#define ESP32_CPU_CLK_SRC_PLL  1U
#define ESP32_CLK_SRC_RC_FAST  2U

/* Supported CPU frequencies */
#define ESP32_CLK_CPU_PLL_40M      40000000
#define ESP32_CLK_CPU_PLL_60M      60000000
#define ESP32_CLK_CPU_PLL_80M      80000000
#define ESP32_CLK_CPU_PLL_120M    120000000
#define ESP32_CLK_CPU_RC_FAST_FREQ  8750000

/* Supported XTAL frequencies */
#define ESP32_CLK_XTAL_26M 26000000
#define ESP32_CLK_XTAL_32M 32000000
#define ESP32_CLK_XTAL_40M 40000000

/* Supported RTC fast clock sources */
#define ESP32_RTC_FAST_CLK_SRC_XTAL_D2 0
#define ESP32_RTC_FAST_CLK_SRC_RC_FAST 1

/* Supported RTC slow clock sources */
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW      0
#define ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW     1
#define ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256 2

/* RTC slow clock frequencies */
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ      136000
#define ESP32_RTC_SLOW_CLK_SRC_OSC_SLOW_FREQ      32768
#define ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256_FREQ  68359

/* Modules IDs
 * These are used by the clock control driver to identify peripheral modules.
 */
#define ESP32_TIMG0_MODULE           0
#define ESP32_UHCI0_MODULE           1
#define ESP32_RNG_MODULE             2
#define ESP32_WIFI_MODULE            3
#define ESP32_BT_MODULE              4
#define ESP32_WIFI_BT_COMMON_MODULE  5
#define ESP32_SYSTIMER_MODULE        6
#define ESP32_PHY_CALIBRATION_MODULE 7
#define ESP32_COEX_MODULE            8
#define ESP32_MODULE_MAX             9

/* Non-shared peripherals - these have dedicated clock control in their drivers
 * and don't use periph_module_enable(). Values start after MODULE_MAX.
 */
#define ESP32_LEDC_MODULE        100
#define ESP32_UART0_MODULE       101
#define ESP32_UART1_MODULE       102
#define ESP32_I2C0_MODULE        103
#define ESP32_TIMG1_MODULE       104
#define ESP32_SPI_MODULE         105
#define ESP32_SPI2_MODULE        106
#define ESP32_BT_BASEBAND_MODULE 107
#define ESP32_BT_LC_MODULE       108
#define ESP32_AES_MODULE         109
#define ESP32_SHA_MODULE         110
#define ESP32_ECC_MODULE         111
#define ESP32_GDMA_MODULE        112
#define ESP32_SARADC_MODULE      113
#define ESP32_TEMPSENSOR_MODULE  114
#define ESP32_MODEM_RPA_MODULE   115

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ESP32C2_CLOCK_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

支持的 CPU 时钟源（clock sources）。

### 注释 3：原第 15 行

支持的 CPU 频率。

### 注释 4：原第 22 行

支持的晶体（XTAL）频率。

### 注释 5：原第 27 行

支持的 RTC 快速时钟源。

### 注释 6：原第 31 行

支持的 RTC 慢速时钟源。

### 注释 7：原第 36 行

RTC 慢速时钟频率。

### 注释 8：原第 41 行

模块标识符（module IDs）。时钟控制驱动使用这些标识符来识别外设模块。

### 注释 9：原第 55 行

非共享外设（non-shared peripherals）：这些外设在各自驱动中拥有专用时钟控制，不使用 `periph_module_enable()`。取值从 `MODULE_MAX` 之后开始。

### 注释 10：原第 75 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ESP32C2_CLOCK_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp32c2__clock_8h.html)

---

[上一章](P006_esp32_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_esp32c3_clock.h_源码浏览.md)
