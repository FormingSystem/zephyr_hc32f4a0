---
id: learning.zephyr-docs.kconfig-reference.page-334
title: "`subsys/console`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第334章\_`subsys/console`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/console` 的 5 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CONSOLE_GETCHAR"></a>

## 334.1 `CONFIG_CONSOLE_GETCHAR`

**提示（Prompt）**：逐字符输入输出（Character by character input and output）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN
CONFIG_EVENTS
```

**定义位置（Location）**：[`subsys/console/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/console/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制台子系统／支持例程（Console subsystem/support routines） → 控制台读取函数选择（Console get function selection）

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_CONSOLE_GETCHAR_BUFSIZE"></a>

## 334.2 `CONFIG_CONSOLE_GETCHAR_BUFSIZE`

**提示（Prompt）**：console_getchar() 缓冲区大小（buffer size）

**说明（Help）**

`console_getchar()` 的缓冲区大小。默认值针对节省 RAM 进行优化；例如，需要支持主机端粘贴大量剪贴板内容时，可能需要增大。设为 `0` 可禁用中断驱动（interrupt-driven）操作，改用忙轮询（busy-polling）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CONSOLE_GETCHAR && CONFIG_CONSOLE_SUBSYS
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/console/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/console/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制台子系统／支持例程（Console subsystem/support routines）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE_GETCHAR`](P334_subsys_console_配置项参考.md#CONFIG_CONSOLE_GETCHAR)、[`CONFIG_CONSOLE_SUBSYS`](P334_subsys_console_配置项参考.md#CONFIG_CONSOLE_SUBSYS)。

<a id="CONFIG_CONSOLE_GETLINE"></a>

## 334.3 `CONFIG_CONSOLE_GETLINE`

**提示（Prompt）**：逐行输入（Line by line input）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE_HANDLER
```

**定义位置（Location）**：[`subsys/console/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/console/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制台子系统／支持例程（Console subsystem/support routines） → 控制台读取函数选择（Console get function selection）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE_HANDLER`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE_HANDLER)。

<a id="CONFIG_CONSOLE_PUTCHAR_BUFSIZE"></a>

## 334.4 `CONFIG_CONSOLE_PUTCHAR_BUFSIZE`

**提示（Prompt）**：console_putchar() 缓冲区大小（buffer size）

**说明（Help）**

`console_putchar()` 的缓冲区大小。默认值针对节省 RAM 进行优化；例如，需要支持主机端粘贴大量剪贴板内容时，可能需要增大。设为 `0` 可禁用中断驱动（interrupt-driven）操作，改用忙轮询（busy-polling）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CONSOLE_GETCHAR && CONFIG_CONSOLE_SUBSYS
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/console/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/console/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制台子系统／支持例程（Console subsystem/support routines）

**配置项引用（Symbol References）**：[`CONFIG_CONSOLE_GETCHAR`](P334_subsys_console_配置项参考.md#CONFIG_CONSOLE_GETCHAR)、[`CONFIG_CONSOLE_SUBSYS`](P334_subsys_console_配置项参考.md#CONFIG_CONSOLE_SUBSYS)。

<a id="CONFIG_CONSOLE_SUBSYS"></a>

## 334.5 `CONFIG_CONSOLE_SUBSYS`

**提示（Prompt）**：控制台子系统／支持例程（Console subsystem/support routines）

**说明（Help）**

控制台子系统与辅助函数（Console subsystem and helper functions）

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/console/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/console/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

<!-- kconfig-navigation -->

[上一章](P333_subsys_canbus_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P335_subsys_cpu_freq_配置项参考.md)
