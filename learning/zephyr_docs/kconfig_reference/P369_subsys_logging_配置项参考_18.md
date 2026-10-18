---
id: learning.zephyr-docs.kconfig-reference.page-369
title: "`subsys/logging`配置项参考（18/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第369章\_`subsys/logging`配置项参考（18/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LOG_FRONTEND_STMESP_FSC"></a>

## 369.1 `CONFIG_LOG_FRONTEND_STMESP_FSC`

**提示（Prompt）**：发送完全自包含的消息（self-contained messages）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_STMESP && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_MSG_APPEND_RO_STRING_LOC if !(CONFIG_DEBUG_NRF_ETR || CONFIG_SOC_NRF54H20_CPUPPR || CONFIG_SOC_NRF54H20_CPUFLPR)
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → CoreSight 系统跟踪宏单元前端（STM frontend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_STMESP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_MSG_APPEND_RO_STRING_LOC`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MSG_APPEND_RO_STRING_LOC)、[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_SOC_NRF54H20_CPUPPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUPPR)、[`CONFIG_SOC_NRF54H20_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUFLPR)。

<a id="CONFIG_LOG_FRONTEND_STMESP_GUARANTEED_ACCESS"></a>

## 369.2 `CONFIG_LOG_FRONTEND_STMESP_GUARANTEED_ACCESS`

**提示（Prompt）**：使用 STMESP 保证型访问（guaranteed access）

**说明（Help）**

启用后，如果无法执行写入，例如 ETR 缓冲区已满，访问 STMESP 寄存器将停顿（stall）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_STMESP && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → CoreSight 系统跟踪宏单元前端（STM frontend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_STMESP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FRONTEND_STMESP_MSG_END_TIMESTAMP"></a>

## 369.3 `CONFIG_LOG_FRONTEND_STMESP_MSG_END_TIMESTAMP`

**提示（Prompt）**：在消息末尾生成时间戳和标记（timestamp and marker）

**说明（Help）**

在消息末尾生成一个带时间戳（timestamp）和标记（marker）的零数据字节，而不是在消息开头生成时间戳和标记、末尾生成标志（flag）。这可用于保持与某些解码器的兼容性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_STMESP && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → CoreSight 系统跟踪宏单元前端（STM frontend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_STMESP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FRONTEND_STMESP_TP_CHAN_BASE"></a>

## 369.4 `CONFIG_LOG_FRONTEND_STMESP_TP_CHAN_BASE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

不要更改此值，因为它与主机解码器 `nrfutil trace` 相匹配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_LOG_FRONTEND_STMESP_DEMUX || CONFIG_LOG_FRONTEND_STMESP) && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**默认值（Defaults）**

```text
255
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_STMESP_DEMUX`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP_DEMUX)、[`CONFIG_LOG_FRONTEND_STMESP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FRONTEND_STMESP_TURBO_DROP_OTHERS"></a>

## 369.5 `CONFIG_LOG_FRONTEND_STMESP_TURBO_DROP_OTHERS`

**提示（Prompt）**：除 turbo 日志外丢弃所有日志

**说明（Help）**

内存受限时可启用此项，移除除 turbo 日志外的所有日志相关代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_STMESP && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → CoreSight 系统跟踪宏单元前端（STM frontend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_STMESP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FRONTEND_STMESP_TURBO_LOG"></a>

## 369.6 `CONFIG_LOG_FRONTEND_STMESP_TURBO_LOG`

**提示（Prompt）**：优化短日志（short_logs）

**说明（Help）**

启用后，对包含 `0` 或 `1` 个数值参数的日志消息进行优化，其处理速度明显快于其他消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_FRONTEND_STMESP && CONFIG_LOG_FRONTEND && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if (CONFIG_DEBUG_NRF_ETR || CONFIG_SOC_NRF54H20_CPUPPR || CONFIG_SOC_NRF54H20_CPUFLPR) && CONFIG_LOG_FRONTEND_STMESP_FSC
```

**主动选择（Selects）**

```text
CONFIG_LOG_CUSTOM_HEADER
```

**定义位置（Location）**：[`subsys/logging/frontends/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 前端（Frontends） → CoreSight 系统跟踪宏单元前端（STM frontend）

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_STMESP`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_STMESP)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DEBUG_NRF_ETR`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR)、[`CONFIG_SOC_NRF54H20_CPUPPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUPPR)、[`CONFIG_SOC_NRF54H20_CPUFLPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_SOC_NRF54H20_CPUFLPR)、[`CONFIG_LOG_FRONTEND_STMESP_FSC`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_FRONTEND_STMESP_FSC)、[`CONFIG_LOG_CUSTOM_HEADER`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_CUSTOM_HEADER)。

<a id="CONFIG_LOG_FUNC_NAME_PREFIX_DBG"></a>

## 369.7 `CONFIG_LOG_FUNC_NAME_PREFIX_DBG`

**提示（Prompt）**：调试消息添加前缀（Debug messages prepended）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → 在非十六进制转储（non-hexdump）日志消息前添加函数名。

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FUNC_NAME_PREFIX_ERR"></a>

## 369.8 `CONFIG_LOG_FUNC_NAME_PREFIX_ERR`

**提示（Prompt）**：错误消息添加前缀（Error messages prepended）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → 在非十六进制转储（non-hexdump）日志消息前添加函数名。

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FUNC_NAME_PREFIX_INF"></a>

## 369.9 `CONFIG_LOG_FUNC_NAME_PREFIX_INF`

**提示（Prompt）**：信息消息添加前缀（Info messages prepended）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → 在非十六进制转储（non-hexdump）日志消息前添加函数名。

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_FUNC_NAME_PREFIX_WRN"></a>

## 369.10 `CONFIG_LOG_FUNC_NAME_PREFIX_WRN`

**提示（Prompt）**：警告消息添加前缀（Warning messages prepended）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → 在非十六进制转储（non-hexdump）日志消息前添加函数名。

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_IMMEDIATE_CLEAN_OUTPUT"></a>

## 369.11 `CONFIG_LOG_IMMEDIATE_CLEAN_OUTPUT`

**提示（Prompt）**：避免交错的日志输出（Clean log output）

**说明（Help）**

启用后，在整条日志消息处理期间锁定中断，防止一条日志消息的处理被另一条打断，从而使输出不交错。不过，这会导致中断被锁定较长时间，可能达到数毫秒。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MODE_IMMEDIATE && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_IMMEDIATE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_IMMEDIATE)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_INFO_COLOR_GREEN"></a>

## 369.12 `CONFIG_LOG_INFO_COLOR_GREEN`

**提示（Prompt）**：信息级别日志使用绿色（info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_SHOW_COLOR && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → 后端彩色输出（Colors）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_SHOW_COLOR`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SHOW_COLOR)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_LINK_IPC_SERVICE"></a>

## 369.13 `CONFIG_LOG_LINK_IPC_SERVICE`

**提示（Prompt）**：处理器间通信服务链路（IPC service link）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MULTIDOMAIN && CONFIG_LOG_MULTIDOMAIN && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_MULTIDOMAIN_LINK
```

**定义位置（Location）**：[`subsys/logging/Kconfig.links:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.links#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LOG_MULTIDOMAIN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MULTIDOMAIN)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_MULTIDOMAIN_LINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MULTIDOMAIN_LINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LOG_MULTIDOMAIN_LINK`。

<a id="CONFIG_LOG_LINK_IPC_SERVICE_BUFFER_SIZE"></a>

## 369.14 `CONFIG_LOG_LINK_IPC_SERVICE_BUFFER_SIZE`

**提示（Prompt）**：专用缓冲区大小（Dedicated buffer size）

**说明（Help）**

专用缓冲区用于维持已处理消息的顺序。设为 `0` 时，使用主缓冲区，按到达顺序处理消息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_LINK_IPC_SERVICE && CONFIG_LOG_MULTIDOMAIN && CONFIG_LOG
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/logging/Kconfig.links:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.links#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理器间通信服务链路（IPC service link）

**配置项引用（Symbol References）**：[`CONFIG_LOG_LINK_IPC_SERVICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_LINK_IPC_SERVICE)、[`CONFIG_LOG_MULTIDOMAIN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MULTIDOMAIN)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_MAX_LEVEL"></a>

## 369.15 `CONFIG_LOG_MAX_LEVEL`

**提示（Prompt）**：系统编译纳入的最高日志级别（Maximal log level）

**说明（Help）**

为所有模块强制指定最高日志级别。原文说明：模块指定的级别若高于此值，则限制到此值；否则，模块使用本选项的级别，代替其默认级别或手动设置的级别。各级别如下：

- `0`：关闭（OFF），关闭日志。
- `1`：错误（ERROR），最高级别为 `LOG_LEVEL_ERR`。
- `2`：警告（WARNING），最高级别为 `LOG_LEVEL_WRN`。
- `3`：信息（INFO），最高级别为 `LOG_LEVEL_INFO`。
- `4`：调试（DEBUG），最高级别为 `LOG_LEVEL_DBG`。

译注：此处保留原文对高于和未高于配置值两种情形的描述；不可将其直接等同于运行时日志过滤。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`subsys/logging/Kconfig.filtering:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.filtering#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 日志级别过滤（Logging levels filtering）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_MEM_UTILIZATION"></a>

## 369.16 `CONFIG_LOG_MEM_UTILIZATION`

**提示（Prompt）**：跟踪最大内存使用量（maximum memory utilization）

**说明（Help）**

启用后，跟踪延迟模式（deferred mode）下日志消息占用内存的峰值，以便调整并减小 `LOG_BUFFER_SIZE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MODE_DEFERRED && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if CONFIG_LOG_CMDS
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_CMDS`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_CMDS)。

<a id="CONFIG_LOG_MIPI_SYST_ARGS_BUFFER_SIZE"></a>

## 369.17 `CONFIG_LOG_MIPI_SYST_ARGS_BUFFER_SIZE`

**提示（Prompt）**：缓冲区大小，单位为字节。

**说明（Help）**

用户可配置本项，指定 MIPI Sys-T 库处理日志格式字符串时，在调用栈（call stack）中预留的最大字节数。增大此值可记录更长字符串，但增加栈占用；减小则降低栈负担，但限制日志字符串的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → MIPI SyS-T 格式输出（format output）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_MIPI_SYST_CATALOG_ARGS_BUFFER_SIZE"></a>

## 369.18 `CONFIG_LOG_MIPI_SYST_CATALOG_ARGS_BUFFER_SIZE`

**提示（Prompt）**：使用 Sys-T 目录（Catalog）时的临时参数缓冲区大小

**说明（Help）**

临时缓冲区大小，单位为字节，用于保存 MIPI Sys-T 库处理目录消息（catalog messages）所需的展开参数列表（expanded argument list）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_USE_CATALOG && CONFIG_LOG_MIPI_SYST_ENABLE && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → MIPI SyS-T 格式输出（format output）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_USE_CATALOG`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_USE_CATALOG)、[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_MIPI_SYST_DISABLE_TIMESTAMP"></a>

## 369.19 `CONFIG_LOG_MIPI_SYST_DISABLE_TIMESTAMP`

**提示（Prompt）**：禁用 MIPI Sys-T 协议时间戳（timestamp）

**说明（Help）**

从 MIPI Sys-T 协议中移除时间戳（timestamp）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → MIPI SyS-T 格式输出（format output）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_MIPI_SYST_ENABLE"></a>

## 369.20 `CONFIG_LOG_MIPI_SYST_ENABLE`

**提示（Prompt）**：MIPI SyS-T 格式输出（format output）

**说明（Help）**

为日志系统启用 MIPI SyS-T 格式输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_MIPI_SYST_LIB
CONFIG_LOG_OUTPUT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MIPI_SYST_LIB`](P214_modules_Kconfig.syst_配置项参考.md#CONFIG_MIPI_SYST_LIB)、[`CONFIG_LOG_OUTPUT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_OUTPUT)。

<a id="CONFIG_LOG_MIPI_SYST_MSG_DEFAULT_MODULE_ID"></a>

## 369.21 `CONFIG_LOG_MIPI_SYST_MSG_DEFAULT_MODULE_ID`

**提示（Prompt）**：Sys-T 消息中的默认模块 ID（module ID）

**说明（Help）**

嵌入 Sys-T 消息头来源单元（origin unit）的默认模块 ID。若禁用 `CONFIG_LOG_MIPI_SYST_OUTPUT_LOG_MSG_SRC_ID`，所有 Sys-T 消息均使用该值；若启用，则只用于没有来源 ID 的日志消息，例如启用 `CONFIG_LOG_PRINTK` 后的 `printk()` 消息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
127 if CONFIG_LOG_MIPI_SYST_OUTPUT_LOG_MSG_SRC_ID
0
```

**取值范围（Ranges）**

```text
[0, 127]
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → MIPI SyS-T 格式输出（format output）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_MIPI_SYST_OUTPUT_LOG_MSG_SRC_ID`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_OUTPUT_LOG_MSG_SRC_ID)。

<a id="CONFIG_LOG_MIPI_SYST_MSG_DEFAULT_UNIT_ID"></a>

## 369.22 `CONFIG_LOG_MIPI_SYST_MSG_DEFAULT_UNIT_ID`

**提示（Prompt）**：Sys-T 消息中的默认单元 ID（unit ID）

**说明（Help）**

嵌入 Sys-T 消息头来源单元（origin unit）的默认单元 ID。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → MIPI SyS-T 格式输出（format output）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_MIPI_SYST_OUTPUT_LOG_MSG_SRC_ID"></a>

## 369.23 `CONFIG_LOG_MIPI_SYST_OUTPUT_LOG_MSG_SRC_ID`

**提示（Prompt）**：将日志消息来源 ID 作为模块 ID 输出

**说明（Help）**

启用后，将日志消息来源 ID（source ID）作为 Sys-T 消息模块 ID（module ID）输出，即消息头来源单元（origin unit）中的模块 ID。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MIPI_SYST_ENABLE && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if CONFIG_LOG_MIPI_SYST_USE_CATALOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → MIPI SyS-T 格式输出（format output）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_MIPI_SYST_USE_CATALOG`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_USE_CATALOG)。

<a id="CONFIG_LOG_MIPI_SYST_USE_CATALOG"></a>

## 369.24 `CONFIG_LOG_MIPI_SYST_USE_CATALOG`

**提示（Prompt）**：使用 MIPI Sys-T 目录（Catalog）记录日志

**说明（Help）**

使用 MIPI Sys-T 目录（Catalog）记录日志，而不是纯文本（plain text）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PICOLIBC && CONFIG_LOG_MIPI_SYST_ENABLE && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_FMT_SECTION
CONFIG_LOG_USE_TAGGED_ARGUMENTS
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → MIPI SyS-T 格式输出（format output）

**配置项引用（Symbol References）**：[`CONFIG_PICOLIBC`](P198_lib_配置项参考_2.md#CONFIG_PICOLIBC)、[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_FMT_SECTION`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FMT_SECTION)、[`CONFIG_LOG_USE_TAGGED_ARGUMENTS`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_USE_TAGGED_ARGUMENTS)。

<a id="CONFIG_LOG_MODE"></a>

## 369.25 `CONFIG_LOG_MODE`

**提示（Prompt）**：模式（Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_FRONTEND_ONLY && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_MODE_IMMEDIATE if CONFIG_ARCH_POSIX
CONFIG_LOG_MODE_MINIMAL if CONFIG_LOG_DEFAULT_MINIMAL
CONFIG_LOG_MODE_DEFERRED
```

**可选项（Choices）**

```text
CONFIG_LOG_MODE_DEFERRED
CONFIG_LOG_MODE_IMMEDIATE
CONFIG_LOG_MODE_MINIMAL
```

**定义位置（Location）**：[`subsys/logging/Kconfig.mode:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.mode#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_MODE_IMMEDIATE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_IMMEDIATE)、[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG_DEFAULT_MINIMAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_DEFAULT_MINIMAL)、[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LOG_DEFAULT_MINIMAL`。

<a id="CONFIG_LOG_MODE_DEFERRED"></a>

## 369.26 `CONFIG_LOG_MODE_DEFERRED`

**提示（Prompt）**：延迟日志（Deferred logging）

**说明（Help）**

先缓冲日志消息，稍后处理。这种模式对应用影响最小，将耗时处理推迟到已知上下文（context）执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_MODE>
```

**主动选择（Selects）**

```text
CONFIG_MPSC_PBUF
```

**定义位置（Location）**：[`subsys/logging/Kconfig.mode:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.mode#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 模式（Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE)、[`CONFIG_MPSC_PBUF`](P197_lib_配置项参考_1.md#CONFIG_MPSC_PBUF)。

<a id="CONFIG_LOG_MODE_IMMEDIATE"></a>

## 369.27 `CONFIG_LOG_MODE_IMMEDIATE`

**提示（Prompt）**：同步模式（Synchronous）

**说明（Help）**

启用后，在日志调用所在上下文（context）中处理日志。由于耗时操作在日志产生的位置执行，例如高优先级中断内，会影响系统性能。某次日志操作可能被更高优先级上下文中的另一日志操作中断，因此日志后端必须支持独占访问（exclusive access），才能在此模式下正常工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_MODE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.mode:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.mode#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 模式（Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE)。

<a id="CONFIG_LOG_MODE_MINIMAL"></a>

## 369.28 `CONFIG_LOG_MODE_MINIMAL`

**提示（Prompt）**：最小占用模式（Minimal-footprint）

**说明（Help）**

启用最小日志实现。对于标准日志宏，它在 `printk()` 实现之上只增加极少的空间开销。也支持十六进制转储（hexdump）宏，使用时会链接少量额外代码。支持构建时过滤（build time filtering），不支持运行时过滤；没有时间戳、前缀、颜色或异步日志，所有消息均直接发送给 `printk()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_MODE>
```

**主动选择（Selects）**

```text
CONFIG_PRINTK
```

**定义位置（Location）**：[`subsys/logging/Kconfig.mode:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.mode#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 模式（Mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE)、[`CONFIG_PRINTK`](P338_subsys_debug_配置项参考.md#CONFIG_PRINTK)。

<a id="CONFIG_LOG_MODE_OVERFLOW"></a>

## 369.29 `CONFIG_LOG_MODE_OVERFLOW`

**提示（Prompt）**：缓冲区满时丢弃最旧消息

**说明（Help）**

启用后，若没有空间记录新消息，则丢弃最旧消息；禁用时则丢弃当前消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_MSG_APPEND_RO_STRING_LOC"></a>

## 369.30 `CONFIG_LOG_MSG_APPEND_RO_STRING_LOC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

强制日志消息始终在数据包（package）中附加只读字符串参数的位置。需要此功能的后端应选择本项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**被选择（Selected by）**

```text
CONFIG_LOG_MULTIDOMAIN_BACKEND
CONFIG_LOG_FRONTEND_STMESP_FSC
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_MULTIDOMAIN_BACKEND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MULTIDOMAIN_BACKEND)、[`CONFIG_LOG_FRONTEND_STMESP_FSC`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_FRONTEND_STMESP_FSC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LOG_MULTIDOMAIN_BACKEND`。

<a id="CONFIG_LOG_MULTIDOMAIN"></a>

## 369.31 `CONFIG_LOG_MULTIDOMAIN`

**提示（Prompt）**：多域日志器（Multi-domain logger）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_TIMESTAMP_64BIT
```

**弱选择（Implies）**

```text
CONFIG_LOG_DOMAIN_NAME_PREFIX
```

**定义位置（Location）**：[`subsys/logging/Kconfig.mode:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.mode#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_TIMESTAMP_64BIT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_TIMESTAMP_64BIT)、[`CONFIG_LOG_DOMAIN_NAME_PREFIX`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DOMAIN_NAME_PREFIX)。

<a id="CONFIG_LOG_MULTI_SLOT"></a>

## 369.32 `CONFIG_LOG_MULTI_SLOT`

**提示（Prompt）**：每个核心使用独立调试窗口槽位记录 mtrace 日志

**说明（Help）**

启用后，每个 CPU 核心都有独立的调试窗口槽位（debug window slot）用于 mtrace 日志，使主机能够从不同内存窗口槽位读取各核心日志数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP && CONFIG_INTEL_ADSP_DEBUG_SLOT_MANAGER && CONFIG_LOG_CORE_ID_PREFIX && CONFIG_LOG_BACKEND_ADSP_MTRACE && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.adsp_mtrace:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.adsp_mtrace#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Intel ADSP mtrace 后端

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_INTEL_ADSP_DEBUG_SLOT_MANAGER`](P281_soc_intel_配置项参考.md#CONFIG_INTEL_ADSP_DEBUG_SLOT_MANAGER)、[`CONFIG_LOG_CORE_ID_PREFIX`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_CORE_ID_PREFIX)、[`CONFIG_LOG_BACKEND_ADSP_MTRACE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_OUTPUT"></a>

## 369.33 `CONFIG_LOG_OUTPUT`

**提示（Prompt）**：格式化辅助模块（Formatter helper）

**说明（Help）**

将日志消息格式化为便于阅读的字符串的模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_LOG_BACKEND_I2C
CONFIG_LOG_BACKEND_I2C_OUTPUT_TEXT
CONFIG_DEBUG_NRF_ETR_DECODE
CONFIG_BT_MONITOR
CONFIG_LOG_MIPI_SYST_ENABLE
CONFIG_LOG_BACKEND_ADSP_OUTPUT_TEXT
CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_TEXT
CONFIG_LOG_BACKEND_BLE_OUTPUT_TEXT
CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_TEXT
CONFIG_LOG_BACKEND_FS_OUTPUT_TEXT
CONFIG_LOG_BACKEND_MQTT_OUTPUT_TEXT
CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_TEXT
CONFIG_LOG_BACKEND_NET_OUTPUT_TEXT
CONFIG_LOG_BACKEND_WS
CONFIG_LOG_BACKEND_WS_OUTPUT_TEXT
CONFIG_LOG_BACKEND_RTT_OUTPUT_TEXT
CONFIG_LOG_BACKEND_SPINEL_OUTPUT_TEXT
CONFIG_LOG_BACKEND_SWO_OUTPUT_TEXT
CONFIG_LOG_BACKEND_UART_OUTPUT_TEXT
CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_TEXT
CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_TEXT
CONFIG_SHELL_LOG_BACKEND
```

**定义位置（Location）**：[`subsys/logging/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_I2C`](P011_module_hal_intel_zephyr_配置项参考.md#CONFIG_LOG_BACKEND_I2C)、[`CONFIG_LOG_BACKEND_I2C_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_I2C_OUTPUT_TEXT)、[`CONFIG_DEBUG_NRF_ETR_DECODE`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_DECODE)、[`CONFIG_BT_MONITOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MONITOR)、[`CONFIG_LOG_MIPI_SYST_ENABLE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_ENABLE)、[`CONFIG_LOG_BACKEND_ADSP_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_BLE_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_BLE_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_EFI_CON_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_FS_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_MQTT_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_MQTT_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NATIVE_POSIX_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_NET_OUTPUT_TEXT`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_WS`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS)、[`CONFIG_LOG_BACKEND_WS_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_WS_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_RTT_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_RTT_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_SPINEL_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SPINEL_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_SWO_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SWO_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_UART_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_UART_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_XTENSA_SIM_OUTPUT_TEXT)、[`CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_TEXT`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_BACKEND_SEMIHOST_OUTPUT_TEXT)、[`CONFIG_SHELL_LOG_BACKEND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_LOG_BACKEND)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MONITOR`。

<a id="CONFIG_LOG_OUTPUT_FORMAT_CUSTOM_TIMESTAMP"></a>

## 369.34 `CONFIG_LOG_OUTPUT_FORMAT_CUSTOM_TIMESTAMP`

**提示（Prompt）**：自定义时间戳格式支持（Custom timestamp format）

**说明（Help）**

支持自定义时间戳格式化器（formatter），适用于除 syslog 网络后端以外的所有后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → 时间戳格式模式（Timestamp format mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE)。

<a id="CONFIG_LOG_OUTPUT_FORMAT_DATE_TIMESTAMP"></a>

## 369.35 `CONFIG_LOG_OUTPUT_FORMAT_DATE_TIMESTAMP`

**提示（Prompt）**：将时间戳格式化为日期格式（date format）

**说明（Help）**

启用后，时间戳格式为 `YYYY-MM-DD hh:mm:ss.ms,us`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_C_LANG_SUPPORT_R && <choice CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → 时间戳格式模式（Timestamp format mode）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_C_LANG_SUPPORT_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_C_LANG_SUPPORT_R)、[`CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE)。

<a id="CONFIG_LOG_OUTPUT_FORMAT_ISO8601_TIMESTAMP"></a>

## 369.36 `CONFIG_LOG_OUTPUT_FORMAT_ISO8601_TIMESTAMP`

**提示（Prompt）**：将时间戳格式化为 ISO 8601 格式

**说明（Help）**

启用后，时间戳格式为 `YYYY-MM-DDThh:mm:ss,ffffffZ`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_C_LANG_SUPPORT_R && <choice CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:220`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L220)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → 时间戳格式模式（Timestamp format mode）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_C_LANG_SUPPORT_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_C_LANG_SUPPORT_R)、[`CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE)。

<a id="CONFIG_LOG_OUTPUT_FORMAT_LINUX_TIMESTAMP"></a>

## 369.37 `CONFIG_LOG_OUTPUT_FORMAT_LINUX_TIMESTAMP`

**提示（Prompt）**：将时间戳格式化为 Linux 格式

**说明（Help）**

此格式介于纯原始格式（raw format）与 `hh:mm:ss:ms,us` 格式之间，类似 Linux 内核格式：时间戳打印为定点数（fixed point values），小数点左侧为秒，右侧为微秒。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:226`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L226)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → 时间戳格式模式（Timestamp format mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE)。

<a id="CONFIG_LOG_OUTPUT_FORMAT_TIME_TIMESTAMP"></a>

## 369.38 `CONFIG_LOG_OUTPUT_FORMAT_TIME_TIMESTAMP`

**提示（Prompt）**：将时间戳格式化为时间格式（time format）

**说明（Help）**

启用后，时间戳格式为 `hh:mm:ss.ms,us`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L209)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting） → 时间戳格式模式（Timestamp format mode）

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP_MODE)。

<a id="CONFIG_LOG_OVERRIDE_LEVEL"></a>

## 369.39 `CONFIG_LOG_OVERRIDE_LEVEL`

**提示（Prompt）**：覆盖最低日志级别（lowest log level）

**说明（Help）**

为所有模块强制指定最低日志级别。模块明确指定的级别若高于本项，则保留该级别；否则，使用本项指定级别，替代默认级别或手动设置。各级别为：

- `0`：关闭（OFF），不覆盖。
- `1`：错误（ERROR），覆盖为输出 `LOG_LEVEL_ERR`。
- `2`：警告（WARNING），覆盖为输出 `LOG_LEVEL_WRN`。
- `3`：信息（INFO），覆盖为输出 `LOG_LEVEL_INFO`。
- `4`：调试（DEBUG），覆盖为输出 `LOG_LEVEL_DBG`。

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
[0, 4]
```

**定义位置（Location）**：[`subsys/logging/Kconfig.filtering:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.filtering#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 日志级别过滤（Logging levels filtering）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_PRINTK"></a>

## 369.40 `CONFIG_LOG_PRINTK`

**提示（Prompt）**：处理 printk 消息

**说明（Help）**

启用后，将 `printk` 消息重定向到日志子系统（logging subsystem）。消息在调用处完成格式化，并无条件记录。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if CONFIG_PRINTK
```

**被选择（Selected by）**

```text
CONFIG_LOG_BACKEND_RTT_FORCE_PRINTK
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_PRINTK`](P338_subsys_debug_配置项参考.md#CONFIG_PRINTK)、[`CONFIG_LOG_BACKEND_RTT_FORCE_PRINTK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_RTT_FORCE_PRINTK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LOG_BACKEND_RTT_FORCE_PRINTK`。

<a id="CONFIG_LOG_PRINTK_STATIC"></a>

## 369.41 `CONFIG_LOG_PRINTK_STATIC`

**提示（Prompt）**：静态处理 printk 消息（Static processing）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_PRINTK && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing） → 处理 printk 消息

**配置项引用（Symbol References）**：[`CONFIG_LOG_PRINTK`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_PRINTK)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_PROCESSING_LATENCY_US"></a>

## 369.42 `CONFIG_LOG_PROCESSING_LATENCY_US`

**提示（Prompt）**：远程消息最大延迟（微秒，remote message latency）

**说明（Help）**

指定远程域（remote domain）创建日志消息到本地域（local domain）处理该消息之间预留的时间。较大的值增加消息处理延迟，但也提高保持消息正确顺序的机会。仅在链路（links）为远程消息使用专用缓冲区时使用此项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MULTIDOMAIN && CONFIG_LOG_PROCESS_THREAD && CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
100000
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing） → 使用内部线程处理日志

**配置项引用（Symbol References）**：[`CONFIG_LOG_MULTIDOMAIN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MULTIDOMAIN)、[`CONFIG_LOG_PROCESS_THREAD`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_PROCESS_THREAD)、[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_PROCESS_THREAD"></a>

## 369.43 `CONFIG_LOG_PROCESS_THREAD`

**提示（Prompt）**：使用内部线程处理日志

**说明（Help）**

启用后，日志子系统创建处理线程。线程会定期唤醒，见 `LOG_PROCESS_THREAD_SLEEP_MS`；当缓冲消息数量超过阈值时也会唤醒，见 `LOG_PROCESS_TRIGGER_THR`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_PROCESS_THREAD_CUSTOM_PRIORITY"></a>

## 369.44 `CONFIG_LOG_PROCESS_THREAD_CUSTOM_PRIORITY`

**提示（Prompt）**：自定义日志线程优先级（thread priority）

**说明（Help）**

为日志处理线程设置自定义优先级值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_PROCESS_THREAD && CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing） → 使用内部线程处理日志

**配置项引用（Symbol References）**：[`CONFIG_LOG_PROCESS_THREAD`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_PROCESS_THREAD)、[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_PROCESS_THREAD_PRIORITY"></a>

## 369.45 `CONFIG_LOG_PROCESS_THREAD_PRIORITY`

**提示（Prompt）**：日志处理线程优先级（priority）

**说明（Help）**

日志处理线程的优先级。未设置时，使用 `K_LOWEST_APPLICATION_THREAD_PRIO`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_PROCESS_THREAD_CUSTOM_PRIORITY && CONFIG_LOG_PROCESS_THREAD && CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing） → 使用内部线程处理日志 → 自定义日志线程优先级（thread priority）

**配置项引用（Symbol References）**：[`CONFIG_LOG_PROCESS_THREAD_CUSTOM_PRIORITY`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_PROCESS_THREAD_CUSTOM_PRIORITY)、[`CONFIG_LOG_PROCESS_THREAD`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_PROCESS_THREAD)、[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_PROCESS_THREAD_SLEEP_MS"></a>

## 369.46 `CONFIG_LOG_PROCESS_THREAD_SLEEP_MS`

**提示（Prompt）**：设置内部日志处理线程的休眠周期

**说明（Help）**

日志处理线程休眠指定时间，单位为毫秒。唤醒后，处理所有已缓冲消息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_PROCESS_THREAD && CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing） → 使用内部线程处理日志

**配置项引用（Symbol References）**：[`CONFIG_LOG_PROCESS_THREAD`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_PROCESS_THREAD)、[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_PROCESS_THREAD_STACK_SIZE"></a>

## 369.47 `CONFIG_LOG_PROCESS_THREAD_STACK_SIZE`

**提示（Prompt）**：内部日志处理线程的栈大小（stack size）

**说明（Help）**

设置日志处理线程的内部栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_PROCESS_THREAD && CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
4096 if CONFIG_X86 && CONFIG_X86_64
4096 if CONFIG_ARM64
4096 if CONFIG_ARC && CONFIG_64BIT
4096 if CONFIG_SPARC
2048 if CONFIG_COVERAGE_GCOV
2048 if CONFIG_RISCV && CONFIG_64BIT
2048 if CONFIG_LOG_BACKEND_FS
1152 if CONFIG_LOG_BACKEND_NET
4096 if CONFIG_NO_OPTIMIZATIONS
1024 if CONFIG_XTENSA
2048 if CONFIG_ASSERT || CONFIG_SPIN_VALIDATE
768
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing） → 使用内部线程处理日志

**配置项引用（Symbol References）**：[`CONFIG_LOG_PROCESS_THREAD`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_PROCESS_THREAD)、[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ARC`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARC)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)、[`CONFIG_SPARC`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SPARC)、[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_LOG_BACKEND_FS`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_FS)、[`CONFIG_LOG_BACKEND_NET`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_NET)、[`CONFIG_NO_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NO_OPTIMIZATIONS)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_ASSERT`](P338_subsys_debug_配置项参考.md#CONFIG_ASSERT)、[`CONFIG_SPIN_VALIDATE`](P338_subsys_debug_配置项参考.md#CONFIG_SPIN_VALIDATE)。

<a id="CONFIG_LOG_PROCESS_THREAD_STARTUP_DELAY_MS"></a>

## 369.48 `CONFIG_LOG_PROCESS_THREAD_STARTUP_DELAY_MS`

**提示（Prompt）**：设置日志处理线程的启动延迟

**说明（Help）**

日志处理线程在指定延迟后启动，单位为毫秒。启动后，处理所有已缓冲消息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_PROCESS_THREAD && CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing） → 使用内部线程处理日志

**配置项引用（Symbol References）**：[`CONFIG_LOG_PROCESS_THREAD`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_PROCESS_THREAD)、[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD"></a>

## 369.49 `CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD`

**提示（Prompt）**：触发刷新前缓冲的日志消息数量

**说明（Help）**

缓冲消息数量达到阈值（threshold）时唤醒线程。日志初始化时提供日志处理线程 ID。设为 `0` 可禁用此功能。若启用 `LOG_PROCESS_THREAD`，则内部线程使用此阈值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_RATELIMIT"></a>

## 369.50 `CONFIG_LOG_RATELIMIT`

**提示（Prompt）**：速率受限日志宏（Rate-limited logging macros）

**说明（Help）**

启用后，提供速率受限日志宏（rate-limited logging macros），避免频繁生成消息时日志泛滥。限制按宏调用位置（macro call site）分别计算，每个独立调用位置都有自己的速率限制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_RATELIMIT_FALLBACK"></a>

## 369.51 `CONFIG_LOG_RATELIMIT_FALLBACK`

**提示（Prompt）**：速率受限日志宏的回退行为（Fallback behavior）

**说明（Help）**

选择禁用 `LOG_RATELIMIT` 时速率受限日志宏的回退行为：

- “记录全部输出（Log all prints）”：输出所有日志，忽略速率限制。
- “丢弃全部输出（Drop all prints）”：丢弃所有通过速率受限宏产生的日志。

这样可控制在速率限制不可用时，这些宏始终输出，还是完全被抑制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_RATELIMIT && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_RATELIMIT_FALLBACK_DROP
```

**可选项（Choices）**

```text
CONFIG_LOG_RATELIMIT_FALLBACK_LOG
CONFIG_LOG_RATELIMIT_FALLBACK_DROP
```

**定义位置（Location）**：[`subsys/logging/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LOG_RATELIMIT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_RATELIMIT)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_RATELIMIT_FALLBACK_DROP`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_RATELIMIT_FALLBACK_DROP)、[`CONFIG_LOG_RATELIMIT_FALLBACK_LOG`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_RATELIMIT_FALLBACK_LOG)。

<a id="CONFIG_LOG_RATELIMIT_FALLBACK_DROP"></a>

## 369.52 `CONFIG_LOG_RATELIMIT_FALLBACK_DROP`

**提示（Prompt）**：丢弃全部输出（Drop all prints）

**说明（Help）**

丢弃所有通过速率受限日志宏（rate-limited macros）产生的日志，不产生输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_RATELIMIT_FALLBACK>
```

**定义位置（Location）**：[`subsys/logging/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 速率受限日志宏的回退行为（Fallback behavior）

**配置项引用（Symbol References）**：[`CONFIG_LOG_RATELIMIT_FALLBACK`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_RATELIMIT_FALLBACK)。

<a id="CONFIG_LOG_RATELIMIT_FALLBACK_LOG"></a>

## 369.53 `CONFIG_LOG_RATELIMIT_FALLBACK_LOG`

**提示（Prompt）**：记录全部输出，忽略速率限制（Log all prints）

**说明（Help）**

所有通过速率受限日志宏（rate-limited macros）产生的日志都按普通日志输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOG_RATELIMIT_FALLBACK>
```

**定义位置（Location）**：[`subsys/logging/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 速率受限日志宏的回退行为（Fallback behavior）

**配置项引用（Symbol References）**：[`CONFIG_LOG_RATELIMIT_FALLBACK`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_RATELIMIT_FALLBACK)。

<a id="CONFIG_LOG_RATELIMIT_INTERVAL_MS"></a>

## 369.54 `CONFIG_LOG_RATELIMIT_INTERVAL_MS`

**提示（Prompt）**：默认速率限制间隔（毫秒，rate limit interval）

**说明（Help）**

速率受限日志消息之间的默认间隔。未显式指定速率时，便捷宏 `LOG_*_RATELIMIT` 使用此值。可在各调用处使用 `LOG_*_RATELIMIT_RATE` 宏覆盖。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_RATELIMIT && CONFIG_LOG
```

**默认值（Defaults）**

```text
5000
```

**取值范围（Ranges）**

```text
[100, 60000]
```

**定义位置（Location）**：[`subsys/logging/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 速率受限日志宏（Rate-limited logging macros）

**配置项引用（Symbol References）**：[`CONFIG_LOG_RATELIMIT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_RATELIMIT)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_REMOTE_DOMAIN_MAX_COUNT"></a>

## 369.55 `CONFIG_LOG_REMOTE_DOMAIN_MAX_COUNT`

**提示（Prompt）**：链路域数量上限（Maximum number of link domains）

**说明（Help）**

一条链路（link）能够处理的域（domains）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MULTIDOMAIN && CONFIG_LOG
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MULTIDOMAIN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MULTIDOMAIN)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_RUNTIME_DEFAULT_LEVEL"></a>

## 369.56 `CONFIG_LOG_RUNTIME_DEFAULT_LEVEL`

**提示（Prompt）**：启动时默认运行时日志级别（runtime log level）

**说明（Help）**

设置系统启动时所有模块的初始运行时过滤级别（runtime filter level），在配置任何后端过滤或应用专用过滤之前应用。用于在通过 IPC 等机制动态重配置之前，控制启动阶段的日志详细程度。各级别为：

- `0`：关闭（OFF），启动时不输出日志。
- `1`：错误（ERROR），启动时仅显示错误。
- `2`：警告（WARNING），启动时显示错误和警告。
- `3`：信息（INFO），启动时显示信息及更严重级别的日志。
- `4`：调试（DEBUG），启动时显示全部日志，包括调试日志。

注意：此项仅影响运行时过滤。编译时日志级别由 `CONFIG_LOG_MAX_LEVEL` 及各模块设置控制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_RUNTIME_FILTERING && CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_LOG_DEFAULT_LEVEL
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`subsys/logging/Kconfig.filtering:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.filtering#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 日志级别过滤（Logging levels filtering） → 运行时过滤重配置（Runtime filtering reconfiguration）

**配置项引用（Symbol References）**：[`CONFIG_LOG_RUNTIME_FILTERING`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_RUNTIME_FILTERING)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_DEFAULT_LEVEL`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_DEFAULT_LEVEL)。

<a id="CONFIG_LOG_RUNTIME_FILTERING"></a>

## 369.57 `CONFIG_LOG_RUNTIME_FILTERING`

**提示（Prompt）**：运行时过滤重配置（Runtime filtering reconfiguration）

**说明（Help）**

允许在运行时为实例（instance）独立配置最高严重性级别（severity level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**被弱选择（Implied by）**

```text
CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/logging/Kconfig.filtering:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.filtering#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 日志级别过滤（Logging levels filtering）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)。

<a id="CONFIG_LOG_SIMPLE_MSG_OPTIMIZE"></a>

## 369.58 `CONFIG_LOG_SIMPLE_MSG_OPTIMIZE`

**提示（Prompt）**：针对代码大小优化简单消息（simple messages）

**说明（Help）**

提供专用代码，处理带 `0`～`2` 个 32 位字参数的简单日志消息。应用中约 70%～80% 的日志消息属于此类。根据体系结构不同，代码大小可减少 0%～40%，观察到的最高值出现在 RISCV32；执行时间也可最多减少 40%。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_64BIT && !CONFIG_CBPRINTF_PACKAGE_HEADER_STORE_CREATION_FLAGS && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)、[`CONFIG_CBPRINTF_PACKAGE_HEADER_STORE_CREATION_FLAGS`](P197_lib_配置项参考_1.md#CONFIG_CBPRINTF_PACKAGE_HEADER_STORE_CREATION_FLAGS)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_SOURCE_NAME_CACHE_ENTRY_COUNT"></a>

## 369.59 `CONFIG_LOG_SOURCE_NAME_CACHE_ENTRY_COUNT`

**提示（Prompt）**：来源名称缓存条目数量（source name cache）

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

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MULTIDOMAIN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MULTIDOMAIN)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_SOURCE_NAME_CACHE_ENTRY_SIZE"></a>

## 369.60 `CONFIG_LOG_SOURCE_NAME_CACHE_ENTRY_SIZE`

**提示（Prompt）**：来源名称缓存槽位大小（cache slot size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MULTIDOMAIN && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MULTIDOMAIN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MULTIDOMAIN)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_SPEED"></a>

## 369.61 `CONFIG_LOG_SPEED`

**提示（Prompt）**：优先性能而非体积（Prefer performance over size）

**说明（Help）**

启用后，日志功能可能占用更多代码空间，以获得更快的执行速度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_MODE_DEFERRED && !CONFIG_LOG_FRONTEND && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_DEFERRED`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_DEFERRED)、[`CONFIG_LOG_FRONTEND`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_TAG_DEFAULT"></a>

## 369.62 `CONFIG_LOG_TAG_DEFAULT`

**提示（Prompt）**：默认标签（Default tag）

**说明（Help）**

初始标签（tag）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_TAG_MAX_LEN > 0 && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_TAG_MAX_LEN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_TAG_MAX_LEN)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_TAG_MAX_LEN"></a>

## 369.63 `CONFIG_LOG_TAG_MAX_LEN`

**提示（Prompt）**：标签最大长度（Tag max length）

**说明（Help）**

设为非零值后，允许指定添加到每条日志消息前的标签（tag）。标签可在运行时更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 64]
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_TEST_CLEAR_MESSAGE_SPACE"></a>

## 369.64 `CONFIG_LOG_TEST_CLEAR_MESSAGE_SPACE`

**提示（Prompt）**：分配后清空消息（Clear message after allocation）

**说明（Help）**

用于测试：当消息包含填充字节（paddings）时，简化消息比较。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZTEST && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_THREAD_ID_PREFIX"></a>

## 369.65 `CONFIG_LOG_THREAD_ID_PREFIX`

**提示（Prompt）**：线程标识前缀（Thread ID prefix）

**说明（Help）**

允许在日志消息前添加线程名称或 ID 前缀。启用 `THREAD_NAME` 时，使用线程名称。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.formatting:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.formatting#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 输出格式化（Output Formatting）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_TIMESTAMP_64BIT"></a>

## 369.66 `CONFIG_LOG_TIMESTAMP_64BIT`

**提示（Prompt）**：使用 64 位时间戳（timestamp）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**被选择（Selected by）**

```text
CONFIG_LOG_MULTIDOMAIN
CONFIG_LOG_TIMESTAMP_USE_REALTIME
CONFIG_LOG_MULTIDOMAIN_BACKEND
CONFIG_LOG_MULTIDOMAIN_LINK
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_MULTIDOMAIN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MULTIDOMAIN)、[`CONFIG_LOG_TIMESTAMP_USE_REALTIME`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_TIMESTAMP_USE_REALTIME)、[`CONFIG_LOG_MULTIDOMAIN_BACKEND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MULTIDOMAIN_BACKEND)、[`CONFIG_LOG_MULTIDOMAIN_LINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MULTIDOMAIN_LINK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LOG_MULTIDOMAIN_BACKEND`、`CONFIG_LOG_MULTIDOMAIN_LINK`。

<a id="CONFIG_LOG_TIMESTAMP_USE_REALTIME"></a>

## 369.67 `CONFIG_LOG_TIMESTAMP_USE_REALTIME`

**提示（Prompt）**：使用实时时钟生成时间戳（real time clock）

**说明（Help）**

启用后，使用实时时钟（real time clock）生成时间戳。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_LOG_TIMESTAMP_64BIT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LOG_TIMESTAMP_64BIT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_TIMESTAMP_64BIT)。

<a id="CONFIG_LOG_TRACE_SHORT_TIMESTAMP"></a>

## 369.68 `CONFIG_LOG_TRACE_SHORT_TIMESTAMP`

**提示（Prompt）**：跟踪使用 24 位时间戳（timestamp）

**说明（Help）**

启用后，使用较短的时间戳并压缩跟踪消息（trace message）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/logging/Kconfig.processing:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.processing#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 处理（Processing）

**配置项引用（Symbol References）**：[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_LOG_USE_TAGGED_ARGUMENTS"></a>

## 369.69 `CONFIG_LOG_USE_TAGGED_ARGUMENTS`

**提示（Prompt）**：使用带标签参数进行打包（tagged arguments）

**说明（Help）**

启用后，打包（packaging）使用带标签参数（tagged arguments）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PICOLIBC && CONFIG_LOG
```

**主动选择（Selects）**

```text
CONFIG_CBPRINTF_PACKAGE_SUPPORT_TAGGED_ARGUMENTS
CONFIG_LOG_ALWAYS_RUNTIME
```

**被选择（Selected by）**

```text
CONFIG_LOG_MIPI_SYST_USE_CATALOG
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_PICOLIBC`](P198_lib_配置项参考_2.md#CONFIG_PICOLIBC)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CBPRINTF_PACKAGE_SUPPORT_TAGGED_ARGUMENTS`](P197_lib_配置项参考_1.md#CONFIG_CBPRINTF_PACKAGE_SUPPORT_TAGGED_ARGUMENTS)、[`CONFIG_LOG_ALWAYS_RUNTIME`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_ALWAYS_RUNTIME)、[`CONFIG_LOG_MIPI_SYST_USE_CATALOG`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MIPI_SYST_USE_CATALOG)。

<a id="CONFIG_LOG_USE_VLA"></a>

## 369.70 `CONFIG_LOG_USE_VLA`

**提示（Prompt）**：使用变长数组（variable length arrays）

**说明（Help）**

使用变长数组（VLA）可略微减少栈占用，但某些情况下可能不受支持。注意，这里的 VLA 用于大小可在编译时确定的数组，因此数组在运行时大小固定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TOOLCHAIN_SUPPORTS_VLA_IN_STATEMENTS && CONFIG_LOG
```

**默认值（Defaults）**

```text
y if !CONFIG_MISRA_SANE
```

**定义位置（Location）**：[`subsys/logging/Kconfig.misc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.misc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 杂项（Misc）

**配置项引用（Symbol References）**：[`CONFIG_TOOLCHAIN_SUPPORTS_VLA_IN_STATEMENTS`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_TOOLCHAIN_SUPPORTS_VLA_IN_STATEMENTS)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MISRA_SANE`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_MISRA_SANE)。

<a id="CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE"></a>

## 369.71 `CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：回环磁盘（loopback_disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DISK_DRIVER_LOOPBACK && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_LOOPBACK_DISK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LOOPBACK_DISK_LOG_LEVEL_OFF
CONFIG_LOOPBACK_DISK_LOG_LEVEL_ERR
CONFIG_LOOPBACK_DISK_LOG_LEVEL_WRN
CONFIG_LOOPBACK_DISK_LOG_LEVEL_INF
CONFIG_LOOPBACK_DISK_LOG_LEVEL_DBG
CONFIG_LOOPBACK_DISK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 回环磁盘（Loopback Disk）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DISK_DRIVER_LOOPBACK`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_LOOPBACK)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_LOOPBACK_DISK_LOG_LEVEL_DEFAULT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOOPBACK_DISK_LOG_LEVEL_DEFAULT)、[`CONFIG_LOOPBACK_DISK_LOG_LEVEL_OFF`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOOPBACK_DISK_LOG_LEVEL_OFF)、[`CONFIG_LOOPBACK_DISK_LOG_LEVEL_ERR`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOOPBACK_DISK_LOG_LEVEL_ERR)、[`CONFIG_LOOPBACK_DISK_LOG_LEVEL_WRN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOOPBACK_DISK_LOG_LEVEL_WRN)、[`CONFIG_LOOPBACK_DISK_LOG_LEVEL_INF`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOOPBACK_DISK_LOG_LEVEL_INF)、[`CONFIG_LOOPBACK_DISK_LOG_LEVEL_DBG`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOOPBACK_DISK_LOG_LEVEL_DBG)。

<a id="CONFIG_LOOPBACK_DISK_LOG_LEVEL_DBG"></a>

## 369.72 `CONFIG_LOOPBACK_DISK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 回环磁盘（Loopback Disk） → 回环磁盘（loopback_disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LOOPBACK_DISK_LOG_LEVEL_DEFAULT"></a>

## 369.73 `CONFIG_LOOPBACK_DISK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 回环磁盘（Loopback Disk） → 回环磁盘（loopback_disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LOOPBACK_DISK_LOG_LEVEL_ERR"></a>

## 369.74 `CONFIG_LOOPBACK_DISK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 回环磁盘（Loopback Disk） → 回环磁盘（loopback_disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LOOPBACK_DISK_LOG_LEVEL_INF"></a>

## 369.75 `CONFIG_LOOPBACK_DISK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 回环磁盘（Loopback Disk） → 回环磁盘（loopback_disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LOOPBACK_DISK_LOG_LEVEL_OFF"></a>

## 369.76 `CONFIG_LOOPBACK_DISK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 回环磁盘（Loopback Disk） → 回环磁盘（loopback_disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LOOPBACK_DISK_LOG_LEVEL_WRN"></a>

## 369.77 `CONFIG_LOOPBACK_DISK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 回环磁盘（Loopback Disk） → 回环磁盘（loopback_disk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOOPBACK_DISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORAWAN_LOG_LEVEL_CHOICE"></a>

## 369.78 `CONFIG_LORAWAN_LOG_LEVEL_CHOICE`

**提示（Prompt）**：LoRaWAN 广域网（lorawan）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
CONFIG_LORAWAN_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LORAWAN_LOG_LEVEL_OFF
CONFIG_LORAWAN_LOG_LEVEL_ERR
CONFIG_LORAWAN_LOG_LEVEL_WRN
CONFIG_LORAWAN_LOG_LEVEL_INF
CONFIG_LORAWAN_LOG_LEVEL_DBG
CONFIG_LORAWAN_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LORAWAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN)、[`CONFIG_LORAWAN_LOG_LEVEL_DEFAULT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_LOG_LEVEL_DEFAULT)、[`CONFIG_LORAWAN_LOG_LEVEL_OFF`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_LOG_LEVEL_OFF)、[`CONFIG_LORAWAN_LOG_LEVEL_ERR`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_LOG_LEVEL_ERR)、[`CONFIG_LORAWAN_LOG_LEVEL_WRN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_LOG_LEVEL_WRN)、[`CONFIG_LORAWAN_LOG_LEVEL_INF`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_LOG_LEVEL_INF)、[`CONFIG_LORAWAN_LOG_LEVEL_DBG`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_LOG_LEVEL_DBG)。

<a id="CONFIG_LORAWAN_LOG_LEVEL_DBG"></a>

## 369.79 `CONFIG_LORAWAN_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 广域网（lorawan）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORAWAN_LOG_LEVEL_DEFAULT"></a>

## 369.80 `CONFIG_LORAWAN_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 广域网（lorawan）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORAWAN_LOG_LEVEL_ERR"></a>

## 369.81 `CONFIG_LORAWAN_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 广域网（lorawan）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORAWAN_LOG_LEVEL_INF"></a>

## 369.82 `CONFIG_LORAWAN_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 广域网（lorawan）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORAWAN_LOG_LEVEL_OFF"></a>

## 369.83 `CONFIG_LORAWAN_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 广域网（lorawan）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORAWAN_LOG_LEVEL_WRN"></a>

## 369.84 `CONFIG_LORAWAN_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 广域网（lorawan）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE"></a>

## 369.85 `CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE`

**提示（Prompt）**：LoRaWAN 服务（lorawan_services）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_LORAWAN_SERVICES && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
CONFIG_LORAWAN_SERVICES_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LORAWAN_SERVICES_LOG_LEVEL_OFF
CONFIG_LORAWAN_SERVICES_LOG_LEVEL_ERR
CONFIG_LORAWAN_SERVICES_LOG_LEVEL_WRN
CONFIG_LORAWAN_SERVICES_LOG_LEVEL_INF
CONFIG_LORAWAN_SERVICES_LOG_LEVEL_DBG
CONFIG_LORAWAN_SERVICES_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LORAWAN_SERVICES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_SERVICES)、[`CONFIG_LORAWAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN)、[`CONFIG_LORAWAN_SERVICES_LOG_LEVEL_DEFAULT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_SERVICES_LOG_LEVEL_DEFAULT)、[`CONFIG_LORAWAN_SERVICES_LOG_LEVEL_OFF`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_SERVICES_LOG_LEVEL_OFF)、[`CONFIG_LORAWAN_SERVICES_LOG_LEVEL_ERR`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_SERVICES_LOG_LEVEL_ERR)、[`CONFIG_LORAWAN_SERVICES_LOG_LEVEL_WRN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_SERVICES_LOG_LEVEL_WRN)、[`CONFIG_LORAWAN_SERVICES_LOG_LEVEL_INF`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_SERVICES_LOG_LEVEL_INF)、[`CONFIG_LORAWAN_SERVICES_LOG_LEVEL_DBG`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_SERVICES_LOG_LEVEL_DBG)。

<a id="CONFIG_LORAWAN_SERVICES_LOG_LEVEL_DBG"></a>

## 369.86 `CONFIG_LORAWAN_SERVICES_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → LoRaWAN 服务（lorawan_services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORAWAN_SERVICES_LOG_LEVEL_DEFAULT"></a>

## 369.87 `CONFIG_LORAWAN_SERVICES_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → LoRaWAN 服务（lorawan_services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORAWAN_SERVICES_LOG_LEVEL_ERR"></a>

## 369.88 `CONFIG_LORAWAN_SERVICES_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → LoRaWAN 服务（lorawan_services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORAWAN_SERVICES_LOG_LEVEL_INF"></a>

## 369.89 `CONFIG_LORAWAN_SERVICES_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → LoRaWAN 服务（lorawan_services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORAWAN_SERVICES_LOG_LEVEL_OFF"></a>

## 369.90 `CONFIG_LORAWAN_SERVICES_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → LoRaWAN 服务（lorawan_services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORAWAN_SERVICES_LOG_LEVEL_WRN"></a>

## 369.91 `CONFIG_LORAWAN_SERVICES_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → LoRaWAN 服务（lorawan_services）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORAWAN_SERVICES_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORA_LOG_LEVEL_CHOICE"></a>

## 369.92 `CONFIG_LORA_LOG_LEVEL_CHOICE`

**提示（Prompt）**：LoRa 无线通信（lora）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_LORA
```

**默认值（Defaults）**

```text
CONFIG_LORA_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LORA_LOG_LEVEL_OFF
CONFIG_LORA_LOG_LEVEL_ERR
CONFIG_LORA_LOG_LEVEL_WRN
CONFIG_LORA_LOG_LEVEL_INF
CONFIG_LORA_LOG_LEVEL_DBG
CONFIG_LORA_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)、[`CONFIG_LORA_LOG_LEVEL_DEFAULT`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORA_LOG_LEVEL_DEFAULT)、[`CONFIG_LORA_LOG_LEVEL_OFF`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORA_LOG_LEVEL_OFF)、[`CONFIG_LORA_LOG_LEVEL_ERR`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORA_LOG_LEVEL_ERR)、[`CONFIG_LORA_LOG_LEVEL_WRN`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORA_LOG_LEVEL_WRN)、[`CONFIG_LORA_LOG_LEVEL_INF`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORA_LOG_LEVEL_INF)、[`CONFIG_LORA_LOG_LEVEL_DBG`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORA_LOG_LEVEL_DBG)。

<a id="CONFIG_LORA_LOG_LEVEL_DBG"></a>

## 369.93 `CONFIG_LORA_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → LoRa 无线通信（lora）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORA_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORA_LOG_LEVEL_DEFAULT"></a>

## 369.94 `CONFIG_LORA_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → LoRa 无线通信（lora）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORA_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORA_LOG_LEVEL_ERR"></a>

## 369.95 `CONFIG_LORA_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → LoRa 无线通信（lora）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORA_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORA_LOG_LEVEL_INF"></a>

## 369.96 `CONFIG_LORA_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → LoRa 无线通信（lora）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORA_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORA_LOG_LEVEL_OFF"></a>

## 369.97 `CONFIG_LORA_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → LoRa 无线通信（lora）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORA_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LORA_LOG_LEVEL_WRN"></a>

## 369.98 `CONFIG_LORA_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → LoRa 驱动 → LoRa 无线通信（lora）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LORA_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LORA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LV_Z_LOG_LEVEL_CHOICE"></a>

## 369.99 `CONFIG_LV_Z_LOG_LEVEL_CHOICE`

**提示（Prompt）**：LVGL 图形库（LVGL）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_Z_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LV_Z_LOG_LEVEL_OFF
CONFIG_LV_Z_LOG_LEVEL_ERR
CONFIG_LV_Z_LOG_LEVEL_WRN
CONFIG_LV_Z_LOG_LEVEL_INF
CONFIG_LV_Z_LOG_LEVEL_DBG
CONFIG_LV_Z_LOG_LEVEL_DEFAULT
CONFIG_LV_Z_LOG_LEVEL_OFF
CONFIG_LV_Z_LOG_LEVEL_ERR
CONFIG_LV_Z_LOG_LEVEL_WRN
CONFIG_LV_Z_LOG_LEVEL_INF
CONFIG_LV_Z_LOG_LEVEL_DBG
CONFIG_LV_Z_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_LV_Z_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_LV_Z_LOG_LEVEL_DEFAULT)、[`CONFIG_LV_Z_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_LV_Z_LOG_LEVEL_OFF)、[`CONFIG_LV_Z_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_LV_Z_LOG_LEVEL_ERR)、[`CONFIG_LV_Z_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_LV_Z_LOG_LEVEL_WRN)、[`CONFIG_LV_Z_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_LV_Z_LOG_LEVEL_INF)、[`CONFIG_LV_Z_LOG_LEVEL_DBG`](P369_subsys_logging_配置项参考_18.md#CONFIG_LV_Z_LOG_LEVEL_DBG)。

<a id="CONFIG_LV_Z_LOG_LEVEL_DBG"></a>

## 369.100 `CONFIG_LV_Z_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL 图形库（LVGL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LV_Z_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P368_subsys_logging_配置项参考_17.md) · [返回大纲](大纲.md) · [下一章](P370_subsys_logging_配置项参考_19.md)
