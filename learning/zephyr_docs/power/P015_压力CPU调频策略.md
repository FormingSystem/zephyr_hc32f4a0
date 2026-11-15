---
id: learning.zephyr-docs.power.cpufreq-3
title: 压力CPU调频策略
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/services/cpu_freq/policies/pressure.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第15章\_压力CPU调频策略

原文：[Pressure based CPU Frequency Scaling Policy](https://docs.zephyrproject.org/latest/services/cpu_freq/policies/pressure.html)。读取日期：2026-10-13，`latest`。

## 15.1\_线程压力计算

压力策略（Pressure Policy）评估就绪队列（Ready Queue）的当前压力，据此决定系统性能状态（Performance State，P-state）的切换。这里的 CPU 指中央处理器（Central Processing Unit）。

线程压力（Thread Pressure）按下式计算：

$$
P_{sys} = \frac{\sum_{t \in R} (P_{min} - prio_t + 1)}
                {\sum_{t \in T} (P_{min} - prio_t + 1)} \times 100
$$

其中：

- $R$ 是可运行、已排队线程的集合。
- $T$ 是纳入压力计算的所有线程的集合。
- $w_t = P_{min} - \text{prio}_t + 1$ 是线程 $t$ 的权重。
- $P_{min}$ 是配置中纳入计算的最低优先级，其优先级数值最大。

结果是0～100之间的归一化系统压力（Normalized System Pressure），用于选择 SoC，即片上系统（System on Chip），或叠加配置（Overlay）文件定义的合适性能状态。

## 15.2\_状态选择与优先级配置

得到归一化压力后，策略将它作为系统“负载”，遍历 SoC 的可用性能状态，并选择第一个满足“归一化压力大于或等于该状态阈值”的状态。

如果没有匹配状态，即压力低于所有阈值，则选择 `soc_pstates` 数组的最后一项，也就是最低性能状态。

可通过 Kconfig 配置选项 [`CONFIG_CPU_FREQ_POLICY_PRESSURE_LOWEST_PRIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_FREQ_POLICY_PRESSURE_LOWEST_PRIO) 调整策略的响应特性。它应设置为系统中最低优先级线程的优先级，即数值最大的那个优先级。策略忽略优先级比该选项更低的线程；由于上面的公式，这个选项也会改变策略所感知的高优先级线程运行影响。

## 15.3\_示例与限制

示例见[压力CPU调频示例](P020_压力CPU调频示例.md)。

该策略尝试提前评估队列中的任务，在执行之前主动调整时钟频率。但它不保证性能或确定性，不能保证线程满足截止期限（Deadline）或避免饥饿（Starvation）。

原文提醒，压力相关配置引入 [`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING) 跟踪功能，会增加上下文切换（Context Switch）的开销。译注：原文将这一关系写在 [`CONFIG_CPU_FREQ_POLICY_PRESSURE_LOWEST_PRIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_FREQ_POLICY_PRESSURE_LOWEST_PRIO) 上；[官方Kconfig源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig)中，实际选择 `TRACING` 的是策略开关 `CPU_FREQ_POLICY_PRESSURE`，而 `CPU_FREQ_POLICY_PRESSURE_LOWEST_PRIO` 是其内部的整数优先级配置。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：按需CPU调频策略](P014_按需CPU调频策略.md) · [本模块主线目录](../reading/power.md) · [全部主线](../reading/README.md) · [下一篇：时序噪声CPU调频策略](P016_时序噪声CPU调频策略.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：按需CPU调频策略](P014_按需CPU调频策略.md) · [下一章：时序噪声CPU调频策略](P016_时序噪声CPU调频策略.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
