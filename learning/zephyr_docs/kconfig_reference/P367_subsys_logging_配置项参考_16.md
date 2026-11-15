---
id: learning.zephyr-docs.kconfig-reference.page-367
title: "`subsys/logging`配置项参考（16/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第367章\_`subsys/logging`配置项参考（16/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_ERR"></a>

## 367.1 `CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 本地域动态电压频率调整库（Local domain DVFS library） → 本地域动态电压频率调整库（Local domain DVFS library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_INF"></a>

## 367.2 `CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 本地域动态电压频率调整库（Local domain DVFS library） → 本地域动态电压频率调整库（Local domain DVFS library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_OFF"></a>

## 367.3 `CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 本地域动态电压频率调整库（Local domain DVFS library） → 本地域动态电压频率调整库（Local domain DVFS library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_WRN"></a>

## 367.4 `CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hal_nordic（模块路径 `modules/hal/nordic`，相对于 west 工作区顶层目录） → nRF 服务（Services） → nRF 服务支持（Services Support） → 本地域动态电压频率调整库（Local domain DVFS library） → 本地域动态电压频率调整库（Local domain DVFS library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE`](P366_subsys_logging_配置项参考_15.md#CONFIG_LOCAL_DOMAIN_DVFS_LIB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LOG"></a>

## 367.5 `CONFIG_LOG`

**提示（Prompt）**：日志（Logging）。

**说明（Help）**

日志器（logger）的全局开关。关闭后，日志调用不会编译进程序。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_PRINTK if CONFIG_USERSPACE
```

**被选择（Selected by）**

```text
CONFIG_BT_STM32_IPM_FW_INFO_CHECK
CONFIG_INTC_ESP32_DECISIONS_LOG
CONFIG_NET_BUF_LOG
CONFIG_NET_BUF_SIMPLE_LOG
CONFIG_BT_DEBUG_MONITOR_UART
CONFIG_BT_DEBUG_MONITOR_RTT
CONFIG_THREAD_ANALYZER_USE_LOG
CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING
CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP
CONFIG_NET_LOG
CONFIG_TEST_LOGGING_DEFAULTS
```

**定义位置（Location）**：[`subsys/logging/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_PRINTK`](P338_subsys_debug_配置项参考.md#CONFIG_PRINTK)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_BT_STM32_IPM_FW_INFO_CHECK`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32_IPM_FW_INFO_CHECK)、[`CONFIG_INTC_ESP32_DECISIONS_LOG`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_INTC_ESP32_DECISIONS_LOG)、[`CONFIG_NET_BUF_LOG`](P198_lib_配置项参考_2.md#CONFIG_NET_BUF_LOG)、[`CONFIG_NET_BUF_SIMPLE_LOG`](P198_lib_配置项参考_2.md#CONFIG_NET_BUF_SIMPLE_LOG)、[`CONFIG_BT_DEBUG_MONITOR_UART`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_MONITOR_UART)、[`CONFIG_BT_DEBUG_MONITOR_RTT`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_DEBUG_MONITOR_RTT)、[`CONFIG_THREAD_ANALYZER_USE_LOG`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER_USE_LOG)、[`CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING)、[`CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP)、[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_TEST_LOGGING_DEFAULTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_LOGGING_DEFAULTS)。

<a id="CONFIG_LOG_ALWAYS_RUNTIME"></a>

## 367.6 `CONFIG_LOG_ALWAYS_RUNTIME`

**提示（Prompt）**：始终在运行时创建消息（runtime message creation，v2）

**说明（Help）**

启用后，始终在运行时创建日志消息。静态创建（static creation）依赖编译器依据编译时已知信息进行优化、移除代码。禁用优化时必须采用纯运行时方式，因为某些编译器在 `arm_cortex_m` 和 x86 上曾为无效代码（dead code）使用不合理的大量栈空间。

立即模式（immediate mode）同样要求采用运行时方式，因为它比静态创建消息占用更少的栈，而该模式对速度的优先级较低。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**默认值（Defaults）**

```text
y if CONFIG_NO_OPTIMIZATIONS
y if CONFIG_LOG_MODE_IMMEDIATE
y if "zephyr" = "xcc"
```

**被选择（Selected by）**

```text
CONFIG_LOG_USE_TAGGED_ARGUMENTS
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NO_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NO_OPTIMIZATIONS)、[`CONFIG_LOG_MODE_IMMEDIATE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_IMMEDIATE)、[`CONFIG_LOG_USE_TAGGED_ARGUMENTS`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_USE_TAGGED_ARGUMENTS)。

<a id="CONFIG_LOG_BACKEND_ADSP"></a>

## 367.7 `CONFIG_LOG_BACKEND_ADSP`

**提示（Prompt）**：Intel ADSP 缓冲区后端（buffer backend）

**说明（Help）**

为 Intel ADSP 音频处理器系列的主机跟踪协议（host trace protocol）启用日志后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.adsp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.adsp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_LOG_BACKEND_ADSP_MTRACE"></a>

## 367.8 `CONFIG_LOG_BACKEND_ADSP_MTRACE`

**提示（Prompt）**：Intel ADSP mtrace 后端

**说明（Help）**

提供日志后端，按照 SOF Linux 驱动的 mtrace 缓冲区布局向 SRAM 窗口写入数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_INTEL_ADSP && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.adsp_mtrace:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.adsp_mtrace#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INTEL_ADSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ADSP)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ADSP`。

<a id="CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT"></a>

## 367.9 `CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_ADSP_MTRACE && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_TEXT
CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_SYST
CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Intel ADSP mtrace 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_ADSP_MTRACE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_SYST`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_CUSTOM`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_CUSTOM"></a>

## 367.10 `CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Intel ADSP mtrace 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY"></a>

## 367.11 `CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_DICTIONARY_SUPPORT
```

**弱选择（Implies）**

```text
CONFIG_LOG_FMT_SECTION
CONFIG_LOG_FMT_SECTION_STRIP if !CONFIG_LOG_ALWAYS_RUNTIME
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Intel ADSP mtrace 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_SYST"></a>

## 367.12 `CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Intel ADSP mtrace 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_TEXT"></a>

## 367.13 `CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Intel ADSP mtrace 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_ADSP_OUTPUT"></a>

## 367.14 `CONFIG_LOG_BACKEND_ADSP_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_ADSP && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_ADSP_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_ADSP_OUTPUT_TEXT
CONFIG_LOG_BACKEND_ADSP_OUTPUT_SYST
CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_ADSP_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Intel ADSP 缓冲区后端（buffer backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_ADSP`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_ADSP_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_ADSP_OUTPUT_SYST`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_ADSP_OUTPUT_CUSTOM`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_ADSP_OUTPUT_CUSTOM"></a>

## 367.15 `CONFIG_LOG_BACKEND_ADSP_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_ADSP_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Intel ADSP 缓冲区后端（buffer backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_ADSP_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY"></a>

## 367.16 `CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_ADSP_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_DICTIONARY_SUPPORT
```

**弱选择（Implies）**

```text
CONFIG_LOG_FMT_SECTION
CONFIG_LOG_FMT_SECTION_STRIP if !CONFIG_LOG_ALWAYS_RUNTIME
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Intel ADSP 缓冲区后端（buffer backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_ADSP_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_ADSP_OUTPUT_SYST"></a>

## 367.17 `CONFIG_LOG_BACKEND_ADSP_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_ADSP_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Intel ADSP 缓冲区后端（buffer backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_ADSP_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_ADSP_OUTPUT_TEXT"></a>

## 367.18 `CONFIG_LOG_BACKEND_ADSP_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_ADSP_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Intel ADSP 缓冲区后端（buffer backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_ADSP_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_BLE"></a>

## 367.19 `CONFIG_LOG_BACKEND_BLE`

**提示（Prompt）**：低功耗蓝牙后端（Bluetooth Low Energy，LE）【实验性 EXPERIMENTAL】

**说明（Help）**

通过低功耗蓝牙通知（Bluetooth LE Notifications）发送日志消息的后端。其特征（characteristic）及所属服务兼容 nRF Connect SDK 中的 Nordic UART 服务（NUS），因此可将此 BLE 日志器直接用于兼容应用，例如 nRF UART 2.0 或 nRF Toolbox。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT && CONFIG_LOG_PROCESS_THREAD_STACK_SIZE >= 2048 && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.ble:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.ble#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_LOG_PROCESS_THREAD_STACK_SIZE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_PROCESS_THREAD_STACK_SIZE)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_LOG_BACKEND_BLE_OUTPUT"></a>

## 367.20 `CONFIG_LOG_BACKEND_BLE_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_BLE && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_BLE_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_BLE_OUTPUT_TEXT
CONFIG_LOG_BACKEND_BLE_OUTPUT_SYST
CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_BLE_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 低功耗蓝牙后端（Bluetooth Low Energy，LE）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_BLE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_BLE_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_BLE_OUTPUT_SYST`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_BLE_OUTPUT_CUSTOM`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_BLE_OUTPUT_CUSTOM"></a>

## 367.21 `CONFIG_LOG_BACKEND_BLE_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_BLE_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 低功耗蓝牙后端（Bluetooth Low Energy，LE）【实验性 EXPERIMENTAL】 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_BLE_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY"></a>

## 367.22 `CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_BLE_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_DICTIONARY_SUPPORT
```

**弱选择（Implies）**

```text
CONFIG_LOG_FMT_SECTION
CONFIG_LOG_FMT_SECTION_STRIP if !CONFIG_LOG_ALWAYS_RUNTIME
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 低功耗蓝牙后端（Bluetooth Low Energy，LE）【实验性 EXPERIMENTAL】 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_BLE_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_BLE_OUTPUT_SYST"></a>

## 367.23 `CONFIG_LOG_BACKEND_BLE_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_BLE_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 低功耗蓝牙后端（Bluetooth Low Energy，LE）【实验性 EXPERIMENTAL】 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_BLE_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_BLE_OUTPUT_TEXT"></a>

## 367.24 `CONFIG_LOG_BACKEND_BLE_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_BLE_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 低功耗蓝牙后端（Bluetooth Low Energy，LE）【实验性 EXPERIMENTAL】 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_BLE_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_CRLF_LFONLY"></a>

## 367.25 `CONFIG_LOG_BACKEND_CRLF_LFONLY`

**提示（Prompt）**：强制日志器仅用一个 LF 换行符换行

**说明（Help）**

启用后，所选后端打印日志时仅用一个换行符（LF）换行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L247)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_CRLF_NONE"></a>

## 367.26 `CONFIG_LOG_BACKEND_CRLF_NONE`

**提示（Prompt）**：禁止日志器添加 CR 和 LF

**说明（Help）**

启用后，所选后端打印日志时不添加回车符（CR）和换行符（LF）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:242`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L242)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_EFI_CONSOLE"></a>

## 367.27 `CONFIG_LOG_BACKEND_EFI_CONSOLE`

**提示（Prompt）**：EFI_CONSOLE 后端

**说明（Help）**

启用后，后端使用 EFI 控制台（EFI CONSOLE）输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_EFI_CONSOLE && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if !CONFIG_UART_CONSOLE
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.efi_console:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.efi_console#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_X86_EFI_CONSOLE`](P039_arch_x86_配置项参考.md#CONFIG_X86_EFI_CONSOLE)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_UART_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_UART_CONSOLE)。

<a id="CONFIG_LOG_BACKEND_EFI_CON_OUTPUT"></a>

## 367.28 `CONFIG_LOG_BACKEND_EFI_CON_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_EFI_CONSOLE && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_TEXT
CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_SYST
CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → EFI_CONSOLE 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_EFI_CONSOLE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CONSOLE)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_SYST`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_CUSTOM`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_CUSTOM"></a>

## 367.29 `CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_EFI_CON_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → EFI_CONSOLE 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_EFI_CON_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CON_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY"></a>

## 367.30 `CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_EFI_CON_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_DICTIONARY_SUPPORT
```

**弱选择（Implies）**

```text
CONFIG_LOG_FMT_SECTION
CONFIG_LOG_FMT_SECTION_STRIP if !CONFIG_LOG_ALWAYS_RUNTIME
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → EFI_CONSOLE 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_EFI_CON_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CON_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_SYST"></a>

## 367.31 `CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_EFI_CON_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → EFI_CONSOLE 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_EFI_CON_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CON_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_TEXT"></a>

## 367.32 `CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_EFI_CON_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → EFI_CONSOLE 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_EFI_CON_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CON_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP"></a>

## 367.33 `CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP`

**提示（Prompt）**：后端时间戳格式化（Timestamp formatting）

**说明（Help）**

启用后，对时间戳（timestamp）进行格式化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if CONFIG_LOG_BACKEND_SHOW_TIMESTAMP
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L197)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_SHOW_TIMESTAMP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SHOW_TIMESTAMP)。

<a id="CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE"></a>

## 367.34 `CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE`

**提示（Prompt）**：时间戳格式模式（Timestamp format mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_OUTPUT_FORMAT_DATE_TIMESTAMP if CONFIG_LOG_TIMESTAMP_USE_REALTIME && CONFIG_POSIX_C_LANG_SUPPORT_R
CONFIG_LOG_OUTPUT_FORMAT_TIME_TIMESTAMP
```

**可选项（Choices）**

```text
CONFIG_LOG_OUTPUT_FORMAT_TIME_TIMESTAMP
CONFIG_LOG_OUTPUT_FORMAT_DATE_TIMESTAMP
CONFIG_LOG_OUTPUT_FORMAT_ISO8601_TIMESTAMP
CONFIG_LOG_OUTPUT_FORMAT_LINUX_TIMESTAMP
CONFIG_LOG_OUTPUT_FORMAT_CUSTOM_TIMESTAMP
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_OUTPUT_FORMAT_DATE_TIMESTAMP`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT_FORMAT_DATE_TIMESTAMP)、[`CONFIG_LOG_TIMESTAMP_USE_REALTIME`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_TIMESTAMP_USE_REALTIME)、[`CONFIG_POSIX_C_LANG_SUPPORT_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_C_LANG_SUPPORT_R)、[`CONFIG_LOG_OUTPUT_FORMAT_TIME_TIMESTAMP`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT_FORMAT_TIME_TIMESTAMP)、[`CONFIG_LOG_OUTPUT_FORMAT_ISO8601_TIMESTAMP`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT_FORMAT_ISO8601_TIMESTAMP)、[`CONFIG_LOG_OUTPUT_FORMAT_LINUX_TIMESTAMP`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT_FORMAT_LINUX_TIMESTAMP)、[`CONFIG_LOG_OUTPUT_FORMAT_CUSTOM_TIMESTAMP`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT_FORMAT_CUSTOM_TIMESTAMP)。

<a id="CONFIG_LOG_BACKEND_FS"></a>

## 367.35 `CONFIG_LOG_BACKEND_FS`

**提示（Prompt）**：文件系统后端（File system backend）

**说明（Help）**

启用后，后端使用配置的文件系统输出日志。日志功能要求文件系统已经挂载，因此必须配置自动挂载（auto-mount），或由应用手动挂载。文件系统尚未挂载期间，日志消息都会被丢弃。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.fs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.fs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP)。

<a id="CONFIG_LOG_BACKEND_FS_APPEND_TO_NEWEST_FILE"></a>

## 367.36 `CONFIG_LOG_BACKEND_FS_APPEND_TO_NEWEST_FILE`

**提示（Prompt）**：追加到最新日志文件（Append）

**说明（Help）**

启用后，只要最新日志文件仍有剩余空间，后端就向其追加内容。禁用时，后端每次启动都创建新日志文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_FS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.fs:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.fs#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 文件系统后端（File system backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FS`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_FS_AUTOSTART"></a>

## 367.37 `CONFIG_LOG_BACKEND_FS_AUTOSTART`

**提示（Prompt）**：自动启动文件系统（fs）后端

**说明（Help）**

启用后，在应用启动时自动启动文件系统后端（file system backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_FS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.fs:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.fs#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 文件系统后端（File system backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FS`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_FS_DIR"></a>

## 367.38 `CONFIG_LOG_BACKEND_FS_DIR`

**提示（Prompt）**：日志目录（Log directory）

**说明（Help）**

日志文件将写入的目录。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_FS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
"/lfs1"
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.fs:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.fs#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 文件系统后端（File system backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FS`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_FS_FILES_LIMIT"></a>

## 367.39 `CONFIG_LOG_BACKEND_FS_FILES_LIMIT`

**提示（Prompt）**：日志文件数量上限（Max number of files）

**说明（Help）**

保存日志的文件数量上限，同时还受文件系统分区大小限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_FS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.fs:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.fs#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 文件系统后端（File system backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FS`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_FS_FILE_PREFIX"></a>

## 367.40 `CONFIG_LOG_BACKEND_FS_FILE_PREFIX`

**提示（Prompt）**：日志文件名前缀（Log file name prefix）

**说明（Help）**

由用户定义、用于文件系统中日志文件的名称前缀，前缀后追加日志文件编号。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_FS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
"log."
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.fs:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.fs#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 文件系统后端（File system backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FS`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_FS_FILE_SIZE"></a>

## 367.41 `CONFIG_LOG_BACKEND_FS_FILE_SIZE`

**提示（Prompt）**：用户定义的日志文件大小（log file size）

**说明（Help）**

日志文件最大大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_FS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
4096
```

**取值范围（Ranges）**

```text
[128, 1073741824]
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.fs:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.fs#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 文件系统后端（File system backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FS`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_FS_OUTPUT"></a>

## 367.42 `CONFIG_LOG_BACKEND_FS_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_FS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_FS_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_FS_OUTPUT_TEXT
CONFIG_LOG_BACKEND_FS_OUTPUT_SYST
CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_FS_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 文件系统后端（File system backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FS`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_FS_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_FS_OUTPUT_SYST`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_FS_OUTPUT_CUSTOM`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_FS_OUTPUT_CUSTOM"></a>

## 367.43 `CONFIG_LOG_BACKEND_FS_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_FS_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 文件系统后端（File system backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FS_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY"></a>

## 367.44 `CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_FS_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_DICTIONARY_SUPPORT
```

**弱选择（Implies）**

```text
CONFIG_LOG_FMT_SECTION
CONFIG_LOG_FMT_SECTION_STRIP if !CONFIG_LOG_ALWAYS_RUNTIME
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 文件系统后端（File system backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FS_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_FS_OUTPUT_SYST"></a>

## 367.45 `CONFIG_LOG_BACKEND_FS_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_FS_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 文件系统后端（File system backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_FS_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_FS_OUTPUT_TEXT"></a>

## 367.46 `CONFIG_LOG_BACKEND_FS_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_FS_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 文件系统后端（File system backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FS_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_FS_OVERWRITE"></a>

## 367.47 `CONFIG_LOG_BACKEND_FS_OVERWRITE`

**提示（Prompt）**：覆盖旧日志文件（overwrite）

**说明（Help）**

启用后，后端覆盖最旧的日志文件；否则，在存储空间用满后丢弃新消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_FS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.fs:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.fs#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 文件系统后端（File system backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FS`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_I2C_OUTPUT"></a>

## 367.48 `CONFIG_LOG_BACKEND_I2C_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_I2C && CONFIG_LOG && !CONFIG_LOG_MODE_MINIMAL && CONFIG_INTEL_HAL
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_I2C_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_I2C_OUTPUT_TEXT
CONFIG_LOG_BACKEND_I2C_OUTPUT_SYST
CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_I2C_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → 启用 I2C 日志后端（Log Backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_I2C`](P011_module_hal_intel_zephyr_配置项参考.md#CONFIG_LOG_BACKEND_I2C)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_INTEL_HAL`](P203_modules_Kconfig.intel_配置项参考.md#CONFIG_INTEL_HAL)、[`CONFIG_LOG_BACKEND_I2C_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_I2C_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_I2C_OUTPUT_SYST`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_I2C_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_I2C_OUTPUT_CUSTOM`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_I2C_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_I2C_OUTPUT_CUSTOM"></a>

## 367.49 `CONFIG_LOG_BACKEND_I2C_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_I2C_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → 启用 I2C 日志后端（Log Backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_I2C_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_I2C_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY"></a>

## 367.50 `CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_I2C_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_DICTIONARY_SUPPORT
```

**弱选择（Implies）**

```text
CONFIG_LOG_FMT_SECTION
CONFIG_LOG_FMT_SECTION_STRIP if !CONFIG_LOG_ALWAYS_RUNTIME
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → 启用 I2C 日志后端（Log Backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_I2C_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_I2C_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_I2C_OUTPUT_SYST"></a>

## 367.51 `CONFIG_LOG_BACKEND_I2C_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_I2C_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → 启用 I2C 日志后端（Log Backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_I2C_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_I2C_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_I2C_OUTPUT_TEXT"></a>

## 367.52 `CONFIG_LOG_BACKEND_I2C_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_I2C_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → 启用 I2C 日志后端（Log Backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_I2C_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_I2C_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_IPC_SERVICE"></a>

## 367.53 `CONFIG_LOG_BACKEND_IPC_SERVICE`

**提示（Prompt）**：IPC 服务后端（Backend）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_MULTIDOMAIN_BACKEND
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.multidomain:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.multidomain#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_MULTIDOMAIN_BACKEND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MULTIDOMAIN_BACKEND)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LOG_MULTIDOMAIN_BACKEND`。

<a id="CONFIG_LOG_BACKEND_MQTT"></a>

## 367.54 `CONFIG_LOG_BACKEND_MQTT`

**提示（Prompt）**：MQTT 后端（backend）

**说明（Help）**

使用外部 MQTT 客户端向 MQTT 消息代理（broker）发送日志消息。应用通过 `log_backend_mqtt_client_set()` API 提供 MQTT 客户端，后端使用它向可配置的 MQTT 主题（topic）发布日志消息。应用负责初始化、连接及管理 MQTT 客户端的生命周期（lifecycle）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_LIB && !CONFIG_LOG_MODE_IMMEDIATE && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.mqtt:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.mqtt#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MQTT_LIB)、[`CONFIG_LOG_MODE_IMMEDIATE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_IMMEDIATE)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_MQTT_MAX_MSG_SIZE"></a>

## 367.55 `CONFIG_LOG_BACKEND_MQTT_MAX_MSG_SIZE`

**提示（Prompt）**：日志消息最大大小（Maximum log message size）

**说明（Help）**

单条日志消息的最大大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_MQTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[64, 1024]
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.mqtt:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.mqtt#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_MQTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_MQTT_OUTPUT"></a>

## 367.56 `CONFIG_LOG_BACKEND_MQTT_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_MQTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_MQTT_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_MQTT_OUTPUT_TEXT
CONFIG_LOG_BACKEND_MQTT_OUTPUT_SYST
CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_MQTT_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_MQTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_MQTT_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_MQTT_OUTPUT_SYST`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_MQTT_OUTPUT_CUSTOM`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_MQTT_OUTPUT_CUSTOM"></a>

## 367.57 `CONFIG_LOG_BACKEND_MQTT_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_MQTT_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → MQTT 后端（backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_MQTT_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY"></a>

## 367.58 `CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_MQTT_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_DICTIONARY_SUPPORT
```

**弱选择（Implies）**

```text
CONFIG_LOG_FMT_SECTION
CONFIG_LOG_FMT_SECTION_STRIP if !CONFIG_LOG_ALWAYS_RUNTIME
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → MQTT 后端（backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_MQTT_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_MQTT_OUTPUT_SYST"></a>

## 367.59 `CONFIG_LOG_BACKEND_MQTT_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_MQTT_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → MQTT 后端（backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_MQTT_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_MQTT_OUTPUT_TEXT"></a>

## 367.60 `CONFIG_LOG_BACKEND_MQTT_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_MQTT_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → MQTT 后端（backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_MQTT_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_MQTT_QOS"></a>

## 367.61 `CONFIG_LOG_BACKEND_MQTT_QOS`

**提示（Prompt）**：MQTT 服务质量等级（Quality of Service，QoS）

**说明（Help）**

发布日志消息时使用的服务质量（QoS）等级：

- `0`：至多一次交付（At most once），发送后不等待确认（fire and forget）。
- `1`：至少一次交付（At least once），需要确认（acknowledged delivery）。
- `2`：恰好一次交付（Exactly once），保证交付（assured delivery）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_MQTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.mqtt:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.mqtt#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_MQTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_MQTT_RETAIN"></a>

## 367.62 `CONFIG_LOG_BACKEND_MQTT_RETAIN`

**提示（Prompt）**：保留 MQTT 消息（Retain）

**说明（Help）**

启用后，发布的日志消息将由消息代理（broker）保留，并在新订阅者订阅后立即发送给它们。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_MQTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.mqtt:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.mqtt#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_MQTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_MQTT_TOPIC_DEFAULT"></a>

## 367.63 `CONFIG_LOG_BACKEND_MQTT_TOPIC_DEFAULT`

**提示（Prompt）**：日志消息的默认 MQTT 主题（topic）

**说明（Help）**

日志消息使用的默认 MQTT 主题（topic）。可通过日志后端的 MQTT API 在运行时更改。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_MQTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
"zephyr/logs"
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.mqtt:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.mqtt#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_MQTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NATIVE_POSIX"></a>

## 367.64 `CONFIG_LOG_BACKEND_NATIVE_POSIX`

**提示（Prompt）**：原生后端（Native backend）

**说明（Help）**

在 native_posix 中启用后端（backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.native_posix:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.native_posix#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP)。

<a id="CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT"></a>

## 367.65 `CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NATIVE_POSIX && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_TEXT
CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_SYST
CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 原生后端（Native backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NATIVE_POSIX`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_SYST`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_CUSTOM`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_CUSTOM"></a>

## 367.66 `CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 原生后端（Native backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY"></a>

## 367.67 `CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_DICTIONARY_SUPPORT
```

**弱选择（Implies）**

```text
CONFIG_LOG_FMT_SECTION
CONFIG_LOG_FMT_SECTION_STRIP if !CONFIG_LOG_ALWAYS_RUNTIME
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 原生后端（Native backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_SYST"></a>

## 367.68 `CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 原生后端（Native backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_TEXT"></a>

## 367.69 `CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 原生后端（Native backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_NATIVE_POSIX_STDOUT_BUF_SIZE"></a>

## 367.70 `CONFIG_LOG_BACKEND_NATIVE_POSIX_STDOUT_BUF_SIZE`

**提示（Prompt）**：标准输出缓冲区大小（Standard Output Buffer Size）

**说明（Help）**

将日志刷新到主机终端（host terminal）之前，用于暂存日志消息的缓冲区大小。遇到换行或缓冲区满时刷新消息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NATIVE_POSIX && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.native_posix:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.native_posix#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 原生后端（Native backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NATIVE_POSIX`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NET"></a>

## 367.71 `CONFIG_LOG_BACKEND_NET`

**提示（Prompt）**：网络后端（Networking backend）

**说明（Help）**

向网络服务器发送 syslog 消息。详情参见 RFC 5424（syslog 协议）、RFC 5426（通过 UDP 的 syslog）和 RFC 6587（通过 TCP 的 syslog）规范。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING && (CONFIG_NET_UDP || CONFIG_NET_TCP) && CONFIG_NET_SOCKETS && !CONFIG_LOG_MODE_IMMEDIATE && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_LOG_MODE_IMMEDIATE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_IMMEDIATE)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NET_AUTOSTART"></a>

## 367.72 `CONFIG_LOG_BACKEND_NET_AUTOSTART`

**提示（Prompt）**：自动启动网络后端（networking backend）

**说明（Help）**

启用后，在应用启动时自动启动网络后端。若此时尚无通往日志服务器的路由（routes），必须设为 `n`，由应用稍后启动后端，否则日志线程可能阻塞。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if CONFIG_NET_CONFIG_NEED_IPV4 || CONFIG_NET_CONFIG_NEED_IPV6
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NET_CONFIG_NEED_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_NEED_IPV4)、[`CONFIG_NET_CONFIG_NEED_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_NEED_IPV6)。

<a id="CONFIG_LOG_BACKEND_NET_MAX_BUF_SIZE"></a>

## 367.73 `CONFIG_LOG_BACKEND_NET_MAX_BUF_SIZE`

**提示（Prompt）**：syslog 消息最大大小（Max message size）

**说明（Help）**

每条 syslog 消息都必须能装入一个 UDP 数据包，因此应设置足够的大小以免消息被截断。RFC 5426 建议 IPv4 使用 480 个八位字节（octets），IPv6 使用 1180 个八位字节。每个缓冲区都会消耗 RAM，故应选择足以容纳典型消息的值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
1180 if CONFIG_NET_IPV6
480 if CONFIG_NET_IPV4
256
```

**取值范围（Ranges）**

```text
[64, 1180]
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)。

<a id="CONFIG_LOG_BACKEND_NET_OUTPUT"></a>

## 367.74 `CONFIG_LOG_BACKEND_NET_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_NET_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_NET_OUTPUT_TEXT
CONFIG_LOG_BACKEND_NET_OUTPUT_SYST
CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_NET_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_NET_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_NET_OUTPUT_SYST`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_NET_OUTPUT_CUSTOM`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_NET_OUTPUT_CUSTOM"></a>

## 367.75 `CONFIG_LOG_BACKEND_NET_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_NET_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY"></a>

## 367.76 `CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_NET_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_DICTIONARY_SUPPORT
```

**弱选择（Implies）**

```text
CONFIG_LOG_FMT_SECTION
CONFIG_LOG_FMT_SECTION_STRIP if !CONFIG_LOG_ALWAYS_RUNTIME
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_NET_OUTPUT_SYST"></a>

## 367.77 `CONFIG_LOG_BACKEND_NET_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_NET_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_NET_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_NET_OUTPUT_TEXT"></a>

## 367.78 `CONFIG_LOG_BACKEND_NET_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_NET_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_ISSYNCED"></a>

## 367.79 `CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_ISSYNCED`

**提示（Prompt）**：RFC 5424 第 7.1.2 节的 isSynced 字段

**说明（Help）**

`isSynced` 参数表示消息发起方（originator）是否已与可靠的外部时间源同步，例如通过网络时间协议（NTP）。详情参见 RFC 5424 第 7.1 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA && CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend） → 按 RFC 5424 打印结构化数据（structured data）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA)、[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_SEQID"></a>

## 367.80 `CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_SEQID`

**提示（Prompt）**：RFC 5424 第 7.3.1 节的序列标识字段（sequence id）

**说明（Help）**

序列标识（sequence id）参数跟踪发起方向 syslog 传输层提交待发送消息的顺序。详情参见 RFC 5424 第 7.3.1 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA && CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend） → 按 RFC 5424 打印结构化数据（structured data）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA)、[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_SOFTWARE"></a>

## 367.81 `CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_SOFTWARE`

**提示（Prompt）**：RFC 5424 第 7.2.3 节的软件描述字段（software description）

**说明（Help）**

软件描述（software description）参数唯一标识生成消息的软件。详情参见 RFC 5424 第 7.2 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA && CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend） → 按 RFC 5424 打印结构化数据（structured data）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA)、[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_SOFTWARE_VALUE"></a>

## 367.82 `CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_SOFTWARE_VALUE`

**提示（Prompt）**：RFC 5424 第 7.2.3 节的 software 字段值

**说明（Help）**

用户定义的 `software` 字段值。详情参见 RFC 5424 第 7.2.3 节。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_SOFTWARE && CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
"zephyr"
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend） → 按 RFC 5424 打印结构化数据（structured data） → RFC 5424 第 7.2.3 节的软件描述字段（software description）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_SOFTWARE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_SOFTWARE)、[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_SOFTWARE_VERSION"></a>

## 367.83 `CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_SOFTWARE_VERSION`

**提示（Prompt）**：RFC 5424 第 7.2.4 节的软件版本字段（software version）

**说明（Help）**

软件版本（software version）参数唯一标识生成消息的软件。详情参见 RFC 5424 第 7.2.4 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA && CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend） → 按 RFC 5424 打印结构化数据（structured data）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA)、[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_TZKNOWN"></a>

## 367.84 `CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_TZKNOWN`

**提示（Prompt）**：RFC 5424 第 7.1.1 节的 tzKnown 字段

**说明（Help）**

`tzKnown` 参数表示消息发起方（originator）是否知道其时区（time zone）。详情参见 RFC 5424 第 7.1 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA && CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend） → 按 RFC 5424 打印结构化数据（structured data）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA)、[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_UPTIME"></a>

## 367.85 `CONFIG_LOG_BACKEND_NET_RFC5424_SDATA_UPTIME`

**提示（Prompt）**：RFC 5424 第 7.3.2 节的系统运行时间字段（system uptime）

**说明（Help）**

系统运行时间（system uptime）参数跟踪“自系统网络管理部分上次重新初始化以来的时间”，单位为百分之一秒。Zephyr 当前将其解释为系统运行时间。详情参见 RFC 5424 第 7.3.2 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA && CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend） → 按 RFC 5424 打印结构化数据（structured data）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA)、[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA"></a>

## 367.86 `CONFIG_LOG_BACKEND_NET_RFC5424_STRUCTURED_DATA`

**提示（Prompt）**：按 RFC 5424 打印结构化数据（structured data）

**说明（Help）**

打印 RFC 5424 第 6.3 节所述的附加结构化数据（structured data）。注意，这可能显著增加 syslog 消息长度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NET_SERVER"></a>

## 367.87 `CONFIG_LOG_BACKEND_NET_SERVER`

**提示（Prompt）**：Syslog 服务器 IP 地址

**说明（Help）**

可使用 IPv4 或 IPv6 地址，也可在此配置服务器监听的 UDP 端口号。支持如下语法：

```text
192.0.2.1:514
192.0.2.42
[2001:db8::1]:514
[2001:db8::2]
2001:db::42
```

若需使用 TCP，在地址前添加 `tcp://`，例如：

```text
tcp://192.0.2.1:514
tcp://192.0.2.42
tcp://[2001:db8::1]:514
```

未提供 URI 前缀时，默认使用 UDP。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NET_USE_CONNECTION_MANAGER"></a>

## 367.88 `CONFIG_LOG_BACKEND_NET_USE_CONNECTION_MANAGER`

**提示（Prompt）**：使用连接管理器（connection manager）启停网络后端

**说明（Help）**

启用后，使用连接管理器（connection manager）启动和停止网络后端。适用于应用必须等待网络连接建立后，才能启动日志后端的场景。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONNECTION_MANAGER && CONFIG_LOG_BACKEND_NET_AUTOSTART && CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend） → 自动启动网络后端（networking backend）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONNECTION_MANAGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONNECTION_MANAGER)、[`CONFIG_LOG_BACKEND_NET_AUTOSTART`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_AUTOSTART)、[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_NET_USE_DHCPV4_OPTION"></a>

## 367.89 `CONFIG_LOG_BACKEND_NET_USE_DHCPV4_OPTION`

**提示（Prompt）**：使用 DHCPv4 日志服务器选项配置 syslog 服务器

**说明（Help）**

启用后，从 DHCPv4 日志服务器选项（Log Server Option，编号 `7`）读取 syslog 服务器 IP 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4 && CONFIG_LOG_BACKEND_NET && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.net:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.net#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 网络后端（Networking backend）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4)、[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_RTT"></a>

## 367.90 `CONFIG_LOG_BACKEND_RTT`

**提示（Prompt）**：SEGGER J-Link RTT 后端

**说明（Help）**

启用后，后端使用实时传输（RTT）记录日志。此后端逐条处理消息：根据可用空间及所选模式，一次仅将一条完整消息传入上行缓冲区（up-buffer），消息以回车符 `\r` 结尾。进入致命错误模式（panic mode）后，后端始终阻塞，等待上行缓冲区有足够空间容纳消息，且消息已传至主机。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_LOG_BACKEND
```

**主动选择（Selects）**

```text
CONFIG_SEGGER_RTT_CUSTOM_LOCKING
CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.rtt:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.rtt#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SHELL_LOG_BACKEND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_LOG_BACKEND)、[`CONFIG_SEGGER_RTT_CUSTOM_LOCKING`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_CUSTOM_LOCKING)、[`CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP)。

<a id="CONFIG_LOG_BACKEND_RTT_BUFFER"></a>

## 367.91 `CONFIG_LOG_BACKEND_RTT_BUFFER`

**提示（Prompt）**：用于日志输出（Logger Output）的缓冲区编号。

**说明（Help）**

选择用于日志输出（Logger Output）的上行缓冲区（Up-Buffer）索引；默认使用终端上行缓冲区及其设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_RTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS]
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.rtt:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.rtt#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS)。

<a id="CONFIG_LOG_BACKEND_RTT_BUFFER_SIZE"></a>

## 367.92 `CONFIG_LOG_BACKEND_RTT_BUFFER_SIZE`

**提示（Prompt）**：为日志输出（Logger Output）预留的上行缓冲区（Up-Buffer）大小。

**说明（Help）**

指定用于日志输出（Logger Output）的上行缓冲区（Up-Buffer）预留大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_RTT_BUFFER > 0 && CONFIG_LOG_BACKEND_RTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.rtt:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.rtt#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT_BUFFER`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_BUFFER)、[`CONFIG_LOG_BACKEND_RTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_RTT_MESSAGE_SIZE"></a>

## 367.93 `CONFIG_LOG_BACKEND_RTT_MESSAGE_SIZE`

**提示（Prompt）**：用于存储消息的内部缓冲区大小。

**说明（Help）**

定义可传入上行缓冲区（up-buffer）的最大消息大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_RTT_MODE_DROP && CONFIG_LOG_BACKEND_RTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[32, 256]
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.rtt:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.rtt#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT_MODE_DROP`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_MODE_DROP)、[`CONFIG_LOG_BACKEND_RTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_RTT_MODE"></a>

## 367.94 `CONFIG_LOG_BACKEND_RTT_MODE`

**提示（Prompt）**：日志器行为（Logger behavior）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_RTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_RTT_MODE_BLOCK
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_RTT_MODE_DROP
CONFIG_LOG_BACKEND_RTT_MODE_BLOCK
CONFIG_LOG_BACKEND_RTT_MODE_OVERWRITE
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.rtt:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.rtt#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_RTT_MODE_BLOCK`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_MODE_BLOCK)、[`CONFIG_LOG_BACKEND_RTT_MODE_DROP`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_MODE_DROP)、[`CONFIG_LOG_BACKEND_RTT_MODE_OVERWRITE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_MODE_OVERWRITE)。

<a id="CONFIG_LOG_BACKEND_RTT_MODE_BLOCK"></a>

## 367.95 `CONFIG_LOG_BACKEND_RTT_MODE_BLOCK`

**提示（Prompt）**：阻塞直到消息传至主机（host）。

**说明（Help）**

等待上行缓冲区（up-buffer）有足够空间容纳一条消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_RTT_MODE>
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.rtt:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.rtt#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端 → 日志器行为（Logger behavior）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT_MODE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_MODE)。

<a id="CONFIG_LOG_BACKEND_RTT_MODE_DROP"></a>

## 367.96 `CONFIG_LOG_BACKEND_RTT_MODE_DROP`

**提示（Prompt）**：丢弃无法装入上行缓冲区（up-buffer）的消息。

**说明（Help）**

如果上行缓冲区（up-buffer）空间不足以容纳一条消息，则丢弃它，并记录丢弃消息的数量。增大上行缓冲区可减少消息丢弃。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_RTT_MODE>
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.rtt:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.rtt#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端 → 日志器行为（Logger behavior）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT_MODE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_MODE)。

<a id="CONFIG_LOG_BACKEND_RTT_MODE_OVERWRITE"></a>

## 367.97 `CONFIG_LOG_BACKEND_RTT_MODE_OVERWRITE`

**提示（Prompt）**：上行缓冲区满时覆盖消息（Overwrite）

**说明（Help）**

如果上行缓冲区（up-buffer）空间不足以容纳一条消息，则覆盖最旧的消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_RTT_MODE>
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.rtt:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.rtt#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端 → 日志器行为（Logger behavior）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT_MODE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_MODE)。

<a id="CONFIG_LOG_BACKEND_RTT_OUTPUT"></a>

## 367.98 `CONFIG_LOG_BACKEND_RTT_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_RTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_RTT_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_RTT_OUTPUT_TEXT
CONFIG_LOG_BACKEND_RTT_OUTPUT_SYST
CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_RTT_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_RTT_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_RTT_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_RTT_OUTPUT_SYST`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_RTT_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_RTT_OUTPUT_CUSTOM`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_RTT_OUTPUT_BUFFER_SIZE"></a>

## 367.99 `CONFIG_LOG_BACKEND_RTT_OUTPUT_BUFFER_SIZE`

**提示（Prompt）**：输出缓冲区大小（output buffer）

**说明（Help）**

`log_output` 模块使用此缓冲区准备输出数据，例如进行字符串格式化（string formatting）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_RTT_MODE_BLOCK && CONFIG_LOG_BACKEND_RTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.rtt:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.rtt#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT_MODE_BLOCK`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_MODE_BLOCK)、[`CONFIG_LOG_BACKEND_RTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_RTT_OUTPUT_CUSTOM"></a>

## 367.100 `CONFIG_LOG_BACKEND_RTT_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_RTT_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_OUTPUT)。

<!-- kconfig-navigation -->

[上一章](P366_subsys_logging_配置项参考_15.md) · [返回大纲](大纲.md) · [下一章](P368_subsys_logging_配置项参考_17.md)
