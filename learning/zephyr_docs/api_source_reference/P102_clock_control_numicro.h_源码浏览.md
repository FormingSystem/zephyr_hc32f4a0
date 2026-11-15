---
id: learning.zephyr-docs.api-source-reference.page-102
title: clock_control_numicro.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numicro_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第102章\_clock\_control\_numicro.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numicro_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numicro_8h.html)。

## 102.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00053"></a>
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
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructnumicro__scc__subsys__pcc_html"></a>
<a id="astructnumicro__scc__subsys__pcc_html_a18db15a6377bba17e05a57444828c4cd"></a>
<a id="astructnumicro__scc__subsys__pcc_html_a55df199b041ef093c560f29265782b93"></a>
<a id="astructnumicro__scc__subsys__pcc_html_ab762fc4005619ccefc6cfe7da5c8c158"></a>
<a id="astructnumicro__scc__subsys_html"></a>
<a id="astructnumicro__scc__subsys_html_a2bc16b33c42e4f3b8997a8bd50be7657"></a>
<a id="astructnumicro__scc__subsys_html_a58dd936369388d486bb93cc9c0d5eba7"></a>

```c
/*
 * Copyright (c) 2026 Fiona Behrens
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <stdint.h>


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_NUMICRO_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_NUMICRO_H_


#define NUMICRO_SCC_SUBSYS_ID_PCC 1

struct numicro_scc_subsys_pcc {
        uint32_t clk_mod;
        uint32_t clk_src;
        uint32_t clk_div;
};

struct numicro_scc_subsys {
        uint32_t subsys_id;

        union {
                struct numicro_scc_subsys_pcc pcc;
        };
};

#define DT_NUMICRO_CLOCK_PCC_SUBSYSTEM(dev)                                                        \
        {                                                                                          \
                .subsys_id = NUMICRO_SCC_SUBSYS_ID_PCC,                                            \
                .pcc =                                                                             \
                        {                                                                          \
                                .clk_mod = DT_CLOCKS_CELL(dev, clock_module_index),                \
                                .clk_src = DT_CLOCKS_CELL(dev, clock_source),                      \
                                .clk_div = DT_CLOCKS_CELL(dev, clock_divider),                     \
                        },                                                                         \
        }

#define DT_NUMICRO_CLOCK_PCC_SUBSYSTEM_INST(inst) DT_NUMICRO_CLOCK_PCC_SUBSYSTEM(DT_DRV_INST(inst))


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_NUMICRO_H_ */
```

## 102.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Fiona Behrens。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 69 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_NUMICRO_H_`。

## 102.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numicro_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [numicro_scc_subsys_pcc](../device_power_control_model_reference/P054_numicro_scc_subsys_pcc_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [clk_mod](../device_power_control_model_reference/P054_numicro_scc_subsys_pcc_结构体.md#ab762fc4005619ccefc6cfe7da5c8c158)
- [clk_src](../device_power_control_model_reference/P054_numicro_scc_subsys_pcc_结构体.md#a18db15a6377bba17e05a57444828c4cd)
- [clk_div](../device_power_control_model_reference/P054_numicro_scc_subsys_pcc_结构体.md#a55df199b041ef093c560f29265782b93)
- [numicro_scc_subsys](../device_power_control_model_reference/P053_numicro_scc_subsys_结构体.md)
- [subsys_id](../device_power_control_model_reference/P053_numicro_scc_subsys_结构体.md#a58dd936369388d486bb93cc9c0d5eba7)
- [pcc](../device_power_control_model_reference/P053_numicro_scc_subsys_结构体.md#a2bc16b33c42e4f3b8997a8bd50be7657)
- [numicro_scc_subsys_pcc::clk_src](../device_power_control_model_reference/P054_numicro_scc_subsys_pcc_结构体.md#a18db15a6377bba17e05a57444828c4cd)
- [numicro_scc_subsys_pcc::clk_div](../device_power_control_model_reference/P054_numicro_scc_subsys_pcc_结构体.md#a55df199b041ef093c560f29265782b93)
- [numicro_scc_subsys_pcc::clk_mod](../device_power_control_model_reference/P054_numicro_scc_subsys_pcc_结构体.md#ab762fc4005619ccefc6cfe7da5c8c158)
- [numicro_scc_subsys::pcc](../device_power_control_model_reference/P053_numicro_scc_subsys_结构体.md#a2bc16b33c42e4f3b8997a8bd50be7657)
- [numicro_scc_subsys::subsys_id](../device_power_control_model_reference/P053_numicro_scc_subsys_结构体.md#a58dd936369388d486bb93cc9c0d5eba7)

---

[上一章](P101_clock_control_numaker.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P103_clock_control_rpi_pico.h_源码浏览.md)
