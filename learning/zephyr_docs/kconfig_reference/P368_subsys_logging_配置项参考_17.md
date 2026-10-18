---
id: learning.zephyr-docs.kconfig-reference.page-368
title: "`subsys/logging`配置项参考（17/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第368章\_`subsys/logging`配置项参考（17/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY"></a>

## 368.1 `CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_RTT_OUTPUT>
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

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY_HEX"></a>

## 368.2 `CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY_HEX`

**提示（Prompt）**：以十六进制编码输出字典日志（y），或输出原始二进制（n）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY && CONFIG_LOG_BACKEND_RTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.rtt:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.rtt#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_RTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_RTT_OUTPUT_SYST"></a>

## 368.3 `CONFIG_LOG_BACKEND_RTT_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_RTT_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_RTT_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_RTT_OUTPUT_TEXT"></a>

## 368.4 `CONFIG_LOG_BACKEND_RTT_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_RTT_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT_OUTPUT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_RTT_RETRY_CNT"></a>

## 368.5 `CONFIG_LOG_BACKEND_RTT_RETRY_CNT`

**提示（Prompt）**：重试次数（Number of Retries）

**说明（Help）**

在丢弃数据并认定 RTT 会话（Session）未活动之前，进行发送（TX）重试的次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_RTT_MODE_BLOCK && CONFIG_LOG_BACKEND_RTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.rtt:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.rtt#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT_MODE_BLOCK`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_MODE_BLOCK)、[`CONFIG_LOG_BACKEND_RTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_RTT_RETRY_DELAY_MS"></a>

## 368.6 `CONFIG_LOG_BACKEND_RTT_RETRY_DELAY_MS`

**提示（Prompt）**：发送重试间隔，单位为毫秒（TX Retry Delay）

**说明（Help）**

两次发送重试（TX Retry）之间的休眠时间。实时传输（RTT）会话期间，主机定期拉取数据，周期从 1–2 毫秒起；RTT 流量增加时，包括主机到设备的流量，该周期可能增加。流量较大时可能丢失数据，需要增大延迟或重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_RTT_MODE_BLOCK && CONFIG_LOG_BACKEND_RTT && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.rtt:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.rtt#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → SEGGER J-Link RTT 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_RTT_MODE_BLOCK`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT_MODE_BLOCK)、[`CONFIG_LOG_BACKEND_RTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_SEMIHOST"></a>

## 368.7 `CONFIG_LOG_BACKEND_SEMIHOST`

**提示（Prompt）**：使用半主机（Semihost）后端

**说明（Help）**

启用半主机（semihost）后端，使用主机标准输出（stdout）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEMIHOST && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.semihost:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.semihost#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_SEMIHOST`](P032_arch_common_配置项参考.md#CONFIG_SEMIHOST)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP)。

<a id="CONFIG_LOG_BACKEND_SEMIHOST_AUTOSTART"></a>

## 368.8 `CONFIG_LOG_BACKEND_SEMIHOST_AUTOSTART`

**提示（Prompt）**：自动启动半主机后端（semihost backend）

**说明（Help）**

允许半主机后端（semihost backend）自动启动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_SEMIHOST && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.semihost:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.semihost#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 使用半主机（Semihost）后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SEMIHOST`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_SEMIHOST_BUFFER_SIZE"></a>

## 368.9 `CONFIG_LOG_BACKEND_SEMIHOST_BUFFER_SIZE`

**提示（Prompt）**：为日志输出（Logger Output）预留的上行缓冲区（Up-Buffer）大小。

**说明（Help）**

指定用于日志输出（Logger Output）的上行缓冲区（Up-Buffer）预留大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_SEMIHOST && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.semihost:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.semihost#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 使用半主机（Semihost）后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SEMIHOST`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT"></a>

## 368.10 `CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_SEMIHOST && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_TEXT
CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_SYST
CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 使用半主机（Semihost）后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SEMIHOST`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_SYST`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_CUSTOM`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_CUSTOM"></a>

## 368.11 `CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 使用半主机（Semihost）后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY"></a>

## 368.12 `CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT>
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

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 使用半主机（Semihost）后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_SYST"></a>

## 368.13 `CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 使用半主机（Semihost）后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_TEXT"></a>

## 368.14 `CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 使用半主机（Semihost）后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_SHOW_COLOR"></a>

## 368.15 `CONFIG_LOG_BACKEND_SHOW_COLOR`

**提示（Prompt）**：后端彩色输出（Colors）

**说明（Help）**

启用后，所选后端用红色打印错误（errors）、黄色打印警告（warnings）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if CONFIG_LOG_BACKEND_UART || CONFIG_LOG_BACKEND_NATIVE_POSIX || CONFIG_LOG_BACKEND_RTT || CONFIG_LOG_BACKEND_SWO || CONFIG_LOG_BACKEND_XTENSA_SIM || CONFIG_SHELL_LOG_BACKEND
```

**被弱选择（Implied by）**

```text
CONFIG_DEBUG_NRF_ETR_DECODE
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_UART`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART)、[`CONFIG_LOG_BACKEND_NATIVE_POSIX`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX)、[`CONFIG_LOG_BACKEND_RTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT)、[`CONFIG_LOG_BACKEND_SWO`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO)、[`CONFIG_LOG_BACKEND_XTENSA_SIM`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM)、[`CONFIG_SHELL_LOG_BACKEND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_LOG_BACKEND)、[`CONFIG_DEBUG_NRF_ETR_DECODE`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_DECODE)。

<a id="CONFIG_LOG_BACKEND_SHOW_LEVEL"></a>

## 368.16 `CONFIG_LOG_BACKEND_SHOW_LEVEL`

**提示（Prompt）**：后端日志级别输出（Levels）

**说明（Help）**

启用后，所选后端随日志打印级别（levels）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_SHOW_TIMESTAMP"></a>

## 368.17 `CONFIG_LOG_BACKEND_SHOW_TIMESTAMP`

**提示（Prompt）**：后端时间戳输出（Timestamps）

**说明（Help）**

启用后，所选后端随日志打印时间戳（timestamps）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_SKIP_SOURCE"></a>

## 368.18 `CONFIG_LOG_BACKEND_SKIP_SOURCE`

**提示（Prompt）**：不记录日志来源（source）

**说明（Help）**

启用后，所选后端打印日志时不添加来源（source）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:252`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L252)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_SPINEL"></a>

## 368.19 `CONFIG_LOG_BACKEND_SPINEL`

**提示（Prompt）**：OpenThread 专用 Spinel 协议后端

**说明（Help）**

启用后，后端使用 OpenThread 专用的 SPINEL 协议记录日志。该协议面向字节（byte oriented），将消息封装为串行帧（serial frames）。此后端应仅用于 OpenThread，且必须禁用 UART 后端，或使 UART 后端工作在另一个 UART 设备上，以免相互干扰。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_BACKEND_UART && CONFIG_OPENTHREAD && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.spinel:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.spinel#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_UART`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_SPINEL_BUFFER_SIZE"></a>

## 368.20 `CONFIG_LOG_BACKEND_SPINEL_BUFFER_SIZE`

**提示（Prompt）**：为日志输出（Logger Output）预留的上行缓冲区（Up-Buffer）大小。

**说明（Help）**

指定用于日志输出（Logger Output）的上行缓冲区（Up-Buffer）预留大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_SPINEL && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.spinel:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.spinel#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → OpenThread 专用 Spinel 协议后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SPINEL`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_SPINEL_OUTPUT"></a>

## 368.21 `CONFIG_LOG_BACKEND_SPINEL_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_SPINEL && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_SPINEL_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_SPINEL_OUTPUT_TEXT
CONFIG_LOG_BACKEND_SPINEL_OUTPUT_SYST
CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_SPINEL_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → OpenThread 专用 Spinel 协议后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SPINEL`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_SPINEL_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_SPINEL_OUTPUT_SYST`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_SPINEL_OUTPUT_CUSTOM`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_SPINEL_OUTPUT_CUSTOM"></a>

## 368.22 `CONFIG_LOG_BACKEND_SPINEL_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_SPINEL_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → OpenThread 专用 Spinel 协议后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SPINEL_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY"></a>

## 368.23 `CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_SPINEL_OUTPUT>
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

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → OpenThread 专用 Spinel 协议后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SPINEL_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_SPINEL_OUTPUT_SYST"></a>

## 368.24 `CONFIG_LOG_BACKEND_SPINEL_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_SPINEL_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → OpenThread 专用 Spinel 协议后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_SPINEL_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_SPINEL_OUTPUT_TEXT"></a>

## 368.25 `CONFIG_LOG_BACKEND_SPINEL_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_SPINEL_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → OpenThread 专用 Spinel 协议后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SPINEL_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP"></a>

## 368.26 `CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由支持时间戳格式化（timestamp formatting）的日志后端选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**被选择（Selected by）**

```text
CONFIG_LOG_BACKEND_ADSP
CONFIG_LOG_BACKEND_ADSP_MTRACE
CONFIG_LOG_BACKEND_FS
CONFIG_LOG_BACKEND_NATIVE_POSIX
CONFIG_LOG_BACKEND_RTT
CONFIG_LOG_BACKEND_SWO
CONFIG_LOG_BACKEND_UART
CONFIG_LOG_BACKEND_XTENSA_SIM
CONFIG_LOG_BACKEND_SEMIHOST
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_ADSP`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP)、[`CONFIG_LOG_BACKEND_ADSP_MTRACE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE)、[`CONFIG_LOG_BACKEND_FS`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS)、[`CONFIG_LOG_BACKEND_NATIVE_POSIX`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX)、[`CONFIG_LOG_BACKEND_RTT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_RTT)、[`CONFIG_LOG_BACKEND_SWO`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO)、[`CONFIG_LOG_BACKEND_UART`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART)、[`CONFIG_LOG_BACKEND_XTENSA_SIM`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM)、[`CONFIG_LOG_BACKEND_SEMIHOST`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST)。

<a id="CONFIG_LOG_BACKEND_SWO"></a>

## 368.27 `CONFIG_LOG_BACKEND_SWO`

**提示（Prompt）**：串行线输出后端（Serial Wire Output，SWO）

**说明（Help）**

启用后，后端使用串行线输出（SWO）记录日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SWO && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.swo:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.swo#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SWO`](P030_arch_arm_配置项参考_2.md#CONFIG_HAS_SWO)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP)。

<a id="CONFIG_LOG_BACKEND_SWO_FREQ_HZ"></a>

## 368.28 `CONFIG_LOG_BACKEND_SWO_FREQ_HZ`

**提示（Prompt）**：设置 SWO 输出频率（output frequency）

**说明（Help）**

设置串行线输出（SWO）频率。值 `0` 表示使用给定微控制器（MCU）支持的最高频率。并非所有调试探针（debug probes）都支持高频 SWO，此时需要手动设定频率。

本项定义的 SWO 频率在启动时配置。大多数 SWO 查看程序连接调试探针时也会配置 SWO 频率，该配置仅持续到设备复位。为保证正常工作，此处与 SWO 查看程序配置的频率必须一致。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_SWO && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.swo:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.swo#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 串行线输出后端（Serial Wire Output，SWO）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SWO`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_SWO_OUTPUT"></a>

## 368.29 `CONFIG_LOG_BACKEND_SWO_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_SWO && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_SWO_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_SWO_OUTPUT_TEXT
CONFIG_LOG_BACKEND_SWO_OUTPUT_SYST
CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_SWO_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 串行线输出后端（Serial Wire Output，SWO）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SWO`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_SWO_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_SWO_OUTPUT_SYST`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_SWO_OUTPUT_CUSTOM`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_SWO_OUTPUT_CUSTOM"></a>

## 368.30 `CONFIG_LOG_BACKEND_SWO_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_SWO_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 串行线输出后端（Serial Wire Output，SWO） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SWO_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY"></a>

## 368.31 `CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_SWO_OUTPUT>
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

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 串行线输出后端（Serial Wire Output，SWO） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SWO_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_SWO_OUTPUT_SYST"></a>

## 368.32 `CONFIG_LOG_BACKEND_SWO_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_SWO_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 串行线输出后端（Serial Wire Output，SWO） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_SWO_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_SWO_OUTPUT_TEXT"></a>

## 368.33 `CONFIG_LOG_BACKEND_SWO_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_SWO_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 串行线输出后端（Serial Wire Output，SWO） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SWO_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_SWO_PROTOCOL_MANCHESTER"></a>

## 368.34 `CONFIG_LOG_BACKEND_SWO_PROTOCOL_MANCHESTER`

**提示（Prompt）**：曼彻斯特编码（Manchester encoding）

**说明（Help）**

使用曼彻斯特编码（Manchester encoding）。支持范围较小，但接收端能够自动恢复时钟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.swo:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.swo#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 串行线输出后端（Serial Wire Output，SWO） → SWO 协议（protocol）

<a id="CONFIG_LOG_BACKEND_SWO_PROTOCOL_NRZ"></a>

## 368.35 `CONFIG_LOG_BACKEND_SWO_PROTOCOL_NRZ`

**提示（Prompt）**：不归零编码（NRZ encoding）

**说明（Help）**

使用类似 UART 的不归零编码（NRZ）。这是最常见的选项，但接收端必须知道 SWO 输出频率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.swo:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.swo#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 串行线输出后端（Serial Wire Output，SWO） → SWO 协议（protocol）

<a id="CONFIG_LOG_BACKEND_SWO_REF_FREQ_HZ"></a>

## 368.36 `CONFIG_LOG_BACKEND_SWO_REF_FREQ_HZ`

**提示（Prompt）**：SWO 参考时钟频率（reference clock frequency）

**说明（Help）**

设置 SWO 参考频率，通常等于 CPU 频率。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_SWO && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
0 if n
0 if n
0
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.swo:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.swo#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 串行线输出后端（Serial Wire Output，SWO）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SWO`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_SWO_SYNC_PACKETS"></a>

## 368.37 `CONFIG_LOG_BACKEND_SWO_SYNC_PACKETS`

**提示（Prompt）**：同步包发送（Synchronization packet transmission）

**说明（Help）**

在比特流（bitstream）中生成具有独特模式的同步包（synchronization packets）。如果 SWO 引脚用于通过普通终端程序输出简单的 UART 文本，这些同步包会表现为定期出现的特殊字符。禁用此项即可避免。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_SWO && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.swo:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.swo#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → 串行线输出后端（Serial Wire Output，SWO）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SWO`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_UART"></a>

## 368.38 `CONFIG_LOG_BACKEND_UART`

**提示（Prompt）**：UART 后端（backend）。

**说明（Help）**

启用后，后端使用 UART 输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_CONSOLE && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_BACKEND_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.uart:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.uart#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_UART_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_UART_CONSOLE)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SHELL_BACKEND_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP)。

<a id="CONFIG_LOG_BACKEND_UART_ASYNC"></a>

## 368.39 `CONFIG_LOG_BACKEND_UART_ASYNC`

**提示（Prompt）**：使用 UART 异步 API（Asynchronous API）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_HEX && CONFIG_LOG_BACKEND_UART && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.uart:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.uart#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → UART 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_HEX`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_HEX)、[`CONFIG_LOG_BACKEND_UART`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_UART_AUTOSTART"></a>

## 368.40 `CONFIG_LOG_BACKEND_UART_AUTOSTART`

**提示（Prompt）**：自动启动 UART 后端

**说明（Help）**

启用后，在应用启动时自动启动 UART 日志后端。禁用时，应用必须调用 `log_backend_enable()` 手动启动后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_UART && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.uart:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.uart#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → UART 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_UART`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_UART_BUFFER_SIZE"></a>

## 368.41 `CONFIG_LOG_BACKEND_UART_BUFFER_SIZE`

**提示（Prompt）**：刷新前在 RAM 中缓冲的最大字节数

**说明（Help）**

在延迟日志模式（deferred logging mode）下，设置 RAM 可缓冲的最大字节数，达到后会自动对 UART 后端调用 `log_output_flush`；每条日志消息结束后也会刷新缓冲区。立即日志模式（immediate logging mode）下，已处理的日志消息不缓冲，始终逐字节输出。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_UART && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
32 if CONFIG_LOG_BACKEND_UART_ASYNC
1
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.uart:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.uart#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → UART 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_UART`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_UART_ASYNC`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_ASYNC)。

<a id="CONFIG_LOG_BACKEND_UART_OUTPUT"></a>

## 368.42 `CONFIG_LOG_BACKEND_UART_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_UART && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_UART_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_UART_OUTPUT_TEXT
CONFIG_LOG_BACKEND_UART_OUTPUT_SYST
CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_UART_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → UART 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_UART`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_UART_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_UART_OUTPUT_SYST`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_UART_OUTPUT_CUSTOM`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_UART_OUTPUT_CUSTOM"></a>

## 368.43 `CONFIG_LOG_BACKEND_UART_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_UART_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → UART 后端（backend）。 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_UART_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY"></a>

## 368.44 `CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_UART_OUTPUT>
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

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → UART 后端（backend）。 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_UART_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_BIN"></a>

## 368.45 `CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_BIN`

**提示（Prompt）**：字典模式（二进制，Dictionary binary）

**说明（Help）**

以二进制形式输出基于字典的日志（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.uart:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.uart#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → UART 后端（backend）。 → 字典模式输出格式（Dictionary mode output format）

<a id="CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_HEX"></a>

## 368.46 `CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_HEX`

**提示（Prompt）**：字典模式（十六进制，Dictionary hexadecimal）

**说明（Help）**

以十六进制形式输出基于字典的日志（dictionary-based logging）。仅 UART 后端支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.uart:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.uart#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → UART 后端（backend）。 → 字典模式输出格式（Dictionary mode output format）

<a id="CONFIG_LOG_BACKEND_UART_OUTPUT_SYST"></a>

## 368.47 `CONFIG_LOG_BACKEND_UART_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_UART_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → UART 后端（backend）。 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_UART_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_UART_OUTPUT_TEXT"></a>

## 368.48 `CONFIG_LOG_BACKEND_UART_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_UART_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → UART 后端（backend）。 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_UART_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_WS"></a>

## 368.49 `CONFIG_LOG_BACKEND_WS`

**提示（Prompt）**：WebSocket 后端

**说明（Help）**

向 WebSocket 控制台（console）发送控制台消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WEBSOCKET_CONSOLE && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.ws:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.ws#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_WEBSOCKET_CONSOLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CONSOLE)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_WS_AUTOSTART"></a>

## 368.50 `CONFIG_LOG_BACKEND_WS_AUTOSTART`

**提示（Prompt）**：自动启动 WebSocket 后端

**说明（Help）**

启用后，在应用启动时自动启动 WebSocket 后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_WS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if CONFIG_NET_CONFIG_NEED_IPV4 || CONFIG_NET_CONFIG_NEED_IPV6
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.ws:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.ws#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → WebSocket 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_WS`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NET_CONFIG_NEED_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_NEED_IPV4)、[`CONFIG_NET_CONFIG_NEED_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_NEED_IPV6)。

<a id="CONFIG_LOG_BACKEND_WS_MAX_BUF_SIZE"></a>

## 368.51 `CONFIG_LOG_BACKEND_WS_MAX_BUF_SIZE`

**提示（Prompt）**：消息最大大小（Max message size）

**说明（Help）**

通过 WebSocket 发送的输出字符串最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_WS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[64, 1500]
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.ws:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.ws#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → WebSocket 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_WS`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_WS_OUTPUT"></a>

## 368.52 `CONFIG_LOG_BACKEND_WS_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_WS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_WS_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_WS_OUTPUT_TEXT
CONFIG_LOG_BACKEND_WS_OUTPUT_SYST
CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_WS_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → WebSocket 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_WS`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_WS_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_WS_OUTPUT_SYST`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_WS_OUTPUT_CUSTOM`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_WS_OUTPUT_CUSTOM"></a>

## 368.53 `CONFIG_LOG_BACKEND_WS_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_WS_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → WebSocket 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_WS_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY"></a>

## 368.54 `CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_WS_OUTPUT>
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

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → WebSocket 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_WS_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_WS_OUTPUT_SYST"></a>

## 368.55 `CONFIG_LOG_BACKEND_WS_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_WS_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → WebSocket 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_WS_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_WS_OUTPUT_TEXT"></a>

## 368.56 `CONFIG_LOG_BACKEND_WS_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_WS_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → WebSocket 后端 → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_WS_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_WS_TX_RETRY_CNT"></a>

## 368.57 `CONFIG_LOG_BACKEND_WS_TX_RETRY_CNT`

**提示（Prompt）**：发送重试次数（Number of TX Retries）

**说明（Help）**

丢弃整行数据之前的发送（TX）重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_WS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.ws:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.ws#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → WebSocket 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_WS`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_WS_TX_RETRY_DELAY_MS"></a>

## 368.58 `CONFIG_LOG_BACKEND_WS_TX_RETRY_DELAY_MS`

**提示（Prompt）**：发送重试间隔，单位为毫秒（TX Retry Delay）

**说明（Help）**

发送（TX）重试之间的休眠时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_WS && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.ws:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.ws#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → WebSocket 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_WS`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_XTENSA_OUTPUT_BUFFER_SIZE"></a>

## 368.59 `CONFIG_LOG_BACKEND_XTENSA_OUTPUT_BUFFER_SIZE`

**提示（Prompt）**：输出缓冲区大小（output buffer）

**说明（Help）**

`log_output` 模块使用此缓冲区准备输出数据，例如进行字符串格式化（string formatting）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_XTENSA_SIM && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.xtensa_sim:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.xtensa_sim#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Xtensa 模拟器后端（simulator backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_XTENSA_SIM`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BACKEND_XTENSA_SIM"></a>

## 368.60 `CONFIG_LOG_BACKEND_XTENSA_SIM`

**提示（Prompt）**：Xtensa 模拟器后端（simulator backend）

**说明（Help）**

在 Xtensa 模拟器（simulator）中启用后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SIMULATOR_XTENSA && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if CONFIG_SIMULATOR_XTENSA
```

**主动选择（Selects）**

```text
CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.xtensa_sim:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.xtensa_sim#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends）

**配置项引用（Symbol References）**：[`CONFIG_SIMULATOR_XTENSA`](P040_arch_xtensa_配置项参考.md#CONFIG_SIMULATOR_XTENSA)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SUPPORTS_FORMAT_TIMESTAMP)。

<a id="CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT"></a>

## 368.61 `CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT`

**提示（Prompt）**：后端输出模式（Backend Output Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_XTENSA_SIM && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_TEXT
```

**可选项（Choices）**

```text
CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_TEXT
CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_SYST
CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_CUSTOM
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Xtensa 模拟器后端（simulator backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_XTENSA_SIM`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_SYST`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_SYST)、[`CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_CUSTOM`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_CUSTOM)。

<a id="CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_CUSTOM"></a>

## 368.62 `CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_CUSTOM`

**提示（Prompt）**：外部格式化（Extern）

**说明（Help）**

允许从外部设置自定义格式化函数（formatting function）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Xtensa 模拟器后端（simulator backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY"></a>

## 368.63 `CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY`

**提示（Prompt）**：字典模式（Dictionary）

**说明（Help）**

后端采用基于字典的日志输出模式（dictionary-based logging）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT>
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

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Xtensa 模拟器后端（simulator backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_SYST"></a>

## 368.64 `CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_SYST`

**提示（Prompt）**：MIPI SyS-T 格式

**说明（Help）**

启用后，后端用于输出 syst 格式的日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && <choice CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Xtensa 模拟器后端（simulator backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT)。

<a id="CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_TEXT"></a>

## 368.65 `CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_TEXT`

**提示（Prompt）**：文本模式（Text）

**说明（Help）**

以文本（text）形式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT>
```

**主动选择（Selects）**

```text
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_format_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_format_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Xtensa 模拟器后端（simulator backend） → 后端输出模式（Backend Output Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_BLOCK_IN_THREAD"></a>

## 368.66 `CONFIG_LOG_BLOCK_IN_THREAD`

**提示（Prompt）**：缓冲区满时在线程上下文（thread context）中阻塞

**说明（Help）**

启用后，若日志器内部缓冲区已满、无法为新消息分配空间，日志器在线程上下文（thread context）中会阻塞。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BLOCK_IN_THREAD_TIMEOUT_MS"></a>

## 368.67 `CONFIG_LOG_BLOCK_IN_THREAD_TIMEOUT_MS`

**提示（Prompt）**：线程可阻塞的最长时间（毫秒）

**说明（Help）**

若在该时间内仍无法为日志消息分配新缓冲区，则丢弃消息。可设置永久阻塞（`-1`），但如果用于日志处理的线程，例如日志线程或命令行线程，本身也启用了日志，可能导致日志器死锁（deadlock）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BLOCK_IN_THREAD && CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[-1, 10000]
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing） → 缓冲区满时在线程上下文（thread context）中阻塞

**配置项引用（Symbol References）**：[`CONFIG_LOG_BLOCK_IN_THREAD`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BLOCK_IN_THREAD)、[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_BUFFER_SIZE"></a>

## 368.68 `CONFIG_LOG_BUFFER_SIZE`

**提示（Prompt）**：分配给日志器内部缓冲区的字节数

**说明（Help）**

专用于日志器内部缓冲区（internal buffer）的字节数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[128, 1048576]
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_CMDS"></a>

## 368.69 `CONFIG_LOG_CMDS`

**提示（Prompt）**：命令行命令（Shell Commands）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_CORE_ID_PREFIX"></a>

## 368.70 `CONFIG_LOG_CORE_ID_PREFIX`

**提示（Prompt）**：核心标识前缀（Core ID prefix）

**说明（Help）**

允许在日志消息前添加核心／处理器 ID 前缀。多核心系统可据此识别每条日志由哪个 CPU 核心生成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SMP || CONFIG_MP_MAX_NUM_CPUS > 1) && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_MP_MAX_NUM_CPUS`](P001_kernel_配置项参考_1.md#CONFIG_MP_MAX_NUM_CPUS)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_CORE_INIT_PRIORITY"></a>

## 368.71 `CONFIG_LOG_CORE_INIT_PRIORITY`

**提示（Prompt）**：日志核心初始化优先级（Log Core Initialization Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 99]
```

**定义位置（Location）**：[`subsys/logging/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_CUSTOM_FORMAT_SUPPORT"></a>

## 368.72 `CONFIG_LOG_CUSTOM_FORMAT_SUPPORT`

**提示（Prompt）**：自定义格式支持（Custom format support）

**说明（Help）**

支持自定义格式化器（formatter），允许为日志后端注册自定义格式化回调（callbacks）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_CUSTOM_HEADER"></a>

## 368.73 `CONFIG_LOG_CUSTOM_HEADER`

**提示（Prompt）**：包含自定义日志头文件（Custom Log Header）【实验性 EXPERIMENTAL】

**说明（Help）**

启用后，在 `log.h` 末尾包含由应用提供的自定义头文件 `zephyr_custom_log.h`，从而可在宏级别扩展 `LOG_*` API。请谨慎使用：内部日志 API 可能在未来版本中改变。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_LOG_FRONTEND_STMESP_TURBO_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.mode:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.mode#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_LOG_FRONTEND_STMESP_TURBO_LOG`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_FRONTEND_STMESP_TURBO_LOG)。

<a id="CONFIG_LOG_DBG_COLOR_BLUE"></a>

## 368.74 `CONFIG_LOG_DBG_COLOR_BLUE`

**提示（Prompt）**：调试级别日志使用蓝色（debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_SHOW_COLOR && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → 后端彩色输出（Colors）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SHOW_COLOR`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SHOW_COLOR)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_DEFAULT_LEVEL"></a>

## 368.75 `CONFIG_LOG_DEFAULT_LEVEL`

**提示（Prompt）**：默认日志级别（Default log level）

**说明（Help）**

为没有明确指定日志级别的模块设置默认级别。设为 `0` 时，这些模块不启用日志。各级别为：

- `0`：关闭（OFF），默认不输出。
- `1`：错误（ERROR），默认仅输出 `LOG_LEVEL_ERR`。
- `2`：警告（WARNING），默认输出 `LOG_LEVEL_WRN`。
- `3`：信息（INFO），默认输出 `LOG_LEVEL_INFO`。
- `4`：调试（DEBUG），默认输出 `LOG_LEVEL_DBG`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`subsys/logging/Kconfig.filtering:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.filtering#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 日志级别过滤（Logging levels filtering）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_DICTIONARY_DB_TARGET"></a>

## 368.76 `CONFIG_LOG_DICTIONARY_DB_TARGET`

**提示（Prompt）**：仅通过专用目标生成日志字典数据库

**说明（Help）**

启用后，仅通过日志字典数据库自身的构建目标（build target）生成它。该目标不再属于 `ALL` make 目标，必须额外调用 `log_dict_db_gen`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_DICTIONARY_DB && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_LOG_DICTIONARY_DB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_DICTIONARY_DB)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LOG_DICTIONARY_DB`。

<a id="CONFIG_LOG_DICTIONARY_SUPPORT"></a>

## 368.77 `CONFIG_LOG_DICTIONARY_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用基于字典的日志（dictionary-based logging）支持。这是一种二进制日志方式：输出日志时，将预定义字符串替换为其在已构建二进制映像文件中的地址。若需记录较长的格式字符串，可减少日志输出所需的存储空间。此选项应由后端自动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_DICTIONARY_DB
```

**被选择（Selected by）**

```text
CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY
CONFIG_LOG_FRONTEND_DICT_UART
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_DICTIONARY_DB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_DICTIONARY_DB)、[`CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY)、[`CONFIG_LOG_FRONTEND_DICT_UART`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_DICT_UART)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LOG_DICTIONARY_DB`。

<a id="CONFIG_LOG_DOMAIN_NAME"></a>

## 368.78 `CONFIG_LOG_DOMAIN_NAME`

**提示（Prompt）**：域名称（Domain name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_DOMAIN_NAME_CACHE_ENTRY_COUNT"></a>

## 368.79 `CONFIG_LOG_DOMAIN_NAME_CACHE_ENTRY_COUNT`

**提示（Prompt）**：域名称缓存条目数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MULTIDOMAIN && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MULTIDOMAIN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MULTIDOMAIN)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_DOMAIN_NAME_CACHE_ENTRY_SIZE"></a>

## 368.80 `CONFIG_LOG_DOMAIN_NAME_CACHE_ENTRY_SIZE`

**提示（Prompt）**：域名称缓存槽位大小（cache slot size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MULTIDOMAIN && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MULTIDOMAIN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MULTIDOMAIN)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_DOMAIN_NAME_PREFIX"></a>

## 368.81 `CONFIG_LOG_DOMAIN_NAME_PREFIX`

**提示（Prompt）**：域名称前缀（Domain name prefix）

**说明（Help）**

允许在日志来源（log source）前添加域名称（domain name）前缀。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**被弱选择（Implied by）**

```text
CONFIG_LOG_MULTIDOMAIN
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_MULTIDOMAIN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MULTIDOMAIN)。

<a id="CONFIG_LOG_FAILURE_REPORT_PERIOD"></a>

## 368.82 `CONFIG_LOG_FAILURE_REPORT_PERIOD`

**提示（Prompt）**：故障报告周期（Failure report period，毫秒）

**说明（Help）**

决定故障报告频率。报告包含丢弃消息数量，根据工作模式还可能包含其他信息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MODE_DEFERRED && CONFIG_LOG
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FLUSH_SLEEP_US"></a>

## 368.83 `CONFIG_LOG_FLUSH_SLEEP_US`

**提示（Prompt）**：刷新日志队列时的休眠时间（微秒）

**说明（Help）**

在延迟日志模式（deferred logging mode）下，设置 `log_flush()` 每次循环休眠的时间，单位为微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MODE_DEFERRED && CONFIG_LOG
```

**默认值（Defaults）**

```text
10000
```

**取值范围（Ranges）**

```text
[100, 100000]
```

**定义位置（Location）**：[`subsys/logging/Kconfig.mode:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.mode#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FMT_SECTION"></a>

## 368.84 `CONFIG_LOG_FMT_SECTION`

**提示（Prompt）**：将日志字符串保存在专用段（dedicated section）中

**说明（Help）**

启用后，日志字符串保存在专用内存段（memory section），从而能够从最终二进制文件中移除这些字符串。字典日志（dictionary logging）应使用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**被选择（Selected by）**

```text
CONFIG_LOG_MIPI_SYST_USE_CATALOG
```

**被弱选择（Implied by）**

```text
CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY
CONFIG_LOG_FRONTEND_DICT_UART
CONFIG_LOG_FRONTEND_STMESP_DICT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_MIPI_SYST_USE_CATALOG`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_USE_CATALOG)、[`CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY)、[`CONFIG_LOG_FRONTEND_DICT_UART`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_DICT_UART)、[`CONFIG_LOG_FRONTEND_STMESP_DICT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_FRONTEND_STMESP_DICT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LOG_FRONTEND_STMESP_DICT`。

<a id="CONFIG_LOG_FMT_SECTION_STRIP"></a>

## 368.85 `CONFIG_LOG_FMT_SECTION_STRIP`

**提示（Prompt）**：从二进制文件中剥离日志字符串（Strip log strings）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_DICTIONARY_DB && CONFIG_LOG_FMT_SECTION && CONFIG_LINKER_DEVNULL_SUPPORT && !CONFIG_LOG_ALWAYS_RUNTIME && !CONFIG_LOG_OUTPUT && CONFIG_LOG
```

**弱选择（Implies）**

```text
CONFIG_LINKER_DEVNULL_MEMORY
CONFIG_LOG_FMT_STRING_VALIDATE
```

**被弱选择（Implied by）**

```text
CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY
CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY
CONFIG_LOG_FRONTEND_DICT_UART
CONFIG_LOG_FRONTEND_STMESP_DICT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc） → 将日志字符串保存在专用段（dedicated section）中

**配置项引用（Symbol References）**：[`CONFIG_LOG_DICTIONARY_DB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_DICTIONARY_DB)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LINKER_DEVNULL_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LINKER_DEVNULL_SUPPORT)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LINKER_DEVNULL_MEMORY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_DEVNULL_MEMORY)、[`CONFIG_LOG_FMT_STRING_VALIDATE`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_STRING_VALIDATE)、[`CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_I2C_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_RTT_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_DICTIONARY)、[`CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_DICTIONARY)、[`CONFIG_LOG_FRONTEND_DICT_UART`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_DICT_UART)、[`CONFIG_LOG_FRONTEND_STMESP_DICT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_FRONTEND_STMESP_DICT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LOG_DICTIONARY_DB`、`CONFIG_LINKER_DEVNULL_SUPPORT`、`CONFIG_LOG_FRONTEND_STMESP_DICT`。

<a id="CONFIG_LOG_FMT_STRING_VALIDATE"></a>

## 368.86 `CONFIG_LOG_FMT_STRING_VALIDATE`

**提示（Prompt）**：验证日志字符串（Validate logging strings）

**说明（Help）**

日志字符串不能对字符指针（character pointers）直接使用 `%p`；应先将其转换为其他类型指针，例如 `void *`。启用后，预处理器在编译时检测未转换类型就使用 `%p` 的字符串，并在运行时报告错误。译注：“编译时检测、运行时报告”是原文的表述，此处保留其阶段区别。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**被弱选择（Implied by）**

```text
CONFIG_LOG_FMT_SECTION_STRIP
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)。

<a id="CONFIG_LOG_FRONTEND"></a>

## 368.87 `CONFIG_LOG_FRONTEND`

**提示（Prompt）**：前端（Frontend）

**说明（Help）**

启用后，日志重定向到自定义前端（frontend），这是输出日志最快的方式。此重定向发生在函数级别；若需在宏级别重定向，请参见 `LOG_CUSTOM_HEADER`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.mode:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.mode#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FRONTEND_DICT_UART"></a>

## 368.88 `CONFIG_LOG_FRONTEND_DICT_UART`

**提示（Prompt）**：UART 字典前端（dictionary frontend）

**说明（Help）**

前端以二进制字典模式（binary dictionary mode）发送数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_ASYNC_API || CONFIG_UART_INTERRUPT_DRIVEN) && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_DICTIONARY_SUPPORT
CONFIG_MPSC_PBUF
```

**弱选择（Implies）**

```text
CONFIG_LOG_FMT_SECTION
CONFIG_LOG_FMT_SECTION_STRIP if !CONFIG_LOG_ALWAYS_RUNTIME
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends）

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_DICTIONARY_SUPPORT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DICTIONARY_SUPPORT)、[`CONFIG_MPSC_PBUF`](P197_lib_配置项参考_1.md#CONFIG_MPSC_PBUF)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_FMT_SECTION_STRIP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION_STRIP)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)。

<a id="CONFIG_LOG_FRONTEND_DICT_UART_BUFFER_SIZE"></a>

## 368.89 `CONFIG_LOG_FRONTEND_DICT_UART_BUFFER_SIZE`

**提示（Prompt）**：缓冲区大小（Buffer size）

**说明（Help）**

用于缓冲数据的字节数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_DICT_UART && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → UART 字典前端（dictionary frontend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_DICT_UART`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_DICT_UART)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FRONTEND_DICT_UART_DROPPED_NOTIFY_PERIOD"></a>

## 368.90 `CONFIG_LOG_FRONTEND_DICT_UART_DROPPED_NOTIFY_PERIOD`

**提示（Prompt）**：丢弃通知周期（Dropped notification period）

**说明（Help）**

决定打印消息丢弃报告的频率，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_DICT_UART && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → UART 字典前端（dictionary frontend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_DICT_UART`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_DICT_UART)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FRONTEND_ONLY"></a>

## 368.91 `CONFIG_LOG_FRONTEND_ONLY`

**提示（Prompt）**：无后端（No backends）

**说明（Help）**

表示不打算使用任何后端（backends）。若启用了任意后端，代码会触发断言（assert）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.mode:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.mode#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FRONTEND_OPT_API"></a>

## 368.92 `CONFIG_LOG_FRONTEND_OPT_API`

**提示（Prompt）**：前端优化 API（Frontend optimized API）

**说明（Help）**

启用后，前端实现针对最常见日志消息优化的函数版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**被选择（Selected by）**

```text
CONFIG_LOG_FRONTEND_STMESP_DICT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.mode:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.mode#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_FRONTEND_STMESP_DICT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_FRONTEND_STMESP_DICT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LOG_FRONTEND_STMESP_DICT`。

<a id="CONFIG_LOG_FRONTEND_STMESP"></a>

## 368.93 `CONFIG_LOG_FRONTEND_STMESP`

**提示（Prompt）**：CoreSight 系统跟踪宏单元前端（STM frontend）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_STMESP_ENABLED && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**弱选择（Implies）**

```text
CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK if CONFIG_LOG_FRONTEND_STMESP_FLUSH_COUNT > 0
CONFIG_CBPRINTF_RV32E_USE_DEFAULT_ALIGNMENT if CONFIG_RISCV
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_ON_ENTER_CPU_IDLE_HOOK)、[`CONFIG_LOG_FRONTEND_STMESP_FLUSH_COUNT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP_FLUSH_COUNT)、[`CONFIG_CBPRINTF_RV32E_USE_DEFAULT_ALIGNMENT`](P197_lib_配置项参考_1.md#CONFIG_CBPRINTF_RV32E_USE_DEFAULT_ALIGNMENT)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_LOG_FRONTEND_STMESP_DEMUX"></a>

## 368.94 `CONFIG_LOG_FRONTEND_STMESP_DEMUX`

**提示（Prompt）**：从 STM 数据流中分离日志数据包的解复用器（Demultiplexer）

**说明（Help）**

此模块对编码在 STPv2 流中的消息进行解复用（demultiplex）。消息可能交错，因为它们可能来自多个核心，即不同的主标识（majors）。消息有三类：日志（logging）、跟踪点（tracepoints）和硬件事件（HW events）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_MPSC_PBUF
```

**被选择（Selected by）**

```text
CONFIG_DEBUG_NRF_ETR_DECODE
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MPSC_PBUF`](P197_lib_配置项参考_1.md#CONFIG_MPSC_PBUF)、[`CONFIG_DEBUG_NRF_ETR_DECODE`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_DECODE)。

<a id="CONFIG_LOG_FRONTEND_STMESP_DEMUX_ACTIVE_PACKETS"></a>

## 368.95 `CONFIG_LOG_FRONTEND_STMESP_DEMUX_ACTIVE_PACKETS`

**提示（Prompt）**：活动数据包（Active packets）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_STMESP_DEMUX && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**默认值（Defaults）**

```text
12
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → 从 STM 数据流中分离日志数据包的解复用器（Demultiplexer）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_STMESP_DEMUX`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP_DEMUX)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FRONTEND_STMESP_DEMUX_BUFFER_SIZE"></a>

## 368.96 `CONFIG_LOG_FRONTEND_STMESP_DEMUX_BUFFER_SIZE`

**提示（Prompt）**：缓冲区大小（Buffer size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_STMESP_DEMUX && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → 从 STM 数据流中分离日志数据包的解复用器（Demultiplexer）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_STMESP_DEMUX`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP_DEMUX)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FRONTEND_STMESP_DEMUX_GC_TIMEOUT"></a>

## 368.97 `CONFIG_LOG_FRONTEND_STMESP_DEMUX_GC_TIMEOUT`

**提示（Prompt）**：消息超时（Message timeout，毫秒）

**说明（Help）**

若日志消息未在此时间范围内完成，则丢弃该消息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_STMESP_DEMUX && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → 从 STM 数据流中分离日志数据包的解复用器（Demultiplexer）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_STMESP_DEMUX`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP_DEMUX)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FRONTEND_STMESP_DEMUX_MAX_UTILIZATION"></a>

## 368.98 `CONFIG_LOG_FRONTEND_STMESP_DEMUX_MAX_UTILIZATION`

**提示（Prompt）**：跟踪最大利用率（maximum utilization）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_STMESP_DEMUX && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → 从 STM 数据流中分离日志数据包的解复用器（Demultiplexer）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_STMESP_DEMUX`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP_DEMUX)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FRONTEND_STMESP_EARLY_BUF_SIZE"></a>

## 368.99 `CONFIG_LOG_FRONTEND_STMESP_EARLY_BUF_SIZE`

**提示（Prompt）**：存储早期消息的缓冲区大小

**说明（Help）**

与嵌入式跟踪路由器（ETR）缓冲区配合使用时，只有 ETR 已初始化且内存访问权限（privileges）配置正确，前端才能写入 STM。此前数据保存在缓冲区中，待处理链路（pipeline）就绪后再刷新到 STMESP。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_STMESP && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**默认值（Defaults）**

```text
1024 if CONFIG_DEBUG_NRF_ETR
0
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → CoreSight 系统跟踪宏单元前端（STM frontend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_STMESP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)。

<a id="CONFIG_LOG_FRONTEND_STMESP_FLUSH_COUNT"></a>

## 368.100 `CONFIG_LOG_FRONTEND_STMESP_FLUSH_COUNT`

**提示（Prompt）**：用于刷新的字数（Number of flushing words）

**说明（Help）**

CPU 进入休眠前，应向 STM 写入一些虚拟数据（dummy data），确保所有缓冲数据都传入跟踪端口接口单元（TPIU）或嵌入式跟踪路由器（ETR）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_STMESP && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → CoreSight 系统跟踪宏单元前端（STM frontend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_STMESP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<!-- kconfig-navigation -->

[上一章](P367_subsys_logging_配置项参考_16.md) · [返回大纲](大纲.md) · [下一章](P369_subsys_logging_配置项参考_18.md)
