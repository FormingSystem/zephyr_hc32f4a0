---
id: learning.zephyr-docs.kconfig-reference.page-399
title: "`subsys/net`配置项参考（9/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第399章\_`subsys/net`配置项参考（9/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_HTTP_LOG_LEVEL_INF"></a>

## 399.1 `CONFIG_NET_HTTP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HTTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 客户端库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HTTP_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HTTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HTTP_LOG_LEVEL_OFF"></a>

## 399.2 `CONFIG_NET_HTTP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HTTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 客户端库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HTTP_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HTTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HTTP_LOG_LEVEL_WRN"></a>

## 399.3 `CONFIG_NET_HTTP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HTTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 客户端库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HTTP_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HTTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE"></a>

## 399.4 `CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：HTTP 服务器库日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_HTTP_SERVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_HTTP_SERVER_LOG_LEVEL_OFF
CONFIG_NET_HTTP_SERVER_LOG_LEVEL_ERR
CONFIG_NET_HTTP_SERVER_LOG_LEVEL_WRN
CONFIG_NET_HTTP_SERVER_LOG_LEVEL_INF
CONFIG_NET_HTTP_SERVER_LOG_LEVEL_DBG
CONFIG_NET_HTTP_SERVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_HTTP_SERVER_LOG_LEVEL_DEFAULT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_SERVER_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_HTTP_SERVER_LOG_LEVEL_OFF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_SERVER_LOG_LEVEL_OFF)、[`CONFIG_NET_HTTP_SERVER_LOG_LEVEL_ERR`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_SERVER_LOG_LEVEL_ERR)、[`CONFIG_NET_HTTP_SERVER_LOG_LEVEL_WRN`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_SERVER_LOG_LEVEL_WRN)、[`CONFIG_NET_HTTP_SERVER_LOG_LEVEL_INF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_SERVER_LOG_LEVEL_INF)、[`CONFIG_NET_HTTP_SERVER_LOG_LEVEL_DBG`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_SERVER_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_HTTP_SERVER_LOG_LEVEL_DBG"></a>

## 399.5 `CONFIG_NET_HTTP_SERVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HTTP_SERVER_LOG_LEVEL_DEFAULT"></a>

## 399.6 `CONFIG_NET_HTTP_SERVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HTTP_SERVER_LOG_LEVEL_ERR"></a>

## 399.7 `CONFIG_NET_HTTP_SERVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HTTP_SERVER_LOG_LEVEL_INF"></a>

## 399.8 `CONFIG_NET_HTTP_SERVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HTTP_SERVER_LOG_LEVEL_OFF"></a>

## 399.9 `CONFIG_NET_HTTP_SERVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HTTP_SERVER_LOG_LEVEL_WRN"></a>

## 399.10 `CONFIG_NET_HTTP_SERVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ICMPV4_ACCEPT_BROADCAST"></a>

## 399.11 `CONFIG_NET_ICMPV4_ACCEPT_BROADCAST`

**提示（Prompt）**：接受广播 ICMPv4 回显请求（Echo request）

**说明（Help）**

启用后，响应发往广播地址（Broadcast address）的 ICMPv4 回显请求（Echo request）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE"></a>

## 399.12 `CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE`

**提示（Prompt）**：ICMPv4 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_ICMPV4_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_ICMPV4_LOG_LEVEL_OFF
CONFIG_NET_ICMPV4_LOG_LEVEL_ERR
CONFIG_NET_ICMPV4_LOG_LEVEL_WRN
CONFIG_NET_ICMPV4_LOG_LEVEL_INF
CONFIG_NET_ICMPV4_LOG_LEVEL_DBG
CONFIG_NET_ICMPV4_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_ICMPV4_LOG_LEVEL_DEFAULT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV4_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_ICMPV4_LOG_LEVEL_OFF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV4_LOG_LEVEL_OFF)、[`CONFIG_NET_ICMPV4_LOG_LEVEL_ERR`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV4_LOG_LEVEL_ERR)、[`CONFIG_NET_ICMPV4_LOG_LEVEL_WRN`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV4_LOG_LEVEL_WRN)、[`CONFIG_NET_ICMPV4_LOG_LEVEL_INF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV4_LOG_LEVEL_INF)、[`CONFIG_NET_ICMPV4_LOG_LEVEL_DBG`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV4_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_ICMPV4_LOG_LEVEL_DBG"></a>

## 399.13 `CONFIG_NET_ICMPV4_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → ICMPv4 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ICMPV4_LOG_LEVEL_DEFAULT"></a>

## 399.14 `CONFIG_NET_ICMPV4_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → ICMPv4 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ICMPV4_LOG_LEVEL_ERR"></a>

## 399.15 `CONFIG_NET_ICMPV4_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → ICMPv4 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ICMPV4_LOG_LEVEL_INF"></a>

## 399.16 `CONFIG_NET_ICMPV4_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → ICMPv4 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ICMPV4_LOG_LEVEL_OFF"></a>

## 399.17 `CONFIG_NET_ICMPV4_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → ICMPv4 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ICMPV4_LOG_LEVEL_WRN"></a>

## 399.18 `CONFIG_NET_ICMPV4_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → ICMPv4 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE"></a>

## 399.19 `CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE`

**提示（Prompt）**：ICMPv6 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_ICMPV6_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_ICMPV6_LOG_LEVEL_OFF
CONFIG_NET_ICMPV6_LOG_LEVEL_ERR
CONFIG_NET_ICMPV6_LOG_LEVEL_WRN
CONFIG_NET_ICMPV6_LOG_LEVEL_INF
CONFIG_NET_ICMPV6_LOG_LEVEL_DBG
CONFIG_NET_ICMPV6_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_ICMPV6_LOG_LEVEL_DEFAULT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV6_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_ICMPV6_LOG_LEVEL_OFF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV6_LOG_LEVEL_OFF)、[`CONFIG_NET_ICMPV6_LOG_LEVEL_ERR`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV6_LOG_LEVEL_ERR)、[`CONFIG_NET_ICMPV6_LOG_LEVEL_WRN`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV6_LOG_LEVEL_WRN)、[`CONFIG_NET_ICMPV6_LOG_LEVEL_INF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV6_LOG_LEVEL_INF)、[`CONFIG_NET_ICMPV6_LOG_LEVEL_DBG`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV6_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_ICMPV6_LOG_LEVEL_DBG"></a>

## 399.20 `CONFIG_NET_ICMPV6_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → ICMPv6 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ICMPV6_LOG_LEVEL_DEFAULT"></a>

## 399.21 `CONFIG_NET_ICMPV6_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → ICMPv6 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ICMPV6_LOG_LEVEL_ERR"></a>

## 399.22 `CONFIG_NET_ICMPV6_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → ICMPv6 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ICMPV6_LOG_LEVEL_INF"></a>

## 399.23 `CONFIG_NET_ICMPV6_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → ICMPv6 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ICMPV6_LOG_LEVEL_OFF"></a>

## 399.24 `CONFIG_NET_ICMPV6_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → ICMPv6 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ICMPV6_LOG_LEVEL_WRN"></a>

## 399.25 `CONFIG_NET_ICMPV6_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → ICMPv6 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_ICMPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IF_IPV6_PREFIX_COUNT"></a>

## 399.26 `CONFIG_NET_IF_IPV6_PREFIX_COUNT`

**提示（Prompt）**：每个网络接口的 IPv6 前缀（Prefix）最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_IF_LOG_LEVEL_CHOICE"></a>

## 399.27 `CONFIG_NET_IF_LOG_LEVEL_CHOICE`

**提示（Prompt）**：网络接口代码（Network interface code）的日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IF_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_IF_LOG_LEVEL_OFF
CONFIG_NET_IF_LOG_LEVEL_ERR
CONFIG_NET_IF_LOG_LEVEL_WRN
CONFIG_NET_IF_LOG_LEVEL_INF
CONFIG_NET_IF_LOG_LEVEL_DBG
CONFIG_NET_IF_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IF_LOG_LEVEL_DEFAULT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_IF_LOG_LEVEL_OFF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_LOG_LEVEL_OFF)、[`CONFIG_NET_IF_LOG_LEVEL_ERR`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_LOG_LEVEL_ERR)、[`CONFIG_NET_IF_LOG_LEVEL_WRN`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_LOG_LEVEL_WRN)、[`CONFIG_NET_IF_LOG_LEVEL_INF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_LOG_LEVEL_INF)、[`CONFIG_NET_IF_LOG_LEVEL_DBG`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_IF_LOG_LEVEL_DBG"></a>

## 399.28 `CONFIG_NET_IF_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络接口代码（Network interface code）的日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IF_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IF_LOG_LEVEL_DEFAULT"></a>

## 399.29 `CONFIG_NET_IF_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络接口代码（Network interface code）的日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IF_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IF_LOG_LEVEL_ERR"></a>

## 399.30 `CONFIG_NET_IF_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络接口代码（Network interface code）的日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IF_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IF_LOG_LEVEL_INF"></a>

## 399.31 `CONFIG_NET_IF_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络接口代码（Network interface code）的日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IF_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IF_LOG_LEVEL_OFF"></a>

## 399.32 `CONFIG_NET_IF_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络接口代码（Network interface code）的日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IF_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IF_LOG_LEVEL_WRN"></a>

## 399.33 `CONFIG_NET_IF_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络接口代码（Network interface code）的日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IF_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IF_MAX_IPV4_COUNT"></a>

## 399.34 `CONFIG_NET_IF_MAX_IPV4_COUNT`

**提示（Prompt）**：系统中 IPv4 网络接口的最大数量

**说明（Help）**

指定系统中将启用 IPv4 的网络接口（Network interface）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_VLAN_COUNT if CONFIG_NET_VLAN && CONFIG_NET_VLAN_COUNT > 0
2 if CONFIG_NRF70_ENABLE_DUAL_VIF
2 if CONFIG_NET_LOOPBACK
1
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/ad_apardpfw_sl/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/ad_apardpfw_sl/Kconfig.defconfig)。

```text
3
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_VLAN_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN_COUNT)、[`CONFIG_NET_VLAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN)、[`CONFIG_NRF70_ENABLE_DUAL_VIF`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_ENABLE_DUAL_VIF)、[`CONFIG_NET_LOOPBACK`](P131_drivers_net_配置项参考.md#CONFIG_NET_LOOPBACK)。

<a id="CONFIG_NET_IF_MAX_IPV6_COUNT"></a>

## 399.35 `CONFIG_NET_IF_MAX_IPV6_COUNT`

**提示（Prompt）**：系统中 IPv6 网络接口的最大数量

**说明（Help）**

指定系统中将启用 IPv6 的网络接口（Network interface）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_VLAN_COUNT if CONFIG_NET_VLAN && CONFIG_NET_VLAN_COUNT > 0
2 if CONFIG_NRF70_ENABLE_DUAL_VIF
2 if CONFIG_NET_LOOPBACK
1
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/ad_apardpfw_sl/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/ad_apardpfw_sl/Kconfig.defconfig)。

```text
3
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_VLAN_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN_COUNT)、[`CONFIG_NET_VLAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN)、[`CONFIG_NRF70_ENABLE_DUAL_VIF`](P189_drivers_wifi_配置项参考_2.md#CONFIG_NRF70_ENABLE_DUAL_VIF)、[`CONFIG_NET_LOOPBACK`](P131_drivers_net_配置项参考.md#CONFIG_NET_LOOPBACK)。

<a id="CONFIG_NET_IF_MCAST_IPV4_ADDR_COUNT"></a>

## 399.36 `CONFIG_NET_IF_MCAST_IPV4_ADDR_COUNT`

**提示（Prompt）**：每个网络接口的 IPv4 多播地址（Multicast address）最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3 if CONFIG_PTP_DELAY_MECHANISM_P2P && CONFIG_PTP_UDP_IPV4_PROTOCOL
2 if CONFIG_NET_IPV4_IGMP
1
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PTP_DELAY_MECHANISM_P2P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_DELAY_MECHANISM_P2P)、[`CONFIG_PTP_UDP_IPV4_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_UDP_IPV4_PROTOCOL)、[`CONFIG_NET_IPV4_IGMP`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_IGMP)。

<a id="CONFIG_NET_IF_MCAST_IPV4_SOURCE_COUNT"></a>

## 399.37 `CONFIG_NET_IF_MCAST_IPV4_SOURCE_COUNT`

**提示（Prompt）**：每个多播地址可包含或排除的 IPv4 源地址的最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IF_MCAST_IPV6_ADDR_COUNT"></a>

## 399.38 `CONFIG_NET_IF_MCAST_IPV6_ADDR_COUNT`

**提示（Prompt）**：每个网络接口的 IPv6 多播地址（Multicast address）最大数量

**说明（Help）**

指定网络接口可同时加入的 IPv6 多播地址（Multicast address）数量。除所有节点多播地址（All-nodes multicast address）以及 mDNS 等功能所需的其他多播组外，每个单播地址还需要加入它对应的请求节点多播组（Solicited-node multicast group）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8 if CONFIG_NET_L2_OPENTHREAD
4 if CONFIG_PTP_DELAY_MECHANISM_P2P && CONFIG_PTP_UDP_IPV6_PROTOCOL
4 if CONFIG_NET_DHCPV6
3
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)、[`CONFIG_PTP_DELAY_MECHANISM_P2P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_DELAY_MECHANISM_P2P)、[`CONFIG_PTP_UDP_IPV6_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_UDP_IPV6_PROTOCOL)、[`CONFIG_NET_DHCPV6`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6)。

<a id="CONFIG_NET_IF_UNICAST_IPV4_ADDR_COUNT"></a>

## 399.39 `CONFIG_NET_IF_UNICAST_IPV4_ADDR_COUNT`

**提示（Prompt）**：每个网络接口的 IPv4 单播地址（Unicast address）最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4 if CONFIG_NET_NATIVE_OFFLOADED_SOCKETS
2 if CONFIG_NET_IPV4_AUTO
2 if CONFIG_NET_LOOPBACK
1
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_NATIVE_OFFLOADED_SOCKETS`](P131_drivers_net_配置项参考.md#CONFIG_NET_NATIVE_OFFLOADED_SOCKETS)、[`CONFIG_NET_IPV4_AUTO`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO)、[`CONFIG_NET_LOOPBACK`](P131_drivers_net_配置项参考.md#CONFIG_NET_LOOPBACK)。

<a id="CONFIG_NET_IF_UNICAST_IPV6_ADDR_COUNT"></a>

## 399.40 `CONFIG_NET_IF_UNICAST_IPV6_ADDR_COUNT`

**提示（Prompt）**：每个网络接口的 IPv6 单播地址（Unicast address）最大数量

**说明（Help）**

指定网络接口可同时拥有的 IPv6 单播地址（Unicast address）数量。当 DHCPv6 客户端和无状态地址自动配置（SLAAC）同时启用时，接口通常至少拥有三个单播地址：链路本地地址（Link-local address）、由 SLAAC 派生的全局地址，以及 DHCPv6 分配的全局地址。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4 if CONFIG_NET_NATIVE_OFFLOADED_SOCKETS
6 if CONFIG_NET_L2_OPENTHREAD
3 if CONFIG_NET_LOOPBACK
3 if CONFIG_NET_DHCPV6 && CONFIG_NET_IPV6_ND
2
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_NATIVE_OFFLOADED_SOCKETS`](P131_drivers_net_配置项参考.md#CONFIG_NET_NATIVE_OFFLOADED_SOCKETS)、[`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)、[`CONFIG_NET_LOOPBACK`](P131_drivers_net_配置项参考.md#CONFIG_NET_LOOPBACK)、[`CONFIG_NET_DHCPV6`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6)、[`CONFIG_NET_IPV6_ND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_ND)。

<a id="CONFIG_NET_INITIAL_HOP_LIMIT"></a>

## 399.41 `CONFIG_NET_INITIAL_HOP_LIMIT`

**提示（Prompt）**：IPv6 单播数据包的初始跳数限制（Hop limit）

**说明（Help）**

该值通常应大于 0。设备收到 IPv6 数据包时会递减此值；跳数限制（Hop limit）为 0 时丢弃数据包。发送时，如果跳数限制为 0，则在将数据包传输到网络之前将其丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_INITIAL_IPV4_MCAST_LOOP"></a>

## 399.42 `CONFIG_NET_INITIAL_IPV4_MCAST_LOOP`

**提示（Prompt）**：控制套接字（Socket）是否接收自身发送的多播数据包

**说明（Help）**

如果用户未通过 `setsockopt()` 设置，则为套接字选项中的 `IPV4_MULTICAST_LOOP` 指定初始值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_INITIAL_IPV6_MCAST_LOOP"></a>

## 399.43 `CONFIG_NET_INITIAL_IPV6_MCAST_LOOP`

**提示（Prompt）**：控制套接字（Socket）是否接收自身发送的多播数据包

**说明（Help）**

如果用户未通过 `setsockopt()` 设置，则为套接字选项中的 `IPV6_MULTICAST_LOOP` 指定初始值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_INITIAL_MCAST_HOP_LIMIT"></a>

## 399.44 `CONFIG_NET_INITIAL_MCAST_HOP_LIMIT`

**提示（Prompt）**：IPv6 多播数据包的初始跳数限制（Hop limit）

**说明（Help）**

该值通常应大于 0。设备收到 IPv6 数据包时会递减此值；跳数限制（Hop limit）为 0 时丢弃数据包。发送时，如果跳数限制为 0，则在将数据包传输到网络之前将其丢弃。默认值为 1，与 IPv4 相同，表示除非应用明确要求，否则多播数据包不会离开本地网络。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_INITIAL_MCAST_TTL"></a>

## 399.45 `CONFIG_NET_INITIAL_MCAST_TTL`

**提示（Prompt）**：IPv4 多播数据包的初始生存时间（Time to Live，TTL）

**说明（Help）**

该值通常应大于 0。设备收到 IPv4 数据包时会递减此值；生存时间（TTL）为 0 时丢弃数据包。发送时，如果 TTL 为 0，则在将数据包传输到网络之前将其丢弃。默认值为 1，与 Linux 相同，表示除非应用明确要求，否则多播数据包不会离开本地网络。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_INITIAL_TTL"></a>

## 399.46 `CONFIG_NET_INITIAL_TTL`

**提示（Prompt）**：IPv4 单播数据包的初始生存时间（Time to Live，TTL）

**说明（Help）**

该值通常应大于 0。设备收到 IPv4 数据包时会递减此值；生存时间（TTL）为 0 时丢弃数据包。发送时，如果 TTL 为 0，则在将数据包传输到网络之前将其丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_INIT_PRIO"></a>

## 399.47 `CONFIG_NET_INIT_PRIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

网络初始化优先级（Initialization priority）。该数值决定网络协议栈在启动过程中的初始化先后。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_INTERFACE_NAME"></a>

## 399.48 `CONFIG_NET_INTERFACE_NAME`

**提示（Prompt）**：允许为网络接口（Network interface）设置名称

**说明（Help）**

允许应用为网络接口（Network interface）设置名称，以简化接口管理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NATIVE_SIM
CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALLOWLIST
CONFIG_MDNS_RESPONDER_IFACE_POLICY_DENYLIST
CONFIG_POSIX_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:930`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L930)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIFI_NATIVE_SIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NATIVE_SIM)、[`CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALLOWLIST`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALLOWLIST)、[`CONFIG_MDNS_RESPONDER_IFACE_POLICY_DENYLIST`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_IFACE_POLICY_DENYLIST)、[`CONFIG_POSIX_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_NETWORKING)。

<a id="CONFIG_NET_INTERFACE_NAME_LEN"></a>

## 399.49 `CONFIG_NET_INTERFACE_NAME_LEN`

**提示（Prompt）**：网络接口名称（Interface name）的最大长度

**说明（Help）**

网络接口名称（Interface name）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_INTERFACE_NAME && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[2, 15]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:937`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L937)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 允许为网络接口（Network interface）设置名称

**配置项引用（Symbol References）**：[`CONFIG_NET_INTERFACE_NAME`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_INTERFACE_NAME)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_IPV4"></a>

## 399.50 `CONFIG_NET_IPV4`

**提示（Prompt）**：IPv4（互联网协议第 4 版）

**说明（Help）**

启用 IPv4 支持。启用后，设备能够发送和接收 IPv4 网络数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_CONFIG_NEED_IPV4
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CONFIG_NEED_IPV4`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_NEED_IPV4)。

<a id="CONFIG_NET_IPV4_ACCEPT_ZERO_BROADCAST"></a>

## 399.51 `CONFIG_NET_IPV4_ACCEPT_ZERO_BROADCAST`

**提示（Prompt）**：接受 `0.0.0.0` 广播目的地址（Broadcast destination address）

**说明（Help）**

启用后，接受发往 RFC 1122 第 3.3.6 节所述非标准广播地址 `0.0.0.0` 的 UDP 数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_ACD"></a>

## 399.52 `CONFIG_NET_IPV4_ACD`

**提示（Prompt）**：启用 IPv4 地址冲突检测（Address Conflict Detection，RFC 5227）

**说明（Help）**

启用 RFC 5227 规定的 IPv4 地址冲突检测（Address Conflict Detection），基于 ARP 探测（Probe）和通告（Announcement）检测冲突。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ARP && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_IPV4_AUTO
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_ARP`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4_AUTO`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE"></a>

## 399.53 `CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IPv4 地址冲突检测日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_IPV4_ACD && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IPV4_ACD_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_IPV4_ACD_LOG_LEVEL_OFF
CONFIG_NET_IPV4_ACD_LOG_LEVEL_ERR
CONFIG_NET_IPV4_ACD_LOG_LEVEL_WRN
CONFIG_NET_IPV4_ACD_LOG_LEVEL_INF
CONFIG_NET_IPV4_ACD_LOG_LEVEL_DBG
CONFIG_NET_IPV4_ACD_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_IPV4_ACD`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4_ACD_LOG_LEVEL_DEFAULT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_IPV4_ACD_LOG_LEVEL_OFF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD_LOG_LEVEL_OFF)、[`CONFIG_NET_IPV4_ACD_LOG_LEVEL_ERR`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD_LOG_LEVEL_ERR)、[`CONFIG_NET_IPV4_ACD_LOG_LEVEL_WRN`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD_LOG_LEVEL_WRN)、[`CONFIG_NET_IPV4_ACD_LOG_LEVEL_INF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD_LOG_LEVEL_INF)、[`CONFIG_NET_IPV4_ACD_LOG_LEVEL_DBG`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_ACD_LOG_LEVEL_DBG"></a>

## 399.54 `CONFIG_NET_IPV4_ACD_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 地址冲突检测日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_ACD_LOG_LEVEL_DEFAULT"></a>

## 399.55 `CONFIG_NET_IPV4_ACD_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 地址冲突检测日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_ACD_LOG_LEVEL_ERR"></a>

## 399.56 `CONFIG_NET_IPV4_ACD_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 地址冲突检测日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_ACD_LOG_LEVEL_INF"></a>

## 399.57 `CONFIG_NET_IPV4_ACD_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 地址冲突检测日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_ACD_LOG_LEVEL_OFF"></a>

## 399.58 `CONFIG_NET_IPV4_ACD_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 地址冲突检测日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_ACD_LOG_LEVEL_WRN"></a>

## 399.59 `CONFIG_NET_IPV4_ACD_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 地址冲突检测日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_AUTO"></a>

## 399.60 `CONFIG_NET_IPV4_AUTO`

**提示（Prompt）**：IPv4 自动配置（Autoconfiguration）

**说明（Help）**

启用 IPv4 地址自动配置（Automatic IP address configuration），参见 RFC 3927。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ARP && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_IPV4_ACD
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
CONFIG_NET_MGMT_EVENT_INFO
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_ARP`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4_ACD`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ACD)、[`CONFIG_NET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NET_MGMT_EVENT_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT_INFO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE"></a>

## 399.61 `CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IPv4 自动配置客户端日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_IPV4_AUTO && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IPV4_AUTO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_IPV4_AUTO_LOG_LEVEL_OFF
CONFIG_NET_IPV4_AUTO_LOG_LEVEL_ERR
CONFIG_NET_IPV4_AUTO_LOG_LEVEL_WRN
CONFIG_NET_IPV4_AUTO_LOG_LEVEL_INF
CONFIG_NET_IPV4_AUTO_LOG_LEVEL_DBG
CONFIG_NET_IPV4_AUTO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_IPV4_AUTO`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4_AUTO_LOG_LEVEL_DEFAULT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_IPV4_AUTO_LOG_LEVEL_OFF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO_LOG_LEVEL_OFF)、[`CONFIG_NET_IPV4_AUTO_LOG_LEVEL_ERR`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO_LOG_LEVEL_ERR)、[`CONFIG_NET_IPV4_AUTO_LOG_LEVEL_WRN`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO_LOG_LEVEL_WRN)、[`CONFIG_NET_IPV4_AUTO_LOG_LEVEL_INF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO_LOG_LEVEL_INF)、[`CONFIG_NET_IPV4_AUTO_LOG_LEVEL_DBG`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_AUTO_LOG_LEVEL_DBG"></a>

## 399.62 `CONFIG_NET_IPV4_AUTO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 自动配置客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_AUTO_LOG_LEVEL_DEFAULT"></a>

## 399.63 `CONFIG_NET_IPV4_AUTO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 自动配置客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_AUTO_LOG_LEVEL_ERR"></a>

## 399.64 `CONFIG_NET_IPV4_AUTO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 自动配置客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_AUTO_LOG_LEVEL_INF"></a>

## 399.65 `CONFIG_NET_IPV4_AUTO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 自动配置客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_AUTO_LOG_LEVEL_OFF"></a>

## 399.66 `CONFIG_NET_IPV4_AUTO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 自动配置客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_AUTO_LOG_LEVEL_WRN"></a>

## 399.67 `CONFIG_NET_IPV4_AUTO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 自动配置客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_CONN_TRACK_MAX_NUM"></a>

## 399.68 `CONFIG_NET_IPV4_CONN_TRACK_MAX_NUM`

**提示（Prompt）**：为 IP 转发维护的连接跟踪（Connection tracking）最大数量

**说明（Help）**

同时维护的活动连接跟踪记录（Connection track）的最大数量。连接不活动时间超过超时值后，该记录会老化失效。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_NAT && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L307)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 网络地址转换（Network Address Translation，NAT；实验性）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_NAT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_NAT)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_DEFAULT_NETMASK"></a>

## 399.69 `CONFIG_NET_IPV4_DEFAULT_NETMASK`

**提示（Prompt）**：已注册 IPv4 地址的默认网络掩码长度（Netmask length）

**说明（Help）**

已注册 IPv4 地址的默认网络掩码长度（Netmask length）。必要时，应用可通过 `net_if_ipv4_set_netmask_by_addr()` API 设置自定义网络掩码。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
24
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_IPV4_FORWARDING"></a>

## 399.70 `CONFIG_NET_IPV4_FORWARDING`

**提示（Prompt）**：接口之间的 IPv4 转发（Forwarding）

**说明（Help）**

允许设备在不同网络接口和网络技术之间转发 IPv4 数据包。此项独立于 `NET_IPV4_ROUTE`；后者仅启用用于主机端路由选择和命令行路由命令的 IPv4 路由表（Route table）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_ROUTE && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_IPV4_ROUTING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:269`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L269)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → 邻居缓存（Neighbor cache） → IPv4 单播路由表（Unicast route table）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ROUTE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ROUTE)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4_ROUTING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_ROUTING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_FRAGMENT"></a>

## 399.71 `CONFIG_NET_IPV4_FRAGMENT`

**提示（Prompt）**：支持 IPv4 分片（Fragmentation）

**说明（Help）**

IPv4 分片（Fragmentation）默认禁用，因此接收和发送的数据包大小受最大传输单元（MTU）限制；以太网的 MTU 为 1500 字节。如果启用分片支持，请增加接收（RX）数据缓冲区数量，以便接收更大的数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被弱选择（Implied by）**

```text
CONFIG_NXP_WIFI_TX_RX_ZERO_COPY
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NXP_WIFI_TX_RX_ZERO_COPY`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_TX_RX_ZERO_COPY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_FRAGMENT_MAX_COUNT"></a>

## 399.72 `CONFIG_NET_IPV4_FRAGMENT_MAX_COUNT`

**提示（Prompt）**：可同时重组（Reassemble）的数据包数量

**说明（Help）**

允许同时等待重组（Reassembly）的已分片 IPv4 数据包数量。可能需要增加网络缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_FRAGMENT && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → 支持 IPv4 分片（Fragmentation）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_FRAGMENT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_FRAGMENT)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_FRAGMENT_MAX_PKT"></a>

## 399.73 `CONFIG_NET_IPV4_FRAGMENT_MAX_PKT`

**提示（Prompt）**：重组一个数据包时可处理的分片（Fragment）数量

**说明（Help）**

收到的分片（Fragment）在重组前存放在各数据包独立的队列中。该值定义为重组单个数据包可同时处理的分片数量。如果预计会收到分成两个以上分片的数据包，可以增大该值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_FRAGMENT && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → 支持 IPv4 分片（Fragmentation）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_FRAGMENT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_FRAGMENT)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_FRAGMENT_TIMEOUT"></a>

## 399.74 `CONFIG_NET_IPV4_FRAGMENT_TIMEOUT`

**提示（Prompt）**：等待接收分片（Fragment）的时长

**说明（Help）**

等待 IPv4 分片（Fragment）到达多久后重组操作超时，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_FRAGMENT && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 60]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → 支持 IPv4 分片（Fragmentation）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_FRAGMENT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_FRAGMENT)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_HDR_OPTIONS"></a>

## 399.75 `CONFIG_NET_IPV4_HDR_OPTIONS`

**提示（Prompt）**：IPv4 报头选项（Header option）支持

**说明（Help）**

启用 IPv4 报头选项（Header option）支持。目前仅支持 ICMPv4 回显请求（Echo request），且只处理 RecordRoute 和 Timestamp 选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_IPV4_IGMP
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4_IGMP`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_IGMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_IGMP"></a>

## 399.76 `CONFIG_NET_IPV4_IGMP`

**提示（Prompt）**：互联网组管理协议（Internet Group Management Protocol，IGMPv2）支持

**说明（Help）**

根据网络需求选择此项。如果需要 IPv4 多播（Multicast）支持，通常应启用 IGMP。目前支持 IGMPv2 及更早版本。由于必须发送 IP 路由器警报选项（Router Alert option），因此需要 IPv4 报头支持。详见 RFC 2236。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_IPV4_HDR_OPTIONS
```

**被选择（Selected by）**

```text
CONFIG_MDNS_RESPONDER
CONFIG_LLMNR_RESPONDER
CONFIG_MQTT_SN_TRANSPORT_UDP
CONFIG_PTP_UDP_IPV4_PROTOCOL
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4_HDR_OPTIONS`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_HDR_OPTIONS)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_LLMNR_RESPONDER`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER)、[`CONFIG_MQTT_SN_TRANSPORT_UDP`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_TRANSPORT_UDP)、[`CONFIG_PTP_UDP_IPV4_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_UDP_IPV4_PROTOCOL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_IGMPV3"></a>

## 399.77 `CONFIG_NET_IPV4_IGMPV3`

**提示（Prompt）**：互联网组管理协议第 3 版（Internet Group Management Protocol version 3，IGMPv3）支持

**说明（Help）**

使用 IGMPv3 管理多播组（Multicast group）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_IGMP && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → 互联网组管理协议（Internet Group Management Protocol，IGMPv2）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_IGMP`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_IGMP)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_IGMP_REQUIRE_ROUTER_ALERT"></a>

## 399.78 `CONFIG_NET_IPV4_IGMP_REQUIRE_ROUTER_ALERT`

**提示（Prompt）**：忽略不含路由器警报选项（Router Alert option）的 IGMPv2 和 IGMPv3 查询

**说明（Help）**

查询应携带 IP 路由器警报选项（Router Alert option）；不含该选项的查询可能由本地网络之外伪造，因此主机应忽略它们，参见 RFC 3376 第 9.1 节。但有些查询器（Querier），包括部分 IGMP 侦听交换机（IGMP snooping switch），会省略此选项，从而导致其查询得不到响应。因此，默认不执行此检查，只有启用本选项才进行检查。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_IGMP && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → 互联网组管理协议（Internet Group Management Protocol，IGMPv2）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_IGMP`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_IGMP)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_IGMP_ROBUSTNESS"></a>

## 399.79 `CONFIG_NET_IPV4_IGMP_ROBUSTNESS`

**提示（Prompt）**：IGMP 健壮性变量（Robustness Variable）

**说明（Help）**

RFC 3376 第 8.1 节的健壮性变量（Robustness Variable）用于根据网络预期丢包情况进行调整，不应设为 1。加入组时主动发送的报告总次数等于该变量的值。收到旧版本查询器最后一次查询后，记住该查询器的时长为：健壮性变量乘以查询间隔（Query Interval），再加上一个查询响应间隔（Query Response Interval）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_IGMP && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 7]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → 互联网组管理协议（Internet Group Management Protocol，IGMPv2）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_IGMP`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_IGMP)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_IPTABLE_RULE_MAX_NUM"></a>

## 399.80 `CONFIG_NET_IPV4_IPTABLE_RULE_MAX_NUM`

**提示（Prompt）**：用于 IP 转发的 IP 表规则（IP table rule）最大数量

**说明（Help）**

活动 IP 表规则（IP table rule）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_NAT && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:315`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L315)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 网络地址转换（Network Address Translation，NAT；实验性）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_NAT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_NAT)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_LOG_LEVEL_CHOICE"></a>

## 399.81 `CONFIG_NET_IPV4_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IPv4 核心日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IPV4_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_IPV4_LOG_LEVEL_OFF
CONFIG_NET_IPV4_LOG_LEVEL_ERR
CONFIG_NET_IPV4_LOG_LEVEL_WRN
CONFIG_NET_IPV4_LOG_LEVEL_INF
CONFIG_NET_IPV4_LOG_LEVEL_DBG
CONFIG_NET_IPV4_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4_LOG_LEVEL_DEFAULT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_IPV4_LOG_LEVEL_OFF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_LOG_LEVEL_OFF)、[`CONFIG_NET_IPV4_LOG_LEVEL_ERR`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_LOG_LEVEL_ERR)、[`CONFIG_NET_IPV4_LOG_LEVEL_WRN`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_LOG_LEVEL_WRN)、[`CONFIG_NET_IPV4_LOG_LEVEL_INF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_LOG_LEVEL_INF)、[`CONFIG_NET_IPV4_LOG_LEVEL_DBG`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_LOG_LEVEL_DBG"></a>

## 399.82 `CONFIG_NET_IPV4_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 核心日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_LOG_LEVEL_DEFAULT"></a>

## 399.83 `CONFIG_NET_IPV4_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 核心日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_LOG_LEVEL_ERR"></a>

## 399.84 `CONFIG_NET_IPV4_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 核心日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_LOG_LEVEL_INF"></a>

## 399.85 `CONFIG_NET_IPV4_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 核心日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_LOG_LEVEL_OFF"></a>

## 399.86 `CONFIG_NET_IPV4_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 核心日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_LOG_LEVEL_WRN"></a>

## 399.87 `CONFIG_NET_IPV4_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 核心日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_IPV4_MAPPING_TO_IPV6"></a>

## 399.88 `CONFIG_NET_IPV4_MAPPING_TO_IPV6`

**提示（Prompt）**：支持 IPv4 映射的 IPv6 地址（IPv4-mapped IPv6 address）

**说明（Help）**

支持 IPv4 映射的 IPv6 地址类型（v4-mapped-on-v6），使 IPv4 和 IPv6 共享本地端口空间。当应用通过 IPv6 套接字（Socket）收到 IPv4 连接或数据包时，其源地址会映射为 IPv6 地址。此功能默认禁用，即 `IPV6_V6ONLY` 套接字选项始终开启。启用本选项后，仍可在运行时通过 `IPV6_V6ONLY` 控制套接字行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_SSH_SERVER
CONFIG_SSH_CLIENT
CONFIG_WIREGUARD
```

**被弱选择（Implied by）**

```text
CONFIG_NETMIDI2_HOST
CONFIG_HTTP_SERVER
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SSH_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_SERVER)、[`CONFIG_SSH_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CLIENT)、[`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)、[`CONFIG_NETMIDI2_HOST`](P395_subsys_net_配置项参考_5.md#CONFIG_NETMIDI2_HOST)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_IPV4_MAX_NEIGHBORS"></a>

## 399.89 `CONFIG_NET_IPV4_MAX_NEIGHBORS`

**提示（Prompt）**：支持的 IPv4 邻居（Neighbor）数量

**说明（Help）**

该值取决于网络需求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_NBR_CACHE && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 254]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:248`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L248)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → 邻居缓存（Neighbor cache）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_NBR_CACHE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_NBR_CACHE)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_MAX_ROUTES"></a>

## 399.90 `CONFIG_NET_IPV4_MAX_ROUTES`

**提示（Prompt）**：可存储的路由表项（Routing entry）最大数量

**说明（Help）**

决定路由表（Routing table）能够存储多少个表项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_ROUTE && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IPV4_MAX_NEIGHBORS
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:287`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L287)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → 邻居缓存（Neighbor cache） → IPv4 单播路由表（Unicast route table）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ROUTE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ROUTE)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4_MAX_NEIGHBORS`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_MAX_NEIGHBORS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_MTU"></a>

## 399.91 `CONFIG_NET_IPV4_MTU`

**提示（Prompt）**：IPv4 最大传输单元（MTU）的初始值

**说明（Help）**

该值通常应为 576；按原文说明，这是实现必须在不分片的情况下支持的最小 IPv4 数据包大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
576
```

**取值范围（Ranges）**

```text
[576, 1500]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_NAT"></a>

## 399.92 `CONFIG_NET_IPV4_NAT`

**提示（Prompt）**：IPv4 网络地址转换（Network Address Translation，NAT；实验性）

**说明（Help）**

更新发往其他接口的数据包的地址和端口，并交由路由过程（Route process）处理。添加 IP 表规则（iptable rule），以允许转发指定的数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_FORWARDING && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_PKT_FILTER
CONFIG_NET_PKT_FILTER_IPV4_HOOK
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:294`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L294)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_FORWARDING`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_FORWARDING)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_FILTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_FILTER)、[`CONFIG_NET_PKT_FILTER_IPV4_HOOK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_FILTER_IPV4_HOOK)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_NBR_CACHE"></a>

## 399.93 `CONFIG_NET_IPV4_NBR_CACHE`

**提示（Prompt）**：邻居缓存（Neighbor cache）

**说明（Help）**

该值取决于网络需求。如果有多个网络接口，并希望控制 IPv4 数据包发往何处，可能需要启用邻居缓存（Neighbor cache）和 IPv4 路由表（Route table）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_ARP
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_ARP`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_PMTU"></a>

## 399.94 `CONFIG_NET_IPV4_PMTU`

**提示（Prompt）**：IPv4 路径 MTU 发现（Path MTU Discovery）

**说明（Help）**

启用 IPv4 路径 MTU 发现（Path MTU Discovery），参见 RFC 1191。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_QUIC
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:213`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L213)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_PMTU_DESTINATION_CACHE_ENTRIES"></a>

## 399.95 `CONFIG_NET_IPV4_PMTU_DESTINATION_CACHE_ENTRIES`

**提示（Prompt）**：IPv4 路径 MTU（PMTU）目的地址缓存表项数量

**说明（Help）**

针对各目的地址可跟踪的路径 MTU（PMTU）表项数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_PMTU && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 路径 MTU 发现（Path MTU Discovery）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_PMTU`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_PMTU)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_PMTU_DPLPMTUD"></a>

## 399.96 `CONFIG_NET_IPV4_PMTU_DPLPMTUD`

**提示（Prompt）**：使用数据报（Datagram）执行 IPv4 路径 MTU 发现

**说明（Help）**

启用 IPv4 数据报分组化层路径 MTU 发现（Datagram Packetization Layer Path MTU Discovery），参见 RFC 8899。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && CONFIG_NET_IPV4_PMTU && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_QUIC
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:232`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L232)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 路径 MTU 发现（Path MTU Discovery）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_IPV4_PMTU`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_PMTU)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_PMTU_PTB"></a>

## 399.97 `CONFIG_NET_IPV4_PMTU_PTB`

**提示（Prompt）**：使用 ICMP 报文执行 IPv4 路径 MTU 发现（PMTU Discovery）

**说明（Help）**

启用 IPv4 路径 MTU 发现（Path MTU Discovery），参见 RFC 1191。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_PMTU && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:225`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L225)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 路径 MTU 发现（Path MTU Discovery）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_PMTU`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_PMTU)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_ROUTE"></a>

## 399.98 `CONFIG_NET_IPV4_ROUTE`

**提示（Prompt）**：IPv4 单播路由表（Unicast route table）支持

**说明（Help）**

启用 IPv4 单播路由表（Unicast route table），以及针对本地产生流量的路由感知目的地选择。静态 IPv4 路由、网络命令行中的路由查询，以及 VPN 流量导向等主机端路由选择，都需要此选项。如果设备还必须在接口之间转发数据包，请同时启用 `NET_IPV4_FORWARDING`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_NBR_CACHE && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_IPV4_NBR_CACHE
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv4:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv4#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → 邻居缓存（Neighbor cache）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_NBR_CACHE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_NBR_CACHE)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE"></a>

## 399.99 `CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IPv4 路由管理日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_NATIVE_IPV4 && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_OFF
CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_ERR
CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_WRN
CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_INF
CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_DBG
CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_NATIVE_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV4)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_DEFAULT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_OFF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_OFF)、[`CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_ERR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_ERR)、[`CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_WRN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_WRN)、[`CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_INF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_INF)、[`CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_DBG`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV4`。

<a id="CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_DBG"></a>

## 399.100 `CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv4（互联网协议第 4 版） → IPv4 路由管理日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_ROUTE_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P398_subsys_net_配置项参考_8.md) · [返回大纲](大纲.md) · [下一章](P400_subsys_net_配置项参考_10.md)
