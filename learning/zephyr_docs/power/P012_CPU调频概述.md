---
id: learning.zephyr-docs.power.cpufreq-0
title: CPU调频概述
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/services/cpu_freq/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第12章\_CPU调频概述

原文：[CPU Frequency Scaling](https://docs.zephyrproject.org/latest/services/cpu_freq/index.html)。读取日期：2026-10-13，`latest`。

## 12.1\_概述与设计目标

Zephyr 的中央处理器（Central Processing Unit，CPU）动态调频（Frequency Scaling）子系统，为片上系统（System on Chip，SoC）提供依据监测指标和性能状态（Performance State，P-state）策略算法动态调整处理器频率的框架。

设计目标是让任意策略算法能够与任意 P-state 驱动配合，并允许每种策略利用一个或多个指标确定最合适的 CPU 频率。框架还应具有足够的灵活性，使 SoC 厂商能够定义自有的性能状态、阈值和指标。

## 12.2\_性能状态策略与指标

性能状态策略（P-state Policy）根据其使用的指标，以及各性能状态定义的阈值，确定 CPU 最合适的性能状态。策略可以使用一个或多个指标，依据所需的系统统计信息确定频率。标准策略见[CPU调频策略目录](P013_CPU调频策略目录.md)。

策略应至少包含一个决策指标（Metric），例如 CPU 负载百分比、SoC 温度等。[按需调频策略](P014_按需CPU调频策略.md)展示了指标的用法。

## 12.3\_温度约束

可选的[CPU调频温度上限](P017_CPU调频温度上限.md)功能依据温度触发点（Temperature Trip Point），限制当前策略允许采用的最高性能状态。这是约束层（Constraint Layer），而不是性能状态策略；它用于减少过度发热，保护 SoC 免受热应力影响。

## 12.4\_性能状态驱动

支持本子系统的 SoC 必须提供性能状态驱动（P-state Driver），实现函数 [`cpu_freq_pstate_set()`](P023_CPU调频接口.md)。调用该函数时，驱动将传入的 `p_state` 应用到 CPU。

SoC 还必须通过设备树（Devicetree）中兼容标识为 `zephyr,pstate` 的节点提供可用性能状态。SoC 可以定义自己的性能状态绑定（Binding），在 `zephyr,pstate` 基础上扩展 SoC 驱动所需的其他属性。详见[性能状态绑定](../hardware/P555_性能状态绑定.md)。

## 12.5\_使用注意事项

子系统支持单处理器（Uniprocessor，UP）和对称多处理（Symmetric Multiprocessing，SMP）系统。在 SMP 系统上，默认假设所有 CPU 使用相同的时钟频率，因此一个 CPU 发生性能状态切换时，其他 CPU 也执行相同切换。SoC 可启用 Kconfig 配置选项 [`CONFIG_CPU_FREQ_PER_CPU_SCALING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_FREQ_PER_CPU_SCALING)，让各个 CPU 独立设置时钟频率，覆盖这一默认行为。

支持调频的 SoC 必须遵守 Zephyr 的要求：系统定时器频率在整个程序运行期间保持稳定。详见[内核计时](../kernel/P008_内核计时.md)。

本子系统以 `k_timer` 内核定时器的处理函数运行，即处于中断请求（Interrupt Request，IRQ）上下文。SoC 驱动必须确保 [`cpu_freq_pstate_set()`](P023_CPU调频接口.md) 可安全地在中断上下文调用。如果性能状态切换无法在中断上下文中合理完成，建议将驱动任务实现为工作队列（Workqueue）的工作项。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：电源管理文档入口](P008_电源管理文档入口.md) · [本模块主线目录](../reading/power.md) · [全部主线](../reading/README.md) · [下一篇：CPU调频策略目录](P013_CPU调频策略目录.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：任务看门狗示例](P011_任务看门狗示例.md) · [下一章：CPU调频策略目录](P013_CPU调频策略目录.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
