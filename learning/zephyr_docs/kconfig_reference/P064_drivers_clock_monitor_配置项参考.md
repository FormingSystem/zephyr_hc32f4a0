---
id: learning.zephyr-docs.kconfig-reference.page-64
title: "`drivers/clock_monitor`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第64章\_`drivers/clock_monitor`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/clock_monitor` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CLOCK_MONITOR"></a>

## 64.1 `CONFIG_CLOCK_MONITOR`

**提示（Prompt）**：时钟监测驱动（Clock Monitor Drivers）

**说明（Help）**

启用时钟监测（Clock Monitor）驱动类别。具体时钟监测外设的各个后端驱动（Back-End Driver），由下方引入的各自 Kconfig 符号选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/clock_monitor/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_monitor/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_CLOCK_MONITOR_INIT_PRIORITY"></a>

## 64.2 `CONFIG_CLOCK_MONITOR_INIT_PRIORITY`

**提示（Prompt）**：时钟监测初始化优先级（clock_monitor Init Priority）

**说明（Help）**

时钟监测（clock_monitor）后端驱动的设备初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_MONITOR
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/clock_monitor/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_monitor/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟监测驱动（Clock Monitor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_MONITOR`](P064_drivers_clock_monitor_配置项参考.md#CONFIG_CLOCK_MONITOR)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_CLOCK_MONITOR_NXP_CMU_FC"></a>

## 64.3 `CONFIG_CLOCK_MONITOR_NXP_CMU_FC`

**提示（Prompt）**：恩智浦 CMU_FC 频率检查驱动（NXP Frequency Check Driver）

**说明（Help）**

封装 MCUX SDK 的 `fsl_cmu_fc` 硬件抽象层（HAL）的 Zephyr 时钟监测（clock_monitor）后端，提供用于时钟频率检查（Frequency Check）的窗口模式（WINDOW）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_CMU_FC_ENABLED && CONFIG_CLOCK_MONITOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_monitor/Kconfig.nxp_cmu_fc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_monitor/Kconfig.nxp_cmu_fc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟监测驱动（Clock Monitor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_MONITOR`](P064_drivers_clock_monitor_配置项参考.md#CONFIG_CLOCK_MONITOR)。

<a id="CONFIG_CLOCK_MONITOR_NXP_CMU_FM"></a>

## 64.4 `CONFIG_CLOCK_MONITOR_NXP_CMU_FM`

**提示（Prompt）**：恩智浦 CMU_FM 频率计驱动（NXP Frequency Meter Driver）

**说明（Help）**

封装 MCUX SDK 的 `fsl_cmu_fm` 硬件抽象层（HAL）的 Zephyr 时钟监测（clock_monitor）后端，提供用于时钟频率测量的计量模式（METER）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_CMU_FM_ENABLED && CONFIG_CLOCK_MONITOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/clock_monitor/Kconfig.nxp_cmu_fm:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_monitor/Kconfig.nxp_cmu_fm#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟监测驱动（Clock Monitor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_MONITOR`](P064_drivers_clock_monitor_配置项参考.md#CONFIG_CLOCK_MONITOR)。

<a id="CONFIG_CLOCK_MONITOR_NXP_FMEAS"></a>

## 64.5 `CONFIG_CLOCK_MONITOR_NXP_FMEAS`

**提示（Prompt）**：恩智浦 BASIC FREQME 频率测量驱动，fmeas（NXP Frequency Measurement Driver）

**说明（Help）**

恩智浦（NXP）基本频率测量模块（BASIC Frequency Measurement，FREQME）的 Zephyr 时钟监测（clock_monitor）后端，封装 MCUX SDK 的 `fsl_fmeas` 硬件抽象层（HAL）。

这是 RT6xx／RT5xx／RW6xx 上仅有一个 `FREQMECTRL` 寄存器、没有中断线的变体；只支持单次测量模式（MEASURE / One-Shot），通过工作队列（Workqueue）轮询完成状态。参考时钟和目标时钟通过 INPUTMUX 多路选择器子系统（Mux Subsystem）路由，参考频率从 `clock_control` 查询。测量窗口由硬件／HAL 固定为 `2^20` 个参考时钟周期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FMEAS_ENABLED && CONFIG_CLOCK_MONITOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MUX
CONFIG_MUX_NXP_INPUTMUX
```

**定义位置（Location）**：[`drivers/clock_monitor/Kconfig.nxp_fmeas:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_monitor/Kconfig.nxp_fmeas#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟监测驱动（Clock Monitor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_MONITOR`](P064_drivers_clock_monitor_配置项参考.md#CONFIG_CLOCK_MONITOR)、[`CONFIG_MUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MUX)、[`CONFIG_MUX_NXP_INPUTMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MUX_NXP_INPUTMUX)。

<a id="CONFIG_CLOCK_MONITOR_NXP_FREQME"></a>

## 64.6 `CONFIG_CLOCK_MONITOR_NXP_FREQME`

**提示（Prompt）**：恩智浦 FREQME 频率测量驱动（NXP Frequency Measurement Driver）

**说明（Help）**

恩智浦（NXP）FREQME 外设的 Zephyr 时钟监测（clock_monitor）后端。参考时钟和目标时钟通过 INPUTMUX 多路选择器子系统（Mux Subsystem）路由，参考频率从 `clock_control` 查询。

基于 FREQME 的频率测量工作模式（Frequency-Measurement Operate Mode），同时支持单次测量模式（MEASURE / One-Shot）和连续最小／最大阈值窗口模式（WINDOW / Continuous MIN/MAX Threshold）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FREQME_ENABLED && CONFIG_CLOCK_MONITOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MUX
CONFIG_MUX_NXP_INPUTMUX
```

**定义位置（Location）**：[`drivers/clock_monitor/Kconfig.nxp_freqme:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_monitor/Kconfig.nxp_freqme#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时钟监测驱动（Clock Monitor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_MONITOR`](P064_drivers_clock_monitor_配置项参考.md#CONFIG_CLOCK_MONITOR)、[`CONFIG_MUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MUX)、[`CONFIG_MUX_NXP_INPUTMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MUX_NXP_INPUTMUX)。

<!-- kconfig-navigation -->

[上一章](P063_drivers_clock_control_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P065_drivers_comparator_配置项参考.md)
