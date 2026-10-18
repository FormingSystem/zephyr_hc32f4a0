---
id: learning.zephyr-docs.api-source-reference.page-710
title: renesas_rx_cgc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__cgc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第710章\_renesas\_rx\_cgc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__cgc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__cgc_8h.html)。

## 710.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
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
<a id="foldopen00052"></a>
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
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00112"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="foldopen00123"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="foldopen00158"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="foldopen00165"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="foldopen00173"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="aclock__control_8h_html"></a>
<a id="arx__clock_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructclock__control__rx__pclk__cfg_html"></a>
<a id="astructclock__control__rx__pclk__cfg_html_a46ba3c9011b9bfeb792db0017da55d5c"></a>
<a id="astructclock__control__rx__pclk__cfg_html_ad6b95060d8b16fc514451c9403facbe3"></a>
<a id="astructclock__control__rx__pll__cfg_html"></a>
<a id="astructclock__control__rx__pll__cfg_html_a06f3394bdaadb0f06cce23cd90c95061"></a>
<a id="astructclock__control__rx__pll__data_html"></a>
<a id="astructclock__control__rx__pll__data_html_a81def945f92f0b71412e6945378364fb"></a>
<a id="astructclock__control__rx__pll__data_html_aa8df23fd39a75b6a6a5fde7d4a657dd4"></a>
<a id="astructclock__control__rx__root__cfg_html"></a>
<a id="astructclock__control__rx__root__cfg_html_a3c551c54867d14793fc67b1321f93a92"></a>
<a id="astructclock__control__rx__subsys__cfg_html"></a>
<a id="astructclock__control__rx__subsys__cfg_html_a8668364871caea64aab66294a2fb915e"></a>
<a id="astructclock__control__rx__subsys__cfg_html_aa47beb43957995ad7eda8f5934ae307a"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2024-2026 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RX_CGC_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RX_CGC_H_

#include <zephyr/drivers/clock_control.h>
#include <zephyr/dt-bindings/clock/rx_clock.h>


#define RX_CGC_PROP_HAS_STATUS_OKAY_OR(node_id, prop, default_value)                               \
        COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay), (DT_PROP(node_id, prop)),                   \
                    (default_value))

#ifdef CONFIG_HAS_RENESAS_RX_FSP
#define RX_CGC_CLK_SRC(node_id)                                                                    \
        COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay),                                             \
                    (UTIL_CAT(BSP_CLOCKS_SOURCE_, DT_NODE_FULL_NAME_UPPER_TOKEN(node_id))),        \
                    (BSP_CLOCKS_CLOCK_DISABLED))

#define RX_CGC_CLK_DIV(clk, prop, default_value)                                                   \
        UTIL_CAT(RX_CGC_DIV_, DT_NODE_FULL_NAME_UPPER_TOKEN(clk))                                  \
        (RX_CGC_PROP_HAS_STATUS_OKAY_OR(clk, prop, default_value))

#else
#define RX_CGC_CLK_SRC(node_id)                                                                    \
        COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay),                                             \
                    (UTIL_CAT(RX_CLOCKS_SOURCE_, DT_NODE_FULL_NAME_UPPER_TOKEN(node_id))),        \
                    (RX_CLOCKS_CLOCK_DISABLED))
#endif

#ifdef CONFIG_HAS_RENESAS_RX_FSP
#define RX_CGC_DIV_CPUCLK(n)     UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RX_CGC_DIV_MRICLK(n)     UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RX_CGC_DIV_ICLK(n)       UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RX_CGC_DIV_PCLKA(n)      UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RX_CGC_DIV_PCLKB(n)      UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RX_CGC_DIV_PCLKC(n)      UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RX_CGC_DIV_PCLKD(n)      UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RX_CGC_DIV_PCLKE(n)      UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RX_CGC_DIV_BCLK(n)       UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RX_CGC_DIV_BCLKA(n)      UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RX_CGC_DIV_MRPCLK(n)     UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RX_CGC_DIV_CLKOUT(n)     UTIL_CAT(BSP_CLOCKS_SYS_CLOCK_DIV_, n)
#define RX_CGC_DIV_SCICLK(n)     UTIL_CAT(BSP_CLOCKS_SCI_CLOCK_DIV_, n)
#define RX_CGC_DIV_SPICLK(n)     UTIL_CAT(BSP_CLOCKS_SPI_CLOCK_DIV_, n)
#define RX_CGC_DIV_CANFDCLK(n)   UTIL_CAT(BSP_CLOCKS_CANFD_CLOCK_DIV_, n)
#define RX_CGC_DIV_GPTCLK(n)     UTIL_CAT(BSP_CLOCKS_GPT_CLOCK_DIV_, n)
#define RX_CGC_DIV_I3CCLK(n)     UTIL_CAT(BSP_CLOCKS_I3C_CLOCK_DIV_, n)
#define RX_CGC_DIV_UCLK(n)       UTIL_CAT(BSP_CLOCKS_USB_CLOCK_DIV_, n)
#define RX_CGC_DIV_USB60CLK(n)   UTIL_CAT(BSP_CLOCKS_USB60_CLOCK_DIV_, n)
#define RX_CGC_DIV_OCTASPICLK(n) UTIL_CAT(BSP_CLOCKS_OCTA_CLOCK_DIV_, n)
#define RX_CGC_DIV_PLL(n)        UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RX_CGC_DIV_PLLP(n)       UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RX_CGC_DIV_PLLQ(n)       UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RX_CGC_DIV_PLLR(n)       UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RX_CGC_DIV_PLL2(n)       UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RX_CGC_DIV_PLL2P(n)      UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RX_CGC_DIV_PLL2Q(n)      UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RX_CGC_DIV_PLL2R(n)      UTIL_CAT(BSP_CLOCKS_PLL_DIV_, n)
#define RX_CGC_DIV_ADCCLK(n)     UTIL_CAT(BSP_CLOCKS_ADC_CLOCK_DIV_, n)
#define RX_CGC_DIV_ESWCLK(n)     UTIL_CAT(BSP_CLOCKS_ESW_CLOCK_DIV_, n)
#define RX_CGC_DIV_ESWPHYCLK(n)  UTIL_CAT(BSP_CLOCKS_ESWPHY_CLOCK_DIV_, n)
#define RX_CGC_DIV_ETHPHYCLK(n)  UTIL_CAT(BSP_CLOCKS_ETHPHY_CLOCK_DIV_, n)
#define RX_CGC_DIV_ESCCLK(n)     UTIL_CAT(BSP_CLOCKS_ESC_CLOCK_DIV_, n)
#define RX_CGC_DIV_DSMIFCLK(n)   UTIL_CAT(BSP_CLOCKS_DSMIF_CLOCK_DIV_, n)

#define BSP_CLOCKS_SOURCE_PLL  BSP_CLOCKS_SOURCE_CLOCK_PLL
#define BSP_CLOCKS_SOURCE_PLLP BSP_CLOCKS_SOURCE_CLOCK_PLL
#define BSP_CLOCKS_SOURCE_PLLQ BSP_CLOCKS_SOURCE_CLOCK_PLL1Q
#define BSP_CLOCKS_SOURCE_PLLR BSP_CLOCKS_SOURCE_CLOCK_PLL1R

#define BSP_CLOCKS_SOURCE_PLL2  BSP_CLOCKS_SOURCE_CLOCK_PLL2
#define BSP_CLOCKS_SOURCE_PLL2P BSP_CLOCKS_SOURCE_CLOCK_PLL2
#define BSP_CLOCKS_SOURCE_PLL2Q BSP_CLOCKS_SOURCE_CLOCK_PLL2Q
#define BSP_CLOCKS_SOURCE_PLL2R BSP_CLOCKS_SOURCE_CLOCK_PLL2R

#endif

#define RX_IF_CLK_SRC(node_id)                                                                     \
        COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay),\
                        (UTIL_CAT(RX_IF_CLOCKS_SOURCE_, DT_NODE_FULL_NAME_UPPER_TOKEN(node_id))),\
                        (RX_CLOCKS_CLOCK_DISABLED))

#define RX_LPT_CLK_SRC(node_id)                                                                    \
        COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay),\
                        (UTIL_CAT(RX_LPT_CLOCKS_SOURCE_, DT_NODE_FULL_NAME_UPPER_TOKEN(node_id))),\
                        (RX_LPT_CLOCKS_NON_USE))

#define RX_CGC_PLL_CLK_SRC(node_id)                                                                \
        COND_CODE_1(DT_NODE_HAS_STATUS(node_id, okay),                                             \
                (UTIL_CAT(RX_PLL_CLOCKS_SOURCE_, DT_NODE_FULL_NAME_UPPER_TOKEN(node_id))),        \
                    (RX_CLOCKS_CLOCK_DISABLED))

struct clock_control_rx_pclk_cfg {
        const struct device *clock_src_dev;
        uint32_t clk_div;
};

struct clock_control_rx_subsys_cfg {
        uint32_t mstp;
        uint32_t stop_bit;
};

struct clock_control_rx_pll_cfg {
        const struct device *clock_dev;
};

struct clock_control_rx_pll_data {
        uint32_t pll_div;
        uint32_t pll_mul;
};

struct clock_control_rx_root_cfg {
        uint32_t rate;
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RX_CGC_H_ */
```

## 710.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024-2026 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 179 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RX_CGC_H_`。

## 710.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__cgc_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [zephyr/dt-bindings/clock/rx_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/rx__clock_8h.html)
- [clock_control_rx_pclk_cfg](../clock_cmsis_model_reference/P003_clock_control_rx_pclk_cfg_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [clock_src_dev](../clock_cmsis_model_reference/P003_clock_control_rx_pclk_cfg_结构体.md#a46ba3c9011b9bfeb792db0017da55d5c)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [clk_div](../clock_cmsis_model_reference/P003_clock_control_rx_pclk_cfg_结构体.md#ad6b95060d8b16fc514451c9403facbe3)
- [clock_control_rx_subsys_cfg](../clock_cmsis_model_reference/P007_clock_control_rx_subsys_cfg_结构体.md)
- [mstp](../clock_cmsis_model_reference/P007_clock_control_rx_subsys_cfg_结构体.md#aa47beb43957995ad7eda8f5934ae307a)
- [stop_bit](../clock_cmsis_model_reference/P007_clock_control_rx_subsys_cfg_结构体.md#a8668364871caea64aab66294a2fb915e)
- [clock_control_rx_pll_cfg](../clock_cmsis_model_reference/P004_clock_control_rx_pll_cfg_结构体.md)
- [clock_dev](../clock_cmsis_model_reference/P004_clock_control_rx_pll_cfg_结构体.md#a06f3394bdaadb0f06cce23cd90c95061)
- [clock_control_rx_pll_data](../clock_cmsis_model_reference/P005_clock_control_rx_pll_data_结构体.md)
- [pll_div](../clock_cmsis_model_reference/P005_clock_control_rx_pll_data_结构体.md#a81def945f92f0b71412e6945378364fb)
- [pll_mul](../clock_cmsis_model_reference/P005_clock_control_rx_pll_data_结构体.md#aa8df23fd39a75b6a6a5fde7d4a657dd4)
- [clock_control_rx_root_cfg](../clock_cmsis_model_reference/P006_clock_control_rx_root_cfg_结构体.md)
- [rate](../clock_cmsis_model_reference/P006_clock_control_rx_root_cfg_结构体.md#a3c551c54867d14793fc67b1321f93a92)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [rx_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/rx__clock_8h.html)
- [clock_control_rx_pclk_cfg::clock_src_dev](../clock_cmsis_model_reference/P003_clock_control_rx_pclk_cfg_结构体.md#a46ba3c9011b9bfeb792db0017da55d5c)
- [clock_control_rx_pclk_cfg::clk_div](../clock_cmsis_model_reference/P003_clock_control_rx_pclk_cfg_结构体.md#ad6b95060d8b16fc514451c9403facbe3)
- [clock_control_rx_pll_cfg::clock_dev](../clock_cmsis_model_reference/P004_clock_control_rx_pll_cfg_结构体.md#a06f3394bdaadb0f06cce23cd90c95061)
- [clock_control_rx_pll_data::pll_div](../clock_cmsis_model_reference/P005_clock_control_rx_pll_data_结构体.md#a81def945f92f0b71412e6945378364fb)
- [clock_control_rx_pll_data::pll_mul](../clock_cmsis_model_reference/P005_clock_control_rx_pll_data_结构体.md#aa8df23fd39a75b6a6a5fde7d4a657dd4)
- [clock_control_rx_root_cfg::rate](../clock_cmsis_model_reference/P006_clock_control_rx_root_cfg_结构体.md#a3c551c54867d14793fc67b1321f93a92)
- [clock_control_rx_subsys_cfg::stop_bit](../clock_cmsis_model_reference/P007_clock_control_rx_subsys_cfg_结构体.md#a8668364871caea64aab66294a2fb915e)
- [clock_control_rx_subsys_cfg::mstp](../clock_cmsis_model_reference/P007_clock_control_rx_subsys_cfg_结构体.md#aa47beb43957995ad7eda8f5934ae307a)

---

[上一章](P709_renesas_ra_external_interrupt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P711_renesas_rx_dtc.h_源码浏览.md)
