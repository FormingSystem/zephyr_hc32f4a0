---
id: learning.zephyr-docs.kconfig-reference.page-234
title: "`modules/hal_tdk`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第234章\_`modules/hal_tdk`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/hal_tdk` 的 11 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_TDK_HAL"></a>

## 234.1 `CONFIG_TDK_HAL`

**提示（Prompt）**：TDK 硬件抽象层（HAL）驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**被弱选择（Implied by）**

```text
CONFIG_USE_EMD_ICM42670
CONFIG_USE_EMD_ICM45605
CONFIG_USE_EMD_ICM45605S
CONFIG_USE_EMD_ICM45686
CONFIG_USE_EMD_ICM45686S
CONFIG_USE_EMD_ICM45688P
CONFIG_USE_EMD_ICM42370
CONFIG_USE_EMD_ICP101XX
CONFIG_USE_EMD_ICP201XX
CONFIG_USE_EMD_TAD2144
CONFIG_USE_EMD_ICM56622
CONFIG_USE_EMD_ICM56686
CONFIG_USE_EMD_ICM42670
CONFIG_USE_EMD_ICM45605
CONFIG_USE_EMD_ICM45605S
CONFIG_USE_EMD_ICM45686
CONFIG_USE_EMD_ICM45686S
CONFIG_USE_EMD_ICM45688P
CONFIG_USE_EMD_ICM42370
CONFIG_USE_EMD_ICP101XX
CONFIG_USE_EMD_ICP201XX
CONFIG_USE_EMD_TAD2144
CONFIG_USE_EMD_ICM56622
CONFIG_USE_EMD_ICM56686
```

**定义位置（Location）**：[`modules/hal_tdk/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_tdk/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_tdk（模块路径 `modules/hal/tdk`，相对于 west 工作区顶层目录） → TDK 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_USE_EMD_ICM42670`](P234_modules_hal_tdk_配置项参考.md#CONFIG_USE_EMD_ICM42670)、[`CONFIG_USE_EMD_ICM45605`](P234_modules_hal_tdk_配置项参考.md#CONFIG_USE_EMD_ICM45605)、[`CONFIG_USE_EMD_ICM45605S`](P234_modules_hal_tdk_配置项参考.md#CONFIG_USE_EMD_ICM45605S)、[`CONFIG_USE_EMD_ICM45686`](P234_modules_hal_tdk_配置项参考.md#CONFIG_USE_EMD_ICM45686)、[`CONFIG_USE_EMD_ICM45686S`](P234_modules_hal_tdk_配置项参考.md#CONFIG_USE_EMD_ICM45686S)、[`CONFIG_USE_EMD_ICM45688P`](P234_modules_hal_tdk_配置项参考.md#CONFIG_USE_EMD_ICM45688P)、[`CONFIG_USE_EMD_ICM42370`](P234_modules_hal_tdk_配置项参考.md#CONFIG_USE_EMD_ICM42370)、[`CONFIG_USE_EMD_ICP101XX`](P234_modules_hal_tdk_配置项参考.md#CONFIG_USE_EMD_ICP101XX)、[`CONFIG_USE_EMD_ICP201XX`](P234_modules_hal_tdk_配置项参考.md#CONFIG_USE_EMD_ICP201XX)、[`CONFIG_USE_EMD_TAD2144`](P234_modules_hal_tdk_配置项参考.md#CONFIG_USE_EMD_TAD2144)、[`CONFIG_USE_EMD_ICM56622`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICM56622)、[`CONFIG_USE_EMD_ICM56686`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_EMD_ICM56686)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_EMD_ICM56622`、`CONFIG_USE_EMD_ICM56686`。

<a id="CONFIG_USE_EMD_ICM42370"></a>

## 234.2 `CONFIG_USE_EMD_ICM42370`

**提示（Prompt）**：ICM42370P 高性能三轴 MotionTracking 加速度计（Accelerometer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_HAL_TDK_MODULE && DT_HAS_INVENSENSE_ICM42370P_ENABLED
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ICM42X70
```

**弱选择（Implies）**

```text
CONFIG_TDK_HAL
```

**定义位置（Location）**：[`modules/hal_tdk/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_tdk/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_tdk（模块路径 `modules/hal/tdk`，相对于 west 工作区顶层目录） → TDK 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_ICM42X70`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70)、[`CONFIG_TDK_HAL`](P234_modules_hal_tdk_配置项参考.md#CONFIG_TDK_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<a id="CONFIG_USE_EMD_ICM42670"></a>

## 234.3 `CONFIG_USE_EMD_ICM42670`

**提示（Prompt）**：ICM42x7x 高性能六轴 MotionTracking 惯性测量单元（IMU）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_HAL_TDK_MODULE && (DT_HAS_INVENSENSE_ICM42670P_ENABLED || DT_HAS_INVENSENSE_ICM42670S_ENABLED)
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ICM42X70
```

**弱选择（Implies）**

```text
CONFIG_TDK_HAL
```

**定义位置（Location）**：[`modules/hal_tdk/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_tdk/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_tdk（模块路径 `modules/hal/tdk`，相对于 west 工作区顶层目录） → TDK 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_ICM42X70`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM42X70)、[`CONFIG_TDK_HAL`](P234_modules_hal_tdk_配置项参考.md#CONFIG_TDK_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<a id="CONFIG_USE_EMD_ICM45605"></a>

## 234.4 `CONFIG_USE_EMD_ICM45605`

**提示（Prompt）**：ICM45605 高性能六轴 MotionTracking 惯性测量单元（IMU）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_HAL_TDK_MODULE && DT_HAS_INVENSENSE_ICM45605_ENABLED
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ICM45686
```

**弱选择（Implies）**

```text
CONFIG_TDK_HAL
```

**定义位置（Location）**：[`modules/hal_tdk/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_tdk/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_tdk（模块路径 `modules/hal/tdk`，相对于 west 工作区顶层目录） → TDK 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_ICM45686`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686)、[`CONFIG_TDK_HAL`](P234_modules_hal_tdk_配置项参考.md#CONFIG_TDK_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<a id="CONFIG_USE_EMD_ICM45605S"></a>

## 234.5 `CONFIG_USE_EMD_ICM45605S`

**提示（Prompt）**：ICM45605S 高性能六轴 MotionTracking 惯性测量单元（IMU）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_HAL_TDK_MODULE && DT_HAS_INVENSENSE_ICM45605S_ENABLED
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ICM45686
```

**弱选择（Implies）**

```text
CONFIG_TDK_HAL
```

**定义位置（Location）**：[`modules/hal_tdk/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_tdk/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_tdk（模块路径 `modules/hal/tdk`，相对于 west 工作区顶层目录） → TDK 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_ICM45686`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686)、[`CONFIG_TDK_HAL`](P234_modules_hal_tdk_配置项参考.md#CONFIG_TDK_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<a id="CONFIG_USE_EMD_ICM45686"></a>

## 234.6 `CONFIG_USE_EMD_ICM45686`

**提示（Prompt）**：ICM45686 高性能六轴 MotionTracking 惯性测量单元（IMU）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_HAL_TDK_MODULE && DT_HAS_INVENSENSE_ICM45686_ENABLED
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ICM45686
```

**弱选择（Implies）**

```text
CONFIG_TDK_HAL
```

**定义位置（Location）**：[`modules/hal_tdk/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_tdk/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_tdk（模块路径 `modules/hal/tdk`，相对于 west 工作区顶层目录） → TDK 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_ICM45686`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686)、[`CONFIG_TDK_HAL`](P234_modules_hal_tdk_配置项参考.md#CONFIG_TDK_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<a id="CONFIG_USE_EMD_ICM45686S"></a>

## 234.7 `CONFIG_USE_EMD_ICM45686S`

**提示（Prompt）**：ICM45686S 高性能六轴 MotionTracking 惯性测量单元（IMU）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_HAL_TDK_MODULE && DT_HAS_INVENSENSE_ICM45686S_ENABLED
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ICM45686
```

**弱选择（Implies）**

```text
CONFIG_TDK_HAL
```

**定义位置（Location）**：[`modules/hal_tdk/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_tdk/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_tdk（模块路径 `modules/hal/tdk`，相对于 west 工作区顶层目录） → TDK 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_ICM45686`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686)、[`CONFIG_TDK_HAL`](P234_modules_hal_tdk_配置项参考.md#CONFIG_TDK_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<a id="CONFIG_USE_EMD_ICM45688P"></a>

## 234.8 `CONFIG_USE_EMD_ICM45688P`

**提示（Prompt）**：ICM45688P 高性能六轴 MotionTracking 惯性测量单元（IMU）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_HAL_TDK_MODULE && DT_HAS_INVENSENSE_ICM45688P_ENABLED
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ICM45686
```

**弱选择（Implies）**

```text
CONFIG_TDK_HAL
```

**定义位置（Location）**：[`modules/hal_tdk/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_tdk/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_tdk（模块路径 `modules/hal/tdk`，相对于 west 工作区顶层目录） → TDK 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_ICM45686`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686)、[`CONFIG_TDK_HAL`](P234_modules_hal_tdk_配置项参考.md#CONFIG_TDK_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<a id="CONFIG_USE_EMD_ICP101XX"></a>

## 234.9 `CONFIG_USE_EMD_ICP101XX`

**提示（Prompt）**：ICP101XX 气压与温度传感器（Barometric Pressure and Temperature Sensors）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_HAL_TDK_MODULE && DT_HAS_INVENSENSE_ICP101XX_ENABLED
```

**被选择（Selected by）**

```text
CONFIG_ICP101XX
```

**弱选择（Implies）**

```text
CONFIG_TDK_HAL
```

**定义位置（Location）**：[`modules/hal_tdk/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_tdk/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_tdk（模块路径 `modules/hal/tdk`，相对于 west 工作区顶层目录） → TDK 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_ICP101XX`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP101XX)、[`CONFIG_TDK_HAL`](P234_modules_hal_tdk_配置项参考.md#CONFIG_TDK_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<a id="CONFIG_USE_EMD_ICP201XX"></a>

## 234.10 `CONFIG_USE_EMD_ICP201XX`

**提示（Prompt）**：ICP201XX 气压与温度传感器（Barometric Pressure and Temperature Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_HAL_TDK_MODULE && DT_HAS_INVENSENSE_ICP201XX_ENABLED
```

**被选择（Selected by）**

```text
CONFIG_ICP201XX
```

**弱选择（Implies）**

```text
CONFIG_TDK_HAL
```

**定义位置（Location）**：[`modules/hal_tdk/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_tdk/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_tdk（模块路径 `modules/hal/tdk`，相对于 west 工作区顶层目录） → TDK 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_ICP201XX`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICP201XX)、[`CONFIG_TDK_HAL`](P234_modules_hal_tdk_配置项参考.md#CONFIG_TDK_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<a id="CONFIG_USE_EMD_TAD2144"></a>

## 234.11 `CONFIG_USE_EMD_TAD2144`

**提示（Prompt）**：TAD2144 隧道磁阻角度传感器（TMR angle Sensor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_HAL_TDK_MODULE && DT_HAS_INVENSENSE_TAD2144_ENABLED
```

**被选择（Selected by）**

```text
CONFIG_TAD2144
```

**弱选择（Implies）**

```text
CONFIG_TDK_HAL
```

**定义位置（Location）**：[`modules/hal_tdk/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hal_tdk/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_tdk（模块路径 `modules/hal/tdk`，相对于 west 工作区顶层目录） → TDK 驱动（drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_TDK_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_TDK_MODULE)、[`CONFIG_TAD2144`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144)、[`CONFIG_TDK_HAL`](P234_modules_hal_tdk_配置项参考.md#CONFIG_TDK_HAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_TDK_MODULE`。

<!-- kconfig-navigation -->

[上一章](P233_modules_hal_silabs_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P235_modules_hostap_配置项参考.md)
