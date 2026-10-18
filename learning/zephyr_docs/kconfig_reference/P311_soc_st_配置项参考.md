---
id: learning.zephyr-docs.kconfig-reference.page-311
title: "`soc/st`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第311章\_`soc/st`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/st` 的 41 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HAS_STM32_FLASH_PREFETCH"></a>

## 311.1 `CONFIG_HAS_STM32_FLASH_PREFETCH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由支持 Flash 预取（flash prefetch）的 SoC 选择的隐藏符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_STM32C0X
CONFIG_SOC_SERIES_STM32F0X
CONFIG_SOC_SERIES_STM32F1X
CONFIG_SOC_SERIES_STM32F2X
CONFIG_SOC_SERIES_STM32F3X
CONFIG_SOC_SERIES_STM32F4X
CONFIG_SOC_SERIES_STM32F7X
CONFIG_SOC_SERIES_STM32G0X
CONFIG_SOC_SERIES_STM32G4X
CONFIG_SOC_SERIES_STM32L0X
CONFIG_SOC_SERIES_STM32L1X
CONFIG_SOC_SERIES_STM32L4X
CONFIG_SOC_SERIES_STM32U0X
CONFIG_SOC_SERIES_STM32U3X
CONFIG_SOC_SERIES_STM32WBAX
CONFIG_SOC_SERIES_STM32WBX
CONFIG_SOC_SERIES_STM32WLX
```

**定义位置（Location）**：[`soc/st/stm32/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_SOC_SERIES_STM32C0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C0X)、[`CONFIG_SOC_SERIES_STM32F0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F0X)、[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F2X)、[`CONFIG_SOC_SERIES_STM32F3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F3X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32G0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G0X)、[`CONFIG_SOC_SERIES_STM32G4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G4X)、[`CONFIG_SOC_SERIES_STM32L0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L0X)、[`CONFIG_SOC_SERIES_STM32L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L1X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_SERIES_STM32U0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U0X)、[`CONFIG_SOC_SERIES_STM32U3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U3X)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_SERIES_STM32WBX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBX)、[`CONFIG_SOC_SERIES_STM32WLX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WLX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`、`CONFIG_SOC_SERIES_STM32C0X`、`CONFIG_SOC_SERIES_STM32F0X`、`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F2X`、`CONFIG_SOC_SERIES_STM32F3X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32G0X`、`CONFIG_SOC_SERIES_STM32G4X`、`CONFIG_SOC_SERIES_STM32L0X`、`CONFIG_SOC_SERIES_STM32L1X`、`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32U0X`、`CONFIG_SOC_SERIES_STM32U3X`、`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_SERIES_STM32WBX`、`CONFIG_SOC_SERIES_STM32WLX`。

<a id="CONFIG_HAS_STM32_UNCACHED_ACCESS_ONLY_OTP"></a>

## 311.2 `CONFIG_HAS_STM32_UNCACHED_ACCESS_ONLY_OTP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由具有以下要求的 SoC 选择的隐藏选项：非易失存储器（NVM）的单次可编程／只读区域（OTP/read-only areas）必须通过不带缓存的操作访问，否则会发生总线故障（bus fault）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_STM32C5X
CONFIG_SOC_SERIES_STM32H5X
```

**定义位置（Location）**：[`soc/st/stm32/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`、`CONFIG_SOC_SERIES_STM32C5X`、`CONFIG_SOC_SERIES_STM32H5X`。

<a id="CONFIG_SOC_FAMILY_STM32_HEX_FILE_SEC_RANGE"></a>

## 311.3 `CONFIG_SOC_FAMILY_STM32_HEX_FILE_SEC_RANGE`

**提示（Prompt）**：开发板 HEX 文件通过 Flash 安全地址范围加载非安全镜像（non-secure image）

**说明（Help）**

如果目标开发板在烧录 Flash 之前，已通过选项字节（Option Bytes）将内部 Flash 配置为安全区域，例如使用 `<build>/tfm/api_ns/regression.sh`，请启用此选项。在这种情况下，生成的 HEX 文件应将非安全镜像定位到 Flash 安全内存地址范围中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRUSTED_EXECUTION_NONSECURE && CONFIG_SOC_FAMILY_STM32
```

**定义位置（Location）**：[`soc/st/stm32/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_SOC_LINE_STM32L4PLUS"></a>

## 311.4 `CONFIG_SOC_LINE_STM32L4PLUS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

STM32L4+ 片上系统系列／产品线器件（SoC series/product line device）。与 STM32L4 系列其他 SoC 相比，这些产品具有特定配置约束。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_STM32L4P5XX
CONFIG_SOC_STM32L4Q5XX
CONFIG_SOC_STM32L4R5XX
CONFIG_SOC_STM32L4R9XX
CONFIG_SOC_STM32L4S5XX
```

**定义位置（Location）**：[`soc/st/stm32/stm32l4x/Kconfig.soc:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32l4x/Kconfig.soc#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_STM32L4P5XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32L4P5XX)、[`CONFIG_SOC_STM32L4Q5XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32L4Q5XX)、[`CONFIG_SOC_STM32L4R5XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32L4R5XX)、[`CONFIG_SOC_STM32L4R9XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32L4R9XX)、[`CONFIG_SOC_STM32L4S5XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32L4S5XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_STM32L4P5XX`、`CONFIG_SOC_STM32L4Q5XX`、`CONFIG_SOC_STM32L4R5XX`、`CONFIG_SOC_STM32L4R9XX`、`CONFIG_SOC_STM32L4S5XX`。

<a id="CONFIG_SOC_STM32F10X_CONNECTIVITY_LINE_DEVICE"></a>

## 311.5 `CONFIG_SOC_STM32F10X_CONNECTIVITY_LINE_DEVICE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

互联型产品线（Connectivity line）器件为 STM32F105xx 和 STM32F107xx 微控制器。它们面向需要连接能力和实时性能的应用，例如工业控制、安全应用控制面板、不间断电源（UPS）或家庭音频。STM32F107xx 还提供以太网介质访问控制器（Ethernet MAC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_STM32F105XB
CONFIG_SOC_STM32F105XC
CONFIG_SOC_STM32F107XC
```

**定义位置（Location）**：[`soc/st/stm32/stm32f1x/Kconfig.soc:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32f1x/Kconfig.soc#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_STM32F105XB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32F105XB)、[`CONFIG_SOC_STM32F105XC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32F105XC)、[`CONFIG_SOC_STM32F107XC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32F107XC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_STM32F105XB`、`CONFIG_SOC_STM32F105XC`、`CONFIG_SOC_STM32F107XC`。

<a id="CONFIG_SOC_STM32F10X_DENSITY_DEVICE"></a>

## 311.6 `CONFIG_SOC_STM32F10X_DENSITY_DEVICE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

STM32F101xx、STM32F102xx、STM32F103xx：

- 小容量超值型产品线器件（Low density Value line devices）。
- 中容量超值型产品线器件（Medium density Value line devices）。
- 大容量超值型产品线器件（High density Value line devices）。
- 超大容量超值型产品线器件（XL-density Value line devices）。

译注：型号与 Value line 分类均按官方原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_STM32F103XE
CONFIG_SOC_STM32F103XB
CONFIG_SOC_STM32F103X8
```

**定义位置（Location）**：[`soc/st/stm32/stm32f1x/Kconfig.soc:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32f1x/Kconfig.soc#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_STM32F103XE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32F103XE)、[`CONFIG_SOC_STM32F103XB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32F103XB)、[`CONFIG_SOC_STM32F103X8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32F103X8)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_STM32F103XE`、`CONFIG_SOC_STM32F103XB`、`CONFIG_SOC_STM32F103X8`。

<a id="CONFIG_STM32H7_BOOT_M4_AT_INIT"></a>

## 311.7 `CONFIG_STM32H7_BOOT_M4_AT_INIT`

**提示（Prompt）**：在 M7 初始化期间启动 M4 内核，不受 BCM4 选项字节（option byte）影响。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32H7_DUAL_CORE && CONFIG_SOC_SERIES_STM32H7X && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/st/stm32/stm32h7x/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32h7x/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 双核（Dual Core）

**配置项引用（Symbol References）**：[`CONFIG_STM32H7_DUAL_CORE`](P311_soc_st_配置项参考.md#CONFIG_STM32H7_DUAL_CORE)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32H7_DUAL_CORE"></a>

## 311.8 `CONFIG_STM32H7_DUAL_CORE`

**提示（Prompt）**：双核（Dual Core）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_STM32H7X && CONFIG_SOC_FAMILY_STM32
```

**定义位置（Location）**：[`soc/st/stm32/stm32h7x/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32h7x/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32N6_BOOT_SERIAL"></a>

## 311.9 `CONFIG_STM32N6_BOOT_SERIAL`

**提示（Prompt）**：串行启动目标，USB（Serial boot target）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_STM32N6X && CONFIG_SOC_FAMILY_STM32
```

**定义位置（Location）**：[`soc/st/stm32/stm32n6x/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32n6x/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32N6_BRANCH_CACHE"></a>

## 311.10 `CONFIG_STM32N6_BRANCH_CACHE`

**提示（Prompt）**：Cortex-M55 分支缓存（branch cache）

**说明（Help）**

在 SoC 初始化期间启用 Cortex-M55 的分支缓存（branch cache）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_STM32N6X && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/st/stm32/stm32n6x/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32n6x/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32N6_NPU"></a>

## 311.11 `CONFIG_STM32N6_NPU`

**提示（Prompt）**：Neural-ART 神经处理加速器（NPU）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_NPU_ENABLED && CONFIG_SOC_SERIES_STM32N6X && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RESET
```

**定义位置（Location）**：[`soc/st/stm32/stm32n6x/npu/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32n6x/npu/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32N6_NPU_CACHE_INIT_PRIORITY"></a>

## 311.12 `CONFIG_STM32N6_NPU_CACHE_INIT_PRIORITY`

**提示（Prompt）**：STM32N6 NPU 缓存初始化优先级，亦称 CACHEAXI（init priority）

**说明（Help）**

STM32N6 神经处理单元（NPU）缓存（亦称 CACHEAXI）的初始化优先级。注意：此优先级必须低于 `STM32N6_NPU_INIT_PRIORITY`，即数值更大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32N6_NPU && CONFIG_SOC_SERIES_STM32N6X && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
CONFIG_APPLICATION_INIT_PRIORITY
```

**定义位置（Location）**：[`soc/st/stm32/stm32n6x/npu/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32n6x/npu/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Neural-ART 神经处理加速器（NPU）

**配置项引用（Symbol References）**：[`CONFIG_STM32N6_NPU`](P311_soc_st_配置项参考.md#CONFIG_STM32N6_NPU)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_APPLICATION_INIT_PRIORITY`](P001_kernel_配置项参考_1.md#CONFIG_APPLICATION_INIT_PRIORITY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32N6_NPU_INIT_PRIORITY"></a>

## 311.13 `CONFIG_STM32N6_NPU_INIT_PRIORITY`

**提示（Prompt）**：STM32N6 神经处理单元初始化优先级（NPU init priority）

**说明（Help）**

STM32N6 神经处理单元（NPU）的初始化优先级。注意：此优先级必须高于 `STM32N6_NPU_CACHE_INIT_PRIORITY`，即数值更小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32N6_NPU && CONFIG_SOC_SERIES_STM32N6X && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`soc/st/stm32/stm32n6x/npu/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32n6x/npu/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Neural-ART 神经处理加速器（NPU）

**配置项引用（Symbol References）**：[`CONFIG_STM32N6_NPU`](P311_soc_st_配置项参考.md#CONFIG_STM32N6_NPU)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32N6_RIF_OPEN"></a>

## 311.14 `CONFIG_STM32N6_RIF_OPEN`

**提示（Prompt）**：将资源隔离框架配置为全部开放访问（RIF all OPEN access）

**说明（Help）**

启用后，在 SoC 初始化期间配置所有主设备（masters）的 RIMC 和所有从设备（slaves）的 RISC。以安全权限（Secure privileges）运行的 Zephyr 可完全访问所有 SoC 资源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRUSTED_EXECUTION_SECURE && CONFIG_SOC_SERIES_STM32N6X && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/st/stm32/stm32n6x/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32n6x/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRUSTED_EXECUTION_SECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_SECURE)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32WBA_BLE_CTLR_THREAD_PRIO"></a>

## 311.15 `CONFIG_STM32WBA_BLE_CTLR_THREAD_PRIO`

**提示（Prompt）**：低功耗蓝牙控制器线程优先级（BLE Controller thread priority）

**说明（Help）**

此选项设置低功耗蓝牙控制器线程（BLE Controller thread）的协作式优先级（cooperative priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_STM32WBA && CONFIG_SOC_SERIES_STM32WBAX && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
14
```

**定义位置（Location）**：[`soc/st/stm32/stm32wbax/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32wbax/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32WBA`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32WBA_BLE_CTLR_THREAD_STACK_SIZE"></a>

## 311.16 `CONFIG_STM32WBA_BLE_CTLR_THREAD_STACK_SIZE`

**提示（Prompt）**：低功耗蓝牙控制器线程栈大小（BLE Controller thread stack size）

**说明（Help）**

低功耗蓝牙控制器线程（BLE Controller thread）的栈大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_STM32WBA && CONFIG_SOC_SERIES_STM32WBAX && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`soc/st/stm32/stm32wbax/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32wbax/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32WBA`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32WBA_LL_THREAD_PRIO"></a>

## 311.17 `CONFIG_STM32WBA_LL_THREAD_PRIO`

**提示（Prompt）**：链路层线程优先级（Link Layer thread priority）

**说明（Help）**

此选项设置链路层线程（Link Layer thread，LL）的协作式优先级（cooperative priority）。LL 线程优先级应高于 BLE 控制器线程（CTLR）以及与 BLE 和 IEEE 802.15.4 协议相关的 Zephyr 上层协议栈线程，例如蓝牙接收线程（BT Rx，`BT_RX_PRIO`）、蓝牙长工作队列（BT long workqueue，`BT_LONG_WQ_PRIO`）、网络管理线程（net mgmt）、连接管理监视线程（connection manager monitor）、UDP 线程等。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_STM32WBA || CONFIG_IEEE802154_STM32WBA) && CONFIG_SOC_SERIES_STM32WBAX && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`soc/st/stm32/stm32wbax/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32wbax/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32WBA`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA)、[`CONFIG_IEEE802154_STM32WBA`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_STM32WBA)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32WBA_LL_THREAD_STACK_SIZE"></a>

## 311.18 `CONFIG_STM32WBA_LL_THREAD_STACK_SIZE`

**提示（Prompt）**：链路层线程栈大小（Link Layer thread stack size）

**说明（Help）**

链路层线程（Link Layer thread）的栈大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_STM32WBA || CONFIG_IEEE802154_STM32WBA) && CONFIG_SOC_SERIES_STM32WBAX && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
1536
```

**定义位置（Location）**：[`soc/st/stm32/stm32wbax/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32wbax/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32WBA`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA)、[`CONFIG_IEEE802154_STM32WBA`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_STM32WBA)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WBAX`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_APP_IN_EXT_FLASH"></a>

## 311.19 `CONFIG_STM32_APP_IN_EXT_FLASH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当应用位于外部 Flash 并由 MCUboot 链式加载（chainloaded）时，使 SoC 时钟驱动能够正确初始化 QSPI／OSPI／XSPI 控制器时钟。应用是否原地执行（eXecuted in Place，XiP），取决于使用的 MCUboot 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32
```

**定义位置（Location）**：[`soc/st/stm32/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_BACKUP_PROTECTION"></a>

## 311.20 `CONFIG_STM32_BACKUP_PROTECTION`

**提示（Prompt）**：SoC 具有后备域访问保护（backup domain protection access）

**说明（Help）**

对于需要显式处理后备域资源访问保护（access protection to backup domain resources）的 SoC，启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_BACKUP_SRAM"></a>

## 311.21 `CONFIG_STM32_BACKUP_SRAM`

**提示（Prompt）**：STM32 后备 SRAM（Backup SRAM）

**说明（Help）**

启用 STM32 后备 SRAM（backup SRAM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_BACKUP_SRAM_ENABLED && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_BACKUP_SRAM_INIT_PRIORITY"></a>

## 311.22 `CONFIG_STM32_BACKUP_SRAM_INIT_PRIORITY`

**提示（Prompt）**：STM32 后备 SRAM 初始化优先级（init priority）

**说明（Help）**

STM32 后备 SRAM 设备的初始化优先级（initialization priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_BACKUP_SRAM && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
CONFIG_APPLICATION_INIT_PRIORITY
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 后备 SRAM（Backup SRAM）

**配置项引用（Symbol References）**：[`CONFIG_STM32_BACKUP_SRAM`](P311_soc_st_配置项参考.md#CONFIG_STM32_BACKUP_SRAM)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_APPLICATION_INIT_PRIORITY`](P001_kernel_配置项参考_1.md#CONFIG_APPLICATION_INIT_PRIORITY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_ENABLE_DEBUG_SLEEP_STOP"></a>

## 311.23 `CONFIG_STM32_ENABLE_DEBUG_SLEEP_STOP`

**提示（Prompt）**：允许在停止／睡眠模式中连接调试器（debugger attach in stop/sleep Mode）

**说明（Help）**

某些 STM32 器件出于功耗原因，会在睡眠／停止模式中禁用调试 MCU 模块（DBGMCU）。其副作用是，调试器无法在不复位目标设备的情况下连接，实际上破坏了 `west attach` 的使用场景。SEGGER RTT 等技术也需要保持此连接能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y if CONFIG_DEBUG
```

**被选择（Selected by）**

```text
CONFIG_USE_SEGGER_RTT
CONFIG_USE_SEGGER_RTT
CONFIG_SOC_FAMILY_STM32
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_DEBUG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG)、[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_FLASH_PREFETCH"></a>

## 311.24 `CONFIG_STM32_FLASH_PREFETCH`

**提示（Prompt）**：Flash 预取缓冲区（prefetch buffer）

**说明（Help）**

启用 Flash 预取（prefetch）。通过缓存访问 Flash 时，出于能效考虑建议启用。Flash 预取也会略微提升性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_STM32_FLASH_PREFETCH && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/st/stm32/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_STM32_FLASH_PREFETCH`](P311_soc_st_配置项参考.md#CONFIG_HAS_STM32_FLASH_PREFETCH)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_GPIOPORT_MGR"></a>

## 311.25 `CONFIG_STM32_GPIOPORT_MGR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32 GPIO 端口管理器模块（port manager module）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32
```

**被选择（Selected by）**

```text
CONFIG_GPIO_STM32
CONFIG_PINCTRL_STM32
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_GPIO_STM32`](P099_drivers_gpio_配置项参考_2.md#CONFIG_GPIO_STM32)、[`CONFIG_PINCTRL_STM32`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_HAL2"></a>

## 311.26 `CONFIG_STM32_HAL2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

STM32 硬件抽象层和底层驱动模块（HAL and LL modules）采用 STM32 HAL2 格式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_STM32C5X
```

**定义位置（Location）**：[`soc/st/stm32/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_SOC_SERIES_STM32C5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C5X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`、`CONFIG_SOC_SERIES_STM32C5X`。

<a id="CONFIG_STM32_INT_FLASH_SECURE_BASE_ADDRESS"></a>

## 311.27 `CONFIG_STM32_INT_FLASH_SECURE_BASE_ADDRESS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在适用 STM32 SoC 上启用 TZEN 时，安全内部 Flash 的基地址（secure internal flash base address）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32
```

**定义位置（Location）**：[`soc/st/stm32/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_IOCELL"></a>

## 311.28 `CONFIG_STM32_IOCELL`

**提示（Prompt）**：STM32 输入／输出单元（I/O cell）

**说明（Help）**

启用 STM32 I/O 补偿单元（compensation cell）与高速低电压配置（HSLV configuration）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_IOCELL_ENABLED && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_IOCELL_CHECK_ENABLE"></a>

## 311.29 `CONFIG_STM32_IOCELL_CHECK_ENABLE`

**提示（Prompt）**：STM32 输入／输出单元检查（I/O cell check）

**说明（Help）**

启用 I/O 单元驱动的日志（logging），可用于报告设备树配置与器件单次可编程存储器／选项字节（OTP/option bytes）中保存值之间的差异。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_IOCELL && CONFIG_LOG && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 输入／输出单元（I/O cell）

**配置项引用（Symbol References）**：[`CONFIG_STM32_IOCELL`](P311_soc_st_配置项参考.md#CONFIG_STM32_IOCELL)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_IOCELL_PRIORITY"></a>

## 311.30 `CONFIG_STM32_IOCELL_PRIORITY`

**提示（Prompt）**：STM32 I/O 单元初始化优先级（initialization priority）

**说明（Help）**

该例程在早期初始化级别（EARLY level）中的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_IOCELL && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 输入／输出单元（I/O cell）

**配置项引用（Symbol References）**：[`CONFIG_STM32_IOCELL`](P311_soc_st_配置项参考.md#CONFIG_STM32_IOCELL)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_NEOCHROM_GPU2D"></a>

## 311.31 `CONFIG_STM32_NEOCHROM_GPU2D`

**提示（Prompt）**：STM32 NeoChrom 二维图形处理器支持（GPU2D support）

**说明（Help）**

启用 STM32 NeoChrom GPU2D 加速器支持。此驱动提供对 GPU2D 硬件的底层访问（low-level access），供 NemaGFX 用于硬件加速渲染（hardware-accelerated rendering）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_NEOCHROM_GPU2D_ENABLED && CONFIG_SOC_FAMILY_STM32
```

**主动选择（Selects）**

```text
CONFIG_RESET
CONFIG_USE_STM32_HAL_GPU2D
```

**被选择（Selected by）**

```text
CONFIG_LV_Z_USE_NEMA_GFX
CONFIG_LV_Z_USE_NEMA_GFX
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)、[`CONFIG_USE_STM32_HAL_GPU2D`](P212_modules_Kconfig.stm32_配置项参考_1.md#CONFIG_USE_STM32_HAL_GPU2D)、[`CONFIG_LV_Z_USE_NEMA_GFX`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_USE_NEMA_GFX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_NEOCHROM_GPU2D_INIT_PRIORITY"></a>

## 311.32 `CONFIG_STM32_NEOCHROM_GPU2D_INIT_PRIORITY`

**提示（Prompt）**：NeoChrom GPU2D 设备初始化优先级（device init priority）

**说明（Help）**

NeoChrom GPU2D 设备的初始化优先级（initialization priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_NEOCHROM_GPU2D && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 NeoChrom 二维图形处理器支持（GPU2D support）

**配置项引用（Symbol References）**：[`CONFIG_STM32_NEOCHROM_GPU2D`](P311_soc_st_配置项参考.md#CONFIG_STM32_NEOCHROM_GPU2D)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_STOP3_LP_MODE"></a>

## 311.33 `CONFIG_STM32_STOP3_LP_MODE`

原库同名定义共 2 条；本项为数据库第 18627 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32 STOP3 低功耗模式（low-power mode）支持。它基于 Cortex-M33 深度睡眠模式（Deepsleep mode），结合外设时钟门控（clock gating）。内核域中的所有时钟停止，PLL、MSIS、MSIK、HSI16 和 HSE 振荡器均禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
n && n
```

**定义位置（Location）**：[`soc/st/stm32/stm32u3x/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32u3x/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_STOP3_LP_MODE--record-18628"></a>

## 311.34 `CONFIG_STM32_STOP3_LP_MODE`

原库同名定义共 2 条；本项为数据库第 18628 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 STM32 STOP3 低功耗模式（low-power mode）支持。它基于 Cortex-M33 深度睡眠模式（Deepsleep mode），结合外设时钟门控（clock gating）。内核域中的所有时钟停止，PLL、MSIS、MSIK、HSI16 和 HSE 振荡器均禁用。保留所有 SRAM 和寄存器内容；可将 SRAM 全部或部分断电，以进一步降低功耗。GPIO 处于悬空状态，可通过 PWR 寄存器添加上拉或下拉。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
n && n
```

**定义位置（Location）**：[`soc/st/stm32/stm32u5x/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32u5x/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_WKUP_PINS"></a>

## 311.35 `CONFIG_STM32_WKUP_PINS`

**提示（Prompt）**：STM32 电源唤醒引脚（PWR Wake-up Pins）

**说明（Help）**

启用 STM32 唤醒引脚控制器（wake-up pins controller）支持，该控制器位于 PWR 中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_PWR_WKUPCTRL_ENABLED && CONFIG_SOC_FAMILY_STM32
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_XSPIM"></a>

## 311.36 `CONFIG_STM32_XSPIM`

**提示（Prompt）**：STM32 XSPI 管理器（Manager）

**说明（Help）**

启用 XSPI 管理器（Manager）支持。从外部 Flash 运行的应用不应使用它，因为它会重新初始化串行总线控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_STM32_APP_IN_EXT_FLASH && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y if DT_HAS_ST_STM32_XSPIM_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_XSPI
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_STM32_APP_IN_EXT_FLASH`](P311_soc_st_配置项参考.md#CONFIG_STM32_APP_IN_EXT_FLASH)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_USE_STM32_HAL_XSPI`](P213_modules_Kconfig.stm32_配置项参考_2.md#CONFIG_USE_STM32_HAL_XSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_SWJ_ANALOG_PRIORITY"></a>

## 311.37 `CONFIG_SWJ_ANALOG_PRIORITY`

**提示（Prompt）**：将 SWJ 调试端口切换为模拟模式的例程初始化优先级（SWJ DP port to analog routine）

**说明（Help）**

该例程在 PRE_KERNEL1 级别中的初始化优先级。此优先级数值必须大于 `GPIO_INIT_PRIORITY`，小于 `UART_INIT_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
49
```

**定义位置（Location）**：[`soc/st/stm32/common/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/common/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_USE_STM32_ASSERT"></a>

## 311.38 `CONFIG_USE_STM32_ASSERT`

**提示（Prompt）**：STM32Cube HAL 和 LL 驱动断言（asserts）

**说明（Help）**

在 STM32Cube 硬件抽象层（HAL）和底层驱动（LL）中启用断言（asserts）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ASSERT && CONFIG_SOC_FAMILY_STM32
```

**定义位置（Location）**：[`soc/st/stm32/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ASSERT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="SB_CONFIG_SOC_LINE_STM32L4PLUS"></a>

## 311.39 `SB_CONFIG_SOC_LINE_STM32L4PLUS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

STM32L4+ 片上系统系列／产品线器件（SoC series/product line device）。与 STM32L4 系列其他 SoC 相比，这些产品具有特定配置约束。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_SOC_STM32L4P5XX
SB_CONFIG_SOC_STM32L4Q5XX
SB_CONFIG_SOC_STM32L4R5XX
SB_CONFIG_SOC_STM32L4R9XX
SB_CONFIG_SOC_STM32L4S5XX
```

**定义位置（Location）**：[`soc/st/stm32/stm32l4x/Kconfig.soc:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32l4x/Kconfig.soc#L97)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_STM32L4P5XX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_STM32L4P5XX)、[`SB_CONFIG_SOC_STM32L4Q5XX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_STM32L4Q5XX)、[`SB_CONFIG_SOC_STM32L4R5XX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_STM32L4R5XX)、[`SB_CONFIG_SOC_STM32L4R9XX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_STM32L4R9XX)、[`SB_CONFIG_SOC_STM32L4S5XX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_STM32L4S5XX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_STM32L4P5XX`、`SB_CONFIG_SOC_STM32L4Q5XX`、`SB_CONFIG_SOC_STM32L4R5XX`、`SB_CONFIG_SOC_STM32L4R9XX`、`SB_CONFIG_SOC_STM32L4S5XX`。

<a id="SB_CONFIG_SOC_STM32F10X_CONNECTIVITY_LINE_DEVICE"></a>

## 311.40 `SB_CONFIG_SOC_STM32F10X_CONNECTIVITY_LINE_DEVICE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

互联型产品线（Connectivity line）器件为 STM32F105xx 和 STM32F107xx 微控制器。它们面向需要连接能力和实时性能的应用，例如工业控制、安全应用控制面板、不间断电源（UPS）或家庭音频。STM32F107xx 还提供以太网介质访问控制器（Ethernet MAC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_SOC_STM32F105XB
SB_CONFIG_SOC_STM32F105XC
SB_CONFIG_SOC_STM32F107XC
```

**定义位置（Location）**：[`soc/st/stm32/stm32f1x/Kconfig.soc:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32f1x/Kconfig.soc#L61)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_STM32F105XB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_STM32F105XB)、[`SB_CONFIG_SOC_STM32F105XC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_STM32F105XC)、[`SB_CONFIG_SOC_STM32F107XC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_STM32F107XC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_STM32F105XB`、`SB_CONFIG_SOC_STM32F105XC`、`SB_CONFIG_SOC_STM32F107XC`。

<a id="SB_CONFIG_SOC_STM32F10X_DENSITY_DEVICE"></a>

## 311.41 `SB_CONFIG_SOC_STM32F10X_DENSITY_DEVICE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

STM32F101xx、STM32F102xx、STM32F103xx：

- 小容量超值型产品线器件（Low density Value line devices）。
- 中容量超值型产品线器件（Medium density Value line devices）。
- 大容量超值型产品线器件（High density Value line devices）。
- 超大容量超值型产品线器件（XL-density Value line devices）。

译注：型号与 Value line 分类均按官方原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_SOC_STM32F103XE
SB_CONFIG_SOC_STM32F103XB
SB_CONFIG_SOC_STM32F103X8
```

**定义位置（Location）**：[`soc/st/stm32/stm32f1x/Kconfig.soc:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/st/stm32/stm32f1x/Kconfig.soc#L52)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_STM32F103XE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_STM32F103XE)、[`SB_CONFIG_SOC_STM32F103XB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_STM32F103XB)、[`SB_CONFIG_SOC_STM32F103X8`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_STM32F103X8)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_STM32F103XE`、`SB_CONFIG_SOC_STM32F103XB`、`SB_CONFIG_SOC_STM32F103X8`。

<!-- kconfig-navigation -->

[上一章](P310_soc_snps_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P312_soc_starfive_配置项参考.md)
