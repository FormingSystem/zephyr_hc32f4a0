---
id: learning.zephyr-docs.kconfig-reference.page-174
title: "`drivers/stepper`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第174章\_`drivers/stepper`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/stepper` 的 33 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_A4979_STEPPER"></a>

## 174.1 `CONFIG_A4979_STEPPER`

**提示（Prompt）**：启用 Allegro A4979 步进驱动器（Stepper Driver）

**说明（Help）**

步进电机（Stepper Motor）的微步进电机驱动器（Microstepping Motor Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ALLEGRO_A4979_ENABLED && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_STEP_DIR_STEPPER
```

**定义位置（Location）**：[`drivers/stepper/allegro/Kconfig.a4979:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/allegro/Kconfig.a4979#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_STEP_DIR_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEP_DIR_STEPPER)。

<a id="CONFIG_DRV84XX"></a>

## 174.2 `CONFIG_DRV84XX`

**提示（Prompt）**：TI DRV84XX 步进电机驱动器（Stepper Motor Driver）

**说明（Help）**

启用 TI DRV84XX 步进电机驱动器（Stepper Motor Driver）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_DRV84XX_ENABLED && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_STEP_DIR_STEPPER
```

**定义位置（Location）**：[`drivers/stepper/ti/Kconfig.drv84xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/ti/Kconfig.drv84xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_STEP_DIR_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEP_DIR_STEPPER)。

<a id="CONFIG_FAKE_STEPPER"></a>

## 174.3 `CONFIG_FAKE_STEPPER`

**提示（Prompt）**：模拟步进电机控制器和步进驱动器（Fake Stepper Motor Controller and Stepper Driver）

**说明（Help）**

启用基于伪函数框架（FFF）的模拟步进控制器与驱动器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ZEPHYR_FAKE_STEPPER_DRIVER_ENABLED || DT_HAS_ZEPHYR_FAKE_STEPPER_CTRL_ENABLED) && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/stepper/Kconfig.fake:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/Kconfig.fake#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_GPIO_STEPPER"></a>

## 174.4 `CONFIG_GPIO_STEPPER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用基于 GPIO 的步进控制器（Stepper Controller）所使用的库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER
```

**主动选择（Selects）**

```text
CONFIG_STEPPER_CTRL_EVENT_HANDLER
```

**被选择（Selected by）**

```text
CONFIG_STEPPER_GPIO_STEP_DIR_STEPPER_CTRL
CONFIG_STEPPER_H_BRIDGE_STEPPER_CTRL
```

**定义位置（Location）**：[`drivers/stepper/gpio_stepper/common/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/gpio_stepper/common/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_STEPPER_CTRL_EVENT_HANDLER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_CTRL_EVENT_HANDLER)、[`CONFIG_STEPPER_GPIO_STEP_DIR_STEPPER_CTRL`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_GPIO_STEP_DIR_STEPPER_CTRL)、[`CONFIG_STEPPER_H_BRIDGE_STEPPER_CTRL`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_H_BRIDGE_STEPPER_CTRL)。

<a id="CONFIG_GPIO_STEPPER_COUNTER_TIMING"></a>

## 174.5 `CONFIG_GPIO_STEPPER_COUNTER_TIMING`

**提示（Prompt）**：使用计数器（Counter）进行步进定时

**说明（Help）**

启用计数器设备（Counter Device），以实现准确步进。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO_STEPPER && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER
```

**定义位置（Location）**：[`drivers/stepper/gpio_stepper/common/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/gpio_stepper/common/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_GPIO_STEPPER)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_STEPPER"></a>

## 174.6 `CONFIG_STEPPER`

**提示（Prompt）**：步进控制器（Stepper Controller）驱动

**说明（Help）**

启用步进控制器（Stepper Controller）

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/stepper/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_STEPPER_ADI_TMC2209"></a>

## 174.7 `CONFIG_STEPPER_ADI_TMC2209`

**提示（Prompt）**：启用 Trinamic TMC2209 步进驱动器（Stepper Driver）

**说明（Help）**

TMC2209 步进驱动器（Stepper Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_TMC2209_ENABLED && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_STEP_DIR_STEPPER
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/tmc22xx/Kconfig.tmc22xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmc22xx/Kconfig.tmc22xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_STEP_DIR_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEP_DIR_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMC50XX"></a>

## 174.8 `CONFIG_STEPPER_ADI_TMC50XX`

**提示（Prompt）**：启用 Trinamic TMC50xx

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_TMC50XX_ENABLED && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_STEPPER_ADI_TMC_SPI
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/tmc50xx/Kconfig.tmc50xx:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmc50xx/Kconfig.tmc50xx#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_STEPPER_ADI_TMC_SPI`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC_SPI)。

<a id="CONFIG_STEPPER_ADI_TMC50XX_RAMPSTAT_POLL_INTERVAL_IN_MSEC"></a>

## 174.9 `CONFIG_STEPPER_ADI_TMC50XX_RAMPSTAT_POLL_INTERVAL_IN_MSEC`

**提示（Prompt）**：TMC50xx 斜坡状态（Ramp Status）轮询间隔，单位为毫秒

**说明（Help）**

DIAG0 引脚不可用时，驱动自动退回轮询（Polling）方式。此设置控制驱动轮询斜坡状态寄存器（Ramp Status Register）的间隔，单位为毫秒，以检测到达目标位置、堵转（Stall）或触发行程终点（End Stop）等事件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER_ADI_TMC50XX && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/Kconfig.tmc_rampgen_template:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/Kconfig.tmc_rampgen_template#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 启用 Trinamic TMC50xx

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_ADI_TMC50XX`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC50XX)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMC50XX_RAMPSTAT_POLL_STALLGUARD_LOG"></a>

## 174.10 `CONFIG_STEPPER_ADI_TMC50XX_RAMPSTAT_POLL_STALLGUARD_LOG`

**提示（Prompt）**：记录 TMC50xx StallGuard 日志

**说明（Help）**

轮询 `rampstat` 时启用 StallGuard 日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER_ADI_TMC50XX && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/Kconfig.tmc_rampgen_template:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/Kconfig.tmc_rampgen_template#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 启用 Trinamic TMC50xx

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_ADI_TMC50XX`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC50XX)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMC50XX_RAMP_GEN"></a>

## 174.11 `CONFIG_STEPPER_ADI_TMC50XX_RAMP_GEN`

**提示（Prompt）**：TMC50xx 使用斜坡发生器（Ramp Generator）

**说明（Help）**

为 Trinamic 步进控制器启用斜坡发生器（Ramp Generator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER_ADI_TMC50XX && CONFIG_STEPPER_ADI_TMC50XX && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/Kconfig.tmc_rampgen_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/Kconfig.tmc_rampgen_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 启用 Trinamic TMC50xx

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_ADI_TMC50XX`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC50XX)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMC50XX_STEPPER_CTRL"></a>

## 174.12 `CONFIG_STEPPER_ADI_TMC50XX_STEPPER_CTRL`

**提示（Prompt）**：启用 Trinamic TMC50xx 运动控制器（Motion Controller）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_TMC50XX_STEPPER_CTRL_ENABLED && DT_HAS_ADI_TMC50XX_STEPPER_DRIVER_ENABLED && CONFIG_STEPPER_ADI_TMC50XX && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/tmc50xx/Kconfig.tmc50xx:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmc50xx/Kconfig.tmc50xx#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 启用 Trinamic TMC50xx

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_ADI_TMC50XX`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC50XX)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMC50XX_STEPPER_DRIVER"></a>

## 174.13 `CONFIG_STEPPER_ADI_TMC50XX_STEPPER_DRIVER`

**提示（Prompt）**：启用 Trinamic TMC50xx 步进驱动器（Stepper Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_TMC50XX_STEPPER_DRIVER_ENABLED && CONFIG_STEPPER_ADI_TMC50XX && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/tmc50xx/Kconfig.tmc50xx:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmc50xx/Kconfig.tmc50xx#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 启用 Trinamic TMC50xx

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_ADI_TMC50XX`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC50XX)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMC51XX"></a>

## 174.14 `CONFIG_STEPPER_ADI_TMC51XX`

**提示（Prompt）**：启用 Trinamic TMC51xx

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_TMC51XX_ENABLED && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_STEPPER_ADI_TMC_UART if n
CONFIG_STEPPER_ADI_TMC_SPI if n
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/tmc51xx/Kconfig.tmc51xx:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmc51xx/Kconfig.tmc51xx#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_STEPPER_ADI_TMC_UART`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC_UART)、[`CONFIG_STEPPER_ADI_TMC_SPI`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC_SPI)。

<a id="CONFIG_STEPPER_ADI_TMC51XX_RAMPSTAT_POLL_INTERVAL_IN_MSEC"></a>

## 174.15 `CONFIG_STEPPER_ADI_TMC51XX_RAMPSTAT_POLL_INTERVAL_IN_MSEC`

**提示（Prompt）**：TMC51xx 斜坡状态（Ramp Status）轮询间隔，单位为毫秒

**说明（Help）**

DIAG0 引脚不可用时，驱动自动退回轮询（Polling）方式。此设置控制驱动轮询斜坡状态寄存器（Ramp Status Register）的间隔，单位为毫秒，以检测到达目标位置、堵转（Stall）或触发行程终点（End Stop）等事件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER_ADI_TMC51XX && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/Kconfig.tmc_rampgen_template:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/Kconfig.tmc_rampgen_template#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 启用 Trinamic TMC51xx

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_ADI_TMC51XX`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC51XX)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMC51XX_RAMPSTAT_POLL_STALLGUARD_LOG"></a>

## 174.16 `CONFIG_STEPPER_ADI_TMC51XX_RAMPSTAT_POLL_STALLGUARD_LOG`

**提示（Prompt）**：记录 TMC51xx StallGuard 日志

**说明（Help）**

轮询 `rampstat` 时启用 StallGuard 日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER_ADI_TMC51XX && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/Kconfig.tmc_rampgen_template:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/Kconfig.tmc_rampgen_template#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 启用 Trinamic TMC51xx

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_ADI_TMC51XX`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC51XX)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMC51XX_RAMP_GEN"></a>

## 174.17 `CONFIG_STEPPER_ADI_TMC51XX_RAMP_GEN`

**提示（Prompt）**：TMC51xx 使用斜坡发生器（Ramp Generator）

**说明（Help）**

为 Trinamic 步进控制器启用斜坡发生器（Ramp Generator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER_ADI_TMC51XX && CONFIG_STEPPER_ADI_TMC51XX && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/Kconfig.tmc_rampgen_template:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/Kconfig.tmc_rampgen_template#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 启用 Trinamic TMC51xx

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_ADI_TMC51XX`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC51XX)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMC51XX_STEPPER_CTRL"></a>

## 174.18 `CONFIG_STEPPER_ADI_TMC51XX_STEPPER_CTRL`

**提示（Prompt）**：启用 Trinamic TMC51xx 运动控制器（Motion Controller）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_TMC51XX_STEPPER_CTRL_ENABLED && DT_HAS_ADI_TMC51XX_STEPPER_DRIVER_ENABLED && CONFIG_STEPPER_ADI_TMC51XX && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/tmc51xx/Kconfig.tmc51xx:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmc51xx/Kconfig.tmc51xx#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 启用 Trinamic TMC51xx

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_ADI_TMC51XX`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC51XX)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMC51XX_STEPPER_DRIVER"></a>

## 174.19 `CONFIG_STEPPER_ADI_TMC51XX_STEPPER_DRIVER`

**提示（Prompt）**：启用 Trinamic TMC51xx 步进驱动器（Stepper Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_TMC51XX_STEPPER_DRIVER_ENABLED && CONFIG_STEPPER_ADI_TMC51XX && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/tmc51xx/Kconfig.tmc51xx:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmc51xx/Kconfig.tmc51xx#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 启用 Trinamic TMC51xx

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_ADI_TMC51XX`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC51XX)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMCM3216"></a>

## 174.20 `CONFIG_STEPPER_ADI_TMCM3216`

**提示（Prompt）**：启用 Trinamic TMCM3216

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_TMCM3216_ENABLED && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_STEPPER_ADI_TMCM_RS485
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/tmcm3216/Kconfig.tmcm3216:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmcm3216/Kconfig.tmcm3216#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_STEPPER_ADI_TMCM_RS485`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMCM_RS485)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_STEPPER_ADI_TMCM3216_STEPPER_CTRL"></a>

## 174.21 `CONFIG_STEPPER_ADI_TMCM3216_STEPPER_CTRL`

**提示（Prompt）**：启用 Trinamic TMCM3216 运动控制器（Motion Controller）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_TMCM3216_STEPPER_CTRL_ENABLED && DT_HAS_ADI_TMCM3216_STEPPER_DRIVER_ENABLED && CONFIG_STEPPER_ADI_TMCM3216 && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/tmcm3216/Kconfig.tmcm3216:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmcm3216/Kconfig.tmcm3216#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 启用 Trinamic TMCM3216

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_ADI_TMCM3216`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMCM3216)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMCM3216_STEPPER_DRIVER"></a>

## 174.22 `CONFIG_STEPPER_ADI_TMCM3216_STEPPER_DRIVER`

**提示（Prompt）**：启用 Trinamic TMCM3216 步进驱动器（Stepper Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_TMCM3216_STEPPER_DRIVER_ENABLED && CONFIG_STEPPER_ADI_TMCM3216 && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/tmcm3216/Kconfig.tmcm3216:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmcm3216/Kconfig.tmcm3216#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 启用 Trinamic TMCM3216

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_ADI_TMCM3216`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMCM3216)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_ADI_TMCM_RS485"></a>

## 174.23 `CONFIG_STEPPER_ADI_TMCM_RS485`

**提示（Prompt）**：通过 RS485 使用 Trinamic 步进控制器（Stepper Controller）

**说明（Help）**

已启用使用串行接口（Serial）的 Trinamic 步进控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER
```

**主动选择（Selects）**

```text
CONFIG_SERIAL
```

**被选择（Selected by）**

```text
CONFIG_STEPPER_ADI_TMCM3216
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/bus/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/bus/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_STEPPER_ADI_TMCM3216`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMCM3216)。

<a id="CONFIG_STEPPER_ADI_TMC_SPI"></a>

## 174.24 `CONFIG_STEPPER_ADI_TMC_SPI`

**提示（Prompt）**：通过 SPI 使用 Trinamic 步进控制器（Stepper Controller）

**说明（Help）**

已启用使用 SPI 的 Trinamic 步进控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**被选择（Selected by）**

```text
CONFIG_STEPPER_ADI_TMC50XX
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/bus/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/bus/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_STEPPER_ADI_TMC50XX`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC50XX)。

<a id="CONFIG_STEPPER_ADI_TMC_UART"></a>

## 174.25 `CONFIG_STEPPER_ADI_TMC_UART`

**提示（Prompt）**：通过单线 UART（Single Wire UART）使用 Trinamic 步进控制器

**说明（Help）**

已启用使用单线 UART（Single Wire UART）的 Trinamic 步进控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER
```

**主动选择（Selects）**

```text
CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/stepper/adi_tmc/bus/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/bus/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_STEPPER_CTRL_EVENT_HANDLER"></a>

## 174.26 `CONFIG_STEPPER_CTRL_EVENT_HANDLER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 `stepper_ctrl` 驱动启用公共辅助代码，用于管理和分派事件回调（Event Callbacks）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER
```

**被选择（Selected by）**

```text
CONFIG_GPIO_STEPPER
```

**定义位置（Location）**：[`drivers/stepper/event_handler/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/event_handler/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_GPIO_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_GPIO_STEPPER)。

<a id="CONFIG_STEPPER_CTRL_EVENT_QUEUE_LEN"></a>

## 174.27 `CONFIG_STEPPER_CTRL_EVENT_QUEUE_LEN`

**提示（Prompt）**：待处理 `stepper_ctrl` 事件的最大数量

**说明（Help）**

每个驱动实例允许积压的 `stepper_ctrl` 事件最大数量。达到上限后，新的事件将被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER_CTRL_ISR_SAFE_EVENTS && CONFIG_STEPPER_CTRL_EVENT_HANDLER && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/stepper/event_handler/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/event_handler/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动 → 确保回调在非中断服务程序上下文（Non-ISR Context）中执行

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_CTRL_ISR_SAFE_EVENTS`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_CTRL_ISR_SAFE_EVENTS)、[`CONFIG_STEPPER_CTRL_EVENT_HANDLER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_CTRL_EVENT_HANDLER)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_CTRL_ISR_SAFE_EVENTS"></a>

## 174.28 `CONFIG_STEPPER_CTRL_ISR_SAFE_EVENTS`

**提示（Prompt）**：确保回调在非中断服务程序上下文（Non-ISR Context）中执行

**说明（Help）**

从中断服务程序（ISR）上下文触发事件时，通过工作队列（Work Queue）分派事件回调。可同时积压多个事件，并按顺序处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER_CTRL_EVENT_HANDLER && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/stepper/event_handler/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/event_handler/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER_CTRL_EVENT_HANDLER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_CTRL_EVENT_HANDLER)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_GPIO_STEP_DIR_STEPPER_CTRL"></a>

## 174.29 `CONFIG_STEPPER_GPIO_STEP_DIR_STEPPER_CTRL`

**提示（Prompt）**：启用 GPIO 步进／方向（Step/Dir）步进控制驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_GPIO_STEP_DIR_STEPPER_CTRL_ENABLED && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO_STEPPER
CONFIG_STEP_DIR_STEPPER
```

**定义位置（Location）**：[`drivers/stepper/gpio_stepper/Kconfig.gpio_step_dir:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/gpio_stepper/Kconfig.gpio_step_dir#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_GPIO_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_GPIO_STEPPER)、[`CONFIG_STEP_DIR_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEP_DIR_STEPPER)。

<a id="CONFIG_STEPPER_H_BRIDGE_STEPPER_CTRL"></a>

## 174.30 `CONFIG_STEPPER_H_BRIDGE_STEPPER_CTRL`

**提示（Prompt）**：启用 GPIO H 桥（H-bridge）步进控制驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_H_BRIDGE_STEPPER_CTRL_ENABLED && CONFIG_STEPPER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO_STEPPER
```

**定义位置（Location）**：[`drivers/stepper/gpio_stepper/Kconfig.h_bridge:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/gpio_stepper/Kconfig.h_bridge#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_GPIO_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_GPIO_STEPPER)。

<a id="CONFIG_STEPPER_INIT_PRIORITY"></a>

## 174.31 `CONFIG_STEPPER_INIT_PRIORITY`

**提示（Prompt）**：步进电机控制器初始化优先级（Init Priority）

**说明（Help）**

步进电机控制器的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/stepper/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEPPER_SHELL"></a>

## 174.32 `CONFIG_STEPPER_SHELL`

**提示（Prompt）**：步进电机命令行（Stepper Shell）

**说明（Help）**

启用用于测试的步进电机命令行（Stepper Shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_STEPPER
```

**定义位置（Location）**：[`drivers/stepper/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)。

<a id="CONFIG_STEP_DIR_STEPPER"></a>

## 174.33 `CONFIG_STEP_DIR_STEPPER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用步进／方向（Step/Direction）步进驱动器使用的库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STEPPER
```

**被选择（Selected by）**

```text
CONFIG_STEPPER_ADI_TMC2209
CONFIG_A4979_STEPPER
CONFIG_STEPPER_GPIO_STEP_DIR_STEPPER_CTRL
CONFIG_DRV84XX
```

**定义位置（Location）**：[`drivers/stepper/step_dir/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/step_dir/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 步进控制器（Stepper Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER)、[`CONFIG_STEPPER_ADI_TMC2209`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_ADI_TMC2209)、[`CONFIG_A4979_STEPPER`](P174_drivers_stepper_配置项参考.md#CONFIG_A4979_STEPPER)、[`CONFIG_STEPPER_GPIO_STEP_DIR_STEPPER_CTRL`](P174_drivers_stepper_配置项参考.md#CONFIG_STEPPER_GPIO_STEP_DIR_STEPPER_CTRL)、[`CONFIG_DRV84XX`](P174_drivers_stepper_配置项参考.md#CONFIG_DRV84XX)。

<!-- kconfig-navigation -->

[上一章](P173_drivers_spi_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P175_drivers_syscon_配置项参考.md)
