---
id: learning.zephyr-docs.power.cpufreq-4
title: 时序噪声CPU调频策略
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/services/cpu_freq/policies/timing_noise.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第16章\_时序噪声CPU调频策略

原文：[Timing Noise CPU Frequency Scaling Policy](https://docs.zephyrproject.org/latest/services/cpu_freq/policies/timing_noise.html)。读取日期：2026-10-13，`latest`。

## 16.1\_概述

时序噪声策略（Timing Noise Policy）是一种中央处理器（Central Processing Unit，CPU）动态调频策略，周期性地随机选择性能状态（Performance State，P-state）。它通过扰动 CPU 时钟引入时序变化，干扰假设频率稳定的简单周期计数或实际经过时间测量（Wall-Clock Measurement）。

这是一种随机化性能状态策略，并不是通用的侧信道（Side Channel）防护措施。

## 16.2\_主要缓解措施

经过侧信道泄漏审查的恒定时间（Constant-Time）和恒定控制流（Constant-Flow）实现，仍是防御时序攻击（Timing Attack）的主要手段。本策略不能替代这些做法；它最多可能让某一类测量更复杂。

## 16.3\_攻击者模型

本策略考虑的攻击者具有以下特征：

- 通过周期计数器、实际时间定时器或类似的软件可见时间戳，观察相对执行时间。
- 依赖稳定的 CPU 频率，使指令数量或数据相关执行路径中的微小差异在多次试验之间仍可区分。

随机选择性能状态不能挫败这种攻击。只要样本足够多，攻击者往往能通过求平均消除噪声影响。本策略只是让这类测量更不方便、可重复性更差。

## 16.4\_使用场景

当应用已经建立在可靠的软件实现之上，希望再增加一层时序变化时，可以考虑本策略。应把它视为干扰某些分析的方法，不能把它单独当作安全方案。

本策略不适合以下场景：

- 需要确定执行时间的硬实时（Hard Real-Time）系统。
- 将时序可预测性纳入安全论证的安全相关系统。
- 无法容忍意外进入低速性能状态的延迟敏感工作负载。
- 有严格功耗预算的设计，因为频繁切换性能状态可能提高平均功耗。

## 16.5\_配置

启用 CPU 调频子系统并选择时序噪声策略，使用以下 Kconfig 配置选项：

```ini
CONFIG_CPU_FREQ=y
CONFIG_CPU_FREQ_POLICY_TIMING_NOISE=y
```

策略使用调频子系统的标准更新间隔，通过以下选项配置：

```ini
CONFIG_CPU_FREQ_INTERVAL_MS=<interval>
```

更新间隔越小，时序变化越多，但频率切换次数也越多。

## 16.6\_随机数生成

策略使用函数 [`sys_rand32_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__random__api.html#ga62cb24a6049b7aa9d03d66786e4a4db6) 选择性能状态。在具有硬件熵源（Hardware Entropy Source）的平台上，选择 `CONFIG_CPU_FREQ_POLICY_TIMING_NOISE` 会启用熵驱动。存在真随机数发生器（True Random Number Generator，TRNG）时，应优先通过该驱动获取随机数，使用以下 Kconfig 配置选项：

```ini
CONFIG_ENTROPY_DEVICE_RANDOM_GENERATOR=y
```

## 16.7\_局限性

- 无法消除时序侧信道。
- 无法弥补软件本身的安全缺陷。
- 可能降低系统整体性能。
- 频繁改变性能状态可能增加功耗。
- 对坚持攻击或测量设备完善的攻击者不提供任何保证。

使用示例见[时序噪声CPU调频示例](P021_时序噪声CPU调频示例.md)。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：压力CPU调频策略](P015_压力CPU调频策略.md) · [本模块主线目录](../reading/power.md) · [全部主线](../reading/README.md) · [下一篇：CPU调频温度上限](P017_CPU调频温度上限.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：压力CPU调频策略](P015_压力CPU调频策略.md) · [下一章：CPU调频温度上限](P017_CPU调频温度上限.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
