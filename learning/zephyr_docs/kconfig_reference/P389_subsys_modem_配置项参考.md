---
id: learning.zephyr-docs.kconfig-reference.page-389
title: "`subsys/modem`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第389章\_`subsys/modem`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/modem` 的 35 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MODEM_BACKEND_TTY"></a>

## 389.1 `CONFIG_MODEM_BACKEND_TTY`

**提示（Prompt）**：调制解调器 TTY 后端模块（Modem backend module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX && CONFIG_MODEM_MODULES
```

**主动选择（Selects）**

```text
CONFIG_MODEM_PIPE
```

**定义位置（Location）**：[`subsys/modem/backends/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/backends/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_PIPE`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_PIPE)。

<a id="CONFIG_MODEM_BACKEND_UART"></a>

## 389.2 `CONFIG_MODEM_BACKEND_UART`

**提示（Prompt）**：调制解调器 UART 后端模块（Modem backend module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_INTERRUPT_DRIVEN || CONFIG_UART_ASYNC_API) && CONFIG_MODEM_MODULES
```

**主动选择（Selects）**

```text
CONFIG_MODEM_PIPE
```

**被选择（Selected by）**

```text
CONFIG_GNSS_ERICSSON_F5521GW
CONFIG_GNSS_NMEA_GENERIC
CONFIG_GNSS_GLOBALTOP_PA6H
CONFIG_GNSS_LUATOS_AIR530Z
CONFIG_GNSS_QUECTEL_LCX6G
CONFIG_GNSS_U_BLOX_F9P
CONFIG_GNSS_U_BLOX_M10
CONFIG_GNSS_U_BLOX_M8
CONFIG_LORA_RYLRXXX
CONFIG_MODEM_CELLULAR
CONFIG_MODEM_HL78XX
```

**定义位置（Location）**：[`subsys/modem/backends/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/backends/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules）

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_PIPE`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_PIPE)、[`CONFIG_GNSS_ERICSSON_F5521GW`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_ERICSSON_F5521GW)、[`CONFIG_GNSS_NMEA_GENERIC`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA_GENERIC)、[`CONFIG_GNSS_GLOBALTOP_PA6H`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_GLOBALTOP_PA6H)、[`CONFIG_GNSS_LUATOS_AIR530Z`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_LUATOS_AIR530Z)、[`CONFIG_GNSS_QUECTEL_LCX6G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_QUECTEL_LCX6G)、[`CONFIG_GNSS_U_BLOX_F9P`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P)、[`CONFIG_GNSS_U_BLOX_M10`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10)、[`CONFIG_GNSS_U_BLOX_M8`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M8)、[`CONFIG_LORA_RYLRXXX`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_RYLRXXX)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)。

<a id="CONFIG_MODEM_BACKEND_UART_ASYNC"></a>

## 389.3 `CONFIG_MODEM_BACKEND_UART_ASYNC`

**提示（Prompt）**：调制解调器 UART 后端的异步实现（async implementation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_BACKEND_UART && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
y if CONFIG_UART_ASYNC_API
```

**定义位置（Location）**：[`subsys/modem/backends/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/backends/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器 UART 后端模块（Modem backend module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_BACKEND_UART`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)。

<a id="CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC"></a>

## 389.4 `CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC`

**提示（Prompt）**：调制解调器异步 UART 后端的硬件流控（HWFC）【实验性 EXPERIMENTAL】

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_BACKEND_UART_ASYNC && CONFIG_MODEM_BACKEND_UART && CONFIG_MODEM_MODULES
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/modem/backends/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/backends/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器 UART 后端模块（Modem backend module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_BACKEND_UART_ASYNC`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART_ASYNC)、[`CONFIG_MODEM_BACKEND_UART`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC_BUFFER_COUNT"></a>

## 389.5 `CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC_BUFFER_COUNT`

**提示（Prompt）**：调制解调器异步 UART 硬件流控缓冲区数量（HWFC buffer count）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC && CONFIG_MODEM_BACKEND_UART_ASYNC && CONFIG_MODEM_BACKEND_UART && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[2, 4]
```

**定义位置（Location）**：[`subsys/modem/backends/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/backends/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器 UART 后端模块（Modem backend module） → 调制解调器异步 UART 后端的硬件流控（HWFC）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC)、[`CONFIG_MODEM_BACKEND_UART_ASYNC`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART_ASYNC)、[`CONFIG_MODEM_BACKEND_UART`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_BACKEND_UART_ASYNC_RECEIVE_IDLE_TIMEOUT_MS"></a>

## 389.6 `CONFIG_MODEM_BACKEND_UART_ASYNC_RECEIVE_IDLE_TIMEOUT_MS`

**提示（Prompt）**：调制解调器异步 UART 接收空闲超时（毫秒）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_BACKEND_UART_ASYNC && CONFIG_MODEM_BACKEND_UART && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`subsys/modem/backends/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/backends/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器 UART 后端模块（Modem backend module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_BACKEND_UART_ASYNC`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART_ASYNC)、[`CONFIG_MODEM_BACKEND_UART`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_BACKEND_UART_ASYNC_TRANSMIT_TIMEOUT_MS"></a>

## 389.7 `CONFIG_MODEM_BACKEND_UART_ASYNC_TRANSMIT_TIMEOUT_MS`

**提示（Prompt）**：调制解调器异步 UART 发送超时（毫秒）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_BACKEND_UART_ASYNC && CONFIG_MODEM_BACKEND_UART && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`subsys/modem/backends/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/backends/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器 UART 后端模块（Modem backend module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_BACKEND_UART_ASYNC`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART_ASYNC)、[`CONFIG_MODEM_BACKEND_UART`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_BACKEND_UART_ISR"></a>

## 389.8 `CONFIG_MODEM_BACKEND_UART_ISR`

**提示（Prompt）**：调制解调器 UART 后端的中断驱动实现（interrupt driven implementation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_BACKEND_UART && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
y if CONFIG_UART_INTERRUPT_DRIVEN
```

**定义位置（Location）**：[`subsys/modem/backends/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/backends/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器 UART 后端模块（Modem backend module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_BACKEND_UART`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)。

<a id="CONFIG_MODEM_BACKEND_UART_ISR_RECEIVE_IDLE_TIMEOUT_MS"></a>

## 389.9 `CONFIG_MODEM_BACKEND_UART_ISR_RECEIVE_IDLE_TIMEOUT_MS`

**提示（Prompt）**：中断驱动 UART 首字节接收至 RECEIVE_READY 管道事件的延迟

**说明（Help）**

指定后端接收到字节后，在发送 `RECEIVE_READY` 管道事件前等待的时间，单位为毫秒。如果缓冲区空间提前耗尽，则不等延迟结束就发送事件。合适的值约为填满接收缓冲区一半所需时间的 90%，计算式如下：

```text
(<UART receive_buf_size> / 2) / (<UART baud rate> / <UART bits per byte>) * <ms per sec>
```

其中依次为 UART 接收缓冲区大小、波特率、每字节传输位数和每秒毫秒数。`modem_cellular` 驱动的默认示例：

```text
(512 / 2) / (115200 / 10) * 1000 = 22,222 => 20
```

译注：原文 `22,222` 使用小数逗号，约为 22.222 毫秒，取约 90% 后使用 20 毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_BACKEND_UART_ISR && CONFIG_MODEM_BACKEND_UART && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`subsys/modem/backends/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/backends/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器 UART 后端模块（Modem backend module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_BACKEND_UART_ISR`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART_ISR)、[`CONFIG_MODEM_BACKEND_UART`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_CHAT"></a>

## 389.10 `CONFIG_MODEM_CHAT`

**提示（Prompt）**：调制解调器会话模块（Modem chat module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_MODULES
```

**主动选择（Selects）**

```text
CONFIG_MODEM_PIPE
```

**被选择（Selected by）**

```text
CONFIG_GNSS_ERICSSON_F5521GW
CONFIG_GNSS_NMEA_GENERIC
CONFIG_GNSS_GLOBALTOP_PA6H
CONFIG_GNSS_LUATOS_AIR530Z
CONFIG_GNSS_QUECTEL_LCX6G
CONFIG_LORA_RYLRXXX
CONFIG_MODEM_CELLULAR
CONFIG_MODEM_HL78XX
```

**定义位置（Location）**：[`subsys/modem/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_PIPE`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_PIPE)、[`CONFIG_GNSS_ERICSSON_F5521GW`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_ERICSSON_F5521GW)、[`CONFIG_GNSS_NMEA_GENERIC`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA_GENERIC)、[`CONFIG_GNSS_GLOBALTOP_PA6H`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_GLOBALTOP_PA6H)、[`CONFIG_GNSS_LUATOS_AIR530Z`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_LUATOS_AIR530Z)、[`CONFIG_GNSS_QUECTEL_LCX6G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_QUECTEL_LCX6G)、[`CONFIG_LORA_RYLRXXX`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_RYLRXXX)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)。

<a id="CONFIG_MODEM_CHAT_COMMANDS_CONDITIONAL"></a>

## 389.11 `CONFIG_MODEM_CHAT_COMMANDS_CONDITIONAL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

调制解调器会话（modem chat）的使用需要条件命令支持。定义了条件命令的使用者应选择此项，例如使用 `MODEM_CHAT_SCRIPT_CMD_RESP_COND` 的代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CHAT && CONFIG_MODEM_MODULES
```

**定义位置（Location）**：[`subsys/modem/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器会话模块（Modem chat module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CHAT`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CHAT)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_CHAT_LOG_BUFFER_SIZE"></a>

## 389.12 `CONFIG_MODEM_CHAT_LOG_BUFFER_SIZE`

**提示（Prompt）**：调制解调器会话日志缓冲区大小（字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CHAT && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/modem/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器会话模块（Modem chat module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CHAT`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CHAT)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_CHAT_LOG_RAW_RX"></a>

## 389.13 `CONFIG_MODEM_CHAT_LOG_RAW_RX`

**提示（Prompt）**：记录原始接收的调制解调器文本行

**说明（Help）**

记录调制解调器收到的原始文本行，而不是解析后的调试日志，从而在 `modem_chat` 将响应分词之前，原样保留分隔符和空字段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MODEM_MODULES_LOG_LEVEL_DBG && CONFIG_MODEM_CHAT && CONFIG_MODEM_MODULES
```

**定义位置（Location）**：[`subsys/modem/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器会话模块（Modem chat module）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MODEM_MODULES_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_DBG)、[`CONFIG_MODEM_CHAT`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CHAT)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_CHAT_WORK_BUFFER_SIZE"></a>

## 389.14 `CONFIG_MODEM_CHAT_WORK_BUFFER_SIZE`

**提示（Prompt）**：调制解调器会话工作缓冲区大小（字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CHAT && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/modem/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器会话模块（Modem chat module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CHAT`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CHAT)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_CMUX"></a>

## 389.15 `CONFIG_MODEM_CMUX`

**提示（Prompt）**：调制解调器连接复用模块（Modem CMUX module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_MODULES
```

**主动选择（Selects）**

```text
CONFIG_MODEM_PIPE
CONFIG_EVENTS
CONFIG_CRC
```

**被选择（Selected by）**

```text
CONFIG_MODEM_CELLULAR
```

**定义位置（Location）**：[`subsys/modem/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_PIPE`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_PIPE)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)。

<a id="CONFIG_MODEM_CMUX_DEFAULT_MTU_127"></a>

## 389.16 `CONFIG_MODEM_CMUX_DEFAULT_MTU_127`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

提示默认 `MODEM_CMUX_MTU` 大小应为 127 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CMUX && CONFIG_MODEM_MODULES
```

**被选择（Selected by）**

```text
CONFIG_MODEM_CELLULAR
```

**定义位置（Location）**：[`subsys/modem/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)。

<a id="CONFIG_MODEM_CMUX_LOG_FRAMES"></a>

## 389.17 `CONFIG_MODEM_CMUX_LOG_FRAMES`

**提示（Prompt）**：记录连接复用（CMUX）帧

**说明（Help）**

启用 CMUX 帧日志，可能产生大量日志数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CMUX_LOG_LEVEL_DBG && CONFIG_MODEM_CMUX && CONFIG_MODEM_MODULES
```

**定义位置（Location）**：[`subsys/modem/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_DBG)、[`CONFIG_MODEM_CMUX`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_CMUX_MSC_FC_THRESHOLD"></a>

## 389.18 `CONFIG_MODEM_CMUX_MSC_FC_THRESHOLD`

**提示（Prompt）**：DLCI 环形缓冲区剩余空间少于指定字节数时启用流控

**说明（Help）**

数据链路连接标识（DLCI）接收环形缓冲区的可用空间小于此值时，连接复用（CMUX）模块发送流控位置位的调制解调器状态命令（MSC）帧，通知发送方停止发送。接收缓冲区重新有至少 `MODEM_CMUX_MTU` 字节空闲时解除流控。仅在对端支持 MSC 消息时有效，设为 `0` 可禁用流控。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CMUX && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
CONFIG_MODEM_CMUX_MTU if CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE_EXTRA > 0
0
```

**取值范围（Ranges）**

```text
[0, CONFIG_MODEM_CMUX_MTU]
```

**定义位置（Location）**：[`subsys/modem/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_CMUX_MTU`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CMUX_MTU)、[`CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE_EXTRA`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE_EXTRA)。

<a id="CONFIG_MODEM_CMUX_MTU"></a>

## 389.19 `CONFIG_MODEM_CMUX_MTU`

**提示（Prompt）**：CMUX 最大传输单元大小（MTU，字节）

**说明（Help）**

连接复用（CMUX）模块的最大传输单元（MTU）大小。Linux `ldattach` 默认为 127 字节，3GPP TS 27.010 默认为 31 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CMUX && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
127 if CONFIG_MODEM_CMUX_DEFAULT_MTU_127
31
```

**取值范围（Ranges）**

```text
[16, 1500]
```

**定义位置（Location）**：[`subsys/modem/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_CMUX_DEFAULT_MTU_127`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CMUX_DEFAULT_MTU_127)。

<a id="CONFIG_MODEM_CMUX_T1_TIMEOUT"></a>

## 389.20 `CONFIG_MODEM_CMUX_T1_TIMEOUT`

**提示（Prompt）**：CMUX T1 超时（毫秒）

**说明（Help）**

确认定时器（Acknowledgment Timer，T1）：重新发送帧前等待确认的时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CMUX && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[10, 2550]
```

**定义位置（Location）**：[`subsys/modem/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_CMUX_T2_TIMEOUT"></a>

## 389.21 `CONFIG_MODEM_CMUX_T2_TIMEOUT`

**提示（Prompt）**：CMUX T2 超时（毫秒）

**说明（Help）**

复用器控制通道响应定时器（Response Timer，T2）：等待复用器控制命令响应的时间，超过后认为链路失效，单位为毫秒。

注意：Zephyr 的 CMUX 实现与 3GPP TS 27.010 规范不同，所有重试定时器都使用 T1，而 T2 仅用作总响应超时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CMUX && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
300
```

**取值范围（Ranges）**

```text
[20, 2550]
```

**定义位置（Location）**：[`subsys/modem/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_CMUX_T3_TIMEOUT"></a>

## 389.22 `CONFIG_MODEM_CMUX_T3_TIMEOUT`

**提示（Prompt）**：CMUX T3 超时（秒）

**说明（Help）**

唤醒流程响应定时器（Response Timer for wake-up procedure，T3）：超过此等待时间后认为链路失效，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CMUX && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/modem/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE_EXTRA"></a>

## 389.23 `CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE_EXTRA`

**提示（Prompt）**：CMUX 模块额外工作缓冲区大小（字节）

**说明（Help）**

在 CMUX 模块工作缓冲区中增加的字节数。默认缓冲区大小为 `MODEM_CMUX_MTU + 7`，其中 `7` 为 CMUX 头部大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_CMUX && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/modem/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_DEDICATED_WORKQUEUE"></a>

## 389.24 `CONFIG_MODEM_DEDICATED_WORKQUEUE`

**提示（Prompt）**：为调制解调器操作使用专用工作队列

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_MODULES
```

**被选择（Selected by）**

```text
CONFIG_MODEM_CELLULAR_ON_DEMAND_CONNECT
```

**定义位置（Location）**：[`subsys/modem/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_CELLULAR_ON_DEMAND_CONNECT`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR_ON_DEMAND_CONNECT)。

<a id="CONFIG_MODEM_DEDICATED_WORKQUEUE_PRIORITY"></a>

## 389.25 `CONFIG_MODEM_DEDICATED_WORKQUEUE_PRIORITY`

**提示（Prompt）**：调制解调器专用工作队列优先级（priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_DEDICATED_WORKQUEUE && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
CONFIG_SYSTEM_WORKQUEUE_PRIORITY
```

**定义位置（Location）**：[`subsys/modem/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 为调制解调器操作使用专用工作队列

**配置项引用（Symbol References）**：[`CONFIG_MODEM_DEDICATED_WORKQUEUE`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_DEDICATED_WORKQUEUE)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_SYSTEM_WORKQUEUE_PRIORITY`](P002_kernel_配置项参考_2.md#CONFIG_SYSTEM_WORKQUEUE_PRIORITY)。

<a id="CONFIG_MODEM_DEDICATED_WORKQUEUE_STACK_SIZE"></a>

## 389.26 `CONFIG_MODEM_DEDICATED_WORKQUEUE_STACK_SIZE`

**提示（Prompt）**：调制解调器专用工作队列栈大小（stack size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_DEDICATED_WORKQUEUE && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/modem/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 为调制解调器操作使用专用工作队列

**配置项引用（Symbol References）**：[`CONFIG_MODEM_DEDICATED_WORKQUEUE`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_DEDICATED_WORKQUEUE)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_MODULES"></a>

## 389.27 `CONFIG_MODEM_MODULES`

**提示（Prompt）**：调制解调器模块（Modem modules）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_GNSS_ERICSSON_F5521GW
CONFIG_GNSS_NMEA_GENERIC
CONFIG_GNSS_GLOBALTOP_PA6H
CONFIG_GNSS_LUATOS_AIR530Z
CONFIG_GNSS_QUECTEL_LCX6G
CONFIG_GNSS_U_BLOX_F9P
CONFIG_GNSS_U_BLOX_M10
CONFIG_GNSS_U_BLOX_M8
CONFIG_LORA_RYLRXXX
CONFIG_MODEM_AT_SHELL
CONFIG_MODEM_CELLULAR
CONFIG_MODEM_HL78XX
```

**定义位置（Location）**：[`subsys/modem/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_ERICSSON_F5521GW`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_ERICSSON_F5521GW)、[`CONFIG_GNSS_NMEA_GENERIC`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_NMEA_GENERIC)、[`CONFIG_GNSS_GLOBALTOP_PA6H`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_GLOBALTOP_PA6H)、[`CONFIG_GNSS_LUATOS_AIR530Z`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_LUATOS_AIR530Z)、[`CONFIG_GNSS_QUECTEL_LCX6G`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_QUECTEL_LCX6G)、[`CONFIG_GNSS_U_BLOX_F9P`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_F9P)、[`CONFIG_GNSS_U_BLOX_M10`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M10)、[`CONFIG_GNSS_U_BLOX_M8`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_M8)、[`CONFIG_LORA_RYLRXXX`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_RYLRXXX)、[`CONFIG_MODEM_AT_SHELL`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_AT_SHELL)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)。

<a id="CONFIG_MODEM_PIPE"></a>

## 389.28 `CONFIG_MODEM_PIPE`

**提示（Prompt）**：调制解调器管道模块（Modem pipe module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_MODULES
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**被选择（Selected by）**

```text
CONFIG_LORA_RYLRXXX
CONFIG_MODEM_CELLULAR
CONFIG_MODEM_HL78XX
CONFIG_MODEM_CHAT
CONFIG_MODEM_CMUX
CONFIG_MODEM_PPP
CONFIG_MODEM_UBX
CONFIG_MODEM_BACKEND_TTY
CONFIG_MODEM_BACKEND_UART
```

**定义位置（Location）**：[`subsys/modem/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_LORA_RYLRXXX`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_RYLRXXX)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM_CHAT`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CHAT)、[`CONFIG_MODEM_CMUX`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_PPP`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_PPP)、[`CONFIG_MODEM_UBX`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_UBX)、[`CONFIG_MODEM_BACKEND_TTY`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_TTY)、[`CONFIG_MODEM_BACKEND_UART`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_BACKEND_UART)。

<a id="CONFIG_MODEM_PIPELINK"></a>

## 389.29 `CONFIG_MODEM_PIPELINK`

**提示（Prompt）**：调制解调器管道链接模块（Modem pipelink module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_PIPE && CONFIG_MODEM_MODULES
```

**被选择（Selected by）**

```text
CONFIG_MODEM_CELLULAR
CONFIG_MODEM_HL78XX
```

**定义位置（Location）**：[`subsys/modem/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器管道模块（Modem pipe module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_PIPE`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_PIPE)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)。

<a id="CONFIG_MODEM_PPP"></a>

## 389.30 `CONFIG_MODEM_PPP`

**提示（Prompt）**：调制解调器点对点协议模块（Modem PPP module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_MODEM_MODULES
```

**主动选择（Selects）**

```text
CONFIG_MODEM_PIPE
CONFIG_CRC
CONFIG_PM_DEVICE_RUNTIME_ASYNC if CONFIG_PM_DEVICE_RUNTIME
```

**被选择（Selected by）**

```text
CONFIG_MODEM_CELLULAR
```

**定义位置（Location）**：[`subsys/modem/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PPP)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_PIPE`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_PIPE)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)、[`CONFIG_PM_DEVICE_RUNTIME_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME_ASYNC)、[`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_MODEM_CELLULAR`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_CELLULAR)。

<a id="CONFIG_MODEM_PPP_NET_BUF_FRAG_SIZE"></a>

## 389.31 `CONFIG_MODEM_PPP_NET_BUF_FRAG_SIZE`

**提示（Prompt）**：网络缓冲区分片大小（Network buffer fragment size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_PPP && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
CONFIG_NET_BUF_DATA_SIZE if CONFIG_NET_BUF_FIXED_DATA_SIZE
128
```

**定义位置（Location）**：[`subsys/modem/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器点对点协议模块（Modem PPP module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_PPP`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_PPP)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_NET_BUF_DATA_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF_DATA_SIZE)、[`CONFIG_NET_BUF_FIXED_DATA_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF_FIXED_DATA_SIZE)。

<a id="CONFIG_MODEM_STATS"></a>

## 389.32 `CONFIG_MODEM_STATS`

**提示（Prompt）**：调制解调器统计（Modem statistics）

**说明（Help）**

启用调制解调器统计命令行命令（statistics shell commands），跟踪各调制解调器模块的缓冲区使用情况。这些缓冲区大小与应用有关，统计数据有助于调整其大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_MODEM_MODULES
```

**定义位置（Location）**：[`subsys/modem/Kconfig:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_STATS_BUFFER_NAME_SIZE"></a>

## 389.33 `CONFIG_MODEM_STATS_BUFFER_NAME_SIZE`

**提示（Prompt）**：调制解调器统计缓冲区名称的最大字符串长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[8, 64]
```

**定义位置（Location）**：[`subsys/modem/Kconfig:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<a id="CONFIG_MODEM_UBX"></a>

## 389.34 `CONFIG_MODEM_UBX`

**提示（Prompt）**：U-BLOX 调制解调器模块（Modem module）

**说明（Help）**

启用 U-BLOX 调制解调器模块。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_MODULES
```

**主动选择（Selects）**

```text
CONFIG_MODEM_PIPE
```

**被选择（Selected by）**

```text
CONFIG_GNSS_U_BLOX_PROTOCOL
```

**定义位置（Location）**：[`subsys/modem/Kconfig:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_PIPE`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_PIPE)、[`CONFIG_GNSS_U_BLOX_PROTOCOL`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS_U_BLOX_PROTOCOL)。

<a id="CONFIG_MODEM_UBX_LOG_BUFFER"></a>

## 389.35 `CONFIG_MODEM_UBX_LOG_BUFFER`

**提示（Prompt）**：U-BLOX 调制解调器日志缓冲区大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MODEM_UBX && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/modem/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modem/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → U-BLOX 调制解调器模块（Modem module）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_UBX`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_UBX)、[`CONFIG_MODEM_MODULES`](P389_subsys_modem_配置项参考.md#CONFIG_MODEM_MODULES)。

<!-- kconfig-navigation -->

[上一章](P388_subsys_modbus_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P390_subsys_mpipe_配置项参考.md)
