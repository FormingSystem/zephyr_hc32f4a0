---
id: learning.zephyr-docs.kconfig-reference.page-424
title: "`subsys/shell`配置项参考（1/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第424章\_`subsys/shell`配置项参考（1/3）

本章翻译官方 Kconfig 数据库中 `subsys/shell` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_APP_VERSION_SHELL"></a>

## 424.1 `CONFIG_APP_VERSION_SHELL`

**提示（Prompt）**：应用版本信息命令行（Application version shell）

**说明（Help）**

此命令行命令（Shell command）提供对应用版本信息的只读访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
"" != "" && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/modules/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_DATE_SHELL"></a>

## 424.2 `CONFIG_DATE_SHELL`

**提示（Prompt）**：日期命令行（Date shell）

**说明（Help）**

此命令行（Shell）提供基于 Unix 时间（Unix time）的日期和时间访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/modules/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_DEVICE_SHELL"></a>

## 424.3 `CONFIG_DEVICE_SHELL`

**提示（Prompt）**：设备命令行（Device shell）

**说明（Help）**

此命令行（Shell）提供访问基本设备数据的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/modules/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_DEVICE_SHELL_INIT_CMD"></a>

## 424.4 `CONFIG_DEVICE_SHELL_INIT_CMD`

**提示（Prompt）**：设备命令行初始化命令（Device shell init command）

**说明（Help）**

向设备命令行模块添加 `init` 命令，用于在运行时手动初始化具有 `zephyr,deferred-init` 属性的设备。注意，启用 `CONFIG_DEVICE_DEPS` 后，会同时考虑设备依赖关系（Dependencies）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEVICE_SHELL && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/modules/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 设备命令行（Device shell）

**配置项引用（Symbol References）**：[`CONFIG_DEVICE_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_DEVICE_SHELL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_DEVMEM_SHELL"></a>

## 424.5 `CONFIG_DEVMEM_SHELL`

**提示（Prompt）**：物理内存访问命令行（Devmem shell）

**说明（Help）**

此命令行命令（Shell command）提供物理内存（Physical memory）的读写访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**主动选择（Selects）**

```text
CONFIG_GETOPT
```

**定义位置（Location）**：[`subsys/shell/modules/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)、[`CONFIG_GETOPT`](P197_lib_配置项参考_1.md#CONFIG_GETOPT)。

<a id="CONFIG_KERNEL_SHELL"></a>

## 424.6 `CONFIG_KERNEL_SHELL`

**提示（Prompt）**：内核命令行（Kernel shell）

**说明（Help）**

此命令行（Shell）提供访问内核版本、运行时间（Uptime）等基本数据及其他实用信息的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_SMOKE_TESTS
CONFIG_UPDATEHUB_SHELL
```

**弱选择（Implies）**

```text
CONFIG_INIT_STACKS
CONFIG_THREAD_MONITOR
CONFIG_THREAD_NAME
CONFIG_THREAD_STACK_INFO
```

**定义位置（Location）**：[`subsys/shell/modules/kernel_service/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/kernel_service/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)、[`CONFIG_NXP_WIFI_SMOKE_TESTS`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SMOKE_TESTS)、[`CONFIG_UPDATEHUB_SHELL`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB_SHELL)、[`CONFIG_INIT_STACKS`](P001_kernel_配置项参考_1.md#CONFIG_INIT_STACKS)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)。

<a id="CONFIG_KERNEL_SHELL_PANIC_CMD"></a>

## 424.7 `CONFIG_KERNEL_SHELL_PANIC_CMD`

**提示（Prompt）**：添加内核致命错误命令（Panic command）

**说明（Help）**

无论是否安装了致命错误处理程序（Fatal error handler），都可能需要一种方式，通过命令行可靠地生成类似崩溃的内核致命错误（Kernel panic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_KERNEL_SHELL && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/modules/kernel_service/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/kernel_service/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内核命令行（Kernel shell）

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_SHELL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_KERNEL_SHELL_REBOOT_DELAY"></a>

## 424.8 `CONFIG_KERNEL_SHELL_REBOOT_DELAY`

**提示（Prompt）**：接收命令行重启命令到实际重启之间的延迟（毫秒）

**说明（Help）**

此延迟让命令行（Shell）有时间完整回显输入的重启命令，再执行会突然终止命令行的重启操作。与命令行交互、且需要等待重启命令回显完成的外部系统，可以借此与设备同步。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_REBOOT && CONFIG_KERNEL_SHELL && CONFIG_SHELL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/shell/modules/kernel_service/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/kernel_service/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内核命令行（Kernel shell）

**配置项引用（Symbol References）**：[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)、[`CONFIG_KERNEL_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_SHELL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_KERNEL_THREAD_SHELL"></a>

## 424.9 `CONFIG_KERNEL_THREAD_SHELL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部辅助宏（Helper macro），用于确定是否编译顶层 `thread` 命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_MONITOR && CONFIG_KERNEL_SHELL && CONFIG_SHELL
```

**被选择（Selected by）**

```text
CONFIG_KERNEL_THREAD_SHELL_LIST
CONFIG_KERNEL_THREAD_SHELL_STACKS
CONFIG_KERNEL_THREAD_SHELL_MASK
CONFIG_KERNEL_THREAD_SHELL_PIN
CONFIG_KERNEL_THREAD_SHELL_UNWIND
CONFIG_KERNEL_THREAD_SHELL_SUSPEND
CONFIG_KERNEL_THREAD_SHELL_RESUME
CONFIG_KERNEL_THREAD_SHELL_KILL
```

**定义位置（Location）**：[`subsys/shell/modules/kernel_service/thread/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/kernel_service/thread/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内核命令行（Kernel shell）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_KERNEL_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_SHELL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_KERNEL_THREAD_SHELL_LIST`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL_LIST)、[`CONFIG_KERNEL_THREAD_SHELL_STACKS`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL_STACKS)、[`CONFIG_KERNEL_THREAD_SHELL_MASK`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL_MASK)、[`CONFIG_KERNEL_THREAD_SHELL_PIN`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL_PIN)、[`CONFIG_KERNEL_THREAD_SHELL_UNWIND`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL_UNWIND)、[`CONFIG_KERNEL_THREAD_SHELL_SUSPEND`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL_SUSPEND)、[`CONFIG_KERNEL_THREAD_SHELL_RESUME`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL_RESUME)、[`CONFIG_KERNEL_THREAD_SHELL_KILL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL_KILL)。

<a id="CONFIG_KERNEL_THREAD_SHELL_KILL"></a>

## 424.10 `CONFIG_KERNEL_THREAD_SHELL_KILL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部辅助宏（Helper macro），用于编译 `kill` 子命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_MONITOR && CONFIG_KERNEL_SHELL && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_KERNEL_THREAD_SHELL
```

**定义位置（Location）**：[`subsys/shell/modules/kernel_service/thread/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/kernel_service/thread/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内核命令行（Kernel shell）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_KERNEL_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_SHELL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_KERNEL_THREAD_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL)。

<a id="CONFIG_KERNEL_THREAD_SHELL_LIST"></a>

## 424.11 `CONFIG_KERNEL_THREAD_SHELL_LIST`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部辅助宏（Helper macro），用于编译 `list` 子命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INIT_STACKS && CONFIG_THREAD_MONITOR && CONFIG_THREAD_STACK_INFO && CONFIG_KERNEL_SHELL && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_KERNEL_THREAD_SHELL
```

**定义位置（Location）**：[`subsys/shell/modules/kernel_service/thread/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/kernel_service/thread/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内核命令行（Kernel shell）

**配置项引用（Symbol References）**：[`CONFIG_INIT_STACKS`](P001_kernel_配置项参考_1.md#CONFIG_INIT_STACKS)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_KERNEL_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_SHELL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_KERNEL_THREAD_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL)。

<a id="CONFIG_KERNEL_THREAD_SHELL_MASK"></a>

## 424.12 `CONFIG_KERNEL_THREAD_SHELL_MASK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部辅助宏（Helper macro），用于编译 `mask` 子命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SCHED_CPU_MASK && CONFIG_KERNEL_SHELL && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_KERNEL_THREAD_SHELL
```

**定义位置（Location）**：[`subsys/shell/modules/kernel_service/thread/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/kernel_service/thread/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内核命令行（Kernel shell）

**配置项引用（Symbol References）**：[`CONFIG_SCHED_CPU_MASK`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_CPU_MASK)、[`CONFIG_KERNEL_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_SHELL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_KERNEL_THREAD_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL)。

<a id="CONFIG_KERNEL_THREAD_SHELL_PIN"></a>

## 424.13 `CONFIG_KERNEL_THREAD_SHELL_PIN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部辅助宏（Helper macro），用于编译 `pin` 子命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SCHED_CPU_MASK && CONFIG_KERNEL_SHELL && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_KERNEL_THREAD_SHELL
```

**定义位置（Location）**：[`subsys/shell/modules/kernel_service/thread/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/kernel_service/thread/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内核命令行（Kernel shell）

**配置项引用（Symbol References）**：[`CONFIG_SCHED_CPU_MASK`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_CPU_MASK)、[`CONFIG_KERNEL_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_SHELL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_KERNEL_THREAD_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL)。

<a id="CONFIG_KERNEL_THREAD_SHELL_RESUME"></a>

## 424.14 `CONFIG_KERNEL_THREAD_SHELL_RESUME`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部辅助宏（Helper macro），用于编译 `resume` 子命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_MONITOR && CONFIG_KERNEL_SHELL && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_KERNEL_THREAD_SHELL
```

**定义位置（Location）**：[`subsys/shell/modules/kernel_service/thread/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/kernel_service/thread/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内核命令行（Kernel shell）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_KERNEL_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_SHELL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_KERNEL_THREAD_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL)。

<a id="CONFIG_KERNEL_THREAD_SHELL_STACKS"></a>

## 424.15 `CONFIG_KERNEL_THREAD_SHELL_STACKS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部辅助宏（Helper macro），用于编译 `stacks` 子命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INIT_STACKS && CONFIG_THREAD_MONITOR && CONFIG_THREAD_STACK_INFO && CONFIG_KERNEL_SHELL && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_KERNEL_THREAD_SHELL
```

**定义位置（Location）**：[`subsys/shell/modules/kernel_service/thread/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/kernel_service/thread/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内核命令行（Kernel shell）

**配置项引用（Symbol References）**：[`CONFIG_INIT_STACKS`](P001_kernel_配置项参考_1.md#CONFIG_INIT_STACKS)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_KERNEL_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_SHELL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_KERNEL_THREAD_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL)。

<a id="CONFIG_KERNEL_THREAD_SHELL_SUSPEND"></a>

## 424.16 `CONFIG_KERNEL_THREAD_SHELL_SUSPEND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部辅助宏（Helper macro），用于编译 `suspend` 子命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_MONITOR && CONFIG_KERNEL_SHELL && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_KERNEL_THREAD_SHELL
```

**定义位置（Location）**：[`subsys/shell/modules/kernel_service/thread/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/kernel_service/thread/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内核命令行（Kernel shell）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_KERNEL_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_SHELL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_KERNEL_THREAD_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL)。

<a id="CONFIG_KERNEL_THREAD_SHELL_UNWIND"></a>

## 424.17 `CONFIG_KERNEL_THREAD_SHELL_UNWIND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

内部辅助宏（Helper macro），用于编译 `unwind` 子命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_STACKWALK && CONFIG_THREAD_MONITOR && CONFIG_KERNEL_SHELL && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_KERNEL_THREAD_SHELL
```

**定义位置（Location）**：[`subsys/shell/modules/kernel_service/thread/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/kernel_service/thread/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内核命令行（Kernel shell）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_STACKWALK`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_STACKWALK)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_KERNEL_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_SHELL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_KERNEL_THREAD_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_KERNEL_THREAD_SHELL)。

<a id="CONFIG_SCHED_STATS_SHELL"></a>

## 424.18 `CONFIG_SCHED_STATS_SHELL`

**提示（Prompt）**：调度器统计命令行（Scheduler stats shell：`sched cpus/threads/top`）

**说明（Help）**

注册支持对称多处理（SMP）的调度器统计命令：`sched cpus`、`sched threads` 和 `sched top`。它们使用 `k_thread_runtime_stats_*()`，显示每个 CPU 的忙碌与空闲利用率，以及包含 CPU 百分比和栈使用百分比的紧凑线程表。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_THREAD_RUNTIME_STATS && CONFIG_SCHED_THREAD_USAGE && CONFIG_SCHED_THREAD_USAGE_ALL && CONFIG_THREAD_MONITOR && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/modules/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_THREAD_RUNTIME_STATS`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_RUNTIME_STATS)、[`CONFIG_SCHED_THREAD_USAGE`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_THREAD_USAGE)、[`CONFIG_SCHED_THREAD_USAGE_ALL`](P002_kernel_配置项参考_2.md#CONFIG_SCHED_THREAD_USAGE_ALL)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)。

<a id="CONFIG_SHELL"></a>

## 424.19 `CONFIG_SHELL`

**提示（Prompt）**：命令行解释器（Shell）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_XEN_SHELL
CONFIG_ARM_SCMI_SHELL
CONFIG_MODEM_SHELL
CONFIG_MODEM_CELLULAR_SHELL
CONFIG_BT_MESH_SHELL
CONFIG_BT_SHELL
CONFIG_NET_L2_IEEE802154_SHELL
CONFIG_LWM2M_SHELL
CONFIG_NET_SHELL
CONFIG_ZTEST_SHELL
```

**弱选择（Implies）**

```text
CONFIG_LOG_RUNTIME_FILTERING
```

**被弱选择（Implied by）**

```text
CONFIG_MPIPE_PLAYER
```

**定义位置（Location）**：[`subsys/shell/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_XEN_SHELL`](P025_module_xenlib_Kconfig_配置项参考.md#CONFIG_XEN_SHELL)、[`CONFIG_ARM_SCMI_SHELL`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI_SHELL)、[`CONFIG_MODEM_SHELL`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SHELL)、[`CONFIG_MODEM_CELLULAR_SHELL`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR_SHELL)、[`CONFIG_BT_MESH_SHELL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_SHELL)、[`CONFIG_BT_SHELL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SHELL)、[`CONFIG_NET_L2_IEEE802154_SHELL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_IEEE802154_SHELL)、[`CONFIG_LWM2M_SHELL`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SHELL)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_ZTEST_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_SHELL)、[`CONFIG_LOG_RUNTIME_FILTERING`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_RUNTIME_FILTERING)、[`CONFIG_MPIPE_PLAYER`](P390_subsys_mpipe_配置项参考.md#CONFIG_MPIPE_PLAYER)。

<a id="CONFIG_SHELL_ALIASES"></a>

## 424.20 `CONFIG_SHELL_ALIASES`

**提示（Prompt）**：支持命令别名（Command alias）

**说明（Help）**

命令别名（Alias）的用法与 Linux shell 相同，可通过给现有命令取短名称减少输入。例如，为 `kernel thread stacks` 定义别名 `stacks="kernel thread stacks"` 后，输入 `stacks` 就会执行完整的 `kernel thread stacks` 命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:479`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L479)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_ALIASES_FILE"></a>

## 424.21 `CONFIG_SHELL_ALIASES_FILE`

**提示（Prompt）**：存储别名（Alias）的宿主机文件

**说明（Help）**

别名文件（Aliases file）每行保存一个别名，用户必须在宿主机端创建此文件。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_ALIASES && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:498`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L498)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 支持命令别名（Command alias）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_ALIASES`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_ALIASES)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_ARGC_MAX"></a>

## 424.22 `CONFIG_SHELL_ARGC_MAX`

**提示（Prompt）**：命令行命令的最大参数数量（Maximum arguments）

**说明（Help）**

构成一个命令的最大参数（Argument）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
30 if CONFIG_NET_L2_WIFI_SHELL
71 if CONFIG_CAN_SHELL
20
```

**取值范围（Ranges）**

```text
[3, 255]
```

**定义位置（Location）**：[`subsys/shell/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_NET_L2_WIFI_SHELL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_SHELL)、[`CONFIG_CAN_SHELL`](P060_drivers_can_配置项参考.md#CONFIG_CAN_SHELL)。

<a id="CONFIG_SHELL_ASCII_FILTER"></a>

## 424.23 `CONFIG_SHELL_ASCII_FILTER`

**提示（Prompt）**：过滤传入的 ASCII 字符（Character）

**说明（Help）**

命令行（Shell）不收集 ASCII 范围 `<0, 127>` 之外的字符。被过滤的字符不会显示在终端上，也不会传给命令处理程序（Command handler）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_ASYNC_API"></a>

## 424.24 `CONFIG_SHELL_ASYNC_API`

**提示（Prompt）**：异步命令行 API（Asynchronous shell API）

**说明（Help）**

启用异步命令行 API（Asynchronous shell API）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_AUTOSTART"></a>

## 424.25 `CONFIG_SHELL_AUTOSTART`

**提示（Prompt）**：启动时自动运行命令行（Auto-start shell）

**说明（Help）**

启用后，命令行线程首次被调度时启动命令行（Shell），同时启用其日志后端（Log backend）。此前经日志系统路由的日志及 `printk()` 输出，在延迟模式（Deferred mode）下缓冲，在即时模式（Immediate mode）下丢失。禁用本选项后，可由应用调用 `shell_start()`，例如从 `SYS_INIT()` 钩子中调用，以控制命令行启动时机。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:352`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L352)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKENDS"></a>

## 424.26 `CONFIG_SHELL_BACKENDS`

**提示（Prompt）**：Shell后端（Shell Backends）

**说明（Help）**

启用命令行后端（Shell backends）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_ADSP_MEMORY_WINDOW"></a>

## 424.27 `CONFIG_SHELL_BACKEND_ADSP_MEMORY_WINDOW`

**提示（Prompt）**：基于映射内存窗口（Mapped memory window）实现的命令行后端（Shell backend）。

**说明（Help）**

启用音频数字信号处理器（ADSP）内存窗口后端，让能够访问同一内存窗口的远端主机处理器执行命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:831`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L831)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_SHELL_BACKEND_ADSP_MEMORY_WINDOW_POLL_INTERVAL"></a>

## 424.28 `CONFIG_SHELL_BACKEND_ADSP_MEMORY_WINDOW_POLL_INTERVAL`

**提示（Prompt）**：轮询间隔（Poll interval，微秒）

**说明（Help）**

调整后端检查新命令时采用的轮询间隔（Poll interval）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_ADSP_MEMORY_WINDOW && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:847`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L847)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 基于映射内存窗口（Mapped memory window）实现的命令行后端（Shell backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_ADSP_MEMORY_WINDOW`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_ADSP_MEMORY_WINDOW)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_ADSP_MEMORY_WINDOW_PROMPT"></a>

## 424.29 `CONFIG_SHELL_BACKEND_ADSP_MEMORY_WINDOW_PROMPT`

**提示（Prompt）**：显示的提示符名称（Prompt Name）

**说明（Help）**

ADSP 内存窗口后端显示的提示符（Prompt）名称。设置提示符后，命令行初始化时发送两个换行符。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_ADSP_MEMORY_WINDOW && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"~$ "
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:840`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L840)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 基于映射内存窗口（Mapped memory window）实现的命令行后端（Shell backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_ADSP_MEMORY_WINDOW`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_ADSP_MEMORY_WINDOW)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_DUMMY"></a>

## 424.30 `CONFIG_SHELL_BACKEND_DUMMY`

**提示（Prompt）**：虚拟后端（Dummy backend）

**说明（Help）**

启用虚拟后端（Dummy backend），无需物理传输接口即可执行命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:773`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L773)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_DUMMY_BUF_SIZE"></a>

## 424.31 `CONFIG_SHELL_BACKEND_DUMMY_BUF_SIZE`

**提示（Prompt）**：虚拟缓冲区大小（Dummy buffer size）

**说明（Help）**

虚拟后端（Dummy backend）使用的输出缓冲区大小，限制能够从命令输出中捕获的字符数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_DUMMY && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
400 if CONFIG_LOG_PRINTK
300
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:788`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L788)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 虚拟后端（Dummy backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_DUMMY`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_DUMMY)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_LOG_PRINTK`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_PRINTK)。

<a id="CONFIG_SHELL_BACKEND_MQTT"></a>

## 424.32 `CONFIG_SHELL_BACKEND_MQTT`

**提示（Prompt）**：MQTT 后端（backend）

**说明（Help）**

启用消息队列遥测传输（MQTT）后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && CONFIG_NET_IPV4 && CONFIG_NETWORKING && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**主动选择（Selects）**

```text
CONFIG_DNS_RESOLVER
CONFIG_HWINFO
CONFIG_MQTT_LIB
CONFIG_NET_CONNECTION_MANAGER
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:291`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L291)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)。

<a id="CONFIG_SHELL_BACKEND_MQTT_LOG_MESSAGE_QUEUE_SIZE"></a>

## 424.33 `CONFIG_SHELL_BACKEND_MQTT_LOG_MESSAGE_QUEUE_SIZE`

**提示（Prompt）**：日志消息队列大小（Log message queue size）

**说明（Help）**

用于保存待命令行线程处理的日志消息的缓冲区大小。队列过小可能阻塞日志线程（Logger thread），参见 `$(module)_LOG_MESSAGE_QUEUE_TIMEOUT`；若命令行传输较慢而队列过大，可能因全部日志消息都已排入该队列，导致后续日志被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/shell/Kconfig.template.shell_log_queue_size:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig.template.shell_log_queue_size#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_MQTT_LOG_MESSAGE_QUEUE_TIMEOUT"></a>

## 424.34 `CONFIG_SHELL_BACKEND_MQTT_LOG_MESSAGE_QUEUE_TIMEOUT`

**提示（Prompt）**：日志消息丢弃超时（Drop timeout，毫秒）

**说明（Help）**

待处理日志消息队列满时，先等待指定时间；等待后仍满，则丢弃最旧日志消息。-1 表示一直等待。此期间日志线程（Logger thread）被阻塞，较长超时会影响其他日志后端，必须谨慎使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[-1, 10000]
```

**定义位置（Location）**：[`subsys/shell/Kconfig.template.shell_log_queue_timeout:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig.template.shell_log_queue_timeout#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_RPMSG"></a>

## 424.35 `CONFIG_SHELL_BACKEND_RPMSG`

**提示（Prompt）**：RPMsg 后端（backend）。

**说明（Help）**

启用远程处理器消息（RPMsg）后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:424`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L424)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP`](P208_modules_Kconfig.open-amp_配置项参考.md#CONFIG_OPENAMP)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_RPMSG_FORCE_TX_BLOCKING_MODE"></a>

## 424.36 `CONFIG_SHELL_BACKEND_RPMSG_FORCE_TX_BLOCKING_MODE`

**提示（Prompt）**：强制发送（TX）采用阻塞模式（Blocking mode）

**说明（Help）**

强制 RPMsg 命令行后端（Shell backend）等待可用的发送（TX）缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RPMSG && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:432`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L432)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RPMSG`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RPMSG)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_RPMSG_LOG_MESSAGE_QUEUE_SIZE"></a>

## 424.37 `CONFIG_SHELL_BACKEND_RPMSG_LOG_MESSAGE_QUEUE_SIZE`

**提示（Prompt）**：日志消息队列大小（Log message queue size）

**说明（Help）**

用于保存待命令行线程处理的日志消息的缓冲区大小。队列过小可能阻塞日志线程（Logger thread），参见 `$(module)_LOG_MESSAGE_QUEUE_TIMEOUT`；若命令行传输较慢而队列过大，可能因全部日志消息都已排入该队列，导致后续日志被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RPMSG && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/shell/Kconfig.template.shell_log_queue_size:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig.template.shell_log_queue_size#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RPMSG`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RPMSG)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_RPMSG_LOG_MESSAGE_QUEUE_TIMEOUT"></a>

## 424.38 `CONFIG_SHELL_BACKEND_RPMSG_LOG_MESSAGE_QUEUE_TIMEOUT`

**提示（Prompt）**：日志消息丢弃超时（Drop timeout，毫秒）

**说明（Help）**

待处理日志消息队列满时，先等待指定时间；等待后仍满，则丢弃最旧日志消息。-1 表示一直等待。此期间日志线程（Logger thread）被阻塞，较长超时会影响其他日志后端，必须谨慎使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RPMSG && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[-1, 10000]
```

**定义位置（Location）**：[`subsys/shell/Kconfig.template.shell_log_queue_timeout:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig.template.shell_log_queue_timeout#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RPMSG`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RPMSG)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_RTT"></a>

## 424.39 `CONFIG_SHELL_BACKEND_RTT`

**提示（Prompt）**：RTT 后端（Backend）

**说明（Help）**

启用实时传输（RTT）后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT && !(CONFIG_SHELL_LOG_BACKEND && CONFIG_LOG_MODE_IMMEDIATE) && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**主动选择（Selects）**

```text
CONFIG_CONSOLE
CONFIG_RTT_CONSOLE
CONFIG_SEGGER_RTT_CUSTOM_LOCKING
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends）

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)、[`CONFIG_SHELL_LOG_BACKEND`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_LOG_BACKEND)、[`CONFIG_LOG_MODE_IMMEDIATE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_IMMEDIATE)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_RTT_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_RTT_CONSOLE)、[`CONFIG_SEGGER_RTT_CUSTOM_LOCKING`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_CUSTOM_LOCKING)。

<a id="CONFIG_SHELL_BACKEND_RTT_BUFFER"></a>

## 424.40 `CONFIG_SHELL_BACKEND_RTT_BUFFER`

**提示（Prompt）**：用于命令行输入和输出的缓冲区编号（Buffer number）。

**说明（Help）**

选择命令行输出所用上行缓冲区（Up-buffer）的索引。默认使用终端上行缓冲区及其设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS]
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS)。

<a id="CONFIG_SHELL_BACKEND_RTT_LOG_MESSAGE_QUEUE_SIZE"></a>

## 424.41 `CONFIG_SHELL_BACKEND_RTT_LOG_MESSAGE_QUEUE_SIZE`

**提示（Prompt）**：日志消息队列大小（Log message queue size）

**说明（Help）**

用于保存待命令行线程处理的日志消息的缓冲区大小。队列过小可能阻塞日志线程（Logger thread），参见 `$(module)_LOG_MESSAGE_QUEUE_TIMEOUT`；若命令行传输较慢而队列过大，可能因全部日志消息都已排入该队列，导致后续日志被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/shell/Kconfig.template.shell_log_queue_size:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig.template.shell_log_queue_size#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_RTT_LOG_MESSAGE_QUEUE_TIMEOUT"></a>

## 424.42 `CONFIG_SHELL_BACKEND_RTT_LOG_MESSAGE_QUEUE_TIMEOUT`

**提示（Prompt）**：日志消息丢弃超时（Drop timeout，毫秒）

**说明（Help）**

待处理日志消息队列满时，先等待指定时间；等待后仍满，则丢弃最旧日志消息。-1 表示一直等待。此期间日志线程（Logger thread）被阻塞，较长超时会影响其他日志后端，必须谨慎使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[-1, 10000]
```

**定义位置（Location）**：[`subsys/shell/Kconfig.template.shell_log_queue_timeout:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig.template.shell_log_queue_timeout#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_RTT_RETRY_CNT"></a>

## 424.43 `CONFIG_SHELL_BACKEND_RTT_RETRY_CNT`

**提示（Prompt）**：重试次数（Number of Retries）

**说明（Help）**

在丢弃数据并认定 RTT 会话（Session）未活动之前，进行发送（TX）重试的次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_RTT_RETRY_DELAY_MS"></a>

## 424.44 `CONFIG_SHELL_BACKEND_RTT_RETRY_DELAY_MS`

**提示（Prompt）**：发送重试间隔，单位为毫秒（TX Retry Delay）

**说明（Help）**

两次发送重试（TX Retry）之间的休眠时间。实时传输（RTT）会话期间，主机定期拉取数据，周期从 1–2 毫秒起；RTT 流量增加时，包括主机到设备的流量，该周期可能增加。流量较大时可能丢失数据，需要增大延迟或重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_SERIAL"></a>

## 424.45 `CONFIG_SHELL_BACKEND_SERIAL`

**提示（Prompt）**：串行后端（Serial backend）

**说明（Help）**

启用串行后端（Serial backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SERIAL
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_API"></a>

## 424.46 `CONFIG_SHELL_BACKEND_SERIAL_API`

**提示（Prompt）**：模式（Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC if CONFIG_SHELL_ASYNC_API
CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN if CONFIG_SHELL_BACKEND_SERIAL_INTERRUPT_DRIVEN
CONFIG_SHELL_BACKEND_SERIAL_API_POLLING
```

**可选项（Choices）**

```text
CONFIG_SHELL_BACKEND_SERIAL_API_POLLING
CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN
CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC)、[`CONFIG_SHELL_ASYNC_API`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_ASYNC_API)、[`CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN)、[`CONFIG_SHELL_BACKEND_SERIAL_INTERRUPT_DRIVEN`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_INTERRUPT_DRIVEN)、[`CONFIG_SHELL_BACKEND_SERIAL_API_POLLING`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API_POLLING)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC"></a>

## 424.47 `CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC`

**提示（Prompt）**：异步（Asynchronous）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL_SUPPORT_ASYNC && <choice CONFIG_SHELL_BACKEND_SERIAL_API>
```

**主动选择（Selects）**

```text
CONFIG_UART_ASYNC_RX_HELPER
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend） → 模式（Mode）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL_SUPPORT_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_ASYNC)、[`CONFIG_SHELL_BACKEND_SERIAL_API`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API)、[`CONFIG_UART_ASYNC_RX_HELPER`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_RX_HELPER)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN"></a>

## 424.48 `CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN`

**提示（Prompt）**：中断驱动（Interrupt driven）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL_SUPPORT_INTERRUPT && <choice CONFIG_SHELL_BACKEND_SERIAL_API>
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend） → 模式（Mode）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SHELL_BACKEND_SERIAL_API`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_API_POLLING"></a>

## 424.49 `CONFIG_SHELL_BACKEND_SERIAL_API_POLLING`

**提示（Prompt）**：轮询（Polling）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SHELL_BACKEND_SERIAL_API>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend） → 模式（Mode）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL_API`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_ASYNC_RX_BUFFER_COUNT"></a>

## 424.50 `CONFIG_SHELL_BACKEND_SERIAL_ASYNC_RX_BUFFER_COUNT`

**提示（Prompt）**：接收缓冲区（RX Buffer）数量

**说明（Help）**

接收（RX）缓冲区数量。部分 UART 驱动实现在超时后切换缓冲区，因此数量应足以保证及时处理传入数据。除了 CPU 负载高且命令行线程延迟很大的情况外，4 个缓冲区几乎总是足够。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC && CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[2, 64]
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC)、[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_ASYNC_RX_BUFFER_SIZE"></a>

## 424.51 `CONFIG_SHELL_BACKEND_SERIAL_ASYNC_RX_BUFFER_SIZE`

**提示（Prompt）**：接收缓冲区（RX Buffer）大小

**说明（Help）**

单个接收缓冲区（RX Buffer）的大小。它与缓冲区数量共同决定可容纳接收数据的空间。如果命令行（Shell）输入较慢，可以减小此值；如果会将长消息直接粘贴到命令提示符处，则可能需要增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC && CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC)、[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_ASYNC_RX_TIMEOUT"></a>

## 424.52 `CONFIG_SHELL_BACKEND_SERIAL_ASYNC_RX_TIMEOUT`

**提示（Prompt）**：接收不活动超时（RX inactivity timeout，微秒）

**说明（Help）**

收到数据后，持续无活动达到此超时即上报接收数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC && CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC)、[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_CHECK_DTR"></a>

## 424.53 `CONFIG_SHELL_BACKEND_SERIAL_CHECK_DTR`

**提示（Prompt）**：发送（TX）前检查数据终端就绪（DTR）信号

**说明（Help）**

发送（TX）前检查数据终端就绪（DTR）信号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN && CONFIG_UART_LINE_CTRL && CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN)、[`CONFIG_UART_LINE_CTRL`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_LINE_CTRL)、[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_FORCE_TX_BLOCKING_MODE"></a>

## 424.54 `CONFIG_SHELL_BACKEND_SERIAL_FORCE_TX_BLOCKING_MODE`

**提示（Prompt）**：强制发送（TX）采用阻塞模式（Blocking mode）

**说明（Help）**

强制发送（TX）采用阻塞模式（Blocking mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_INIT_PRIORITY"></a>

## 424.55 `CONFIG_SHELL_BACKEND_SERIAL_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

UART 后端初始化优先级（Initialization priority），数值必须大于所用串行设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
CONFIG_APPLICATION_INIT_PRIORITY
```

**取值范围（Ranges）**

```text
[0, 99]
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_APPLICATION_INIT_PRIORITY`](P001_kernel_配置项参考_1.md#CONFIG_APPLICATION_INIT_PRIORITY)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_INTERRUPT_DRIVEN"></a>

## 424.56 `CONFIG_SHELL_BACKEND_SERIAL_INTERRUPT_DRIVEN`

**提示（Prompt）**：中断驱动（Interrupt driven）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL_SUPPORT_INTERRUPT && CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_UART_NATIVE_PTY
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_UART_NATIVE_PTY`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_NATIVE_PTY)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_LOG_LEVEL_DBG"></a>

## 424.57 `CONFIG_SHELL_BACKEND_SERIAL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_BACKEND_SERIAL_LOG_LEVEL_DEFAULT"></a>

## 424.58 `CONFIG_SHELL_BACKEND_SERIAL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：系统限制（System limit，`LOG_MAX_LEVEL`）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_BACKEND_SERIAL_LOG_LEVEL_ERR"></a>

## 424.59 `CONFIG_SHELL_BACKEND_SERIAL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_BACKEND_SERIAL_LOG_LEVEL_INF"></a>

## 424.60 `CONFIG_SHELL_BACKEND_SERIAL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_BACKEND_SERIAL_LOG_LEVEL_NONE"></a>

## 424.61 `CONFIG_SHELL_BACKEND_SERIAL_LOG_LEVEL_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_BACKEND_SERIAL_LOG_LEVEL_WRN"></a>

## 424.62 `CONFIG_SHELL_BACKEND_SERIAL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_BACKEND_SERIAL_LOG_MESSAGE_QUEUE_SIZE"></a>

## 424.63 `CONFIG_SHELL_BACKEND_SERIAL_LOG_MESSAGE_QUEUE_SIZE`

**提示（Prompt）**：日志消息队列大小（Log message queue size）

**说明（Help）**

用于保存待命令行线程处理的日志消息的缓冲区大小。队列过小可能阻塞日志线程（Logger thread），参见 `$(module)_LOG_MESSAGE_QUEUE_TIMEOUT`；若命令行传输较慢而队列过大，可能因全部日志消息都已排入该队列，导致后续日志被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/shell/Kconfig.template.shell_log_queue_size:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig.template.shell_log_queue_size#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_LOG_MESSAGE_QUEUE_TIMEOUT"></a>

## 424.64 `CONFIG_SHELL_BACKEND_SERIAL_LOG_MESSAGE_QUEUE_TIMEOUT`

**提示（Prompt）**：日志消息丢弃超时（Drop timeout，毫秒）

**说明（Help）**

待处理日志消息队列满时，先等待指定时间；等待后仍满，则丢弃最旧日志消息。-1 表示一直等待。此期间日志线程（Logger thread）被阻塞，较长超时会影响其他日志后端，必须谨慎使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[-1, 10000]
```

**定义位置（Location）**：[`subsys/shell/Kconfig.template.shell_log_queue_timeout:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig.template.shell_log_queue_timeout#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_NEEDS_LARGE_RING_BUFFER"></a>

## 424.65 `CONFIG_SHELL_BACKEND_SERIAL_NEEDS_LARGE_RING_BUFFER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

辅助 Kconfig 选项；实现需要大于 32 kB 的环形缓冲区（Ring buffer）时，选择 `RING_BUFFER_LARGE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if CONFIG_SHELL_BACKEND_SERIAL_TX_RING_BUFFER_SIZE > 32767
y if CONFIG_SHELL_BACKEND_SERIAL_RX_RING_BUFFER_SIZE > 32767
```

**主动选择（Selects）**

```text
CONFIG_RING_BUFFER_LARGE
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_BACKEND_SERIAL_TX_RING_BUFFER_SIZE`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_TX_RING_BUFFER_SIZE)、[`CONFIG_SHELL_BACKEND_SERIAL_RX_RING_BUFFER_SIZE`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_RX_RING_BUFFER_SIZE)、[`CONFIG_RING_BUFFER_LARGE`](P198_lib_配置项参考_2.md#CONFIG_RING_BUFFER_LARGE)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_RX_POLL_PERIOD"></a>

## 424.66 `CONFIG_SHELL_BACKEND_SERIAL_RX_POLL_PERIOD`

**提示（Prompt）**：接收轮询周期（RX polling period，毫秒）

**说明（Help）**

决定轮询 UART 接收字节（RX byte）的频率。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL_API_POLLING && CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL_API_POLLING`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API_POLLING)、[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_RX_RING_BUFFER_SIZE"></a>

## 424.67 `CONFIG_SHELL_BACKEND_SERIAL_RX_RING_BUFFER_SIZE`

**提示（Prompt）**：设置接收环形缓冲区（RX ring buffer）大小

**说明（Help）**

接收环形缓冲区（RX ring buffer）大小决定命令行处理传入字节时允许的延迟。输入来自键盘时，通常几个字节就够，但因转义序列（Escape sequence）至少需要多于一个字节；传输批量数据时，可能需要增大缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN || CONFIG_SHELL_BACKEND_SERIAL_API_POLLING) && CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
256 if CONFIG_MCUMGR_TRANSPORT_SHELL
64
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN)、[`CONFIG_SHELL_BACKEND_SERIAL_API_POLLING`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API_POLLING)、[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_MCUMGR_TRANSPORT_SHELL`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_SHELL)。

<a id="CONFIG_SHELL_BACKEND_SERIAL_TX_RING_BUFFER_SIZE"></a>

## 424.68 `CONFIG_SHELL_BACKEND_SERIAL_TX_RING_BUFFER_SIZE`

**提示（Prompt）**：设置发送环形缓冲区（TX ring buffer）大小

**说明（Help）**

如果 UART 使用直接内存访问（DMA）传输，增大发送环形缓冲区（Ring buffer）可增加单次传输长度，减少中断次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN && CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL_API_INTERRUPT_DRIVEN)、[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BACKEND_SSH"></a>

## 424.69 `CONFIG_SHELL_BACKEND_SSH`

**提示（Prompt）**：SSH 后端（backend）。

**说明（Help）**

启用安全外壳（Secure Shell，SSH）后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:514`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L514)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends）

**配置项引用（Symbol References）**：[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SHELL_BACKEND_TELNET"></a>

## 424.70 `CONFIG_SHELL_BACKEND_TELNET`

**提示（Prompt）**：TELNET 后端（backend）。

**说明（Help）**

启用 TELNET 后端。安全警告：此后端通过未经认证、未加密的 TCP 端口提供完整 Zephyr 命令行（Shell）。任何能够通过网络访问设备的人，都可获得与本地控制台用户相同的控制能力，通常包括擦除和写入闪存、重启、修改设置，以及通过命令行开放的各子系统获取秘密数据。除非网络路径本身可信，否则强烈不建议在生产环境使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && (CONFIG_NET_IPV4 || CONFIG_NET_IPV6) && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS_SERVICE
CONFIG_NET_SOCKETS
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_SMOKE_TESTS
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:535`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L535)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_NET_SOCKETS_SERVICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SERVICE)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NXP_WIFI_SMOKE_TESTS`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SMOKE_TESTS)。

<a id="CONFIG_SHELL_BACKEND_WEBSOCKET"></a>

## 424.71 `CONFIG_SHELL_BACKEND_WEBSOCKET`

**提示（Prompt）**：WebSocket 后端（backend）。

**说明（Help）**

启用 WebSocket 后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER_WEBSOCKET && CONFIG_NET_NATIVE_IP && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS_SERVICE
CONFIG_NET_SOCKETS
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:654`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L654)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends）

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER_WEBSOCKET`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_WEBSOCKET)、[`CONFIG_NET_NATIVE_IP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IP)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_NET_SOCKETS_SERVICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SERVICE)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IP`。

<a id="CONFIG_SHELL_BACKSPACE_MODE_DELETE"></a>

## 424.72 `CONFIG_SHELL_BACKSPACE_MODE_DELETE`

**提示（Prompt）**：退格键默认编码采用 DELETE（`0x7F`）

**说明（Help）**

不同终端对退格键（Backspace）的编码设置不同：有些发送 `0x08`，即 backspace；有些发送 `0x7F`，即 delete。启用此项后，命令行将退格键识别为 `0x7F`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_BYPASS_READ_BUF_SIZE"></a>

## 424.73 `CONFIG_SHELL_BYPASS_READ_BUF_SIZE`

**提示（Prompt）**：旁路读取缓冲区大小（Bypass read buffer size）

**说明（Help）**

旁路模式（Bypass mode）读取数据所用缓冲区的大小。缓冲区在栈上分配；旁路读取采用循环，因此较小的缓冲区即可。该值必须小于 `SHELL_STACK_SIZE`。使用 RTT 后端时，为保持向后兼容，默认值为 `SEGGER_RTT_BUFFER_SIZE_DOWN`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
CONFIG_SEGGER_RTT_BUFFER_SIZE_DOWN if CONFIG_SHELL_BACKEND_RTT
16
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/shell/Kconfig:391`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L391)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SEGGER_RTT_BUFFER_SIZE_DOWN`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_BUFFER_SIZE_DOWN)、[`CONFIG_SHELL_BACKEND_RTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RTT)。

<a id="CONFIG_SHELL_CMDS"></a>

## 424.74 `CONFIG_SHELL_CMDS`

**提示（Prompt）**：内置命令（Built-in commands）

**说明（Help）**

启用 `clear`、`history` 等内置命令（Built-in command）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SHELL_REMOTE_CLI && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:257`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L257)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_REMOTE_CLI`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE_CLI)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_CMDS_ALIASES"></a>

## 424.75 `CONFIG_SHELL_CMDS_ALIASES`

**提示（Prompt）**：别名命令（Aliases command）

**说明（Help）**

显示当前命令别名（Command alias）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_CMDS && CONFIG_SHELL_ALIASES && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:490`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L490)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 支持命令别名（Command alias）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_CMDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_CMDS)、[`CONFIG_SHELL_ALIASES`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_ALIASES)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_CMDS_RESIZE"></a>

## 424.76 `CONFIG_SHELL_CMDS_RESIZE`

**提示（Prompt）**：调整终端大小命令（Resize command）

**说明（Help）**

默认假定终端屏幕宽度为 80 个字符。每次终端宽度变化后，都必须调用 `resize` 命令，确保文字正确显示。可关闭此命令以节省约 0.5 k 的代码空间，原文写作 `~0,5k`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_CMDS && CONFIG_SHELL_VT100_COMMANDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:264`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L264)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内置命令（Built-in commands）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_CMDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_CMDS)、[`CONFIG_SHELL_VT100_COMMANDS`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_VT100_COMMANDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_CMDS_RETURN_VALUE"></a>

## 424.77 `CONFIG_SHELL_CMDS_RETURN_VALUE`

**提示（Prompt）**：返回值命令（Retval command）

**说明（Help）**

启用 `retval` 命令，用于获取最近一次执行命令的返回值（Return value）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_CMDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:364`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L364)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_CMDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_CMDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_CMDS_SELECT"></a>

## 424.78 `CONFIG_SHELL_CMDS_SELECT`

**提示（Prompt）**：选择命令（Select command）

**说明（Help）**

启用 `select` 命令，用于设置新的根命令（Root command）；按 `Alt+R` 可返回主命令树（Main command tree）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_CMDS && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:275`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L275)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 内置命令（Built-in commands）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_CMDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_CMDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_CMD_BUFF_SIZE"></a>

## 424.79 `CONFIG_SHELL_CMD_BUFF_SIZE`

**提示（Prompt）**：命令行命令缓冲区大小（Command buffer size）

**说明（Help）**

命令的最大大小，单位为字节；其中预留一个字节用于字符串结束符（String terminator）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
128 if CONFIG_SHELL_MINIMAL
256
```

**定义位置（Location）**：[`subsys/shell/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_CMD_ROOT"></a>

## 424.80 `CONFIG_SHELL_CMD_ROOT`

**提示（Prompt）**：初始化时设置根命令（Root command）

**说明（Help）**

在命令行初始化时，以及按 `Alt+R` 返回主命令树时，设置指定的根命令（Root command）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:282`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L282)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_CUSTOM_HEADER"></a>

## 424.81 `CONFIG_SHELL_CUSTOM_HEADER`

**提示（Prompt）**：包含自定义命令行头文件（Custom Shell Header）［实验性，Experimental］

**说明（Help）**

启用后，在 `shell.h` 末尾包含应用提供的自定义头文件 `zephyr_custom_shell.h`，以在宏（Macro）层面扩展命令行 API。请谨慎使用，内部命令行 API 可能在未来版本改变。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:372`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L372)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_SHELL_DEFAULT_TERMINAL_HEIGHT"></a>

## 424.82 `CONFIG_SHELL_DEFAULT_TERMINAL_HEIGHT`

**提示（Prompt）**：默认终端高度（Terminal height）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
24
```

**定义位置（Location）**：[`subsys/shell/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_DEFAULT_TERMINAL_WIDTH"></a>

## 424.83 `CONFIG_SHELL_DEFAULT_TERMINAL_WIDTH`

**提示（Prompt）**：默认终端宽度（Terminal width）

**说明（Help）**

默认终端宽度（Terminal width）用于决定换行位置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
80
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/shell/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_DEVICE_HELPERS"></a>

## 424.84 `CONFIG_SHELL_DEVICE_HELPERS`

**提示（Prompt）**：命令行设备辅助功能（Shell device helpers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**弱选择（Implies）**

```text
CONFIG_DEVICE_DT_METADATA
```

**定义位置（Location）**：[`subsys/shell/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)、[`CONFIG_DEVICE_DT_METADATA`](P001_kernel_配置项参考_1.md#CONFIG_DEVICE_DT_METADATA)。

<a id="CONFIG_SHELL_DUMMY_INIT_LOG_LEVEL_DBG"></a>

## 424.85 `CONFIG_SHELL_DUMMY_INIT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:803`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L803)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 虚拟后端（Dummy backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_DUMMY_INIT_LOG_LEVEL_DEFAULT"></a>

## 424.86 `CONFIG_SHELL_DUMMY_INIT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：系统限制（System limit，`LOG_MAX_LEVEL`）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:800`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L800)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 虚拟后端（Dummy backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_DUMMY_INIT_LOG_LEVEL_ERR"></a>

## 424.87 `CONFIG_SHELL_DUMMY_INIT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:812`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L812)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 虚拟后端（Dummy backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_DUMMY_INIT_LOG_LEVEL_INF"></a>

## 424.88 `CONFIG_SHELL_DUMMY_INIT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:806`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L806)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 虚拟后端（Dummy backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_DUMMY_INIT_LOG_LEVEL_NONE"></a>

## 424.89 `CONFIG_SHELL_DUMMY_INIT_LOG_LEVEL_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:815`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L815)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 虚拟后端（Dummy backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_DUMMY_INIT_LOG_LEVEL_WRN"></a>

## 424.90 `CONFIG_SHELL_DUMMY_INIT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:809`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L809)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 虚拟后端（Dummy backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_ECHO_STATUS"></a>

## 424.91 `CONFIG_SHELL_ECHO_STATUS`

**提示（Prompt）**：命令行回显（Shell echo）

**说明（Help）**

启用后，命令行（Shell）回显每个输入字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_GETOPT"></a>

## 424.92 `CONFIG_SHELL_GETOPT`

**提示（Prompt）**：命令行中线程安全的 `getopt` 支持

**说明（Help）**

为命令行实例创建独立的 `getopt_state`，保证在命令行中使用 `getopt` 的线程安全性（Thread safety）。如果多个线程使用 `sys_getopt`，请调用 `sys_getopt_state_get` 获取命令行线程的 getopt 状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**主动选择（Selects）**

```text
CONFIG_GETOPT
```

**被选择（Selected by）**

```text
CONFIG_BT_SHELL
CONFIG_NET_L2_WIFI_SHELL
CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED
CONFIG_NET_SHELL_TFTP_CLIENT_SUPPORTED
CONFIG_NET_SHELL_IP_TABLE_SUPPORTED
CONFIG_SSH_SHELL
CONFIG_WIFI_CREDENTIALS_SHELL
CONFIG_WIREGUARD_SHELL
CONFIG_POSIX_UNAME_SHELL
CONFIG_ZTEST_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:200`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L200)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_GETOPT`](P197_lib_配置项参考_1.md#CONFIG_GETOPT)、[`CONFIG_BT_SHELL`](P331_subsys_bluetooth_配置项参考_12.md#CONFIG_BT_SHELL)、[`CONFIG_NET_L2_WIFI_SHELL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_SHELL)、[`CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED)、[`CONFIG_NET_SHELL_TFTP_CLIENT_SUPPORTED`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_TFTP_CLIENT_SUPPORTED)、[`CONFIG_NET_SHELL_IP_TABLE_SUPPORTED`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_IP_TABLE_SUPPORTED)、[`CONFIG_SSH_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_SHELL)、[`CONFIG_WIFI_CREDENTIALS_SHELL`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_SHELL)、[`CONFIG_WIREGUARD_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_SHELL)、[`CONFIG_POSIX_UNAME_SHELL`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_UNAME_SHELL)、[`CONFIG_ZTEST_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_SHELL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH_SHELL`、`CONFIG_WIREGUARD_SHELL`。

<a id="CONFIG_SHELL_HELP"></a>

## 424.93 `CONFIG_SHELL_HELP`

**提示（Prompt）**：帮助信息（Help message）

**说明（Help）**

启用命令行中用于打印格式化帮助信息（Formatted help message）的函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_HELP_ON_WRONG_ARGUMENT_COUNT"></a>

## 424.94 `CONFIG_SHELL_HELP_ON_WRONG_ARGUMENT_COUNT`

**提示（Prompt）**：参数数量错误时打印帮助信息（Help）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_HELP && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L233)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 帮助信息（Help message）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_HELP`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_HELP)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_HELP_OPT_PARSE"></a>

## 424.95 `CONFIG_SHELL_HELP_OPT_PARSE`

**提示（Prompt）**：解析 `-h` 与 `--help` 选项

**说明（Help）**

命令行（Shell）解析命令以查找 `-h` 或 `--help` 字符串；找到后会自动打印该命令的帮助信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_HELP && !CONFIG_SHELL_GETOPT && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:223`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L223)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 帮助信息（Help message）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_HELP`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_HELP)、[`CONFIG_SHELL_GETOPT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_GETOPT)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_HISTORY"></a>

## 424.96 `CONFIG_SHELL_HISTORY`

**提示（Prompt）**：命令行历史（Shell history）

**说明（Help）**

启用命令历史（Command history），可使用上、下方向键，或 `Ctrl+N`、`Ctrl+P` 组合键访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:238`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L238)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_HISTORY_BUFFER"></a>

## 424.97 `CONFIG_SHELL_HISTORY_BUFFER`

**提示（Prompt）**：历史缓冲区大小（History buffer size，字节）

**说明（Help）**

用于保存已执行命令的字节数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_HISTORY && CONFIG_SHELL
```

**默认值（Defaults）**

```text
128 if CONFIG_SHELL_MINIMAL
512
```

**定义位置（Location）**：[`subsys/shell/Kconfig:245`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L245)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 命令行历史（Shell history）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_HISTORY`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_HISTORY)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_LOCAL"></a>

## 424.98 `CONFIG_SHELL_LOCAL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示此命令行（Shell）位于本地，而非远程客户端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SHELL_REMOTE_CLI && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**定义位置（Location）**：[`subsys/shell/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_REMOTE_CLI`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE_CLI)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_SHELL_LOG_BACKEND"></a>

## 424.99 `CONFIG_SHELL_LOG_BACKEND`

**提示（Prompt）**：命令行日志后端（Shell log backend）

**说明（Help）**

启用后，后端使用命令行（Shell）输出日志。此项默认启用；禁用会关闭全部命令行后端的日志输出。若只想禁用某个后端的日志，可使用该后端的 `LOG_LEVEL` 选项，例如 `CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_NONE=y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && !CONFIG_LOG_MODE_MINIMAL && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_MPSC_PBUF
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/shell/Kconfig:288`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L288)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_MPSC_PBUF`](P197_lib_配置项参考_1.md#CONFIG_MPSC_PBUF)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_SHELL_LOG_BACKEND_CUSTOM"></a>

## 424.100 `CONFIG_SHELL_LOG_BACKEND_CUSTOM`

**提示（Prompt）**：使用自定义后端实现（Custom backend implementation）

**说明（Help）**

启用后，不包含标准的命令行日志后端（Shell log backend）实现，允许自行实现日志消息与命令行数据的复用（Multiplexing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**被选择（Selected by）**

```text
CONFIG_DEBUG_NRF_ETR_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:302`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L302)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_DEBUG_NRF_ETR_SHELL`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_SHELL)。

<!-- kconfig-navigation -->

[上一章](P423_subsys_settings_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P425_subsys_shell_配置项参考_2.md)
