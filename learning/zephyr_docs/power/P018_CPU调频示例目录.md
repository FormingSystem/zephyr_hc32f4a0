---
id: learning.zephyr-docs.power.cpufreqsample-0
title: CPU调频示例目录
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/cpu_freq/cpu_freq.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第18章\_CPU调频示例目录

原文：[CPU Freq](https://docs.zephyrproject.org/latest/samples/subsys/cpu_freq/cpu_freq.html)。读取日期：2026-10-13，`latest`。

这些示例展示中央处理器（Central Processing Unit，CPU）动态调频（Frequency Scaling）子系统。

## 18.1\_示例入口

| 示例 | 演示内容 |
| --- | --- |
| [时序噪声调频](P021_时序噪声CPU调频示例.md) | 随机选择性能状态（Performance State，P-state）如何干扰简单的周期计数密码猜测实验 |
| [温度上限](P022_CPU调频温度上限示例.md) | 根据芯片裸片温度（Die Temperature）限制 CPU 频率 |
| [按需调频](P019_按需CPU调频示例.md) | 使用按需策略（On-Demand Policy）动态调整 CPU 频率 |
| [压力调频](P020_压力CPU调频示例.md) | 使用压力策略（Pressure Policy）动态调整 CPU 频率 |

---

[上一章：CPU调频温度上限](P017_CPU调频温度上限.md) · [下一章：按需CPU调频示例](P019_按需CPU调频示例.md) · [返回大纲](大纲.md)
