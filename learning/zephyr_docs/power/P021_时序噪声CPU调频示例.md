---
id: learning.zephyr-docs.power.cpufreqsample-3
title: 时序噪声CPU调频示例
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/cpu_freq/timing_noise/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="cpu_freq_timing_noise"></a>

# 第21章\_时序噪声CPU调频示例

原文：[CPU frequency scaling timing noise sample](https://docs.zephyrproject.org/latest/samples/subsys/cpu_freq/timing_noise/README.html)。读取日期：2026-10-13，`latest`。

## 21.1\_概述

本示例故意实现一个非恒定时间（Non-Constant-Time）的密码检查，并提供一个简单的时序实验：根据周期计数（Cycle Count）为候选字符排序。以默认配置构建时，它展示在中央处理器（Central Processing Unit，CPU）频率稳定的情况下，实验如何恢复密码。

使用 `timing_noise_prj.conf` 重新构建会启用[时序噪声策略（Timing Noise Policy）](P016_时序噪声CPU调频策略.md)，周期性地随机选择性能状态（Performance State，P-state）。频率抖动（Frequency Jitter）往往会扰乱本实验使用的排序，使猜测字符串不再等于秘密值。这一结果只针对本测量设置，既不表示底层泄漏已消失，也不表示一般意义上的攻击者已被击败。

正确修复仍然是采用恒定时间（Constant-Time）密码检查。本示例只演示随机化性能状态如何干扰简单的周期计数排序。

```shell
west build -b frdm_mcxn236 samples/subsys/cpu_freq/timing_noise \
  -- -DEXTRA_CONF_FILE=timing_noise_prj.conf
```

## 21.2\_构建与运行

不启用时序噪声策略进行构建：频率稳定，实验能够成功。

```shell
west build -b frdm_mcxn236 samples/subsys/cpu_freq/timing_noise
```

启用时序噪声策略进行构建；`EXTRA_CONF_FILE` 是指定附加配置文件的构建参数：

```shell
west build -b frdm_mcxn236 samples/subsys/cpu_freq/timing_noise -- -DEXTRA_CONF_FILE=timing_noise_prj.conf
```

烧录并运行；以下保留原页的命令：

```shell
west build -b frdm_mcxn236 samples/subsys/cpu_freq/timing_noise
west flash
```

译注：原页此处再次给出未带附加配置参数的构建命令。比较两种配置时，应核对最终构建产物使用的配置，向目标板烧录希望观察的那个构建结果；不能仅凭该小节标题认定已经启用时序噪声。

## 21.3\_示例输出

默认模式下频率稳定，排序可逐步恢复秘密值：

```text
pos 0 try A -> 79 cycles
pos 0 try B -> 83 cycles
pos 0 try C -> 91 cycles
...
Recovered so far: P

pos 1 try A -> 87 cycles
pos 1 try B -> 92 cycles
...
Recovered so far: Pa
```

启用时序噪声后，本实验的排序失效，候选之间没有稳定次序：

```text
pos 0 try A -> 101 cycles
pos 0 try B -> 100 cycles
pos 0 try C -> 102 cycles
...
Recovered so far: PxSaaZ

(no stable ordering between candidates)
```

## 21.4\_另请参阅

[CPU调频概述](P012_CPU调频概述.md)及[官方CPUFreq接口](P023_CPU调频接口.md)。

---

[上一章：压力CPU调频示例](P020_压力CPU调频示例.md) · [下一章：CPU调频温度上限示例](P022_CPU调频温度上限示例.md) · [返回大纲](大纲.md)
