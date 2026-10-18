---
id: learning.zephyr-docs.kconfig-reference.page-425
title: "`subsys/shell`配置项参考（2/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第425章\_`subsys/shell`配置项参考（2/3）

本章翻译官方 Kconfig 数据库中 `subsys/shell` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SHELL_LOG_FORMAT_TIMESTAMP"></a>

## 425.1 `CONFIG_SHELL_LOG_FORMAT_TIMESTAMP`

**提示（Prompt）**：格式化时间戳（Format timestamp）

**说明（Help）**

启用时间戳格式化（Timestamp formatting）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_LOG_BACKEND && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:317`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L317)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_BACKEND`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_LOG_BACKEND)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_LOG_OUTPUT_CRLF_LFONLY"></a>

## 425.2 `CONFIG_SHELL_LOG_OUTPUT_CRLF_LFONLY`

**提示（Prompt）**：日志输出仅使用 LF 换行

**说明（Help）**

将日志输出中的回车加换行（CRLF）转换为单个换行（LF）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_LOG_BACKEND && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:334`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L334)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_BACKEND`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_LOG_BACKEND)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_LOG_OUTPUT_CRLF_NONE"></a>

## 425.3 `CONFIG_SHELL_LOG_OUTPUT_CRLF_NONE`

**提示（Prompt）**：日志输出不处理 CRLF

**说明（Help）**

不修改日志输出中的回车和换行字符（CRLF）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_LOG_BACKEND && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:329`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L329)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_BACKEND`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_LOG_BACKEND)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_LOG_OUTPUT_LEVEL"></a>

## 425.4 `CONFIG_SHELL_LOG_OUTPUT_LEVEL`

**提示（Prompt）**：日志输出级别（Log output level）

**说明（Help）**

在日志输出中包含日志级别（Log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_LOG_BACKEND && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L323)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_BACKEND`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_LOG_BACKEND)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_LOG_OUTPUT_SKIP_SOURCE"></a>

## 425.5 `CONFIG_SHELL_LOG_OUTPUT_SKIP_SOURCE`

**提示（Prompt）**：日志输出省略来源（Skip source）

**说明（Help）**

日志输出时省略来源（Source）信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_LOG_BACKEND && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:345`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L345)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_BACKEND`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_LOG_BACKEND)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_LOG_OUTPUT_THREAD"></a>

## 425.6 `CONFIG_SHELL_LOG_OUTPUT_THREAD`

**提示（Prompt）**：日志输出线程信息（Thread）

**说明（Help）**

启用线程 ID 或名称的日志输出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_LOG_BACKEND && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:339`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L339)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_BACKEND`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_LOG_BACKEND)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_LOG_OUTPUT_TIMESTAMP"></a>

## 425.7 `CONFIG_SHELL_LOG_OUTPUT_TIMESTAMP`

**提示（Prompt）**：日志输出时间戳（Timestamp）

**说明（Help）**

在日志输出中包含时间戳（Timestamp）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_LOG_BACKEND && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:311`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L311)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_LOG_BACKEND`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_LOG_BACKEND)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_METAKEYS"></a>

## 425.8 `CONFIG_SHELL_METAKEYS`

**提示（Prompt）**：元键组合（Metakeys）

**说明（Help）**

启用命令行元键组合（Meta keys）：`Ctrl+A`、`Ctrl+B`、`Ctrl+C`、`Ctrl+D`、`Ctrl+E`、`Ctrl+F`、`Ctrl+K`、`Ctrl+L`、`Ctrl+U`、`Ctrl+W`、`Alt+B` 和 `Alt+F`。关闭命令行回显（Echo）时，这些组合键不生效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L209)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_MINIMAL"></a>

## 425.9 `CONFIG_SHELL_MINIMAL`

**提示（Prompt）**：降低闪存和内存需求的默认配置（Default configuration）

**说明（Help）**

这是一个元配置选项（Meta-configuration option），用于显著减少命令行的闪存（Flash）与内存需求。启用后，Kconfig 默认值会优先减少资源占用，而非提供额外功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**被弱选择（Implied by）**

```text
CONFIG_SHELL_REMOTE_CLI
```

**定义位置（Location）**：[`subsys/shell/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_REMOTE_CLI`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE_CLI)。

<a id="CONFIG_SHELL_MQTT_CONNECT_TIMEOUT_MS"></a>

## 425.10 `CONFIG_SHELL_MQTT_CONNECT_TIMEOUT_MS`

**提示（Prompt）**：MQTT 连接超时（Connect timeout，毫秒）

**说明（Help）**

等待 MQTT 连接确认（Connect acknowledge）的时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
2000
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:348`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L348)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_MQTT_INIT_LOG_LEVEL_DBG"></a>

## 425.11 `CONFIG_SHELL_MQTT_INIT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:392`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L392)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_MQTT_INIT_LOG_LEVEL_DEFAULT"></a>

## 425.12 `CONFIG_SHELL_MQTT_INIT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：系统限制（System limit，`LOG_MAX_LEVEL`）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:389`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L389)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_MQTT_INIT_LOG_LEVEL_ERR"></a>

## 425.13 `CONFIG_SHELL_MQTT_INIT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:401`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L401)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_MQTT_INIT_LOG_LEVEL_INF"></a>

## 425.14 `CONFIG_SHELL_MQTT_INIT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:395`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L395)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_MQTT_INIT_LOG_LEVEL_NONE"></a>

## 425.15 `CONFIG_SHELL_MQTT_INIT_LOG_LEVEL_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:404`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L404)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_MQTT_INIT_LOG_LEVEL_WRN"></a>

## 425.16 `CONFIG_SHELL_MQTT_INIT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:398`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L398)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_MQTT_LISTEN_TIMEOUT_MS"></a>

## 425.17 `CONFIG_SHELL_MQTT_LISTEN_TIMEOUT_MS`

**提示（Prompt）**：MQTT 监听超时（Listen timeout，毫秒）

**说明（Help）**

监听传入数据包的时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:360`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L360)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_MQTT_NEEDS_LARGE_RING_BUFFER"></a>

## 425.18 `CONFIG_SHELL_MQTT_NEEDS_LARGE_RING_BUFFER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

辅助 Kconfig 选项；实现需要大于 32 kB 的环形缓冲区（Ring buffer）时，选择 `RING_BUFFER_LARGE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if CONFIG_SHELL_MQTT_RX_BUF_SIZE > 32767
```

**主动选择（Selects）**

```text
CONFIG_RING_BUFFER_LARGE
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:333`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L333)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MQTT_RX_BUF_SIZE`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MQTT_RX_BUF_SIZE)、[`CONFIG_RING_BUFFER_LARGE`](P198_lib_配置项参考_2.md#CONFIG_RING_BUFFER_LARGE)。

<a id="CONFIG_SHELL_MQTT_RX_BUF_SIZE"></a>

## 425.19 `CONFIG_SHELL_MQTT_RX_BUF_SIZE`

**提示（Prompt）**：接收缓冲区大小（RX buffer size）

**说明（Help）**

用于 MQTT 数据接收的缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:327`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L327)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_MQTT_SERVER_ADDR"></a>

## 425.20 `CONFIG_SHELL_MQTT_SERVER_ADDR`

**提示（Prompt）**：MQTT 服务器地址（Server address）

**说明（Help）**

MQTT 服务器地址（Server address）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"192.168.0.100"
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:305`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L305)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_MQTT_SERVER_PASSWORD"></a>

## 425.21 `CONFIG_SHELL_MQTT_SERVER_PASSWORD`

**提示（Prompt）**：MQTT 服务器密码（Server password）

**说明（Help）**

MQTT 服务器密码（Server password）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:322`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L322)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_MQTT_SERVER_PORT"></a>

## 425.22 `CONFIG_SHELL_MQTT_SERVER_PORT`

**提示（Prompt）**：MQTT 服务器端口（Server port）

**说明（Help）**

MQTT 服务器端口（Server port）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
1883
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:311`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L311)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_MQTT_SERVER_USERNAME"></a>

## 425.23 `CONFIG_SHELL_MQTT_SERVER_USERNAME`

**提示（Prompt）**：MQTT 服务器用户名（Server username）

**说明（Help）**

MQTT 服务器用户名（Server username）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:317`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L317)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_MQTT_TOPIC_RX_ID"></a>

## 425.24 `CONFIG_SHELL_MQTT_TOPIC_RX_ID`

**提示（Prompt）**：MQTT 主题接收标识符（Topic receive identifier）

**说明（Help）**

在 MQTT 主题（Topic）中用作接收标识符的字符串。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"/sh/rx"
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:366`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L366)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_MQTT_TOPIC_TX_ID"></a>

## 425.25 `CONFIG_SHELL_MQTT_TOPIC_TX_ID`

**提示（Prompt）**：MQTT 主题发送标识符（Topic transmit identifier）

**说明（Help）**

在 MQTT 主题（Topic）中用作发送标识符的字符串。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"/sh/tx"
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:372`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L372)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_MQTT_TX_BUF_SIZE"></a>

## 425.26 `CONFIG_SHELL_MQTT_TX_BUF_SIZE`

**提示（Prompt）**：发送缓冲区大小（TX buffer size）

**说明（Help）**

用于 MQTT 数据发送的缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[32, 65535]
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:341`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L341)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_MQTT_WORK_DELAY_MS"></a>

## 425.27 `CONFIG_SHELL_MQTT_WORK_DELAY_MS`

**提示（Prompt）**：MQTT 工作间隔（Work delay，毫秒）

**说明（Help）**

两次 MQTT 工作执行之间的周期，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_MQTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:354`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L354)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → MQTT 后端（backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_MQTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_MQTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_MSG_CMD_NOT_FOUND"></a>

## 425.28 `CONFIG_SHELL_MSG_CMD_NOT_FOUND`

**提示（Prompt）**：命令行中的“未找到命令”提示（`: command not found`）

**说明（Help）**

启用后，命令行打印此消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_MSG_SPECIFY_SUBCOMMAND"></a>

## 425.29 `CONFIG_SHELL_MSG_SPECIFY_SUBCOMMAND`

**提示（Prompt）**：命令行中的“请指定子命令”提示（`Please specify a subcommand.`）

**说明（Help）**

启用后，命令行打印此消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_PRINTF_AUTOFLUSH"></a>

## 425.30 `CONFIG_SHELL_PRINTF_AUTOFLUSH`

**提示（Prompt）**：指定是否自动刷新缓冲区（Flush buffer）

**说明（Help）**

指定命令行打印函数是否自动刷新（Flush）`printf` 缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_PRINTF_BUFF_SIZE"></a>

## 425.31 `CONFIG_SHELL_PRINTF_BUFF_SIZE`

**提示（Prompt）**：命令行打印缓冲区大小（Print buffer size）

**说明（Help）**

`fprintf` 函数使用的文本缓冲区最大大小。工作方式类似 Linux 系统中的标准 I/O（stdio）缓冲，用于减少外设访问调用次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`subsys/shell/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_PROMPT_BUFF_SIZE"></a>

## 425.32 `CONFIG_SHELL_PROMPT_BUFF_SIZE`

**提示（Prompt）**：命令行提示符缓冲区大小（Prompt buffer size）

**说明（Help）**

提示符（Prompt）的最大大小，单位为字节；其中预留一个字节用于字符串结束符（String terminator）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_PROMPT_CHANGE && CONFIG_SHELL
```

**默认值（Defaults）**

```text
10 if CONFIG_SHELL_MINIMAL
20
```

**取值范围（Ranges）**

```text
[2, 40]
```

**定义位置（Location）**：[`subsys/shell/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 允许运行时修改提示符（Prompt）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_PROMPT_CHANGE`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_PROMPT_CHANGE)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_PROMPT_CHANGE"></a>

## 425.33 `CONFIG_SHELL_PROMPT_CHANGE`

**提示（Prompt）**：允许运行时修改提示符（Prompt）

**说明（Help）**

允许在运行时修改命令行提示符（Shell prompt）。启用后，将分配额外 RAM 保存提示符字符串。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_PROMPT_DUMMY"></a>

## 425.34 `CONFIG_SHELL_PROMPT_DUMMY`

**提示（Prompt）**：显示的提示符名称（Prompt Name）

**说明（Help）**

虚拟（DUMMY）后端显示的提示符（Prompt）名称。设置提示符后，命令行初始化时发送两个换行符。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_DUMMY && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"~$ "
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:781`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L781)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 虚拟后端（Dummy backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_DUMMY`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_DUMMY)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_PROMPT_RPMSG"></a>

## 425.35 `CONFIG_SHELL_PROMPT_RPMSG`

**提示（Prompt）**：显示的提示符名称（Prompt Name）

**说明（Help）**

远程处理器消息（RPMsg）后端显示的提示符（Prompt）名称。设置提示符后，命令行初始化时发送两个换行符。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RPMSG && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"ipc:~$ "
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:437`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L437)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RPMSG`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RPMSG)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_PROMPT_RTT"></a>

## 425.36 `CONFIG_SHELL_PROMPT_RTT`

**提示（Prompt）**：显示的提示符名称（Prompt Name）

**说明（Help）**

实时传输（RTT）后端显示的提示符（Prompt）名称。设置提示符后，命令行初始化时发送两个换行符。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"rtt:~$ "
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_PROMPT_SSH"></a>

## 425.37 `CONFIG_SHELL_PROMPT_SSH`

**提示（Prompt）**：显示的提示符名称（Prompt Name）

**说明（Help）**

安全外壳（SSH）后端显示的提示符（Prompt）名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SSH && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"zephyr:~$ "
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:523`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L523)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → SSH 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SSH`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SSH)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_PROMPT_TELNET"></a>

## 425.38 `CONFIG_SHELL_PROMPT_TELNET`

**提示（Prompt）**：显示的提示符名称（Prompt Name）

**说明（Help）**

TELNET 后端显示的提示符（Prompt）名称。设置提示符后，命令行初始化时发送两个换行符。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_TELNET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"~$ "
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:563`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L563)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_TELNET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_PROMPT_UART"></a>

## 425.39 `CONFIG_SHELL_PROMPT_UART`

**提示（Prompt）**：显示的提示符名称（Prompt Name）

**说明（Help）**

UART 后端显示的提示符（Prompt）名称。设置提示符后，命令行初始化时发送两个换行符。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SERIAL && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"uart:~$ "
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → 串行后端（Serial backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SERIAL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_REMOTE"></a>

## 425.40 `CONFIG_SHELL_REMOTE`

**提示（Prompt）**：远程命令行主机（Shell remote host）

**说明（Help）**

启用后，命令行支持远程客户端（Remote client）。来自远程客户端的打印消息在格式化时不进行校验，能够访问主机任意内存。仅当远程客户端核心可信时才应启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:405`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L405)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_REMOTE_CLI"></a>

## 425.41 `CONFIG_SHELL_REMOTE_CLI`

**提示（Prompt）**：远程命令行客户端（Shell remote client）

**说明（Help）**

启用后，命令行作为远程客户端（Remote client）运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPC_SERVICE && CONFIG_SHELL
```

**弱选择（Implies）**

```text
CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:433`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L433)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE`](P348_subsys_ipc_配置项参考.md#CONFIG_IPC_SERVICE)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_REMOTE_CLI_BUF_SIZE"></a>

## 425.42 `CONFIG_SHELL_REMOTE_CLI_BUF_SIZE`

**提示（Prompt）**：内部缓冲区大小（Internal Buffer Size）

**说明（Help）**

用于远程消息（Remote message）的内部缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_REMOTE_CLI && CONFIG_SHELL
```

**默认值（Defaults）**

```text
128 if CONFIG_SHELL_REMOTE_CLI_SKIP_RO_STRINGS
256
```

**取值范围（Ranges）**

```text
[64, 2048]
```

**定义位置（Location）**：[`subsys/shell/Kconfig:460`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L460)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_REMOTE_CLI`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE_CLI)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_REMOTE_CLI_SKIP_RO_STRINGS`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE_CLI_SKIP_RO_STRINGS)。

<a id="CONFIG_SHELL_REMOTE_CLI_KWORK"></a>

## 425.43 `CONFIG_SHELL_REMOTE_CLI_KWORK`

**提示（Prompt）**：使用内核工作项（kwork）上下文执行命令

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_REMOTE_CLI && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/shell/Kconfig:468`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L468)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_REMOTE_CLI`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE_CLI)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_REMOTE_CLI_SKIP_RO_STRINGS"></a>

## 425.44 `CONFIG_SHELL_REMOTE_CLI_SKIP_RO_STRINGS`

**提示（Prompt）**：在远程消息中省略只读字符串（Read-only string）

**说明（Help）**

启用后，远程消息不包含只读字符串（Read-only string），从而节省部分内存，例如栈空间，并减小核间通信（IPC）消息的大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_REMOTE_CLI && CONFIG_SHELL
```

**被弱选择（Implied by）**

```text
CONFIG_RISCV_CORE_NORDIC_VPR
```

**定义位置（Location）**：[`subsys/shell/Kconfig:453`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L453)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_REMOTE_CLI`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE_CLI)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](P290_soc_nordic_配置项参考_2.md#CONFIG_RISCV_CORE_NORDIC_VPR)。

<a id="CONFIG_SHELL_REMOTE_CLI_STACK_SIZE"></a>

## 425.45 `CONFIG_SHELL_REMOTE_CLI_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_SHELL_REMOTE_CLI_KWORK && CONFIG_SHELL_REMOTE_CLI && CONFIG_SHELL
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/shell/Kconfig:472`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L472)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_REMOTE_CLI_KWORK`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE_CLI_KWORK)、[`CONFIG_SHELL_REMOTE_CLI`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE_CLI)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_REMOTE_EP_NAME"></a>

## 425.46 `CONFIG_SHELL_REMOTE_EP_NAME`

**提示（Prompt）**：远程命令行端点名称（Remote endpoint name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
(CONFIG_SHELL_REMOTE || CONFIG_SHELL_REMOTE_CLI) && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"shell_remote"
```

**定义位置（Location）**：[`subsys/shell/Kconfig:440`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L440)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_REMOTE`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE)、[`CONFIG_SHELL_REMOTE_CLI`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE_CLI)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_REMOTE_MULTI_CLI"></a>

## 425.47 `CONFIG_SHELL_REMOTE_MULTI_CLI`

**提示（Prompt）**：多远程客户端（Multiple remote clients）支持

**说明（Help）**

启用后，命令行支持多个远程客户端（Remote client）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_REMOTE && CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:417`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L417)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 远程命令行主机（Shell remote host）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_REMOTE`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_REMOTE_TIMEOUT_MS"></a>

## 425.48 `CONFIG_SHELL_REMOTE_TIMEOUT_MS`

**提示（Prompt）**：远程命令行超时（Remote timeout，毫秒）

**说明（Help）**

核间通信（IPC）的超时时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`subsys/shell/Kconfig:445`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L445)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_REMOTE_TMP_BUF_SIZE"></a>

## 425.49 `CONFIG_SHELL_REMOTE_TMP_BUF_SIZE`

**提示（Prompt）**：远程命令行命令数据的临时缓冲区大小（Temporary buffer size）

**说明（Help）**

命令行主机（Shell host）上的缓冲区大小，用于保存远程命令语法和帮助文本，以及打包发往远程命令行客户端的执行消息（Exec message）。缓冲区过小时，帮助字符串会被截断。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_REMOTE && CONFIG_SHELL
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[16, 2048]
```

**定义位置（Location）**：[`subsys/shell/Kconfig:422`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L422)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 远程命令行主机（Shell remote host）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_REMOTE`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_REMOTE)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_RPMSG_DST_ADDR"></a>

## 425.50 `CONFIG_SHELL_RPMSG_DST_ADDR`

**提示（Prompt）**：远端地址（Remote address）

**说明（Help）**

远程处理器消息（RPMsg）端点的目标地址（Target address）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RPMSG && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
0xffffffff
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:456`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L456)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RPMSG`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RPMSG)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_RPMSG_INIT_LOG_LEVEL_DBG"></a>

## 425.51 `CONFIG_SHELL_RPMSG_INIT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:482`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L482)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_RPMSG_INIT_LOG_LEVEL_DEFAULT"></a>

## 425.52 `CONFIG_SHELL_RPMSG_INIT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：系统限制（System limit，`LOG_MAX_LEVEL`）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:479`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L479)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_RPMSG_INIT_LOG_LEVEL_ERR"></a>

## 425.53 `CONFIG_SHELL_RPMSG_INIT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:491`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L491)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_RPMSG_INIT_LOG_LEVEL_INF"></a>

## 425.54 `CONFIG_SHELL_RPMSG_INIT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:485`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L485)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_RPMSG_INIT_LOG_LEVEL_NONE"></a>

## 425.55 `CONFIG_SHELL_RPMSG_INIT_LOG_LEVEL_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:494`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L494)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_RPMSG_INIT_LOG_LEVEL_WRN"></a>

## 425.56 `CONFIG_SHELL_RPMSG_INIT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:488`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L488)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_RPMSG_MAX_RX"></a>

## 425.57 `CONFIG_SHELL_RPMSG_MAX_RX`

**提示（Prompt）**：接收缓冲区大小（Receive buffer size）

**说明（Help）**

可排队的已接收消息的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RPMSG && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:462`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L462)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RPMSG`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RPMSG)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_RPMSG_SERVICE_NAME"></a>

## 425.58 `CONFIG_SHELL_RPMSG_SERVICE_NAME`

**提示（Prompt）**：服务名称（Service name）

**说明（Help）**

与远程处理器消息（RPMsg）端点关联的服务名称（Service name）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RPMSG && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"rpmsg-tty"
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:444`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L444)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RPMSG`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RPMSG)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_RPMSG_SRC_ADDR"></a>

## 425.59 `CONFIG_SHELL_RPMSG_SRC_ADDR`

**提示（Prompt）**：本地地址（Local address）

**说明（Help）**

远程处理器消息（RPMsg）端点的本地地址（Local address）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RPMSG && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
0xffffffff
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:450`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L450)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RPMsg 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RPMSG`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RPMSG)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_RTT_INIT_LOG_LEVEL_DBG"></a>

## 425.60 `CONFIG_SHELL_RTT_INIT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:259`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L259)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_RTT_INIT_LOG_LEVEL_DEFAULT"></a>

## 425.61 `CONFIG_SHELL_RTT_INIT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：系统限制（System limit，`LOG_MAX_LEVEL`）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_RTT_INIT_LOG_LEVEL_ERR"></a>

## 425.62 `CONFIG_SHELL_RTT_INIT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:268`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L268)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_RTT_INIT_LOG_LEVEL_INF"></a>

## 425.63 `CONFIG_SHELL_RTT_INIT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_RTT_INIT_LOG_LEVEL_NONE"></a>

## 425.64 `CONFIG_SHELL_RTT_INIT_LOG_LEVEL_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:271`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L271)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_RTT_INIT_LOG_LEVEL_WRN"></a>

## 425.65 `CONFIG_SHELL_RTT_INIT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend） → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_RTT_RX_POLL_PERIOD"></a>

## 425.66 `CONFIG_SHELL_RTT_RX_POLL_PERIOD`

**提示（Prompt）**：接收轮询周期（RX polling period，毫秒）

**说明（Help）**

决定轮询实时传输（RTT）接收字节的频率。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_RTT && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → RTT 后端（Backend）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_RTT`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_RTT)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_STACK_SIZE"></a>

## 425.67 `CONFIG_SHELL_STACK_SIZE`

**提示（Prompt）**：命令行线程栈大小（Shell thread stack size）

**说明（Help）**

为每个命令行实例创建的线程的栈大小（Stack size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
4096 if CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED
3168 if CONFIG_OPENTHREAD_SHELL
3072 if CONFIG_64BIT
2048 if CONFIG_MULTITHREADING
0 if !CONFIG_MULTITHREADING
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_arduino_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_arduino_wifi_bt/Kconfig.defconfig)。

```text
4096 if CONFIG_SHELL
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
4096
```

**定义位置（Location）**：[`subsys/shell/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED)、[`CONFIG_OPENTHREAD_SHELL`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SHELL)、[`CONFIG_64BIT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_64BIT)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)。

<a id="CONFIG_SHELL_START_OBSCURED"></a>

## 425.68 `CONFIG_SHELL_START_OBSCURED`

**提示（Prompt）**：回显时显示星号（Asterisk）

**说明（Help）**

启用后，不回显实际字符，而是显示 `*`，用于登录提示（Login prompt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_STATS"></a>

## 425.69 `CONFIG_SHELL_STATS`

**提示（Prompt）**：命令行统计（Shell statistics）

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

**定义位置（Location）**：[`subsys/shell/Kconfig:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_TAB"></a>

## 425.70 `CONFIG_SHELL_TAB`

**提示（Prompt）**：命令行中的 Tab 键支持

**说明（Help）**

允许在命令行中使用 Tab 键，用于提示命令或自动补全（Autocompletion）。此功能会显著增加闪存（Flash）占用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_TAB_AUTOCOMPLETION"></a>

## 425.71 `CONFIG_SHELL_TAB_AUTOCOMPLETION`

**提示（Prompt）**：使用 Tab 键自动补全命令（Command autocompletion）

**说明（Help）**

启用通过 Tab 键自动补全命令及子命令（Subcommand）的功能，可关闭以节省部分闪存（Flash）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_TAB && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 命令行中的 Tab 键支持

**配置项引用（Symbol References）**：[`CONFIG_SHELL_TAB`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_TAB)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_DBG"></a>

## 425.72 `CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:622`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L622)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_DEFAULT"></a>

## 425.73 `CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：系统限制（System limit，`LOG_MAX_LEVEL`）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:619`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L619)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_ERR"></a>

## 425.74 `CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:631`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L631)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_INF"></a>

## 425.75 `CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:625`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L625)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_NONE"></a>

## 425.76 `CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:634`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L634)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_WRN"></a>

## 425.77 `CONFIG_SHELL_TELNET_INIT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:628`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L628)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_TELNET_INIT_PRIORITY"></a>

## 425.78 `CONFIG_SHELL_TELNET_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

Telnet 命令行后端（Shell backend）的初始化优先级数值必须高于套接字服务（Socket service）的初始化优先级，因为套接字服务需要先初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_TELNET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
95
```

**取值范围（Ranges）**

```text
[0, 99]
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:554`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L554)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_TELNET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_TELNET_LINE_BUF_SIZE"></a>

## 425.79 `CONFIG_SHELL_TELNET_LINE_BUF_SIZE`

**提示（Prompt）**：Telnet 行缓冲区大小（Line buffer size）

**说明（Help）**

调整向网络发送前保存命令行输出行的缓冲区大小。输出行可以超过此大小；达到该大小时即开始发送。应根据预期输出类型选择：大量短行适合减小该值，较长的行则适合增大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_TELNET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:577`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L577)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_TELNET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_TELNET_LOG_MESSAGE_QUEUE_SIZE"></a>

## 425.80 `CONFIG_SHELL_TELNET_LOG_MESSAGE_QUEUE_SIZE`

**提示（Prompt）**：日志消息队列大小（Log message queue size）

**说明（Help）**

用于保存待命令行线程处理的日志消息的缓冲区大小。队列过小可能阻塞日志线程（Logger thread），参见 `$(module)_LOG_MESSAGE_QUEUE_TIMEOUT`；若命令行传输较慢而队列过大，可能因全部日志消息都已排入该队列，导致后续日志被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_TELNET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/shell/Kconfig.template.shell_log_queue_size:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig.template.shell_log_queue_size#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_TELNET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_TELNET_LOG_MESSAGE_QUEUE_TIMEOUT"></a>

## 425.81 `CONFIG_SHELL_TELNET_LOG_MESSAGE_QUEUE_TIMEOUT`

**提示（Prompt）**：日志消息丢弃超时（Drop timeout，毫秒）

**说明（Help）**

待处理日志消息队列满时，先等待指定时间；等待后仍满，则丢弃最旧日志消息。-1 表示一直等待。此期间日志线程（Logger thread）被阻塞，较长超时会影响其他日志后端，必须谨慎使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_TELNET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
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

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_TELNET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_TELNET_PORT"></a>

## 425.82 `CONFIG_SHELL_TELNET_PORT`

**提示（Prompt）**：Telnet 端口号（Port number）

**说明（Help）**

配置 Telnet 绑定的端口（Port）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_TELNET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
23
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:570`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L570)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_TELNET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_TELNET_SEND_TIMEOUT"></a>

## 425.83 `CONFIG_SHELL_TELNET_SEND_TIMEOUT`

**提示（Prompt）**：Telnet 行发送超时（Line send timeout）

**说明（Help）**

调整计时器时长；当行缓冲区（Line buffer）非空但尚未遇到换行符（Line feed）时，该计时器生效。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_TELNET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:589`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L589)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_TELNET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_TELNET_SUPPORT_COMMAND"></a>

## 425.84 `CONFIG_SHELL_TELNET_SUPPORT_COMMAND`

**提示（Prompt）**：添加 Telnet 命令（IAC）支持［实验性，Experimental］

**说明（Help）**

目前支持很有限，通常没有必要启用；如果将来证明有需要，可以进一步扩展。现有实现支持回显（Echo）和逐字符模式（Character-at-a-time），从而启用命令行历史与行编辑功能。注意：Telnet 客户端每输入一个字符就发送一个 TCP 数据包，因此会增加网络使用量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_TELNET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_SMOKE_TESTS
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:596`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L596)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → TELNET 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_TELNET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_NXP_WIFI_SMOKE_TESTS`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SMOKE_TESTS)。

<a id="CONFIG_SHELL_THREAD_PRIORITY"></a>

## 425.85 `CONFIG_SHELL_THREAD_PRIORITY`

**提示（Prompt）**：命令行线程优先级（Shell thread priority）

**说明（Help）**

设置命令行（Shell）的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_THREAD_PRIORITY_OVERRIDE && CONFIG_SHELL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/shell/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 覆盖默认命令行线程优先级（Default shell thread priority）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_THREAD_PRIORITY_OVERRIDE`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_THREAD_PRIORITY_OVERRIDE)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_THREAD_PRIORITY_OVERRIDE"></a>

## 425.86 `CONFIG_SHELL_THREAD_PRIORITY_OVERRIDE`

**提示（Prompt）**：覆盖默认命令行线程优先级（Default shell thread priority）

**说明（Help）**

允许修改命令行线程优先级（Shell thread priority）的默认值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**被选择（Selected by）**

```text
CONFIG_ZTEST_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_ZTEST_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_SHELL)。

<a id="CONFIG_SHELL_TX_TIMEOUT_MS"></a>

## 425.87 `CONFIG_SHELL_TX_TIMEOUT_MS`

**提示（Prompt）**：命令行发送超时（Shell TX timeout，毫秒）

**说明（Help）**

命令行发送互斥锁（TX mutex）的超时，单位为毫秒，用于避免从命令行处理线程之外调用时发生死锁（Deadlock）。使用命令行日志后端（Shell log backend）时，应采用更长超时，避免日志处理导致超时。原文规定 0 表示不超时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
500 if CONFIG_SHELL_LOG_BACKEND
50
```

**定义位置（Location）**：[`subsys/shell/Kconfig:381`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L381)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_LOG_BACKEND`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_LOG_BACKEND)。

<a id="CONFIG_SHELL_VT100_COLORS"></a>

## 425.88 `CONFIG_SHELL_VT100_COLORS`

**提示（Prompt）**：命令行颜色（Shell colors）

**说明（Help）**

启用后，命令行使用 VT100 颜色，例如以红色打印错误。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_VT100_COMMANDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
y if !CONFIG_SHELL_MINIMAL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → 命令行中的 VT100 命令

**配置项引用（Symbol References）**：[`CONFIG_SHELL_VT100_COMMANDS`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_VT100_COMMANDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)。

<a id="CONFIG_SHELL_VT100_COMMANDS"></a>

## 425.89 `CONFIG_SHELL_VT100_COMMANDS`

**提示（Prompt）**：命令行中的 VT100 命令

**说明（Help）**

启用命令行中的 VT100 命令，例如光标定位（Cursor positioning）、清屏等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_AUDIO_DMIC_SHELL
```

**定义位置（Location）**：[`subsys/shell/Kconfig:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_AUDIO_DMIC_SHELL`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_SHELL)。

<a id="CONFIG_SHELL_WEBSOCKET_BACKEND_COUNT"></a>

## 425.90 `CONFIG_SHELL_WEBSOCKET_BACKEND_COUNT`

**提示（Prompt）**：支持的网页控制台会话（Webconsole session）数量

**说明（Help）**

每个连接都会占用内存，应根据需要选择数量。每个控制台会话还需要配置唯一的 HTTP 端点（Endpoint）。如果 WebSocket 控制台只有一个 HTTP 端点，将此值设为 2，可让后连接的控制台会话替换之前的会话；设为 1 时，后续连接的网页控制台会话会失败。如果有多个 HTTP 端点，则应相应增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_WEBSOCKET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:665`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L665)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_WEBSOCKET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_WEBSOCKET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_WEBSOCKET_ENDPOINT_URL"></a>

## 425.91 `CONFIG_SHELL_WEBSOCKET_ENDPOINT_URL`

**提示（Prompt）**：WebSocket 端点 URL（Endpoint URL）

**说明（Help）**

客户端应连接的 HTTP 端点 URL（Endpoint URL）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_WEBSOCKET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
"console"
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:686`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L686)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_WEBSOCKET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_WEBSOCKET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_WEBSOCKET_INIT_LOG_LEVEL_DBG"></a>

## 425.92 `CONFIG_SHELL_WEBSOCKET_INIT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:741`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L741)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_WEBSOCKET_INIT_LOG_LEVEL_DEFAULT"></a>

## 425.93 `CONFIG_SHELL_WEBSOCKET_INIT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：系统限制（System limit，`LOG_MAX_LEVEL`）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:738`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L738)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_WEBSOCKET_INIT_LOG_LEVEL_ERR"></a>

## 425.94 `CONFIG_SHELL_WEBSOCKET_INIT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:750`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L750)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_WEBSOCKET_INIT_LOG_LEVEL_INF"></a>

## 425.95 `CONFIG_SHELL_WEBSOCKET_INIT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:744`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L744)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_WEBSOCKET_INIT_LOG_LEVEL_NONE"></a>

## 425.96 `CONFIG_SHELL_WEBSOCKET_INIT_LOG_LEVEL_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:753`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L753)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_WEBSOCKET_INIT_LOG_LEVEL_WRN"></a>

## 425.97 `CONFIG_SHELL_WEBSOCKET_INIT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:747`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L747)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。 → 初始日志级别限制（Initial log level limit）

<a id="CONFIG_SHELL_WEBSOCKET_IP_ADDR"></a>

## 425.98 `CONFIG_SHELL_WEBSOCKET_IP_ADDR`

**提示（Prompt）**：WebSocket 的 IP 监听地址（Listen address）

**说明（Help）**

配置 HTTP 服务器监听的 IP 地址和网络接口。留空时监听全部网络接口（Network interface）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_WEBSOCKET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:692`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L692)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_WEBSOCKET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_WEBSOCKET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_WEBSOCKET_LINE_BUF_SIZE"></a>

## 425.99 `CONFIG_SHELL_WEBSOCKET_LINE_BUF_SIZE`

**提示（Prompt）**：WebSocket 行缓冲区大小（Line buffer size）

**说明（Help）**

调整向网络发送前保存命令行输出行的缓冲区大小。输出行可以超过此大小；达到该大小时即开始发送。应根据预期输出类型选择：大量短行适合减小该值，较长的行则适合增大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_WEBSOCKET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:708`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L708)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_WEBSOCKET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_WEBSOCKET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_WEBSOCKET_LOG_MESSAGE_QUEUE_SIZE"></a>

## 425.100 `CONFIG_SHELL_WEBSOCKET_LOG_MESSAGE_QUEUE_SIZE`

**提示（Prompt）**：日志消息队列大小（Log message queue size）

**说明（Help）**

用于保存待命令行线程处理的日志消息的缓冲区大小。队列过小可能阻塞日志线程（Logger thread），参见 `$(module)_LOG_MESSAGE_QUEUE_TIMEOUT`；若命令行传输较慢而队列过大，可能因全部日志消息都已排入该队列，导致后续日志被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_WEBSOCKET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/shell/Kconfig.template.shell_log_queue_size:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig.template.shell_log_queue_size#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_WEBSOCKET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_WEBSOCKET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<!-- kconfig-navigation -->

[上一章](P424_subsys_shell_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P426_subsys_shell_配置项参考_3.md)
