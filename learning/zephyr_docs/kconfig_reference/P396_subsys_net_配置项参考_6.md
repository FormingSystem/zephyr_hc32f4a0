---
id: learning.zephyr-docs.kconfig-reference.page-396
title: "`subsys/net`配置项参考（6/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第396章\_`subsys/net`配置项参考（6/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_6LO_LOG_LEVEL_DBG"></a>

## 396.1 `CONFIG_NET_6LO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_6LO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 低功耗无线个域网 IPv6 压缩库（6LoWPAN） → 6LoWPAN 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_6LO_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_NET_6LO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_6LO_LOG_LEVEL_DEFAULT"></a>

## 396.2 `CONFIG_NET_6LO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_6LO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 低功耗无线个域网 IPv6 压缩库（6LoWPAN） → 6LoWPAN 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_6LO_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_NET_6LO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_6LO_LOG_LEVEL_ERR"></a>

## 396.3 `CONFIG_NET_6LO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_6LO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 低功耗无线个域网 IPv6 压缩库（6LoWPAN） → 6LoWPAN 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_6LO_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_NET_6LO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_6LO_LOG_LEVEL_INF"></a>

## 396.4 `CONFIG_NET_6LO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_6LO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 低功耗无线个域网 IPv6 压缩库（6LoWPAN） → 6LoWPAN 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_6LO_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_NET_6LO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_6LO_LOG_LEVEL_OFF"></a>

## 396.5 `CONFIG_NET_6LO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_6LO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 低功耗无线个域网 IPv6 压缩库（6LoWPAN） → 6LoWPAN 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_6LO_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_NET_6LO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_6LO_LOG_LEVEL_WRN"></a>

## 396.6 `CONFIG_NET_6LO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_6LO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 低功耗无线个域网 IPv6 压缩库（6LoWPAN） → 6LoWPAN 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_6LO_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_NET_6LO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ALLOW_ANY_PRIORITY"></a>

## 396.7 `CONFIG_NET_ALLOW_ANY_PRIORITY`

**提示（Prompt）**：允许使用任意网络数据包优先级

**说明（Help）**

启用后，可使用用户提供的任意网络数据包优先级（packet priority）；否则限制为 `0–7`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:430`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L430)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ARP"></a>

## 396.8 `CONFIG_NET_ARP`

**提示（Prompt）**：地址解析协议（ARP）

**说明（Help）**

启用地址解析协议（ARP）支持。以太网设备等硬件需要 ARP 才能正常使用 IPv4。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ARP_GRATUITOUS"></a>

## 396.9 `CONFIG_NET_ARP_GRATUITOUS`

**提示（Prompt）**：支持免费 ARP 请求／应答（gratuitous ARP）。

**说明（Help）**

此处“免费（gratuitous）”指 ARP 规范通常不要求、但在某些场景可使用的请求或应答。免费 ARP 请求中，源和目的 IP 都设为发送设备自身 IP，目的 MAC 为广播地址 `ff:ff:ff:ff:ff:ff`，通常不会收到应答。免费 ARP 应答则是在没有对应请求的情况下发出的应答。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ARP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 地址解析协议（ARP）

**配置项引用（Symbol References）**：[`CONFIG_NET_ARP`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ARP_GRATUITOUS_INTERVAL"></a>

## 396.10 `CONFIG_NET_ARP_GRATUITOUS_INTERVAL`

**提示（Prompt）**：发送免费 ARP 请求之间的间隔（秒）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ARP_GRATUITOUS_TRANSMISSION && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 地址解析协议（ARP） → 支持免费 ARP 请求／应答（gratuitous ARP）。 → 发送免费 ARP 请求（gratuitous ARP requests）

**配置项引用（Symbol References）**：[`CONFIG_NET_ARP_GRATUITOUS_TRANSMISSION`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_GRATUITOUS_TRANSMISSION)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ARP_GRATUITOUS_TRANSMISSION"></a>

## 396.11 `CONFIG_NET_ARP_GRATUITOUS_TRANSMISSION`

**提示（Prompt）**：发送免费 ARP 请求（gratuitous ARP requests）

**说明（Help）**

按照 RFC 5227 发送免费 ARP 请求（gratuitous ARP requests）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ARP_GRATUITOUS && CONFIG_NET_MGMT_EVENT && CONFIG_NET_MGMT_EVENT_INFO && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 地址解析协议（ARP） → 支持免费 ARP 请求／应答（gratuitous ARP）。

**配置项引用（Symbol References）**：[`CONFIG_NET_ARP_GRATUITOUS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_GRATUITOUS)、[`CONFIG_NET_MGMT_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NET_MGMT_EVENT_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT_INFO)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ARP_LOG_LEVEL_CHOICE"></a>

## 396.12 `CONFIG_NET_ARP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：IPv4 ARP 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_ARP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_ARP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_ARP_LOG_LEVEL_OFF
CONFIG_NET_ARP_LOG_LEVEL_ERR
CONFIG_NET_ARP_LOG_LEVEL_WRN
CONFIG_NET_ARP_LOG_LEVEL_INF
CONFIG_NET_ARP_LOG_LEVEL_DBG
CONFIG_NET_ARP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 地址解析协议（ARP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_ARP`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_ARP_LOG_LEVEL_DEFAULT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_ARP_LOG_LEVEL_OFF`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_LOG_LEVEL_OFF)、[`CONFIG_NET_ARP_LOG_LEVEL_ERR`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_LOG_LEVEL_ERR)、[`CONFIG_NET_ARP_LOG_LEVEL_WRN`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_LOG_LEVEL_WRN)、[`CONFIG_NET_ARP_LOG_LEVEL_INF`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_LOG_LEVEL_INF)、[`CONFIG_NET_ARP_LOG_LEVEL_DBG`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_ARP_LOG_LEVEL_DBG"></a>

## 396.13 `CONFIG_NET_ARP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ARP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 地址解析协议（ARP） → IPv4 ARP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ARP_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ARP_LOG_LEVEL_DEFAULT"></a>

## 396.14 `CONFIG_NET_ARP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ARP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 地址解析协议（ARP） → IPv4 ARP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ARP_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ARP_LOG_LEVEL_ERR"></a>

## 396.15 `CONFIG_NET_ARP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ARP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 地址解析协议（ARP） → IPv4 ARP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ARP_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ARP_LOG_LEVEL_INF"></a>

## 396.16 `CONFIG_NET_ARP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ARP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 地址解析协议（ARP） → IPv4 ARP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ARP_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ARP_LOG_LEVEL_OFF"></a>

## 396.17 `CONFIG_NET_ARP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ARP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 地址解析协议（ARP） → IPv4 ARP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ARP_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ARP_LOG_LEVEL_WRN"></a>

## 396.18 `CONFIG_NET_ARP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ARP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 地址解析协议（ARP） → IPv4 ARP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ARP_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ARP_TABLE_SIZE"></a>

## 396.19 `CONFIG_NET_ARP_TABLE_SIZE`

**提示（Prompt）**：ARP 表条目数量（entries）。

**说明（Help）**

ARP 表中每个条目消耗 48 字节内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ARP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 地址解析协议（ARP）

**配置项引用（Symbol References）**：[`CONFIG_NET_ARP`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_ARP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_BUF_DATA_SIZE"></a>

## 396.20 `CONFIG_NET_BUF_DATA_SIZE`

**提示（Prompt）**：每个网络数据分片的大小

**说明（Help）**

指定每个网络缓冲区的固定大小（fixed size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_BUF_FIXED_DATA_SIZE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:799`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L799)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_FIXED_DATA_SIZE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_BUF_FIXED_DATA_SIZE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_BUF_FIXED_DATA_SIZE"></a>

## 396.21 `CONFIG_NET_BUF_FIXED_DATA_SIZE`

**提示（Prompt）**：固定数据大小缓冲区（Fixed data size buffer）

**说明（Help）**

每个缓冲区的大小在构建时配置。运行时请求更大空间时，分配足够数量的 `net_buf` 以满足请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_DATA_ALLOC_TYPE>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:785`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L785)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络数据包分配器类型（data allocator type）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_DATA_ALLOC_TYPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_DATA_ALLOC_TYPE)。

<a id="CONFIG_NET_BUF_RX_COUNT"></a>

## 396.22 `CONFIG_NET_BUF_RX_COUNT`

**提示（Prompt）**：为接收数据分配的网络缓冲区数量

**说明（Help）**

每个数据缓冲区占用 `CONFIG_NET_BUF_DATA_SIZE` 加一个较小头部的空间，其中头部大小为 `sizeof(struct net_buf)`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
36 if CONFIG_NET_PKT_LARGE_DEFAULTS
16
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:762`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L762)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_LARGE_DEFAULTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_LARGE_DEFAULTS)。

<a id="CONFIG_NET_BUF_TX_COUNT"></a>

## 396.23 `CONFIG_NET_BUF_TX_COUNT`

**提示（Prompt）**：为发送数据分配的网络缓冲区数量

**说明（Help）**

每个数据缓冲区占用 `CONFIG_NET_BUF_DATA_SIZE` 加一个较小头部的空间，其中头部大小为 `sizeof(struct net_buf)`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
36 if CONFIG_NET_PKT_LARGE_DEFAULTS
16
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:770`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L770)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_LARGE_DEFAULTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_LARGE_DEFAULTS)。

<a id="CONFIG_NET_BUF_VARIABLE_DATA_SIZE"></a>

## 396.24 `CONFIG_NET_BUF_VARIABLE_DATA_SIZE`

**提示（Prompt）**：可变数据大小缓冲区（Variable data size buffer）

**说明（Help）**

根据运行时请求的大小动态分配缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_DATA_ALLOC_TYPE>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:792`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L792)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络数据包分配器类型（data allocator type）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_DATA_ALLOC_TYPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_DATA_ALLOC_TYPE)。

<a id="CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE"></a>

## 396.25 `CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：CAN 总线网络驱动日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NET_CANBUS && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_NET_CANBUS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_CANBUS_LOG_LEVEL_OFF
CONFIG_NET_CANBUS_LOG_LEVEL_ERR
CONFIG_NET_CANBUS_LOG_LEVEL_WRN
CONFIG_NET_CANBUS_LOG_LEVEL_INF
CONFIG_NET_CANBUS_LOG_LEVEL_DBG
CONFIG_NET_CANBUS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 控制器局域网（Controller Area Network，CAN）总线网络驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NET_CANBUS`](P131_drivers_net_配置项参考.md#CONFIG_NET_CANBUS)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)、[`CONFIG_NET_CANBUS_LOG_LEVEL_DEFAULT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CANBUS_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_CANBUS_LOG_LEVEL_OFF`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CANBUS_LOG_LEVEL_OFF)、[`CONFIG_NET_CANBUS_LOG_LEVEL_ERR`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CANBUS_LOG_LEVEL_ERR)、[`CONFIG_NET_CANBUS_LOG_LEVEL_WRN`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CANBUS_LOG_LEVEL_WRN)、[`CONFIG_NET_CANBUS_LOG_LEVEL_INF`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CANBUS_LOG_LEVEL_INF)、[`CONFIG_NET_CANBUS_LOG_LEVEL_DBG`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CANBUS_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_CANBUS_LOG_LEVEL_DBG"></a>

## 396.26 `CONFIG_NET_CANBUS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 控制器局域网（Controller Area Network，CAN）总线网络驱动 → CAN 总线网络驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CANBUS_LOG_LEVEL_DEFAULT"></a>

## 396.27 `CONFIG_NET_CANBUS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 控制器局域网（Controller Area Network，CAN）总线网络驱动 → CAN 总线网络驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CANBUS_LOG_LEVEL_ERR"></a>

## 396.28 `CONFIG_NET_CANBUS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 控制器局域网（Controller Area Network，CAN）总线网络驱动 → CAN 总线网络驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CANBUS_LOG_LEVEL_INF"></a>

## 396.29 `CONFIG_NET_CANBUS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 控制器局域网（Controller Area Network，CAN）总线网络驱动 → CAN 总线网络驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CANBUS_LOG_LEVEL_OFF"></a>

## 396.30 `CONFIG_NET_CANBUS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 控制器局域网（Controller Area Network，CAN）总线网络驱动 → CAN 总线网络驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CANBUS_LOG_LEVEL_WRN"></a>

## 396.31 `CONFIG_NET_CANBUS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 控制器局域网（Controller Area Network，CAN）总线网络驱动 → CAN 总线网络驱动日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CANBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CAPTURE"></a>

## 396.32 `CONFIG_NET_CAPTURE`

**提示（Prompt）**：网络数据包捕获支持（Network packet capture）

**说明（Help）**

允许用户捕获网络数据包，并发送到另一主机处理。可使用 Wireshark 等网络数据包分析器。捕获的数据包通过 IP-in-IP（IPIP）隧道，以 UDP 数据报载荷的形式发送。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_VIRTUAL
CONFIG_NET_L2_VIRTUAL_MGMT
CONFIG_NET_L2_IPIP
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
CONFIG_NET_CONTEXT_NET_PKT_POOL
```

**定义位置（Location）**：[`subsys/net/lib/capture/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/capture/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_VIRTUAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_VIRTUAL)、[`CONFIG_NET_L2_VIRTUAL_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_VIRTUAL_MGMT)、[`CONFIG_NET_L2_IPIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IPIP)、[`CONFIG_NET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NET_CONTEXT_NET_PKT_POOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONTEXT_NET_PKT_POOL)。

<a id="CONFIG_NET_CAPTURE_BUF_COUNT"></a>

## 396.33 `CONFIG_NET_CAPTURE_BUF_COUNT`

**提示（Prompt）**：为捕获分配的网络缓冲区数量

**说明（Help）**

指定为捕获网络流量分配的 `net_buf` 数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CAPTURE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/net/lib/capture/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/capture/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture）

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CAPTURE_COOKED_MODE"></a>

## 396.34 `CONFIG_NET_CAPTURE_COOKED_MODE`

**提示（Prompt）**：捕获非 IP 数据包，熟化捕获模式（cooked/SLL）【实验性 EXPERIMENTAL】

**说明（Help）**

允许应用以 Linux 熟化捕获模式（Linux cooked mode，SLL）捕获数据包，使用合成链路层头部（synthetic link layer header）替代真实网络链路头部。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CAPTURE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_PSEUDO_IFACE
CONFIG_NET_L2_DUMMY
CONFIG_NET_L2_VIRTUAL
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/capture/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/capture/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture）

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PSEUDO_IFACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PSEUDO_IFACE)、[`CONFIG_NET_L2_DUMMY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_DUMMY)、[`CONFIG_NET_L2_VIRTUAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_VIRTUAL)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_NET_CAPTURE_COOKED_MODE_INTERFACE_NAME"></a>

## 396.35 `CONFIG_NET_CAPTURE_COOKED_MODE_INTERFACE_NAME`

**提示（Prompt）**：熟化捕获模式网络接口名称（cooked mode）

**说明（Help）**

设置熟化捕获模式（cooked mode）的捕获网络接口名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CAPTURE_COOKED_MODE && CONFIG_NET_CAPTURE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"cooked"
```

**定义位置（Location）**：[`subsys/net/lib/capture/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/capture/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture） → 捕获非 IP 数据包，熟化捕获模式（cooked/SLL）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_COOKED_MODE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_COOKED_MODE)、[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CAPTURE_COOKED_MODE_MAX_LINK_TYPES"></a>

## 396.36 `CONFIG_NET_CAPTURE_COOKED_MODE_MAX_LINK_TYPES`

**提示（Prompt）**：可同时捕获的链路类型数量（ETH_P_*）

**说明（Help）**

定义熟化捕获模式下，可同时捕获的 `ETH_P_*` 链路类型值数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CAPTURE_COOKED_MODE && CONFIG_NET_CAPTURE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/net/lib/capture/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/capture/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture） → 捕获非 IP 数据包，熟化捕获模式（cooked/SLL）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_COOKED_MODE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_COOKED_MODE)、[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CAPTURE_COOKED_MODE_SLLV1"></a>

## 396.37 `CONFIG_NET_CAPTURE_COOKED_MODE_SLLV1`

**提示（Prompt）**：SLL 版本 1

**说明（Help）**

使用 SLL 版本 1，头部大小为 16 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CAPTURE_COOKED_MODE && <choice CONFIG_NET_CAPTURE_COOKED_MODE_SLL_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/capture/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/capture/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture） → 捕获非 IP 数据包，熟化捕获模式（cooked/SLL）【实验性 EXPERIMENTAL】 → 使用的 SLL 版本

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_COOKED_MODE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_COOKED_MODE)、[`CONFIG_NET_CAPTURE_COOKED_MODE_SLL_VERSION`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_COOKED_MODE_SLL_VERSION)。

<a id="CONFIG_NET_CAPTURE_COOKED_MODE_SLLV2"></a>

## 396.38 `CONFIG_NET_CAPTURE_COOKED_MODE_SLLV2`

**提示（Prompt）**：SLL 版本 2

**说明（Help）**

使用 SLL 版本 2，头部大小为 20 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CAPTURE_COOKED_MODE && <choice CONFIG_NET_CAPTURE_COOKED_MODE_SLL_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/capture/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/capture/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture） → 捕获非 IP 数据包，熟化捕获模式（cooked/SLL）【实验性 EXPERIMENTAL】 → 使用的 SLL 版本

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_COOKED_MODE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_COOKED_MODE)、[`CONFIG_NET_CAPTURE_COOKED_MODE_SLL_VERSION`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_COOKED_MODE_SLL_VERSION)。

<a id="CONFIG_NET_CAPTURE_COOKED_MODE_SLL_VERSION"></a>

## 396.39 `CONFIG_NET_CAPTURE_COOKED_MODE_SLL_VERSION`

**提示（Prompt）**：使用的 SLL 版本

**说明（Help）**

指定使用的 SLL 头部版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CAPTURE_COOKED_MODE && CONFIG_NET_CAPTURE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_CAPTURE_COOKED_MODE_SLLV1
```

**可选项（Choices）**

```text
CONFIG_NET_CAPTURE_COOKED_MODE_SLLV1
CONFIG_NET_CAPTURE_COOKED_MODE_SLLV2
```

**定义位置（Location）**：[`subsys/net/lib/capture/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/capture/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture） → 捕获非 IP 数据包，熟化捕获模式（cooked/SLL）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_COOKED_MODE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_COOKED_MODE)、[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CAPTURE_COOKED_MODE_SLLV1`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_COOKED_MODE_SLLV1)、[`CONFIG_NET_CAPTURE_COOKED_MODE_SLLV2`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_COOKED_MODE_SLLV2)。

<a id="CONFIG_NET_CAPTURE_DEVICE_COUNT"></a>

## 396.40 `CONFIG_NET_CAPTURE_DEVICE_COUNT`

**提示（Prompt）**：网络捕获设备数量（capture devices）

**说明（Help）**

网络捕获设备数量。通常一个足够；若需将捕获数据发送到多个不同设备，应增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CAPTURE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/capture/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/capture/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture）

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE"></a>

## 396.41 `CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：网络捕获 API 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_CAPTURE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_CAPTURE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_CAPTURE_LOG_LEVEL_OFF
CONFIG_NET_CAPTURE_LOG_LEVEL_ERR
CONFIG_NET_CAPTURE_LOG_LEVEL_WRN
CONFIG_NET_CAPTURE_LOG_LEVEL_INF
CONFIG_NET_CAPTURE_LOG_LEVEL_DBG
CONFIG_NET_CAPTURE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CAPTURE_LOG_LEVEL_DEFAULT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_CAPTURE_LOG_LEVEL_OFF`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_OFF)、[`CONFIG_NET_CAPTURE_LOG_LEVEL_ERR`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_ERR)、[`CONFIG_NET_CAPTURE_LOG_LEVEL_WRN`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_WRN)、[`CONFIG_NET_CAPTURE_LOG_LEVEL_INF`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_INF)、[`CONFIG_NET_CAPTURE_LOG_LEVEL_DBG`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_CAPTURE_LOG_LEVEL_DBG"></a>

## 396.42 `CONFIG_NET_CAPTURE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture） → 网络捕获 API 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CAPTURE_LOG_LEVEL_DEFAULT"></a>

## 396.43 `CONFIG_NET_CAPTURE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture） → 网络捕获 API 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CAPTURE_LOG_LEVEL_ERR"></a>

## 396.44 `CONFIG_NET_CAPTURE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture） → 网络捕获 API 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CAPTURE_LOG_LEVEL_INF"></a>

## 396.45 `CONFIG_NET_CAPTURE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture） → 网络捕获 API 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CAPTURE_LOG_LEVEL_OFF"></a>

## 396.46 `CONFIG_NET_CAPTURE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture） → 网络捕获 API 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CAPTURE_LOG_LEVEL_WRN"></a>

## 396.47 `CONFIG_NET_CAPTURE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture） → 网络捕获 API 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CAPTURE_PKT_COUNT"></a>

## 396.48 `CONFIG_NET_CAPTURE_PKT_COUNT`

**提示（Prompt）**：为捕获分配的网络数据包数量

**说明（Help）**

指定捕获网络流量时分配的 `net_pkt` 数量。每个收发网络帧都会分配一个 `net_pkt` 保存网络元数据；每个 `net_pkt` 包含一个 `net_buf` 列表，保存实际网络数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CAPTURE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/capture/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/capture/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture）

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CAPTURE_TX_DEBUG"></a>

## 396.49 `CONFIG_NET_CAPTURE_TX_DEBUG`

**提示（Prompt）**：调试已发送数据包（Debug sent packets）

**说明（Help）**

启用已发送网络数据包的打印。输出可能很多，因此默认禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CAPTURE_LOG_LEVEL_DBG && CONFIG_NET_CAPTURE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/capture/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/capture/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 网络数据包捕获支持（Network packet capture）

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_LOG_LEVEL_DBG`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE_LOG_LEVEL_DBG)、[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CHECKSUM_OFFLOAD"></a>

## 396.50 `CONFIG_NET_CHECKSUM_OFFLOAD`

**提示（Prompt）**：校验和卸载（Checksum offload）

**说明（Help）**

驱动支持时，将校验和检查和计算（checksum checking/calculation）卸载给硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED"></a>

## 396.51 `CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

应由支持校验和卸载（checksum offloading）的驱动选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_ETH_CYCLONEV
CONFIG_ETH_MCHP_GMAC_G1
CONFIG_ETH_NXP_ENET
CONFIG_ETH_NXP_S32_GMAC
CONFIG_ETH_NXP_S32_NETC
CONFIG_ETH_STM32_HAL
CONFIG_ETH_XILINX_AXIENET
CONFIG_ETH_XLNX_GEM
CONFIG_ETH_XMC4XXX
CONFIG_ETH_DWC_ETHER_TX_HW_CHECKSUM
CONFIG_ETH_DWC_ETHER_RX_HW_CHECKSUM
CONFIG_ETH_DWC_XGMAC
CONFIG_ETH_NXP_ENET_QOS
CONFIG_ETH_NXP_IMX_NETC
CONFIG_WIFI_NRF70
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_ETH_CYCLONEV`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_CYCLONEV)、[`CONFIG_ETH_MCHP_GMAC_G1`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_MCHP_GMAC_G1)、[`CONFIG_ETH_NXP_ENET`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET)、[`CONFIG_ETH_NXP_S32_GMAC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_GMAC)、[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ETH_XILINX_AXIENET`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XILINX_AXIENET)、[`CONFIG_ETH_XLNX_GEM`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XLNX_GEM)、[`CONFIG_ETH_XMC4XXX`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_XMC4XXX)、[`CONFIG_ETH_DWC_ETHER_TX_HW_CHECKSUM`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_TX_HW_CHECKSUM)、[`CONFIG_ETH_DWC_ETHER_RX_HW_CHECKSUM`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_RX_HW_CHECKSUM)、[`CONFIG_ETH_DWC_XGMAC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_XGMAC)、[`CONFIG_ETH_NXP_ENET_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS)、[`CONFIG_ETH_NXP_IMX_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_IMX_NETC)、[`CONFIG_WIFI_NRF70`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NRF70)。

<a id="CONFIG_NET_CONFIG_AUTO_INIT"></a>

## 396.52 `CONFIG_NET_CONFIG_AUTO_INIT`

**提示（Prompt）**：设备启动时自动初始化网络支持

**说明（Help）**

启用后，设备启动时自动初始化网络系统。若不需要自动初始化，则禁用，并由应用调用 `net_config_init()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if !(CONFIG_USB_DEVICE_NETWORK || CONFIG_USBD_CDC_ECM_CLASS || CONFIG_USBD_CDC_NCM_CLASS)
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_USB_DEVICE_NETWORK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_NETWORK)、[`CONFIG_USBD_CDC_ECM_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_CDC_ECM_CLASS)、[`CONFIG_USBD_CDC_NCM_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_CDC_NCM_CLASS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USB_DEVICE_NETWORK`。

<a id="CONFIG_NET_CONFIG_CLOCK_SNTP_INIT"></a>

## 396.53 `CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`

**提示（Prompt）**：应用启动时通过 SNTP 初始化系统时钟

**说明（Help）**

通过网络发送简单网络时间协议（SNTP）请求，获取绝对挂钟时间（wall clock time）并初始化系统时间，使 `sys_clock_gettime(SYS_CLOCK_REALTIME, ...)`、`time()`、`gettimeofday()` 等返回正确的绝对时间，而非仅返回启动以来的时间。需要网络支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SNTP && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries）

**配置项引用（Symbol References）**：[`CONFIG_SNTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SNTP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_CLOCK_SNTP_SET_RTC"></a>

## 396.54 `CONFIG_NET_CONFIG_CLOCK_SNTP_SET_RTC`

**提示（Prompt）**：收到 SNTP 响应后设置实时时钟（RTC）

**说明（Help）**

收到 SNTP 响应时设置实时时钟（RTC），要求设备树提供 `zephyr,rtc` chosen 配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 应用启动时通过 SNTP 初始化系统时钟

<a id="CONFIG_NET_CONFIG_DHCPV6_REQUEST_ADDR"></a>

## 396.55 `CONFIG_NET_CONFIG_DHCPV6_REQUEST_ADDR`

**提示（Prompt）**：配置 DHCPv6 客户端时请求 IPv6 地址

**说明（Help）**

启用 DHCPv6 时，配置客户端向 DHCPv6 服务器请求 IPv6 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV6 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L191)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV6)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_DHCPV6_REQUEST_PREFIX"></a>

## 396.56 `CONFIG_NET_CONFIG_DHCPV6_REQUEST_PREFIX`

**提示（Prompt）**：配置 DHCPv6 客户端时请求 IPv6 前缀

**说明（Help）**

启用 DHCPv6 时，配置客户端向 DHCPv6 服务器请求 IPv6 前缀（prefix）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV6 && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV6)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_IEEE802154_ACK_REQUIRED"></a>

## 396.57 `CONFIG_NET_CONFIG_IEEE802154_ACK_REQUIRED`

**提示（Prompt）**：IEEE 802.15.4 确认（acknowledgment）

**说明（Help）**

是否请求并要求收到 IEEE 802.15.4 确认数据包（acknowledgment packets）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_L2_IEEE802154 || CONFIG_IEEE802154_RAW_MODE) && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154)、[`CONFIG_IEEE802154_RAW_MODE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_RAW_MODE)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_IEEE802154_CHANNEL"></a>

## 396.58 `CONFIG_NET_CONFIG_IEEE802154_CHANNEL`

**提示（Prompt）**：IEEE 802.15.4 信道（channel）

**说明（Help）**

示例应用默认使用的信道。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_L2_IEEE802154 || CONFIG_IEEE802154_RAW_MODE) && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
26
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154)、[`CONFIG_IEEE802154_RAW_MODE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_RAW_MODE)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_IEEE802154_PAN_ID"></a>

## 396.59 `CONFIG_NET_CONFIG_IEEE802154_PAN_ID`

**提示（Prompt）**：IEEE 802.15.4 个域网标识（PAN ID）

**说明（Help）**

示例默认使用的个域网标识（PAN ID）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_L2_IEEE802154 || CONFIG_IEEE802154_RAW_MODE) && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0xabcd
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154)、[`CONFIG_IEEE802154_RAW_MODE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_RAW_MODE)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_IEEE802154_RADIO_TX_POWER"></a>

## 396.60 `CONFIG_NET_CONFIG_IEEE802154_RADIO_TX_POWER`

**提示（Prompt）**：IEEE 802.15.4 发射功率（TX power，dBm）

**说明（Help）**

示例应用默认使用的发射功率。详情参见 `NET_L2_IEEE802154_RADIO_DFLT_TX_POWER`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_L2_IEEE802154 || CONFIG_IEEE802154_RAW_MODE) && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154)、[`CONFIG_IEEE802154_RAW_MODE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_RAW_MODE)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_IEEE802154_SECURITY_KEY"></a>

## 396.61 `CONFIG_NET_CONFIG_IEEE802154_SECURITY_KEY`

**提示（Prompt）**：IEEE 802.15.4 安全密钥（security key）

**说明（Help）**

链路层安全（link-layer security）使用的密钥字符串。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154_SECURITY && (CONFIG_NET_L2_IEEE802154 || CONFIG_IEEE802154_RAW_MODE) && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"moooh!"
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_SECURITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_SECURITY)、[`CONFIG_NET_L2_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154)、[`CONFIG_IEEE802154_RAW_MODE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_RAW_MODE)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_IEEE802154_SECURITY_KEY_MODE"></a>

## 396.62 `CONFIG_NET_CONFIG_IEEE802154_SECURITY_KEY_MODE`

**提示（Prompt）**：IEEE 802.15.4 安全密钥模式（key mode）

**说明（Help）**

链路层安全使用的密钥模式。仅支持隐式模式（implicit mode），因此为 `0`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154_SECURITY && (CONFIG_NET_L2_IEEE802154 || CONFIG_IEEE802154_RAW_MODE) && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0]
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_SECURITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_SECURITY)、[`CONFIG_NET_L2_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154)、[`CONFIG_IEEE802154_RAW_MODE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_RAW_MODE)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_IEEE802154_SECURITY_LEVEL"></a>

## 396.63 `CONFIG_NET_CONFIG_IEEE802154_SECURITY_LEVEL`

**提示（Prompt）**：IEEE 802.15.4 安全级别（security level，0–7）

**说明（Help）**

链路层安全使用的级别：

| 值 | 含义 |
| --- | --- |
| 0 | 无安全保护（no security） |
| 1 | 仅认证（authentication），4 字节标签 |
| 2 | 仅认证，8 字节标签 |
| 3 | 仅认证，16 字节标签 |
| 4 | 自 IEEE 802.15.4-2015 起弃用（deprecated） |
| 5 | 加密与认证（encryption/authentication），4 字节标签 |
| 6 | 加密与认证，8 字节标签 |
| 7 | 加密与认证，16 字节标签 |

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154_SECURITY && (CONFIG_NET_L2_IEEE802154 || CONFIG_IEEE802154_RAW_MODE) && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_SECURITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_SECURITY)、[`CONFIG_NET_L2_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154)、[`CONFIG_IEEE802154_RAW_MODE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_RAW_MODE)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_INIT_PRIO"></a>

## 396.64 `CONFIG_NET_CONFIG_INIT_PRIO`

**提示（Prompt）**：网络应用初始化的启动优先级

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONFIG_AUTO_INIT && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
95
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings） → 设备启动时自动初始化网络支持

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_AUTO_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_AUTO_INIT)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_INIT_TIMEOUT"></a>

## 396.65 `CONFIG_NET_CONFIG_INIT_TIMEOUT`

**提示（Prompt）**：等待网络就绪且可用的最长时间

**说明（Help）**

单位为秒。例如，若未在此期限内通过 DHCPv4 获取 IPv4 地址，则设备启动时的 `net_config_init()` 调用失败。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE"></a>

## 396.66 `CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE`

**提示（Prompt）**：网络配置库日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_CONFIG_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_CONFIG_LOG_LEVEL_OFF
CONFIG_NET_CONFIG_LOG_LEVEL_ERR
CONFIG_NET_CONFIG_LOG_LEVEL_WRN
CONFIG_NET_CONFIG_LOG_LEVEL_INF
CONFIG_NET_CONFIG_LOG_LEVEL_DBG
CONFIG_NET_CONFIG_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CONFIG_LOG_LEVEL_DEFAULT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_CONFIG_LOG_LEVEL_OFF`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_LOG_LEVEL_OFF)、[`CONFIG_NET_CONFIG_LOG_LEVEL_ERR`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_LOG_LEVEL_ERR)、[`CONFIG_NET_CONFIG_LOG_LEVEL_WRN`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_LOG_LEVEL_WRN)、[`CONFIG_NET_CONFIG_LOG_LEVEL_INF`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_LOG_LEVEL_INF)、[`CONFIG_NET_CONFIG_LOG_LEVEL_DBG`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_CONFIG_LOG_LEVEL_DBG"></a>

## 396.67 `CONFIG_NET_CONFIG_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络配置库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONFIG_LOG_LEVEL_DEFAULT"></a>

## 396.68 `CONFIG_NET_CONFIG_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络配置库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONFIG_LOG_LEVEL_ERR"></a>

## 396.69 `CONFIG_NET_CONFIG_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络配置库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONFIG_LOG_LEVEL_INF"></a>

## 396.70 `CONFIG_NET_CONFIG_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络配置库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONFIG_LOG_LEVEL_OFF"></a>

## 396.71 `CONFIG_NET_CONFIG_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络配置库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONFIG_LOG_LEVEL_WRN"></a>

## 396.72 `CONFIG_NET_CONFIG_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络配置库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONFIG_MY_IPV4_ADDR"></a>

## 396.73 `CONFIG_NET_CONFIG_MY_IPV4_ADDR`

**提示（Prompt）**：本机 IPv4 地址（My IPv4 address）

**说明（Help）**

不确定时，在此使用 `192.0.2.1`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_MY_IPV4_GW"></a>

## 396.74 `CONFIG_NET_CONFIG_MY_IPV4_GW`

**提示（Prompt）**：本机 IPv4 网关（gateway）

**说明（Help）**

未被 DHCP 覆盖时使用的静态网关（static gateway）。设为空值可跳过静态设置。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_MY_IPV4_NETMASK"></a>

## 396.75 `CONFIG_NET_CONFIG_MY_IPV4_NETMASK`

**提示（Prompt）**：本机 IPv4 子网掩码（netmask）

**说明（Help）**

未被 DHCP 覆盖时使用的静态子网掩码。设为空值可跳过静态设置。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"255.255.255.0"
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_MY_IPV6_ADDR"></a>

## 396.76 `CONFIG_NET_CONFIG_MY_IPV6_ADDR`

**提示（Prompt）**：本机 IPv6 地址（My IPv6 address）

**说明（Help）**

不确定时，在此使用 `2001:db8::1`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_MY_VLAN_ID"></a>

## 396.77 `CONFIG_NET_CONFIG_MY_VLAN_ID`

**提示（Prompt）**：本机虚拟局域网标识（VLAN identifier）

**说明（Help）**

不确定时，在此使用 `0`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_VLAN && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_VLAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_VLAN)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_NEED_IPV4"></a>

## 396.78 `CONFIG_NET_CONFIG_NEED_IPV4`

**提示（Prompt）**：此应用需要 IPv4 支持

**说明（Help）**

网络应用需要 IPv4 才能正常工作。本项确保正确初始化应用，以便使用 IPv4。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONFIG_AUTO_INIT && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_IPV4
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings） → 设备启动时自动初始化网络支持

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_AUTO_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_AUTO_INIT)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)。

<a id="CONFIG_NET_CONFIG_NEED_IPV6"></a>

## 396.79 `CONFIG_NET_CONFIG_NEED_IPV6`

**提示（Prompt）**：此应用需要 IPv6 支持

**说明（Help）**

网络应用需要 IPv6 才能正常工作。本项确保正确初始化应用，以便使用 IPv6。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONFIG_AUTO_INIT && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_IPV6
```

**被弱选择（Implied by）**

```text
CONFIG_NET_L2_OPENTHREAD
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings） → 设备启动时自动初始化网络支持

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_AUTO_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_AUTO_INIT)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)。

<a id="CONFIG_NET_CONFIG_NEED_IPV6_ROUTER"></a>

## 396.80 `CONFIG_NET_CONFIG_NEED_IPV6_ROUTER`

**提示（Prompt）**：此应用要求存在 IPv6 路由器

**说明（Help）**

应用必须确认存在 IPv6 路由器后才继续，即等待收到 IPv6 路由器通告（Router Advertisement）消息后再继续。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && CONFIG_NET_CONFIG_AUTO_INIT && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings） → 设备启动时自动初始化网络支持

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_CONFIG_AUTO_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_AUTO_INIT)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_PEER_IPV4_ADDR"></a>

## 396.81 `CONFIG_NET_CONFIG_PEER_IPV4_ADDR`

**提示（Prompt）**：对端 IPv4 地址（Peer address）

**说明（Help）**

仅适用于尝试与对端主机建立连接的客户端应用。不确定时，在此使用 `192.0.2.2`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_PEER_IPV6_ADDR"></a>

## 396.82 `CONFIG_NET_CONFIG_PEER_IPV6_ADDR`

**提示（Prompt）**：对端 IPv6 地址（Peer address）

**说明（Help）**

仅适用于尝试与对端主机建立连接的客户端应用。不确定时，在此使用 `2001:db8::2`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && CONFIG_NET_CONFIG_SETTINGS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 设置应用的网络配置（network settings）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_SETTINGS"></a>

## 396.83 `CONFIG_NET_CONFIG_SETTINGS`

**提示（Prompt）**：设置应用的网络配置（network settings）

**说明（Help）**

允许在网络客户端／服务器示例应用的配置文件中设置 IP 地址，以及信道等链路层专用参数。注意：此功能用于快速试用或测试，不适合作为正式部署配置（provisioning）机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT)。

<a id="CONFIG_NET_CONFIG_SNTP_INIT_RESYNC"></a>

## 396.84 `CONFIG_NET_CONFIG_SNTP_INIT_RESYNC`

**提示（Prompt）**：定期通过 SNTP 重新同步系统时钟

**说明（Help）**

定期通过网络发送 SNTP 请求，获取绝对挂钟时间（wall clock time），并据此重新同步系统时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SERVICE && CONFIG_NET_CONFIG_CLOCK_SNTP_INIT && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:266`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L266)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 应用启动时通过 SNTP 初始化系统时钟

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SERVICE)、[`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_SNTP_INIT_RESYNC_INTERVAL"></a>

## 396.85 `CONFIG_NET_CONFIG_SNTP_INIT_RESYNC_INTERVAL`

**提示（Prompt）**：SNTP 重新同步间隔（秒）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONFIG_SNTP_INIT_RESYNC && CONFIG_NET_CONFIG_CLOCK_SNTP_INIT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3600
```

**取值范围（Ranges）**

```text
[15, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:275`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L275)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 应用启动时通过 SNTP 初始化系统时钟 → 定期通过 SNTP 重新同步系统时钟

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_SNTP_INIT_RESYNC`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SNTP_INIT_RESYNC)、[`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_SNTP_INIT_RESYNC_ON_FAILURE_INTERVAL"></a>

## 396.86 `CONFIG_NET_CONFIG_SNTP_INIT_RESYNC_ON_FAILURE_INTERVAL`

**提示（Prompt）**：失败后的 SNTP 重新同步间隔（秒）

**说明（Help）**

SNTP 请求失败时，在再次尝试之前等待此时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONFIG_SNTP_INIT_RESYNC && CONFIG_NET_CONFIG_CLOCK_SNTP_INIT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_CONFIG_SNTP_INIT_RESYNC_INTERVAL
```

**取值范围（Ranges）**

```text
[15, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L280)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 应用启动时通过 SNTP 初始化系统时钟 → 定期通过 SNTP 重新同步系统时钟

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_SNTP_INIT_RESYNC`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SNTP_INIT_RESYNC)、[`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CONFIG_SNTP_INIT_RESYNC_INTERVAL`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SNTP_INIT_RESYNC_INTERVAL)。

<a id="CONFIG_NET_CONFIG_SNTP_INIT_SERVER"></a>

## 396.87 `CONFIG_NET_CONFIG_SNTP_INIT_SERVER`

**提示（Prompt）**：初始化系统时钟使用的 SNTP 服务器

**说明（Help）**

Zephyr 不为此选项提供默认值。各应用和厂商应根据所在地区、需求及服务器服务条款选择合适的设置。服务器信息示例参见 [NTP Pool Servers](https://support.ntp.org/bin/view/Servers/NTPPoolServers)。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONFIG_CLOCK_SNTP_INIT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 应用启动时通过 SNTP 初始化系统时钟

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_SNTP_INIT_SERVER_MAX_LEN"></a>

## 396.88 `CONFIG_NET_CONFIG_SNTP_INIT_SERVER_MAX_LEN`

**提示（Prompt）**：运行时设置的 SNTP 服务器名称最大长度

**说明（Help）**

`net_config_sntp_set_server()` 接受的服务器名称最大长度，不含末尾空字符（NUL）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONFIG_SNTP_INIT_SERVER_RUNTIME && CONFIG_NET_CONFIG_CLOCK_SNTP_INIT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
63
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 应用启动时通过 SNTP 初始化系统时钟 → 允许运行时设置初始化系统时钟的 SNTP 服务器

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_SNTP_INIT_SERVER_RUNTIME`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SNTP_INIT_SERVER_RUNTIME)、[`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_SNTP_INIT_SERVER_RUNTIME"></a>

## 396.89 `CONFIG_NET_CONFIG_SNTP_INIT_SERVER_RUNTIME`

**提示（Prompt）**：允许运行时设置初始化系统时钟的 SNTP 服务器

**说明（Help）**

启用后，应用可通过 `net_config_sntp_set_server()` 在运行时选择 SNTP 服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONFIG_CLOCK_SNTP_INIT && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L247)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 应用启动时通过 SNTP 初始化系统时钟

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_SNTP_INIT_SERVER_USE_DHCPV4_OPTION"></a>

## 396.90 `CONFIG_NET_CONFIG_SNTP_INIT_SERVER_USE_DHCPV4_OPTION`

**提示（Prompt）**：通过 DHCPv4 选项设置初始化系统时钟的 SNTP 服务器

**说明（Help）**

启用后，可通过 DHCPv4 选项设置用于初始化系统时钟的 SNTP 服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_OPTION_NTP_SERVER && CONFIG_NET_CONFIG_CLOCK_SNTP_INIT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 应用启动时通过 SNTP 初始化系统时钟

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_OPTION_NTP_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4_OPTION_NTP_SERVER)、[`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_SNTP_INIT_TIMEOUT"></a>

## 396.91 `CONFIG_NET_CONFIG_SNTP_INIT_TIMEOUT`

**提示（Prompt）**：SNTP 初始化系统时钟的超时（毫秒）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONFIG_CLOCK_SNTP_INIT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3000
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 应用启动时通过 SNTP 初始化系统时钟

**配置项引用（Symbol References）**：[`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONFIG_SNTP_INIT_USE_CONNECTION_MANAGER"></a>

## 396.92 `CONFIG_NET_CONFIG_SNTP_INIT_USE_CONNECTION_MANAGER`

**提示（Prompt）**：使用连接管理器启停 SNTP 客户端

**说明（Help）**

启用后，由连接管理器（connection manager）启动和停止 SNTP 客户端。每次网络连接建立时，也会发送 SNTP 请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONNECTION_MANAGER && CONFIG_NET_CONFIG_SNTP_INIT_RESYNC && CONFIG_NET_CONFIG_CLOCK_SNTP_INIT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/config/Kconfig:288`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/config/Kconfig#L288)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 应用启动时通过 SNTP 初始化系统时钟 → 定期通过 SNTP 重新同步系统时钟

**配置项引用（Symbol References）**：[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)、[`CONFIG_NET_CONFIG_SNTP_INIT_RESYNC`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SNTP_INIT_RESYNC)、[`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONNECTION_MANAGER"></a>

## 396.93 `CONFIG_NET_CONNECTION_MANAGER`

**提示（Prompt）**：网络连接管理器（Network connection manager）

**说明（Help）**

启用后，启动连接管理器（connection manager），监听网络接口和 IP 事件，以判断接口是否已连接，并据此发出传输层（L4）的“已连接（connected）”或“已断开（disconnected）”事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_IPV6 || CONFIG_NET_IPV4) && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
CONFIG_NET_MGMT_EVENT_INFO
```

**被选择（Selected by）**

```text
CONFIG_MCUMGR_TRANSPORT_UDP
CONFIG_MDNS_RESPONDER_PROBE
CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED
CONFIG_SHELL_BACKEND_MQTT
```

**定义位置（Location）**：[`subsys/net/conn_mgr/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/conn_mgr/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NET_MGMT_EVENT_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT_INFO)、[`CONFIG_MCUMGR_TRANSPORT_UDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP)、[`CONFIG_MDNS_RESPONDER_PROBE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_PROBE)、[`CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SHELL_HTTP_CLIENT_SUPPORTED)、[`CONFIG_SHELL_BACKEND_MQTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_MQTT)。

<a id="CONFIG_NET_CONNECTION_MANAGER_AUTO_IF_DOWN"></a>

## 396.94 `CONFIG_NET_CONNECTION_MANAGER_AUTO_IF_DOWN`

**提示（Prompt）**：对放弃连接的接口自动调用 net_if_down

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CONNECTION_MANAGER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/conn_mgr/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/conn_mgr/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONNECTION_MANAGER_CONNECTIVITY_WIFI_MGMT"></a>

## 396.95 `CONFIG_NET_CONNECTION_MANAGER_CONNECTIVITY_WIFI_MGMT`

**提示（Prompt）**：通用 Wi-Fi 管理连接实现（connectivity implementation）

**说明（Help）**

在 Wi-Fi 驱动上启用 `CONNECTIVITY_WIFI_MGMT` 连接绑定（connectivity bindings）。编译哪一种实现，由 `CONNECTIVITY_WIFI_MGMT_IMPL` 控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NET_CONNECTION_MANAGER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/conn_mgr/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/conn_mgr/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE"></a>

## 396.96 `CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：连接管理器日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_CONNECTION_MANAGER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_OFF
CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_ERR
CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_WRN
CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_INF
CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_DBG
CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_DEFAULT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_OFF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_OFF)、[`CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_ERR`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_ERR)、[`CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_WRN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_WRN)、[`CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_INF`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_INF)、[`CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_DBG`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_DBG"></a>

## 396.97 `CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager） → 连接管理器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_DEFAULT"></a>

## 396.98 `CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager） → 连接管理器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_ERR"></a>

## 396.99 `CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager） → 连接管理器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_INF"></a>

## 396.100 `CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络连接管理器（Network connection manager） → 连接管理器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P395_subsys_net_配置项参考_5.md) · [返回大纲](大纲.md) · [下一章](P397_subsys_net_配置项参考_7.md)
