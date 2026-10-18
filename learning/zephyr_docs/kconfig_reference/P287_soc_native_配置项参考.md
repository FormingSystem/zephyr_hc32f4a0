---
id: learning.zephyr-docs.kconfig-reference.page-287
title: "`soc/native`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第287章\_`soc/native`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/native` 的 8 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NATIVE_SIMULATOR_AUTOSTART_MCU"></a>

## 287.1 `CONFIG_NATIVE_SIMULATOR_AUTOSTART_MCU`

**提示（Prompt）**：自动启动此微控制器（Auto-start this MCU）

**说明（Help）**

硬件启动时，自动启动此 Zephyr 镜像所针对的微控制器（MCU），即使该 MCU 在其他情况下不会自动启动，例如原本需要另一个内核释放其复位。如果按硬件设计，此 MCU 无论如何都会在硬件启动时运行，则此选项不起作用。此选项旨在方便开发。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_POSIX
```

**定义位置（Location）**：[`soc/native/inf_clock/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/native/inf_clock/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_POSIX`](P287_soc_native_配置项参考.md#CONFIG_SOC_POSIX)。

<a id="CONFIG_NATIVE_SIMULATOR_EXTRA_IMAGE_PATHS"></a>

## 287.2 `CONFIG_NATIVE_SIMULATOR_EXTRA_IMAGE_PATHS`

**提示（Prompt）**：要包含的其他内核镜像（Other cores images to include）

**说明（Help）**

此选项可向原生模拟器（native simulator）提供其他 MCU／内核镜像，这些镜像可以由其他 Zephyr 构建或不同操作系统的构建生成。例如，可以使用当前应用构建生成一个内核镜像，同时将它与原生模拟器运行器（runner）及其他 MCU 镜像完成最终链接。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_POSIX
```

**定义位置（Location）**：[`soc/native/inf_clock/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/native/inf_clock/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_POSIX`](P287_soc_native_配置项参考.md#CONFIG_SOC_POSIX)。

<a id="CONFIG_NATIVE_SIMULATOR_MCU_N"></a>

## 287.3 `CONFIG_NATIVE_SIMULATOR_MCU_N`

**提示（Prompt）**：此镜像的目标 CPU 编号（CPU Number）

**说明（Help）**

此镜像针对原生模拟器（native simulator）的哪个微控制器／CPU 编号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_POSIX
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`soc/native/inf_clock/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/native/inf_clock/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_POSIX`](P287_soc_native_配置项参考.md#CONFIG_SOC_POSIX)。

<a id="CONFIG_NATIVE_SIMULATOR_NUMBER_MCUS"></a>

## 287.4 `CONFIG_NATIVE_SIMULATOR_NUMBER_MCUS`

**提示（Prompt）**：此目标的微控制器总数（Total number of MCUs）

**说明（Help）**

此目标总共有多少个非对称多处理微控制器（AMP MCUs）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_POSIX
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`soc/native/inf_clock/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/native/inf_clock/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_POSIX`](P287_soc_native_配置项参考.md#CONFIG_SOC_POSIX)。

<a id="CONFIG_NATIVE_SIMULATOR_PRIMARY_MCU_INDEX"></a>

## 287.5 `CONFIG_NATIVE_SIMULATOR_PRIMARY_MCU_INDEX`

**提示（Prompt）**：哪个 CPU 是主要／首选 CPU（primary/preferred）

**说明（Help）**

在多微控制器设备（multi MCU device）上，指定首选 MCU。例如，此 MCU 的测试命令行参数将不带任何前缀。注意，某个 MCU 被设为主要 MCU，不意味着它会首先启动，甚至不意味着它会自动启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_POSIX
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`soc/native/inf_clock/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/native/inf_clock/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_POSIX`](P287_soc_native_配置项参考.md#CONFIG_SOC_POSIX)。

<a id="CONFIG_NATIVE_SIMULATOR_STATIC_LINKING"></a>

## 287.6 `CONFIG_NATIVE_SIMULATOR_STATIC_LINKING`

**提示（Prompt）**：尝试使用静态链接（Attempt to use static linking）

**说明（Help）**

不要将最终的原生模拟器运行器（native simulator runner）与共享库（shared libraries）链接。静态链接（static linking）要求所有必需的库都存在静态库版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_POSIX
```

**定义位置（Location）**：[`soc/native/inf_clock/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/native/inf_clock/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_POSIX`](P287_soc_native_配置项参考.md#CONFIG_SOC_POSIX)。

<a id="CONFIG_SOC_POSIX"></a>

## 287.7 `CONFIG_SOC_POSIX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于 POSIX 架构的片上系统（SoC）。它模拟一个以无限快时钟运行的 CPU：每次唤醒事件（例如中断）发生后，CPU 总是在零模拟时间内运行至完成，然后返回空闲。注意，如果代码存在不会使 CPU 休眠的无限循环，进程看起来就会“挂起”（hung），因为 CPU 不休眠时模拟时间不会推进。因此，等待某件事情发生时不要使用忙等待（busy wait）；如果确实需要，请使用 `k_busy_wait()`。注意，中断处理（interrupt handling）由开发板提供。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_NATIVE_SIM
CONFIG_BOARD_NRF52_BSIM
CONFIG_BOARD_NRF5340BSIM
CONFIG_BOARD_NRF54L15BSIM
CONFIG_BOARD_NRF54LM20BSIM
```

**定义位置（Location）**：[`soc/native/inf_clock/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/native/inf_clock/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_NATIVE_SIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NATIVE_SIM)、[`CONFIG_BOARD_NRF52_BSIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF52_BSIM)、[`CONFIG_BOARD_NRF5340BSIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF5340BSIM)、[`CONFIG_BOARD_NRF54L15BSIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54L15BSIM)、[`CONFIG_BOARD_NRF54LM20BSIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NRF54LM20BSIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NATIVE_SIM`、`CONFIG_BOARD_NRF52_BSIM`、`CONFIG_BOARD_NRF5340BSIM`、`CONFIG_BOARD_NRF54L15BSIM`、`CONFIG_BOARD_NRF54LM20BSIM`。

<a id="SB_CONFIG_SOC_POSIX"></a>

## 287.8 `SB_CONFIG_SOC_POSIX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于 POSIX 架构的片上系统（SoC）。它模拟一个以无限快时钟运行的 CPU：每次唤醒事件（例如中断）发生后，CPU 总是在零模拟时间内运行至完成，然后返回空闲。注意，如果代码存在不会使 CPU 休眠的无限循环，进程看起来就会“挂起”（hung），因为 CPU 不休眠时模拟时间不会推进。因此，等待某件事情发生时不要使用忙等待（busy wait）；如果确实需要，请使用 `k_busy_wait()`。注意，中断处理（interrupt handling）由开发板提供。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NATIVE_SIM
SB_CONFIG_BOARD_NRF52_BSIM
SB_CONFIG_BOARD_NRF5340BSIM
SB_CONFIG_BOARD_NRF54L15BSIM
SB_CONFIG_BOARD_NRF54LM20BSIM
```

**定义位置（Location）**：[`soc/native/inf_clock/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/native/inf_clock/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_NATIVE_SIM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NATIVE_SIM)、[`SB_CONFIG_BOARD_NRF52_BSIM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF52_BSIM)、[`SB_CONFIG_BOARD_NRF5340BSIM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF5340BSIM)、[`SB_CONFIG_BOARD_NRF54L15BSIM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54L15BSIM)、[`SB_CONFIG_BOARD_NRF54LM20BSIM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NRF54LM20BSIM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NATIVE_SIM`、`SB_CONFIG_BOARD_NRF52_BSIM`、`SB_CONFIG_BOARD_NRF5340BSIM`、`SB_CONFIG_BOARD_NRF54L15BSIM`、`SB_CONFIG_BOARD_NRF54LM20BSIM`。

<!-- kconfig-navigation -->

[上一章](P286_soc_microchip_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P288_soc_neorv32_配置项参考.md)
