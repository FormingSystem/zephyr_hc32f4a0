---
id: learning.zephyr-docs.kconfig-reference.page-175
title: "`drivers/syscon`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第175章\_`drivers/syscon`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/syscon` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SYSCON"></a>

## 175.1 `CONFIG_SYSCON`

**提示（Prompt）**：系统控制器（System Controller，SYSCON）驱动

**说明（Help）**

系统控制器（System Controller，SYSCON）驱动。系统控制器节点表示一个包含各种杂项寄存器的寄存器区域；这些寄存器在功能上不够集中，无法归为某种特定设备。典型用途是其他节点的驱动或平台特定代码取得对 `syscon` 节点的引用，并从中提取信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AST10X0
CONFIG_SOC_SERIES_XC7ZXXX
CONFIG_SOC_SERIES_XC7ZXXXS
CONFIG_CLOCK_CONTROL_AESC
CONFIG_CLOCK_CONTROL_EM32_AHB
CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS
CONFIG_GPIO_EM32
CONFIG_PINCTRL_EM32
CONFIG_PWM_TI_AM3352_EHRPWM
CONFIG_REGULATOR_RTS5817
CONFIG_RTC_MCHP_G2
```

**定义位置（Location）**：[`drivers/syscon/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/syscon/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AST10X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AST10X0)、[`CONFIG_SOC_SERIES_XC7ZXXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XC7ZXXX)、[`CONFIG_SOC_SERIES_XC7ZXXXS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XC7ZXXXS)、[`CONFIG_CLOCK_CONTROL_AESC`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_AESC)、[`CONFIG_CLOCK_CONTROL_EM32_AHB`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_EM32_AHB)、[`CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_ROCKCHIP_DWC_ETHER_QOS)、[`CONFIG_GPIO_EM32`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_EM32)、[`CONFIG_PINCTRL_EM32`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL_EM32)、[`CONFIG_PWM_TI_AM3352_EHRPWM`](P143_drivers_pwm_配置项参考.md#CONFIG_PWM_TI_AM3352_EHRPWM)、[`CONFIG_REGULATOR_RTS5817`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR_RTS5817)、[`CONFIG_RTC_MCHP_G2`](P147_drivers_rtc_配置项参考.md#CONFIG_RTC_MCHP_G2)。

<a id="CONFIG_SYSCON_GENERIC"></a>

## 175.2 `CONFIG_SYSCON_GENERIC`

**提示（Prompt）**：通用系统控制器（Generic SYSCON）驱动

**说明（Help）**

启用通用系统控制器（System Controller，SYSCON）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SYSCON_ENABLED && CONFIG_SYSCON
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/syscon/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/syscon/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统控制器（System Controller，SYSCON）驱动

**配置项引用（Symbol References）**：[`CONFIG_SYSCON`](P175_drivers_syscon_配置项参考.md#CONFIG_SYSCON)。

<a id="CONFIG_SYSCON_INIT_PRIORITY"></a>

## 175.3 `CONFIG_SYSCON_INIT_PRIORITY`

**提示（Prompt）**：系统控制器（SYSCON）驱动初始化优先级

**说明（Help）**

此选项控制 `syscon` 设备初始化的优先级。较高的初始化优先级可确保设备在启动流程中较早初始化；此处指初始化次序，不应直接理解为数值越大越早。如果不确定，请保留默认值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SYSCON
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/syscon/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/syscon/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统控制器（System Controller，SYSCON）驱动

**配置项引用（Symbol References）**：[`CONFIG_SYSCON`](P175_drivers_syscon_配置项参考.md#CONFIG_SYSCON)。

<a id="CONFIG_SYSCON_SHELL"></a>

## 175.4 `CONFIG_SYSCON_SHELL`

**提示（Prompt）**：系统控制器命令行（SYSCON Shell）

**说明（Help）**

启用包含 SYSCON 相关命令的系统控制器命令行（SYSCON Shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_SYSCON
```

**定义位置（Location）**：[`drivers/syscon/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/syscon/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统控制器（System Controller，SYSCON）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SYSCON`](P175_drivers_syscon_配置项参考.md#CONFIG_SYSCON)。

<!-- kconfig-navigation -->

[上一章](P174_drivers_stepper_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P176_drivers_tee_配置项参考.md)
