---
id: learning.zephyr-docs.kconfig-reference.page-408
title: "`subsys/net`配置项参考（18/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第408章\_`subsys/net`配置项参考（18/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SNTP_LOG_LEVEL_CHOICE"></a>

## 408.1 `CONFIG_SNTP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：SNTP 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_SNTP_LIB && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_SNTP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SNTP_LOG_LEVEL_OFF
CONFIG_SNTP_LOG_LEVEL_ERR
CONFIG_SNTP_LOG_LEVEL_WRN
CONFIG_SNTP_LOG_LEVEL_INF
CONFIG_SNTP_LOG_LEVEL_DBG
CONFIG_SNTP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 简单网络时间协议（Simple Network Time Protocol，SNTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_SNTP_LIB`](P407_subsys_net_配置项参考_17.md#CONFIG_SNTP_LIB)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SNTP_LOG_LEVEL_DEFAULT`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_LOG_LEVEL_DEFAULT)、[`CONFIG_SNTP_LOG_LEVEL_OFF`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_LOG_LEVEL_OFF)、[`CONFIG_SNTP_LOG_LEVEL_ERR`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_LOG_LEVEL_ERR)、[`CONFIG_SNTP_LOG_LEVEL_WRN`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_LOG_LEVEL_WRN)、[`CONFIG_SNTP_LOG_LEVEL_INF`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_LOG_LEVEL_INF)、[`CONFIG_SNTP_LOG_LEVEL_DBG`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_LOG_LEVEL_DBG)。

<a id="CONFIG_SNTP_LOG_LEVEL_DBG"></a>

## 408.2 `CONFIG_SNTP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SNTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 简单网络时间协议（Simple Network Time Protocol，SNTP）支持 → SNTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SNTP_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SNTP_LOG_LEVEL_DEFAULT"></a>

## 408.3 `CONFIG_SNTP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SNTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 简单网络时间协议（Simple Network Time Protocol，SNTP）支持 → SNTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SNTP_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SNTP_LOG_LEVEL_ERR"></a>

## 408.4 `CONFIG_SNTP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SNTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 简单网络时间协议（Simple Network Time Protocol，SNTP）支持 → SNTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SNTP_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SNTP_LOG_LEVEL_INF"></a>

## 408.5 `CONFIG_SNTP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SNTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 简单网络时间协议（Simple Network Time Protocol，SNTP）支持 → SNTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SNTP_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SNTP_LOG_LEVEL_OFF"></a>

## 408.6 `CONFIG_SNTP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SNTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 简单网络时间协议（Simple Network Time Protocol，SNTP）支持 → SNTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SNTP_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SNTP_LOG_LEVEL_WRN"></a>

## 408.7 `CONFIG_SNTP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SNTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 简单网络时间协议（Simple Network Time Protocol，SNTP）支持 → SNTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SNTP_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SNTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SNTP_SERVER"></a>

## 408.8 `CONFIG_SNTP_SERVER`

**提示（Prompt）**：SNTP 服务器

**说明（Help）**

启用简单网络时间协议（SNTP）服务器支持。服务器在每个已启用的地址族（Address family）上通过 UDP 端口 123 响应查询。应用负责设置系统时钟，并通过 `sntp_server_clock_source()` 告知服务器时钟来源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && (CONFIG_NET_IPV4 || CONFIG_NET_IPV6) && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_SNTP_LIB
CONFIG_NET_SOCKETS_SERVICE
```

**定义位置（Location）**：[`subsys/net/lib/sntp/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sntp/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 简单网络时间协议（Simple Network Time Protocol，SNTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SNTP_LIB`](P407_subsys_net_配置项参考_17.md#CONFIG_SNTP_LIB)、[`CONFIG_NET_SOCKETS_SERVICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SERVICE)。

<a id="CONFIG_SNTP_UNCERTAINTY"></a>

## 408.9 `CONFIG_SNTP_UNCERTAINTY`

**提示（Prompt）**：计算 SNTP 不确定度（Uncertainty）并设置运行时间时间戳（Uptime timestamp）

**说明（Help）**

为 `sntp_time` 结构提供时间有效时刻对应的系统运行时间时间戳（Uptime timestamp），以及以微秒为单位的时间不确定度（Uncertainty），从而获得更可靠的时间戳。时间的表达方式为：在给定运行时间时间戳处，`seconds,fraction +/- uncertainty`。启用后会使用更多内存等资源，通常无需启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SNTP && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/sntp/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sntp/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 简单网络时间协议（Simple Network Time Protocol，SNTP）支持 → 简单网络时间协议客户端（SNTP client）

**配置项引用（Symbol References）**：[`CONFIG_SNTP`](P407_subsys_net_配置项参考_17.md#CONFIG_SNTP)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_SOCKS"></a>

## 408.10 `CONFIG_SOCKS`

**提示（Prompt）**：SOCKS5 代理（Proxy）

**说明（Help）**

启用 SOCKS5 代理（Proxy）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/socks/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/socks/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_SOCKS_LOG_LEVEL_CHOICE"></a>

## 408.11 `CONFIG_SOCKS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：SOCKS 代理（Proxy）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_SOCKS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_SOCKS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SOCKS_LOG_LEVEL_OFF
CONFIG_SOCKS_LOG_LEVEL_ERR
CONFIG_SOCKS_LOG_LEVEL_WRN
CONFIG_SOCKS_LOG_LEVEL_INF
CONFIG_SOCKS_LOG_LEVEL_DBG
CONFIG_SOCKS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → SOCKS5 代理（Proxy）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_SOCKS`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SOCKS_LOG_LEVEL_DEFAULT`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS_LOG_LEVEL_DEFAULT)、[`CONFIG_SOCKS_LOG_LEVEL_OFF`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS_LOG_LEVEL_OFF)、[`CONFIG_SOCKS_LOG_LEVEL_ERR`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS_LOG_LEVEL_ERR)、[`CONFIG_SOCKS_LOG_LEVEL_WRN`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS_LOG_LEVEL_WRN)、[`CONFIG_SOCKS_LOG_LEVEL_INF`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS_LOG_LEVEL_INF)、[`CONFIG_SOCKS_LOG_LEVEL_DBG`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS_LOG_LEVEL_DBG)。

<a id="CONFIG_SOCKS_LOG_LEVEL_DBG"></a>

## 408.12 `CONFIG_SOCKS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOCKS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → SOCKS5 代理（Proxy） → SOCKS 代理（Proxy）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SOCKS_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SOCKS_LOG_LEVEL_DEFAULT"></a>

## 408.13 `CONFIG_SOCKS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOCKS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → SOCKS5 代理（Proxy） → SOCKS 代理（Proxy）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SOCKS_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SOCKS_LOG_LEVEL_ERR"></a>

## 408.14 `CONFIG_SOCKS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOCKS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → SOCKS5 代理（Proxy） → SOCKS 代理（Proxy）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SOCKS_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SOCKS_LOG_LEVEL_INF"></a>

## 408.15 `CONFIG_SOCKS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOCKS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → SOCKS5 代理（Proxy） → SOCKS 代理（Proxy）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SOCKS_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SOCKS_LOG_LEVEL_OFF"></a>

## 408.16 `CONFIG_SOCKS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOCKS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → SOCKS5 代理（Proxy） → SOCKS 代理（Proxy）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SOCKS_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SOCKS_LOG_LEVEL_WRN"></a>

## 408.17 `CONFIG_SOCKS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SOCKS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → SOCKS5 代理（Proxy） → SOCKS 代理（Proxy）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SOCKS_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SOCKS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SSH_CHANNEL_BUF_SIZE"></a>

## 408.18 `CONFIG_SSH_CHANNEL_BUF_SIZE`

**提示（Prompt）**：SSH 通道缓冲区大小（Channel buffer size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SSH_CLIENT"></a>

## 408.19 `CONFIG_SSH_CLIENT`

**提示（Prompt）**：SSH 客户端（Client）［实验性，Experimental］

**说明（Help）**

SSH-2 客户端（Client）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_ZVFS
CONFIG_ZVFS_EVENTFD
CONFIG_NET_IPV4_MAPPING_TO_IPV6 if CONFIG_NET_IPV4 && CONFIG_NET_IPV6
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_EVENTFD`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_EVENTFD)、[`CONFIG_NET_IPV4_MAPPING_TO_IPV6`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_MAPPING_TO_IPV6)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)。

<a id="CONFIG_SSH_CLIENT_MAX_CLIENTS"></a>

## 408.20 `CONFIG_SSH_CLIENT_MAX_CLIENTS`

**提示（Prompt）**：SSH 客户端实例（Client instance）的最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH_CLIENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH_CLIENT`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_CLIENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_SSH_DEFAULT_INFO_BANNER"></a>

## 408.21 `CONFIG_SSH_DEFAULT_INFO_BANNER`

**提示（Prompt）**：默认 SSH 信息横幅（Info banner）

**说明（Help）**

此文本打印在欢迎横幅（Welcome banner）之后。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"To exit press 'Enter' then '~' then '.' (i.e. enter tilde dot)"
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH_SERVER`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_SSH_DEFAULT_TERMINAL_HEIGHT"></a>

## 408.22 `CONFIG_SSH_DEFAULT_TERMINAL_HEIGHT`

**提示（Prompt）**：默认终端高度（Terminal height）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
24
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SSH_DEFAULT_TERMINAL_WIDTH"></a>

## 408.23 `CONFIG_SSH_DEFAULT_TERMINAL_WIDTH`

**提示（Prompt）**：默认终端宽度（Terminal width）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SSH_DEFAULT_WELCOME_BANNER"></a>

## 408.24 `CONFIG_SSH_DEFAULT_WELCOME_BANNER`

**提示（Prompt）**：默认 SSH 欢迎横幅（Welcome banner）

**说明（Help）**

Zephyr SSH 构建版本（Build version）会追加到此字符串之后。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"Welcome to Zephyr OS build "
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SSH_HOST_KEY_ALG_RSA_SHA2_256"></a>

## 408.25 `CONFIG_SSH_HOST_KEY_ALG_RSA_SHA2_256`

**提示（Prompt）**：`rsa-sha2-256` 主机密钥算法（Host key algorithm）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SSH_HOST_KEY_ALG_RSA_SHA2_512"></a>

## 408.26 `CONFIG_SSH_HOST_KEY_ALG_RSA_SHA2_512`

**提示（Prompt）**：`rsa-sha2-512` 主机密钥算法（Host key algorithm）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH && CONFIG_NETWORKING
```

**弱选择（Implies）**

```text
CONFIG_PSA_WANT_ALG_SHA_512
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PSA_WANT_ALG_SHA_512`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_512)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SSH_HOST_KEY_RSA"></a>

## 408.27 `CONFIG_SSH_HOST_KEY_RSA`

**提示（Prompt）**：RSA 主机密钥（Host key）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SSH_IDENTITY_OVERRIDE"></a>

## 408.28 `CONFIG_SSH_IDENTITY_OVERRIDE`

**提示（Prompt）**：覆盖 SSH 身份标识（Identity override）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH_IDENTITY_OVERRIDE_ENABLE && CONFIG_SSH && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 覆盖默认 SSH 身份标识（Identity），可用于测试。

**配置项引用（Symbol References）**：[`CONFIG_SSH_IDENTITY_OVERRIDE_ENABLE`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_IDENTITY_OVERRIDE_ENABLE)、[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SSH_IDENTITY_OVERRIDE_ENABLE"></a>

## 408.29 `CONFIG_SSH_IDENTITY_OVERRIDE_ENABLE`

**提示（Prompt）**：覆盖默认 SSH 身份标识（Identity），可用于测试。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SSH_LOG_LEVEL_CHOICE"></a>

## 408.30 `CONFIG_SSH_LOG_LEVEL_CHOICE`

**提示（Prompt）**：SSH 库日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_SSH_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SSH_LOG_LEVEL_OFF
CONFIG_SSH_LOG_LEVEL_ERR
CONFIG_SSH_LOG_LEVEL_WRN
CONFIG_SSH_LOG_LEVEL_INF
CONFIG_SSH_LOG_LEVEL_DBG
CONFIG_SSH_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SSH_LOG_LEVEL_DEFAULT`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_LOG_LEVEL_DEFAULT)、[`CONFIG_SSH_LOG_LEVEL_OFF`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_LOG_LEVEL_OFF)、[`CONFIG_SSH_LOG_LEVEL_ERR`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_LOG_LEVEL_ERR)、[`CONFIG_SSH_LOG_LEVEL_WRN`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_LOG_LEVEL_WRN)、[`CONFIG_SSH_LOG_LEVEL_INF`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_LOG_LEVEL_INF)、[`CONFIG_SSH_LOG_LEVEL_DBG`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_LOG_LEVEL_DBG)。

<a id="CONFIG_SSH_LOG_LEVEL_DBG"></a>

## 408.31 `CONFIG_SSH_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SSH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → SSH 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SSH_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SSH_LOG_LEVEL_DEFAULT"></a>

## 408.32 `CONFIG_SSH_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SSH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → SSH 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SSH_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SSH_LOG_LEVEL_ERR"></a>

## 408.33 `CONFIG_SSH_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SSH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → SSH 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SSH_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SSH_LOG_LEVEL_INF"></a>

## 408.34 `CONFIG_SSH_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SSH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → SSH 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SSH_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SSH_LOG_LEVEL_OFF"></a>

## 408.35 `CONFIG_SSH_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SSH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → SSH 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SSH_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SSH_LOG_LEVEL_WRN"></a>

## 408.36 `CONFIG_SSH_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SSH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → SSH 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_SSH_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SSH_MAX_CHANNELS"></a>

## 408.37 `CONFIG_SSH_MAX_CHANNELS`

**提示（Prompt）**：每个传输连接的 SSH 通道（Channel）最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SSH_MAX_HOST_KEYS"></a>

## 408.38 `CONFIG_SSH_MAX_HOST_KEYS`

**提示（Prompt）**：SSH 密钥生成器（Keygen）的主机密钥最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SSH_PORT"></a>

## 408.39 `CONFIG_SSH_PORT`

**提示（Prompt）**：SSH 监听或连接端口（Listen/connect port）

**说明（Help）**

SSH 服务器监听或 SSH 客户端连接的默认 TCP 端口。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
22
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SSH`。

<a id="CONFIG_SSH_SERVER"></a>

## 408.40 `CONFIG_SSH_SERVER`

**提示（Prompt）**：SSH 服务器（Server）［实验性，Experimental］

**说明（Help）**

SSH-2 服务器（Server）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_ZVFS
CONFIG_ZVFS_EVENTFD
CONFIG_NET_IPV4_MAPPING_TO_IPV6 if CONFIG_NET_IPV4 && CONFIG_NET_IPV6
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_EVENTFD`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_EVENTFD)、[`CONFIG_NET_IPV4_MAPPING_TO_IPV6`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_MAPPING_TO_IPV6)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)。

<a id="CONFIG_SSH_SERVER_MAX_CLIENTS"></a>

## 408.41 `CONFIG_SSH_SERVER_MAX_CLIENTS`

**提示（Prompt）**：每个 SSH 服务器的客户端（Client）最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH_SERVER`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_SSH_SERVER_MAX_SERVERS"></a>

## 408.42 `CONFIG_SSH_SERVER_MAX_SERVERS`

**提示（Prompt）**：SSH 服务器实例（Server instance）的最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSH_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SSH_SERVER`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_SSH_SERVER_SHELL_COUNT"></a>

## 408.43 `CONFIG_SSH_SERVER_SHELL_COUNT`

**提示（Prompt）**：每个传输连接的 SSH 命令行通道（Shell channel）最大数量

**说明（Help）**

本端作为服务器时，允许对端同时建立的 SSH 命令行连接（Shell connection）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL_BACKEND_SSH && CONFIG_SSH_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/ssh/Kconfig:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ssh/Kconfig#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_SHELL_BACKEND_SSH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_SSH)、[`CONFIG_SSH_SERVER`](P408_subsys_net_配置项参考_18.md#CONFIG_SSH_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_TFTPC_REQUEST_RETRANSMITS"></a>

## 408.44 `CONFIG_TFTPC_REQUEST_RETRANSMITS`

**提示（Prompt）**：TFTP 客户端向服务器重传请求（Request）的次数。

**说明（Help）**

TFTP 客户端发出请求后，等待 `TFTPC_REQUEST_TIMEOUT` 毫秒，接收服务器返回的数据。如果数据未在指定时间内到达，就向服务器重传请求，期待服务器及时响应。本值决定放弃并退出前，最多重传（Retransmit）请求多少次。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TFTP_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/net/lib/tftp/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tftp/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 TFTP 库支持（Socket TFTP Library Support）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_TFTP_LIB`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_TFTPC_REQUEST_TIMEOUT"></a>

## 408.45 `CONFIG_TFTPC_REQUEST_TIMEOUT`

**提示（Prompt）**：TFTP 客户端等待服务器响应（Response）的最长时间。

**说明（Help）**

TFTP 客户端等待服务器数据的最长时间，单位为毫秒。超过后，客户端认定服务器失败，并关闭连接。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TFTP_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`subsys/net/lib/tftp/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tftp/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 TFTP 库支持（Socket TFTP Library Support）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_TFTP_LIB`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_TFTP_LIB"></a>

## 408.46 `CONFIG_TFTP_LIB`

**提示（Prompt）**：基于套接字的 TFTP 库支持（Socket TFTP Library Support）［实验性，Experimental］

**说明（Help）**

启用 Zephyr 简单文件传输协议（TFTP）库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/tftp/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tftp/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_TFTP_LOG_LEVEL_CHOICE"></a>

## 408.47 `CONFIG_TFTP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：TFTP 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_TFTP_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_TFTP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_TFTP_LOG_LEVEL_OFF
CONFIG_TFTP_LOG_LEVEL_ERR
CONFIG_TFTP_LOG_LEVEL_WRN
CONFIG_TFTP_LOG_LEVEL_INF
CONFIG_TFTP_LOG_LEVEL_DBG
CONFIG_TFTP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 TFTP 库支持（Socket TFTP Library Support）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_TFTP_LIB`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_TFTP_LOG_LEVEL_DEFAULT`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LOG_LEVEL_DEFAULT)、[`CONFIG_TFTP_LOG_LEVEL_OFF`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LOG_LEVEL_OFF)、[`CONFIG_TFTP_LOG_LEVEL_ERR`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LOG_LEVEL_ERR)、[`CONFIG_TFTP_LOG_LEVEL_WRN`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LOG_LEVEL_WRN)、[`CONFIG_TFTP_LOG_LEVEL_INF`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LOG_LEVEL_INF)、[`CONFIG_TFTP_LOG_LEVEL_DBG`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LOG_LEVEL_DBG)。

<a id="CONFIG_TFTP_LOG_LEVEL_DBG"></a>

## 408.48 `CONFIG_TFTP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 TFTP 库支持（Socket TFTP Library Support）［实验性，Experimental］ → TFTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_TFTP_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TFTP_LOG_LEVEL_DEFAULT"></a>

## 408.49 `CONFIG_TFTP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 TFTP 库支持（Socket TFTP Library Support）［实验性，Experimental］ → TFTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_TFTP_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TFTP_LOG_LEVEL_ERR"></a>

## 408.50 `CONFIG_TFTP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 TFTP 库支持（Socket TFTP Library Support）［实验性，Experimental］ → TFTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_TFTP_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TFTP_LOG_LEVEL_INF"></a>

## 408.51 `CONFIG_TFTP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 TFTP 库支持（Socket TFTP Library Support）［实验性，Experimental］ → TFTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_TFTP_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TFTP_LOG_LEVEL_OFF"></a>

## 408.52 `CONFIG_TFTP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 TFTP 库支持（Socket TFTP Library Support）［实验性，Experimental］ → TFTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_TFTP_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TFTP_LOG_LEVEL_WRN"></a>

## 408.53 `CONFIG_TFTP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 TFTP 库支持（Socket TFTP Library Support）［实验性，Experimental］ → TFTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_TFTP_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_TFTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TLS_CREDENTIALS"></a>

## 408.54 `CONFIG_TLS_CREDENTIALS`

**提示（Prompt）**：传输层安全（TLS）的凭据管理。

**说明（Help）**

启用 TLS 凭据管理子系统（Credentials management subsystem）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_MCUMGR_TRANSPORT_UDP_DTLS
CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES
CONFIG_QUIC
CONFIG_WIFI_CREDENTIALS_RUNTIME_CERTIFICATES
```

**被弱选择（Implied by）**

```text
CONFIG_QUIC_SOCKOPT_TLS
CONFIG_NET_SOCKETS_SOCKOPT_TLS
```

**定义位置（Location）**：[`subsys/net/lib/tls_credentials/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tls_credentials/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MCUMGR_TRANSPORT_UDP_DTLS`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP_DTLS)、[`CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES)、[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)、[`CONFIG_WIFI_CREDENTIALS_RUNTIME_CERTIFICATES`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_RUNTIME_CERTIFICATES)、[`CONFIG_QUIC_SOCKOPT_TLS`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC_SOCKOPT_TLS)、[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)。

<a id="CONFIG_TLS_CREDENTIALS_BACKEND"></a>

## 408.55 `CONFIG_TLS_CREDENTIALS_BACKEND`

**提示（Prompt）**：TLS 凭据管理后端（Credentials management backend）

**说明（Help）**

TLS 凭据管理后端（Credentials management backend）的实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TLS_CREDENTIALS && CONFIG_TLS_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_TLS_CREDENTIALS_BACKEND_VOLATILE
```

**可选项（Choices）**

```text
CONFIG_TLS_CREDENTIALS_BACKEND_VOLATILE
CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE
```

**定义位置（Location）**：[`subsys/net/lib/tls_credentials/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tls_credentials/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_TLS_CREDENTIALS_BACKEND_VOLATILE`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS_BACKEND_VOLATILE)、[`CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE)。

<a id="CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE"></a>

## 408.56 `CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE`

**提示（Prompt）**：TLS 凭据管理受保护存储后端（Protected storage backend）

**说明（Help）**

使用受保护存储 API（Protected Storage API）的 TLS 凭据管理后端，通过完整性检查（Integrity check）保护凭据以应对物理攻击，并在系统重启后保留表项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BUILD_WITH_TFM || CONFIG_SECURE_STORAGE) && <choice CONFIG_TLS_CREDENTIALS_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_SECURE_STORAGE_64_BIT_UID if CONFIG_SECURE_STORAGE
```

**定义位置（Location）**：[`subsys/net/lib/tls_credentials/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tls_credentials/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。 → TLS 凭据管理后端（Credentials management backend）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SECURE_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE)、[`CONFIG_TLS_CREDENTIALS_BACKEND`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS_BACKEND)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_SECURE_STORAGE_64_BIT_UID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_64_BIT_UID)。

<a id="CONFIG_TLS_CREDENTIALS_BACKEND_VOLATILE"></a>

## 408.57 `CONFIG_TLS_CREDENTIALS_BACKEND_VOLATILE`

**提示（Prompt）**：TLS 凭据管理易失性后端（Volatile backend）

**说明（Help）**

TLS 凭据管理易失性后端（Volatile backend）的实现，将凭据保存在系统运行时内存中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TLS_CREDENTIALS_BACKEND>
```

**定义位置（Location）**：[`subsys/net/lib/tls_credentials/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tls_credentials/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。 → TLS 凭据管理后端（Credentials management backend）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS_BACKEND`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS_BACKEND)。

<a id="CONFIG_TLS_CREDENTIALS_SHELL"></a>

## 408.58 `CONFIG_TLS_CREDENTIALS_SHELL`

**提示（Prompt）**：TLS 凭据管理命令行（credentials management shell）

**说明（Help）**

启用用于管理 TLS 凭据（Credential）的命令行命令（Shell command）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TLS_CREDENTIALS && CONFIG_SHELL && CONFIG_BASE64 && CONFIG_TLS_CREDENTIALS && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES
CONFIG_WIFI_CREDENTIALS_RUNTIME_CERTIFICATES
```

**定义位置（Location）**：[`subsys/net/lib/tls_credentials/Kconfig.shell:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tls_credentials/Kconfig.shell#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_BASE64`](P197_lib_配置项参考_1.md#CONFIG_BASE64)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES)、[`CONFIG_WIFI_CREDENTIALS_RUNTIME_CERTIFICATES`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_RUNTIME_CERTIFICATES)。

<a id="CONFIG_TLS_CREDENTIALS_SHELL_CRED_BUF_SIZE"></a>

## 408.59 `CONFIG_TLS_CREDENTIALS_SHELL_CRED_BUF_SIZE`

**提示（Prompt）**：用于存储和获取凭据（Credential）的缓冲区大小，单位为字节。

**说明（Help）**

用于存储和获取凭据（Credential）的预分配缓冲区大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TLS_CREDENTIALS_SHELL && CONFIG_TLS_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/net/lib/tls_credentials/Kconfig.shell:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tls_credentials/Kconfig.shell#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。 → TLS 凭据管理命令行（credentials management shell）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS_SHELL`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS_SHELL)、[`CONFIG_TLS_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_TLS_CREDENTIALS_SHELL_CRED_OUTPUT_WIDTH"></a>

## 408.60 `CONFIG_TLS_CREDENTIALS_SHELL_CRED_OUTPUT_WIDTH`

**提示（Prompt）**：凭据输出行宽（Credential output line width，字符）

**说明（Help）**

指定 Base64 凭据（Credential）输出中连续各行的长度，单位为字符，必须为 4 的倍数。原文说明仅适用于 `???` 模式。

译注：`???` 是原文尚未明确的模式名称，未自行补全。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TLS_CREDENTIALS_SHELL && CONFIG_TLS_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/net/lib/tls_credentials/Kconfig.shell:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tls_credentials/Kconfig.shell#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。 → TLS 凭据管理命令行（credentials management shell）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS_SHELL`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS_SHELL)、[`CONFIG_TLS_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_TLS_CREDENTIALS_SHELL_DIGEST_BUF_SIZE"></a>

## 408.61 `CONFIG_TLS_CREDENTIALS_SHELL_DIGEST_BUF_SIZE`

**提示（Prompt）**：用于生成凭据摘要（Credential digest）的缓冲区

**说明（Help）**

预分配的缓冲区大小，单位为字节，用于临时存储凭据摘要（Credential digest）。摘要生成失败时，也用于打印错误消息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TLS_CREDENTIALS_SHELL && CONFIG_TLS_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
48
```

**定义位置（Location）**：[`subsys/net/lib/tls_credentials/Kconfig.shell:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tls_credentials/Kconfig.shell#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。 → TLS 凭据管理命令行（credentials management shell）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS_SHELL`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS_SHELL)、[`CONFIG_TLS_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_TLS_CREDENTIAL_FILENAMES"></a>

## 408.62 `CONFIG_TLS_CREDENTIAL_FILENAMES`

**提示（Prompt）**：指定 TLS 凭据文件名（Credential filename）

**说明（Help）**

允许套接字 API 的调用方指定安全证书（Security certificate）和私钥（Private key）的文件名，用于后续 TLS/SSL 协商。这些安全文件应已通过供应商工具或单独的二进制程序等方式预置到设备的安全文件系统（Secure file system）。目前，此选项仅适用于支持安全套接字卸载（Secure socket offload）的设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_OFFLOAD && CONFIG_TLS_CREDENTIALS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/tls_credentials/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tls_credentials/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_OFFLOAD`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_OFFLOAD)、[`CONFIG_TLS_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_TLS_MAX_CREDENTIALS_NUMBER"></a>

## 408.63 `CONFIG_TLS_MAX_CREDENTIALS_NUMBER`

**提示（Prompt）**：TLS 凭据（Credential）的最大数量

**说明（Help）**

可注册的 TLS 凭据（Credential）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TLS_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/tls_credentials/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tls_credentials/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE"></a>

## 408.64 `CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 设备网络（USB Device Network）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USB_DEVICE_NETWORK && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_OFF
CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_ERR
CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_WRN
CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_INF
CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_DBG
CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USB_DEVICE_NETWORK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_NETWORK)、[`CONFIG_USB_DEVICE_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_DEFAULT`](P408_subsys_net_配置项参考_18.md#CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_DEFAULT)、[`CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_OFF`](P408_subsys_net_配置项参考_18.md#CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_OFF)、[`CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_ERR`](P408_subsys_net_配置项参考_18.md#CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_ERR)、[`CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_WRN`](P408_subsys_net_配置项参考_18.md#CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_WRN)、[`CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_INF`](P408_subsys_net_配置项参考_18.md#CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_INF)、[`CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_DBG`](P408_subsys_net_配置项参考_18.md#CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USB_DEVICE_NETWORK`。

<a id="CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_DBG"></a>

## 408.65 `CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持 → USB 设备网络（USB Device Network）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_DEFAULT"></a>

## 408.66 `CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持 → USB 设备网络（USB Device Network）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_ERR"></a>

## 408.67 `CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持 → USB 设备网络（USB Device Network）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_INF"></a>

## 408.68 `CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持 → USB 设备网络（USB Device Network）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_OFF"></a>

## 408.69 `CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持 → USB 设备网络（USB Device Network）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_WRN"></a>

## 408.70 `CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备网络（USB Device Networking）支持 → USB 设备网络（USB Device Network）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE`](P408_subsys_net_配置项参考_18.md#CONFIG_USB_DEVICE_NETWORK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WEBSOCKET"></a>

## 408.71 `CONFIG_WEBSOCKET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通用 WebSocket 支持的辅助符号（Helper symbol）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_WEBSOCKET_CLIENT
```

**被选择（Selected by）**

```text
CONFIG_HTTP_SERVER_WEBSOCKET
```

**定义位置（Location）**：[`subsys/net/lib/websocket/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/websocket/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WEBSOCKET_CLIENT`](P408_subsys_net_配置项参考_18.md#CONFIG_WEBSOCKET_CLIENT)、[`CONFIG_HTTP_SERVER_WEBSOCKET`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_WEBSOCKET)。

<a id="CONFIG_WEBSOCKET_CLIENT"></a>

## 408.72 `CONFIG_WEBSOCKET_CLIENT`

**提示（Prompt）**：WebSocket 客户端（Client）支持［实验性，Experimental］

**说明（Help）**

启用 WebSocket 客户端库（Client library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS
CONFIG_HTTP_PARSER
CONFIG_HTTP_PARSER_URL
CONFIG_HTTP_CLIENT
CONFIG_BASE64
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_ALG_SHA_1
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_HTTP_SERVER_WEBSOCKET
```

**定义位置（Location）**：[`subsys/net/lib/websocket/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/websocket/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_HTTP_PARSER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER)、[`CONFIG_HTTP_PARSER_URL`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER_URL)、[`CONFIG_HTTP_CLIENT`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_CLIENT)、[`CONFIG_BASE64`](P197_lib_配置项参考_1.md#CONFIG_BASE64)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_ALG_SHA_1`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_1)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_HTTP_SERVER_WEBSOCKET`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_WEBSOCKET)。

<a id="CONFIG_WEBSOCKET_CONSOLE"></a>

## 408.73 `CONFIG_WEBSOCKET_CONSOLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，仅在 WebSocket 控制台（Console）所需的全部选项均已设置时启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_HTTP_SERVER_WEBSOCKET && CONFIG_SHELL_BACKEND_WEBSOCKET
```

**定义位置（Location）**：[`subsys/net/lib/http/Kconfig:297`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/http/Kconfig#L297)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 服务器（Server）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_HTTP_SERVER_WEBSOCKET`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_WEBSOCKET)、[`CONFIG_SHELL_BACKEND_WEBSOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_WEBSOCKET)。

<a id="CONFIG_WEBSOCKET_DEDICATED_HEAP"></a>

## 408.74 `CONFIG_WEBSOCKET_DEDICATED_HEAP`

**提示（Prompt）**：为 WebSocket 使用专用堆（Dedicated heap）

**说明（Help）**

使用专用堆（Dedicated heap）进行 WebSocket 内部分配。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WEBSOCKET_CLIENT && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/websocket/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/websocket/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_WEBSOCKET_CLIENT`](P408_subsys_net_配置项参考_18.md#CONFIG_WEBSOCKET_CLIENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WEBSOCKET_DEDICATED_HEAP_SIZE"></a>

## 408.75 `CONFIG_WEBSOCKET_DEDICATED_HEAP_SIZE`

**提示（Prompt）**：WebSocket 专用堆大小（Dedicated heap size）

**说明（Help）**

WebSocket 专用堆（Dedicated heap）的大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WEBSOCKET_DEDICATED_HEAP && CONFIG_WEBSOCKET_CLIENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/net/lib/websocket/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/websocket/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 为 WebSocket 使用专用堆（Dedicated heap）

**配置项引用（Symbol References）**：[`CONFIG_WEBSOCKET_DEDICATED_HEAP`](P408_subsys_net_配置项参考_18.md#CONFIG_WEBSOCKET_DEDICATED_HEAP)、[`CONFIG_WEBSOCKET_CLIENT`](P408_subsys_net_配置项参考_18.md#CONFIG_WEBSOCKET_CLIENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WEBSOCKET_MAX_CONTEXTS"></a>

## 408.76 `CONFIG_WEBSOCKET_MAX_CONTEXTS`

**提示（Prompt）**：可分配的 WebSocket 最大数量

**说明（Help）**

系统中可创建的 WebSocket 数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WEBSOCKET_CLIENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_SHELL_WEBSOCKET_BACKEND_COUNT if CONFIG_SHELL_BACKEND_WEBSOCKET
1
```

**定义位置（Location）**：[`subsys/net/lib/websocket/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/websocket/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_WEBSOCKET_CLIENT`](P408_subsys_net_配置项参考_18.md#CONFIG_WEBSOCKET_CLIENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SHELL_WEBSOCKET_BACKEND_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_WEBSOCKET_BACKEND_COUNT)、[`CONFIG_SHELL_BACKEND_WEBSOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_WEBSOCKET)。

<a id="CONFIG_WIFI_CERTIFICATE_LIB"></a>

## 408.77 `CONFIG_WIFI_CERTIFICATE_LIB`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用后，处理企业模式（Enterprise mode）中的证书（Certificate）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE
CONFIG_ESP32_WIFI_ENTERPRISE
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE)、[`CONFIG_ESP32_WIFI_ENTERPRISE`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_ENTERPRISE)。

<a id="CONFIG_WIFI_CREDENTIALS"></a>

## 408.78 `CONFIG_WIFI_CREDENTIALS`

**提示（Prompt）**：Wi-Fi 凭据管理（credentials management）

**说明（Help）**

启用 Wi-Fi 凭据管理子系统（Credentials management subsystem）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_CREDENTIALS_BACKEND"></a>

## 408.79 `CONFIG_WIFI_CREDENTIALS_BACKEND`

**提示（Prompt）**：Wi-Fi 凭据后端（Credentials backend）

**说明（Help）**

选择使用 PSA 受保护存储（Protected Storage）还是 Zephyr 设置子系统（Settings subsystem）保存凭据（Credential）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_WIFI_CREDENTIALS_BACKEND_PSA if CONFIG_BUILD_WITH_TFM
CONFIG_WIFI_CREDENTIALS_BACKEND_SETTINGS
CONFIG_WIFI_CREDENTIALS_BACKEND_NONE if CONFIG_WIFI_CREDENTIALS_STATIC
```

**可选项（Choices）**

```text
CONFIG_WIFI_CREDENTIALS_BACKEND_SETTINGS
CONFIG_WIFI_CREDENTIALS_BACKEND_PSA
CONFIG_WIFI_CREDENTIALS_BACKEND_NONE
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIFI_CREDENTIALS_BACKEND_PSA`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_BACKEND_PSA)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_WIFI_CREDENTIALS_BACKEND_SETTINGS`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_BACKEND_SETTINGS)、[`CONFIG_WIFI_CREDENTIALS_BACKEND_NONE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_BACKEND_NONE)、[`CONFIG_WIFI_CREDENTIALS_STATIC`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC)。

<a id="CONFIG_WIFI_CREDENTIALS_BACKEND_NONE"></a>

## 408.80 `CONFIG_WIFI_CREDENTIALS_BACKEND_NONE`

**提示（Prompt）**：不存储凭据（No credentials storage）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_CREDENTIALS_STATIC && <choice CONFIG_WIFI_CREDENTIALS_BACKEND>
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management） → Wi-Fi 凭据后端（Credentials backend）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_STATIC`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC)、[`CONFIG_WIFI_CREDENTIALS_BACKEND`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_BACKEND)。

<a id="CONFIG_WIFI_CREDENTIALS_BACKEND_PSA"></a>

## 408.81 `CONFIG_WIFI_CREDENTIALS_BACKEND_PSA`

**提示（Prompt）**：PSA 受保护存储（Protected Storage）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM && <choice CONFIG_WIFI_CREDENTIALS_BACKEND>
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management） → Wi-Fi 凭据后端（Credentials backend）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_WIFI_CREDENTIALS_BACKEND`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_BACKEND)。

<a id="CONFIG_WIFI_CREDENTIALS_BACKEND_SETTINGS"></a>

## 408.82 `CONFIG_WIFI_CREDENTIALS_BACKEND_SETTINGS`

**提示（Prompt）**：Zephyr 设置子系统（Settings）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && !CONFIG_SETTINGS_NONE && <choice CONFIG_WIFI_CREDENTIALS_BACKEND>
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management） → Wi-Fi 凭据后端（Credentials backend）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_SETTINGS_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS_NONE)、[`CONFIG_WIFI_CREDENTIALS_BACKEND`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_BACKEND)。

<a id="CONFIG_WIFI_CREDENTIALS_CONNECT_STORED"></a>

## 408.83 `CONFIG_WIFI_CREDENTIALS_CONNECT_STORED`

**提示（Prompt）**：添加直接连接已存储网络的命令。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_CREDENTIALS_CONNECT_STORED_CONNECTION_TIMEOUT"></a>

## 408.84 `CONFIG_WIFI_CREDENTIALS_CONNECT_STORED_CONNECTION_TIMEOUT`

**提示（Prompt）**：连接超时（Connection timeout）

**说明（Help）**

回退到已存储服务集标识符（SSID）列表的下一个表项前，等待的时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_CREDENTIALS_CONNECT_STORED && CONFIG_WIFI_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management） → 添加直接连接已存储网络的命令。

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_CONNECT_STORED`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_CONNECT_STORED)、[`CONFIG_WIFI_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_CREDENTIALS_MAX_ENTRIES"></a>

## 408.85 `CONFIG_WIFI_CREDENTIALS_MAX_ENTRIES`

**提示（Prompt）**：支持的 Wi-Fi 凭据（Credential）数量

**说明（Help）**

决定可同时配置多少个不同的 Wi-Fi 网络。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_CREDENTIALS_RUNTIME_CERTIFICATES"></a>

## 408.86 `CONFIG_WIFI_CREDENTIALS_RUNTIME_CERTIFICATES`

**提示（Prompt）**：在运行时提供 Wi-Fi 企业级安全证书

**说明（Help）**

允许在运行时提供 Wi-Fi 企业安全证书（Enterprise security certificate），使用 TLS 凭据子系统（TLS credentials subsystem）存储和管理证书。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE && CONFIG_WIFI_CREDENTIALS_CONNECT_STORED && CONFIG_WIFI_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES
```

**主动选择（Selects）**

```text
CONFIG_TLS_CREDENTIALS
CONFIG_TLS_CREDENTIALS_SHELL
CONFIG_BASE64
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management） → 添加直接连接已存储网络的命令。

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_CREDENTIALS_CONNECT_STORED`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_CONNECT_STORED)、[`CONFIG_WIFI_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES)、[`CONFIG_TLS_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS)、[`CONFIG_TLS_CREDENTIALS_SHELL`](P408_subsys_net_配置项参考_18.md#CONFIG_TLS_CREDENTIALS_SHELL)、[`CONFIG_BASE64`](P197_lib_配置项参考_1.md#CONFIG_BASE64)。

<a id="CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH"></a>

## 408.87 `CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH`

**提示（Prompt）**：对等实体同时认证（SAE）密码的最大长度

**说明（Help）**

对等实体同时认证（Simultaneous Authentication of Equals，SAE）密码长度没有正式规定的上限；但例如 Linux 6.0 将其硬编码限制为 128 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_CREDENTIALS_SHELL"></a>

## 408.88 `CONFIG_WIFI_CREDENTIALS_SHELL`

**提示（Prompt）**：用于管理 Wi-Fi 凭据的命令行命令（Shell command）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && !CONFIG_WIFI_CREDENTIALS_BACKEND_NONE && CONFIG_WIFI_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SHELL_GETOPT
CONFIG_GETOPT_LONG
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_WIFI_CREDENTIALS_BACKEND_NONE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_BACKEND_NONE)、[`CONFIG_WIFI_CREDENTIALS`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SHELL_GETOPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_GETOPT)、[`CONFIG_GETOPT_LONG`](P197_lib_配置项参考_1.md#CONFIG_GETOPT_LONG)。

<a id="CONFIG_WIFI_CREDENTIALS_STATIC"></a>

## 408.89 `CONFIG_WIFI_CREDENTIALS_STATIC`

**提示（Prompt）**：静态 Wi-Fi 网络配置（Static network configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_CREDENTIALS_STATIC_PASSWORD"></a>

## 408.90 `CONFIG_WIFI_CREDENTIALS_STATIC_PASSWORD`

**提示（Prompt）**：静态配置 Wi-Fi 网络的密码（Password）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_CREDENTIALS_STATIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 静态 Wi-Fi 网络配置（Static network configuration）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_STATIC`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_CREDENTIALS_STATIC_SSID"></a>

## 408.91 `CONFIG_WIFI_CREDENTIALS_STATIC_SSID`

**提示（Prompt）**：静态配置 Wi-Fi 网络的服务集标识符（SSID）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_CREDENTIALS_STATIC && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 静态 Wi-Fi 网络配置（Static network configuration）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_STATIC`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_CREDENTIALS_STATIC_TYPE"></a>

## 408.92 `CONFIG_WIFI_CREDENTIALS_STATIC_TYPE`

**提示（Prompt）**：静态 Wi-Fi 网络的安全类型（Security type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_CREDENTIALS_STATIC && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_PSK
```

**可选项（Choices）**

```text
CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_OPEN
CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_OWE
CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_PSK
CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_PSK_SHA256
CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_SAE
CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_WPA_PSK
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 静态 Wi-Fi 网络配置（Static network configuration）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_STATIC`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_PSK`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_PSK)、[`CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_OPEN`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_OPEN)、[`CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_OWE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_OWE)、[`CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_PSK_SHA256`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_PSK_SHA256)、[`CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_SAE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_SAE)、[`CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_WPA_PSK`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_WPA_PSK)。

<a id="CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_OPEN"></a>

## 408.93 `CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_OPEN`

**提示（Prompt）**：开放网络（OPEN）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_CREDENTIALS_STATIC_TYPE>
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 静态 Wi-Fi 网络配置（Static network configuration） → 静态 Wi-Fi 网络的安全类型（Security type）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_STATIC_TYPE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC_TYPE)。

<a id="CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_OWE"></a>

## 408.94 `CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_OWE`

**提示（Prompt）**：机会性无线加密（Opportunistic Wireless Encryption，OWE）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_CREDENTIALS_STATIC_TYPE>
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 静态 Wi-Fi 网络配置（Static network configuration） → 静态 Wi-Fi 网络的安全类型（Security type）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_STATIC_TYPE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC_TYPE)。

<a id="CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_PSK"></a>

## 408.95 `CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_PSK`

**提示（Prompt）**：WPA2 预共享密钥（WPA2-PSK）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_CREDENTIALS_STATIC_TYPE>
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 静态 Wi-Fi 网络配置（Static network configuration） → 静态 Wi-Fi 网络的安全类型（Security type）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_STATIC_TYPE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC_TYPE)。

<a id="CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_PSK_SHA256"></a>

## 408.96 `CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_PSK_SHA256`

**提示（Prompt）**：WPA2 预共享密钥与 SHA-256（WPA2-PSK-SHA256）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_CREDENTIALS_STATIC_TYPE>
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 静态 Wi-Fi 网络配置（Static network configuration） → 静态 Wi-Fi 网络的安全类型（Security type）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_STATIC_TYPE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC_TYPE)。

<a id="CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_SAE"></a>

## 408.97 `CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_SAE`

**提示（Prompt）**：对等实体同时认证（Simultaneous Authentication of Equals，SAE）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_CREDENTIALS_STATIC_TYPE>
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 静态 Wi-Fi 网络配置（Static network configuration） → 静态 Wi-Fi 网络的安全类型（Security type）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_STATIC_TYPE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC_TYPE)。

<a id="CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_WPA_PSK"></a>

## 408.98 `CONFIG_WIFI_CREDENTIALS_STATIC_TYPE_WPA_PSK`

**提示（Prompt）**：WPA 预共享密钥（WPA-PSK）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_CREDENTIALS_STATIC_TYPE>
```

**定义位置（Location）**：[`subsys/net/lib/wifi_credentials/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 静态 Wi-Fi 网络配置（Static network configuration） → 静态 Wi-Fi 网络的安全类型（Security type）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_STATIC_TYPE`](P408_subsys_net_配置项参考_18.md#CONFIG_WIFI_CREDENTIALS_STATIC_TYPE)。

<a id="CONFIG_WIFI_ENT_IDENTITY_MAX_USERS"></a>

## 408.99 `CONFIG_WIFI_ENT_IDENTITY_MAX_USERS`

**提示（Prompt）**：允许连接的身份用户（Identity user）最大数量

**说明（Help）**

定义允许连接的身份用户（Identity user）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/net/l2/wifi/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → Wi-Fi 管理支持（Management support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_WIFI_LOG_LEVEL_CHOICE"></a>

## 408.100 `CONFIG_WIFI_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Wi-Fi 驱动日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_WIFI_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_WIFI_LOG_LEVEL_OFF
CONFIG_WIFI_LOG_LEVEL_ERR
CONFIG_WIFI_LOG_LEVEL_WRN
CONFIG_WIFI_LOG_LEVEL_INF
CONFIG_WIFI_LOG_LEVEL_DBG
CONFIG_WIFI_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_LOG_LEVEL_DEFAULT`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_LOG_LEVEL_DEFAULT)、[`CONFIG_WIFI_LOG_LEVEL_OFF`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_LOG_LEVEL_OFF)、[`CONFIG_WIFI_LOG_LEVEL_ERR`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_LOG_LEVEL_ERR)、[`CONFIG_WIFI_LOG_LEVEL_WRN`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_LOG_LEVEL_WRN)、[`CONFIG_WIFI_LOG_LEVEL_INF`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_LOG_LEVEL_INF)、[`CONFIG_WIFI_LOG_LEVEL_DBG`](P409_subsys_net_配置项参考_19.md#CONFIG_WIFI_LOG_LEVEL_DBG)。

<!-- kconfig-navigation -->

[上一章](P407_subsys_net_配置项参考_17.md) · [返回大纲](大纲.md) · [下一章](P409_subsys_net_配置项参考_19.md)
