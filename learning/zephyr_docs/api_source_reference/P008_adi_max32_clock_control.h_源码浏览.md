---
id: learning.zephyr-docs.api-source-reference.page-8
title: adi_max32_clock_control.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock__control_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_adi\_max32\_clock\_control.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock__control_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock__control_8h.html)。

## 8.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00027"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
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
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="aadi__max32__clock_8h_html"></a>
<a id="aclock__control_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructmax32__perclk_html"></a>
<a id="astructmax32__perclk_html_a02bb20153ff5e67ad9a7dbc5a45c646c"></a>
<a id="astructmax32__perclk_html_a10dd006d4c09983c0947a07eb9085348"></a>
<a id="astructmax32__perclk_html_aef1b470aa172b72c180b1cb2a700c459"></a>

```c
/*
 * Copyright (c) 2023-2024 Analog Devices, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ADI_MAX32_CLOCK_CONTROL_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ADI_MAX32_CLOCK_CONTROL_H_

#include <zephyr/drivers/clock_control.h>

#include <zephyr/dt-bindings/clock/adi_max32_clock.h>

#include <wrap_max32_sys.h>


struct max32_perclk {
        uint32_t bus;
        uint32_t bit;
        uint32_t clk_src;
};

#define ADI_MAX32_SYSCLK_PRESCALER DT_PROP_OR(DT_NODELABEL(gcr), sysclk_prescaler, 1)

#define ADI_MAX32_CLK_IPO_FREQ    DT_PROP(DT_NODELABEL(clk_ipo), clock_frequency)
#define ADI_MAX32_CLK_ERFO_FREQ   DT_PROP_OR(DT_NODELABEL(clk_erfo), clock_frequency, 0)
#define ADI_MAX32_CLK_IBRO_FREQ   DT_PROP_OR(DT_NODELABEL(clk_ibro), clock_frequency, 0)
#define ADI_MAX32_CLK_ISO_FREQ    DT_PROP_OR(DT_NODELABEL(clk_iso), clock_frequency, 0)
#define ADI_MAX32_CLK_INRO_FREQ   DT_PROP(DT_NODELABEL(clk_inro), clock_frequency)
#define ADI_MAX32_CLK_ERTCO_FREQ  DT_PROP(DT_NODELABEL(clk_ertco), clock_frequency)
#define ADI_MAX32_CLK_IPLL_FREQ   DT_PROP_OR(DT_NODELABEL(clk_ipll), clock_frequency, 0)
#define ADI_MAX32_CLK_EBO_FREQ    DT_PROP_OR(DT_NODELABEL(clk_ebo), clock_frequency, 0)
#define ADI_MAX32_CLK_EXTCLK_FREQ DT_PROP_OR(DT_NODELABEL(clk_extclk), clock_frequency, 0)


#define DT_GCR_CLOCKS_CTRL DT_CLOCKS_CTLR(DT_NODELABEL(gcr))

#if DT_SAME_NODE(DT_GCR_CLOCKS_CTRL, DT_NODELABEL(clk_ipo))
#define ADI_MAX32_SYSCLK_SRC  ADI_MAX32_CLK_IPO
#define ADI_MAX32_SYSCLK_FREQ (ADI_MAX32_CLK_IPO_FREQ / ADI_MAX32_SYSCLK_PRESCALER)
#endif
#if DT_SAME_NODE(DT_GCR_CLOCKS_CTRL, DT_NODELABEL(clk_erfo))
#define ADI_MAX32_SYSCLK_SRC  ADI_MAX32_CLK_ERFO
#define ADI_MAX32_SYSCLK_FREQ (ADI_MAX32_CLK_ERFO_FREQ / ADI_MAX32_SYSCLK_PRESCALER)
#endif
#if DT_SAME_NODE(DT_GCR_CLOCKS_CTRL, DT_NODELABEL(clk_ibro))
#define ADI_MAX32_SYSCLK_SRC  ADI_MAX32_CLK_IBRO
#define ADI_MAX32_SYSCLK_FREQ (ADI_MAX32_CLK_IBRO_FREQ / ADI_MAX32_SYSCLK_PRESCALER)
#endif
#if DT_SAME_NODE(DT_GCR_CLOCKS_CTRL, DT_NODELABEL(clk_iso))
#define ADI_MAX32_SYSCLK_SRC  ADI_MAX32_CLK_ISO
#define ADI_MAX32_SYSCLK_FREQ (ADI_MAX32_CLK_ISO_FREQ / ADI_MAX32_SYSCLK_PRESCALER)
#endif
#if DT_SAME_NODE(DT_GCR_CLOCKS_CTRL, DT_NODELABEL(clk_inro))
#define ADI_MAX32_SYSCLK_SRC  ADI_MAX32_CLK_INRO
#define ADI_MAX32_SYSCLK_FREQ (ADI_MAX32_CLK_INRO_FREQ / ADI_MAX32_SYSCLK_PRESCALER)
#endif
#if DT_SAME_NODE(DT_GCR_CLOCKS_CTRL, DT_NODELABEL(clk_ertco))
#define ADI_MAX32_SYSCLK_SRC  ADI_MAX32_CLK_ERTCO
#define ADI_MAX32_SYSCLK_FREQ (ADI_MAX32_CLK_ERTCO_FREQ / ADI_MAX32_SYSCLK_PRESCALER)
#endif
#if DT_SAME_NODE(DT_GCR_CLOCKS_CTRL, DT_NODELABEL(clk_extclk))
#define ADI_MAX32_SYSCLK_SRC  ADI_MAX32_CLK_EXTCLK
#define ADI_MAX32_SYSCLK_FREQ (ADI_MAX32_CLK_EXTCLK_FREQ / ADI_MAX32_SYSCLK_PRESCALER)
#endif
#if DT_SAME_NODE(DT_GCR_CLOCKS_CTRL, DT_NODELABEL(clk_ipll))
#define ADI_MAX32_SYSCLK_SRC  ADI_MAX32_CLK_IPLL
#define ADI_MAX32_SYSCLK_FREQ (ADI_MAX32_CLK_IPLL_FREQ / ADI_MAX32_SYSCLK_PRESCALER)
#endif
#if DT_SAME_NODE(DT_GCR_CLOCKS_CTRL, DT_NODELABEL(clk_ebo))
#define ADI_MAX32_SYSCLK_SRC  ADI_MAX32_CLK_EBO
#define ADI_MAX32_SYSCLK_FREQ (ADI_MAX32_CLK_EBO_FREQ / ADI_MAX32_SYSCLK_PRESCALER)
#endif

#ifndef ADI_MAX32_SYSCLK_SRC
#define ADI_MAX32_SYSCLK_SRC  ADI_MAX32_CLK_IPO
#define ADI_MAX32_SYSCLK_FREQ (ADI_MAX32_CLK_IPO_FREQ / ADI_MAX32_SYSCLK_PRESCALER)
#endif

#define ADI_MAX32_PCLK_FREQ (ADI_MAX32_SYSCLK_FREQ / 2)

#define ADI_MAX32_GET_PRPH_CLK_FREQ(clk_src)                                                       \
        ((clk_src) == ADI_MAX32_PRPH_CLK_SRC_PCLK        ? ADI_MAX32_PCLK_FREQ                     \
         : (clk_src) == ADI_MAX32_PRPH_CLK_SRC_IBRO      ? ADI_MAX32_CLK_IBRO_FREQ                 \
         : (clk_src) == ADI_MAX32_PRPH_CLK_SRC_ERFO      ? ADI_MAX32_CLK_ERFO_FREQ                 \
         : (clk_src) == ADI_MAX32_PRPH_CLK_SRC_ERTCO     ? ADI_MAX32_CLK_ERTCO_FREQ                \
         : (clk_src) == ADI_MAX32_PRPH_CLK_SRC_INRO      ? ADI_MAX32_CLK_INRO_FREQ                 \
         : (clk_src) == ADI_MAX32_PRPH_CLK_SRC_ISO       ? ADI_MAX32_CLK_ISO_FREQ                  \
         : (clk_src) == ADI_MAX32_PRPH_CLK_SRC_IBRO_DIV8 ? (ADI_MAX32_CLK_IBRO_FREQ / 8)           \
         : (clk_src) == ADI_MAX32_PRPH_CLK_SRC_EXTCLK    ? ADI_MAX32_CLK_EXTCLK_FREQ               \
         : (clk_src) == ADI_MAX32_PRPH_CLK_SRC_IPLL      ? ADI_MAX32_CLK_IPLL_FREQ                 \
         : (clk_src) == ADI_MAX32_PRPH_CLK_SRC_EBO       ? ADI_MAX32_CLK_EBO_FREQ                  \
                                                         : 0)



#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ADI_MAX32_CLOCK_CONTROL_H_ */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023-2024 Analog Devices, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ADI_MAX32_CLOCK_CONTROL_H_`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock__control_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [zephyr/dt-bindings/clock/adi_max32_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock_8h.html)
- [max32_perclk](../device_power_control_model_reference/P025_max32_perclk_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bus](../device_power_control_model_reference/P025_max32_perclk_结构体.md#aef1b470aa172b72c180b1cb2a700c459)
- [bit](../device_power_control_model_reference/P025_max32_perclk_结构体.md#a10dd006d4c09983c0947a07eb9085348)
- [clk_src](../device_power_control_model_reference/P025_max32_perclk_结构体.md#a02bb20153ff5e67ad9a7dbc5a45c646c)
- [adi_max32_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock_8h.html)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [max32_perclk::clk_src](../device_power_control_model_reference/P025_max32_perclk_结构体.md#a02bb20153ff5e67ad9a7dbc5a45c646c)
- [max32_perclk::bit](../device_power_control_model_reference/P025_max32_perclk_结构体.md#a10dd006d4c09983c0947a07eb9085348)
- [max32_perclk::bus](../device_power_control_model_reference/P025_max32_perclk_结构体.md#aef1b470aa172b72c180b1cb2a700c459)

---

[上一章](P007_adi-max32-hpb.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P009_adltc2990.h_源码浏览.md)
