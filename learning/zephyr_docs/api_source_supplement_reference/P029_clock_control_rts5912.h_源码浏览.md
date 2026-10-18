---
id: learning.zephyr-docs.api-source-supplement-reference.page-29
title: clock_control_rts5912.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__rts5912_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_clock\_control\_rts5912.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__rts5912_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__rts5912_8h.html)。

## 29.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00024"></a>
<a id="foldopen00026"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructrts5912__sccon__subsys_html"></a>
<a id="astructrts5912__sccon__subsys_html_a1657eff3e6d6846e87e6d844f0bd102b"></a>
<a id="astructrts5912__sccon__subsys_html_a28a8e0a3078f7a724948ecec91760382"></a>
<a id="astructrts5912__sccon__subsys_html_a4743dd2a82bce16d93eb3caf60615909"></a>
<a id="astructrts5912__sccon__subsys_html_aeadd64cc7eb73d39d5f7119c2b86365e"></a>

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright (c) 2024 Realtek Semiconductor Corporation, SIBG-SD7
 * Author: Lin Yu-Cheng <lin_yu_cheng@realtek.com>
 */


#include <stdint.h>

#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_RTS5912_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_RTS5912_H_


struct rts5912_sccon_subsys {
        uint32_t clk_grp;
        uint32_t clk_idx;
        uint32_t clk_src;
        uint32_t clk_div;
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_RTS5912_H_ */
```

## 29.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

版权（Copyright）：© 2024 Realtek Semiconductor Corporation, SIBG-SD7。

作者（Author）：Lin Yu-Cheng <lin_yu_cheng@realtek.com>。

### 注释 2：原第 35 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_RTS5912_H_`。

## 29.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__rts5912_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [rts5912_sccon_subsys](../device_power_control_model_reference/P076_rts5912_sccon_subsys_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [clk_grp](../device_power_control_model_reference/P076_rts5912_sccon_subsys_结构体.md#aeadd64cc7eb73d39d5f7119c2b86365e)
- [clk_idx](../device_power_control_model_reference/P076_rts5912_sccon_subsys_结构体.md#a28a8e0a3078f7a724948ecec91760382)
- [clk_src](../device_power_control_model_reference/P076_rts5912_sccon_subsys_结构体.md#a4743dd2a82bce16d93eb3caf60615909)
- [clk_div](../device_power_control_model_reference/P076_rts5912_sccon_subsys_结构体.md#a1657eff3e6d6846e87e6d844f0bd102b)
- [rts5912_sccon_subsys::clk_div](../device_power_control_model_reference/P076_rts5912_sccon_subsys_结构体.md#a1657eff3e6d6846e87e6d844f0bd102b)
- [rts5912_sccon_subsys::clk_idx](../device_power_control_model_reference/P076_rts5912_sccon_subsys_结构体.md#a28a8e0a3078f7a724948ecec91760382)
- [rts5912_sccon_subsys::clk_src](../device_power_control_model_reference/P076_rts5912_sccon_subsys_结构体.md#a4743dd2a82bce16d93eb3caf60615909)
- [rts5912_sccon_subsys::clk_grp](../device_power_control_model_reference/P076_rts5912_sccon_subsys_结构体.md#aeadd64cc7eb73d39d5f7119c2b86365e)

---

[上一章](P028_kernel.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P030_clock_control_ti_cdce9xx.h_源码浏览.md)
