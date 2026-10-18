---
id: learning.zephyr-docs.kconfig-reference.page-263
title: "`soc/arm`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第263章\_`soc/arm`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/arm` 的 42 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_AN383"></a>

## 263.1 `CONFIG_SOC_AN383`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MPS2 上的 ARM Cortex-M0+ SMM，应用说明 AN383（Application Note AN383）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_MPS2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MPS2
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MPS2`](P263_soc_arm_配置项参考.md#CONFIG_SOC_SERIES_MPS2)、[`CONFIG_BOARD_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MPS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_MPS2`。

<a id="CONFIG_SOC_AN385"></a>

## 263.2 `CONFIG_SOC_AN385`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MPS2 上的 ARM Cortex-M3 SMM，应用说明 AN385（Application Note AN385）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_MPS2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MPS2
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MPS2`](P263_soc_arm_配置项参考.md#CONFIG_SOC_SERIES_MPS2)、[`CONFIG_BOARD_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MPS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_MPS2`。

<a id="CONFIG_SOC_AN386"></a>

## 263.3 `CONFIG_SOC_AN386`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MPS2 上的 ARM Cortex-M4 SMM，应用说明 AN386（Application Note AN386）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_MPS2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MPS2
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MPS2`](P263_soc_arm_配置项参考.md#CONFIG_SOC_SERIES_MPS2)、[`CONFIG_BOARD_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MPS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_MPS2`。

<a id="CONFIG_SOC_AN500"></a>

## 263.4 `CONFIG_SOC_AN500`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MPS2+ 上的 ARM Cortex-M7 SMM，应用说明 AN500（Application Note AN500）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_MPS2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MPS2
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MPS2`](P263_soc_arm_配置项参考.md#CONFIG_SOC_SERIES_MPS2)、[`CONFIG_BOARD_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MPS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_MPS2`。

<a id="CONFIG_SOC_AN521_CPU0"></a>

## 263.5 `CONFIG_SOC_AN521_CPU0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MPS2+ 上的 ARM Cortex-M33 SMM-SSE-200（AN521），CPU0 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AN521
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MPS2
CONFIG_BOARD_MPS2
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AN521`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN521)、[`CONFIG_BOARD_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MPS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AN521`、`CONFIG_BOARD_MPS2`。

<a id="CONFIG_SOC_AN521_CPU1"></a>

## 263.6 `CONFIG_SOC_AN521_CPU1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MPS2+ 上的 ARM Cortex-M33 SMM-SSE-200（AN521），CPU1 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AN521
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MPS2
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AN521`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN521)、[`CONFIG_BOARD_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MPS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AN521`、`CONFIG_BOARD_MPS2`。

<a id="CONFIG_SOC_AN536_CPU0"></a>

## 263.7 `CONFIG_SOC_AN536_CPU0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

MPS3 AN536 平台的 Arm Cortex-R52 CPU0 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AN536
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MPS3
```

**定义位置（Location）**：[`soc/arm/mps3/Kconfig.soc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps3/Kconfig.soc#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AN536`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN536)、[`CONFIG_BOARD_MPS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MPS3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AN536`、`CONFIG_BOARD_MPS3`。

<a id="CONFIG_SOC_BEETLE_R0"></a>

## 263.8 `CONFIG_SOC_BEETLE_R0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM BEETLE R0 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_BEETLE
```

**被选择（Selected by）**

```text
CONFIG_BOARD_V2M_BEETLE
```

**定义位置（Location）**：[`soc/arm/beetle/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/beetle/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_BEETLE`](P263_soc_arm_配置项参考.md#CONFIG_SOC_SERIES_BEETLE)、[`CONFIG_BOARD_V2M_BEETLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_V2M_BEETLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_V2M_BEETLE`。

<a id="CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1"></a>

## 263.9 `CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM Cortex-M1 DesignStart 现场可编程门阵列（FPGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_DESIGNSTART
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ARTY_A7
```

**定义位置（Location）**：[`soc/arm/designstart/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/designstart/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_DESIGNSTART`](P263_soc_arm_配置项参考.md#CONFIG_SOC_SERIES_DESIGNSTART)、[`CONFIG_BOARD_ARTY_A7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ARTY_A7)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ARTY_A7`。

<a id="CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3"></a>

## 263.10 `CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM Cortex-M3 DesignStart 现场可编程门阵列（FPGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_DESIGNSTART
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ARTY_A7
CONFIG_BOARD_SCOBC_A1
```

**定义位置（Location）**：[`soc/arm/designstart/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/designstart/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_DESIGNSTART`](P263_soc_arm_配置项参考.md#CONFIG_SOC_SERIES_DESIGNSTART)、[`CONFIG_BOARD_ARTY_A7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ARTY_A7)、[`CONFIG_BOARD_SCOBC_A1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_SCOBC_A1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ARTY_A7`、`CONFIG_BOARD_SCOBC_A1`。

<a id="CONFIG_SOC_FVP_AEMV8R_SIMULATE_CPU_PM"></a>

## 263.11 `CONFIG_SOC_FVP_AEMV8R_SIMULATE_CPU_PM`

**提示（Prompt）**：为 FVP_BaseR_AEMv8R 模拟 CPU 电源管理（Simulate CPU Power Management）

**说明（Help）**

为 FVP_BaseR_AEMv8R 模拟 CPU 电源管理功能（cpu power management）。当 Zephyr 内核尝试通过 `pm_cpu_on()` 启动辅助内核（secondary core）时，此操作始终成功，因为它确实成功启动了辅助内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FVP_AEMV8R_AARCH64
```

**定义位置（Location）**：[`soc/arm/fvp_aemv8r/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/fvp_aemv8r/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FVP_AEMV8R_AARCH64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH64)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FVP_AEMV8R_AARCH64`。

<a id="CONFIG_SOC_MUSCA_B1"></a>

## 263.12 `CONFIG_SOC_MUSCA_B1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MUSCA-B1 上的 ARM Cortex-M33 SMM-SSE-200

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_MUSCA
```

**被选择（Selected by）**

```text
CONFIG_BOARD_V2M_MUSCA_B1
```

**定义位置（Location）**：[`soc/arm/musca/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/musca/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MUSCA`](P263_soc_arm_配置项参考.md#CONFIG_SOC_SERIES_MUSCA)、[`CONFIG_BOARD_V2M_MUSCA_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_V2M_MUSCA_B1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_V2M_MUSCA_B1`。

<a id="CONFIG_SOC_MUSCA_S1"></a>

## 263.13 `CONFIG_SOC_MUSCA_S1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MUSCA-S1 上的 ARM Cortex-M33 SMM-SSE-200

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_MUSCA
```

**被选择（Selected by）**

```text
CONFIG_BOARD_V2M_MUSCA_S1
```

**定义位置（Location）**：[`soc/arm/musca/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/musca/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MUSCA`](P263_soc_arm_配置项参考.md#CONFIG_SOC_SERIES_MUSCA)、[`CONFIG_BOARD_V2M_MUSCA_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_V2M_MUSCA_S1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_V2M_MUSCA_S1`。

<a id="CONFIG_SOC_SERIES_BEETLE"></a>

## 263.14 `CONFIG_SOC_SERIES_BEETLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Beetle 微控制器系列支持（MCU Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_BEETLE_R0
```

**定义位置（Location）**：[`soc/arm/beetle/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/beetle/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ARM)、[`CONFIG_SOC_BEETLE_R0`](P263_soc_arm_配置项参考.md#CONFIG_SOC_BEETLE_R0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ARM`。

<a id="CONFIG_SOC_SERIES_DESIGNSTART"></a>

## 263.15 `CONFIG_SOC_SERIES_DESIGNSTART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM DesignStart 片上系统系列（SoC Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1
CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3
```

**定义位置（Location）**：[`soc/arm/designstart/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/designstart/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ARM)、[`CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1`](P263_soc_arm_配置项参考.md#CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1)、[`CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3`](P263_soc_arm_配置项参考.md#CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ARM`。

<a id="CONFIG_SOC_SERIES_FVP_AEM"></a>

## 263.16 `CONFIG_SOC_SERIES_FVP_AEM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Arm 固定虚拟平台架构包络模型系列支持（FVP AEM，Architectural Envelope Model）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_V8A
CONFIG_SOC_V9A
CONFIG_SOC_A320
CONFIG_SOC_V8A_AARCH32
```

**定义位置（Location）**：[`soc/arm/fvp_aem/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/fvp_aem/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_V8A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_V8A)、[`CONFIG_SOC_V9A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_V9A)、[`CONFIG_SOC_A320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_A320)、[`CONFIG_SOC_V8A_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_V8A_AARCH32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_V8A`、`CONFIG_SOC_V9A`、`CONFIG_SOC_A320`、`CONFIG_SOC_V8A_AARCH32`。

<a id="CONFIG_SOC_SERIES_FVP_AEMV8R"></a>

## 263.17 `CONFIG_SOC_SERIES_FVP_AEMV8R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ARM FVP AEMv8R AArch64 系列支持（Series support）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FVP_AEMV8R_AARCH64
CONFIG_SOC_FVP_AEMV8R_AARCH32
```

**定义位置（Location）**：[`soc/arm/fvp_aemv8r/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/fvp_aemv8r/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FVP_AEMV8R_AARCH64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH64)、[`CONFIG_SOC_FVP_AEMV8R_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FVP_AEMV8R_AARCH64`、`CONFIG_SOC_FVP_AEMV8R_AARCH32`。

<a id="CONFIG_SOC_SERIES_MPS2"></a>

## 263.18 `CONFIG_SOC_SERIES_MPS2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ARM MPS2 微控制器系列支持（MCU Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_AN383
CONFIG_SOC_AN385
CONFIG_SOC_AN386
CONFIG_SOC_AN500
CONFIG_SOC_AN521
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ARM)、[`CONFIG_SOC_AN383`](P263_soc_arm_配置项参考.md#CONFIG_SOC_AN383)、[`CONFIG_SOC_AN385`](P263_soc_arm_配置项参考.md#CONFIG_SOC_AN385)、[`CONFIG_SOC_AN386`](P263_soc_arm_配置项参考.md#CONFIG_SOC_AN386)、[`CONFIG_SOC_AN500`](P263_soc_arm_配置项参考.md#CONFIG_SOC_AN500)、[`CONFIG_SOC_AN521`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN521)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ARM`、`CONFIG_SOC_AN521`。

<a id="CONFIG_SOC_SERIES_MPS3"></a>

## 263.19 `CONFIG_SOC_SERIES_MPS3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ARM MPS3 微控制器系列支持（MCU Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ARM
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MPS3
CONFIG_SOC_CORSTONE300
CONFIG_SOC_CORSTONE310
CONFIG_SOC_AN536
```

**定义位置（Location）**：[`soc/arm/mps3/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps3/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ARM)、[`CONFIG_BOARD_MPS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MPS3)、[`CONFIG_SOC_CORSTONE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE300)、[`CONFIG_SOC_CORSTONE310`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE310)、[`CONFIG_SOC_AN536`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN536)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ARM`、`CONFIG_BOARD_MPS3`、`CONFIG_SOC_CORSTONE300`、`CONFIG_SOC_CORSTONE310`、`CONFIG_SOC_AN536`。

<a id="CONFIG_SOC_SERIES_MPS4"></a>

## 263.20 `CONFIG_SOC_SERIES_MPS4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ARM MPS4 微控制器系列支持（MCU Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ARM
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MPS4
CONFIG_SOC_CORSTONE315
CONFIG_SOC_CORSTONE320
```

**定义位置（Location）**：[`soc/arm/mps4/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps4/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ARM)、[`CONFIG_BOARD_MPS4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MPS4)、[`CONFIG_SOC_CORSTONE315`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE315)、[`CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CORSTONE320)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ARM`、`CONFIG_BOARD_MPS4`、`CONFIG_SOC_CORSTONE315`、`CONFIG_SOC_CORSTONE320`。

<a id="CONFIG_SOC_SERIES_MUSCA"></a>

## 263.21 `CONFIG_SOC_SERIES_MUSCA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM v2m MUSCA 微控制器系列（MCU Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ARM
```

**被选择（Selected by）**

```text
CONFIG_SOC_MUSCA_B1
CONFIG_SOC_MUSCA_S1
```

**定义位置（Location）**：[`soc/arm/musca/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/musca/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ARM)、[`CONFIG_SOC_MUSCA_B1`](P263_soc_arm_配置项参考.md#CONFIG_SOC_MUSCA_B1)、[`CONFIG_SOC_MUSCA_S1`](P263_soc_arm_配置项参考.md#CONFIG_SOC_MUSCA_S1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ARM`。

<a id="SB_CONFIG_SOC_AN383"></a>

## 263.22 `SB_CONFIG_SOC_AN383`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MPS2 上的 ARM Cortex-M0+ SMM，应用说明 AN383（Application Note AN383）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_MPS2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MPS2
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_MPS2`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_SERIES_MPS2)、[`SB_CONFIG_BOARD_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MPS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_MPS2`。

<a id="SB_CONFIG_SOC_AN385"></a>

## 263.23 `SB_CONFIG_SOC_AN385`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MPS2 上的 ARM Cortex-M3 SMM，应用说明 AN385（Application Note AN385）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_MPS2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MPS2
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_MPS2`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_SERIES_MPS2)、[`SB_CONFIG_BOARD_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MPS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_MPS2`。

<a id="SB_CONFIG_SOC_AN386"></a>

## 263.24 `SB_CONFIG_SOC_AN386`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MPS2 上的 ARM Cortex-M4 SMM，应用说明 AN386（Application Note AN386）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_MPS2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MPS2
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L23)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_MPS2`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_SERIES_MPS2)、[`SB_CONFIG_BOARD_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MPS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_MPS2`。

<a id="SB_CONFIG_SOC_AN500"></a>

## 263.25 `SB_CONFIG_SOC_AN500`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MPS2+ 上的 ARM Cortex-M7 SMM，应用说明 AN500（Application Note AN500）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_MPS2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MPS2
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L29)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_MPS2`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_SERIES_MPS2)、[`SB_CONFIG_BOARD_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MPS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_MPS2`。

<a id="SB_CONFIG_SOC_AN521_CPU0"></a>

## 263.26 `SB_CONFIG_SOC_AN521_CPU0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MPS2+ 上的 ARM Cortex-M33 SMM-SSE-200（AN521），CPU0 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AN521
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MPS2
SB_CONFIG_BOARD_MPS2
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L39)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AN521`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AN521)、[`SB_CONFIG_BOARD_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MPS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_AN521`、`SB_CONFIG_BOARD_MPS2`。

<a id="SB_CONFIG_SOC_AN521_CPU1"></a>

## 263.27 `SB_CONFIG_SOC_AN521_CPU1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MPS2+ 上的 ARM Cortex-M33 SMM-SSE-200（AN521），CPU1 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AN521
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MPS2
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L45)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AN521`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AN521)、[`SB_CONFIG_BOARD_MPS2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MPS2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_AN521`、`SB_CONFIG_BOARD_MPS2`。

<a id="SB_CONFIG_SOC_AN536_CPU0"></a>

## 263.28 `SB_CONFIG_SOC_AN536_CPU0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

MPS3 AN536 平台的 Arm Cortex-R52 CPU0 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AN536
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MPS3
```

**定义位置（Location）**：[`soc/arm/mps3/Kconfig.soc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps3/Kconfig.soc#L27)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AN536`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AN536)、[`SB_CONFIG_BOARD_MPS3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MPS3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_AN536`、`SB_CONFIG_BOARD_MPS3`。

<a id="SB_CONFIG_SOC_BEETLE_R0"></a>

## 263.29 `SB_CONFIG_SOC_BEETLE_R0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM BEETLE R0 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_BEETLE
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_V2M_BEETLE
```

**定义位置（Location）**：[`soc/arm/beetle/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/beetle/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_BEETLE`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_SERIES_BEETLE)、[`SB_CONFIG_BOARD_V2M_BEETLE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_V2M_BEETLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_V2M_BEETLE`。

<a id="SB_CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1"></a>

## 263.30 `SB_CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM Cortex-M1 DesignStart 现场可编程门阵列（FPGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_DESIGNSTART
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ARTY_A7
```

**定义位置（Location）**：[`soc/arm/designstart/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/designstart/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_DESIGNSTART`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_SERIES_DESIGNSTART)、[`SB_CONFIG_BOARD_ARTY_A7`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ARTY_A7)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ARTY_A7`。

<a id="SB_CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3"></a>

## 263.31 `SB_CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM Cortex-M3 DesignStart 现场可编程门阵列（FPGA）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_DESIGNSTART
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ARTY_A7
SB_CONFIG_BOARD_SCOBC_A1
```

**定义位置（Location）**：[`soc/arm/designstart/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/designstart/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_DESIGNSTART`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_SERIES_DESIGNSTART)、[`SB_CONFIG_BOARD_ARTY_A7`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ARTY_A7)、[`SB_CONFIG_BOARD_SCOBC_A1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_SCOBC_A1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ARTY_A7`、`SB_CONFIG_BOARD_SCOBC_A1`。

<a id="SB_CONFIG_SOC_FVP_AEMV8R_SIMULATE_CPU_PM"></a>

## 263.32 `SB_CONFIG_SOC_FVP_AEMV8R_SIMULATE_CPU_PM`

**提示（Prompt）**：为 FVP_BaseR_AEMv8R 模拟 CPU 电源管理（Simulate CPU Power Management）

**说明（Help）**

为 FVP_BaseR_AEMv8R 模拟 CPU 电源管理功能（cpu power management）。当 Zephyr 内核尝试通过 `pm_cpu_on()` 启动辅助内核（secondary core）时，此操作始终成功，因为它确实成功启动了辅助内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_SOC_FVP_AEMV8R_AARCH64
```

**定义位置（Location）**：[`soc/arm/fvp_aemv8r/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/fvp_aemv8r/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FVP_AEMV8R_AARCH64`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FVP_AEMV8R_AARCH64)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FVP_AEMV8R_AARCH64`。

<a id="SB_CONFIG_SOC_MUSCA_B1"></a>

## 263.33 `SB_CONFIG_SOC_MUSCA_B1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MUSCA-B1 上的 ARM Cortex-M33 SMM-SSE-200

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_MUSCA
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_V2M_MUSCA_B1
```

**定义位置（Location）**：[`soc/arm/musca/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/musca/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_MUSCA`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_SERIES_MUSCA)、[`SB_CONFIG_BOARD_V2M_MUSCA_B1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_V2M_MUSCA_B1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_V2M_MUSCA_B1`。

<a id="SB_CONFIG_SOC_MUSCA_S1"></a>

## 263.34 `SB_CONFIG_SOC_MUSCA_S1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

V2M-MUSCA-S1 上的 ARM Cortex-M33 SMM-SSE-200

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_MUSCA
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_V2M_MUSCA_S1
```

**定义位置（Location）**：[`soc/arm/musca/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/musca/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_MUSCA`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_SERIES_MUSCA)、[`SB_CONFIG_BOARD_V2M_MUSCA_S1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_V2M_MUSCA_S1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_V2M_MUSCA_S1`。

<a id="SB_CONFIG_SOC_SERIES_BEETLE"></a>

## 263.35 `SB_CONFIG_SOC_SERIES_BEETLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Beetle 微控制器系列支持（MCU Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ARM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_BEETLE_R0
```

**定义位置（Location）**：[`soc/arm/beetle/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/beetle/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ARM)、[`SB_CONFIG_SOC_BEETLE_R0`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_BEETLE_R0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ARM`。

<a id="SB_CONFIG_SOC_SERIES_DESIGNSTART"></a>

## 263.36 `SB_CONFIG_SOC_SERIES_DESIGNSTART`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM DesignStart 片上系统系列（SoC Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ARM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1
SB_CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3
```

**定义位置（Location）**：[`soc/arm/designstart/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/designstart/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ARM)、[`SB_CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1)、[`SB_CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ARM`。

<a id="SB_CONFIG_SOC_SERIES_FVP_AEM"></a>

## 263.37 `SB_CONFIG_SOC_SERIES_FVP_AEM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Arm 固定虚拟平台架构包络模型系列支持（FVP AEM，Architectural Envelope Model）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_SOC_V8A
SB_CONFIG_SOC_V9A
SB_CONFIG_SOC_A320
SB_CONFIG_SOC_V8A_AARCH32
```

**定义位置（Location）**：[`soc/arm/fvp_aem/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/fvp_aem/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_V8A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_V8A)、[`SB_CONFIG_SOC_V9A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_V9A)、[`SB_CONFIG_SOC_A320`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_A320)、[`SB_CONFIG_SOC_V8A_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_V8A_AARCH32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_V8A`、`SB_CONFIG_SOC_V9A`、`SB_CONFIG_SOC_A320`、`SB_CONFIG_SOC_V8A_AARCH32`。

<a id="SB_CONFIG_SOC_SERIES_FVP_AEMV8R"></a>

## 263.38 `SB_CONFIG_SOC_SERIES_FVP_AEMV8R`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ARM FVP AEMv8R AArch64 系列支持（Series support）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_SOC_FVP_AEMV8R_AARCH64
SB_CONFIG_SOC_FVP_AEMV8R_AARCH32
```

**定义位置（Location）**：[`soc/arm/fvp_aemv8r/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/fvp_aemv8r/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FVP_AEMV8R_AARCH64`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FVP_AEMV8R_AARCH64)、[`SB_CONFIG_SOC_FVP_AEMV8R_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FVP_AEMV8R_AARCH32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FVP_AEMV8R_AARCH64`、`SB_CONFIG_SOC_FVP_AEMV8R_AARCH32`。

<a id="SB_CONFIG_SOC_SERIES_MPS2"></a>

## 263.39 `SB_CONFIG_SOC_SERIES_MPS2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ARM MPS2 微控制器系列支持（MCU Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ARM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_AN383
SB_CONFIG_SOC_AN385
SB_CONFIG_SOC_AN386
SB_CONFIG_SOC_AN500
SB_CONFIG_SOC_AN521
```

**定义位置（Location）**：[`soc/arm/mps2/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps2/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ARM)、[`SB_CONFIG_SOC_AN383`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_AN383)、[`SB_CONFIG_SOC_AN385`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_AN385)、[`SB_CONFIG_SOC_AN386`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_AN386)、[`SB_CONFIG_SOC_AN500`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_AN500)、[`SB_CONFIG_SOC_AN521`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AN521)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ARM`、`SB_CONFIG_SOC_AN521`。

<a id="SB_CONFIG_SOC_SERIES_MPS3"></a>

## 263.40 `SB_CONFIG_SOC_SERIES_MPS3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ARM MPS3 微控制器系列支持（MCU Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ARM
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MPS3
SB_CONFIG_SOC_CORSTONE300
SB_CONFIG_SOC_CORSTONE310
SB_CONFIG_SOC_AN536
```

**定义位置（Location）**：[`soc/arm/mps3/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps3/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ARM)、[`SB_CONFIG_BOARD_MPS3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MPS3)、[`SB_CONFIG_SOC_CORSTONE300`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CORSTONE300)、[`SB_CONFIG_SOC_CORSTONE310`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CORSTONE310)、[`SB_CONFIG_SOC_AN536`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AN536)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ARM`、`SB_CONFIG_BOARD_MPS3`、`SB_CONFIG_SOC_CORSTONE300`、`SB_CONFIG_SOC_CORSTONE310`、`SB_CONFIG_SOC_AN536`。

<a id="SB_CONFIG_SOC_SERIES_MPS4"></a>

## 263.41 `SB_CONFIG_SOC_SERIES_MPS4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ARM MPS4 微控制器系列支持（MCU Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ARM
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MPS4
SB_CONFIG_SOC_CORSTONE315
SB_CONFIG_SOC_CORSTONE320
```

**定义位置（Location）**：[`soc/arm/mps4/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/mps4/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ARM)、[`SB_CONFIG_BOARD_MPS4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MPS4)、[`SB_CONFIG_SOC_CORSTONE315`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CORSTONE315)、[`SB_CONFIG_SOC_CORSTONE320`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_CORSTONE320)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ARM`、`SB_CONFIG_BOARD_MPS4`、`SB_CONFIG_SOC_CORSTONE315`、`SB_CONFIG_SOC_CORSTONE320`。

<a id="SB_CONFIG_SOC_SERIES_MUSCA"></a>

## 263.42 `SB_CONFIG_SOC_SERIES_MUSCA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM v2m MUSCA 微控制器系列（MCU Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ARM
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MUSCA_B1
SB_CONFIG_SOC_MUSCA_S1
```

**定义位置（Location）**：[`soc/arm/musca/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/arm/musca/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ARM)、[`SB_CONFIG_SOC_MUSCA_B1`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_MUSCA_B1)、[`SB_CONFIG_SOC_MUSCA_S1`](P263_soc_arm_配置项参考.md#SB_CONFIG_SOC_MUSCA_S1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ARM`。

<!-- kconfig-navigation -->

[上一章](P262_soc_antmicro_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P264_soc_aspeed_配置项参考.md)
