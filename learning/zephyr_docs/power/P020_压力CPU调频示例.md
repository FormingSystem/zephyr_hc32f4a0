---
id: learning.zephyr-docs.power.cpufreqsample-2
title: 压力CPU调频示例
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/cpu_freq/pressure/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="cpu_freq_pressure"></a>

# 第20章\_压力CPU调频示例

原文：[Pressure based CPU frequency scaling](https://docs.zephyrproject.org/latest/samples/subsys/cpu_freq/pressure/README.html)。读取日期：2026-10-13，`latest`。

## 20.1\_概述

本示例展示中央处理器（Central Processing Unit，CPU）调频子系统的[压力策略（Pressure Policy）](P015_压力CPU调频策略.md)，根据线程队列压力调整 CPU 频率。竞争 CPU 时间的可运行线程越多，策略选择的性能状态（Performance State，P-state）越高；活动线程减少时，降低频率。

示例创建低、中、高三个优先级的线程，在三种模式之间循环，以模拟不同系统负载：

| 模式 | 运行线程 | 压力 |
| --- | --- | --- |
| 模式1 | 只有低优先级线程 | 低 |
| 模式2 | 低、中优先级线程 | 中等 |
| 模式3 | 三个线程全部运行 | 高 |

示例启用了调试日志，因此可以在控制台看到压力评估和性能状态选择。

## 20.2\_构建与运行

按以下命令构建和运行，将主机原生模拟目标 `native_sim` 替换为自己的开发板：

```shell
west build -b native_sim samples/subsys/cpu_freq/pressure
west build -t run
```

## 20.3\_示例输出

下列原始输出保留各线程优先级和状态、原始压力比值、百分比、阈值及所选性能状态。输出中的 SoC 指片上系统（System on Chip），OS 指操作系统（Operating System）；`CPU0` 为第0个处理器。

```text
[00:00:00.000,000] <inf> cpu_freq: CPU frequency subsystem initialized with interval 500 ms
*** Booting Zephyr OS build v4.4.0-rc1-171-ga6b41c41d385 ***
[00:00:00.000,000] <inf> cpu_freq_pressure_sample: Starting CPU Freq Pressure Policy Sample!
[00:00:00.000,000] <inf> cpu_freq_pressure_sample: Mode 1: Low only
[00:00:00.500,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x430728 with prio: 1 status: 16
[00:00:00.500,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x430810 with prio: 5 status: 16
[00:00:00.500,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x4308f8 with prio: 10 status: 128
[00:00:00.500,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x431078 with prio: 15 status: 0
[00:00:00.500,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x431160 with prio: 0 status: 4
[00:00:00.500,000] <dbg> cpu_freq_policy_pressure: get_normalized_sys_pressure: System pressure is: 3% (raw: 1 / max: 28)
[00:00:00.500,000] <dbg> cpu_freq_policy_pressure: cpu_freq_policy_select_pstate: CPU0 Pressure: 3%
[00:00:00.500,000] <dbg> cpu_freq_policy_pressure: cpu_freq_policy_select_pstate: Pressure Policy: Selected P-state 2 with load_threshold=0%
[00:00:00.500,000] <dbg> native_sim_cpu_freq: cpu_freq_pstate_set: SoC setting performance state: 2
[00:00:00.500,000] <dbg> native_sim_cpu_freq: cpu_freq_pstate_set: SoC setting P-state 2: Ultra-low Power Mode

  ...

[00:00:01.510,000] <inf> cpu_freq_pressure_sample: Mode 2: Low + Medium
[00:00:02.000,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x430728 with prio: 1 status: 16
[00:00:02.000,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x430810 with prio: 5 status: 128
[00:00:02.000,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x4308f8 with prio: 10 status: 128
[00:00:02.000,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x431078 with prio: 15 status: 0
[00:00:02.000,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x431160 with prio: 0 status: 4
[00:00:02.000,000] <dbg> cpu_freq_policy_pressure: get_normalized_sys_pressure: System pressure is: 25% (raw: 7 / max: 28)
[00:00:02.000,000] <dbg> cpu_freq_policy_pressure: cpu_freq_policy_select_pstate: CPU0 Pressure: 25%
[00:00:02.000,000] <dbg> cpu_freq_policy_pressure: cpu_freq_policy_select_pstate: Pressure Policy: Selected P-state 1 with load_threshold=20%
[00:00:02.000,000] <dbg> native_sim_cpu_freq: cpu_freq_pstate_set: SoC setting performance state: 1
[00:00:02.000,000] <dbg> native_sim_cpu_freq: cpu_freq_pstate_set: SoC setting P-state 1: Low Power Mode


   ...

[00:00:03.020,000] <inf> cpu_freq_pressure_sample: Mode 3: Low + Medium + High
[00:00:03.500,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x430728 with prio: 1 status: 128
[00:00:03.500,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x430810 with prio: 5 status: 128
[00:00:03.500,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x4308f8 with prio: 10 status: 128
[00:00:03.500,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x431078 with prio: 15 status: 0
[00:00:03.500,000] <dbg> cpu_freq_policy_pressure: thread_eval_cb: Evaluating thread: 0x431160 with prio: 0 status: 4
[00:00:03.500,000] <dbg> cpu_freq_policy_pressure: get_normalized_sys_pressure: System pressure is: 60% (raw: 17 / max: 28)
[00:00:03.500,000] <dbg> cpu_freq_policy_pressure: cpu_freq_policy_select_pstate: CPU0 Pressure: 60%
[00:00:03.500,000] <dbg> cpu_freq_policy_pressure: cpu_freq_policy_select_pstate: Pressure Policy: Selected P-state 0 with load_threshold=50%
[00:00:03.500,000] <dbg> native_sim_cpu_freq: cpu_freq_pstate_set: SoC setting performance state: 0
[00:00:03.500,000] <dbg> native_sim_cpu_freq: cpu_freq_pstate_set: SoC setting P-state 0: Nominal Mode

   ...
```

## 20.4\_另请参阅

[CPU调频概述](P012_CPU调频概述.md)及[官方CPUFreq接口](P023_CPU调频接口.md)。

---

[上一章：按需CPU调频示例](P019_按需CPU调频示例.md) · [下一章：时序噪声CPU调频示例](P021_时序噪声CPU调频示例.md) · [返回大纲](大纲.md)
