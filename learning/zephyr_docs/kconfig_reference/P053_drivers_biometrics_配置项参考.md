---
id: learning.zephyr-docs.kconfig-reference.page-53
title: "`drivers/biometrics`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第53章\_`drivers/biometrics`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/biometrics` 的 8 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BIOMETRICS"></a>

## 53.1 `CONFIG_BIOMETRICS`

**提示（Prompt）**：生物识别驱动（Biometrics Drivers）

**说明（Help）**

启用生物识别传感器（Biometric Sensor）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/biometrics/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/biometrics/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_BIOMETRICS_EMUL"></a>

## 53.2 `CONFIG_BIOMETRICS_EMUL`

**提示（Prompt）**：生物识别仿真驱动（Emulated Biometrics Driver）

**说明（Help）**

启用用于测试的生物识别仿真驱动（Emulated Biometrics Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_BIOMETRICS_EMUL_ENABLED && CONFIG_BIOMETRICS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/biometrics/Kconfig.emul:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/biometrics/Kconfig.emul#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BIOMETRICS`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS)。

<a id="CONFIG_BIOMETRICS_GT5X"></a>

## 53.3 `CONFIG_BIOMETRICS_GT5X`

**提示（Prompt）**：ADH GT5X 系列光学指纹传感器（Optical Fingerprint Sensor）

**说明（Help）**

启用 ADH GT5X 系列光学指纹传感器（Optical Fingerprint Sensor）驱动，支持 GT-511C1R、GT-511C3、GT-521F32 和 GT-521F52 型号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADH_TECH_GT5X_ENABLED && CONFIG_BIOMETRICS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL
CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`drivers/biometrics/Kconfig.gt5x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/biometrics/Kconfig.gt5x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BIOMETRICS`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS)、[`CONFIG_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL)、[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_BIOMETRICS_INIT_PRIORITY"></a>

## 53.4 `CONFIG_BIOMETRICS_INIT_PRIORITY`

**提示（Prompt）**：生物识别初始化优先级（Biometrics Init Priority）

**说明（Help）**

生物识别（Biometric）设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BIOMETRICS
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/biometrics/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/biometrics/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BIOMETRICS`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS)。

<a id="CONFIG_BIOMETRICS_SHELL"></a>

## 53.5 `CONFIG_BIOMETRICS_SHELL`

**提示（Prompt）**：生物识别命令行（Biometrics Shell）

**说明（Help）**

启用用于测试的生物识别传感器命令行（Biometric Sensor Shell）命令，提供录入（Enrollment）、匹配（Matching）、模板管理（Template Management）和设备信息查询功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_BIOMETRICS
```

**定义位置（Location）**：[`drivers/biometrics/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/biometrics/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_BIOMETRICS`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS)。

<a id="CONFIG_BIOMETRICS_ZFM_X0"></a>

## 53.6 `CONFIG_BIOMETRICS_ZFM_X0`

**提示（Prompt）**：ZFM-x0 系列光学指纹传感器（Optical Fingerprint Sensor）

**说明（Help）**

启用 ZFM-x0 系列光学指纹传感器（Optical Fingerprint Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZHIANTEC_ZFM_X0_ENABLED && CONFIG_BIOMETRICS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL
CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`drivers/biometrics/Kconfig.zfm_x0:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/biometrics/Kconfig.zfm_x0#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BIOMETRICS`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS)、[`CONFIG_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL)、[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_GT5X_TIMEOUT_MS"></a>

## 53.7 `CONFIG_GT5X_TIMEOUT_MS`

**提示（Prompt）**：默认操作超时，单位为毫秒（Default Operation Timeout）

**说明（Help）**

录入（Enrollment）和匹配（Matching）操作的默认超时时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BIOMETRICS_GT5X && CONFIG_BIOMETRICS
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`drivers/biometrics/Kconfig.gt5x:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/biometrics/Kconfig.gt5x#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers） → ADH GT5X 系列光学指纹传感器（Optical Fingerprint Sensor）

**配置项引用（Symbol References）**：[`CONFIG_BIOMETRICS_GT5X`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS_GT5X)、[`CONFIG_BIOMETRICS`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS)。

<a id="CONFIG_ZFM_X0_TIMEOUT_MS"></a>

## 53.8 `CONFIG_ZFM_X0_TIMEOUT_MS`

**提示（Prompt）**：默认操作超时，单位为毫秒（Default Operation Timeout）

**说明（Help）**

录入（Enrollment）和匹配（Matching）操作的默认超时时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BIOMETRICS_ZFM_X0 && CONFIG_BIOMETRICS
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`drivers/biometrics/Kconfig.zfm_x0:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/biometrics/Kconfig.zfm_x0#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers） → ZFM-x0 系列光学指纹传感器（Optical Fingerprint Sensor）

**配置项引用（Symbol References）**：[`CONFIG_BIOMETRICS_ZFM_X0`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS_ZFM_X0)、[`CONFIG_BIOMETRICS`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS)。

<!-- kconfig-navigation -->

[上一章](P052_drivers_bbram_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P054_drivers_bluetooth_配置项参考_1.md)
