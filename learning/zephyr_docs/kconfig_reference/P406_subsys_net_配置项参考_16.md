---
id: learning.zephyr-docs.kconfig-reference.page-406
title: "`subsys/net`配置项参考（16/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第406章\_`subsys/net`配置项参考（16/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_ZPERF_LOG_LEVEL_WRN"></a>

## 406.1 `CONFIG_NET_ZPERF_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library） → zperf 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ZPERF_MAX_PACKET_SIZE"></a>

## 406.2 `CONFIG_NET_ZPERF_MAX_PACKET_SIZE`

**提示（Prompt）**：最大数据包大小（Maximum packet size）

**说明（Help）**

zperf 发送数据包的大小上限。默认值允许包含 1 kB 有效载荷（Payload）和 40 字节的 iperf UDP 客户端报头。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1064
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ZPERF_MAX_SESSIONS"></a>

## 406.3 `CONFIG_NET_ZPERF_MAX_SESSIONS`

**提示（Prompt）**：zperf 会话（Session）的最大数量

**说明（Help）**

zperf 可处理的连接数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ZPERF_SERVER && CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library） → zperf 服务器（Server）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_SERVER`](P406_subsys_net_配置项参考_16.md#CONFIG_NET_ZPERF_SERVER)、[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ZPERF_PROTOCOL"></a>

## 406.4 `CONFIG_NET_ZPERF_PROTOCOL`

**提示（Prompt）**：iperf 协议版本（Protocol version）

**说明（Help）**

zperf 使用的 iperf 协议版本。iperf2 与 iperf3 的线上协议（Wire protocol）互不兼容，因此一次构建只支持其中一种。两者使用相同的 zperf API 和命令行命令（Shell command）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_ZPERF_IPERF2
```

**可选项（Choices）**

```text
CONFIG_NET_ZPERF_IPERF2
CONFIG_NET_ZPERF_IPERF3
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_ZPERF_IPERF2`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_IPERF2)、[`CONFIG_NET_ZPERF_IPERF3`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_IPERF3)。

<a id="CONFIG_NET_ZPERF_RAW_TX"></a>

## 406.5 `CONFIG_NET_ZPERF_RAW_TX`

**提示（Prompt）**：原始数据包发送（Raw packet TX）支持

**说明（Help）**

启用 zperf 中原始数据包套接字（Raw packet socket）的发送支持，允许发送带有用户自定义报头的原始数据包，用于性能测试。适用于测试供应商专用协议或自定义第二层（L2）帧。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_PACKET && CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_PACKET`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_PACKET)、[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ZPERF_RAW_TX_MAX_HDR_SIZE"></a>

## 406.6 `CONFIG_NET_ZPERF_RAW_TX_MAX_HDR_SIZE`

**提示（Prompt）**：原始发送报头（Raw TX header）的最大大小

**说明（Help）**

可添加在原始发送数据包之前的自定义报头的最大大小。用户以十六进制字节（Hex byte）形式提供报头。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ZPERF_RAW_TX && CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library） → 原始数据包发送（Raw packet TX）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_RAW_TX`](P406_subsys_net_配置项参考_16.md#CONFIG_NET_ZPERF_RAW_TX)、[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ZPERF_SERVER"></a>

## 406.7 `CONFIG_NET_ZPERF_SERVER`

**提示（Prompt）**：zperf 服务器（Server）支持

**说明（Help）**

支持从应用运行 zperf 服务器以测试下载（Download）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS_SERVICE
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS_SERVICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SERVICE)。

<a id="CONFIG_NET_ZPERF_TCP_RECEIVER_BUF_SIZE"></a>

## 406.8 `CONFIG_NET_ZPERF_TCP_RECEIVER_BUF_SIZE`

**提示（Prompt）**：TCP 接收器缓冲区大小（Receiver buffer size，字节）

**说明（Help）**

zperf TCP 接收器每次调用 `recv()` 时使用的接收缓冲区大小。更大的缓冲区可在一次调用中从套接字读取更多数据，有助于增大 TCP 窗口（Window），提高高速连接的吞吐量（Throughput）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ZPERF_SERVER && CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1500
```

**取值范围（Ranges）**

```text
[256, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_ZPERF_SERVER`](P406_subsys_net_配置项参考_16.md#CONFIG_NET_ZPERF_SERVER)、[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ZPERF_UDP_REPORT_RETANSMISSION_COUNT"></a>

## 406.9 `CONFIG_NET_ZPERF_UDP_REPORT_RETANSMISSION_COUNT`

**提示（Prompt）**：UDP 上传报告（Upload report）的最大重传次数

**说明（Help）**

zperf 从服务器获取 UDP 上传报告（Upload report）时的最大重试次数。`0` 表示完全不请求报告，可用于测试。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && CONFIG_NET_ZPERF && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[0, 16]
```

**定义位置（Location）**：[`subsys/net/lib/zperf/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → zperf 性能测试库（Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP)、[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OCPP"></a>

## 406.10 `CONFIG_OCPP`

**提示（Prompt）**：开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］

**说明（Help）**

启用开放充电协议（Open Charge Point Protocol，OCPP）库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_JSON_LIBRARY && CONFIG_WEBSOCKET_CLIENT && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_POSIX_C_LANG_SUPPORT_R
```

**定义位置（Location）**：[`subsys/net/lib/ocpp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_JSON_LIBRARY`](P197_lib_配置项参考_1.md#CONFIG_JSON_LIBRARY)、[`CONFIG_WEBSOCKET_CLIENT`](P408_subsys_net_配置项参考_18.md#CONFIG_WEBSOCKET_CLIENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_POSIX_C_LANG_SUPPORT_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_C_LANG_SUPPORT_R)。

<a id="CONFIG_OCPP_INTERNAL_MSGQ_CNT"></a>

## 406.11 `CONFIG_OCPP_INTERNAL_MSGQ_CNT`

**提示（Prompt）**：OCPP 内部消息队列（Message queue）的容量

**说明（Help）**

用于 WebSocket 读取线程与内部处理线程之间的消息通信（Message communication）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OCPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/net/lib/ocpp/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_OCPP`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OCPP_INT_THREAD_STACKSIZE"></a>

## 406.12 `CONFIG_OCPP_INT_THREAD_STACKSIZE`

**提示（Prompt）**：OCPP 内部线程栈大小（Thread stack size）

**说明（Help）**

OCPP 内部线程栈大小（Thread stack size）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OCPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/net/lib/ocpp/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_OCPP`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OCPP_LOG_LEVEL_CHOICE"></a>

## 406.13 `CONFIG_OCPP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：OCPP 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_OCPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_OCPP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_OCPP_LOG_LEVEL_OFF
CONFIG_OCPP_LOG_LEVEL_ERR
CONFIG_OCPP_LOG_LEVEL_WRN
CONFIG_OCPP_LOG_LEVEL_INF
CONFIG_OCPP_LOG_LEVEL_DBG
CONFIG_OCPP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_OCPP`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_OCPP_LOG_LEVEL_DEFAULT`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP_LOG_LEVEL_DEFAULT)、[`CONFIG_OCPP_LOG_LEVEL_OFF`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP_LOG_LEVEL_OFF)、[`CONFIG_OCPP_LOG_LEVEL_ERR`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP_LOG_LEVEL_ERR)、[`CONFIG_OCPP_LOG_LEVEL_WRN`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP_LOG_LEVEL_WRN)、[`CONFIG_OCPP_LOG_LEVEL_INF`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP_LOG_LEVEL_INF)、[`CONFIG_OCPP_LOG_LEVEL_DBG`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP_LOG_LEVEL_DBG)。

<a id="CONFIG_OCPP_LOG_LEVEL_DBG"></a>

## 406.14 `CONFIG_OCPP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OCPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］ → OCPP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_OCPP_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OCPP_LOG_LEVEL_DEFAULT"></a>

## 406.15 `CONFIG_OCPP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OCPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］ → OCPP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_OCPP_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OCPP_LOG_LEVEL_ERR"></a>

## 406.16 `CONFIG_OCPP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OCPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］ → OCPP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_OCPP_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OCPP_LOG_LEVEL_INF"></a>

## 406.17 `CONFIG_OCPP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OCPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］ → OCPP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_OCPP_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OCPP_LOG_LEVEL_OFF"></a>

## 406.18 `CONFIG_OCPP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OCPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］ → OCPP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_OCPP_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OCPP_LOG_LEVEL_WRN"></a>

## 406.19 `CONFIG_OCPP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OCPP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］ → OCPP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_OCPP_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OCPP_MSG_JSON"></a>

## 406.20 `CONFIG_OCPP_MSG_JSON`

**提示（Prompt）**：使用 JSON 格式的协议数据单元（PDU）消息

**说明（Help）**

设为 `y` 后，充电点（Charge Point）与中央系统（Central System）的协议数据单元（PDU）消息采用 JSON 格式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OCPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/ocpp/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_OCPP`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OCPP_PROFILE_FIRMWARE_MGNT"></a>

## 406.21 `CONFIG_OCPP_PROFILE_FIRMWARE_MGNT`

**提示（Prompt）**：OCPP 固件管理功能配置文件（Firmware Management profile）

**说明（Help）**

让 OCPP 库支持充电点（Charge Point）的固件管理（Firmware Management），作为可选功能配置文件（Optional profile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OCPP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/ocpp/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_OCPP`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OCPP_PROFILE_LOCAL_AUTH_LIST"></a>

## 406.22 `CONFIG_OCPP_PROFILE_LOCAL_AUTH_LIST`

**提示（Prompt）**：OCPP 本地授权列表功能配置文件（Local Authorization List profile）

**说明（Help）**

让 OCPP 库支持本地授权列表（Local Authorization List）功能，将 `IdTag` 及其有效性信息保存在持久存储（Persistent storage）中。充电点（Charge Point）可选择支持此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OCPP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/ocpp/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_OCPP`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OCPP_PROFILE_REMOTE_TRIG"></a>

## 406.23 `CONFIG_OCPP_PROFILE_REMOTE_TRIG`

**提示（Prompt）**：OCPP 远程触发功能配置文件（Remote Trigger profile）

**说明（Help）**

让 OCPP 库支持远程触发（Remote Trigger）功能。充电点（Charge Point）可选择支持此功能配置文件（Profile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OCPP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/ocpp/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_OCPP`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OCPP_PROFILE_RESERVATION"></a>

## 406.24 `CONFIG_OCPP_PROFILE_RESERVATION`

**提示（Prompt）**：OCPP 预约功能配置文件（Reservation profile）

**说明（Help）**

让 OCPP 库支持预约（Reservation）功能。充电点（Charge Point）可选择支持此功能配置文件（Profile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OCPP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/ocpp/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_OCPP`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OCPP_PROFILE_SMART_CHARGE"></a>

## 406.25 `CONFIG_OCPP_PROFILE_SMART_CHARGE`

**提示（Prompt）**：OCPP 智能充电功能配置文件（Smart Charging profile）

**说明（Help）**

让 OCPP 库支持智能充电（Smart Charging）功能配置文件。充电点（Charge Point）可选择支持此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OCPP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/ocpp/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_OCPP`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OCPP_RECV_BUFFER_SIZE"></a>

## 406.26 `CONFIG_OCPP_RECV_BUFFER_SIZE`

**提示（Prompt）**：OCPP WebSocket 接收缓冲区大小（Receive buffer size）

**说明（Help）**

OCPP WebSocket 接收缓冲区大小（Receive buffer size）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OCPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/net/lib/ocpp/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_OCPP`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OCPP_WSREADER_THREAD_STACKSIZE"></a>

## 406.27 `CONFIG_OCPP_WSREADER_THREAD_STACKSIZE`

**提示（Prompt）**：OCPP WebSocket 读取线程栈大小（Reader thread stack size）

**说明（Help）**

OCPP WebSocket 读取线程栈大小（Reader thread stack size）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OCPP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/net/lib/ocpp/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放充电协议（Open Charge Point Protocol，OCPP）［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_OCPP`](P406_subsys_net_配置项参考_16.md#CONFIG_OCPP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OPENTHREAD_L2_DEBUG"></a>

## 406.28 `CONFIG_OPENTHREAD_L2_DEBUG`

**提示（Prompt）**：OpenThread 第二层（L2）日志支持

**说明（Help）**

启用 OpenThread 日志（Log）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_OPENTHREAD && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/openthread/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/openthread/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → OpenThread 第二层（L2） → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_OPENTHREAD`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_OPENTHREAD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OPENTHREAD_L2_DEBUG_DUMP_15_4"></a>

## 406.29 `CONFIG_OPENTHREAD_L2_DEBUG_DUMP_15_4`

**提示（Prompt）**：转储 IEEE 802.15.4 数据包（Dump packets）

**说明（Help）**

启用 IEEE 802.15.4 数据包转储（Packet dump）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_L2_DEBUG && CONFIG_NET_L2_OPENTHREAD && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/openthread/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/openthread/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → OpenThread 第二层（L2） → 日志（Logging）。 → OpenThread 第二层（L2）日志支持

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_L2_DEBUG`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_DEBUG)、[`CONFIG_NET_L2_OPENTHREAD`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_OPENTHREAD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OPENTHREAD_L2_DEBUG_DUMP_IPV6"></a>

## 406.30 `CONFIG_OPENTHREAD_L2_DEBUG_DUMP_IPV6`

**提示（Prompt）**：转储 IPv6 数据包（Dump packets）

**说明（Help）**

启用 IPv6 数据包转储（Packet dump）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_L2_DEBUG && CONFIG_NET_L2_OPENTHREAD && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/openthread/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/openthread/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → OpenThread 第二层（L2） → 日志（Logging）。 → OpenThread 第二层（L2）日志支持

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_L2_DEBUG`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_DEBUG)、[`CONFIG_NET_L2_OPENTHREAD`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_OPENTHREAD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE"></a>

## 406.31 `CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE`

**提示（Prompt）**：OpenThread 驱动日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_L2_OPENTHREAD && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_OPENTHREAD_L2_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_OPENTHREAD_L2_LOG_LEVEL_OFF
CONFIG_OPENTHREAD_L2_LOG_LEVEL_ERR
CONFIG_OPENTHREAD_L2_LOG_LEVEL_WRN
CONFIG_OPENTHREAD_L2_LOG_LEVEL_INF
CONFIG_OPENTHREAD_L2_LOG_LEVEL_DBG
CONFIG_OPENTHREAD_L2_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → OpenThread 第二层（L2） → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_L2_OPENTHREAD`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_OPENTHREAD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_OPENTHREAD_L2_LOG_LEVEL_DEFAULT`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_LOG_LEVEL_DEFAULT)、[`CONFIG_OPENTHREAD_L2_LOG_LEVEL_OFF`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_LOG_LEVEL_OFF)、[`CONFIG_OPENTHREAD_L2_LOG_LEVEL_ERR`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_LOG_LEVEL_ERR)、[`CONFIG_OPENTHREAD_L2_LOG_LEVEL_WRN`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_LOG_LEVEL_WRN)、[`CONFIG_OPENTHREAD_L2_LOG_LEVEL_INF`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_LOG_LEVEL_INF)、[`CONFIG_OPENTHREAD_L2_LOG_LEVEL_DBG`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_LOG_LEVEL_DBG)。

<a id="CONFIG_OPENTHREAD_L2_LOG_LEVEL_DBG"></a>

## 406.32 `CONFIG_OPENTHREAD_L2_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → OpenThread 第二层（L2） → 日志（Logging）。 → OpenThread 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPENTHREAD_L2_LOG_LEVEL_DEFAULT"></a>

## 406.33 `CONFIG_OPENTHREAD_L2_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → OpenThread 第二层（L2） → 日志（Logging）。 → OpenThread 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPENTHREAD_L2_LOG_LEVEL_ERR"></a>

## 406.34 `CONFIG_OPENTHREAD_L2_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → OpenThread 第二层（L2） → 日志（Logging）。 → OpenThread 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPENTHREAD_L2_LOG_LEVEL_INF"></a>

## 406.35 `CONFIG_OPENTHREAD_L2_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → OpenThread 第二层（L2） → 日志（Logging）。 → OpenThread 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPENTHREAD_L2_LOG_LEVEL_OFF"></a>

## 406.36 `CONFIG_OPENTHREAD_L2_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → OpenThread 第二层（L2） → 日志（Logging）。 → OpenThread 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPENTHREAD_L2_LOG_LEVEL_WRN"></a>

## 406.37 `CONFIG_OPENTHREAD_L2_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → OpenThread 第二层（L2） → 日志（Logging）。 → OpenThread 驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_OPENTHREAD_L2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PHY_LOG_LEVEL_CHOICE"></a>

## 406.38 `CONFIG_PHY_LOG_LEVEL_CHOICE`

**提示（Prompt）**：以太网物理层（Ethernet PHY）驱动日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ETH_PHY_DRIVER && CONFIG_ETH_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_PHY_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PHY_LOG_LEVEL_OFF
CONFIG_PHY_LOG_LEVEL_ERR
CONFIG_PHY_LOG_LEVEL_WRN
CONFIG_PHY_LOG_LEVEL_INF
CONFIG_PHY_LOG_LEVEL_DBG
CONFIG_PHY_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ETH_PHY_DRIVER`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_PHY_DRIVER)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_PHY_LOG_LEVEL_DEFAULT`](P406_subsys_net_配置项参考_16.md#CONFIG_PHY_LOG_LEVEL_DEFAULT)、[`CONFIG_PHY_LOG_LEVEL_OFF`](P406_subsys_net_配置项参考_16.md#CONFIG_PHY_LOG_LEVEL_OFF)、[`CONFIG_PHY_LOG_LEVEL_ERR`](P406_subsys_net_配置项参考_16.md#CONFIG_PHY_LOG_LEVEL_ERR)、[`CONFIG_PHY_LOG_LEVEL_WRN`](P406_subsys_net_配置项参考_16.md#CONFIG_PHY_LOG_LEVEL_WRN)、[`CONFIG_PHY_LOG_LEVEL_INF`](P406_subsys_net_配置项参考_16.md#CONFIG_PHY_LOG_LEVEL_INF)、[`CONFIG_PHY_LOG_LEVEL_DBG`](P406_subsys_net_配置项参考_16.md#CONFIG_PHY_LOG_LEVEL_DBG)。

<a id="CONFIG_PHY_LOG_LEVEL_DBG"></a>

## 406.39 `CONFIG_PHY_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PHY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → 以太网物理层（Ethernet PHY）驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PHY_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PHY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PHY_LOG_LEVEL_DEFAULT"></a>

## 406.40 `CONFIG_PHY_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PHY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → 以太网物理层（Ethernet PHY）驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PHY_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PHY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PHY_LOG_LEVEL_ERR"></a>

## 406.41 `CONFIG_PHY_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PHY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → 以太网物理层（Ethernet PHY）驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PHY_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PHY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PHY_LOG_LEVEL_INF"></a>

## 406.42 `CONFIG_PHY_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PHY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → 以太网物理层（Ethernet PHY）驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PHY_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PHY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PHY_LOG_LEVEL_OFF"></a>

## 406.43 `CONFIG_PHY_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PHY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → 以太网物理层（Ethernet PHY）驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PHY_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PHY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PHY_LOG_LEVEL_WRN"></a>

## 406.44 `CONFIG_PHY_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PHY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 以太网驱动（Ethernet Drivers） → 以太网物理层驱动（Ethernet PHY Drivers） → 以太网物理层（Ethernet PHY）驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PHY_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PHY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PROMETHEUS"></a>

## 406.45 `CONFIG_PROMETHEUS`

**提示（Prompt）**：Prometheus 客户端库（Client Library；拉取方式，Pull Method）

**说明（Help）**

启用 Prometheus 客户端库（Client library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_HTTP_SERVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/prometheus/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/prometheus/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PROMETHEUS_LABEL_MAX_COUNT"></a>

## 406.46 `CONFIG_PROMETHEUS_LABEL_MAX_COUNT`

**提示（Prompt）**：每个指标（Metric）的最大标签数（Label count）

**说明（Help）**

指定一个指标（Metric）最多可附带多少个标签（Label）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PROMETHEUS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`subsys/net/lib/prometheus/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/prometheus/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Prometheus 客户端库（Client Library；拉取方式，Pull Method）

**配置项引用（Symbol References）**：[`CONFIG_PROMETHEUS`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE"></a>

## 406.47 `CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Prometheus 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_PROMETHEUS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_PROMETHEUS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PROMETHEUS_LOG_LEVEL_OFF
CONFIG_PROMETHEUS_LOG_LEVEL_ERR
CONFIG_PROMETHEUS_LOG_LEVEL_WRN
CONFIG_PROMETHEUS_LOG_LEVEL_INF
CONFIG_PROMETHEUS_LOG_LEVEL_DBG
CONFIG_PROMETHEUS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Prometheus 客户端库（Client Library；拉取方式，Pull Method）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_PROMETHEUS`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PROMETHEUS_LOG_LEVEL_DEFAULT`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS_LOG_LEVEL_DEFAULT)、[`CONFIG_PROMETHEUS_LOG_LEVEL_OFF`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS_LOG_LEVEL_OFF)、[`CONFIG_PROMETHEUS_LOG_LEVEL_ERR`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS_LOG_LEVEL_ERR)、[`CONFIG_PROMETHEUS_LOG_LEVEL_WRN`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS_LOG_LEVEL_WRN)、[`CONFIG_PROMETHEUS_LOG_LEVEL_INF`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS_LOG_LEVEL_INF)、[`CONFIG_PROMETHEUS_LOG_LEVEL_DBG`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS_LOG_LEVEL_DBG)。

<a id="CONFIG_PROMETHEUS_LOG_LEVEL_DBG"></a>

## 406.48 `CONFIG_PROMETHEUS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Prometheus 客户端库（Client Library；拉取方式，Pull Method） → Prometheus 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PROMETHEUS_LOG_LEVEL_DEFAULT"></a>

## 406.49 `CONFIG_PROMETHEUS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Prometheus 客户端库（Client Library；拉取方式，Pull Method） → Prometheus 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PROMETHEUS_LOG_LEVEL_ERR"></a>

## 406.50 `CONFIG_PROMETHEUS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Prometheus 客户端库（Client Library；拉取方式，Pull Method） → Prometheus 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PROMETHEUS_LOG_LEVEL_INF"></a>

## 406.51 `CONFIG_PROMETHEUS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Prometheus 客户端库（Client Library；拉取方式，Pull Method） → Prometheus 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PROMETHEUS_LOG_LEVEL_OFF"></a>

## 406.52 `CONFIG_PROMETHEUS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Prometheus 客户端库（Client Library；拉取方式，Pull Method） → Prometheus 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PROMETHEUS_LOG_LEVEL_WRN"></a>

## 406.53 `CONFIG_PROMETHEUS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Prometheus 客户端库（Client Library；拉取方式，Pull Method） → Prometheus 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PROMETHEUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTP"></a>

## 406.54 `CONFIG_PTP`

**提示（Prompt）**：IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**说明（Help）**

启用精确时间协议（PTP）协议栈，用于发送和接收 PTP 数据包，以及处理网络数据包时间戳（Timestamp）。该协议实现仅支持 PTP 节点（Node）中的一个 PTP 实例（Instance）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && !CONFIG_NET_GPTP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_PRECISION_TIMING
CONFIG_ZVFS
CONFIG_ZVFS_EVENTFD
CONFIG_NET_SOCKETS
CONFIG_NET_CONTEXT_PRIORITY
CONFIG_PTP_CLOCK
CONFIG_NET_L2_PTP_TIMESTAMPING
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_PRECISION_TIMING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PRECISION_TIMING)、[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_EVENTFD`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_EVENTFD)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NET_CONTEXT_PRIORITY`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_CONTEXT_PRIORITY)、[`CONFIG_PTP_CLOCK`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PTP_TIMESTAMPING)。

<a id="CONFIG_PTP_ANNOUNCE_LOG_INTERVAL"></a>

## 406.55 `CONFIG_PTP_ANNOUNCE_LOG_INTERVAL`

**提示（Prompt）**：连续 Announce 报文之间的间隔

**说明（Help）**

定义连续 Announce 报文之间的平均时间间隔。此值在整个 PTP 域（Domain）内应一致，详见 IEEE 1588-2019 第 7.7.2.2 节。配置值按以下公式转换为纳秒：`nanoseconds = (10^9) * 2^(value)`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 4]
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:325`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L325)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_ANNOUNCE_RECV_TIMEOUT"></a>

## 406.56 `CONFIG_PTP_ANNOUNCE_RECV_TIMEOUT`

**提示（Prompt）**：等待的通告间隔（Announce interval）数量

**说明（Help）**

定义连续多少个通告间隔（Announce interval）没有收到 Announce 报文后，就认定时间发送端（timeTransmitter）已停止发送 Announce，并触发超时事件（Timeout event）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[2, 10]
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:316`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L316)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_BOUNDARY_CLOCK"></a>

## 406.57 `CONFIG_PTP_BOUNDARY_CLOCK`

**提示（Prompt）**：边界时钟（Boundary Clock）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟类型（Clock Type）

<a id="CONFIG_PTP_CLOCK_ACCURACY_100MS"></a>

## 406.58 `CONFIG_PTP_CLOCK_ACCURACY_100MS`

**提示（Prompt）**：100 毫秒（100 ms）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L260)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_100NS"></a>

## 406.59 `CONFIG_PTP_CLOCK_ACCURACY_100NS`

**提示（Prompt）**：100 纳秒（100 ns）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:224`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L224)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_100US"></a>

## 406.60 `CONFIG_PTP_CLOCK_ACCURACY_100US`

**提示（Prompt）**：100 微秒（100 us）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:242`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L242)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_10MS"></a>

## 406.61 `CONFIG_PTP_CLOCK_ACCURACY_10MS`

**提示（Prompt）**：10 毫秒（10 ms）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:254`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L254)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_10S"></a>

## 406.62 `CONFIG_PTP_CLOCK_ACCURACY_10S`

**提示（Prompt）**：10 秒（10 s）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:269`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L269)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_10US"></a>

## 406.63 `CONFIG_PTP_CLOCK_ACCURACY_10US`

**提示（Prompt）**：10 微秒（10 us）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:236`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L236)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_1MS"></a>

## 406.64 `CONFIG_PTP_CLOCK_ACCURACY_1MS`

**提示（Prompt）**：1 毫秒（1 ms）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:248`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L248)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_1S"></a>

## 406.65 `CONFIG_PTP_CLOCK_ACCURACY_1S`

**提示（Prompt）**：1 秒（1 s）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:266`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L266)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_1US"></a>

## 406.66 `CONFIG_PTP_CLOCK_ACCURACY_1US`

**提示（Prompt）**：1 微秒（1 us）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:230`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L230)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_250MS"></a>

## 406.67 `CONFIG_PTP_CLOCK_ACCURACY_250MS`

**提示（Prompt）**：250 ms

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:263`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L263)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_250NS"></a>

## 406.68 `CONFIG_PTP_CLOCK_ACCURACY_250NS`

**提示（Prompt）**：250 纳秒（250 ns）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_250US"></a>

## 406.69 `CONFIG_PTP_CLOCK_ACCURACY_250US`

**提示（Prompt）**：250 微秒（250 us）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:245`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L245)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_25MS"></a>

## 406.70 `CONFIG_PTP_CLOCK_ACCURACY_25MS`

**提示（Prompt）**：25 毫秒（25 ms）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:257`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L257)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_25NS"></a>

## 406.71 `CONFIG_PTP_CLOCK_ACCURACY_25NS`

**提示（Prompt）**：25 纳秒（25 ns）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_25US"></a>

## 406.72 `CONFIG_PTP_CLOCK_ACCURACY_25US`

**提示（Prompt）**：25 微秒（25 us）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_2_5MS"></a>

## 406.73 `CONFIG_PTP_CLOCK_ACCURACY_2_5MS`

**提示（Prompt）**：1.5 毫秒（1.5 ms）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L251)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_2_5US"></a>

## 406.74 `CONFIG_PTP_CLOCK_ACCURACY_2_5US`

**提示（Prompt）**：2.5 微秒（2.5 us）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L233)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_GT_10S"></a>

## 406.75 `CONFIG_PTP_CLOCK_ACCURACY_GT_10S`

**提示（Prompt）**：大于 10 秒（> 10 s）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:272`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L272)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_CLOCK_ACCURACY_UNKNOWN"></a>

## 406.76 `CONFIG_PTP_CLOCK_ACCURACY_UNKNOWN`

**提示（Prompt）**：未知（Unknown）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:218`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L218)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 时钟精度（Clock Accuracy）

<a id="CONFIG_PTP_DELAY_MECHANISM_E2E"></a>

## 406.77 `CONFIG_PTP_DELAY_MECHANISM_E2E`

**提示（Prompt）**：端到端（End-to-End，E2E）

**说明（Help）**

使用 Delay_Req 和 Delay_Resp 报文，测量时间接收端（timeReceiver）与时间发送端（timeTransmitter）之间的延迟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_DELAY_MECHANISM_TYPE>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 延迟测量机制（Delay Mechanism）

**配置项引用（Symbol References）**：[`CONFIG_PTP_DELAY_MECHANISM_TYPE`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_DELAY_MECHANISM_TYPE)。

<a id="CONFIG_PTP_DELAY_MECHANISM_P2P"></a>

## 406.78 `CONFIG_PTP_DELAY_MECHANISM_P2P`

**提示（Prompt）**：对等（Peer-to-Peer，P2P）

**说明（Help）**

使用 Pdelay_Req、Pdelay_Resp 和 Pdelay_Resp_Follow_Up 报文，测量相邻端口之间的延迟。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_DELAY_MECHANISM_TYPE>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 延迟测量机制（Delay Mechanism）

**配置项引用（Symbol References）**：[`CONFIG_PTP_DELAY_MECHANISM_TYPE`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_DELAY_MECHANISM_TYPE)。

<a id="CONFIG_PTP_DELAY_MECHANISM_TYPE"></a>

## 406.79 `CONFIG_PTP_DELAY_MECHANISM_TYPE`

**提示（Prompt）**：PTP 延迟测量机制（Delay Mechanism）

**说明（Help）**

选择用于测量传播延迟（Propagation delay）的延迟机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_PTP_DELAY_MECHANISM_E2E
```

**可选项（Choices）**

```text
CONFIG_PTP_DELAY_MECHANISM_E2E
CONFIG_PTP_DELAY_MECHANISM_P2P
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PTP_DELAY_MECHANISM_E2E`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_DELAY_MECHANISM_E2E)、[`CONFIG_PTP_DELAY_MECHANISM_P2P`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_DELAY_MECHANISM_P2P)。

<a id="CONFIG_PTP_DSCP_HIGH_PRIORITY"></a>

## 406.80 `CONFIG_PTP_DSCP_HIGH_PRIORITY`

**提示（Prompt）**：PTP 数据包分类的高优先级（High priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_DSCP_PRIORITY>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:406`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L406)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 数据包分类优先级（Packet classification priority）

**配置项引用（Symbol References）**：[`CONFIG_PTP_DSCP_PRIORITY`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_DSCP_PRIORITY)。

<a id="CONFIG_PTP_DSCP_MEDIUM_PRIORITY"></a>

## 406.81 `CONFIG_PTP_DSCP_MEDIUM_PRIORITY`

**提示（Prompt）**：PTP 数据包分类的中优先级（Medium priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_DSCP_PRIORITY>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:409`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L409)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 数据包分类优先级（Packet classification priority）

**配置项引用（Symbol References）**：[`CONFIG_PTP_DSCP_PRIORITY`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_DSCP_PRIORITY)。

<a id="CONFIG_PTP_DSCP_NONE_PRIORITY"></a>

## 406.82 `CONFIG_PTP_DSCP_NONE_PRIORITY`

**提示（Prompt）**：PTP 数据包分类的默认优先级（Default priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_DSCP_PRIORITY>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:412`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L412)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 数据包分类优先级（Packet classification priority）

**配置项引用（Symbol References）**：[`CONFIG_PTP_DSCP_PRIORITY`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_DSCP_PRIORITY)。

<a id="CONFIG_PTP_DSCP_PRIORITY"></a>

## 406.83 `CONFIG_PTP_DSCP_PRIORITY`

**提示（Prompt）**：PTP 数据包分类优先级（Packet classification priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_PTP_DSCP_NONE_PRIORITY
```

**可选项（Choices）**

```text
CONFIG_PTP_DSCP_HIGH_PRIORITY
CONFIG_PTP_DSCP_MEDIUM_PRIORITY
CONFIG_PTP_DSCP_NONE_PRIORITY
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:402`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L402)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PTP_DSCP_NONE_PRIORITY`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_DSCP_NONE_PRIORITY)、[`CONFIG_PTP_DSCP_HIGH_PRIORITY`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_DSCP_HIGH_PRIORITY)、[`CONFIG_PTP_DSCP_MEDIUM_PRIORITY`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_DSCP_MEDIUM_PRIORITY)。

<a id="CONFIG_PTP_FOREIGN_TIME_TRANSMITTER_RECORD_SIZE"></a>

## 406.84 `CONFIG_PTP_FOREIGN_TIME_TRANSMITTER_RECORD_SIZE`

**提示（Prompt）**：存储外部时间发送端（Foreign timeTransmitter）数据的数组大小

**说明（Help）**

IEEE 1588-2019 规定，每个 PTP 端口的列表至少容纳 5 条外部时间发送端（Foreign timeTransmitter）记录。Kconfig 不支持数学运算，因此当启用 `PTP_FOREIGN_TIME_TRANSMITTER_FEATURE`，且 `PTP_NUM_PORTS` 大于 1 时，应相应调整本选项的值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_FOREIGN_TIME_TRANSMITTER_FEATURE && CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:392`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L392)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP_FOREIGN_TIME_TRANSMITTER_FEATURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_FOREIGN_TIME_TRANSMITTER_FEATURE)、[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_PTP_FOREIGN_TIME_TRANSMITTER_FEATURE`。

<a id="CONFIG_PTP_HYBRID_FALLBACK_ATTEMPTS"></a>

## 406.85 `CONFIG_PTP_HYBRID_FALLBACK_ATTEMPTS`

**提示（Prompt）**：回退到多播前，未得到响应的单播 Delay_Req 次数

**说明（Help）**

连续多少次单播 Delay_Req 未收到匹配的 Delay_Resp 后，端口就认定时间发送端（timeTransmitter）不支持单播延迟测量，并回退到多播（Multicast）Delay_Req。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_PTP_NETWORK_MODE_HYBRID_NO_FALLBACK && CONFIG_PTP_NETWORK_MODE_HYBRID && CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP_NETWORK_MODE_HYBRID_NO_FALLBACK`](P407_subsys_net_配置项参考_17.md#CONFIG_PTP_NETWORK_MODE_HYBRID_NO_FALLBACK)、[`CONFIG_PTP_NETWORK_MODE_HYBRID`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_NETWORK_MODE_HYBRID)、[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_IEEE_802_3_PROTOCOL"></a>

## 406.86 `CONFIG_PTP_IEEE_802_3_PROTOCOL`

**提示（Prompt）**：IEEE 802.3（第二层，Layer 2；EtherType `0x88F7`）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_NETWORKING_PROTOCOL>
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS_PACKET
CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L203)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 协议栈使用的网络协议（Networking Protocol）

**配置项引用（Symbol References）**：[`CONFIG_PTP_NETWORKING_PROTOCOL`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_NETWORKING_PROTOCOL)、[`CONFIG_NET_SOCKETS_PACKET`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_PACKET)、[`CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP)。

<a id="CONFIG_PTP_INIT_PRIO"></a>

## 406.87 `CONFIG_PTP_INIT_PRIO`

**提示（Prompt）**：PTP 协议栈初始化的启动优先级（Startup priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
96
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_LOG_LEVEL_CHOICE"></a>

## 406.88 `CONFIG_PTP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：PTP 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_PTP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_PTP_LOG_LEVEL_OFF
CONFIG_PTP_LOG_LEVEL_ERR
CONFIG_PTP_LOG_LEVEL_WRN
CONFIG_PTP_LOG_LEVEL_INF
CONFIG_PTP_LOG_LEVEL_DBG
CONFIG_PTP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PTP_LOG_LEVEL_DEFAULT`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_LOG_LEVEL_DEFAULT)、[`CONFIG_PTP_LOG_LEVEL_OFF`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_LOG_LEVEL_OFF)、[`CONFIG_PTP_LOG_LEVEL_ERR`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_LOG_LEVEL_ERR)、[`CONFIG_PTP_LOG_LEVEL_WRN`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_LOG_LEVEL_WRN)、[`CONFIG_PTP_LOG_LEVEL_INF`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_LOG_LEVEL_INF)、[`CONFIG_PTP_LOG_LEVEL_DBG`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_LOG_LEVEL_DBG)。

<a id="CONFIG_PTP_LOG_LEVEL_DBG"></a>

## 406.89 `CONFIG_PTP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PTP_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTP_LOG_LEVEL_DEFAULT"></a>

## 406.90 `CONFIG_PTP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PTP_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTP_LOG_LEVEL_ERR"></a>

## 406.91 `CONFIG_PTP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PTP_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTP_LOG_LEVEL_INF"></a>

## 406.92 `CONFIG_PTP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PTP_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTP_LOG_LEVEL_OFF"></a>

## 406.93 `CONFIG_PTP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PTP_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTP_LOG_LEVEL_WRN"></a>

## 406.94 `CONFIG_PTP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → PTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_PTP_LOG_LEVEL_CHOICE`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_PTP_MIN_DELAY_REQ_LOG_INTERVAL"></a>

## 406.95 `CONFIG_PTP_MIN_DELAY_REQ_LOG_INTERVAL`

**提示（Prompt）**：连续 Delay_Req 报文之间的间隔

**说明（Help）**

Delay_Req 报文之间的最短时间间隔。配置值按以下公式转换为纳秒：`nanoseconds = (10^9) * 2^(value)`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 5]
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:334`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L334)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_MIN_PDELAY_REQ_LOG_INTERVAL"></a>

## 406.96 `CONFIG_PTP_MIN_PDELAY_REQ_LOG_INTERVAL`

**提示（Prompt）**：以 2 为底的对数（Log2）设置 Pdelay_Req 间隔

**说明（Help）**

指定连续 Pdelay_Req 报文之间允许的最小平均时间间隔。配置值按以下公式转换为纳秒：`nanoseconds = (10^9) * 2^(value)`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[-7, 5]
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:351`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L351)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_MSG_POLL_SIZE"></a>

## 406.97 `CONFIG_PTP_MSG_POLL_SIZE`

**提示（Prompt）**：可供分配的报文（Message）数量

**说明（Help）**

PTP 报文从内存块池（Memory slab）动态分配，此 Kconfig 符号定义池中的块数量。其中一半报文可用于所有 PTP 端口的外部时间发送端（Foreign timeTransmitter）记录中保存的 Announce 报文。每个 PTP 端口会为当前时间发送端保存最多三个此类报文，因此使用更多端口时，应增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_PTP_NETWORKING_PROTOCOL"></a>

## 406.98 `CONFIG_PTP_NETWORKING_PROTOCOL`

**提示（Prompt）**：PTP 协议栈使用的网络协议（Networking Protocol）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_PTP_UDP_IPV4_PROTOCOL
```

**可选项（Choices）**

```text
CONFIG_PTP_UDP_IPV4_PROTOCOL
CONFIG_PTP_UDP_IPV6_PROTOCOL
CONFIG_PTP_IEEE_802_3_PROTOCOL
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:188`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L188)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PTP_UDP_IPV4_PROTOCOL`](P407_subsys_net_配置项参考_17.md#CONFIG_PTP_UDP_IPV4_PROTOCOL)、[`CONFIG_PTP_UDP_IPV6_PROTOCOL`](P407_subsys_net_配置项参考_17.md#CONFIG_PTP_UDP_IPV6_PROTOCOL)、[`CONFIG_PTP_IEEE_802_3_PROTOCOL`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_IEEE_802_3_PROTOCOL)。

<a id="CONFIG_PTP_NETWORK_MODE"></a>

## 406.99 `CONFIG_PTP_NETWORK_MODE`

**提示（Prompt）**：网络传输模式（Network transmission mode）

**说明（Help）**

选择如何发送延迟测量（Delay measurement）报文。Announce、Sync 和 Follow_Up 报文始终发送到默认多播地址（Multicast address）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_PTP_NETWORK_MODE_MULTICAST
```

**可选项（Choices）**

```text
CONFIG_PTP_NETWORK_MODE_MULTICAST
CONFIG_PTP_NETWORK_MODE_HYBRID
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_PTP`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PTP_NETWORK_MODE_MULTICAST`](P407_subsys_net_配置项参考_17.md#CONFIG_PTP_NETWORK_MODE_MULTICAST)、[`CONFIG_PTP_NETWORK_MODE_HYBRID`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_NETWORK_MODE_HYBRID)。

<a id="CONFIG_PTP_NETWORK_MODE_HYBRID"></a>

## 406.100 `CONFIG_PTP_NETWORK_MODE_HYBRID`

**提示（Prompt）**：混合模式（Hybrid）

**说明（Help）**

混合模式（Hybrid）下，端到端（End-to-End）延迟测量使用单播报文：Delay_Req 直接发往当前时间发送端（timeTransmitter）的协议地址，即 IP 地址，或 IEEE 802.3 传输中的 MAC 地址；Delay_Resp 直接返回发起请求的时间接收端（timeReceiver）。由于节点不再收到其他节点的延迟测量报文，这可降低大型 PTP 域中的多播负载。此模式兼容 linuxptp 的 `hybrid_e2e` 选项和 sfptpd 的 `hybrid` `ptp_network_mode`。除非启用 `PTP_NETWORK_MODE_HYBRID_NO_FALLBACK`，否则时间发送端连续 `PTP_HYBRID_FALLBACK_ATTEMPTS` 次未响应单播 Delay_Req 后，端口会回退到多播 Delay_Req，并保持多播，直到选择新的时间发送端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PTP_DELAY_MECHANISM_E2E && <choice CONFIG_PTP_NETWORK_MODE>
```

**定义位置（Location）**：[`subsys/net/lib/ptp/Kconfig:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ptp/Kconfig#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → IEEE 1588 精确时间协议（PTP）支持［实验性，Experimental］ → 网络传输模式（Network transmission mode）

**配置项引用（Symbol References）**：[`CONFIG_PTP_DELAY_MECHANISM_E2E`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_DELAY_MECHANISM_E2E)、[`CONFIG_PTP_NETWORK_MODE`](P406_subsys_net_配置项参考_16.md#CONFIG_PTP_NETWORK_MODE)。

<!-- kconfig-navigation -->

[上一章](P405_subsys_net_配置项参考_15.md) · [返回大纲](大纲.md) · [下一章](P407_subsys_net_配置项参考_17.md)
