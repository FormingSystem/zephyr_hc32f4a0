---
id: learning.zephyr-docs.api-source-reference.page-505
title: mchp_sam_pmc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__pmc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第505章\_mchp\_sam\_pmc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__pmc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__pmc_8h.html)。

## 505.1\_原始可见代码（Source Code）

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
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="aclock__control_8h_html"></a>
<a id="amicrochip__sam__pmc_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructsam__clk__cfg_html"></a>
<a id="astructsam__clk__cfg_html_a267eec7843a416198edf26c31db252e7"></a>
<a id="astructsam__clk__cfg_html_af393258d1cf2fc592970658896075b17"></a>
<a id="astructsam__pmc__cfg_html"></a>
<a id="astructsam__pmc__cfg_html_a0fc5ba6ce43a1f7b91d854ace83f59df"></a>
<a id="astructsam__pmc__cfg_html_a149d058d1170af8eb75628dfd6b9cc92"></a>
<a id="astructsam__pmc__cfg_html_a3029662f9fa5ca96c142a9564c44f4d2"></a>
<a id="astructsam__pmc__cfg_html_a8459cfb8ca7a99416e0c2e5e9a680481"></a>
<a id="astructsam__pmc__cfg_html_aa2584519cb128e96715a6a01140f609c"></a>
<a id="astructsam__pmc__cfg_html_abd4cbbd2082fe579bc6edd3d4548f390"></a>
<a id="astructsam__pmc__data_html"></a>
<a id="astructsam__pmc__data_html_abdab335def8be1593fdac72a5092a77d"></a>
<a id="astructsam__sckc__config_html"></a>
<a id="astructsam__sckc__config_html_a332b32859d73b961eb0f32f376390824"></a>
<a id="astructsam__sckc__config_html_a9a634b76cc127423dbfcb2b86435eb96"></a>

```c
/*
 * Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_SAM_PMC_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_SAM_PMC_H_

#include <soc.h>
#include <zephyr/drivers/clock_control.h>
#include <zephyr/dt-bindings/clock/microchip_sam_pmc.h>


struct sam_sckc_config {
        uint32_t crystal_osc: 1;
        uint32_t reserved: 31;
};

struct sam_clk_cfg {
        uint32_t clock_type;
        uint32_t clock_id;
};

struct sam_pmc_cfg {
        uint32_t *const reg;
        const struct device *td_slck;
        const struct device *md_slck;
        const struct device *main_xtal;
        const struct sam_sckc_config td_slck_cfg;
        const struct sam_sckc_config md_slck_cfg;
};

struct sam_pmc_data {
        struct pmc_data *pmc;
};

#define SAM_DT_CLOCK_PMC_CFG(clock, node_id) {                                          \
                .clock_type = DT_CLOCKS_CELL_BY_IDX(node_id,                            \
                                                    clock,                              \
                                                    clock_type),                        \
                .clock_id = DT_CLOCKS_CELL_BY_IDX(node_id,                              \
                                                  clock,                                \
                                                  peripheral_id)                        \
        }

#define SAM_DT_INST_CLOCK_PMC_CFG(inst) SAM_DT_CLOCK_PMC_CFG(0, DT_DRV_INST(inst))

#define SAM_DT_CLOCKS_PMC_CFG(node_id) {                                                \
                LISTIFY(DT_NUM_CLOCKS(node_id),                                         \
                SAM_DT_CLOCK_PMC_CFG, (,), node_id)                                     \
        }

#define SAM_DT_INST_CLOCKS_PMC_CFG(inst) SAM_DT_CLOCKS_PMC_CFG(DT_DRV_INST(inst))


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_SAM_PMC_H_ */
```

## 505.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：(C) 2025 Microchip Technology Inc. and its subsidiaries。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 94 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_SAM_PMC_H_`。

## 505.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__pmc_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [zephyr/dt-bindings/clock/microchip_sam_pmc.h](https://docs.zephyrproject.org/latest/doxygen/html/microchip__sam__pmc_8h.html)
- [sam_sckc_config](../device_power_control_model_reference/P081_sam_sckc_config_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [crystal_osc](../device_power_control_model_reference/P081_sam_sckc_config_结构体.md#a332b32859d73b961eb0f32f376390824)
- [reserved](../device_power_control_model_reference/P081_sam_sckc_config_结构体.md#a9a634b76cc127423dbfcb2b86435eb96)
- [sam_clk_cfg](../device_power_control_model_reference/P078_sam_clk_cfg_结构体.md)
- [clock_type](../device_power_control_model_reference/P078_sam_clk_cfg_结构体.md#a267eec7843a416198edf26c31db252e7)
- [clock_id](../device_power_control_model_reference/P078_sam_clk_cfg_结构体.md#af393258d1cf2fc592970658896075b17)
- [sam_pmc_cfg](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md)
- [reg](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md#aa2584519cb128e96715a6a01140f609c)
- [device](../device_reference/P002_设备对象结构.md)
- [td_slck](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md#a0fc5ba6ce43a1f7b91d854ace83f59df)
- [md_slck](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md#abd4cbbd2082fe579bc6edd3d4548f390)
- [main_xtal](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md#a8459cfb8ca7a99416e0c2e5e9a680481)
- [td_slck_cfg](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md#a3029662f9fa5ca96c142a9564c44f4d2)
- [md_slck_cfg](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md#a149d058d1170af8eb75628dfd6b9cc92)
- [sam_pmc_data](../device_power_control_model_reference/P080_sam_pmc_data_结构体.md)
- [pmc](../device_power_control_model_reference/P080_sam_pmc_data_结构体.md#abdab335def8be1593fdac72a5092a77d)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [microchip_sam_pmc.h](https://docs.zephyrproject.org/latest/doxygen/html/microchip__sam__pmc_8h.html)
- [sam_clk_cfg::clock_type](../device_power_control_model_reference/P078_sam_clk_cfg_结构体.md#a267eec7843a416198edf26c31db252e7)
- [sam_clk_cfg::clock_id](../device_power_control_model_reference/P078_sam_clk_cfg_结构体.md#af393258d1cf2fc592970658896075b17)
- [sam_pmc_cfg::td_slck](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md#a0fc5ba6ce43a1f7b91d854ace83f59df)
- [sam_pmc_cfg::md_slck_cfg](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md#a149d058d1170af8eb75628dfd6b9cc92)
- [sam_pmc_cfg::td_slck_cfg](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md#a3029662f9fa5ca96c142a9564c44f4d2)
- [sam_pmc_cfg::main_xtal](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md#a8459cfb8ca7a99416e0c2e5e9a680481)
- [sam_pmc_cfg::reg](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md#aa2584519cb128e96715a6a01140f609c)
- [sam_pmc_cfg::md_slck](../device_power_control_model_reference/P079_sam_pmc_cfg_结构体.md#abd4cbbd2082fe579bc6edd3d4548f390)
- [sam_pmc_data::pmc](../device_power_control_model_reference/P080_sam_pmc_data_结构体.md#abdab335def8be1593fdac72a5092a77d)
- [sam_sckc_config::crystal_osc](../device_power_control_model_reference/P081_sam_sckc_config_结构体.md#a332b32859d73b961eb0f32f376390824)
- [sam_sckc_config::reserved](../device_power_control_model_reference/P081_sam_sckc_config_结构体.md#a9a634b76cc127423dbfcb2b86435eb96)

---

[上一章](P504_mchp_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P506_mchp_xec_espi.h_源码浏览.md)
