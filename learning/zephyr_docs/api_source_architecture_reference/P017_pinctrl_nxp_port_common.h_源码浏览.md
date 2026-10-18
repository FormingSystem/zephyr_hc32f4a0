---
id: learning.zephyr-docs.api-source-architecture-reference.page-17
title: pinctrl_nxp_port_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__nxp__port__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_pinctrl\_nxp\_port\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__nxp__port__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P303_zephyr__drivers__pinctrl__pinctrl_nxp_port_common.h_文件参考.md)。

## 17.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
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
<a id="l00043"></a>
<a id="l00044"></a>
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
<a id="l00077"></a>
<a id="l00078"></a>
<a id="adevicetree_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="apinctrl__rcar__common_8h_html_a022eeb1c811e7ef94d3a7a99cbda0e2d"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright 2022, 2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/*
 * @file
 * NXP PORT SOC specific helpers for pinctrl driver
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_NXP_PORT_COMMON_H_
#define ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_NXP_PORT_COMMON_H_


#include <zephyr/devicetree.h>
#include <zephyr/types.h>

/* Include SOC headers, so we get definitions for PCR bitmasks */
#include <soc.h>

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Some PORT IP instantiations lack certain features, include input buffers,
 * open drain, and slew rate. If masks aren't defined for these bitfields,
 * define them to have no effect
 */
#ifndef PORT_PCR_IBE_MASK /* Input buffer enable */
#define PORT_PCR_IBE_MASK 0x0
#define PORT_PCR_IBE(x) 0x0
#endif

#ifndef PORT_PCR_SRE_MASK /* Slew rate */
#define PORT_PCR_SRE_MASK 0x0
#define PORT_PCR_SRE(x) 0x0
#endif

#ifndef PORT_PCR_ODE_MASK /* Open drain */
#define PORT_PCR_ODE_MASK 0x0
#define PORT_PCR_ODE(x) 0x0
#endif


typedef uint32_t pinctrl_soc_pin_t;

#define Z_PINCTRL_NXP_PORT_PINCFG(node_id)                                                         \
        (PORT_PCR_DSE(DT_ENUM_IDX(node_id, drive_strength)) |                                      \
         PORT_PCR_PS(DT_PROP(node_id, bias_pull_up)) |                                             \
         PORT_PCR_PE(DT_PROP(node_id, bias_pull_up)) |                                             \
         PORT_PCR_PE(DT_PROP(node_id, bias_pull_down)) |                                           \
         PORT_PCR_ODE(DT_PROP(node_id, drive_open_drain)) |                                        \
         PORT_PCR_SRE(DT_ENUM_IDX(node_id, slew_rate)) |                                           \
         PORT_PCR_IBE(DT_PROP(node_id, input_enable)) |                                            \
         PORT_PCR_PFE(DT_PROP(node_id, nxp_passive_filter)))

#define Z_PINCTRL_NXP_PORT_PCR_MASK                                                                \
        (PORT_PCR_MUX_MASK | PORT_PCR_DSE_MASK | PORT_PCR_ODE_MASK | PORT_PCR_PFE_MASK |           \
         PORT_PCR_IBE_MASK | PORT_PCR_SRE_MASK | PORT_PCR_PE_MASK | PORT_PCR_PS_MASK)

#define Z_PINCTRL_STATE_PIN_INIT(group, pin_prop, idx)                                             \
        DT_PROP_BY_IDX(group, pin_prop, idx) | Z_PINCTRL_NXP_PORT_PINCFG(group),

#define Z_PINCTRL_STATE_PINS_INIT(node_id, prop)                                                   \
        {DT_FOREACH_CHILD_VARGS(DT_PHANDLE(node_id, prop), DT_FOREACH_PROP_ELEM, pinmux,           \
                                Z_PINCTRL_STATE_PIN_INIT)};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_NXP_PORT_COMMON_H_ */
```

## 17.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022, 2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 7 行

文件说明（`@file`）：NXP PORT 片上系统（SoC）专用的引脚控制驱动辅助工具（Pinctrl Driver Helpers）。

### 注释 3：原第 21 行

包含 SoC 头文件（Headers），以取得引脚控制寄存器位掩码（PCR Bitmasks）的定义。

### 注释 4：原第 28 行

某些 PORT IP 实例（Instantiations）缺少输入缓冲器（Input Buffers）、开漏（Open Drain）和转换速率（Slew Rate）等特性。如果这些位域没有定义掩码（Masks），则将其定义为不产生作用的值。

### 注释 5：原第 33 行

输入缓冲器使能（Input Buffer Enable）。

### 注释 6：原第 38 行

转换速率（Slew Rate）。

### 注释 7：原第 43 行

开漏（Open Drain）。

### 注释 8：原第 78 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_NXP_PORT_COMMON_H_`。

## 17.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P303_zephyr__drivers__pinctrl__pinctrl_nxp_port_common.h_文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pinctrl_soc_pin_t](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h.html#a022eeb1c811e7ef94d3a7a99cbda0e2d)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)

---

[上一章](P016_nxp_mc_cgm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P018_sam0_eic.h_源码浏览.md)
