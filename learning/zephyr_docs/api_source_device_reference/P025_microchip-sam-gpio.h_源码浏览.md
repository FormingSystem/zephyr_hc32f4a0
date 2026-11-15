---
id: learning.zephyr-docs.api-source-device-reference.page-25
title: microchip-sam-gpio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/microchip-sam-gpio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_microchip-sam-gpio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/microchip-sam-gpio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P222_zephyr__dt-bindings__gpio__microchip-sam-gpio.h_文件参考.md)。

## 25.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
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

```c
/*
 * Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_MICROCHIP_SAM_GPIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_MICROCHIP_SAM_GPIO_H_

/*
 * By default the gpio driver will enable slew rate control for
 * each GPIO being used.
 * Use this flag to disable the enable operation
 */
#define SAM_GPIO_DIS_SLEWRATE           (1U << 8)
/*
 * With this flag, IFEN and IFSCEN will be enabled simultaneously
 */
#define SAM_GPIO_DEBOUNCE               (1U << 9)
/*
 * The Schmitt Trigger is enabled after chip reset
 * Use this flag to disable it
 */
#define SAM_GPIO_DIS_SCHMIT             (1U << 10)

/*
 * Use these flags to select the drive strength
 * Otherwise the SAM_GPIO_DRVSTR_DEFAULT will be used
 */
#define SAM_GPIO_DRVSTR_POS             (11U)
#define SAM_GPIO_DRVSTR_MASK            (0x3U << SAM_GPIO_DRVSTR_POS)
#define SAM_GPIO_DRVSTR_DEFAULT         (0U << SAM_GPIO_DRVSTR_POS)
#define SAM_GPIO_DRVSTR_LOW             (1U << SAM_GPIO_DRVSTR_POS)
#define SAM_GPIO_DRVSTR_MED             (2U << SAM_GPIO_DRVSTR_POS)
#define SAM_GPIO_DRVSTR_HI              (3U << SAM_GPIO_DRVSTR_POS)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_MICROCHIP_SAM_GPIO_H_ */
```

## 25.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：(C) 2025 Microchip Technology Inc. and its subsidiaries。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

默认情况下，GPIO 驱动会为每个正在使用的 GPIO 启用转换速率控制（Slew Rate Control）。使用此标志（Flag）可禁止该启用操作。

### 注释 3：原第 17 行

使用此标志（Flag）时，将同时启用 `IFEN` 和 `IFSCEN`。

### 注释 4：原第 21 行

施密特触发器（Schmitt Trigger）在芯片复位后处于启用状态。使用此标志（Flag）可禁用它。

### 注释 5：原第 27 行

使用这些标志（Flags）选择驱动强度（Drive Strength）；否则使用 `SAM_GPIO_DRVSTR_DEFAULT`。

### 注释 6：原第 38 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_MICROCHIP_SAM_GPIO_H_`。

## 25.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P222_zephyr__dt-bindings__gpio__microchip-sam-gpio.h_文件参考.md)

---

[上一章](P024_lpc84x-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P026_net_compat.h_源码浏览.md)
