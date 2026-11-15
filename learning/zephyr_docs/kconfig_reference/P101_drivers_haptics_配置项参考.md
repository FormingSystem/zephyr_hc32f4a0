---
id: learning.zephyr-docs.kconfig-reference.page-101
title: "`drivers/haptics`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第101章\_`drivers/haptics`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/haptics` 的 19 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HAPTICS"></a>

## 101.1 `CONFIG_HAPTICS`

**提示（Prompt）**：触觉反馈驱动（Haptic Feedback Drivers）

**说明（Help）**

启用触觉反馈（Haptics）驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/haptics/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_HAPTICS_CS40L26"></a>

## 101.2 `CONFIG_HAPTICS_CS40L26`

**提示（Prompt）**：CS40L26/27 触觉反馈驱动（Haptics Driver）

**说明（Help）**

启用 CS40L26/27 触觉反馈（Haptics）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_CIRRUS_CS40L26_ENABLED || DT_HAS_CIRRUS_CS40L27_ENABLED) && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l26:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l26#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_CS40L26_CALIBRATION"></a>

## 101.3 `CONFIG_HAPTICS_CS40L26_CALIBRATION`

**提示（Prompt）**：校准（Calibration）

**说明（Help）**

允许设备运行校准程序（Calibration Routine）；如果提供闪存存储，还可选择将校准数据（Calibration Data）写入闪存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS_CS40L26 && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l26:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l26#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → CS40L26/27 触觉反馈驱动（Haptics Driver）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_CS40L26`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_CS40L26)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_CS40L26_CLICK_COMPENSATION"></a>

## 101.4 `CONFIG_HAPTICS_CS40L26_CLICK_COMPENSATION`

**提示（Prompt）**：点击补偿（Click Compensation）

**说明（Help）**

为触觉效果（Haptic Effect）启用点击补偿（Click Compensation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS_CS40L26 && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l26:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l26#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → CS40L26/27 触觉反馈驱动（Haptics Driver）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_CS40L26`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_CS40L26)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_CS40L26_DYNAMIC_F0"></a>

## 101.5 `CONFIG_HAPTICS_CS40L26_DYNAMIC_F0`

**提示（Prompt）**：动态 F0（Dynamic F0）

**说明（Help）**

为触觉效果（Haptic Effect）启用动态 F0 补偿（Dynamic F0 Compensation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS_CS40L26 && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l26:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l26#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → CS40L26/27 触觉反馈驱动（Haptics Driver）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_CS40L26`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_CS40L26)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_CS40L26_PM_ACTIVE_TIMEOUT_MS"></a>

## 101.6 `CONFIG_HAPTICS_CS40L26_PM_ACTIVE_TIMEOUT_MS`

**提示（Prompt）**：活动状态超时（Active Timeout）

**说明（Help）**

设备播放完一个触觉效果（Effect）后，等待指定的毫秒数，再进入待机状态（Standby State）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS_CS40L26 && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10000]
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l26:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l26#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → CS40L26/27 触觉反馈驱动（Haptics Driver）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_CS40L26`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_CS40L26)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_CS40L26_PM_STDBY_TIMEOUT_MS"></a>

## 101.7 `CONFIG_HAPTICS_CS40L26_PM_STDBY_TIMEOUT_MS`

**提示（Prompt）**：待机超时（Standby Timeout）

**说明（Help）**

启用休眠（Hibernation）功能时，设备进入待机状态（Standby State）后等待指定的毫秒数，再进入休眠。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS_CS40L26 && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[0, 10000]
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l26:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l26#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → CS40L26/27 触觉反馈驱动（Haptics Driver）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_CS40L26`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_CS40L26)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_CS40L5X"></a>

## 101.8 `CONFIG_HAPTICS_CS40L5X`

**提示（Prompt）**：CS40L5x 触觉反馈驱动（Haptics Driver）

**说明（Help）**

启用 CS40L5x 触觉反馈（Haptics）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_CIRRUS_CS40L50_ENABLED || DT_HAS_CIRRUS_CS40L51_ENABLED || DT_HAS_CIRRUS_CS40L52_ENABLED || DT_HAS_CIRRUS_CS40L53_ENABLED) && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l5x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l5x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_CS40L5X_CALIBRATION"></a>

## 101.9 `CONFIG_HAPTICS_CS40L5X_CALIBRATION`

**提示（Prompt）**：校准（Calibration）

**说明（Help）**

允许设备运行校准程序（Calibration Routine）；如果提供闪存存储，还可选择将校准数据（Calibration Data）写入闪存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS_CS40L5X && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l5x:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l5x#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → CS40L5x 触觉反馈驱动（Haptics Driver）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_CS40L5X`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_CS40L5X)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_CS40L5X_CLICK_COMPENSATION"></a>

## 101.10 `CONFIG_HAPTICS_CS40L5X_CLICK_COMPENSATION`

**提示（Prompt）**：点击补偿（Click Compensation）

**说明（Help）**

为触觉效果（Haptic Effect）启用点击补偿（Click Compensation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS_CS40L5X && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l5x:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l5x#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → CS40L5x 触觉反馈驱动（Haptics Driver）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_CS40L5X`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_CS40L5X)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_CS40L5X_DYNAMIC_F0"></a>

## 101.11 `CONFIG_HAPTICS_CS40L5X_DYNAMIC_F0`

**提示（Prompt）**：动态 F0（Dynamic F0）

**说明（Help）**

为触觉效果（Haptic Effect）启用动态 F0 补偿（Dynamic F0 Compensation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS_CS40L5X && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l5x:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l5x#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → CS40L5x 触觉反馈驱动（Haptics Driver）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_CS40L5X`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_CS40L5X)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_CS40L5X_PM_ACTIVE_TIMEOUT_MS"></a>

## 101.12 `CONFIG_HAPTICS_CS40L5X_PM_ACTIVE_TIMEOUT_MS`

**提示（Prompt）**：活动状态超时（Active Timeout）

**说明（Help）**

设备播放完一个触觉效果（Effect）后，等待指定的毫秒数，再进入待机状态（Standby State）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS_CS40L5X && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10000]
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l5x:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l5x#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → CS40L5x 触觉反馈驱动（Haptics Driver）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_CS40L5X`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_CS40L5X)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_CS40L5X_PM_STDBY_TIMEOUT_MS"></a>

## 101.13 `CONFIG_HAPTICS_CS40L5X_PM_STDBY_TIMEOUT_MS`

**提示（Prompt）**：待机超时（Standby Timeout）

**说明（Help）**

启用休眠（Hibernation）功能时，设备进入待机状态（Standby State）后等待指定的毫秒数，再进入休眠。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS_CS40L5X && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[0, 10000]
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l5x:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l5x#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → CS40L5x 触觉反馈驱动（Haptics Driver）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_CS40L5X`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_CS40L5X)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_CS40L5X_RTH_EFFECTS"></a>

## 101.14 `CONFIG_HAPTICS_CS40L5X_RTH_EFFECTS`

**提示（Prompt）**：PCM 与 PWLE 效果（Effects）

**说明（Help）**

启用脉冲编码调制（PCM）和 PWLE 波形（Waveform）的上传与播放。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS_CS40L5X && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/haptics/cirrus/Kconfig.cs40l5x:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/cirrus/Kconfig.cs40l5x#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → CS40L5x 触觉反馈驱动（Haptics Driver）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_CS40L5X`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_CS40L5X)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_DRV2605"></a>

## 101.15 `CONFIG_HAPTICS_DRV2605`

**提示（Prompt）**：DRV2605 触觉反馈驱动（Haptics Driver）

**说明（Help）**

启用基于 I2C 的德州仪器（Texas Instruments）DRV2605 触觉反馈驱动（Haptics Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_DRV2605_ENABLED && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/haptics/ti/Kconfig.drv2605:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/ti/Kconfig.drv2605#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_HAPTICS_INIT_PRIORITY"></a>

## 101.16 `CONFIG_HAPTICS_INIT_PRIORITY`

**提示（Prompt）**：触觉反馈驱动初始化优先级（Haptic Driver Init Priority）

**说明（Help）**

触觉反馈驱动（Haptic Driver）的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/haptics/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_SHELL"></a>

## 101.17 `CONFIG_HAPTICS_SHELL`

**提示（Prompt）**：触觉反馈命令行（Haptics Shell）

**说明（Help）**

启用触觉反馈（Haptics）相关的命令行（Shell）命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_HAPTICS
```

**定义位置（Location）**：[`drivers/haptics/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_SHELL_BUFFER_SIZE"></a>

## 101.18 `CONFIG_HAPTICS_SHELL_BUFFER_SIZE`

**提示（Prompt）**：触觉反馈命令行缓冲区大小（Haptics Shell Buffer Size）

**说明（Help）**

向触觉反馈驱动（Haptic Driver）流式传送采样数据（Stream Samples）时使用的缓冲区大小，以字节为单位。该缓冲区分配在栈（Stack）上。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAPTICS_SHELL && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/haptics/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → 触觉反馈命令行（Haptics Shell）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_SHELL`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS_SHELL)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)。

<a id="CONFIG_HAPTICS_TM6605"></a>

## 101.19 `CONFIG_HAPTICS_TM6605`

**提示（Prompt）**：TM6605 触觉反馈驱动（Haptics Driver）

**说明（Help）**

启用基于 I2C 的天微电子（Titan Micro Electronics）TM6605 线性谐振执行器（Linear Resonant Actuator，LRA）触觉反馈驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TITANMEC_TM6605_ENABLED && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/haptics/titanmec/Kconfig.tm6605:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/titanmec/Kconfig.tm6605#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<!-- kconfig-navigation -->

[上一章](P100_drivers_gpio_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P102_drivers_hdlc_rcp_if_配置项参考.md)
