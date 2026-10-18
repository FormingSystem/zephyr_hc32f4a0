---
id: learning.zephyr-docs.kconfig-reference.page-70
title: "`drivers/crc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第70章\_`drivers/crc`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/crc` 的 27 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CRC_AMBIQ"></a>

## 70.1 `CONFIG_CRC_AMBIQ`

**提示（Prompt）**：Ambiq Apollo510 循环冗余校验支持（CRC Support）

**说明（Help）**

启用 Ambiq Apollo510 片上系统（SoC）的硬件加速 CRC32 IEEE 支持。使用 SECURITY CRC 引擎，并对紧耦合存储器（TCM）和 SSRAM 区域提供跨边界保护（Boundary-Crossing Protection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_HW_CRC32_ENABLED && CONFIG_CRC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC_DRIVER_HAS_CRC32_IEEE
```

**定义位置（Location）**：[`drivers/crc/Kconfig.ambiq:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig.ambiq#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_HAS_CRC32_IEEE`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_IEEE)。

<a id="CONFIG_CRC_DRIVER"></a>

## 70.2 `CONFIG_CRC_DRIVER`

**提示（Prompt）**：循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**说明（Help）**

启用循环冗余校验（CRC）设备驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/crc/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_CRC_DRIVER_HAS_CRC16"></a>

## 70.3 `CONFIG_CRC_DRIVER_HAS_CRC16`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC16 计算能力（CRC16 Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_NXP
CONFIG_CRC_DRIVER_NXP_LPC
CONFIG_CRC_DRIVER_RENESAS_RA
CONFIG_CRC_DRIVER_SF32LB
CONFIG_CRC_DRIVER_SILABS_GPCRC
CONFIG_CRC_STM32
```

**定义位置（Location）**：[`drivers/crc/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_NXP`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP)、[`CONFIG_CRC_DRIVER_NXP_LPC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP_LPC)、[`CONFIG_CRC_DRIVER_RENESAS_RA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_RENESAS_RA)、[`CONFIG_CRC_DRIVER_SF32LB`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SF32LB)、[`CONFIG_CRC_DRIVER_SILABS_GPCRC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SILABS_GPCRC)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC16_ANSI"></a>

## 70.4 `CONFIG_CRC_DRIVER_HAS_CRC16_ANSI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC16 ANSI 计算能力（CRC16 ANSI Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT && CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_NXP
CONFIG_CRC_DRIVER_RENESAS_RA
CONFIG_CRC_DRIVER_SF32LB
CONFIG_CRC_DRIVER_SILABS_GPCRC
CONFIG_CRC_STM32
```

**定义位置（Location）**：[`drivers/crc/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT)、[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_NXP`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP)、[`CONFIG_CRC_DRIVER_RENESAS_RA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_RENESAS_RA)、[`CONFIG_CRC_DRIVER_SF32LB`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SF32LB)、[`CONFIG_CRC_DRIVER_SILABS_GPCRC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SILABS_GPCRC)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC16_CCITT"></a>

## 70.5 `CONFIG_CRC_DRIVER_HAS_CRC16_CCITT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC16 CCITT 计算能力（CRC16 CCITT Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_NXP
CONFIG_CRC_DRIVER_NXP_LPC
CONFIG_CRC_DRIVER_RENESAS_RA
CONFIG_CRC_DRIVER_SF32LB
CONFIG_CRC_DRIVER_SILABS_GPCRC
CONFIG_CRC_STM32
```

**定义位置（Location）**：[`drivers/crc/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_NXP`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP)、[`CONFIG_CRC_DRIVER_NXP_LPC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP_LPC)、[`CONFIG_CRC_DRIVER_RENESAS_RA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_RENESAS_RA)、[`CONFIG_CRC_DRIVER_SF32LB`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SF32LB)、[`CONFIG_CRC_DRIVER_SILABS_GPCRC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SILABS_GPCRC)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T"></a>

## 70.6 `CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC16 ITU-T 计算能力（CRC16 ITU-T Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_NXP
CONFIG_CRC_DRIVER_NXP_LPC
CONFIG_CRC_DRIVER_RENESAS_RA
CONFIG_CRC_DRIVER_SF32LB
CONFIG_CRC_DRIVER_SILABS_GPCRC
CONFIG_CRC_STM32
```

**定义位置（Location）**：[`drivers/crc/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_NXP`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP)、[`CONFIG_CRC_DRIVER_NXP_LPC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP_LPC)、[`CONFIG_CRC_DRIVER_RENESAS_RA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_RENESAS_RA)、[`CONFIG_CRC_DRIVER_SF32LB`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SF32LB)、[`CONFIG_CRC_DRIVER_SILABS_GPCRC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SILABS_GPCRC)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT"></a>

## 70.7 `CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备反射式 CRC16 计算能力（CRC16 Reflect Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_NXP
CONFIG_CRC_DRIVER_RENESAS_RA
CONFIG_CRC_DRIVER_SF32LB
CONFIG_CRC_DRIVER_SILABS_GPCRC
CONFIG_CRC_STM32
```

**定义位置（Location）**：[`drivers/crc/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_NXP`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP)、[`CONFIG_CRC_DRIVER_RENESAS_RA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_RENESAS_RA)、[`CONFIG_CRC_DRIVER_SF32LB`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SF32LB)、[`CONFIG_CRC_DRIVER_SILABS_GPCRC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SILABS_GPCRC)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC24_PGP"></a>

## 70.8 `CONFIG_CRC_DRIVER_HAS_CRC24_PGP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC24 PGP 计算能力（CRC24 PGP Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**定义位置（Location）**：[`drivers/crc/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC32_C"></a>

## 70.9 `CONFIG_CRC_DRIVER_HAS_CRC32_C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC32C 计算能力（CRC32C Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_NXP
CONFIG_CRC_DRIVER_RENESAS_RA
CONFIG_CRC_DRIVER_SF32LB
CONFIG_CRC_STM32
```

**定义位置（Location）**：[`drivers/crc/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_NXP`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP)、[`CONFIG_CRC_DRIVER_RENESAS_RA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_RENESAS_RA)、[`CONFIG_CRC_DRIVER_SF32LB`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SF32LB)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC32_IEEE"></a>

## 70.10 `CONFIG_CRC_DRIVER_HAS_CRC32_IEEE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC32 IEEE 计算能力（CRC32 IEEE Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_AMBIQ
CONFIG_CRC_DRIVER_NXP
CONFIG_CRC_DRIVER_NXP_LPC
CONFIG_CRC_DRIVER_RENESAS_RA
CONFIG_CRC_DRIVER_SF32LB
CONFIG_CRC_DRIVER_SILABS_GPCRC
CONFIG_CRC_STM32
```

**定义位置（Location）**：[`drivers/crc/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_AMBIQ`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_AMBIQ)、[`CONFIG_CRC_DRIVER_NXP`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP)、[`CONFIG_CRC_DRIVER_NXP_LPC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP_LPC)、[`CONFIG_CRC_DRIVER_RENESAS_RA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_RENESAS_RA)、[`CONFIG_CRC_DRIVER_SF32LB`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SF32LB)、[`CONFIG_CRC_DRIVER_SILABS_GPCRC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SILABS_GPCRC)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC32_K_4_2"></a>

## 70.11 `CONFIG_CRC_DRIVER_HAS_CRC32_K_4_2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC32K/4.2 计算能力（CRC32K/4.2 Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_SF32LB
```

**定义位置（Location）**：[`drivers/crc/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_SF32LB`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SF32LB)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2"></a>

## 70.12 `CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC32 MPEG-2 计算能力（CRC32 MPEG-2 Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_NXP
CONFIG_CRC_DRIVER_NXP_LPC
CONFIG_CRC_STM32
```

**定义位置（Location）**：[`drivers/crc/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_NXP`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP)、[`CONFIG_CRC_DRIVER_NXP_LPC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_NXP_LPC)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC4"></a>

## 70.13 `CONFIG_CRC_DRIVER_HAS_CRC4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC4 计算能力（CRC4 Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**定义位置（Location）**：[`drivers/crc/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC4_TI"></a>

## 70.14 `CONFIG_CRC_DRIVER_HAS_CRC4_TI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC4 TI 计算能力（CRC4 TI Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**定义位置（Location）**：[`drivers/crc/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC7_BE"></a>

## 70.15 `CONFIG_CRC_DRIVER_HAS_CRC7_BE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备大端 CRC7 计算能力（CRC7 BE Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_STM32
```

**定义位置（Location）**：[`drivers/crc/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC8"></a>

## 70.16 `CONFIG_CRC_DRIVER_HAS_CRC8`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC8 计算能力（CRC8 Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_RENESAS_RA
CONFIG_CRC_DRIVER_SF32LB
CONFIG_CRC_STM32
```

**定义位置（Location）**：[`drivers/crc/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_RENESAS_RA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_RENESAS_RA)、[`CONFIG_CRC_DRIVER_SF32LB`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SF32LB)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC8_CCITT"></a>

## 70.17 `CONFIG_CRC_DRIVER_HAS_CRC8_CCITT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC8 CCITT 计算能力（CRC8 CCITT Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_RENESAS_RA
CONFIG_CRC_DRIVER_SF32LB
CONFIG_CRC_STM32
```

**定义位置（Location）**：[`drivers/crc/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_RENESAS_RA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_RENESAS_RA)、[`CONFIG_CRC_DRIVER_SF32LB`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SF32LB)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)。

<a id="CONFIG_CRC_DRIVER_HAS_CRC8_ROHC"></a>

## 70.18 `CONFIG_CRC_DRIVER_HAS_CRC8_ROHC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

CRC 驱动具备 CRC8 ROHC 计算能力（CRC8 ROHC Computation）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**被选择（Selected by）**

```text
CONFIG_CRC_DRIVER_RENESAS_RA
CONFIG_CRC_DRIVER_SF32LB
CONFIG_CRC_STM32
```

**定义位置（Location）**：[`drivers/crc/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_RENESAS_RA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_RENESAS_RA)、[`CONFIG_CRC_DRIVER_SF32LB`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_SF32LB)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)。

<a id="CONFIG_CRC_DRIVER_INIT_PRIORITY"></a>

## 70.19 `CONFIG_CRC_DRIVER_INIT_PRIORITY`

**提示（Prompt）**：CRC 初始化优先级（Init Priority）

**说明（Help）**

循环冗余校验（CRC）驱动设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/crc/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_CRC_DRIVER_NXP"></a>

## 70.20 `CONFIG_CRC_DRIVER_NXP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用恩智浦（NXP）微控制器（Microcontroller）的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_CRC_ENABLED && CONFIG_CRC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC_DRIVER_HAS_CRC16
CONFIG_CRC_DRIVER_HAS_CRC16_CCITT
CONFIG_CRC_DRIVER_HAS_CRC16_ANSI
CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T
CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT
CONFIG_CRC_DRIVER_HAS_CRC32_C
CONFIG_CRC_DRIVER_HAS_CRC32_IEEE
CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2
```

**定义位置（Location）**：[`drivers/crc/Kconfig.nxp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig.nxp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_HAS_CRC16`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16)、[`CONFIG_CRC_DRIVER_HAS_CRC16_CCITT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_CCITT)、[`CONFIG_CRC_DRIVER_HAS_CRC16_ANSI`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ANSI)、[`CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T)、[`CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT)、[`CONFIG_CRC_DRIVER_HAS_CRC32_C`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_C)、[`CONFIG_CRC_DRIVER_HAS_CRC32_IEEE`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_IEEE)、[`CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2)。

<a id="CONFIG_CRC_DRIVER_NXP_LPC"></a>

## 70.21 `CONFIG_CRC_DRIVER_NXP_LPC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用恩智浦（NXP）微控制器的 LPC 循环冗余校验（CRC）驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_CRC_ENABLED && CONFIG_CRC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC_DRIVER_HAS_CRC16
CONFIG_CRC_DRIVER_HAS_CRC16_CCITT
CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T
CONFIG_CRC_DRIVER_HAS_CRC32_IEEE
CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2
```

**定义位置（Location）**：[`drivers/crc/Kconfig.nxp:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig.nxp#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_HAS_CRC16`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16)、[`CONFIG_CRC_DRIVER_HAS_CRC16_CCITT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_CCITT)、[`CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T)、[`CONFIG_CRC_DRIVER_HAS_CRC32_IEEE`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_IEEE)、[`CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2)。

<a id="CONFIG_CRC_DRIVER_RENESAS_RA"></a>

## 70.22 `CONFIG_CRC_DRIVER_RENESAS_RA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用瑞萨（Renesas）RA 微控制器（Microcontroller）的驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_CRC_ENABLED && CONFIG_CRC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC_DRIVER_HAS_CRC8
CONFIG_CRC_DRIVER_HAS_CRC8_ROHC
CONFIG_CRC_DRIVER_HAS_CRC8_CCITT
CONFIG_CRC_DRIVER_HAS_CRC16
CONFIG_CRC_DRIVER_HAS_CRC16_CCITT
CONFIG_CRC_DRIVER_HAS_CRC16_ANSI
CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T
CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT
CONFIG_CRC_DRIVER_HAS_CRC32_C
CONFIG_CRC_DRIVER_HAS_CRC32_IEEE
CONFIG_USE_RA_FSP_CRC
```

**定义位置（Location）**：[`drivers/crc/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_HAS_CRC8`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC8)、[`CONFIG_CRC_DRIVER_HAS_CRC8_ROHC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC8_ROHC)、[`CONFIG_CRC_DRIVER_HAS_CRC8_CCITT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC8_CCITT)、[`CONFIG_CRC_DRIVER_HAS_CRC16`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16)、[`CONFIG_CRC_DRIVER_HAS_CRC16_CCITT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_CCITT)、[`CONFIG_CRC_DRIVER_HAS_CRC16_ANSI`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ANSI)、[`CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T)、[`CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT)、[`CONFIG_CRC_DRIVER_HAS_CRC32_C`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_C)、[`CONFIG_CRC_DRIVER_HAS_CRC32_IEEE`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_IEEE)、[`CONFIG_USE_RA_FSP_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_CRC)。

<a id="CONFIG_CRC_DRIVER_SF32LB"></a>

## 70.23 `CONFIG_CRC_DRIVER_SF32LB`

**提示（Prompt）**：思澈 SF32LB CRC 驱动（SiFli CRC Driver）

**说明（Help）**

启用思澈（SiFli）SF32LB 片上系统（SoC）中的循环冗余校验（CRC）外设支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_CRC_ENABLED && CONFIG_CRC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC_DRIVER_HAS_CRC8
CONFIG_CRC_DRIVER_HAS_CRC8_ROHC
CONFIG_CRC_DRIVER_HAS_CRC8_CCITT
CONFIG_CRC_DRIVER_HAS_CRC16
CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT
CONFIG_CRC_DRIVER_HAS_CRC16_ANSI
CONFIG_CRC_DRIVER_HAS_CRC16_CCITT
CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T
CONFIG_CRC_DRIVER_HAS_CRC32_IEEE
CONFIG_CRC_DRIVER_HAS_CRC32_C
CONFIG_CRC_DRIVER_HAS_CRC32_K_4_2
```

**定义位置（Location）**：[`drivers/crc/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_HAS_CRC8`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC8)、[`CONFIG_CRC_DRIVER_HAS_CRC8_ROHC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC8_ROHC)、[`CONFIG_CRC_DRIVER_HAS_CRC8_CCITT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC8_CCITT)、[`CONFIG_CRC_DRIVER_HAS_CRC16`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16)、[`CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT)、[`CONFIG_CRC_DRIVER_HAS_CRC16_ANSI`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ANSI)、[`CONFIG_CRC_DRIVER_HAS_CRC16_CCITT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_CCITT)、[`CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T)、[`CONFIG_CRC_DRIVER_HAS_CRC32_IEEE`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_IEEE)、[`CONFIG_CRC_DRIVER_HAS_CRC32_C`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_C)、[`CONFIG_CRC_DRIVER_HAS_CRC32_K_4_2`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_K_4_2)。

<a id="CONFIG_CRC_DRIVER_SILABS_GPCRC"></a>

## 70.24 `CONFIG_CRC_DRIVER_SILABS_GPCRC`

**提示（Prompt）**：Silicon Labs 通用 CRC 驱动（GPCRC Driver）

**说明（Help）**

启用 Silicon Labs Gecko，即 EFR32／EFM32，微控制器的通用循环冗余校验（General Purpose CRC，GPCRC）驱动实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GPCRC_ENABLED && CONFIG_CRC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_GPCRC
CONFIG_CRC_DRIVER_HAS_CRC16
CONFIG_CRC_DRIVER_HAS_CRC16_ANSI
CONFIG_CRC_DRIVER_HAS_CRC16_CCITT
CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T
CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT
CONFIG_CRC_DRIVER_HAS_CRC32_IEEE
```

**定义位置（Location）**：[`drivers/crc/Kconfig.silabs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig.silabs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_SILABS_SISDK_GPCRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_GPCRC)、[`CONFIG_CRC_DRIVER_HAS_CRC16`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16)、[`CONFIG_CRC_DRIVER_HAS_CRC16_ANSI`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ANSI)、[`CONFIG_CRC_DRIVER_HAS_CRC16_CCITT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_CCITT)、[`CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T)、[`CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT)、[`CONFIG_CRC_DRIVER_HAS_CRC32_IEEE`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_IEEE)。

<a id="CONFIG_CRC_STM32"></a>

## 70.25 `CONFIG_CRC_STM32`

**提示（Prompt）**：STM32 CRC 驱动（Driver）

**说明（Help）**

启用 STM32 系列的循环冗余校验（CRC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_CRC_ENABLED && CONFIG_CRC_DRIVER
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC_DRIVER_HAS_CRC7_BE
CONFIG_CRC_DRIVER_HAS_CRC8
CONFIG_CRC_DRIVER_HAS_CRC8_CCITT
CONFIG_CRC_DRIVER_HAS_CRC8_ROHC
CONFIG_CRC_DRIVER_HAS_CRC16
CONFIG_CRC_DRIVER_HAS_CRC16_CCITT
CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T
CONFIG_CRC_DRIVER_HAS_CRC16_ANSI
CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT
CONFIG_CRC_DRIVER_HAS_CRC32_C
CONFIG_CRC_DRIVER_HAS_CRC32_IEEE
CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2
```

**定义位置（Location）**：[`drivers/crc/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_CRC_DRIVER_HAS_CRC7_BE`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC7_BE)、[`CONFIG_CRC_DRIVER_HAS_CRC8`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC8)、[`CONFIG_CRC_DRIVER_HAS_CRC8_CCITT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC8_CCITT)、[`CONFIG_CRC_DRIVER_HAS_CRC8_ROHC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC8_ROHC)、[`CONFIG_CRC_DRIVER_HAS_CRC16`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16)、[`CONFIG_CRC_DRIVER_HAS_CRC16_CCITT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_CCITT)、[`CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T)、[`CONFIG_CRC_DRIVER_HAS_CRC16_ANSI`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ANSI)、[`CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT)、[`CONFIG_CRC_DRIVER_HAS_CRC32_C`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_C)、[`CONFIG_CRC_DRIVER_HAS_CRC32_IEEE`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_IEEE)、[`CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2)。

<a id="CONFIG_CRC_STM32_DMA"></a>

## 70.26 `CONFIG_CRC_STM32_DMA`

**提示（Prompt）**：直接内存访问支持（DMA Support）

**说明（Help）**

为设备树节点（Devicetree Node）中启用了 DMA 通道的 CRC 实例，启用直接内存访问（DMA）传输，将数据送到 CRC 输入端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_STM32 && CONFIG_CRC_DRIVER
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/crc/Kconfig.stm32:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig.stm32#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC） → STM32 CRC 驱动（Driver）

**配置项引用（Symbol References）**：[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)、[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_CRC_STM32_DMA_THRESHOLD"></a>

## 70.27 `CONFIG_CRC_STM32_DMA_THRESHOLD`

**提示（Prompt）**：使用 DMA 传输的最小缓冲区大小（Minimal Buffer Size）

**说明（Help）**

将提供给 `crc_update()` 的缓冲区复制到 CRC 外设时，允许使用直接内存访问（DMA）传输的最小大小。

缓冲区大小大于或等于此值时，使用 DMA 将内容复制到 CRC 外设；传输期间，CPU 可以执行其他线程。缓冲区大小严格小于此值时，由 CPU 忙于执行复制（Busy CPU Copy），不使用 DMA。

默认值 1 会让 `crc_update()` 无条件使用 DMA 传输，不受缓冲区大小影响。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_STM32_DMA && CONFIG_CRC_STM32 && CONFIG_CRC_DRIVER
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 4294967295]
```

**定义位置（Location）**：[`drivers/crc/Kconfig.stm32:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crc/Kconfig.stm32#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 循环冗余校验驱动（Cyclic Redundancy Check，CRC） → STM32 CRC 驱动（Driver） → 直接内存访问支持（DMA Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_STM32_DMA`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32_DMA)、[`CONFIG_CRC_STM32`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_STM32)、[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)。

<!-- kconfig-navigation -->

[上一章](P069_drivers_counter_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P071_drivers_crypto_配置项参考.md)
