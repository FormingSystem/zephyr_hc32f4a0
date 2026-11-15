---
id: learning.zephyr-docs.kconfig-reference.page-291
title: "`soc/nordic`配置项参考（3/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第291章\_`soc/nordic`配置项参考（3/3）

本章翻译官方 Kconfig 数据库中 `soc/nordic` 的 76 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_NRF9280_CPUPPR"></a>

## 291.1 `CONFIG_SOC_NRF9280_CPUPPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF9280 PPR 内核（CPUPPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF9280
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF9280PDK
```

**定义位置（Location）**：[`soc/nordic/nrf92/Kconfig.soc:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf92/Kconfig.soc#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF9280`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF9280)、[`CONFIG_BOARD_NRF9280PDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF9280PDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF9280PDK`。

<a id="CONFIG_SOC_NRF9280_CPURAD"></a>

## 291.2 `CONFIG_SOC_NRF9280_CPURAD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF9280 无线电 CPU（CPURAD）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_NRF9280
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NRF9280PDK
```

**定义位置（Location）**：[`soc/nordic/nrf92/Kconfig.soc:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf92/Kconfig.soc#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF9280`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF9280)、[`CONFIG_BOARD_NRF9280PDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF9280PDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NRF9280PDK`。

<a id="CONFIG_SOC_NRF_FORCE_CONSTLAT"></a>

## 291.3 `CONFIG_SOC_NRF_FORCE_CONSTLAT`

**提示（Prompt）**：系统开启时强制使用恒定延迟模式（constant latency mode in system ON）

**说明（Help）**

在恒定延迟模式（constant latency mode）中，CPU 唤醒延迟和可编程外设互连（PPI）任务响应时间将保持恒定且最小。通过在睡眠期间强制开启一组基础资源来保证这一点。获得恒定、可预测延迟的代价是功耗增加。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_RISCV && CONFIG_NRF_SYS_EVENT && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → nRF 系统事件支持（system event support）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_NRF_SYS_EVENT`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SYS_EVENT)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_NRF_GPIO_FORWARDER_FOR_NRF5340"></a>

## 291.4 `CONFIG_SOC_NRF_GPIO_FORWARDER_FOR_NRF5340`

**提示（Prompt）**：将 GPIO 引脚转交网络内核（Forward GPIO pins to network core）

**说明（Help）**

使用转发器兼容标识（forwarder compatible）配置的引脚将转交网络内核使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_SOC_SECURE_SUPPORTED && CONFIG_SOC_NRF5340_CPUAPP && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_NRF_SOC_SECURE_SUPPORTED`](P290_soc_nordic_配置项参考_2.md#CONFIG_NRF_SOC_SECURE_SUPPORTED)、[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_SERIES_NRF51"></a>

## 291.5 `CONFIG_SOC_SERIES_NRF51`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NRF51 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_NRF51X
CONFIG_SOC_NRF51822_QFAA
CONFIG_SOC_NRF51822_QFAB
CONFIG_SOC_NRF51822_QFAC
```

**定义位置（Location）**：[`soc/nordic/nrf51/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf51/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_SERIES_NRF51X`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51X)、[`CONFIG_SOC_NRF51822_QFAA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF51822_QFAA)、[`CONFIG_SOC_NRF51822_QFAB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF51822_QFAB)、[`CONFIG_SOC_NRF51822_QFAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF51822_QFAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_NRF51822_QFAA`、`CONFIG_SOC_NRF51822_QFAB`、`CONFIG_SOC_NRF51822_QFAC`。

<a id="CONFIG_SOC_SERIES_NRF51X"></a>

## 291.6 `CONFIG_SOC_SERIES_NRF51X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF51`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF51
```

**定义位置（Location）**：[`soc/nordic/nrf51/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf51/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF51)。

<a id="CONFIG_SOC_SERIES_NRF52"></a>

## 291.7 `CONFIG_SOC_SERIES_NRF52`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NRF52 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_NRF52X
CONFIG_SOC_NRF52805
CONFIG_SOC_NRF52810
CONFIG_SOC_NRF52811
CONFIG_SOC_NRF52820
CONFIG_SOC_NRF52832
CONFIG_SOC_NRF52833
CONFIG_SOC_NRF52840
```

**定义位置（Location）**：[`soc/nordic/nrf52/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf52/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_SERIES_NRF52X`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF52X)、[`CONFIG_SOC_NRF52805`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52805)、[`CONFIG_SOC_NRF52810`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52810)、[`CONFIG_SOC_NRF52811`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52811)、[`CONFIG_SOC_NRF52820`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52820)、[`CONFIG_SOC_NRF52832`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52832)、[`CONFIG_SOC_NRF52833`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52833)、[`CONFIG_SOC_NRF52840`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52840)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_NRF52805`、`CONFIG_SOC_NRF52810`、`CONFIG_SOC_NRF52811`、`CONFIG_SOC_NRF52820`、`CONFIG_SOC_NRF52832`、`CONFIG_SOC_NRF52833`、`CONFIG_SOC_NRF52840`。

<a id="CONFIG_SOC_SERIES_NRF52X"></a>

## 291.8 `CONFIG_SOC_SERIES_NRF52X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF52`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF52
```

**定义位置（Location）**：[`soc/nordic/nrf52/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf52/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF52`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF52)。

<a id="CONFIG_SOC_SERIES_NRF53"></a>

## 291.9 `CONFIG_SOC_SERIES_NRF53`

原库同名定义共 2 条；本项为数据库第 17992 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NRF53 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_NRF53X
CONFIG_SOC_NRF5340_CPUAPP
CONFIG_SOC_NRF5340_CPUNET
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_SERIES_NRF53X`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53X)、[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_NRF5340_CPUNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUNET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_NRF5340_CPUNET`。

<a id="CONFIG_SOC_SERIES_NRF53--record-17993"></a>

## 291.10 `CONFIG_SOC_SERIES_NRF53`

原库同名定义共 2 条；本项为数据库第 17993 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NRF53 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**主动选择（Selects）**

```text
CONFIG_ARM
CONFIG_SOC_COMPATIBLE_NRF53X
CONFIG_SOC_EARLY_INIT_HOOK
CONFIG_CPU_CORTEX_M33
CONFIG_CPU_CORTEX_M_HAS_DWT
CONFIG_CPU_HAS_ARM_MPU
CONFIG_HAS_NRFX
CONFIG_HAS_NORDIC_DRIVERS
CONFIG_HAS_NORDIC_RAM_CTRL
CONFIG_HAS_SEGGER_RTT if CONFIG_ZEPHYR_SEGGER_MODULE
CONFIG_HAS_SWO
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_NRF53X
CONFIG_SOC_NRF5340_CPUAPP
CONFIG_SOC_NRF5340_CPUNET
```

**弱选择（Implies）**

```text
CONFIG_XIP
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_SOC_COMPATIBLE_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF53X)、[`CONFIG_SOC_EARLY_INIT_HOOK`](P002_kernel_配置项参考_2.md#CONFIG_SOC_EARLY_INIT_HOOK)、[`CONFIG_CPU_CORTEX_M33`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M33)、[`CONFIG_CPU_CORTEX_M_HAS_DWT`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_DWT)、[`CONFIG_CPU_HAS_ARM_MPU`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_ARM_MPU)、[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_HAS_NORDIC_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_DRIVERS)、[`CONFIG_HAS_NORDIC_RAM_CTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_RAM_CTRL)、[`CONFIG_HAS_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_HAS_SEGGER_RTT)、[`CONFIG_ZEPHYR_SEGGER_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_SEGGER_MODULE)、[`CONFIG_HAS_SWO`](P030_arch_arm_配置项参考_2.md#CONFIG_HAS_SWO)、[`CONFIG_SOC_SERIES_NRF53X`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53X)、[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_NRF5340_CPUNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUNET)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_COMPATIBLE_NRF53X`、`CONFIG_HAS_NRFX`、`CONFIG_HAS_NORDIC_DRIVERS`、`CONFIG_HAS_NORDIC_RAM_CTRL`、`CONFIG_ZEPHYR_SEGGER_MODULE`、`CONFIG_SOC_NRF5340_CPUAPP`、`CONFIG_SOC_NRF5340_CPUNET`。

<a id="CONFIG_SOC_SERIES_NRF53X"></a>

## 291.11 `CONFIG_SOC_SERIES_NRF53X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF53`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF53
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)。

<a id="CONFIG_SOC_SERIES_NRF54H"></a>

## 291.12 `CONFIG_SOC_SERIES_NRF54H`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Nordic Semiconductor nRF54H 系列微控制器（series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_NRF54HX
CONFIG_SOC_NRF54H20
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_SERIES_NRF54HX`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54HX)、[`CONFIG_SOC_NRF54H20`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_SERIES_NRF54HX"></a>

## 291.13 `CONFIG_SOC_SERIES_NRF54HX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF54H`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF54H
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54H)。

<a id="CONFIG_SOC_SERIES_NRF54L"></a>

## 291.14 `CONFIG_SOC_SERIES_NRF54L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Nordic Semiconductor nRF54L 系列微控制器（series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_NRF54LX
CONFIG_SOC_NRF54L05
CONFIG_SOC_NRF54L10
CONFIG_SOC_NRF54L15
CONFIG_SOC_NRF54LM20A
CONFIG_SOC_NRF54LM20B
CONFIG_SOC_NRF54LV10A
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_SERIES_NRF54LX`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54LX)、[`CONFIG_SOC_NRF54L05`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L05)、[`CONFIG_SOC_NRF54L10`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L10)、[`CONFIG_SOC_NRF54L15`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54L15)、[`CONFIG_SOC_NRF54LM20A`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LM20A)、[`CONFIG_SOC_NRF54LM20B`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LM20B)、[`CONFIG_SOC_NRF54LV10A`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54LV10A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_SERIES_NRF54LX"></a>

## 291.15 `CONFIG_SOC_SERIES_NRF54LX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF54L`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF54L
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF54L)。

<a id="CONFIG_SOC_SERIES_NRF71"></a>

## 291.16 `CONFIG_SOC_SERIES_NRF71`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Nordic Semiconductor nRF71 系列微控制器（series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
CONFIG_SOC_NRF7120
CONFIG_SOC_NRF7120E
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_NRF7120`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120)、[`CONFIG_SOC_NRF7120E`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF7120E)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_SERIES_NRF71_TFM_RAM_CTRL_SERVICE"></a>

## 291.17 `CONFIG_SOC_SERIES_NRF71_TFM_RAM_CTRL_SERVICE`

**提示（Prompt）**：TF-M RAM 控制服务（RAM control service）

**说明（Help）**

提供 TF-M 安全服务（secure service），允许非安全应用驱动仅供安全侧使用的 MEMCONF：在系统开启状态（System ON）中为非安全 RAM 上电／断电，并选择在系统关闭状态（System OFF）期间保留哪些 RAM 区段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NORDIC_RAM_CTRL && CONFIG_SOC_SERIES_NRF71 && CONFIG_BUILD_WITH_TFM && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NORDIC_RAM_CTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NORDIC_RAM_CTRL)、[`CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NORDIC_RAM_CTRL`、`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_SERIES_NRF91"></a>

## 291.18 `CONFIG_SOC_SERIES_NRF91`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NRF91 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_NRF91X
CONFIG_SOC_NRF9120
CONFIG_SOC_NRF9160
```

**定义位置（Location）**：[`soc/nordic/nrf91/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf91/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_SERIES_NRF91X`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF91X)、[`CONFIG_SOC_NRF9120`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9120)、[`CONFIG_SOC_NRF9160`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9160)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_NRF9120`、`CONFIG_SOC_NRF9160`。

<a id="CONFIG_SOC_SERIES_NRF91X"></a>

## 291.19 `CONFIG_SOC_SERIES_NRF91X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF91`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF91
```

**定义位置（Location）**：[`soc/nordic/nrf91/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf91/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF91`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF91)。

<a id="CONFIG_SOC_SERIES_NRF92"></a>

## 291.20 `CONFIG_SOC_SERIES_NRF92`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NRF92 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_NRF92X
CONFIG_SOC_NRF9230_ENGB
```

**定义位置（Location）**：[`soc/nordic/nrf92/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf92/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SOC_SERIES_NRF92X`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF92X)、[`CONFIG_SOC_NRF9230_ENGB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`、`CONFIG_SOC_NRF9230_ENGB`。

<a id="CONFIG_SOC_SERIES_NRF92X"></a>

## 291.21 `CONFIG_SOC_SERIES_NRF92X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF92`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NRF92
```

**定义位置（Location）**：[`soc/nordic/nrf92/Kconfig.soc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf92/Kconfig.soc#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NRF92`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF92)。

<a id="CONFIG_SOC_VENDOR_NORDIC_GPPI_EXT_ALLOCATOR_DEFER_CONN_REQ"></a>

## 291.22 `CONFIG_SOC_VENDOR_NORDIC_GPPI_EXT_ALLOCATOR_DEFER_CONN_REQ`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在系统工作队列（system workqueue）中处理连接分配与释放请求，而不是直接在进程间通信（IPC）接收回调中处理。当连接管理可能阻塞时，例如触发 IRONSIDE 调用时，需要这样做，因为 IPC 接收回调可能运行在中断上下文（interrupt context）中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPPI_EXT_ALLOCATOR && CONFIG_MULTITHREADING && CONFIG_IRONSIDE_SE_CALL && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 通用可编程外设互连外部分配器（GPPI external allocator）

**配置项引用（Symbol References）**：[`CONFIG_GPPI_EXT_ALLOCATOR`](P289_soc_nordic_配置项参考_1.md#CONFIG_GPPI_EXT_ALLOCATOR)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_IRONSIDE_SE_CALL`](P227_modules_hal_nordic_配置项参考_1.md#CONFIG_IRONSIDE_SE_CALL)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SOC_VENDOR_NORDIC_GPPI_EXT_ALLOCATOR_DEFER_CONN_REQ_CNT"></a>

## 291.23 `CONFIG_SOC_VENDOR_NORDIC_GPPI_EXT_ALLOCATOR_DEFER_CONN_REQ_CNT`

**提示（Prompt）**：队列中等待处理的 GPPI 外部分配器连接请求数量（pending connection requests）

**说明（Help）**

可排队等待延迟处理（deferred handling）的连接请求数量。队列已满时收到的请求会被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_VENDOR_NORDIC_GPPI_EXT_ALLOCATOR_DEFER_CONN_REQ && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`soc/nordic/common/Kconfig:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/common/Kconfig#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 通用可编程外设互连外部分配器（GPPI external allocator）

**配置项引用（Symbol References）**：[`CONFIG_SOC_VENDOR_NORDIC_GPPI_EXT_ALLOCATOR_DEFER_CONN_REQ`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_VENDOR_NORDIC_GPPI_EXT_ALLOCATOR_DEFER_CONN_REQ)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_TFM_FLASH_MERGED_BINARY"></a>

## 291.24 `CONFIG_TFM_FLASH_MERGED_BINARY`

原库同名定义共 2 条；本项为数据库第 18924 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

默认情况下，如果与 TF-M 一同构建，则指示构建系统烧录合并的 TF-M 安全镜像（Secure）与 Zephyr 非安全镜像（Non Secure）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_TFM_LOG_LEVEL_SILENCE"></a>

## 291.25 `CONFIG_TFM_LOG_LEVEL_SILENCE`

原库同名定义共 2 条；本项为数据库第 18939 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 `uart1` 节点未通过引脚控制（pinctrl）分配 GPIO 引脚，则禁用 TF-M 安全侧输出（secure output）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y if !n
```

**定义位置（Location）**：[`soc/nordic/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_TFM_NRF_NS_STORAGE"></a>

## 291.26 `CONFIG_TFM_NRF_NS_STORAGE`

**提示（Prompt）**：TF-M 非安全存储分区（non-secure storage partition）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nordic/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="SB_CONFIG_SOC_NRF54H20"></a>

## 291.27 `SB_CONFIG_SOC_NRF54H20`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF54H20 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF54H
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF54H20_CPUAPP
SB_CONFIG_SOC_NRF54H20_CPURAD
SB_CONFIG_SOC_NRF54H20_CPUPPR
SB_CONFIG_SOC_NRF54H20_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF54H)、[`SB_CONFIG_SOC_NRF54H20_CPUAPP`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54H20_CPUAPP)、[`SB_CONFIG_SOC_NRF54H20_CPURAD`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54H20_CPURAD)、[`SB_CONFIG_SOC_NRF54H20_CPUPPR`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54H20_CPUPPR)、[`SB_CONFIG_SOC_NRF54H20_CPUFLPR`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54H20_CPUFLPR)。

<a id="SB_CONFIG_SOC_NRF54H20_CPUAPP"></a>

## 291.28 `SB_CONFIG_SOC_NRF54H20_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF54H20 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54H20
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54H20DK
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L27)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54H20`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54H20)、[`SB_CONFIG_BOARD_NRF54H20DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54H20DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54H20DK`。

<a id="SB_CONFIG_SOC_NRF54H20_CPUFLPR"></a>

## 291.29 `SB_CONFIG_SOC_NRF54H20_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF54H20 FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54H20
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54H20DK
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L45)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54H20`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54H20)、[`SB_CONFIG_BOARD_NRF54H20DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54H20DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54H20DK`。

<a id="SB_CONFIG_SOC_NRF54H20_CPUPPR"></a>

## 291.30 `SB_CONFIG_SOC_NRF54H20_CPUPPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF54H20 PPR 内核（CPUPPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54H20
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54H20DK
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L39)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54H20`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54H20)、[`SB_CONFIG_BOARD_NRF54H20DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54H20DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54H20DK`。

<a id="SB_CONFIG_SOC_NRF54H20_CPURAD"></a>

## 291.31 `SB_CONFIG_SOC_NRF54H20_CPURAD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF54H20 无线电 CPU（CPURAD）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54H20
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54H20DK
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L33)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54H20`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54H20)、[`SB_CONFIG_BOARD_NRF54H20DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54H20DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54H20DK`。

<a id="SB_CONFIG_SOC_NRF54L05"></a>

## 291.32 `SB_CONFIG_SOC_NRF54L05`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L05 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF54L
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF54L05_CPUAPP
SB_CONFIG_SOC_NRF54L05_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF54L)、[`SB_CONFIG_SOC_NRF54L05_CPUAPP`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L05_CPUAPP)、[`SB_CONFIG_SOC_NRF54L05_CPUFLPR`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L05_CPUFLPR)。

<a id="SB_CONFIG_SOC_NRF54L05_CPUAPP"></a>

## 291.33 `SB_CONFIG_SOC_NRF54L05_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L05 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54L05
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54L15DK
SB_CONFIG_BOARD_UBX_EVKNORAB2
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L27)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54L05`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L05)、[`SB_CONFIG_BOARD_NRF54L15DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54L15DK)、[`SB_CONFIG_BOARD_UBX_EVKNORAB2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UBX_EVKNORAB2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54L15DK`、`SB_CONFIG_BOARD_UBX_EVKNORAB2`。

<a id="SB_CONFIG_SOC_NRF54L05_CPUFLPR"></a>

## 291.34 `SB_CONFIG_SOC_NRF54L05_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L05 FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54L05
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54L15DK
SB_CONFIG_BOARD_UBX_EVKNORAB2
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L33)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54L05`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L05)、[`SB_CONFIG_BOARD_NRF54L15DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54L15DK)、[`SB_CONFIG_BOARD_UBX_EVKNORAB2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UBX_EVKNORAB2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54L15DK`、`SB_CONFIG_BOARD_UBX_EVKNORAB2`。

<a id="SB_CONFIG_SOC_NRF54L10"></a>

## 291.35 `SB_CONFIG_SOC_NRF54L10`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L10 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF54L
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF54L10_CPUAPP
SB_CONFIG_SOC_NRF54L10_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L39)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF54L)、[`SB_CONFIG_SOC_NRF54L10_CPUAPP`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L10_CPUAPP)、[`SB_CONFIG_SOC_NRF54L10_CPUFLPR`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L10_CPUFLPR)。

<a id="SB_CONFIG_SOC_NRF54L10_CPUAPP"></a>

## 291.36 `SB_CONFIG_SOC_NRF54L10_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L10 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54L10
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54L15DK
SB_CONFIG_BOARD_UBX_EVKNORAB2
SB_CONFIG_BOARD_BL54L15_DVK
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L45)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54L10`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L10)、[`SB_CONFIG_BOARD_NRF54L15DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54L15DK)、[`SB_CONFIG_BOARD_UBX_EVKNORAB2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UBX_EVKNORAB2)、[`SB_CONFIG_BOARD_BL54L15_DVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BL54L15_DVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54L15DK`、`SB_CONFIG_BOARD_UBX_EVKNORAB2`、`SB_CONFIG_BOARD_BL54L15_DVK`。

<a id="SB_CONFIG_SOC_NRF54L10_CPUFLPR"></a>

## 291.37 `SB_CONFIG_SOC_NRF54L10_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L10 FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54L10
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54L15DK
SB_CONFIG_BOARD_UBX_EVKNORAB2
SB_CONFIG_BOARD_BL54L15_DVK
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L51)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54L10`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L10)、[`SB_CONFIG_BOARD_NRF54L15DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54L15DK)、[`SB_CONFIG_BOARD_UBX_EVKNORAB2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UBX_EVKNORAB2)、[`SB_CONFIG_BOARD_BL54L15_DVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BL54L15_DVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54L15DK`、`SB_CONFIG_BOARD_UBX_EVKNORAB2`、`SB_CONFIG_BOARD_BL54L15_DVK`。

<a id="SB_CONFIG_SOC_NRF54L15"></a>

## 291.38 `SB_CONFIG_SOC_NRF54L15`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L15 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF54L
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF54L15_CPUAPP
SB_CONFIG_SOC_NRF54L15_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L57)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF54L)、[`SB_CONFIG_SOC_NRF54L15_CPUAPP`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L15_CPUAPP)、[`SB_CONFIG_SOC_NRF54L15_CPUFLPR`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L15_CPUFLPR)。

<a id="SB_CONFIG_SOC_NRF54L15_CPUAPP"></a>

## 291.39 `SB_CONFIG_SOC_NRF54L15_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L15 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54L15
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54L15TAG
SB_CONFIG_BOARD_NRF54L15DK
SB_CONFIG_BOARD_NRF93M1DK
SB_CONFIG_BOARD_OPHELIA4EV
SB_CONFIG_BOARD_XIAO_NRF54L15
SB_CONFIG_BOARD_EC4L15BA1
SB_CONFIG_BOARD_UBX_EVKNORAB2
SB_CONFIG_BOARD_HOLYIOT_25008
SB_CONFIG_BOARD_RAYTAC_AN54LV_DB_15
SB_CONFIG_BOARD_RAYTAC_AN54LQ_DB_15
SB_CONFIG_BOARD_BL54L15_DVK
SB_CONFIG_BOARD_PANB611EVB
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L63)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54L15`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L15)、[`SB_CONFIG_BOARD_NRF54L15TAG`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54L15TAG)、[`SB_CONFIG_BOARD_NRF54L15DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54L15DK)、[`SB_CONFIG_BOARD_NRF93M1DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF93M1DK)、[`SB_CONFIG_BOARD_OPHELIA4EV`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_OPHELIA4EV)、[`SB_CONFIG_BOARD_XIAO_NRF54L15`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_NRF54L15)、[`SB_CONFIG_BOARD_EC4L15BA1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EC4L15BA1)、[`SB_CONFIG_BOARD_UBX_EVKNORAB2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UBX_EVKNORAB2)、[`SB_CONFIG_BOARD_HOLYIOT_25008`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HOLYIOT_25008)、[`SB_CONFIG_BOARD_RAYTAC_AN54LV_DB_15`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RAYTAC_AN54LV_DB_15)、[`SB_CONFIG_BOARD_RAYTAC_AN54LQ_DB_15`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RAYTAC_AN54LQ_DB_15)、[`SB_CONFIG_BOARD_BL54L15_DVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BL54L15_DVK)、[`SB_CONFIG_BOARD_PANB611EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_PANB611EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54L15TAG`、`SB_CONFIG_BOARD_NRF54L15DK`、`SB_CONFIG_BOARD_NRF93M1DK`、`SB_CONFIG_BOARD_OPHELIA4EV`、`SB_CONFIG_BOARD_XIAO_NRF54L15`、`SB_CONFIG_BOARD_EC4L15BA1`、`SB_CONFIG_BOARD_UBX_EVKNORAB2`、`SB_CONFIG_BOARD_HOLYIOT_25008`、`SB_CONFIG_BOARD_RAYTAC_AN54LV_DB_15`、`SB_CONFIG_BOARD_RAYTAC_AN54LQ_DB_15`、`SB_CONFIG_BOARD_BL54L15_DVK`、`SB_CONFIG_BOARD_PANB611EVB`。

<a id="SB_CONFIG_SOC_NRF54L15_CPUFLPR"></a>

## 291.40 `SB_CONFIG_SOC_NRF54L15_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54L15 FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54L15
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54L15TAG
SB_CONFIG_BOARD_NRF54L15DK
SB_CONFIG_BOARD_NRF93M1DK
SB_CONFIG_BOARD_OPHELIA4EV
SB_CONFIG_BOARD_XIAO_NRF54L15
SB_CONFIG_BOARD_EC4L15BA1
SB_CONFIG_BOARD_UBX_EVKNORAB2
SB_CONFIG_BOARD_RAYTAC_AN54LV_DB_15
SB_CONFIG_BOARD_RAYTAC_AN54LQ_DB_15
SB_CONFIG_BOARD_BL54L15_DVK
SB_CONFIG_BOARD_PANB611EVB
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L69)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54L15`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L15)、[`SB_CONFIG_BOARD_NRF54L15TAG`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54L15TAG)、[`SB_CONFIG_BOARD_NRF54L15DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54L15DK)、[`SB_CONFIG_BOARD_NRF93M1DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF93M1DK)、[`SB_CONFIG_BOARD_OPHELIA4EV`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_OPHELIA4EV)、[`SB_CONFIG_BOARD_XIAO_NRF54L15`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_NRF54L15)、[`SB_CONFIG_BOARD_EC4L15BA1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EC4L15BA1)、[`SB_CONFIG_BOARD_UBX_EVKNORAB2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UBX_EVKNORAB2)、[`SB_CONFIG_BOARD_RAYTAC_AN54LV_DB_15`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RAYTAC_AN54LV_DB_15)、[`SB_CONFIG_BOARD_RAYTAC_AN54LQ_DB_15`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RAYTAC_AN54LQ_DB_15)、[`SB_CONFIG_BOARD_BL54L15_DVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BL54L15_DVK)、[`SB_CONFIG_BOARD_PANB611EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_PANB611EVB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54L15TAG`、`SB_CONFIG_BOARD_NRF54L15DK`、`SB_CONFIG_BOARD_NRF93M1DK`、`SB_CONFIG_BOARD_OPHELIA4EV`、`SB_CONFIG_BOARD_XIAO_NRF54L15`、`SB_CONFIG_BOARD_EC4L15BA1`、`SB_CONFIG_BOARD_UBX_EVKNORAB2`、`SB_CONFIG_BOARD_RAYTAC_AN54LV_DB_15`、`SB_CONFIG_BOARD_RAYTAC_AN54LQ_DB_15`、`SB_CONFIG_BOARD_BL54L15_DVK`、`SB_CONFIG_BOARD_PANB611EVB`。

<a id="SB_CONFIG_SOC_NRF54LM20A"></a>

## 291.41 `SB_CONFIG_SOC_NRF54LM20A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LM20A 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF54L
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF54LM20A_CPUAPP
SB_CONFIG_SOC_NRF54LM20A_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L75)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF54L)、[`SB_CONFIG_SOC_NRF54LM20A_CPUAPP`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LM20A_CPUAPP)、[`SB_CONFIG_SOC_NRF54LM20A_CPUFLPR`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LM20A_CPUFLPR)。

<a id="SB_CONFIG_SOC_NRF54LM20A_CPUAPP"></a>

## 291.42 `SB_CONFIG_SOC_NRF54LM20A_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LM20A 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54LM20A
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54LM20DK
SB_CONFIG_BOARD_XIAO_NRF54LM20A
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L81)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54LM20A`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LM20A)、[`SB_CONFIG_BOARD_NRF54LM20DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54LM20DK)、[`SB_CONFIG_BOARD_XIAO_NRF54LM20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_NRF54LM20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54LM20DK`、`SB_CONFIG_BOARD_XIAO_NRF54LM20A`。

<a id="SB_CONFIG_SOC_NRF54LM20A_CPUFLPR"></a>

## 291.43 `SB_CONFIG_SOC_NRF54LM20A_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LM20A FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54LM20A
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54LM20DK
SB_CONFIG_BOARD_XIAO_NRF54LM20A
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L87)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54LM20A`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LM20A)、[`SB_CONFIG_BOARD_NRF54LM20DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54LM20DK)、[`SB_CONFIG_BOARD_XIAO_NRF54LM20A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_NRF54LM20A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54LM20DK`、`SB_CONFIG_BOARD_XIAO_NRF54LM20A`。

<a id="SB_CONFIG_SOC_NRF54LM20B"></a>

## 291.44 `SB_CONFIG_SOC_NRF54LM20B`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LM20B 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF54L
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF54LM20B_CPUAPP
SB_CONFIG_SOC_NRF54LM20B_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L93)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF54L)、[`SB_CONFIG_SOC_NRF54LM20B_CPUAPP`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LM20B_CPUAPP)、[`SB_CONFIG_SOC_NRF54LM20B_CPUFLPR`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LM20B_CPUFLPR)。

<a id="SB_CONFIG_SOC_NRF54LM20B_CPUAPP"></a>

## 291.45 `SB_CONFIG_SOC_NRF54LM20B_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LM20B 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54LM20B
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54LM20DK
SB_CONFIG_BOARD_XIAO_NRF54LM20B
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L99)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54LM20B`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LM20B)、[`SB_CONFIG_BOARD_NRF54LM20DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54LM20DK)、[`SB_CONFIG_BOARD_XIAO_NRF54LM20B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_NRF54LM20B)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54LM20DK`、`SB_CONFIG_BOARD_XIAO_NRF54LM20B`。

<a id="SB_CONFIG_SOC_NRF54LM20B_CPUFLPR"></a>

## 291.46 `SB_CONFIG_SOC_NRF54LM20B_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LM20B FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54LM20B
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54LM20DK
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L105)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54LM20B`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LM20B)、[`SB_CONFIG_BOARD_NRF54LM20DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54LM20DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54LM20DK`。

<a id="SB_CONFIG_SOC_NRF54LV10A"></a>

## 291.47 `SB_CONFIG_SOC_NRF54LV10A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LV10A 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF54L
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF54LV10A_CPUAPP
SB_CONFIG_SOC_NRF54LV10A_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L111)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF54L)、[`SB_CONFIG_SOC_NRF54LV10A_CPUAPP`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LV10A_CPUAPP)、[`SB_CONFIG_SOC_NRF54LV10A_CPUFLPR`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LV10A_CPUFLPR)。

<a id="SB_CONFIG_SOC_NRF54LV10A_CPUAPP"></a>

## 291.48 `SB_CONFIG_SOC_NRF54LV10A_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LV10A 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54LV10A
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54LV10DK
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L117)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54LV10A`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LV10A)、[`SB_CONFIG_BOARD_NRF54LV10DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54LV10DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54LV10DK`。

<a id="SB_CONFIG_SOC_NRF54LV10A_CPUFLPR"></a>

## 291.49 `SB_CONFIG_SOC_NRF54LV10A_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF54LV10A FLPR 内核（CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF54LV10A
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF54LV10DK
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L123)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF54LV10A`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LV10A)、[`SB_CONFIG_BOARD_NRF54LV10DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54LV10DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF54LV10DK`。

<a id="SB_CONFIG_SOC_NRF7120"></a>

## 291.50 `SB_CONFIG_SOC_NRF7120`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF71
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF7120_ENGA
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF71)、[`SB_CONFIG_SOC_NRF7120_ENGA`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120_ENGA)。

<a id="SB_CONFIG_SOC_NRF7120E"></a>

## 291.51 `SB_CONFIG_SOC_NRF7120E`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120E 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF71
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF7120E_ENGA
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L39)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF71`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF71)、[`SB_CONFIG_SOC_NRF7120E_ENGA`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120E_ENGA)。

<a id="SB_CONFIG_SOC_NRF7120E_ENGA"></a>

## 291.52 `SB_CONFIG_SOC_NRF7120E_ENGA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120E 工程 A 版（ENGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF7120E
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF7120E_ENGA_CPUAPP
SB_CONFIG_SOC_NRF7120E_ENGA_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L45)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF7120E`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120E)、[`SB_CONFIG_SOC_NRF7120E_ENGA_CPUAPP`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120E_ENGA_CPUAPP)、[`SB_CONFIG_SOC_NRF7120E_ENGA_CPUFLPR`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120E_ENGA_CPUFLPR)。

<a id="SB_CONFIG_SOC_NRF7120E_ENGA_CPUAPP"></a>

## 291.53 `SB_CONFIG_SOC_NRF7120E_ENGA_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120E 工程 A 版应用 CPU（ENGA CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF7120E_ENGA
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF7120DK
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L51)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF7120E_ENGA`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120E_ENGA)、[`SB_CONFIG_BOARD_NRF7120DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF7120DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF7120DK`。

<a id="SB_CONFIG_SOC_NRF7120E_ENGA_CPUFLPR"></a>

## 291.54 `SB_CONFIG_SOC_NRF7120E_ENGA_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120E 工程 A 版 FLPR 内核（ENGA CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF7120E_ENGA
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF7120DK
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L57)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF7120E_ENGA`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120E_ENGA)、[`SB_CONFIG_BOARD_NRF7120DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF7120DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF7120DK`。

<a id="SB_CONFIG_SOC_NRF7120_ENGA"></a>

## 291.55 `SB_CONFIG_SOC_NRF7120_ENGA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120 工程 A 版（ENGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF7120
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF7120_ENGA_CPUAPP
SB_CONFIG_SOC_NRF7120_ENGA_CPUFLPR
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF7120`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120)、[`SB_CONFIG_SOC_NRF7120_ENGA_CPUAPP`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120_ENGA_CPUAPP)、[`SB_CONFIG_SOC_NRF7120_ENGA_CPUFLPR`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120_ENGA_CPUFLPR)。

<a id="SB_CONFIG_SOC_NRF7120_ENGA_CPUAPP"></a>

## 291.56 `SB_CONFIG_SOC_NRF7120_ENGA_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120 工程 A 版应用 CPU（ENGA CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF7120_ENGA
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF7120DK
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L27)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF7120_ENGA`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120_ENGA)、[`SB_CONFIG_BOARD_NRF7120DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF7120DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF7120DK`。

<a id="SB_CONFIG_SOC_NRF7120_ENGA_CPUFLPR"></a>

## 291.57 `SB_CONFIG_SOC_NRF7120_ENGA_CPUFLPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NRF7120 工程 A 版 FLPR 内核（ENGA CPUFLPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF7120_ENGA
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF7120DK
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L33)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF7120_ENGA`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120_ENGA)、[`SB_CONFIG_BOARD_NRF7120DK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF7120DK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF7120DK`。

<a id="SB_CONFIG_SOC_NRF9280"></a>

## 291.58 `SB_CONFIG_SOC_NRF9280`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF9280 系统级封装（SiP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF9230_ENGB_CPUAPP if SB_CONFIG_SOC_NRF9280_CPUAPP
SB_CONFIG_SOC_NRF9230_ENGB_CPURAD if SB_CONFIG_SOC_NRF9280_CPURAD
SB_CONFIG_SOC_NRF9230_ENGB_CPUPPR if SB_CONFIG_SOC_NRF9280_CPUPPR
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF9280_CPUAPP
SB_CONFIG_SOC_NRF9280_CPURAD
SB_CONFIG_SOC_NRF9280_CPUPPR
```

**定义位置（Location）**：[`soc/nordic/nrf92/Kconfig.soc:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf92/Kconfig.soc#L53)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`SB_CONFIG_SOC_NRF9280_CPUAPP`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF9280_CPUAPP)、[`SB_CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`SB_CONFIG_SOC_NRF9280_CPURAD`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF9280_CPURAD)、[`SB_CONFIG_SOC_NRF9230_ENGB_CPUPPR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF9230_ENGB_CPUPPR)、[`SB_CONFIG_SOC_NRF9280_CPUPPR`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF9280_CPUPPR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`SB_CONFIG_SOC_NRF9230_ENGB_CPURAD`、`SB_CONFIG_SOC_NRF9230_ENGB_CPUPPR`。

<a id="SB_CONFIG_SOC_NRF9280_CPUAPP"></a>

## 291.59 `SB_CONFIG_SOC_NRF9280_CPUAPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF9280 应用 CPU（CPUAPP）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF9280
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF9280PDK
```

**定义位置（Location）**：[`soc/nordic/nrf92/Kconfig.soc:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf92/Kconfig.soc#L62)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF9280`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF9280)、[`SB_CONFIG_BOARD_NRF9280PDK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF9280PDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF9280PDK`。

<a id="SB_CONFIG_SOC_NRF9280_CPUPPR"></a>

## 291.60 `SB_CONFIG_SOC_NRF9280_CPUPPR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF9280 PPR 内核（CPUPPR）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF9280
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF9280PDK
```

**定义位置（Location）**：[`soc/nordic/nrf92/Kconfig.soc:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf92/Kconfig.soc#L74)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF9280`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF9280)、[`SB_CONFIG_BOARD_NRF9280PDK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF9280PDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF9280PDK`。

<a id="SB_CONFIG_SOC_NRF9280_CPURAD"></a>

## 291.61 `SB_CONFIG_SOC_NRF9280_CPURAD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nRF9280 无线电 CPU（CPURAD）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_NRF9280
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NRF9280PDK
```

**定义位置（Location）**：[`soc/nordic/nrf92/Kconfig.soc:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf92/Kconfig.soc#L68)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_NRF9280`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF9280)、[`SB_CONFIG_BOARD_NRF9280PDK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF9280PDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NRF9280PDK`。

<a id="SB_CONFIG_SOC_SERIES_NRF51"></a>

## 291.62 `SB_CONFIG_SOC_SERIES_NRF51`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NRF51 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_NRF51X
SB_CONFIG_SOC_NRF51822_QFAA
SB_CONFIG_SOC_NRF51822_QFAB
SB_CONFIG_SOC_NRF51822_QFAC
```

**定义位置（Location）**：[`soc/nordic/nrf51/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf51/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NORDIC_NRF)、[`SB_CONFIG_SOC_SERIES_NRF51X`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF51X)、[`SB_CONFIG_SOC_NRF51822_QFAA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF51822_QFAA)、[`SB_CONFIG_SOC_NRF51822_QFAB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF51822_QFAB)、[`SB_CONFIG_SOC_NRF51822_QFAC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF51822_QFAC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`、`SB_CONFIG_SOC_NRF51822_QFAA`、`SB_CONFIG_SOC_NRF51822_QFAB`、`SB_CONFIG_SOC_NRF51822_QFAC`。

<a id="SB_CONFIG_SOC_SERIES_NRF51X"></a>

## 291.63 `SB_CONFIG_SOC_SERIES_NRF51X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF51`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF51
```

**定义位置（Location）**：[`soc/nordic/nrf51/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf51/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF51`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF51)。

<a id="SB_CONFIG_SOC_SERIES_NRF52"></a>

## 291.64 `SB_CONFIG_SOC_SERIES_NRF52`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NRF52 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_NRF52X
SB_CONFIG_SOC_NRF52805
SB_CONFIG_SOC_NRF52810
SB_CONFIG_SOC_NRF52811
SB_CONFIG_SOC_NRF52820
SB_CONFIG_SOC_NRF52832
SB_CONFIG_SOC_NRF52833
SB_CONFIG_SOC_NRF52840
```

**定义位置（Location）**：[`soc/nordic/nrf52/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf52/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NORDIC_NRF)、[`SB_CONFIG_SOC_SERIES_NRF52X`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF52X)、[`SB_CONFIG_SOC_NRF52805`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF52805)、[`SB_CONFIG_SOC_NRF52810`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF52810)、[`SB_CONFIG_SOC_NRF52811`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF52811)、[`SB_CONFIG_SOC_NRF52820`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF52820)、[`SB_CONFIG_SOC_NRF52832`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF52832)、[`SB_CONFIG_SOC_NRF52833`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF52833)、[`SB_CONFIG_SOC_NRF52840`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF52840)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`、`SB_CONFIG_SOC_NRF52805`、`SB_CONFIG_SOC_NRF52810`、`SB_CONFIG_SOC_NRF52811`、`SB_CONFIG_SOC_NRF52820`、`SB_CONFIG_SOC_NRF52832`、`SB_CONFIG_SOC_NRF52833`、`SB_CONFIG_SOC_NRF52840`。

<a id="SB_CONFIG_SOC_SERIES_NRF52X"></a>

## 291.65 `SB_CONFIG_SOC_SERIES_NRF52X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF52`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF52
```

**定义位置（Location）**：[`soc/nordic/nrf52/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf52/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF52`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF52)。

<a id="SB_CONFIG_SOC_SERIES_NRF53"></a>

## 291.66 `SB_CONFIG_SOC_SERIES_NRF53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NRF53 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_NRF53X
SB_CONFIG_SOC_NRF5340_CPUAPP
SB_CONFIG_SOC_NRF5340_CPUNET
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NORDIC_NRF)、[`SB_CONFIG_SOC_SERIES_NRF53X`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF53X)、[`SB_CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF5340_CPUAPP)、[`SB_CONFIG_SOC_NRF5340_CPUNET`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF5340_CPUNET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`、`SB_CONFIG_SOC_NRF5340_CPUAPP`、`SB_CONFIG_SOC_NRF5340_CPUNET`。

<a id="SB_CONFIG_SOC_SERIES_NRF53X"></a>

## 291.67 `SB_CONFIG_SOC_SERIES_NRF53X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF53`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF53
```

**定义位置（Location）**：[`soc/nordic/nrf53/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf53/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF53)。

<a id="SB_CONFIG_SOC_SERIES_NRF54H"></a>

## 291.68 `SB_CONFIG_SOC_SERIES_NRF54H`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Nordic Semiconductor nRF54H 系列微控制器（series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_NRF54HX
SB_CONFIG_SOC_NRF54H20
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NORDIC_NRF)、[`SB_CONFIG_SOC_SERIES_NRF54HX`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF54HX)、[`SB_CONFIG_SOC_NRF54H20`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54H20)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="SB_CONFIG_SOC_SERIES_NRF54HX"></a>

## 291.69 `SB_CONFIG_SOC_SERIES_NRF54HX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF54H`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF54H
```

**定义位置（Location）**：[`soc/nordic/nrf54h/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54h/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF54H`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF54H)。

<a id="SB_CONFIG_SOC_SERIES_NRF54L"></a>

## 291.70 `SB_CONFIG_SOC_SERIES_NRF54L`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Nordic Semiconductor nRF54L 系列微控制器（series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_NRF54LX
SB_CONFIG_SOC_NRF54L05
SB_CONFIG_SOC_NRF54L10
SB_CONFIG_SOC_NRF54L15
SB_CONFIG_SOC_NRF54LM20A
SB_CONFIG_SOC_NRF54LM20B
SB_CONFIG_SOC_NRF54LV10A
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NORDIC_NRF)、[`SB_CONFIG_SOC_SERIES_NRF54LX`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF54LX)、[`SB_CONFIG_SOC_NRF54L05`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L05)、[`SB_CONFIG_SOC_NRF54L10`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L10)、[`SB_CONFIG_SOC_NRF54L15`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54L15)、[`SB_CONFIG_SOC_NRF54LM20A`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LM20A)、[`SB_CONFIG_SOC_NRF54LM20B`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LM20B)、[`SB_CONFIG_SOC_NRF54LV10A`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF54LV10A)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="SB_CONFIG_SOC_SERIES_NRF54LX"></a>

## 291.71 `SB_CONFIG_SOC_SERIES_NRF54LX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF54L`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF54L
```

**定义位置（Location）**：[`soc/nordic/nrf54l/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf54l/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF54L`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF54L)。

<a id="SB_CONFIG_SOC_SERIES_NRF71"></a>

## 291.72 `SB_CONFIG_SOC_SERIES_NRF71`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Nordic Semiconductor nRF71 系列微控制器（series MCU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_NRF7120
SB_CONFIG_SOC_NRF7120E
```

**定义位置（Location）**：[`soc/nordic/nrf71/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf71/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NORDIC_NRF)、[`SB_CONFIG_SOC_NRF7120`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120)、[`SB_CONFIG_SOC_NRF7120E`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_NRF7120E)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="SB_CONFIG_SOC_SERIES_NRF91"></a>

## 291.73 `SB_CONFIG_SOC_SERIES_NRF91`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NRF91 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_NRF91X
SB_CONFIG_SOC_NRF9120
SB_CONFIG_SOC_NRF9160
```

**定义位置（Location）**：[`soc/nordic/nrf91/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf91/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NORDIC_NRF)、[`SB_CONFIG_SOC_SERIES_NRF91X`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF91X)、[`SB_CONFIG_SOC_NRF9120`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF9120)、[`SB_CONFIG_SOC_NRF9160`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF9160)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`、`SB_CONFIG_SOC_NRF9120`、`SB_CONFIG_SOC_NRF9160`。

<a id="SB_CONFIG_SOC_SERIES_NRF91X"></a>

## 291.74 `SB_CONFIG_SOC_SERIES_NRF91X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF91`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF91
```

**定义位置（Location）**：[`soc/nordic/nrf91/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf91/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF91`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF91)。

<a id="SB_CONFIG_SOC_SERIES_NRF92"></a>

## 291.75 `SB_CONFIG_SOC_SERIES_NRF92`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NRF92 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_NORDIC_NRF
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_SERIES_NRF92X
SB_CONFIG_SOC_NRF9230_ENGB
```

**定义位置（Location）**：[`soc/nordic/nrf92/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf92/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_NORDIC_NRF)、[`SB_CONFIG_SOC_SERIES_NRF92X`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF92X)、[`SB_CONFIG_SOC_NRF9230_ENGB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_NRF9230_ENGB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_NORDIC_NRF`、`SB_CONFIG_SOC_NRF9230_ENGB`。

<a id="SB_CONFIG_SOC_SERIES_NRF92X"></a>

## 291.76 `SB_CONFIG_SOC_SERIES_NRF92X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已弃用的 Kconfig（Deprecated Kconfig），请改用 `SOC_SERIES_NRF92`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NRF92
```

**定义位置（Location）**：[`soc/nordic/nrf92/Kconfig.soc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nordic/nrf92/Kconfig.soc#L27)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NRF92`](P291_soc_nordic_配置项参考_3.md#SB_CONFIG_SOC_SERIES_NRF92)。

<!-- kconfig-navigation -->

[上一章](P290_soc_nordic_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P292_soc_nuvoton_配置项参考.md)
