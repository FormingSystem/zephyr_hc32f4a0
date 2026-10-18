---
id: learning.zephyr-docs.kconfig-reference.page-294
title: "`soc/nxp`配置项参考（2/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第294章\_`soc/nxp`配置项参考（2/3）

本章翻译官方 Kconfig 数据库中 `soc/nxp` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_OSC_HIGH_GAIN"></a>

## 294.1 `CONFIG_OSC_HIGH_GAIN`

**提示（Prompt）**：高增益振荡器（High gain oscillator）

**说明（Help）**

设置此项以使用振荡器的高增益模式（high-gain mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 振荡器模式选择（Oscillator Mode Selection）

<a id="CONFIG_OSC_LOW_POWER"></a>

## 294.2 `CONFIG_OSC_LOW_POWER`

**提示（Prompt）**：低功耗振荡器（Low power oscillator）

**说明（Help）**

设置此项以使用振荡器的低功耗模式（low-power mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 振荡器模式选择（Oscillator Mode Selection）

<a id="CONFIG_OSC_XTAL0_FREQ"></a>

## 294.3 `CONFIG_OSC_XTAL0_FREQ`

**提示（Prompt）**：外部振荡器频率（External oscillator frequency）

**说明（Help）**

设置外部振荡器频率，单位为 Hz。应由开发板的 defconfig 设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_OSC && CONFIG_SOC_FAMILY_KINETIS
```

**定义位置（Location）**：[`soc/nxp/kinetis/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_OSC`](P293_soc_nxp_配置项参考_1.md#CONFIG_HAS_OSC)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_PM_MCUX_DCDC"></a>

## 294.4 `CONFIG_PM_MCUX_DCDC`

**提示（Prompt）**：MCUX 直流－直流转换器模块驱动（dcdc converter module driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_IMXRT10XX || CONFIG_SOC_SERIES_IMXRT11XX || CONFIG_SOC_SERIES_IMXRT118X) && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_PM_MCUX_GPC"></a>

## 294.5 `CONFIG_PM_MCUX_GPC`

**提示（Prompt）**：MCUX 通用电源控制器驱动（general power controller driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_IMXRT10XX || CONFIG_SOC_SERIES_IMXRT11XX || CONFIG_SOC_SERIES_IMXRT118X) && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_PM_MCUX_PMU"></a>

## 294.6 `CONFIG_PM_MCUX_PMU`

**提示（Prompt）**：MCUX 电源管理单元驱动（power management unit driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_IMXRT10XX || CONFIG_SOC_SERIES_IMXRT11XX || CONFIG_SOC_SERIES_IMXRT118X) && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT10XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT10XX)、[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT10XX`、`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_RT685_ADSP_STACK_SIZE"></a>

## 294.7 `CONFIG_RT685_ADSP_STACK_SIZE`

**提示（Prompt）**：启动时栈大小（Boot time stack size）

**说明（Help）**

在 `RT685_ADSP_DATA_MEM` 区域末尾预留栈空间（stack space），起始位置为 `RT685_ADSP_DATA_MEM_ADDR - RT685_ADSP_STACK_SIZE`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_MIMXRT685S_HIFI4 && CONFIG_SOC_SERIES_IMXRT6XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
0x1000
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt6xx/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt6xx/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT685S_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_HIFI4)、[`CONFIG_SOC_SERIES_IMXRT6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT6XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT685S_HIFI4`、`CONFIG_SOC_SERIES_IMXRT6XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_RT798_HIFI4_STACK_SIZE"></a>

## 294.8 `CONFIG_RT798_HIFI4_STACK_SIZE`

**提示（Prompt）**：启动时栈大小（Boot time stack size）

**说明（Help）**

在数据区域末尾预留栈空间（stack space），起始位置为 `(data base - RT798_HIFI4_STACK_SIZE)`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_MIMXRT798S_HIFI4 && CONFIG_SOC_SERIES_IMXRT7XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
0x1000
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/hifi4/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/hifi4/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT798S_HIFI4`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMXRT798S_HIFI4)、[`CONFIG_SOC_SERIES_IMXRT7XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT7XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT7XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_S3MU_MCUX_S3MU"></a>

## 294.9 `CONFIG_S3MU_MCUX_S3MU`

**提示（Prompt）**：使用 MCUX 的 S3MU 驱动（S3MU MCUX Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT118X && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt118x/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt118x/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SECOND_CORE_BOOT_ADDRESS_MCUX"></a>

## 294.10 `CONFIG_SECOND_CORE_BOOT_ADDRESS_MCUX`

原库同名定义共 2 条；本项为数据库第 16592 条记录，各定义分别保留。

**提示（Prompt）**：第二内核的启动地址（second core boot address）

**说明（Help）**

这是第二内核的启动地址，也是复制 `SECOND_IMAGE` 的目标地址。默认设为 SRAM1 的基地址（base address）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SECOND_CORE_MCUX && CONFIG_SOC_SERIES_LPC54XXX && CONFIG_SOC_FAMILY_LPC
```

**默认值（Defaults）**

```text
0x20010000
```

**定义位置（Location）**：[`soc/nxp/lpc/lpc54xxx/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/lpc/lpc54xxx/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → LPC54114 Cortex-M0 第二内核（second core）

**配置项引用（Symbol References）**：[`CONFIG_SECOND_CORE_MCUX`](P294_soc_nxp_配置项参考_2.md#CONFIG_SECOND_CORE_MCUX)、[`CONFIG_SOC_SERIES_LPC54XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC54XXX)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC54XXX`、`CONFIG_SOC_FAMILY_LPC`。

<a id="CONFIG_SECOND_CORE_BOOT_ADDRESS_MCUX--record-16593"></a>

## 294.11 `CONFIG_SECOND_CORE_BOOT_ADDRESS_MCUX`

原库同名定义共 2 条；本项为数据库第 16593 条记录，各定义分别保留。

**提示（Prompt）**：第二内核的启动地址（second core boot address）

**说明（Help）**

这是第二内核的启动地址（boot address）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SECOND_CORE_MCUX && CONFIG_SOC_SERIES_LPC55XXX && CONFIG_SOC_FAMILY_LPC
```

**默认值（Defaults）**

```text
0x0
```

**定义位置（Location）**：[`soc/nxp/lpc/lpc55xxx/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/lpc/lpc55xxx/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → LPC55xxx 的第二内核（second core）

**配置项引用（Symbol References）**：[`CONFIG_SECOND_CORE_MCUX`](P294_soc_nxp_配置项参考_2.md#CONFIG_SECOND_CORE_MCUX)、[`CONFIG_SOC_SERIES_LPC55XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC55XXX)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC55XXX`、`CONFIG_SOC_FAMILY_LPC`。

<a id="CONFIG_SECOND_CORE_MCUX"></a>

## 294.12 `CONFIG_SECOND_CORE_MCUX`

原库同名定义共 4 条；本项为数据库第 16594 条记录，各定义分别保留。

**提示（Prompt）**：LPC54114 Cortex-M0 第二内核（second core）

**说明（Help）**

第二内核启动驱动（Driver for second core startup）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_LPC54XXX && CONFIG_SOC_FAMILY_LPC
```

**定义位置（Location）**：[`soc/nxp/lpc/lpc54xxx/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/lpc/lpc54xxx/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_LPC54XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC54XXX)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC54XXX`、`CONFIG_SOC_FAMILY_LPC`。

<a id="CONFIG_SECOND_CORE_MCUX--record-16595"></a>

## 294.13 `CONFIG_SECOND_CORE_MCUX`

原库同名定义共 4 条；本项为数据库第 16595 条记录，各定义分别保留。

**提示（Prompt）**：LPC55xxx 的第二内核（second core）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_LPC55XXX && CONFIG_SOC_FAMILY_LPC
```

**定义位置（Location）**：[`soc/nxp/lpc/lpc55xxx/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/lpc/lpc55xxx/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_LPC55XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC55XXX)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC55XXX`、`CONFIG_SOC_FAMILY_LPC`。

<a id="CONFIG_SECOND_CORE_MCUX--record-16596"></a>

## 294.14 `CONFIG_SECOND_CORE_MCUX`

原库同名定义共 4 条；本项为数据库第 16596 条记录，各定义分别保留。

**提示（Prompt）**：MCXNX4X 的第二内核（second core）

**说明（Help）**

表示将启用第二内核，器件会运行在双核模式（dual core mode）中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX && (CONFIG_SOC_MCXN947 || CONFIG_SOC_MCXN547) && CONFIG_SOC_FAMILY_MCXN
```

**主动选择（Selects）**

```text
CONFIG_SOC_LATE_INIT_HOOK if CONFIG_SOC_MCXN947_CPU0 || CONFIG_SOC_MCXN547_CPU0
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxn/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxn/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_SOC_MCXN947`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947)、[`CONFIG_SOC_MCXN547`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)、[`CONFIG_SOC_LATE_INIT_HOOK`](P002_kernel_配置项参考_2.md#CONFIG_SOC_LATE_INIT_HOOK)、[`CONFIG_SOC_MCXN947_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN947_CPU0)、[`CONFIG_SOC_MCXN547_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXN547_CPU0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`、`CONFIG_SOC_MCXN947`、`CONFIG_SOC_MCXN547`、`CONFIG_SOC_FAMILY_MCXN`、`CONFIG_SOC_MCXN947_CPU0`、`CONFIG_SOC_MCXN547_CPU0`。

<a id="CONFIG_SECOND_CORE_MCUX--record-16597"></a>

## 294.15 `CONFIG_SECOND_CORE_MCUX`

原库同名定义共 4 条；本项为数据库第 16597 条记录，各定义分别保留。

**提示（Prompt）**：RT 多核系列的双核运行（Dual core operation）

**说明（Help）**

表示将启用第二内核，器件会运行在双核模式（dual core mode）中。主内核（primary core）启动针对辅助内核（secondary core）的镜像。第二内核镜像根据生成的头部从 Flash 加载到 RAM；该头部指定每个待加载内存节的虚拟内存地址（VMA）和加载内存地址（LMA）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_IMXRT11XX || CONFIG_SOC_SERIES_IMXRT7XX || (CONFIG_SOC_SERIES_IMXRT118X && !CONFIG_SOC_MIMXRT1182 && !CONFIG_SOC_MIMXRT1181)) && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_SERIES_IMXRT7XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT7XX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_MIMXRT1182`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1182)、[`CONFIG_SOC_MIMXRT1181`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1181)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_SERIES_IMXRT7XX`、`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_MIMXRT1182`、`CONFIG_SOC_MIMXRT1181`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SECOND_CORE_MCUX_ACCESS_LEVEL"></a>

## 294.16 `CONFIG_SECOND_CORE_MCUX_ACCESS_LEVEL`

**提示（Prompt）**：辅助内核的默认 TrustZone 访问级别（default access level）

**说明（Help）**

在启用 cpu1 之前，为它配置 AHBSC 的 `MASTER_SEC_LEVEL` 寄存器。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SECOND_CORE_MCUX && CONFIG_SOC_FAMILY_MCXN
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxn/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxn/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SECOND_CORE_MCUX`](P294_soc_nxp_配置项参考_2.md#CONFIG_SECOND_CORE_MCUX)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MCXN`。

<a id="CONFIG_SECOND_CORE_MCUX_REMOTE_DIR"></a>

## 294.17 `CONFIG_SECOND_CORE_MCUX_REMOTE_DIR`

**提示（Prompt）**：包含第二内核输出镜像头部的目录（output image header directory）

**说明（Help）**

设置远端目录（remote directory），在启动第二内核镜像时从中包含输出镜像头部数据。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SECOND_CORE_MCUX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → RT 多核系列的双核运行（Dual core operation）

**配置项引用（Symbol References）**：[`CONFIG_SECOND_CORE_MCUX`](P294_soc_nxp_配置项参考_2.md#CONFIG_SECOND_CORE_MCUX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SOC_FAMILY_MCXA_DEBUG_IN_LOW_POWER"></a>

## 294.18 `CONFIG_SOC_FAMILY_MCXA_DEBUG_IN_LOW_POWER`

**提示（Prompt）**：在低功耗模式中保持调试逻辑启用（debug logic enabled）

**说明（Help）**

内核处于低功耗模式时，保持调试逻辑工作，清除 CMC 的 `DBGCTL[SOD]`，使调试探针（debug probe）在挂起和恢复过程中保持连接；代价是低功耗电流增加。设为 `n` 会在进入低功耗状态时关闭调试逻辑。此后，挂起的目标设备在不复位的情况下无法再暂停、检查或重新烧录。对于关闭整个内核电源域的模式，例如深度掉电（Deep Power Down），无论此选项如何设置，调试逻辑都会断电。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && CONFIG_SOC_FAMILY_MCXA
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxa/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxa/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_FAMILY_MCXA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MCXA`。

<a id="CONFIG_SOC_FAMILY_MCXN_DEBUG_IN_LOW_POWER"></a>

## 294.19 `CONFIG_SOC_FAMILY_MCXN_DEBUG_IN_LOW_POWER`

**提示（Prompt）**：在低功耗模式中保持调试逻辑启用（debug logic enabled）

**说明（Help）**

内核处于低功耗模式时，保持调试逻辑工作，清除 CMC 的 `DBGCTL[SOD]`，使调试探针（debug probe）在挂起和恢复过程中保持连接；代价是低功耗电流增加。设为 `n` 会在进入低功耗状态时关闭调试逻辑。此后，挂起的目标设备在不复位的情况下无法再暂停、检查或重新烧录。对于关闭整个内核电源域的模式，例如深度掉电（Deep Power Down），无论此选项如何设置，调试逻辑都会断电。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && CONFIG_SOC_FAMILY_MCXN
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxn/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxn/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MCXN`。

<a id="CONFIG_SOC_IMX943_PM_MCORE"></a>

## 294.20 `CONFIG_SOC_IMX943_PM_MCORE`

**提示（Prompt）**：i.MX943 多核电源管理共享逻辑（multi-core PM shared logic）

**说明（Help）**

i.MX943 上 Cortex-M 内核（M33／M7）的公共电源管理流程（Common PM flow）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && (CONFIG_SOC_MIMX94398_M33 || CONFIG_SOC_MIMX94398_M7_0 || CONFIG_SOC_MIMX94398_M7_1) && CONFIG_NXP_SCMI_CPU_DOMAIN_HELPERS && CONFIG_SOC_SERIES_IMX9 && CONFIG_SOC_FAMILY_NXP_IMX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx943/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx943/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_MIMX94398_M33`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX94398_M33)、[`CONFIG_SOC_MIMX94398_M7_0`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX94398_M7_0)、[`CONFIG_SOC_MIMX94398_M7_1`](P294_soc_nxp_配置项参考_2.md#CONFIG_SOC_MIMX94398_M7_1)、[`CONFIG_NXP_SCMI_CPU_DOMAIN_HELPERS`](P091_drivers_firmware_配置项参考.md#CONFIG_NXP_SCMI_CPU_DOMAIN_HELPERS)、[`CONFIG_SOC_SERIES_IMX9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX9)、[`CONFIG_SOC_FAMILY_NXP_IMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMX9`、`CONFIG_SOC_FAMILY_NXP_IMX`。

<a id="CONFIG_SOC_IMXRT118X_SECOND_CORE_KICKOFF"></a>

## 294.21 `CONFIG_SOC_IMXRT118X_SECOND_CORE_KICKOFF`

**提示（Prompt）**：RT11xx 系列第二内核启动（Second core kickoff）

**说明（Help）**

表示主内核会在其系统初始化期间启动第二内核。否则，可在之后由应用层独立启动辅助内核（secondary core）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SECOND_CORE_MCUX && CONFIG_SOC_SERIES_IMXRT118X && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → RT 多核系列的双核运行（Dual core operation）

**配置项引用（Symbol References）**：[`CONFIG_SECOND_CORE_MCUX`](P294_soc_nxp_配置项参考_2.md#CONFIG_SECOND_CORE_MCUX)、[`CONFIG_SOC_SERIES_IMXRT118X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT118X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT118X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SOC_IMXRT11XX_SINGLE_CORE"></a>

## 294.22 `CONFIG_SOC_IMXRT11XX_SINGLE_CORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由集成单个 Cortex-M7 内核的 i.MX RT11xx SoC 选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT1151
CONFIG_SOC_MIMXRT1152
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt11xx/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT1151`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1151)、[`CONFIG_SOC_MIMXRT1152`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT1152)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT1151`、`CONFIG_SOC_MIMXRT1152`。

<a id="CONFIG_SOC_IMXRT7XX_POWEROFF_DPD"></a>

## 294.23 `CONFIG_SOC_IMXRT7XX_POWEROFF_DPD`

**提示（Prompt）**：深度掉电（Deep Power Down，DPD）

**说明（Help）**

`sys_poweroff()` 进入深度掉电模式（Deep Power Down）：除 VDD1V8_AON 和 VDD1V8_PMC 电源域外，整个芯片断电。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/cm33/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/cm33/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 系统关机模式（System power-off，sys_poweroff）

<a id="CONFIG_SOC_IMXRT7XX_POWEROFF_FDPD"></a>

## 294.24 `CONFIG_SOC_IMXRT7XX_POWEROFF_FDPD`

**提示（Prompt）**：完全深度掉电（Full Deep Power Down，FDPD）

**说明（Help）**

`sys_poweroff()` 进入完全深度掉电模式（Full Deep Power Down），仅 VDD1V8_AON 保持供电。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/cm33/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/cm33/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 系统关机模式（System power-off，sys_poweroff）

<a id="CONFIG_SOC_IMXRT7XX_POWER_DOMAIN_COMPUTE"></a>

## 294.25 `CONFIG_SOC_IMXRT7XX_POWER_DOMAIN_COMPUTE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为处于 RT7xx 计算电源域（Compute power domain）内的内核构建时选择。此域由 PMC0／SLEEPCON0 控制，覆盖 Common、Compute、Media 三类电源轨（rails）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT7XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT798S_CM33_CPU0
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/cm33/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/cm33/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT7XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT7XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT7XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`、`CONFIG_SOC_MIMXRT798S_CM33_CPU0`。

<a id="CONFIG_SOC_IMXRT7XX_POWER_DOMAIN_SENSE"></a>

## 294.26 `CONFIG_SOC_IMXRT7XX_POWER_DOMAIN_SENSE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为处于 RT7xx 感知电源域（Sense power domain）内的内核构建时选择。此域由 PMC1／SLEEPCON1 控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT7XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**被选择（Selected by）**

```text
CONFIG_SOC_MIMXRT798S_CM33_CPU1
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/cm33/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/cm33/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT7XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT7XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_SOC_MIMXRT798S_CM33_CPU1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S_CM33_CPU1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT7XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`、`CONFIG_SOC_MIMXRT798S_CM33_CPU1`。

<a id="CONFIG_SOC_LS1046A"></a>

## 294.27 `CONFIG_SOC_LS1046A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP Layerscape ls1046a 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_LS1046A
```

**被选择（Selected by）**

```text
CONFIG_BOARD_LS1046ARDB
```

**定义位置（Location）**：[`soc/nxp/layerscape/ls1046a/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/layerscape/ls1046a/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_LS1046A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LS1046A)、[`CONFIG_BOARD_LS1046ARDB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_LS1046ARDB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LS1046A`、`CONFIG_BOARD_LS1046ARDB`。

<a id="CONFIG_SOC_MCIMX6X_M4"></a>

## 294.28 `CONFIG_SOC_MCIMX6X_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP iMX6 SoloX M4 内核（core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MCIMX6X
```

**被选择（Selected by）**

```text
CONFIG_BOARD_UDOO_NEO_FULL
```

**定义位置（Location）**：[`soc/nxp/imx/imx6sx/Kconfig.soc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx6sx/Kconfig.soc#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MCIMX6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCIMX6X)、[`CONFIG_BOARD_UDOO_NEO_FULL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UDOO_NEO_FULL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MCIMX6X`、`CONFIG_BOARD_UDOO_NEO_FULL`。

<a id="CONFIG_SOC_MCIMX7D_M4"></a>

## 294.29 `CONFIG_SOC_MCIMX7D_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP iMX7 Dual M4 内核（Core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MCIMX7D
```

**被选择（Selected by）**

```text
CONFIG_BOARD_COLIBRI_IMX7D
CONFIG_BOARD_WARP7
CONFIG_BOARD_PICO_PI
CONFIG_BOARD_96B_MEERKAT96
```

**定义位置（Location）**：[`soc/nxp/imx/imx7d/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx7d/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MCIMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCIMX7D)、[`CONFIG_BOARD_COLIBRI_IMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_COLIBRI_IMX7D)、[`CONFIG_BOARD_WARP7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WARP7)、[`CONFIG_BOARD_PICO_PI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_PICO_PI)、[`CONFIG_BOARD_96B_MEERKAT96`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_96B_MEERKAT96)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MCIMX7D`、`CONFIG_BOARD_COLIBRI_IMX7D`、`CONFIG_BOARD_WARP7`、`CONFIG_BOARD_PICO_PI`、`CONFIG_BOARD_96B_MEERKAT96`。

<a id="CONFIG_SOC_MIMX8ML8_A53"></a>

## 294.30 `CONFIG_SOC_MIMX8ML8_A53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX8MP A53 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX8ML8
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX8MP_EVK
CONFIG_BOARD_IMX8MP_VAR_DART
CONFIG_BOARD_IMX8MP_VAR_SOM
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX8ML8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8)、[`CONFIG_BOARD_IMX8MP_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8MP_EVK)、[`CONFIG_BOARD_IMX8MP_VAR_DART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8MP_VAR_DART)、[`CONFIG_BOARD_IMX8MP_VAR_SOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8MP_VAR_SOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX8ML8`、`CONFIG_BOARD_IMX8MP_EVK`、`CONFIG_BOARD_IMX8MP_VAR_DART`、`CONFIG_BOARD_IMX8MP_VAR_SOM`。

<a id="CONFIG_SOC_MIMX8ML8_ADSP"></a>

## 294.31 `CONFIG_SOC_MIMX8ML8_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NXP i.MX 8MPLUS 音频数字信号处理器（Audio DSP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX8ML8
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX8MP_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX8ML8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8)、[`CONFIG_BOARD_IMX8MP_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8MP_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX8ML8`、`CONFIG_BOARD_IMX8MP_EVK`。

<a id="CONFIG_SOC_MIMX8ML8_M7"></a>

## 294.32 `CONFIG_SOC_MIMX8ML8_M7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NXP i.MX 8MPLUS M7 微控制器（MCU）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX8ML8
```

**被选择（Selected by）**

```text
CONFIG_BOARD_VERDIN_IMX8MP
CONFIG_BOARD_IMX8MP_EVK
CONFIG_BOARD_PHYBOARD_POLLUX
CONFIG_BOARD_IMX8MP_VAR_DART
CONFIG_BOARD_IMX8MP_VAR_SOM
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX8ML8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8)、[`CONFIG_BOARD_VERDIN_IMX8MP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_VERDIN_IMX8MP)、[`CONFIG_BOARD_IMX8MP_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8MP_EVK)、[`CONFIG_BOARD_PHYBOARD_POLLUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_PHYBOARD_POLLUX)、[`CONFIG_BOARD_IMX8MP_VAR_DART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8MP_VAR_DART)、[`CONFIG_BOARD_IMX8MP_VAR_SOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8MP_VAR_SOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX8ML8`、`CONFIG_BOARD_VERDIN_IMX8MP`、`CONFIG_BOARD_IMX8MP_EVK`、`CONFIG_BOARD_PHYBOARD_POLLUX`、`CONFIG_BOARD_IMX8MP_VAR_DART`、`CONFIG_BOARD_IMX8MP_VAR_SOM`。

<a id="CONFIG_SOC_MIMX8MM6_A53"></a>

## 294.33 `CONFIG_SOC_MIMX8MM6_A53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX8MM A53 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX8MM6
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX8MM_EVK
CONFIG_BOARD_PHYBOARD_POLIS
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX8MM6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6)、[`CONFIG_BOARD_IMX8MM_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8MM_EVK)、[`CONFIG_BOARD_PHYBOARD_POLIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_PHYBOARD_POLIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX8MM6`、`CONFIG_BOARD_IMX8MM_EVK`、`CONFIG_BOARD_PHYBOARD_POLIS`。

<a id="CONFIG_SOC_MIMX8MM6_M4"></a>

## 294.34 `CONFIG_SOC_MIMX8MM6_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX8MM M4 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX8MM6
```

**被选择（Selected by）**

```text
CONFIG_BOARD_VERDIN_IMX8MM
CONFIG_BOARD_IMX8MM_EVK
CONFIG_BOARD_PHYBOARD_POLIS
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX8MM6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6)、[`CONFIG_BOARD_VERDIN_IMX8MM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_VERDIN_IMX8MM)、[`CONFIG_BOARD_IMX8MM_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8MM_EVK)、[`CONFIG_BOARD_PHYBOARD_POLIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_PHYBOARD_POLIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX8MM6`、`CONFIG_BOARD_VERDIN_IMX8MM`、`CONFIG_BOARD_IMX8MM_EVK`、`CONFIG_BOARD_PHYBOARD_POLIS`。

<a id="CONFIG_SOC_MIMX8MN6_A53"></a>

## 294.35 `CONFIG_SOC_MIMX8MN6_A53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX8MN A53 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX8MN6
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX8MN_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX8MN6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MN6)、[`CONFIG_BOARD_IMX8MN_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8MN_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX8MN6`、`CONFIG_BOARD_IMX8MN_EVK`。

<a id="CONFIG_SOC_MIMX8MQ6_M4"></a>

## 294.36 `CONFIG_SOC_MIMX8MQ6_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NXP i.MX 8M Quad M4 微控制器（MCU）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX8MQ6
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX8MQ_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX8MQ6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MQ6)、[`CONFIG_BOARD_IMX8MQ_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8MQ_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX8MQ6`、`CONFIG_BOARD_IMX8MQ_EVK`。

<a id="CONFIG_SOC_MIMX8QM6_ADSP"></a>

## 294.37 `CONFIG_SOC_MIMX8QM6_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NXP i.MX 8QM 音频数字信号处理器（Audio DSP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX8QM6
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX8QM_MEK
```

**定义位置（Location）**：[`soc/nxp/imx/imx8/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX8QM6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QM6)、[`CONFIG_BOARD_IMX8QM_MEK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8QM_MEK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX8QM6`、`CONFIG_BOARD_IMX8QM_MEK`。

<a id="CONFIG_SOC_MIMX8QX6_ADSP"></a>

## 294.38 `CONFIG_SOC_MIMX8QX6_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NXP i.MX 8QXP 音频数字信号处理器（Audio DSP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX8QX6
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX8QXP_MEK
```

**定义位置（Location）**：[`soc/nxp/imx/imx8x/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8x/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX8QX6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8QX6)、[`CONFIG_BOARD_IMX8QXP_MEK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8QXP_MEK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX8QX6`、`CONFIG_BOARD_IMX8QXP_MEK`。

<a id="CONFIG_SOC_MIMX8UD7_ADSP"></a>

## 294.39 `CONFIG_SOC_MIMX8UD7_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NXP i.MX 8ULP 音频数字信号处理器（Audio DSP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX8UD7
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX8ULP_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx8ulp/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8ulp/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX8UD7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8UD7)、[`CONFIG_BOARD_IMX8ULP_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX8ULP_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX8UD7`、`CONFIG_BOARD_IMX8ULP_EVK`。

<a id="CONFIG_SOC_MIMX9111"></a>

## 294.40 `CONFIG_SOC_MIMX9111`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX91 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_IMX9
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX91_QSB
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx91/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx91/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMX9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX9)、[`CONFIG_BOARD_IMX91_QSB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX91_QSB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMX9`、`CONFIG_BOARD_IMX91_QSB`。

<a id="CONFIG_SOC_MIMX9131"></a>

## 294.41 `CONFIG_SOC_MIMX9131`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX91 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_IMX9
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX91_EVK
CONFIG_BOARD_FRDM_IMX91
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx91/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx91/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMX9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMX9)、[`CONFIG_BOARD_IMX91_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX91_EVK)、[`CONFIG_BOARD_FRDM_IMX91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_FRDM_IMX91)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMX9`、`CONFIG_BOARD_IMX91_EVK`、`CONFIG_BOARD_FRDM_IMX91`。

<a id="CONFIG_SOC_MIMX9352_A55"></a>

## 294.42 `CONFIG_SOC_MIMX9352_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX93 A55 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX9352
```

**被选择（Selected by）**

```text
CONFIG_BOARD_FRDM_IMX93
CONFIG_BOARD_IMX93_EVK
CONFIG_BOARD_PHYBOARD_NASH
CONFIG_BOARD_IMX93_VAR_DART
CONFIG_BOARD_IMX93_VAR_SOM
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx93/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx93/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX9352`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352)、[`CONFIG_BOARD_FRDM_IMX93`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_FRDM_IMX93)、[`CONFIG_BOARD_IMX93_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX93_EVK)、[`CONFIG_BOARD_PHYBOARD_NASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_PHYBOARD_NASH)、[`CONFIG_BOARD_IMX93_VAR_DART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX93_VAR_DART)、[`CONFIG_BOARD_IMX93_VAR_SOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX93_VAR_SOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX9352`、`CONFIG_BOARD_FRDM_IMX93`、`CONFIG_BOARD_IMX93_EVK`、`CONFIG_BOARD_PHYBOARD_NASH`、`CONFIG_BOARD_IMX93_VAR_DART`、`CONFIG_BOARD_IMX93_VAR_SOM`。

<a id="CONFIG_SOC_MIMX9352_M33"></a>

## 294.43 `CONFIG_SOC_MIMX9352_M33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX93 M33 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX9352
```

**被选择（Selected by）**

```text
CONFIG_BOARD_FRDM_IMX93
CONFIG_BOARD_IMX93_EVK
CONFIG_BOARD_PHYBOARD_NASH
CONFIG_BOARD_IMX93_VAR_DART
CONFIG_BOARD_IMX93_VAR_SOM
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx93/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx93/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX9352`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352)、[`CONFIG_BOARD_FRDM_IMX93`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_FRDM_IMX93)、[`CONFIG_BOARD_IMX93_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX93_EVK)、[`CONFIG_BOARD_PHYBOARD_NASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_PHYBOARD_NASH)、[`CONFIG_BOARD_IMX93_VAR_DART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX93_VAR_DART)、[`CONFIG_BOARD_IMX93_VAR_SOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX93_VAR_SOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX9352`、`CONFIG_BOARD_FRDM_IMX93`、`CONFIG_BOARD_IMX93_EVK`、`CONFIG_BOARD_PHYBOARD_NASH`、`CONFIG_BOARD_IMX93_VAR_DART`、`CONFIG_BOARD_IMX93_VAR_SOM`。

<a id="CONFIG_SOC_MIMX94398_A55"></a>

## 294.44 `CONFIG_SOC_MIMX94398_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX943 A55 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX94398
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX943_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx943/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx943/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX94398`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398)、[`CONFIG_BOARD_IMX943_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX943_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX94398`、`CONFIG_BOARD_IMX943_EVK`。

<a id="CONFIG_SOC_MIMX94398_M33"></a>

## 294.45 `CONFIG_SOC_MIMX94398_M33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX943 的 NETC MIX 中的 Cortex-M33 内核 1（Core1）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX94398
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX943_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx943/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx943/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX94398`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398)、[`CONFIG_BOARD_IMX943_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX943_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX94398`、`CONFIG_BOARD_IMX943_EVK`。

<a id="CONFIG_SOC_MIMX94398_M7_0"></a>

## 294.46 `CONFIG_SOC_MIMX94398_M7_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX943 的 M7MIX0 中的 Cortex-M7 内核 0（Core0）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX94398
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX943_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx943/Kconfig.soc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx943/Kconfig.soc#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX94398`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398)、[`CONFIG_BOARD_IMX943_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX943_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX94398`、`CONFIG_BOARD_IMX943_EVK`。

<a id="CONFIG_SOC_MIMX94398_M7_1"></a>

## 294.47 `CONFIG_SOC_MIMX94398_M7_1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX943 的 M7MIX1 中的 Cortex-M7 内核 1（Core1）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX94398
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX943_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx943/Kconfig.soc:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx943/Kconfig.soc#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX94398`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398)、[`CONFIG_BOARD_IMX943_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX943_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX94398`、`CONFIG_BOARD_IMX943_EVK`。

<a id="CONFIG_SOC_MIMX9529_A55"></a>

## 294.48 `CONFIG_SOC_MIMX9529_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX952 A55 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX9529
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX952_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx952/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx952/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX9529`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529)、[`CONFIG_BOARD_IMX952_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX952_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX9529`、`CONFIG_BOARD_IMX952_EVK`。

<a id="CONFIG_SOC_MIMX9529_M7"></a>

## 294.49 `CONFIG_SOC_MIMX9529_M7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX952 M7 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX9529
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX952_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx952/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx952/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX9529`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529)、[`CONFIG_BOARD_IMX952_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX952_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX9529`、`CONFIG_BOARD_IMX952_EVK`。

<a id="CONFIG_SOC_MIMX9596_A55"></a>

## 294.50 `CONFIG_SOC_MIMX9596_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX95 A55 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX9596
```

**被选择（Selected by）**

```text
CONFIG_BOARD_IMX95_EVK_15X15
CONFIG_BOARD_IMX95_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx95/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx95/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX9596`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596)、[`CONFIG_BOARD_IMX95_EVK_15X15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX95_EVK_15X15)、[`CONFIG_BOARD_IMX95_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX95_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX9596`、`CONFIG_BOARD_IMX95_EVK_15X15`、`CONFIG_BOARD_IMX95_EVK`。

<a id="CONFIG_SOC_MIMX9596_M7"></a>

## 294.51 `CONFIG_SOC_MIMX9596_M7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX95 M7 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMX9596
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MR_NAVQ95B
CONFIG_BOARD_IMX95_EVK_15X15
CONFIG_BOARD_IMX95_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx95/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx95/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMX9596`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596)、[`CONFIG_BOARD_MR_NAVQ95B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MR_NAVQ95B)、[`CONFIG_BOARD_IMX95_EVK_15X15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX95_EVK_15X15)、[`CONFIG_BOARD_IMX95_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IMX95_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMX9596`、`CONFIG_BOARD_MR_NAVQ95B`、`CONFIG_BOARD_IMX95_EVK_15X15`、`CONFIG_BOARD_IMX95_EVK`。

<a id="CONFIG_SOC_MIMXRT595S_CM33"></a>

## 294.52 `CONFIG_SOC_MIMXRT595S_CM33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP RT5xx CM33 内核（core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMXRT595S
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MIMXRT595_EVK
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt5xx/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt5xx/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT595S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S)、[`CONFIG_BOARD_MIMXRT595_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MIMXRT595_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT595S`、`CONFIG_BOARD_MIMXRT595_EVK`。

<a id="CONFIG_SOC_MIMXRT595S_F1"></a>

## 294.53 `CONFIG_SOC_MIMXRT595S_F1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP RT5xx 音频 DSP 系列（ADSP Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMXRT595S
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MIMXRT595_EVK
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt5xx/Kconfig.soc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt5xx/Kconfig.soc#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT595S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT595S)、[`CONFIG_BOARD_MIMXRT595_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MIMXRT595_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT595S`、`CONFIG_BOARD_MIMXRT595_EVK`。

<a id="CONFIG_SOC_MIMXRT735S_HIFI1"></a>

## 294.54 `CONFIG_SOC_MIMXRT735S_HIFI1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MXRT7xx HiFi1 DSP 内核（Core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMXRT735S
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/Kconfig.soc:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/Kconfig.soc#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT735S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT735S)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT735S`。

<a id="CONFIG_SOC_MIMXRT758S_HIFI1"></a>

## 294.55 `CONFIG_SOC_MIMXRT758S_HIFI1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MXRT7xx HiFi1 DSP 内核（Core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMXRT758S
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/Kconfig.soc:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/Kconfig.soc#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT758S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT758S)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT758S`。

<a id="CONFIG_SOC_MIMXRT798S_HIFI1"></a>

## 294.56 `CONFIG_SOC_MIMXRT798S_HIFI1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MXRT7xx HiFi1 DSP 内核（Core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMXRT798S
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MIMXRT700_EVK
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/Kconfig.soc:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/Kconfig.soc#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT798S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S)、[`CONFIG_BOARD_MIMXRT700_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MIMXRT700_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT798S`、`CONFIG_BOARD_MIMXRT700_EVK`。

<a id="CONFIG_SOC_MIMXRT798S_HIFI4"></a>

## 294.57 `CONFIG_SOC_MIMXRT798S_HIFI4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MXRT7xx HiFi4 DSP 内核（Core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_MIMXRT798S
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MIMXRT700_EVK
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/Kconfig.soc:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/Kconfig.soc#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT798S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT798S)、[`CONFIG_BOARD_MIMXRT700_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MIMXRT700_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT798S`、`CONFIG_BOARD_MIMXRT700_EVK`。

<a id="CONFIG_SOC_MIMXRT7XX_PM_XIP_HANDOVER"></a>

## 294.58 `CONFIG_SOC_MIMXRT7XX_PM_XIP_HANDOVER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部配置，不是用户选项：编入原地执行（XIP）的挂起／恢复辅助函数，并从进入低功耗的路径调用。执行 XIP 代码时进入深度睡眠／DSR，必须在相关电源域断电前使 XSPI 控制器及其缓存停止活动，并在之后重新启用。对于同时启用电源管理（PM）与 XIP（`FLASH_MCUX_XSPI_XIP`）的构建，此项自动启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && CONFIG_SOC_SERIES_IMXRT7XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
y if CONFIG_FLASH_MCUX_XSPI_XIP
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt7xx/cm33/Kconfig:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt7xx/cm33/Kconfig#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_SERIES_IMXRT7XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT7XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_FLASH_MCUX_XSPI_XIP`](P293_soc_nxp_配置项参考_1.md#CONFIG_FLASH_MCUX_XSPI_XIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT7XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SOC_NXP_MCXE31X_BOOT_HEADER"></a>

## 294.59 `CONFIG_SOC_NXP_MCXE31X_BOOT_HEADER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 NXP MCXE31X SoC 启用启动头部配置（boot header configuration）。需要启动头部支持的开发板应选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_MCXE31X && CONFIG_SOC_FAMILY_MCXE
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxe/mcxe31x/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxe/mcxe31x/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_FAMILY_MCXE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_FAMILY_MCXE`。

<a id="CONFIG_SOC_SERIES_IMX7D"></a>

## 294.60 `CONFIG_SOC_SERIES_IMX7D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 iMX7D 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_NXP_IMX
```

**被选择（Selected by）**

```text
CONFIG_SOC_MCIMX7D
```

**定义位置（Location）**：[`soc/nxp/imx/imx7d/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx7d/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_NXP_IMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMX)、[`CONFIG_SOC_MCIMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCIMX7D)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMX`、`CONFIG_SOC_MCIMX7D`。

<a id="CONFIG_SOC_SERIES_LPC54XXX_SRAM_CLOCKS"></a>

## 294.61 `CONFIG_SOC_SERIES_LPC54XXX_SRAM_CLOCKS`

**提示（Prompt）**：为 LPC54XXX SRAM 存储体提供时钟（Clock SRAM banks）

**说明（Help）**

复位后 SRAM 存储体（banks）处于禁用状态。默认情况下，CMSIS 的 `SystemInit` 会为这些 RAM 存储体启用时钟。禁用此 Kconfig 项，可以使其在复位后保持原状。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_LPC54XXX && CONFIG_SOC_FAMILY_LPC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/nxp/lpc/lpc54xxx/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/lpc/lpc54xxx/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_LPC54XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_LPC54XXX)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_LPC54XXX`、`CONFIG_SOC_FAMILY_LPC`。

<a id="CONFIG_SOC_SERIES_MCXW7XX_SHUTDOWN_UNUSED_RAM"></a>

## 294.62 `CONFIG_SOC_SERIES_MCXW7XX_SHUTDOWN_UNUSED_RAM`

**提示（Prompt）**：初始化时关闭未使用 SRAM 存储体的电源（Power off unused SRAM banks）

**说明（Help）**

在 SoC 电源初始化期间，通过 CMC 的 `SRAMDIS` 寄存器，在所有模式中持续关闭所有未与链接镜像所依赖的任何内存区域重叠、且受 CMC 控制的 SRAM 存储体（bank）。对于未使用全部 SRAM 的镜像，这会降低活动状态与低功耗状态的漏电。每个存储体的起始地址、大小和 CMC 禁用位来自设备树 `cmc` 节点的 `sram-banks` 属性。

若存储体与以下任意区域重叠，则保持供电：选定的 `zephyr,sram` 节点；在片上链接时选定的 `zephyr,flash` 节点；或任何已启用的 `zephyr,memory-region` 节点。因此，应用只需声明使用该存储体的区域，即可保持其供电，例如将保存关键数据的错误纠正码（ECC）区域声明为 `zephyr,memory-region`。此决策不使用链接器符号，所以不绑定到某一个链接器区域。

默认情况下，`zephyr,sram` 覆盖全部系统 SRAM，因此仅关闭其范围之外的存储体，例如常见 Flash 执行配置中的代码紧耦合内存（Code-TCM）存储体。若要释放系统 SRAM 存储体，可在开发板覆盖文件（overlay）中缩小 `zephyr,sram`，使未使用的高地址存储体落在其范围之外。禁用此选项时，不会编程 `SRAMDIS`，行为保持不变。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxw/mcxw7xx/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxw/mcxw7xx/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

<a id="CONFIG_SRAM_CONFIG_RELOCATE_MEM"></a>

## 294.63 `CONFIG_SRAM_CONFIG_RELOCATE_MEM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

选择用于重定位 sram_config.c 代码的内存（memory relocation）

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_CODE_DATA_RELOCATION && CONFIG_SOC_SERIES_MCXE31X && CONFIG_SOC_FAMILY_MCXE
```

**默认值（Defaults）**

```text
"ITCM"
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxe/mcxe31x/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxe/mcxe31x/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CODE_DATA_RELOCATION)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_FAMILY_MCXE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_FAMILY_MCXE`。

<a id="CONFIG_SYSOSC_SETTLING_US"></a>

## 294.64 `CONFIG_SYSOSC_SETTLING_US`

**提示（Prompt）**：系统振荡器稳定时间（System oscillator settling time）

**说明（Help）**

设置开发板系统振荡器的稳定时间（settling time），单位为微秒。应由开发板的 defconfig 设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_MIMXRT685S_CM33 && CONFIG_SOC_SERIES_IMXRT6XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt6xx/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt6xx/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_SERIES_IMXRT6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT6XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_SERIES_IMXRT6XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SYS_PLL2_PFD0_DIV"></a>

## 294.65 `CONFIG_SYS_PLL2_PFD0_DIV`

**提示（Prompt）**：系统锁相环 2 的相位分数分频器 0 分频值（System PLL2 PFD0 divider）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT11XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
27
```

**取值范围（Ranges）**

```text
[13, 35]
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt11xx/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SYS_PLL2_PFD1_DIV"></a>

## 294.66 `CONFIG_SYS_PLL2_PFD1_DIV`

**提示（Prompt）**：系统锁相环 2 的相位分数分频器 1 分频值（System PLL2 PFD1 divider）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT11XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[13, 35]
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt11xx/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SYS_PLL2_PFD2_DIV"></a>

## 294.67 `CONFIG_SYS_PLL2_PFD2_DIV`

**提示（Prompt）**：系统锁相环 2 的相位分数分频器 2 分频值（System PLL2 PFD2 divider）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT11XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
24
```

**取值范围（Ranges）**

```text
[13, 35]
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt11xx/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SYS_PLL2_PFD3_DIV"></a>

## 294.68 `CONFIG_SYS_PLL2_PFD3_DIV`

**提示（Prompt）**：系统锁相环 2 的相位分数分频器 3 分频值（System PLL2 PFD3 divider）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT11XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[13, 35]
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt11xx/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SYS_PLL3_PFD0_DIV"></a>

## 294.69 `CONFIG_SYS_PLL3_PFD0_DIV`

**提示（Prompt）**：系统锁相环 3 的相位分数分频器 0 分频值（System PLL3 PFD0 divider）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT11XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
13
```

**取值范围（Ranges）**

```text
[13, 35]
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt11xx/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SYS_PLL3_PFD1_DIV"></a>

## 294.70 `CONFIG_SYS_PLL3_PFD1_DIV`

**提示（Prompt）**：系统锁相环 3 的相位分数分频器 1 分频值（System PLL3 PFD1 divider）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT11XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
17
```

**取值范围（Ranges）**

```text
[13, 35]
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt11xx/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SYS_PLL3_PFD2_DIV"></a>

## 294.71 `CONFIG_SYS_PLL3_PFD2_DIV`

**提示（Prompt）**：系统锁相环 3 的相位分数分频器 2 分频值（System PLL3 PFD2 divider）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT11XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[13, 35]
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt11xx/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_SYS_PLL3_PFD3_DIV"></a>

## 294.72 `CONFIG_SYS_PLL3_PFD3_DIV`

**提示（Prompt）**：系统锁相环 3 的相位分数分频器 3 分频值（System PLL3 PFD3 divider）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_IMXRT11XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
22
```

**取值范围（Ranges）**

```text
[13, 35]
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt11xx/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_IMXRT11XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT11XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_IMXRT11XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_WDOG_ENABLE_AT_BOOT"></a>

## 294.73 `CONFIG_WDOG_ENABLE_AT_BOOT`

原库同名定义共 2 条；本项为数据库第 20939 条记录，各定义分别保留。

**提示（Prompt）**：启动时保持看门狗定时器启用（Keep watchdog timer enabled）

**说明（Help）**

启动时保持 SoC 看门狗定时器（watchdog timer）启用。启动时具体的超时和时钟配置由 SoC 决定。注意：若启动时启用了看门狗，用户需要使用 `z_arm_watchdog_init` 配置它，因为 SoC 要求在首次超时之前完成看门狗配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_MCXE24X && CONFIG_SOC_FAMILY_MCXE
```

**定义位置（Location）**：[`soc/nxp/mcx/mcxe/mcxe24x/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/mcx/mcxe/mcxe24x/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_MCXE24X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE24X)、[`CONFIG_SOC_FAMILY_MCXE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_MCXE24X`、`CONFIG_SOC_FAMILY_MCXE`。

<a id="CONFIG_WDOG_ENABLE_AT_BOOT--record-20940"></a>

## 294.74 `CONFIG_WDOG_ENABLE_AT_BOOT`

原库同名定义共 2 条；本项为数据库第 20940 条记录，各定义分别保留。

**提示（Prompt）**：启动时保持看门狗定时器启用（Keep watchdog timer enabled）

**说明（Help）**

启动时保持看门狗定时器（watchdog timer）启用，使用内部 128kHz 低功耗振荡器（LPO）时钟作为时钟源，并采用 256 的预分频值。应用可在启动后接管看门狗，并按需设置不同的超时时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_KE1XF && CONFIG_SOC_FAMILY_KINETIS
```

**定义位置（Location）**：[`soc/nxp/kinetis/ke1xf/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/ke1xf/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_WDOG_INITIAL_TIMEOUT"></a>

## 294.75 `CONFIG_WDOG_INITIAL_TIMEOUT`

**提示（Prompt）**：看门狗定时器初始超时，单位为毫秒（Initial timeout）

**说明（Help）**

看门狗定时器（watchdog timer）的初始超时值，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WDOG_ENABLE_AT_BOOT && CONFIG_WDOG_INIT && CONFIG_SOC_SERIES_KE1XF && CONFIG_SOC_FAMILY_KINETIS
```

**默认值（Defaults）**

```text
2048
```

**取值范围（Ranges）**

```text
[2, 131070]
```

**定义位置（Location）**：[`soc/nxp/kinetis/ke1xf/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/kinetis/ke1xf/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动时保持看门狗定时器启用（Keep watchdog timer enabled）

**配置项引用（Symbol References）**：[`CONFIG_WDOG_ENABLE_AT_BOOT`](P294_soc_nxp_配置项参考_2.md#CONFIG_WDOG_ENABLE_AT_BOOT)、[`CONFIG_WDOG_INIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDOG_INIT)、[`CONFIG_SOC_SERIES_KE1XF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_KE1XF)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WDOG_INIT`、`CONFIG_SOC_SERIES_KE1XF`、`CONFIG_SOC_FAMILY_KINETIS`。

<a id="CONFIG_XSPI_CONFIG_BLOCK_OFFSET"></a>

## 294.76 `CONFIG_XSPI_CONFIG_BLOCK_OFFSET`

**提示（Prompt）**：XSPI 配置块偏移（config block offset）

**说明（Help）**

XSPI 配置块（configuration block）由特定 Flash 器件的参数组成，包括读取命令序列、可选的四线模式启用序列（quad mode enablement sequence）等。启动 ROM（boot ROM）要求 XSPI 配置参数位于串行 NOR Flash 中。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOT_XSPI_NOR && CONFIG_NXP_IMXRT_BOOT_HEADER && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**默认值（Defaults）**

```text
0x0
```

**定义位置（Location）**：[`soc/nxp/imxrt/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 启动头部（Boot header）

**配置项引用（Symbol References）**：[`CONFIG_BOOT_XSPI_NOR`](P293_soc_nxp_配置项参考_1.md#CONFIG_BOOT_XSPI_NOR)、[`CONFIG_NXP_IMXRT_BOOT_HEADER`](P293_soc_nxp_配置项参考_1.md#CONFIG_NXP_IMXRT_BOOT_HEADER)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="CONFIG_XTAL_SYS_CLK_HZ"></a>

## 294.77 `CONFIG_XTAL_SYS_CLK_HZ`

**提示（Prompt）**：外部振荡器频率（External oscillator frequency）

**说明（Help）**

设置外部振荡器频率，单位为 Hz。应由开发板的 defconfig 设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_MIMXRT685S_CM33 && CONFIG_SOC_SERIES_IMXRT6XX && CONFIG_SOC_FAMILY_NXP_IMXRT
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt6xx/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt6xx/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_MIMXRT685S_CM33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMXRT685S_CM33)、[`CONFIG_SOC_SERIES_IMXRT6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_IMXRT6XX)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MIMXRT685S_CM33`、`CONFIG_SOC_SERIES_IMXRT6XX`、`CONFIG_SOC_FAMILY_NXP_IMXRT`。

<a id="SB_CONFIG_SOC_IMXRT11XX_SINGLE_CORE"></a>

## 294.78 `SB_CONFIG_SOC_IMXRT11XX_SINGLE_CORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由集成单个 Cortex-M7 内核的 i.MX RT11xx SoC 选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_SOC_MIMXRT1151
SB_CONFIG_SOC_MIMXRT1152
```

**定义位置（Location）**：[`soc/nxp/imxrt/imxrt11xx/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMXRT1151`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMXRT1151)、[`SB_CONFIG_SOC_MIMXRT1152`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMXRT1152)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMXRT1151`、`SB_CONFIG_SOC_MIMXRT1152`。

<a id="SB_CONFIG_SOC_LS1046A"></a>

## 294.79 `SB_CONFIG_SOC_LS1046A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP Layerscape ls1046a 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_LS1046A
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_LS1046ARDB
```

**定义位置（Location）**：[`soc/nxp/layerscape/ls1046a/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/layerscape/ls1046a/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_LS1046A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_LS1046A)、[`SB_CONFIG_BOARD_LS1046ARDB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_LS1046ARDB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_LS1046A`、`SB_CONFIG_BOARD_LS1046ARDB`。

<a id="SB_CONFIG_SOC_MCIMX6X_M4"></a>

## 294.80 `SB_CONFIG_SOC_MCIMX6X_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP iMX6 SoloX M4 内核（core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MCIMX6X
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_UDOO_NEO_FULL
```

**定义位置（Location）**：[`soc/nxp/imx/imx6sx/Kconfig.soc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx6sx/Kconfig.soc#L15)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MCIMX6X`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MCIMX6X)、[`SB_CONFIG_BOARD_UDOO_NEO_FULL`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UDOO_NEO_FULL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MCIMX6X`、`SB_CONFIG_BOARD_UDOO_NEO_FULL`。

<a id="SB_CONFIG_SOC_MCIMX7D_M4"></a>

## 294.81 `SB_CONFIG_SOC_MCIMX7D_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP iMX7 Dual M4 内核（Core）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MCIMX7D
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_COLIBRI_IMX7D
SB_CONFIG_BOARD_WARP7
SB_CONFIG_BOARD_PICO_PI
SB_CONFIG_BOARD_96B_MEERKAT96
```

**定义位置（Location）**：[`soc/nxp/imx/imx7d/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx7d/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MCIMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MCIMX7D)、[`SB_CONFIG_BOARD_COLIBRI_IMX7D`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_COLIBRI_IMX7D)、[`SB_CONFIG_BOARD_WARP7`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WARP7)、[`SB_CONFIG_BOARD_PICO_PI`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_PICO_PI)、[`SB_CONFIG_BOARD_96B_MEERKAT96`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_96B_MEERKAT96)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MCIMX7D`、`SB_CONFIG_BOARD_COLIBRI_IMX7D`、`SB_CONFIG_BOARD_WARP7`、`SB_CONFIG_BOARD_PICO_PI`、`SB_CONFIG_BOARD_96B_MEERKAT96`。

<a id="SB_CONFIG_SOC_MIMX8ML8_A53"></a>

## 294.82 `SB_CONFIG_SOC_MIMX8ML8_A53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX8MP A53 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX8ML8
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX8MP_EVK
SB_CONFIG_BOARD_IMX8MP_VAR_DART
SB_CONFIG_BOARD_IMX8MP_VAR_SOM
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L31)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX8ML8`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX8ML8)、[`SB_CONFIG_BOARD_IMX8MP_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8MP_EVK)、[`SB_CONFIG_BOARD_IMX8MP_VAR_DART`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8MP_VAR_DART)、[`SB_CONFIG_BOARD_IMX8MP_VAR_SOM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8MP_VAR_SOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX8ML8`、`SB_CONFIG_BOARD_IMX8MP_EVK`、`SB_CONFIG_BOARD_IMX8MP_VAR_DART`、`SB_CONFIG_BOARD_IMX8MP_VAR_SOM`。

<a id="SB_CONFIG_SOC_MIMX8ML8_ADSP"></a>

## 294.83 `SB_CONFIG_SOC_MIMX8ML8_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NXP i.MX 8MPLUS 音频数字信号处理器（Audio DSP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX8ML8
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX8MP_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L37)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX8ML8`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX8ML8)、[`SB_CONFIG_BOARD_IMX8MP_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8MP_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX8ML8`、`SB_CONFIG_BOARD_IMX8MP_EVK`。

<a id="SB_CONFIG_SOC_MIMX8ML8_M7"></a>

## 294.84 `SB_CONFIG_SOC_MIMX8ML8_M7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NXP i.MX 8MPLUS M7 微控制器（MCU）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX8ML8
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_VERDIN_IMX8MP
SB_CONFIG_BOARD_IMX8MP_EVK
SB_CONFIG_BOARD_PHYBOARD_POLLUX
SB_CONFIG_BOARD_IMX8MP_VAR_DART
SB_CONFIG_BOARD_IMX8MP_VAR_SOM
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L43)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX8ML8`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX8ML8)、[`SB_CONFIG_BOARD_VERDIN_IMX8MP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_VERDIN_IMX8MP)、[`SB_CONFIG_BOARD_IMX8MP_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8MP_EVK)、[`SB_CONFIG_BOARD_PHYBOARD_POLLUX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_PHYBOARD_POLLUX)、[`SB_CONFIG_BOARD_IMX8MP_VAR_DART`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8MP_VAR_DART)、[`SB_CONFIG_BOARD_IMX8MP_VAR_SOM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8MP_VAR_SOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX8ML8`、`SB_CONFIG_BOARD_VERDIN_IMX8MP`、`SB_CONFIG_BOARD_IMX8MP_EVK`、`SB_CONFIG_BOARD_PHYBOARD_POLLUX`、`SB_CONFIG_BOARD_IMX8MP_VAR_DART`、`SB_CONFIG_BOARD_IMX8MP_VAR_SOM`。

<a id="SB_CONFIG_SOC_MIMX8MM6_A53"></a>

## 294.85 `SB_CONFIG_SOC_MIMX8MM6_A53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX8MM A53 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX8MM6
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX8MM_EVK
SB_CONFIG_BOARD_PHYBOARD_POLIS
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L15)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX8MM6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX8MM6)、[`SB_CONFIG_BOARD_IMX8MM_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8MM_EVK)、[`SB_CONFIG_BOARD_PHYBOARD_POLIS`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_PHYBOARD_POLIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX8MM6`、`SB_CONFIG_BOARD_IMX8MM_EVK`、`SB_CONFIG_BOARD_PHYBOARD_POLIS`。

<a id="SB_CONFIG_SOC_MIMX8MM6_M4"></a>

## 294.86 `SB_CONFIG_SOC_MIMX8MM6_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX8MM M4 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX8MM6
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_VERDIN_IMX8MM
SB_CONFIG_BOARD_IMX8MM_EVK
SB_CONFIG_BOARD_PHYBOARD_POLIS
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX8MM6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX8MM6)、[`SB_CONFIG_BOARD_VERDIN_IMX8MM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_VERDIN_IMX8MM)、[`SB_CONFIG_BOARD_IMX8MM_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8MM_EVK)、[`SB_CONFIG_BOARD_PHYBOARD_POLIS`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_PHYBOARD_POLIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX8MM6`、`SB_CONFIG_BOARD_VERDIN_IMX8MM`、`SB_CONFIG_BOARD_IMX8MM_EVK`、`SB_CONFIG_BOARD_PHYBOARD_POLIS`。

<a id="SB_CONFIG_SOC_MIMX8MN6_A53"></a>

## 294.87 `SB_CONFIG_SOC_MIMX8MN6_A53`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX8MN A53 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX8MN6
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX8MN_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L67)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX8MN6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX8MN6)、[`SB_CONFIG_BOARD_IMX8MN_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8MN_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX8MN6`、`SB_CONFIG_BOARD_IMX8MN_EVK`。

<a id="SB_CONFIG_SOC_MIMX8MQ6_M4"></a>

## 294.88 `SB_CONFIG_SOC_MIMX8MQ6_M4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NXP i.MX 8M Quad M4 微控制器（MCU）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX8MQ6
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX8MQ_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx8m/Kconfig.soc:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8m/Kconfig.soc#L53)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX8MQ6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX8MQ6)、[`SB_CONFIG_BOARD_IMX8MQ_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8MQ_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX8MQ6`、`SB_CONFIG_BOARD_IMX8MQ_EVK`。

<a id="SB_CONFIG_SOC_MIMX8QM6_ADSP"></a>

## 294.89 `SB_CONFIG_SOC_MIMX8QM6_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NXP i.MX 8QM 音频数字信号处理器（Audio DSP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX8QM6
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX8QM_MEK
```

**定义位置（Location）**：[`soc/nxp/imx/imx8/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX8QM6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX8QM6)、[`SB_CONFIG_BOARD_IMX8QM_MEK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8QM_MEK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX8QM6`、`SB_CONFIG_BOARD_IMX8QM_MEK`。

<a id="SB_CONFIG_SOC_MIMX8QX6_ADSP"></a>

## 294.90 `SB_CONFIG_SOC_MIMX8QX6_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NXP i.MX 8QXP 音频数字信号处理器（Audio DSP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX8QX6
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX8QXP_MEK
```

**定义位置（Location）**：[`soc/nxp/imx/imx8x/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8x/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX8QX6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX8QX6)、[`SB_CONFIG_BOARD_IMX8QXP_MEK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8QXP_MEK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX8QX6`、`SB_CONFIG_BOARD_IMX8QXP_MEK`。

<a id="SB_CONFIG_SOC_MIMX8UD7_ADSP"></a>

## 294.91 `SB_CONFIG_SOC_MIMX8UD7_ADSP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 NXP i.MX 8ULP 音频数字信号处理器（Audio DSP）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX8UD7
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX8ULP_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx8ulp/Kconfig.soc:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx8ulp/Kconfig.soc#L18)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX8UD7`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX8UD7)、[`SB_CONFIG_BOARD_IMX8ULP_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX8ULP_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX8UD7`、`SB_CONFIG_BOARD_IMX8ULP_EVK`。

<a id="SB_CONFIG_SOC_MIMX9111"></a>

## 294.92 `SB_CONFIG_SOC_MIMX9111`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX91 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_IMX9
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX91_QSB
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx91/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx91/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_IMX9`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_IMX9)、[`SB_CONFIG_BOARD_IMX91_QSB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX91_QSB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_IMX9`、`SB_CONFIG_BOARD_IMX91_QSB`。

<a id="SB_CONFIG_SOC_MIMX9131"></a>

## 294.93 `SB_CONFIG_SOC_MIMX9131`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX91 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_IMX9
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX91_EVK
SB_CONFIG_BOARD_FRDM_IMX91
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx91/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx91/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_IMX9`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_IMX9)、[`SB_CONFIG_BOARD_IMX91_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX91_EVK)、[`SB_CONFIG_BOARD_FRDM_IMX91`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_FRDM_IMX91)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_IMX9`、`SB_CONFIG_BOARD_IMX91_EVK`、`SB_CONFIG_BOARD_FRDM_IMX91`。

<a id="SB_CONFIG_SOC_MIMX9352_A55"></a>

## 294.94 `SB_CONFIG_SOC_MIMX9352_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX93 A55 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX9352
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_FRDM_IMX93
SB_CONFIG_BOARD_IMX93_EVK
SB_CONFIG_BOARD_PHYBOARD_NASH
SB_CONFIG_BOARD_IMX93_VAR_DART
SB_CONFIG_BOARD_IMX93_VAR_SOM
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx93/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx93/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX9352`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX9352)、[`SB_CONFIG_BOARD_FRDM_IMX93`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_FRDM_IMX93)、[`SB_CONFIG_BOARD_IMX93_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX93_EVK)、[`SB_CONFIG_BOARD_PHYBOARD_NASH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_PHYBOARD_NASH)、[`SB_CONFIG_BOARD_IMX93_VAR_DART`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX93_VAR_DART)、[`SB_CONFIG_BOARD_IMX93_VAR_SOM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX93_VAR_SOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX9352`、`SB_CONFIG_BOARD_FRDM_IMX93`、`SB_CONFIG_BOARD_IMX93_EVK`、`SB_CONFIG_BOARD_PHYBOARD_NASH`、`SB_CONFIG_BOARD_IMX93_VAR_DART`、`SB_CONFIG_BOARD_IMX93_VAR_SOM`。

<a id="SB_CONFIG_SOC_MIMX9352_M33"></a>

## 294.95 `SB_CONFIG_SOC_MIMX9352_M33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX93 M33 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX9352
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_FRDM_IMX93
SB_CONFIG_BOARD_IMX93_EVK
SB_CONFIG_BOARD_PHYBOARD_NASH
SB_CONFIG_BOARD_IMX93_VAR_DART
SB_CONFIG_BOARD_IMX93_VAR_SOM
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx93/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx93/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX9352`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX9352)、[`SB_CONFIG_BOARD_FRDM_IMX93`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_FRDM_IMX93)、[`SB_CONFIG_BOARD_IMX93_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX93_EVK)、[`SB_CONFIG_BOARD_PHYBOARD_NASH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_PHYBOARD_NASH)、[`SB_CONFIG_BOARD_IMX93_VAR_DART`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX93_VAR_DART)、[`SB_CONFIG_BOARD_IMX93_VAR_SOM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX93_VAR_SOM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX9352`、`SB_CONFIG_BOARD_FRDM_IMX93`、`SB_CONFIG_BOARD_IMX93_EVK`、`SB_CONFIG_BOARD_PHYBOARD_NASH`、`SB_CONFIG_BOARD_IMX93_VAR_DART`、`SB_CONFIG_BOARD_IMX93_VAR_SOM`。

<a id="SB_CONFIG_SOC_MIMX94398_A55"></a>

## 294.96 `SB_CONFIG_SOC_MIMX94398_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX943 A55 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX94398
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX943_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx943/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx943/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX94398`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX94398)、[`SB_CONFIG_BOARD_IMX943_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX943_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX94398`、`SB_CONFIG_BOARD_IMX943_EVK`。

<a id="SB_CONFIG_SOC_MIMX94398_M33"></a>

## 294.97 `SB_CONFIG_SOC_MIMX94398_M33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX943 的 NETC MIX 中的 Cortex-M33 内核 1（Core1）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX94398
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX943_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx943/Kconfig.soc:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx943/Kconfig.soc#L14)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX94398`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX94398)、[`SB_CONFIG_BOARD_IMX943_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX943_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX94398`、`SB_CONFIG_BOARD_IMX943_EVK`。

<a id="SB_CONFIG_SOC_MIMX94398_M7_0"></a>

## 294.98 `SB_CONFIG_SOC_MIMX94398_M7_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX943 的 M7MIX0 中的 Cortex-M7 内核 0（Core0）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX94398
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX943_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx943/Kconfig.soc:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx943/Kconfig.soc#L20)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX94398`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX94398)、[`SB_CONFIG_BOARD_IMX943_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX943_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX94398`、`SB_CONFIG_BOARD_IMX943_EVK`。

<a id="SB_CONFIG_SOC_MIMX94398_M7_1"></a>

## 294.99 `SB_CONFIG_SOC_MIMX94398_M7_1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX943 的 M7MIX1 中的 Cortex-M7 内核 1（Core1）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX94398
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX943_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx943/Kconfig.soc:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx943/Kconfig.soc#L26)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX94398`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX94398)、[`SB_CONFIG_BOARD_IMX943_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX943_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX94398`、`SB_CONFIG_BOARD_IMX943_EVK`。

<a id="SB_CONFIG_SOC_MIMX9529_A55"></a>

## 294.100 `SB_CONFIG_SOC_MIMX9529_A55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NXP i.MX952 A55 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_MIMX9529
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IMX952_EVK
```

**定义位置（Location）**：[`soc/nxp/imx/imx9/imx952/Kconfig.soc:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imx/imx9/imx952/Kconfig.soc#L8)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_MIMX9529`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_MIMX9529)、[`SB_CONFIG_BOARD_IMX952_EVK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IMX952_EVK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_MIMX9529`、`SB_CONFIG_BOARD_IMX952_EVK`。

<!-- kconfig-navigation -->

[上一章](P293_soc_nxp_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P295_soc_nxp_配置项参考_3.md)
