---
id: learning.zephyr-docs.kconfig-reference.page-288
title: "`soc/neorv32`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第288章\_`soc/neorv32`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/neorv32` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_NEORV32"></a>

## 288.1 `CONFIG_SOC_NEORV32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NEORV32 处理器（片上系统，SoC）。为了支持 Zephyr，NEORV32 CPU 实现必须启用以下 RISC-V 指令集架构扩展（ISA extensions）：

- Zicsr，始终启用。
- Zifencei，始终启用。
- Zicntr。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_NEORV32
```

**定义位置（Location）**：[`soc/neorv32/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/neorv32/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_NEORV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NEORV32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NEORV32`。

<a id="CONFIG_SOC_NEORV32_READ_FREQUENCY_AT_RUNTIME"></a>

## 288.2 `CONFIG_SOC_NEORV32_READ_FREQUENCY_AT_RUNTIME`

**提示（Prompt）**：运行时读取 NEORV32 时钟频率（clock frequency at runtime）

**说明（Help）**

启用后，启动时会从 SYSINFO 读取 NEORV32 时钟频率（clock frequency），这会产生少量开销。如果构建时已知频率，可设置设备树 `cpu@0` 节点的 `clock-frequency` 属性以避免此开销。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_SYS_CLOCK_EXISTS && CONFIG_SOC_NEORV32
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SOC_EARLY_INIT_HOOK
CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME
```

**定义位置（Location）**：[`soc/neorv32/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/neorv32/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_SOC_NEORV32`](P288_soc_neorv32_配置项参考.md#CONFIG_SOC_NEORV32)、[`CONFIG_SOC_EARLY_INIT_HOOK`](P002_kernel_配置项参考_2.md#CONFIG_SOC_EARLY_INIT_HOOK)、[`CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME)。

<a id="CONFIG_SOC_NEORV32_VERSION"></a>

## 288.3 `CONFIG_SOC_NEORV32_VERSION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

目标 NEORV32 版本，以二进制编码十进制数（BCD-coded number）表示。格式与 NEORV32 机器实现标识寄存器（Machine implementation ID，`mimpid`）相同。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NEORV32
```

**默认值（Defaults）**

```text
0x01110600
```

**定义位置（Location）**：[`soc/neorv32/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/neorv32/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NEORV32`](P288_soc_neorv32_配置项参考.md#CONFIG_SOC_NEORV32)。

<a id="SB_CONFIG_SOC_NEORV32"></a>

## 288.4 `SB_CONFIG_SOC_NEORV32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

NEORV32 处理器（片上系统，SoC）。为了支持 Zephyr，NEORV32 CPU 实现必须启用以下 RISC-V 指令集架构扩展（ISA extensions）：

- Zicsr，始终启用。
- Zifencei，始终启用。
- Zicntr。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_NEORV32
```

**定义位置（Location）**：[`soc/neorv32/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/neorv32/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_NEORV32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_NEORV32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_NEORV32`。

<!-- kconfig-navigation -->

[上一章](P287_soc_native_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P289_soc_nordic_配置项参考_1.md)
