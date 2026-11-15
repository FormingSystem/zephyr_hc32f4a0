---
id: learning.zephyr-docs.kconfig-reference.page-140
title: "`drivers/psi5`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第140章\_`drivers/psi5`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/psi5` 的 3 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PSI5"></a>

## 140.1 `CONFIG_PSI5`

**提示（Prompt）**：外设传感器接口（Peripheral Sensor Interface，PSI5）驱动

**说明（Help）**

启用 PSI5 驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/psi5/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/psi5/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_PSI5_INIT_PRIORITY"></a>

## 140.2 `CONFIG_PSI5_INIT_PRIORITY`

**提示（Prompt）**：PSI5 驱动初始化优先级

**说明（Help）**

PSI5 驱动设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PSI5
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/psi5/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/psi5/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外设传感器接口（Peripheral Sensor Interface，PSI5）驱动

**配置项引用（Symbol References）**：[`CONFIG_PSI5`](P140_drivers_psi5_配置项参考.md#CONFIG_PSI5)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_PSI5_NXP_S32"></a>

## 140.3 `CONFIG_PSI5_NXP_S32`

**提示（Prompt）**：NXP S32 PSI5 驱动

**说明（Help）**

启用 NXP S32 PSI5 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_PSI5_ENABLED && CONFIG_PSI5
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL if n
```

**定义位置（Location）**：[`drivers/psi5/Kconfig.nxp_s32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/psi5/Kconfig.nxp_s32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外设传感器接口（Peripheral Sensor Interface，PSI5）驱动

**配置项引用（Symbol References）**：[`CONFIG_PSI5`](P140_drivers_psi5_配置项参考.md#CONFIG_PSI5)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<!-- kconfig-navigation -->

[上一章](P139_drivers_ps2_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P141_drivers_ptp_clock_配置项参考.md)
