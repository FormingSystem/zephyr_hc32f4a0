---
id: learning.zephyr-docs.kconfig-reference.page-316
title: "`soc/xlnx`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第316章\_`soc/xlnx`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/xlnx` 的 42 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_AMD_VERSAL2_APU"></a>

## 316.1 `CONFIG_SOC_AMD_VERSAL2_APU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AMD Versal 第二代应用处理单元（Gen 2 APU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AMD_VERSAL2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_VERSAL2_APU
```

**定义位置（Location）**：[`soc/xlnx/versal2/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versal2/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AMD_VERSAL2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2)、[`CONFIG_BOARD_VERSAL2_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_VERSAL2_APU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AMD_VERSAL2`、`CONFIG_BOARD_VERSAL2_APU`。

<a id="CONFIG_SOC_AMD_VERSAL2_RPU"></a>

## 316.2 `CONFIG_SOC_AMD_VERSAL2_RPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AMD Versal 第二代实时处理单元（Gen 2 RPU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AMD_VERSAL2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_VERSAL2_RPU
```

**定义位置（Location）**：[`soc/xlnx/versal2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versal2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AMD_VERSAL2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2)、[`CONFIG_BOARD_VERSAL2_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_VERSAL2_RPU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AMD_VERSAL2`、`CONFIG_BOARD_VERSAL2_RPU`。

<a id="CONFIG_SOC_AMD_VERSALNET_APU"></a>

## 316.3 `CONFIG_SOC_AMD_VERSALNET_APU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AMD Versal NET SoC 应用处理单元（APU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AMD_VERSALNET
```

**被选择（Selected by）**

```text
CONFIG_BOARD_VERSALNET_APU
```

**定义位置（Location）**：[`soc/xlnx/versalnet/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versalnet/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AMD_VERSALNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET)、[`CONFIG_BOARD_VERSALNET_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_VERSALNET_APU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AMD_VERSALNET`、`CONFIG_BOARD_VERSALNET_APU`。

<a id="CONFIG_SOC_AMD_VERSALNET_RPU"></a>

## 316.4 `CONFIG_SOC_AMD_VERSALNET_RPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AMD Versal NET SoC 实时处理单元（RPU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AMD_VERSALNET
```

**被选择（Selected by）**

```text
CONFIG_BOARD_VERSALNET_RPU
```

**定义位置（Location）**：[`soc/xlnx/versalnet/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versalnet/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AMD_VERSALNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET)、[`CONFIG_BOARD_VERSALNET_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_VERSALNET_RPU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AMD_VERSALNET`、`CONFIG_BOARD_VERSALNET_RPU`。

<a id="CONFIG_SOC_SERIES_XC7ZXXX"></a>

## 316.5 `CONFIG_SOC_SERIES_XC7ZXXX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Xilinx Zynq-7000（XC7Zxxx）片上系统系列（SoC series）支持，采用双核 ARM Cortex-A9。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_XILINX_ZYNQ7000
```

**被选择（Selected by）**

```text
CONFIG_SOC_XC7Z010
CONFIG_SOC_XC7Z015
CONFIG_SOC_XC7Z020
CONFIG_SOC_XC7Z030
CONFIG_SOC_XC7Z035
CONFIG_SOC_XC7Z045
CONFIG_SOC_XC7Z100
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_XILINX_ZYNQ7000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_XILINX_ZYNQ7000)、[`CONFIG_SOC_XC7Z010`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_XC7Z010)、[`CONFIG_SOC_XC7Z015`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_XC7Z015)、[`CONFIG_SOC_XC7Z020`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_XC7Z020)、[`CONFIG_SOC_XC7Z030`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_XC7Z030)、[`CONFIG_SOC_XC7Z035`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_XC7Z035)、[`CONFIG_SOC_XC7Z045`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_XC7Z045)、[`CONFIG_SOC_XC7Z100`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_XC7Z100)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_XILINX_ZYNQ7000`。

<a id="CONFIG_SOC_SERIES_XC7ZXXXS"></a>

## 316.6 `CONFIG_SOC_SERIES_XC7ZXXXS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Xilinx Zynq-7000S（XC7ZxxxS）片上系统系列（SoC series）支持，采用单核 ARM Cortex-A9。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_XILINX_ZYNQ7000
```

**被选择（Selected by）**

```text
CONFIG_SOC_XC7Z007S
CONFIG_SOC_XC7Z012S
CONFIG_SOC_XC7Z014S
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_XILINX_ZYNQ7000`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_XILINX_ZYNQ7000)、[`CONFIG_SOC_XC7Z007S`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_XC7Z007S)、[`CONFIG_SOC_XC7Z012S`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_XC7Z012S)、[`CONFIG_SOC_XC7Z014S`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_XC7Z014S)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_XILINX_ZYNQ7000`。

<a id="CONFIG_SOC_VERSAL_APU"></a>

## 316.7 `CONFIG_SOC_VERSAL_APU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AMD Versal 应用处理单元（APU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AMD_VERSAL
```

**被选择（Selected by）**

```text
CONFIG_BOARD_VERSAL_APU
```

**定义位置（Location）**：[`soc/xlnx/versal/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versal/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AMD_VERSAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL)、[`CONFIG_BOARD_VERSAL_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_VERSAL_APU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AMD_VERSAL`、`CONFIG_BOARD_VERSAL_APU`。

<a id="CONFIG_SOC_VERSAL_RPU"></a>

## 316.8 `CONFIG_SOC_VERSAL_RPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AMD Versal 实时处理单元（RPU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_AMD_VERSAL
```

**被选择（Selected by）**

```text
CONFIG_BOARD_VERSAL_RPU
CONFIG_BOARD_TE0950
CONFIG_BOARD_SCOBC_V1
```

**定义位置（Location）**：[`soc/xlnx/versal/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versal/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AMD_VERSAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL)、[`CONFIG_BOARD_VERSAL_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_VERSAL_RPU)、[`CONFIG_BOARD_TE0950`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TE0950)、[`CONFIG_BOARD_SCOBC_V1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_SCOBC_V1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_AMD_VERSAL`、`CONFIG_BOARD_VERSAL_RPU`、`CONFIG_BOARD_TE0950`、`CONFIG_BOARD_SCOBC_V1`。

<a id="CONFIG_SOC_VERSAL_RPU_REMOTEPROC"></a>

## 316.9 `CONFIG_SOC_VERSAL_RPU_REMOTEPROC`

**提示（Prompt）**：支持主机侧远程处理器加载和附着（remoteproc loading and attachment）

**说明（Help）**

将资源表（resource table）放入名为 `RPROC` 的链接器内存区域。还将 AMD-Xilinx R5 远程处理器驱动（remoteproc driver）用于附着到已运行实时处理单元（RPU）的元数据，放在该区域起始处。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_VERSAL_RPU && CONFIG_OPENAMP_RSC_TABLE
```

**定义位置（Location）**：[`soc/xlnx/versal/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versal/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_VERSAL_RPU`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_VERSAL_RPU)、[`CONFIG_OPENAMP_RSC_TABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENAMP_RSC_TABLE)。

<a id="CONFIG_SOC_VERSAL_RPU_REMOTEPROC_DATA_LMA"></a>

## 316.10 `CONFIG_SOC_VERSAL_RPU_REMOTEPROC_DATA_LMA`

**提示（Prompt）**：在 RPROC 区域存储已初始化数据的加载镜像（initialized data load image）

**说明（Help）**

将 `RPROC` 用作已初始化运行时数据的加载区域（load region）。当包含 RPU 代码的 ROM 区域无法同时容纳数据加载镜像时启用，例如代码位于紧耦合内存（TCM）、数据位于片上存储器（OCM）的分离布局。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_VERSAL_RPU_REMOTEPROC && CONFIG_XIP
```

**定义位置（Location）**：[`soc/xlnx/versal/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versal/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 支持主机侧远程处理器加载和附着（remoteproc loading and attachment）

**配置项引用（Symbol References）**：[`CONFIG_SOC_VERSAL_RPU_REMOTEPROC`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_VERSAL_RPU_REMOTEPROC)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

<a id="CONFIG_SOC_XC7Z007S"></a>

## 316.11 `CONFIG_SOC_XC7Z007S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

1 个最高 766 MHz 的 ARM Cortex-A9 内核、Artix-7 可编程逻辑（programmable logic）、23k 个逻辑单元（logic cells）、1.8 Mb 块 RAM（block RAM）、60 个 DSP 单元（slices），最多 100 个 I/O 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XC7ZXXXS
```

**被选择（Selected by）**

```text
CONFIG_BOARD_QEMU_CORTEX_A9
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XC7ZXXXS`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_SERIES_XC7ZXXXS)、[`CONFIG_BOARD_QEMU_CORTEX_A9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_QEMU_CORTEX_A9)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_QEMU_CORTEX_A9`。

<a id="CONFIG_SOC_XC7Z010"></a>

## 316.12 `CONFIG_SOC_XC7Z010`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 866 MHz 的 ARM Cortex-A9 内核、Artix-7 可编程逻辑（programmable logic）、28k 个逻辑单元（logic cells）、2.1Mb 块 RAM（block RAM）、800 个 DSP 单元（slices），最多 100 个 I/O 引脚。译注：DSP 数量 800 按官方原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XC7ZXXX
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ZYBO
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_SERIES_XC7ZXXX)、[`CONFIG_BOARD_ZYBO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ZYBO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ZYBO`。

<a id="CONFIG_SOC_XC7Z012S"></a>

## 316.13 `CONFIG_SOC_XC7Z012S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

1 个最高 766 MHz 的 ARM Cortex-A9 内核、Artix-7 可编程逻辑（programmable logic）、55k 个逻辑单元（logic cells）、2.5Mb 块 RAM（block RAM）、120 个 DSP 单元（slices），最多 150 个 I/O 引脚和 4 个收发器（transceivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XC7ZXXXS
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XC7ZXXXS`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_SERIES_XC7ZXXXS)。

<a id="CONFIG_SOC_XC7Z014S"></a>

## 316.14 `CONFIG_SOC_XC7Z014S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

1 个最高 766 MHz 的 ARM Cortex-A9 内核、Artix-7 可编程逻辑（programmable logic）、65k 个逻辑单元（logic cells）、3.8Mb 块 RAM（block RAM）、170 个 DSP 单元（slices），最多 200 个 I/O 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XC7ZXXXS
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XC7ZXXXS`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_SERIES_XC7ZXXXS)。

<a id="CONFIG_SOC_XC7Z015"></a>

## 316.15 `CONFIG_SOC_XC7Z015`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 866 MHz 的 ARM Cortex-A9 内核、Artix-7 可编程逻辑（programmable logic）、74k 个逻辑单元（logic cells）、3.3Mb 块 RAM（block RAM）、160 个 DSP 单元（slices），最多 150 个 I/O 引脚和 4 个收发器（transceivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XC7ZXXX
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_SERIES_XC7ZXXX)。

<a id="CONFIG_SOC_XC7Z020"></a>

## 316.16 `CONFIG_SOC_XC7Z020`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 866 MHz 的 ARM Cortex-A9 内核、Artix-7 可编程逻辑（programmable logic）、85k 个逻辑单元（logic cells）、4.9Mb 块 RAM（block RAM）、220 个 DSP 单元（slices），最多 200 个 I/O 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XC7ZXXX
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ZEDBOARD
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_SERIES_XC7ZXXX)、[`CONFIG_BOARD_ZEDBOARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ZEDBOARD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ZEDBOARD`。

<a id="CONFIG_SOC_XC7Z030"></a>

## 316.17 `CONFIG_SOC_XC7Z030`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 1 GHz 的 ARM Cortex-A9 内核、Kintex-7 可编程逻辑（programmable logic）、125k 个逻辑单元（logic cells）、9.3Mb 块 RAM（block RAM）、400 个 DSP 单元（slices），最多 250 个 I/O 引脚和 4 个收发器（transceivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XC7ZXXX
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_SERIES_XC7ZXXX)。

<a id="CONFIG_SOC_XC7Z035"></a>

## 316.18 `CONFIG_SOC_XC7Z035`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 1 GHz 的 ARM Cortex-A9 内核、Kintex-7 可编程逻辑（programmable logic）、275k 个逻辑单元（logic cells）、17.6Mb 块 RAM（block RAM）、900 个 DSP 单元（slices），最多 362 个 I/O 引脚和 16 个收发器（transceivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XC7ZXXX
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_SERIES_XC7ZXXX)。

<a id="CONFIG_SOC_XC7Z045"></a>

## 316.19 `CONFIG_SOC_XC7Z045`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 1 GHz 的 ARM Cortex-A9 内核、Kintex-7 可编程逻辑（programmable logic）、350k 个逻辑单元（logic cells）、19.1Mb 块 RAM（block RAM）、900 个 DSP 单元（slices），最多 362 个 I/O 引脚和 16 个收发器（transceivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XC7ZXXX
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_SERIES_XC7ZXXX)。

<a id="CONFIG_SOC_XC7Z100"></a>

## 316.20 `CONFIG_SOC_XC7Z100`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 1 GHz 的 ARM Cortex-A9 内核、Kintex-7 可编程逻辑（programmable logic）、444k 个逻辑单元（logic cells）、26.5Mb 块 RAM（block RAM）、2020 个 DSP 单元（slices），最多 400 个 I/O 引脚和 16 个收发器（transceivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_XC7ZXXX
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#CONFIG_SOC_SERIES_XC7ZXXX)。

<a id="CONFIG_SOC_XILINX_ZYNQMP_APU"></a>

## 316.21 `CONFIG_SOC_XILINX_ZYNQMP_APU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Xilinx ZynqMP 应用处理单元（APU，Cortex-A53）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_XILINX_ZYNQMP
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ZYNQMP_APU
```

**定义位置（Location）**：[`soc/xlnx/zynqmp/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynqmp/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_XILINX_ZYNQMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP)、[`CONFIG_BOARD_ZYNQMP_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ZYNQMP_APU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_XILINX_ZYNQMP`、`CONFIG_BOARD_ZYNQMP_APU`。

<a id="CONFIG_SOC_XILINX_ZYNQMP_RPU"></a>

## 316.22 `CONFIG_SOC_XILINX_ZYNQMP_RPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Xilinx ZynqMP 实时处理单元（RPU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_XILINX_ZYNQMP
```

**被选择（Selected by）**

```text
CONFIG_BOARD_QEMU_CORTEX_R5
CONFIG_BOARD_KV260_R5
CONFIG_BOARD_ZYNQMP_RPU
CONFIG_BOARD_MERCURY_XU
```

**定义位置（Location）**：[`soc/xlnx/zynqmp/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynqmp/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_XILINX_ZYNQMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP)、[`CONFIG_BOARD_QEMU_CORTEX_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_QEMU_CORTEX_R5)、[`CONFIG_BOARD_KV260_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_KV260_R5)、[`CONFIG_BOARD_ZYNQMP_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ZYNQMP_RPU)、[`CONFIG_BOARD_MERCURY_XU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MERCURY_XU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_XILINX_ZYNQMP`、`CONFIG_BOARD_QEMU_CORTEX_R5`、`CONFIG_BOARD_KV260_R5`、`CONFIG_BOARD_ZYNQMP_RPU`、`CONFIG_BOARD_MERCURY_XU`。

<a id="SB_CONFIG_SOC_AMD_VERSAL2_APU"></a>

## 316.23 `SB_CONFIG_SOC_AMD_VERSAL2_APU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AMD Versal 第二代应用处理单元（Gen 2 APU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AMD_VERSAL2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_VERSAL2_APU
```

**定义位置（Location）**：[`soc/xlnx/versal2/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versal2/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AMD_VERSAL2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AMD_VERSAL2)、[`SB_CONFIG_BOARD_VERSAL2_APU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_VERSAL2_APU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_AMD_VERSAL2`、`SB_CONFIG_BOARD_VERSAL2_APU`。

<a id="SB_CONFIG_SOC_AMD_VERSAL2_RPU"></a>

## 316.24 `SB_CONFIG_SOC_AMD_VERSAL2_RPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AMD Versal 第二代实时处理单元（Gen 2 RPU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AMD_VERSAL2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_VERSAL2_RPU
```

**定义位置（Location）**：[`soc/xlnx/versal2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versal2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AMD_VERSAL2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AMD_VERSAL2)、[`SB_CONFIG_BOARD_VERSAL2_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_VERSAL2_RPU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_AMD_VERSAL2`、`SB_CONFIG_BOARD_VERSAL2_RPU`。

<a id="SB_CONFIG_SOC_AMD_VERSALNET_APU"></a>

## 316.25 `SB_CONFIG_SOC_AMD_VERSALNET_APU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AMD Versal NET SoC 应用处理单元（APU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AMD_VERSALNET
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_VERSALNET_APU
```

**定义位置（Location）**：[`soc/xlnx/versalnet/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versalnet/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AMD_VERSALNET`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AMD_VERSALNET)、[`SB_CONFIG_BOARD_VERSALNET_APU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_VERSALNET_APU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_AMD_VERSALNET`、`SB_CONFIG_BOARD_VERSALNET_APU`。

<a id="SB_CONFIG_SOC_AMD_VERSALNET_RPU"></a>

## 316.26 `SB_CONFIG_SOC_AMD_VERSALNET_RPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AMD Versal NET SoC 实时处理单元（RPU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AMD_VERSALNET
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_VERSALNET_RPU
```

**定义位置（Location）**：[`soc/xlnx/versalnet/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versalnet/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AMD_VERSALNET`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AMD_VERSALNET)、[`SB_CONFIG_BOARD_VERSALNET_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_VERSALNET_RPU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_AMD_VERSALNET`、`SB_CONFIG_BOARD_VERSALNET_RPU`。

<a id="SB_CONFIG_SOC_SERIES_XC7ZXXX"></a>

## 316.27 `SB_CONFIG_SOC_SERIES_XC7ZXXX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Xilinx Zynq-7000（XC7Zxxx）片上系统系列（SoC series）支持，采用双核 ARM Cortex-A9。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_XILINX_ZYNQ7000
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_XC7Z010
SB_CONFIG_SOC_XC7Z015
SB_CONFIG_SOC_XC7Z020
SB_CONFIG_SOC_XC7Z030
SB_CONFIG_SOC_XC7Z035
SB_CONFIG_SOC_XC7Z045
SB_CONFIG_SOC_XC7Z100
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_XILINX_ZYNQ7000`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_XILINX_ZYNQ7000)、[`SB_CONFIG_SOC_XC7Z010`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_XC7Z010)、[`SB_CONFIG_SOC_XC7Z015`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_XC7Z015)、[`SB_CONFIG_SOC_XC7Z020`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_XC7Z020)、[`SB_CONFIG_SOC_XC7Z030`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_XC7Z030)、[`SB_CONFIG_SOC_XC7Z035`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_XC7Z035)、[`SB_CONFIG_SOC_XC7Z045`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_XC7Z045)、[`SB_CONFIG_SOC_XC7Z100`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_XC7Z100)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_XILINX_ZYNQ7000`。

<a id="SB_CONFIG_SOC_SERIES_XC7ZXXXS"></a>

## 316.28 `SB_CONFIG_SOC_SERIES_XC7ZXXXS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Xilinx Zynq-7000S（XC7ZxxxS）片上系统系列（SoC series）支持，采用单核 ARM Cortex-A9。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_XILINX_ZYNQ7000
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_XC7Z007S
SB_CONFIG_SOC_XC7Z012S
SB_CONFIG_SOC_XC7Z014S
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc#L9)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_XILINX_ZYNQ7000`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_XILINX_ZYNQ7000)、[`SB_CONFIG_SOC_XC7Z007S`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_XC7Z007S)、[`SB_CONFIG_SOC_XC7Z012S`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_XC7Z012S)、[`SB_CONFIG_SOC_XC7Z014S`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_XC7Z014S)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_XILINX_ZYNQ7000`。

<a id="SB_CONFIG_SOC_VERSAL_APU"></a>

## 316.29 `SB_CONFIG_SOC_VERSAL_APU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AMD Versal 应用处理单元（APU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AMD_VERSAL
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_VERSAL_APU
```

**定义位置（Location）**：[`soc/xlnx/versal/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versal/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AMD_VERSAL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AMD_VERSAL)、[`SB_CONFIG_BOARD_VERSAL_APU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_VERSAL_APU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_AMD_VERSAL`、`SB_CONFIG_BOARD_VERSAL_APU`。

<a id="SB_CONFIG_SOC_VERSAL_RPU"></a>

## 316.30 `SB_CONFIG_SOC_VERSAL_RPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

AMD Versal 实时处理单元（RPU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_AMD_VERSAL
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_VERSAL_RPU
SB_CONFIG_BOARD_TE0950
SB_CONFIG_BOARD_SCOBC_V1
```

**定义位置（Location）**：[`soc/xlnx/versal/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/versal/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_AMD_VERSAL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_AMD_VERSAL)、[`SB_CONFIG_BOARD_VERSAL_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_VERSAL_RPU)、[`SB_CONFIG_BOARD_TE0950`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TE0950)、[`SB_CONFIG_BOARD_SCOBC_V1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_SCOBC_V1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_AMD_VERSAL`、`SB_CONFIG_BOARD_VERSAL_RPU`、`SB_CONFIG_BOARD_TE0950`、`SB_CONFIG_BOARD_SCOBC_V1`。

<a id="SB_CONFIG_SOC_XC7Z007S"></a>

## 316.31 `SB_CONFIG_SOC_XC7Z007S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

1 个最高 766 MHz 的 ARM Cortex-A9 内核、Artix-7 可编程逻辑（programmable logic）、23k 个逻辑单元（logic cells）、1.8 Mb 块 RAM（block RAM）、60 个 DSP 单元（slices），最多 100 个 I/O 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XC7ZXXXS
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_QEMU_CORTEX_A9
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XC7ZXXXS`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_SERIES_XC7ZXXXS)、[`SB_CONFIG_BOARD_QEMU_CORTEX_A9`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_QEMU_CORTEX_A9)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_QEMU_CORTEX_A9`。

<a id="SB_CONFIG_SOC_XC7Z010"></a>

## 316.32 `SB_CONFIG_SOC_XC7Z010`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 866 MHz 的 ARM Cortex-A9 内核、Artix-7 可编程逻辑（programmable logic）、28k 个逻辑单元（logic cells）、2.1Mb 块 RAM（block RAM）、800 个 DSP 单元（slices），最多 100 个 I/O 引脚。译注：DSP 数量 800 按官方原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XC7ZXXX
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ZYBO
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_SERIES_XC7ZXXX)、[`SB_CONFIG_BOARD_ZYBO`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ZYBO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ZYBO`。

<a id="SB_CONFIG_SOC_XC7Z012S"></a>

## 316.33 `SB_CONFIG_SOC_XC7Z012S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

1 个最高 766 MHz 的 ARM Cortex-A9 内核、Artix-7 可编程逻辑（programmable logic）、55k 个逻辑单元（logic cells）、2.5Mb 块 RAM（block RAM）、120 个 DSP 单元（slices），最多 150 个 I/O 引脚和 4 个收发器（transceivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XC7ZXXXS
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc#L23)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XC7ZXXXS`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_SERIES_XC7ZXXXS)。

<a id="SB_CONFIG_SOC_XC7Z014S"></a>

## 316.34 `SB_CONFIG_SOC_XC7Z014S`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

1 个最高 766 MHz 的 ARM Cortex-A9 内核、Artix-7 可编程逻辑（programmable logic）、65k 个逻辑单元（logic cells）、3.8Mb 块 RAM（block RAM）、170 个 DSP 单元（slices），最多 200 个 I/O 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XC7ZXXXS
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxxs/Kconfig.soc#L31)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XC7ZXXXS`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_SERIES_XC7ZXXXS)。

<a id="SB_CONFIG_SOC_XC7Z015"></a>

## 316.35 `SB_CONFIG_SOC_XC7Z015`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 866 MHz 的 ARM Cortex-A9 内核、Artix-7 可编程逻辑（programmable logic）、74k 个逻辑单元（logic cells）、3.3Mb 块 RAM（block RAM）、160 个 DSP 单元（slices），最多 150 个 I/O 引脚和 4 个收发器（transceivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XC7ZXXX
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L23)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_SERIES_XC7ZXXX)。

<a id="SB_CONFIG_SOC_XC7Z020"></a>

## 316.36 `SB_CONFIG_SOC_XC7Z020`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 866 MHz 的 ARM Cortex-A9 内核、Artix-7 可编程逻辑（programmable logic）、85k 个逻辑单元（logic cells）、4.9Mb 块 RAM（block RAM）、220 个 DSP 单元（slices），最多 200 个 I/O 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XC7ZXXX
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ZEDBOARD
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L31)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_SERIES_XC7ZXXX)、[`SB_CONFIG_BOARD_ZEDBOARD`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ZEDBOARD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ZEDBOARD`。

<a id="SB_CONFIG_SOC_XC7Z030"></a>

## 316.37 `SB_CONFIG_SOC_XC7Z030`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 1 GHz 的 ARM Cortex-A9 内核、Kintex-7 可编程逻辑（programmable logic）、125k 个逻辑单元（logic cells）、9.3Mb 块 RAM（block RAM）、400 个 DSP 单元（slices），最多 250 个 I/O 引脚和 4 个收发器（transceivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XC7ZXXX
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L38)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_SERIES_XC7ZXXX)。

<a id="SB_CONFIG_SOC_XC7Z035"></a>

## 316.38 `SB_CONFIG_SOC_XC7Z035`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 1 GHz 的 ARM Cortex-A9 内核、Kintex-7 可编程逻辑（programmable logic）、275k 个逻辑单元（logic cells）、17.6Mb 块 RAM（block RAM）、900 个 DSP 单元（slices），最多 362 个 I/O 引脚和 16 个收发器（transceivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XC7ZXXX
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L46)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_SERIES_XC7ZXXX)。

<a id="SB_CONFIG_SOC_XC7Z045"></a>

## 316.39 `SB_CONFIG_SOC_XC7Z045`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 1 GHz 的 ARM Cortex-A9 内核、Kintex-7 可编程逻辑（programmable logic）、350k 个逻辑单元（logic cells）、19.1Mb 块 RAM（block RAM）、900 个 DSP 单元（slices），最多 362 个 I/O 引脚和 16 个收发器（transceivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XC7ZXXX
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L54)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_SERIES_XC7ZXXX)。

<a id="SB_CONFIG_SOC_XC7Z100"></a>

## 316.40 `SB_CONFIG_SOC_XC7Z100`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

2 个最高 1 GHz 的 ARM Cortex-A9 内核、Kintex-7 可编程逻辑（programmable logic）、444k 个逻辑单元（logic cells）、26.5Mb 块 RAM（block RAM）、2020 个 DSP 单元（slices），最多 400 个 I/O 引脚和 16 个收发器（transceivers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_XC7ZXXX
```

**定义位置（Location）**：[`soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynq7000/xc7zxxx/Kconfig.soc#L62)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_XC7ZXXX`](P316_soc_xlnx_配置项参考.md#SB_CONFIG_SOC_SERIES_XC7ZXXX)。

<a id="SB_CONFIG_SOC_XILINX_ZYNQMP_APU"></a>

## 316.41 `SB_CONFIG_SOC_XILINX_ZYNQMP_APU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Xilinx ZynqMP 应用处理单元（APU，Cortex-A53）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_XILINX_ZYNQMP
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ZYNQMP_APU
```

**定义位置（Location）**：[`soc/xlnx/zynqmp/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynqmp/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_XILINX_ZYNQMP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_XILINX_ZYNQMP)、[`SB_CONFIG_BOARD_ZYNQMP_APU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ZYNQMP_APU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_XILINX_ZYNQMP`、`SB_CONFIG_BOARD_ZYNQMP_APU`。

<a id="SB_CONFIG_SOC_XILINX_ZYNQMP_RPU"></a>

## 316.42 `SB_CONFIG_SOC_XILINX_ZYNQMP_RPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Xilinx ZynqMP 实时处理单元（RPU）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_XILINX_ZYNQMP
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_QEMU_CORTEX_R5
SB_CONFIG_BOARD_KV260_R5
SB_CONFIG_BOARD_ZYNQMP_RPU
SB_CONFIG_BOARD_MERCURY_XU
```

**定义位置（Location）**：[`soc/xlnx/zynqmp/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/xlnx/zynqmp/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_XILINX_ZYNQMP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_XILINX_ZYNQMP)、[`SB_CONFIG_BOARD_QEMU_CORTEX_R5`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_QEMU_CORTEX_R5)、[`SB_CONFIG_BOARD_KV260_R5`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_KV260_R5)、[`SB_CONFIG_BOARD_ZYNQMP_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ZYNQMP_RPU)、[`SB_CONFIG_BOARD_MERCURY_XU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MERCURY_XU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_XILINX_ZYNQMP`、`SB_CONFIG_BOARD_QEMU_CORTEX_R5`、`SB_CONFIG_BOARD_KV260_R5`、`SB_CONFIG_BOARD_ZYNQMP_RPU`、`SB_CONFIG_BOARD_MERCURY_XU`。

<!-- kconfig-navigation -->

[上一章](P315_soc_wch_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P317_subsys_Kconfig_配置项参考.md)
