---
id: learning.zephyr-docs.api-source-reference.page-105
title: clock_control_silabs_siwx91x.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs__siwx91x_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第105章\_clock\_control\_silabs\_siwx91x.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs__siwx91x_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs__siwx91x_8h.html)。

## 105.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00025"></a>
<a id="foldopen00027"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__clock__control__silabs__siwx91x_html_gab38e7d7ff3ea5e9a12358aa4a98bd1dd"></a>
<a id="asiwx91x-clock_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructsilabs__siwx91x__clock__control__config_html"></a>
<a id="astructsilabs__siwx91x__clock__control__config_html_a3376c611ad9f1450b340d5e2b764c641"></a>
<a id="astructsilabs__siwx91x__clock__control__config_html_a5907249c723db10770838f2d2bb435fb"></a>
<a id="astructsilabs__siwx91x__clock__control__config_html_aa14c50b1e6a313daa690b016cdb7305c"></a>
<a id="astructsilabs__siwx91x__clock__control__pll__config_html"></a>
<a id="astructsilabs__siwx91x__clock__control__pll__config_html_a04bda8d54ed92f4103029a3a834f1ec3"></a>
<a id="astructsilabs__siwx91x__clock__control__pll__config_html_aa474e8ff41ecd61fe1d3a99f1844d94b"></a>
<a id="astructsilabs__siwx91x__clock__control__pll__config_html_ac7fa89c1dd94c0f17cc5f1de5939d89d"></a>

```c
/*
 * Copyright (c) 2024-2026 Silicon Laboratories Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_SILABS_SIWX91X_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_SILABS_SIWX91X_H_

#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/dt-bindings/clock/silabs/siwx91x-clock.h>


struct silabs_siwx91x_clock_control_config {
        uint32_t clkid;
        uint32_t ref_clkid;
        uint32_t clock_div;
};

struct silabs_siwx91x_clock_control_pll_config {
        uint32_t clkid;
        uint32_t ref_clkid;
        uint32_t frequency;
};

const struct device *siwx91x_clock_control_get_device(uint32_t clkid);


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_SILABS_SIWX91X_H_ */
```

## 105.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024-2026 Silicon Laboratories Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_SILABS_SIWX91X_H_`。

## 105.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs__siwx91x_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/dt-bindings/clock/silabs/siwx91x-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/siwx91x-clock_8h.html)
- [silabs_siwx91x_clock_control_config](../device_power_control_model_reference/P088_silabs_siwx91x_clock_control_config_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [clkid](../device_power_control_model_reference/P088_silabs_siwx91x_clock_control_config_结构体.md#aa14c50b1e6a313daa690b016cdb7305c)
- [ref_clkid](../device_power_control_model_reference/P088_silabs_siwx91x_clock_control_config_结构体.md#a5907249c723db10770838f2d2bb435fb)
- [clock_div](../device_power_control_model_reference/P088_silabs_siwx91x_clock_control_config_结构体.md#a3376c611ad9f1450b340d5e2b764c641)
- [silabs_siwx91x_clock_control_pll_config](../device_power_control_model_reference/P089_silabs_siwx91x_clock_control_pll_config_结构体.md)
- [clkid](../device_power_control_model_reference/P089_silabs_siwx91x_clock_control_pll_config_结构体.md#ac7fa89c1dd94c0f17cc5f1de5939d89d)
- [ref_clkid](../device_power_control_model_reference/P089_silabs_siwx91x_clock_control_pll_config_结构体.md#aa474e8ff41ecd61fe1d3a99f1844d94b)
- [frequency](../device_power_control_model_reference/P089_silabs_siwx91x_clock_control_pll_config_结构体.md#a04bda8d54ed92f4103029a3a834f1ec3)
- [device](../device_reference/P002_设备对象结构.md)
- [siwx91x_clock_control_get_device](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs__siwx91x.html#gab38e7d7ff3ea5e9a12358aa4a98bd1dd)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [siwx91x-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/siwx91x-clock_8h.html)
- [silabs_siwx91x_clock_control_config::clock_div](../device_power_control_model_reference/P088_silabs_siwx91x_clock_control_config_结构体.md#a3376c611ad9f1450b340d5e2b764c641)
- [silabs_siwx91x_clock_control_config::ref_clkid](../device_power_control_model_reference/P088_silabs_siwx91x_clock_control_config_结构体.md#a5907249c723db10770838f2d2bb435fb)
- [silabs_siwx91x_clock_control_config::clkid](../device_power_control_model_reference/P088_silabs_siwx91x_clock_control_config_结构体.md#aa14c50b1e6a313daa690b016cdb7305c)
- [silabs_siwx91x_clock_control_pll_config::frequency](../device_power_control_model_reference/P089_silabs_siwx91x_clock_control_pll_config_结构体.md#a04bda8d54ed92f4103029a3a834f1ec3)
- [silabs_siwx91x_clock_control_pll_config::ref_clkid](../device_power_control_model_reference/P089_silabs_siwx91x_clock_control_pll_config_结构体.md#aa474e8ff41ecd61fe1d3a99f1844d94b)
- [silabs_siwx91x_clock_control_pll_config::clkid](../device_power_control_model_reference/P089_silabs_siwx91x_clock_control_pll_config_结构体.md#ac7fa89c1dd94c0f17cc5f1de5939d89d)

---

[上一章](P104_clock_control_silabs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P106_cmsis_types.h_源码浏览.md)
