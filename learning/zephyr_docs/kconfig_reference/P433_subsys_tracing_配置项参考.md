---
id: learning.zephyr-docs.kconfig-reference.page-433
title: "`subsys/tracing`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第433章\_`subsys/tracing`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/tracing` 的 75 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PERCEPIO_TRACERECORDER"></a>

## 433.1 `CONFIG_PERCEPIO_TRACERECORDER`

**提示（Prompt）**：Percepio Tracealyzer 支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_PERCEPIO_MODULE && <choice CONFIG_TRACING_FORMAT_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_THREAD_NAME
CONFIG_INIT_STACKS
CONFIG_THREAD_MONITOR
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪格式（Tracing Format）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_PERCEPIO_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_PERCEPIO_MODULE)、[`CONFIG_TRACING_FORMAT_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_FORMAT_CHOICE)、[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)、[`CONFIG_INIT_STACKS`](P001_kernel_配置项参考_1.md#CONFIG_INIT_STACKS)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_PERCEPIO_MODULE`。

<a id="CONFIG_RAM_TRACING_BUFFER_SIZE"></a>

## 433.2 `CONFIG_RAM_TRACING_BUFFER_SIZE`

**提示（Prompt）**：RAM 跟踪缓冲区大小（Tracing buffer size）

**说明（Help）**

RAM 跟踪缓冲区（Trace buffer）的大小，超过容量的跟踪数据会被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_BACKEND_RAM && CONFIG_TRACING
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:264`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L264)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING_BACKEND_RAM`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_RAM)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_SEGGER_SYSTEMVIEW"></a>

## 433.3 `CONFIG_SEGGER_SYSTEMVIEW`

**提示（Prompt）**：SEGGER SystemView 支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TRACING_FORMAT_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_USE_SEGGER_RTT
CONFIG_THREAD_MONITOR
CONFIG_SEGGER_RTT_CUSTOM_LOCKING
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪格式（Tracing Format）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_FORMAT_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_FORMAT_CHOICE)、[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_SEGGER_RTT_CUSTOM_LOCKING`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_CUSTOM_LOCKING)。

<a id="CONFIG_SEGGER_SYSTEMVIEW_BOOT_ENABLE"></a>

## 433.4 `CONFIG_SEGGER_SYSTEMVIEW_BOOT_ENABLE`

**提示（Prompt）**：系统启动时开始记录 SystemView 事件（Event）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEGGER_SYSTEMVIEW
```

**定义位置（Location）**：[`subsys/tracing/sysview/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/sysview/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_SYSTEMVIEW`](P433_subsys_tracing_配置项参考.md#CONFIG_SEGGER_SYSTEMVIEW)。

<a id="CONFIG_SEGGER_SYSVIEW_APP_NAME"></a>

## 433.5 `CONFIG_SEGGER_SYSVIEW_APP_NAME`

**提示（Prompt）**：SystemView 中显示的应用名称（Application name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SEGGER_SYSTEMVIEW
```

**默认值（Defaults）**

```text
"ZephyrSysView"
```

**定义位置（Location）**：[`subsys/tracing/sysview/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/sysview/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_SYSTEMVIEW`](P433_subsys_tracing_配置项参考.md#CONFIG_SEGGER_SYSTEMVIEW)。

<a id="CONFIG_SEGGER_SYSVIEW_POST_MORTEM_MODE"></a>

## 433.6 `CONFIG_SEGGER_SYSVIEW_POST_MORTEM_MODE`

**提示（Prompt）**：SystemView 事后分析模式（Post-mortem mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEGGER_SYSTEMVIEW
```

**定义位置（Location）**：[`subsys/tracing/sysview/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/sysview/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_SYSTEMVIEW`](P433_subsys_tracing_配置项参考.md#CONFIG_SEGGER_SYSTEMVIEW)。

<a id="CONFIG_SEGGER_SYSVIEW_RTT_BUFFER_SIZE"></a>

## 433.7 `CONFIG_SEGGER_SYSVIEW_RTT_BUFFER_SIZE`

**提示（Prompt）**：SystemView 实时传输（RTT）缓冲区大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SEGGER_SYSTEMVIEW
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/tracing/sysview/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/sysview/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_SYSTEMVIEW`](P433_subsys_tracing_配置项参考.md#CONFIG_SEGGER_SYSTEMVIEW)。

<a id="CONFIG_SEGGER_SYSVIEW_RTT_CHANNEL"></a>

## 433.8 `CONFIG_SEGGER_SYSVIEW_RTT_CHANNEL`

**提示（Prompt）**：SystemView 使用的实时传输（RTT）通道

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SEGGER_SYSTEMVIEW
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/tracing/sysview/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/sysview/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_SYSTEMVIEW`](P433_subsys_tracing_配置项参考.md#CONFIG_SEGGER_SYSTEMVIEW)。

<a id="CONFIG_SEGGER_SYSVIEW_SECTION"></a>

## 433.9 `CONFIG_SEGGER_SYSVIEW_SECTION`

**提示（Prompt）**：选择 SystemView 数据的链接器段（Linker section）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEGGER_SYSTEMVIEW
```

**可选项（Choices）**

```text
CONFIG_SEGGER_SYSVIEW_SECTION_NONE
CONFIG_SEGGER_SYSVIEW_SECTION_DTCM
```

**定义位置（Location）**：[`subsys/tracing/sysview/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/sysview/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_SYSTEMVIEW`](P433_subsys_tracing_配置项参考.md#CONFIG_SEGGER_SYSTEMVIEW)、[`CONFIG_SEGGER_SYSVIEW_SECTION_NONE`](P433_subsys_tracing_配置项参考.md#CONFIG_SEGGER_SYSVIEW_SECTION_NONE)、[`CONFIG_SEGGER_SYSVIEW_SECTION_DTCM`](P433_subsys_tracing_配置项参考.md#CONFIG_SEGGER_SYSVIEW_SECTION_DTCM)。

<a id="CONFIG_SEGGER_SYSVIEW_SECTION_DTCM"></a>

## 433.10 `CONFIG_SEGGER_SYSVIEW_SECTION_DTCM`

**提示（Prompt）**：将 SystemView 数据放入数据紧耦合内存（DTCM）链接器段

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SEGGER_SYSVIEW_SECTION>
```

**定义位置（Location）**：[`subsys/tracing/sysview/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/sysview/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 选择 SystemView 数据的链接器段（Linker section）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_SYSVIEW_SECTION`](P433_subsys_tracing_配置项参考.md#CONFIG_SEGGER_SYSVIEW_SECTION)。

<a id="CONFIG_SEGGER_SYSVIEW_SECTION_NONE"></a>

## 433.11 `CONFIG_SEGGER_SYSVIEW_SECTION_NONE`

**提示（Prompt）**：将 SystemView 数据放入默认链接器段（Default linker section）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SEGGER_SYSVIEW_SECTION>
```

**定义位置（Location）**：[`subsys/tracing/sysview/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/sysview/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 选择 SystemView 数据的链接器段（Linker section）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_SYSVIEW_SECTION`](P433_subsys_tracing_配置项参考.md#CONFIG_SEGGER_SYSVIEW_SECTION)。

<a id="CONFIG_SYS_IDLE_HOOKS"></a>

## 433.12 `CONFIG_SYS_IDLE_HOOKS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏符号，由需要架构空闲路径调用 `sys_trace_idle()` 和 `sys_trace_idle_exit()` 通知钩子的子系统选择，例如 `TRACING` 和 `CPU_LOAD`。没有子系统选择时，架构空闲路径完全省略这些钩子调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_CPU_LOAD_BACKEND_IDLE_HOOK
CONFIG_TRACING
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_CPU_LOAD_BACKEND_IDLE_HOOK`](P197_lib_配置项参考_1.md#CONFIG_CPU_LOAD_BACKEND_IDLE_HOOK)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING"></a>

## 433.13 `CONFIG_TRACING`

**提示（Prompt）**：跟踪（Tracing）支持

**说明（Help）**

启用系统跟踪（System tracing），同时还需要启用 SEGGER SystemView 等跟踪后端（Backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_INSTRUMENT_THREAD_SWITCHING
CONFIG_SYS_IDLE_HOOKS
```

**被选择（Selected by）**

```text
CONFIG_CPU_FREQ_POLICY_PRESSURE
CONFIG_INSTRUMENTATION_MODE_CALLGRAPH
```

**弱选择（Implies）**

```text
CONFIG_THREAD_NAME
CONFIG_THREAD_STACK_INFO
CONFIG_THREAD_MONITOR
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_INSTRUMENT_THREAD_SWITCHING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENT_THREAD_SWITCHING)、[`CONFIG_SYS_IDLE_HOOKS`](P433_subsys_tracing_配置项参考.md#CONFIG_SYS_IDLE_HOOKS)、[`CONFIG_CPU_FREQ_POLICY_PRESSURE`](P335_subsys_cpu_freq_配置项参考.md#CONFIG_CPU_FREQ_POLICY_PRESSURE)、[`CONFIG_INSTRUMENTATION_MODE_CALLGRAPH`](P347_subsys_instrumentation_配置项参考.md#CONFIG_INSTRUMENTATION_MODE_CALLGRAPH)、[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_INSTRUMENT_THREAD_SWITCHING`。

<a id="CONFIG_TRACING_ASYNC"></a>

## 433.14 `CONFIG_TRACING_ASYNC`

**提示（Prompt）**：异步跟踪（Asynchronous Tracing）

**说明（Help）**

启用异步跟踪（Asynchronous tracing）。先将全部跟踪数据包放入环形缓冲区（Ring buffer）；跟踪线程得到调度后，尽可能多地输出缓冲区中的数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TRACING_METHOD_CHOICE>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪方式（Tracing Method）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_METHOD_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_METHOD_CHOICE)。

<a id="CONFIG_TRACING_BACKEND_ADSP_MEMORY_WINDOW"></a>

## 433.15 `CONFIG_TRACING_BACKEND_ADSP_MEMORY_WINDOW`

**提示（Prompt）**：RAM 内存窗口（Memory window）

**说明（Help）**

使用音频数字信号处理器（ADSP）的内存调试窗口输出跟踪数据（Tracing data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP && CONFIG_TRACING_SYNC && <choice CONFIG_TRACING_BACKEND_CHOICE>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:237`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L237)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪后端（Tracing Backend）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_TRACING_SYNC`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_SYNC)、[`CONFIG_TRACING_BACKEND_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_CHOICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_TRACING_BACKEND_CHOICE"></a>

## 433.16 `CONFIG_TRACING_BACKEND_CHOICE`

**提示（Prompt）**：跟踪后端（Tracing Backend）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
CONFIG_TRACING_BACKEND_UART
```

**可选项（Choices）**

```text
CONFIG_TRACING_BACKEND_UART
CONFIG_TRACING_BACKEND_USB
CONFIG_TRACING_BACKEND_POSIX
CONFIG_TRACING_BACKEND_RAM
CONFIG_TRACING_BACKEND_SEMIHOST
CONFIG_TRACING_BACKEND_ADSP_MEMORY_WINDOW
CONFIG_TRACING_BACKEND_ITM
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_TRACING_BACKEND_UART`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_UART)、[`CONFIG_TRACING_BACKEND_USB`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_USB)、[`CONFIG_TRACING_BACKEND_POSIX`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_POSIX)、[`CONFIG_TRACING_BACKEND_RAM`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_RAM)、[`CONFIG_TRACING_BACKEND_SEMIHOST`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_SEMIHOST)、[`CONFIG_TRACING_BACKEND_ADSP_MEMORY_WINDOW`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_ADSP_MEMORY_WINDOW)、[`CONFIG_TRACING_BACKEND_ITM`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_ITM)。

<a id="CONFIG_TRACING_BACKEND_ITM"></a>

## 433.17 `CONFIG_TRACING_BACKEND_ITM`

**提示（Prompt）**：指令跟踪宏单元（ITM）后端

**说明（Help）**

通过指令跟踪宏单元（Instrumentation Trace Macrocell，ITM）的激励端口（Stimulus port）输出跟踪数据。跟踪出口，即串行线输出（SWO）引脚或跟踪端口接口单元（TPIU）的并行跟踪，由开发板或调试探针配置，本后端不负责配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARMV7_M_ARMV8_M_MAINLINE && <choice CONFIG_TRACING_BACKEND_CHOICE>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪后端（Tracing Backend）

**配置项引用（Symbol References）**：[`CONFIG_ARMV7_M_ARMV8_M_MAINLINE`](P029_arch_arm_配置项参考_1.md#CONFIG_ARMV7_M_ARMV8_M_MAINLINE)、[`CONFIG_TRACING_BACKEND_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_CHOICE)。

<a id="CONFIG_TRACING_BACKEND_ITM_BUS_ID"></a>

## 433.18 `CONFIG_TRACING_BACKEND_ITM_BUS_ID`

**提示（Prompt）**：ITM 的高级跟踪总线（ATB）跟踪 ID

**说明（Help）**

用于在跟踪总线上标识 ITM 数据流的高级跟踪总线（ATB）跟踪 ID。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_BACKEND_ITM && CONFIG_TRACING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 127]
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:282`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L282)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING_BACKEND_ITM`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_ITM)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_BACKEND_ITM_POLL"></a>

## 433.19 `CONFIG_TRACING_BACKEND_ITM_POLL`

**提示（Prompt）**：丢弃前轮询就绪位（Ready bit）的次数

**说明（Help）**

丢弃数据包剩余内容之前，轮询激励端口（Stimulus port）就绪位的次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_TRACING_BACKEND_ITM_STALL && CONFIG_TRACING_BACKEND_ITM && CONFIG_TRACING
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:296`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L296)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING_BACKEND_ITM_STALL`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_ITM_STALL)、[`CONFIG_TRACING_BACKEND_ITM`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_ITM)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_BACKEND_ITM_PORT"></a>

## 433.20 `CONFIG_TRACING_BACKEND_ITM_PORT`

**提示（Prompt）**：跟踪数据流使用的 ITM 激励端口（Stimulus port）

**说明（Help）**

此后端写入的激励端口（Stimulus port）。应避免与其他子系统使用的端口冲突；SWO 日志后端使用端口 0。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_BACKEND_ITM && CONFIG_TRACING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 31]
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:274`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L274)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING_BACKEND_ITM`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_ITM)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_BACKEND_ITM_STALL"></a>

## 433.21 `CONFIG_TRACING_BACKEND_ITM_STALL`

**提示（Prompt）**：激励端口满时停等内核，而不是丢弃数据

**说明（Help）**

持续自旋（Spin），直到激励端口（Stimulus port）腾出空间，而不是有限次数轮询后丢弃数据包剩余部分。此方式不会丢失数据，但如果没有组件取走跟踪数据，会使处理器核心停等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_BACKEND_ITM && CONFIG_TRACING
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:289`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L289)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING_BACKEND_ITM`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_ITM)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_BACKEND_POSIX"></a>

## 433.22 `CONFIG_TRACING_BACKEND_POSIX`

**提示（Prompt）**：POSIX 原生架构后端（Native backend）

**说明（Help）**

使用 POSIX 架构将跟踪数据（Tracing data）输出到文件系统。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_SYNC && CONFIG_ARCH_POSIX && <choice CONFIG_TRACING_BACKEND_CHOICE>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪后端（Tracing Backend）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_SYNC`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_SYNC)、[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_TRACING_BACKEND_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_CHOICE)。

<a id="CONFIG_TRACING_BACKEND_RAM"></a>

## 433.23 `CONFIG_TRACING_BACKEND_RAM`

**提示（Prompt）**：RAM 后端（Backend）

**说明（Help）**

使用 RAM 缓冲区保存跟踪数据，运行时可通过调试器将其转储到文件。例如，参见 GDB 的 `dump binary memory` 文档。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TRACING_BACKEND_CHOICE>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:223`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L223)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪后端（Tracing Backend）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_BACKEND_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_CHOICE)。

<a id="CONFIG_TRACING_BACKEND_SEMIHOST"></a>

## 433.24 `CONFIG_TRACING_BACKEND_SEMIHOST`

**提示（Prompt）**：半主机后端（Semihost backend）

**说明（Help）**

使用半主机（Semihosting）输出跟踪数据，适用于在宿主机上调试，例如使用 QEMU 的场景。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEMIHOST && <choice CONFIG_TRACING_BACKEND_CHOICE>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:230`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L230)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪后端（Tracing Backend）

**配置项引用（Symbol References）**：[`CONFIG_SEMIHOST`](P032_arch_common_配置项参考.md#CONFIG_SEMIHOST)、[`CONFIG_TRACING_BACKEND_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_CHOICE)。

<a id="CONFIG_TRACING_BACKEND_UART"></a>

## 433.25 `CONFIG_TRACING_BACKEND_UART`

**提示（Prompt）**：UART 后端（backend）。

**说明（Help）**

使用 UART 输出跟踪数据（Tracing data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL && <choice CONFIG_TRACING_BACKEND_CHOICE>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪后端（Tracing Backend）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_TRACING_BACKEND_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_CHOICE)。

<a id="CONFIG_TRACING_BACKEND_USB"></a>

## 433.26 `CONFIG_TRACING_BACKEND_USB`

**提示（Prompt）**：USB 后端（USB backend）

**说明（Help）**

使用 USB 输出跟踪数据（Tracing data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT && CONFIG_TRACING_ASYNC && <choice CONFIG_TRACING_BACKEND_CHOICE>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L209)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪后端（Tracing Backend）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_TRACING_ASYNC`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_ASYNC)、[`CONFIG_TRACING_BACKEND_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_CHOICE)。

<a id="CONFIG_TRACING_BUFFER_SIZE"></a>

## 433.27 `CONFIG_TRACING_BUFFER_SIZE`

**提示（Prompt）**：跟踪缓冲区大小（Tracing buffer size）

**说明（Help）**

跟踪缓冲区（Tracing buffer）的大小。启用 `TRACING_ASYNC` 时，作为环形缓冲区保存数据包和字符串包；启用 `TRACING_SYNC` 时，用于保存格式化后的数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
2048 if CONFIG_TRACING_ASYNC
CONFIG_TRACING_PACKET_MAX_SIZE if CONFIG_TRACING_SYNC
```

**取值范围（Ranges）**

```text
[32, 65536]
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_TRACING_ASYNC`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_ASYNC)、[`CONFIG_TRACING_PACKET_MAX_SIZE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_PACKET_MAX_SIZE)、[`CONFIG_TRACING_SYNC`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_SYNC)。

<a id="CONFIG_TRACING_CMD_BUFFER_SIZE"></a>

## 433.28 `CONFIG_TRACING_CMD_BUFFER_SIZE`

**提示（Prompt）**：跟踪命令缓冲区大小（Tracing command buffer size）

**说明（Help）**

跟踪命令缓冲区（Tracing command buffer）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[32, 128]
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:314`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L314)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_CONDVAR"></a>

## 433.29 `CONFIG_TRACING_CONDVAR`

**提示（Prompt）**：跟踪条件变量（Condition Variables）

**说明（Help）**

启用条件变量（Condition variable）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:374`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L374)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_CORE"></a>

## 433.30 `CONFIG_TRACING_CORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由需要核心跟踪基础设施（Core tracing infrastructure）的格式自动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**被选择（Selected by）**

```text
CONFIG_TRACING_CTF
CONFIG_TRACING_TEST
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_TRACING_CTF`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_CTF)、[`CONFIG_TRACING_TEST`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_TEST)。

<a id="CONFIG_TRACING_CTF"></a>

## 433.31 `CONFIG_TRACING_CTF`

**提示（Prompt）**：通用跟踪格式（Common Trace Format，CTF）支持

**说明（Help）**

启用向通用跟踪格式（Common Trace Format，CTF）数据流输出跟踪数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TRACING_FORMAT_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_TRACING_CORE
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪格式（Tracing Format）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_FORMAT_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_FORMAT_CHOICE)、[`CONFIG_TRACING_CORE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_CORE)。

<a id="CONFIG_TRACING_CTF_TIMESTAMP"></a>

## 433.32 `CONFIG_TRACING_CTF_TIMESTAMP`

**提示（Prompt）**：CTF 内部时间戳（Internal timestamp）

**说明（Help）**

在内部为 CTF 事件开头添加时间戳前缀（Timestamp prefix）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_CTF && CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TIMING_FUNCTIONS
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING_CTF`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_CTF)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_TIMING_FUNCTIONS`](P432_subsys_timing_配置项参考.md#CONFIG_TIMING_FUNCTIONS)。

<a id="CONFIG_TRACING_CUSTOM"></a>

## 433.33 `CONFIG_TRACING_CUSTOM`

**提示（Prompt）**：包含自定义跟踪头文件（Custom tracing header）［实验性，Experimental］

**说明（Help）**

启用后，在 `tracing.h` 末尾包含应用提供的自定义头文件 `zephyr_custom_tracing.h`，以在宏（Macro）层面扩展 `sys_port_trace*` API。请谨慎使用，内部 TRACE API 可能在未来版本改变。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TRACING_FORMAT_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪格式（Tracing Format）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_FORMAT_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_FORMAT_CHOICE)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_TRACING_EVENT"></a>

## 433.34 `CONFIG_TRACING_EVENT`

**提示（Prompt）**：跟踪事件（Events）

**说明（Help）**

启用事件（Event）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:440`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L440)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_FIFO"></a>

## 433.35 `CONFIG_TRACING_FIFO`

**提示（Prompt）**：跟踪先进先出队列（FIFO queues）

**说明（Help）**

启用先进先出队列（FIFO queue）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:386`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L386)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_FORMAT_CHOICE"></a>

## 433.36 `CONFIG_TRACING_FORMAT_CHOICE`

**提示（Prompt）**：跟踪格式（Tracing Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
CONFIG_TRACING_NONE
```

**可选项（Choices）**

```text
CONFIG_TRACING_NONE
CONFIG_PERCEPIO_TRACERECORDER
CONFIG_SEGGER_SYSTEMVIEW
CONFIG_TRACING_CTF
CONFIG_TRACING_TEST
CONFIG_TRACING_USER
CONFIG_TRACING_CUSTOM
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_TRACING_NONE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_NONE)、[`CONFIG_PERCEPIO_TRACERECORDER`](P433_subsys_tracing_配置项参考.md#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_SEGGER_SYSTEMVIEW`](P433_subsys_tracing_配置项参考.md#CONFIG_SEGGER_SYSTEMVIEW)、[`CONFIG_TRACING_CTF`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_CTF)、[`CONFIG_TRACING_TEST`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_TEST)、[`CONFIG_TRACING_USER`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_USER)、[`CONFIG_TRACING_CUSTOM`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_CUSTOM)。

<a id="CONFIG_TRACING_FORMAT_HEADER"></a>

## 433.37 `CONFIG_TRACING_FORMAT_HEADER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

指定从 `<zephyr/tracing/tracing.h>` 通过计算得到的 `#include` 包含的跟踪格式头文件名称。这样，源码树外模块（Out-of-tree module）无需修改核心源码树即可提供自己的跟踪格式：模块的 Kconfig 设置此字符串，例如 `default "my_format.h" if TRACING_MY_FORMAT`，并将头文件目录加入包含路径（Include path）。头文件应定义它要记录的 `sys_port_trace_*` 钩子，并以 `#include <zephyr/tracing/tracing_hooks.h>` 结束，使未定义的钩子回退为空操作（No-op）。仅在未选择上述任何源码树内格式时，才使用此设置。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_GPIO"></a>

## 433.38 `CONFIG_TRACING_GPIO`

**提示（Prompt）**：跟踪通用输入输出（GPIO）

**说明（Help）**

启用通用输入输出（GPIO）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:479`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L479)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_HANDLE_HOST_CMD"></a>

## 433.39 `CONFIG_TRACING_HANDLE_HOST_CMD`

**提示（Prompt）**：宿主机命令处理（Host command handling）

**说明（Help）**

启用后，跟踪系统处理宿主机命令，动态启用或禁用跟踪，方便宿主机捕获跟踪数据流（Tracing stream）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**主动选择（Selects）**

```text
CONFIG_UART_INTERRUPT_DRIVEN if CONFIG_TRACING_BACKEND_UART
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:306`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L306)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_TRACING_BACKEND_UART`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_BACKEND_UART)。

<a id="CONFIG_TRACING_HEAP"></a>

## 433.40 `CONFIG_TRACING_HEAP`

**提示（Prompt）**：跟踪内存堆（Memory Heaps）

**说明（Help）**

启用内存堆（Memory heap）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:422`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L422)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_IDLE"></a>

## 433.41 `CONFIG_TRACING_IDLE`

**提示（Prompt）**：跟踪空闲（Idle）

**说明（Help）**

启用空闲状态（Idle state）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:485`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L485)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_INIT_LEVEL"></a>

## 433.42 `CONFIG_TRACING_INIT_LEVEL`

**提示（Prompt）**：跟踪初始化级别（Initialization level）

**说明（Help）**

跟踪后端初始化所处的 `SYS_INIT` 级别。较低级别能更早开始跟踪、捕获更多启动过程，但也意味着执行时，较晚初始化的子系统尚不可用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_CORE && CONFIG_TRACING
```

**默认值（Defaults）**

```text
CONFIG_TRACING_INIT_LEVEL_APPLICATION
```

**可选项（Choices）**

```text
CONFIG_TRACING_INIT_LEVEL_PRE_KERNEL_2
CONFIG_TRACING_INIT_LEVEL_POST_KERNEL
CONFIG_TRACING_INIT_LEVEL_APPLICATION
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING_CORE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_CORE)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_TRACING_INIT_LEVEL_APPLICATION`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_INIT_LEVEL_APPLICATION)、[`CONFIG_TRACING_INIT_LEVEL_PRE_KERNEL_2`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_INIT_LEVEL_PRE_KERNEL_2)、[`CONFIG_TRACING_INIT_LEVEL_POST_KERNEL`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_INIT_LEVEL_POST_KERNEL)。

<a id="CONFIG_TRACING_INIT_LEVEL_APPLICATION"></a>

## 433.43 `CONFIG_TRACING_INIT_LEVEL_APPLICATION`

**提示（Prompt）**：应用初始化级别（APPLICATION）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TRACING_INIT_LEVEL>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪初始化级别（Initialization level）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_INIT_LEVEL`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_INIT_LEVEL)。

<a id="CONFIG_TRACING_INIT_LEVEL_POST_KERNEL"></a>

## 433.44 `CONFIG_TRACING_INIT_LEVEL_POST_KERNEL`

**提示（Prompt）**：内核后初始化级别（POST_KERNEL）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TRACING_INIT_LEVEL>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪初始化级别（Initialization level）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_INIT_LEVEL`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_INIT_LEVEL)。

<a id="CONFIG_TRACING_INIT_LEVEL_PRE_KERNEL_2"></a>

## 433.45 `CONFIG_TRACING_INIT_LEVEL_PRE_KERNEL_2`

**提示（Prompt）**：内核前第二初始化级别（PRE_KERNEL_2）

**说明（Help）**

最早支持的初始化级别，仅适用于同步跟踪（Sync tracing）。异步跟踪（Async tracing）在 `tracing_init()` 中创建输出缓冲数据的线程（Drainer thread），需要内核已可用。系统定时器也在 `PRE_KERNEL_2` 初始化，即 `sys_clock_driver_init` 使用 `SYSTEM_CLOCK_INIT_PRIORITY`，因此 `TRACING_INIT_PRIORITY` 必须设为比它更大的值。否则，跟踪会在周期计数器（Cycle counter）可用前运行，产生无效事件时间戳。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_SYNC && <choice CONFIG_TRACING_INIT_LEVEL>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪初始化级别（Initialization level）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_SYNC`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_SYNC)、[`CONFIG_TRACING_INIT_LEVEL`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_INIT_LEVEL)。

<a id="CONFIG_TRACING_INIT_PRIORITY"></a>

## 433.46 `CONFIG_TRACING_INIT_PRIORITY`

**提示（Prompt）**：跟踪初始化优先级（Initialization priority）

**说明（Help）**

跟踪后端在 `TRACING_INIT_LEVEL` 级别内的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_CORE && CONFIG_TRACING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING_CORE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_CORE)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_ISR"></a>

## 433.47 `CONFIG_TRACING_ISR`

**提示（Prompt）**：跟踪中断服务程序（ISRs）

**说明（Help）**

启用中断服务程序（ISR）跟踪，要求后端延迟极低。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:355`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L355)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_LIFO"></a>

## 433.48 `CONFIG_TRACING_LIFO`

**提示（Prompt）**：跟踪后进先出队列（LIFO queues）

**说明（Help）**

启用后进先出队列（LIFO queue）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:392`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L392)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_MAILBOX"></a>

## 433.49 `CONFIG_TRACING_MAILBOX`

**提示（Prompt）**：跟踪邮箱（Mailboxes）

**说明（Help）**

启用邮箱（Mailbox）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:410`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L410)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_MEMORY_SLAB"></a>

## 433.50 `CONFIG_TRACING_MEMORY_SLAB`

**提示（Prompt）**：跟踪内存块池（Memory Slabs）

**说明（Help）**

启用内存块池（Memory slab）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:428`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L428)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_MESSAGE_QUEUE"></a>

## 433.51 `CONFIG_TRACING_MESSAGE_QUEUE`

**提示（Prompt）**：跟踪消息队列（Message Queues）

**说明（Help）**

启用消息队列（Message queue）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:404`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L404)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_METHOD_CHOICE"></a>

## 433.52 `CONFIG_TRACING_METHOD_CHOICE`

**提示（Prompt）**：跟踪方式（Tracing Method）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
CONFIG_TRACING_ASYNC
```

**可选项（Choices）**

```text
CONFIG_TRACING_SYNC
CONFIG_TRACING_ASYNC
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_TRACING_ASYNC`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_ASYNC)、[`CONFIG_TRACING_SYNC`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_SYNC)。

<a id="CONFIG_TRACING_MUTEX"></a>

## 433.53 `CONFIG_TRACING_MUTEX`

**提示（Prompt）**：跟踪互斥锁（Mutexes）

**说明（Help）**

启用互斥锁（Mutex）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:368`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L368)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_NETWORKING"></a>

## 433.54 `CONFIG_TRACING_NETWORKING`

**提示（Prompt）**：跟踪网络对象（Network Objects）

**说明（Help）**

启用网络对象（Network object）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y if CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:458`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L458)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_TRACING_NET_CORE"></a>

## 433.55 `CONFIG_TRACING_NET_CORE`

**提示（Prompt）**：跟踪网络核心 IP 协议栈（Network Core IP stack）

**说明（Help）**

启用网络核心 IP 协议栈跟踪，例如数据包接收和发送。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_NETWORKING && CONFIG_TRACING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_IP
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:471`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L471)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration） → 跟踪网络对象（Network Objects）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_NETWORKING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_NETWORKING)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_NET_IP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_IP`。

<a id="CONFIG_TRACING_NET_SOCKETS"></a>

## 433.56 `CONFIG_TRACING_NET_SOCKETS`

**提示（Prompt）**：跟踪网络套接字（Network Sockets）

**说明（Help）**

启用网络套接字（Network socket）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_NETWORKING && CONFIG_TRACING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_SOCKETS
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:464`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L464)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration） → 跟踪网络对象（Network Objects）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_NETWORKING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_NETWORKING)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)。

<a id="CONFIG_TRACING_NONE"></a>

## 433.57 `CONFIG_TRACING_NONE`

**提示（Prompt）**：未选择跟踪格式（No tracing format selected）

**说明（Help）**

未选择任何可用的跟踪格式（Tracing format）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TRACING_FORMAT_CHOICE>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪格式（Tracing Format）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_FORMAT_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_FORMAT_CHOICE)。

<a id="CONFIG_TRACING_OBJECT_TRACKING"></a>

## 433.58 `CONFIG_TRACING_OBJECT_TRACKING`

**提示（Prompt）**：对象跟踪（Object tracking）

**说明（Help）**

通过对象核心框架（Object core framework）跟踪内核对象，该框架按对象类型枚举对象。参见 `CONFIG_OBJ_CORE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**主动选择（Selects）**

```text
CONFIG_OBJ_CORE
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:321`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L321)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)。

<a id="CONFIG_TRACING_PACKET_MAX_SIZE"></a>

## 433.59 `CONFIG_TRACING_PACKET_MAX_SIZE`

**提示（Prompt）**：单个跟踪数据包（Tracing packet）的最大大小

**说明（Help）**

单个跟踪数据包（Tracing packet）的最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_PIPE"></a>

## 433.60 `CONFIG_TRACING_PIPE`

**提示（Prompt）**：跟踪管道（Pipes）

**说明（Help）**

启用管道（Pipe）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:416`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L416)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_PM"></a>

## 433.61 `CONFIG_TRACING_PM`

**提示（Prompt）**：跟踪电源管理（Power Management）

**说明（Help）**

启用电源管理（Power Management）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:452`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L452)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_POLLING"></a>

## 433.62 `CONFIG_TRACING_POLLING`

**提示（Prompt）**：跟踪轮询（Polling）

**说明（Help）**

启用工作轮询（Work Polling）和轮询 API（Polling API）的跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:446`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L446)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_QUEUE"></a>

## 433.63 `CONFIG_TRACING_QUEUE`

**提示（Prompt）**：跟踪队列（Queues）

**说明（Help）**

启用队列（Queue）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:380`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L380)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_SEMAPHORE"></a>

## 433.64 `CONFIG_TRACING_SEMAPHORE`

**提示（Prompt）**：跟踪信号量（Semaphores）

**说明（Help）**

启用信号量（Semaphore）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:362`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L362)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_SHELL"></a>

## 433.65 `CONFIG_TRACING_SHELL`

**提示（Prompt）**：跟踪命令行命令（Tracing shell commands）

**说明（Help）**

启用 `tracing` 命令，用于在运行时启用或禁用跟踪输出、查看丢包统计，以及刷新后端（Backend flush）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_CORE && CONFIG_SHELL && CONFIG_TRACING
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:328`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L328)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING_CORE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_CORE)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_STACK"></a>

## 433.66 `CONFIG_TRACING_STACK`

**提示（Prompt）**：跟踪内存栈（Memory Stacks）

**说明（Help）**

启用内存栈（Memory stack）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:398`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L398)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR)。

<a id="CONFIG_TRACING_SYNC"></a>

## 433.67 `CONFIG_TRACING_SYNC`

**提示（Prompt）**：同步跟踪（Synchronous Tracing）

**说明（Help）**

启用同步跟踪（Synchronous tracing），要求后端延迟极低。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TRACING_METHOD_CHOICE>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪方式（Tracing Method）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_METHOD_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_METHOD_CHOICE)。

<a id="CONFIG_TRACING_SYSCALL"></a>

## 433.68 `CONFIG_TRACING_SYSCALL`

**提示（Prompt）**：跟踪系统调用（Syscalls）

**说明（Help）**

启用系统调用（Syscall）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:337`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L337)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_TEST"></a>

## 433.69 `CONFIG_TRACING_TEST`

**提示（Prompt）**：用于测试的跟踪（Tracing for test usage）

**说明（Help）**

启用用于测试各种格式的跟踪支持，必须实现 `tracing_test.h` 中定义的跟踪钩子（Tracing hook）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TRACING_FORMAT_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_TRACING_CORE
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪格式（Tracing Format）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_FORMAT_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_FORMAT_CHOICE)、[`CONFIG_TRACING_CORE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_CORE)。

<a id="CONFIG_TRACING_THREAD"></a>

## 433.70 `CONFIG_TRACING_THREAD`

**提示（Prompt）**：跟踪线程（Threads）

**说明（Help）**

启用线程（Thread）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:343`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L343)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_THREAD_STACK_SIZE"></a>

## 433.71 `CONFIG_TRACING_THREAD_STACK_SIZE`

**提示（Prompt）**：跟踪线程栈大小（Tracing thread stack size）

**说明（Help）**

跟踪线程（Tracing thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_ASYNC && CONFIG_TRACING
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING_ASYNC`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_ASYNC)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_THREAD_WAIT_THRESHOLD"></a>

## 433.72 `CONFIG_TRACING_THREAD_WAIT_THRESHOLD`

**提示（Prompt）**：跟踪线程等待阈值（Waiting threshold）

**说明（Help）**

每次向跟踪缓冲区放入首个数据包后，跟踪线程的等待时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING_ASYNC && CONFIG_TRACING
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持

**配置项引用（Symbol References）**：[`CONFIG_TRACING_ASYNC`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_ASYNC)、[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_TIMER"></a>

## 433.73 `CONFIG_TRACING_TIMER`

**提示（Prompt）**：跟踪定时器（Timers）

**说明（Help）**

启用定时器（Timer）跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:434`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L434)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<a id="CONFIG_TRACING_USER"></a>

## 433.74 `CONFIG_TRACING_USER`

**提示（Prompt）**：使用用户定义函数进行跟踪（User-defined tracing）

**说明（Help）**

使用用户定义函数跟踪任务切换（Task switching）和中断（IRQ）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TRACING_FORMAT_CHOICE>
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪格式（Tracing Format）

**配置项引用（Symbol References）**：[`CONFIG_TRACING_FORMAT_CHOICE`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING_FORMAT_CHOICE)。

<a id="CONFIG_TRACING_WORK"></a>

## 433.75 `CONFIG_TRACING_WORK`

**提示（Prompt）**：跟踪工作项（Work）

**说明（Help）**

启用工作项（Work）和工作队列（Work queue）事件跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/tracing/Kconfig:349`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/tracing/Kconfig#L349)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 跟踪（Tracing）支持 → 跟踪配置（Tracing Configuration）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](P433_subsys_tracing_配置项参考.md#CONFIG_TRACING)。

<!-- kconfig-navigation -->

[上一章](P432_subsys_timing_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P434_subsys_usb_配置项参考_1.md)
