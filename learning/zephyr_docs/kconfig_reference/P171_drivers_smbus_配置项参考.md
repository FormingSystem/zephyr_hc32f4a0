---
id: learning.zephyr-docs.kconfig-reference.page-171
title: "`drivers/smbus`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第171章\_`drivers/smbus`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/smbus` 的 14 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SMBUS"></a>

## 171.1 `CONFIG_SMBUS`

**提示（Prompt）**：系统管理总线（System Management Bus，SMBus）驱动

**说明（Help）**

启用 SMBus 驱动配置

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/smbus/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_SMBUS_INIT_PRIORITY"></a>

## 171.2 `CONFIG_SMBUS_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

SMBus 设备驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SMBUS
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/smbus/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动

**配置项引用（Symbol References）**：[`CONFIG_SMBUS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_SMBUS_INTEL_PCH"></a>

## 171.3 `CONFIG_SMBUS_INTEL_PCH`

**提示（Prompt）**：SMBus Intel PCH 驱动

**说明（Help）**

启用 Intel 平台控制器集线器（Platform Controller Hub，PCH）SMBus 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_PCH_SMBUS_ENABLED && CONFIG_SMBUS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PCIE
CONFIG_DYNAMIC_INTERRUPTS
```

**定义位置（Location）**：[`drivers/smbus/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动

**配置项引用（Symbol References）**：[`CONFIG_SMBUS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS)、[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)。

<a id="CONFIG_SMBUS_INTEL_PCH_ACCESS"></a>

## 171.4 `CONFIG_SMBUS_INTEL_PCH_ACCESS`

**提示（Prompt）**：SMBus 寄存器访问模式（Register Access Mode）

**说明（Help）**

默认 PCH 寄存器访问模式（Register Access Mode）。默认设为 I/O 访问，以同时支持 QEMU Q35 和 Intel 硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMBUS_INTEL_PCH && CONFIG_SMBUS
```

**默认值（Defaults）**

```text
CONFIG_SMBUS_INTEL_PCH_ACCESS_IO
```

**可选项（Choices）**

```text
CONFIG_SMBUS_INTEL_PCH_ACCESS_IO
CONFIG_SMBUS_INTEL_PCH_ACCESS_MMIO
```

**定义位置（Location）**：[`drivers/smbus/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动 → SMBus Intel PCH 驱动

**配置项引用（Symbol References）**：[`CONFIG_SMBUS_INTEL_PCH`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS_INTEL_PCH)、[`CONFIG_SMBUS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS)、[`CONFIG_SMBUS_INTEL_PCH_ACCESS_IO`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS_INTEL_PCH_ACCESS_IO)、[`CONFIG_SMBUS_INTEL_PCH_ACCESS_MMIO`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS_INTEL_PCH_ACCESS_MMIO)。

<a id="CONFIG_SMBUS_INTEL_PCH_ACCESS_IO"></a>

## 171.5 `CONFIG_SMBUS_INTEL_PCH_ACCESS_IO`

**提示（Prompt）**：I/O PCH SMBus 寄存器访问模式

**说明（Help）**

通过输入／输出空间（I/O Space）访问 PCH SMBus 寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SMBUS_INTEL_PCH_ACCESS>
```

**定义位置（Location）**：[`drivers/smbus/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动 → SMBus Intel PCH 驱动 → SMBus 寄存器访问模式（Register Access Mode）

**配置项引用（Symbol References）**：[`CONFIG_SMBUS_INTEL_PCH_ACCESS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS_INTEL_PCH_ACCESS)。

<a id="CONFIG_SMBUS_INTEL_PCH_ACCESS_MMIO"></a>

## 171.6 `CONFIG_SMBUS_INTEL_PCH_ACCESS_MMIO`

**提示（Prompt）**：MMIO PCH SMBus 寄存器访问模式

**说明（Help）**

通过内存映射输入／输出空间（MMIO Space）访问 PCH SMBus 寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SMBUS_INTEL_PCH_ACCESS>
```

**定义位置（Location）**：[`drivers/smbus/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动 → SMBus Intel PCH 驱动 → SMBus 寄存器访问模式（Register Access Mode）

**配置项引用（Symbol References）**：[`CONFIG_SMBUS_INTEL_PCH_ACCESS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS_INTEL_PCH_ACCESS)。

<a id="CONFIG_SMBUS_INTEL_PCH_HOST_NOTIFY"></a>

## 171.7 `CONFIG_SMBUS_INTEL_PCH_HOST_NOTIFY`

**提示（Prompt）**：SMBus Intel PCH 主机通知（Host Notify）支持

**说明（Help）**

支持来自外设的主机通知（Host Notify）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMBUS_INTEL_PCH && CONFIG_SMBUS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/smbus/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动 → SMBus Intel PCH 驱动

**配置项引用（Symbol References）**：[`CONFIG_SMBUS_INTEL_PCH`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS_INTEL_PCH)、[`CONFIG_SMBUS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS)。

<a id="CONFIG_SMBUS_INTEL_PCH_SMBALERT"></a>

## 171.8 `CONFIG_SMBUS_INTEL_PCH_SMBALERT`

**提示（Prompt）**：SMBus Intel PCH SMBALERT 信号支持

**说明（Help）**

支持来自外设的 SMBALERT 信号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMBUS_INTEL_PCH && CONFIG_SMBUS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/smbus/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动 → SMBus Intel PCH 驱动

**配置项引用（Symbol References）**：[`CONFIG_SMBUS_INTEL_PCH`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS_INTEL_PCH)、[`CONFIG_SMBUS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS)。

<a id="CONFIG_SMBUS_ITE_IT51XXX"></a>

## 171.9 `CONFIG_SMBUS_ITE_IT51XXX`

**提示（Prompt）**：ITE SMBus 驱动

**说明（Help）**

启用 ITE SMBus 驱动。支持九个控制器，可在启用或禁用包错误校验（Packet Error Checking，PEC）的情况下执行 SMBus 消息传输。支持的速率为 50 kHz、100 kHz、400 kHz 和 1 MHz，并支持主机通知（Host Notify）命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_SMBUS_ENABLED && CONFIG_SMBUS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/smbus/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动

**配置项引用（Symbol References）**：[`CONFIG_SMBUS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_SMBUS_SHELL"></a>

## 171.10 `CONFIG_SMBUS_SHELL`

**提示（Prompt）**：SMBus 命令行（Shell）

**说明（Help）**

启用 SMBus 命令行（Shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_SMBUS
```

**定义位置（Location）**：[`drivers/smbus/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SMBUS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS)。

<a id="CONFIG_SMBUS_SOFT_PEC"></a>

## 171.11 `CONFIG_SMBUS_SOFT_PEC`

**提示（Prompt）**：SMBus 软件包错误校验（Software PEC）支持

**说明（Help）**

启用软件包错误校验（Packet Error Checking，PEC）支持。这些通用函数可由 SMBus 驱动使用，支持硬件未实现 PEC 的收发器（Transceiver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMBUS
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**被选择（Selected by）**

```text
CONFIG_SMBUS_STM32
```

**定义位置（Location）**：[`drivers/smbus/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动

**配置项引用（Symbol References）**：[`CONFIG_SMBUS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)、[`CONFIG_SMBUS_STM32`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS_STM32)。

<a id="CONFIG_SMBUS_STATS"></a>

## 171.12 `CONFIG_SMBUS_STATS`

**提示（Prompt）**：SMBus 设备统计（Stats）

**说明（Help）**

启用 SMBus 统计（Stats）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STATS && CONFIG_SMBUS
```

**定义位置（Location）**：[`drivers/smbus/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动

**配置项引用（Symbol References）**：[`CONFIG_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS)、[`CONFIG_SMBUS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS)。

<a id="CONFIG_SMBUS_STM32"></a>

## 171.13 `CONFIG_SMBUS_STM32`

**提示（Prompt）**：STM32 SMBus 驱动

**说明（Help）**

启用 STM32 SMBus 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_SMBUS_ENABLED && CONFIG_I2C_STM32 && CONFIG_SMBUS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_SMBUS_SOFT_PEC
```

**定义位置（Location）**：[`drivers/smbus/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动

**配置项引用（Symbol References）**：[`CONFIG_I2C_STM32`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_STM32)、[`CONFIG_SMBUS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SMBUS_SOFT_PEC`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS_SOFT_PEC)。

<a id="CONFIG_SMBUS_STM32_SMBALERT"></a>

## 171.14 `CONFIG_SMBUS_STM32_SMBALERT`

**提示（Prompt）**：SMBus STM32 SMBALERT 信号支持

**说明（Help）**

支持来自外设的 SMBALERT 信号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMBUS_STM32 && CONFIG_SMBUS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/smbus/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/smbus/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统管理总线（System Management Bus，SMBus）驱动 → STM32 SMBus 驱动

**配置项引用（Symbol References）**：[`CONFIG_SMBUS_STM32`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS_STM32)、[`CONFIG_SMBUS`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS)。

<!-- kconfig-navigation -->

[上一章](P170_drivers_sip_svc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P172_drivers_spi_配置项参考_1.md)
