---
id: learning.zephyr-docs.kconfig-reference.page-116
title: "`drivers/lin`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第116章\_`drivers/lin`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/lin` 的 7 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LIN"></a>

## 116.1 `CONFIG_LIN`

**提示（Prompt）**：局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】

**说明（Help）**

局域互连网络（Local Interconnect Network，LIN）驱动子系统。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/lin/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lin/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_LIN_AUTO_SYNCHRONIZATION"></a>

## 116.2 `CONFIG_LIN_AUTO_SYNCHRONIZATION`

**提示（Prompt）**：LIN 自动同步（Auto Synchronization）

**说明（Help）**

启用 LIN 帧自动同步。禁用时，驱动不处理帧同步（Frame Synchronization）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/lin/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lin/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_LIN`](P116_drivers_lin_配置项参考.md#CONFIG_LIN)。

<a id="CONFIG_LIN_INIT_PRIORITY"></a>

## 116.3 `CONFIG_LIN_INIT_PRIORITY`

**提示（Prompt）**：LIN 驱动初始化优先级（Initialization Priority）

**说明（Help）**

LIN 驱动设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIN
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/lin/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lin/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_LIN`](P116_drivers_lin_配置项参考.md#CONFIG_LIN)。

<a id="CONFIG_LIN_RENESAS_RA"></a>

## 116.4 `CONFIG_LIN_RENESAS_RA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Renesas RA 系列 LIN 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LIN
```

**被选择（Selected by）**

```text
CONFIG_LIN_RENESAS_RA_SCI_B
```

**定义位置（Location）**：[`drivers/lin/renesas/ra/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lin/renesas/ra/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_LIN`](P116_drivers_lin_配置项参考.md#CONFIG_LIN)、[`CONFIG_LIN_RENESAS_RA_SCI_B`](P116_drivers_lin_配置项参考.md#CONFIG_LIN_RENESAS_RA_SCI_B)。

<a id="CONFIG_LIN_RENESAS_RA_SCI_B"></a>

## 116.5 `CONFIG_LIN_RENESAS_RA_SCI_B`

**提示（Prompt）**：Renesas RA LIN SCI_B

**说明（Help）**

启用 Renesas RA LIN SCI B 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_LIN_SCI_B_ENABLED && CONFIG_LIN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LIN_RENESAS_RA
CONFIG_USE_RA_FSP_SCI_B_LIN
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/lin/renesas/ra/Kconfig.renesas_ra:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lin/renesas/ra/Kconfig.renesas_ra#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_LIN`](P116_drivers_lin_配置项参考.md#CONFIG_LIN)、[`CONFIG_LIN_RENESAS_RA`](P116_drivers_lin_配置项参考.md#CONFIG_LIN_RENESAS_RA)、[`CONFIG_USE_RA_FSP_SCI_B_LIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SCI_B_LIN)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_LIN_TRANSCEIVER_GPIO"></a>

## 116.6 `CONFIG_LIN_TRANSCEIVER_GPIO`

**提示（Prompt）**：GPIO 控制的 LIN 收发器（Transceiver）

**说明（Help）**

启用 GPIO 控制的 LIN 收发器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LIN_TRANSCEIVER_GPIO_ENABLED && CONFIG_LIN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/lin/transceiver/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lin/transceiver/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】 → LIN 收发器（Transceiver）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIN`](P116_drivers_lin_配置项参考.md#CONFIG_LIN)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_LIN_TRANSCEIVER_INIT_PRIORITY"></a>

## 116.7 `CONFIG_LIN_TRANSCEIVER_INIT_PRIORITY`

**提示（Prompt）**：LIN 收发器驱动初始化优先级（Initialization Priority）

**说明（Help）**

LIN 收发器设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LIN
```

**默认值（Defaults）**

```text
45
```

**定义位置（Location）**：[`drivers/lin/transceiver/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/lin/transceiver/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 局域互连网络（Local Interconnect Network，LIN）驱动【实验性（EXPERIMENTAL）】 → LIN 收发器（Transceiver）驱动

**配置项引用（Symbol References）**：[`CONFIG_LIN`](P116_drivers_lin_配置项参考.md#CONFIG_LIN)。

<!-- kconfig-navigation -->

[上一章](P115_drivers_led_strip_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P117_drivers_lora_配置项参考.md)
