---
id: learning.zephyr-docs.kconfig-reference.page-426
title: "`subsys/shell`配置项参考（3/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第426章\_`subsys/shell`配置项参考（3/3）

本章翻译官方 Kconfig 数据库中 `subsys/shell` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SHELL_WEBSOCKET_LOG_MESSAGE_QUEUE_TIMEOUT"></a>

## 426.1 `CONFIG_SHELL_WEBSOCKET_LOG_MESSAGE_QUEUE_TIMEOUT`

**提示（Prompt）**：日志消息丢弃超时（Drop timeout，毫秒）

**说明（Help）**

待处理日志消息队列满时，先等待指定时间；等待后仍满，则丢弃最旧日志消息。-1 表示一直等待。此期间日志线程（Logger thread）被阻塞，较长超时会影响其他日志后端，必须谨慎使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_WEBSOCKET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
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

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_WEBSOCKET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_WEBSOCKET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_WEBSOCKET_PORT"></a>

## 426.2 `CONFIG_SHELL_WEBSOCKET_PORT`

**提示（Prompt）**：WebSocket 端口号（Port number）

**说明（Help）**

配置 WebSocket 绑定的端口（Port）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_WEBSOCKET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
443 if CONFIG_NET_SOCKETS_SOCKOPT_TLS
80
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:700`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L700)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_WEBSOCKET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_WEBSOCKET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)。

<a id="CONFIG_SHELL_WEBSOCKET_PROMPT"></a>

## 426.3 `CONFIG_SHELL_WEBSOCKET_PROMPT`

**提示（Prompt）**：显示的提示符名称（Prompt Name）

**说明（Help）**

WebSocket 后端显示的提示符（Prompt）名称。设置提示符后，命令行初始化时发送两个换行符。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_WEBSOCKET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:679`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L679)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_WEBSOCKET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_WEBSOCKET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_WEBSOCKET_SEND_TIMEOUT"></a>

## 426.4 `CONFIG_SHELL_WEBSOCKET_SEND_TIMEOUT`

**提示（Prompt）**：WebSocket 行发送超时（Line send timeout）

**说明（Help）**

调整计时器时长；当行缓冲区（Line buffer）非空但尚未遇到换行符（Line feed）时，该计时器生效。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_WEBSOCKET && CONFIG_SHELL_BACKENDS && CONFIG_SHELL
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/shell/backends/Kconfig.backends:720`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/Kconfig.backends#L720)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell） → Shell后端（Shell Backends） → WebSocket 后端（backend）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_WEBSOCKET`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKEND_WEBSOCKET)、[`CONFIG_SHELL_BACKENDS`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL_BACKENDS)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)。

<a id="CONFIG_SHELL_WILDCARD"></a>

## 426.5 `CONFIG_SHELL_WILDCARD`

**提示（Prompt）**：命令行通配符（Wildcard）支持

**说明（Help）**

允许在命令行中使用通配符（Wildcard）`*` 和 `?`。

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
CONFIG_POSIX_C_LIB_EXT
```

**定义位置（Location）**：[`subsys/shell/Kconfig:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/Kconfig#L156)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_SHELL_MINIMAL`](P425_subsys_shell_配置项参考_2.md#CONFIG_SHELL_MINIMAL)、[`CONFIG_POSIX_C_LIB_EXT`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_C_LIB_EXT)。

<a id="CONFIG_ZYCLICTEST_SHELL"></a>

## 426.6 `CONFIG_ZYCLICTEST_SHELL`

**提示（Prompt）**：Zyclictest 命令行（Shell）

**说明（Help）**

提供延迟测量（Latency measurement）命令，测量定时器唤醒中断服务程序（ISR）和线程时的延迟。目标应用在前台运行时，可在后台收集数据；按需开启，在生产应用的真实运行条件下测量最坏情况延迟（Worst-case latency）。由此可判断中断或抢占锁（Preemption lock）等是否阻止应用运行。此工具受到 Linux `cyclictest` 的启发。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER && CONFIG_SHELL
```

**主动选择（Selects）**

```text
CONFIG_POSIX_C_LIB_EXT
```

**定义位置（Location）**：[`subsys/shell/modules/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 命令行解释器（Shell）

**配置项引用（Symbol References）**：[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_POSIX_C_LIB_EXT`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_C_LIB_EXT)。

<!-- kconfig-navigation -->

[上一章](P425_subsys_shell_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P427_subsys_sip_svc_配置项参考.md)
