---
id: learning.zephyr-docs.kconfig-reference.page-301
title: "`soc/realtek`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第301章\_`soc/realtek`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/realtek` 的 19 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_REALTEK_RTS5912_BOOTROM_HEADER"></a>

## 301.1 `CONFIG_REALTEK_RTS5912_BOOTROM_HEADER`

**提示（Prompt）**：为 RTS5912 创建启动 ROM 头部（BOOTROM header）

**说明（Help）**

RTS5912 启动 ROM（BOOTROM）需要关于启动过程的信息。调用 `rts5912_imgtool`，生成 RTS5912 启动 ROM 头部。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_REALTEK_EC
```

**定义位置（Location）**：[`soc/realtek/ec/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ec/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_REALTEK_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_EC`。

<a id="CONFIG_REALTEK_RTS5912_BOOTROM_HEADER_LOAD_ADDRESS"></a>

## 301.2 `CONFIG_REALTEK_RTS5912_BOOTROM_HEADER_LOAD_ADDRESS`

**提示（Prompt）**：设置启动 ROM 使用的地址（address for BOOTROM）

**说明（Help）**

RTS5912 启动 ROM（BOOTROM）将使用此地址确定固件镜像起始位置。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_REALTEK_RTS5912_BOOTROM_HEADER && CONFIG_SOC_FAMILY_REALTEK_EC
```

**默认值（Defaults）**

```text
"0x0 - 0x20"
```

**定义位置（Location）**：[`soc/realtek/ec/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ec/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 为 RTS5912 创建启动 ROM 头部（BOOTROM header）

**配置项引用（Symbol References）**：[`CONFIG_REALTEK_RTS5912_BOOTROM_HEADER`](P301_soc_realtek_配置项参考.md#CONFIG_REALTEK_RTS5912_BOOTROM_HEADER)、[`CONFIG_SOC_FAMILY_REALTEK_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_EC`。

<a id="CONFIG_RTS5912_DEBUG_SWJ"></a>

## 301.3 `CONFIG_RTS5912_DEBUG_SWJ`

**提示（Prompt）**：串行线 JTAG（Serial wire JTAG）

**说明（Help）**

启用 RTS5912 嵌入式控制器（EC）上的串行线 JTAG 连接（serial wire JTAG connection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SWJ_CONNECTOR_ENABLED && CONFIG_SOC_SERIES_RTS5912 && CONFIG_SOC_FAMILY_REALTEK_EC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/realtek/ec/rts5912/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ec/rts5912/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RTS5912`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SOC_FAMILY_REALTEK_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_EC`。

<a id="CONFIG_RTS5912_ON_ENTER_CPU_IDLE_HOOK"></a>

## 301.4 `CONFIG_RTS5912_ON_ENTER_CPU_IDLE_HOOK`

**提示（Prompt）**：启用 CPU 空闲钩子（CPU idle hook）

**说明（Help）**

启用钩子 `z_arm_on_enter_cpu_idle()`，在通过 `k_cpu_idle()` 或 `k_cpu_atomic_idle()` 使 CPU 空闲时调用。必要时，可通过该钩子跳过 `WFE/WFI` 指令，阻止 CPU 实际进入休眠（Sleep）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RTS5912 && CONFIG_SOC_FAMILY_REALTEK_EC
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK
```

**定义位置（Location）**：[`soc/realtek/ec/rts5912/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ec/rts5912/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RTS5912`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SOC_FAMILY_REALTEK_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_EC)、[`CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_EC`。

<a id="CONFIG_SOC_AMEBA_NP_CORE"></a>

## 301.5 `CONFIG_SOC_AMEBA_NP_CORE`

**提示（Prompt）**：Ameba NP 预构建镜像（prebuilt images）

**说明（Help）**

选择在 Ameba 多核 MCU 的 NP 内核上执行的预构建镜像（prebuilt image）。该镜像负责在设备上启动 NP。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_REALTEK_AMEBA
```

**默认值（Defaults）**

```text
CONFIG_SOC_AMEBA_NP_DISABLED
```

**可选项（Choices）**

```text
CONFIG_SOC_AMEBA_NP_DISABLED
CONFIG_SOC_AMEBA_NP_IMAGE
```

**定义位置（Location）**：[`soc/realtek/ameba/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ameba/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_SOC_AMEBA_NP_DISABLED`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_AMEBA_NP_DISABLED)、[`CONFIG_SOC_AMEBA_NP_IMAGE`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_AMEBA_NP_IMAGE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_AMEBA`。

<a id="CONFIG_SOC_AMEBA_NP_DISABLED"></a>

## 301.6 `CONFIG_SOC_AMEBA_NP_DISABLED`

**提示（Prompt）**：无（None）

**说明（Help）**

不包含任何 NP 内核的预构建镜像（prebuilt image）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_AMEBA_NP_CORE>
```

**定义位置（Location）**：[`soc/realtek/ameba/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ameba/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Ameba NP 预构建镜像（prebuilt images）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AMEBA_NP_CORE`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_AMEBA_NP_CORE)。

<a id="CONFIG_SOC_AMEBA_NP_IMAGE"></a>

## 301.7 `CONFIG_SOC_AMEBA_NP_IMAGE`

**提示（Prompt）**：深度睡眠（DeepSleep）

**说明（Help）**

深度睡眠预构建镜像（DeepSleep prebuilt image）在 Ameba 多核 MCU 的 NP 内核上执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOC_AMEBA_NP_CORE>
```

**定义位置（Location）**：[`soc/realtek/ameba/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ameba/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Ameba NP 预构建镜像（prebuilt images）

**配置项引用（Symbol References）**：[`CONFIG_SOC_AMEBA_NP_CORE`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_AMEBA_NP_CORE)。

<a id="CONFIG_SOC_FAMILY_REALTEK_BEE_IMAGE_HEADER"></a>

## 301.8 `CONFIG_SOC_FAMILY_REALTEK_BEE_IMAGE_HEADER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此配置将在 Zephyr 二进制文件前添加 `bee_image_header` 镜像头部。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_REALTEK_BEE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/realtek/bee/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/bee/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_BEE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_BEE`。

<a id="CONFIG_SOC_RTS5912_ULPM"></a>

## 301.9 `CONFIG_SOC_RTS5912_ULPM`

**提示（Prompt）**：Realtek RTS5912 超低功耗模式（Ultra Low Power Mode，ULPM）

**说明（Help）**

启用 RTS5912 超低功耗模式（ULPM）的电源唤醒引脚（PWR wake-up pins）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_ULPM_ENABLED && CONFIG_SOC_SERIES_RTS5912 && CONFIG_SOC_FAMILY_REALTEK_EC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_POWEROFF
```

**定义位置（Location）**：[`soc/realtek/ec/rts5912/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ec/rts5912/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RTS5912`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SOC_FAMILY_REALTEK_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_EC)、[`CONFIG_HAS_POWEROFF`](P197_lib_配置项参考_1.md#CONFIG_HAS_POWEROFF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_EC`。

<a id="CONFIG_SOC_RTS5912_ULPM_POWEROFF_BRAM"></a>

## 301.10 `CONFIG_SOC_RTS5912_ULPM_POWEROFF_BRAM`

**提示（Prompt）**：超低功耗模式中关闭 BRAM 电源（Poweroff BRAM while in ULPM）

**说明（Help）**

RTS5912 进入超低功耗模式（ULPM）时关闭 BRAM 电源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RTS5912 && CONFIG_SOC_FAMILY_REALTEK_EC
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`soc/realtek/ec/rts5912/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ec/rts5912/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RTS5912`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SOC_FAMILY_REALTEK_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_EC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_EC`。

<a id="CONFIG_SOC_RTS5915"></a>

## 301.11 `CONFIG_SOC_RTS5915`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RTS5915 是 RTS5912 的重新封装版本，无需修改驱动或软件。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_RTS5915
CONFIG_SOC_SERIES_RTS5912
CONFIG_SOC_RTS5912
```

**定义位置（Location）**：[`soc/realtek/ec/rts5912/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ec/rts5912/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RTS5915`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_SERIES_RTS5915)、[`CONFIG_SOC_SERIES_RTS5912`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SOC_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5912)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_RTS5912`。

<a id="CONFIG_SOC_SERIES_RTL8752H"></a>

## 301.12 `CONFIG_SOC_SERIES_RTL8752H`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 RTL8752H 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_REALTEK_BEE
```

**主动选择（Selects）**

```text
CONFIG_ARM
CONFIG_CPU_CORTEX_M0PLUS
CONFIG_CPU_CORTEX_M_HAS_VTOR
CONFIG_CPU_CORTEX_M_HAS_SYSTICK
CONFIG_CPU_HAS_ARM_MPU
CONFIG_CLOCK_CONTROL
CONFIG_GEN_ISR_TABLES
CONFIG_PINCTRL
CONFIG_DYNAMIC_INTERRUPTS
CONFIG_THREAD_STACK_INFO
CONFIG_SOC_EARLY_RESET_HOOK
CONFIG_SOC_EARLY_INIT_HOOK
CONFIG_SOC_LATE_INIT_HOOK
CONFIG_USE_REALTEK_BEE_OS_INTERFACE
```

**被选择（Selected by）**

```text
CONFIG_SOC_RTL8752HJL
CONFIG_SOC_RTL8752HMF
CONFIG_SOC_RTL8752HKF
CONFIG_SOC_RTL8752HJF
```

**定义位置（Location）**：[`soc/realtek/bee/rtl8752h/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/bee/rtl8752h/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_BEE)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M0PLUS`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M0PLUS)、[`CONFIG_CPU_CORTEX_M_HAS_VTOR`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_VTOR)、[`CONFIG_CPU_CORTEX_M_HAS_SYSTICK`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_SYSTICK)、[`CONFIG_CPU_HAS_ARM_MPU`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_ARM_MPU)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_GEN_ISR_TABLES`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_GEN_ISR_TABLES)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_SOC_EARLY_RESET_HOOK`](P002_kernel_配置项参考_2.md#CONFIG_SOC_EARLY_RESET_HOOK)、[`CONFIG_SOC_EARLY_INIT_HOOK`](P002_kernel_配置项参考_2.md#CONFIG_SOC_EARLY_INIT_HOOK)、[`CONFIG_SOC_LATE_INIT_HOOK`](P002_kernel_配置项参考_2.md#CONFIG_SOC_LATE_INIT_HOOK)、[`CONFIG_USE_REALTEK_BEE_OS_INTERFACE`](P230_modules_hal_realtek_配置项参考.md#CONFIG_USE_REALTEK_BEE_OS_INTERFACE)、[`CONFIG_SOC_RTL8752HJL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8752HJL)、[`CONFIG_SOC_RTL8752HMF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8752HMF)、[`CONFIG_SOC_RTL8752HKF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8752HKF)、[`CONFIG_SOC_RTL8752HJF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8752HJF)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_BEE`、`CONFIG_SOC_RTL8752HJL`、`CONFIG_SOC_RTL8752HMF`、`CONFIG_SOC_RTL8752HKF`、`CONFIG_SOC_RTL8752HJF`。

<a id="CONFIG_SOC_SERIES_RTL87X2G"></a>

## 301.13 `CONFIG_SOC_SERIES_RTL87X2G`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Realtek RTL87x2G 系列支持（series support）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_REALTEK_BEE
```

**被选择（Selected by）**

```text
CONFIG_SOC_RTL8762GC
CONFIG_SOC_RTL8762GKU
CONFIG_SOC_RTL8762GKH
CONFIG_SOC_RTL8762GRU
CONFIG_SOC_RTL8762GRH
CONFIG_SOC_RTL8762GTP
CONFIG_SOC_RTL8762GTU
CONFIG_SOC_RTL8762GTH
CONFIG_SOC_RTL8772GWF
CONFIG_SOC_RTL8772GWP
```

**定义位置（Location）**：[`soc/realtek/bee/rtl87x2g/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/bee/rtl87x2g/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_BEE)、[`CONFIG_SOC_RTL8762GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8762GC)、[`CONFIG_SOC_RTL8762GKU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8762GKU)、[`CONFIG_SOC_RTL8762GKH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8762GKH)、[`CONFIG_SOC_RTL8762GRU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8762GRU)、[`CONFIG_SOC_RTL8762GRH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8762GRH)、[`CONFIG_SOC_RTL8762GTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8762GTP)、[`CONFIG_SOC_RTL8762GTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8762GTU)、[`CONFIG_SOC_RTL8762GTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8762GTH)、[`CONFIG_SOC_RTL8772GWF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8772GWF)、[`CONFIG_SOC_RTL8772GWP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTL8772GWP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_BEE`、`CONFIG_SOC_RTL8762GC`、`CONFIG_SOC_RTL8762GKU`、`CONFIG_SOC_RTL8762GKH`、`CONFIG_SOC_RTL8762GRU`、`CONFIG_SOC_RTL8762GRH`、`CONFIG_SOC_RTL8762GTP`、`CONFIG_SOC_RTL8762GTU`、`CONFIG_SOC_RTL8762GTH`、`CONFIG_SOC_RTL8772GWF`、`CONFIG_SOC_RTL8772GWP`。

<a id="CONFIG_SOC_SERIES_RTS5912"></a>

## 301.14 `CONFIG_SOC_SERIES_RTS5912`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 REALTEK 嵌入式控制器微控制器系列支持（EC MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_REALTEK_EC
```

**被选择（Selected by）**

```text
CONFIG_SOC_RTS5912
CONFIG_SOC_RTS5915
```

**定义位置（Location）**：[`soc/realtek/ec/rts5912/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ec/rts5912/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_REALTEK_EC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_EC)、[`CONFIG_SOC_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RTS5912)、[`CONFIG_SOC_RTS5915`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_RTS5915)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_REALTEK_EC`、`CONFIG_SOC_RTS5912`。

<a id="CONFIG_SOC_SERIES_RTS5915"></a>

## 301.15 `CONFIG_SOC_SERIES_RTS5915`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RTS5915 的标识（Token）。无需修改驱动或软件。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_RTS5915
```

**定义位置（Location）**：[`soc/realtek/ec/rts5912/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ec/rts5912/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_RTS5915`](P301_soc_realtek_配置项参考.md#CONFIG_SOC_RTS5915)。

<a id="SB_CONFIG_SOC_RTS5915"></a>

## 301.16 `SB_CONFIG_SOC_RTS5915`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RTS5915 是 RTS5912 的重新封装版本，无需修改驱动或软件。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_RTS5915
SB_CONFIG_SOC_SERIES_RTS5912
SB_CONFIG_SOC_RTS5912
```

**定义位置（Location）**：[`soc/realtek/ec/rts5912/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ec/rts5912/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_RTS5915`](P301_soc_realtek_配置项参考.md#SB_CONFIG_SOC_SERIES_RTS5915)、[`SB_CONFIG_SOC_SERIES_RTS5912`](P301_soc_realtek_配置项参考.md#SB_CONFIG_SOC_SERIES_RTS5912)、[`SB_CONFIG_SOC_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RTS5912)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_RTS5912`。

<a id="SB_CONFIG_SOC_SERIES_RTL87X2G"></a>

## 301.17 `SB_CONFIG_SOC_SERIES_RTL87X2G`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Realtek RTL87x2G 系列支持（series support）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_REALTEK_BEE
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_RTL8762GC
SB_CONFIG_SOC_RTL8762GKU
SB_CONFIG_SOC_RTL8762GKH
SB_CONFIG_SOC_RTL8762GRU
SB_CONFIG_SOC_RTL8762GRH
SB_CONFIG_SOC_RTL8762GTP
SB_CONFIG_SOC_RTL8762GTU
SB_CONFIG_SOC_RTL8762GTH
SB_CONFIG_SOC_RTL8772GWF
SB_CONFIG_SOC_RTL8772GWP
```

**定义位置（Location）**：[`soc/realtek/bee/rtl87x2g/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/bee/rtl87x2g/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_REALTEK_BEE)、[`SB_CONFIG_SOC_RTL8762GC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RTL8762GC)、[`SB_CONFIG_SOC_RTL8762GKU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RTL8762GKU)、[`SB_CONFIG_SOC_RTL8762GKH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RTL8762GKH)、[`SB_CONFIG_SOC_RTL8762GRU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RTL8762GRU)、[`SB_CONFIG_SOC_RTL8762GRH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RTL8762GRH)、[`SB_CONFIG_SOC_RTL8762GTP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RTL8762GTP)、[`SB_CONFIG_SOC_RTL8762GTU`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RTL8762GTU)、[`SB_CONFIG_SOC_RTL8762GTH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RTL8762GTH)、[`SB_CONFIG_SOC_RTL8772GWF`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RTL8772GWF)、[`SB_CONFIG_SOC_RTL8772GWP`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RTL8772GWP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_REALTEK_BEE`、`SB_CONFIG_SOC_RTL8762GC`、`SB_CONFIG_SOC_RTL8762GKU`、`SB_CONFIG_SOC_RTL8762GKH`、`SB_CONFIG_SOC_RTL8762GRU`、`SB_CONFIG_SOC_RTL8762GRH`、`SB_CONFIG_SOC_RTL8762GTP`、`SB_CONFIG_SOC_RTL8762GTU`、`SB_CONFIG_SOC_RTL8762GTH`、`SB_CONFIG_SOC_RTL8772GWF`、`SB_CONFIG_SOC_RTL8772GWP`。

<a id="SB_CONFIG_SOC_SERIES_RTS5912"></a>

## 301.18 `SB_CONFIG_SOC_SERIES_RTS5912`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 REALTEK 嵌入式控制器微控制器系列支持（EC MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_REALTEK_EC
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_RTS5912
SB_CONFIG_SOC_RTS5915
```

**定义位置（Location）**：[`soc/realtek/ec/rts5912/Kconfig.soc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ec/rts5912/Kconfig.soc#L6)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_REALTEK_EC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_REALTEK_EC)、[`SB_CONFIG_SOC_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RTS5912)、[`SB_CONFIG_SOC_RTS5915`](P301_soc_realtek_配置项参考.md#SB_CONFIG_SOC_RTS5915)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_REALTEK_EC`、`SB_CONFIG_SOC_RTS5912`。

<a id="SB_CONFIG_SOC_SERIES_RTS5915"></a>

## 301.19 `SB_CONFIG_SOC_SERIES_RTS5915`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RTS5915 的标识（Token）。无需修改驱动或软件。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_SOC_RTS5915
```

**定义位置（Location）**：[`soc/realtek/ec/rts5912/Kconfig.soc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/realtek/ec/rts5912/Kconfig.soc#L19)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_RTS5915`](P301_soc_realtek_配置项参考.md#SB_CONFIG_SOC_RTS5915)。

<!-- kconfig-navigation -->

[上一章](P300_soc_raspberrypi_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P302_soc_renesas_配置项参考_1.md)
