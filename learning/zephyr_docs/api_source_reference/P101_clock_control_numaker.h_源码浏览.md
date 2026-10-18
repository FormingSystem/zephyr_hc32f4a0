---
id: learning.zephyr-docs.api-source-reference.page-101
title: clock_control_numaker.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numaker_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第101章\_clock\_control\_numaker.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numaker_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numaker_8h.html)。

## 101.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00045"></a>
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
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructnumaker__scc__subsys__pcc__rate_html"></a>
<a id="astructnumaker__scc__subsys__pcc__rate_html_a14bfb22faf2ac674a3769242de557bd6"></a>
<a id="astructnumaker__scc__subsys__pcc__rate_html_a20d5cc4ed27b98c995ddaf89a6b7938f"></a>
<a id="astructnumaker__scc__subsys__pcc__rate_html_a792d0898930c44509f9be2daaf00ba97"></a>
<a id="astructnumaker__scc__subsys__pcc__rate_html_a8e32abe756e48ba9836d2498651e4b48"></a>
<a id="astructnumaker__scc__subsys__pcc__rate_html_ac1368bffb5781c37662535ea7a11b3fb"></a>
<a id="astructnumaker__scc__subsys__pcc__rate_html_af826904ecf107d6e2a027832922afbb1"></a>
<a id="astructnumaker__scc__subsys__pcc_html"></a>
<a id="astructnumaker__scc__subsys__pcc_html_a4ebf5a91a803cd92f10d25fcdd0c0eeb"></a>
<a id="astructnumaker__scc__subsys__pcc_html_aed6a31a6ba27aa4eaf05cff984b9c360"></a>
<a id="astructnumaker__scc__subsys__pcc_html_af24dd5113645830ca2e4a3c9d0b92126"></a>
<a id="astructnumaker__scc__subsys__rate_html"></a>
<a id="astructnumaker__scc__subsys__rate_html_a159486917a5c695f66edebb4749cd1d7"></a>
<a id="astructnumaker__scc__subsys_html"></a>
<a id="astructnumaker__scc__subsys_html_af8e2099977ecba2c53808fe8db4e041a"></a>
<a id="astructnumaker__scc__subsys_html_af8e8bc8bd9236ed245d56ef57b6e9082"></a>

```c
/*
 * Copyright (c) 2023 Nuvoton Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#include <stdint.h>

#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_NUMAKER_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_NUMAKER_H_


#define NUMAKER_SCC_CLKSW_UNTOUCHED 0
#define NUMAKER_SCC_CLKSW_ENABLE    1
#define NUMAKER_SCC_CLKSW_DISABLE   2

#define NUMAKER_SCC_SUBSYS_ID_PCC 1

struct numaker_scc_subsys_pcc {
        uint32_t clk_modidx;
        uint32_t clk_src;
        uint32_t clk_div;
};

struct numaker_scc_subsys_pcc_rate {
#if defined(CONFIG_SOC_SERIES_M55M1X)
        uint64_t clk_modidx_real;
#else
        uint32_t clk_modidx_real;
#endif
        uint32_t clk_src_idx;
        uint32_t clk_src_rate;
        uint32_t clk_div_value;
        uint32_t clk_div_value_max;
        uint32_t clk_mod_rate;
};

struct numaker_scc_subsys {
        uint32_t subsys_id;

        union {
                struct numaker_scc_subsys_pcc pcc;
        };
};

struct numaker_scc_subsys_rate {
        union {
                struct numaker_scc_subsys_pcc_rate pcc;
        };
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_NUMAKER_H_ */
```

## 101.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nuvoton Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 76 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_NUMAKER_H_`。

## 101.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numaker_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [numaker_scc_subsys_pcc](../device_power_control_model_reference/P050_numaker_scc_subsys_pcc_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [clk_modidx](../device_power_control_model_reference/P050_numaker_scc_subsys_pcc_结构体.md#a4ebf5a91a803cd92f10d25fcdd0c0eeb)
- [clk_src](../device_power_control_model_reference/P050_numaker_scc_subsys_pcc_结构体.md#aed6a31a6ba27aa4eaf05cff984b9c360)
- [clk_div](../device_power_control_model_reference/P050_numaker_scc_subsys_pcc_结构体.md#af24dd5113645830ca2e4a3c9d0b92126)
- [numaker_scc_subsys_pcc_rate](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [clk_modidx_real](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md#a792d0898930c44509f9be2daaf00ba97)
- [clk_src_idx](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md#a8e32abe756e48ba9836d2498651e4b48)
- [clk_src_rate](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md#a14bfb22faf2ac674a3769242de557bd6)
- [clk_div_value](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md#a20d5cc4ed27b98c995ddaf89a6b7938f)
- [clk_div_value_max](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md#ac1368bffb5781c37662535ea7a11b3fb)
- [clk_mod_rate](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md#af826904ecf107d6e2a027832922afbb1)
- [numaker_scc_subsys](../device_power_control_model_reference/P049_numaker_scc_subsys_结构体.md)
- [subsys_id](../device_power_control_model_reference/P049_numaker_scc_subsys_结构体.md#af8e2099977ecba2c53808fe8db4e041a)
- [pcc](../device_power_control_model_reference/P049_numaker_scc_subsys_结构体.md#af8e8bc8bd9236ed245d56ef57b6e9082)
- [numaker_scc_subsys_rate](../device_power_control_model_reference/P052_numaker_scc_subsys_rate_结构体.md)
- [pcc](../device_power_control_model_reference/P052_numaker_scc_subsys_rate_结构体.md#a159486917a5c695f66edebb4749cd1d7)
- [numaker_scc_subsys_pcc_rate::clk_src_rate](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md#a14bfb22faf2ac674a3769242de557bd6)
- [numaker_scc_subsys_pcc_rate::clk_div_value](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md#a20d5cc4ed27b98c995ddaf89a6b7938f)
- [numaker_scc_subsys_pcc_rate::clk_modidx_real](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md#a792d0898930c44509f9be2daaf00ba97)
- [numaker_scc_subsys_pcc_rate::clk_src_idx](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md#a8e32abe756e48ba9836d2498651e4b48)
- [numaker_scc_subsys_pcc_rate::clk_div_value_max](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md#ac1368bffb5781c37662535ea7a11b3fb)
- [numaker_scc_subsys_pcc_rate::clk_mod_rate](../device_power_control_model_reference/P051_numaker_scc_subsys_pcc_rate_结构体.md#af826904ecf107d6e2a027832922afbb1)
- [numaker_scc_subsys_pcc::clk_modidx](../device_power_control_model_reference/P050_numaker_scc_subsys_pcc_结构体.md#a4ebf5a91a803cd92f10d25fcdd0c0eeb)
- [numaker_scc_subsys_pcc::clk_src](../device_power_control_model_reference/P050_numaker_scc_subsys_pcc_结构体.md#aed6a31a6ba27aa4eaf05cff984b9c360)
- [numaker_scc_subsys_pcc::clk_div](../device_power_control_model_reference/P050_numaker_scc_subsys_pcc_结构体.md#af24dd5113645830ca2e4a3c9d0b92126)
- [numaker_scc_subsys_rate::pcc](../device_power_control_model_reference/P052_numaker_scc_subsys_rate_结构体.md#a159486917a5c695f66edebb4749cd1d7)
- [numaker_scc_subsys::subsys_id](../device_power_control_model_reference/P049_numaker_scc_subsys_结构体.md#af8e2099977ecba2c53808fe8db4e041a)
- [numaker_scc_subsys::pcc](../device_power_control_model_reference/P049_numaker_scc_subsys_结构体.md#af8e8bc8bd9236ed245d56ef57b6e9082)

---

[上一章](P100_clock_control_ifx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P102_clock_control_numicro.h_源码浏览.md)
