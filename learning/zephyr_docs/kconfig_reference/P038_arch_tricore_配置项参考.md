---
id: learning.zephyr-docs.kconfig-reference.page-38
title: "`arch/tricore`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第38章\_`arch/tricore`配置项参考

本章翻译官方 Kconfig 数据库中 `arch/tricore` 的 4 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CPU_HAS_TRICORE_VIRTUALIZATION"></a>

## 38.1 `CONFIG_CPU_HAS_TRICORE_VIRTUALIZATION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由 TriCore 1.8 内核实现了虚拟机监控器扩展（Hypervisor Extension）的片上系统（SoC）选择。内核在复位时退出虚拟化模式（Virtualization Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_TC18 && CONFIG_TRICORE
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_TC4X
```

**定义位置（Location）**：[`arch/tricore/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/tricore/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → TriCore 架构选项（Architecture Options） → TriCore 处理器选项（Processor Options）

**配置项引用（Symbol References）**：[`CONFIG_CPU_TC18`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_TC18)、[`CONFIG_TRICORE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRICORE)、[`CONFIG_SOC_SERIES_TC4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TC4X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CPU_TC18`、`CONFIG_SOC_SERIES_TC4X`。

<a id="CONFIG_TRICORE_CSA_COUNT"></a>

## 38.2 `CONFIG_TRICORE_CSA_COUNT`

**提示（Prompt）**：分配的上下文保存区数量（Context Save Areas）

**说明（Help）**

控制内核分配的上下文保存区（Context Save Area，CSA）数量。CSA 用于在函数调用和中断期间保存上部上下文（Upper Context）与下部上下文（Lower Context）信息。默认值 256 通常足以满足大多数应用；如果应用具有大量嵌套函数调用、中断或线程，可以增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRICORE
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`arch/tricore/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/tricore/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → TriCore 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_TRICORE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRICORE)。

<a id="CONFIG_TRICORE_CSA_FCD_RESERVE"></a>

## 38.3 `CONFIG_TRICORE_CSA_FCD_RESERVE`

**提示（Prompt）**：在 LCX 以下为 FCD 陷阱处理程序保留的上下文保存区（Context Save Areas）

**说明（Help）**

在 `LCX` 限制寄存器与空闲链表（Free List）末端之间保留的上下文保存区（CSA）数量。当一次上下文保存到达 `LCX` 时，会触发空闲上下文链表耗尽陷阱（Free Context list Depletion，FCD），其处理程序使用这些保留区运行。指令集架构（ISA）要求至少保留两个 CSA，处理程序每进行一次调用还需额外增加一个。默认值为故障处理和线程终止路径留出了空间，使耗尽情况可以恢复，而不会进一步引发不可恢复的 FCU 陷阱。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRICORE
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`arch/tricore/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/tricore/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → TriCore 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_TRICORE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRICORE)。

<a id="CONFIG_TRICORE_RESET_TRAMPOLINE"></a>

## 38.4 `CONFIG_TRICORE_RESET_TRAMPOLINE`

**提示（Prompt）**：跳转到可缓存地址的跳板（Trampoline）

**说明（Help）**

启用启动跳板函数（Startup Trampoline Function），从任意地址，例如不可缓存地址，跳转到实际的启动函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRICORE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`arch/tricore/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/tricore/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → TriCore 架构选项（Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_TRICORE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRICORE)。

<!-- kconfig-navigation -->

[上一章](P037_arch_sparc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P039_arch_x86_配置项参考.md)
