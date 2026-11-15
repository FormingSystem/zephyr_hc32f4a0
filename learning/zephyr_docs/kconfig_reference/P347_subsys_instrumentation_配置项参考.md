---
id: learning.zephyr-docs.kconfig-reference.page-347
title: "`subsys/instrumentation`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第347章\_`subsys/instrumentation`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/instrumentation` 的 13 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_INSTRUMENTATION"></a>

## 347.1 `CONFIG_INSTRUMENTATION`

**提示（Prompt）**：编译器插桩支持（Compiler Instrumentation Support）

**说明（Help）**

启用由编译器管理的运行时系统插桩（runtime system instrumentation）。要求编译器支持函数插桩，并提供后端（backend）以捕获和处理来自目标的插桩事件，例如串口。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_REBOOT
CONFIG_UART_CONSOLE
CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)、[`CONFIG_UART_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_UART_CONSOLE)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER"></a>

## 347.2 `CONFIG_INSTRUMENTATION_DYNAMIC_TRIGGER`

**提示（Prompt）**：动态配置触发／停止函数（trigger/stopper functions）

**说明（Help）**

允许运行时配置触发／停止函数（trigger/stopper functions）。需要在设备树（device tree）中配置 `instrumentation_triggers` 保留内存区域（retained memory region）。启用后，可通过 `zaru` 命令行工具（CLI）在运行时更改这些函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_RETAINED_RAM_ENABLED && CONFIG_INSTRUMENTATION
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RETAINED_MEM
CONFIG_RETAINED_MEM_ZEPHYR_RAM
CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE
CONFIG_RETENTION
CONFIG_RETENTION_MUTEX_FORCE_DISABLE
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 编译器插桩支持（Compiler Instrumentation Support）

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION)、[`CONFIG_RETAINED_MEM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM)、[`CONFIG_RETAINED_MEM_ZEPHYR_RAM`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM_ZEPHYR_RAM)、[`CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE`](P146_drivers_retained_mem_配置项参考.md#CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE)、[`CONFIG_RETENTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RETENTION)、[`CONFIG_RETENTION_MUTEX_FORCE_DISABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RETENTION_MUTEX_FORCE_DISABLE)。

<a id="CONFIG_INSTRUMENTATION_EXCLUDE_FILE_LIST"></a>

## 347.3 `CONFIG_INSTRUMENTATION_EXCLUDE_FILE_LIST`

**提示（Prompt）**：排除文件列表（Exclude file list）

**说明（Help）**

设置不参与插桩（instrumentation）的文件列表，采用子串匹配：列表条目若是文件名的子串，即视为匹配。文件以逗号分隔，例如 `file0, file1, ...`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
(CONFIG_INSTRUMENTATION_MODE_CALLGRAPH || CONFIG_INSTRUMENTATION_MODE_STATISTICAL) && CONFIG_INSTRUMENTATION
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 编译器插桩支持（Compiler Instrumentation Support）

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION_MODE_CALLGRAPH`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_MODE_CALLGRAPH)、[`CONFIG_INSTRUMENTATION_MODE_STATISTICAL`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_MODE_STATISTICAL)、[`CONFIG_INSTRUMENTATION`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION)。

<a id="CONFIG_INSTRUMENTATION_EXCLUDE_FUNCTION_LIST"></a>

## 347.4 `CONFIG_INSTRUMENTATION_EXCLUDE_FUNCTION_LIST`

**提示（Prompt）**：排除函数列表（Exclude function list）

**说明（Help）**

设置不参与插桩（instrumentation）的函数名列表，匹配对象是用户可见的函数名。采用子串匹配：列表中的函数名若是某函数名的子串，即视为匹配。函数名以逗号分隔，例如 `sym0, sym1, ...`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
(CONFIG_INSTRUMENTATION_MODE_CALLGRAPH || CONFIG_INSTRUMENTATION_MODE_STATISTICAL) && CONFIG_INSTRUMENTATION
```

**默认值（Defaults）**

```text
"arch_timing_counter_get,arch_irq_lock,arch_irq_unlock,		k_cycle_get_64,sys_clock_cycle_get_64,elapsed"
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 编译器插桩支持（Compiler Instrumentation Support）

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION_MODE_CALLGRAPH`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_MODE_CALLGRAPH)、[`CONFIG_INSTRUMENTATION_MODE_STATISTICAL`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_MODE_STATISTICAL)、[`CONFIG_INSTRUMENTATION`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION)。

<a id="CONFIG_INSTRUMENTATION_MODE_CALLGRAPH"></a>

## 347.5 `CONFIG_INSTRUMENTATION_MODE_CALLGRAPH`

**提示（Prompt）**：调用图模式（Call graph mode，Tracing 跟踪）

**说明（Help）**

在跟踪缓冲区（trace buffer）容量限制范围内，支持重建函数调用图（function call graphs），并观察线程上下文切换（context switches）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INSTRUMENTATION
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_THREAD_NAME
CONFIG_TRACING
CONFIG_TIMING_FUNCTIONS
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 编译器插桩支持（Compiler Instrumentation Support）

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION)、[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_TIMING_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TIMING_FUNCTIONS)。

<a id="CONFIG_INSTRUMENTATION_MODE_CALLGRAPH_BUFFER_OVERWRITE"></a>

## 347.6 `CONFIG_INSTRUMENTATION_MODE_CALLGRAPH_BUFFER_OVERWRITE`

**提示（Prompt）**：跟踪缓冲区覆盖模式（overwriting mode）

**说明（Help）**

设为覆盖模式时，跟踪缓冲区作为环形缓冲区（ring buffer）工作：缓冲区满后，新记录覆盖旧记录。这种模式可记录最近的跟踪事件，但会丢失旧事件。未选择本模式时，缓冲区一满就停止跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INSTRUMENTATION_MODE_CALLGRAPH && <choice>
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 编译器插桩支持（Compiler Instrumentation Support） → 选择缓冲区满时的操作

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION_MODE_CALLGRAPH`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_MODE_CALLGRAPH)。

<a id="CONFIG_INSTRUMENTATION_MODE_CALLGRAPH_DUMP_ON_FULL"></a>

## 347.7 `CONFIG_INSTRUMENTATION_MODE_CALLGRAPH_DUMP_ON_FULL`

**提示（Prompt）**：缓冲区满时转储事件（Dump events）

**说明（Help）**

缓冲区满时，通过 UART 转储其内容并清空缓冲区，而不是禁用插桩（instrumentation），从而能够持续采集事件。当前在事件转储期间，`zaru` 脚本可能无法正常工作，因此建议在应用结束后使用它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INSTRUMENTATION_MODE_CALLGRAPH && <choice>
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 编译器插桩支持（Compiler Instrumentation Support） → 选择缓冲区满时的操作

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION_MODE_CALLGRAPH`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_MODE_CALLGRAPH)。

<a id="CONFIG_INSTRUMENTATION_MODE_CALLGRAPH_TRACE_BUFFER_SIZE"></a>

## 347.8 `CONFIG_INSTRUMENTATION_MODE_CALLGRAPH_TRACE_BUFFER_SIZE`

**提示（Prompt）**：跟踪缓冲区大小（字节，trace buffer）

**说明（Help）**

跟踪缓冲区大小。此缓冲区用于暂存跟踪事件（tracing events），支持两种模式：普通缓冲区，或环形缓冲区（ring buffer，即覆盖模式）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INSTRUMENTATION_MODE_CALLGRAPH && CONFIG_INSTRUMENTATION
```

**默认值（Defaults）**

```text
12000
```

**取值范围（Ranges）**

```text
[20, 4294967296]
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 编译器插桩支持（Compiler Instrumentation Support） → 调用图模式（Call graph mode，Tracing 跟踪）

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION_MODE_CALLGRAPH`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_MODE_CALLGRAPH)、[`CONFIG_INSTRUMENTATION`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION)。

<a id="CONFIG_INSTRUMENTATION_MODE_STATISTICAL"></a>

## 347.9 `CONFIG_INSTRUMENTATION_MODE_STATISTICAL`

**提示（Prompt）**：统计模式（Statistical mode，Profiling 性能分析）

**说明（Help）**

启用运行时系统的统计性能分析（statistical profiling），跟踪总执行时间，可跟踪的函数数量为 `INSTRUMENTATION_MODE_STATISTICAL_MAX_NUM_FUNC`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INSTRUMENTATION
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TIMING_FUNCTIONS
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 编译器插桩支持（Compiler Instrumentation Support）

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION)、[`CONFIG_TIMING_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TIMING_FUNCTIONS)。

<a id="CONFIG_INSTRUMENTATION_MODE_STATISTICAL_MAX_CALL_DEPTH"></a>

## 347.10 `CONFIG_INSTRUMENTATION_MODE_STATISTICAL_MAX_CALL_DEPTH`

**提示（Prompt）**：最大调用深度（Maximum call depth）

**说明（Help）**

同一函数可递归调用（recursively called）的最大次数；超过后不再收集性能数据，即时间差（delta time）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INSTRUMENTATION_MODE_STATISTICAL && CONFIG_INSTRUMENTATION
```

**默认值（Defaults）**

```text
65535
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 编译器插桩支持（Compiler Instrumentation Support） → 统计模式（Statistical mode，Profiling 性能分析）

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION_MODE_STATISTICAL`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_MODE_STATISTICAL)、[`CONFIG_INSTRUMENTATION`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION)。

<a id="CONFIG_INSTRUMENTATION_MODE_STATISTICAL_MAX_NUM_FUNC"></a>

## 347.11 `CONFIG_INSTRUMENTATION_MODE_STATISTICAL_MAX_NUM_FUNC`

**提示（Prompt）**：收集统计数据的函数数量上限

**说明（Help）**

设置需要收集统计数据的函数数量上限。在触发点（trigger）与停止点（stopper）界定的插桩区域内，收集每个被调用函数的总执行时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INSTRUMENTATION_MODE_STATISTICAL && CONFIG_INSTRUMENTATION
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[1, 4096]
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 编译器插桩支持（Compiler Instrumentation Support） → 统计模式（Statistical mode，Profiling 性能分析）

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION_MODE_STATISTICAL`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_MODE_STATISTICAL)、[`CONFIG_INSTRUMENTATION`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION)。

<a id="CONFIG_INSTRUMENTATION_STOPPER_FUNCTION"></a>

## 347.12 `CONFIG_INSTRUMENTATION_STOPPER_FUNCTION`

**提示（Prompt）**：用于关闭插桩的默认停止函数（stopper function）

**说明（Help）**

设置停止函数（stopper function）。只有该函数返回时，才关闭插桩，包括跟踪（tracing）和性能分析（profiling）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_INSTRUMENTATION
```

**默认值（Defaults）**

```text
"main"
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 编译器插桩支持（Compiler Instrumentation Support）

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION)。

<a id="CONFIG_INSTRUMENTATION_TRIGGER_FUNCTION"></a>

## 347.13 `CONFIG_INSTRUMENTATION_TRIGGER_FUNCTION`

**提示（Prompt）**：用于开启插桩的默认触发函数（trigger function）

**说明（Help）**

设置触发函数（trigger function）。只有调用该函数时，才开启插桩，包括跟踪（tracing）和性能分析（profiling）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_INSTRUMENTATION
```

**默认值（Defaults）**

```text
"main"
```

**定义位置（Location）**：[`subsys/instrumentation/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/instrumentation/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 编译器插桩支持（Compiler Instrumentation Support）

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENTATION`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION)。

<!-- kconfig-navigation -->

[上一章](P346_subsys_input_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P348_subsys_ipc_配置项参考.md)
