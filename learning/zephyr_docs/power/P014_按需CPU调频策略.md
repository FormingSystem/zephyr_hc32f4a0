---
id: learning.zephyr-docs.power.cpufreq-2
title: 按需CPU调频策略
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/services/cpu_freq/policies/on_demand.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第14章\_按需CPU调频策略

原文：[On-Demand CPU Frequency Scaling Policy](https://docs.zephyrproject.org/latest/services/cpu_freq/policies/on_demand.html)。读取日期：2026-10-13，`latest`。

## 14.1\_负载与状态选择

按需策略（On-Demand Policy）使用 [CPU负载](../observability/P007_CPU负载.md)机制评估中央处理器（Central Processing Unit，CPU）的当前负载，并与片上系统（System on Chip，SoC）的性能状态（Performance State，P-state）定义中的触发阈值比较。

策略遍历已定义的性能状态，选择第一个满足“CPU 负载大于或等于该状态阈值”的性能状态。

如果没有匹配的性能状态，即 CPU 负载低于所有阈值，则选择 `soc_pstates` 数组的最后一个元素，也就是最低性能状态。这是策略本身的行为：设备树（Devicetree）中的性能状态必须按阈值递减顺序排列，负载低于所有阈值时使用最后一项。

## 14.2\_示例与边界

使用示例见[按需CPU调频示例](P019_按需CPU调频示例.md)。

这是响应式（Reactive）策略：只有观察到系统负载变化后才调整频率，因此无法预先应对突发高负载。它不感知任务截止期限（Deadline），不应视为实时（Real-Time）策略。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CPU调频策略目录](P013_CPU调频策略目录.md) · [本模块主线目录](../reading/power.md) · [全部主线](../reading/README.md) · [下一篇：压力CPU调频策略](P015_压力CPU调频策略.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：CPU调频策略目录](P013_CPU调频策略目录.md) · [下一章：压力CPU调频策略](P015_压力CPU调频策略.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
