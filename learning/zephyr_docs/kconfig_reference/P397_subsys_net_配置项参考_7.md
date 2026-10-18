---
id: learning.zephyr-docs.kconfig-reference.page-397
title: "`subsys/net`配置项参考（7/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第397章\_`subsys/net`配置项参考（7/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_OFF"></a>

## 397.1 `CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager） → 连接管理器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_WRN"></a>

## 397.2 `CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager） → 连接管理器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONNECTION_MANAGER_MONITOR_PRIORITY"></a>

## 397.3 `CONFIG_NET_CONNECTION_MANAGER_MONITOR_PRIORITY`

**提示（Prompt）**：监控线程初始优先级（starting priority）

**说明（Help）**

设置 `conn_mgr_monitor` 线程的初始优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONNECTION_MANAGER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 99]
```

**定义位置（Location）**：[`subsys/net/conn_mgr/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/conn_mgr/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONNECTION_MANAGER_MONITOR_STACK_SIZE"></a>

## 397.4 `CONFIG_NET_CONNECTION_MANAGER_MONITOR_STACK_SIZE`

**提示（Prompt）**：conn_mgr_monitor 线程分配的栈大小

**说明（Help）**

设置连接管理器（connection manager）进行连接监控所用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONNECTION_MANAGER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/net/conn_mgr/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/conn_mgr/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONN_LOG_LEVEL_CHOICE"></a>

## 397.5 `CONFIG_NET_CONN_LOG_LEVEL_CHOICE`

**提示（Prompt）**：UDP／TCP 连接处理日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_CONN_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_CONN_LOG_LEVEL_OFF
CONFIG_NET_CONN_LOG_LEVEL_ERR
CONFIG_NET_CONN_LOG_LEVEL_WRN
CONFIG_NET_CONN_LOG_LEVEL_INF
CONFIG_NET_CONN_LOG_LEVEL_DBG
CONFIG_NET_CONN_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CONN_LOG_LEVEL_DEFAULT`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONN_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_CONN_LOG_LEVEL_OFF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONN_LOG_LEVEL_OFF)、[`CONFIG_NET_CONN_LOG_LEVEL_ERR`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONN_LOG_LEVEL_ERR)、[`CONFIG_NET_CONN_LOG_LEVEL_WRN`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONN_LOG_LEVEL_WRN)、[`CONFIG_NET_CONN_LOG_LEVEL_INF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONN_LOG_LEVEL_INF)、[`CONFIG_NET_CONN_LOG_LEVEL_DBG`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONN_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_CONN_LOG_LEVEL_DBG"></a>

## 397.6 `CONFIG_NET_CONN_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → UDP／TCP 连接处理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONN_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONN_LOG_LEVEL_DEFAULT"></a>

## 397.7 `CONFIG_NET_CONN_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → UDP／TCP 连接处理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONN_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONN_LOG_LEVEL_ERR"></a>

## 397.8 `CONFIG_NET_CONN_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → UDP／TCP 连接处理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONN_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONN_LOG_LEVEL_INF"></a>

## 397.9 `CONFIG_NET_CONN_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → UDP／TCP 连接处理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONN_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONN_LOG_LEVEL_OFF"></a>

## 397.10 `CONFIG_NET_CONN_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → UDP／TCP 连接处理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONN_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONN_LOG_LEVEL_WRN"></a>

## 397.11 `CONFIG_NET_CONN_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → UDP／TCP 连接处理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONN_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONN_PACKET_CLONE_TIMEOUT"></a>

## 397.12 `CONFIG_NET_CONN_PACKET_CLONE_TIMEOUT`

**提示（Prompt）**：克隆数据包超时（毫秒）

**说明（Help）**

为网络连接克隆数据包（cloning a packet）时的最长等待时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:553`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L553)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONTEXT_CHECK"></a>

## 397.13 `CONFIG_NET_CONTEXT_CHECK`

**提示（Prompt）**：调用 net_context 函数时检查选项

**说明（Help）**

若确定传给 `net_context...()` 函数的选项正确，可禁用检查以节省内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:590`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L590)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONTEXT_CLAMP_PORT_RANGE"></a>

## 397.14 `CONFIG_NET_CONTEXT_CLAMP_PORT_RANGE`

**提示（Prompt）**：允许 net_context 缩小全局本地端口范围

**说明（Help）**

设置或获取每个上下文（context）的默认本地端口范围，可为指定上下文缩小全局本地 UDP／TCP 端口范围。通常通过 `IP_LOCAL_PORT_RANGE` 套接字选项设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_UDP || CONFIG_NET_TCP) && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:698`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L698)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONTEXT_DSCP_ECN"></a>

## 397.15 `CONFIG_NET_CONTEXT_DSCP_ECN`

**提示（Prompt）**：允许为 net_context 设置 DSCP／ECN IP 属性

**说明（Help）**

允许在 `net_context` 上设置区分服务（Differentiated Services）与显式拥塞通知（Explicit Congestion Notification，ECN）值。通过该上下文发送数据包时，将这些值写入 IPv4／IPv6 头部。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IP_DSCP_ECN && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:652`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L652)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_IP_DSCP_ECN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IP_DSCP_ECN)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONTEXT_LINGER"></a>

## 397.16 `CONFIG_NET_CONTEXT_LINGER`

**提示（Prompt）**：为 net_context 添加 SO_LINGER 支持

**说明（Help）**

允许在 TCP 套接字上设置 `SO_LINGER`。启用延留（linger）且超时为零时，关闭套接字会发送 RST 段中止连接，而不是正常发送 FIN 关闭。启用且超时非零时，`close()` 阻塞，直到协议栈完成关闭或指定秒数到期；超时则通过 RST 中止连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:641`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L641)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE"></a>

## 397.17 `CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：网络上下文分配日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_CONTEXT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_CONTEXT_LOG_LEVEL_OFF
CONFIG_NET_CONTEXT_LOG_LEVEL_ERR
CONFIG_NET_CONTEXT_LOG_LEVEL_WRN
CONFIG_NET_CONTEXT_LOG_LEVEL_INF
CONFIG_NET_CONTEXT_LOG_LEVEL_DBG
CONFIG_NET_CONTEXT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CONTEXT_LOG_LEVEL_DEFAULT`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_CONTEXT_LOG_LEVEL_OFF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_LOG_LEVEL_OFF)、[`CONFIG_NET_CONTEXT_LOG_LEVEL_ERR`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_LOG_LEVEL_ERR)、[`CONFIG_NET_CONTEXT_LOG_LEVEL_WRN`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_LOG_LEVEL_WRN)、[`CONFIG_NET_CONTEXT_LOG_LEVEL_INF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_LOG_LEVEL_INF)、[`CONFIG_NET_CONTEXT_LOG_LEVEL_DBG`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_CONTEXT_LOG_LEVEL_DBG"></a>

## 397.18 `CONFIG_NET_CONTEXT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络上下文分配日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONTEXT_LOG_LEVEL_DEFAULT"></a>

## 397.19 `CONFIG_NET_CONTEXT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络上下文分配日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONTEXT_LOG_LEVEL_ERR"></a>

## 397.20 `CONFIG_NET_CONTEXT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络上下文分配日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONTEXT_LOG_LEVEL_INF"></a>

## 397.21 `CONFIG_NET_CONTEXT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络上下文分配日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONTEXT_LOG_LEVEL_OFF"></a>

## 397.22 `CONFIG_NET_CONTEXT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络上下文分配日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONTEXT_LOG_LEVEL_WRN"></a>

## 397.23 `CONFIG_NET_CONTEXT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络上下文分配日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONTEXT_NET_PKT_POOL"></a>

## 397.24 `CONFIG_NET_CONTEXT_NET_PKT_POOL`

**提示（Prompt）**：按上下文配置 net_buf 发送池（TX pool）

**说明（Help）**

启用后，可为每个上下文精细配置网络数据发送所用的数据包池。应用应使用 `NET_PKT_TX_POOL_DEFINE()` 和 `NET_PKT_DATA_POOL_DEFINE()` 宏定义池，并通过 `net_context_setup_pools()` 绑定到目标上下文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_TCP && CONFIG_NET_6LO
```

**被选择（Selected by）**

```text
CONFIG_NET_CAPTURE
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:572`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L572)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_6LO`](P395_subsys_net_配置项参考_5.md#CONFIG_NET_6LO)、[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)。

<a id="CONFIG_NET_CONTEXT_PRIORITY"></a>

## 397.25 `CONFIG_NET_CONTEXT_PRIORITY`

**提示（Prompt）**：为 net_context 添加优先级支持（priority）

**说明（Help）**

允许为网络流量设置优先级，还需要流量类别（traffic class）支持才能按预期工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_PTP
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:597`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L597)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP)。

<a id="CONFIG_NET_CONTEXT_RCVBUF"></a>

## 397.26 `CONFIG_NET_CONTEXT_RCVBUF`

**提示（Prompt）**：为 net_context 添加接收缓冲区支持（RCVBUF）

**说明（Help）**

允许为每个套接字定义接收缓冲区最大大小，默认值由 `CONFIG_NET_TCP_MAX_RECV_WINDOW_SIZE` 设置。对于 TCP，`rcvbuf` 决定接收窗口大小（receive window size）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:627`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L627)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONTEXT_RCVTIMEO"></a>

## 397.27 `CONFIG_NET_CONTEXT_RCVTIMEO`

**提示（Prompt）**：为 net_context 添加接收超时支持（RCVTIMEO）

**说明（Help）**

允许网络数据包接收超时，应用可在运行时配置超时时间。网络套接字通过 `setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, ...)` 逐个配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_ZPERF
CONFIG_NET_ZPERF_IPERF3
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:611`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L611)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_ZPERF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF)、[`CONFIG_NET_ZPERF_IPERF3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_IPERF3)。

<a id="CONFIG_NET_CONTEXT_RECV_HOPLIMIT"></a>

## 397.28 `CONFIG_NET_CONTEXT_RECV_HOPLIMIT`

**提示（Prompt）**：为 net_context 添加接收跳数限制或 TTL 支持

**说明（Help）**

允许在套接字上设置 `IPV6_RECVHOPLIMIT` 或 `IP_RECVTTL`，获取 IPv6 跳数限制（hop limit）或 IPv4 生存时间（TTL）的附加信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:683`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L683)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONTEXT_RECV_PKTINFO"></a>

## 397.29 `CONFIG_NET_CONTEXT_RECV_PKTINFO`

**提示（Prompt）**：为 net_context 添加接收数据包信息支持（PKTINFO）

**说明（Help）**

允许在套接字上设置 `IP_PKTINFO` 或 `IPV6_RECVPKTINFO`，获取收到的数据的附加信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_COAP_SERVER
CONFIG_PTP_UDP_IPV6_PROTOCOL
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:675`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L675)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_PTP_UDP_IPV6_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_UDP_IPV6_PROTOCOL)。

<a id="CONFIG_NET_CONTEXT_REUSEADDR"></a>

## 397.30 `CONFIG_NET_CONTEXT_REUSEADDR`

**提示（Prompt）**：为 net_context 添加地址复用支持（REUSEADDR）

**说明（Help）**

允许设置 `SO_REUSEADDR` 标志，使多个套接字可绑定到同一本地 IP 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_TCP || CONFIG_NET_UDP
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:661`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L661)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)。

<a id="CONFIG_NET_CONTEXT_REUSEPORT"></a>

## 397.31 `CONFIG_NET_CONTEXT_REUSEPORT`

**提示（Prompt）**：为 net_context 添加端口复用支持（REUSEPORT）

**说明（Help）**

允许设置 `SO_REUSEPORT` 标志，使多个套接字可绑定到同一本地 IP 地址和端口组合。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_TCP || CONFIG_NET_UDP
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:668`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L668)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)。

<a id="CONFIG_NET_CONTEXT_SNDBUF"></a>

## 397.32 `CONFIG_NET_CONTEXT_SNDBUF`

**提示（Prompt）**：为 net_context 添加发送缓冲区支持（SNDBUF）

**说明（Help）**

允许为每个套接字定义发送缓冲区最大大小。对于 TCP，`sndbuf` 决定 TCP 层排队数据的总大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:634`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L634)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONTEXT_SNDTIMEO"></a>

## 397.33 `CONFIG_NET_CONTEXT_SNDTIMEO`

**提示（Prompt）**：为 net_context 添加发送超时支持（SNDTIMEO）

**说明（Help）**

允许网络数据包发送超时，应用可在运行时配置超时时间。网络套接字通过 `setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO, ...)` 逐个配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:619`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L619)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONTEXT_SYNC_RECV"></a>

## 397.34 `CONFIG_NET_CONTEXT_SYNC_RECV`

**提示（Prompt）**：支持 net_context_recv() API 的同步功能

**说明（Help）**

若仅以超时为 `0` 的异步方式调用 `net_context_recv()`，可禁用同步支持以节省内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:583`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L583)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONTEXT_TIMESTAMPING"></a>

## 397.35 `CONFIG_NET_CONTEXT_TIMESTAMPING`

**提示（Prompt）**：为 net_context 添加时间戳支持（TIMESTAMPING）

**说明（Help）**

允许在套接字上设置 `TIMESTAMPING`，将网络数据包时间戳添加到 `net_pkt` 结构体。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_UDP && CONFIG_NET_PKT_TIMESTAMP
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:691`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L691)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_PKT_TIMESTAMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_TIMESTAMP)。

<a id="CONFIG_NET_CONTEXT_TXTIME"></a>

## 397.36 `CONFIG_NET_CONTEXT_TXTIME`

**提示（Prompt）**：为 net_context 添加发送时刻支持（TXTIME）

**说明（Help）**

允许指定出站网络数据包应在何时发送。发送时间（TX time）信息应放在 `sendmsg` 调用的辅助数据（ancillary data）字段中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_PKT_TXTIME
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:603`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L603)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_TXTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_TXTIME)。

<a id="CONFIG_NET_CORE_LOG_LEVEL_CHOICE"></a>

## 397.37 `CONFIG_NET_CORE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：核心 IP 协议栈日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_CORE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_CORE_LOG_LEVEL_OFF
CONFIG_NET_CORE_LOG_LEVEL_ERR
CONFIG_NET_CORE_LOG_LEVEL_WRN
CONFIG_NET_CORE_LOG_LEVEL_INF
CONFIG_NET_CORE_LOG_LEVEL_DBG
CONFIG_NET_CORE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CORE_LOG_LEVEL_DEFAULT`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CORE_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_CORE_LOG_LEVEL_OFF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CORE_LOG_LEVEL_OFF)、[`CONFIG_NET_CORE_LOG_LEVEL_ERR`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CORE_LOG_LEVEL_ERR)、[`CONFIG_NET_CORE_LOG_LEVEL_WRN`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CORE_LOG_LEVEL_WRN)、[`CONFIG_NET_CORE_LOG_LEVEL_INF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CORE_LOG_LEVEL_INF)、[`CONFIG_NET_CORE_LOG_LEVEL_DBG`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CORE_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_CORE_LOG_LEVEL_DBG"></a>

## 397.38 `CONFIG_NET_CORE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 核心 IP 协议栈日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CORE_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CORE_LOG_LEVEL_DEFAULT"></a>

## 397.39 `CONFIG_NET_CORE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 核心 IP 协议栈日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CORE_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CORE_LOG_LEVEL_ERR"></a>

## 397.40 `CONFIG_NET_CORE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 核心 IP 协议栈日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CORE_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CORE_LOG_LEVEL_INF"></a>

## 397.41 `CONFIG_NET_CORE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 核心 IP 协议栈日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CORE_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CORE_LOG_LEVEL_OFF"></a>

## 397.42 `CONFIG_NET_CORE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 核心 IP 协议栈日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CORE_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CORE_LOG_LEVEL_WRN"></a>

## 397.43 `CONFIG_NET_CORE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CORE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 核心 IP 协议栈日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CORE_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CORE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DEBUG_L2_IEEE802154_DISPLAY_PACKET"></a>

## 397.44 `CONFIG_NET_DEBUG_L2_IEEE802154_DISPLAY_PACKET`

**提示（Prompt）**：IEEE 802.15.4 数据包显示（packet display）

**说明（Help）**

打印入站和出站 IEEE 802.15.4 数据包，输出极其详细。仅在明确了解用途时启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_L2_IEEE802154 && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_L2_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DEBUG_L2_IEEE802154_DISPLAY_PACKET_FULL"></a>

## 397.45 `CONFIG_NET_DEBUG_L2_IEEE802154_DISPLAY_PACKET_FULL`

**提示（Prompt）**：同时打印接收和发送数据包（RX/TX）

**说明（Help）**

同时打印收到和发出的数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 数据包显示（packet display） → 选择要打印的数据包类型

<a id="CONFIG_NET_DEBUG_L2_IEEE802154_DISPLAY_PACKET_RX"></a>

## 397.46 `CONFIG_NET_DEBUG_L2_IEEE802154_DISPLAY_PACKET_RX`

**提示（Prompt）**：仅打印接收数据包（RX）

**说明（Help）**

只打印收到的数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 数据包显示（packet display） → 选择要打印的数据包类型

<a id="CONFIG_NET_DEBUG_L2_IEEE802154_DISPLAY_PACKET_TX"></a>

## 397.47 `CONFIG_NET_DEBUG_L2_IEEE802154_DISPLAY_PACKET_TX`

**提示（Prompt）**：仅打印发送数据包（TX）

**说明（Help）**

只打印发出的数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/l2/ieee802154/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ieee802154/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → IEEE 802.15.4 无线电（Radio） → IEEE 802.15.4 数据包显示（packet display） → 选择要打印的数据包类型

<a id="CONFIG_NET_DEBUG_MGMT_EVENT_STACK"></a>

## 397.48 `CONFIG_NET_DEBUG_MGMT_EVENT_STACK`

**提示（Prompt）**：网络管理事件核心的栈分析输出（Net MGMT）

**说明（Help）**

添加调试消息，报告网络管理（Net MGMT）事件栈已使用的空间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT_EVENT_THREAD && CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_INIT_STACKS
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT_THREAD)、[`CONFIG_NET_MGMT_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_INIT_STACKS`](P001_kernel_配置项参考_1.md#CONFIG_INIT_STACKS)。

<a id="CONFIG_NET_DEBUG_NET_PKT_ALLOC"></a>

## 397.49 `CONFIG_NET_DEBUG_NET_PKT_ALLOC`

**提示（Prompt）**：调试每次网络数据包及缓冲区分配

**说明（Help）**

逐次打印网络数据包和缓冲区的分配、释放情况。输出可能很多，因此默认禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_PKT_LOG_LEVEL_DBG
```

**被选择（Selected by）**

```text
CONFIG_NET_DEBUG_NET_PKT_NON_FRAGILE_ACCESS
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.debug:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.debug#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_LOG_LEVEL_DBG)、[`CONFIG_NET_DEBUG_NET_PKT_NON_FRAGILE_ACCESS`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEBUG_NET_PKT_NON_FRAGILE_ACCESS)。

<a id="CONFIG_NET_DEBUG_NET_PKT_EXTERNALS"></a>

## 397.50 `CONFIG_NET_DEBUG_NET_PKT_EXTERNALS`

**提示（Prompt）**：外部网络数据包分配数量（external allocations）

**说明（Help）**

用户专用池中的外部 `net_pkt` 对象数量。为跟踪内存分配预留空间时使用此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.debug:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.debug#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DEBUG_NET_PKT_NON_FRAGILE_ACCESS"></a>

## 397.51 `CONFIG_NET_DEBUG_NET_PKT_NON_FRAGILE_ACCESS`

**提示（Prompt）**：释放时重置数据包游标，降低后续读写的脆弱性

**说明（Help）**

只有调试难以定位的缺陷时才可使用。释放数据包时重置其游标（cursor），使后续读写不发生段错误，而是直接退出，希望有助于定位是谁、在哪里提前释放了数据包。除正在主动调试外，绝不要设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_DEBUG_NET_PKT_ALLOC
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.debug:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.debug#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_DEBUG_NET_PKT_ALLOC`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEBUG_NET_PKT_ALLOC)。

<a id="CONFIG_NET_DEFAULT_IF"></a>

## 397.52 `CONFIG_NET_DEFAULT_IF`

**提示（Prompt）**：默认网络接口（Default Network Interface）

**说明（Help）**

系统启用多个接口时，用户应能选择默认接口；否则，第一个接口作为默认接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_DEFAULT_IF_DUMMY if CONFIG_NET_TEST
CONFIG_NET_DEFAULT_IF_FIRST
```

**可选项（Choices）**

```text
CONFIG_NET_DEFAULT_IF_FIRST
CONFIG_NET_DEFAULT_IF_UP
CONFIG_NET_DEFAULT_IF_ETHERNET
CONFIG_NET_DEFAULT_IF_IEEE802154
CONFIG_NET_DEFAULT_IF_OFFLOAD
CONFIG_NET_DEFAULT_IF_DUMMY
CONFIG_NET_DEFAULT_IF_CANBUS_RAW
CONFIG_NET_DEFAULT_IF_PPP
CONFIG_NET_DEFAULT_IF_OFFLOADED_NETDEV
CONFIG_NET_DEFAULT_IF_WIFI
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:882`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L882)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_DEFAULT_IF_DUMMY`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF_DUMMY)、[`CONFIG_NET_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TEST)、[`CONFIG_NET_DEFAULT_IF_FIRST`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF_FIRST)、[`CONFIG_NET_DEFAULT_IF_UP`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF_UP)、[`CONFIG_NET_DEFAULT_IF_ETHERNET`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF_ETHERNET)、[`CONFIG_NET_DEFAULT_IF_IEEE802154`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF_IEEE802154)、[`CONFIG_NET_DEFAULT_IF_OFFLOAD`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF_OFFLOAD)、[`CONFIG_NET_DEFAULT_IF_CANBUS_RAW`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF_CANBUS_RAW)、[`CONFIG_NET_DEFAULT_IF_PPP`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF_PPP)、[`CONFIG_NET_DEFAULT_IF_OFFLOADED_NETDEV`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF_OFFLOADED_NETDEV)、[`CONFIG_NET_DEFAULT_IF_WIFI`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF_WIFI)。

<a id="CONFIG_NET_DEFAULT_IF_CANBUS_RAW"></a>

## 397.53 `CONFIG_NET_DEFAULT_IF_CANBUS_RAW`

**提示（Prompt）**：套接字 CAN（SocketCAN）接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_CANBUS_RAW && <choice CONFIG_NET_DEFAULT_IF>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:913`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L913)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 默认网络接口（Default Network Interface）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_CANBUS_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_CANBUS_RAW)、[`CONFIG_NET_DEFAULT_IF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF)。

<a id="CONFIG_NET_DEFAULT_IF_DUMMY"></a>

## 397.54 `CONFIG_NET_DEFAULT_IF_DUMMY`

**提示（Prompt）**：用于测试的虚拟（Dummy）接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_DUMMY && <choice CONFIG_NET_DEFAULT_IF>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:909`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L909)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 默认网络接口（Default Network Interface）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_DUMMY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_DUMMY)、[`CONFIG_NET_DEFAULT_IF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF)。

<a id="CONFIG_NET_DEFAULT_IF_ETHERNET"></a>

## 397.55 `CONFIG_NET_DEFAULT_IF_ETHERNET`

**提示（Prompt）**：以太网（Ethernet）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && <choice CONFIG_NET_DEFAULT_IF>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:897`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L897)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 默认网络接口（Default Network Interface）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_DEFAULT_IF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF)。

<a id="CONFIG_NET_DEFAULT_IF_FIRST"></a>

## 397.56 `CONFIG_NET_DEFAULT_IF_FIRST`

**提示（Prompt）**：首个可用接口（First available interface）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DEFAULT_IF>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:891`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L891)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 默认网络接口（Default Network Interface）

**配置项引用（Symbol References）**：[`CONFIG_NET_DEFAULT_IF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF)。

<a id="CONFIG_NET_DEFAULT_IF_IEEE802154"></a>

## 397.57 `CONFIG_NET_DEFAULT_IF_IEEE802154`

**提示（Prompt）**：IEEE 802.15.4 接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154 && <choice CONFIG_NET_DEFAULT_IF>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:901`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L901)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 默认网络接口（Default Network Interface）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154)、[`CONFIG_NET_DEFAULT_IF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF)。

<a id="CONFIG_NET_DEFAULT_IF_OFFLOAD"></a>

## 397.58 `CONFIG_NET_DEFAULT_IF_OFFLOAD`

**提示（Prompt）**：卸载式接口（Offloaded interface）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_OFFLOAD && <choice CONFIG_NET_DEFAULT_IF>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:905`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L905)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 默认网络接口（Default Network Interface）

**配置项引用（Symbol References）**：[`CONFIG_NET_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_OFFLOAD)、[`CONFIG_NET_DEFAULT_IF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF)。

<a id="CONFIG_NET_DEFAULT_IF_OFFLOADED_NETDEV"></a>

## 397.59 `CONFIG_NET_DEFAULT_IF_OFFLOADED_NETDEV`

**提示（Prompt）**：卸载式网络设备（Offloaded network device）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DEFAULT_IF>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:921`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L921)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 默认网络接口（Default Network Interface）

**配置项引用（Symbol References）**：[`CONFIG_NET_DEFAULT_IF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF)。

<a id="CONFIG_NET_DEFAULT_IF_PPP"></a>

## 397.60 `CONFIG_NET_DEFAULT_IF_PPP`

**提示（Prompt）**：点对点协议（PPP）接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && <choice CONFIG_NET_DEFAULT_IF>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:917`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L917)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 默认网络接口（Default Network Interface）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PPP)、[`CONFIG_NET_DEFAULT_IF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF)。

<a id="CONFIG_NET_DEFAULT_IF_UP"></a>

## 397.61 `CONFIG_NET_DEFAULT_IF_UP`

**提示（Prompt）**：首个已启用（up）的接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DEFAULT_IF>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:894`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L894)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 默认网络接口（Default Network Interface）

**配置项引用（Symbol References）**：[`CONFIG_NET_DEFAULT_IF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF)。

<a id="CONFIG_NET_DEFAULT_IF_WIFI"></a>

## 397.62 `CONFIG_NET_DEFAULT_IF_WIFI`

**提示（Prompt）**：Wi-Fi 接口

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && <choice CONFIG_NET_DEFAULT_IF>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:924`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L924)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 默认网络接口（Default Network Interface）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_DEFAULT_IF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DEFAULT_IF)。

<a id="CONFIG_NET_DHCPV4"></a>

## 397.63 `CONFIG_NET_DHCPV4`

**提示（Prompt）**：DHCPv4 客户端（Client）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && CONFIG_NET_UDP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
CONFIG_NET_MGMT_EVENT_INFO if CONFIG_NET_IPV4_ACD
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_IPV4
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_IPV4
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NET_MGMT_EVENT_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT_INFO)、[`CONFIG_NET_IPV4_ACD`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD)、[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_IPV4`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_IPV4)。

<a id="CONFIG_NET_DHCPV4_ACCEPT_UNICAST"></a>

## 397.64 `CONFIG_NET_DHCPV4_ACCEPT_UNICAST`

**提示（Prompt）**：接受单播（Unicast）DHCPv4 流量

**说明（Help）**

启用后，在接口尚未配置服务器分配的地址时，网络协议栈也会接受服务器发送的单播（Unicast）DHCPv4 响应。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_DNS_SERVER_VIA_INTERFACE"></a>

## 397.65 `CONFIG_NET_DHCPV4_DNS_SERVER_VIA_INTERFACE`

**提示（Prompt）**：将 DNS 服务器限定到对应的网络接口（Network interface）

**说明（Help）**

启用后，如果系统有多个网络接口且各接口均启用了 DHCP，则从某个接口收到的 DNS 服务器地址只分配给该接口。禁用时，执行 DNS 查询可以通过任意接口访问所有已配置的 DNS 服务器。例如，Wi-Fi 接口通过 DHCPv4 选项收到 DNS 服务器 `192.0.2.53`，以太网（Ethernet）接口收到 `198.51.100.53`。启用本选项后，DNS 解析器（Resolver）通过 Wi-Fi 接口发送查询时使用 `192.0.2.53`，通过以太网接口发送查询时使用 `198.51.100.53`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_OPTION_DNS_ADDRESS && CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_OPTION_DNS_ADDRESS`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_OPTION_DNS_ADDRESS)、[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_INITIAL_DELAY_MAX"></a>

## 397.66 `CONFIG_NET_DHCPV4_INITIAL_DELAY_MAX`

**提示（Prompt）**：初始发现请求（Discover request）的最大等待时间

**说明（Help）**

按照 RFC 2131 第 4.4.1 节，在发送初始发现报文（Discover）前，随机等待 1～10 秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[2, 10]
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_INIT_REBOOT"></a>

## 397.67 `CONFIG_NET_DHCPV4_INIT_REBOOT`

**提示（Prompt）**：支持 INIT-REBOOT 状态

**说明（Help）**

在已知网络地址的情况下初始化：如果 DHCPv4 客户端以前已经获得过地址，则从 INIT-REBOOT 状态开始，并发送 DHCPREQUEST 报文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_INIT_REBOOT_ATTEMPTS"></a>

## 397.68 `CONFIG_NET_DHCPV4_INIT_REBOOT_ATTEMPTS`

**提示（Prompt）**：回退到 DISCOVER 前尝试发送 INIT-REBOOT REQUEST 的次数

**说明（Help）**

DHCPv4 客户端针对记住的地址发送 INIT-REBOOT DHCPREQUEST 的次数；超过该次数后，放弃该地址并通过完整的 DHCPDISCOVER 重新开始配置。INIT-REBOOT 的用途是进行乐观的快速探测：网络改变时，许多接入点（Access point）会直接丢弃来自其他子网的 REQUEST，而不回复 NAK。因此，较小的值能让客户端较快回退到 DISCOVER。按照 RFC 2131 第 4.1 节，重传采用指数退避（Exponential backoff），间隔依次为 4 秒、8 秒、16 秒等，所以每增加一次尝试，开始 DISCOVER 前的最坏等待时间约翻倍。设为 1 时回退最快，约需 4 秒；较大的值可容忍同一网络上的丢包，但回退较慢。若要完全禁用 INIT-REBOOT，应禁用 `CONFIG_NET_DHCPV4_INIT_REBOOT`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_INIT_REBOOT && CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client） → 支持 INIT-REBOOT 状态

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_INIT_REBOOT`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_INIT_REBOOT)、[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE"></a>

## 397.69 `CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE`

**提示（Prompt）**：DHCPv4 客户端日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_DHCPV4_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_DHCPV4_LOG_LEVEL_OFF
CONFIG_NET_DHCPV4_LOG_LEVEL_ERR
CONFIG_NET_DHCPV4_LOG_LEVEL_WRN
CONFIG_NET_DHCPV4_LOG_LEVEL_INF
CONFIG_NET_DHCPV4_LOG_LEVEL_DBG
CONFIG_NET_DHCPV4_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_DHCPV4_LOG_LEVEL_DEFAULT`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_DHCPV4_LOG_LEVEL_OFF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_LOG_LEVEL_OFF)、[`CONFIG_NET_DHCPV4_LOG_LEVEL_ERR`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_LOG_LEVEL_ERR)、[`CONFIG_NET_DHCPV4_LOG_LEVEL_WRN`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_LOG_LEVEL_WRN)、[`CONFIG_NET_DHCPV4_LOG_LEVEL_INF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_LOG_LEVEL_INF)、[`CONFIG_NET_DHCPV4_LOG_LEVEL_DBG`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_DHCPV4_LOG_LEVEL_DBG"></a>

## 397.70 `CONFIG_NET_DHCPV4_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client） → DHCPv4 客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV4_LOG_LEVEL_DEFAULT"></a>

## 397.71 `CONFIG_NET_DHCPV4_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client） → DHCPv4 客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV4_LOG_LEVEL_ERR"></a>

## 397.72 `CONFIG_NET_DHCPV4_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client） → DHCPv4 客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV4_LOG_LEVEL_INF"></a>

## 397.73 `CONFIG_NET_DHCPV4_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client） → DHCPv4 客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV4_LOG_LEVEL_OFF"></a>

## 397.74 `CONFIG_NET_DHCPV4_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client） → DHCPv4 客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV4_LOG_LEVEL_WRN"></a>

## 397.75 `CONFIG_NET_DHCPV4_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client） → DHCPv4 客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV4_MAX_REQUESTED_OPTIONS"></a>

## 397.76 `CONFIG_NET_DHCPV4_MAX_REQUESTED_OPTIONS`

**提示（Prompt）**：请求选项（Requested option）的最大数量

**说明（Help）**

可添加到 DHCPv4 请求报文中的请求选项（Requested option）的最大数量。使用 `net_dhcpv4_add_option_callback()` API 添加这些选项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_OPTION_CALLBACKS && CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[3, 255]
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client） → 选项回调（Option callback）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_OPTION_CALLBACKS`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_OPTION_CALLBACKS)、[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_OPTION_CALLBACKS"></a>

## 397.77 `CONFIG_NET_DHCPV4_OPTION_CALLBACKS`

**提示（Prompt）**：选项回调（Option callback）

**说明（Help）**

启用后，可为任意 DHCP 选项添加自定义回调（Callback），以支持系统其他部分未使用的 DHCP 选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_DHCPV4_OPTION_CALLBACKS_VENDOR_SPECIFIC
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_DHCPV4_OPTION_CALLBACKS_VENDOR_SPECIFIC`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_OPTION_CALLBACKS_VENDOR_SPECIFIC)。

<a id="CONFIG_NET_DHCPV4_OPTION_CALLBACKS_VENDOR_SPECIFIC"></a>

## 397.78 `CONFIG_NET_DHCPV4_OPTION_CALLBACKS_VENDOR_SPECIFIC`

**提示（Prompt）**：封装的供应商专用选项回调（Encapsulated vendor-specific option callback）

**说明（Help）**

启用后，可为 DHCP 选项 43 中封装的供应商专用信息（Vendor-specific information）添加自定义回调。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_DHCPV4_OPTION_CALLBACKS
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_DHCPV4_OPTION_CALLBACKS`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_OPTION_CALLBACKS)。

<a id="CONFIG_NET_DHCPV4_OPTION_DNS_ADDRESS"></a>

## 397.79 `CONFIG_NET_DHCPV4_OPTION_DNS_ADDRESS`

**提示（Prompt）**：采用 DHCPv4 选项中的 DNS 服务器并保存到 DNS 解析器默认上下文（Default context）

**说明（Help）**

启用后，可通过 DHCPv4 选项设置 DNS 服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_OPTION_NTP_SERVER"></a>

## 397.80 `CONFIG_NET_DHCPV4_OPTION_NTP_SERVER`

**提示（Prompt）**：采用 DHCPv4 选项中的 NTP 服务器并保存到 `net_if`

**说明（Help）**

启用后，可通过 DHCPv4 选项设置网络时间协议（NTP）服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SNTP && CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_SNTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SNTP)、[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_OPTION_PRINT_IGNORED"></a>

## 397.81 `CONFIG_NET_DHCPV4_OPTION_PRINT_IGNORED`

**提示（Prompt）**：打印被忽略选项（Ignored option）的信息

**说明（Help）**

启用后，打印已收到但被忽略的选项的信息。禁用时，这些选项会作为未知选项（Unknown option）打印。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_RESTART_ON_IF_UP"></a>

## 397.82 `CONFIG_NET_DHCPV4_RESTART_ON_IF_UP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当外部软件模块会在接口进入适合开始绑定（Binding）的状态时自动调用 `net_dhcpv4_restart`，而不是由内部在 `NET_EVENT_IF_UP` 事件发生时调用它，应禁用此项。对于 `NET_EVENT_IF_UP` 并不意味着已能发送任意数据包的接口，这可以避免在接口准备就绪前发送 DHCP 请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
n if CONFIG_WIFI_NM_WPA_SUPPLICANT
y
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)。

<a id="CONFIG_NET_DHCPV4_SERVER"></a>

## 397.83 `CONFIG_NET_DHCPV4_SERVER`

**提示（Prompt）**：DHCPv4 服务器

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && CONFIG_NET_UDP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS
CONFIG_NET_SOCKETS_SERVICE
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_SOFTAP_DHCP_SERVER
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_NET_SOCKETS_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SERVICE)、[`CONFIG_NXP_WIFI_SOFTAP_DHCP_SERVER`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_DHCP_SERVER)。

<a id="CONFIG_NET_DHCPV4_SERVER_ADDR_COUNT"></a>

## 397.84 `CONFIG_NET_DHCPV4_SERVER_ADDR_COUNT`

**提示（Prompt）**：服务器可分配的 IPv4 地址数量

**说明（Help）**

每个 DHCPv4 服务器实例可分配的 IPv4 地址的最大数量。地址池（Address pool）的起始 IPv4 地址在运行时初始化服务器时提供。池中的连续地址通过递增地址最低位的八位组（Octet）生成。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
32
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_SERVER_ADDR_DECLINE_TIME"></a>

## 397.85 `CONFIG_NET_DHCPV4_SERVER_ADDR_DECLINE_TIME`

**提示（Prompt）**：检测到冲突后 IPv4 地址保持禁用的时间（秒）

**说明（Help）**

如果 IPv4 地址因收到 Decline 报文或 ICMP 探测发现冲突而被禁用，该地址便不能继续分配。此超时值指定地址保持在 Declined 状态的时长。注意：如果没有空闲地址可供分配，服务器可能尝试重新使用处于 Declined 状态时间最长的地址。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
86400
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_SERVER_ADDR_LEASE_TIME"></a>

## 397.86 `CONFIG_NET_DHCPV4_SERVER_ADDR_LEASE_TIME`

**提示（Prompt）**：服务器分配的 IPv4 地址租期（Lease time，秒）

**说明（Help）**

服务器分配的 IPv4 地址的租期（Lease time），单位为秒。如果客户端不续租，该值决定 IPv4 地址租约何时到期。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
86400
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L186)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_SERVER_ICMP_PROBE_TIMEOUT"></a>

## 397.87 `CONFIG_NET_DHCPV4_SERVER_ICMP_PROBE_TIMEOUT`

**提示（Prompt）**：服务器发送的 ICMP 探测超时（毫秒）

**说明（Help）**

DHCPv4 服务器会探测拟提供的 IP 地址，即发送 ICMP 回显请求（Echo request），并等待本配置指定的时间后再提供该地址。设为 0 可禁用 ICMP 探测。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[0, 60000]
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
100
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_SERVER_INSTANCES"></a>

## 397.88 `CONFIG_NET_DHCPV4_SERVER_INSTANCES`

**提示（Prompt）**：DHCPv4 服务器实例（Instance）的最大数量

**说明（Help）**

系统支持的 DHCPv4 服务器实例的最大数量。每个需要充当 DHCPv4 服务器的网络接口都需要一个独立实例。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE"></a>

## 397.89 `CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：DHCPv4 服务器日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_DHCPV4_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_OFF
CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_ERR
CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_WRN
CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_INF
CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_DBG
CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_DEFAULT`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_OFF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_OFF)、[`CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_ERR`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_ERR)、[`CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_WRN`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_WRN)、[`CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_INF`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_INF)、[`CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_DBG`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_DBG"></a>

## 397.90 `CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器 → DHCPv4 服务器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_DEFAULT"></a>

## 397.91 `CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器 → DHCPv4 服务器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_ERR"></a>

## 397.92 `CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器 → DHCPv4 服务器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_INF"></a>

## 397.93 `CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器 → DHCPv4 服务器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_OFF"></a>

## 397.94 `CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器 → DHCPv4 服务器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_WRN"></a>

## 397.95 `CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器 → DHCPv4 服务器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV4_SERVER_NAK_UNRECOGNIZED_REQUESTS"></a>

## 397.96 `CONFIG_NET_DHCPV4_SERVER_NAK_UNRECOGNIZED_REQUESTS`

**提示（Prompt）**：对无法识别的客户端所发 DHCP Request 回复 NAK

**说明（Help）**

Zephyr 的 DHCPv4 服务器未实现地址租约（Address lease）的持久化存储。因此，重启会丢失全部租约；从 INIT-REBOOT 状态开始的客户端可能先发送若干次 Request，再尝试完整的 Discover-Request 流程，从而产生延迟。启用此项会在这一点上违反 RFC：服务器对无法识别的 Request 不再保持静默，而是发送否定确认（NAK），通知客户端执行完整流程。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_SERVER_OPTION_CAPTIVE_PORTAL"></a>

## 397.97 `CONFIG_NET_DHCPV4_SERVER_OPTION_CAPTIVE_PORTAL`

**提示（Prompt）**：DHCP 选项 114（RFC 8910 强制门户 URI，Captive portal URI）

**说明（Help）**

启用后，如果客户端在参数请求列表（Parameter Request List，选项 55）中列出了选项 114，则 DHCPv4 服务器在 Offer 和 Acknowledgment 报文中加入选项 114。客户端可用该 URI 在隔离网络中检测强制门户（Captive portal），例如 SoftAP 配网场景。如果 `NET_DHCPV4_SERVER_OPTION_CAPTIVE_PORTAL_URI` 字符串非空，就使用该字符串；否则，服务器使用 `http://`、DHCP 接口自身的 IPv4 地址和路径 `/generate_204` 组合生成 URI。RFC 8910 不建议使用 IP 地址字面量（IP literal）；DNS 可用时应通过上述配置覆盖该 URI。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_SERVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:249`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L249)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_SERVER_OPTION_CAPTIVE_PORTAL_URI"></a>

## 397.98 `CONFIG_NET_DHCPV4_SERVER_OPTION_CAPTIVE_PORTAL_URI`

**提示（Prompt）**：覆盖强制门户 URI（Captive portal URI override）

**说明（Help）**

非空时，将该字符串原样作为 DHCP 选项 114 发送。为空时，DHCPv4 服务器使用 `http://`、DHCP 服务器接口自身的 IPv4 地址和路径 `/generate_204` 组合生成 URI。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_SERVER_OPTION_CAPTIVE_PORTAL && CONFIG_NET_DHCPV4_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:263`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L263)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器 → DHCP 选项 114（RFC 8910 强制门户 URI，Captive portal URI）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER_OPTION_CAPTIVE_PORTAL`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER_OPTION_CAPTIVE_PORTAL)、[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_SERVER_OPTION_DNS_ADDRESS"></a>

## 397.99 `CONFIG_NET_DHCPV4_SERVER_OPTION_DNS_ADDRESS`

**提示（Prompt）**：DNS 服务器地址（DNS server address）

**说明（Help）**

指定客户端请求 IP 地址时，DHCPv4 服务器应提供的 DNS 服务器地址。DHCPv4 服务器将该地址加入发给客户端的 DHCP Offer 和 Acknowledgment 报文，让客户端使用指定的 DNS 服务器进行名称解析（Name resolution）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_DNS_SERVER1 if CONFIG_DNS_SERVER_IP_ADDRESSES
""
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_DNS_SERVER1`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SERVER1)、[`CONFIG_DNS_SERVER_IP_ADDRESSES`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SERVER_IP_ADDRESSES)。

<a id="CONFIG_NET_DHCPV4_SERVER_OPTION_ROUTER"></a>

## 397.100 `CONFIG_NET_DHCPV4_SERVER_OPTION_ROUTER`

**提示（Prompt）**：在 DHCP 服务器响应中设置路由器选项（Router option）

**说明（Help）**

启用后，在 DHCP 服务器响应中设置路由器选项（Router option），使其指向该接口自身的网关地址。可以禁用此项，避免客户端尝试向本设备转发流量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:240`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L240)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 服务器

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<!-- kconfig-navigation -->

[上一章](P396_subsys_net_配置项参考_6.md) · [返回大纲](大纲.md) · [下一章](P398_subsys_net_配置项参考_8.md)
