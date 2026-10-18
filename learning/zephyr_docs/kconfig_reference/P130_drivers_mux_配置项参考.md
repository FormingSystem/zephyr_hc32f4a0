---
id: learning.zephyr-docs.kconfig-reference.page-130
title: "`drivers/mux`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第130章\_`drivers/mux`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/mux` 的 9 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MUX"></a>

## 130.1 `CONFIG_MUX`

**提示（Prompt）**：多路复用器（Multiplexer，MUX）驱动

**说明（Help）**

通用多路复用控制器子系统，为信号路由器提供统一 API（`mux_control_set`、`mux_state_apply`）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CLOCK_MONITOR_NXP_FREQME
CONFIG_CLOCK_MONITOR_NXP_FMEAS
CONFIG_COUNTER_MCUX_CTIMER
CONFIG_PWM_MCUX_CTIMER
CONFIG_PWM_MCUX_SCTIMER
CONFIG_EQDC_MCUX
CONFIG_QDC_MCUX
CONFIG_QDEC_MCUX
```

**定义位置（Location）**：[`drivers/mux/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mux/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_MONITOR_NXP_FREQME`](P064_drivers_clock_monitor_配置项参考.md#CONFIG_CLOCK_MONITOR_NXP_FREQME)、[`CONFIG_CLOCK_MONITOR_NXP_FMEAS`](P064_drivers_clock_monitor_配置项参考.md#CONFIG_CLOCK_MONITOR_NXP_FMEAS)、[`CONFIG_COUNTER_MCUX_CTIMER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER_MCUX_CTIMER)、[`CONFIG_PWM_MCUX_CTIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_MCUX_CTIMER)、[`CONFIG_PWM_MCUX_SCTIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_MCUX_SCTIMER)、[`CONFIG_EQDC_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EQDC_MCUX)、[`CONFIG_QDC_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QDC_MCUX)、[`CONFIG_QDEC_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QDEC_MCUX)。

<a id="CONFIG_MUX_ADI_ADGM3121"></a>

## 130.2 `CONFIG_MUX_ADI_ADGM3121`

**提示（Prompt）**：ADI ADGM3121 微机电系统（MEMS）开关 MUX 驱动

**说明（Help）**

将 ADI ADGM3121 双刀双掷（DPDT）MEMS 开关作为 MUX 控制器启用。四个开关作为单条控制线公开，其状态为 4 位开关位掩码（Bitmask），其中位 i 对应 `SW(i+1)`。支持 SPI（`adi,adgm3121`）和并行 GPIO（`adi,adgm3121-gpio`）两种控制模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ADI_ADGM3121_ENABLED || DT_HAS_ADI_ADGM3121_GPIO_ENABLED) && CONFIG_MUX
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI if DT_HAS_ADI_ADGM3121_ENABLED
CONFIG_GPIO if DT_HAS_ADI_ADGM3121_GPIO_ENABLED
```

**定义位置（Location）**：[`drivers/mux/Kconfig.adi_adgm3121:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mux/Kconfig.adi_adgm3121#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_MUX_ADI_ADGM3121_INIT_PRIORITY"></a>

## 130.3 `CONFIG_MUX_ADI_ADGM3121_INIT_PRIORITY`

**提示（Prompt）**：ADGM3121 初始化优先级

**说明（Help）**

设备初始化优先级。与片上 MUX 后端不同，ADGM3121 连接在总线上，因此必须晚于其 SPI 或 GPIO 控制器初始化（`SPI_INIT_PRIORITY` 默认为 `KERNEL_INIT_PRIORITY_DEVICE`），同时仍要早于任何引用它的 MUX 使用方。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MUX_ADI_ADGM3121 && CONFIG_MUX
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：[`drivers/mux/Kconfig.adi_adgm3121:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mux/Kconfig.adi_adgm3121#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动 → ADI ADGM3121 微机电系统（MEMS）开关 MUX 驱动

**配置项引用（Symbol References）**：[`CONFIG_MUX_ADI_ADGM3121`](P130_drivers_mux_配置项参考.md#CONFIG_MUX_ADI_ADGM3121)、[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)。

<a id="CONFIG_MUX_GPIO"></a>

## 130.4 `CONFIG_MUX_GPIO`

**提示（Prompt）**：基于 GPIO 的 MUX 驱动

**说明（Help）**

启用基于 GPIO 的多路复用器驱动。状态值以二进制位模式编码到 `mux-gpios` 属性列出的 GPIO 线上。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GPIO_MUX_ENABLED && CONFIG_GPIO && CONFIG_MUX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mux/Kconfig.gpio:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mux/Kconfig.gpio#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)。

<a id="CONFIG_MUX_INIT_PRIORITY"></a>

## 130.5 `CONFIG_MUX_INIT_PRIORITY`

**提示（Prompt）**：MUX 驱动初始化优先级

**说明（Help）**

MUX 控制器驱动的初始化优先级。MUX 控制器是传感器、PWM 等使用方通过设备树依赖的提供者，因此必须早于任何使用方初始化，即优先级数值更低，例如低于 `KERNEL_INIT_PRIORITY_DEVICE`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MUX
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`drivers/mux/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mux/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)。

<a id="CONFIG_MUX_MAX_CELLS"></a>

## 130.6 `CONFIG_MUX_MAX_CELLS`

**提示（Prompt）**：MUX 描述符中寻址单元（Addressing Cells）的最大数量

**说明（Help）**

单个 `mux-controls` 或 `mux-states` 描述符（Specifier）中寻址单元长度的上限。用户空间系统调用处理程序据此在内核侧为单元数组分配固定大小副本，避免可变长度数组（VLA），并限制从用户空间复制到可信内存的数据量。如果控制器绑定需要更多寻址单元，应增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MUX
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/mux/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mux/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)。

<a id="CONFIG_MUX_NXP_INPUTMUX"></a>

## 130.7 `CONFIG_MUX_NXP_INPUTMUX`

**提示（Prompt）**：NXP INPUTMUX MUX 驱动

**说明（Help）**

启用基于 NXP INPUTMUX 的多路复用器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_INPUTMUX_ENABLED && CONFIG_MUX
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NXP_INPUTMUX
```

**被选择（Selected by）**

```text
CONFIG_CLOCK_MONITOR_NXP_FREQME
CONFIG_CLOCK_MONITOR_NXP_FMEAS
```

**定义位置（Location）**：[`drivers/mux/Kconfig.nxp_inputmux:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mux/Kconfig.nxp_inputmux#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)、[`CONFIG_NXP_INPUTMUX`](P123_drivers_misc_配置项参考.md#CONFIG_NXP_INPUTMUX)、[`CONFIG_CLOCK_MONITOR_NXP_FREQME`](P064_drivers_clock_monitor_配置项参考.md#CONFIG_CLOCK_MONITOR_NXP_FREQME)、[`CONFIG_CLOCK_MONITOR_NXP_FMEAS`](P064_drivers_clock_monitor_配置项参考.md#CONFIG_CLOCK_MONITOR_NXP_FMEAS)。

<a id="CONFIG_MUX_NXP_TRGMUX"></a>

## 130.8 `CONFIG_MUX_NXP_TRGMUX`

**提示（Prompt）**：NXP TRGMUX MUX 驱动

**说明（Help）**

启用基于 NXP TRGMUX 的多路复用器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_TRGMUX_ENABLED && CONFIG_MUX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mux/Kconfig.nxp_trgmux:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mux/Kconfig.nxp_trgmux#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)。

<a id="CONFIG_MUX_NXP_XBAR"></a>

## 130.9 `CONFIG_MUX_NXP_XBAR`

**提示（Prompt）**：NXP MCUX XBAR MUX 驱动

**说明（Help）**

启用 NXP MCUX XBAR（交叉开关，Cross-bar Switch）多路复用器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MCUX_XBAR_ENABLED && CONFIG_MUX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mux/Kconfig.nxp_xbar:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mux/Kconfig.nxp_xbar#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)。

<!-- kconfig-navigation -->

[上一章](P129_drivers_mspi_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P131_drivers_net_配置项参考.md)
