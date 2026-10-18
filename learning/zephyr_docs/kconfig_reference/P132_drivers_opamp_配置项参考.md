---
id: learning.zephyr-docs.kconfig-reference.page-132
title: "`drivers/opamp`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第132章\_`drivers/opamp`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/opamp` 的 7 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_OPAMP"></a>

## 132.1 `CONFIG_OPAMP`

**提示（Prompt）**：运算放大器（Operational Amplifier，Opamp）驱动

**说明（Help）**

启用运算放大器驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/opamp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/opamp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_OPAMP_INFINEON_AUTANALOG_CTB"></a>

## 132.2 `CONFIG_OPAMP_INFINEON_AUTANALOG_CTB`

**提示（Prompt）**：Infineon AutAnalog CTB 运算放大器驱动

**说明（Help）**

启用 Infineon AutAnalog CTB 运算放大器驱动。每个实例提供 CTB 模块中的单个运放（OA0 或 OA1），通过自主控制器（Autonomous Controller）的 STT 实现运行时增益控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_AUTANALOG_CTB_OPAMP_ENABLED && CONFIG_OPAMP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/opamp/Kconfig.infineon_autanalog_ctb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/opamp/Kconfig.infineon_autanalog_ctb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动

**配置项引用（Symbol References）**：[`CONFIG_OPAMP`](P132_drivers_opamp_配置项参考.md#CONFIG_OPAMP)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_OPAMP_INFINEON_AUTANALOG_CTB_INIT_PRIORITY"></a>

## 132.3 `CONFIG_OPAMP_INFINEON_AUTANALOG_CTB_INIT_PRIORITY`

**提示（Prompt）**：Infineon AutAnalog CTB 运放初始化优先级

**说明（Help）**

CTB 运放驱动的初始化优先级。数值必须高于 CTB MFD 初始化优先级（默认 42），即更晚执行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPAMP_INFINEON_AUTANALOG_CTB && CONFIG_OPAMP
```

**默认值（Defaults）**

```text
43
```

**定义位置（Location）**：[`drivers/opamp/Kconfig.infineon_autanalog_ctb:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/opamp/Kconfig.infineon_autanalog_ctb#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动 → Infineon AutAnalog CTB 运算放大器驱动

**配置项引用（Symbol References）**：[`CONFIG_OPAMP_INFINEON_AUTANALOG_CTB`](P132_drivers_opamp_配置项参考.md#CONFIG_OPAMP_INFINEON_AUTANALOG_CTB)、[`CONFIG_OPAMP`](P132_drivers_opamp_配置项参考.md#CONFIG_OPAMP)。

<a id="CONFIG_OPAMP_INIT_PRIORITY"></a>

## 132.4 `CONFIG_OPAMP_INIT_PRIORITY`

**提示（Prompt）**：OPAMP 初始化优先级

**说明（Help）**

运算放大器设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPAMP
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/opamp/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/opamp/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动

**配置项引用（Symbol References）**：[`CONFIG_OPAMP`](P132_drivers_opamp_配置项参考.md#CONFIG_OPAMP)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_OPAMP_MCUX_OPAMP"></a>

## 132.5 `CONFIG_OPAMP_MCUX_OPAMP`

**提示（Prompt）**：NXP MCUX 运算放大器（Opamp）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_OPAMP_ENABLED && CONFIG_OPAMP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_RESET if CONFIG_SOC_FAMILY_LPC
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/opamp/Kconfig.mcux_opamp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/opamp/Kconfig.mcux_opamp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动

**配置项引用（Symbol References）**：[`CONFIG_OPAMP`](P132_drivers_opamp_配置项参考.md#CONFIG_OPAMP)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_LPC`。

<a id="CONFIG_OPAMP_MCUX_OPAMP_FAST"></a>

## 132.6 `CONFIG_OPAMP_MCUX_OPAMP_FAST`

**提示（Prompt）**：NXP MCUX Opamp_fast 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_OPAMP_FAST_ENABLED && CONFIG_OPAMP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/opamp/Kconfig.mcux_opamp_fast:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/opamp/Kconfig.mcux_opamp_fast#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动

**配置项引用（Symbol References）**：[`CONFIG_OPAMP`](P132_drivers_opamp_配置项参考.md#CONFIG_OPAMP)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_OPAMP_STM32"></a>

## 132.7 `CONFIG_OPAMP_STM32`

**提示（Prompt）**：STM32 OPAMP 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_OPAMP_ENABLED && CONFIG_OPAMP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/opamp/Kconfig.stm32_opamp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/opamp/Kconfig.stm32_opamp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 运算放大器（Operational Amplifier，Opamp）驱动

**配置项引用（Symbol References）**：[`CONFIG_OPAMP`](P132_drivers_opamp_配置项参考.md#CONFIG_OPAMP)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<!-- kconfig-navigation -->

[上一章](P131_drivers_net_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P133_drivers_otp_配置项参考.md)
