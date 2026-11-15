---
id: learning.zephyr-docs.kconfig-reference.page-139
title: "`drivers/ps2`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第139章\_`drivers/ps2`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/ps2` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PS2"></a>

## 139.1 `CONFIG_PS2`

**提示（Prompt）**：PS/2 驱动

**说明（Help）**

在系统配置中纳入 PS/2 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/ps2/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ps2/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_PS2_CHANNEL_INIT_PRIORITY"></a>

## 139.2 `CONFIG_PS2_CHANNEL_INIT_PRIORITY`

**提示（Prompt）**：PS/2 通道驱动初始化优先级

**说明（Help）**

PS/2 通道设备驱动的初始化优先级。原文说明应比 `PS2_INIT_PRIORITY` 更低（Lower），因为 NPCX PS/2 控制器设备驱动应先于通道设备驱动初始化。译注：这里应按原文给出的执行顺序理解，不能直接将 lower 解释为数值更小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PS2_NPCX && CONFIG_PS2
```

**默认值（Defaults）**

```text
41
```

**定义位置（Location）**：[`drivers/ps2/Kconfig.npcx:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ps2/Kconfig.npcx#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PS/2 驱动 → Nuvoton NPCX 嵌入式控制器（EC）PS/2 驱动

**配置项引用（Symbol References）**：[`CONFIG_PS2_NPCX`](P139_drivers_ps2_配置项参考.md#CONFIG_PS2_NPCX)、[`CONFIG_PS2`](P139_drivers_ps2_配置项参考.md#CONFIG_PS2)。

<a id="CONFIG_PS2_INIT_PRIORITY"></a>

## 139.3 `CONFIG_PS2_INIT_PRIORITY`

**提示（Prompt）**：PS/2 驱动初始化优先级

**说明（Help）**

PS/2 设备驱动的初始化优先级。原文说明，目前没有关键组件依赖此优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PS2
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`drivers/ps2/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ps2/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PS/2 驱动

**配置项引用（Symbol References）**：[`CONFIG_PS2`](P139_drivers_ps2_配置项参考.md#CONFIG_PS2)。

<a id="CONFIG_PS2_IT51XXX"></a>

## 139.4 `CONFIG_PS2_IT51XXX`

**提示（Prompt）**：IT51XXX PS/2 驱动

**说明（Help）**

启用 IT51XXX PS/2 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_PS2_ENABLED && CONFIG_PS2
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/ps2/Kconfig.it51xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ps2/Kconfig.it51xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PS/2 驱动

**配置项引用（Symbol References）**：[`CONFIG_PS2`](P139_drivers_ps2_配置项参考.md#CONFIG_PS2)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PS2_NPCX"></a>

## 139.5 `CONFIG_PS2_NPCX`

**提示（Prompt）**：Nuvoton NPCX 嵌入式控制器（EC）PS/2 驱动

**说明（Help）**

启用 NPCX 系列 PS/2 驱动。它提供四个 PS/2 通道，每个通道有两个准双向信号（Quasi-bidirectional Signals），作为与外部键盘、鼠标或其他 PS/2 兼容指点设备直接连接的接口。此驱动还依赖 KBC 8042 键盘控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_PS2_CHANNEL_ENABLED && CONFIG_PS2
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/ps2/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ps2/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PS/2 驱动

**配置项引用（Symbol References）**：[`CONFIG_PS2`](P139_drivers_ps2_配置项参考.md#CONFIG_PS2)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_PS2_XEC"></a>

## 139.6 `CONFIG_PS2_XEC`

**提示（Prompt）**：XEC Microchip PS/2 驱动

**说明（Help）**

启用 Microchip XEC PS/2 IO 驱动。它还依赖 KBC 8042 键盘控制器。注意，MEC15xx 系列有两个控制器，MEC172x 系列有一个。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MICROCHIP_MEC && CONFIG_ESPI_PERIPHERAL_8042_KBC && CONFIG_PS2
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/ps2/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ps2/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → PS/2 驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_ESPI_PERIPHERAL_8042_KBC`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_8042_KBC)、[`CONFIG_PS2`](P139_drivers_ps2_配置项参考.md#CONFIG_PS2)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MICROCHIP_MEC`。

<!-- kconfig-navigation -->

[上一章](P138_drivers_power_domain_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P140_drivers_psi5_配置项参考.md)
