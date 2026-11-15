---
id: learning.zephyr-docs.api-source-reference.page-150
title: renesas_cpg_mssr.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2renesas__cpg__mssr_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第150章\_renesas\_cpg\_mssr.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2renesas__cpg__mssr_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2renesas__cpg__mssr_8h.html)。

## 150.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="aclock__control_8h_html"></a>
<a id="adt-bindings_2clock_2renesas__cpg__mssr_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructrcar__cpg__clk_html"></a>
<a id="astructrcar__cpg__clk_html_a126cf65226ac7e3521c724d4c9d7b3a4"></a>
<a id="astructrcar__cpg__clk_html_a84f173b12e610177932cf58d85659f0e"></a>
<a id="astructrcar__cpg__clk_html_aff97932d122b50e3d7546adfe2fc29f5"></a>

```c
/*
 * Copyright (c) 2016 Open-RnD Sp. z o.o.
 * Copyright (c) 2016 BayLibre, SAS
 * Copyright (c) 2017 Linaro Limited.
 * Copyright (c) 2017 RnDity Sp. z o.o.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_CPG_MSSR_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_CPG_MSSR_H_

#include <zephyr/drivers/clock_control.h>
#include <zephyr/dt-bindings/clock/renesas_cpg_mssr.h>


struct rcar_cpg_clk {
        uint32_t domain;
        uint32_t module;
        uint32_t rate;
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_CPG_MSSR_H_ */
```

## 150.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Open-RnD Sp. z o.o.。

版权（Copyright）：© 2016 BayLibre, SAS。

版权（Copyright）：© 2017 Linaro Limited.。

版权（Copyright）：© 2017 RnDity Sp. z o.o.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 37 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_CPG_MSSR_H_`。

## 150.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2renesas__cpg__mssr_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [zephyr/dt-bindings/clock/renesas_cpg_mssr.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2clock_2renesas__cpg__mssr_8h.html)
- [rcar_cpg_clk](../device_power_control_model_reference/P071_rcar_cpg_clk_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [domain](../device_power_control_model_reference/P071_rcar_cpg_clk_结构体.md#a126cf65226ac7e3521c724d4c9d7b3a4)
- [module](../device_power_control_model_reference/P071_rcar_cpg_clk_结构体.md#aff97932d122b50e3d7546adfe2fc29f5)
- [rate](../device_power_control_model_reference/P071_rcar_cpg_clk_结构体.md#a84f173b12e610177932cf58d85659f0e)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [renesas_cpg_mssr.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2clock_2renesas__cpg__mssr_8h.html)
- [rcar_cpg_clk::domain](../device_power_control_model_reference/P071_rcar_cpg_clk_结构体.md#a126cf65226ac7e3521c724d4c9d7b3a4)
- [rcar_cpg_clk::rate](../device_power_control_model_reference/P071_rcar_cpg_clk_结构体.md#a84f173b12e610177932cf58d85659f0e)
- [rcar_cpg_clk::module](../device_power_control_model_reference/P071_rcar_cpg_clk_结构体.md#aff97932d122b50e3d7546adfe2fc29f5)

---

[上一章](P149_atmel_sam_pmc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P151_console.h_源码浏览.md)
