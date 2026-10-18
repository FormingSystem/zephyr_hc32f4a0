---
id: learning.zephyr-docs.kconfig-reference.page-6
title: "`drivers/interrupt_controller`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第6章\_`drivers/interrupt_controller`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/interrupt_controller` 的 56 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NXP_IRQSTEER"></a>

## 6.1 `CONFIG_NXP_IRQSTEER`

**提示（Prompt）**：NXP 芯片的 IRQ_STEER 中断控制器（Interrupt Controller）

**说明（Help）**

IRQSTEER 中断控制器（INTC）支持将多个外设中断多路复用（MUX）到一条或多条 CPU 中断线上。XTENSA DSP 等 CPU 使用此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IRQSTEER_INTC_ENABLED && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.nxp_irqsteer:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.nxp_irqsteer#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_NXP_PINT"></a>

## 6.2 `CONFIG_NXP_PINT`

**提示（Prompt）**：NXP MCU 的引脚中断与模式匹配引擎（Pin Interrupt and Pattern Match Engine，PINT）

**说明（Help）**

启用 NXP 微控制器（MCU）的 PINT 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PINT_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NXP_INPUTMUX
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.nxp_pint:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.nxp_pint#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NXP_INPUTMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_INPUTMUX)。

<a id="CONFIG_NXP_S32_WKPU"></a>

## 6.3 `CONFIG_NXP_S32_WKPU`

**提示（Prompt）**：NXP S32 MCU 的唤醒单元（Wake-up Unit）中断控制器驱动

**说明（Help）**

NXP S32 MCU 的唤醒单元（Wake-up Unit）中断控制器驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_WKPU_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.nxp_s32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.nxp_s32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_NXP_S32_WKPU_SOURCES_MAX"></a>

## 6.4 `CONFIG_NXP_S32_WKPU_SOURCES_MAX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

每个控制器的 WKPU 外部和内部源数量。这是片上系统集成（SoC Integration）选项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_S32_WKPU
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[32, 64]
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.nxp_s32:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.nxp_s32#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → NXP S32 MCU 的唤醒单元（Wake-up Unit）中断控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_NXP_S32_WKPU`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_NXP_S32_WKPU)。

<a id="CONFIG_NXP_SIUL2_EIRQ"></a>

## 6.5 `CONFIG_NXP_SIUL2_EIRQ`

**提示（Prompt）**：NXP SIUL2 外部中断控制器（External Interrupt Controller）驱动

**说明（Help）**

NXP SIUL2 外部中断控制器（External Interrupt Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SIUL2_EIRQ_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.nxp_siul2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.nxp_siul2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NOCACHE_MEMORY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_NXP_SIUL2_EIRQ_EXT_INTERRUPTS_GROUP"></a>

## 6.6 `CONFIG_NXP_SIUL2_EIRQ_EXT_INTERRUPTS_GROUP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

合并到单条内核中断线的 SIUL2 外部中断数量。这是片上系统集成（SoC Integration）选项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_SIUL2_EIRQ
```

**默认值（Defaults）**

```text
8
16 if CONFIG_SOC_SERIES_S32K5
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.nxp_siul2:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.nxp_siul2#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → NXP SIUL2 外部中断控制器（External Interrupt Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_NXP_SIUL2_EIRQ`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_NXP_SIUL2_EIRQ)、[`CONFIG_SOC_SERIES_S32K5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K5)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32K5`。

<a id="CONFIG_NXP_SIUL2_EIRQ_EXT_INTERRUPTS_MAX"></a>

## 6.7 `CONFIG_NXP_SIUL2_EIRQ_EXT_INTERRUPTS_MAX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

每个控制器的 SIUL2 外部中断数量。这是片上系统集成（SoC Integration）选项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_SIUL2_EIRQ
```

**默认值（Defaults）**

```text
8 if CONFIG_SOC_SERIES_S32ZE
16 if CONFIG_SOC_SERIES_S32K5
32 if CONFIG_SOC_SERIES_S32K3 || CONFIG_SOC_SERIES_MCXE31X
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.nxp_siul2:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.nxp_siul2#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → NXP SIUL2 外部中断控制器（External Interrupt Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_NXP_SIUL2_EIRQ`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_NXP_SIUL2_EIRQ)、[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)、[`CONFIG_SOC_SERIES_S32K5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K5)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_S32ZE`、`CONFIG_SOC_SERIES_S32K5`、`CONFIG_SOC_SERIES_S32K3`、`CONFIG_SOC_SERIES_MCXE31X`。

<a id="CONFIG_PLIC"></a>

## 6.8 `CONFIG_PLIC`

**提示（Prompt）**：平台级中断控制器（Platform Level Interrupt Controller，PLIC）

**说明（Help）**

平台级中断控制器（Platform Level Interrupt Controller，PLIC）支持 RISC-V SoC 定义的外部中断线。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFIVE_PLIC_1_0_0_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MULTI_LEVEL_INTERRUPTS
CONFIG_2ND_LEVEL_INTERRUPTS
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.plic:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.plic#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)、[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)。

<a id="CONFIG_PLIC_IRQ_AFFINITY"></a>

## 6.9 `CONFIG_PLIC_IRQ_AFFINITY`

**提示（Prompt）**：配置 IRQ 亲和性（Affinity）

**说明（Help）**

启用 IRQ 亲和性（Affinity）配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP && CONFIG_MP_MAX_NUM_CPUS > 1 && CONFIG_PLIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.plic:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.plic#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 平台级中断控制器（Platform Level Interrupt Controller，PLIC）

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)、[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)。

<a id="CONFIG_PLIC_IRQ_AFFINITY_MASK"></a>

## 6.10 `CONFIG_PLIC_IRQ_AFFINITY_MASK`

**提示（Prompt）**：默认 IRQ 亲和性掩码（Affinity Mask）

**说明（Help）**

启用 IRQ 亲和性（Affinity）时驱动使用的默认掩码。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_PLIC_IRQ_AFFINITY && CONFIG_PLIC
```

**默认值（Defaults）**

```text
0x1
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.plic:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.plic#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 平台级中断控制器（Platform Level Interrupt Controller，PLIC） → 配置 IRQ 亲和性（Affinity）

**配置项引用（Symbol References）**：[`CONFIG_PLIC_IRQ_AFFINITY`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC_IRQ_AFFINITY)、[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)。

<a id="CONFIG_PLIC_SHELL"></a>

## 6.11 `CONFIG_PLIC_SHELL`

**提示（Prompt）**：PLIC 命令行（Shell）命令

**说明（Help）**

启用有助于调试的附加命令行（Shell）命令。注意：这可能使用相当多的 RAM，大小为 `PLICs * IRQs * sizeof(uint16_t)`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_PLIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.plic:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.plic#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 平台级中断控制器（Platform Level Interrupt Controller，PLIC）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)。

<a id="CONFIG_PLIC_SHELL_IRQ_AFFINITY"></a>

## 6.12 `CONFIG_PLIC_SHELL_IRQ_AFFINITY`

**提示（Prompt）**：用于配置 IRQ 亲和性（Affinity）的 Shell 命令

**说明（Help）**

提供在运行时配置 IRQ 亲和性（Affinity）的命令行（Shell）命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PLIC_IRQ_AFFINITY && CONFIG_PLIC_SHELL && CONFIG_PLIC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.plic:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.plic#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 平台级中断控制器（Platform Level Interrupt Controller，PLIC） → PLIC 命令行（Shell）命令

**配置项引用（Symbol References）**：[`CONFIG_PLIC_IRQ_AFFINITY`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC_IRQ_AFFINITY)、[`CONFIG_PLIC_SHELL`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC_SHELL)、[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)。

<a id="CONFIG_PLIC_SHELL_IRQ_COUNT"></a>

## 6.13 `CONFIG_PLIC_SHELL_IRQ_COUNT`

**提示（Prompt）**：IRQ 计数（Count）Shell 命令

**说明（Help）**

记录每条中断线的触发次数，并提供用于访问计数的命令行（Shell）命令。注意：这可能使用相当多的 RAM，大小为 `PLICs * IRQs * sizeof(PLIC_IRQ_COUNT_TYPE)`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PLIC_SHELL && CONFIG_PLIC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.plic:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.plic#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 平台级中断控制器（Platform Level Interrupt Controller，PLIC） → PLIC 命令行（Shell）命令

**配置项引用（Symbol References）**：[`CONFIG_PLIC_SHELL`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC_SHELL)、[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)。

<a id="CONFIG_PLIC_SUPPORTS_SOFT_INTERRUPT"></a>

## 6.14 `CONFIG_PLIC_SUPPORTS_SOFT_INTERRUPT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

PLIC 支持软件触发中断（Software-triggered Interrupt）时启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_NCEPLIC100_ENABLED && CONFIG_PLIC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.plic:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.plic#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 平台级中断控制器（Platform Level Interrupt Controller，PLIC）

**配置项引用（Symbol References）**：[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)。

<a id="CONFIG_PLIC_SUPPORTS_TRIG_EDGE"></a>

## 6.15 `CONFIG_PLIC_SUPPORTS_TRIG_EDGE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

PLIC 支持边沿触发中断（Edge-triggered Interrupt）时启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_NCEPLIC100_ENABLED && CONFIG_PLIC_SUPPORTS_TRIG_TYPE && CONFIG_PLIC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.plic:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.plic#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 平台级中断控制器（Platform Level Interrupt Controller，PLIC）

**配置项引用（Symbol References）**：[`CONFIG_PLIC_SUPPORTS_TRIG_TYPE`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC_SUPPORTS_TRIG_TYPE)、[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)。

<a id="CONFIG_PLIC_SUPPORTS_TRIG_TYPE"></a>

## 6.16 `CONFIG_PLIC_SUPPORTS_TRIG_TYPE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

PLIC 支持电平、边沿等多种触发类型（Trigger Type）时启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_NCEPLIC100_ENABLED && CONFIG_PLIC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.plic:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.plic#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 平台级中断控制器（Platform Level Interrupt Controller，PLIC）

**配置项引用（Symbol References）**：[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)。

<a id="CONFIG_PLIC_TRIG_TYPE_BITWIDTH"></a>

## 6.17 `CONFIG_PLIC_TRIG_TYPE_BITWIDTH`

**提示（Prompt）**：触发类型位宽（Trigger Type Bitwidth）

**说明（Help）**

区分各触发类型（Trigger Type）所需的位数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PLIC_SUPPORTS_TRIG_TYPE && CONFIG_PLIC
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.plic:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.plic#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 平台级中断控制器（Platform Level Interrupt Controller，PLIC）

**配置项引用（Symbol References）**：[`CONFIG_PLIC_SUPPORTS_TRIG_TYPE`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC_SUPPORTS_TRIG_TYPE)、[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)。

<a id="CONFIG_PLIC_TRIG_TYPE_REG_OFFSET"></a>

## 6.18 `CONFIG_PLIC_TRIG_TYPE_REG_OFFSET`

**提示（Prompt）**：触发类型寄存器偏移量（Trigger Type Register Offset）

**说明（Help）**

“触发类型（Trigger Type）”寄存器的偏移量。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_PLIC_SUPPORTS_TRIG_TYPE && CONFIG_PLIC
```

**默认值（Defaults）**

```text
0x1080 if DT_HAS_ANDESTECH_NCEPLIC100_ENABLED
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.plic:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.plic#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 平台级中断控制器（Platform Level Interrupt Controller，PLIC）

**配置项引用（Symbol References）**：[`CONFIG_PLIC_SUPPORTS_TRIG_TYPE`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC_SUPPORTS_TRIG_TYPE)、[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)。

<a id="CONFIG_PLIC_WARM_BOOT"></a>

## 6.19 `CONFIG_PLIC_WARM_BOOT`

**提示（Prompt）**：PLIC 热启动（Warm Boot）

**说明（Help）**

热启动（Warm Boot）时禁用部分初始化，例如在非对称多处理（Asymmetric Multi Processing）场景中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PLIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.plic:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.plic#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 平台级中断控制器（Platform Level Interrupt Controller，PLIC）

**配置项引用（Symbol References）**：[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)。

<a id="CONFIG_RENESAS_RX_GRP_INTC"></a>

## 6.20 `CONFIG_RENESAS_RX_GRP_INTC`

**提示（Prompt）**：Renesas RX 系列分组中断（Group Interrupt）

**说明（Help）**

Renesas RX 系列分组中断（Group Interrupt）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_GRP_INTC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.renesas_rx:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.renesas_rx#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_RENESAS_RX_ICU"></a>

## 6.21 `CONFIG_RENESAS_RX_ICU`

**提示（Prompt）**：Renesas RX 系列中断控制器单元（Interrupt Controller Unit）

**说明（Help）**

Renesas RX 系列中断控制器单元（Interrupt Controller Unit）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_ICU_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.renesas_rx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.renesas_rx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_RENESAS_RZ_EXT_IRQ"></a>

## 6.22 `CONFIG_RENESAS_RZ_EXT_IRQ`

**提示（Prompt）**：Renesas RZ 外部中断控制器（External Interrupt Controller）驱动

**说明（Help）**

Renesas RZ 外部中断控制器（External Interrupt Controller）驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_EXT_IRQ_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_EXT_IRQ
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.renesas_rz:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.renesas_rz#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USE_RZ_FSP_EXT_IRQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_EXT_IRQ)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_RENESAS_RZ_ICU_V2"></a>

## 6.23 `CONFIG_RENESAS_RZ_ICU_V2`

**提示（Prompt）**：Renesas RZ 中断控制器单元（Interrupt Controller Unit，ICU）

**说明（Help）**

Renesas RZ 中断控制器单元（Interrupt Controller Unit，ICU）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_ICU_V2_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.renesas_rz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.renesas_rz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_RENESAS_RZ_INTC_HAS_NMI"></a>

## 6.24 `CONFIG_RENESAS_RZ_INTC_HAS_NMI`

**提示（Prompt）**：不可屏蔽中断（Non Maskable Interrupt，NMI）引脚

**说明（Help）**

Renesas RZ 中断控制器具有不可屏蔽中断（Non Maskable Interrupt，NMI）引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_RZG3S || CONFIG_SOC_SERIES_RZA3UL) && CONFIG_RENESAS_RZ_EXT_IRQ
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.renesas_rz:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.renesas_rz#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → Renesas RZ 外部中断控制器（External Interrupt Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZG3S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3S)、[`CONFIG_SOC_SERIES_RZA3UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3UL)、[`CONFIG_RENESAS_RZ_EXT_IRQ`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RENESAS_RZ_EXT_IRQ)。

<a id="CONFIG_RENESAS_RZ_INTC_SELECT_INTERRUPT"></a>

## 6.25 `CONFIG_RENESAS_RZ_INTC_SELECT_INTERRUPT`

**提示（Prompt）**：Renesas RZ INTC 中断选择（Select Interrupt）

**说明（Help）**

Renesas RZ INTC 中断选择（Select Interrupt）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_INTC_V2_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.renesas_rz:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.renesas_rz#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_RENESAS_RZ_TINT"></a>

## 6.26 `CONFIG_RENESAS_RZ_TINT`

**提示（Prompt）**：Renesas RZ GPIO 中断（TINT）控制器驱动

**说明（Help）**

Renesas RZ GPIO 中断（TINT）控制器驱动

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_TINT_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.renesas_rz:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.renesas_rz#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_RENESAS_RZ_TINT_SUPPORT_STATUS_CLEAR_REG"></a>

## 6.27 `CONFIG_RENESAS_RZ_TINT_SUPPORT_STATUS_CLEAR_REG`

**提示（Prompt）**：Renesas RZ TINT 支持状态清除寄存器（Status Clear Register）

**说明（Help）**

Renesas RZ/V2H、RZ/V2N 支持通过状态清除寄存器（Status Clear Register）复位中断标志，而其他 SoC 通过状态寄存器（Status Register）复位中断标志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_INTC_V2_ENABLED && CONFIG_RENESAS_RZ_TINT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.renesas_rz:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.renesas_rz#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → Renesas RZ GPIO 中断（TINT）控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_RENESAS_RZ_TINT`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RENESAS_RZ_TINT)。

<a id="CONFIG_RISCV_AIA"></a>

## 6.28 `CONFIG_RISCV_AIA`

**提示（Prompt）**：RISC-V 高级中断架构（AIA）统一协调器（Unified Coordinator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_RISCV_APLIC_MSI || CONFIG_RISCV_APLIC_DIRECT) && ((!CONFIG_RISCV_S_MODE && CONFIG_RISCV_ISA_EXT_SMAIA) || (CONFIG_RISCV_S_MODE && CONFIG_RISCV_ISA_EXT_SSAIA))
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MULTI_LEVEL_INTERRUPTS
CONFIG_2ND_LEVEL_INTERRUPTS
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.riscv_aia:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.riscv_aia#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_APLIC_MSI`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RISCV_APLIC_MSI)、[`CONFIG_RISCV_APLIC_DIRECT`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RISCV_APLIC_DIRECT)、[`CONFIG_RISCV_S_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_S_MODE)、[`CONFIG_RISCV_ISA_EXT_SMAIA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_ISA_EXT_SMAIA)、[`CONFIG_RISCV_ISA_EXT_SSAIA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_ISA_EXT_SSAIA)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)、[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)。

<a id="CONFIG_RISCV_APLIC"></a>

## 6.29 `CONFIG_RISCV_APLIC`

**提示（Prompt）**：RISC-V 高级平台级中断控制器（Advanced Platform-Level Interrupt Controller，APLIC）

**说明（Help）**

RISC-V 高级平台级中断控制器（Advanced Platform-Level Interrupt Controller，APLIC），在 RISC-V 高级中断架构（AIA）系统中路由有线中断（Wired Interrupt）。当设备树（Devicetree）中存在 APLIC 节点时，自动启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RISCV_APLIC_ENABLED && CONFIG_RISCV
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.riscv_aia:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.riscv_aia#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV)。

<a id="CONFIG_RISCV_APLIC_DIRECT"></a>

## 6.30 `CONFIG_RISCV_APLIC_DIRECT`

**提示（Prompt）**：RISC-V APLIC 直接交付模式（Direct Delivery Mode）

**说明（Help）**

启用 APLIC 的直接交付模式（Direct Delivery Mode）。将有线中断（Wired Interrupt）直接路由到硬件线程（Hart）的 MEXT 中断线。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_APLIC && !n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.riscv_aia:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.riscv_aia#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_APLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RISCV_APLIC)。

<a id="CONFIG_RISCV_APLIC_DIRECT_IRQ_AFFINITY"></a>

## 6.31 `CONFIG_RISCV_APLIC_DIRECT_IRQ_AFFINITY`

**提示（Prompt）**：为 APLIC 直接模式（Direct Mode）配置 IRQ 亲和性（Affinity）

**说明（Help）**

启用 IRQ 亲和性（Affinity）配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_APLIC_DIRECT && CONFIG_SMP && CONFIG_MP_MAX_NUM_CPUS > 1
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.riscv_aia:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.riscv_aia#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → RISC-V APLIC 直接交付模式（Direct Delivery Mode）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_APLIC_DIRECT`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RISCV_APLIC_DIRECT)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)。

<a id="CONFIG_RISCV_APLIC_MSI"></a>

## 6.32 `CONFIG_RISCV_APLIC_MSI`

**提示（Prompt）**：RISC-V APLIC MSI 交付模式（MSI Delivery Mode）

**说明（Help）**

启用 APLIC 的 MSI 交付模式（MSI Delivery Mode）。将有线中断（Wired Interrupt）以消息信号中断（Message-Signaled Interrupt，MSI）的形式路由至 IMSIC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RISCV_IMSIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.riscv_aia:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.riscv_aia#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_IMSIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RISCV_IMSIC)。

<a id="CONFIG_RISCV_IMSIC"></a>

## 6.33 `CONFIG_RISCV_IMSIC`

**提示（Prompt）**：RISC-V 传入消息信号中断控制器（Incoming Message-Signaled Interrupt Controller，IMSIC）

**说明（Help）**

RISC-V 传入消息信号中断控制器（Incoming Message-Signaled Interrupt Controller，IMSIC），在 RISC-V 高级中断架构（AIA）中为每个硬件线程（Hart）提供用于 MSI 交付的中断文件（Interrupt File）。当设备树（Devicetree）中存在 IMSIC 节点时，自动启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV && CONFIG_RISCV_ISA_EXT_SMCSRIND
```

**默认值（Defaults）**

```text
y if DT_HAS_RISCV_IMSIC_ENABLED
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.riscv_aia:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.riscv_aia#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV)、[`CONFIG_RISCV_ISA_EXT_SMCSRIND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_ISA_EXT_SMCSRIND)。

<a id="CONFIG_RV32M1_INTMUX"></a>

## 6.34 `CONFIG_RV32M1_INTMUX`

**提示（Prompt）**：OpenISA RV32M1 INTMUX 中断控制器（Interrupt Controller）支持

**说明（Help）**

选择此选项以启用 RV32M1 INTMUX 驱动支持。该驱动为 SoC 提供第二级中断控制器（Interrupt Controller）。INTMUX 外设将第二级中断合并到八个通道（Channel）中；每个通道都有一条通往内核的独立第一级中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OPENISA_RV32M1_INTMUX_ENABLED && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.rv32m1:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.rv32m1#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_RV32M1_INTMUX_CHANNEL_0"></a>

## 6.35 `CONFIG_RV32M1_INTMUX_CHANNEL_0`

**提示（Prompt）**：INTMUX 通道 0（Channel 0）

**说明（Help）**

启用 INTMUX 通道 0（Channel 0）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RV32M1_INTMUX
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.rv32m1:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.rv32m1#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → OpenISA RV32M1 INTMUX 中断控制器（Interrupt Controller）支持

**配置项引用（Symbol References）**：[`CONFIG_RV32M1_INTMUX`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RV32M1_INTMUX)。

<a id="CONFIG_RV32M1_INTMUX_CHANNEL_1"></a>

## 6.36 `CONFIG_RV32M1_INTMUX_CHANNEL_1`

**提示（Prompt）**：INTMUX 通道 1（Channel 1）

**说明（Help）**

启用 INTMUX 通道 1（Channel 1）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RV32M1_INTMUX
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.rv32m1:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.rv32m1#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → OpenISA RV32M1 INTMUX 中断控制器（Interrupt Controller）支持

**配置项引用（Symbol References）**：[`CONFIG_RV32M1_INTMUX`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RV32M1_INTMUX)。

<a id="CONFIG_RV32M1_INTMUX_CHANNEL_2"></a>

## 6.37 `CONFIG_RV32M1_INTMUX_CHANNEL_2`

**提示（Prompt）**：INTMUX 通道 2（Channel 2）

**说明（Help）**

启用 INTMUX 通道 2（Channel 2）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BT && CONFIG_RV32M1_INTMUX
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.rv32m1:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.rv32m1#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → OpenISA RV32M1 INTMUX 中断控制器（Interrupt Controller）支持

**配置项引用（Symbol References）**：[`CONFIG_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT)、[`CONFIG_RV32M1_INTMUX`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RV32M1_INTMUX)。

<a id="CONFIG_RV32M1_INTMUX_CHANNEL_3"></a>

## 6.38 `CONFIG_RV32M1_INTMUX_CHANNEL_3`

**提示（Prompt）**：INTMUX 通道 3（Channel 3）

**说明（Help）**

启用 INTMUX 通道 3（Channel 3）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BT && CONFIG_RV32M1_INTMUX
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.rv32m1:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.rv32m1#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → OpenISA RV32M1 INTMUX 中断控制器（Interrupt Controller）支持

**配置项引用（Symbol References）**：[`CONFIG_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT)、[`CONFIG_RV32M1_INTMUX`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RV32M1_INTMUX)。

<a id="CONFIG_RV32M1_INTMUX_CHANNEL_4"></a>

## 6.39 `CONFIG_RV32M1_INTMUX_CHANNEL_4`

**提示（Prompt）**：INTMUX 通道 4（Channel 4）

**说明（Help）**

启用 INTMUX 通道 4（Channel 4）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RV32M1_INTMUX
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.rv32m1:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.rv32m1#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → OpenISA RV32M1 INTMUX 中断控制器（Interrupt Controller）支持

**配置项引用（Symbol References）**：[`CONFIG_RV32M1_INTMUX`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RV32M1_INTMUX)。

<a id="CONFIG_RV32M1_INTMUX_CHANNEL_5"></a>

## 6.40 `CONFIG_RV32M1_INTMUX_CHANNEL_5`

**提示（Prompt）**：INTMUX 通道 5（Channel 5）

**说明（Help）**

启用 INTMUX 通道 5（Channel 5）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RV32M1_INTMUX
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.rv32m1:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.rv32m1#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → OpenISA RV32M1 INTMUX 中断控制器（Interrupt Controller）支持

**配置项引用（Symbol References）**：[`CONFIG_RV32M1_INTMUX`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RV32M1_INTMUX)。

<a id="CONFIG_RV32M1_INTMUX_CHANNEL_6"></a>

## 6.41 `CONFIG_RV32M1_INTMUX_CHANNEL_6`

**提示（Prompt）**：INTMUX 通道 6（Channel 6）

**说明（Help）**

启用 INTMUX 通道 6（Channel 6）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RV32M1_INTMUX
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.rv32m1:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.rv32m1#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → OpenISA RV32M1 INTMUX 中断控制器（Interrupt Controller）支持

**配置项引用（Symbol References）**：[`CONFIG_RV32M1_INTMUX`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RV32M1_INTMUX)。

<a id="CONFIG_RV32M1_INTMUX_CHANNEL_7"></a>

## 6.42 `CONFIG_RV32M1_INTMUX_CHANNEL_7`

**提示（Prompt）**：INTMUX 通道 7（Channel 7）

**说明（Help）**

启用 INTMUX 通道 7（Channel 7）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RV32M1_INTMUX
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.rv32m1:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.rv32m1#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → OpenISA RV32M1 INTMUX 中断控制器（Interrupt Controller）支持

**配置项引用（Symbol References）**：[`CONFIG_RV32M1_INTMUX`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RV32M1_INTMUX)。

<a id="CONFIG_RV32M1_INTMUX_INIT_PRIORITY"></a>

## 6.43 `CONFIG_RV32M1_INTMUX_INIT_PRIORITY`

**提示（Prompt）**：INTMUX 驱动初始化优先级（Initialization Priority）

**说明（Help）**

INTMUX 驱动在启动时的初始化优先级（Initialization Priority）。除非明确了解修改的影响，否则不要更改默认值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RV32M1_INTMUX
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.rv32m1:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.rv32m1#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → OpenISA RV32M1 INTMUX 中断控制器（Interrupt Controller）支持

**配置项引用（Symbol References）**：[`CONFIG_RV32M1_INTMUX`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RV32M1_INTMUX)。

<a id="CONFIG_SAM0_EIC"></a>

## 6.44 `CONFIG_SAM0_EIC`

**提示（Prompt）**：SAM0 系列器件外部中断控制器（External Interrupt Controller，EIC）驱动

**说明（Help）**

启用 SAM0 系列器件的外部中断控制器（EIC）驱动。GPIO 中断支持需要此驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_EIC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.sam0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.sam0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_SHARED_IRQ"></a>

## 6.45 `CONFIG_SHARED_IRQ`

**提示（Prompt）**：共享中断驱动（Shared Interrupt Driver）

**说明（Help）**

在系统中加入共享中断（Shared Interrupt）支持。大多数系统不需要共享中断支持；如不确定，选择否。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SHARED_IRQ_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.shared_irq:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.shared_irq#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_SHARED_IRQ_INIT_PRIORITY"></a>

## 6.46 `CONFIG_SHARED_IRQ_INIT_PRIORITY`

**提示（Prompt）**：共享 IRQ 初始化优先级（Initialization Priority）

**说明（Help）**

共享 IRQ（Shared IRQ）在 `POST_KERNEL` 初始化级别进行初始化，必须先于任何使用它们的设备完成初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHARED_IRQ
```

**默认值（Defaults）**

```text
45
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.shared_irq:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.shared_irq#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 共享中断驱动（Shared Interrupt Driver）

**配置项引用（Symbol References）**：[`CONFIG_SHARED_IRQ`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_SHARED_IRQ)。

<a id="CONFIG_SWERV_PIC"></a>

## 6.47 `CONFIG_SWERV_PIC`

**提示（Prompt）**：Cadence SweRV 可编程中断控制器（Programmable Interrupt Controller，PIC）

**说明（Help）**

Cadence SweRV RISC-V CPU 的可编程中断控制器（Programmable Interrupt Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CDNS_SWERV_PIC_ENABLED || DT_HAS_SWERV_PIC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.swerv:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.swerv#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_SWERV_PIC_MAX_GENERIC_IRQ"></a>

## 6.48 `CONFIG_SWERV_PIC_MAX_GENERIC_IRQ`

**提示（Prompt）**：Cadence SweRV 通用 IRQ 最大数量（Maximum Number of Generic IRQs）

**说明（Help）**

通用 IRQ（Generic IRQ）的最大数量，超过该数量后的中断设置由 SweRV 中断控制器处理。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SWERV_PIC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.swerv:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.swerv#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → Cadence SweRV 可编程中断控制器（Programmable Interrupt Controller，PIC）

**配置项引用（Symbol References）**：[`CONFIG_SWERV_PIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_SWERV_PIC)。

<a id="CONFIG_THEJAS32_INTC"></a>

## 6.49 `CONFIG_THEJAS32_INTC`

**提示（Prompt）**：C-DAC THEJAS32 中断控制器（Interrupt Controller）

**说明（Help）**

C-DAC THEJAS32 第二级中断控制器（Second-level Interrupt Controller）驱动，将 SoC 外设中断源聚合到 RISC-V 机器外部中断线（Machine External Interrupt Line）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CDAC_THEJAS32_INTC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MULTI_LEVEL_INTERRUPTS
CONFIG_2ND_LEVEL_INTERRUPTS
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.thejas32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.thejas32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)、[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)。

<a id="CONFIG_TI_VIM"></a>

## 6.50 `CONFIG_TI_VIM`

**提示（Prompt）**：TI 向量中断管理器（Vectored Interrupt Manager）

**说明（Help）**

TI 向量中断管理器（Vectored Interrupt Manager）提供硬件辅助，为 ARM Cortex-R5 处理器内核排列中断源优先级并聚合中断源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_VIM_ENABLED && CONFIG_CPU_CORTEX_R5
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AM64X_R5
CONFIG_SOC_SERIES_J721E_R5
CONFIG_SOC_SERIES_J722S_R5
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.vim:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.vim#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_R5)、[`CONFIG_SOC_SERIES_AM64X_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM64X_R5)、[`CONFIG_SOC_SERIES_J721E_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J721E_R5)、[`CONFIG_SOC_SERIES_J722S_R5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_J722S_R5)。

<a id="CONFIG_VEXRISCV_LITEX_IRQ"></a>

## 6.51 `CONFIG_VEXRISCV_LITEX_IRQ`

**提示（Prompt）**：VexRiscv LiteX 中断控制器（Interrupt Controller）

**说明（Help）**

LiteX VexRiscv 的 IRQ 实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_VEXRISCV_INTC0_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_WCH_EXTI"></a>

## 6.52 `CONFIG_WCH_EXTI`

**提示（Prompt）**：WCH CH32V00x/20x/30x 外部中断与事件控制器（External Interrupt and Event Controller，EXTI）

**说明（Help）**

启用 WCH CH32V00x/20x/30x 外部中断与事件控制器（External Interrupt and Event Controller，EXTI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_EXTI_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.wch_exti:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.wch_exti#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_WCH_PFIC"></a>

## 6.53 `CONFIG_WCH_PFIC`

**提示（Prompt）**：WCH 可编程快速中断控制器（Programmable Fast Interrupt Controller，PFIC）

**说明（Help）**

WCH PFIC 中断控制器（Interrupt Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_PFIC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.wch_pfic:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.wch_pfic#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_X2APIC"></a>

## 6.54 `CONFIG_X2APIC`

**提示（Prompt）**：以 x2APIC 模式访问本地 APIC（Local APIC）

**说明（Help）**

如果本地 APIC（Local APIC）支持 x2APIC 模式，请启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOAPIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.loapic:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.loapic#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 本地高级可编程中断控制器（Local APIC，LOAPIC）

**配置项引用（Symbol References）**：[`CONFIG_LOAPIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_LOAPIC)。

<a id="CONFIG_XEC_GIRQ_INIT_PRIORITY"></a>

## 6.55 `CONFIG_XEC_GIRQ_INIT_PRIORITY`

**提示（Prompt）**：XEX GIRQ 中断控制器初始化优先级（Initialization Priority）

**说明（Help）**

XEC GIRQ 中断控制器（Interrupt Controller）设备的初始化优先级。该优先级值需要大于 `INTC_INIT_PRIORITY`，使 XEC GIRQ 控制器在 `xec_ecia` 之后初始化。

译注：此项提示中的 `XEX` 按原文保留，帮助正文使用 `XEC`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCHP_ECIA_XEC
```

**默认值（Defaults）**

```text
41
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MCHP_ECIA_XEC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MCHP_ECIA_XEC)。

<a id="CONFIG_XMC4XXX_INTC"></a>

## 6.56 `CONFIG_XMC4XXX_INTC`

**提示（Prompt）**：XMC4XXX 系列器件中断控制器（Interrupt Controller）驱动

**说明（Help）**

启用 XMC4XXX 系列器件的中断控制器（Interrupt Controller）驱动。GPIO 中断支持需要此驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_INTC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.xmc4xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.xmc4xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<!-- kconfig-navigation -->

[上一章](P005_drivers_interrupt_controller_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P007_drivers_timer_配置项参考_1.md)
