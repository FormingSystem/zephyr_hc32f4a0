---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-6
title: esp32_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_esp32\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock_8h.html)。

## 6.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2020 Mohamed ElShahawi
 * Copyright (c) 2021 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ESP32_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ESP32_CLOCK_H_

/* Supported CPU clock Sources */
#define ESP32_CPU_CLK_SRC_XTAL 0U
#define ESP32_CPU_CLK_SRC_PLL  1U
#define ESP32_CLK_SRC_RC_FAST  2U
#define ESP32_CLK_SRC_APLL_CLK 3U

/* Supported PLL CPU frequencies */
#define ESP32_CLK_CPU_PLL_80M     80000000
#define ESP32_CLK_CPU_PLL_160M    160000000
#define ESP32_CLK_CPU_PLL_240M    240000000
#define ESP32_CLK_CPU_RC_FAST_FREQ 1062500

/* Supported XTAL frequencies */
#define ESP32_CLK_XTAL_24M             24000000
#define ESP32_CLK_XTAL_26M             26000000
#define ESP32_CLK_XTAL_40M             40000000

/* Supported RTC fast clock sources */
#define ESP32_RTC_FAST_CLK_SRC_XTAL_D4 0
#define ESP32_RTC_FAST_CLK_SRC_RC_FAST 1

/* Supported RTC slow clock sources */
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW      0
#define ESP32_RTC_SLOW_CLK_SRC_XTAL32K      1
#define ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256 2
#define ESP32_RTC_SLOW_CLK_32K_EXT_OSC      9

/* RTC slow clock frequencies */
#define ESP32_RTC_SLOW_CLK_SRC_RC_SLOW_FREQ      150000
#define ESP32_RTC_SLOW_CLK_SRC_XTAL32K_FREQ      32768
#define ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256_FREQ 33203

/* Modules IDs
 * These are used by the clock control driver to identify peripheral modules.
 */
#define ESP32_UART1_MODULE           0
#define ESP32_UART2_MODULE           1
#define ESP32_I2S0_MODULE            2
#define ESP32_TIMG0_MODULE           3
#define ESP32_TIMG1_MODULE           4
#define ESP32_UHCI0_MODULE           5
#define ESP32_SPI_MODULE             6
#define ESP32_HSPI_MODULE            7
#define ESP32_VSPI_MODULE            8
#define ESP32_RNG_MODULE             9
#define ESP32_WIFI_MODULE            10
#define ESP32_BT_MODULE              11
#define ESP32_WIFI_BT_COMMON_MODULE  12
#define ESP32_BT_BASEBAND_MODULE     13
#define ESP32_PHY_CALIBRATION_MODULE 14
#define ESP32_MODULE_MAX             15

/* Non-shared peripherals - these have dedicated clock control in their drivers
 * and don't use periph_module_enable(). Values start after MODULE_MAX.
 */
#define ESP32_LEDC_MODULE       100
#define ESP32_UART0_MODULE      101
#define ESP32_I2C0_MODULE       102
#define ESP32_I2C1_MODULE       103
#define ESP32_I2S1_MODULE       104
#define ESP32_PWM0_MODULE       105
#define ESP32_PWM1_MODULE       106
#define ESP32_UHCI1_MODULE      107
#define ESP32_RMT_MODULE        108
#define ESP32_PCNT_MODULE       109
#define ESP32_SPI_DMA_MODULE    110
#define ESP32_SDMMC_MODULE      111
#define ESP32_SDIO_SLAVE_MODULE 112
#define ESP32_TWAI_MODULE       113
#define ESP32_CAN_MODULE        ESP32_TWAI_MODULE
#define ESP32_EMAC_MODULE       114
#define ESP32_AES_MODULE        115
#define ESP32_SHA_MODULE        116
#define ESP32_RSA_MODULE        117
#define ESP32_SARADC_MODULE     118
#define ESP32_BT_LC_MODULE      119

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ESP32_CLOCK_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Mohamed ElShahawi。

版权（Copyright）：© 2021 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

支持的 CPU 时钟源（clock sources）。

### 注释 3：原第 17 行

支持的 PLL CPU 频率。

### 注释 4：原第 23 行

支持的晶体（XTAL）频率。

### 注释 5：原第 28 行

支持的 RTC 快速时钟源。

### 注释 6：原第 32 行

支持的 RTC 慢速时钟源。

### 注释 7：原第 38 行

RTC 慢速时钟频率。

### 注释 8：原第 43 行

模块标识符（module IDs）。时钟控制驱动使用这些标识符来识别外设模块。

### 注释 9：原第 63 行

非共享外设（non-shared peripherals）：这些外设在各自驱动中拥有专用时钟控制，不使用 `periph_module_enable()`。取值从 `MODULE_MAX` 之后开始。

### 注释 10：原第 88 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ESP32_CLOCK_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock_8h.html)

---

[上一章](P005_dap_link.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_esp32c2_clock.h_源码浏览.md)
