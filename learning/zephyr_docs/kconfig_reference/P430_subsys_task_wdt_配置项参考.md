---
id: learning.zephyr-docs.kconfig-reference.page-430
title: "`subsys/task_wdt`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第430章\_`subsys/task_wdt`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/task_wdt` 的 9 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_TASK_WDT"></a>

## 430.1 `CONFIG_TASK_WDT`

**提示（Prompt）**：任务级软件看门狗（Task-level software watchdog）

**说明（Help）**

启用任务看门狗（Task watchdog）。即使硬件只支持一个看门狗，也允许为每个线程提供独立的看门狗通道（Watchdog channel）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_REBOOT
```

**定义位置（Location）**：[`subsys/task_wdt/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/task_wdt/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)。

<a id="CONFIG_TASK_WDT_CHANNELS"></a>

## 430.2 `CONFIG_TASK_WDT_CHANNELS`

**提示（Prompt）**：任务看门狗通道（Task watchdog channel）的最大数量

**说明（Help）**

各通道的超时值保存在数组中。仅分配所需通道数量，以减少内存占用（Memory footprint）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TASK_WDT
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[2, 100]
```

**定义位置（Location）**：[`subsys/task_wdt/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/task_wdt/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 任务级软件看门狗（Task-level software watchdog）

**配置项引用（Symbol References）**：[`CONFIG_TASK_WDT`](P430_subsys_task_wdt_配置项参考.md#CONFIG_TASK_WDT)。

<a id="CONFIG_TASK_WDT_DUMMY"></a>

## 430.3 `CONFIG_TASK_WDT_DUMMY`

**提示（Prompt）**：用于测试的空实现（Dummy implementation）

**说明（Help）**

允许代码使用全部任务看门狗（Task Watchdog）API，但不执行实际操作。调试时，可用于暂时禁用任务看门狗。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TASK_WDT
```

**定义位置（Location）**：[`subsys/task_wdt/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/task_wdt/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 任务级软件看门狗（Task-level software watchdog）

**配置项引用（Symbol References）**：[`CONFIG_TASK_WDT`](P430_subsys_task_wdt_配置项参考.md#CONFIG_TASK_WDT)。

<a id="CONFIG_TASK_WDT_HW_FALLBACK"></a>

## 430.4 `CONFIG_TASK_WDT_HW_FALLBACK`

**提示（Prompt）**：使用硬件看门狗（Hardware watchdog）作为后备

**说明（Help）**

允许应用指定一个硬件看门狗（Hardware watchdog）设备，在任务看门狗（Task watchdog）自身卡住时提供额外保护。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TASK_WDT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/task_wdt/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/task_wdt/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 任务级软件看门狗（Task-level software watchdog）

**配置项引用（Symbol References）**：[`CONFIG_TASK_WDT`](P430_subsys_task_wdt_配置项参考.md#CONFIG_TASK_WDT)。

<a id="CONFIG_TASK_WDT_HW_FALLBACK_DELAY"></a>

## 430.5 `CONFIG_TASK_WDT_HW_FALLBACK_DELAY`

**提示（Prompt）**：硬件看门狗的附加延迟（Additional delay，毫秒）

**说明（Help）**

后备硬件看门狗（Hardware watchdog fallback）的超时会增加此值，为回调函数中的纠正措施提供足够时间。此延迟还可补偿硬件看门狗与内核定时器采用不同钟源时的偏差；硬件看门狗使用精度较低的低速 RC 振荡器时尤其重要。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TASK_WDT_HW_FALLBACK && CONFIG_TASK_WDT
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[1, 10000]
```

**定义位置（Location）**：[`subsys/task_wdt/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/task_wdt/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 任务级软件看门狗（Task-level software watchdog） → 使用硬件看门狗（Hardware watchdog）作为后备

**配置项引用（Symbol References）**：[`CONFIG_TASK_WDT_HW_FALLBACK`](P430_subsys_task_wdt_配置项参考.md#CONFIG_TASK_WDT_HW_FALLBACK)、[`CONFIG_TASK_WDT`](P430_subsys_task_wdt_配置项参考.md#CONFIG_TASK_WDT)。

<a id="CONFIG_TASK_WDT_HW_FALLBACK_PAUSE_HALTED_BY_DBG"></a>

## 430.6 `CONFIG_TASK_WDT_HW_FALLBACK_PAUSE_HALTED_BY_DBG`

**提示（Prompt）**：调试器暂停系统时暂停硬件看门狗（Hardware watchdog）

**说明（Help）**

配置硬件看门狗（Hardware watchdog），使系统被调试器暂停时自动暂停。注意，仅部分硬件看门狗支持此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TASK_WDT_HW_FALLBACK && CONFIG_TASK_WDT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/task_wdt/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/task_wdt/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 任务级软件看门狗（Task-level software watchdog） → 使用硬件看门狗（Hardware watchdog）作为后备

**配置项引用（Symbol References）**：[`CONFIG_TASK_WDT_HW_FALLBACK`](P430_subsys_task_wdt_配置项参考.md#CONFIG_TASK_WDT_HW_FALLBACK)、[`CONFIG_TASK_WDT`](P430_subsys_task_wdt_配置项参考.md#CONFIG_TASK_WDT)。

<a id="CONFIG_TASK_WDT_HW_FALLBACK_PAUSE_IN_SLEEP"></a>

## 430.7 `CONFIG_TASK_WDT_HW_FALLBACK_PAUSE_IN_SLEEP`

**提示（Prompt）**：系统睡眠时暂停硬件看门狗（Hardware watchdog）

**说明（Help）**

配置硬件看门狗（Hardware watchdog），使系统进入睡眠电源状态时自动暂停，系统恢复时自动恢复。注意，仅部分硬件看门狗支持此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TASK_WDT_HW_FALLBACK && CONFIG_TASK_WDT
```

**定义位置（Location）**：[`subsys/task_wdt/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/task_wdt/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 任务级软件看门狗（Task-level software watchdog） → 使用硬件看门狗（Hardware watchdog）作为后备

**配置项引用（Symbol References）**：[`CONFIG_TASK_WDT_HW_FALLBACK`](P430_subsys_task_wdt_配置项参考.md#CONFIG_TASK_WDT_HW_FALLBACK)、[`CONFIG_TASK_WDT`](P430_subsys_task_wdt_配置项参考.md#CONFIG_TASK_WDT)。

<a id="CONFIG_TASK_WDT_MIN_TIMEOUT"></a>

## 430.8 `CONFIG_TASK_WDT_MIN_TIMEOUT`

**提示（Prompt）**：任务看门狗的最小超时（Minimum timeout，毫秒）

**说明（Help）**

任务看门狗（Task watchdog）以不断重新启动的 `k_timer` 作为后端。本值指定应用中所有任务看门狗的最小超时，单位为毫秒。如果配置了后备硬件看门狗，其超时设为此值加 `TASK_WDT_HW_FALLBACK_DELAY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TASK_WDT_HW_FALLBACK && CONFIG_TASK_WDT
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[1, 10000]
```

**定义位置（Location）**：[`subsys/task_wdt/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/task_wdt/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 任务级软件看门狗（Task-level software watchdog） → 使用硬件看门狗（Hardware watchdog）作为后备

**配置项引用（Symbol References）**：[`CONFIG_TASK_WDT_HW_FALLBACK`](P430_subsys_task_wdt_配置项参考.md#CONFIG_TASK_WDT_HW_FALLBACK)、[`CONFIG_TASK_WDT`](P430_subsys_task_wdt_配置项参考.md#CONFIG_TASK_WDT)。

<a id="CONFIG_TASK_WDT_SHELL"></a>

## 430.9 `CONFIG_TASK_WDT_SHELL`

**提示（Prompt）**：任务看门狗命令行工具（Task watchdog shell utilities）

**说明（Help）**

启用提供任务看门狗（Task watchdog）命令的命令行模块（Shell module）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_TASK_WDT
```

**定义位置（Location）**：[`subsys/task_wdt/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/task_wdt/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 任务级软件看门狗（Task-level software watchdog）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_TASK_WDT`](P430_subsys_task_wdt_配置项参考.md#CONFIG_TASK_WDT)。

<!-- kconfig-navigation -->

[上一章](P429_subsys_storage_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P431_subsys_testsuite_配置项参考.md)
