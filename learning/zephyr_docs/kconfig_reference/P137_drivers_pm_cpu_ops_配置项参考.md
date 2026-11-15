---
id: learning.zephyr-docs.kconfig-reference.page-137
title: "`drivers/pm_cpu_ops`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第137章\_`drivers/pm_cpu_ops`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/pm_cpu_ops` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PM_CPU_OPS"></a>

## 137.1 `CONFIG_PM_CPU_OPS`

**提示（Prompt）**：CPU 电源管理（Power Management）驱动

**说明（Help）**

启用 CPU 电源管理驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/pm_cpu_ops/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pm_cpu_ops/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_PM_CPU_OPS_FVP"></a>

## 137.2 `CONFIG_PM_CPU_OPS_FVP`

**提示（Prompt）**：Arm FVP CPU 电源管理支持

**说明（Help）**

如果希望 Zephyr 在不使用 PSCI 的情况下，支持 Arm 固定虚拟平台（Fixed Virtual Platform，FVP）上的 CPU 电源管理操作，请选 Y。此驱动直接控制 FVP 电源控制器和 V2M 系统寄存器，用于 CPU 上电与系统复位操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_FVP_PWRC_ENABLED && !CONFIG_PM_CPU_OPS_PSCI && CONFIG_PM_CPU_OPS
```

**默认值（Defaults）**

```text
y if CONFIG_SMP
```

**主动选择（Selects）**

```text
CONFIG_PM_CPU_OPS_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/pm_cpu_ops/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pm_cpu_ops/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → CPU 电源管理（Power Management）驱动

**配置项引用（Symbol References）**：[`CONFIG_PM_CPU_OPS_PSCI`](P137_drivers_pm_cpu_ops_配置项参考.md#CONFIG_PM_CPU_OPS_PSCI)、[`CONFIG_PM_CPU_OPS`](P137_drivers_pm_cpu_ops_配置项参考.md#CONFIG_PM_CPU_OPS)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_PM_CPU_OPS_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_CPU_OPS_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PM_CPU_OPS_HAS_DRIVER`。

<a id="CONFIG_PM_CPU_OPS_PSCI"></a>

## 137.3 `CONFIG_PM_CPU_OPS_PSCI`

**提示（Prompt）**：ARM 电源状态协调接口（Power State Coordination Interface，PSCI）支持

**说明（Help）**

如果希望 Zephyr 与实现 PSCI 规范的系统固件通信，执行以 CPU 为中心的电源管理操作，请选 Y。相关操作见 ARM 文档 ARM DEN 0022A《ARM 处理器上的电源状态协调接口系统软件》（Power State Coordination Interface System Software on ARM processors）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ARM_PSCI_0_2_ENABLED || DT_HAS_ARM_PSCI_1_1_ENABLED) && CONFIG_PM_CPU_OPS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PM_CPU_OPS_HAS_DRIVER
CONFIG_HAS_POWEROFF
```

**定义位置（Location）**：[`drivers/pm_cpu_ops/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pm_cpu_ops/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → CPU 电源管理（Power Management）驱动

**配置项引用（Symbol References）**：[`CONFIG_PM_CPU_OPS`](P137_drivers_pm_cpu_ops_配置项参考.md#CONFIG_PM_CPU_OPS)、[`CONFIG_PM_CPU_OPS_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_CPU_OPS_HAS_DRIVER)、[`CONFIG_HAS_POWEROFF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_POWEROFF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PM_CPU_OPS_HAS_DRIVER`。

<a id="CONFIG_PM_CPU_OPS_SBI"></a>

## 137.4 `CONFIG_PM_CPU_OPS_SBI`

**提示（Prompt）**：RISC-V SBI 硬件线程状态管理扩展（Hart State Management Extension）支持

**说明（Help）**

如果通过 RISC-V 监管者二进制接口（SBI）的硬件线程状态管理扩展启动次级 CPU，请选 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_S_MODE_EXTERNAL_SBI && CONFIG_PM_CPU_OPS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PM_CPU_OPS_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/pm_cpu_ops/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pm_cpu_ops/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → CPU 电源管理（Power Management）驱动

**配置项引用（Symbol References）**：[`CONFIG_RISCV_S_MODE_EXTERNAL_SBI`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_S_MODE_EXTERNAL_SBI)、[`CONFIG_PM_CPU_OPS`](P137_drivers_pm_cpu_ops_配置项参考.md#CONFIG_PM_CPU_OPS)、[`CONFIG_PM_CPU_OPS_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_CPU_OPS_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PM_CPU_OPS_HAS_DRIVER`。

<a id="CONFIG_PM_CPU_OPS_SPIN_TABLE"></a>

## 137.5 `CONFIG_PM_CPU_OPS_SPIN_TABLE`

**提示（Prompt）**：ARM 自旋表（Spin-table）启动协议支持

**说明（Help）**

如果通过 ARM64 自旋表（Spin-table）启动协议启动次级 CPU，请选 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PM_CPU_OPS_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/pm_cpu_ops/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pm_cpu_ops/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → CPU 电源管理（Power Management）驱动

**配置项引用（Symbol References）**：[`CONFIG_PM_CPU_OPS_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_CPU_OPS_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PM_CPU_OPS_HAS_DRIVER`。

<a id="CONFIG_PSCI_SHELL"></a>

## 137.6 `CONFIG_PSCI_SHELL`

**提示（Prompt）**：PSCI 接口 Shell 命令支持

**说明（Help）**

需要启用 PSCI 接口 Shell 命令，例如 `warm` 热复位和 `cold` 冷复位命令时，请选 Y。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_PM_CPU_OPS_PSCI && CONFIG_PM_CPU_OPS
```

**定义位置（Location）**：[`drivers/pm_cpu_ops/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pm_cpu_ops/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → CPU 电源管理（Power Management）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_PM_CPU_OPS_PSCI`](P137_drivers_pm_cpu_ops_配置项参考.md#CONFIG_PM_CPU_OPS_PSCI)、[`CONFIG_PM_CPU_OPS`](P137_drivers_pm_cpu_ops_配置项参考.md#CONFIG_PM_CPU_OPS)。

<!-- kconfig-navigation -->

[上一章](P136_drivers_pinctrl_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P138_drivers_power_domain_配置项参考.md)
