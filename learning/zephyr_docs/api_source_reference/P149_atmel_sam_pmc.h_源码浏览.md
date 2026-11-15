---
id: learning.zephyr-docs.api-source-reference.page-149
title: atmel_sam_pmc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2atmel__sam__pmc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第149章\_atmel\_sam\_pmc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2atmel__sam__pmc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2atmel__sam__pmc_8h.html)。

## 149.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="l00027"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="aclock__control_8h_html"></a>
<a id="adt-bindings_2clock_2atmel__sam__pmc_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructatmel__sam__pmc__config_html"></a>
<a id="astructatmel__sam__pmc__config_html_a8e2bbec7dd455159da3f469c6fb45635"></a>
<a id="astructatmel__sam__pmc__config_html_aab47279eb62b0d9fb6e097a935f09edd"></a>

```c
/*
 * Copyright (c) 2023 Gerson Fernando Budke <nandojve@gmail.com
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ATMEL_SAM_PMC_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ATMEL_SAM_PMC_H_

#include <zephyr/drivers/clock_control.h>
#include <zephyr/dt-bindings/clock/atmel_sam_pmc.h>


#define SAM_DT_PMC_CONTROLLER DEVICE_DT_GET(DT_NODELABEL(pmc))

struct atmel_sam_pmc_config {
        uint32_t clock_type;
        uint32_t peripheral_id;
};

#define SAM_DT_CLOCK_PMC_CFG(clock_id, node_id)                                 \
        {                                                                       \
        .clock_type = DT_CLOCKS_CELL_BY_IDX(node_id, clock_id, clock_type),     \
        .peripheral_id = DT_CLOCKS_CELL_BY_IDX(node_id, clock_id, peripheral_id)\
        }

#define SAM_DT_INST_CLOCK_PMC_CFG(inst) SAM_DT_CLOCK_PMC_CFG(0, DT_DRV_INST(inst))

#define SAM_DT_CLOCKS_PMC_CFG(node_id)                                          \
        {                                                                       \
                LISTIFY(DT_NUM_CLOCKS(node_id),                                 \
                        SAM_DT_CLOCK_PMC_CFG, (,), node_id)                     \
        }

#define SAM_DT_INST_CLOCKS_PMC_CFG(inst)                                        \
        SAM_DT_CLOCKS_PMC_CFG(DT_DRV_INST(inst))


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ATMEL_SAM_PMC_H_ */
```

## 149.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Gerson Fernando Budke <nandojve@gmail.com。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_ATMEL_SAM_PMC_H_`。

## 149.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2atmel__sam__pmc_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [zephyr/dt-bindings/clock/atmel_sam_pmc.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2clock_2atmel__sam__pmc_8h.html)
- [atmel_sam_pmc_config](../driver_model_reference/P015_Atmel_SAM电源管理时钟配置.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [clock_type](../driver_model_reference/P015_Atmel_SAM电源管理时钟配置.md#a8e2bbec7dd455159da3f469c6fb45635)
- [peripheral_id](../driver_model_reference/P015_Atmel_SAM电源管理时钟配置.md#aab47279eb62b0d9fb6e097a935f09edd)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [atmel_sam_pmc.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2clock_2atmel__sam__pmc_8h.html)
- [atmel_sam_pmc_config::clock_type](../driver_model_reference/P015_Atmel_SAM电源管理时钟配置.md#a8e2bbec7dd455159da3f469c6fb45635)
- [atmel_sam_pmc_config::peripheral_id](../driver_model_reference/P015_Atmel_SAM电源管理时钟配置.md#aab47279eb62b0d9fb6e097a935f09edd)

---

[上一章](P148_npm10xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P150_renesas_cpg_mssr.h_源码浏览.md)
