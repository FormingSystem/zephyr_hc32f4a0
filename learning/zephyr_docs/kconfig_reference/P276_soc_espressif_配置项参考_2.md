---
id: learning.zephyr-docs.kconfig-reference.page-276
title: "`soc/espressif`配置项参考（2/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第276章\_`soc/espressif`配置项参考（2/3）

本章翻译官方 Kconfig 数据库中 `soc/espressif` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ESP32_TIMER_TASK_PRIO"></a>

## 276.1 `CONFIG_ESP32_TIMER_TASK_PRIO`

**提示（Prompt）**：高分辨率 ESP 定时器任务优先级（high resolution ESP Timer task priority）

**说明（Help）**

设置 Wi-Fi 和低功耗蓝牙（BLE）外设使用的内部高分辨率 ESP 定时器（ESP Timer）的任务优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_TIMER_TASK_STACK_SIZE"></a>

## 276.2 `CONFIG_ESP32_TIMER_TASK_STACK_SIZE`

**提示（Prompt）**：高分辨率 ESP 定时器栈大小（high resolution ESP Timer stack size）

**说明（Help）**

设置 Wi-Fi 和低功耗蓝牙（BLE）外设使用的内部高分辨率 ESP 定时器（ESP Timer）的栈大小。已注册的定时器回调在此任务上下文中运行，包括分派到此处的 Wi-Fi、BLE、网格网络（mesh）、物理层（PHY）和共存（coexistence）回调。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
1536
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_ULP_COPROC_ENABLED"></a>

## 276.3 `CONFIG_ESP32_ULP_COPROC_ENABLED`

**提示（Prompt）**：超低功耗协处理器（Ultra Low Power Coprocessor，ULP）

**说明（Help）**

如果计划使用超低功耗协处理器（ULP Coprocessor），请启用此功能。启用后，菜单中将显示更多 ULP 协处理器配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_ESP32C5_LPCORE || CONFIG_SOC_ESP32C6_LPCORE || CONFIG_SOC_ESP32P4_LPCORE || CONFIG_MBOX_ESP32
```

**主动选择（Selects）**

```text
CONFIG_SOC_LATE_INIT_HOOK if CONFIG_SOC_ESP32C5_HPCORE || CONFIG_SOC_ESP32C6_HPCORE || CONFIG_SOC_ESP32P4_HPCORE
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_ESP32C5_LPCORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32C5_LPCORE)、[`CONFIG_SOC_ESP32C6_LPCORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32C6_LPCORE)、[`CONFIG_SOC_ESP32P4_LPCORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32P4_LPCORE)、[`CONFIG_MBOX_ESP32`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX_ESP32)、[`CONFIG_SOC_LATE_INIT_HOOK`](P002_kernel_配置项参考_2.md#CONFIG_SOC_LATE_INIT_HOOK)、[`CONFIG_SOC_ESP32C5_HPCORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32C5_HPCORE)、[`CONFIG_SOC_ESP32C6_HPCORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32C6_HPCORE)、[`CONFIG_SOC_ESP32P4_HPCORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32P4_HPCORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_ULP_COPROC_RESERVE_MEM"></a>

## 276.4 `CONFIG_ESP32_ULP_COPROC_RESERVE_MEM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 ULP 协处理器固件和数据预留的低功耗 SRAM（LP SRAM）。此值从 `ulp_ram` 设备树节点的大小推导得到。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_ULP_COPROC_ENABLED && (CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32P4 || CONFIG_SOC_ESP32C5_LPCORE || CONFIG_SOC_ESP32C6_LPCORE || CONFIG_SOC_ESP32P4_LPCORE) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
0x0
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_COPROC_ENABLED`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_ENABLED)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_ESP32C5_LPCORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32C5_LPCORE)、[`CONFIG_SOC_ESP32C6_LPCORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32C6_LPCORE)、[`CONFIG_SOC_ESP32P4_LPCORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32P4_LPCORE)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_ULP_COPROC_TYPE"></a>

## 276.5 `CONFIG_ESP32_ULP_COPROC_TYPE`

**提示（Prompt）**：ULP 协处理器类型（Coprocessor type）

**说明（Help）**

选择 ULP 协处理器类型：ULP 有限状态机（Finite State Machine，FSM）或 ULP RISC-V。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_ULP_COPROC_ENABLED && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE if CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32P4
```

**可选项（Choices）**

```text
CONFIG_ESP32_ULP_COPROC_TYPE_FSM
CONFIG_ESP32_ULP_COPROC_TYPE_RISCV
CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_COPROC_ENABLED`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_ENABLED)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_ESP32_ULP_COPROC_TYPE_FSM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE_FSM)、[`CONFIG_ESP32_ULP_COPROC_TYPE_RISCV`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE_RISCV)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_ESP32_ULP_COPROC_TYPE_FSM"></a>

## 276.6 `CONFIG_ESP32_ULP_COPROC_TYPE_FSM`

**提示（Prompt）**：ULP 有限状态机（Finite State Machine，FSM）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3) && <choice CONFIG_ESP32_ULP_COPROC_TYPE>
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → ULP 协处理器类型（Coprocessor type）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_ESP32_ULP_COPROC_TYPE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE)。

<a id="CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE"></a>

## 276.7 `CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE`

**提示（Prompt）**：低功耗内核 RISC-V（LP core RISC-V）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32P4) && <choice CONFIG_ESP32_ULP_COPROC_TYPE>
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → ULP 协处理器类型（Coprocessor type）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_ESP32_ULP_COPROC_TYPE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_ESP32_ULP_COPROC_TYPE_RISCV"></a>

## 276.8 `CONFIG_ESP32_ULP_COPROC_TYPE_RISCV`

**提示（Prompt）**：ULP RISC-V 超低功耗协处理器

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3) && <choice CONFIG_ESP32_ULP_COPROC_TYPE>
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → ULP 协处理器类型（Coprocessor type）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_ESP32_ULP_COPROC_TYPE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE)。

<a id="CONFIG_ESP32_ULP_HP_UART_CONSOLE_PRINT"></a>

## 276.9 `CONFIG_ESP32_ULP_HP_UART_CONSOLE_PRINT`

**提示（Prompt）**：将 lp_core_printf 路由到控制台高性能 UART（HP-UART）

**说明（Help）**

设置此项可将 `lp_core_printf` 路由到控制台高性能 UART（HP-UART）。这样无需连接低功耗 UART（LP-UART），便可轻松查看低功耗内核（LP core）的打印输出。此选项有以下限制：

1. 高性能内核（HP-Core）与低功耗内核（LP-Core）访问 HP-UART 时没有互斥机制（mutual exclusion）；如果两个内核都大量输出日志，字符串可能相互混杂。
2. HP-UART 只能在 HP-Core 运行时工作；如果 HP-Core 处于深度睡眠（deep sleep），LP-Core 将无法向控制台 HP-UART 打印。

由于这些限制，仅建议将此选项用于便捷调试。对于更正式的使用场景，应使用 LP-UART。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → ULP 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_ULP_LP_CORE_LP_TIMER_SLEEP_DURATION_US"></a>

## 276.10 `CONFIG_ESP32_ULP_LP_CORE_LP_TIMER_SLEEP_DURATION_US`

**提示（Prompt）**：低功耗定时器睡眠时长，单位为微秒（LP timer sleep duration）

**说明（Help）**

使用低功耗定时器（LP timer）作为唤醒源时，低功耗内核两次唤醒之间的睡眠时长，单位为微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_TIMER && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
2000000
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_TIMER`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_TIMER)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE"></a>

## 276.11 `CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE`

**提示（Prompt）**：低功耗内核唤醒源（LP core wakeup source）

**说明（Help）**

选择低功耗内核（LP core）的唤醒源（wakeup source）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_HP_CPU
```

**可选项（Choices）**

```text
CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_HP_CPU
CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_TIMER
CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_IO
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_HP_CPU`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_HP_CPU)、[`CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_TIMER`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_TIMER)、[`CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_IO`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_IO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_HP_CPU"></a>

## 276.12 `CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_HP_CPU`

**提示（Prompt）**：高性能 CPU，单次唤醒（HP CPU, single wakeup）

**说明（Help）**

由高性能 CPU（HP CPU）启动低功耗内核（LP core）一次。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE>
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → 低功耗内核唤醒源（LP core wakeup source）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE)。

<a id="CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_IO"></a>

## 276.13 `CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_IO`

**提示（Prompt）**：低功耗 IO，GPIO 中断（LP IO, GPIO interrupt）

**说明（Help）**

低功耗内核（LP core）因低功耗 IO 中断（LP IO interrupt）而唤醒。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE>
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → 低功耗内核唤醒源（LP core wakeup source）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE)。

<a id="CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_TIMER"></a>

## 276.14 `CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE_LP_TIMER`

**提示（Prompt）**：低功耗定时器，周期性唤醒（LP timer, periodic wakeup）

**说明（Help）**

低功耗内核（LP core）由低功耗定时器（LP timer）周期性唤醒。睡眠时长由 `ESP32_ULP_LP_CORE_LP_TIMER_SLEEP_DURATION_US` 配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE>
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → 低功耗内核唤醒源（LP core wakeup source）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_LP_CORE_WAKEUP_SOURCE)。

<a id="CONFIG_ESP32_ULP_NORESET_UNDER_DEBUG"></a>

## 276.15 `CONFIG_ESP32_ULP_NORESET_UNDER_DEBUG`

**提示（Prompt）**：连接调试器时避免复位低功耗内核（LP core）

**说明（Help）**

启用此功能可在已连接调试器（debugger）时避免在睡眠模式中复位低功耗内核（LP core），否则已配置的硬件断点（HW breakpoints）和 `dcsr.ebreak*` 位会丢失。这是在硬件修复之前采用的规避措施（workaround）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → ULP 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_ULP_PANIC_OUTPUT_ENABLE"></a>

## 276.16 `CONFIG_ESP32_ULP_PANIC_OUTPUT_ENABLE`

**提示（Prompt）**：致命错误处理程序输出到低功耗 UART（Panic handler outputs to LP UART）

**说明（Help）**

设置此项可启用致命错误处理程序（panic handler）。启用后，低功耗内核（LP Core）会通过 LP UART 输出致命错误转储（panic dump），类似主内核的行为。输出要求 LP UART 已完成初始化和配置。禁用此选项会省去致命错误处理功能的链接，从而减小低功耗内核二进制文件体积。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → ULP 调试选项（Debugging Options）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_ULP_RISCV_INTERRUPT_ENABLE"></a>

## 276.17 `CONFIG_ESP32_ULP_RISCV_INTERRUPT_ENABLE`

**提示（Prompt）**：ULP RISC-V 中断（interrupts）

**说明（Help）**

开启此设置以启用 ULP RISC-V 内核上的中断（interrupts）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_ULP_COPROC_TYPE_RISCV && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP） → ULP RISC-V 设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_COPROC_TYPE_RISCV`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE_RISCV)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_ULP_ROM_PRINT_ENABLE"></a>

## 276.18 `CONFIG_ESP32_ULP_ROM_PRINT_ENABLE`

**提示（Prompt）**：使用低功耗 ROM 的打印工具（Print utilities from LP ROM）

**说明（Help）**

设置此项以启用低功耗 ROM（LP ROM）中的 printf 功能。通过不链接 RAM 代码中的 printf 实现，此选项有助于减小低功耗内核（LP core）的二进制文件体积。注意：要使 LP ROM 打印正常工作，必须确保低功耗内核从 LP ROM 启动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_ULP_TRAP_WAKEUP"></a>

## 276.19 `CONFIG_ESP32_ULP_TRAP_WAKEUP`

**提示（Prompt）**：低功耗内核发生异常时唤醒高性能 CPU（Wakeup HP-CPU）

**说明（Help）**

设置此项后，低功耗内核（LP-core）发生异常（exception）时，也会向高性能 CPU（HP-CPU）发送唤醒信号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/espressif/Kconfig.ulp:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig.ulp#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 超低功耗协处理器（Ultra Low Power Coprocessor，ULP）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_ULP_COPROC_TYPE_LP_CORE)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES"></a>

## 276.20 `CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES`

**提示（Prompt）**：由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**说明（Help）**

配置由 IEEE 全局管理的 MAC 地址（universally administered MAC address）数量。初始化时，每个网络接口的 MAC 地址都从单个基础 MAC 地址（base MAC address）生成或派生。

如果全局 MAC 地址数量为四个，则全部四个接口（Wi-Fi 站点、Wi-Fi 软件接入点 softap、蓝牙和以太网）都会获得全局管理的 MAC 地址。它们分别通过在基础 MAC 地址的最后一个八位组（octet）上加 0、1、2、3 依次生成。

如果全局 MAC 地址数量为两个，则只有两个接口（Wi-Fi 站点和蓝牙）获得全局管理的 MAC 地址，分别通过在基础 MAC 地址上加 0 和 1 依次生成。其余两个接口（Wi-Fi 软件接入点和以太网）获得本地 MAC 地址（local MAC address），分别从 Wi-Fi 站点和蓝牙的全局 MAC 地址派生。

使用默认的 Espressif 分配的基础 MAC 地址时，两种设置均可使用。使用自定义的全局 MAC 地址范围时，正确设置取决于该范围内的地址分配方式，即每台设备分配 2 个还是 4 个地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**可选项（Choices）**

```text
CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig.mac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig.mac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES_FOUR`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES_TWO`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES_TWO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES_FOUR"></a>

## 276.21 `CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES_FOUR`

**提示（Prompt）**：四个（Four）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig.mac:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig.mac#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`。

<a id="CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES_TWO"></a>

## 276.22 `CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES_TWO`

**提示（Prompt）**：两个（Two）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig.mac:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig.mac#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`。

<a id="CONFIG_ESP32_USE_UNSUPPORTED_REVISION"></a>

## 276.23 `CONFIG_ESP32_USE_UNSUPPORTED_REVISION`

**提示（Prompt）**：使用不受支持的 ESP32 修订版 Rev 0／1（unsupported ESP32 revision）

**说明（Help）**

ESP32 SoC 有多个修订版（revision），其中一些不受当前实现支持，例如 REV0 和 REV1。如果需要这些修订版，可以设置此选项以启用支持。注意，不推荐这样做，并且可能导致意外行为（unexpected behavior）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESPTOOLPY_AFTER"></a>

## 276.24 `CONFIG_ESPTOOLPY_AFTER`

**提示（Prompt）**：烧录之后（After flashing）

**说明（Help）**

配置 esptool.py 是否在烧录后复位 ESP32。自动复位依赖串口的 RTS 和 DTR 信号已连接到 ESP32；大多数 USB 开发板在内部已完成这些连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESPTOOLPY_AFTER_RESET
```

**可选项（Choices）**

```text
CONFIG_ESPTOOLPY_AFTER_RESET
CONFIG_ESPTOOLPY_AFTER_NORESET
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESPTOOLPY_AFTER_RESET`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_AFTER_RESET)、[`CONFIG_ESPTOOLPY_AFTER_NORESET`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_AFTER_NORESET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESPTOOLPY_AFTER_NORESET"></a>

## 276.25 `CONFIG_ESPTOOLPY_AFTER_NORESET`

**提示（Prompt）**：停留在引导加载程序（Stay in bootloader）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_AFTER>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:241`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L241)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 烧录之后（After flashing）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_AFTER`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_AFTER)。

<a id="CONFIG_ESPTOOLPY_AFTER_RESET"></a>

## 276.26 `CONFIG_ESPTOOLPY_AFTER_RESET`

**提示（Prompt）**：烧录后复位（Reset after flashing）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_AFTER>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:238`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L238)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 烧录之后（After flashing）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_AFTER`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_AFTER)。

<a id="CONFIG_ESPTOOLPY_BEFORE"></a>

## 276.27 `CONFIG_ESPTOOLPY_BEFORE`

**提示（Prompt）**：烧录之前（Before flashing）

**说明（Help）**

配置 esptool.py 是否在烧录前复位 ESP32。自动复位依赖串口的 RTS 和 DTR 信号已连接到 ESP32；大多数 USB 开发板在内部已完成这些连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESPTOOLPY_BEFORE_RESET
```

**可选项（Choices）**

```text
CONFIG_ESPTOOLPY_BEFORE_RESET
CONFIG_ESPTOOLPY_BEFORE_NORESET
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESPTOOLPY_BEFORE_RESET`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_BEFORE_RESET)、[`CONFIG_ESPTOOLPY_BEFORE_NORESET`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_BEFORE_NORESET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESPTOOLPY_BEFORE_NORESET"></a>

## 276.28 `CONFIG_ESPTOOLPY_BEFORE_NORESET`

**提示（Prompt）**：不复位（No reset）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_BEFORE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L219)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 烧录之前（Before flashing）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_BEFORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_BEFORE)。

<a id="CONFIG_ESPTOOLPY_BEFORE_RESET"></a>

## 276.29 `CONFIG_ESPTOOLPY_BEFORE_RESET`

**提示（Prompt）**：复位进入引导加载程序（Reset to bootloader）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_BEFORE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 烧录之前（Before flashing）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_BEFORE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_BEFORE)。

<a id="CONFIG_ESPTOOLPY_FLASHFREQ"></a>

## 276.30 `CONFIG_ESPTOOLPY_FLASHFREQ`

**提示（Prompt）**：Flash SPI 速率（Flash SPI speed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESPTOOLPY_FLASHFREQ_40M if CONFIG_SOC_SERIES_ESP32
CONFIG_ESPTOOLPY_FLASHFREQ_48M if CONFIG_SOC_SERIES_ESP32H2
CONFIG_ESPTOOLPY_FLASHFREQ_60M if CONFIG_SOC_SERIES_ESP32C2
CONFIG_ESPTOOLPY_FLASHFREQ_80M if CONFIG_ESPTOOLPY_FLASHFREQ_80M_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ESPTOOLPY_FLASHFREQ_120M
CONFIG_ESPTOOLPY_FLASHFREQ_80M
CONFIG_ESPTOOLPY_FLASHFREQ_60M
CONFIG_ESPTOOLPY_FLASHFREQ_48M
CONFIG_ESPTOOLPY_FLASHFREQ_40M
CONFIG_ESPTOOLPY_FLASHFREQ_26M
CONFIG_ESPTOOLPY_FLASHFREQ_20M
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESPTOOLPY_FLASHFREQ_40M`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ_40M)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_ESPTOOLPY_FLASHFREQ_48M`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ_48M)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_ESPTOOLPY_FLASHFREQ_60M`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ_60M)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_ESPTOOLPY_FLASHFREQ_80M`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ_80M)、[`CONFIG_ESPTOOLPY_FLASHFREQ_80M_DEFAULT`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ_80M_DEFAULT)、[`CONFIG_ESPTOOLPY_FLASHFREQ_120M`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ_120M)、[`CONFIG_ESPTOOLPY_FLASHFREQ_26M`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ_26M)、[`CONFIG_ESPTOOLPY_FLASHFREQ_20M`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ_20M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32C2`。

<a id="CONFIG_ESPTOOLPY_FLASHFREQ_120M"></a>

## 276.31 `CONFIG_ESPTOOLPY_FLASHFREQ_120M`

**提示（Prompt）**：120 兆赫（120 MHz）

**说明（Help）**

- Flash 的 120 MHz 单倍数据速率模式（SDR mode）稳定。
- Flash 的 120 MHz 双倍数据速率模式（DDR mode）是实验性功能，在温度稳定时可以工作。

风险：如果芯片在某一温度下上电，之后温度升高或降低约 20 摄氏度（取决于具体芯片），程序会随机崩溃。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32S3) && CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_STR && <choice CONFIG_ESPTOOLPY_FLASHFREQ>
```

**主动选择（Selects）**

```text
CONFIG_SPI_FLASH_HPM_ENABLE if CONFIG_SOC_SERIES_ESP32S3
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash SPI 速率（Flash SPI speed）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_STR`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_STR)、[`CONFIG_ESPTOOLPY_FLASHFREQ`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ)、[`CONFIG_SPI_FLASH_HPM_ENABLE`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPI_FLASH_HPM_ENABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`。

<a id="CONFIG_ESPTOOLPY_FLASHFREQ_20M"></a>

## 276.32 `CONFIG_ESPTOOLPY_FLASHFREQ_20M`

**提示（Prompt）**：20 兆赫（20 MHz）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHFREQ>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash SPI 速率（Flash SPI speed）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHFREQ`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ)。

<a id="CONFIG_ESPTOOLPY_FLASHFREQ_26M"></a>

## 276.33 `CONFIG_ESPTOOLPY_FLASHFREQ_26M`

**提示（Prompt）**：26 兆赫（26 MHz）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_ESP32S3 && <choice CONFIG_ESPTOOLPY_FLASHFREQ>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash SPI 速率（Flash SPI speed）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_ESPTOOLPY_FLASHFREQ`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ)。

<a id="CONFIG_ESPTOOLPY_FLASHFREQ_40M"></a>

## 276.34 `CONFIG_ESPTOOLPY_FLASHFREQ_40M`

**提示（Prompt）**：40 兆赫（40 MHz）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHFREQ>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash SPI 速率（Flash SPI speed）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHFREQ`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ)。

<a id="CONFIG_ESPTOOLPY_FLASHFREQ_48M"></a>

## 276.35 `CONFIG_ESPTOOLPY_FLASHFREQ_48M`

**提示（Prompt）**：48 兆赫（48 MHz）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHFREQ>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash SPI 速率（Flash SPI speed）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHFREQ`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ)。

<a id="CONFIG_ESPTOOLPY_FLASHFREQ_60M"></a>

## 276.36 `CONFIG_ESPTOOLPY_FLASHFREQ_60M`

**提示（Prompt）**：60 兆赫（60 MHz）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHFREQ>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash SPI 速率（Flash SPI speed）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHFREQ`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ)。

<a id="CONFIG_ESPTOOLPY_FLASHFREQ_80M"></a>

## 276.37 `CONFIG_ESPTOOLPY_FLASHFREQ_80M`

**提示（Prompt）**：80 兆赫（80 MHz）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHFREQ>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash SPI 速率（Flash SPI speed）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHFREQ`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ)。

<a id="CONFIG_ESPTOOLPY_FLASHFREQ_80M_DEFAULT"></a>

## 276.38 `CONFIG_ESPTOOLPY_FLASHFREQ_80M_DEFAULT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

这是不可见配置项，用于定义默认使用 80MHz Flash SPI 速率的目标（targets）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32C3 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32P4
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32C3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_ESPTOOLPY_FLASHMODE"></a>

## 276.39 `CONFIG_ESPTOOLPY_FLASHMODE`

**提示（Prompt）**：Flash SPI 模式（Flash SPI mode）

**说明（Help）**

烧录 Flash 芯片时使用的模式，以及二进制程序运行时使用的默认模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESPTOOLPY_FLASHMODE_DIO
CONFIG_ESPTOOLPY_FLASHMODE_OPI if CONFIG_ESPTOOLPY_OCT_FLASH
```

**可选项（Choices）**

```text
CONFIG_ESPTOOLPY_FLASHMODE_QIO
CONFIG_ESPTOOLPY_FLASHMODE_QOUT
CONFIG_ESPTOOLPY_FLASHMODE_DIO
CONFIG_ESPTOOLPY_FLASHMODE_DOUT
CONFIG_ESPTOOLPY_FLASHMODE_OPI
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESPTOOLPY_FLASHMODE_DIO`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHMODE_DIO)、[`CONFIG_ESPTOOLPY_FLASHMODE_OPI`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHMODE_OPI)、[`CONFIG_ESPTOOLPY_OCT_FLASH`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_OCT_FLASH)、[`CONFIG_ESPTOOLPY_FLASHMODE_QIO`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHMODE_QIO)、[`CONFIG_ESPTOOLPY_FLASHMODE_QOUT`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHMODE_QOUT)、[`CONFIG_ESPTOOLPY_FLASHMODE_DOUT`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHMODE_DOUT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESPTOOLPY_FLASHMODE_DIO"></a>

## 276.40 `CONFIG_ESPTOOLPY_FLASHMODE_DIO`

**提示（Prompt）**：双线 IO（DIO）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ESPTOOLPY_OCT_FLASH && <choice CONFIG_ESPTOOLPY_FLASHMODE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash SPI 模式（Flash SPI mode）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_OCT_FLASH`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_OCT_FLASH)、[`CONFIG_ESPTOOLPY_FLASHMODE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHMODE)。

<a id="CONFIG_ESPTOOLPY_FLASHMODE_DOUT"></a>

## 276.41 `CONFIG_ESPTOOLPY_FLASHMODE_DOUT`

**提示（Prompt）**：双线输出（DOUT）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ESPTOOLPY_OCT_FLASH && <choice CONFIG_ESPTOOLPY_FLASHMODE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash SPI 模式（Flash SPI mode）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_OCT_FLASH`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_OCT_FLASH)、[`CONFIG_ESPTOOLPY_FLASHMODE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHMODE)。

<a id="CONFIG_ESPTOOLPY_FLASHMODE_OPI"></a>

## 276.42 `CONFIG_ESPTOOLPY_FLASHMODE_OPI`

**提示（Prompt）**：八线外设接口（OPI）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPTOOLPY_OCT_FLASH && <choice CONFIG_ESPTOOLPY_FLASHMODE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash SPI 模式（Flash SPI mode）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_OCT_FLASH`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_OCT_FLASH)、[`CONFIG_ESPTOOLPY_FLASHMODE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHMODE)。

<a id="CONFIG_ESPTOOLPY_FLASHMODE_QIO"></a>

## 276.43 `CONFIG_ESPTOOLPY_FLASHMODE_QIO`

**提示（Prompt）**：四线 IO（QIO）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ESPTOOLPY_OCT_FLASH && <choice CONFIG_ESPTOOLPY_FLASHMODE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash SPI 模式（Flash SPI mode）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_OCT_FLASH`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_OCT_FLASH)、[`CONFIG_ESPTOOLPY_FLASHMODE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHMODE)。

<a id="CONFIG_ESPTOOLPY_FLASHMODE_QOUT"></a>

## 276.44 `CONFIG_ESPTOOLPY_FLASHMODE_QOUT`

**提示（Prompt）**：四线输出（QOUT）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ESPTOOLPY_OCT_FLASH && <choice CONFIG_ESPTOOLPY_FLASHMODE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash SPI 模式（Flash SPI mode）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_OCT_FLASH`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_OCT_FLASH)、[`CONFIG_ESPTOOLPY_FLASHMODE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHMODE)。

<a id="CONFIG_ESPTOOLPY_FLASHSIZE"></a>

## 276.45 `CONFIG_ESPTOOLPY_FLASHSIZE`

**提示（Prompt）**：Flash 大小（Flash size）

**说明（Help）**

SPI Flash 大小，单位为兆字节（megabytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESPTOOLPY_FLASHSIZE_2MB
```

**可选项（Choices）**

```text
CONFIG_ESPTOOLPY_FLASHSIZE_1MB
CONFIG_ESPTOOLPY_FLASHSIZE_2MB
CONFIG_ESPTOOLPY_FLASHSIZE_4MB
CONFIG_ESPTOOLPY_FLASHSIZE_8MB
CONFIG_ESPTOOLPY_FLASHSIZE_16MB
CONFIG_ESPTOOLPY_FLASHSIZE_32MB
CONFIG_ESPTOOLPY_FLASHSIZE_64MB
CONFIG_ESPTOOLPY_FLASHSIZE_128MB
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESPTOOLPY_FLASHSIZE_2MB`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE_2MB)、[`CONFIG_ESPTOOLPY_FLASHSIZE_1MB`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE_1MB)、[`CONFIG_ESPTOOLPY_FLASHSIZE_4MB`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE_4MB)、[`CONFIG_ESPTOOLPY_FLASHSIZE_8MB`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE_8MB)、[`CONFIG_ESPTOOLPY_FLASHSIZE_16MB`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE_16MB)、[`CONFIG_ESPTOOLPY_FLASHSIZE_32MB`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE_32MB)、[`CONFIG_ESPTOOLPY_FLASHSIZE_64MB`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE_64MB)、[`CONFIG_ESPTOOLPY_FLASHSIZE_128MB`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE_128MB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESPTOOLPY_FLASHSIZE_128MB"></a>

## 276.46 `CONFIG_ESPTOOLPY_FLASHSIZE_128MB`

**提示（Prompt）**：128 兆字节（128 MB）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHSIZE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHSIZE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE)。

<a id="CONFIG_ESPTOOLPY_FLASHSIZE_16MB"></a>

## 276.47 `CONFIG_ESPTOOLPY_FLASHSIZE_16MB`

**提示（Prompt）**：16 兆字节（16 MB）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHSIZE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHSIZE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE)。

<a id="CONFIG_ESPTOOLPY_FLASHSIZE_1MB"></a>

## 276.48 `CONFIG_ESPTOOLPY_FLASHSIZE_1MB`

**提示（Prompt）**：1 兆字节（1 MB）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHSIZE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHSIZE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE)。

<a id="CONFIG_ESPTOOLPY_FLASHSIZE_2MB"></a>

## 276.49 `CONFIG_ESPTOOLPY_FLASHSIZE_2MB`

**提示（Prompt）**：2 兆字节（2 MB）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHSIZE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHSIZE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE)。

<a id="CONFIG_ESPTOOLPY_FLASHSIZE_32MB"></a>

## 276.50 `CONFIG_ESPTOOLPY_FLASHSIZE_32MB`

**提示（Prompt）**：32 兆字节（32 MB）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHSIZE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHSIZE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE)。

<a id="CONFIG_ESPTOOLPY_FLASHSIZE_4MB"></a>

## 276.51 `CONFIG_ESPTOOLPY_FLASHSIZE_4MB`

**提示（Prompt）**：4 兆字节（4 MB）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHSIZE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHSIZE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE)。

<a id="CONFIG_ESPTOOLPY_FLASHSIZE_64MB"></a>

## 276.52 `CONFIG_ESPTOOLPY_FLASHSIZE_64MB`

**提示（Prompt）**：64 兆字节（64 MB）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHSIZE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L176)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHSIZE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE)。

<a id="CONFIG_ESPTOOLPY_FLASHSIZE_8MB"></a>

## 276.53 `CONFIG_ESPTOOLPY_FLASHSIZE_8MB`

**提示（Prompt）**：8 兆字节（8 MB）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASHSIZE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash 大小（Flash size）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHSIZE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHSIZE)。

<a id="CONFIG_ESPTOOLPY_FLASH_MODE_AUTO_DETECT"></a>

## 276.54 `CONFIG_ESPTOOLPY_FLASH_MODE_AUTO_DETECT`

**提示（Prompt）**：自动选择 Flash 模式，请阅读帮助（Choose flash mode automatically）

**说明（Help）**

此配置选项帮助判断 Flash 使用四线（Quad）还是八线（Octal），但需注意以下限制：

1. 如果 Flash 芯片为八线器件，即使在 `ESPTOOLPY_FLASHMODE` 中选择了 `QIO`、`QOUT`、`DIO`、`DOUT` 之一，代码也会自动将模式改为 `OPI`，采样模式为 STR。
2. 如果 Flash 芯片为四线器件，即使在 `ESPTOOLPY_FLASHMODE` 中选择了 `OPI`，代码也会自动将模式改为 `DIO`。
3. 如果已经确定使用八线 Flash，请不要依赖此选项，而应启用 `ESPTOOLPY_OCT_FLASH`，随后便可在 `ESPTOOLPY_FLASH_SAMPLE_MODE` 中选择 `DTR` 采样模式。否则仅可使用 `STR` 模式。
4. 启用此功能会减少约 900 字节的可用内部 RAM。如果指令 RAM（IRAM）空间不足，并且已知 Flash 类型，请禁用此项并选择相应的 Flash 类型选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE"></a>

## 276.55 `CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE`

**提示（Prompt）**：Flash 采样模式（Flash Sampling Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_DTR if CONFIG_ESPTOOLPY_OCT_FLASH
CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_STR if !CONFIG_ESPTOOLPY_OCT_FLASH
```

**可选项（Choices）**

```text
CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_STR
CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_DTR
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_DTR`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_DTR)、[`CONFIG_ESPTOOLPY_OCT_FLASH`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_OCT_FLASH)、[`CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_STR`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_STR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_DTR"></a>

## 276.56 `CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_DTR`

**提示（Prompt）**：双传输速率模式（DTR Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPTOOLPY_OCT_FLASH && <choice CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash 采样模式（Flash Sampling Mode）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_OCT_FLASH`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_OCT_FLASH)、[`CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE)。

<a id="CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_STR"></a>

## 276.57 `CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE_STR`

**提示（Prompt）**：单传输速率模式（STR Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Flash 采样模式（Flash Sampling Mode）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASH_SAMPLE_MODE)。

<a id="CONFIG_ESPTOOLPY_HEADER_FLASHSIZE_UPDATE"></a>

## 276.58 `CONFIG_ESPTOOLPY_HEADER_FLASHSIZE_UPDATE`

**提示（Prompt）**：烧录引导加载程序时检测 Flash 大小（Detect flash size）

**说明（Help）**

设置此项后，烧录项目时会自动检测目标芯片的 Flash 大小，并在烧录前更新引导加载程序镜像（bootloader image）。启用此项会关闭基于 SHA256 摘要（digest）的镜像损坏保护，因为烧录前更新引导加载程序镜像会使摘要失效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESPTOOLPY_OCT_FLASH"></a>

## 276.59 `CONFIG_ESPTOOLPY_OCT_FLASH`

**提示（Prompt）**：使用八线 Flash（Use Octal Flash）

**说明（Help）**

仅当开发板实际装有八线（OPI）Flash 芯片时才启用。此项会选择 OPI Flash 模式和经过调整的 DTR 采样时序。Flash 与 PSRAM 的线路模式（line mode）相互独立：多数八线 PSRAM 模组（例如 N8R8、N16R8）搭配的是八线 PSRAM 和四线 Flash，因此除非 Flash 芯片本身为八线器件，否则应保持此项禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.esptool:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.esptool#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_APPCPU_DRAM_SIZE"></a>

## 276.60 `CONFIG_ESP_APPCPU_DRAM_SIZE`

**提示（Prompt）**：ESP32* 应用 CPU 数据 RAM 大小（APPCPU DRAM size）

**说明（Help）**

定义应用 CPU 数据 RAM 区域（APPCPU DRAM area）的大小，单位为字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ENABLE_APPCPU && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
0x10000
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.amp:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.amp#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 非对称多处理配置（AMP Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ENABLE_APPCPU`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ENABLE_APPCPU)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_APPCPU_DROM_SIZE"></a>

## 276.61 `CONFIG_ESP_APPCPU_DROM_SIZE`

**提示（Prompt）**：ESP32* 应用 CPU 数据 RAM 大小（APPCPU DRAM size）

**说明（Help）**

定义应用 CPU 数据 ROM 区域（APPCPU DROM area）的大小，单位为字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ENABLE_APPCPU && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
0x100000
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.amp:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.amp#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 非对称多处理配置（AMP Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ENABLE_APPCPU`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ENABLE_APPCPU)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_APPCPU_IRAM_SIZE"></a>

## 276.62 `CONFIG_ESP_APPCPU_IRAM_SIZE`

**提示（Prompt）**：ESP32* 应用 CPU 指令 RAM 大小（APPCPU IRAM size）

**说明（Help）**

定义应用 CPU 指令 RAM 区域（APPCPU IRAM area）的大小，单位为字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ENABLE_APPCPU && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
0x10000
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.amp:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.amp#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 非对称多处理配置（AMP Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ENABLE_APPCPU`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ENABLE_APPCPU)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_APPCPU_IROM_SIZE"></a>

## 276.63 `CONFIG_ESP_APPCPU_IROM_SIZE`

**提示（Prompt）**：ESP32* 应用 CPU 指令 ROM 大小（APPCPU IROM size）

**说明（Help）**

定义应用 CPU 指令 ROM 区域（APPCPU IROM area）的大小，单位为字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ENABLE_APPCPU && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
0x100000
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.amp:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.amp#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 非对称多处理配置（AMP Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ENABLE_APPCPU`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ENABLE_APPCPU)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_FLASH_ENCRYPTION"></a>

## 276.64 `CONFIG_ESP_FLASH_ENCRYPTION`

**提示（Prompt）**：硬件 Flash 加密兼容性（Hardware flash encryption compatibility）

**说明（Help）**

启用 Espressif 硬件 Flash 加密与 MCUboot Espressif 移植版（Port）的兼容支持。必须在引导加载程序中启用 Flash 加密配置，并在 Zephyr 设备树中将 Flash 写入块大小（write block size）设为 32 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ESP_SIMPLE_BOOT && !CONFIG_MCUBOOT && "0" = 32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ESP_SIMPLE_BOOT`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SIMPLE_BOOT)、[`CONFIG_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_SIMPLE_BOOT"></a>

## 276.65 `CONFIG_ESP_SIMPLE_BOOT`

**提示（Prompt）**：简单启动方式（Simple Boot method）

**说明（Help）**

简单启动（Simple Boot）是一种不需要第二阶段引导加载程序（2nd stage bootloader）的启动方式。输出为单个镜像，应烧录到所用 SoC 定义的偏移处。请注意，此方式能够在完成所有内存设置后启动系统，但不提供其他功能，例如安全启动（secure boot）、空中升级（OTA）或槽位管理（slots management）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if !CONFIG_BOOTLOADER_MCUBOOT && !CONFIG_MCUBOOT
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_SPIRAM"></a>

## 276.66 `CONFIG_ESP_SPIRAM`

**提示（Prompt）**：外部 SPI 连接 RAM 支持（external SPI-connected RAM）

**说明（Help）**

启用外部 SPI RAM 芯片支持；该芯片与主 SPI Flash 芯片并行连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
n if CONFIG_MCUBOOT
n if CONFIG_ESP32_USE_UNSUPPORTED_REVISION && CONFIG_SOC_SERIES_ESP32
```

**被选择（Selected by）**

```text
CONFIG_DISPLAY_ESP32_DSI
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT)、[`CONFIG_ESP32_USE_UNSUPPORTED_REVISION`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP32_USE_UNSUPPORTED_REVISION)、[`CONFIG_DISPLAY_ESP32_DSI`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_ESP32_DSI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_SPIRAM_BSS_RELOC_LIBS_AND_OBJS"></a>

## 276.67 `CONFIG_ESP_SPIRAM_BSS_RELOC_LIBS_AND_OBJS`

**提示（Prompt）**：需要将 BSS 重定位到 PSRAM 的库与目标文件（Libraries and objects）

**说明（Help）**

以空格分隔的库或目标文件名称列表，例如 `libfile.a` 或 `file.o`。启用 `CONFIG_ESP_SPIRAM` 时，它们的 `.bss` 段将放入 `.ext_ram.data`。留空则不重定位任何 BSS。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_SPIRAM && CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:255`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L255)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 将 BSS 重定位到 PSRAM（Relocate BSS to PSRAM）

**配置项引用（Symbol References）**：[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_SPIRAM_HEAP_SIZE"></a>

## 276.68 `CONFIG_ESP_SPIRAM_HEAP_SIZE`

**提示（Prompt）**：SPI RAM 堆大小（Size of SPIRAM heap）

**说明（Help）**

指定 SPI RAM 堆（SPIRAM heap）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
262128 if CONFIG_SYS_HEAP_SMALL_ONLY
1048576 if !CONFIG_SYS_HEAP_SMALL_ONLY
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config）

**配置项引用（Symbol References）**：[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SYS_HEAP_SMALL_ONLY`](P199_lib_配置项参考_3.md#CONFIG_SYS_HEAP_SMALL_ONLY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_SPIRAM_MEMTEST"></a>

## 276.69 `CONFIG_ESP_SPIRAM_MEMTEST`

**提示（Prompt）**：初始化 SPI RAM 时运行内存测试（memory test）

**说明（Help）**

初始化时运行内存测试（memory test）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config）

**配置项引用（Symbol References）**：[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_SPIRAM_SIZE"></a>

## 276.70 `CONFIG_ESP_SPIRAM_SIZE`

**提示（Prompt）**：SPI RAM 器件大小（Size of SPIRAM part）

**说明（Help）**

指定 SPI RAM 器件（SPIRAM part）的大小。注意：在 ESP32 上，如果 SPI RAM 大于 4MB，只有低地址的 4MB 可通过 `k_malloc()` 分配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
0 if n
0
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config）

**配置项引用（Symbol References）**：[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_USB_SERIAL_JTAG_ENABLED"></a>

## 276.71 `CONFIG_ESP_USB_SERIAL_JTAG_ENABLED`

**提示（Prompt）**：保持 USB 串口／JTAG 控制器启用（USB Serial/JTAG controller）

**说明（Help）**

启动时保持 USB 串口／JTAG 控制器的时钟及物理层焊盘（PHY pads）启用。通过内置 USB 端口进行 JTAG 调试，以及 USB 串口输出，都需要此设置。只有在需要节电且不使用 USB 串口／JTAG 端口进行调试或控制台输出时，才应禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C3 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32H2 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.console:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.console#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_MAC_BB_PD"></a>

## 276.72 `CONFIG_MAC_BB_PD`

原库同名定义共 6 条；本项为数据库第 10644 条记录，各定义分别保留。

**提示（Prompt）**：禁用 PHY 时关闭 Wi-Fi 和蓝牙的 MAC 与基带电源（Power down MAC and baseband）

**说明（Help）**

启用后，在物理层（PHY）禁用时，会关闭 Wi-Fi 和蓝牙的介质访问控制（MAC）与基带（baseband）电源。此设置略微降低功耗，但会增加 RAM 使用量：仅 Wi-Fi 时约 4 KB，仅蓝牙时约 2 KB，同时使用 Wi-Fi 与蓝牙时约 5.3 KB。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C2 && CONFIG_TICKLESS_KERNEL && CONFIG_PM && CONFIG_SOC_SERIES_ESP32C2 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
CONFIG_ESP32_BT_LE_SLEEP_ENABLE
CONFIG_IEEE802154_ESP32_SLEEP_ENABLE
```

**定义位置（Location）**：[`soc/espressif/esp32c2/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c2/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32_BT_LE_SLEEP_ENABLE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SLEEP_ENABLE)、[`CONFIG_IEEE802154_ESP32_SLEEP_ENABLE`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_SLEEP_ENABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_MAC_BB_PD--record-10645"></a>

## 276.73 `CONFIG_MAC_BB_PD`

原库同名定义共 6 条；本项为数据库第 10645 条记录，各定义分别保留。

**提示（Prompt）**：禁用 PHY 时关闭 Wi-Fi 和蓝牙的 MAC 与基带电源（Power down MAC and baseband）

**说明（Help）**

启用后，在物理层（PHY）禁用时，会关闭 Wi-Fi 和蓝牙的介质访问控制（MAC）与基带（baseband）电源。此设置略微降低功耗，但会增加 RAM 使用量：仅 Wi-Fi 时约 4 KB，仅蓝牙时约 2 KB，同时使用 Wi-Fi 与蓝牙时约 5.3 KB。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C3 && CONFIG_TICKLESS_KERNEL && CONFIG_PM && CONFIG_SOC_SERIES_ESP32C3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
CONFIG_ESP32_BT_LE_SLEEP_ENABLE
CONFIG_IEEE802154_ESP32_SLEEP_ENABLE
```

**定义位置（Location）**：[`soc/espressif/esp32c3/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c3/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32_BT_LE_SLEEP_ENABLE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SLEEP_ENABLE)、[`CONFIG_IEEE802154_ESP32_SLEEP_ENABLE`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_SLEEP_ENABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_MAC_BB_PD--record-10646"></a>

## 276.74 `CONFIG_MAC_BB_PD`

原库同名定义共 6 条；本项为数据库第 10646 条记录，各定义分别保留。

**提示（Prompt）**：禁用 PHY 时关闭 Wi-Fi 和蓝牙的 MAC 与基带电源（Power down MAC and baseband）

**说明（Help）**

启用后，在物理层（PHY）禁用时，会关闭 Wi-Fi 和蓝牙的介质访问控制（MAC）与基带（baseband）电源。此设置略微降低功耗，但会增加 RAM 使用量：仅 Wi-Fi 时约 4 KB，仅蓝牙时约 2 KB，同时使用 Wi-Fi 与蓝牙时约 5.3 KB。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C5 && CONFIG_TICKLESS_KERNEL && CONFIG_PM && CONFIG_SOC_SERIES_ESP32C5 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
CONFIG_ESP32_BT_LE_SLEEP_ENABLE
CONFIG_IEEE802154_ESP32_SLEEP_ENABLE
```

**定义位置（Location）**：[`soc/espressif/esp32c5/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c5/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32_BT_LE_SLEEP_ENABLE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SLEEP_ENABLE)、[`CONFIG_IEEE802154_ESP32_SLEEP_ENABLE`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_SLEEP_ENABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_MAC_BB_PD--record-10647"></a>

## 276.75 `CONFIG_MAC_BB_PD`

原库同名定义共 6 条；本项为数据库第 10647 条记录，各定义分别保留。

**提示（Prompt）**：禁用 PHY 时关闭 Wi-Fi 和蓝牙的 MAC 与基带电源（Power down MAC and baseband）

**说明（Help）**

启用后，在物理层（PHY）禁用时，会关闭 Wi-Fi 和蓝牙的介质访问控制（MAC）与基带（baseband）电源。此设置略微降低功耗，但会增加 RAM 使用量：仅 Wi-Fi 时约 4 KB，仅蓝牙时约 2 KB，同时使用 Wi-Fi 与蓝牙时约 5.3 KB。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C6 && CONFIG_TICKLESS_KERNEL && CONFIG_PM && CONFIG_SOC_SERIES_ESP32C6 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
CONFIG_ESP32_BT_LE_SLEEP_ENABLE
CONFIG_IEEE802154_ESP32_SLEEP_ENABLE
```

**定义位置（Location）**：[`soc/espressif/esp32c6/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c6/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32_BT_LE_SLEEP_ENABLE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SLEEP_ENABLE)、[`CONFIG_IEEE802154_ESP32_SLEEP_ENABLE`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_SLEEP_ENABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_MAC_BB_PD--record-10648"></a>

## 276.76 `CONFIG_MAC_BB_PD`

原库同名定义共 6 条；本项为数据库第 10648 条记录，各定义分别保留。

**提示（Prompt）**：禁用 PHY 时关闭 Wi-Fi 和蓝牙的 MAC 与基带电源（Power down MAC and baseband）

**说明（Help）**

启用后，在物理层（PHY）禁用时，会关闭 Wi-Fi 和蓝牙的介质访问控制（MAC）与基带（baseband）电源。此设置略微降低功耗，但会增加 RAM 使用量：仅 Wi-Fi 时约 4 KB，仅蓝牙时约 2 KB，同时使用 Wi-Fi 与蓝牙时约 5.3 KB。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C61 && CONFIG_TICKLESS_KERNEL && CONFIG_PM && CONFIG_SOC_SERIES_ESP32C61 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
CONFIG_ESP32_BT_LE_SLEEP_ENABLE
CONFIG_IEEE802154_ESP32_SLEEP_ENABLE
```

**定义位置（Location）**：[`soc/espressif/esp32c61/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c61/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32_BT_LE_SLEEP_ENABLE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SLEEP_ENABLE)、[`CONFIG_IEEE802154_ESP32_SLEEP_ENABLE`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_SLEEP_ENABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_MAC_BB_PD--record-10649"></a>

## 276.77 `CONFIG_MAC_BB_PD`

原库同名定义共 6 条；本项为数据库第 10649 条记录，各定义分别保留。

**提示（Prompt）**：禁用 PHY 时关闭 Wi-Fi 和蓝牙的 MAC 与基带电源（Power down MAC and baseband）

**说明（Help）**

启用后，在物理层（PHY）禁用时，会关闭 Wi-Fi 和蓝牙的介质访问控制（MAC）与基带（baseband）电源。此设置略微降低功耗，但会增加 RAM 使用量：仅 Wi-Fi 时约 4KB，仅蓝牙时约 2KB，同时使用 Wi-Fi 与蓝牙时约 5.3KB。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_TICKLESS_KERNEL && CONFIG_PM && CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
CONFIG_ESP32_BT_LE_SLEEP_ENABLE
CONFIG_IEEE802154_ESP32_SLEEP_ENABLE
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32_BT_LE_SLEEP_ENABLE`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SLEEP_ENABLE)、[`CONFIG_IEEE802154_ESP32_SLEEP_ENABLE`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_SLEEP_ENABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_PICO_PSRAM_CS_IO"></a>

## 276.78 `CONFIG_PICO_PSRAM_CS_IO`

**提示（Prompt）**：PSRAM 片选 IO 编号（CS IO number）

**说明（Help）**

PSRAM 片选 IO（CS IO）可以使用任意未使用的 GPIO，用户可根据硬件设计配置。对于 ESP32-PICO 芯片，PSRAM 与 Flash 共享时钟，因此无需配置时钟 IO。硬件参考设计请参阅 [ESP32-PICO-D4 数据手册](https://www.espressif.com/sites/default/files/documentation/esp32-pico-d4_datasheet_en.pdf)。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32 && CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 33]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:208`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L208)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → ESP32-PICO 的 PSRAM 时钟和片选 IO（clock and cs IO）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_RESERVE_RTC_MEM"></a>

## 276.79 `CONFIG_RESERVE_RTC_MEM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项在 RTC 快速内存（RTC FAST memory）中预留一块区域，单位为字节。它用于将 RTC 定时器保留数据（retention data）保存在固定地址，使时间读取在睡眠前后保持有效。没有 RTC 保留内存的 SoC 会忽略此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
24
```

**定义位置（Location）**：[`soc/espressif/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SOC_ENABLE_APPCPU"></a>

## 276.80 `CONFIG_SOC_ENABLE_APPCPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置使 PROCPU 内核在启用处理器间消息传递（IPM）时映射并启动 APPCPU。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_IPM || CONFIG_MBOX) && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32S3) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.amp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.amp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SOC_ESP32"></a>

## 276.81 `CONFIG_SOC_ESP32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_ESP32
```

**被选择（Selected by）**

```text
CONFIG_BOARD_YD_ESP32
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32
CONFIG_BOARD_TTGO_T7V1_5
CONFIG_BOARD_TTGO_TBEAM
CONFIG_BOARD_TTGO_LORA32
CONFIG_BOARD_ESP32_ETHERNET_KIT
CONFIG_BOARD_ESP_WROVER_KIT
CONFIG_BOARD_ESP32_DEVKITC
CONFIG_BOARD_ESP32_CAM
CONFIG_BOARD_INKPLATE_6COLOR
CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1
CONFIG_BOARD_LOLIN32_LITE
CONFIG_BOARD_UDOO_KEY
CONFIG_BOARD_M5STACK_CORE2
CONFIG_BOARD_M5STACK_FIRE
CONFIG_BOARD_M5STICKC_PLUS
CONFIG_BOARD_M5STACK_ATOM_LITE
CONFIG_BOARD_OLIMEX_ESP32_EVB
CONFIG_BOARD_CAN485DBV1
CONFIG_BOARD_KINCONY_KC868_A8
CONFIG_BOARD_KINCONY_KC868_A32
CONFIG_BOARD_ODROID_GO
CONFIG_BOARD_HELTEC_WIFI_LORA32_V2
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_BOARD_YD_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_YD_ESP32)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32)、[`CONFIG_BOARD_TTGO_T7V1_5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_T7V1_5)、[`CONFIG_BOARD_TTGO_TBEAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_TBEAM)、[`CONFIG_BOARD_TTGO_LORA32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_LORA32)、[`CONFIG_BOARD_ESP32_ETHERNET_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32_ETHERNET_KIT)、[`CONFIG_BOARD_ESP_WROVER_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP_WROVER_KIT)、[`CONFIG_BOARD_ESP32_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32_DEVKITC)、[`CONFIG_BOARD_ESP32_CAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32_CAM)、[`CONFIG_BOARD_INKPLATE_6COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_INKPLATE_6COLOR)、[`CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1)、[`CONFIG_BOARD_LOLIN32_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_LOLIN32_LITE)、[`CONFIG_BOARD_UDOO_KEY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UDOO_KEY)、[`CONFIG_BOARD_M5STACK_CORE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_CORE2)、[`CONFIG_BOARD_M5STACK_FIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_FIRE)、[`CONFIG_BOARD_M5STICKC_PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STICKC_PLUS)、[`CONFIG_BOARD_M5STACK_ATOM_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_ATOM_LITE)、[`CONFIG_BOARD_OLIMEX_ESP32_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_OLIMEX_ESP32_EVB)、[`CONFIG_BOARD_CAN485DBV1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CAN485DBV1)、[`CONFIG_BOARD_KINCONY_KC868_A8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_KINCONY_KC868_A8)、[`CONFIG_BOARD_KINCONY_KC868_A32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_KINCONY_KC868_A32)、[`CONFIG_BOARD_ODROID_GO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ODROID_GO)、[`CONFIG_BOARD_HELTEC_WIFI_LORA32_V2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HELTEC_WIFI_LORA32_V2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_YD_ESP32`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32`、`CONFIG_BOARD_TTGO_T7V1_5`、`CONFIG_BOARD_TTGO_TBEAM`、`CONFIG_BOARD_TTGO_LORA32`、`CONFIG_BOARD_ESP32_ETHERNET_KIT`、`CONFIG_BOARD_ESP_WROVER_KIT`、`CONFIG_BOARD_ESP32_DEVKITC`、`CONFIG_BOARD_ESP32_CAM`、`CONFIG_BOARD_INKPLATE_6COLOR`、`CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1`、`CONFIG_BOARD_LOLIN32_LITE`、`CONFIG_BOARD_UDOO_KEY`、`CONFIG_BOARD_M5STACK_CORE2`、`CONFIG_BOARD_M5STACK_FIRE`、`CONFIG_BOARD_M5STICKC_PLUS`、`CONFIG_BOARD_M5STACK_ATOM_LITE`、`CONFIG_BOARD_OLIMEX_ESP32_EVB`、`CONFIG_BOARD_CAN485DBV1`、`CONFIG_BOARD_KINCONY_KC868_A8`、`CONFIG_BOARD_KINCONY_KC868_A32`、`CONFIG_BOARD_ODROID_GO`、`CONFIG_BOARD_HELTEC_WIFI_LORA32_V2`。

<a id="CONFIG_SOC_ESP32C2_REV_2_0"></a>

## 276.82 `CONFIG_SOC_ESP32C2_REV_2_0`

**提示（Prompt）**：SoC 修订版为 v2.0（ECO4）

**说明（Help）**

ESP32-C2 修订版 v2.0 更新了 ROM 函数（ROM functions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C2 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/esp32c2/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c2/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SOC_ESP32C3"></a>

## 276.83 `CONFIG_SOC_ESP32C3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32C3 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_ESP32C3
```

**被选择（Selected by）**

```text
CONFIG_BOARD_BEETLE_ESP32C3
CONFIG_BOARD_WE_ORTHOSIE1EV
CONFIG_BOARD_UEDX24240013_MD50E
CONFIG_BOARD_GLYPH_C3
CONFIG_BOARD_XIAO_ESP32C3
CONFIG_BOARD_TTGO_T8C3
CONFIG_BOARD_TTGO_TOIPLUS
CONFIG_BOARD_ESP32C3_RUST
CONFIG_BOARD_ESP32C3_DEVKITC
CONFIG_BOARD_ESP32C3_DEVKITM
CONFIG_BOARD_ESP32C3_042_OLED
CONFIG_BOARD_ICEV_WIRELESS
CONFIG_BOARD_ESP32C3_SUPERMINI
CONFIG_BOARD_ESP32C3_LCKFB
CONFIG_BOARD_STAMP_C3
CONFIG_BOARD_WEACT_ESP32C3_MINI
CONFIG_BOARD_ESP32C3_LUATOS_CORE
```

**定义位置（Location）**：[`soc/espressif/esp32c3/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c3/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_BOARD_BEETLE_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BEETLE_ESP32C3)、[`CONFIG_BOARD_WE_ORTHOSIE1EV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WE_ORTHOSIE1EV)、[`CONFIG_BOARD_UEDX24240013_MD50E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UEDX24240013_MD50E)、[`CONFIG_BOARD_GLYPH_C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_GLYPH_C3)、[`CONFIG_BOARD_XIAO_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_ESP32C3)、[`CONFIG_BOARD_TTGO_T8C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_T8C3)、[`CONFIG_BOARD_TTGO_TOIPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_TOIPLUS)、[`CONFIG_BOARD_ESP32C3_RUST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C3_RUST)、[`CONFIG_BOARD_ESP32C3_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C3_DEVKITC)、[`CONFIG_BOARD_ESP32C3_DEVKITM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C3_DEVKITM)、[`CONFIG_BOARD_ESP32C3_042_OLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C3_042_OLED)、[`CONFIG_BOARD_ICEV_WIRELESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ICEV_WIRELESS)、[`CONFIG_BOARD_ESP32C3_SUPERMINI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C3_SUPERMINI)、[`CONFIG_BOARD_ESP32C3_LCKFB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C3_LCKFB)、[`CONFIG_BOARD_STAMP_C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_STAMP_C3)、[`CONFIG_BOARD_WEACT_ESP32C3_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WEACT_ESP32C3_MINI)、[`CONFIG_BOARD_ESP32C3_LUATOS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C3_LUATOS_CORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_BEETLE_ESP32C3`、`CONFIG_BOARD_WE_ORTHOSIE1EV`、`CONFIG_BOARD_UEDX24240013_MD50E`、`CONFIG_BOARD_GLYPH_C3`、`CONFIG_BOARD_XIAO_ESP32C3`、`CONFIG_BOARD_TTGO_T8C3`、`CONFIG_BOARD_TTGO_TOIPLUS`、`CONFIG_BOARD_ESP32C3_RUST`、`CONFIG_BOARD_ESP32C3_DEVKITC`、`CONFIG_BOARD_ESP32C3_DEVKITM`、`CONFIG_BOARD_ESP32C3_042_OLED`、`CONFIG_BOARD_ICEV_WIRELESS`、`CONFIG_BOARD_ESP32C3_SUPERMINI`、`CONFIG_BOARD_ESP32C3_LCKFB`、`CONFIG_BOARD_STAMP_C3`、`CONFIG_BOARD_WEACT_ESP32C3_MINI`、`CONFIG_BOARD_ESP32C3_LUATOS_CORE`。

<a id="CONFIG_SOC_ESP32C3_REV_1_1"></a>

## 276.84 `CONFIG_SOC_ESP32C3_REV_1_1`

**提示（Prompt）**：SoC 修订版为 v1.1（revision v1.1）

**说明（Help）**

ESP32-C3 修订版 v1.1 更新了 Wi-Fi 和低功耗蓝牙（BLE）的 ROM 函数，可释放最多 35kB RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/esp32c3/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c3/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SOC_ESP32C5_HPCORE"></a>

## 276.85 `CONFIG_SOC_ESP32C5_HPCORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为高性能内核（HP CORE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_XIAO_ESP32C5
CONFIG_BOARD_ESP32C5_DEVKITC
```

**定义位置（Location）**：[`soc/espressif/esp32c5/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c5/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_XIAO_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_ESP32C5)、[`CONFIG_BOARD_ESP32C5_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C5_DEVKITC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_XIAO_ESP32C5`、`CONFIG_BOARD_ESP32C5_DEVKITC`。

<a id="CONFIG_SOC_ESP32C5_LPCORE"></a>

## 276.86 `CONFIG_SOC_ESP32C5_LPCORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为低功耗内核（LP CORE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_XIAO_ESP32C5
CONFIG_BOARD_ESP32C5_DEVKITC
```

**定义位置（Location）**：[`soc/espressif/esp32c5/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c5/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_XIAO_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_ESP32C5)、[`CONFIG_BOARD_ESP32C5_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C5_DEVKITC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_XIAO_ESP32C5`、`CONFIG_BOARD_ESP32C5_DEVKITC`。

<a id="CONFIG_SOC_ESP32C61_REV_MIN_FULL"></a>

## 276.87 `CONFIG_SOC_ESP32C61_REV_MIN_FULL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

最低支持的 ESP32-C61 芯片修订版（chip revision），采用 `major * 100 + minor` 格式，与运行时 `efuse_hal_chip_revision()` 的返回值一致。此值从开发板选择的 `SOC_ESP32C61_REV_*` 符号推导，默认为该家族的最低版本 v1.0（100）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C61 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
100 if CONFIG_SOC_ESP32C61_REV_1_0
101 if CONFIG_SOC_ESP32C61_REV_1_1
100
```

**定义位置（Location）**：[`soc/espressif/esp32c61/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c61/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_ESP32C61_REV_1_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32C61_REV_1_0)、[`CONFIG_SOC_ESP32C61_REV_1_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32C61_REV_1_1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`、`CONFIG_SOC_ESP32C61_REV_1_0`、`CONFIG_SOC_ESP32C61_REV_1_1`。

<a id="CONFIG_SOC_ESP32C6_HPCORE"></a>

## 276.88 `CONFIG_SOC_ESP32C6_HPCORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为高性能内核（HP CORE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_GLYPH_C6
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6
CONFIG_BOARD_XIAO_ESP32C6
CONFIG_BOARD_ARDUINO_NESSO_N1
CONFIG_BOARD_ESP32C6_DEVKITC
CONFIG_BOARD_ESP32C6_LCD_1_47
CONFIG_BOARD_M5STACK_NANOC6
CONFIG_BOARD_M5STACK_UNITC6L
CONFIG_BOARD_WEACT_ESP32C6_MINI
```

**定义位置（Location）**：[`soc/espressif/esp32c6/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c6/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_GLYPH_C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_GLYPH_C6)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6)、[`CONFIG_BOARD_XIAO_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_ESP32C6)、[`CONFIG_BOARD_ARDUINO_NESSO_N1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ARDUINO_NESSO_N1)、[`CONFIG_BOARD_ESP32C6_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C6_DEVKITC)、[`CONFIG_BOARD_ESP32C6_LCD_1_47`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C6_LCD_1_47)、[`CONFIG_BOARD_M5STACK_NANOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_NANOC6)、[`CONFIG_BOARD_M5STACK_UNITC6L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_UNITC6L)、[`CONFIG_BOARD_WEACT_ESP32C6_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WEACT_ESP32C6_MINI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_GLYPH_C6`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6`、`CONFIG_BOARD_XIAO_ESP32C6`、`CONFIG_BOARD_ARDUINO_NESSO_N1`、`CONFIG_BOARD_ESP32C6_DEVKITC`、`CONFIG_BOARD_ESP32C6_LCD_1_47`、`CONFIG_BOARD_M5STACK_NANOC6`、`CONFIG_BOARD_M5STACK_UNITC6L`、`CONFIG_BOARD_WEACT_ESP32C6_MINI`。

<a id="CONFIG_SOC_ESP32C6_LPCORE"></a>

## 276.89 `CONFIG_SOC_ESP32C6_LPCORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为低功耗内核（LP CORE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_GLYPH_C6
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6
CONFIG_BOARD_XIAO_ESP32C6
CONFIG_BOARD_ARDUINO_NESSO_N1
CONFIG_BOARD_ESP32C6_DEVKITC
CONFIG_BOARD_ESP32C6_LCD_1_47
CONFIG_BOARD_M5STACK_NANOC6
CONFIG_BOARD_M5STACK_UNITC6L
CONFIG_BOARD_WEACT_ESP32C6_MINI
```

**定义位置（Location）**：[`soc/espressif/esp32c6/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c6/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_GLYPH_C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_GLYPH_C6)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6)、[`CONFIG_BOARD_XIAO_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_ESP32C6)、[`CONFIG_BOARD_ARDUINO_NESSO_N1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ARDUINO_NESSO_N1)、[`CONFIG_BOARD_ESP32C6_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C6_DEVKITC)、[`CONFIG_BOARD_ESP32C6_LCD_1_47`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32C6_LCD_1_47)、[`CONFIG_BOARD_M5STACK_NANOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_NANOC6)、[`CONFIG_BOARD_M5STACK_UNITC6L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_UNITC6L)、[`CONFIG_BOARD_WEACT_ESP32C6_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WEACT_ESP32C6_MINI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_GLYPH_C6`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6`、`CONFIG_BOARD_XIAO_ESP32C6`、`CONFIG_BOARD_ARDUINO_NESSO_N1`、`CONFIG_BOARD_ESP32C6_DEVKITC`、`CONFIG_BOARD_ESP32C6_LCD_1_47`、`CONFIG_BOARD_M5STACK_NANOC6`、`CONFIG_BOARD_M5STACK_UNITC6L`、`CONFIG_BOARD_WEACT_ESP32C6_MINI`。

<a id="CONFIG_SOC_ESP32P4_HPCORE"></a>

## 276.90 `CONFIG_SOC_ESP32P4_HPCORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为高性能内核（HP CORE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_ESP32P4
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD
CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD
CONFIG_BOARD_WAVESHARE_ESP32P4_ETH
CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT
CONFIG_BOARD_ESP32P4_WIFI6
CONFIG_BOARD_ESP32P4_PC
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig.soc:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig.soc#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32P4)、[`CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD)、[`CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD)、[`CONFIG_BOARD_WAVESHARE_ESP32P4_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WAVESHARE_ESP32P4_ETH)、[`CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT)、[`CONFIG_BOARD_ESP32P4_WIFI6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32P4_WIFI6)、[`CONFIG_BOARD_ESP32P4_PC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32P4_PC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32P4`、`CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD`、`CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD`、`CONFIG_BOARD_WAVESHARE_ESP32P4_ETH`、`CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT`、`CONFIG_BOARD_ESP32P4_WIFI6`、`CONFIG_BOARD_ESP32P4_PC`。

<a id="CONFIG_SOC_ESP32P4_LPCORE"></a>

## 276.91 `CONFIG_SOC_ESP32P4_LPCORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为低功耗内核（LP CORE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_ESP32P4
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD
CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD
CONFIG_BOARD_WAVESHARE_ESP32P4_ETH
CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT
CONFIG_BOARD_ESP32P4_WIFI6
CONFIG_BOARD_ESP32P4_PC
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig.soc:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig.soc#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32P4)、[`CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD)、[`CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD)、[`CONFIG_BOARD_WAVESHARE_ESP32P4_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WAVESHARE_ESP32P4_ETH)、[`CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT)、[`CONFIG_BOARD_ESP32P4_WIFI6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32P4_WIFI6)、[`CONFIG_BOARD_ESP32P4_PC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32P4_PC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32P4`、`CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD`、`CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD`、`CONFIG_BOARD_WAVESHARE_ESP32P4_ETH`、`CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT`、`CONFIG_BOARD_ESP32P4_WIFI6`、`CONFIG_BOARD_ESP32P4_PC`。

<a id="CONFIG_SOC_ESP32P4_REV_MIN_FULL"></a>

## 276.92 `CONFIG_SOC_ESP32P4_REV_MIN_FULL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

最低支持的 ESP32-P4 芯片修订版（chip revision），采用 `major * 100 + minor` 格式，与运行时 `efuse_hal_chip_revision()` 的返回值一致。此值从开发板选择的 `SOC_ESP32P4_REV_*` 符号推导；未选择时，默认为 v3.x 家族的最低版本 v3.1（301）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32P4 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
103 if CONFIG_SOC_ESP32P4_REV_1_3
300 if CONFIG_SOC_ESP32P4_REV_3_0
301 if CONFIG_SOC_ESP32P4_REV_3_1
301
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_ESP32P4_REV_1_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32P4_REV_1_3)、[`CONFIG_SOC_ESP32P4_REV_3_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32P4_REV_3_0)、[`CONFIG_SOC_ESP32P4_REV_3_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32P4_REV_3_1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`、`CONFIG_SOC_ESP32P4_REV_1_3`、`CONFIG_SOC_ESP32P4_REV_3_0`、`CONFIG_SOC_ESP32P4_REV_3_1`。

<a id="CONFIG_SOC_ESP32S2"></a>

## 276.93 `CONFIG_SOC_ESP32S2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32S2 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_ESP32S2
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT_REVERSE
CONFIG_BOARD_ESP32S2_DEVKITC
CONFIG_BOARD_ESP32S2_SAOLA
CONFIG_BOARD_ESP32S2_LOLIN_MINI
CONFIG_BOARD_ESP32S2_FRANZININHO
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT_REVERSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT_REVERSE)、[`CONFIG_BOARD_ESP32S2_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S2_DEVKITC)、[`CONFIG_BOARD_ESP32S2_SAOLA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S2_SAOLA)、[`CONFIG_BOARD_ESP32S2_LOLIN_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S2_LOLIN_MINI)、[`CONFIG_BOARD_ESP32S2_FRANZININHO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S2_FRANZININHO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT_REVERSE`、`CONFIG_BOARD_ESP32S2_DEVKITC`、`CONFIG_BOARD_ESP32S2_SAOLA`、`CONFIG_BOARD_ESP32S2_LOLIN_MINI`、`CONFIG_BOARD_ESP32S2_FRANZININHO`。

<a id="CONFIG_SOC_ESP32S3"></a>

## 276.94 `CONFIG_SOC_ESP32S3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32S3 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_SERIES_ESP32S3
```

**被选择（Selected by）**

```text
CONFIG_BOARD_MATOUCH_MTRO128G
CONFIG_BOARD_UEDX24320028E_WB_A
CONFIG_BOARD_UEDX32480035E_WB_A
CONFIG_BOARD_DNESP32S3B
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3
CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT
CONFIG_BOARD_RETERMINAL_E1001
CONFIG_BOARD_XIAO_ESP32S3
CONFIG_BOARD_RETERMINAL_E1003
CONFIG_BOARD_RETERMINAL_E1002
CONFIG_BOARD_EORA_HUB_900TB
CONFIG_BOARD_TWATCH_S3
CONFIG_BOARD_TDONGLE_S3
CONFIG_BOARD_TTGO_T8S3
CONFIG_BOARD_T_DECK
CONFIG_BOARD_ESP32S3_BOX3
CONFIG_BOARD_ESP_THREADBR
CONFIG_BOARD_ESP32S3_DEVKITC
CONFIG_BOARD_ESP32S3_EYE
CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28
CONFIG_BOARD_ESP32S3_GEEK
CONFIG_BOARD_ESP32S3_MATRIX
CONFIG_BOARD_ESP32S3_RLCD_4_2
CONFIG_BOARD_WALTER
CONFIG_BOARD_SHRIKE_FI
CONFIG_BOARD_RAK3112
CONFIG_BOARD_M5STACK_ATOMS3_LITE
CONFIG_BOARD_M5STACK_CORES3
CONFIG_BOARD_M5STACK_STAMPS3
CONFIG_BOARD_M5STACK_ATOMS3
CONFIG_BOARD_M5STACK_STACKCHAN
CONFIG_BOARD_M5STACK_PAPER_COLOR
CONFIG_BOARD_M5STACK_STICKS3
CONFIG_BOARD_WEACT_ESP32S3_MINI
CONFIG_BOARD_WEACT_ESP32S3_B
CONFIG_BOARD_HELTEC_WIFI_LORA32_V3
CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3
CONFIG_BOARD_HELTEC_WIRELESS_TRACKER
CONFIG_BOARD_ESP32S3_LUATOS_CORE
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_BOARD_MATOUCH_MTRO128G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MATOUCH_MTRO128G)、[`CONFIG_BOARD_UEDX24320028E_WB_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UEDX24320028E_WB_A)、[`CONFIG_BOARD_UEDX32480035E_WB_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UEDX32480035E_WB_A)、[`CONFIG_BOARD_DNESP32S3B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_DNESP32S3B)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3)、[`CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT)、[`CONFIG_BOARD_RETERMINAL_E1001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RETERMINAL_E1001)、[`CONFIG_BOARD_XIAO_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_ESP32S3)、[`CONFIG_BOARD_RETERMINAL_E1003`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RETERMINAL_E1003)、[`CONFIG_BOARD_RETERMINAL_E1002`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RETERMINAL_E1002)、[`CONFIG_BOARD_EORA_HUB_900TB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EORA_HUB_900TB)、[`CONFIG_BOARD_TWATCH_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TWATCH_S3)、[`CONFIG_BOARD_TDONGLE_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TDONGLE_S3)、[`CONFIG_BOARD_TTGO_T8S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_T8S3)、[`CONFIG_BOARD_T_DECK`](P045_boards_lilygo_配置项参考.md#CONFIG_BOARD_T_DECK)、[`CONFIG_BOARD_ESP32S3_BOX3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_BOX3)、[`CONFIG_BOARD_ESP_THREADBR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP_THREADBR)、[`CONFIG_BOARD_ESP32S3_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_DEVKITC)、[`CONFIG_BOARD_ESP32S3_EYE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_EYE)、[`CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28)、[`CONFIG_BOARD_ESP32S3_GEEK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_GEEK)、[`CONFIG_BOARD_ESP32S3_MATRIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_MATRIX)、[`CONFIG_BOARD_ESP32S3_RLCD_4_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_RLCD_4_2)、[`CONFIG_BOARD_WALTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WALTER)、[`CONFIG_BOARD_SHRIKE_FI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_SHRIKE_FI)、[`CONFIG_BOARD_RAK3112`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RAK3112)、[`CONFIG_BOARD_M5STACK_ATOMS3_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_ATOMS3_LITE)、[`CONFIG_BOARD_M5STACK_CORES3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_CORES3)、[`CONFIG_BOARD_M5STACK_STAMPS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_STAMPS3)、[`CONFIG_BOARD_M5STACK_ATOMS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_ATOMS3)、[`CONFIG_BOARD_M5STACK_STACKCHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_STACKCHAN)、[`CONFIG_BOARD_M5STACK_PAPER_COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_PAPER_COLOR)、[`CONFIG_BOARD_M5STACK_STICKS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_STICKS3)、[`CONFIG_BOARD_WEACT_ESP32S3_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WEACT_ESP32S3_MINI)、[`CONFIG_BOARD_WEACT_ESP32S3_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WEACT_ESP32S3_B)、[`CONFIG_BOARD_HELTEC_WIFI_LORA32_V3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HELTEC_WIFI_LORA32_V3)、[`CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3)、[`CONFIG_BOARD_HELTEC_WIRELESS_TRACKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HELTEC_WIRELESS_TRACKER)、[`CONFIG_BOARD_ESP32S3_LUATOS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_LUATOS_CORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_MATOUCH_MTRO128G`、`CONFIG_BOARD_UEDX24320028E_WB_A`、`CONFIG_BOARD_UEDX32480035E_WB_A`、`CONFIG_BOARD_DNESP32S3B`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3`、`CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT`、`CONFIG_BOARD_RETERMINAL_E1001`、`CONFIG_BOARD_XIAO_ESP32S3`、`CONFIG_BOARD_RETERMINAL_E1003`、`CONFIG_BOARD_RETERMINAL_E1002`、`CONFIG_BOARD_EORA_HUB_900TB`、`CONFIG_BOARD_TWATCH_S3`、`CONFIG_BOARD_TDONGLE_S3`、`CONFIG_BOARD_TTGO_T8S3`、`CONFIG_BOARD_ESP32S3_BOX3`、`CONFIG_BOARD_ESP_THREADBR`、`CONFIG_BOARD_ESP32S3_DEVKITC`、`CONFIG_BOARD_ESP32S3_EYE`、`CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28`、`CONFIG_BOARD_ESP32S3_GEEK`、`CONFIG_BOARD_ESP32S3_MATRIX`、`CONFIG_BOARD_ESP32S3_RLCD_4_2`、`CONFIG_BOARD_WALTER`、`CONFIG_BOARD_SHRIKE_FI`、`CONFIG_BOARD_RAK3112`、`CONFIG_BOARD_M5STACK_ATOMS3_LITE`、`CONFIG_BOARD_M5STACK_CORES3`、`CONFIG_BOARD_M5STACK_STAMPS3`、`CONFIG_BOARD_M5STACK_ATOMS3`、`CONFIG_BOARD_M5STACK_STACKCHAN`、`CONFIG_BOARD_M5STACK_PAPER_COLOR`、`CONFIG_BOARD_M5STACK_STICKS3`、`CONFIG_BOARD_WEACT_ESP32S3_MINI`、`CONFIG_BOARD_WEACT_ESP32S3_B`、`CONFIG_BOARD_HELTEC_WIFI_LORA32_V3`、`CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3`、`CONFIG_BOARD_HELTEC_WIRELESS_TRACKER`、`CONFIG_BOARD_ESP32S3_LUATOS_CORE`。

<a id="CONFIG_SOC_ESP32S3_APPCPU"></a>

## 276.95 `CONFIG_SOC_ESP32S3_APPCPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为应用 CPU（APPCPU，内核 1）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_MATOUCH_MTRO128G
CONFIG_BOARD_UEDX24320028E_WB_A
CONFIG_BOARD_UEDX32480035E_WB_A
CONFIG_BOARD_DNESP32S3B
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3
CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT
CONFIG_BOARD_RETERMINAL_E1001
CONFIG_BOARD_XIAO_ESP32S3
CONFIG_BOARD_RETERMINAL_E1003
CONFIG_BOARD_RETERMINAL_E1002
CONFIG_BOARD_EORA_HUB_900TB
CONFIG_BOARD_TWATCH_S3
CONFIG_BOARD_TDONGLE_S3
CONFIG_BOARD_TTGO_T8S3
CONFIG_BOARD_T_DECK
CONFIG_BOARD_ESP32S3_BOX3
CONFIG_BOARD_ESP_THREADBR
CONFIG_BOARD_ESP32S3_DEVKITC
CONFIG_BOARD_ESP32S3_EYE
CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28
CONFIG_BOARD_ESP32S3_GEEK
CONFIG_BOARD_ESP32S3_MATRIX
CONFIG_BOARD_ESP32S3_RLCD_4_2
CONFIG_BOARD_WALTER
CONFIG_BOARD_SHRIKE_FI
CONFIG_BOARD_RAK3112
CONFIG_BOARD_M5STACK_ATOMS3_LITE
CONFIG_BOARD_M5STACK_CORES3
CONFIG_BOARD_M5STACK_STAMPS3
CONFIG_BOARD_M5STACK_ATOMS3
CONFIG_BOARD_M5STACK_STACKCHAN
CONFIG_BOARD_M5STACK_PAPER_COLOR
CONFIG_BOARD_M5STACK_STICKS3
CONFIG_BOARD_WEACT_ESP32S3_MINI
CONFIG_BOARD_WEACT_ESP32S3_B
CONFIG_BOARD_HELTEC_WIFI_LORA32_V3
CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3
CONFIG_BOARD_HELTEC_WIRELESS_TRACKER
CONFIG_BOARD_ESP32S3_LUATOS_CORE
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_MATOUCH_MTRO128G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MATOUCH_MTRO128G)、[`CONFIG_BOARD_UEDX24320028E_WB_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UEDX24320028E_WB_A)、[`CONFIG_BOARD_UEDX32480035E_WB_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UEDX32480035E_WB_A)、[`CONFIG_BOARD_DNESP32S3B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_DNESP32S3B)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3)、[`CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT)、[`CONFIG_BOARD_RETERMINAL_E1001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RETERMINAL_E1001)、[`CONFIG_BOARD_XIAO_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_ESP32S3)、[`CONFIG_BOARD_RETERMINAL_E1003`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RETERMINAL_E1003)、[`CONFIG_BOARD_RETERMINAL_E1002`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RETERMINAL_E1002)、[`CONFIG_BOARD_EORA_HUB_900TB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EORA_HUB_900TB)、[`CONFIG_BOARD_TWATCH_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TWATCH_S3)、[`CONFIG_BOARD_TDONGLE_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TDONGLE_S3)、[`CONFIG_BOARD_TTGO_T8S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_T8S3)、[`CONFIG_BOARD_T_DECK`](P045_boards_lilygo_配置项参考.md#CONFIG_BOARD_T_DECK)、[`CONFIG_BOARD_ESP32S3_BOX3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_BOX3)、[`CONFIG_BOARD_ESP_THREADBR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP_THREADBR)、[`CONFIG_BOARD_ESP32S3_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_DEVKITC)、[`CONFIG_BOARD_ESP32S3_EYE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_EYE)、[`CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28)、[`CONFIG_BOARD_ESP32S3_GEEK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_GEEK)、[`CONFIG_BOARD_ESP32S3_MATRIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_MATRIX)、[`CONFIG_BOARD_ESP32S3_RLCD_4_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_RLCD_4_2)、[`CONFIG_BOARD_WALTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WALTER)、[`CONFIG_BOARD_SHRIKE_FI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_SHRIKE_FI)、[`CONFIG_BOARD_RAK3112`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RAK3112)、[`CONFIG_BOARD_M5STACK_ATOMS3_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_ATOMS3_LITE)、[`CONFIG_BOARD_M5STACK_CORES3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_CORES3)、[`CONFIG_BOARD_M5STACK_STAMPS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_STAMPS3)、[`CONFIG_BOARD_M5STACK_ATOMS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_ATOMS3)、[`CONFIG_BOARD_M5STACK_STACKCHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_STACKCHAN)、[`CONFIG_BOARD_M5STACK_PAPER_COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_PAPER_COLOR)、[`CONFIG_BOARD_M5STACK_STICKS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_STICKS3)、[`CONFIG_BOARD_WEACT_ESP32S3_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WEACT_ESP32S3_MINI)、[`CONFIG_BOARD_WEACT_ESP32S3_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WEACT_ESP32S3_B)、[`CONFIG_BOARD_HELTEC_WIFI_LORA32_V3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HELTEC_WIFI_LORA32_V3)、[`CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3)、[`CONFIG_BOARD_HELTEC_WIRELESS_TRACKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HELTEC_WIRELESS_TRACKER)、[`CONFIG_BOARD_ESP32S3_LUATOS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_LUATOS_CORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_MATOUCH_MTRO128G`、`CONFIG_BOARD_UEDX24320028E_WB_A`、`CONFIG_BOARD_UEDX32480035E_WB_A`、`CONFIG_BOARD_DNESP32S3B`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3`、`CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT`、`CONFIG_BOARD_RETERMINAL_E1001`、`CONFIG_BOARD_XIAO_ESP32S3`、`CONFIG_BOARD_RETERMINAL_E1003`、`CONFIG_BOARD_RETERMINAL_E1002`、`CONFIG_BOARD_EORA_HUB_900TB`、`CONFIG_BOARD_TWATCH_S3`、`CONFIG_BOARD_TDONGLE_S3`、`CONFIG_BOARD_TTGO_T8S3`、`CONFIG_BOARD_ESP32S3_BOX3`、`CONFIG_BOARD_ESP_THREADBR`、`CONFIG_BOARD_ESP32S3_DEVKITC`、`CONFIG_BOARD_ESP32S3_EYE`、`CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28`、`CONFIG_BOARD_ESP32S3_GEEK`、`CONFIG_BOARD_ESP32S3_MATRIX`、`CONFIG_BOARD_ESP32S3_RLCD_4_2`、`CONFIG_BOARD_WALTER`、`CONFIG_BOARD_SHRIKE_FI`、`CONFIG_BOARD_RAK3112`、`CONFIG_BOARD_M5STACK_ATOMS3_LITE`、`CONFIG_BOARD_M5STACK_CORES3`、`CONFIG_BOARD_M5STACK_STAMPS3`、`CONFIG_BOARD_M5STACK_ATOMS3`、`CONFIG_BOARD_M5STACK_STACKCHAN`、`CONFIG_BOARD_M5STACK_PAPER_COLOR`、`CONFIG_BOARD_M5STACK_STICKS3`、`CONFIG_BOARD_WEACT_ESP32S3_MINI`、`CONFIG_BOARD_WEACT_ESP32S3_B`、`CONFIG_BOARD_HELTEC_WIFI_LORA32_V3`、`CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3`、`CONFIG_BOARD_HELTEC_WIRELESS_TRACKER`、`CONFIG_BOARD_ESP32S3_LUATOS_CORE`。

<a id="CONFIG_SOC_ESP32S3_PROCPU"></a>

## 276.96 `CONFIG_SOC_ESP32S3_PROCPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为协议 CPU（PROCPU，内核 0）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_MATOUCH_MTRO128G
CONFIG_BOARD_UEDX24320028E_WB_A
CONFIG_BOARD_UEDX32480035E_WB_A
CONFIG_BOARD_DNESP32S3B
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3
CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT
CONFIG_BOARD_RETERMINAL_E1001
CONFIG_BOARD_XIAO_ESP32S3
CONFIG_BOARD_RETERMINAL_E1003
CONFIG_BOARD_RETERMINAL_E1002
CONFIG_BOARD_EORA_HUB_900TB
CONFIG_BOARD_TWATCH_S3
CONFIG_BOARD_TDONGLE_S3
CONFIG_BOARD_TTGO_T8S3
CONFIG_BOARD_T_DECK
CONFIG_BOARD_ESP32S3_BOX3
CONFIG_BOARD_ESP_THREADBR
CONFIG_BOARD_ESP32S3_DEVKITC
CONFIG_BOARD_ESP32S3_EYE
CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28
CONFIG_BOARD_ESP32S3_GEEK
CONFIG_BOARD_ESP32S3_MATRIX
CONFIG_BOARD_ESP32S3_RLCD_4_2
CONFIG_BOARD_WALTER
CONFIG_BOARD_SHRIKE_FI
CONFIG_BOARD_RAK3112
CONFIG_BOARD_M5STACK_ATOMS3_LITE
CONFIG_BOARD_M5STACK_CORES3
CONFIG_BOARD_M5STACK_STAMPS3
CONFIG_BOARD_M5STACK_ATOMS3
CONFIG_BOARD_M5STACK_STACKCHAN
CONFIG_BOARD_M5STACK_PAPER_COLOR
CONFIG_BOARD_M5STACK_STICKS3
CONFIG_BOARD_WEACT_ESP32S3_MINI
CONFIG_BOARD_WEACT_ESP32S3_B
CONFIG_BOARD_HELTEC_WIFI_LORA32_V3
CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3
CONFIG_BOARD_HELTEC_WIRELESS_TRACKER
CONFIG_BOARD_ESP32S3_LUATOS_CORE
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_MATOUCH_MTRO128G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MATOUCH_MTRO128G)、[`CONFIG_BOARD_UEDX24320028E_WB_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UEDX24320028E_WB_A)、[`CONFIG_BOARD_UEDX32480035E_WB_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UEDX32480035E_WB_A)、[`CONFIG_BOARD_DNESP32S3B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_DNESP32S3B)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3)、[`CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT)、[`CONFIG_BOARD_RETERMINAL_E1001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RETERMINAL_E1001)、[`CONFIG_BOARD_XIAO_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_ESP32S3)、[`CONFIG_BOARD_RETERMINAL_E1003`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RETERMINAL_E1003)、[`CONFIG_BOARD_RETERMINAL_E1002`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RETERMINAL_E1002)、[`CONFIG_BOARD_EORA_HUB_900TB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_EORA_HUB_900TB)、[`CONFIG_BOARD_TWATCH_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TWATCH_S3)、[`CONFIG_BOARD_TDONGLE_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TDONGLE_S3)、[`CONFIG_BOARD_TTGO_T8S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_T8S3)、[`CONFIG_BOARD_T_DECK`](P045_boards_lilygo_配置项参考.md#CONFIG_BOARD_T_DECK)、[`CONFIG_BOARD_ESP32S3_BOX3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_BOX3)、[`CONFIG_BOARD_ESP_THREADBR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP_THREADBR)、[`CONFIG_BOARD_ESP32S3_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_DEVKITC)、[`CONFIG_BOARD_ESP32S3_EYE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_EYE)、[`CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28)、[`CONFIG_BOARD_ESP32S3_GEEK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_GEEK)、[`CONFIG_BOARD_ESP32S3_MATRIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_MATRIX)、[`CONFIG_BOARD_ESP32S3_RLCD_4_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_RLCD_4_2)、[`CONFIG_BOARD_WALTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WALTER)、[`CONFIG_BOARD_SHRIKE_FI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_SHRIKE_FI)、[`CONFIG_BOARD_RAK3112`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RAK3112)、[`CONFIG_BOARD_M5STACK_ATOMS3_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_ATOMS3_LITE)、[`CONFIG_BOARD_M5STACK_CORES3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_CORES3)、[`CONFIG_BOARD_M5STACK_STAMPS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_STAMPS3)、[`CONFIG_BOARD_M5STACK_ATOMS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_ATOMS3)、[`CONFIG_BOARD_M5STACK_STACKCHAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_STACKCHAN)、[`CONFIG_BOARD_M5STACK_PAPER_COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_PAPER_COLOR)、[`CONFIG_BOARD_M5STACK_STICKS3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_STICKS3)、[`CONFIG_BOARD_WEACT_ESP32S3_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WEACT_ESP32S3_MINI)、[`CONFIG_BOARD_WEACT_ESP32S3_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_WEACT_ESP32S3_B)、[`CONFIG_BOARD_HELTEC_WIFI_LORA32_V3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HELTEC_WIFI_LORA32_V3)、[`CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3)、[`CONFIG_BOARD_HELTEC_WIRELESS_TRACKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HELTEC_WIRELESS_TRACKER)、[`CONFIG_BOARD_ESP32S3_LUATOS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32S3_LUATOS_CORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_MATOUCH_MTRO128G`、`CONFIG_BOARD_UEDX24320028E_WB_A`、`CONFIG_BOARD_UEDX32480035E_WB_A`、`CONFIG_BOARD_DNESP32S3B`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3`、`CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT`、`CONFIG_BOARD_RETERMINAL_E1001`、`CONFIG_BOARD_XIAO_ESP32S3`、`CONFIG_BOARD_RETERMINAL_E1003`、`CONFIG_BOARD_RETERMINAL_E1002`、`CONFIG_BOARD_EORA_HUB_900TB`、`CONFIG_BOARD_TWATCH_S3`、`CONFIG_BOARD_TDONGLE_S3`、`CONFIG_BOARD_TTGO_T8S3`、`CONFIG_BOARD_ESP32S3_BOX3`、`CONFIG_BOARD_ESP_THREADBR`、`CONFIG_BOARD_ESP32S3_DEVKITC`、`CONFIG_BOARD_ESP32S3_EYE`、`CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28`、`CONFIG_BOARD_ESP32S3_GEEK`、`CONFIG_BOARD_ESP32S3_MATRIX`、`CONFIG_BOARD_ESP32S3_RLCD_4_2`、`CONFIG_BOARD_WALTER`、`CONFIG_BOARD_SHRIKE_FI`、`CONFIG_BOARD_RAK3112`、`CONFIG_BOARD_M5STACK_ATOMS3_LITE`、`CONFIG_BOARD_M5STACK_CORES3`、`CONFIG_BOARD_M5STACK_STAMPS3`、`CONFIG_BOARD_M5STACK_ATOMS3`、`CONFIG_BOARD_M5STACK_STACKCHAN`、`CONFIG_BOARD_M5STACK_PAPER_COLOR`、`CONFIG_BOARD_M5STACK_STICKS3`、`CONFIG_BOARD_WEACT_ESP32S3_MINI`、`CONFIG_BOARD_WEACT_ESP32S3_B`、`CONFIG_BOARD_HELTEC_WIFI_LORA32_V3`、`CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3`、`CONFIG_BOARD_HELTEC_WIRELESS_TRACKER`、`CONFIG_BOARD_ESP32S3_LUATOS_CORE`。

<a id="CONFIG_SOC_ESP32_APPCPU"></a>

## 276.97 `CONFIG_SOC_ESP32_APPCPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为应用 CPU（APPCPU，内核 1）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_YD_ESP32
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32
CONFIG_BOARD_TTGO_T7V1_5
CONFIG_BOARD_TTGO_TBEAM
CONFIG_BOARD_TTGO_LORA32
CONFIG_BOARD_ESP32_ETHERNET_KIT
CONFIG_BOARD_ESP_WROVER_KIT
CONFIG_BOARD_ESP32_DEVKITC
CONFIG_BOARD_ESP32_CAM
CONFIG_BOARD_INKPLATE_6COLOR
CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1
CONFIG_BOARD_LOLIN32_LITE
CONFIG_BOARD_UDOO_KEY
CONFIG_BOARD_M5STACK_CORE2
CONFIG_BOARD_M5STACK_FIRE
CONFIG_BOARD_M5STICKC_PLUS
CONFIG_BOARD_M5STACK_ATOM_LITE
CONFIG_BOARD_OLIMEX_ESP32_EVB
CONFIG_BOARD_CAN485DBV1
CONFIG_BOARD_KINCONY_KC868_A8
CONFIG_BOARD_KINCONY_KC868_A32
CONFIG_BOARD_ODROID_GO
CONFIG_BOARD_HELTEC_WIFI_LORA32_V2
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_YD_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_YD_ESP32)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32)、[`CONFIG_BOARD_TTGO_T7V1_5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_T7V1_5)、[`CONFIG_BOARD_TTGO_TBEAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_TBEAM)、[`CONFIG_BOARD_TTGO_LORA32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_LORA32)、[`CONFIG_BOARD_ESP32_ETHERNET_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32_ETHERNET_KIT)、[`CONFIG_BOARD_ESP_WROVER_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP_WROVER_KIT)、[`CONFIG_BOARD_ESP32_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32_DEVKITC)、[`CONFIG_BOARD_ESP32_CAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32_CAM)、[`CONFIG_BOARD_INKPLATE_6COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_INKPLATE_6COLOR)、[`CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1)、[`CONFIG_BOARD_LOLIN32_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_LOLIN32_LITE)、[`CONFIG_BOARD_UDOO_KEY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UDOO_KEY)、[`CONFIG_BOARD_M5STACK_CORE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_CORE2)、[`CONFIG_BOARD_M5STACK_FIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_FIRE)、[`CONFIG_BOARD_M5STICKC_PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STICKC_PLUS)、[`CONFIG_BOARD_M5STACK_ATOM_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_ATOM_LITE)、[`CONFIG_BOARD_OLIMEX_ESP32_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_OLIMEX_ESP32_EVB)、[`CONFIG_BOARD_CAN485DBV1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CAN485DBV1)、[`CONFIG_BOARD_KINCONY_KC868_A8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_KINCONY_KC868_A8)、[`CONFIG_BOARD_KINCONY_KC868_A32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_KINCONY_KC868_A32)、[`CONFIG_BOARD_ODROID_GO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ODROID_GO)、[`CONFIG_BOARD_HELTEC_WIFI_LORA32_V2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HELTEC_WIFI_LORA32_V2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_YD_ESP32`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32`、`CONFIG_BOARD_TTGO_T7V1_5`、`CONFIG_BOARD_TTGO_TBEAM`、`CONFIG_BOARD_TTGO_LORA32`、`CONFIG_BOARD_ESP32_ETHERNET_KIT`、`CONFIG_BOARD_ESP_WROVER_KIT`、`CONFIG_BOARD_ESP32_DEVKITC`、`CONFIG_BOARD_ESP32_CAM`、`CONFIG_BOARD_INKPLATE_6COLOR`、`CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1`、`CONFIG_BOARD_LOLIN32_LITE`、`CONFIG_BOARD_UDOO_KEY`、`CONFIG_BOARD_M5STACK_CORE2`、`CONFIG_BOARD_M5STACK_FIRE`、`CONFIG_BOARD_M5STICKC_PLUS`、`CONFIG_BOARD_M5STACK_ATOM_LITE`、`CONFIG_BOARD_OLIMEX_ESP32_EVB`、`CONFIG_BOARD_CAN485DBV1`、`CONFIG_BOARD_KINCONY_KC868_A8`、`CONFIG_BOARD_KINCONY_KC868_A32`、`CONFIG_BOARD_ODROID_GO`、`CONFIG_BOARD_HELTEC_WIFI_LORA32_V2`。

<a id="CONFIG_SOC_ESP32_APPCPU_TARGET"></a>

## 276.98 `CONFIG_SOC_ESP32_APPCPU_TARGET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标是双核 Espressif SoC 的应用 CPU（APPCPU，内核 1）镜像。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_ESP32_APPCPU || CONFIG_SOC_ESP32S3_APPCPU
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.amp:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.amp#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_ESP32_APPCPU`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32_APPCPU)、[`CONFIG_SOC_ESP32S3_APPCPU`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32S3_APPCPU)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SOC_ESP32_ENABLE_PVT"></a>

## 276.99 `CONFIG_SOC_ESP32_ENABLE_PVT`

**提示（Prompt）**：使用工艺－电压－温度功能自动调节高性能／低功耗电压（PVT function）

**说明（Help）**

启用后，可根据工艺－电压－温度特性（PVT characteristic）自动调节高性能／低功耗（hp／lp）电压。否则，内部电压设置为固定的 dbias。此功能是稳定量产所必需的；仅应为调试而禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
n if CONFIG_SOC_SERIES_ESP32C6
y
```

**定义位置（Location）**：[`soc/espressif/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SOC_ESP32_PM_SLEEP_STATS"></a>

## 276.100 `CONFIG_SOC_ESP32_PM_SLEEP_STATS`

**提示（Prompt）**：记录轻度睡眠统计（Log light sleep statistics）

**说明（Help）**

为每个轻度睡眠窗口（light sleep window）记录一行日志，包含请求时间和实际执行时间、分段数量（fragment count）、断电标志（power down flags）及错误码。可用于不接电流表、直接在目标设备上检查外设是否断电。它会给睡眠路径增加少量开销。此行日志使用 `soc_pm` 的 `LOG_DBG` 级别，因此需要 `CONFIG_SOC_LOG_LEVEL_DBG` 才能打印。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**主动选择（Selects）**

```text
CONFIG_SOC_ESP32_SLEEP_DEBUG
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_SOC_ESP32_SLEEP_DEBUG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_SLEEP_DEBUG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`、`CONFIG_SOC_ESP32_SLEEP_DEBUG`。

<!-- kconfig-navigation -->

[上一章](P275_soc_espressif_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P277_soc_espressif_配置项参考_3.md)
