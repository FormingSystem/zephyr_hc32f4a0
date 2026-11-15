---
id: learning.zephyr-docs.api-source-configuration-reference.page-95
title: renesas_rcar_generic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rcar__generic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第95章\_renesas\_rcar\_generic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rcar__generic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rcar__generic_8h.html)。

## 95.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="aclock__control_8h_html"></a>
<a id="adrivers_2clock__control_2renesas__cpg__mssr_8h_html"></a>
<a id="agroup__clock__control__interface_html_gaa7d3935eaaf18902801a7d94859483db"></a>
<a id="agroup__clock__control__renesas__rcar_html_gab6254d94158b3eed9aebe694180731ee"></a>
<a id="astructrcar__cpg__clk_html"></a>

```c
/*
 * Copyright (c) 2026 BayLibre, SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RCAR_GENERIC_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RCAR_GENERIC_H_


/* Gen 5 boards deal with clocks through SCMI. */
#ifdef CONFIG_CLOCK_CONTROL_ARM_SCMI

#include <zephyr/drivers/clock_control.h>

#define RCAR_DT_INST_CLOCKS_CELL_BY_IDX(inst, idx)                                      \
{                                                                                       \
        .subsys = (clock_control_subsys_t)DT_INST_CLOCKS_CELL_BY_IDX(inst, idx, name)   \
}

#define RCAR_CLOCK_SUBSYS(clk) (clk).subsys

struct rcar_generic_clk {
        clock_control_subsys_t subsys;
};

typedef struct rcar_generic_clk rcar_generic_clk_t;

/* Gen 3 and gen 4 boards directly access the clock controller module. */
#else

#include <zephyr/drivers/clock_control/renesas_cpg_mssr.h>

#define RCAR_DT_INST_CLOCKS_CELL_BY_IDX(inst, idx)                      \
{                                                                       \
        .module = DT_INST_CLOCKS_CELL_BY_IDX(inst, idx, module),        \
        .domain = DT_INST_CLOCKS_CELL_BY_IDX(inst, idx, domain)         \
}

#define RCAR_CLOCK_SUBSYS(clk) (clock_control_subsys_t)&(clk)

typedef struct rcar_cpg_clk rcar_generic_clk_t;

#endif /* CONFIG_CLOCK_CONTROL_ARM_SCMI */


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RCAR_GENERIC_H_ */
```

## 95.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 BayLibre, SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 22 行

第 5 代（Gen 5）开发板通过系统控制与管理接口（SCMI）处理时钟。

### 注释 3：原第 53 行

第 3 代和第 4 代（Gen 3 / Gen 4）开发板直接访问时钟控制器模块。

### 注释 4：原第 80 行

条件编译配置（Configuration）标记：`CONFIG_CLOCK_CONTROL_ARM_SCMI`。

### 注释 5：原第 84 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RCAR_GENERIC_H_`。

## 95.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rcar__generic_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)
- [rcar_generic_clk_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__renesas__rcar.html#gab6254d94158b3eed9aebe694180731ee)
- [zephyr/drivers/clock_control/renesas_cpg_mssr.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2renesas__cpg__mssr_8h.html)
- [rcar_cpg_clk](../device_power_control_model_reference/P071_rcar_cpg_clk_结构体.md)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [renesas_cpg_mssr.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2clock__control_2renesas__cpg__mssr_8h.html)

---

[上一章](P094_ra8t1-elc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P096_renesas_rz_pwm.h_源码浏览.md)
