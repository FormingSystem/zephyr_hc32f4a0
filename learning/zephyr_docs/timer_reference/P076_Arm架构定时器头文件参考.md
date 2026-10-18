---
id: learning.zephyr-docs.timer_reference.systemtimer-76
title: Arm架构定时器头文件参考
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arm__arch__timer_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第76章\_Arm架构定时器头文件参考

原文：[arm__arch__timer_8h](https://docs.zephyrproject.org/latest/doxygen/html/arm__arch__timer_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/timer/arm_arch_timer.h`定义Arm架构定时器（Arm Architectural Timer）所使用的中断相关宏。头文件包含：

```c
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>
#include <zephyr/types.h>
#include <zephyr/devicetree.h>
```

## 76.1\_中断编号与标志

下表完整保留原文件参考中的8个中断请求（Interrupt Request，IRQ）与标志（Flags）宏。设备树（Devicetree）宏`DT_IRQ_BY_IDX`按中断索引从`ARM_TIMER_NODE`读取指定单元。

| 宏 | 原展开式 | 对应项 |
| --- | --- | --- |
| `ARM_TIMER_SECURE_IRQ` | `DT_IRQ_BY_IDX(ARM_TIMER_NODE, 0, irq)` | 安全（Secure）中断编号。 |
| `ARM_TIMER_SECURE_FLAGS` | `DT_IRQ_BY_IDX(ARM_TIMER_NODE, 0, flags)` | 安全（Secure）中断标志。 |
| `ARM_TIMER_NON_SECURE_IRQ` | `DT_IRQ_BY_IDX(ARM_TIMER_NODE, 1, irq)` | 非安全（Non-secure）中断编号。 |
| `ARM_TIMER_NON_SECURE_FLAGS` | `DT_IRQ_BY_IDX(ARM_TIMER_NODE, 1, flags)` | 非安全（Non-secure）中断标志。 |
| `ARM_TIMER_VIRTUAL_IRQ` | `DT_IRQ_BY_IDX(ARM_TIMER_NODE, 2, irq)` | 虚拟（Virtual）中断编号。 |
| `ARM_TIMER_VIRTUAL_FLAGS` | `DT_IRQ_BY_IDX(ARM_TIMER_NODE, 2, flags)` | 虚拟（Virtual）中断标志。 |
| `ARM_TIMER_HYP_IRQ` | `DT_IRQ_BY_IDX(ARM_TIMER_NODE, 3, irq)` | HYP中断编号。 |
| `ARM_TIMER_HYP_FLAGS` | `DT_IRQ_BY_IDX(ARM_TIMER_NODE, 3, flags)` | HYP中断标志。 |

原文未进一步解释HYP命名，此处保留该名称及索引3的映射，不据此扩展硬件行为。

## 76.2\_中断优先级

四个优先级（Priority）宏读取相同索引的`priority`单元。以下按原参考页顺序保留多行展开式，包括续行符。

`ARM_TIMER_HYP_PRIO`：

```c
DT_IRQ_BY_IDX(ARM_TIMER_NODE, 3,\
priority)
```

`ARM_TIMER_NON_SECURE_PRIO`：

```c
DT_IRQ_BY_IDX(ARM_TIMER_NODE, 1,\
priority)
```

`ARM_TIMER_SECURE_PRIO`：

```c
DT_IRQ_BY_IDX(ARM_TIMER_NODE, 0,\
priority)
```

`ARM_TIMER_VIRTUAL_PRIO`：

```c
DT_IRQ_BY_IDX(ARM_TIMER_NODE, 2,\
priority)
```

## 76.3\_节点选择

源码首先检查是否存在状态可用的`arm_armv8_timer`兼容节点；如果有，将`ARM_TIMER_NODE`定义为`DT_INST(0, arm_armv8_timer)`。否则再检查`arm_armv7_timer`，使用对应的实例0。两者都不满足时，这段条件代码不定义`ARM_TIMER_NODE`。这是[可见源码](P077_Arm架构定时器头文件源码.md)中的节点选择逻辑。

---

[上一章：计数器驱动头文件目录](P075_计数器驱动头文件目录.md) · [下一章：Arm架构定时器头文件源码](P077_Arm架构定时器头文件源码.md) · [返回大纲](大纲.md)
