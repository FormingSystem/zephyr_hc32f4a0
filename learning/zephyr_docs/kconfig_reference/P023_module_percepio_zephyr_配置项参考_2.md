---
id: learning.zephyr-docs.kconfig-reference.page-23
title: "`<module:percepio>/zephyr`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第23章\_`<module:percepio>/zephyr`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `<module:percepio>/zephyr` 的 24 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP"></a>

## 23.1 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP`

**提示（Prompt）**：用户数据报协议（UDP）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && <choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT>
```

**主动选择（Selects）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER
CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StreamPort:47`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 流端口（StreamPort）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER)、[`CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP_IP"></a>

## 23.2 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP_IP`

**提示（Prompt）**：主机 IP 地址（Host IP Address）

**说明（Help）**

设置跟踪数据（Trace Data）的目标 IP 地址。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
"192.168.0.100"
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/UDP/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP_PORT"></a>

## 23.3 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP_PORT`

**提示（Prompt）**：主机 UDP 端口（Host UDP Port）

**说明（Help）**

设置跟踪数据（Trace Data）的目标 UDP 端口。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
18419
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/UDP/Kconfig:10`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER"></a>

## 23.4 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER`

**提示（Prompt）**：内部缓冲区（Internal Buffer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE || CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM || CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_FILE || CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP || CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP || CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_STM32_USB_CDC) && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.InternalBuffer:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_FILE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_FILE)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_STM32_USB_CDC`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_STM32_USB_CDC)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ZEPHYR_SEMIHOST"></a>

## 23.5 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ZEPHYR_SEMIHOST`

**提示（Prompt）**：半主机（Semihost）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && CONFIG_SEMIHOST && <choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StreamPort:59`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 流端口（StreamPort）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_SEMIHOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEMIHOST)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT)。

<a id="CONFIG_PERCEPIO_TRC_CFG_TASK_MONITOR_MAX_TASKS"></a>

## 23.6 `CONFIG_PERCEPIO_TRC_CFG_TASK_MONITOR_MAX_TASKS`

**提示（Prompt）**：任务监测最大任务数（Task Monitor Max Tasks）

**说明（Help）**

控制任务监测器（Task Monitor）可以监测的任务数量。如果此值过小，部分任务可能无法正确注册。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_ENABLE_TASK_MONITOR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TaskMonitor:20`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 任务监测器（Task Monitor）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_ENABLE_TASK_MONITOR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_ENABLE_TASK_MONITOR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_TRAX_BLOCKING_MODE"></a>

## 23.7 `CONFIG_PERCEPIO_TRC_CFG_TRAX_BLOCKING_MODE`

**提示（Prompt）**：流阻塞模式（Stream Blocking Mode）

**说明（Help）**

此通过 Xtensa TRAX 进行流传输（Streaming）的流端口依赖 apptrace。apptrace 使用一个内部 TRAX RAM 缓冲区，由 OpenOCD 在执行期间读取。可选值为：

- `APPTRACE_TRAX_MODE_BLOCK_IF_FIFO_FULL`。
- `APPTRACE_TRAX_MODE_NO_BLOCK_SKIP`，默认值。

使用 `APPTRACE_TRAX_MODE_BLOCK_IF_FIFO_FULL` 可确保获得完整有效的跟踪，但如果流传输接口速度不够，可能引起阻塞，干扰实时行为（Real-time Behavior）。因此建议使用 `APPTRACE_TRAX_MODE_NO_BLOCK_SKIP`。此模式下，如果传输不够快，Tracealyzer 会报告事件丢失；遇到问题时，可尝试增大 `sdkconfig` 中的 apptrace 缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_TRC_CFG_TRAX_MODE_NO_BLOCK_SKIP
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_TRC_CFG_TRAX_MODE_BLOCK_IF_FIFO_FULL
CONFIG_PERCEPIO_TRC_CFG_TRAX_MODE_NO_BLOCK_SKIP
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../kernelports/ESP-IDF_FreeRTOS/streamports/ESP_IDF_APPTRACE/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_PERCEPIO_TRC_CFG_TRAX_MODE_NO_BLOCK_SKIP`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_TRAX_MODE_NO_BLOCK_SKIP)、[`CONFIG_PERCEPIO_TRC_CFG_TRAX_MODE_BLOCK_IF_FIFO_FULL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_TRAX_MODE_BLOCK_IF_FIFO_FULL)。

<a id="CONFIG_PERCEPIO_TRC_CFG_TRAX_MODE_BLOCK_IF_FIFO_FULL"></a>

## 23.8 `CONFIG_PERCEPIO_TRC_CFG_TRAX_MODE_BLOCK_IF_FIFO_FULL`

**提示（Prompt）**：FIFO 满时阻塞（Block if FIFO Full）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_TRAX_BLOCKING_MODE>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../kernelports/ESP-IDF_FreeRTOS/streamports/ESP_IDF_APPTRACE/Kconfig:24`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 流阻塞模式（Stream Blocking Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_TRAX_BLOCKING_MODE`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_TRAX_BLOCKING_MODE)。

<a id="CONFIG_PERCEPIO_TRC_CFG_TRAX_MODE_NO_BLOCK_SKIP"></a>

## 23.9 `CONFIG_PERCEPIO_TRC_CFG_TRAX_MODE_NO_BLOCK_SKIP`

**提示（Prompt）**：FIFO 满时跳过（Skip if FIFO Full）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_TRAX_BLOCKING_MODE>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../kernelports/ESP-IDF_FreeRTOS/streamports/ESP_IDF_APPTRACE/Kconfig:27`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 流阻塞模式（Stream Blocking Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_TRAX_BLOCKING_MODE`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_TRAX_BLOCKING_MODE)。

<a id="CONFIG_PERCEPIO_TRC_CFG_USE_CORTEX_M_DWT"></a>

## 23.10 `CONFIG_PERCEPIO_TRC_CFG_USE_CORTEX_M_DWT`

**提示（Prompt）**：使用 DWT 时间戳（Timestamping，仅 Arm Cortex-M）

**说明（Help）**

在 Arm Cortex-M 器件上，启用此选项可使用数据观察点与跟踪（DWT）时钟周期计数器为事件添加时间戳（Timestamp），代替通用 Zephyr 函数 `k_cycle_get_32()`。在某些开发板上，该 Zephyr 函数可能依赖 RTC 时钟；器件被暂停时，RTC 时钟通常仍继续运行，导致断点影响跟踪，而且频率往往过低，无法提供准确时间戳。因此，使用 DWT 时钟周期计数器生成时间戳更合适。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CORTEX_M_DWT && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
y if CONFIG_CORTEX_M_DWT
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/Kconfig:6`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder）

**配置项引用（Symbol References）**：[`CONFIG_CORTEX_M_DWT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_DWT)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_USE_SYSCALL_EXTENSION"></a>

## 23.11 `CONFIG_PERCEPIO_TRC_CFG_USE_SYSCALL_EXTENSION`

**提示（Prompt）**：使用系统调用扩展（Syscall Extension）

**说明（Help）**

启用后，向 Tracealyzer 提交系统调用（Syscall）时使用 ID 而非名称，从而减少每次系统调用需要传输的数据。但这也要求在 Tracealyzer 中将 `build/syscalls-v<zephyr-version>.xml` 文件加载为扩展（Extension）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/Kconfig:56`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 实时操作系统专用设置（RTOS Specific）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_USE_TRACE_ASSERT"></a>

## 23.12 `CONFIG_PERCEPIO_TRC_CFG_USE_TRACE_ASSERT`

**提示（Prompt）**：跟踪断言（Trace Asserts）

**说明（Help）**

启用或禁用调试断言（Debug Assert）。任何被触发断言的相关信息都会位于 `trcAssert.c` 中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.Debug:25`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 调试（Debug）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_ALL"></a>

## 23.13 `CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_ALL`

**提示（Prompt）**：全部传输（Transfer All）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_TRANSFER_MODE>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.InternalBuffer:24`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 内部缓冲区（Internal Buffer） → 内部缓冲区传输模式（Internal Buffer Transfer Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_TRANSFER_MODE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_TRANSFER_MODE)。

<a id="CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK"></a>

## 23.14 `CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK`

**提示（Prompt）**：分块传输（Transfer Chunks）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_TRANSFER_MODE>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.InternalBuffer:27`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 内部缓冲区（Internal Buffer） → 内部缓冲区传输模式（Internal Buffer Transfer Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_TRANSFER_MODE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_TRANSFER_MODE)。

<a id="CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_CUSTOM"></a>

## 23.15 `CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_CUSTOM`

**提示（Prompt）**：自定义分配（Custom Allocation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_RECORDER_BUFFER_ALLOCATION>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.BufferAllocation:27`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 记录器分配模式（Recorder Allocation Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_BUFFER_ALLOCATION`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_BUFFER_ALLOCATION)。

<a id="CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_DYNAMIC"></a>

## 23.16 `CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_DYNAMIC`

**提示（Prompt）**：动态分配（Dynamic Allocation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_RECORDER_BUFFER_ALLOCATION>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.BufferAllocation:24`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 记录器分配模式（Recorder Allocation Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_BUFFER_ALLOCATION`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_BUFFER_ALLOCATION)。

<a id="CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_STATIC"></a>

## 23.17 `CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_STATIC`

**提示（Prompt）**：静态分配（Static Allocation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_RECORDER_BUFFER_ALLOCATION>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.BufferAllocation:21`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 记录器分配模式（Recorder Allocation Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_BUFFER_ALLOCATION`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_BUFFER_ALLOCATION)。

<a id="CONFIG_PERCEPIO_TRC_START_MODE_MANUAL"></a>

## 23.18 `CONFIG_PERCEPIO_TRC_START_MODE_MANUAL`

**提示（Prompt）**：手动（Manual）

**说明（Help）**

可通过手动调用 `xTraceEnable(TRC_START)` 开始跟踪（Tracing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_START_MODE>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StartMode:30`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 记录器启动模式（Recorder Start Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_START_MODE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_START_MODE)。

<a id="CONFIG_PERCEPIO_TRC_START_MODE_START"></a>

## 23.19 `CONFIG_PERCEPIO_TRC_START_MODE_START`

**提示（Prompt）**：启动时开始（Start at Boot）

**说明（Help）**

内核启动时直接开始跟踪（Tracing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_START_MODE>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StartMode:11`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 记录器启动模式（Recorder Start Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_START_MODE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_START_MODE)。

<a id="CONFIG_PERCEPIO_TRC_START_MODE_START_AWAIT_HOST"></a>

## 23.20 `CONFIG_PERCEPIO_TRC_START_MODE_START_AWAIT_HOST`

**提示（Prompt）**：等待主机（Await Host）

**说明（Help）**

阻塞内核启动，直到收到启动命令（Start Command），例如来自 Tracealyzer 的“开始记录（Start Recording）”按钮。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL && <choice CONFIG_PERCEPIO_TRC_CFG_START_MODE>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StartMode:16`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 记录器启动模式（Recorder Start Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL)、[`CONFIG_PERCEPIO_TRC_CFG_START_MODE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_START_MODE)。

<a id="CONFIG_PERCEPIO_TRC_START_MODE_START_FROM_HOST"></a>

## 23.21 `CONFIG_PERCEPIO_TRC_START_MODE_START_FROM_HOST`

**提示（Prompt）**：由主机启动（From Host）

**说明（Help）**

启动时不阻塞；收到启动命令（Start Command）后开始跟踪，例如来自 Tracealyzer 的“开始记录（Start Recording）”按钮。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL && <choice CONFIG_PERCEPIO_TRC_CFG_START_MODE>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StartMode:23`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 记录器启动模式（Recorder Start Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL)、[`CONFIG_PERCEPIO_TRC_CFG_START_MODE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_START_MODE)。

<a id="CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL"></a>

## 23.22 `CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

流端口（StreamPort）可接收主机命令时，选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**被选择（Selected by）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_STM32_USB_CDC
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StreamPort:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_STM32_USB_CDC`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_STM32_USB_CDC)。

<a id="CONFIG_PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_OVERWRITE_WHEN_FULL"></a>

## 23.23 `CONFIG_PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_OVERWRITE_WHEN_FULL`

**提示（Prompt）**：满时覆盖（Overwrite When Full）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER_MODE>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/RingBuffer/Kconfig:25`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 环形缓冲区模式（Ring Buffer Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER_MODE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER_MODE)。

<a id="CONFIG_PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_STOP_WHEN_FULL"></a>

## 23.24 `CONFIG_PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_STOP_WHEN_FULL`

**提示（Prompt）**：满时停止（Stop When Full）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER_MODE>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/RingBuffer/Kconfig:28`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 环形缓冲区模式（Ring Buffer Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER_MODE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER_MODE)。

<!-- kconfig-navigation -->

[上一章](P022_module_percepio_zephyr_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P024_module_picolibc_zephyr_配置项参考.md)
