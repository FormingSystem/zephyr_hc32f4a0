---
id: learning.zephyr-docs.api-source-supplement-reference.page-7
title: ameba_clock_control.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ameba__clock__control_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_ameba\_clock\_control.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ameba__clock__control_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ameba__clock__control_8h.html)。

## 7.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
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
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="aamebad__clock_8h_html"></a>
<a id="aamebadplus__clock_8h_html"></a>
<a id="aamebag2__clock_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Realtek Semiconductor Corp.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_AMEBA_CLOCK_CONTROL_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_AMEBA_CLOCK_CONTROL_H_

#ifdef __cplusplus
extern "C" {
#endif


/*
 * Select the appropriate Ameba clock Devicetree binding header
 * according to the SoC series in use.
 */
#if defined(CONFIG_SOC_SERIES_AMEBADPLUS)
#include <zephyr/dt-bindings/clock/amebadplus_clock.h>
#elif defined(CONFIG_SOC_SERIES_AMEBAD)
#include <zephyr/dt-bindings/clock/amebad_clock.h>
#elif defined(CONFIG_SOC_SERIES_AMEBAG2)
#include <zephyr/dt-bindings/clock/amebag2_clock.h>
#else
#error "Please select the correct Ameba SoC series."
#endif


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_AMEBA_CLOCK_CONTROL_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Realtek Semiconductor Corp.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 29 行

根据正在使用的片上系统（SoC）系列，选择合适的 Ameba 时钟设备树绑定（Devicetree binding）头文件。

### 注释 3：原第 49 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_AMEBA_CLOCK_CONTROL_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ameba__clock__control_8h.html)
- [zephyr/dt-bindings/clock/amebadplus_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/amebadplus__clock_8h.html)
- [zephyr/dt-bindings/clock/amebad_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/amebad__clock_8h.html)
- [zephyr/dt-bindings/clock/amebag2_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/amebag2__clock_8h.html)
- [amebad_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/amebad__clock_8h.html)
- [amebadplus_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/amebadplus__clock_8h.html)
- [amebag2_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/amebag2__clock_8h.html)

---

[上一章](P006_ambiq-apollo2-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_ans.h_源码浏览.md)
