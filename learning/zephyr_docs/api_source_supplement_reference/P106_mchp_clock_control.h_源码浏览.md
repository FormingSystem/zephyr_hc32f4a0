---
id: learning.zephyr-docs.api-source-supplement-reference.page-106
title: mchp_clock_control.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__control_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第106章\_mchp\_clock\_control.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__control_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__control_8h.html)。

## 106.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
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
<a id="l00053"></a>
<a id="l00054"></a>
<a id="aclock__control_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amchp__clock__pic32ck__sg__gc_8h_html"></a>
<a id="amchp__clock__pic32cm__jh_8h_html"></a>
<a id="amchp__clock__pic32cm__pl_8h_html"></a>
<a id="amchp__clock__pic32cm__sg__gc_8h_html"></a>
<a id="amchp__clock__pic32cz__ca_8h_html"></a>
<a id="amchp__clock__sam__d5x__e5x_8h_html"></a>

```c
/*
 * Copyright (c) 2025-2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_CONTROL_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_CONTROL_H_


#include <zephyr/kernel.h>
#include <zephyr/drivers/clock_control.h>

#if CONFIG_CLOCK_CONTROL_MCHP_SAM_D5X_E5X
#include <zephyr/drivers/clock_control/mchp_clock_sam_d5x_e5x.h>
#endif /* CLOCK_CONTROL_MCHP_SAM_D5X_E5X */

#if CONFIG_CLOCK_CONTROL_MCHP_PIC32CK_SG_GC
#include <zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h>
#endif /* CONFIG_CLOCK_CONTROL_MCHP_PIC32CK_SG_GC */

#if CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_JH
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h>
#endif /* CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_JH */

#if CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_PL
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_pl.h>
#endif /* CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_PL */

#if CONFIG_CLOCK_CONTROL_MCHP_PIC32CZ_CA
#include <zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h>
#endif /* CONFIG_CLOCK_CONTROL_MCHP_PIC32CZ_CA */

#if CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_SG_GC
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h>
#endif /* CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_SG_GC */


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_CONTROL_H_ */
```

## 106.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025-2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 30 行

条件编译标记：`CLOCK_CONTROL_MCHP_SAM_D5X_E5X`。

### 注释 3：原第 34 行

条件编译配置（Configuration）标记：`CONFIG_CLOCK_CONTROL_MCHP_PIC32CK_SG_GC`。

### 注释 4：原第 38 行

条件编译配置（Configuration）标记：`CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_JH`。

### 注释 5：原第 42 行

条件编译配置（Configuration）标记：`CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_PL`。

### 注释 6：原第 46 行

条件编译配置（Configuration）标记：`CONFIG_CLOCK_CONTROL_MCHP_PIC32CZ_CA`。

### 注释 7：原第 50 行

条件编译配置（Configuration）标记：`CONFIG_CLOCK_CONTROL_MCHP_PIC32CM_SG_GC`。

### 注释 8：原第 54 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_CLOCK_CONTROL_H_`。

## 106.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__control_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [zephyr/drivers/clock_control/mchp_clock_sam_d5x_e5x.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__sam__d5x__e5x_8h.html)
- [zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html)
- [zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h.html)
- [zephyr/drivers/clock_control/mchp_clock_pic32cm_pl.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__pl_8h.html)
- [zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h.html)
- [zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mchp_clock_pic32ck_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h.html)
- [mchp_clock_pic32cm_jh.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h.html)
- [mchp_clock_pic32cm_pl.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__pl_8h.html)
- [mchp_clock_pic32cm_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h.html)
- [mchp_clock_pic32cz_ca.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h.html)
- [mchp_clock_sam_d5x_e5x.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__sam__d5x__e5x_8h.html)

---

[上一章](P105_mchp-xec-dmac.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P107_mchp_mss_reset.h_源码浏览.md)
