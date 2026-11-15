---
id: learning.zephyr-docs.kconfig-reference.page-310
title: "`soc/snps`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第310章\_`soc/snps`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/snps` 的 29 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ARC_IOT_CUSTOM_CPU_IDLE"></a>

## 310.1 `CONFIG_ARC_IOT_CUSTOM_CPU_IDLE`

**提示（Prompt）**：使用跳过睡眠的自定义 CPU 空闲实现（custom CPU idle）

**说明（Help）**

ARC IoT SoC 存在硬件限制：进入睡眠模式（sleep mode）会使 UART 等外设断电，从而无法通过外设中断唤醒。启用此项可使用跳过睡眠的自定义空闲实现（idle implementation），保持外设供电。需要在空闲期间持续运行 UART 的测试应启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ARC_IOT
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_CUSTOM_CPU_IDLE
CONFIG_ARCH_HAS_CUSTOM_CPU_ATOMIC_IDLE
```

**定义位置（Location）**：[`soc/snps/arc_iot/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/arc_iot/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ARC_IOT`](P310_soc_snps_配置项参考.md#CONFIG_SOC_ARC_IOT)、[`CONFIG_ARCH_HAS_CUSTOM_CPU_IDLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CUSTOM_CPU_IDLE)、[`CONFIG_ARCH_HAS_CUSTOM_CPU_ATOMIC_IDLE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_HAS_CUSTOM_CPU_ATOMIC_IDLE)。

<a id="CONFIG_SOC_ARC_HSDK4XD"></a>

## 310.2 `CONFIG_SOC_ARC_HSDK4XD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Synopsys ARC HSDK4XD 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_HSDK4XD
```

**定义位置（Location）**：[`soc/snps/hsdk4xd/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/hsdk4xd/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_HSDK4XD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HSDK4XD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_HSDK4XD`。

<a id="CONFIG_SOC_ARC_IOT"></a>

## 310.3 `CONFIG_SOC_ARC_IOT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Synopsys ARC IoT 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_IOTDK
```

**定义位置（Location）**：[`soc/snps/arc_iot/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/arc_iot/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_IOTDK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_IOTDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_IOTDK`。

<a id="CONFIG_SOC_EMSDP_EM11D"></a>

## 310.4 `CONFIG_SOC_EMSDP_EM11D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM11D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_EMSDP)、[`CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ARC_EMSDP`、`CONFIG_BOARD_EMSDP`。

<a id="CONFIG_SOC_EMSDP_EM4"></a>

## 310.5 `CONFIG_SOC_EMSDP_EM4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM4 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_EMSDP)、[`CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ARC_EMSDP`、`CONFIG_BOARD_EMSDP`。

<a id="CONFIG_SOC_EMSDP_EM5D"></a>

## 310.6 `CONFIG_SOC_EMSDP_EM5D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM5D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_EMSDP)、[`CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ARC_EMSDP`、`CONFIG_BOARD_EMSDP`。

<a id="CONFIG_SOC_EMSDP_EM6"></a>

## 310.7 `CONFIG_SOC_EMSDP_EM6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM6 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_EMSDP)、[`CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ARC_EMSDP`、`CONFIG_BOARD_EMSDP`。

<a id="CONFIG_SOC_EMSDP_EM7D"></a>

## 310.8 `CONFIG_SOC_EMSDP_EM7D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM7D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_EMSDP)、[`CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ARC_EMSDP`、`CONFIG_BOARD_EMSDP`。

<a id="CONFIG_SOC_EMSDP_EM7D_ESP"></a>

## 310.9 `CONFIG_SOC_EMSDP_EM7D_ESP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM7D+ESP 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_EMSDP)、[`CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ARC_EMSDP`、`CONFIG_BOARD_EMSDP`。

<a id="CONFIG_SOC_EMSDP_EM9D"></a>

## 310.10 `CONFIG_SOC_EMSDP_EM9D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM9D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ARC_EMSDP)、[`CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ARC_EMSDP`、`CONFIG_BOARD_EMSDP`。

<a id="CONFIG_SOC_EMSK"></a>

## 310.11 `CONFIG_SOC_EMSK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Synopsys ARC EM 入门套件片上系统（Starter Kit SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_EM_STARTERKIT
CONFIG_SOC_EMSK_EM7D
CONFIG_SOC_EMSK_EM9D
CONFIG_SOC_EMSK_EM11D
```

**定义位置（Location）**：[`soc/snps/emsk/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsk/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_EM_STARTERKIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EM_STARTERKIT)、[`CONFIG_SOC_EMSK_EM7D`](P310_soc_snps_配置项参考.md#CONFIG_SOC_EMSK_EM7D)、[`CONFIG_SOC_EMSK_EM9D`](P310_soc_snps_配置项参考.md#CONFIG_SOC_EMSK_EM9D)、[`CONFIG_SOC_EMSK_EM11D`](P310_soc_snps_配置项参考.md#CONFIG_SOC_EMSK_EM11D)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EM_STARTERKIT`。

<a id="CONFIG_SOC_EMSK_EM11D"></a>

## 310.12 `CONFIG_SOC_EMSK_EM11D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSK 的 Synopsys ARC EM11D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_EMSK
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EM_STARTERKIT
```

**定义位置（Location）**：[`soc/snps/emsk/Kconfig.soc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsk/Kconfig.soc#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_EMSK`](P310_soc_snps_配置项参考.md#CONFIG_SOC_EMSK)、[`CONFIG_BOARD_EM_STARTERKIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EM_STARTERKIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EM_STARTERKIT`。

<a id="CONFIG_SOC_EMSK_EM7D"></a>

## 310.13 `CONFIG_SOC_EMSK_EM7D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSK 的 Synopsys ARC EM7D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_EMSK
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EM_STARTERKIT
```

**定义位置（Location）**：[`soc/snps/emsk/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsk/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_EMSK`](P310_soc_snps_配置项参考.md#CONFIG_SOC_EMSK)、[`CONFIG_BOARD_EM_STARTERKIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EM_STARTERKIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EM_STARTERKIT`。

<a id="CONFIG_SOC_EMSK_EM9D"></a>

## 310.14 `CONFIG_SOC_EMSK_EM9D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSK 的 Synopsys ARC EM9D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_EMSK
```

**被选择（Selected by）**

```text
CONFIG_BOARD_EM_STARTERKIT
```

**定义位置（Location）**：[`soc/snps/emsk/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsk/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_EMSK`](P310_soc_snps_配置项参考.md#CONFIG_SOC_EMSK)、[`CONFIG_BOARD_EM_STARTERKIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EM_STARTERKIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_EM_STARTERKIT`。

<a id="CONFIG_SOC_NSIM_VPX5"></a>

## 310.15 `CONFIG_SOC_NSIM_VPX5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nSIM 中的 Synopsys ARC VPX5 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_NSIM_VPX5
```

**被选择（Selected by）**

```text
CONFIG_BOARD_NSIM
CONFIG_BOARD_NSIM
```

**定义位置（Location）**：[`soc/snps/nsim/arc_classic/vpx5/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/nsim/arc_classic/vpx5/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_NSIM_VPX5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NSIM_VPX5)、[`CONFIG_BOARD_NSIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NSIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_NSIM_VPX5`、`CONFIG_BOARD_NSIM`。

<a id="SB_CONFIG_SOC_ARC_HSDK4XD"></a>

## 310.16 `SB_CONFIG_SOC_ARC_HSDK4XD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Synopsys ARC HSDK4XD 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_HSDK4XD
```

**定义位置（Location）**：[`soc/snps/hsdk4xd/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/hsdk4xd/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_HSDK4XD`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HSDK4XD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_HSDK4XD`。

<a id="SB_CONFIG_SOC_ARC_IOT"></a>

## 310.17 `SB_CONFIG_SOC_ARC_IOT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Synopsys ARC IoT 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_IOTDK
```

**定义位置（Location）**：[`soc/snps/arc_iot/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/arc_iot/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_IOTDK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_IOTDK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_IOTDK`。

<a id="SB_CONFIG_SOC_EMSDP_EM11D"></a>

## 310.18 `SB_CONFIG_SOC_EMSDP_EM11D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM11D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L43)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ARC_EMSDP)、[`SB_CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_ARC_EMSDP`、`SB_CONFIG_BOARD_EMSDP`。

<a id="SB_CONFIG_SOC_EMSDP_EM4"></a>

## 310.19 `SB_CONFIG_SOC_EMSDP_EM4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM4 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L7)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ARC_EMSDP)、[`SB_CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_ARC_EMSDP`、`SB_CONFIG_BOARD_EMSDP`。

<a id="SB_CONFIG_SOC_EMSDP_EM5D"></a>

## 310.20 `SB_CONFIG_SOC_EMSDP_EM5D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM5D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ARC_EMSDP)、[`SB_CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_ARC_EMSDP`、`SB_CONFIG_BOARD_EMSDP`。

<a id="SB_CONFIG_SOC_EMSDP_EM6"></a>

## 310.21 `SB_CONFIG_SOC_EMSDP_EM6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM6 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ARC_EMSDP)、[`SB_CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_ARC_EMSDP`、`SB_CONFIG_BOARD_EMSDP`。

<a id="SB_CONFIG_SOC_EMSDP_EM7D"></a>

## 310.22 `SB_CONFIG_SOC_EMSDP_EM7D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM7D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L25)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ARC_EMSDP)、[`SB_CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_ARC_EMSDP`、`SB_CONFIG_BOARD_EMSDP`。

<a id="SB_CONFIG_SOC_EMSDP_EM7D_ESP"></a>

## 310.23 `SB_CONFIG_SOC_EMSDP_EM7D_ESP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM7D+ESP 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L31)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ARC_EMSDP)、[`SB_CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_ARC_EMSDP`、`SB_CONFIG_BOARD_EMSDP`。

<a id="SB_CONFIG_SOC_EMSDP_EM9D"></a>

## 310.24 `SB_CONFIG_SOC_EMSDP_EM9D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSDP 的 Synopsys ARC EM9D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_ARC_EMSDP
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EMSDP
```

**定义位置（Location）**：[`soc/snps/emsdp/Kconfig.soc:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsdp/Kconfig.soc#L37)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_ARC_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ARC_EMSDP)、[`SB_CONFIG_BOARD_EMSDP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EMSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_ARC_EMSDP`、`SB_CONFIG_BOARD_EMSDP`。

<a id="SB_CONFIG_SOC_EMSK"></a>

## 310.25 `SB_CONFIG_SOC_EMSK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Synopsys ARC EM 入门套件片上系统（Starter Kit SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EM_STARTERKIT
SB_CONFIG_SOC_EMSK_EM7D
SB_CONFIG_SOC_EMSK_EM9D
SB_CONFIG_SOC_EMSK_EM11D
```

**定义位置（Location）**：[`soc/snps/emsk/Kconfig.soc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsk/Kconfig.soc#L5)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_EM_STARTERKIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EM_STARTERKIT)、[`SB_CONFIG_SOC_EMSK_EM7D`](P310_soc_snps_配置项参考.md#SB_CONFIG_SOC_EMSK_EM7D)、[`SB_CONFIG_SOC_EMSK_EM9D`](P310_soc_snps_配置项参考.md#SB_CONFIG_SOC_EMSK_EM9D)、[`SB_CONFIG_SOC_EMSK_EM11D`](P310_soc_snps_配置项参考.md#SB_CONFIG_SOC_EMSK_EM11D)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EM_STARTERKIT`。

<a id="SB_CONFIG_SOC_EMSK_EM11D"></a>

## 310.26 `SB_CONFIG_SOC_EMSK_EM11D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSK 的 Synopsys ARC EM11D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_EMSK
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EM_STARTERKIT
```

**定义位置（Location）**：[`soc/snps/emsk/Kconfig.soc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsk/Kconfig.soc#L22)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_EMSK`](P310_soc_snps_配置项参考.md#SB_CONFIG_SOC_EMSK)、[`SB_CONFIG_BOARD_EM_STARTERKIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EM_STARTERKIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EM_STARTERKIT`。

<a id="SB_CONFIG_SOC_EMSK_EM7D"></a>

## 310.27 `SB_CONFIG_SOC_EMSK_EM7D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSK 的 Synopsys ARC EM7D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_EMSK
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EM_STARTERKIT
```

**定义位置（Location）**：[`soc/snps/emsk/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsk/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_EMSK`](P310_soc_snps_配置项参考.md#SB_CONFIG_SOC_EMSK)、[`SB_CONFIG_BOARD_EM_STARTERKIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EM_STARTERKIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EM_STARTERKIT`。

<a id="SB_CONFIG_SOC_EMSK_EM9D"></a>

## 310.28 `SB_CONFIG_SOC_EMSK_EM9D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

EMSK 的 Synopsys ARC EM9D 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_EMSK
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_EM_STARTERKIT
```

**定义位置（Location）**：[`soc/snps/emsk/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/emsk/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_EMSK`](P310_soc_snps_配置项参考.md#SB_CONFIG_SOC_EMSK)、[`SB_CONFIG_BOARD_EM_STARTERKIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EM_STARTERKIT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_EM_STARTERKIT`。

<a id="SB_CONFIG_SOC_NSIM_VPX5"></a>

## 310.29 `SB_CONFIG_SOC_NSIM_VPX5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

nSIM 中的 Synopsys ARC VPX5 内核

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_NSIM_VPX5
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NSIM
SB_CONFIG_BOARD_NSIM
```

**定义位置（Location）**：[`soc/snps/nsim/arc_classic/vpx5/Kconfig.soc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/snps/nsim/arc_classic/vpx5/Kconfig.soc#L11)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_NSIM_VPX5`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_SERIES_NSIM_VPX5)、[`SB_CONFIG_BOARD_NSIM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NSIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_SERIES_NSIM_VPX5`、`SB_CONFIG_BOARD_NSIM`。

<!-- kconfig-navigation -->

[上一章](P309_soc_silabs_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P311_soc_st_配置项参考.md)
