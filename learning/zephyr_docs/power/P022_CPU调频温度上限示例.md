---
id: learning.zephyr-docs.power.cpufreqsample-4
title: CPU调频温度上限示例
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/cpu_freq/thermal_cap/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="cpu_freq_thermal_cap"></a>

# 第22章\_CPU调频温度上限示例

原文：[CPU frequency thermal cap](https://docs.zephyrproject.org/latest/samples/subsys/cpu_freq/thermal_cap/README.html)。读取日期：2026-10-13，`latest`。

## 22.1\_概述

本示例演示中央处理器（Central Processing Unit，CPU）频率的[温度限制（Thermal Cap）](P017_CPU调频温度上限.md)。按需调频策略（On-Demand Policy）根据 CPU 负载选择请求的性能状态（Performance State，P-state），温度约束则根据芯片裸片温度（Die Temperature）限制允许使用的最高性能状态。

开发板叠加配置（Overlay）启用板上裸片温度传感器，并设置较低的温度触发点（Temperature Trip Point），以便在示例中观察约束行为。产品固件应按自己的热设计选择触发点。

示例不会自动使裸片温度在配置的范围内循环。要观察所有触发点，原文要求使用受控的外部热源使开发板升温，然后让它冷却到解除阈值（Release Threshold）以下。

## 22.2\_构建与运行

按以下命令构建和运行：

```shell
west build -b frdm_mcxn236 samples/subsys/cpu_freq/thermal_cap
west flash
```

## 22.3\_示例输出

```text
CPUFreq thermal cap sample
trip 0: 25.000 C -> cap pstate-1, release at 22.000 C
trip 1: 40.000 C -> cap pstate-2, release at 37.000 C

die temperature: 24.875 C, thermal cap: none
die temperature: 25.125 C, thermal cap: pstate-1
die temperature: 40.250 C, thermal cap: pstate-2
```

---

[上一章：时序噪声CPU调频示例](P021_时序噪声CPU调频示例.md) · [下一章：CPU调频接口](P023_CPU调频接口.md) · [返回大纲](大纲.md)
