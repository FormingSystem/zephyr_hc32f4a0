---
id: learning.zephyr-docs.kconfig-reference.page-415
title: "`subsys/precision_timing`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第415章\_`subsys/precision_timing`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/precision_timing` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PRECISION_TIMING"></a>

## 415.1 `CONFIG_PRECISION_TIMING`

**提示（Prompt）**：精密计时基础设施（Precision timing infrastructure）

**说明（Help）**

启用不依赖具体协议的精密时间运算（Precision time arithmetic）、时钟操作（Clock operation）及可复用的比例积分控制器（Proportional-Integral controller，PI）。按 Zephyr API 生命周期定义，此 API 尚处于实验阶段（Experimental），仍可能改变。该子系统是 PTP、gPTP 等协议的基础组件，不会改变这些协议本身的成熟度。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_NET_GPTP
CONFIG_PTP
```

**定义位置（Location）**：[`subsys/precision_timing/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/precision_timing/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)。

<a id="CONFIG_PRECISION_TIMING_PI_KI"></a>

## 415.2 `CONFIG_PRECISION_TIMING_PI_KI`

**提示（Prompt）**：PI 控制器积分增益（Integral gain），以千分之一表示

**说明（Help）**

PTP 和 gPTP 时钟 PI 控制器使用的积分增益（Integral gain），以千分之一表示。例如，300 对应增益 0.3。默认值适用于约 1 秒的 Sync 间隔；更短的同步间隔可能需要更小增益，以避免振荡（Oscillation）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PRECISION_TIMING
```

**默认值（Defaults）**

```text
300
```

**取值范围（Ranges）**

```text
[0, 10000]
```

**定义位置（Location）**：[`subsys/precision_timing/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/precision_timing/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 精密计时基础设施（Precision timing infrastructure）

**配置项引用（Symbol References）**：[`CONFIG_PRECISION_TIMING`](P415_subsys_precision_timing_配置项参考.md#CONFIG_PRECISION_TIMING)。

<a id="CONFIG_PRECISION_TIMING_PI_KP"></a>

## 415.3 `CONFIG_PRECISION_TIMING_PI_KP`

**提示（Prompt）**：PI 控制器比例增益（Proportional gain），以千分之一表示

**说明（Help）**

PTP 和 gPTP 时钟 PI 控制器使用的比例增益（Proportional gain），以千分之一表示。例如，700 对应增益 0.7。默认值适用于约 1 秒的 Sync 间隔；更短的同步间隔可能需要更小增益，以避免振荡（Oscillation）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PRECISION_TIMING
```

**默认值（Defaults）**

```text
700
```

**取值范围（Ranges）**

```text
[0, 10000]
```

**定义位置（Location）**：[`subsys/precision_timing/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/precision_timing/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 精密计时基础设施（Precision timing infrastructure）

**配置项引用（Symbol References）**：[`CONFIG_PRECISION_TIMING`](P415_subsys_precision_timing_配置项参考.md#CONFIG_PRECISION_TIMING)。

<!-- kconfig-navigation -->

[上一章](P414_subsys_portability_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P416_subsys_profiling_配置项参考.md)
