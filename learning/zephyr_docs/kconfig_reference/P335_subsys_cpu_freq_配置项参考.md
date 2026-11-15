---
id: learning.zephyr-docs.kconfig-reference.page-335
title: "`subsys/cpu_freq`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第335章\_`subsys/cpu_freq`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/cpu_freq` 的 17 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CPU_FREQ"></a>

## 335.1 `CONFIG_CPU_FREQ`

**提示（Prompt）**：CPU 频率调整子系统（CPU Frequency Scaling Subsystem）

**说明（Help）**

CPU 频率调整子系统（CPU Frequency scaling subsystem）

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

<a id="CONFIG_CPU_FREQ_INTERVAL_MS"></a>

## 335.2 `CONFIG_CPU_FREQ_INTERVAL_MS`

**提示（Prompt）**：CPU 频率评估间隔（CPU Freq evaluation interval）

**说明（Help）**

控制 CPU 频率子系统（CPU Frequency subsystem）运行并评估当前策略（policy）的间隔，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_FREQ
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ)。

<a id="CONFIG_CPU_FREQ_PER_CPU_SCALING"></a>

## 335.3 `CONFIG_CPU_FREQ_PER_CPU_SCALING`

**提示（Prompt）**：逐 CPU 频率调整（Per-CPU frequency scaling）

**说明（Help）**

启用逐 CPU 频率调整（per-CPU frequency scaling）支持。禁用时，设置性能状态（P-state）会应用于整个系统，而非仅当前 CPU。此配置应在 SoC 层完成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP && CONFIG_CPU_FREQ
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_CPU_FREQ`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ)。

<a id="CONFIG_CPU_FREQ_POLICY"></a>

## 335.4 `CONFIG_CPU_FREQ_POLICY`

**提示（Prompt）**：CPU 频率调节策略（CPU Frequency Scaling Policy）

**说明（Help）**

使用 CPU 频率子系统（CPU freq subsystem）时采用的策略算法（policy algorithm）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_FREQ
```

**默认值（Defaults）**

```text
CONFIG_CPU_FREQ_POLICY_NONE
```

**可选项（Choices）**

```text
CONFIG_CPU_FREQ_POLICY_NONE
CONFIG_CPU_FREQ_POLICY_ON_DEMAND
CONFIG_CPU_FREQ_POLICY_PRESSURE
CONFIG_CPU_FREQ_POLICY_TIMING_NOISE
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ)、[`CONFIG_CPU_FREQ_POLICY_NONE`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_POLICY_NONE)、[`CONFIG_CPU_FREQ_POLICY_ON_DEMAND`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_POLICY_ON_DEMAND)、[`CONFIG_CPU_FREQ_POLICY_PRESSURE`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_POLICY_PRESSURE)、[`CONFIG_CPU_FREQ_POLICY_TIMING_NOISE`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_POLICY_TIMING_NOISE)。

<a id="CONFIG_CPU_FREQ_POLICY_NONE"></a>

## 335.5 `CONFIG_CPU_FREQ_POLICY_NONE`

**提示（Prompt）**：未选择策略（No selected policy）

**说明（Help）**

没有选定策略（policy）时使用的 Kconfig 占位项，此项会产生构建错误。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_FREQ_POLICY>
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调节策略（CPU Frequency Scaling Policy）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_POLICY`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_POLICY)。

<a id="CONFIG_CPU_FREQ_POLICY_ON_DEMAND"></a>

## 335.6 `CONFIG_CPU_FREQ_POLICY_ON_DEMAND`

**提示（Prompt）**：按需策略（On-demand Policy）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_FREQ_POLICY>
```

**主动选择（Selects）**

```text
CONFIG_CPU_LOAD
CONFIG_CPU_LOAD_MULTICPU
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调节策略（CPU Frequency Scaling Policy）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_POLICY`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_POLICY)、[`CONFIG_CPU_LOAD`](P197_lib_配置项参考_1.md#CONFIG_CPU_LOAD)、[`CONFIG_CPU_LOAD_MULTICPU`](P197_lib_配置项参考_1.md#CONFIG_CPU_LOAD_MULTICPU)。

<a id="CONFIG_CPU_FREQ_POLICY_PRESSURE"></a>

## 335.7 `CONFIG_CPU_FREQ_POLICY_PRESSURE`

**提示（Prompt）**：基于压力的策略（Pressure based Policy）

**说明（Help）**

基于压力的策略（Pressure based policy）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_FREQ_POLICY>
```

**主动选择（Selects）**

```text
CONFIG_TRACING
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调节策略（CPU Frequency Scaling Policy）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_POLICY`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_POLICY)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)。

<a id="CONFIG_CPU_FREQ_POLICY_PRESSURE_LOWEST_PRIO"></a>

## 335.8 `CONFIG_CPU_FREQ_POLICY_PRESSURE_LOWEST_PRIO`

**提示（Prompt）**：要累计的最低优先级，数值最大（lowest priority level, highest numerically）

**说明（Help）**

要累计的最低优先级级别，即数值最大的级别。它应对应最低优先级线程，且优先级不得低于空闲线程（idle thread）的优先级。

译注：这里区分调度优先级与数值大小；“不得更低”意味着优先级数值不得比空闲线程更大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_FREQ_POLICY_PRESSURE && <choice CONFIG_CPU_FREQ_POLICY>
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调节策略（CPU Frequency Scaling Policy） → 基于压力的策略（Pressure based Policy）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_POLICY_PRESSURE`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_POLICY_PRESSURE)、[`CONFIG_CPU_FREQ_POLICY`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_POLICY)。

<a id="CONFIG_CPU_FREQ_POLICY_TIMING_NOISE"></a>

## 335.9 `CONFIG_CPU_FREQ_POLICY_TIMING_NOISE`

**提示（Prompt）**：时序噪声策略（Timing noise policy）

**说明（Help）**

时序噪声策略（Timing noise policy），周期性通过 `sys_rand32_get()` 随机选择性能状态（performance state），引入时序变化。这可能扰乱假定 CPU 频率稳定的简单时序分析，但不是通用的侧信道防护措施（side-channel countermeasure）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_FREQ_POLICY>
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_GENERATOR if CONFIG_ENTROPY_NODE_ENABLED
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调节策略（CPU Frequency Scaling Policy）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_POLICY`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_POLICY)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_NODE_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_NODE_ENABLED)。

<a id="CONFIG_CPU_FREQ_PSTATE_SET"></a>

## 335.10 `CONFIG_CPU_FREQ_PSTATE_SET`

**提示（Prompt）**：选择 CPU P-state 设置方法（method of setting CPU P-state）

**说明（Help）**

用于设置 CPU 性能状态（P-state）的实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_FREQ
```

**默认值（Defaults）**

```text
CONFIG_CPU_FREQ_PSTATE_SET_SOC if CONFIG_HAS_CPU_FREQ
CONFIG_CPU_FREQ_PSTATE_SET_STUB
```

**可选项（Choices）**

```text
CONFIG_CPU_FREQ_PSTATE_SET_STUB
CONFIG_CPU_FREQ_PSTATE_SET_SOC
CONFIG_CPU_FREQ_PSTATE_SET_CUSTOM
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ)、[`CONFIG_CPU_FREQ_PSTATE_SET_SOC`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_PSTATE_SET_SOC)、[`CONFIG_HAS_CPU_FREQ`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_HAS_CPU_FREQ)、[`CONFIG_CPU_FREQ_PSTATE_SET_STUB`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_PSTATE_SET_STUB)、[`CONFIG_CPU_FREQ_PSTATE_SET_CUSTOM`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_PSTATE_SET_CUSTOM)。

<a id="CONFIG_CPU_FREQ_PSTATE_SET_CUSTOM"></a>

## 335.11 `CONFIG_CPU_FREQ_PSTATE_SET_CUSTOM`

**提示（Prompt）**：项目定义的自定义 P-state 设置器（Custom P-state setter）

**说明（Help）**

通过项目专用机制设置 CPU 性能状态（P-state）的自定义实现，要求项目提供所需的 `cpu_freq_pstate_set()` 实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_FREQ_PSTATE_SET>
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → 选择 CPU P-state 设置方法（method of setting CPU P-state）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_PSTATE_SET`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_PSTATE_SET)。

<a id="CONFIG_CPU_FREQ_PSTATE_SET_SOC"></a>

## 335.12 `CONFIG_CPU_FREQ_PSTATE_SET_SOC`

**提示（Prompt）**：SoC 专用 P-state 设置器（SoC-specific P-state setter）

**说明（Help）**

通过 SoC 专用机制设置 CPU 性能状态（P-state）的实现，要求 SoC 提供所需的 `cpu_freq_pstate_set()` 实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_CPU_FREQ && <choice CONFIG_CPU_FREQ_PSTATE_SET>
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → 选择 CPU P-state 设置方法（method of setting CPU P-state）

**配置项引用（Symbol References）**：[`CONFIG_HAS_CPU_FREQ`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_HAS_CPU_FREQ)、[`CONFIG_CPU_FREQ_PSTATE_SET`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_PSTATE_SET)。

<a id="CONFIG_CPU_FREQ_PSTATE_SET_STUB"></a>

## 335.13 `CONFIG_CPU_FREQ_PSTATE_SET_STUB`

**提示（Prompt）**：P-state 空桩设置器（Stub P-state setter）

**说明（Help）**

不执行任何操作的空桩实现（stub implementation），可用于验证 CPU 频率子系统流程，而不实际改变 CPU 频率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CPU_FREQ_PSTATE_SET>
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → 选择 CPU P-state 设置方法（method of setting CPU P-state）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_PSTATE_SET`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_PSTATE_SET)。

<a id="CONFIG_CPU_FREQ_THERMAL_CAP"></a>

## 335.14 `CONFIG_CPU_FREQ_THERMAL_CAP`

**提示（Prompt）**：CPU 频率调整的热限制上限（Thermal cap for CPU frequency scaling）

**说明（Help）**

为 CPU 频率调整启用热约束层（thermal constraint layer）。当前 CPU 频率策略仍负责选择请求的性能状态（P-state）；当配置的温度触发点（temperature trip points）生效时，热限制上限（thermal cap）可限制允许使用的最高性能状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSOR && DT_HAS_ZEPHYR_CPU_FREQ_THERMAL_CAP_ENABLED && CONFIG_CPU_FREQ
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_CPU_FREQ`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ)。

<a id="CONFIG_CPU_FREQ_THERMAL_CAP_FAIL_SAFE"></a>

## 335.15 `CONFIG_CPU_FREQ_THERMAL_CAP_FAIL_SAFE`

**提示（Prompt）**：温度传感器故障后应用故障安全 P-state（fail-safe P-state after thermal sensor failures）

**说明（Help）**

连续发生温度传感器采样失败后，应用已配置的故障安全性能状态（fail-safe P-state）。禁用时，保留最后计算得到的热限制上限（thermal cap）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_FREQ_THERMAL_CAP && CONFIG_CPU_FREQ
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调整的热限制上限（Thermal cap for CPU frequency scaling）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_THERMAL_CAP`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_THERMAL_CAP)、[`CONFIG_CPU_FREQ`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ)。

<a id="CONFIG_CPU_FREQ_THERMAL_CAP_SENSOR_FAILURE_LIMIT"></a>

## 335.16 `CONFIG_CPU_FREQ_THERMAL_CAP_SENSOR_FAILURE_LIMIT`

**提示（Prompt）**：温度传感器失败次数阈值（Thermal sensor failure limit）

**说明（Help）**

在热限制功能应用故障安全性能状态（fail-safe P-state）之前，允许出现的连续温度传感器采样失败次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_FREQ_THERMAL_CAP && CONFIG_CPU_FREQ
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → CPU 频率调整子系统（CPU Frequency Scaling Subsystem） → CPU 频率调整的热限制上限（Thermal cap for CPU frequency scaling）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_THERMAL_CAP`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_THERMAL_CAP)、[`CONFIG_CPU_FREQ`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ)。

<a id="CONFIG_HAS_CPU_FREQ"></a>

## 335.17 `CONFIG_HAS_CPU_FREQ`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 SoC 具有表明支持 CPU 频率调整（CPU frequency scaling）的 DTS 属性，则由 SoC 启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_MCXN236
CONFIG_SOC_MIMX9131
CONFIG_SOC_MIMX9352_A55
CONFIG_SOC_POSIX
```

**定义位置（Location）**：[`subsys/cpu_freq/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_MIMX9131`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX9131)、[`CONFIG_SOC_MIMX9352_A55`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX9352_A55)、[`CONFIG_SOC_POSIX`](P287_soc_native_配置项参考.md#CONFIG_SOC_POSIX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MCXN236`。

<!-- kconfig-navigation -->

[上一章](P334_subsys_console_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P336_subsys_crc_配置项参考.md)
