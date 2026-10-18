---
id: learning.zephyr-docs.api-source-supplement-reference.page-56
title: esp32_clock_control.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock__control_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_esp32\_clock\_control.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock__control_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock__control_8h.html)。

## 56.1\_原始可见代码（Source Code）

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
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00061"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="aesp32__clock_8h_html"></a>
<a id="aesp32c2__clock_8h_html"></a>
<a id="aesp32c3__clock_8h_html"></a>
<a id="aesp32c5__clock_8h_html"></a>
<a id="aesp32c61__clock_8h_html"></a>
<a id="aesp32c6__clock_8h_html"></a>
<a id="aesp32h2__clock_8h_html"></a>
<a id="aesp32p4__clock_8h_html"></a>
<a id="aesp32s2__clock_8h_html"></a>
<a id="aesp32s3__clock_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructesp32__clock__config_html"></a>
<a id="astructesp32__clock__config_html_a5cf7a77ea5b5e4780bde683c2cd10526"></a>
<a id="astructesp32__clock__config_html_ad42eba0397b1a988357b83a030298078"></a>
<a id="astructesp32__cpu__clock__config_html"></a>
<a id="astructesp32__cpu__clock__config_html_a181474dc51b7ddca51bc9b56e7a935e4"></a>
<a id="astructesp32__cpu__clock__config_html_a6b7de043a1282e7ea73a2b81b5f0abfd"></a>
<a id="astructesp32__cpu__clock__config_html_a7496bee5adc8d235bd4df9b93d791576"></a>
<a id="astructesp32__rtc__clock__config_html"></a>
<a id="astructesp32__rtc__clock__config_html_a2d4090c4e97f15c4ab04d92905d5119c"></a>
<a id="astructesp32__rtc__clock__config_html_ae04b2762e26a5e8d135c91b6f5d360e9"></a>

```c
/*
 * Copyright (c) 2024-2025 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ESP32_CLOCK_CONTROL_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ESP32_CLOCK_CONTROL_H_


#if defined(CONFIG_SOC_SERIES_ESP32)
#include <zephyr/dt-bindings/clock/esp32_clock.h>
#elif defined(CONFIG_SOC_SERIES_ESP32S2)
#include <zephyr/dt-bindings/clock/esp32s2_clock.h>
#elif defined(CONFIG_SOC_SERIES_ESP32S3)
#include <zephyr/dt-bindings/clock/esp32s3_clock.h>
#elif defined(CONFIG_SOC_SERIES_ESP32C2)
#include <zephyr/dt-bindings/clock/esp32c2_clock.h>
#elif defined(CONFIG_SOC_SERIES_ESP32C3)
#include <zephyr/dt-bindings/clock/esp32c3_clock.h>
#elif defined(CONFIG_SOC_SERIES_ESP32C5)
#include <zephyr/dt-bindings/clock/esp32c5_clock.h>
#elif defined(CONFIG_SOC_SERIES_ESP32C6)
#include <zephyr/dt-bindings/clock/esp32c6_clock.h>
#elif defined(CONFIG_SOC_SERIES_ESP32C61)
#include <zephyr/dt-bindings/clock/esp32c61_clock.h>
#elif defined(CONFIG_SOC_SERIES_ESP32H2)
#include <zephyr/dt-bindings/clock/esp32h2_clock.h>
#elif defined(CONFIG_SOC_SERIES_ESP32P4)
#include <zephyr/dt-bindings/clock/esp32p4_clock.h>
#endif /* CONFIG_SOC_SERIES_ESP32xx */

#define ESP32_CLOCK_CONTROL_SUBSYS_CPU 50
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST 51
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW 52
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST_NOMINAL 53
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW_NOMINAL 54

struct esp32_cpu_clock_config {
        int clk_src;
        uint32_t cpu_freq;
        uint32_t xtal_freq;
};

struct esp32_rtc_clock_config {
        uint32_t rtc_fast_clock_src;
        uint32_t rtc_slow_clock_src;
};

struct esp32_clock_config {
        struct esp32_cpu_clock_config cpu;
        struct esp32_rtc_clock_config rtc;
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ESP32_CLOCK_CONTROL_H_ */
```

## 56.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024-2025 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 42 行

条件编译配置标记：`CONFIG_SOC_SERIES_ESP32xx`。

### 注释 3：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ESP32_CLOCK_CONTROL_H_`。

## 56.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock__control_8h.html)
- [zephyr/dt-bindings/clock/esp32_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock_8h.html)
- [zephyr/dt-bindings/clock/esp32s2_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32s2__clock_8h.html)
- [zephyr/dt-bindings/clock/esp32s3_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32s3__clock_8h.html)
- [zephyr/dt-bindings/clock/esp32c2_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32c2__clock_8h.html)
- [zephyr/dt-bindings/clock/esp32c3_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32c3__clock_8h.html)
- [zephyr/dt-bindings/clock/esp32c5_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32c5__clock_8h.html)
- [zephyr/dt-bindings/clock/esp32c6_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32c6__clock_8h.html)
- [zephyr/dt-bindings/clock/esp32c61_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32c61__clock_8h.html)
- [zephyr/dt-bindings/clock/esp32h2_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32h2__clock_8h.html)
- [zephyr/dt-bindings/clock/esp32p4_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32p4__clock_8h.html)
- [esp32_cpu_clock_config](../device_power_control_model_reference/P009_esp32_cpu_clock_config_结构体.md)
- [clk_src](../device_power_control_model_reference/P009_esp32_cpu_clock_config_结构体.md#a7496bee5adc8d235bd4df9b93d791576)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [cpu_freq](../device_power_control_model_reference/P009_esp32_cpu_clock_config_结构体.md#a181474dc51b7ddca51bc9b56e7a935e4)
- [xtal_freq](../device_power_control_model_reference/P009_esp32_cpu_clock_config_结构体.md#a6b7de043a1282e7ea73a2b81b5f0abfd)
- [esp32_rtc_clock_config](../device_power_control_model_reference/P010_esp32_rtc_clock_config_结构体.md)
- [rtc_fast_clock_src](../device_power_control_model_reference/P010_esp32_rtc_clock_config_结构体.md#a2d4090c4e97f15c4ab04d92905d5119c)
- [rtc_slow_clock_src](../device_power_control_model_reference/P010_esp32_rtc_clock_config_结构体.md#ae04b2762e26a5e8d135c91b6f5d360e9)
- [esp32_clock_config](../device_power_control_model_reference/P008_esp32_clock_config_结构体.md)
- [cpu](../device_power_control_model_reference/P008_esp32_clock_config_结构体.md#a5cf7a77ea5b5e4780bde683c2cd10526)
- [rtc](../device_power_control_model_reference/P008_esp32_clock_config_结构体.md#ad42eba0397b1a988357b83a030298078)
- [esp32_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock_8h.html)
- [esp32c2_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32c2__clock_8h.html)
- [esp32c3_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32c3__clock_8h.html)
- [esp32c5_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32c5__clock_8h.html)
- [esp32c61_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32c61__clock_8h.html)
- [esp32c6_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32c6__clock_8h.html)
- [esp32h2_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32h2__clock_8h.html)
- [esp32p4_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32p4__clock_8h.html)
- [esp32s2_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32s2__clock_8h.html)
- [esp32s3_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32s3__clock_8h.html)
- [esp32_clock_config::cpu](../device_power_control_model_reference/P008_esp32_clock_config_结构体.md#a5cf7a77ea5b5e4780bde683c2cd10526)
- [esp32_clock_config::rtc](../device_power_control_model_reference/P008_esp32_clock_config_结构体.md#ad42eba0397b1a988357b83a030298078)
- [esp32_cpu_clock_config::cpu_freq](../device_power_control_model_reference/P009_esp32_cpu_clock_config_结构体.md#a181474dc51b7ddca51bc9b56e7a935e4)
- [esp32_cpu_clock_config::xtal_freq](../device_power_control_model_reference/P009_esp32_cpu_clock_config_结构体.md#a6b7de043a1282e7ea73a2b81b5f0abfd)
- [esp32_cpu_clock_config::clk_src](../device_power_control_model_reference/P009_esp32_cpu_clock_config_结构体.md#a7496bee5adc8d235bd4df9b93d791576)
- [esp32_rtc_clock_config::rtc_fast_clock_src](../device_power_control_model_reference/P010_esp32_rtc_clock_config_结构体.md#a2d4090c4e97f15c4ab04d92905d5119c)
- [esp32_rtc_clock_config::rtc_slow_clock_src](../device_power_control_model_reference/P010_esp32_rtc_clock_config_结构体.md#ae04b2762e26a5e8d135c91b6f5d360e9)

---

[上一章](P055_esp32-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P057_esp32c2-pinctrl.h_源码浏览.md)
