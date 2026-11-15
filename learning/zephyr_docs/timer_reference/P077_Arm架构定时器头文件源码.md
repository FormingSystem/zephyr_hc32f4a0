---
id: learning.zephyr-docs.timer_reference.systemtimer-77
title: Arm架构定时器头文件源码
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arm__arch__timer_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第77章\_Arm架构定时器头文件源码

原文：[arm__arch__timer_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/arm__arch__timer_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保存官方源码浏览页的全部可见代码、版权和许可，仅移除网页行号及行尾空白。中文文件参考见[上一章](P076_Arm架构定时器头文件参考.md)。

## 77.1\_完整可见源码

```c
/*
 * Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_TIMER_ARM_ARCH_TIMER_H_
#define ZEPHYR_INCLUDE_DRIVERS_TIMER_ARM_ARCH_TIMER_H_

#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
#include <zephyr/types.h>
#include <zephyr/devicetree.h>

#if DT_HAS_COMPAT_STATUS_OKAY(arm_armv8_timer)
#define ARM_TIMER_NODE DT_INST(0, arm_armv8_timer)
#elif DT_HAS_COMPAT_STATUS_OKAY(arm_armv7_timer)
#define ARM_TIMER_NODE DT_INST(0, arm_armv7_timer)
#endif

#define ARM_TIMER_SECURE_IRQ            DT_IRQ_BY_IDX(ARM_TIMER_NODE, 0, irq)
#define ARM_TIMER_NON_SECURE_IRQ        DT_IRQ_BY_IDX(ARM_TIMER_NODE, 1, irq)
#define ARM_TIMER_VIRTUAL_IRQ           DT_IRQ_BY_IDX(ARM_TIMER_NODE, 2, irq)
#define ARM_TIMER_HYP_IRQ               DT_IRQ_BY_IDX(ARM_TIMER_NODE, 3, irq)

#define ARM_TIMER_SECURE_PRIO           DT_IRQ_BY_IDX(ARM_TIMER_NODE, 0,\
                                        priority)
#define ARM_TIMER_NON_SECURE_PRIO       DT_IRQ_BY_IDX(ARM_TIMER_NODE, 1,\
                                        priority)
#define ARM_TIMER_VIRTUAL_PRIO          DT_IRQ_BY_IDX(ARM_TIMER_NODE, 2,\
                                        priority)
#define ARM_TIMER_HYP_PRIO              DT_IRQ_BY_IDX(ARM_TIMER_NODE, 3,\
                                        priority)

#define ARM_TIMER_SECURE_FLAGS          DT_IRQ_BY_IDX(ARM_TIMER_NODE, 0, flags)
#define ARM_TIMER_NON_SECURE_FLAGS      DT_IRQ_BY_IDX(ARM_TIMER_NODE, 1, flags)
#define ARM_TIMER_VIRTUAL_FLAGS         DT_IRQ_BY_IDX(ARM_TIMER_NODE, 2, flags)
#define ARM_TIMER_HYP_FLAGS             DT_IRQ_BY_IDX(ARM_TIMER_NODE, 3, flags)

#endif /* ZEPHYR_INCLUDE_DRIVERS_TIMER_ARM_ARCH_TIMER_H_ */
```

## 77.2\_源码注释与阅读说明

源码保留三个包含项、Armv8／Armv7设备树（Devicetree）节点选择分支，以及安全／非安全／虚拟／HYP各四组中断编号、优先级（Priority）和标志（Flags）宏。12个宏的原始索引和续行格式均保留。原代码没有额外英文实现注释。

---

[上一章：Arm架构定时器头文件参考](P076_Arm架构定时器头文件参考.md) · [下一章：InfineonTCPWM定时器头文件参考](P078_InfineonTCPWM定时器头文件参考.md) · [返回大纲](大纲.md)
