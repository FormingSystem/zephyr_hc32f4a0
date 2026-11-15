---
id: learning.zephyr-docs.timer_reference.litexclock-122
title: LiteX时钟控制完整头文件
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__litex_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第122章\_LiteX时钟控制完整头文件

原文：[clock__control__litex_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__litex_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方网页展示的`zephyr/drivers/clock_control/clock_control_litex.h`完整可见源码。文件用于 LiteX 混合模式时钟管理器（Mixed Mode Clock Manager，MMCM）的时钟控制（Clock Control）。

## 122.1\_源码阅读说明

头文件保护宏（Include Guard）为`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_LITEX_H_`，防止重复包含。文件包含`zephyr/types.h`；`MMCM`由节点标签宏`DT_NODELABEL(clock0)`取得设备树节点，`NCLKOUT`由属性长度宏`DT_PROP_LEN`取得输出数量。

结构体`litex_clk_setup`含四个字段：`clkout_nr`为输出索引（Output Index），`rate`为频率（Frequency，Hz），`phase`为相位偏移（Phase Offset，度），`duty`为占空比（Duty Cycle，百分数）。`uint8_t`／`uint16_t`／`uint32_t`为相应位宽的无符号整数类型（Unsigned Integer Type）。

## 122.2\_完整原始代码

版权属于2020年 Antmicro，采用 Apache-2.0 许可证（License）。保留原始版权、网站及 SPDX 许可证标识，仅移除网页行号和行尾空白。Doxygen 文档生成器在源码页隐藏的说明注释，其可见文档内容已在接口与结构体译文中翻译。

```c
/*
 * Copyright (c) 2020 Antmicro <www.antmicro.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_LITEX_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_LITEX_H_


#include <zephyr/types.h>

#define MMCM                    DT_NODELABEL(clock0)
#define NCLKOUT                 DT_PROP_LEN(MMCM, clock_output_names)

struct litex_clk_setup {
        uint8_t clkout_nr;
        uint32_t rate;
        uint16_t phase;
        uint8_t duty;
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_LITEX_H_ */
```

## 122.3\_相关说明

- [头文件参考](P121_LiteX时钟控制头文件参考.md)。
- [结构体字段说明](P120_LiteX时钟设置结构.md)。
- [宏接口说明](P119_LiteX时钟控制接口.md)。

---

[上一章：LiteX时钟控制头文件参考](P121_LiteX时钟控制头文件参考.md) · [下一章：STM32时钟控制接口](P123_STM32时钟控制接口.md) · [返回大纲](大纲.md)
