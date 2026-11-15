---
id: learning.zephyr-docs.kconfig-reference.page-405
title: "`subsys/net`配置项参考（15/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第405章\_`subsys/net`配置项参考（15/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_TCP_KEEPCNT_DEFAULT"></a>

## 405.1 `CONFIG_NET_TCP_KEEPCNT_DEFAULT`

**提示（Prompt）**：`TCP_KEEPCNT` 默认值

**说明（Help）**

TCP 在断开连接前应发送的保活探测（Keepalive probe）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP_KEEPALIVE && CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
9
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:223`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L223)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP） → TCP 保活（Keep-alive）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP_KEEPALIVE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP_KEEPALIVE)、[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_KEEPIDLE_DEFAULT"></a>

## 405.2 `CONFIG_NET_TCP_KEEPIDLE_DEFAULT`

**提示（Prompt）**：`TCP_KEEPIDLE` 默认值

**说明（Help）**

如果此套接字设置了 `SO_KEEPALIVE`，则连接空闲达到此时长后，TCP 开始发送保活探测（Keepalive probe），单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP_KEEPALIVE && CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
7200
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP） → TCP 保活（Keep-alive）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP_KEEPALIVE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP_KEEPALIVE)、[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_KEEPINTVL_DEFAULT"></a>

## 405.3 `CONFIG_NET_TCP_KEEPINTVL_DEFAULT`

**提示（Prompt）**：`TCP_KEEPINTVL` 默认值

**说明（Help）**

各次保活探测（Keepalive probe）之间的时间间隔，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP_KEEPALIVE && CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
75
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP） → TCP 保活（Keep-alive）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP_KEEPALIVE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP_KEEPALIVE)、[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_LOG_LEVEL_CHOICE"></a>

## 405.4 `CONFIG_NET_TCP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：TCP 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_TCP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_TCP_LOG_LEVEL_OFF
CONFIG_NET_TCP_LOG_LEVEL_ERR
CONFIG_NET_TCP_LOG_LEVEL_WRN
CONFIG_NET_TCP_LOG_LEVEL_INF
CONFIG_NET_TCP_LOG_LEVEL_DBG
CONFIG_NET_TCP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_TCP_LOG_LEVEL_DEFAULT`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_TCP_LOG_LEVEL_OFF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_LOG_LEVEL_OFF)、[`CONFIG_NET_TCP_LOG_LEVEL_ERR`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_LOG_LEVEL_ERR)、[`CONFIG_NET_TCP_LOG_LEVEL_WRN`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_LOG_LEVEL_WRN)、[`CONFIG_NET_TCP_LOG_LEVEL_INF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_LOG_LEVEL_INF)、[`CONFIG_NET_TCP_LOG_LEVEL_DBG`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_TCP_LOG_LEVEL_DBG"></a>

## 405.5 `CONFIG_NET_TCP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP） → TCP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TCP_LOG_LEVEL_DEFAULT"></a>

## 405.6 `CONFIG_NET_TCP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP） → TCP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TCP_LOG_LEVEL_ERR"></a>

## 405.7 `CONFIG_NET_TCP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP） → TCP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TCP_LOG_LEVEL_INF"></a>

## 405.8 `CONFIG_NET_TCP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP） → TCP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TCP_LOG_LEVEL_OFF"></a>

## 405.9 `CONFIG_NET_TCP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP） → TCP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TCP_LOG_LEVEL_WRN"></a>

## 405.10 `CONFIG_NET_TCP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP） → TCP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TCP_MAX_RECV_WINDOW_SIZE"></a>

## 405.11 `CONFIG_NET_TCP_MAX_RECV_WINDOW_SIZE`

**提示（Prompt）**：使用的最大接收窗口（Receive window）大小

**说明（Help）**

定义 TCP 接收窗口（Receive window）的最大大小。增大此值可提高连接吞吐量，但系统需要提供更多接收缓冲区才能高效运行。默认值 0 表示由 TCP 协议栈根据系统配置的网络缓冲区数量自动选择。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_MAX_SEND_WINDOW_SIZE"></a>

## 405.12 `CONFIG_NET_TCP_MAX_SEND_WINDOW_SIZE`

**提示（Prompt）**：使用的最大发送窗口（Sending window）大小

**说明（Help）**

影响 TCP 如何选择最大发送窗口（Sending window）大小。默认值 0 表示由 TCP 协议栈根据系统配置的网络缓冲区数量自动选择。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_PKT_ALLOC_TIMEOUT"></a>

## 405.13 `CONFIG_NET_TCP_PKT_ALLOC_TIMEOUT`

**提示（Prompt）**：等待分配 TCP 数据包的时长（毫秒）

**说明（Help）**

TCP 网络协议栈从缓冲区分配数据包，具体情况下分配可能需要一定时间。此值指定在返回内部错误并重试前，协议栈应等待数据包分配完成的时长。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[10, 1000]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_PRESERVE_CONTEXT_STATE_ON_IFACE_DOWN"></a>

## 405.14 `CONFIG_NET_TCP_PRESERVE_CONTEXT_STATE_ON_IFACE_DOWN`

**提示（Prompt）**：接口关闭（Down）时保留 TCP 连接上下文（Context）

**说明（Help）**

默认情况下，网络接口关闭时，Zephyr 会关闭关联的全部 TCP 上下文（Context），导致相关网络套接字报告错误，让应用能够重新打开套接字，例如应对网络或 IP 地址改变。但已有反馈指出，在某些情况下不希望有此行为。启用本选项后，网络接口关闭时，TCP 协议栈不会关闭任何 TCP 上下文；应用必须自行监测 IP 地址或接口状态变化，并在需要时重新启动 TCP 套接字。只有能够保证应用正确处理这些情况时，才应启用本选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:255`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L255)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_RANDOMIZED_RTO"></a>

## 405.15 `CONFIG_NET_TCP_RANDOMIZED_RTO`

**提示（Prompt）**：使用随机化的重传时间（Randomized retransmission time）

**说明（Help）**

两个相似的协议栈可能因数据包碰撞（Collision）进入重传循环。如果重传超时相同，两者会同时重试，导致再次碰撞。引入随机重试超时后，可以降低第二次碰撞的概率，并随着重传次数增多进一步降低持续碰撞的概率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_RECV_QUEUE_TIMEOUT"></a>

## 405.16 `CONFIG_NET_TCP_RECV_QUEUE_TIMEOUT`

**提示（Prompt）**：收到的数据保持排队的时长（毫秒）

**说明（Help）**

收到乱序 TCP 数据（Out-of-order data）时，将其入队。此值指定数据未能交给应用时，保留多久再丢弃，单位为毫秒。设为 0 表示禁用接收排队。目前只对序号连续的数据排队，即队列中不能有空缺。例如，正在等待序号（SEQ）2 时，依次收到 5、4、3、6，则将报文段 3、4、5、6 按此顺序排队，收到 2 后再交给应用。但若收到的是 5、4、3、7，则丢弃 7，因为缺少 6，列表不连续。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2000
```

**取值范围（Ranges）**

```text
[0, 10000]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_REJECT_CONN_WITH_RST"></a>

## 405.17 `CONFIG_NET_TCP_REJECT_CONN_WITH_RST`

**提示（Prompt）**：使用 RST 拒绝对未绑定 TCP 端口的连接尝试

**说明（Help）**

启用后，TCP 协议栈会对未绑定端口上的连接尝试回复 TCP 复位（RST）数据包，拒绝连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:240`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L240)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_RETRY_COUNT"></a>

## 405.18 `CONFIG_NET_TCP_RETRY_COUNT`

**提示（Prompt）**：TCP 报文段（Segment）的最大重传次数

**说明（Help）**

可用以下原始公式确定报文段在等待重传时最多缓冲多久，单位为毫秒：

```text
n=NET_TCP_RETRY_COUNT
Sum((1<<n) * NET_TCP_INIT_RETRANSMISSION_TIMEOUT)
n=0
```

上方和下方两行分别标记求和的上限与下限。默认值为 9 时，IP 协议栈最多尝试重传 1 分 42 秒，尽量接近 RFC 1122 推荐的最小值 1 分 40 秒。重传计数仅分配了 5 位，因此允许范围为 0～31，但强烈建议不要小于 9。如果发生重传超时，则使用 `-ETIMEDOUT` 错误码调用接收回调（Receive callback），并释放对上下文（Context）的引用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
9
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_SACK"></a>

## 405.19 `CONFIG_NET_TCP_SACK`

**提示（Prompt）**：对收到的数据进行选择确认（Selective Acknowledgment，SACK）

**说明（Help）**

在握手中提供 SACK permitted 选项（RFC 2018），并在对端同意后，通过 SACK 块报告接收队列中保存的乱序数据，使发送方只重传缺失部分。目前仅实现接收端功能：重传时不使用对端发送的 SACK 块。即使排队数据已在 SACK 块中报告，经过 `NET_TCP_RECV_QUEUE_TIMEOUT` 毫秒后仍会被丢弃。RFC 2018 第 8 节允许这种行为，发送方必须能应对；调试与本协议栈之间的停滞问题时应留意这一点。禁用本选项可停止提供 SACK，例如用于排查互操作问题（Interoperability problem）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP_RECV_QUEUE_TIMEOUT > 0 && CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP_RECV_QUEUE_TIMEOUT`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TCP_RECV_QUEUE_TIMEOUT)、[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_TIME_WAIT_DELAY"></a>

## 405.20 `CONFIG_NET_TCP_TIME_WAIT_DELAY`

**提示（Prompt）**：TIME_WAIT 状态的等待时间（毫秒）

**说明（Help）**

前一连接的延迟数据包可能以较低概率误投递给复用相同本地和远程端口的新连接。为避免此问题，RFC 793（TCP）建议旧连接关闭后继续处于特殊的 `TIME_WAIT` 状态，持续时间为 `2*MSL`，其中 MSL 为最大报文段生存期（Maximum Segment Lifetime）。RFC 建议 MSL 为 2 分钟，同时指出这是工程选择，可根据实践经验调整。对资源较少的系统，较大的 MSL 可能很快耗尽资源，并引发相关拒绝服务（DoS）攻击。另一方面，现代 TCP 协议栈采用随机且不重复的端口号与初始序列号，已大幅缓解数据包误投递问题。因此，Zephyr 默认采用小得多的 1500 毫秒。设为 0 可完全禁用 `TIME_WAIT` 状态。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_WORKER_PRIO"></a>

## 405.21 `CONFIG_NET_TCP_WORKER_PRIO`

**提示（Prompt）**：TCP 工作队列（Work queue）的优先级

**说明（Help）**

设置 TCP 工作队列（Work queue）的优先级，该队列处理 TCP 协议栈中的全部发送与维护工作。0 表示最高优先级；当 `CONFIG_NET_TC_THREAD_COOPERATIVE = y` 时，最低优先级为 `CONFIG_NUM_COOP_PRIORITIES-1`，否则为 `CONFIG_NUM_PREEMPT_PRIORITIES-1`。应确保其优先级低于下层发送线程（TX thread），避免 TCP 协议栈在将执行权交给下层之前消耗全部 `net_buf`，造成很高的缓冲区耗尽风险。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_WORKQ_STACK_SIZE"></a>

## 405.22 `CONFIG_NET_TCP_WORKQ_STACK_SIZE`

**提示（Prompt）**：TCP 工作队列线程栈大小（Work queue thread stack size）

**说明（Help）**

设置 TCP 工作队列线程栈大小（Thread stack size），单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1200 if CONFIG_X86
1024
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_NET_TC_LOG_LEVEL_CHOICE"></a>

## 405.23 `CONFIG_NET_TC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：网络流量类别（Traffic class）代码日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_TC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_TC_LOG_LEVEL_OFF
CONFIG_NET_TC_LOG_LEVEL_ERR
CONFIG_NET_TC_LOG_LEVEL_WRN
CONFIG_NET_TC_LOG_LEVEL_INF
CONFIG_NET_TC_LOG_LEVEL_DBG
CONFIG_NET_TC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_TC_LOG_LEVEL_DEFAULT`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_TC_LOG_LEVEL_OFF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_LOG_LEVEL_OFF)、[`CONFIG_NET_TC_LOG_LEVEL_ERR`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_LOG_LEVEL_ERR)、[`CONFIG_NET_TC_LOG_LEVEL_WRN`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_LOG_LEVEL_WRN)、[`CONFIG_NET_TC_LOG_LEVEL_INF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_LOG_LEVEL_INF)、[`CONFIG_NET_TC_LOG_LEVEL_DBG`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_TC_LOG_LEVEL_DBG"></a>

## 405.24 `CONFIG_NET_TC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络流量类别（Traffic class）代码日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TC_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TC_LOG_LEVEL_DEFAULT"></a>

## 405.25 `CONFIG_NET_TC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络流量类别（Traffic class）代码日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TC_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TC_LOG_LEVEL_ERR"></a>

## 405.26 `CONFIG_NET_TC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络流量类别（Traffic class）代码日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TC_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TC_LOG_LEVEL_INF"></a>

## 405.27 `CONFIG_NET_TC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络流量类别（Traffic class）代码日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TC_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TC_LOG_LEVEL_OFF"></a>

## 405.28 `CONFIG_NET_TC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络流量类别（Traffic class）代码日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TC_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TC_LOG_LEVEL_WRN"></a>

## 405.29 `CONFIG_NET_TC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络流量类别（Traffic class）代码日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TC_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TC_MAPPING_SR_CLASS_A_AND_B"></a>

## 405.30 `CONFIG_NET_TC_MAPPING_SR_CLASS_A_AND_B`

**提示（Prompt）**：流预留（SR）A 类与 B 类映射

**说明（Help）**

这是对同时支持流预留（Stream Reservation，SR）A 类和 B 类的系统所推荐的优先级到流量类别（Traffic class）的映射。详见 IEEE 802.1Q 第 34.5 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TC_TX_COUNT >= 2 && CONFIG_NET_TC_RX_COUNT >= 2 && <choice>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:395`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L395)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 优先级到流量类别（Traffic class）的映射

**配置项引用（Symbol References）**：[`CONFIG_NET_TC_TX_COUNT`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_TX_COUNT)、[`CONFIG_NET_TC_RX_COUNT`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_RX_COUNT)。

<a id="CONFIG_NET_TC_MAPPING_SR_CLASS_B_ONLY"></a>

## 405.31 `CONFIG_NET_TC_MAPPING_SR_CLASS_B_ONLY`

**提示（Prompt）**：仅支持流预留（SR）B 类的映射

**说明（Help）**

这是对仅支持流预留（Stream Reservation，SR）B 类的系统所推荐的优先级到流量类别（Traffic class）的映射。详见 IEEE 802.1Q 第 34.5 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TC_TX_COUNT >= 2 && CONFIG_NET_TC_RX_COUNT >= 2 && <choice>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:404`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L404)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 优先级到流量类别（Traffic class）的映射

**配置项引用（Symbol References）**：[`CONFIG_NET_TC_TX_COUNT`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_TX_COUNT)、[`CONFIG_NET_TC_RX_COUNT`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_RX_COUNT)。

<a id="CONFIG_NET_TC_MAPPING_STRICT"></a>

## 405.32 `CONFIG_NET_TC_MAPPING_STRICT`

**提示（Prompt）**：严格优先级映射（Strict priority mapping）

**说明（Help）**

这是推荐的默认优先级到流量类别（Traffic class）映射，适用于不支持基于信用的整形器（Credit-based shaper）发送选择算法的实现。详见 IEEE 802.1Q 第 8.6.6 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:387`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L387)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 优先级到流量类别（Traffic class）的映射

<a id="CONFIG_NET_TC_RX_COUNT"></a>

## 405.33 `CONFIG_NET_TC_RX_COUNT`

**提示（Prompt）**：每个网络设备的接收流量类别（RX traffic class）数量

**说明（Help）**

定义系统接收网络数据包时应有多少个接收流量类别（RX traffic class），也就是队列。数据包优先级可映射到流量类别，使高优先级数据包先处理。每个队列由独立线程处理，需要 RAM 存放线程栈；只有确实需要时才应将该值增大到 1 以上。默认值 1 表示平等处理全部网络流量。按原文，此实现中较高的流量类别值对应较低的线程优先级。设为 0 时，全部网络流量从驱动直接交给应用线程，不经过中间接收队列。不过，设备驱动与应用之间始终有一个接收套接字队列（Receive socket queue）。禁用接收线程意味着通常在中断（IRQ）上下文运行的网络驱动，会一路处理数据包直到交给应用；接收处理耗时较长时，可能丢失其他到达的数据包。注意，启用用户空间（USERSPACE）支持时，目前必须至少启用一个接收线程。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, CONFIG_NET_TC_NUM_PRIORITIES] if CONFIG_NET_TC_NUM_PRIORITIES <= 8 && CONFIG_USERSPACE
[0, CONFIG_NET_TC_NUM_PRIORITIES] if CONFIG_NET_TC_NUM_PRIORITIES <= 8
[1, 8] if CONFIG_USERSPACE
[0, 8]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_TC_NUM_PRIORITIES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TC_NUM_PRIORITIES)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_TC_NUM_PRIORITIES`。

<a id="CONFIG_NET_TC_RX_SKIP_FOR_HIGH_PRIO"></a>

## 405.34 `CONFIG_NET_TC_RX_SKIP_FOR_HIGH_PRIO`

**提示（Prompt）**：将高优先级数据包直接交给应用（Application）

**说明（Help）**

启用后，高优先级，即优先级大于或等于 `NET_PRIORITY_CA` 的 `net_pkt`，直接交给应用，跳过流量类别队列（Traffic class queue）。这意味着高优先级网络流量从驱动直接交给应用线程，不经过中间接收队列。如果网络设备驱动运行在中断（IRQ）上下文，它将一路处理数据包直到交给应用；接收处理耗时较长时，可能丢失其他到达的数据包。此功能目前默认禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:300`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L300)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TC_RX_THREAD_BASE_PRIO"></a>

## 405.35 `CONFIG_NET_TC_RX_THREAD_BASE_PRIO`

**提示（Prompt）**：接收流量类别线程的基准优先级（Base thread priority）

**说明（Help）**

接收流量类别（RX traffic class）线程的优先级以此值为起点增减。如果 `NET_TC_RX_COUNT` 为 1，此值就是该接收流量类别线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TC_THREAD_PRIO_CUSTOM && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:370`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L370)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 自定义流量类别线程优先级（Traffic class thread priority）

**配置项引用（Symbol References）**：[`CONFIG_NET_TC_THREAD_PRIO_CUSTOM`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_THREAD_PRIO_CUSTOM)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TC_RX_THREAD_PRIO_SPREAD"></a>

## 405.36 `CONFIG_NET_TC_RX_THREAD_PRIO_SPREAD`

**提示（Prompt）**：接收流量类别线程的优先级间隔（Priority spread）

**说明（Help）**

接收流量类别（RX traffic class）线程的优先级按此步长增减，各线程优先级之间相差这么多个级别。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TC_THREAD_PRIO_CUSTOM && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:353`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L353)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 自定义流量类别线程优先级（Traffic class thread priority）

**配置项引用（Symbol References）**：[`CONFIG_NET_TC_THREAD_PRIO_CUSTOM`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_THREAD_PRIO_CUSTOM)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TC_THREAD_COOPERATIVE"></a>

## 405.37 `CONFIG_NET_TC_THREAD_COOPERATIVE`

**提示（Prompt）**：使用协作式发送与接收线程（Co-operative TX/RX threads）

**说明（Help）**

采用协作式线程（Co-operative thread）时，该线程不能被抢占。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COOP_ENABLED && <choice CONFIG_NET_TC_THREAD_TYPE>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:319`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L319)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络接收与发送线程（RX/TX threads）的工作方式

**配置项引用（Symbol References）**：[`CONFIG_COOP_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COOP_ENABLED)、[`CONFIG_NET_TC_THREAD_TYPE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_THREAD_TYPE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_COOP_ENABLED`。

<a id="CONFIG_NET_TC_THREAD_PREEMPTIVE"></a>

## 405.38 `CONFIG_NET_TC_THREAD_PREEMPTIVE`

**提示（Prompt）**：使用抢占式发送与接收线程（Pre-emptive TX/RX threads）

**说明（Help）**

采用抢占式线程（Preemptive Thread）时，该线程可被抢占（Preempted）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PREEMPT_ENABLED && <choice CONFIG_NET_TC_THREAD_TYPE>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:325`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L325)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络接收与发送线程（RX/TX threads）的工作方式

**配置项引用（Symbol References）**：[`CONFIG_PREEMPT_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PREEMPT_ENABLED)、[`CONFIG_NET_TC_THREAD_TYPE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_THREAD_TYPE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PREEMPT_ENABLED`。

<a id="CONFIG_NET_TC_THREAD_PRIO_CUSTOM"></a>

## 405.39 `CONFIG_NET_TC_THREAD_PRIO_CUSTOM`

**提示（Prompt）**：自定义流量类别线程优先级（Traffic class thread priority）

**说明（Help）**

分别自定义各网络线程的优先级（Thread priority）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:338`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L338)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TC_THREAD_TYPE"></a>

## 405.40 `CONFIG_NET_TC_THREAD_TYPE`

**提示（Prompt）**：网络接收与发送线程（RX/TX threads）的工作方式

**说明（Help）**

请选择接收与发送线程（RX/TX threads）采用抢占式（Pre-emptive）还是协作式（Co-operative）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**可选项（Choices）**

```text
CONFIG_NET_TC_THREAD_COOPERATIVE
CONFIG_NET_TC_THREAD_PREEMPTIVE
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:313`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L313)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_TC_THREAD_COOPERATIVE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_THREAD_COOPERATIVE)、[`CONFIG_NET_TC_THREAD_PREEMPTIVE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_THREAD_PREEMPTIVE)。

<a id="CONFIG_NET_TC_TX_COUNT"></a>

## 405.41 `CONFIG_NET_TC_TX_COUNT`

**提示（Prompt）**：每个网络设备的发送流量类别（TX traffic class）数量

**说明（Help）**

定义系统发送网络数据包时应有多少个发送流量类别（TX traffic class），也就是队列。数据包优先级可映射到流量类别，使高优先级数据包先处理。每个队列由独立线程处理，需要 RAM 存放线程栈；只有确实需要时才应将该值增大到 1 以上。默认值 1 表示平等处理全部网络流量。按原文，此实现中较高的流量类别值对应较低的线程优先级。设为 0 时，全部网络流量直接交给驱动，不经过任何队列。注意，启用用户空间（USERSPACE）支持时，目前必须至少启用一个发送线程。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1 if CONFIG_USERSPACE || CONFIG_USB_DEVICE_NETWORK || CONFIG_USBD_CDC_ECM_CLASS || CONFIG_USBD_CDC_NCM_CLASS || CONFIG_NET_SHELL_REQUIRE_TX_THREAD
0
```

**取值范围（Ranges）**

```text
[1, CONFIG_NET_TC_NUM_PRIORITIES] if CONFIG_NET_TC_NUM_PRIORITIES <= 8 && (CONFIG_USERSPACE || CONFIG_NET_SHELL_REQUIRE_TX_THREAD)
[0, CONFIG_NET_TC_NUM_PRIORITIES] if CONFIG_NET_TC_NUM_PRIORITIES <= 8
[1, 8] if CONFIG_USERSPACE || CONFIG_NET_SHELL_REQUIRE_TX_THREAD
[0, 8]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_USB_DEVICE_NETWORK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_NETWORK)、[`CONFIG_USBD_CDC_ECM_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_CDC_ECM_CLASS)、[`CONFIG_USBD_CDC_NCM_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_CDC_NCM_CLASS)、[`CONFIG_NET_SHELL_REQUIRE_TX_THREAD`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_REQUIRE_TX_THREAD)、[`CONFIG_NET_TC_NUM_PRIORITIES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TC_NUM_PRIORITIES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USB_DEVICE_NETWORK`、`CONFIG_NET_TC_NUM_PRIORITIES`。

<a id="CONFIG_NET_TC_TX_SKIP_FOR_HIGH_PRIO"></a>

## 405.42 `CONFIG_NET_TC_TX_SKIP_FOR_HIGH_PRIO`

**提示（Prompt）**：将高优先级数据包直接交给网络驱动（Network driver）

**说明（Help）**

启用后，高优先级，即优先级大于或等于 `NET_PRIORITY_CA` 的 `net_pkt`，直接交给网络驱动，跳过流量类别队列（Traffic class queue）。此功能目前默认禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:293`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L293)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TC_TX_THREAD_BASE_PRIO"></a>

## 405.43 `CONFIG_NET_TC_TX_THREAD_BASE_PRIO`

**提示（Prompt）**：发送流量类别线程的基准优先级（Base thread priority）

**说明（Help）**

发送流量类别（TX traffic class）线程的优先级以此值为起点增减。如果 `NET_TC_TX_COUNT` 为 1，此值就是该发送流量类别线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TC_THREAD_PRIO_CUSTOM && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:361`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L361)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 自定义流量类别线程优先级（Traffic class thread priority）

**配置项引用（Symbol References）**：[`CONFIG_NET_TC_THREAD_PRIO_CUSTOM`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_THREAD_PRIO_CUSTOM)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TC_TX_THREAD_PRIO_SPREAD"></a>

## 405.44 `CONFIG_NET_TC_TX_THREAD_PRIO_SPREAD`

**提示（Prompt）**：发送流量类别线程的优先级间隔（Priority spread）

**说明（Help）**

发送流量类别（TX traffic class）线程的优先级按此步长增减，各线程优先级之间相差这么多个级别。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TC_THREAD_PRIO_CUSTOM && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:345`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L345)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 自定义流量类别线程优先级（Traffic class thread priority）

**配置项引用（Symbol References）**：[`CONFIG_NET_TC_THREAD_PRIO_CUSTOM`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TC_THREAD_PRIO_CUSTOM)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TEST"></a>

## 405.45 `CONFIG_NET_TEST`

**提示（Prompt）**：网络测试（Network Testing）

**说明（Help）**

用于无需网络设备的自包含网络测试（Self-contained networking test）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:726`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L726)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TRICKLE"></a>

## 405.46 `CONFIG_NET_TRICKLE`

**提示（Prompt）**：Trickle 算法库（Library）

**说明（Help）**

通常会在需要时自动启用，不确定是否需要时选择 `n`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/trickle/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/trickle/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE"></a>

## 405.47 `CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Trickle 算法日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_TRICKLE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_TRICKLE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_TRICKLE_LOG_LEVEL_OFF
CONFIG_NET_TRICKLE_LOG_LEVEL_ERR
CONFIG_NET_TRICKLE_LOG_LEVEL_WRN
CONFIG_NET_TRICKLE_LOG_LEVEL_INF
CONFIG_NET_TRICKLE_LOG_LEVEL_DBG
CONFIG_NET_TRICKLE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Trickle 算法库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_TRICKLE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_TRICKLE_LOG_LEVEL_DEFAULT`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_TRICKLE_LOG_LEVEL_OFF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE_LOG_LEVEL_OFF)、[`CONFIG_NET_TRICKLE_LOG_LEVEL_ERR`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE_LOG_LEVEL_ERR)、[`CONFIG_NET_TRICKLE_LOG_LEVEL_WRN`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE_LOG_LEVEL_WRN)、[`CONFIG_NET_TRICKLE_LOG_LEVEL_INF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE_LOG_LEVEL_INF)、[`CONFIG_NET_TRICKLE_LOG_LEVEL_DBG`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_TRICKLE_LOG_LEVEL_DBG"></a>

## 405.48 `CONFIG_NET_TRICKLE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Trickle 算法库（Library） → Trickle 算法日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TRICKLE_LOG_LEVEL_DEFAULT"></a>

## 405.49 `CONFIG_NET_TRICKLE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Trickle 算法库（Library） → Trickle 算法日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TRICKLE_LOG_LEVEL_ERR"></a>

## 405.50 `CONFIG_NET_TRICKLE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Trickle 算法库（Library） → Trickle 算法日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TRICKLE_LOG_LEVEL_INF"></a>

## 405.51 `CONFIG_NET_TRICKLE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Trickle 算法库（Library） → Trickle 算法日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TRICKLE_LOG_LEVEL_OFF"></a>

## 405.52 `CONFIG_NET_TRICKLE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Trickle 算法库（Library） → Trickle 算法日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TRICKLE_LOG_LEVEL_WRN"></a>

## 405.53 `CONFIG_NET_TRICKLE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Trickle 算法库（Library） → Trickle 算法日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TRICKLE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_TX_DEFAULT_PRIORITY"></a>

## 405.54 `CONFIG_NET_TX_DEFAULT_PRIORITY`

**提示（Prompt）**：未设置时采用的网络发送数据包默认优先级（TX packet priority）

**说明（Help）**

指定用户未明确设置优先级时网络数据包使用的默认优先级。0 为最低，7 为最高。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:414`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L414)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TX_STACK_SIZE"></a>

## 405.55 `CONFIG_NET_TX_STACK_SIZE`

**提示（Prompt）**：发送线程栈大小（TX Thread Stack Size）

**说明（Help）**

设置发送线程（TX thread）的栈大小，单位为字节。发送线程等待应用提供数据。每个网络接口会启动一个发送线程，发送交给该接口的网络数据包。此值是基准值，实际发送线程栈大小可能因启用的功能而更大。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1200
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stack:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stack#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 栈使用情况（Stack usage）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_UDP"></a>

## 405.56 `CONFIG_NET_UDP`

**提示（Prompt）**：用户数据报协议（UDP）

**说明（Help）**

该值取决于网络需求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_NETMIDI2_HOST
```

**被弱选择（Implied by）**

```text
CONFIG_NET_L2_OPENTHREAD
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:454`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L454)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_IP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NETMIDI2_HOST`](P395_subsys_net_配置项参考_5.md#CONFIG_NETMIDI2_HOST)、[`CONFIG_NET_L2_OPENTHREAD`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_OPENTHREAD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_IP`。

<a id="CONFIG_NET_UDP_CHECKSUM"></a>

## 405.57 `CONFIG_NET_UDP_CHECKSUM`

**提示（Prompt）**：检查 UDP 校验和（Checksum）

**说明（Help）**

让 UDP 处理程序检查 UDP 校验和（Checksum）；校验和无效时，丢弃数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:461`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L461)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_UDP_LOG_LEVEL_CHOICE"></a>

## 405.58 `CONFIG_NET_UDP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：UDP 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_UDP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_UDP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_UDP_LOG_LEVEL_OFF
CONFIG_NET_UDP_LOG_LEVEL_ERR
CONFIG_NET_UDP_LOG_LEVEL_WRN
CONFIG_NET_UDP_LOG_LEVEL_INF
CONFIG_NET_UDP_LOG_LEVEL_DBG
CONFIG_NET_UDP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_UDP`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_UDP_LOG_LEVEL_DEFAULT`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_UDP_LOG_LEVEL_OFF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_LOG_LEVEL_OFF)、[`CONFIG_NET_UDP_LOG_LEVEL_ERR`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_LOG_LEVEL_ERR)、[`CONFIG_NET_UDP_LOG_LEVEL_WRN`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_LOG_LEVEL_WRN)、[`CONFIG_NET_UDP_LOG_LEVEL_INF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_LOG_LEVEL_INF)、[`CONFIG_NET_UDP_LOG_LEVEL_DBG`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_UDP_LOG_LEVEL_DBG"></a>

## 405.59 `CONFIG_NET_UDP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_UDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP） → UDP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_UDP_LOG_LEVEL_DEFAULT"></a>

## 405.60 `CONFIG_NET_UDP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_UDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP） → UDP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_UDP_LOG_LEVEL_ERR"></a>

## 405.61 `CONFIG_NET_UDP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_UDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP） → UDP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_UDP_LOG_LEVEL_INF"></a>

## 405.62 `CONFIG_NET_UDP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_UDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP） → UDP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_UDP_LOG_LEVEL_OFF"></a>

## 405.63 `CONFIG_NET_UDP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_UDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP） → UDP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_UDP_LOG_LEVEL_WRN"></a>

## 405.64 `CONFIG_NET_UDP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_UDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP） → UDP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_UDP_MISSING_CHECKSUM"></a>

## 405.65 `CONFIG_NET_UDP_MISSING_CHECKSUM`

**提示（Prompt）**：接受缺少校验和（Checksum）的数据包，仅限 IPv4

**说明（Help）**

RFC 768 允许省略校验和（Checksum），例如用于调试。但此功能仅对 IPv4 的接收方向有效，因为 Zephyr 在发送路径中始终计算 UDP 校验和。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && CONFIG_NET_IPV4 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:469`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L469)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_UDP_OPTIONS"></a>

## 405.66 `CONFIG_NET_UDP_OPTIONS`

**提示（Prompt）**：UDP 传输选项（Transport options，RFC 9868）［实验性，Experimental］

**说明（Help）**

启用 RFC 9868 定义的 UDP 传输选项（Transport options）支持，允许在 IP 数据报的剩余区域（Surplus area）发送和接收 UDP 选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:479`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L479)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_NET_UDP_OPTIONS_DPLPMTUD"></a>

## 405.67 `CONFIG_NET_UDP_OPTIONS_DPLPMTUD`

**提示（Prompt）**：通过 UDP 选项执行 DPLPMTUD（RFC 9869）［实验性，Experimental］

**说明（Help）**

使用 UDP 选项（RFC 9869），为普通 UDP 套接字启用数据报分组化层路径 MTU 发现（Datagram Packetization Layer Path MTU Discovery，DPLPMTUD；RFC 8899）。在套接字上启用后，协议栈通过请求（REQ）和响应（RES）UDP 选项探测路径可使用的最大数据报大小，并通过 `getsockopt(IP_MTU/IPV6_MTU)` 报告结果。同时也响应收到的探测，将 REQ 令牌（Token）放入 RES 选项原样返回。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP_OPTIONS && CONFIG_NET_PMTU_DPLPMTUD && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:488`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L488)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP） → UDP 传输选项（Transport options，RFC 9868）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP_OPTIONS`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_OPTIONS)、[`CONFIG_NET_PMTU_DPLPMTUD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PMTU_DPLPMTUD)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_PMTU_DPLPMTUD`。

<a id="CONFIG_NET_UDP_OPTIONS_DPLPMTUD_ECHO_MIN_INTERVAL_MS"></a>

## 405.68 `CONFIG_NET_UDP_OPTIONS_DPLPMTUD_ECHO_MIN_INTERVAL_MS`

**提示（Prompt）**：UDP 选项 DPLPMTUD 的最小 RES 回送间隔（毫秒）

**说明（Help）**

套接字充当 DPLPMTUD 响应端（Responder）时，两次自动生成的响应（RES）回送之间的最短时间。协议栈通过向数据报源地址发送 RES 来响应请求（REQ），因此若无限制，路径外攻击者（Off-path attacker）大量发送伪造源地址的 REQ，就可能利用该套接字反射流量。RES 从不大于 REQ，因此不存在放大效应；此速率限制用于约束反射流量。设为 0 可禁用限制，例如用于必须同时响应许多不同探测端的服务器。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP_OPTIONS_DPLPMTUD && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:520`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L520)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP） → UDP 传输选项（Transport options，RFC 9868）［实验性，Experimental］ → 通过 UDP 选项执行 DPLPMTUD（RFC 9869）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP_OPTIONS_DPLPMTUD`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_OPTIONS_DPLPMTUD)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_UDP_OPTIONS_DPLPMTUD_PROBE_TIMEOUT_MS"></a>

## 405.69 `CONFIG_NET_UDP_OPTIONS_DPLPMTUD_PROBE_TIMEOUT_MS`

**提示（Prompt）**：UDP 选项 DPLPMTUD 的探测超时（Probe timeout，毫秒）

**说明（Help）**

等待探测响应（RES）的时间，超过后判定探测丢失并重传，对应 RFC 8899 的 `PROBE_TIMER`。由于 UDP 没有往返时间估计（Round-trip estimate），因此使用固定值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP_OPTIONS_DPLPMTUD && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:502`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L502)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP） → UDP 传输选项（Transport options，RFC 9868）［实验性，Experimental］ → 通过 UDP 选项执行 DPLPMTUD（RFC 9869）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP_OPTIONS_DPLPMTUD`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_OPTIONS_DPLPMTUD)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_UDP_OPTIONS_DPLPMTUD_RAISE_TIMEOUT_MS"></a>

## 405.70 `CONFIG_NET_UDP_OPTIONS_DPLPMTUD_RAISE_TIMEOUT_MS`

**提示（Prompt）**：UDP 选项 DPLPMTUD 的 MTU 增大探测计时器（Raise timer，毫秒）

**说明（Help）**

搜索完成后，等待多久再次探测，以发现路径 MTU 可能出现的增大，对应 RFC 8899 的 `PMTU_RAISE_TIMER`。默认值为 10 分钟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP_OPTIONS_DPLPMTUD && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
600000
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:511`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L511)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 用户数据报协议（UDP） → UDP 传输选项（Transport options，RFC 9868）［实验性，Experimental］ → 通过 UDP 选项执行 DPLPMTUD（RFC 9869）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP_OPTIONS_DPLPMTUD`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP_OPTIONS_DPLPMTUD)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_UTILS_LOG_LEVEL_CHOICE"></a>

## 405.71 `CONFIG_NET_UTILS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IP 协议栈实用函数（Utility function）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_UTILS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_UTILS_LOG_LEVEL_OFF
CONFIG_NET_UTILS_LOG_LEVEL_ERR
CONFIG_NET_UTILS_LOG_LEVEL_WRN
CONFIG_NET_UTILS_LOG_LEVEL_INF
CONFIG_NET_UTILS_LOG_LEVEL_DBG
CONFIG_NET_UTILS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_UTILS_LOG_LEVEL_DEFAULT`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UTILS_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_UTILS_LOG_LEVEL_OFF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UTILS_LOG_LEVEL_OFF)、[`CONFIG_NET_UTILS_LOG_LEVEL_ERR`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UTILS_LOG_LEVEL_ERR)、[`CONFIG_NET_UTILS_LOG_LEVEL_WRN`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UTILS_LOG_LEVEL_WRN)、[`CONFIG_NET_UTILS_LOG_LEVEL_INF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UTILS_LOG_LEVEL_INF)、[`CONFIG_NET_UTILS_LOG_LEVEL_DBG`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UTILS_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_UTILS_LOG_LEVEL_DBG"></a>

## 405.72 `CONFIG_NET_UTILS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_UTILS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IP 协议栈实用函数（Utility function）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_UTILS_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UTILS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_UTILS_LOG_LEVEL_DEFAULT"></a>

## 405.73 `CONFIG_NET_UTILS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_UTILS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IP 协议栈实用函数（Utility function）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_UTILS_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UTILS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_UTILS_LOG_LEVEL_ERR"></a>

## 405.74 `CONFIG_NET_UTILS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_UTILS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IP 协议栈实用函数（Utility function）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_UTILS_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UTILS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_UTILS_LOG_LEVEL_INF"></a>

## 405.75 `CONFIG_NET_UTILS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_UTILS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IP 协议栈实用函数（Utility function）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_UTILS_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UTILS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_UTILS_LOG_LEVEL_OFF"></a>

## 405.76 `CONFIG_NET_UTILS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_UTILS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IP 协议栈实用函数（Utility function）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_UTILS_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UTILS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_UTILS_LOG_LEVEL_WRN"></a>

## 405.77 `CONFIG_NET_UTILS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_UTILS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IP 协议栈实用函数（Utility function）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_UTILS_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UTILS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_VLAN"></a>

## 405.78 `CONFIG_NET_VLAN`

**提示（Prompt）**：虚拟局域网（Virtual LAN，VLAN）支持

**说明（Help）**

启用以太网的虚拟局域网（VLAN）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_VIRTUAL
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_VIRTUAL`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL)。

<a id="CONFIG_NET_VLAN_COUNT"></a>

## 405.79 `CONFIG_NET_VLAN_COUNT`

**提示（Prompt）**：系统支持的 VLAN 标签（Tag）最大数量

**说明（Help）**

可以配置的 VLAN 标签（Tag）数量。设为 0 时，只处理标签值为 0 的优先级标记 VLAN 帧。如果只希望接收标签 0，而不接收其他带 VLAN 标签的帧，此设置很有用。此时不会创建 VLAN 虚拟接口，因此可节省一些内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_VLAN && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 虚拟局域网（Virtual LAN，VLAN）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_VLAN`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_VLAN)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_VLAN_TXRX_DEBUG"></a>

## 405.80 `CONFIG_NET_VLAN_TXRX_DEBUG`

**提示（Prompt）**：调试 VLAN 中接收和发送的数据包（Packet）

**说明（Help）**

启用后，打印接收和发送的网络数据包。这可能产生大量输出，因此默认禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DBG && CONFIG_NET_VLAN && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 虚拟局域网（Virtual LAN，VLAN）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DBG`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DBG)、[`CONFIG_NET_VLAN`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_VLAN)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_VPN"></a>

## 405.81 `CONFIG_NET_VPN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在网络协议栈中配置虚拟专用网络（VPN）所需的基础支持，应由 VPN 实现启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_WIREGUARD
```

**定义位置（Location）**：[`subsys/net/lib/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)。

<a id="CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE"></a>

## 405.82 `CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE`

**提示（Prompt）**：WebSocket 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_WEBSOCKET_CLIENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_WEBSOCKET_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_WEBSOCKET_LOG_LEVEL_OFF
CONFIG_NET_WEBSOCKET_LOG_LEVEL_ERR
CONFIG_NET_WEBSOCKET_LOG_LEVEL_WRN
CONFIG_NET_WEBSOCKET_LOG_LEVEL_INF
CONFIG_NET_WEBSOCKET_LOG_LEVEL_DBG
CONFIG_NET_WEBSOCKET_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_WEBSOCKET_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CLIENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_WEBSOCKET_LOG_LEVEL_DEFAULT`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_WEBSOCKET_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_WEBSOCKET_LOG_LEVEL_OFF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_WEBSOCKET_LOG_LEVEL_OFF)、[`CONFIG_NET_WEBSOCKET_LOG_LEVEL_ERR`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_WEBSOCKET_LOG_LEVEL_ERR)、[`CONFIG_NET_WEBSOCKET_LOG_LEVEL_WRN`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_WEBSOCKET_LOG_LEVEL_WRN)、[`CONFIG_NET_WEBSOCKET_LOG_LEVEL_INF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_WEBSOCKET_LOG_LEVEL_INF)、[`CONFIG_NET_WEBSOCKET_LOG_LEVEL_DBG`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_WEBSOCKET_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_WEBSOCKET_LOG_LEVEL_DBG"></a>

## 405.83 `CONFIG_NET_WEBSOCKET_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → WebSocket 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_WEBSOCKET_LOG_LEVEL_DEFAULT"></a>

## 405.84 `CONFIG_NET_WEBSOCKET_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → WebSocket 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_WEBSOCKET_LOG_LEVEL_ERR"></a>

## 405.85 `CONFIG_NET_WEBSOCKET_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → WebSocket 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_WEBSOCKET_LOG_LEVEL_INF"></a>

## 405.86 `CONFIG_NET_WEBSOCKET_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → WebSocket 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_WEBSOCKET_LOG_LEVEL_OFF"></a>

## 405.87 `CONFIG_NET_WEBSOCKET_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → WebSocket 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_WEBSOCKET_LOG_LEVEL_WRN"></a>

## 405.88 `CONFIG_NET_WEBSOCKET_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → WebSocket 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_WEBSOCKET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ZPERF"></a>

## 405.89 `CONFIG_NET_ZPERF`

**提示（Prompt）**：zperf 性能测试库（Library）

**说明（Help）**

启用 zperf 库，可生成网络流量，并配合其他运行 zperf 的设备，或运行 iperf2、iperf3 工具的桌面计算机，评估网络带宽（Network bandwidth）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_CONTEXT_RCVTIMEO if CONFIG_NET_NATIVE_UDP
CONFIG_NET_SOCKETS
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CONTEXT_RCVTIMEO`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_RCVTIMEO)、[`CONFIG_NET_NATIVE_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_UDP)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_UDP`。

<a id="CONFIG_NET_ZPERF_IPERF2"></a>

## 405.90 `CONFIG_NET_ZPERF_IPERF2`

**提示（Prompt）**：iperf2

**说明（Help）**

与 iperf 2.0.10 及更新版本互操作（Interoperate）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ZPERF_PROTOCOL>
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library） → iperf 协议版本（Protocol version）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_PROTOCOL)。

<a id="CONFIG_NET_ZPERF_IPERF3"></a>

## 405.91 `CONFIG_NET_ZPERF_IPERF3`

**提示（Prompt）**：iperf3［实验性，Experimental］

**说明（Help）**

与 iperf 3 互操作（Interoperate）。测试通过 TCP 或 UDP 使用单个流（Single stream）。反向、双向、并行测试以及忽略测试开头一段时间的请求均会被拒绝，iperf3 客户端将报告不支持该选项的错误。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && <choice CONFIG_NET_ZPERF_PROTOCOL>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_JSON_LIBRARY
CONFIG_NET_CONTEXT_RCVTIMEO if CONFIG_NET_NATIVE_TCP
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library） → iperf 协议版本（Protocol version）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_ZPERF_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_PROTOCOL)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_JSON_LIBRARY`](P197_lib_配置项参考_1.md#CONFIG_JSON_LIBRARY)、[`CONFIG_NET_CONTEXT_RCVTIMEO`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_RCVTIMEO)、[`CONFIG_NET_NATIVE_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_TCP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_TCP`。

<a id="CONFIG_NET_ZPERF_IPERF3_IDLE_TIMEOUT"></a>

## 405.92 `CONFIG_NET_ZPERF_IPERF3_IDLE_TIMEOUT`

**提示（Prompt）**：丢弃空闲 iperf3 测试前等待的秒数

**说明（Help）**

如果 iperf3 测试的连接在此时长内没有活动，就结束测试，避免已消失的客户端阻止服务器接受下一次测试。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ZPERF_SERVER && CONFIG_NET_ZPERF_IPERF3 && CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[1, 3600]
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_SERVER)、[`CONFIG_NET_ZPERF_IPERF3`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_IPERF3)、[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ZPERF_IPERF3_JSON_MAX_LEN"></a>

## 405.93 `CONFIG_NET_ZPERF_IPERF3_JSON_MAX_LEN`

**提示（Prompt）**：iperf3 控制消息（Control message）的最大大小

**说明（Help）**

iperf3 控制连接可接收或发送的 JSON 消息的最大大小。iperf3 客户端发送的参数以及单流测试结果，通常为几百字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ZPERF_IPERF3 && CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[256, 8192]
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_IPERF3`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_IPERF3)、[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ZPERF_LEGACY_HEADER_COMPAT"></a>

## 405.94 `CONFIG_NET_ZPERF_LEGACY_HEADER_COMPAT`

**提示（Prompt）**：传统 iperf UDP 报头格式（Legacy header format）

**说明（Help）**

iperf 2.0.10（2017 年）以不向后兼容的方式更新了 UDP 报头格式，且无法自动检测。启用此项会恢复旧报头格式，以配合 iperf 2.0.9 及更早版本使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ZPERF_IPERF2 && CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_IPERF2`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_IPERF2)、[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE"></a>

## 405.95 `CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE`

**提示（Prompt）**：zperf 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_ZPERF_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_ZPERF_LOG_LEVEL_OFF
CONFIG_NET_ZPERF_LOG_LEVEL_ERR
CONFIG_NET_ZPERF_LOG_LEVEL_WRN
CONFIG_NET_ZPERF_LOG_LEVEL_INF
CONFIG_NET_ZPERF_LOG_LEVEL_DBG
CONFIG_NET_ZPERF_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_ZPERF_LOG_LEVEL_DEFAULT`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_ZPERF_LOG_LEVEL_OFF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_LOG_LEVEL_OFF)、[`CONFIG_NET_ZPERF_LOG_LEVEL_ERR`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_LOG_LEVEL_ERR)、[`CONFIG_NET_ZPERF_LOG_LEVEL_WRN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_LOG_LEVEL_WRN)、[`CONFIG_NET_ZPERF_LOG_LEVEL_INF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_LOG_LEVEL_INF)、[`CONFIG_NET_ZPERF_LOG_LEVEL_DBG`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_ZPERF_LOG_LEVEL_DBG"></a>

## 405.96 `CONFIG_NET_ZPERF_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library） → zperf 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ZPERF_LOG_LEVEL_DEFAULT"></a>

## 405.97 `CONFIG_NET_ZPERF_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library） → zperf 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ZPERF_LOG_LEVEL_ERR"></a>

## 405.98 `CONFIG_NET_ZPERF_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library） → zperf 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ZPERF_LOG_LEVEL_INF"></a>

## 405.99 `CONFIG_NET_ZPERF_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library） → zperf 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ZPERF_LOG_LEVEL_OFF"></a>

## 405.100 `CONFIG_NET_ZPERF_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library） → zperf 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P404_subsys_net_配置项参考_14.md) · [返回大纲](大纲.md) · [下一章](P406_subsys_net_配置项参考_16.md)
