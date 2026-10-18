---
id: learning.zephyr-docs.hardware.dacext-7
title: Infineon连续时间DAC常量源码
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第835章\_Infineon连续时间DAC常量源码

原文：[infineon-autanalog-ctdac_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctdac_8h_source.html)。读取日期：2026-10-13，`latest`。

文件路径为 `zephyr/dt-bindings/dac/infineon-autanalog-ctdac.h`。

本页保留Infineon自主模拟（Autonomous Analog，AutAnalog）连续时间数模转换器（Continuous-Time Digital-to-Analog Converter，CTDAC）的设备树常量（Devicetree Constants）声明。文件文档入口对应[常量中文参考](P820_Infineon连续时间DAC设备树常量.md)。

## 835.1\_常量分组

48个常量按参考缓冲器功耗（Reference Buffer Power）、输出缓冲器功耗（Output Buffer Power）、参考电压源（Vref Source）、拓扑（Topology）、波形工作模式（Waveform Operating Mode）、步长选择器（Step Selector）、状态选择器（Status Selector）与限值条件（Limit Condition）分组。完整数值与逐项中文解释见常量参考页；此处保留所有原始声明。

文件版权注释注明权利人为Infineon Technologies AG或其关联公司，保留所有权利；授权标记为Apache-2.0。头文件保护宏（Header Guard）、版权和许可证标记全部保留。

## 835.2\_网页源码

以下保留Doxygen源码页实际展示的代码，剔除网页行号并清理行尾空白。网页隐藏的文档注释由对应参考页提供，本节没有自行补写或修改代码。

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DAC_INFINEON_AUTANALOG_CTDAC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DAC_INFINEON_AUTANALOG_CTDAC_H_

#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_OFF             0
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_ULTRA_LOW       1
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_ULTRA_LOW_RAIL  2
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_LOW_RAIL        4
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_MEDIUM_RAIL     6
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_HIGH            7
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_HIGH_RAIL       8
#define IFX_AUTANALOG_CTDAC_REF_BUF_PWR_ULTRA_HIGH_RAIL 10

#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_OFF             0
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_ULTRA_LOW       1
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_ULTRA_LOW_RAIL  2
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_LOW_RAIL        4
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_MEDIUM_RAIL     6
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_HIGH_RAIL       8
#define IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_ULTRA_HIGH_RAIL 10

#define IFX_AUTANALOG_CTDAC_VREF_VDDA     0x100
#define IFX_AUTANALOG_CTDAC_VREF_VBGR     0
#define IFX_AUTANALOG_CTDAC_VREF_CTB0_OA0 1
#define IFX_AUTANALOG_CTDAC_VREF_CTB0_OA1 2
#define IFX_AUTANALOG_CTDAC_VREF_CTB1_OA0 3
#define IFX_AUTANALOG_CTDAC_VREF_CTB1_OA1 4
#define IFX_AUTANALOG_CTDAC_VREF_PRB_OUT0 6
#define IFX_AUTANALOG_CTDAC_VREF_PRB_OUT1 7

#define IFX_AUTANALOG_CTDAC_TOPO_DIRECT            0
#define IFX_AUTANALOG_CTDAC_TOPO_DIRECT_TRACK_CAP  1
#define IFX_AUTANALOG_CTDAC_TOPO_DIRECT_TRACK_HOLD 2
#define IFX_AUTANALOG_CTDAC_TOPO_BUFFERED_INTERNAL 3
#define IFX_AUTANALOG_CTDAC_TOPO_BUFFERED_EXTERNAL 4

#define IFX_AUTANALOG_CTDAC_OP_OS_ONE_QUAD    0
#define IFX_AUTANALOG_CTDAC_OP_OS_TWO_QUAD    1
#define IFX_AUTANALOG_CTDAC_OP_OS_FOUR_QUAD   2
#define IFX_AUTANALOG_CTDAC_OP_CONT_ONE_QUAD  3
#define IFX_AUTANALOG_CTDAC_OP_CONT_TWO_QUAD  4
#define IFX_AUTANALOG_CTDAC_OP_CONT_FOUR_QUAD 5
#define IFX_AUTANALOG_CTDAC_OP_ADDR           6
#define IFX_AUTANALOG_CTDAC_OP_DATA           7

#define IFX_AUTANALOG_CTDAC_STEP_SEL_DISABLED 0
#define IFX_AUTANALOG_CTDAC_STEP_SEL_0        1
#define IFX_AUTANALOG_CTDAC_STEP_SEL_1        2
#define IFX_AUTANALOG_CTDAC_STEP_SEL_2        3

#define IFX_AUTANALOG_CTDAC_STAT_SEL_DISABLED 0
#define IFX_AUTANALOG_CTDAC_STAT_SEL_0        1
#define IFX_AUTANALOG_CTDAC_STAT_SEL_1        2
#define IFX_AUTANALOG_CTDAC_STAT_SEL_2        3

#define IFX_AUTANALOG_CTDAC_LIMIT_BELOW   0
#define IFX_AUTANALOG_CTDAC_LIMIT_INSIDE  1
#define IFX_AUTANALOG_CTDAC_LIMIT_ABOVE   2
#define IFX_AUTANALOG_CTDAC_LIMIT_OUTSIDE 3

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DAC_INFINEON_AUTANALOG_CTDAC_H_ */
```

---

[上一章：DACx0508设备树常量源码](P834_DACx0508设备树常量源码.md) · [下一章：SiliconLabsVDAC常量源码](P836_SiliconLabsVDAC常量源码.md) · [返回大纲](大纲.md)
