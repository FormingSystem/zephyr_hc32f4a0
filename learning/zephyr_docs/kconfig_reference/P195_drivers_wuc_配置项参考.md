---
id: learning.zephyr-docs.kconfig-reference.page-195
title: "`drivers/wuc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第195章\_`drivers/wuc`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/wuc` 的 5 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_WUC"></a>

## 195.1 `CONFIG_WUC`

**提示（Prompt）**：唤醒控制器驱动（Wakeup Controller drivers）

**说明（Help）**

启用唤醒控制器驱动配置（wakeup controller driver configuration）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_MCXA1X3
CONFIG_SOC_SERIES_MCXA1X6
CONFIG_SOC_SERIES_MCXAXX6
CONFIG_SOC_SERIES_MCXAXX4
CONFIG_SOC_SERIES_MCXAXX7
CONFIG_SOC_MCXN947_CPU0
CONFIG_SOC_MCXN547_CPU0
CONFIG_SOC_MCXN236
CONFIG_SOC_MIMXRT798S_CM33_CPU0
```

**定义位置（Location）**：[`drivers/wuc/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wuc/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MCXA1X3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXA1X3)、[`CONFIG_SOC_SERIES_MCXA1X6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXA1X6)、[`CONFIG_SOC_SERIES_MCXAXX6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX6)、[`CONFIG_SOC_SERIES_MCXAXX4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX4)、[`CONFIG_SOC_SERIES_MCXAXX7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXAXX7)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)、[`CONFIG_SOC_MCXN236`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN236)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_MCXA1X3`、`CONFIG_SOC_SERIES_MCXA1X6`、`CONFIG_SOC_SERIES_MCXAXX6`、`CONFIG_SOC_SERIES_MCXAXX4`、`CONFIG_SOC_SERIES_MCXAXX7`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`、`CONFIG_SOC_MCXN236`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`。

<a id="CONFIG_WUC_INIT_PRIORITY"></a>

## 195.2 `CONFIG_WUC_INIT_PRIORITY`

**提示（Prompt）**：唤醒控制器初始化优先级（init priority）

**说明（Help）**

唤醒控制器设备驱动（wakeup controller device driver）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WUC
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/wuc/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wuc/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 唤醒控制器驱动（Wakeup Controller drivers）

**配置项引用（Symbol References）**：[`CONFIG_WUC`](P195_drivers_wuc_配置项参考.md#CONFIG_WUC)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_WUC_MCUX_LLWU"></a>

## 195.3 `CONFIG_WUC_MCUX_LLWU`

**提示（Prompt）**：NXP 低漏电唤醒单元（Low Leakage Wakeup Unit）

**说明（Help）**

启用 NXP 低漏电唤醒单元（Low Leakage Wakeup Unit，LLWU）唤醒控制器驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LLWU_ENABLED && CONFIG_WUC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wuc/Kconfig.mcux_wuc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wuc/Kconfig.mcux_wuc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 唤醒控制器驱动（Wakeup Controller drivers）

**配置项引用（Symbol References）**：[`CONFIG_WUC`](P195_drivers_wuc_配置项参考.md#CONFIG_WUC)。

<a id="CONFIG_WUC_MCUX_SLEEPCON"></a>

## 195.4 `CONFIG_WUC_MCUX_SLEEPCON`

**提示（Prompt）**：NXP SLEEPCON 唤醒控制（wakeup control）

**说明（Help）**

启用以 NXP 睡眠控制器（Sleep Controller，SLEEPCON）充当唤醒控制器的驱动支持。SLEEPCON 的 `WAKEUPEN` 寄存器选择哪些外设中断可以使 CPU 从低功耗模式（low-power modes）唤醒。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SLEEPCON_WUC_ENABLED && CONFIG_WUC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wuc/Kconfig.mcux_wuc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wuc/Kconfig.mcux_wuc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 唤醒控制器驱动（Wakeup Controller drivers）

**配置项引用（Symbol References）**：[`CONFIG_WUC`](P195_drivers_wuc_配置项参考.md#CONFIG_WUC)。

<a id="CONFIG_WUC_MCUX_WUU"></a>

## 195.5 `CONFIG_WUC_MCUX_WUU`

**提示（Prompt）**：NXP WUU 唤醒控制（wakeup control）

**说明（Help）**

启用 NXP 唤醒单元（Wakeup Unit，WUU）唤醒控制器驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_WUC_WUU_ENABLED && CONFIG_WUC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wuc/Kconfig.mcux_wuc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wuc/Kconfig.mcux_wuc#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 唤醒控制器驱动（Wakeup Controller drivers）

**配置项引用（Symbol References）**：[`CONFIG_WUC`](P195_drivers_wuc_配置项参考.md#CONFIG_WUC)。

<!-- kconfig-navigation -->

[上一章](P194_drivers_wifi_配置项参考_7.md) · [返回大纲](大纲.md) · [下一章](P196_drivers_xen_配置项参考.md)
